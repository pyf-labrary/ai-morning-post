"""用 Claude 把一天的素材聚类、打分、分板块。

输出 out/articles/{date}.curated.json，结构：
{
  "date": "...",
  "sections": [
    {"id": "model_release", "name": "模型发布",
     "stories": [{"headline": "...", "summary": "...", "items": [<原始 fingerprint>...],
                  "importance": 0-10, "primary_url": "..."}]},
    ...
  ]
}
"""
from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict
from pathlib import Path

import yaml
from anthropic import Anthropic

from .common import ARTICLES_DIR, CONFIG_DIR, Item, load_raw, today_str

MODEL = "claude-opus-4-7"

SYSTEM_PROMPT = """你是 AI 行业新闻主编，专为中文读者整理「AI 晨报」。

任务：把过去 24 小时的全网素材聚类、去重、打分、分板块。

要求：
1. 同一事件的多条素材合并成一个 story（譬如 OpenAI 发布会被多家媒体报道，只算 1 条）。
2. 每个 story 给一个 1–10 的重要性分数（10 = 必读头条；5 = 中等；1 = 边角料）。打分参考：
   - 一手权威来源（公司官博、官方公告）+2
   - 多源覆盖（≥3 个独立来源）+2
   - X / Reddit 热度（>1000 likes / >500 upvotes）+1
   - arXiv 仅在被多人引用或带突破性 claim 时才入选，分数压在 5 以下
3. 板块（必须用这些 id）：
   - model_release  模型发布（新模型/版本/能力升级）
   - company        公司动态（融资/收购/人事/诉讼/战略）
   - research       研究论文（学术突破、benchmark、技术路线）
   - product        应用产品（C 端/B 端 AI 产品、agent、新功能）
   - opinion        行业观点（访谈、长文、监管、争议）
   - opensource     开源工具（GitHub repo、库、框架）
4. 每板块按 importance 降序排列，板块内最多保留 8 个 story。
5. story.headline 用中文，简短有钩子（≤30 字），不要标题党但要传神。
6. story.summary 1–2 句话讲清楚是什么，可能的中文。
7. story.primary_url 选最权威的一个原文链接（官方 > 主流媒体 > 社区）。
8. items 字段填入参与该 story 的所有素材 fingerprint。
9. 当天没有 story 的板块，sections 数组里仍保留 id 但 stories 为空。

只输出 JSON，不要任何 markdown 代码块包裹，不要前后多余文字。"""


def items_to_compact(items: list[Item]) -> str:
    lines = []
    for it in items:
        score_part = f" score={int(it.score)}" if it.score else ""
        lines.append(
            f"[{it.fingerprint}] ({it.source}{score_part} w={it.weight}) "
            f"{it.title}\n  {it.url}\n  {it.summary[:240]}"
        )
    return "\n\n".join(lines)


def curate(date: str | None = None) -> Path:
    date = date or today_str()
    items = load_raw(date)
    if not items:
        raise SystemExit(f"no raw items for {date}; run fetch first")

    cfg = yaml.safe_load((CONFIG_DIR / "sources.example.yaml").read_text(encoding="utf-8"))
    sections_def = cfg.get("sections", [])

    client = Anthropic()
    user_msg = (
        f"日期：{date}\n\n"
        f"板块定义（参考关键词，但分类时以语义为准）：\n"
        f"{json.dumps(sections_def, ensure_ascii=False, indent=2)}\n\n"
        f"素材（共 {len(items)} 条）：\n\n"
        f"{items_to_compact(items)}\n\n"
        "请输出 JSON。"
    )

    resp = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=[
            {"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    if text.startswith("```"):
        text = text.strip("`").split("\n", 1)[1].rsplit("\n", 1)[0]

    data = json.loads(text)
    data["date"] = date
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTICLES_DIR / f"{date}.curated.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"curated → {out}")
    print(f"cache: created={resp.usage.cache_creation_input_tokens or 0} "
          f"read={resp.usage.cache_read_input_tokens or 0} "
          f"input={resp.usage.input_tokens} output={resp.usage.output_tokens}")
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    curate(args.date)


if __name__ == "__main__":
    main()
