"""Markdown → 微信公众号 HTML（精致排版）。

设计原则：
- 全 inline CSS（微信不允许 <style> 与外链 CSS）
- 移动端优先（公众号 90% 在手机看），字号 16px、行高 1.85
- 主色调：#1a73e8（深蓝）+ 灰阶，避免花哨
- 视觉节奏：顶部色块 → 导语 → 分隔 → 多个小节（每节带封面图）→ 结语 → 落款
- 每个 ## 小节后插入对应 cover_path（按顺序匹配 curated.json 里的 stories）
"""
from __future__ import annotations

import argparse
import base64
import json
import re
from pathlib import Path

import markdown as md

from .common import ARTICLES_DIR, ROOT, today_str

ACCENT = "#1a73e8"
MUTED = "#8a94a6"
INK = "#1f2330"
SOFT_BG = "#f6f8fb"

INLINE = {
    "wrap": (
        "max-width:100%;font-size:16px;line-height:1.85;"
        f"color:{INK};letter-spacing:0.3px;"
        "font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',"
        "'Helvetica Neue',Helvetica,'Microsoft YaHei',Arial,sans-serif;"
        "word-break:break-word;"
    ),
    "header": (
        "margin:-4px 0 22px;padding:18px 18px 16px;"
        f"background:linear-gradient(135deg,{ACCENT} 0%,#0d4ac1 100%);"
        "border-radius:12px;color:#fff;"
    ),
    "header_label": (
        "display:inline-block;padding:3px 10px;border-radius:999px;"
        "background:rgba(255,255,255,0.18);font-size:12px;letter-spacing:1px;"
        "margin-bottom:10px;"
    ),
    "header_h1": (
        "margin:0;padding:0;font-size:26px;font-weight:700;"
        "color:#fff;line-height:1.35;border:0;"
    ),
    "header_meta": (
        "margin:8px 0 0;font-size:13px;color:rgba(255,255,255,0.85);"
    ),
    "lead": (
        "margin:18px 0 24px;padding:14px 16px;"
        f"background:{SOFT_BG};border-left:3px solid {ACCENT};"
        "border-radius:0 8px 8px 0;font-size:15.5px;color:#2a2f3a;"
    ),
    "h2": (
        "font-size:19px;font-weight:700;margin:34px 0 12px;"
        f"color:{INK};padding:6px 0 6px 12px;"
        f"border-left:4px solid {ACCENT};line-height:1.5;"
    ),
    "h3": (
        f"font-size:17px;font-weight:600;margin:24px 0 8px;color:{INK};"
    ),
    "p": "margin:12px 0;",
    "a": (
        f"color:{ACCENT};text-decoration:none;"
        f"border-bottom:1px solid {ACCENT}33;padding-bottom:1px;"
    ),
    "blockquote": (
        f"margin:16px 0;padding:10px 14px;background:{SOFT_BG};"
        "border-left:3px solid #cdd5e0;border-radius:0 6px 6px 0;"
        f"color:{MUTED};font-size:14.5px;"
    ),
    "code": (
        "background:#eef1f6;padding:2px 6px;border-radius:4px;font-size:14px;"
        "font-family:'SF Mono',Menlo,Consolas,monospace;color:#cf3a52;"
    ),
    "ul": "margin:12px 0;padding-left:22px;",
    "ol": "margin:12px 0;padding-left:22px;",
    "li": "margin:6px 0;",
    "hr": (
        "border:0;height:1px;background:linear-gradient(90deg,"
        "transparent 0%,#dde3ec 50%,transparent 100%);margin:28px 0;"
    ),
    "img_wrap": "margin:16px 0;text-align:center;",
    "img": (
        "max-width:100%;border-radius:10px;"
        "box-shadow:0 2px 8px rgba(20,30,60,0.08);"
    ),
    "footer": (
        f"margin-top:36px;padding:20px 16px;background:{SOFT_BG};"
        "border-radius:10px;text-align:center;"
        f"color:{MUTED};font-size:13px;line-height:1.7;"
    ),
}

SECTION_META = {
    "model_release": ("模型发布", "🚀"),
    "company":       ("公司动态", "🏢"),
    "research":      ("研究论文", "🔬"),
    "product":       ("应用产品", "📱"),
    "opinion":       ("行业观点", "💭"),
    "opensource":    ("开源工具", "⚙️"),
}


def encode_local_image(rel_path: str) -> str | None:
    """本地图片转 data URI，方便单文件预览；微信发布前会被 publish 替换成微信 URL。"""
    p = ROOT / rel_path
    if not p.exists():
        return None
    suffix = p.suffix.lstrip(".").lower()
    mime = "jpeg" if suffix in ("jpg", "jpeg") else suffix
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/{mime};base64,{b64}"


