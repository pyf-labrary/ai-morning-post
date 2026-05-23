# 开源工具爆发：Claude Code目录、Chrome DevTools MCP、微软Agent治理

今天开源社区围绕 AI 代理（Agent）工具链集中发力：Anthropic 官方上架了 Claude Code 插件目录，Chrome 团队开源了 DevTools 的 Model Context Protocol 服务，微软则拿出了覆盖 OWASP Top 10 的 Agent 治理工具包。三件事指向同一个信号：代理生态正在从“能跑”走向“能用且可控”。

## Anthropic官方Claude Code插件目录上线GitHub

Anthropic 在 GitHub 上建立了 `claude-plugins-official` 仓库，作为官方管理的 Claude Code 插件事务目录。开发者可以在此发现、提交和审核高质量插件，类似于 VS Code 的扩展市场，但更侧重 agentic 工作流（如数据访问、代码操作）。

关键点在于：这是 Anthropic 首次为 Claude 的插件生态提供官方排序与质量背书，而非任由第三方分散发布。对于企业用户，这意味着代理功能的可信度与可维护性大幅提升；对于插件开发者，则有了明确的曝光渠道和合规标准。

> 原文：[https://github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

## Chrome DevTools MCP开源：为编码代理提供浏览器调试能力

Chrome 团队发布了 `chrome-devtools-mcp`，一个基于 Model Context Protocol (MCP) 的服务，允许 AI 编码代理直接连接并控制 Chrome DevTools。这意味着代理可以像人类开发者一样执行 DOM 检查、网络面板分析、性能审计等操作，而不仅仅是输出文本代码。

重要性在于：此前编码代理缺乏对真实浏览器运行环境的细粒度操控能力。MCP 接口标准化了代理与调试工具的交互，让自动化测试、UI 修复、性能优化等任务具备了闭环可行性。这是 AI 开发工具从“生成代码”向“操作运行环境”迈出的关键一步。

> 原文：[https://github.com/ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

## 微软开源AI Agent治理工具包，覆盖OWASP Top 10

微软的 `agent-governance-toolkit` 提供了一个策略引擎，围绕 OWASP Top 10 安全风险为 AI 代理提供执行控制。核心能力包括：零信任身份认证、沙箱执行、输入/输出过滤、审计日志等。

为什么重要？当前大多数代理框架（如 LangChain、AutoGPT）侧重能力扩展，而缺乏内建的安全护栏。微软此举直接将企业级安全标准引入代理开发，降低了 AI 代理上生产线的合规成本。对于 CTO 和安全团队，这是一个“拿来即用”的治理层参考实现。

> 原文：[https://github.com/microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)

## Meta开源SAM 3：下一代图像分割模型

Meta 发布了 `sam3`，相比 SAM 2，在分割精度、多尺度目标识别和预训练权重泛化能力上均有提升。模型依旧以 ViT 为骨干，但训练数据量和训练策略有所升级，支持更细粒度的 mask 输出。

对于计算机视觉工程师，SAM 3 延续了“一键分割”的便利性，同时显著降低了在长尾物体和密集场景下的失效概率。开源权重意味着可以直接用于微调或集成到现有分割流水线中，而无需重新训练全量模型。

> 原文：[https://github.com/facebookresearch/sam3](https://github.com/facebookresearch/sam3)

## NousResearch开源Hermes Agent：可成长的AI代理

`hermes-agent` 是一个基于 NousResearch 的 Hermes 模型的代理框架，强调“成长性”：支持插件动态加载、长期记忆持久化、自定义工具调用以及多轮对话中的上下文扩展。

设计上，Hermes Agent 并非提供一个固定功能的代理，而是一个可扩展的代理基础架构，类似一个 AI 代理操作系统。对于想快速搭建专属代理（如客服、代码助手）的团队，提供了一个比 langchain 更轻量、更聚焦的起点。

> 原文：[https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

## 腾讯开源TencentDB Agent Memory：4层本地记忆流水线

TencentDB Agent Memory 是一个完全在本地运行的 AI 代理记忆系统，包含四层结构：符号短时记忆、任务画布、长期存储索引和语义检索。灵感来自认知架构，但针对数据库场景优化。

对于隐私敏感的应用（如金融、医疗），本地记忆意味着数据不离开设备；四层流水线则让代理既能记住短期会话状态，又能跨 session 调用历史知识。它可作为 RAG 系统的记忆层替代方案，尤其适合本地部署的 agent。

> 原文：[https://www.marktechpost.com/2026/05/23/tencent-open-sources-tencentdb-agent-memory-a-4-tier-local-memory-pipeline-for-ai-agents/](https://www.marktechpost.com/2026/05/23/tencent-open-sources-tencentdb-agent-memory-a-4-tier-local-memory-pipeline-for-ai-agents/)

## Perplexity开源Bumblebee：只读的供应链安全检查工具

Bumblebee 是 Perplexity 内部使用的开发者端点库存扫描器，现已开源。它以只读方式扫描组织内所有暴露的 API 端点、第三方依赖、开发环境，识别潜在供应链攻击面。

扫射面是“只读”，意味着无需在目标系统安装 agent，仅通过公开信息和元数据即可生成风险清单。对于 DevSecOps 团队，这是一个零部署成本的快速初始审计工具，特别适合云原生和多微服务架构。

> 原文：[https://www.marktechpost.com/2026/05/23/perplexity-open-sources-bumblebee-a-read-only-supply-chain-scanner-for-developer-endpoints/](https://www.marktechpost.com/2026/05/23/perplexity-open-sources-bumblebee-a-read-only-supply-chain-scanner-for-developer-endpoints/)

## Models.dev：开源AI模型规格与定价数据库

`models.dev` 是一个开源数据库，收录了数百个 AI 模型的技术规格（参数量、上下文长度、推理速度）、定价（API 调用价格、硬件成本）和能力分类（文本、图像、多模态）。开发者可以通过 API 或 CLI 查询，便于做模型选型对比。

在模型爆发、定价不透明的当下，这类结构化数据工具是工程团队的“刚需”。它把分散在 Hugging Face、各大厂商定价页上的信息统一化，减少了选型时的调研成本。注意目前依赖于社区贡献，数据完整性和时效性需关注。

> 原文：[https://github.com/anomalyco/models.dev](https://github.com/anomalyco/models.dev)

今天开源社区的共同主题是“代理生态的基础设施化”——从官方目录、浏览器调试、安全治理到记忆系统，每个项目都在解决代理走向生产环境的某个短板。当工具链逐渐成熟，留给开发者的核心问题不再是“能否造出代理”，而是“如何让代理可信、可控且可维护”。