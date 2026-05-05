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


def _parse(xml_text: str, cutoff: datetime, cat: str) -> tuple[list[Item], int, int]:
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
            if dt < cutoff:
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


def _fetch_category(cat: str, max_per_category: int, cutoff: datetime) -> list[Item]:
    params = {
        "search_query": f"cat:{cat}",
        "sortBy": "lastUpdatedDate",
        "sortOrder": "descending",
        "max_results": max_per_category,
    }
    last_err: Exception | None = None
    for attempt, endpoint in enumerate(ARXIV_ENDPOINTS):
        try:
            r = _query(endpoint, params)
            r.raise_for_status()
            items, total, raw_n = _parse(r.text, cutoff, cat)
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


def fetch_arxiv(categories: list[str], max_per_category: int = 30) -> list[Item]:
    out: list[Item] = []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=36)
    for cat in categories:
        out.extend(_fetch_category(cat, max_per_category, cutoff))
    return out
