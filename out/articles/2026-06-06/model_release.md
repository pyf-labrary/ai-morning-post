# NVIDIA 开源 Nemotron 3 Ultra：550B 参数 MoE

今日最值得关注的是 NVIDIA 开源了 550B 总参数（55B 活跃）的 Nemotron 3 Ultra，采用混合 Mamba-Transformer 架构，支持 100 万 token 上下文，推理吞吐量比同等开源 LLM 高约 6 倍。这标志着开源模型在效率与长上下文上再进一阶，尤其为长期运行的 Agent 场景提供了新的基础选择。

## NVIDIA 开源 Nemotron 3 Ultra：550B 混合 MoE，专为长时 Agent 设计

**是什么**：NVIDIA 发布 Nemotron 3 Ultra，一个 550B 总参数、55B 活跃参数的 MoE 模型，融合 Mamba 状态空间模型与 Transformer，支持 100 万 token 上下文窗口。官方宣称其推理吞吐量比同类开源 LLM 高约 6 倍。

**关键点**：该模型专为“长期运行代理”设计，混合架构减少 KV 缓存占用，同时利用 Mamba 高效处理长序列。NVIDIA 以 Apache 2.0 开源权重和推理代码，并提供了针对 agentic 工作流的优化示例。

**为什么重要**：在 Agent 和工具使用场景中，长上下文和低延迟是关键瓶颈。Nemotron 3 Ultra 提供了一个开源基座，让团队可以在不牺牲速度的情况下构建需要持续交互（如代码编写、多步推理）的代理系统，可能推动更多生产级 Agent 原生模型的出现。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/06/04/nvidia-ai-releases-nemotron-3-ultra-an-open-550b-mixture-of-experts-hybrid-mamba-transformer-for-long-running-agents/)

## DeepMind 发布 Gemma 4 QAT 检查点：显存占用再降，加速边缘部署

**是什么**：Google DeepMind 为 Gemma 4 推出量化感知训练（QAT）检查点，包括 Q4_0 版本和面向移动端的新格式，旨在降低设备端显存占用。

**关键点**：QAT 在训练过程中模拟量化，比后训练量化损失更小。新移动格式进一步适配手机等资源受限设备，使 Gemma 4 能在更低的 RAM 下运行，同时保持推理质量接近 BF16 基线。

**为什么重要**：边缘部署是开源模型落地的关键一步。Gemma 4 本身参数量适中，结合 QAT 检查点后，开发者可以在手机、IoT 设备上直接运行模型，无需依赖云端。这对于隐私敏感和离线场景（如医疗、翻译）有直接价值，也可能推动更多 “模型上机” 的产品设计。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/06/05/google-deepmind-releases-gemma-4-qat-checkpoints-q4_0-and-a-new-mobile-format-cut-on-device-memory/)

## 中科闻歌发布 Decitron 决策机：从问答到真实世界推演

**是什么**：中科闻歌推出 Decitron 决策机，宣称超越传统问答大模型，进入“真实世界推演”阶段，可用于辅助复杂商业、政策或管理决策。

**关键点**：产品核心能力包括因果推理、假设推演和多步动态模拟，而非简单的文本生成。官方表示它通过结构化知识图谱与模型结合，实现从“理解问题”到“模拟结果”的闭环。

**为什么重要**：国产模型在决策智能方向的探索多处于初期，Decitron 若真能实现推演能力，将对金融、应急管理、战略规划等领域产生实质影响。不过目前公开技术细节甚少，还需观察其落地效果和泛化能力。这一方向也提醒行业：大模型的竞赛正在从“能答”转向“能推演”。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/JvMzCFCNVVx3dav9.html)

当模型从生成答案走到“推演”世界，我们是否需要重新定义“智能”的边界？