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

from .common import ARTICLES_DIR, CONFIG_DIR, Item, load_raw, today_str
from .llm import LLM_MODEL, USE_CACHE, get_client

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
8. items 字段填入该 story 最具代表性的 fingerprint，最多 3 个（下游只作溯源，别铺满）。
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


# 喂给 LLM 的素材条数上限。源越加越多（dedupe 后已破 260），全量塞进去会把
# curate 的输出 JSON 顶过 max_tokens 导致截断。按 (来源权重, 热度) 取头部即可，
# 低价值长尾对成稿没贡献。
MAX_ITEMS = int(os.getenv("CURATE_MAX_ITEMS", "180"))

# 输出 token 上限。保持 32000——LLM_BASE_URL 指向的第三方 Anthropic-compat 端点
# 已验证接受这个值，调高有被 400 拒绝的风险；且部分端点会按自己更低的上限静默
# 截断，调高也未必生效。真正的兜底是下面的降档阶梯。
MAX_TOKENS = int(os.getenv("CURATE_MAX_TOKENS", "32000"))

# 一次 curate 被截断 / JSON 解析失败时的素材条数降档阶梯：少喂一些换一次能跑完
# 的输出，远好过整轮流水线在第 2 步挂掉（2026-08 连挂 6 天的根因）。
FALLBACK_LADDER = (120, 80, 50)

# 一次 curate 至少要填出这么多个板块才算数。只填出一两个板块通常是这轮跑偏
# 了（2026-08-15 补录踩过：过了「至少一个板块非空」的松校验，出了篇只有单板块
# 的残缺晨报），不是当天真没新闻。达不到就重试，但结果留着兜底。
MIN_FILLED_SECTIONS = int(os.getenv("CURATE_MIN_SECTIONS", "3"))


class CurateTruncated(RuntimeError):
    """本轮输出被截断 / 不是完整 JSON——可以少喂素材重试。"""


def _extract_json(text: str) -> str:
    """剥掉 ```json 围栏和前后杂字，取最外层 JSON 对象。"""
    text = text.strip()
    if text.startswith("```"):
        # ```json\n{...}\n``` —— 去首行围栏与尾部围栏
        text = text.split("\n", 1)[1] if "\n" in text else ""
        text = text.rsplit("```", 1)[0]
        text = text.strip()
    # 有些端点会在 JSON 前后加一句话
    lo, hi = text.find("{"), text.rfind("}")
    if lo == -1 or hi <= lo:
        raise CurateTruncated(f"响应里没有完整 JSON 对象（前 200 字：{text[:200]!r}）")
    return text[lo:hi + 1]


def _curate_once(date: str, items: list[Item], sections_def: list, client) -> dict:
    system = (
        [{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}]
        if USE_CACHE else SYSTEM_PROMPT
    )
    user_msg = (
        f"日期：{date}\n\n"
        f"板块定义（参考关键词，但分类时以语义为准）：\n"
        f"{json.dumps(sections_def, ensure_ascii=False, indent=2)}\n\n"
        f"素材（共 {len(items)} 条）：\n\n"
        f"{items_to_compact(items)}\n\n"
        "请输出 JSON。"
    )

    # 走流式：max_tokens 调大后非流式请求会被 SDK 以「可能超 10 分钟」拒绝。
    with client.messages.stream(
        model=LLM_MODEL,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        resp = stream.get_final_message()

    u = resp.usage
    cache_info = (
        f"cache_created={getattr(u, 'cache_creation_input_tokens', 0) or 0} "
        f"cache_read={getattr(u, 'cache_read_input_tokens', 0) or 0} "
    ) if USE_CACHE else ""
    print(f"  {cache_info}input={u.input_tokens} output={u.output_tokens} "
          f"stop={resp.stop_reason}")

    if resp.stop_reason == "max_tokens":
        raise CurateTruncated(
            f"输出被 max_tokens 截断（{len(items)} 条素材，max_tokens={MAX_TOKENS}）"
        )
    text = "".join(b.text for b in resp.content if b.type == "text")
    try:
        data = json.loads(_extract_json(text))
    except json.JSONDecodeError as e:
        raise CurateTruncated(f"JSON 解析失败：{e}") from e
    if not isinstance(data, dict) or not data.get("sections"):
        raise CurateTruncated("JSON 里没有 sections")
    filled = [sec for sec in data["sections"] if sec.get("stories")]
    if not filled:
        raise CurateTruncated("所有板块都是空的")
    return data


def _score(data: dict) -> tuple[int, int]:
    """(有内容的板块数, story 总数)——用来在多次尝试里挑最好的一次。"""
    filled = [sec for sec in data.get("sections", []) if sec.get("stories")]
    return len(filled), sum(len(sec["stories"]) for sec in filled)


def curate(date: str | None = None) -> Path:
    date = date or today_str()
    items = load_raw(date)
    if not items:
        raise SystemExit(f"no raw items for {date}; run fetch first")
    ranked = sorted(items, key=lambda it: (it.weight, it.score), reverse=True)

    cfg = yaml.safe_load((CONFIG_DIR / "sources.example.yaml").read_text(encoding="utf-8"))
    sections_def = cfg.get("sections", [])
    client = get_client()

    # 从 MAX_ITEMS 起，被截断就顺着阶梯少喂一点重试。
    budgets = [MAX_ITEMS, *(n for n in FALLBACK_LADDER if n < MAX_ITEMS)]
    last_err: Exception | None = None
    best: dict | None = None
    for attempt, n in enumerate(budgets, 1):
        batch = ranked[:n]
        print(f"[curate] attempt {attempt}/{len(budgets)}: top {len(batch)} "
              f"of {len(ranked)} items by (weight, score)")
        try:
            data = _curate_once(date, batch, sections_def, client)
        except CurateTruncated as e:
            last_err = e
            print(f"  ✗ {e} —— 降档重试")
            continue
        filled, stories = _score(data)
        print(f"  → {filled} 个板块有内容，共 {stories} 条 story")
        if best is None or _score(data) > _score(best):
            best = data
        if filled >= MIN_FILLED_SECTIONS:
            break
        # 只填出一两个板块多半是这轮跑偏了（不是当天真没新闻）——再试一次，
        # 但把这次的结果留着兜底，别为了追求完美最后一无所有。
        print(f"  ✗ 只有 {filled} 个板块有内容（要求 ≥{MIN_FILLED_SECTIONS}）—— 重试")

    if best is None:
        raise RuntimeError(
            f"curate 降档到 {budgets[-1]} 条素材仍失败，最后一次：{last_err}"
        )
    best["date"] = date
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    out = ARTICLES_DIR / f"{date}.curated.json"
    out.write_text(json.dumps(best, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"curated → {out}（{_score(best)[0]} 板块 / {_score(best)[1]} story）")
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    curate(args.date)


if __name__ == "__main__":
    main()
