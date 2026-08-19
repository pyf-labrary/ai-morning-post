"""一键跑全流程。本地与 GH Actions 都用这个。"""
from __future__ import annotations

import sys

from src.common import today_str
from src.fetch import main as run_fetch
from src.curate import curate
from src.media import enrich_curated
from src.write import write_articles
from src.render import render_date
from src.preview import build as build_preview
from src.publish import build_articles
from src.publish_marginalia import publish as publish_marginalia

import os


def main() -> None:
    date = today_str()
    print(f"=== AI Morning Post · {date} ===")

    print("[1/8] fetch")
    sys.argv = ["fetch"]
    run_fetch()

    print("[2/8] curate")
    curate(date)

    print("[3/8] media (OG image fetch + resize)")
    enrich_curated(date)

    print("[4/8] write")
    write_articles(date)

    print("[5/8] render")
    render_date(date)

    print("[6/8] preview index")
    build_preview(date)

    print("[7/8] publish to Marginalia")
    if os.getenv("SKIP_MARGINALIA") == "1":
        print("  SKIP_MARGINALIA=1, skipping")
    else:
        publish_marginalia(date=date, push=os.getenv("MARGINALIA_NO_PUSH") != "1")

    print("[8/8] publish to WeChat (dry-run)")
    # 站点（第 7 步）已经发出去了；微信这步只是 dry-run，失败不该把整轮判红。
    try:
        arts = build_articles(date)
        print(f"  prepared {len(arts)} articles")
    except Exception as e:  # noqa: BLE001
        print(f"  WARN: WeChat dry-run failed ({type(e).__name__}: {e}) —— 不影响站点发布")


if __name__ == "__main__":
    main()
