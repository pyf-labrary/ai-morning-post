# 975B开源多模态模型，手机可跑27B推理

今天最值得关注的是 Thinking Machines Lab 发布旗下首款开源模型 Inkling——975B 参数、支持视频和音频理解，直接挑战 Anthropic 和 OpenAI 的闭源模型。与此同时，PrismML 推出 Bonsai 27B，将推理模型压缩到可上 iPhone 运行；阿里更新实时语音模型 Qwen-Audio-3.0-Realtime；Soofi 发布混合 Mamba-Transformer MoE 模型。开源生态正加速向多模态、移动化和架构创新方面拓展。

## Thinking Machines 发布 975B 开源多模态模型 Inkling

**是什么**：Thinking Machines Lab 发布开源多模态模型 Inkling，参数量达 975B，支持视频与音频理解，是其迄今最大开源模型，目标对标 Anthropic 的 Claude 和 OpenAI 的 GPT 系列。  
**关键点**：Inkling 在开源模型中首次将参数规模推至接近闭源前沿（如 GPT-4 水平），且覆盖视频、音频两种模态。团队强调其不是“一刀切”方案，可能更侧重特定场景优化。  
**为什么重要**：这一发布意味着开源社区在模型体量上真正迈入与闭源巨头竞争的门槛。若 Inkling 性能可比肩闭源模型，将大幅降低企业、开发者使用高性能多模态 AI 的成本，并可能重塑市场格局。

> 原文：https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/

## Bonsai 27B：可在手机上运行的开源推理模型

**是什么**：PrismML 发布 Bonsai 27B，一个基于 Qwen3.6-27B 的低比特量化开源推理模型，采用 Apache 2.0 许可，可在 iPhone 等移动设备上本地运行。  
**关键点**：27B 参数的推理模型被压缩至手机端可部署，体现了优秀的工程优化。Apache 2.0 许可允许商用和修改，对开发者友好。  
**为什么重要**：推理模型向小型化、端侧发展，加速 AI 从云端走向边缘。Bonsai 27B 展示了在有限算力下实现强大推理能力的可能，将推动移动端 AI 应用落地。

> 原文：https://the-decoder.com/bonsai-27b-is-a-full-open-reasoning-model-that-fits-on-an-iphone/

## 阿里发布实时语音大模型 Qwen-Audio-3.0-Realtime

**是什么**：阿里巴巴发布 Qwen-Audio-3.0-Realtime 实时语音交互模型，在智商、工具调用、共情能力和双工流畅度上全面升级。  
**关键点**：该模型支持双工（同时说话与聆听）、通过语音控制智能设备，并提升情感理解和响应自然度，专注实时交互场景。  
**为什么重要**：智能音箱、车载语音和客服等场景对实时语音需求旺盛。Qwen-Audio-3.0-Realtime 将进一步增强阿里在语音 AI 领域的竞争力，并为开发者提供更强大的多模态语音能力。

> 原文：https://www.qbitai.com/2026/07/450250.html

## Soofi 发布开源混合 Mamba-Transformer MoE 模型

**是什么**：Soofi 联合体发布 Soofi S 30B-A3B，一个面向德语和英语的开源基础模型，采用 Mamba-Transformer 混合架构和 MoE（混合专家），激活参数仅 3.2B。  
**关键点**：架构创新：结合状态空间模型 Mamba 与 Transformer，MoE 使总参数量 30B 但每次推理只激活 3.2B，提升效率。模型专注德语和英语双语。  
**为什么重要**：混合架构探索为更高效的语言模型提供了新方向。同时，针对德语等小语种的优化，反映出开源社区正在填补非英语模型空白，促进多语言 AI 生态。

> 原文：https://www.marktechpost.com/2026/07/15/soofi-consortium-releases-soofi-s-30b-a3b-an-open-hybrid-mamba-transformer-moe-foundation-model-for-german-and-english/

从 975B 的超大开源到 27B 的手机端推理，模型规模的两端同时迈进——你更看好哪一端对行业的影响？