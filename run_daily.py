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


def main() -> None:
    date = today_str()
    print(f"=== AI Morning Post · {date} ===")

    print("[1/7] fetch")
    sys.argv = ["fetch"]
    run_fetch()

    print("[2/7] curate")
    curate(date)

    print("[3/7] media (OG image fetch + resize)")
    enrich_curated(date)

    print("[4/7] write")
    write_articles(date)

    print("[5/7] render")
    render_date(date)

    print("[6/7] preview index")
    build_preview(date)

    print("[7/7] publish (dry-run)")
    arts = build_articles(date)
    print(f"  prepared {len(arts)} articles")


if __name__ == "__main__":
    main()
