# AI代理的“观看-重复”时代开启

OpenAI Codex 今天升级了“观看-重复”功能，这意味着 AI 不再需要指令描述，只需看一次操作即可自动执行。这可能是 AI 自动化从“对话式”走向“演示式”的转折点。与此同时，Cloudflare 与 AWS 分别从安全访问和业务上下文两个角度为 AI 代理铺路，企业落地正在加速。

## OpenAI Codex 学会“看一次，重复一辈子”

OpenAI 发布了 Codex 的重大更新：新增“观看-重复”功能。它不再依赖用户用自然语言描述操作流程，而是直接记录用户在一次操作中的鼠标点击、按键和界面交互，然后自主复现该流程。关键点在于：Codex 能理解操作背后的意图，而非简单记录宏。例如一个复杂的报表生成流程，用户只需演示一遍，Codex 就可以每天自动执行。为什么重要？这大幅降低了自动化门槛——企业里大量“知道怎么做但说不清楚”的任务，现在可以直接交给 AI 学习并反复执行，可能催生新一代流程自动化工具。

> 原文：[The Decoder - OpenAI's Codex can now watch you work once and repeat the task forever](https://the-decoder.com/openais-codex-can-now-watch-you-work-once-and-repeat-the-task-forever/)

## Cloudflare 推出 AI 代理临时账户，解决安全访问痛点

Cloudflare 发布了临时账户服务，专为 AI 代理设计。传统上，AI 代理访问系统需要长期有效的凭证，带来严重安全风险。临时账户允许代理在运行期间生成一次性凭证，任务结束后自动撤销，且仅开放最小必要权限。为什么重要？这是在基础设施层解决 AI 代理安全问题的关键拼图——企业不敢让 AI 代理触碰核心系统，核心原因就是“怕它乱动”。临时账户让“放开手”变得可控。

> 原文：[Cloudflare Blog - Temporary Accounts](https://blog.cloudflare.com/temporary-accounts/)

## AWS 推出两项新服务，为 AI 代理补齐业务上下文与安全

AWS 今天发布两项服务，直指 AI 代理在企业落地时的两大障碍：缺乏业务上下文和安全保障。第一项服务能让代理理解企业内部的业务规则、数据模型和流程逻辑；第二项则提供细粒度的权限管理和审计能力。为什么重要？AWS 正试图证明 AI 代理不仅是玩票工具，而是能真正融入企业生产环境的“员工”。这两项服务如果落地成功，将显著提升企业对 AI 代理的信任度，加速从 POC 到生产的转换。

> 原文：[The Decoder - AWS says AI agents lack business context and security, launches two services to patch the gaps](https://the-decoder.com/aws-says-ai-agents-lack-business-context-and-security-launches-two-services-to-patch-the-gaps/)

## iOS 27 带来一系列实用 AI 功能，不止 Siri 升级

苹果在 iOS 27 中放入了大量“看不见但用得到”的 AI 能力。例如：相册内自动识别并整理重复文件，邮件中智能提取日程并生成日历邀请，输入法新增语境感知的自动纠错等。关键点：这些功能不标榜“AI”，也不叫 Siri，而是内嵌在系统级交互中让用户无感知地受益。为什么重要？苹果一贯的策略是“AI 即体验”，而非“AI 即聊天”。这可能会带动普通用户对 AI 的接受度，并为苹果后续的 Agent 生态打下基础。

> 原文：[TechCrunch - Beyond Siri: here are the practical AI features coming to your iPhone in iOS 27](https://techcrunch.com/2026/06/21/beyond-siri-here-are-the-practical-ai-features-coming-to-your-iphone-in-ios-27/)

## 微信 AI 助手“小微”小范围灰度上线

微信内原生的 AI 助手“小微”开始灰度测试。用户可以通过文字或语音直接调用微信功能（如发消息、建群、搜朋友圈）以及拉起第三方小程序。关键点：这是微信首次将 AI 助手内置到聊天界面中，而不是作为一个独立入口。为什么重要？微信拥有 10 亿级用户和丰富的小程序生态，一旦“小微”全面放开，可能成为国内最大的 AI Agent 入口。不过目前仅灰度，具体能力和流畅度尚需观察。

> 原文：[36Kr - 微信AI助手“小微”小范围灰度上线](https://36kr.com/newsflashes/3862458180359424?f=rss)

## In the Weights 推出 AI 虚荣搜索：查你的 AI 影响力分数

一个新工具 In the Weights 允许用户查询自己的“AI 影响力”分数——类似谷歌的 PageRank 但专门针对 AI 模型训练数据中的被引用情况。它统计你的名字、作品或公司在主流 AI 数据集（如 C4、LAION）中出现频率。为什么重要？对技术从业者和开发者来说，这是社交资本的新度量，类似“你会被 AI 记住吗？”的虚荣搜索。但该工具的数据源和算法不透明，娱乐性大于实用性。

> 原文：[TechCrunch - In the Weights is your new AI-centric vanity search](https://techcrunch.com/2026/06/20/in-the-weights-is-your-new-ai-centric-vanity-search/)

## Cloudback MCP Server：从 Claude 直接管理备份

Cloudback 发布了 MCP（Model Context Protocol）服务器，允许用户通过 Claude、Cursor、VS Code 等 AI 编程助手直接管理数据库和文件系统备份。你可以对 Claude 说“把上周的数据库备份恢复到测试环境”，它就能执行操作。关键点：这是 AI 与基础设施工具融合的又一个小而美的例子，但受众小众，主要是开发者和 SRE。为什么重要？MCP 协议正在扩大 AI 工具的边界，未来更多运维场景可能实现自然语言驱动。

> 原文：[Product Hunt - Cloudback](https://www.producthunt.com/products/cloudback)

## Agent 37 Cloud：为每位客户部署专属 AI 代理

Agent 37 Cloud 发布新服务，允许企业为每个客户创建独立的 AI 代理实例，每个实例可搭载 Hermes 或 OpenClaw 模型，并支持定制知识库与行为规则。为什么重要？这切中了企业服务中的“个性化”需求——传统聊天机器人只能给所有客户相同回答，而 Agent 37 Cloud 能做到“一客一代理”。但目前仍处于早期，实际效果和成本控制有待验证。

> 原文：[Product Hunt - Agent 37](https://www.producthunt.com/products/agent-37-38)

---

当 AI 代理学会观摩你的操作并永久执行，你准备好在哪个环节放手了吗？