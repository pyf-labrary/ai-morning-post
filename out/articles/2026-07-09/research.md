# 阿里Agent评测新范式获ACL最佳论文

今日研究板块最具信号意义的事件是阿里获得ACL 2026最佳资源论文奖，提出专家级Agent评测基准，直指现有Benchmark在真实规则推理上的盲区。与此同时，智源发布世界基础模型Orca、RoboDojo测评显示最强机器人模型仅12.8分——三件事共同指向一个判断：AI在“理解真实世界”这一关，依然有结构性的短板。ICML 2026正在进行中，中国大厂展台抢人也是一条侧面线索。

## 阿里ACL最佳论文：Agent评测为何失效？

阿里研究团队提出的专家Agent评测基准（EvalAgent？原文未给出具体名称），在ACL 2026上获得最佳资源论文奖。其核心发现是：当前多数Agent Benchmark更关注“完成任务”，而非“理解规则”——当任务涉及现实世界的多步规则推理（如合同条款、医疗流程），Agent的表现会急剧下降。该基准通过专家设计的复杂场景，揭露了现有模型对隐含前提和因果链条的忽视。

> 原文：https://www.qbitai.com/2026/07/446069.html

## 智源发布悟界·Orca：世界模型的Next State Prediction路径

悟界·Orca并非一个对话助手，而是一个旨在理解“世界如何变化”的基础模型。它采用双路径学习架构：一条路径负责感知当前状态，另一条路径预测下一个状态（next state prediction）。这种设计试图让模型超越语言表面的相关性，获得类似人类对物理和抽象世界动态的直觉。智源声称它是“通用世界基础模型”，但尚未公布与现有世界模型（如Sora、UniSim）的横向对比数据。

> 原文：https://www.qbitai.com/2026/07/446075.html

## RoboDojo：最强机器人操作策略仅12.8分，人类100分

RoboDojo是一个统一仿真-现实的具身智能测评基准，覆盖抓取、组装、精细操作等任务。论文公布的结果里，当前顶尖机器人策略（可能指基于视觉+强化学习的方法）平均得分仅为12.8，而人类达到100。这意味着即使在仿真环境中，机器人操作能力距离实用仍有数量级差距。该基准的优势在于提供标准化硬件与模拟器接口，便于社区横向复现。

> 原文：http://arxiv.org/abs/2607.04434v2

## ICML 2026：中国大厂游轮上抢人才

机器学习顶会ICML 2026已经进入第二天，中国互联网公司（阿里、字节、腾讯、华为等）的展台热闹程度甚至超过微软和Google。除了常规摊位，部分厂商还在会议酒店附近的游轮上举办闭门招待会，直接面向博士生和博士后发放面试邀请。这一现象侧面反映中国AI公司在基础研究人才储备上的紧迫感，也说明当前纯研究导向的论文数量并非招聘唯一门槛——落地经验和动手能力更受青睐。

> 原文：https://www.leiphone.com/category/academic/DiVzwoGAPFZarhqd.html

## OpenAI分析：SWE-Bench Pro有严重噪音

OpenAI发表了一篇题为《Separating Signal from Noise in Coding Evaluations》的分析文章，直接指出SWE-Bench Pro（一个软件工程编码基准）存在显著的噪音和可靠性问题。例如，测试用例覆盖不全、环境配置差异导致分数波动、以及部分任务存在“记忆填充”的捷径。OpenAI呼吁社区重新审视这类编码评测的有效性，并提出了更严谨的评估协议。这将对许多依赖SWE-Bench Pro衡量模型编程能力的团队产生直接影响。

> 原文：https://openai.com/index/separating-signal-from-noise-coding-evaluations

## NVIDIA发布Audex：统一音频与文本的30B模型

NVIDIA推出的Audex（Nemotron-Labs-Audex-30B-A3B）是一种混合架构模型，能在音频理解（语音识别、声纹识别）、音频翻译（语音到文本跨语言）、音频生成（文本到语音、情绪语调合成）之间切换，同时保留其主干模型（可能是Llama或Nemotron家族）的文本智能。关键创新在于“保持文本智能”——即音频任务不降低下游语言能力。30B激活参数但总参数可能更大，适合边缘部署。

> 原文：https://www.marktechpost.com/2026/07/07/nvidia-releases-audex-nemotron-labs-audex-30b-a3b-a-unified-audio-text-llm-that-preserves-the-text-intelligence-of-its-backbone/

## Anthropic研究：语言模型中的全局工作空间机制

Anthropic在一篇新论文中提出，语言模型内部可能存在类似于认知科学中“全局工作空间”的机制——一个可被所有模块访问的共享信息缓冲区，用于协调长程推理和跨任务迁移。他们通过干预实验发现，注意力层中的某些特定节点承担了类似“黑板”的角色，丢弃这些节点会导致模型在需要跨步推理的任务上显著恶化。这项工作为理解Transformer的“思考过程”提供了新的可解释性视角。

> 原文：https://www.anthropic.com/research/global-workspace

## 翁荔总结35篇论文：自我进化AI的Harness工程

前OpenAI研究科学家Lilian Weng（翁荔）发布了一篇长文，系统总结了35篇关于“自我进化AI”的论文，并将主题提炼为“Harness Engineering”——即如何设计评估、约束和安全机制让AI在自我迭代中不偏离目标。她提出了一个分类框架：从内部监督信号到外部交互反馈，再到分布外泛化控制。这篇文章是近期该方向最全面的文献综述，适合希望快速入门的从业者。

> 原文：https://www.latent.space/p/ainews-lilian-weng-summarizes-35

---

今天的论文扎堆指向一个问题：当AI试图从“人工标注”走向“自我进化”和“真实世界操作”时，我们是否真的准备好了衡量它的尺子？