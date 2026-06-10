"""把当天 AI 晨报合并成一篇 Jekyll post 推到 marginalia 站。

设计：
- 一天一篇 post：marginalia/_posts/{date}-ai-morning-post.md
- 图片同步到 marginalia/assets/img/ai-hot/{date}/，markdown 里改写成站内 URL
- post 带 tag `ai-hot`，home.html 用这个 tag 找最新一篇做置顶卡片
- 多板块用 H2 串起来；每个板块下复用 write.py 的 Markdown，去掉外层 H1 后挂进去
- 调 git add/commit/push（用 ~/.config/gh/org_pyf-labrary.token 的 GH_TOKEN）
- 完全无人值守，无须改代码
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .common import ARTICLES_DIR, MEDIA_DIR, ROOT, today_str
from .render import SECTION_META

SECTION_ORDER = [
    "model_release", "company", "research", "product", "opinion", "opensource"
]

DEFAULT_MARGINALIA = Path.home() / "claw" / "marginalia"


SECTION_ID_MAP = {
    "model_release": "model-release",
    "company": "company",
    "research": "research",
    "product": "product",
    "opinion": "opinion",
    "opensource": "opensource",
}


def _section_marker(sid: str, name: str, emoji: str) -> str:
    """每个板块上方的视觉分隔（带 anchor id 让侧栏 TOC 可跳转）。"""
    anchor = SECTION_ID_MAP.get(sid, sid.replace("_", "-"))
    return (
        f'\n\n<h2 id="{anchor}" class="ai-section-divider">{emoji} {name}</h2>\n\n'
    )


def _strip_h1(md: str) -> str:
    """去掉 markdown 文件首个 H1（避免和 post title 重复）。"""
    lines = md.split("\n")
    out = []
    skipped = False
    for line in lines:
        if not skipped and line.startswith("# "):
            skipped = True
            continue
        out.append(line)
    return "\n".join(out).lstrip("\n")


def _insert_covers(md: str, stories: list[dict], img_url_prefix: str) -> str:
    """按 ## 标题顺序插入对应 story 的 cover。"""
    out_lines: list[str] = []
    h2_idx = 0
    for line in md.split("\n"):
        out_lines.append(line)
        if line.startswith("## ") and h2_idx < len(stories):
            cover = stories[h2_idx].get("cover_path")
            if cover:
                fname = Path(cover).name
                out_lines += ["", f"![{fname}]({img_url_prefix}/{fname})", ""]
            h2_idx += 1
    return "\n".join(out_lines)


def _copy_images(date: str, marginalia: Path) -> Path:
    src = MEDIA_DIR / date
    dst = marginalia / "assets" / "img" / "ai-hot" / date
    if src.exists():
        dst.mkdir(parents=True, exist_ok=True)
        for f in src.iterdir():
            if f.is_file():
                shutil.copy2(f, dst / f.name)
        print(f"  copied {len(list(src.iterdir()))} images → {dst.relative_to(marginalia)}")
    return dst


def _build_lead(curated: dict) -> str:
    """从 curated.json 抽几条最高分 story 做整篇导语。"""
    all_stories = []
    for s in curated.get("sections", []):
        for st in s.get("stories", []):
            all_stories.append((st.get("importance", 0), s["id"], st))
    all_stories.sort(key=lambda x: -x[0])
    top3 = all_stories[:3]
    if not top3:
        return ""
    bullets = "\n".join(
        f"- **{SECTION_META.get(sid, ('', ''))[0]}** · {st.get('headline', '')}"
        for _, sid, st in top3
    )
    return (
        "今天最值得看的三件事：\n\n"
        f"{bullets}\n\n"
        "下文按板块展开，正文每条均附原始链接。\n"
    )


