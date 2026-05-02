"""Reddit fetcher，使用免登录 JSON 接口。"""
from __future__ import annotations

import httpx
from datetime import datetime, timezone

from ..common import Item

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
HEADERS = {
    "User-Agent": UA,
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
}


def _fetch_one(sub: str, max_per_sub: int) -> dict | None:
    """先尝试 old.reddit.com（对数据中心 IP 友好些），再 fallback 到 www。"""
    for host in ("old.reddit.com", "www.reddit.com"):
        url = f"https://{host}/r/{sub}/top.json?t=day&limit={max_per_sub}"
        try:
            r = httpx.get(url, headers=HEADERS, timeout=30, follow_redirects=True)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            last = e
    print(f"[reddit] r/{sub} failed: {last}")
    return None


def fetch_reddit(subreddits: list[str], min_score: int = 50, max_per_sub: int = 20) -> list[Item]:
    out: list[Item] = []
    for sub in subreddits:
        data = _fetch_one(sub, max_per_sub)
        if not data:
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
