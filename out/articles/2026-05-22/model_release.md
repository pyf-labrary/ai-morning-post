# OpenAI攻破80年数学难题，开源模型同日井喷

2026年5月22日，模型发布板块上演多幕高潮。最值得关注的是OpenAI的GPT-next推理模型首次自主解决1946年迄今未决的单位距离问题，成本不足千美元，并获得菲尔兹奖得主背书。与此同时，Cohere开源218B MoE模型、阿里发布Qwen3.7-Max、字节开源Lance、腾讯推出翻译模型，密集程度罕见。以下逐一拆解。

## OpenAI“GPT-next”破解平面单位距离问题，AI数学推理迈入新阶段

OpenAI宣称其最新推理模型成功证伪（disprove）了Erdős问题中关于平面单位距离的猜想——一个困扰数学界80年的离散几何难题。模型自主生成了反例，并得到了菲尔兹奖得主Timothy Gowers的认可。整个过程计算成本不到1000美元，远低于传统的人工或大规模搜索方法。关键点在于，模型并非简单检索或枚举，而是通过推理迭代发现了人工未曾构想的构造。为什么重要：这是AI首次在没有人类直接提示的情况下，攻克一个长期开放的著名猜想，标志着推理模型从“解题机器”跃升至“研究助手”层面。对于投资人和技术从业者，这意味着LLM在科学发现中的经济性与可靠性开始被正式验证。

> 原文：[OpenAI](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)

## Cohere开源Command A+：218B稀疏MoE，双卡可跑

Cohere正式开源Command A+，一个2180亿参数的稀疏MoE模型，激活参数约60B。支持48种语言，可在两张H100上运行推理，是Cohere迄今为止最强的开源模型。关键点：采用了动态路由和跨语言对齐技术，在代码、推理和多轮对话上相比Command A有显著提升。为什么重要：在Llama、Qwen等闭源或半开源主导的格局下，Cohere用“两个卡能跑的218B”降低了企业部署超大规模模型的门槛，尤其适合多语言场景。对产品经理而言，这意味着可以以更低成本获得接近GPT-4级别（部分benchmark）的多语言能力。

> 原文：[The Decoder](https://the-decoder.com/cohere-open-sources-its-strongest-model-yet/)

## 阿里Qwen3.7-Max登顶国产榜首，1M上下文窗口

阿里云发布Qwen3.7-Max，拥有100万token上下文窗口，在Artificial Analysis的国产模型评测中排名第一，全球综合前五。关键点：基于MoE架构，在长文档理解、复杂推理和金融场景中表现突出，支持多模态输入但本次未强调图像能力。为什么重要：国产大模型在顶尖基准上的竞争已进入“百万上下文+MoE”阶段，Qwen3.7-Max的排名意味着中国模型厂商在国际评估中首次占据头部位置，对投资人和技术选型者来说，这是评估国产替代可行性的重要参照。

> 原文：[InfoQ](https://www.infoq.cn/article/jAICqmzYVqQ8sHdGSzEH)

## 字节跳动开源Lance：3B参数统一图像视频理解与生成

字节跳动智能创作实验室开源Lance，一个3B参数的原生多模态模型，同时支持图像/视频的理解、生成与编辑。关键点：采用统一的transformer架构而非组合式管线，在COCO Caption、VideoInstruct等基准上达到同类体量最优。为什么重要：3B参数意味着消费级GPU即可微调和部署，统一架构简化了多模态应用开发。对产品经理来说，这开辟了“端到端视频理解+生成”的低成本可能性，尤其在短视频和搜索场景中。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/21/one-model-three-modalities-bytedance-releases-lance-for-image-and-video-understanding-generation-and-editing/)

## 腾讯混元Hy-MT2：指令遵循能力提升，翻译小程序同步上线

腾讯混元发布新一代翻译模型Hy-MT2，在WMT等权威评测中BLEU分数提升显著，尤其擅长处理长难句和领域术语。关键点：模型采用混合对齐训练，指令遵循能力比上一代提升30%以上；同时上线“腾讯Hy翻译”微信小程序，支持端侧部署。为什么重要：翻译模型本身的突破不算大新闻，但结合小程序上线，表明腾讯在尝试将高质量翻译能力直接嵌入日常场景，对出海和内容本地化团队有实际价值。

> 原文：[量子位](https://www.qbitai.com/2026/05/422068.html)

---

今天五条新闻构成了一条清晰的能力分层：OpenAI展示了前沿推理的边界，Cohere和阿里提供了规模化部署的选项，字节和腾讯则在特定模态和任务上深耕。留给读者的问题：当AI能解决80年数学难题时，我们是否还应该用它来翻译邮件？