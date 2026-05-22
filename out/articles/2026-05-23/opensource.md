# 开源代理工具井喷：Datasette、Claude Code领衔

AI 代理开发正从单点实验走向基础设施搭建。今天开源社区集中发布了 8 个相关项目，覆盖代理的交互界面、技能框架、记忆管理和工具调用优化——这些不是零散的尝试，而是生态正在寻找标准化接口的信号。

## Datasette Agent 发布：可扩展 AI 助手

Simon Willison 正式发布 Datasette Agent，这是一个基于 Datasette 生态构建的 AI 助手，核心能力是通过插件机制扩展其知识库和工具集。关键点：支持 SQL 查询直接与数据库交互，插件可自定义数据源和处理管道。为什么重要：它将 AI 助手从通用聊天转向“可审计、可定制”的数据工作流，适合团队在内部数据上构建安全可控的代理。

> 原文：[Datasette Agent 发布公告](https://datasette.io/blog/2026/datasette-agent/)

## Claude Code 官方插件目录发布

Anthropic 推出了 Claude Code 的官方插件仓库，提供验证过的第三方扩展。关键点：插件涵盖代码审查、CI/CD 集成、文档生成等场景，统一发布在 GitHub 上。为什么重要：这是大型模型厂商首次为代码代理建立标准化插件市场，意味着开发者可以像装 VS Code 扩展一样增强 Claude Code 的能力，生态对复用的需求开始被平台方正式回应。

> 原文：[Anthropic 官方 Claude 插件仓库](https://github.com/anthropics/claude-plugins-official)

## CodeGraph：预索引代码知识图谱减少 Token 消耗

CodeGraph 为 Claude Code 等代理提供本地的代码索引服务，将整个代码库结构化表示为知识图谱。关键点：预索引后，代理调用工具时只需查询图谱而非全文检索，显著降低 token 开销。为什么重要：Token 成本是代理普及的隐性障碍，CodeGraph 证明“本地先验知识”可以成为降低调用成本的标准范式。

> 原文：[CodeGraph GitHub 仓库](https://github.com/colbymchenry/codegraph)

## Superpowers：编码代理的可组合技能框架

Superpowers 是一套完整的软件方法论，用于构建基于可组合技能的编码代理。关键点：它将复杂开发任务拆解为独立技能单元，代理按需组装执行。为什么重要：与之前“端到端 prompt”不同，这套框架强调技能的可复用性和调试性，符合工程化 AI 代理的趋势。

> 原文：[Superpowers GitHub 仓库](https://github.com/obra/superpowers)

## Google ADK 示例：Agent 开发工具包

Google 发布 ADK Samples，提供一系列构建代理应用的参考实现。关键点：包含多轮对话、工具调用、记忆管理等典型场景的代码模板。为什么重要：ADK 是 Google 在 agentic 方向上的核心工具栈，这些示例降低了学习门槛，有利于吸引更多开发者进入其生态。

> 原文：[Google ADK Samples GitHub 仓库](https://github.com/google/adk-samples)

## Hermes Agent：开源可成长代理框架

Nous Research 开源 Hermes Agent，一个持续学习的代理框架。关键点：代理可以在与用户交互过程中自我改进，更新自身知识库和行为策略。为什么重要：“可成长”是当前代理的痛点——静态模型无法适应动态环境，Hermes Agent 提供了开源的增量学习方案。

> 原文：[Hermes Agent GitHub 仓库](https://github.com/NousResearch/hermes-agent)

## OpenViking：面向 AI 代理的上下文数据库

字节跳动开源 OpenViking，为代理统一管理内存、资源和技能。关键点：提供结构化上下文存储，支持将长期记忆与临时对话分离，并内置资源调度。为什么重要：代理的“记忆碎片化”是导致任务失败的常见原因，OpenViking 试图成为代理的专用“操作系统层”。

> 原文：[OpenViking GitHub 仓库](https://github.com/volcengine/OpenViking)

## CLI-Anything：让所有软件原生支持代理

HKUDS 项目 CLI-Anything 将任意桌面应用转化为 CLI 接口，使得 AI 代理可以通过命令调用它们。关键点：无需修改原软件代码，通过自动提取 GUI 元素生成 CLI。为什么重要：它解决了代理无法直接操作现有 GUI 软件的难题，扩展了代理的“肢体”范围。

> 原文：[CLI-Anything GitHub 仓库](https://github.com/HKUDS/CLI-Anything)

---

今天这些项目有一个共同暗示：Agent 开发正在进入“铺水管”阶段——接口标准化、成本优化、记忆管理、技能复用——这些基础设施一旦成熟，真正的 agentic 应用才会井喷。你所在的团队，准备好迁移到这套新工具链了吗？