"""Markdown → 微信公众号 HTML。

微信不支持 <style>/外链 CSS，所有样式必须 inline。第一版给一套基础 inline 样式，
等公众号正式上线后，再依据真实预览微调字号 / 间距 / 配色。
"""
from __future__ import annotations

import argparse
from pathlib import Path

import markdown as md

from .common import ARTICLES_DIR, today_str

INLINE = {
    "wrap": "font-size:16px;line-height:1.75;color:#222;letter-spacing:0.3px;",
    "h1": "font-size:22px;font-weight:700;margin:24px 0 12px;color:#111;",
    "h2": "font-size:19px;font-weight:700;margin:28px 0 10px;color:#111;"
          "border-left:4px solid #1f6feb;padding-left:10px;",
    "h3": "font-size:17px;font-weight:600;margin:22px 0 8px;color:#222;",
    "p":  "margin:12px 0;",
    "a":  "color:#1f6feb;text-decoration:none;border-bottom:1px solid #d0e3ff;",
    "blockquote": "margin:14px 0;padding:10px 14px;border-left:3px solid #ddd;"
                  "background:#fafafa;color:#555;font-size:15px;",
    "code": "background:#f5f5f5;padding:2px 6px;border-radius:4px;font-size:14px;"
            "font-family:Menlo,Consolas,monospace;",
    "ul": "margin:10px 0;padding-left:22px;",
    "ol": "margin:10px 0;padding-left:22px;",
    "li": "margin:6px 0;",
    "hr": "border:0;border-top:1px solid #e5e5e5;margin:24px 0;",
}


def inline_style(html: str) -> str:
    """非常朴素的 tag → style 替换；已经够用，后续可以替换成 premailer。"""
    rules = [
        ("<h1>",         f'<h1 style="{INLINE["h1"]}">'),
        ("<h2>",         f'<h2 style="{INLINE["h2"]}">'),
        ("<h3>",         f'<h3 style="{INLINE["h3"]}">'),
        ("<p>",          f'<p style="{INLINE["p"]}">'),
        ("<a ",          f'<a style="{INLINE["a"]}" '),
        ("<blockquote>", f'<blockquote style="{INLINE["blockquote"]}">'),
        ("<code>",       f'<code style="{INLINE["code"]}">'),
        ("<ul>",         f'<ul style="{INLINE["ul"]}">'),
        ("<ol>",         f'<ol style="{INLINE["ol"]}">'),
        ("<li>",         f'<li style="{INLINE["li"]}">'),
        ("<hr />",       f'<hr style="{INLINE["hr"]}" />'),
    ]
    for old, new in rules:
        html = html.replace(old, new)
    return f'<section style="{INLINE["wrap"]}">{html}</section>'


def render_md_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    html = md.markdown(text, extensions=["extra", "sane_lists"])
    return inline_style(html)


def render_date(date: str | None = None) -> list[Path]:
    date = date or today_str()
    src_dir = ARTICLES_DIR / date
    if not src_dir.exists():
        raise SystemExit(f"missing {src_dir}; run write first")
    written: list[Path] = []
    for md_path in sorted(src_dir.glob("*.md")):
        html = render_md_file(md_path)
        out = md_path.with_suffix(".html")
        out.write_text(html, encoding="utf-8")
        written.append(out)
        print(f"  {md_path.name} → {out.name}")
    return written


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    render_date(args.date)


if __name__ == "__main__":
    main()
