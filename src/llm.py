"""LLM 客户端工厂。

通过环境变量切换后端：
  LLM_BASE_URL   默认 https://api.anthropic.com  （留空 = 官方 Anthropic）
  LLM_API_KEY    优先；缺省 fallback 到 ANTHROPIC_API_KEY
  LLM_MODEL      默认 claude-opus-4-7

DeepSeek Anthropic-compat 示例：
  LLM_BASE_URL=https://api.deepseek.com/anthropic
  LLM_API_KEY=sk-xxx
  LLM_MODEL=deepseek-v4-flash

prompt cache_control 只在使用原生 Anthropic 端点时启用；其他端点直接传字符串 system。
"""
from __future__ import annotations

import os

from anthropic import Anthropic

_ANTHROPIC_BASE = "https://api.anthropic.com"

LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", _ANTHROPIC_BASE).rstrip("/")
LLM_API_KEY: str = os.getenv("LLM_API_KEY") or os.getenv("ANTHROPIC_API_KEY") or ""
LLM_MODEL: str = os.getenv("LLM_MODEL", "claude-opus-4-7")
USE_CACHE: bool = (LLM_BASE_URL == _ANTHROPIC_BASE)


def get_client() -> Anthropic:
    kwargs: dict = {"api_key": LLM_API_KEY}
    if LLM_BASE_URL != _ANTHROPIC_BASE:
        kwargs["base_url"] = LLM_BASE_URL
    return Anthropic(**kwargs)


def system_param(prompt: str) -> list | str:
    """原生 Anthropic 返回带 cache_control 的 list；其他端点直接返回字符串。"""
    if USE_CACHE:
        return [{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}]
    return prompt
