"""主入口：抓取所有源 → 去重 → 落 raw json。"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from .common import CONFIG_DIR, dedupe, edition_window, save_raw
from .fetchers import fetch_arxiv, fetch_hackernews, fetch_reddit, fetch_rss, fetch_x


def load_config() -> dict:
    path = CONFIG_DIR / "sources.yaml"
    if not path.exists():
        path = CONFIG_DIR / "sources.example.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def run(skip: list[str] | None = None, date: str | None = None,
        backfill: bool = False) -> Path:
    """backfill=True 时按 date 那一期的历史时间窗抓取。

    只有 HN（Algolia 支持 created_at_i 区间）和 arXiv（submittedDate 区间）
    可以回溯；RSS / Reddit / X 没有历史接口，补录时自动跳过。
    """
    skip = list(skip or [])
    window = None
    if backfill:
        if not date:
            raise SystemExit("backfill 需要 --date")
        window = edition_window(date)
        for src in ("rss", "reddit", "x"):
            if src not in skip:
                skip.append(src)
        print(f"  [backfill] 窗口 {window[0].isoformat()} → {window[1].isoformat()}"
              f"，跳过无历史接口的 rss/reddit/x")

    cfg = load_config()
    items = []

    if "rss" not in skip:
        rss_items = fetch_rss(cfg.get("rss", []))
        print(f"  rss: {len(rss_items)}")
        items.extend(rss_items)

    if "arxiv" not in skip:
        a = cfg.get("arxiv", {})
        arxiv_items = fetch_arxiv(a.get("categories", []), a.get("max_per_category", 30),
                                  window=window)
        print(f"  arxiv: {len(arxiv_items)}")
        items.extend(arxiv_items)

    if "reddit" not in skip:
        r = cfg.get("reddit", {})
        reddit_items = fetch_reddit(
            r.get("subreddits", []), r.get("min_score", 50), r.get("max_per_sub", 20)
        )
        print(f"  reddit: {len(reddit_items)}")
        items.extend(reddit_items)

    if "hn" not in skip:
        h = cfg.get("hackernews", {})
        hn_items = fetch_hackernews(h.get("min_points", 80), h.get("keywords"),
                                    window=window)
        print(f"  hackernews: {len(hn_items)}")
        items.extend(hn_items)

    if "x" not in skip:
        x = cfg.get("x", {})
        x_items = fetch_x(x.get("accounts", []))
        print(f"  x: {len(x_items)}")
        items.extend(x_items)

    deduped = dedupe(items)
    print(f"total {len(items)} → after dedupe {len(deduped)}")
    path = save_raw(deduped, date)
    print(f"saved → {path}")
    return path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--skip", nargs="*", default=[], help="跳过的源类型：rss arxiv reddit hn x")
    p.add_argument("--date", help="落盘用的日期（默认今天）")
    p.add_argument("--backfill", action="store_true", help="按 --date 的历史时间窗回溯抓取")
    args = p.parse_args()
    run(skip=args.skip, date=args.date, backfill=args.backfill)


if __name__ == "__main__":
    main()
