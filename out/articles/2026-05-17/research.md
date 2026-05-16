# AI能写漏洞利用，但视频模型不懂物理

今日研究板块最值得关注的是：Claude Mythos与GPT-5.5已能在基准测试中自主编写真实的浏览器漏洞利用代码，这标志着大模型在安全领域的能力从识别跃升至主动攻击。与此同时，最先进的视频生成模型在物理推理基准上依然表现糟糕，两者对比说明当前AI在「能力」与「理解」之间仍有鸿沟。

## 新基准显示AI可自主开发浏览器漏洞利用

最新基准测试表明，Claude Mythos和GPT-5.5能从零开始编写真实的浏览器漏洞利用代码，而不仅限于识别或修补。测试环境模拟了真实浏览器漏洞链，模型需要搜索文档、编写脚本、调试并成功触发漏洞。结果显示，两个模型在部分用例中达到与初级安全研究员相当的水平。这一能力对网络安全既是利刃也是风险——自动化的漏洞挖掘将加速攻防博弈，但也可能被滥用。

> 原文：[The Decoder](https://the-decoder.com/new-benchmark-shows-claude-mythos-and-gpt-5-5-can-develop-real-browser-exploits-autonomously/)

## 基准确认AI视频模型视觉惊艳但缺乏世界推理

新推出的视频物理基准评估了Sora、VideoPoet等模型对物体碰撞、重力、流体行为等基础物理的生成一致性。结果一致：视觉效果逼近真实，但推理得分低于随机基线。模型能生成流畅的落体动画，却无法保证物体在接触地面后停止、弹起方向正确。这意味着当前视频生成仍停留在像素级模仿，缺乏对因果关系的符号理解。对于需要物理可信度的自动驾驶仿真、影视预演等场景，这一缺陷是根本性的。

> 原文：[The Decoder](https://the-decoder.com/new-benchmark-confirms-ai-video-generators-look-stunning-but-still-cant-reason-about-the-world/)

## 研究：仅用12.5%专家激活即可达到近完整性能

研究人员训练了一个Mixture-of-Experts模型，在推理时仅激活12.5%的专家参数，却能达到接近全量激活的性能。关键设计在于一种「专家路由器」剪枝训练策略——先在训练中动态选择子集，再通过蒸馏补偿未激活专家贡献的信息。这使得模型在保持推理速度（与dense模型相当）的同时，训练成本显著降低。对于MoE的实际部署，这意味着可以更激进地增加专家总数而不必担心推理延迟，为千亿参数级经济性推理铺路。

> 原文：[The Decoder](https://the-decoder.com/researchers-train-ai-model-that-hits-near-full-performance-with-just-12-5-percent-of-its-experts/)

## Nous Research提出灯塔注意力，预训练提速1.7倍

Nous Research发布了Lighthouse Attention，一种仅用于训练的筛选式层次注意力机制。它通过动态选择对当前batch最相关的token子集（而非全注意力），在128K长上下文预训练中实现1.4–1.7倍加速，且推理时无需做任何改动——模型权重与标准Transformer兼容。这意味着团队可以将长上下文训练时间压缩近一半，尤其利好需要处理长文档的LLM。不过这种选择式注意力可能漏掉长程弱关联信息，需在特定任务上验证。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/16/nous-research-proposes-lighthouse-attention-a-training-only-selection-based-hierarchical-attention-that-delivers-1-4-1-7x-pretraining-speedup-at-long-context/)

## Δ-Mem论文提出大模型高效在线记忆

arXiv预印本中，作者提出Δ-Mem方法，允许LLM在不增加模型参数量的情况下，通过外部记忆差异向量实现高效在线记忆更新。与传统的Fine-Tuning或检索增强不同，Δ-Mem将新知识编码为与旧知识之间的「差值」，并压缩存储于轻量记忆层中。实验显示，在持续学习场景下，Δ-Mem以微乎其微的推理开销，将长尾事实召回率提升近20%。对于需要频繁更新知识的对话助手或知识库系统，这是一种低成本的记忆方案。

> 原文：[arXiv](https://arxiv.org/abs/2605.12357)

## CVPR 2026综述：自动驾驶与视频模型走向可控真实世界

雷锋网对CVPR 2026中热门方向的总结指出，自动驾驶和视频生成正从「生成逼真画面」转向「对真实世界的可控推理」。亮点包括：端到端驾驶模型内置因果推理模块，以及视频模型通过训练目标从像素损失转向动作/物理一致性损失。整体趋势是模型必须学会「理解」才能「生成」——与本周视频推理基准的结论一致。但论文中多数方法仍依赖大量人工标注，离完全自主认知还有距离。

> 原文：[雷锋网](https://www.leiphone.com/category/ai/fMkWxfMZbW2XRxwK.html)

---

当模型能自己写漏洞利用代码却看不明白一个球落地后的反弹方向时，AI 的「智能」到底缺了什么？