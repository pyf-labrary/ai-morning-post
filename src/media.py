"""配图：优先抓原文 OG 图，缺则后续接图像生成 API。

第一版只实现 OG 图抓取 + 本地缓存。文生图留 TODO，等接入再加（候选：fal.ai Flux / Replicate / OpenAI Images）。
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

from .common import MEDIA_DIR, today_str


def fetch_og_image(url: str) -> Path | None:
    try:
        r = httpx.get(url, follow_redirects=True, timeout=20,
                      headers={"User-Agent": "Mozilla/5.0 ai-morning-post"})
        r.raise_for_status()
    except Exception as e:
        print(f"[media] fetch {url} failed: {e}")
        return None
    soup = BeautifulSoup(r.text, "lxml")
    og = (soup.find("meta", property="og:image")
          or soup.find("meta", attrs={"name": "twitter:image"}))
    if not og or not og.get("content"):
        return None
    img_url = og["content"]
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    try:
        ir = httpx.get(img_url, timeout=30, follow_redirects=True)
        ir.raise_for_status()
    except Exception as e:
        print(f"[media] fetch image {img_url} failed: {e}")
        return None
    ext = re.search(r"\.(png|jpe?g|webp|gif)(?:$|\?)", img_url, re.I)
    suffix = "." + (ext.group(1).lower() if ext else "jpg")
    h = hashlib.sha1(img_url.encode()).hexdigest()[:12]
    out_dir = MEDIA_DIR / today_str()
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{h}{suffix}"
    path.write_bytes(ir.content)
    return path


def generate_cover(prompt: str, section_id: str) -> Path | None:
    """文生图占位。接入后改成调 fal.ai / Replicate / OpenAI 即可。"""
    print(f"[media] TODO generate cover for {section_id}: {prompt[:80]}")
    return None