def build_post(date: str, marginalia: Path) -> Path:
    curated_path = ARTICLES_DIR / f"{date}.curated.json"
    src_dir = ARTICLES_DIR / date
    if not curated_path.exists() or not src_dir.exists():
        raise SystemExit(f"missing curated/articles for {date}; run pipeline first")

    curated = json.loads(curated_path.read_text(encoding="utf-8"))

    _copy_images(date, marginalia)
    img_url_prefix = f"/marginalia/assets/img/ai-hot/{date}"
    sec_by_id = {s["id"]: s for s in curated.get("sections", [])}

    # 拼装正文 + 收集 TOC sections
    parts: list[str] = [_build_lead(curated)]
    toc_sections: list[dict] = []
    for sid in SECTION_ORDER:
        md_path = src_dir / f"{sid}.md"
        if not md_path.exists():
            continue
        stories = sec_by_id.get(sid, {}).get("stories", [])
        if not stories:
            continue
        name, emoji = SECTION_META.get(sid, (sid, "📰"))
        anchor = SECTION_ID_MAP.get(sid, sid.replace("_", "-"))
        toc_sections.append({
            "id": anchor,
            "name": name,
            "emoji": emoji,
            "count": len(stories),
        })
        body = md_path.read_text(encoding="utf-8")
        body = _strip_h1(body)
        body = _insert_covers(body, stories, img_url_prefix)
        # story heading 从 H2 降级为 H3，避免与板块标题（H2）级别相同
        body = re.sub(r"^## ", "### ", body, flags=re.M)
        parts.append(_section_marker(sid, name, emoji))
        parts.append(body)

    body_md = "\n".join(parts).strip()

    # excerpt：取导语第一行 + top1 story 标题
    excerpt = ""
    for s in curated.get("sections", []):
        for st in s.get("stories", []):
            if st.get("importance", 0) >= 8:
                excerpt = st.get("summary") or st.get("headline") or ""
                break
        if excerpt:
            break
    if not excerpt:
        excerpt = "全网 AI 动态汇总：模型发布、公司动态、研究论文、应用产品、观点与开源工具。"

    title = f"AI 晨报 · {date}"
    description = f"{date} 的 AI 圈每日动态汇总：{excerpt}"[:160]

    # 时间：当天 06:00 +0800（让排序稳定且不晚于真实抓取时间）
    date_iso = f"{date} 06:00:00 +0800"

    sections_yaml = "\n".join(
        f'  - {{ id: {s["id"]}, name: "{s["name"]}", emoji: "{s["emoji"]}", count: {s["count"]} }}'
        for s in toc_sections
    )
    front = (
        "---\n"
        'layout: "ai-hot"\n'
        f'title: "{title}"\n'
        f'date: "{date_iso}"\n'
        'author: "Marginalia"\n'
        f'description: "{description.replace(chr(34), chr(39))}"\n'
        f'excerpt: "{excerpt[:160].replace(chr(34), chr(39))}"\n'
        'tags: [ai-hot, ai-morning-post, daily]\n'
        'keywords: "AI 晨报, AI 新闻, LLM, 大模型, daily AI news, ai-hot"\n'
        f"sections:\n{sections_yaml}\n"
        "---\n\n"
    )

    target = marginalia / "_posts" / f"{date}-ai-morning-post.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(front + body_md + "\n", encoding="utf-8")
    print(f"  wrote {target.relative_to(marginalia)} ({len(body_md):,} chars)")
    return target


def _run(cmd: list[str], cwd: Path, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, check=True)


def git_commit_push(marginalia: Path, date: str, push: bool) -> None:
    env = os.environ.copy()
    if "GH_TOKEN" not in env:
        token_file = Path.home() / ".config/gh/org_pyf-labrary.token"
        if token_file.exists():
            env["GH_TOKEN"] = token_file.read_text().strip()

    _run(["git", "add", "_posts", "assets/img/ai-hot", "_data/hot_topics.json"], marginalia, env=env)
    diff = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=marginalia, capture_output=True, text=True,
    ).stdout.strip()
    if not diff:
        print("  no changes to commit")
        return

    msg = f"ai-hot: daily {date}"
    _run(["git", "-c", "user.name=gittee-coder",
          "-c", "user.email=259323426+gittee-coder@users.noreply.github.com",
          "commit", "-q", "-m", msg], marginalia, env=env)
    sha = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=marginalia, capture_output=True, text=True,
    ).stdout.strip()
    print(f"  committed {sha}: {msg}")

    if push:
        out = subprocess.run(["git", "push"], cwd=marginalia, env=env,
                             capture_output=True, text=True)
        if out.returncode != 0:
            print(f"!! push failed:\n{out.stderr}", file=sys.stderr)
            sys.exit(1)
        print("  pushed to origin")


