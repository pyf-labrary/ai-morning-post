# Blackwell领跑Agentic基准，微软用Markdown优化GPT-5.5

今天最值得关注的事是首个针对代理 AI（agentic AI）的标准化基准 AgentPerf 发布，NVIDIA Blackwell 在首批结果中拔得头筹。与此同时，Google 的 Gemini-SQL2 在 Text-to-SQL 基准上大幅刷新纪录，微软则用一种几乎零成本的方法——训练一个小型 Markdown 文件——提升了 GPT-5.5 的推理能力。三者指向同一趋势：评估和效率正成为模型竞争力的新入口。

## NVIDIA Blackwell 在 AgentPerf 基准测试中领跑

Artificial Analysis 发布 AgentPerf，这是业界首个专门衡量代理 AI 系统（agentic AI system）性能的基准。首批结果中，NVIDIA Blackwell 平台表现最佳，为开发者提供了从延迟、吞吐量到任务完成率的统一对比标尺。

**关键点**：AgentPerf 不只测模型，还测调用链和工具使用。Blackwell 的优势在于推理优化与生态适配。

**为什么重要**：随着 agentic 应用从实验走向生产，缺乏量化标准正在拖慢部署。AgentPerf 填补了这一空白，Blackwell 的领跑意味着 NVIDIA 延续了其硬件+软件捆绑策略在代理场景的有效性。

> 原文：[NVIDIA Blog](https://blogs.nvidia.com/blog/nvidia-blackwell-agentperf-artificial-analysis/)

## Gemini-SQL2 登顶 BIRD 单模型排行榜

Google Research 推出的 Gemini-SQL2 在 BIRD Text-to-SQL 基准上达到 80.04% 执行准确率，大幅领先此前最佳结果。该模型基于 Gemini 3.1 Pro 微调，专门针对自然语言到数据库查询的转换任务。

**关键点**：BIRD 是业界公认最难的 Text-to-SQL 基准之一，80% 的准确率是里程碑式突破。Gemini-SQL2 未使用多模型集成或外部工具，单模型即实现这一结果。

**为什么重要**：Text-to-SQL 对于企业级数据查询自动化至关重要。Gemini-SQL2 的进步意味着 Google 在自然语言与结构化数据交互领域已构筑显著的技术壁垒。

> 原文：[The Decoder](https://the-decoder.com/google-researchs-gemini-sql2-tops-text-to-sql-benchmarks-by-a-wide-margin/)

## 微软 SkillOpt：用一个训练过的 Markdown 文件优化 GPT-5.5

微软发布 SkillOpt 技术，核心思路是训练一个仅数百 KB 的 Markdown 文件，作为“推理提示”输入给 GPT-5.5，从而显著提升其在数学、推理等任务上的表现，整个过程不修改模型权重。

**关键点**：Markdown 文件内部编码了推理策略和上下文范例，本质上是一种可学习的、轻量级的任务引导。微软团队称在某些基准上，性能提升超过 10%，且部署成本几乎为零。

**为什么重要**：这是“提示工程”的延伸，但更加系统化。如果只需微调一个文本文件就能改进顶级模型，那么未来模型更新的瓶颈可能从“训练”转移到“如何设计引导文件”。SkillOpt 可能让大模型的能力更高效地被“租赁”而非“重训”。

> 原文：[The Decoder](https://the-decoder.com/microsofts-skillopt-boosts-gpt-5-5-by-using-nothing-but-a-trained-markdown-file/)

## HuggingFace 发布 Olmo-Eval：模型开发评估工作台

Allen AI 与 HuggingFace 合作推出 Olmo-Eval，旨在为模型开发循环（training loop）提供一体化的评估工作台。开发者可以快速在不同阶段、不同基准上测试模型，并可视化性能变化。

**关键点**：Olmo-Eval 开源，支持多任务并行评估，并内置了多种社区基准（如 MMLU、HellaSwag 等）。主要面向模型研发团队，帮助他们更早发现训练中的退化或偏差。

**为什么重要**：模型训练是昂贵的试错过程，Olmo-Eval 降低了“评估”的门槛，让开发者能像调试代码一样调试模型行为。这有助于缩短开发周期，尤其适合中小型实验室。

> 原文：[HuggingFace Blog](https://huggingface.co/blog/allenai/olmo-eval)

---

当基准测试和效率工具密集落地时，模型的能力分化将不再只靠参数量，而是比拼谁的系统更“可测”、更“可优”。明天，你会用什么标准来判断自己的 agent 够不够好？