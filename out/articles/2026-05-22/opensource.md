# 开源日报：Agent 编排规范与自动化科研齐发

今日开源社区围绕 AI Agent 迎来多项目同日发布——OpenAI 推出了自主编码 Agent 的编排规范 Symphony，Karpathy 发布单 GPU 跑科研的 autoresearch，GitHub 则推出了规范驱动开发的 Spec Kit。标志性信号：Agent 开发正从“手工作坊”走向标准与自动化。

## OpenAI 开源 Symphony，定义自主编码 Agent 编排规范

**是什么 / 关键点 / 为什么重要**

OpenAI 发布了 Symphony SPEC，一个面向自主编码智能体编排的开放标准规范。这不是一个具体产品，而是一套定义了 Agent 之间如何通信、任务如何拆解与分配的协议。核心目的是让不同厂商、不同框架的编码 Agent 能够互操作，类似 HTTP 对于 Web 的意义。对于开源生态而言，这意味着未来顶级的 Agent 工作流（如多 Agent 协作写代码）可能不再绑定单一平台，而是可以自由组合。虽然规范初版，但 OpenAI 的背书有望加速行业采用，降低 Agent 编排的开发成本。

> 原文：[InfoQ](https://www.infoq.cn/article/kmcvx8qNTQRYpPHVDq4B)

## Karpathy 开源 autoresearch：单 GPU 自动跑科研

**是什么 / 关键点 / 为什么重要**

Andrej Karpathy 发布 autoresearch，一个让 AI 代理自动在单 GPU 上运行 nanochat 训练研究的开源项目。项目基于 PyTorch，Agent 可以自动设计实验、执行训练、收集结果并迭代。关键点：它让单卡用户也能进行一定规模的自动化研究探索，大幅降低了超参搜索和消融实验的人力成本。重要性在于，这是开源界第一次将“科研劳动”本身 Agent 化，可能推动更多小型团队或个人研究者用低成本跑通完整实验链路，加速模型迭代。

> 原文：[GitHub - karpathy/autoresearch](https://github.com/karpathy/autoresearch)

## 火山引擎开源 OpenViking：专为 AI Agent 设计的上下文数据库

**是什么 / 关键点 / 为什么重要**

火山引擎发布 OpenViking，一个开源的上下文数据库，通过文件系统范式统一管理 Agent 的记忆、资源和技能。它将 Agent 运行所需的上下文（历史对话、知识库、工具配置等）持久化、可查询，并支持版本管理。关键在于：传统 LLM 应用往往把上下文存在内存或简单键值存储中，而 OpenViking 提供了类似文件系统的分层组织，更符合 Agent 长会话场景的需求。重要性在于，这是国内云厂商在 Agent 基础设施层的少有开源贡献，为构建可落地的生产级 Agent 提供了存储基座。

> 原文：[GitHub - volcengine/OpenViking](https://github.com/volcengine/OpenViking)

## GitHub 发布 Spec Kit，助力规范驱动开发

**是什么 / 关键点 / 为什么重要**

GitHub 推出开源工具包 Spec Kit，帮助开发者采用 Spec-Driven Development（SDD）方法。SDD 强调先写详细规范描述（类似技术文档），再用工具自动生成代码骨架或约束。Spec Kit 包含模板、命令行工具和 CI 集成示例。关键点：它让“先写规范再写代码”的流程变得可复用，尤其适合 Agent 开发中需要明确定义输入输出行为的场景。重要性在于，GitHub 试图将 Agent 开发者的注意力拉回“界定问题”而不是“调试 Agent 行为”，从方法论上提升 Agent 的可信度。

> 原文：[GitHub - github/spec-kit](https://github.com/github/spec-kit)

---

今天的开源 Agent 发布不约而同指向同一个方向：用标准、数据库和工具链把 Agent 从 Demo 变成工程。下一个改变研发流程的 Agent 工具，会是来自大厂的规范，还是顶级研究者的“玩具”？