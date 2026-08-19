"""HackerNews fetcher，用 Algolia 搜索接口按时间窗口拉。"""
from __future__ import annotations

import httpx
from datetime import datetime, timedelta, timezone

from ..common import Item

ALGOLIA = "https://hn.algolia.com/api/v1/search_by_date"


def fetch_hackernews(min_points: int = 80, keywords: list[str] | None = None,
                     window: tuple[datetime, datetime] | None = None) -> list[Item]:
    keywords = keywords or ["AI", "LLM", "GPT", "Claude", "Gemini", "model", "agent"]
    # window=(start, end) 用于回溯补录某一天；缺省就是「此刻往前 36 小时」。
    if window:
        cutoff, until = int(window[0].timestamp()), int(window[1].timestamp())
    else:
        cutoff = int((datetime.now(timezone.utc) - timedelta(hours=36)).timestamp())
        until = None
    out: list[Item] = []
    seen: set[str] = set()
    for kw in keywords:
        params = {
            "query": kw,
            "tags": "story",
            "numericFilters": (
                f"created_at_i>{cutoff},points>{min_points}"
                + (f",created_at_i<{until}" if until else "")
            ),
            "hitsPerPage": 30,
        }
        try:
            r = httpx.get(ALGOLIA, params=params, timeout=30)
            r.raise_for_status()
            hits = r.json().get("hits", [])
        except Exception as e:
            print(f"[hn] {kw} failed: {e}")
            continue
        for h in hits:
            obj_id = h.get("objectID")
            if obj_id in seen:
                continue
            seen.add(obj_id)
            url = h.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
            created = h.get("created_at", "")
            out.append(Item(
                source="hackernews",
                source_type="hn",
                title=(h.get("title") or "").strip(),
                url=url,
                summary=(h.get("story_text") or "")[:600],
                published=created,
                author=h.get("author", ""),
                score=float(h.get("points", 0)),
                weight=5,
                extra={"hn_id": obj_id, "comments": h.get("num_comments", 0)},
            ))
    return out
