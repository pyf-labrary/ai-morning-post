"""X / Twitter fetcher。

第一版用 twitterapi.io（最便宜，~$0.15/1000 推文）。需要环境变量 TWITTERAPI_IO_KEY。
未配置时静默返回空列表，整条流水线仍可运行。
"""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

import httpx

from ..common import Item

API_BASE = "https://api.twitterapi.io/twitter/user/last_tweets"


def fetch_x(accounts: list[str]) -> list[Item]:
    key = os.getenv("TWITTERAPI_IO_KEY")
    if not key:
        print("[x] TWITTERAPI_IO_KEY 未配置，跳过 X")
        return []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=36)
    out: list[Item] = []
    headers = {"X-API-Key": key}
    for handle in accounts:
        try:
            r = httpx.get(API_BASE, params={"userName": handle}, headers=headers, timeout=30)
            r.raise_for_status()
            tweets = r.json().get("data", {}).get("tweets", [])
        except Exception as e:
            print(f"[x] @{handle} failed: {e}")
            continue
        for t in tweets[:20]:
            created = t.get("createdAt", "")
            try:
                # X 时间格式：Wed Oct 10 20:19:24 +0000 2024
                dt = datetime.strptime(created, "%a %b %d %H:%M:%S %z %Y")
                if dt < cutoff:
                    continue
                iso = dt.isoformat()
            except Exception:
                iso = ""
            text = t.get("text", "").strip()
            tid = t.get("id")
            out.append(Item(
                source=f"x:@{handle}",
                source_type="x",
                title=text[:140],
                url=f"https://x.com/{handle}/status/{tid}",
                summary=text,
                published=iso,
                author=handle,
                score=float(t.get("likeCount", 0)),
                weight=6,
                extra={
                    "retweets": t.get("retweetCount", 0),
                    "replies": t.get("replyCount", 0),
                    "views": t.get("viewCount", 0),
                },
            ))
    return out