def insert_covers(md_text: str, stories: list[dict]) -> str:
    """按 ## 标题顺序在每个小节标题下插入 ![]()。"""
    out_lines: list[str] = []
    h2_idx = 0
    for line in md_text.split("\n"):
        out_lines.append(line)
        if line.startswith("## ") and h2_idx < len(stories):
            cover = stories[h2_idx].get("cover_path")
            if cover:
                out_lines += ["", f"![cover]({cover})", ""]
            h2_idx += 1
    return "\n".join(out_lines)


def style_html(html: str) -> str:
    """给 markdown 转出的 HTML 注入 inline 样式 + 包装图片。"""
    rules = [
        (r"<h1>",         f'<h1 style="font-size:24px;font-weight:700;margin:20px 0 14px;color:{INK};line-height:1.4;">'),
        (r"<h2>",         f'<h2 style="{INLINE["h2"]}">'),
        (r"<h3>",         f'<h3 style="{INLINE["h3"]}">'),
        (r"<p>",          f'<p style="{INLINE["p"]}">'),
        (r"<a ",          f'<a style="{INLINE["a"]}" '),
        (r"<blockquote>", f'<blockquote style="{INLINE["blockquote"]}">'),
        (r"<code>",       f'<code style="{INLINE["code"]}">'),
        (r"<ul>",         f'<ul style="{INLINE["ul"]}">'),
        (r"<ol>",         f'<ol style="{INLINE["ol"]}">'),
        (r"<li>",         f'<li style="{INLINE["li"]}">'),
        (r"<hr />",       f'<hr style="{INLINE["hr"]}" />'),
    ]
    for pat, repl in rules:
        html = re.sub(pat, repl, html)
    # 把 <p><img></p> 包成居中容器
    html = re.sub(
        r'<p style="[^"]*"><img alt="[^"]*" src="([^"]+)" /></p>',
        rf'<section style="{INLINE["img_wrap"]}"><img src="\1" style="{INLINE["img"]}" /></section>',
        html,
    )
    return html


def render_section(section_id: str, md_path: Path, curated_section: dict, date: str) -> str:
    name, emoji = SECTION_META.get(section_id, (section_id, "📰"))
    md_text = md_path.read_text(encoding="utf-8")
    stories = curated_section.get("stories", [])
    md_text = insert_covers(md_text, stories)

    # 把 markdown 里第一个 # 标题抽出来当顶部 hero 用，剩下的渲染
    lines = md_text.split("\n")
    title = ""
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        lines = lines[1:]
        # 跳过紧随的空行
        while lines and not lines[0].strip():
            lines = lines[1:]
    body_md = "\n".join(lines)

    # 把图片相对路径转 data URI（本地预览用；微信发布时由 publish 替换）
    def repl_img(m: re.Match) -> str:
        path = m.group(1)
        data_uri = encode_local_image(path)
        return f"![cover]({data_uri or path})"
    body_md = re.sub(r"!\[cover\]\(([^)]+)\)", repl_img, body_md)

    body_html = md.markdown(body_md, extensions=["extra", "sane_lists"])
    body_html = style_html(body_html)

    header = (
        f'<section style="{INLINE["header"]}">'
        f'  <div style="{INLINE["header_label"]}">{emoji} AI 晨报 · {name}</div>'
        f'  <h1 style="{INLINE["header_h1"]}">{title}</h1>'
        f'  <p style="{INLINE["header_meta"]}">{date} · 每日 06:00 自动生成</p>'
        f'</section>'
    )

    footer = (
        f'<section style="{INLINE["footer"]}">'
        f'  <div>「AI 晨报」每日 06:00 自动汇编全网 AI 动态</div>'
        f'  <div style="margin-top:4px;color:#b6bcc8;font-size:12px;">'
        f'  来源：官方博客 · arXiv · Reddit · Hacker News · X</div>'
        f'</section>'
    )

    return f'<section style="{INLINE["wrap"]}">{header}{body_html}{footer}</section>'


def render_date(date: str | None = None) -> list[Path]:
    date = date or today_str()
    curated_path = ARTICLES_DIR / f"{date}.curated.json"
    if not curated_path.exists():
        raise SystemExit(f"missing {curated_path}; run curate first")
    curated = json.loads(curated_path.read_text(encoding="utf-8"))
    sec_by_id = {s["id"]: s for s in curated.get("sections", [])}

    src_dir = ARTICLES_DIR / date
    if not src_dir.exists():
        raise SystemExit(f"missing {src_dir}; run write first")

    written: list[Path] = []
    for md_path in sorted(src_dir.glob("*.md")):
        sid = md_path.stem
        section_data = sec_by_id.get(sid, {"id": sid, "stories": []})
        html = render_section(sid, md_path, section_data, date)
        out = md_path.with_suffix(".html")
        out.write_text(html, encoding="utf-8")
        written.append(out)
        print(f"  {md_path.name} → {out.name} ({len(html):,} bytes)")
    return written


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    render_date(args.date)


if __name__ == "__main__":
    main()
