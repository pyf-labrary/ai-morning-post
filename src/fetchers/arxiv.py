"""arXiv API fetcher。"""
from __future__ import annotations

import httpx
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET

from ..common import Item

ARXIV_API = "https://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom"}


def fetch_arxiv(categories: list[str], max_per_category: int = 30) -> list[Item]:
    out: list[Item] = []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=36)
    for cat in categories:
        params = {
            "search_query": f"cat:{cat}",
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": max_per_category,
        }
        try:
            r = httpx.get(ARXIV_API, params=params, timeout=30)
            r.raise_for_status()
        except Exception as e:
            print(f"[arxiv] {cat} failed: {e}")
            continue
        root = ET.fromstring(r.text)
        for entry in root.findall("atom:entry", NS):
            pub = entry.findtext("atom:published", default="", namespaces=NS)
            try:
                dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
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
    return out
