# Kimi K3开源：2.8万亿参数，成本仅为Sonnet级

月之暗面今天扔出业界最重磅消息：2.8万亿参数的MoE模型Kimi K3以开放权重形式发布，性能接近Opus 4.8但推理成本仅为Sonnet 5级别。同一日，Mira Murati创立的Thinking Machines Lab、英伟达、腾讯与Zyphra分别发布新模型，开源生态在模型规模、嵌入、脑电等方向同时刷新认知。

## 月之暗面发布Kimi K3：2.8万亿参数开源MoE模型

**是什么：** Moonshot AI今天正式开源Kimi K3，一个2.8万亿参数（2.8T）的Mixture-of-Experts模型，采用自研Kimi Delta Attention架构，每次推理激活16个专家。支持100万token上下文窗口，且在多项基准上性能接近OpenAI的Opus 4.8，但其推理成本仅对标Sonnet 5级别。

**关键点：** 这是目前开源世界公开的最大MoE模型之一（参数规模与DeepSeek-V3相当）。Kimi Delta Attention通过动态路由和稀疏注意力降低了长上下文计算开销，使得百万token推理成为可负担的工程实践。模型权重和架构细节已完整公开。

**为什么重要：** 开源模型在“性能-成本”曲线上第一次如此接近闭源旗舰。Kimi K3证明了超大规模MoE可以在遵循OpenAI级别能力的同时，将部署成本压至主流商用模型水平。这直接挑战了“强模型必昂贵”的前提，加速了AI基础设施层的商品化。

> 原文：[Kimi Blog](https://www.kimi.com/blog/kimi-k3)

## Mira Murati团队发布首个开源模型Inkling

**是什么：** 前OpenAI CTO Mira Murati创立的Thinking Machines Lab今天发布了Inkling，一个开放权重的MoE模型。这是该团队首次公开其AI能力，模型架构细节尚未完全披露，但已知采用混合专家设计。

**关键点：** 作为Mira Murati离开OpenAI后的首个公开作品，Inkling选择了完全开放的路径（开放权重而非仅提供API），叠加了团队在推理和可靠性上的研究积累。目前模型已在Hugging Face上开放下载，但尚未发布完整技术报告。

**为什么重要：** Murati团队的动向一直是业界焦点。Inkling的发布标志着又一支顶尖团队加入开源阵营，且选择MoE架构说明其延续了对大规模稀疏模型的判断。这进一步压缩了闭源模型的差异化空间，也让OpenAI的人才外溢效应更加显性。

> 原文：[Thinking Machines Lab](https://thinkingmachines.ai/news/introducing-inkling/)

## 英伟达开源Nemotron 3 Embed：8B模型排名RTEB第一

**是什么：** NVIDIA发布了Nemotron 3 Embed嵌入模型集合，包括8B、1B（BF16）和1B（NVFP4）三个版本。其中8B版本在RTEB检索基准上以78.46 NDCG@10的成绩排名第一。

**关键点：** 这是专门为检索增强生成（RAG）和语义搜索优化的嵌入模型。8B版本在RTEB上击败了此前所有竞品，1B版本在轻量场景下提供了精度与速度的平衡，而NVFP4量化版专为英伟达硬件优化推理效率。所有模型均开源。

**为什么重要：** 嵌入模型是RAG管线的地基。英伟达以“硬件+模型”组合拳再次推进了生态标准——RTEB榜单被自家模型屠榜，既验证了架构优势，也为开发者提供了可直接部署的顶级嵌入方案。对于做搜索、知识库的产品团队，这可能是近期最值得换上的组件。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/17/nvidia-ai-releases-nemotron-3-embed-an-open-embedding-collection-whose-8b-checkpoint-ranks-1-on-rteb/)

## WAIC 2026：腾讯混元Hy3大模型首秀

**是什么：** 腾讯在世界人工智能大会上首次公开混元Hy3大模型，并同步上线AI技能支付体系——开发者可通过平台销售基于混元的微调模型或技能组件。

**关键点：** 混元Hy3的具体参数与基准分数尚未披露，但腾讯在大会上强调了“模型+支付”的闭环：开发者训练的技能可在混元生态内定价销售，平台抽成。这一模式类似App Store，但针对的是AI模型能力和API服务。

**为什么重要：** 模型发布本身未必是最亮眼的部分，“技能支付体系”才是腾讯此次的核心产品。它将模型提供方从“卖服务”转向“建生态”，试图用商业模式吸引开发者建链。如果执行顺利，这可能成为国内AI商业化的新范式——但开放程度和抽成比例仍需观察。

> 原文：[InfoQ](https://www.infoq.cn/article/FeWLPKLYDjWko8rJjxKq)

## Zyphra开源脑电基础模型ZUNA1.1

**是什么：** Zyphra发布了ZUNA1.1，一个380M参数的EEG（脑电图）基础模型，基于Apache 2.0许可。支持0.5到30秒的可变长度输入，可重建和去噪头皮脑电信号。

**关键点：** 这是少有的面向神经信号的基础模型。模型采用Transformer架构在百万条脑电数据上预训练，能处理不同长度的时序输入，并自动学习去噪和重建。项目完全开源，提供预训练权重和微调脚本。

**为什么重要：** 脑机接口（BCI）领域长期缺少通用的基础模型，ZUNA1.1填补了这一空白。它让研究人员无需从零训练就能获得脑电信号的表征能力，可能加速BCI在医疗、人机交互中的应用。380M的参数规模也使得在边缘设备上部署成为可能。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/17/zyphra-releases-zuna1-1-an-apache-2-0-eeg-foundation-model-with-variable-length-inputs-from-0-5-to-30-seconds/)

---

今天的模型发布潮给出了一个清晰信号：开源正在从“追赶者”变为“成本定义者”。当2.8万亿参数的Kimi K3可以用Sonnet级成本运行，闭源模型还剩多少溢价空间？