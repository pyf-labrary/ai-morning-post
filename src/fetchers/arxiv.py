"""arXiv API fetcher。"""
from __future__ import annotations

import time
import httpx
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET

from ..common import Item

ARXIV_ENDPOINTS = [
    "https://export.arxiv.org/api/query",
    "http://export.arxiv.org/api/query",
]
NS = {"atom": "http://www.w3.org/2005/Atom", "opensearch": "http://a9.com/-/spec/opensearch/1.1/"}
HEADERS = {
    "User-Agent": "ai-morning-post/1.0 (+https://github.com/pyf-labrary/ai-morning-post)",
    "Accept": "application/atom+xml,application/xml;q=0.9,*/*;q=0.8",
}


def _query(endpoint: str, params: dict) -> httpx.Response:
    return httpx.get(endpoint, params=params, headers=HEADERS, timeout=30, follow_redirects=True)


def _parse(xml_text: str, cutoff: datetime, cat: str,
           until: datetime | None = None) -> tuple[list[Item], int, int]:
    """returns (items, total_results, raw_entries)"""
    root = ET.fromstring(xml_text)
    total = int((root.findtext("opensearch:totalResults", default="0", namespaces=NS) or "0"))
    entries = root.findall("atom:entry", NS)
    out: list[Item] = []
    for entry in entries:
        pub = entry.findtext("atom:published", default="", namespaces=NS)
        upd = entry.findtext("atom:updated", default="", namespaces=NS) or pub
        try:
            dt = datetime.fromisoformat((upd or pub).replace("Z", "+00:00"))
            if dt < cutoff or (until and dt > until):
                continue
        except ValueError:
            continue
        title = (entry.findtext("atom:title", default="", namespaces=NS) or "").strip().replace("\n", " ")
        link = entry.findtext("atom:id", default="", namespaces=NS) or ""
        summary = (entry.findtext("atom:summary", default="", namespaces=NS) or "").strip()[:600]
        authors = [a.findtext("atom:name", default="", namespaces=NS)
                   for a in entry.findall("atom:author", NS)]
        out.append(Item(
            source=f"arxiv:{cat}",
            source_type="arxiv",
            title=title,
            url=link,
            summary=summary,
            published=pub,
            author=", ".join(authors[:3]),
            weight=6,
        ))
    return out, total, len(entries)


def _fetch_category(cat: str, max_per_category: int, cutoff: datetime,
                    until: datetime | None = None) -> list[Item]:
    # 回溯补录：用 submittedDate 区间把查询限死在当时的窗口内，否则按
    # lastUpdatedDate 降序拿到的全是最新论文，客户端过滤后一条不剩。
    query = f"cat:{cat}"
    if until:
        lo = cutoff.strftime("%Y%m%d%H%M")
        hi = until.strftime("%Y%m%d%H%M")
        query = f"cat:{cat} AND submittedDate:[{lo} TO {hi}]"
    params = {
        "search_query": query,
        "sortBy": "lastUpdatedDate",
        "sortOrder": "descending",
        "max_results": max_per_category,
    }
    last_err: Exception | None = None
    for attempt, endpoint in enumerate(ARXIV_ENDPOINTS):
        try:
            r = _query(endpoint, params)
            r.raise_for_status()
            items, total, raw_n = _parse(r.text, cutoff, cat, until)
            if items:
                return items
            # 0 命中：先打印诊断信息，再换下一个端点重试
            snippet = r.text[:200].replace("\n", " ")
            print(f"[arxiv] {cat} via {endpoint} → status={r.status_code} "
                  f"totalResults={total} raw_entries={raw_n} kept=0 "
                  f"snippet={snippet!r}")
        except Exception as e:
            last_err = e
            print(f"[arxiv] {cat} via {endpoint} failed: {e}")
        if attempt + 1 < len(ARXIV_ENDPOINTS):
            time.sleep(2)
    if last_err:
        print(f"[arxiv] {cat} all endpoints failed, last={last_err}")
    return []


def fetch_arxiv(categories: list[str], max_per_category: int = 30,
                window: tuple[datetime, datetime] | None = None) -> list[Item]:
    out: list[Item] = []
    if window:
        cutoff, until = window
    else:
        cutoff, until = datetime.now(timezone.utc) - timedelta(hours=36), None
    for cat in categories:
        out.extend(_fetch_category(cat, max_per_category, cutoff, until))
    return out
