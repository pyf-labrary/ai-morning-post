# Gemma 4 12B本地跑，模型发布潮再起

今日模型发布板块最值得看的是 Google DeepMind 的 Gemma 4 12B——一个能在 16GB 笔记本上本地运行的多模态模型，标志着高效小模型竞争进入新阶段。与此同时，OpenAI 强化了生命科学专用模型，微软拿出了完全自研的推理模型，开源侧亦有 Ideogram 4.0 贡献原生高清生成能力。以下逐一拆解各看点。

## Google Gemma 4 12B：无编码器架构，16GB 笔记本可运行

Google DeepMind 发布的 Gemma 4 12B 多模态模型，抛弃传统视觉编码器，采用纯解码器架构处理图像与文本。关键点在于：模型权重约 12B 参数，但凭借量化与架构优化，可在 16GB 内存的消费级笔记本上本地推理，同时支持文本和图像输入。这意味着开发者无需昂贵 GPU 即可搭建多模态应用。为什么重要：这是目前开源级别中，能在低端硬件上实现多模态推理的最轻量方案之一，可能加速边缘端 AI 应用的普及。

> 原文：https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/

## OpenAI 升级 GPT-Rosalind：生命科学推理能力增强

GPT-Rosalind 获得生物学推理、药物化学和基因组分析三项新能力。关键点：该模型并非通用版 GPT，而是专门针对生命科学研究场景微调的版本，新增能力覆盖从分子结构理解到基因变异解读。为什么重要：生命科学领域对推理精度要求极高，OpenAI 选择专项提升而非通用迭代，表明其在医疗制药垂直方向上的战略聚焦，可能加速新药发现与个性化医疗。

> 原文：https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind

## 微软 MAI-Thinking-1：从零自研，追平 Claude Opus

微软发布推理模型 MAI-Thinking-1，宣称从零训练（拒绝蒸馏第三方模型），性能追平 Anthropic Claude Opus 4.6。关键点：这标志着微软在自研大模型上的重大决心——不再依赖 OpenAI 的闭源能力，而是构建独立技术栈。为什么重要：如果性能确实持平顶尖闭源模型，MAI-Thinking-1 将打破“微软只会整合，不会自研”的刻板印象，并可能推动企业级推理模型的定价与生态竞争。

> 原文：https://www.infoq.cn/article/StrGjRRmFKm4fXCvLOSP

## xAI Grok Imagine 1.5：图像到视频生成，720p 输出

xAI 更新 Grok Imagine 1.5，新增图像到视频生成功能，输出分辨率达 720p。关键点：此前多数视频生成模型（如 Sora、Runway）支持文本转视频或图像转视频，但 Grok 的选择将多帧一致性与角色保持作为优化方向。为什么重要：720p 分辨率虽不算最高，但对于社交媒体、短视频场景已够用。xAI 在图像生成后迅速补全视频能力，意图打造多模态内容创作闭环。

> 原文：https://the-decoder.com/xai-updates-grok-imagine-to-1-5-with-image-to-video-generation-at-720p-resolution/

## Ideogram 4.0 开源：原生 2K 分辨率，文本渲染改进

Ideogram 发布第四代模型并开源权重，原生支持 2K 分辨率输出，文本渲染质量显著提升。关键点：开源模型的 2K 原生分辨率在行业里少见，直接对标 Midjourney 的付费产出。为什么重要：开源社区获得了一个高质量、高分辨率的文生图基线，对于需要精确文字嵌入（如海报、Logo）的应用场景尤其有价值。Ideogram 选择开源，可能改变图像生成市场的格局。

> 原文：https://the-decoder.com/ideogram-4-0-drops-as-an-open-weight-model-with-native-2k-resolution-and-improved-text-rendering/

## NVIDIA Nemotron 3.5：多模态内容安全审核模型

NVIDIA 推出 Nemotron 3.5 Content Safety，面向企业级多模态 AI 安全审核。关键点：模型可检查图像、文本、代码等内容是否违反安全策略，支持自定义规则。为什么重要：多模态模型落地最大的障碍之一是安全合规，NVIDIA 直接提供审核模型，让企业不必从零构建过滤系统，可能成为 AI 部署的基础设施组件。

> 原文：https://huggingface.co/blog/nvidia/nemotron-3-5-content-safety

结语：今天六款模型横跨本地部署、垂直科学、自研推理、视频生成、开源图像和安全审核，几乎覆盖了 AI 产业链的所有关键节点。一个问题留给你：当小模型在笔记本上就能跑多模态，你还需要租云算力吗？