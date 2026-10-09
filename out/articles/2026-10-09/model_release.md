# 便宜到不像前沿的模型来了

今天模型发布板块有五条消息，但信号最集中的是第一条：Anthropic 把 100 万 token 上下文塞进了 0.1 美元/百万输入 token 的价位。这不是一次普通的降价，而是把"长上下文"从高端能力变成默认配置——当便宜的模型都能一次读完整个代码库时，围绕上下文长度做产品设计的门槛就消失了。与此同时，Mistral、JetBrains、Liquid AI、Perplexity 各自开源，开源与闭源的差距继续在收敛，但收敛的位置很有意思：几乎都集中在"专用任务"而非通用对话上。

## Claude Haiku 5.5：1M 上下文，百万输入 token 一毛钱

Anthropic 发布 Claude Haiku 5.5，定位低价小模型，但保留 100 万 token 上下文窗口。定价为每百万输入 token 0.10 美元，OSWorld 得分 72.4%。Anthropic 给出的对比是：同价位强于 GPT-6 Luna，但复杂编程任务上仍有差距。

关键点在于价格与上下文的组合。以往百万级上下文是旗舰模型的卖点，成本高到只适合少量请求；Haiku 5.5 把这个组合压到可以放进批量处理、全仓库检索、长文档流水线这类高频场景。OSWorld 72.4% 说明它在 GUI 操作类任务上不是"能跑就行"的水平。

为什么重要：这条消息实际上在重新划线——哪些任务值得用贵模型。如果一个便宜模型能吞下完整上下文并做基础 agentic 操作，那么旗舰模型的溢价就必须靠更难的推理和编程来支撑。对做应用的人来说，架构上"必须先做检索压缩"的假设可以松一松了。

> 原文：[Anthropic](https://www.anthropic.com/claude-haiku-5-5)

## Mistral 放出 Le Chonk，开源权重叫板闭源前沿

Mistral 发布新模型 Le Chonk，官方说法是在保持开源权重的前提下可以挑战最强的闭源模型。这是欧洲开源阵营对中美前沿模型的又一次公开叫板。

关键点有两个：一是"开源权重"这个前提没有让步，二是"挑战"的具体含义需要看后续评测验证——原文并未给出逐项基准对比，所以目前应视为厂商主张而非已证结论。

为什么重要：欧洲在大模型竞赛中的位置一直尴尬，算力与资本都不占优，开源是它少数能打的牌。如果 Le Chonk 的能力主张站得住，说明前沿能力扩散的速度比预期快，闭源模型的护城河更多来自产品与分发，而不是权重本身。

> 原文：[Ars Technica](https://arstechnica.com/ai/2026/10/mistral-says-le-chonk-can-challenge-the-best-ai-models/)

## JetBrains 开源 Mellum2.1：12B MoE 编码智能体模型

JetBrains 发布 Mellum2.1，采用 Apache 2.0 许可，是一个 12B 总参数、2.5B 激活参数的 MoE（Mixture of Experts）"思考"模型，面向编码智能体。在真实仓库上做强化学习后，SWE-bench Verified 从 2.0 版本的得分提升到 47.0。

关键点是训练方式：不是刷通用语料，而是在真实代码仓库里做 RL。这直接对应智能体的实际工作环境——多文件、有依赖、要跑测试。激活参数只有 2.5B，意味着推理成本相对可控。

为什么重要：SWE-bench Verified 从低位跳到 47.0，说明"小模型 + 真实仓库 RL"这条路在编码智能体上是成立的。对 JetBrains 而言，开源这个模型是在给自己的 IDE 生态铺基础设施；对其他人而言，这是一个可以直接拿去做微调的起点。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/08/jetbrains-releases-mellum2-1-a-12b-moe-open-model-for-coding-agents/)

## Liquid AI 开源 d1：不写 token，直接给决策

Liquid AI 发布开源权重多模态决策模型 d1-3B 与 d1-omni-600M。与主流生成式模型不同，d1 不生成文本，而是直接输出校准后的决策结果，主要面向边缘侧场景。

关键点是"零输出 token"。省掉解码环节，延迟和成本都随之下降，输出的是一个带校准的决策而非一段可读文本。代价是灵活性——你没法让它解释理由，或者把结果拼进自然语言流程里。

为什么重要：这是一条与"更大、更通用"相反的路。边缘设备上跑不动生成式推理，但如果任务本身只是分类、判断、选择，那么直接输出决策比输出文本再解析更合理。它提示了一种分工：云端做生成，端侧做决策。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/07/liquid-ai-releases-open-weight-d1-3b-and-d1-omni-600m-multimodal-decision-models-with-zero-output-tokens/)

## Perplexity 开源嵌入模型，分边缘版和索引版

Perplexity 发布 pplx-embed-v2-late，MIT 许可，包含 0.6B 的边缘版和 9B 的索引版。最高在 MADQA 上取得 92.4%，最弱项为 ViDoRe v3 Markdown 的 61.2%。

关键点是产品线的划分方式：小模型给端侧和低延迟场景，大模型给离线索引。这种"一模型两尺寸"的做法，说明嵌入模型也在走向分层部署。同时，官方给出的 92.4% 与 61.2% 之间差距很大，说明它在文档理解类任务上仍有明显短板。

为什么重要：检索质量决定 RAG（Retrieval-Augmented Generation）的上限，而嵌入模型长期被少数闭源 API 把持。MIT 许可加上两个尺寸，等于把检索层的选择权交回给开发者——特别是那些需要自托管、不能把文档送到外部 API 的团队。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/07/perplexity-ai-releases-pplx-embed-v2-late-a-0-6b-edge-model-and-a-9b-model-scoring-92-4-on-madqa/)

## 结语

今天的五条消息里，四条是开源，三条是专用模型——前沿能力的扩散正在从"通用对话"转向"具体任务"。当百万上下文只要一毛钱，你还会为"省 token"重构产品吗？

> 原文：[Anthropic](https://www.anthropic.com/claude-haiku-5-5)