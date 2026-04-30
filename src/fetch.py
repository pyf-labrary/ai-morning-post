"""主入口：抓取所有源 → 去重 → 落 raw json。"""
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from .common import CONFIG_DIR, dedupe, save_raw
from .fetchers import fetch_arxiv, fetch_hackernews, fetch_reddit, fetch_rss, fetch_x


def load_config() -> dict:
    path = CONFIG_DIR / "sources.yaml"
    if not path.exists():
        path = CONFIG_DIR / "sources.example.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--skip", nargs="*", default=[], help="跳过的源类型：rss arxiv reddit hn x")
    args = p.parse_args()

    cfg = load_config()
    items = []

    if "rss" not in args.skip:
        rss_items = fetch_rss(cfg.get("rss", []))
        print(f"  rss: {len(rss_items)}")
        items.extend(rss_items)

    if "arxiv" not in args.skip:
        a = cfg.get("arxiv", {})
        arxiv_items = fetch_arxiv(a.get("categories", []), a.get("max_per_category", 30))
        print(f"  arxiv: {len(arxiv_items)}")
        items.extend(arxiv_items)

    if "reddit" not in args.skip:
        r = cfg.get("reddit", {})
        reddit_items = fetch_reddit(
            r.get("subreddits", []), r.get("min_score", 50), r.get("max_per_sub", 20)
        )
        print(f"  reddit: {len(reddit_items)}")
        items.extend(reddit_items)

    if "hn" not in args.skip:
        h = cfg.get("hackernews", {})
        hn_items = fetch_hackernews(h.get("min_points", 80), h.get("keywords"))
        print(f"  hackernews: {len(hn_items)}")
        items.extend(hn_items)

    if "x" not in args.skip:
        x = cfg.get("x", {})
        x_items = fetch_x(x.get("accounts", []))
        print(f"  x: {len(x_items)}")
        items.extend(x_items)

    deduped = dedupe(items)
    print(f"total {len(items)} → after dedupe {len(deduped)}")
    path = save_raw(deduped)
    print(f"saved → {path}")


if __name__ == "__main__":
    main()
