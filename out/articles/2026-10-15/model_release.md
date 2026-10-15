# Gemini 4 登顶，竞争转向端侧与语音

今天是模型发布板块少见的密集日：Google 正式 GA Gemini 4 Argon，Meta 用百万上下文 Agent 模型宣布回到第一梯队，xAI、Liquid AI、Fish Audio 则分别在语音代理、端侧推理、开源语音三条线上出牌。如果只看一件事，是 Gemini 4 把「单次可输出 100 万 token」写进了卖点——过去两年卷的是长输入，现在开始卷长输出。更值得注意的是分层：前沿模型的绝对差距在收敛，定价、跑在哪台设备上、许可是怎么写的，正在取代参数规模成为新的差异化变量。

## Gemini 4 Argon 正式 GA：Vals Index 登顶，长输出成新战场

Google 正式发布 Gemini 4 Argon，架构为稀疏 MoE（Mixture of Experts），单次可输出 100 万 token，在 Vals Index 上以 68.90% 登顶。同步发布了机器人版本和安全对齐说明，并优先在付费版 Gemini 应用和 Antigravity 中开放。

关键点在两个数字上。一是 68.90% 的榜首位置，属于「追赶者交卷」的信号；二是 100 万 token 的输出上限——它改变的不是问答体验，而是任务形态：长篇代码库重构、整份报告生成、多章节文档一次性成型，这类过去需要靠编排（orchestration）硬拼的活儿，现在可以压进单次调用。

为什么重要：优先在付费应用和 Antigravity 开放，说明 Google 想先吃下 agentic 开发者场景，而不是先做 C 端拉新；同时放出机器人版，意味着具身方向在同步铺路，模型能力开始向硬件侧溢出。

