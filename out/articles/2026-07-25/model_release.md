# Opus 5 半价对标 Fable 5；FLUX 3 原生音视频

今日最值得关注的是 Anthropic 的定价策略转向：Opus 5 性能逼近旗舰 Fable 5，但输入/输出价格直接腰斩至 $5/百万 token。这释放了一个信号——模型竞争从单纯能力跃升转向 token 效率与性价比博弈。与此同时，Black Forest Labs 的 FLUX 3 首次实现视频+音频原生生成，多模态门槛进一步降低。

## Anthropic Opus 5：性能接近但价格减半，转向效率竞争

**是什么**：Anthropic 今日发布 Claude Opus 5，官方宣称性能接近旗舰模型 Fable 5，但价格仅为后者一半（$5/百万 token）。Opus 5 并非全新架构，而是基于 Fable 4 的优化版本，重点提升推理速度和内存效率。

**关键点**：定价策略从“算力堆砌”转向“成本可控”。Anthropic 在博客中强调，Opus 5 在复杂推理、代码生成等任务上比 Fable 4 有 20%-30% 的提升，但不再是“更大更强”的老路。对手 OpenAI 和 Google 的旗舰模型定价仍在 $10-15/百万 token 区间，Opus 5 可能倒逼行业调价。

**为什么重要**：对于预算敏感的企业客户，Opus 5 提供了“准旗舰”能力而成本减半，可能加速模型替代决策。这也暗示模型即服务（MaaS）市场正在从“跑分竞赛”转向“每百万 token 价值”的竞争。

> 原文：[TechCrunch](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)

## Black Forest Labs FLUX 3：视频+音频原生生成，20 秒长片段

**是什么**：黑森林实验室发布 FLUX 3 多模态模型，首次支持最长 20 秒视频生成并同步输出音频，无需后期配音。此前同类视频生成模型（如 Runway Gen-3）均需独立生成音频后对齐。

**关键点**：FLUX 3 采用统一 latent space 处理视频帧和音频波形，实现时间轴精确同步。官方演示显示，场景中物体碰撞、风吹树叶等动作的音频细节自然匹配。模型支持文字或图像输入，生成分辨率可达 1080p。

**为什么重要**：原生音频能力解决了视频生成的“音画不同步”痛点，对短视频、广告、游戏资产制作等行业意义明确。这是多模态模型在“视听一致性”上的一次实质性突破，可能推动更多创意工具转向端到端生成。

> 原文：[The Decoder](https://the-decoder.com/flux-3-generates-videos-with-native-audio-up-to-20-seconds-long-a-first-for-black-forest-labs/)

## 德国 AI 联盟开源 Soofi S：30B 参数，英德双语登顶

**是什么**：德国 AI 研究所联合发布开源模型 Soofi S，参数量 30B，在英语和德语多项基准测试（如 MMLU、HellaSwag、GermanBench）中取得 SOTA 成绩，超越同等尺寸的 Llama 3 和 Mistral 等模型。

**关键点**：Soofi S 基于改进的混合专家架构（MoE），训练数据中德语占比约 25%，同时保持了英语竞争力。模型以 Apache 2.0 许可证开源，支持商用。官方称其推理速度比 Llama 3 70B 快 2 倍，内存占用减少 40%。

**为什么重要**：欧洲在开源大模型领域持续发力，Soofi S 为德语 NLP 提供了高质基线，同时验证了 MoE 架构在小参数量下的效率潜力。对于需要多语言（尤其德语）本地部署的企业，这是一个值得关注的开源选项。

> 原文：[The Decoder](https://the-decoder.com/german-ai-consortium-releases-soofi-s-an-open-30b-model-that-tops-benchmarks-in-both-english-and-german/)

## Poolside Laguna S 2.1：小模型编程“拳打”大模型

**是什么**：Poolside 发布开源轻量级编程模型 Laguna S 2.1，参数规模未公开（推测<7B），但在多项编程基准（HumanEval、MBPP、SWE-bench）中超越同尺寸模型，甚至接近部分 13B-30B 模型表现。

**关键点**：模型针对代码补全、bug 修复、代码生成等场景优化，采用大量合成数据微调，推理速度适合本地 IDE 环境。官方强调其“幻觉率”比竞品低 30%。模型以 MIT 许可证开源，支持离线部署。

**为什么重要**：编程助手是当前最落地的 AI 应用之一，Laguna S 2.1 证明小模型通过定向优化可以达到实用水平，降低了对云端推理的依赖。对于注重数据隐私或延迟的开发者，这是一个成本极低的替代方案。

> 原文：[The Decoder](https://the-decoder.com/poolsides-laguna-s-2-1-is-a-small-open-weight-coding-model-that-punches-well-above-its-size/)

今天模型发布的共同主题是“效率优先”——无论是 Anhtropic 的定价调整、FLUX 的音视频同步，还是两个开源模型的小参数高性能。当能力增长趋缓，下一个季度是否会迎来一轮价格战？