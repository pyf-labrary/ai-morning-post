# AI Morning Post · AI晨报

每天早上自动汇集前 24 小时全网 AI 新闻，用 Claude 整理成多板块图文，推送到微信公众号草稿箱。

## 流水线

```
GitHub Actions cron (每日 06:00 CST)
  └─ fetch.py    抓取：RSS / arXiv / Reddit / HN / X / Product Hunt
  └─ curate.py   Claude：去重 + 聚类 + 重要性打分 + 板块划分
  └─ write.py    Claude：每板块一篇文章（标题/导语/正文/结语）
  └─ media.py    封面 + 配图（优先 OG 图，缺则文生图）
  └─ render.py   Markdown → 微信 HTML
  └─ publish.py  微信草稿接口（多图文，人工最终点发布）
```

## 板块

模型发布 · 公司动态 · 研究论文 · 应用产品 · 行业观点 · 开源工具

## 配置

复制 `config/sources.example.yaml` 为 `config/sources.yaml`，填入 X 抓取 key、微信 appid/secret。

环境变量：
- `ANTHROPIC_API_KEY`
- `WECHAT_APPID` / `WECHAT_APPSECRET`
- `TWITTERAPI_IO_KEY`（可选，X 抓取用）
- `IMAGE_API_KEY`（可选，配图生成用）

## 状态

- [x] 项目脚手架
- [x] RSS / arXiv / Reddit / HackerNews fetcher
- [ ] X / Product Hunt fetcher
- [ ] curate.py（Claude 聚类）
- [ ] write.py（文章生成）
- [ ] media.py（图像）
- [ ] render.py（微信 HTML）
- [ ] publish.py（微信草稿 API）
- [ ] GitHub Actions workflow
