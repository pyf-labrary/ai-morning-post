# Agent技能标准来了，Anthropic带头

今天开源圈最值得关注的是Anthropic 正式发布 Agent Skills 仓库——一套可扩展的技能规范，让 Claude 的 Agent 能力变成社区共建的标准。这标志着 Agent 开发正从个人 hack 走向工程化协作，技能复用和安全性将成为下一波竞争焦点。

## Anthropic 官方 Agent Skills 仓库：Agent 技能标准化第一步

Anthropic 开源了官方 Agent Skills 实现，为 Claude 提供标准化的技能扩展框架。社区成员可以提交、审核并复用技能，使 Agent 行为可编程、可组合。关键点在于：这是大模型厂商首次将 Agent 技能层作为一种开源协议推出，意味着 Agent 生态的“插件系统”开始成型。对于开发者来说，未来调用 Agent 能力可能像安装 npm 包一样简单。

> 原文：[GitHub - anthropics/skills](https://github.com/anthropics/skills)

## addyosmani 开源生产级 Agent 编码技能集

知名开发者 addyosmani 整理了一套面向 AI 编码 Agent 的生产级工程技能集，目标是提升 Agent 代码质量。与 Anthropic 官方仓库不同，这套技能更偏向代码生成的实际经验，包含错误处理、测试生成、依赖管理等实用模式。对于正在构建代码 Agent 的团队，这是即插即用的最佳实践集合。

> 原文：[GitHub - addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

## Superpowers：可组合的 Agent 开发方法论

Superpowers 提供了一个更抽象的技能框架：它不仅是技能集合，而是一套完整的软件开发方法论，帮助 AI Agent 高效编码。其核心是可组合性——技能可以像积木一样组装，配合结构化工作流。项目作者 Obra 在底层设计上与现有 Agent 框架（如 LangChain）有差异化，强调方法论而非工具绑定。

> 原文：[GitHub - obra/superpowers](https://github.com/obra/superpowers)

## NVIDIA 开源 SkillSpector：给 Agent 技能做安全扫描

NVIDIA 推出 SkillSpector，专门扫描 AI Agent 技能中的安全漏洞和恶意模式。随着技能仓库大量涌现，安全问题日益突出——不安全的技能可能导致 Agent 执行危险操作。SkillSpector 可以集成到 CI/CD 管道中，在部署前自动检查。对于企业级 Agent 落地，这是基础设施级的能力补齐。

> 原文：[GitHub - NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

## browser-use：让 Agent 像人一样操控浏览器

browser-use 项目让 AI Agent 能直接操作浏览器，自动完成填写表单、抓取数据、登录等在线任务。不同于传统的 Selenium 自动化，它基于视觉理解与 DOM 交互的结合，更接近人类操作逻辑。对 RPA 场景和网页自动化需求而言，这可能是自 Playwright 以来最有价值的开源项目之一。

> 原文：[GitHub - browser-use/browser-use](https://github.com/browser-use/browser-use)

## Andrew Ng 开源 aisuite：统一多家 AI 服务接口

aisuite 由 Andrew Ng 团队发布，提供一个轻量级接口来调用 OpenAI、Anthropic、Google 等多家生成式 AI 服务。设计理念类似于数据库的 ORM——开发者只需切换字符串即可更换底层模型，无需重写业务逻辑。在 API 差异化加剧的当下，这个工具能显著降低多模型实验成本。

> 原文：[GitHub - andrewyng/aisuite](https://github.com/andrewyng/aisuite)

## LMCache：号称最快的 KV 缓存层

LMCache 专注于 LLM 推理中的 KV 缓存优化，通过智能缓存策略显著降低延迟、提升吞吐量。在长上下文推理和多轮对话场景中，KV 缓存往往是性能瓶颈。该项目宣称是目前最快的方案，但实际效果需要结合模型和硬件场景测试。对于追求推理效率的团队，值得一试。

> 原文：[GitHub - LMCache/LMCache](https://github.com/LMCache/LMCache)

## agentsview：本地化 Agent 会话追踪，比 cusage 快 100 倍

agentsview 开源项目支持本地浏览、搜索 Claude Code 等多种 Agent 的会话记录，并能追踪成本。它替代了 cusage，性能提升 100 倍，完全本地运行。对于重度使用 Agent 的开发者，这是管理对话历史与费用的实用工具，尤其适合需要审计和调试的场景。

> 原文：[GitHub - kenn-io/agentsview](https://github.com/kenn-io/agentsview)

---

今天开源 Agent 生态的主题是“技能标准化与工程化”。当 Anthropic、NVIDIA 和独立开发者都在围绕技能层发力，你是否已经想好如何管理 Agent 的“大脑插件”？