# AI Agent 自主工作26分钟，搜索仅33秒

哈佛与 Perplexity 的最新联合研究揭示了 AI Agent 与传统搜索在自主工作时长上的巨大鸿沟——单会话平均26分钟 vs 33秒。这一差异不仅是速度对比，更指向 agentic 工作流在复杂任务中的代际优势，但成本与可靠性仍需验证。

## 哈佛与 Perplexity 研究：AI Agent 自主工作时间是搜索的47倍

这项配对实验由哈佛大学和 Perplexity 联合开展，测量 AI Agent 在每会话中无需人工干预的自主工作时间。结果显示，AI Agent 平均能连续自主工作26分钟，而传统搜索引擎仅有33秒。关键点在于，Agent 不仅能自主分解任务、调用工具，还能在长流程中保持上下文一致性。为什么重要？这标志着 AI 从“信息检索”转向“任务执行”的能力跃升，但相应的计算成本和潜在错误率也需企业级评估。

> 原文：[A New Study from Harvard and Perplexity Finds AI Agents Perform 26 Minutes of Autonomous Work Per Session vs 33 Seconds for Search](https://www.marktechpost.com/2026/06/08/a-new-study-from-harvard-and-perplexity-finds-ai-agents-perform-26-minutes-of-autonomous-work-per-session-vs-33-seconds-for-search/)

## Latent Space 发布 FrontierCode 代码质量基准

Latent Space 推出的 FrontierCode 基准，旨在评估 AI 模型生成代码的**质量**而非数量。此前多数基准关注通过率或执行正确性，FrontierCode 则引入可维护性、可读性和架构合理性等维度。关键点：它覆盖20+主流编程语言，并包含人工专家标注的评分数据集。意义在于，当模型在数量指标上趋于饱和时，质量维度的评测将成为区分模型实际工程能力的标尺——尤其对采纳 AI 辅助开发的团队有直接参考价值。

> 原文：[Latent Space: FrontierCode Benchmarking](https://www.latent.space/p/ainews-frontiercode-benchmarking)

## 微软 Lens 研究：详细描述比原始规模更重要

微软研究院通过 Lens 实验证明，训练高效图像生成器时，**详细的标题描述**（dense captions）对最终效果的影响远超单纯扩大模型参数规模。实验对比了不同规模模型在有无精细描述下的生成质量，发现大规模模型若无精细描述，其输出在细节一致性和语义对齐上显著弱于小模型+高质量描述。这意味着，对初创公司和成本敏感团队而言，提升数据标注质量可能是比堆算力更经济的优化路径。

> 原文：[Microsoft Research’s Lens Proves Detailed Captions Matter More than Raw Scale for Training Efficient Image Generators](https://the-decoder.com/microsoft-researchs-lens-proves-detailed-captions-matter-more-than-raw-scale-for-training-efficient-image-generators/)

当 Agent 自主工作逼近半小时，代码评测转向质量，图像生成依赖描述而非参数量——这三条研究共同指向一个信号：AI 的下半场，精细化比粗放扩张更重要。你的团队，准备好切换衡量维度了吗？