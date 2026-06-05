# NVIDIA 开源 Cosmos，物理 AI 有了世界模型

昨天开源圈最值得关注的是 NVIDIA 的物理 AI 世界模型平台 Cosmos 正式开源。它补上了机器人、自动驾驶等场景从仿真到部署的中间层基础设施。与此同时，GitHub 和 Arm 分别放出了 Copilot SDK 和 AI 安全框架 Metis，一个降低 Agent 集成门槛，一个提升漏洞检测效率——工具链的成熟度正在加速。

## NVIDIA 开源 Cosmos：面向物理 AI 的世界模型平台

**是什么**：NVIDIA 在 GitHub 上开源了 Cosmos 平台，包含世界模型、数据集和工具链，专为机器人、自动驾驶等物理 AI 应用设计。

**关键点**：Cosmos 提供预训练的世界模型和仿真数据生成管道，开发者可以直接在真实场景之前，用其进行策略训练和验证。平台还包含用于物理规律学习的模块。

**为什么重要**：此前物理 AI 的模拟训练依赖碎片化工具，Cosmos 试图提供标准化底座。NVIDIA 将其开源意味着社区可以复用其数年的闭门积累，可能加速自动驾驶和机器人行业从实验室走向量产。

> 原文：[https://github.com/NVIDIA/cosmos](https://github.com/NVIDIA/cosmos)

## NVIDIA Dynamo Snapshot 开源：K8s 上 AI 推理快速启动

**是什么**：NVIDIA 开源 Dynamo Snapshot，利用 CRIU 和 cuda-checkpoint，实现 vLLM 推理工作负载在 Kubernetes 上的快速检查点恢复。

**关键点**：该方案允许将 GPU 内存状态序列化，启动时间从分钟级降至秒级，且不丢失推理进度。适合需要弹性扩缩的在线推理场景。

**为什么重要**：AI 推理的冷启动延迟一直是生产环境的痛点，Dynamo Snapshot 给出了一个开箱即用的 K8s 集成方案，偏向工程实用，而非研究性突破。

> 原文：[https://www.marktechpost.com/2026/06/05/nvidia-ai-releases-dynamo-snapshot-a-criu-based-fast-startup-system-for-ai-inference-on-kubernetes/](https://www.marktechpost.com/2026/06/05/nvidia-ai-releases-dynamo-snapshot-a-criu-based-fast-startup-system-for-ai-inference-on-kubernetes/)

## GitHub 开源 Copilot SDK：集成 AI Agent 到任何应用

**是什么**：GitHub 发布 Copilot CLI SDK（github.com/github/copilot-sdk），允许开发者将 Copilot Agent 集成到自己的应用和服务中，支持多平台。

**关键点**：SDK 提供了 Agent 的完整 API 接口，开发者可以自定义触发逻辑、上下文、输出格式，不再局限于 IDE 内的 Copilot Chat。

**为什么重要**：这是 GitHub 将 Copilot 从“编辑器插件”升级为“平台能力”的关键一步。对于 SaaS 产品经理和技术决策者，这意味着可以用官方渠道快速给自己的产品加一个“AI 助手”，而不是从头训练。

> 原文：[https://github.com/github/copilot-sdk](https://github.com/github/copilot-sdk)

## Arm 开源 AI 安全框架 Metis：比 SAST 更高效

**是什么**：Arm 开源 AI 安全框架 Metis，在安全漏洞检测方面性能优于传统静态应用安全测试（SAST）工具。

**关键点**：Metis 专为 AI 模型和推理管道设计，能检测模型中毒、对抗样本路径、敏感数据泄露等 SAST 难得发现的漏洞。已通过 Arm 内部测试，平均检出率高 30%。

**为什么重要**：AI 供应链安全是 2026 年的高频话题，但现有工具多从传统软件安全移植而来。Metis 是首个由芯片巨头开源的、针对 AI 流程的专用框架，更适合部署 AI 应用的团队参考。

> 原文：[https://www.infoq.cn/article/WBSYmfvEkiaHEcgkYOcA](https://www.infoq.cn/article/WBSYmfvEkiaHEcgkYOcA)

## Hermes Agent 开源：随你成长的自主 AI 代理

**是什么**：Nous Research 开源 Hermes Agent，一个可以在本地运行、持续学习和增长的自主代理框架（github.com/NousResearch/hermes-agent）。

**关键点**：它支持长期记忆、工具调用和动态技能扩展，能在本地硬件上运行，不依赖云端 API。代码和模型权重一并开源。

**为什么重要**：自主 Agent 赛道拥挤但多锁定在专有 API。Hermes Agent 强调“本地+持续学习”，适合对数据隐私有要求的开发者研究 or 二次开发。

> 原文：[https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

## Open Notebook 开源：NotebookLM 的灵活替代方案

**是什么**：开源项目 Open Notebook（github.com/lfnovo/open-notebook）实现类似谷歌 NotebookLM 的能力，但更灵活可定制。

**关键点**：支持多源文档上传、本地模型调用、用户自定义知识库和聊天界面。全部代码可自托管。

**为什么重要**：NotebookLM 仅限谷歌生态，Open Notebook 让追求数据主权或想要定制化 RAG 管道的团队有了开源选项。

> 原文：[https://github.com/lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)

## GitHub 开源 Spec Kit：引导规范驱动开发

**是什么**：GitHub 发布 Spec Kit（github.com/github/spec-kit），提供入门模板和工具，帮助团队采用规范驱动开发（Spec-Driven Development）。

**关键点**：包含 API 规范模板、测试验证脚本、CI 集成示例，支持 OpenAPI 和 AsyncAPI 等标准。

**为什么重要**：规范驱动开发能减少前后端联调摩擦，但推行门槛高。Spec Kit 给出官方入门套件，适合研发团队快速试水。

> 原文：[https://github.com/github/spec-kit](https://github.com/github/spec-kit)

## DuckDB 开源 Quack 协议：面向多用户分析的 HTTP 接口

**是什么**：DuckDB 推出 Quack，一种基于 HTTP 的客户端/服务器协议，旨在支持多用户分析场景。

**关键点**：Quack 允许 DuckDB 作为轻量级服务运行，多个客户端通过 HTTP 查询，支持并发和权限控制。

**为什么重要**：DuckDB 本是嵌入式分析数据库，Quack 让它具备服务器化能力，适合需要快速搭建分析 API 或数据沙箱的团队。

> 原文：[https://www.infoq.cn/article/au8ICoBCuxOaOuyr0wWI](https://www.infoq.cn/article/au8ICoBCuxOaOuyr0wWI)

---

今天最忙的是 NVIDIA 和 GitHub——一个在物理 AI 底座上放出了重磅开源，一个在 Agent 集成上降低了门槛。剩下的故事也在告诉开发者：工具层的战争已经从“要不要用 AI”变成了“怎么更好集成和落地”。你正在为哪个场景找开源拼图？