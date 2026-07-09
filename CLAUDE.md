# ai-morning-post · 常用命令

> 本文件由 `~/claw/CLAUDE.md` 拆出（2026-07-09 doctor 迁移，原文件全局常驻改为按需加载）。跨项目背景/子项目地图/契约见根 [`../CLAUDE.md`](../CLAUDE.md)。

```bash
cd ~/claw/ai-morning-post
python run_daily.py     # 跑全 8 步流水线（fetch → curate → media → write → render → preview → publish → publish_marginalia）
```

GH Actions cron 每天 06:00 CST 跑同一脚本。需要的环境变量：`ANTHROPIC_API_KEY`、`WECHAT_APPID/SECRET`、可选 `TWITTERAPI_IO_KEY`、`IMAGE_API_KEY`。
