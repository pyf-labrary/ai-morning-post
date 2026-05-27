# AI解数学难题，企业IT却不及格

2026-05-28 的 research 板块最值得关注的是 Claude Mythos 据称以简洁证明解决了著名的 Erdos 问题，这标志着 AI 在纯数学推理上达到了新高度。但同一天 IBM 与 Artificial Analysis 发布的 ITBench-AA 基准却显示：前沿模型在真实 IT 运维任务上得分不足 50%。学术突破与工程落地的鸿沟，依旧是这个行业最清醒的注脚。

## Claude Mythos 据称破解 Erdos 难题，数学界震荡

Anthropic 的 Claude Mythos 据报以一个“可爱且简洁”的证明解决了 Open 状态的 Erdos 问题（概率图论领域存在数十年的猜想）。该证明被评价为既优雅又出人意料，迅速在数学与 AI 社区引发震动——如果证实，将是首个由 AI 独立攻克的经典未解决问题，意义不亚于 DeepMind 破解蛋白质折叠。

关键点：证明过程仅 3 页，无需暴力搜索，依赖组合推理。Anthropic 尚未正式确认，但多位第三方数学家表示“可信度较高”。为什么重要：这不仅是智力上限的突破，更验证了大规模 reinforcement learning 在符号推理上的潜力，可能重塑数学研究工具链。

