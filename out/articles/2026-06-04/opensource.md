# 开源 AI Agent 的桌面霸权时代，从 Hermes 开始

今天开源世界最值得关注的是 Nous Research 发布的 Hermes Desktop——一个能操控电脑桌面的跨平台 AI Agent。当 Agent 从聊天窗口走进操作系统，开发者与产品经理该思考的，不只是代码优化，而是人机交互范式的下一个转折点。

## Nous Research 发布 Hermes Desktop：AI Agent 接管你的桌面

Hermes Desktop 是一个开源 AI Agent，支持 Windows、macOS 和 Linux 三大平台。它能够理解桌面 GUI 状态，模拟鼠标键盘操作，完成文件整理、网页填写等多步任务。与目前主流的“说一句话就执行”不同，Hermes 更强调对桌面环境的持续感知与自主决策。

> 原文：https://the-decoder.com/nous-research-releases-hermes-desktop-an-open-source-ai-agent-for-every-platform/

## Arm 开源 Metis：AI 安全审计性能超越传统 SAST

Arm 推出基于 AI 的源代码安全分析框架 Metis，在漏洞发现率与误报率上均优于传统静态应用安全测试（SAST）工具。Metis 利用 LLM 理解代码语义而非单纯模式匹配，能够检测逻辑缺陷与配置错误。开源意味着安全团队可以自托管并微调，降低 SaaS 依赖风险。

> 原文：https://www.infoq.cn/article/WBSYmfvEkiaHEcgkYOcA

## Headroom：Token 压缩 60-95%，RAG 成本骤降

Headroom 是一个开源工具，专门针对日志、文档等输入进行 token 压缩，可节省 60-95% 的 token 消耗，同时保持 LLM 回答质量。它提供库与 MCP 服务器两种接入方式，适合 RAG 流水线中作为预处理步骤。对于 token 计费的 AI 应用，这是一个直接降低成本、提升吞吐量的实用方案。

> 原文：https://github.com/chopratejas/headroom

## OpenBMB VoxCPM2：无需分词器的多语言语音合成与克隆

VoxCPM2 是 OpenBMB 开源的多语言语音生成模型，最大的技术特点是“无分词器”（tokenizer-free），直接建模原始音频，支持语音合成、创意声音设计和逼真语音克隆。相比传统 pipeline，端到端架构减少了音色失真和多语言切换时的质量衰减，适合语音 Agent 与内容创作场景。

> 原文：https://github.com/OpenBMB/VoxCPM

## Datawhale 开源《从零开始构建智能体》教程

hello-agents 是 Datawhale 出品的零基础智能体教程，从 Agent 核心概念（工具使用、记忆、规划）讲到代码实现，路径清晰，适合想从理论进入实践的开发者。教程以交互式 notebook 呈现，可直接在 Colab 运行。

> 原文：https://github.com/datawhalechina/hello-agents

## Trellis 引入 RadixAttention 提升长序列推理速度

开源推理框架 Trellis 发布 RadixAttention 技术，优化长上下文注意力计算。RadixAttention 通过复用中间状态与稀疏化策略，在长序列（如多轮对话、长文档）推理中减少了内存占用与延迟。对于需要运行大上下文 Agent 的团队，Trellis 提供了一个优化推理性能的落地选项。

> 原文：https://trellis.unfoldml.com/blog/radix-attention-intro

## Supermemory：为 AI Agent 打造超快记忆引擎

Supermemory 开源了一个高性能记忆存储引擎与 API，为 AI Agent 提供跨会话、跨应用的持久记忆能力。它支持向量检索与结构化管理，让 Agent 在不同对话或任务间“记住”用户偏好与上下文。产品经理可以以此构建连贯的 Agent 体验，而非每次对话都从零开始。

> 原文：https://github.com/supermemoryai/supermemory

## Vibe-Trading：用多智能体 LLM 做股票交易

港大团队开源 Vibe-Trading，一个基于多智能体 LLM 的金融交易框架。它集成了情绪分析、市场数据解读与交易决策功能，Agent 之间分工协作（例如分析师、交易员、风控员角色），模拟人类交易团队流程。适合量化研究者与 AI Agent 开发者探索多智能体在实际金融场景中的表现。

> 原文：https://github.com/HKUDS/Vibe-Trading

---

当 Hermes Desktop 让 Agent 操作你的鼠标，Memories 让 Agent 记住你的习惯，Vibe-Trading 让 Agent 替你买卖股票——你愿意把哪个任务交给开源 Agent？