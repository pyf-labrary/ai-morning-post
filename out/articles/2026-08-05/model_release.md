# 当大模型开始拼工具：今日是Qwen3.8的场

国产模型今日密集放量：阿里 Qwen3.8 发布当天即获海外主流平台接入，编程与 Agent 能力成为主叙事。值得注意的不只是参数，而是「发布即接入」——海外基础设施厂商对头部中国模型的响应速度，已经从「观望」变成「抢位」。

## 阿里 Qwen3.8 双版本齐发，海外平台发布当日接入

阿里巴巴正式发布新一代基座大模型 Qwen3.8 系列，包含 Max（2.4T 参数）与 27B 两个版本，重点强化编程与 Agent 能力。发布当天，OpenRouter、Vercel、DeepInfra 等海外平台即完成接入，速度罕见。

关键点在于 27B 小参数版本：它意味着在同等规模下追求更高代码推理效率，直接面向开发者本地部署与私有化场景。Max 版本则主攻复杂多步任务与工具调用。

OpenRouter 等分发平台的即时接入，说明海外开发社区对 Qwen 系列的权重与 API 有真实需求，中国基座模型在编程场景的竞争力已进入国际主流视野。这是继 DeepSeek 之后又一次「发布即全球化」。

> 原文：[https://www.latent.space/p/ainews-qwen-38-max24t-and-27b-new](https://www.latent.space/p/ainews-qwen-38-max24t-and-27b-new)

## MiniMax-H3 登顶 AI 视频榜，开源权重首次问鼎

MiniMax 发布 H3 系列，成为首个登上 AI 视频生成排行榜榜首的开源权重模型。同时已通过 MLX 支持在苹果芯片上本地运行。

此前 AI 视频生成榜单头部长期被闭源模型占据，开源模型在画面质量与运动一致性上始终差一口气。H3 打破这一格局，且选择开源权重而非仅开放 API，策略上意在抢占开发者生态。

MLX 支持意味着 Mac 用户可直接本地跑视频生成，大幅降低尝鲜门槛。这对独立开发者和中小团队是实质性利好——视频生成不再是只能调用云 API 的黑盒。

> 原文：[https://the-decoder.com/chinas-minimax-h3-is-the-first-open-model-to-top-an-ai-video-ranking/](https://the-decoder.com/chinas-minimax-h3-is-the-first-open-model-to-top-an-ai-video-ranking/)

## 英伟达开放 Alpamayo 2 Super 商用，专攻自动驾驶长尾难题

英伟达宣布 Alpamayo 2 Super 开源模型现已可商用，面向 Robotaxi 与自动驾驶场景，核心定位是解决罕见复杂路况的长尾问题。

自动驾驶的长尾场景——施工改道、极端天气、非常规车辆——是数据驱动方案的天然短板。英伟达这套模型的技术路线聚焦于提升对罕见事件的泛化能力，而非堆积更多常规驾驶数据。

开放商用意味着车企与自动驾驶创业公司不必从零训练基座模型，可在英伟达方案之上做场景微调。这是一个信号：自动驾驶模型层正在走向分工——底层通用能力由算力厂商提供，场景适配留给车厂。

> 原文：[https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/](https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/)

## 商汤开源轻量多模态模型，4K 直出拉低图像生成门槛

商汤开源 SenseNova U1.5-Lite-Preview，在 U1 基础上增强图像生成与编辑能力，支持原生 4K 图像直出，定位轻量级统一多模态模型。

「轻量级」与「4K 直出」是本次的两个关键词。此前高分辨率图像生成通常依赖重型模型或级联放大，对推理资源要求高。U1.5-Lite 试图在较小参数量下直接输出 4K，面向的是对成本敏感的生产环境。

结合 MiniMax-H3 登顶视频榜来看，中国模型厂在多模态生成领域正同时走「开源」与「轻量化」两条路。对下游应用开发者而言，可商用、可本地部署的多模态模型选项正在快速增多。

> 原文：[https://www.leiphone.com/category/industrynews/qqTUnzcUVPuJaEeA.html](https://www.leiphone.com/category/industrynews/qqTUnzcUVPuJaEeA.html)

## DeepSeek V4 Flash 低价屠榜，硅谷称「用性价比打服」

DeepSeek V4 Flash 以极低价格引发硅谷震动，海外 API 平台和开发者社区纷纷接入支持，被评价为「用性价比打服硅谷」。

V4 Flash 的定位是极致性价比的推理模型，压低单次调用成本，目标显然是高频、大规模的业务场景。这不是参数竞赛，而是单位成本竞赛。

当头部模型的能力差距缩小，价格就成了决定开发者选型的关键变量。DeepSeek 在与 Qwen3.8 同日发布的时间窗口下，用 Flash 版本打出差异牌：不比最强，比最省。这条路是否可持续，取决于低价是否建立在真实成本优势之上。

> 原文：[https://www.qbitai.com/2026/08/465814.html](https://www.qbitai.com/2026/08/465814.html)

## 腾讯混元 Hy ASR 3.0：让语音识别懂上下文

腾讯混元推出 Hy ASR 3.0 preview，在语音识别中引入上下文理解能力，已接入腾讯元宝。

传统 ASR 的痛点是字准但意偏——同音词、专业术语、指代关系容易出错。Hy ASR 3.0 的思路是在声学识别之外加入语义层，让模型根据对话上下文纠偏。这不是新概念，但落地到产品中且接入元宝，说明技术上已过可用线。

对国内语音交互市场而言，ASR 从「听见」到「听懂」的演进，将直接影响语音助手、会议转写、客服质检等场景的体验上限。值得关注的是它是否会进一步开放 API。

> 原文：[https://www.qbitai.com/2026/08/465973.html](https://www.qbitai.com/2026/08/465973.html)

---

今天六条发布，主角都是中国模型。从基座到视频生成到语音，能力已不是短板，接下来要观察的是：价格战与生态战之后，谁能建立不可替代的护城河。