def check_pages_size(marginalia: Path) -> None:
    """GitHub Pages 站点软限 1 GB。ai-hot 每天进图，体积只会涨——
    每次发布后量一次工作树（即 Pages 实际发布内容），快到线提前喊。
    fail-soft：只告警不阻断发布。"""
    WARN_MB, ALERT_MB = 700, 900

    def du_mb(path: Path) -> float:
        total = 0
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in (".git", "_site", ".jekyll-cache", "vendor")]
            for f in files:
                try:
                    total += (Path(root) / f).stat().st_size
                except OSError:
                    pass
        return total / 1e6

    try:
        site_mb = du_mb(marginalia)
        hot_mb = du_mb(marginalia / "assets" / "img" / "ai-hot")
        line = (f"pages size check: worktree {site_mb:.0f} MB"
                f" (ai-hot images {hot_mb:.0f} MB) / soft limit 1000 MB")
        print(f"  {line}")
        if site_mb >= ALERT_MB:
            # GH Actions annotation —— 在 run 页面顶部红字醒目展示
            print(f"::error title=marginalia Pages 容量告急::{line}，需要立刻清理旧 ai-hot 图片或迁移外部托管")
        elif site_mb >= WARN_MB:
            print(f"::warning title=marginalia Pages 容量预警::{line}，建议规划旧图治理")
        summary = os.getenv("GITHUB_STEP_SUMMARY")
        if summary:
            with open(summary, "a", encoding="utf-8") as fh:
                fh.write(f"\n- {line}\n")
    except Exception as e:  # 容量检查永不打断发布
        print(f"  (size check skipped: {e})", file=sys.stderr)


def publish(date: str | None = None, marginalia: Path | None = None,
            push: bool = True, commit: bool = True) -> Path:
    date = date or today_str()
    marginalia = Path(marginalia or os.getenv("MARGINALIA_REPO") or DEFAULT_MARGINALIA)
    if not (marginalia / "_config.yml").exists():
        raise SystemExit(f"marginalia repo not found at {marginalia}")
    print(f"publish to marginalia: {marginalia}")
    target = build_post(date, marginalia)
    refresh_hot_topics(marginalia)
    if commit:
        git_commit_push(marginalia, date, push=push)
    check_pages_size(marginalia)
    return target


def refresh_hot_topics(marginalia: Path) -> None:
    """重算近 30 天话题热度榜（marginalia/scripts/hot-topics.py →
    _data/hot_topics.json，/ai-hot/ 页静态渲染）。fail-soft 不阻断发布。"""
    script = marginalia / "scripts" / "hot-topics.py"
    if not script.exists():
        return
    out = subprocess.run([sys.executable, str(script)], cwd=marginalia,
                         capture_output=True, text=True)
    if out.returncode == 0:
        print("  " + (out.stdout.strip().splitlines() or ["hot-topics refreshed"])[0])
    else:
        print(f"!! hot-topics failed (non-fatal):\n{out.stderr}", file=sys.stderr)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    p.add_argument("--marginalia", help="path to marginalia repo (default ~/claw/marginalia)")
    p.add_argument("--no-push", action="store_true")
    p.add_argument("--no-commit", action="store_true")
    args = p.parse_args()
    publish(
        date=args.date,
        marginalia=Path(args.marginalia) if args.marginalia else None,
        push=not args.no_push,
        commit=not args.no_commit,
    )


if __name__ == "__main__":
    main()
