# DeepSeek 发力视觉，Flash 对标 Opus 4.8

今天该板块最值得关注的是 DeepSeek 的 Flash 视觉模型：它在智能体基准上对标 Opus 4.8，但定位明显是「平价可用」而非「顶配炫技」。我的判断是，多模态竞争已经进入下沉阶段，接下来拼的是成本、易用性和生态适配。以下按重要性梳理今日 6 条发布。

## DeepSeek Flash：多模态能力对标 Opus 4.8

DeepSeek 发布实验性 Flash 视觉模型，主打多模态理解与智能体（agentic）场景，在智能体基准测试上可以媲美 Opus 4.8。「实验性」意味着团队还在快速迭代，未到稳定定版阶段。

关键点在于「下沉」：去年多模态还是旗舰模型的专属能力，现在被放进 Flash 这样更轻量、更便宜的产品线里。对开发者来说，这意味着构建视觉 agent 的门槛进一步降低，也意味着 DeepSeek 正在把资源押注到 agentic 这条赛道。

为什么重要：模型竞争的战场正从「谁的参数多」转向「谁能让 agent 跑得更稳更省」。Flash 如果真能在成本可控的前提下接近 Opus 4.8，有可能挤压一批依赖闭源 API 的多模态玩家。

> 原文：[The Decoder](https://the-decoder.com/deepseek-releases-experimental-flash-vision-model-that-rivals-opus-4-8-on-agent-benchmarks/)

## Liquid AI DSpark：草稿模型推理提速 3.18 倍

Liquid AI 发布约 3 亿参数的草稿模型 DSpark，配合投机解码（speculative decoding）使用，让 LFM2.5 的推理速度最高提升 3.18 倍，且输出与原始模型完全一致。

关键点：这是一个「加速器」而不是独立模型。草稿模型先快速生成候选 token，再由大模型验证，属于经典的投机解码路线。把 DSpark 单独拆出来开源，意味着开发者不需要动 LFM2.5 本身，就能拿到近乎无损的速度收益。

为什么重要：推理成本是模型规模化落地的最大瓶颈之一，尤其在高并发 agent 场景下。3.18 倍的速度提升，对生产环境的成本账有明显影响，也让 Liquid AI 在效率型模型里抢到一个差异化位置。

> 原文：[Hugging Face](https://huggingface.co/blog/LiquidAI/lfm25-dspark)

## Meta 开源可本地部署的视觉智能体模型

Meta 发布了支持视觉理解与工具调用的开源智能体模型，最大特点是可完全本地部署。官方强调它适合隐私敏感的终端场景，尤其是需要数据不出域、安全审计较严格的场景。

关键点：和云端 API 路线不同，这类模型的价值在于「不出域」——数据不需要离开本地环境，合规压力更小。视觉 + 工具调用意味着它不只是看图片，还能执行动作，具备 agent 的基本形态。

为什么重要：开源 + 本地部署的组合，让中小团队也有机会搭建自己的多模态 agent，而不是被锁定在闭源 API 上。Meta 继续押注开源生态，背后是对开发者分发渠道的争夺。

> 原文：[InfoQ 中文](https://www.infoq.cn/article/aGfkSN1YlmLrUQMPea9L)

## 商汤开源 SenseNova U1.5 Lite

商汤发布并开源轻量多模态大模型 SenseNova U1.5 Lite，两个卖点最突出：一是支持超长指令输入，二是能原生生成 4K 真实视觉内容。

关键点：「原生生成 4K」区别于后处理放大，意味着模型在生成阶段就具备高分辨率输出能力，对高清视觉素材类任务更直接。超长指令则让它在复杂任务描述、多轮编辑类场景里更可用。

为什么重要：SenseNova 系列走的是开源 + 轻量路线，目标显然是端侧、私有化部署和行业定制。相比通用对话模型，这类垂直能力更容易在 B 端找到付费场景。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/6sNCkUYytWV6ixlf.html)

## GPT-Image-2 新增透明背景生成

OpenAI 的 GPT-Image-2 新增无背景图像生成能力，可以直接输出透明背景的图片，省掉后期抠图这一步。

关键点：透明背景是设计素材的基本需求——图标、贴纸、电商图、版式设计都离不开。以前生成式模型要先出一张完整图，再靠工具抠图；现在从生成端直接解决，工作流短了一截。

为什么重要：这个功能不炫目，但很实用。AI 图像生成竞争正从「能画得多惊艳」转向「能不能直接进工作流」，GPT-Image-2 在往生产力工具方向做产品迭代。

> 原文：[The Decoder](https://the-decoder.com/openais-gpt-image-2-can-now-generate-images-without-a-background/)

## 神秘模型 Ox Alpha 现身 OpenRouter

OpenRouter 上出现一个未公开的模型 Ox Alpha，跑分超过 Fable 5，但发布方完全未知。目前网友已经开始猜测厂商，智谱和小米被反复提及——不过都只是猜测，没有任何官方信息。

关键点：匿名上架 + 高跑分，通常意味着测试或造势。这类事件最终有两种结局：要么是知名实验室的新版本提前流出，要么是能力验证不足、不了了之。

为什么重要：如果 Ox Alpha 对应到某家国内实验室，说明国内模型的能力已经接近甚至局部超越头部闭源模型。但在官方确认之前，跑分只能当作一个信号，不值得过度解读。

> 原文：[InfoQ 中文](https://www.infoq.cn/article/3MNJh5F34GSsRQJJWJzY)

今天 6 条发布指向同一个信号：竞争焦点已经不再是谁的模型更大，而是谁的模型更便宜、更快、更好落地。留一个问题给你：跑赢 Fable 5 的 Ox Alpha，到底是谁家的？