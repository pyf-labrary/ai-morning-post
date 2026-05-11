# 百度 Ernie 5.1 砍掉94%预训练成本

导语：今天最值得关注的，是百度 Ernie 5.1 在预训练成本上砍掉94%的同时，评测成绩仍与头部模型持平。这意味着模型训练的“工程效率”正取代“参数规模”成为下一阶段的核心竞争维度，而不仅仅是又一个新模型发布。

## 百度 Ernie 5.1：预训练成本骤降94%，性能不妥协

百度正式发布 Ernie 5.1 大模型，核心亮点在于预训练成本相比前代降低了94%，但综合性能（MMLU、HumanEval等基准）跻身第一梯队，与GPT-4o、Claude 3.5等持平。百度并未披露成本削减的具体技术路径，但业内人士猜测极可能在数据效率、模型架构或训练并行策略上有显著突破。**关键点**：这不是一个“更大更强”的故事，而是一个“更省更准”的故事——当预训练成本从千万美元级降至百万美元级，大模型商业化的门槛将大幅降低。**为什么重要**：成本是模型即服务（MaaS）的核心壁垒，Ernie 5.1 验证了“低成本顶级模型”的可行性，可能倒逼云厂商重新定价，并加速中小团队入场。

> 原文：[The Decoder](https://the-decoder.com/baidus-ernie-5-1-cuts-94-percent-of-pre-training-costs-while-competing-with-top-models/)

## Interfaze 发布新架构：高精度+大尺度，能否打破Scaling Law瓶颈？

Interfaze 公开了一种名为“Interfaze”的新型模型架构，声称在参数规模十亿至千亿级别上均实现更高精度，与同等参数量的Transformer相比有3%-8%的提升。该架构未采用标准注意力机制，而是引入了一种“稀疏激活门控网络”与“动态维度重组”的组合。**关键点**：Interfaze 强调“高精度 at scale”，即规模越大优势越明显，这意味着它可能找到了一条绕过传统Scaling Law回报递减的路径。**为什么重要**：如果该架构在更大规模（万亿参数）上仍保持线性收益，将改写下一代大模型的技术路线。但社区反馈尚处于早期验证阶段，需关注后续第三方复现。

> 原文：[Interfaze Blog](https://interfaze.ai/blog/interfaze-a-new-model-architecture-built-for-high-accuracy-at-scale)

## Together AI 展示 DeepSeek-V4 百万 Token 推理优化：KV缓存压缩是关键

Together AI 发布技术博文，详解如何在 NVIDIA B200 上为 DeepSeek-V4 实现百万 token 级上下文的高效推理。核心手段包括：KV 缓存压缩（通过量化与稀疏化），前缀缓存复用（对常见 prompt 前缀预计算并缓存），以及注意力计算的算子级优化。**关键点**：百万 token 推理在工程上已非“不可能”，而是“成本与延迟”问题。Together AI 将首次推理延迟压缩至1.5秒内，并实现约80%的缓存命中率。**为什么重要**：长上下文（超长文档、代码库、多轮对话）是 GPT-4-128K 等模型的主要卖点，而 DeepSeek-V4 的百万级推理如果通过系统优化落地，将直接冲击现有长上下文生产方案的成本结构。

> 原文：[Together AI Blog](https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem)

结语：当预训练成本骤降94%、新架构向Scaling Law发起挑战、长上下文推理走向可部署，大模型的竞争已从“参数军备”转向“工程效率”——而你更关心哪个环节的突破？