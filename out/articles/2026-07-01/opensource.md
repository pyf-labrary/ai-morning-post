# 开源工具双响：渗透测试与视频录制

今日最值得关注的是 VulnClaw 开源——一款基于 AI Agent 和 MCP 的渗透测试 CLI，自然语言即可驱动漏洞发现。与此同时，shot-scraper 1.10 新增 Agent 视频录制功能，让测试过程可回放、可审计。这两个 6/10 重要性的事件，代表开源生态正加速将 AI Agent 落地到安全与开发运维的垂直场景中。

## shot-scraper 1.10：Agent 录屏功能正式上线

shot-scraper 是一款命令行截图工具，新版本引入视频录制能力。关键点在于：Agent 在执行自动化任务时，可以自动录下完整屏幕操作过程，生成 mp4 文件。这对调试、演示和审计都非常有用——开发者无需额外搭建录屏流水线，直接在 CI/CD 中就能获得 Agent 的行为录像。为什么重要：随着 Agent 自主性增强，可观察性成为瓶颈，shot-scraper 用极简方式解决了「Agent 到底干了什么」的问题，是 Agent 工作流基础设施的补全。

> 原文：[GitHub Release](https://github.com/simonw/shot-scraper/releases/tag/1.10)

## VulnClaw：AI Agent 驱动的渗透测试 CLI

VulnClaw 是一个结合 LLM Agent 和 MCP（Model Context Protocol）工具链的开源渗透测试工具。关键点：用户只需输入自然语言指令（如“扫描这个 IP 的常见 Web 漏洞”），Agent 会自动调用 nmap、sqlmap、dirb 等底层工具，组合攻击路径并输出发现。为什么重要：传统渗透测试门槛高，需要手动串联多个工具；VulnClaw 让非安全专家也能发起结构化漏洞扫描，但同时也带来滥用风险。对于安全团队，这是效率提升，对于红蓝对抗，则是新的自动化维度。

> 原文：[GitHub](https://github.com/Unclecheng-li/VulnClaw)

## Crawl4AI：专为 LLM 优化的网页爬虫

Crawl4AI 是一个开源爬虫，针对大语言模型的数据需求做专门优化。关键点：它能在一次请求中抽取结构化内容（Markdown / JSON），自动剔除广告、导航等噪音，并支持 JS 渲染。为什么重要：LLM 应用需要干净、及时的网页数据做 RAG 或微调，但通用爬虫往往产出冗余。Crawl4AI 填补了“爬虫 → 可用语料”之间的转换层，预计会成为 AI 数据管线的常用组件。

> 原文：[GitHub](https://github.com/unclecode/crawl4ai)

## video-use：用编码 Agent 自动化视频编辑

Browser-use 团队推出的视频编辑 Agent 工具。关键点：用户以自然语言描述剪辑需求（如“截取前 5 秒，加上字幕”），Agent 自动生成 Python 代码调用 ffmpeg 等后端执行。为什么重要：视频编辑长期被 GUI 工具主导，video-use 将 AI Agent 引入编辑流程，代码生成 + 可复现工作流，适合批量处理、模板化生产。对媒体行业的技术团队，这是低门槛的视频自动化方案。

> 原文：[GitHub](https://github.com/browser-use/video-use)

## Google OpenRL：自托管 LLM 后训练 API

Google 开源的 OpenRL 项目，提供一套强化学习后训练（RLHF / RLHF-like）的 API，支持在自托管环境运行。关键点：它实现了 Reward Model 训练、PPO 优化等核心流程，兼容 Hugging Face 模型格式。为什么重要：此前大模型后训练主要依赖几家云厂商的闭源服务，OpenRL 允许团队在自有 GPU 上完成对齐微调，降低了 RL 后训练的门槛，对关注数据安全的中型企业尤其有吸引力。

> 原文：[InfoQ](https://www.infoq.cn/article/d5MOPSyGi5XPi1erhUW3)

当 Agent 学会了录屏、渗透测试和剪辑视频，下一步它会接管你的工作吗？你会用这些开源工具做第一个实验吗？