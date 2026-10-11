# 当模型不再写答案，只打分

今天最值得看的不是某个旗舰模型升级，而是一条新赛道浮出水面：微软发布 Decision-1，Nace AI 开源 Drex 1.5，OpenAI 的 Decisions API 同日进入公测——三家在同一天把「决策打分」做成了独立产品。这背后的共性是：文本生成之外，「在给定选项里选一个」被证明是更可评测、更容易做小的任务。当 Agent 规模从几个涨到上千个，这一层的延迟和单位成本，会比旗舰模型的能力上限更早成为瓶颈。

## 微软发布 Decision-1，专攻「决策打分」

微软 AI 发布 Microsoft-Decision-1，一个基于 Qwen3.5-9B 的决策打分模型，为路由、分类、验证和 Agent 控制输出校准后的选项概率，已上线 Foundry。

值得注意的是它的形态：不做生成，只对给定选项打分并给出校准概率。这恰好卡在 Agent 系统里调用最频繁、却最容易被旗舰模型浪费的那一层——路由和验证。用 9B 基座加概率校准，比让大模型「思考一下再选」更便宜，也更可评测。另一个信号是基座选了 Qwen3.5：微软在自有模型之外挑基座，说明这类任务的竞争力在数据与校准，不在参数量。

> 原文：[Microsoft-Decision-1 on Foundry](https://commandline.microsoft.com/microsoft-decision-1-model-foundry/)

## Claude 可并行编排上千个 Agent

Anthropic 为 Claude 引入动态工作流（dynamic workflows）能力，最多可同时编排 1000 个 Agent 并行执行任务，把多智能体协作推向工程化规模。

从「几个 Agent 协作」到「上千个并行」，量级变化带来的是工程问题：任务拆分、结果聚合、失败重试、成本上限。数量上去之后，单点判断错一次会被放大一千倍——这恰好解释了为什么同一天里决策类模型密集出现：编排规模越大，越需要一层廉价可靠的路由与校验。

> 原文：[the-decoder](https://the-decoder.com/anthropics-claude-can-now-orchestrate-up-to-1000-ai-agents-in-parallel-through-dynamic-workflows/)

## 谷歌 Gemini 4「Carbon」传闻对标 Opus 5.5

有爆料称谷歌下一代旗舰 Gemini 4（代号 Carbon）的编码能力已接近 Anthropic Opus 5.5。消息尚未获官方确认，按传闻对待。

若属实，第一梯队的编码差距会被压缩回「难以感知」的区间。但更值得关注的是节奏：旗舰之间的领先窗口越来越短，靠单代模型建立护城河越来越难，真正拉开差距的会是工具链、上下文管理和企业分发能力。

> 原文：[the-decoder](https://the-decoder.com/googles-gemini-4-carbon-model-is-reportedly-matching-anthropics-opus-5-5-coding-performance/)

## 阶跃 Step 5 Preview 登顶 OpenRouter，10/15 开源

阶跃星辰新旗舰基座模型 Step 5 Preview 冲上 OpenRouter Trending 榜首、日榜全球第二，官方宣布将于 10 月 15 日正式开源。

OpenRouter 榜单是海外开发者用真实调用投票的地方，冲榜本身比发布会更有说服力。先开放 API 试用、再开源权重，也是国内团队近一年跑通的节奏：先用调用量验证，再拿开源换生态位。开源当天的权重许可与推理成本，比榜单名次更值得盯。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/7iRgmb0q4JgVbmU8.html)

## GPT-6.1 Sol 极速版上线，被吐槽用不起

OpenAI 推出 GPT-6.1 Sol 极速版，响应更快，但价格比 Astra 还贵，社区抱怨 500 美元套餐撑不过一天。

「更快但更贵」是个明确的定价信号：低延迟被单独标价，说明推理侧算力约束仍然紧张，速度成了稀缺资源而非默认福利。对使用方来说，问题从「用不用」变成「哪些环节值得为延迟付费」——批量任务、离线评估这类场景，很可能被挤回更便宜的模型。

> 原文：[InfoQ](https://www.infoq.cn/article/soBOt9TSckGlJlBS519y?utm_source=rss&utm_medium=article)

## 决策模型成新赛道：Drex 1.5、Decisions API 齐发

决策模型正在变成一条独立赛道。Nace AI 开源 9B 决策模型 Drex 1.5，一次前向即给出各选项概率；OpenAI 的 Decisions API 进入公测，号称比 Responses API 快 10 倍；另有一个 11MB 的边缘端决策模型 ej 出现。

三条路线指向同一个判断：相比文本生成，「在给定选项里选一个」更可评测、也更容易做小。从 9B 到 11MB，模型体积跨了两个数量级，说明这一层的竞争焦点是延迟与单位成本，而不是通用能力。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/09/nace-ai-open-sources-drex-1-5-a-9b-decision-model-that-scores-options-not-text/)

## 通义千问开源 8 步出图的图像模型

阿里 Qwen 团队发布 Qwen-Image-2.1-Turbo，把开源图像模型 Qwen-Image-2.1 的默认 40 步去噪压缩到 8 步，兼顾生成与编辑速度。

步数从 40 降到 8，意味着单张图的推理成本大约降了一个量级，开源图像模型开始从「能出好图」转向「能稳定批量出图」。对做内容管线、电商素材、设计工具的产品而言，这类提速比画质榜上的小幅领先更有实际意义。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/09/alibaba-qwen-releases-qwen-image-2-1-turbo-an-8-step-7b-image-model/)

今天七条里，有五条在讲同一件事：模型不再只负责输出内容，也开始负责做出选择。当编排规模来到一千个 Agent，你更担心它的能力上限，还是它选错的成本？