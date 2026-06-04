# Gemma 4 12B 与 MAI-Thinking-1 同日发布

今天模型发布板块迎来两大重磅：Google Gemma 4 12B 让多模态模型落地笔记本，微软 Build 2026 推出完全自研的 MAI-Thinking-1 推理模型性能追平 Claude Opus 4.6。开源轻量化与自研推理两条路线同时在加速，值得跟进的是边缘部署边际成本能否真正打平云端。

## 笔记本跑 Gemma 4 12B，多模态门槛再降

Google DeepMind 发布 Gemma 4 12B，采用无编码器设计，直接支持多模态输入（图像、文本），只需 16GB 内存即可在笔记本上运行。Ars Technica 等媒体称其“极强的性价比”——12B 参数规模下，性能对标上一代 30B+ 级别模型。这意味着开发者和中小企业可以用消费级硬件本地部署多模态推理，无需 GPU 集群。

> 原文：[Introducing Gemma 4 12B | Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/)

## 微软 MAI-Thinking-1：从零训练的推理模型追上第一梯队

微软在 Build 2026 上推出 MAI 系列，其中最受关注的是 MAI-Thinking-1，完全从零训练（非基于开源架构），在推理基准上追平 Claude Opus 4.6。该模型定位长链条推理场景（数学、代码、科学分析），微软同时发布了 MAI 家族其他尺寸模型，覆盖端侧至云端。关键点：这是微软第一次在基础模型上达到竞品头部水平，且训练策略完全自研，产业链意义大于单点性能。

> 原文：[微软Build 2026发布MAI-Thinking-1 | InfoQ](https://www.infoq.cn/article/StrGjRRmFKm4fXCvLOSP)

## OpenAI 升级 GPT-Rosalind，深入生命科学

OpenAI 为 GPT-Rosalind（科学专用版本）新增生物学推理、药物化学和基因组学分析能力。该模型在分子性质预测、蛋白质结构理解等任务上有所增强，直接面向制药与科研场景。重要性在于 OpenAI 开始将通用大模型能力拆解为垂直科学工具，而非仅依靠 API 通用调优。

> 原文：[Introducing new capabilities to GPT-Rosalind | OpenAI](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind)

## xAI Grok Imagine 1.5 支持图生视频

xAI 更新 Grok Imagine 图像生成模型至 1.5 版本，新增图像到视频生成能力，最高 720p 分辨率。这是一个相对较小的迭代，但图生视频是当前多模态生成的热点方向，xAI 选择在分辨率上做到 720p（而非竞品的 1080p 或更高），表明其更关注生成速度与可用性。

> 原文：[xAI updates Grok Imagine to 1.5 with image-to-video generation | The Decoder](https://the-decoder.com/xai-updates-grok-imagine-to-1-5-with-image-to-video-generation-at-720p-resolution/)

## Ideogram 4.0 开源：原生 2K 分辨率与强文本渲染

Ideogram 4.0 以开源权重形式发布，支持原生 2K 分辨率输出，文本渲染能力显著提升。这是文本到图像领域少有的高分辨率开源模型，且在文字（如海报、Logo）生成上比竞品更稳定。对于需要高质量图像生成的开发者，这是一个有吸引力的自托管选项。

> 原文：[Ideogram 4.0 drops as an open-weight model | The Decoder](https://the-decoder.com/ideogram-4-0-drops-as-an-open-weight-model-with-native-2k-resolution-and-improved-text-rendering/)

今天的发布指向同一个问题：当边缘算力足够跑 12B 多模态、开源模型能做 2K 输出、自研推理追上头部——你还会为每一次 API 调用付费吗？