> 原文：[Introducing Gemini 4 Argon - Google DeepMind](https://deepmind.google/blog/introducing-gemini-4-argon/)

## Meta 发布 Muse Wonder：百万上下文 Agent 模型，定价 4/20 美元

Meta 推出 Muse Wonder 与 Muse Wonder Full 两款百万上下文 Agent 模型，定价为每百万 token 4 美元输入、20 美元输出。其中 Wonder Full 在 DeepSWE、SWE-Marathon 两项评测上领先。

关键点是产品定义与评测选择的匹配：DeepSWE、SWE-Marathon 都是长周期、多步软件工程类任务，Meta 用它们来证明「百万上下文不是营销数字，而是 agent 能跑完长任务的前提」。分两档发布也延续了 Meta 一贯的打法——用低价档拉调用量，用 Full 档守能力上限。

为什么重要：这是 Meta 重新回到前沿梯队的明确动作。对开发者而言，一个百万上下文、且愿意在价格上做文章的选项，会直接影响 agent 产品的成本结构；对市场而言，前沿模型阵营又多了一个不愿意只做「开源好人」的玩家。

> 原文：[Meta releases Muse Wonder and Muse Wonder Full - MarkTechPost](https://www.marktechpost.com/2026/10/13/meta-muse-wonder-muse-wonder-full-release/)

## xAI 上线 Grok Voice 3.0：语音代理 API 每分钟 0.08 美元

xAI 发布 Grok Voice 3.0，通过语音代理 API 开放，价格与上一代持平，为每分钟 0.08 美元。该模型目前已用于特斯拉车机语音和星链客服中心，后者每天约 2 万通来电中有七成无需人工介入。

关键点不在参数，而在闭环：特斯拉车机和星链客服是 xAI 自家体系内的真实流量，七成免人工是一个可被业务方直接验证的指标——这比任何语音 benchmark 都有说服力。

为什么重要：语音代理的单位经济模型第一次有了清晰的锚点。0.08 美元/分钟意味着 1000 分钟约 80 美元，这个量级已经能让「AI 接客服」在人力成本面前算得过账。接下来值得观察的是，价格持平而能力升级，是否会把语音客服从试点推向规模替换。

> 原文：[xAI 发布 Grok Voice 3.0 - 36氪](https://36kr.com/newsflashes/4026343653314441?f=rss)

## Liquid AI 开源 LFM2.5：24B MoE、2B 激活，主打端侧 Agent

Liquid AI 开源 LFM2.5-24B-A2B，一个面向本地 Agent 的推理模型：总参数 24B、激活约 2B，开放权重。官方数据显示 LiveClaw 得分 48.09，在 Apple M5 Max 上解码速度达到 184 tokens/s。

关键点是稀疏结构带来的落地空间：2B 激活意味着推理时对内存带宽的压力远小于同总参数量的稠密模型，184 tokens/s 在单机消费级芯片上已经进入「可交互」区间。

为什么重要：端侧 Agent 的门槛正在从「能不能跑」转向「跑得好不好」。对产品经理而言，这意味着更多涉及隐私或离线场景的功能可以不必再走云端；对云厂商而言，端云分工的边界又要重新画一次。

> 原文：[LFM2.5-24B-A2B - Hugging Face](https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b)

## Fish Audio 开源 35B MoE 语音模型 Drama 3

Fish Audio 发布 Drama 3，一个 35B 参数、激活约 3B 的 MoE 语音模型，支持自然语言指令控制与 83 种语言，以「收入上限社区许可」（revenue-capped community license）开放权重。

关键点有两个。一是能力层面，自然语言指令控制把语音合成从「调参」变成「描述需求」，这对内容生产流程的改变比音质提升更直接；83 种语言则指向本地化配音这类明确需求。二是许可层面，收入上限模式意味着中小团队可以免费商用，超过阈值再谈授权。

为什么重要：语音模型的开源阵营正在快速补齐，同时「收入上限许可」是介于纯开源与商用授权之间的第三条路。对创业者，这是低成本试错的窗口；对投资人，这是需要重新评估资产归属和授权成本的变量。

> 原文：[Fish Audio releases Drama 3 open-weight TTS model - MarkTechPost](https://www.marktechpost.com/2026/10/14/fish-audio-drama-3-open-weight-tts-model/)

## 传 OpenAI 年内至少发一款新模型，旗舰仍待对齐打磨

有报道称，OpenAI 年内还会发布至少一个新模型，但其旗舰模型的可靠性仍取决于后续的对齐（alignment）工作。

关键点是这句话里隐含的排序：决定发布节奏的不再只是训练是否收敛，而是对齐是否到位。这与过去「能力先行、对齐补票」的发布节奏形成了对比。

为什么重要：如果连头部实验室都开始把对齐当作发布的阻塞项，那么整个行业的交付预期都需要调整——benchmark 分数不再等于可发布状态，安全与可靠性评估会更多进入排期。对下游依赖模型版本做产品的团队，这意味着要更早准备多模型兜底方案。

> 原文：[OpenAI will reportedly ship at least one model this year - The Decoder](https://the-decoder.com/openai-will-reportedly-ship-at-least-one-model-this-year-but-its-flagship-still-needs-alignment-work/)

## DeepMind 与新加坡政府合作：端侧 Gemma 拦截聊天诈骗

DeepMind 与新加坡政府合作，基于轻量 Gemma 微调出端侧反诈模型，可在私聊中识别对话式诈骗，全程零云端数据外传。

关键点是「对话式诈骗」这个目标：它不是关键词过滤，而是对一段持续交互的意图判断，同时约束在端侧完成，不上传任何聊天内容。

为什么重要：这是端侧 AI 最自然的落点之一——隐私敏感、需要实时、且数据不能出境（或出设备）。政府合作的形式也提供了一个监管友好的样板：把模型能力做成公共基础设施的一部分，而不是交给平台自行治理。对做合规与风控的团队，这个思路比模型本身更值得抄。

> 原文：[On-device AI scam detection with Singapore - Google DeepMind](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)

今天的发布几乎没有一条是靠参数刷存在感的，定价、部署位置和许可条款才是真正的分野。当「百万上下文」和「每分钟 0.08 美元」同时出现，你会把下一个产品押在云端前沿模型，还是端侧小模型？