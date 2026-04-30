"""Reddit fetcher，使用免登录 JSON 接口。"""
from __future__ import annotations

import httpx
from datetime import datetime, timezone

from ..common import Item

UA = "ai-morning-post/0.1 (by /u/gittee-coder)"


def fetch_reddit(subreddits: list[str], min_score: int = 50, max_per_sub: int = 20) -> list[Item]:
    out: list[Item] = []
    for sub in subreddits:
        url = f"https://www.reddit.com/r/{sub}/top.json?t=day&limit={max_per_sub}"
        try:
            r = httpx.get(url, headers={"User-Agent": UA}, timeout=30)
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            print(f"[reddit] r/{sub} failed: {e}")
            continue
        for child in data.get("data", {}).get("children", []):
            d = child.get("data", {})
            score = d.get("score", 0)
            if score < min_score:
                continue
            created = datetime.fromtimestamp(d.get("created_utc", 0), tz=timezone.utc)
            permalink = "https://www.reddit.com" + d.get("permalink", "")
            external = d.get("url_overridden_by_dest") or permalink
            out.append(Item(
                source=f"reddit:{sub}",
                source_type="reddit",
                title=d.get("title", "").strip(),
                url=external,
                summary=(d.get("selftext", "") or "")[:600],
                published=created.isoformat(),
                author=d.get("author", ""),
                score=float(score),
                weight=4,
                extra={"permalink": permalink, "num_comments": d.get("num_comments", 0)},
            ))
    return out