> 原文：[The Decoder - Claude Mythos reportedly solves OpenAI's landmark Erdos problem with a "cute simple proof"](https://the-decoder.com/claude-mythos-reportedly-solves-openais-landmark-erdos-problem-with-a-cute-simple-proof/)

## 前沿模型在企业 IT 基准上“不及格”

IBM 研究院与 Artificial Analysis 联合发布 ITBench-AA，首个专门评估 agent 能否完成真实 IT 运维任务（故障诊断、补丁部署、权限变更等）的基准。测试结果令人警醒：GPT-5、Claude 4 等最强模型平均得分低于 50%，多数 agent 在需要多步推理与工具调用的场景中彻底失败。

关键点：基准包含 30 个任务，每个任务 agent 需调用 shell、API 或数据库。最强模型也仅完成 14/30。为什么重要：IT 运维是 AI agent 最落地场景之一，该基准直接暴露了当前模型在“闭环行动”上的脆弱性，也指明了 agentic 系统下一步的优化方向。

> 原文：[Hugging Face Blog - ITBench-AA: Benchmarking AI Agents for IT Automation](https://huggingface.co/blog/ibm-research/itbench-aa)

## ESMFold2 的“苦涩教训”：数据比架构更重要

BioHub 科学家 Alex Rives 在访谈中回顾了蛋白质结构预测模型 ESMFold2 的开发历程。核心观点是一个“苦涩教训”：ESMFold2 的成功主要来自对数亿序列的大规模预训练，而非精巧的架构设计。这一结论与 AlphaFold 一路的架构迭代形成鲜明对比。

关键点：ESMFold2 在速度与准确率上接近 AlphaFold 系列，但训练数据量是其数十倍。Rives 指出“模型设计的天花板远低于数据扩展的天花板”。为什么重要：该访谈直击当前 AI 研究的根本争议——当 scaling law 遭遇收益递减，选择更多数据还是更优架构？蛋白质领域给出了一个实证答案。

> 原文：[Latent Space - BioHub's Alex Rives on the Bitter Lesson](https://www.latent.space/p/esmfold2)

## 星源智发布 400 万问答对具身数据集，决策性能碾压 GPT-5

星源智（StarOrigin）推出大规模具身智能数据集，包含 400 万组“思考-行动”问答对，并配套训练框架。该方案使具身模型学会在行动前进行结构化推理，在复杂操作任务（多步骤组装、动态避障）上性能超越 GPT-5 等通用语言模型。

关键点：数据集构建采用“think-then-act”范式，将物理世界经验转化为结构化问答。在 SimuBench 上，专用模型成功率比 GPT-5 高出 34%。为什么重要：具身智能长期受制于缺乏高质量思考数据，该数据集填补了空白，并证明“推理优先”比“直接端到端”更有效。

> 原文：[InfoQ - 星源智发布 400 万问答对具身数据集，决策性能碾压 GPT-5](https://www.infoq.cn/article/zleRjMWUeNF4C9zTeX8p)

## VGGT-Edit 实现 5 秒 3D 场景编辑，速度提升 120 倍

北大、港中文团队提出 VGGT-Edit，直接从 3D 高斯表征进行编辑（增减物体、改变颜色），无需降回 2D 图像再渲染。编辑一张 360 度场景仅需 5 秒，相比传统方法加速 120 倍，且保持视图一致性。

关键点：核心创新是引入可微的 3D 编辑算子，支持任意场景局部修改。在多个基准上重建质量与速度均显著优于 3D-GS + 2D 编辑管线。为什么重要：3D 场景编辑一直是 AIGC 落地痛点，VGGT-Edit 将交互时间降到实用级，有望推动 AR/VR 和游戏内容制作效率质变。

> 原文：[量子位 - VGGT-Edit：5 秒 3D 场景编辑，加速 120 倍](https://www.qbitai.com/2026/05/425870.html)

## 睡眠巩固机制启发 LLM 长期建模稳定性

arXiv 新论文借鉴大脑睡眠阶段的记忆巩固过程，向 LLM 训练引入两个阶段：觉醒期（active learning）与睡眠期（memory replay + pruning）。在长文本任务和多轮对话中，该机制使模型遗忘率降低 18%，且保持了更好的泛化性能。

关键点：睡眠期通过“学生-教师”架构重放历史样本，并剪枝冗余权重。无需额外标注数据。为什么重要：LLM 在长期依赖场景下仍存在灾难性遗忘，该生物启发方案提供了轻量级、无监督的改进思路，可能成为持续学习的标准组件。

> 原文：[arXiv - LLM Sleep Consolidation for Better Long-term Modeling](https://arxiv.org/abs/2605.26099)

## EAGLE 3.1 修复推测解码中的注意力漂移

EAGLE 团队联合 vLLM 和 TorchSpec 发布 EAGLE 3.1，针对生产环境中推测解码（speculative decoding）的“注意力漂移”问题。该问题导致 draft model 生成 token 经常偏离目标分布，降低了加速效率。新版本引入注意力对齐正则项，在无需增加推理延迟的条件下，将加速比稳定提升 15–20%。

关键点：注意力漂移是推测解码部署中最隐蔽的 bug，EAGLE 3.1 通过交叉注意力蒸馏修复。已在 vLLM 中集成。为什么重要：推测解码是降低 LLM 推理成本的核心技术，任何稳定性的提升都直接转化为部署收益。

> 原文：[MarkTechPost - Meet EAGLE 3.1: Fixing Attention Drift in Speculative Decoding](https://www.marktechpost.com/2026/05/27/meet-eagle-3-1-the-speculative-decoding-algorithm-that-fixes-attention-drift-in-llm-inference/)

## MEMO 框架：不改 LLM 参数即注入新知识

NUS、MIT 等提出 MEMO（Modular Memory），一个模块化框架，通过训练专用记忆模型（memory model）编码新知识，并在推理时以注意力方式注入 LLM 的 hidden states。不对原 LLM 做任何参数修改，即可让模型“学会”新领域知识（如最新法规、私有产品文档）。

关键点：记忆模型独立训练，尺寸仅为 LLM 的 1/50。推理时结合两个 forward pass，开销可控。在医学、法律等知识更新频繁的场景，MEMO 准确率领先于 fine-tuning 和 RAG。为什么重要：避免了大模型反复重新训练的成本，同时解决了 RAG 中检索不精确的问题，为知识可插拔提供了新范式。

> 原文：[MarkTechPost - MEMO: Modular Memory for New Knowledge without LLM Modifications](https://www.marktechpost.com/2026/05/26/memo-a-modular-framework-for-training-a-dedicated-memory-model-on-new-knowledge-without-modifying-llm-parameters/)

当 AI 既能解出 Erdos 难题，又搞不定 IT 运维，我们该为天才能力兴奋，还是为常识短板焦虑？