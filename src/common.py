"""共享工具：素材数据结构 + 持久化 + 去重。"""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "out" / "raw"
ARTICLES_DIR = ROOT / "out" / "articles"
MEDIA_DIR = ROOT / "out" / "media"
CONFIG_DIR = ROOT / "config"

CST = timezone(timedelta(hours=8))


@dataclass
class Item:
    """一条原始素材。"""
    source: str           # e.g. "OpenAI" / "reddit:LocalLLaMA"
    source_type: str      # rss / arxiv / reddit / hn / x / ph
    title: str
    url: str
    summary: str = ""
    published: str = ""   # ISO8601
    author: str = ""
    score: float = 0.0    # 原始热度（reddit upvotes / hn points / arxiv 0）
    weight: float = 1.0   # 来源权重
    extra: dict = field(default_factory=dict)

    @property
    def fingerprint(self) -> str:
        # 用规范化 URL + 标题前 80 字 做指纹
        u = re.sub(r"[?#].*$", "", self.url.lower().rstrip("/"))
        t = re.sub(r"\s+", " ", self.title.lower()).strip()[:80]
        return hashlib.sha1(f"{u}|{t}".encode()).hexdigest()[:16]


def today_str() -> str:
    return datetime.now(CST).strftime("%Y-%m-%d")


def yesterday_str() -> str:
    return (datetime.now(CST) - timedelta(days=1)).strftime("%Y-%m-%d")


def within_24h(iso: str) -> bool:
    if not iso:
        return True  # 没有时间信息的保留，让 LLM 判断
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return True
    return datetime.now(timezone.utc) - dt <= timedelta(hours=36)


def dedupe(items: Iterable[Item]) -> list[Item]:
    seen: dict[str, Item] = {}
    for it in items:
        fp = it.fingerprint
        if fp not in seen or it.score > seen[fp].score:
            seen[fp] = it
    return list(seen.values())


def save_raw(items: list[Item], date: str | None = None) -> Path:
    date = date or today_str()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / f"{date}.json"
    path.write_text(
        json.dumps([asdict(it) for it in items], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def load_raw(date: str | None = None) -> list[Item]:
    date = date or today_str()
    path = RAW_DIR / f"{date}.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [Item(**d) for d in data]
