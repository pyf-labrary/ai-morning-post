"""每个非空板块生成一篇微信公众号文章（Markdown）。

输出 out/articles/{date}/{section_id}.md
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .common import ARTICLES_DIR, today_str
from .llm import LLM_MODEL, USE_CACHE, get_client

SYSTEM_PROMPT = """你是 AI 晨报主笔，给微信公众号写稿。读者画像：技术从业者、投资人、产品经理，一半是中文母语，看重信息密度与判断力。

风格要求：
- 标题：6–18 字，有钩子但不标题党，避免「震惊体」「最」字开头。
- 导语：1 段，3–4 句，先抛今天该板块最值得看的 1 件事，给一个判断或视角。
- 正文：每个 story 一个小节，二级标题（用 `## `），约 150–300 字。结构 = 是什么 / 关键点 / 为什么重要。
- 引用原文链接：每个小节末尾用 markdown 链接形式列出 `> 原文：[来源](url)`。如有多个来源，最多列 3 个。
- 结语：1 段，2 句以内，给一句记忆点或留给读者的问题。
- 全文用简体中文，专业名词首次出现保留英文（如 GPT-5、agentic）。
- 不写未提供的事实；不编数据；语气克制、有判断、不堆砌形容词。
- 输出纯 Markdown，从 `# 标题` 开始，不要 frontmatter，不要代码块包裹整篇。"""


def render_story_block(story: dict) -> str:
    parts = [f"### {story.get('headline', '')}", ""]
    parts.append(story.get("summary", ""))
    if story.get("primary_url"):
        parts.append(f"\n原文：{story['primary_url']}")
    parts.append(f"\n（重要性 {story.get('importance', 0)}/10）")
    return "\n".join(parts)


def write_articles(date: str | None = None) -> list[Path]:
    date = date or today_str()
    curated_path = ARTICLES_DIR / f"{date}.curated.json"
    if not curated_path.exists():
        raise SystemExit(f"missing {curated_path}; run curate first")
    data = json.loads(curated_path.read_text(encoding="utf-8"))

    out_dir = ARTICLES_DIR / date
    out_dir.mkdir(parents=True, exist_ok=True)

    client = get_client()
    system = (
        [{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}]
        if USE_CACHE else SYSTEM_PROMPT
    )
    written: list[Path] = []

    for section in data.get("sections", []):
        stories = section.get("stories", [])
        if not stories:
            continue
        sid = section["id"]
        sname = section.get("name", sid)

        story_dump = "\n\n".join(render_story_block(s) for s in stories)
        user_msg = (
            f"日期：{date}\n板块：{sname}（id={sid}）\n\n"
            f"今日该板块共 {len(stories)} 条 story（已按重要性排序）：\n\n"
            f"{story_dump}\n\n"
            "请按规范产出整篇 Markdown。"
        )

        resp = client.messages.create(
            model=LLM_MODEL,
            max_tokens=8000,
            system=system,
            messages=[{"role": "user", "content": user_msg}],
        )
        md = "".join(b.text for b in resp.content if b.type == "text").strip()
        path = out_dir / f"{sid}.md"
        path.write_text(md, encoding="utf-8")
        written.append(path)
        u = resp.usage
        cache_info = f"cache_read={getattr(u, 'cache_read_input_tokens', 0) or 0} " if USE_CACHE else ""
        print(f"  {sname} → {path.name} ({cache_info}in={u.input_tokens} out={u.output_tokens})")

    return written


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    write_articles(args.date)


if __name__ == "__main__":
    main()
