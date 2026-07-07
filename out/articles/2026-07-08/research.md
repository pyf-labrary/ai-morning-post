# 清华ICML最佳论文，Liquid AI破死循环

第43届ICML在首尔开幕，清华团队摘得最佳论文奖，同时Liquid AI开源了解决推理模型死循环的Antidoom——这两个消息分别指向学术界前沿和工程化痛点。今天最值得关注的是：中国团队在机器学习顶级会议上的竞争力再获验证，而开源社区对推理效率的修复也指向了落地瓶颈的突破。

## ICML 2026开幕，清华团队获最佳论文奖

**是什么**：第43届国际机器学习大会（ICML 2026）在首尔正式开幕，清华大学研究团队获得本届最佳论文奖，同时DeepMind的经典工作获得了时间检验奖。

**关键点**：最佳论文具体题目未披露，但此项荣誉标志着中国高校在深度学习理论或方法上的持续输出。时间检验奖授予DeepMind早年工作，突显其对领域基础的深远影响。

**为什么重要**：ICML是机器学习三大顶会之一，获奖是研究实力和影响力的直接证明。对于技术从业者，关注获奖工作可以捕捉未来1-2年的算法趋势；对于投资人，清华团队的表现也侧面反映了国内学术创新的强度。

> 原文：[https://www.leiphone.com/category/academic/GqOdEOoGq3kVosQr.html](https://www.leiphone.com/category/academic/GqOdEOoGq3kVosQr.html)

## Liquid AI开源Antidoom，消除推理模型死循环

**是什么**：Liquid AI开源了名为Antidoom的工具，采用最终token偏好优化（FTPO）方法，专门修复推理模型（如链式思维推理）陷入无限循环（doom loops）的问题。

**关键点**：Antidoom并非调整模型架构，而是通过偏好优化让模型在推理过程中自动避免重复循环。该项目已开源发布，可直接集成到现有推理体系中。

**为什么重要**：推理模型在实际应用中常因自我纠错或反复推理而导致死循环，浪费计算资源甚至阻塞服务。Antidoom提供了一种轻量级、无需重新训练模型的修复方案，对产品经理和工程师有直接实用价值。开源也意味着社区可在此基础上快速迭代。

> 原文：[https://www.marktechpost.com/2026/07/07/liquid-ai-antidoom-doom-loops-ftpo/](https://www.marktechpost.com/2026/07/07/liquid-ai-antidoom-doom-loops-ftpo/)

今日研究板块指向一个清晰信号：学术顶会认可基础创新，开源社区解决工程顽疾。这两者之间，是不是也藏着你的下一个技术选型或投资判断？