# 微软图像模型追平谷歌旗舰

今日模型发布板块最值得关注的是微软 MAI-Image-2.5 在多项基准上追平谷歌 Nano Banana 2，图像生成赛道首次出现双雄对峙格局。Stability AI 同步开源轻量级音频模型 Stable Audio 3，让本地化音频生成门槛进一步降低。

## 微软 MAI-Image-2.5 性能持平谷歌 Nano Banana 2

**是什么**：微软发布新一代图像生成模型 MAI-Image-2.5，在 FID、CLIP score 等常见基准测试上取得与谷歌旗舰 Nano Banana 2 同等级别的分数。

**关键点**：这是微软图像模型首次与谷歌顶级模型平起平坐。此前微软在图像领域长期落后于谷歌、OpenAI 和 Stability AI，此次追赶主要依赖其对 Diffusion Transformer 架构的深度优化，而非单纯堆参数量。

**为什么重要**：图像生成进入“可用性”竞争阶段后，性能接近意味着体验差异将更多体现在 prompt 跟随、风格控制等细节，以及产品部署策略。微软可借助 Azure 生态快速落地，对开发者而言多了一个不依赖单一供应商的可靠选择。

> 原文：[The Decoder](https://the-decoder.com/microsofts-mai-image-2-5-pulls-even-with-googles-nano-banana-2-on-benchmarks/)

## Stability AI 开源 Stable Audio 3，轻量模型可本地跑

**是什么**：Stability AI 发布 Stable Audio 3 系列开源模型，包含不同大小版本，最小模型可在 MacBook CPU 上运行，支持音乐与音效生成、音频编辑。

**关键点**：模型使用 Latent Diffusion 架构，生成速度比上一代提升 2–3 倍。开源后开发者可自行微调、部署，无需依赖云端 API。音频编辑功能允许对已有音频进行局部替换或风格转换。

**为什么重要**：在图像与视频模型密集发布的同时，音频生成往往被忽视。Stable Audio 3 的轻量化和开源策略降低了音效/音乐生成的使用门槛，尤其适合游戏、短视频、独立创作者等场景，也为硬件端 AI 助手提供了本地音频能力。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/26/stability-ai-releases-stable-audio-3-a-family-of-fast-latent-diffusion-models-for-audio-generation-and-editing/)

当图像生成不再有绝对“最强”，开发者会优先选择生态绑定最自然的模型，还是代码最开放的模型？