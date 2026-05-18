# 开源晨报：Files.md 登顶，代理工具省98% Token

今日开源社区最值得关注的是笔记工具 Files.md 在 HackerNews 上获得近 500 赞，被视为 Obsidian 的开源替代方案；与此同时，专为 AI 代理设计的代码搜索工具 Semble 宣称相比 grep 节省 98% Token 消耗。这两个项目分别指向个人知识管理和 AI 基础设施两大赛道，开源社区正在快速回应开发者对可控、低成本工具的刚需。

## Files.md 开源笔记工具登顶 HN，受称 Obsidian 替代品

**是什么**：Files.md 是一个纯文本笔记管理工具，基于文件系统运作，支持 Markdown 语法，开源在 GitHub。项目在 HackerNews 上获得约 500 个点赞，社区反响热烈。

**关键点**：Files.md 强调“文件即笔记”，不依赖私有数据库，与 Obsidian 的设计哲学相似，但完全开源且可自托管。其核心功能包括文件夹管理、全文搜索、标签系统和插件机制。

**为什么重要**：Obsidian 虽广受欢迎，但其核心闭源，部分用户担心长期锁定。Files.md 提供了一个可自由定制、隐私可控的替代选项，反映了开发者对开源笔记工具的持续需求。

> 原文：[GitHub - zakirullin/files.md](https://github.com/zakirullin/files.md)

## Semble：让 AI 代理代码搜索节省 98% Token

**是什么**：Semble 是一个专门为 AI 代理设计的代码搜索工具，能够显著降低搜索时的 Token 消耗，对比传统 grep 方法减少约 98% 的 API 使用成本。

**关键点**：Semble 通过索引和智能片段提取，只向 LLM 传递最相关的代码上下文，而非整个文件。它支持多种语言，可直接集成到 agentic 工作流中。

**为什么重要**：Token 成本是 AI 代理规模化使用的核心瓶颈之一。Semble 如果效果如所述，将大幅降低代理在代码理解场景下的运行费用，对 MCP 协议生态是一个有力的补充。

> 原文：[GitHub - MinishLab/semble](https://github.com/MinishLab/semble)

## OpenHuman：开源个人 AI 超级智能助手

**是什么**：OpenHuman 是一个完全本地运行的 AI 助手，支持聊天、检索增强生成（RAG）、语音交互等功能，旨在替代云端个人助手。

**关键点**：所有数据处理在本地完成，不依赖外部 API。内置语音模型、文本转语音和本地向量数据库，用户可下载并离线使用。

**为什么重要**：在隐私法规日益严格的环境下，本地 AI 助手是企业和个人用户的务实选择。OpenHuman 简化了部署步骤，但性能受硬件限制，适合边缘设备场景。

> 原文：[GitHub - tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)

## CLI-Anything：为所有软件添加 Agent 原生接口

**是什么**：香港大学团队开源的 CLI-Anything，通过命令行接口让任意软件可被 AI 代理直接操控，无需修改目标软件代码。

**关键点**：CLI-Anything 利用操作系统的进程通信机制，将图形界面应用的交互抽象成标准化 CLI 命令。代理只需执行命令，即可完成点击、输入等操作。

**为什么重要**：当前许多工具缺乏 API，AI 代理难以自动操作。该项目提供了一种“万能适配器”，有望加速代理在桌面自动化和测试领域的落地。

> 原文：[GitHub - HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

## Anthropic 开源 Agent Skills 标准仓库

**是什么**：Anthropic 发布了一个名为 Agent Skills 的公共 GitHub 仓库，提供可验证的技能注册系统，允许开发者为 Claude Code 等代理注册标准化的技能模块。

**关键点**：每个技能包含元数据、验证用例和实现代码。仓库的目标是建立跨代理的技能互操作性规范，开发者可贡献或复用技能。

**为什么重要**：当前各代理框架的技能定义碎片化严重。Anthropic 作为头部厂商推动标准，可能影响行业方向，减少重复开发，但也需警惕锁定效应。

> 原文：[GitHub - anthropics/skills](https://github.com/anthropics/skills)

## Agent-S 开源框架让 AI 像人类一样操作电脑

**是什么**：开源的 Agent-S 框架模拟人类操作电脑，支持点击、拖拽、键盘输入等自动化任务，基于视觉观察和动作规划。

**关键点**：Agent-S 通过截图获取屏幕信息，利用视觉语言模型解析元素位置，再执行低级别动作。支持跨平台（Windows/macOS/Linux）。

**为什么重要**：与 CLI-Anything 互补，Agent-S 面向图形界面操作，适合复杂网页或桌面软件自动化。但依赖视觉模型推理，实时性和准确性是挑战。

> 原文：[GitHub - simular-ai/Agent-S](https://github.com/simular-ai/Agent-S)

## 微软开源 12 课时 AI Agent 入门课程

**是什么**：微软在 GitHub 上发布《AI Agents for Beginners》课程，包含 12 个课时，从基础概念到实践项目，面向初学者系统教学。

**关键点**：课程内容覆盖代理架构、工具调用、记忆系统、多代理协作等主题，配有代码示例和 Jupyter Notebook。所有材料以 MIT 协议开源。

**为什么重要**：大厂体系化的入门课程能有效降低学习门槛，吸引更多开发者进入代理开发领域。虽然深度有限，但作为起点很扎实。

> 原文：[GitHub - microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)

## Langflow 低代码 AI Agent 构建平台更新

**是什么**：Langflow 是一个低代码平台，用于快速构建和部署 AI 代理及工作流。近日有版本更新，增强了节点库和部署能力。

**关键点**：Langflow 提供拖拽式界面，支持连接 LLM、向量数据库、函数调用等组件。更新后支持自定义节点和云部署。

**为什么重要**：低代码工具使非工程师也能搭建代理原型，加速业务验证。但可扩展性和自由度不及代码框架，适合快速探索场景。

> 原文：[GitHub - langflow-ai/langflow](https://github.com/langflow-ai/langflow)

---

当代理工具开始从“能用”转向“好用”，开源社区的创新密度正在急剧提升——你准备好选择哪个生态了吗？