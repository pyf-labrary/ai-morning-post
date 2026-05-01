"""生成本地预览首页：把当天所有 .html 文章串成一个可滚动浏览的索引页。"""
from __future__ import annotations

import argparse
from pathlib import Path

from .common import ARTICLES_DIR, today_str
from .render import SECTION_META

PAGE = """<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI 晨报 · {date}</title>
<style>
  body{{margin:0;background:#eef1f6;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;}}
  .nav{{position:sticky;top:0;background:#fff;border-bottom:1px solid #e5e9f0;
       padding:12px 18px;z-index:10;display:flex;gap:14px;flex-wrap:wrap;}}
  .nav a{{color:#1a73e8;text-decoration:none;font-size:14px;}}
  .nav a:hover{{text-decoration:underline;}}
  .grid{{max-width:520px;margin:0 auto;padding:18px 14px 60px;}}
  article{{background:#fff;margin:18px 0;padding:18px;border-radius:14px;
          box-shadow:0 4px 14px rgba(20,30,60,0.06);}}
  h2.section-tag{{font-size:13px;color:#8a94a6;margin:0 0 10px;font-weight:500;}}
</style></head><body>
<div class="nav">{nav}</div>
<div class="grid">{articles}</div>
</body></html>"""

ORDER = ["model_release", "company", "research", "product", "opinion", "opensource"]


def build(date: str | None = None) -> Path:
    date = date or today_str()
    src_dir = ARTICLES_DIR / date
    if not src_dir.exists():
        raise SystemExit(f"missing {src_dir}")

    nav_links, articles = [], []
    for sid in ORDER:
        path = src_dir / f"{sid}.html"
        if not path.exists():
            continue
        name, emoji = SECTION_META.get(sid, (sid, ""))
        nav_links.append(f'<a href="#{sid}">{emoji} {name}</a>')
        body = path.read_text(encoding="utf-8")
        articles.append(f'<article id="{sid}">{body}</article>')

    html = PAGE.format(
        date=date,
        nav=" · ".join(nav_links),
        articles="\n".join(articles),
    )
    out = src_dir / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"preview → {out}")
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    build(args.date)


if __name__ == "__main__":
    main()
