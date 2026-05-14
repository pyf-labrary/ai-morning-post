# Hermes自改进Agent开源，腾讯降本61%

今天开源工具板块最值得关注的，是两件事：NVIDIA 支持的 Hermes Agent 框架获 14 万 GitHub Star，实现了 Agent 的自改进能力；腾讯同步开源了 Agent 记忆技术，在任务成功率提升的同时将 Token 消耗降低 61%。两者从不同维度指向同一个趋势：Agent 工程化正在从“可用”走向“高效可用”，自演进能力和成本控制将成为下一阶段竞争的核心指标。

## Hermes Agent：14 万星的自改进 AI Agent

Hermes Agent 基于 NVIDIA RTX 和 DGX Spark 平台，提供一套自改进机制的 AI Agent 框架。其核心能力是 Agent 在运行过程中能根据环境反馈自动优化自身行为，无需手工调参或重新部署。社区活跃度极高，上线后迅速突破 14 万 Star，反映出开发者对“自我进化型 Agent”的强烈需求。关键点：它不只是一个框架，而是将硬件（NVIDIA RTX/DGX Spark）与软件自学习闭环深度耦合，降低了 Agent 持续优化的门槛。重要性在于，当 Agent 能在生产环境中自主迭代，传统 MLOps 的维护成本结构将被重塑。

> 原文：[https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/](https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/)

## 腾讯开源 Agent 记忆技术，Token 消耗降低 61%

腾讯开源的 Agent 记忆方案，通过优化长期记忆的存取策略，在多个基准任务上实现了成功率提升（具体数值未公布），同时将 Token 消耗平均降低 61%。关键点：记忆是 Agent 长期任务的瓶颈，该方案在不多层记忆之间做压缩与召回，显著减少冗余调用。为什么重要：Token 成本是目前大规模部署 Agent 的主要障碍之一，腾讯的解法直接切中痛点，且开源后有望被快速集成到 LangChain 等生态中，推动 Agent 从 demo 走向业务。

> 原文：[https://www.qbitai.com/2026/05/417753.html](https://www.qbitai.com/2026/05/417753.html)

## Fastino Labs 开源 GLiGuard 300M 安全审核模型

GLiGuard 仅 300M 参数，在内容安全审核任务上匹敌甚至超越 23–90 倍大小的模型（如 7B、27B 规模）。关键点：模型架构采用极度轻量的设计，推理速度极快，适合端侧部署。重要性在于，安全审核模型通常需要大算力和高延迟，GLiGuard 证明了小模型在垂直领域可以达到工业化精度，从而降低平台的内容审核成本。

> 原文：[https://www.marktechpost.com/2026/05/13/fastino-labs-open-sources-gliguard-a-300m-parameter-safety-moderation-model-that-matches-or-exceeds-accuracy-of-models-23-90x-its-size/](https://www.marktechpost.com/2026/05/13/fastino-labs-open-sources-gliguard-a-300m-parameter-safety-moderation-model-that-matches-or-exceeds-accuracy-of-models-23-90x-its-size/)

## Nous Research 开源 Token Superposition 预训练加速

Nous Research 发布的 Token Superposition Training 方法，在 270M 到 10B 参数的模型上实现最高 2.5 倍的预训练加速。关键点：通过在训练阶段将多个 token 的信息叠加到单个位置，减少序列长度对注意力的计算负担，从而提升吞吐。重要性：预训练成本是大模型发展的核心瓶颈，如果能稳定加速 2 倍以上，将大幅降低新模型的入场门槛，尤其利好中小研究团队。

> 原文：[https://www.marktechpost.com/2026/05/13/nous-research-releases-token-superposition-training-to-speed-up-llm-pre-training-by-up-to-2-5x-across-270m-to-10b-parameter-models/](https://www.marktechpost.com/2026/05/13/nous-research-releases-token-superposition-training-to-speed-up-llm-pre-training-by-up-to-2-5x-across-270m-to-10b-parameter-models/)

## agentmemory：AI 编码 Agent 持久内存库

agentmemory 在基于多个基准的 AI 编码 Agent 持久内存方案排名中拿到第一。它提供一种结构化的长期记忆存储机制，让 Agent 能在多次回合中保留上下文并持续复用经验。关键点：不依赖模型上下文窗口，而是通过外挂数据库实现记忆持久化。重要性：编码 Agent 当前最大的痛点之一是任务中断后无法继续，agentmemory 提供了一个轻量级的插件层，可被直接融入现有开源 Agent 工作流。

> 原文：[https://github.com/rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

## superpowers：Agent 技能框架与开发方法论

superpowers 提供一套可组合的 Agent 技能框架，将开发方法定义为“技能”和“能力”的模块化组合，旨在提升编码 Agent 的构建效率。关键点：它更像一种设计模式而非具体实现，适合团队在现有 LLM 上快速搭建具备多步骤推理能力的 Agent。重要性：随着 Agent 应用场景增加，缺乏标准化的开发范式成为效率瓶颈，superpowers 尝试给出方法论层面的参考。

> 原文：[https://github.com/obra/superpowers](https://github.com/obra/superpowers)

## OpenHuman：个人 AI 超级智能开源项目

OpenHuman 旨在提供私密、简单且强大的个人 AI 超级智能，全部代码开源，强调隐私本地化。关键点：项目由 tinyhumansai 团队维护，定位是个人助理 Agent 的终极形态——能长期理解用户并自主完成复杂任务。重要性：在大模型厂商纷纷推出云端个人助手的背景下，OpenHuman 以开源、本地化、隐私保护作为差异化，可能吸引对数据主权敏感的开发者用户。

> 原文：[https://github.com/tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)

## Scientific Agent Skills 科研 Agent 技能集

面向研究、科学、工程、分析等领域的即用 Agent 技能集合，提供现成的工具链，包括文献检索、数据图表解析、实验设计建议等。关键点：每个技能是一个独立的 Agent 模块，可被串接组合成完整的科研工作流。重要性：科研自动化是 Agent 的重要垂直场景，该技能集降低了非工程师研究人员使用 Agent 的门槛，有望加速科研效率提升。

> 原文：[https://github.com/K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

---

当 Agent 学会自我改进且成本骤降，下一个需要攻克的是自动化信任机制——你愿意让一个能自我修改的 Agent 全权代理你的开发任务吗？