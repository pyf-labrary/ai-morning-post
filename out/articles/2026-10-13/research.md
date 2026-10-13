# 今天的 AI 研究：可验证、能自我改进，但别急着组队

## 导语

今天的六篇研究里，最值得看的是 DeepMind 的 AlphaProof Nexus——它解出的数学题通过了同行评审，这在 AI 数学推理领域是稀缺的「可验证」成果。与此同时，三篇关于自改进与多智能体的研究给出了同一个方向的冷水：能力提升真实存在，但自我认知的天花板和多智能体的 token 浪费同样真实。对做产品的人来说，今天的关键词是「成本核算」而不是「能力幻想」。

## AlphaProof Nexus 解出数十道开放数学题，且过了同行评审

Google DeepMind 的 AlphaProof Nexus 解决了数十个此前未被解决的数学问题，成果通过了同行评审。这一点比「解出多少题」更重要——AI 生成数学结果的新闻近年不少，但多数停留在预印本或未经独立验证阶段，能进入正式评审流程的很少。

关键点在于「可验证性」。数学是少数能对 AI 输出做严格判定的领域，因此它常被当作推理能力的试金石。AlphaProof Nexus 的进展如果经得起后续复现，说明形式化推理与搜索的结合正在从竞赛题走向真正的开放问题。

为什么重要：对研究机构和投资人来说，这是一个可被第三方核验的能力信号，而不是又一份自我评估报告。它也提示了一条路线——把 AI 放进有明确判定标准的领域，比在开放对话里比分数更能说明问题。

> 原文：[The Decoder](https://the-decoder.com/google-deepminds-alphaproof-nexus-solved-dozens-of-open-math-problems-and-actually-got-peer-reviewed/)

## 华为用 RSI 通关 25 款游戏，操作次数少 56%

华为团队采用递归自我改进（RSI，recursive self-improvement）方法，让 AI 通关了 25 款游戏，操作次数比人类少 56%，在部分场景下已不再需要调用大模型。

关键点有两个。一是效率：操作次数少 56% 意味着策略更精简，而不是靠暴力搜索堆算力。二是「不再需要调用大模型」——这说明部分能力已经被内化到更小的策略里，推理开销可以下降。

为什么重要：如果自我改进的产出能被固化下来，agent 的边际推理成本就有下降空间。这与今天另一篇 Sakana AI 的结论形成对照：自我改进能变强，但强在哪里、强到什么程度，需要分开看。

> 原文：[量子位](https://www.qbitai.com/2026/10/502654.html)

## Sakana AI：越会解题，越看不到自己的盲区

Sakana AI 的自改进模型在解题和自我评判两个维度上持续变强，但研究发现它无法识别自身的盲点，递归自我提升存在能力天花板。

关键点是「解题能力」和「自我评判能力」同步提升，却没有带来「发现盲区」的能力。这其实符合直觉：评判标准如果由模型自己生成，它只能在自己已知的空间里打分，看不见的部分永远打不到分。

为什么重要：这给所有基于自我博弈、自我评分（self-reward）的训练路线提了个醒——外部信号不可省。纯靠模型自我循环，收敛到的是自身认知的上限，而不是任务的上限。

> 原文：[The Decoder](https://the-decoder.com/sakana-ais-self-improving-model-gets-better-at-solving-and-judging-but-cant-catch-its-own-blind-spots/)

## 多智能体组队：token 烧掉一大截，质量几乎没动

一项新研究发现，让多个 AI agent（智能体）组队协作会消耗远超单体的 token，但带来的质量提升几乎可以忽略，多智能体并非普遍更优解。

关键点在于成本与收益的严重不对称。多智能体架构通常需要额外的通信、协调和结果汇总环节，这些环节本身就是 token 消耗大户，而它们并不直接贡献答案质量。

为什么重要：过去一年「多智能体」被当成默认的进阶方案写进不少架构图。这项研究给出的判断是，它应该是一个需要论证的选项，而不是默认配置。选型时先问：这个任务真的需要多个视角，还是只是单体 prompt 没调好？

> 原文：[The Decoder](https://the-decoder.com/ai-agent-teams-waste-massive-tokens-for-barely-measurable-quality-gains-research-finds/)

## 微软：清空对话历史，agent 反而找到更好的解法

微软研究团队发现，在上下文中有意识地丢弃历史对话（fork and flush）能帮助 AI agent 找到更好的解法。长上下文并非越长越好。

关键点是「历史即噪声」。累积的对话里包含大量已被否决的尝试、无关的中间步骤和过时的假设，它们会持续影响后续决策，把模型锚定在早期的错误路径上。果断 fork 出新分支并清空历史，等于强制重新思考。

为什么重要：这与业界「上下文窗口越大越好」的叙事相反。对 agent 产品的启示是，上下文管理应该包含主动删除策略，而不只是扩容和检索。什么时候该清空，可能比塞进什么更值得调。

> 原文：[The Decoder](https://the-decoder.com/clearing-chat-history-helps-ai-agents-find-better-solutions/)

## 阿里 Qwen 推出 QwenGyre 弹性 RL 框架

阿里 Qwen 团队推出 QwenGyre，一个面向超长程 agent 训练的弹性强化学习（RL，reinforcement learning）框架，通过在线 RL 训练编码类智能体。

关键点是「超长程」与「弹性」。编码任务往往跨越大量步骤，奖励信号稀疏且延迟，这对训练框架的稳定性和资源调度提出更高要求。QwenGyre 的定位正是补这一块基础设施。

为什么重要：模型能力之外，训练框架正在成为 agent 落地的一环。谁能让长程任务上的 RL 跑得更稳、更省，谁就更容易把编码 agent 从 demo 推到可用。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/12/alibaba-qwen-introduces-qwengyre-elastic-reinforcement-learning-rl-for-xlong-horizon-agents/)

## 结语

今天的研究串起来是一个提醒：能力在涨，但涨的地方和想象中的不一样。如果让你选，你会先砍掉多智能体架构，还是先给 agent 加上「主动遗忘」？