# Agent Skills 标准化，GitHub 趋势三连击

今日核心看点：三个「Agent Skills」仓库同登 GitHub 热门，标志着 AI 编码 agent 的技能模板正在走向标准化。这不再是零散的工具，而是可复用、可组合的元技能生态。

## Agent Skills 生态爆发：三个仓库齐上 GitHub 趋势

**是什么**：addyosmani/agent-skills、google/skills、superpowers 等仓库同时冲上 GitHub 趋势榜，均提供面向 AI 编码 agent 的预定义技能模板。

**关键点**：这些仓库定义了一组可复用的“技能”——如“创建 React 组件”“运行测试”“部署到 Vercel”——agent 可以直接调用。addyosmani 版本更偏向社区贡献的通用技能集，google/skills 则可能将 Google Cloud 生态封装其中。

**为什么重要**：技能模板的标准化意味着 AI agent 之间的能力可以互换和组合。过去每个 agent 需要单独训练或配置，如今有了类似“包管理器”的抽象层。这可能是 agent 从 demo 走向生产级协作的第一步。

> 原文：[https://github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

## vLLM 发布 vllm-omni，多模态推理统一框架

**是什么**：vLLM 团队开源 vllm-omni，专为多模态模型（文本+图像+音频）设计的高效推理框架，支持动态批处理、paged attention 扩展。

**关键点**：项目基于 vLLM 现有基础设施，对多模态输入做了 token 级调度优化。与早期多模态推理依赖专用服务不同，vllm-omni 让一个引擎同时处理多种模态，且保持与 OpenAI API 兼容。

**为什么重要**：多模态模型正在走向主流（如 GPT-5、Gemini 2），但推理效率一直是瓶颈。vllm-omni 降低了部署多模态服务的门槛，同时保留开源社区的灵活性和性能优势。

> 原文：[https://github.com/vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni)

## Activeloop 开源 Hivemind：多 Agent 共享记忆与知识

**是什么**：Hivemind 是一个框架，允许多个 AI agent 之间共享统一的知识库和记忆层，实现协作式推理。

**关键点**：每个 agent 仍然有独立的执行逻辑，但可以读写同一向量数据库（基于 Activeloop Deep Lake）。记忆层支持长期记忆和上下文窗口外的知识检索，agent 间可相互调用推理结果。

**为什么重要**：单 agent 能力有上限，多 agent 协作是解决复杂任务的自然路径。Hivemind 提供了一个开箱即用的共享记忆方案，类似给 agent 团队配备一个共享的“黑板”。

> 原文：[https://github.com/activeloopai/hivemind](https://github.com/activeloopai/hivemind)

## turbovec：基于 TurboQuant 的高性能向量索引

**是什么**：turbovec 用 Rust 实现了一个向量索引库，核心使用 Google 的 TurboQuant 量化技术，附带 Python 绑定。

**关键点**：TurboQuant 在保持召回率的同时大幅压缩索引大小，turbovec 进一步优化了查询延迟。与 FAISS 等成熟方案相比，官方基准显示索引构建速度提升 2 倍，内存占用降低 40%。

**为什么重要**：向量数据库和多模态搜索场景下，索引性能直接影响延迟。turbovec 为 Rust/ Python 生态提供了一个轻量且高性能的选择，适合资源受限的 edge case。

> 原文：[https://github.com/RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec)

## whichllm：一键测试并推荐本地最优模型

**是什么**：whichllm 是一个 CLI 工具，自动检测机器硬件（GPU/CPU/内存），下载多个候选 LLM，运行真实任务 benchmark，然后给出性能最佳的模型推荐。

**关键点**：测试基准包括推理速度、首 token 延迟、代码生成准确率（HumanEval 子集）。工具会删除测试后产生的缓存，避免占满磁盘。

**为什么重要**：本地部署 LLM 正变得普遍，但用户往往盲目选择模型。whichllm 提供了一种“先测再选”的方法论，降低试错成本，尤其适合开发者寻找离线运行的最佳平衡点。

> 原文：[https://github.com/Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm)

## claude-howto：可视化 Claude Code 使用指南

**是什么**：claude-howto 是一个开源文档项目，以图片+代码示例的形式，覆盖从基本提示到高级 agent 工作流的 Claude Code 用法。

**关键点**：区别于官方文档的抽象描述，该指南提供可运行的例子，如 “让 Claude 分析一个 repo 并自动生成 PR”。可视化 diagrams 清晰显示了 prompt → tool call → response 的循环。

**为什么重要**：AI agent 工具的使用门槛在于理解“agent 如何思考”。claude-howto 降低了教学成本，适合希望快速上手 Claude Code 的产品经理和初级开发者。

> 原文：[https://github.com/luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)

---

Agent Skills 正在成为 AI agent 的“Dockerfile”——统一抽象层让能力可组合、可复用。你会为你的 agent 编写多少个 Skill？