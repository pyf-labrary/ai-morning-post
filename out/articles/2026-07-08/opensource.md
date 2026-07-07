# sqlite-utils 4.0 发布，数据库迁移功能来了

今日开源圈最值得关注的是 sqlite-utils 4.0 正式拥抱 schema 迁移，这意味着轻量级 SQLite 工具链补齐了最后一个工程短板。同时在机器人学习、Agent 技能库、向量数据库等方向也有多项新作值得关注——开源工具正从“能用”向“生产级”加速进化。

## sqlite-utils 4.0：轻量数据库迎来正式迁移支持

Simon Willison 发布 sqlite-utils 4.0 稳定版，首次原生支持数据库 schema 迁移。新版本允许开发者用声明式方式定义表结构的变化（如新增列、修改索引），并自动生成迁移脚本。同时推出兼容库 sqlite-migrate，让旧版本 sqlite-utils 用户也能平滑过渡。对于经常用 SQLite 做原型或轻量存储的开发者来说，这消除了手动维护 schema 变更的痛点，使 sqlite-utils 更接近生产级工具。

> 原文：[https://simonwillison.net/2026/Jul/7/sqlite-utils-4/](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/)

## Hugging Face 与 NVIDIA 联合发布 LeRobot v0.6.0

机器人学习框架 LeRobot 迎来大版本更新，新增 Imagine（仿真想象）、Evaluate（评估）、Improve（改进）三大模块，形成“想象–评估–改进”闭环。同时获得 NVIDIA 的新模型与框架集成，支持更高效的机器人操作策略训练。对于从事具身智能或机器人仿真的团队，LeRobot 正逐渐成为 ROS 之外的一个轻量级替代方案。

> 原文：[https://huggingface.co/blog/lerobot-release-v060](https://huggingface.co/blog/lerobot-release-v060)

## AI Agent Skills 仓库集中涌现，生态爆发

多个高质量的 Agent Skills 仓库在 GitHub 流行，覆盖 Claude Code、Codex 等主流代理工具。这些仓库提供生产级的工程技能——包括代码审查、自动调试、任务规划等——使开发者能快速为 agent 注入专业能力。例如 addyosmani/agent-skills 提供了数百个可复用的技能函数。虽然单个仓库可能只是阶段性整理，但集中涌现的趋势表明：Agent 的能力边界正从“通用对话”转向“专业工具链”。

> 原文：[https://github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

## 阿里开源轻量级向量数据库 zvec

zvec 是阿里开源的内存向量数据库，核心卖点：极快、进程内运行，无需独立部署。它专为 AI 嵌入检索场景设计，支持近似最近邻搜索，内存 footprint 极低。对于需要将向量检索嵌入现有 Python 应用（如 RAG、推荐系统）的团队，zvec 提供了一个零依赖的轻量选项，适合原型和小规模生产。

> 原文：[https://github.com/alibaba/zvec](https://github.com/alibaba/zvec)

## Google 开源 Antigravity Python SDK

Google 发布 Antigravity SDK 的 Python 版本，用于构建基于 Antigravity 和 Gemini 的 AI 代理。Antigravity 是 Google 的分布式代理运行时，允许 agent 在异构环境（边缘、云端）中调度。Python SDK 让开发者能用熟悉的语法定义 agent 行为、集成 Gemini 模型能力。虽然目前仍属早期，但作为 Google 在 agent 基础设施方向的一次开源，值得关注。

> 原文：[https://github.com/google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python)

## 开源爬虫框架 Firecrawl 持续更新

Firecrawl 提供稳定 API，支持大规模搜索、爬取和与网页交互，专为 AI 数据采集设计。最近更新包括更智能的 JS 渲染处理、结构化输出格式优化等。对于需要从网页抽取新鲜数据以喂给 LLM 的团队，Firecrawl 比传统的 Scrapy 更“开箱即用”，无需处理复杂反爬与动态内容。

> 原文：[https://github.com/firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)

## 自托管书签管理工具 Karakeep 支持 AI 标签

Karakeep 是一款可自托管的书签管理工具，支持链接、笔记和图片收藏。新版本引入 AI 自动标签和全文搜索，能基于内容语义为书签打上分类标签，无需手动整理。对于自建知识库或隐私敏感的用户，这是一个不错的 Pinboard 替代品。

> 原文：[https://github.com/karakeep-app/karakeep](https://github.com/karakeep-app/karakeep)

## TradingAgents：多智能体金融交易框架开源

Tauric Research 开源 TradingAgents，基于 LLM 的多智能体框架，用于金融交易策略研究。它支持多个 agent 协作：一个负责市场分析，一个负责风险控制，一个负责执行决策等。虽然金融量化领域已有许多自动化框架，但基于 LLM agent 的协作模式为策略开发提供了新的交互范式。

> 原文：[https://github.com/TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

---

数据库迁移、机器人学习、Agent 技能库、向量数据库、金融 agent——开源工具正从基础组件向垂直智能体演进。你更关注哪个方向？