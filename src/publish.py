"""推送到微信公众号草稿箱（多图文）。

第一版只生成草稿，由人工最终在公众号后台点「发布」。等稳定再切到 freepublish/submit。

接口文档：https://developers.weixin.qq.com/doc/offiaccount/Publish/Add_draft.html

需要环境变量：
- WECHAT_APPID
- WECHAT_APPSECRET

注意：草稿接口要求文章字数 ≥ 200，封面图必须先用 add_material 上传。
本模块还未真接 — 先把代码骨架写好，公众号 appid/secret 拿到后改 SKIP_PUBLISH 为 False 即可联调。
"""
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import httpx

from .common import ARTICLES_DIR, today_str

API_BASE = "https://api.weixin.qq.com/cgi-bin"
SKIP_PUBLISH = os.getenv("WECHAT_SKIP_PUBLISH", "1") == "1"


def get_access_token() -> str:
    appid = os.environ["WECHAT_APPID"]
    secret = os.environ["WECHAT_APPSECRET"]
    r = httpx.get(f"{API_BASE}/token", params={
        "grant_type": "client_credential",
        "appid": appid,
        "secret": secret,
    }, timeout=15)
    r.raise_for_status()
    data = r.json()
    if "access_token" not in data:
        raise RuntimeError(f"token error: {data}")
    return data["access_token"]


def upload_image(token: str, image_path: Path) -> str:
    """上传永久素材，返回 media_id。"""
    with image_path.open("rb") as f:
        files = {"media": (image_path.name, f, "image/jpeg")}
        r = httpx.post(
            f"{API_BASE}/material/add_material",
            params={"access_token": token, "type": "image"},
            files=files,
            timeout=60,
        )
    r.raise_for_status()
    data = r.json()
    if "media_id" not in data:
        raise RuntimeError(f"upload error: {data}")
    return data["media_id"]


def add_draft(token: str, articles: list[dict]) -> str:
    """articles: [{title, author, content, content_source_url, thumb_media_id, digest, ...}]"""
    r = httpx.post(
        f"{API_BASE}/draft/add",
        params={"access_token": token},
        content=json.dumps({"articles": articles}, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        timeout=60,
    )
    r.raise_for_status()
    data = r.json()
    if "media_id" not in data:
        raise RuntimeError(f"draft error: {data}")
    return data["media_id"]


SECTION_ORDER = ["model_release", "company", "research", "product", "opinion", "opensource"]


def build_articles(date: str) -> list[dict]:
    src_dir = ARTICLES_DIR / date
    curated = json.loads((ARTICLES_DIR / f"{date}.curated.json").read_text(encoding="utf-8"))
    section_meta = {s["id"]: s for s in curated.get("sections", [])}
    out: list[dict] = []
    for sid in SECTION_ORDER:
        html_path = src_dir / f"{sid}.html"
        if not html_path.exists():
            continue
        meta = section_meta.get(sid, {})
        # 标题：从 markdown 第一行取
        md_path = src_dir / f"{sid}.md"
        title = meta.get("name", sid)
        if md_path.exists():
            # write 步偶尔会落一个空 md（LLM 返回空），别让它把整轮流水线带崩
            lines = md_path.read_text(encoding="utf-8").splitlines()
            first = lines[0] if lines else ""
            if first.startswith("# "):
                title = first[2:].strip()
        out.append({
            "title": title[:64],
            "author": "AI 晨报",
            "content": html_path.read_text(encoding="utf-8"),
            "digest": (meta.get("stories", [{}])[0].get("summary", "") or title)[:120],
            "content_source_url": "",
            # thumb_media_id 必填——先留空，等 media.py 接好后填
            "thumb_media_id": "",
            "need_open_comment": 1,
        })
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    date = args.date or today_str()

    articles = build_articles(date)
    if not articles:
        print("no articles to publish")
        return
    print(f"prepared {len(articles)} articles for {date}")

    if SKIP_PUBLISH:
        print("WECHAT_SKIP_PUBLISH=1，跳过实际推送（dry run）")
        for a in articles:
            print(f"  · {a['title']} ({len(a['content'])} chars)")
        return

    token = get_access_token()
    media_id = add_draft(token, articles)
    print(f"draft created: media_id={media_id}")
    print("→ 去公众号后台「草稿箱」预览并点发布")


if __name__ == "__main__":
    main()
