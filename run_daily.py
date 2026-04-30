"""一键跑全流程。本地与 GH Actions 都用这个。"""
from __future__ import annotations

import sys

from src.common import today_str
from src.fetch import main as run_fetch
from src.curate import curate
from src.write import write_articles
from src.render import render_date
from src.publish import build_articles


def main() -> None:
    date = today_str()
    print(f"=== AI Morning Post · {date} ===")

    print("[1/5] fetch")
    sys.argv = ["fetch"]
    run_fetch()

    print("[2/5] curate")
    curate(date)

    print("[3/5] write")
    write_articles(date)

    print("[4/5] render")
    render_date(date)

    print("[5/5] publish (dry-run)")
    arts = build_articles(date)
    print(f"  prepared {len(arts)} articles")


if __name__ == "__main__":
    main()
