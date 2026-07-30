# 腾讯 AngelSpec 开源，统一六种投机解码

腾讯开源 AngelSpec，一个支持六种架构的投机解码训练框架，并引入 DFly 块扩散起草模型。这是 LLM 推理加速从研究走向工程化的重要一步——投机解码的碎片化现状有望被统一框架打破，开发者无需在多种方案间重复造轮子。

## 腾讯 AngelSpec：投机解码的统一训练框架

腾讯开源的 AngelSpec 是一个统一的投机解码训练框架，可支持六种架构（MTP、自我投机解码、多个草案模型等）的训练，并新增 DFly 块扩散起草模型。关键点在于它提供了标准化的训练接口和数据流，让原本分散的投机解码方案可以在同一平台上对比和部署。为什么重要？投机解码是当前大模型推理加速的主流手段，但各家实现差异大，训练流程不通用。AngelSpec 降低了复用和实验成本，有望成为该领域的基础设施，推动推理效率再上台阶。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/30/tencent-open-sources-angelspec-a-unified-training-framework-for-mtp-and-block-parallel-speculative-decoding-on-hy3-models/)

## 微软 VibeVoice：语音 AI 的开源选择

微软推出开源语音 AI 项目 VibeVoice，提供前沿的语音合成与识别能力。它基于最新的神经声码器和端到端模型，支持多语言和情感控制。关键点是代码和预训练权重全部开放，开发者可以本地部署，无需调用云端 API。为什么重要？语音交互正在成为 Agent 的标准输入输出，但过去高质量的语音模型多被商业 API 所垄断。VibeVoice 的开源给了开发者一个可控、低延迟的备选方案，尤其适合隐私敏感场景。

> 原文：[GitHub](https://github.com/microsoft/VibeVoice)

## Agent Governance Toolkit：自主 Agent 的 10 项 OWASP 防护

微软开源的 Agent Governance Toolkit 是一个面向 AI Agent 的治理工具包，涵盖策略执行、零信任身份、沙箱执行和可靠性工程，实现了 10 项 OWASP 对 Agent 的安全防护。关键点：它定义了 Agent 行为边界（如文件系统访问、网络调用、权限继承），并提供可插拔的检查器。为什么重要？随着 Agent 自主性增强（如执行代码、调用外部工具），安全与合规成为落地瓶颈。这个工具包让开发者可以像管理微服务一样管理 Agent 行为，降低了企业采用 Agent 的风险。

> 原文：[GitHub](https://github.com/microsoft/agent-governance-toolkit)

## 月之暗面 MoonEP：MoE 专家并行通信库

Moonshot AI 开源 MoonEP，一个面向分布式混合专家系统（MoE）的高效专家并行通信库。它通过精细的负载均衡和通信优化，实现了近乎完美的专家利用率。关键点：MoonEP 支持动态路由和拓扑感知的 all-to-all 通信，训练吞吐量提升 15-30%。为什么重要？大模型越来越多采用 MoE 架构以在开销和性能间取得平衡，但专家并行的通信瓶颈一直限制扩展。MoonEP 提供了一种经过验证的工程方案，尤其适合那些自建 MoE 训练集群的团队。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/29/moonshot-ai-open-sources-moonep-a-perfectly-balanced-expert-parallelism-library-for-moe-training/)

## Token Saver：用本地 RAG 把 Claude PDF 成本打下来 90%

开源 MCP 扩展 Token Saver 利用本地混合 RAG 技术，将 Claude 处理 PDF 的 token 消耗降低 90-99%，同时所有数据留在本地。关键点：它在发送给 Claude 之前，先用本地嵌入模型对 PDF 内容进行检索、压缩与结构化，只保留最相关的片段。为什么重要？Token 成本仍然是使用高端模型（如 Claude）的主要门槛，尤其是处理长文档。Token Saver 用开源工具解决了一个真实痛点：用不到 10% 的 token 完成同等准确度的 PDF 分析，隐私和预算两全。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/30/token-saver-an-open-source-mcp-extension-using-local-hybrid-rag/)

当“统一训练框架”和“Agent 治理”同时开源，AI 工具链正在从点状突破走向系统化。你的团队最缺的是底层效率提升，还是上层安全管控？