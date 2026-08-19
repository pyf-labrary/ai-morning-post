# ai-morning-post · 常用命令

> 本文件由 `~/claw/CLAUDE.md` 拆出（2026-07-09 doctor 迁移，原文件全局常驻改为按需加载）。跨项目背景/子项目地图/契约见根 [`../CLAUDE.md`](../CLAUDE.md)。

```bash
cd ~/claw/ai-morning-post
python run_daily.py                          # 跑全 8 步流水线（fetch → curate → media → write → render → preview → publish → publish_marginalia）
python run_daily.py --date D --backfill      # 回溯补录某一天（只有 HN/arXiv 能回溯，rss/reddit/x 自动跳过）

# 补录多天走 CI（逐日跑、各自 commit、最后统一 push 一次）
gh workflow run "AI Morning Post · daily" -f dates="2026-08-12,2026-08-13"
```

排查失败：`gh api repos/pyf-labrary/ai-morning-post/actions/jobs/<jobid>/logs`
（`gh run view --log-failed` 在这个仓返回空）。**run 红 ≠ 站点没内容**——第 8 步微信
dry-run 在站点发布之后，先看 marginalia `origin/main` 有没有当天 post。
详见 `~/claw/docs/SESSION-2026-08-19-ai-morning-post-fix-and-backfill.md`。

GH Actions cron 每天 06:00 CST 跑同一脚本。需要的环境变量：`ANTHROPIC_API_KEY`、`WECHAT_APPID/SECRET`、可选 `TWITTERAPI_IO_KEY`、`IMAGE_API_KEY`。
