"""RSS / Atom fetcher：用于 AI 公司官博 + 中文媒体。"""
from __future__ import annotations

import feedparser

from ..common import Item, within_24h


def fetch_rss(feeds: list[dict]) -> list[Item]:
    out: list[Item] = []
    for feed in feeds:
        try:
            parsed = feedparser.parse(feed["url"])
        except Exception as e:
            print(f"[rss] {feed['name']} failed: {e}")
            continue
        for entry in parsed.entries[:30]:
            published = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                from time import strftime
                published = strftime("%Y-%m-%dT%H:%M:%S+00:00", entry.published_parsed)
            if not within_24h(published):
                continue
            summary = getattr(entry, "summary", "")[:600]
            out.append(Item(
                source=feed["name"],
                source_type="rss",
                title=entry.title,
                url=entry.link,
                summary=summary,
                published=published,
                weight=feed.get("weight", 5),
            ))
    return out
