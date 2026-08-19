# Mojo 开源，Agent 互操作网络亮相

今日开源板块最值得关注的是 Mojo 编程语言正式开源。作为面向 AI 基础设施的高性能语言，Mojo 终于打开大门；接下来真正值得观察的，是社区能否围绕它形成合力。同批开源动态里，Agent（智能体）网格、模型转换器等工具也在各自环节降低门槛。

## Mojo 编程语言正式开源

Modular 宣布 Mojo 编程语言正式开源。Mojo 一开始就定位为面向 AI 基础设施的高性能语言，希望兼顾开发效率和底层性能。

关键点在于：代码开放之后，外部开发者可以审查实现、提交优化、围绕它构建工具链。相比闭源版本，开源意味着生态建设进入新阶段。

为什么重要：AI 基础设施的语言层长期被 C++/CUDA 和 Python 两侧挤压。Mojo 选择开源，是想用社区来扩大采用。但开放只是第一步，治理机制和实际性能落地才是生态能否壮大的关键。

> 原文：[Simon Willison](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/)

## 英伟达开源 TensorRT Model Connect，两命令转换 HF 模型

英伟达发布 TensorRT Model Connect 公开预览，可以把 Hugging Face 检查点转换成原生 C++ 推理，无需 ONNX 中间格式。官方称两个命令即可完成转换。

关键点：省掉 ONNX 这一中间层，部署链路更短，也更贴近 TensorRT 的优化路径。对使用 Hugging Face 模型的团队，这可能简化从研究到生产的转换过程。

为什么重要：模型部署的格式转换一直是隐性成本。若 TensorRT Model Connect 成熟，NVIDIA 生态接入开源模型的阻力会进一步下降。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/08/18/nvidia-releases-tensorrt-model-connect-in-public-preview-hugging-face-checkpoint-to-native-c-inference-in-two-commands/)

## 谷歌开源 Agent 网格 SAM

Google 开源 Sovereign Agent Mesh（SAM），一个零配置、零信任的 P2P 网络，让 Agent 可以发现并调用彼此的 MCP 工具。

关键点：零配置意味着不需要额外基础设施；零信任则意味着默认不信任网络中的任何节点。两者结合，尝试让 Agent 在不依赖中心化服务的情况下互操作。

为什么重要：Agent 之间互操作是 agentic 应用规模化的核心瓶颈。SAM 把发现和调用放到网络层，有可能成为 agentic 应用的基础设施之一。但零信任的安全边界仍要经过实战检验。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/08/18/meet-sam-sovereign-agent-mesh-a-zero-config-zero-trust-p2p-network-for-ai-agents/)

## 火山引擎开源 OpenViking：Agent 自进化上下文数据库

火山引擎开源 OpenViking，定位是统一 Agent 记忆、知识 RAG（Retrieval-Augmented Generation）与技能，实现自进化的上下文数据库。

关键点：它将记忆、检索、技能放在一个系统中的思路，试图解决 Agent 状态持久化问题。开源后开发者可以自行部署和改造。

为什么重要：Agent 应用普遍缺乏统一的上下文管理。OpenViking 能否成为通用层还看不清楚，但它把问题摆上桌面，也给了社区一个可实验的起点。

> 原文：[GitHub - volcengine/OpenViking](https://github.com/volcengine/OpenViking)

## 开源 AI 渗透测试工具 Strix

Strix 是一个开源 AI 渗透测试工具，目标帮助开发者发现并修复应用安全漏洞。

关键点：用 AI 驱动漏洞发现，可以让安全测试更早进入开发流程。开源也让安全团队能审计其检测逻辑。

为什么重要：AI 在安全领域的应用越来越普遍，但自动发现的漏洞仍需要人工验证。Strix 的价值取决于检测精度和误报率，不能只看“AI”标签。

> 原文：[GitHub - usestrix/strix](https://github.com/usestrix/strix)

## video-use：用编码 Agent 编辑视频

browser-use 团队开源 video-use，让编码 Agent 通过自然语言指令完成视频剪辑。

关键点：延续 browser-use 的 Agent 操控思路，把操作对象从浏览器扩展到了视频编辑。用户用自然语言描述，Agent 负责编排具体动作。

为什么重要：多模态 Agent 正在进入创作工具链。视频剪辑包含语义理解、时间线和渲染调度，复杂度高于普通网页操作；video-use 能否实用，要看