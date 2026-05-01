"""配图：抓 OG 图 + 写回 curated.json。

设计：
- enrich_curated() 遍历 curated.json 每个 story，抓取 primary_url 的 og:image，
  存到 out/media/{date}/{section_id}-{idx}.{ext}，把相对路径写回 story.cover_path
- 失败的 story 不阻塞流程
- 文生图（用于无图源的 story 或封面）留 TODO
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

from .common import ARTICLES_DIR, MEDIA_DIR, ROOT, today_str

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
MIN_BYTES = 4 * 1024  # 小于 4KB 的多半是占位/icon


def fetch_og_image(url: str, save_dir: Path, slug: str) -> Path | None:
    try:
        r = httpx.get(url, follow_redirects=True, timeout=20, headers={"User-Agent": UA})
        r.raise_for_status()
    except Exception as e:
        print(f"  ✗ {url} → fetch html failed: {e}")
        return None
    soup = BeautifulSoup(r.text, "lxml")
    candidates = []
    for sel in [
        ("meta", {"property": "og:image"}),
        ("meta", {"property": "og:image:secure_url"}),
        ("meta", {"name": "twitter:image"}),
        ("meta", {"name": "twitter:image:src"}),
    ]:
        tag = soup.find(*sel) if isinstance(sel, tuple) and len(sel) == 2 else None
        if tag and tag.get("content"):
            candidates.append(tag["content"])
    # arxiv 没有 og:image，用 thumbnail link
    if not candidates and "arxiv.org" in url:
        # arxiv 论文可以用第一页 PDF 截图，但太重；先跳过
        return None
    if not candidates:
        return None

    img_url = candidates[0]
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    elif img_url.startswith("/"):
        from urllib.parse import urlparse
        p = urlparse(url)
        img_url = f"{p.scheme}://{p.netloc}{img_url}"

    try:
        ir = httpx.get(img_url, timeout=30, follow_redirects=True, headers={"User-Agent": UA})
        ir.raise_for_status()
    except Exception as e:
        print(f"  ✗ {img_url} → download failed: {e}")
        return None

    if len(ir.content) < MIN_BYTES:
        print(f"  ✗ {img_url} → too small ({len(ir.content)}B)")
        return None

    save_dir.mkdir(parents=True, exist_ok=True)
    path = save_dir / f"{slug}.jpg"
    try:
        img = Image.open(BytesIO(ir.content))
        if img.mode in ("RGBA", "LA", "P"):
            bg = Image.new("RGB", img.size, "white")
            bg.paste(img, mask=img.convert("RGBA").split()[-1] if img.mode != "P" else None)
            img = bg
        elif img.mode != "RGB":
            img = img.convert("RGB")
        # 缩放到最大宽度 1080（微信公众号建议宽度）
        if img.width > 1080:
            ratio = 1080 / img.width
            img = img.resize((1080, int(img.height * ratio)), Image.LANCZOS)
        img.save(path, "JPEG", quality=82, optimize=True)
    except Exception as e:
        print(f"  ✗ {img_url} → image decode failed: {e}")
        return None
    print(f"  ✓ {url[:60]} → {path.name} ({path.stat().st_size // 1024}KB)")
    return path


def enrich_curated(date: str | None = None) -> Path:
    date = date or today_str()
    curated_path = ARTICLES_DIR / f"{date}.curated.json"
    if not curated_path.exists():
        raise SystemExit(f"missing {curated_path}; run curate first")
    data = json.loads(curated_path.read_text(encoding="utf-8"))

    media_dir = MEDIA_DIR / date
    total, hits = 0, 0
    for section in data.get("sections", []):
        sid = section["id"]
        for idx, story in enumerate(section.get("stories", [])):
            url = story.get("primary_url")
            if not url:
                continue
            total += 1
            slug = f"{sid}-{idx:02d}"
            path = fetch_og_image(url, media_dir, slug)
            if path:
                # 用相对项目根的路径，render 阶段再处理
                story["cover_path"] = str(path.relative_to(ROOT))
                hits += 1

    curated_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"media: {hits}/{total} stories got cover images")
    return curated_path


def generate_cover(prompt: str, section_id: str) -> Path | None:
    """文生图占位。接入 fal.ai / Replicate 后实现。"""
    print(f"[media] TODO generate cover for {section_id}: {prompt[:80]}")
    return None


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--date")
    args = p.parse_args()
    enrich_curated(args.date)


if __name__ == "__main__":
    main()
