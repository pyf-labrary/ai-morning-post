# OpenAI 开放 Codex 底座，一天三连发

OpenAI 一天发了三个产品，但最值得看的不是任何一个垂直场景，而是 Agents API——它把驱动 Codex 的智能体运行框架开放成了公共基础设施。这意味着 OpenAI 不再只卖模型，开始卖「跑智能体的地方」；配合金融版 ChatGPT 和 ChatGPT Work 的 Data Agent，路线很清楚：通用能力下沉成底座，垂直场景抬客单价。同一天，国内侧支付宝和蚂蚁数科也在抢 agent 的开发与分发入口，这条赛道今天同时从两端收紧了。

## OpenAI 开放 Codex 底座，Agents API 进入公测

OpenAI 把驱动 Codex 的智能体运行框架开放为 Agents API，开发者可指定任务、模型、工具与运行环境，既能跑在 OpenAI 的托管沙箱里，也能接入自有基础设施，公测期不额外收费。

关键点在「运行框架」四个字。过去一年 agent 之间的差距往往不在模型，而在 harness——工具调用、上下文管理、沙箱、失败重试这些看不见的工程。OpenAI 把这套内部跑通的东西做成 API，等于把门槛从「谁能调通模型」上移到「谁有更好的运行时」。

为什么重要：这让 agent framework 层的创业公司位置变得尴尬；「公测期不额外收费」的措辞也留了定价后手。更值得观察的是，当运行时被商品化，差异会回到数据与分发上——今天后面几条恰好都在讲这两件事。

> 原文：[OpenAI](https://openai.com/index/introducing-the-agents-api)

## ChatGPT 走向金融前台，内置行情与研报数据

ChatGPT for Financial Services 面向投行与股票研究员，把 Daloopa、PitchBook、LSEG News 等数据源内置进产品，配合 GPT-6 Astra，用于研究、建模与客户材料生成。

这条最值得读的是合作名单。金融是 LLM 最早验证付费意愿的场景，但门槛从来不是生成能力，而是授权数据的完整性与时效性——财务数据、私募并购数据、新闻流，每一类都要单独谈。OpenAI 选择买进来，而不是自己做。

为什么重要：这是对 Bloomberg 终端和一批金融 AI 初创的正面竞争，切入点选的是研究员的一整天：查数据、搭模型、做材料。谁先占住这个工作流，谁就拿到了金融场景的默认入口。

> 原文：[OpenAI](https://openai.com/index/introducing-chatgpt-financial-services)

## ChatGPT Work 加 Data Agent，自然语言生成看板

ChatGPT Work 上线数据智能体，可连接企业数据源，用自然语言提问、挖掘洞察，并直接生成可交互的仪表盘。

方向很明确：把 ChatGPT 从问答框推向工作台。传统 BI 的链路是建模、拖拽、配图、分享，Data Agent 想砍掉中间几步，让业务方跳过数据分析师直接拿结论。对企业采购来说，BI 的比价清单里从此多了一个 OpenAI。

为什么重要：text-to-SQL 与自动可视化是过去两年最拥挤的赛道之一，现在由平台方自己做了。这类能力一旦成为 ChatGPT Work 的默认入口，纯工具型产品的空间会被压缩，剩下的价值在深度治理、权限与行业语义层。

> 原文：[OpenAI](https://openai.com/index/put-data-to-work)

## Meta 的 Muse 冲到美国 App 榜第二

Meta 的新智能体应用 Muse 可以直接在 WhatsApp 内帮用户购物、写邮件，甚至代为议价，目前已成为美国下载量第二的应用——但起量速度慢于 Meta AI 与 Threads。

「议价」是这条里信息量最大的功能，它意味着 agent 开始代表消费者与商家博弈，而不只是帮人写字。入口放在 WhatsApp 内，等于免掉了冷启动的装机成本。

值得注意的是那个对比：下载量第二，但起量不如两个前作。分发从来不是 agent 产品的瓶颈，用完还回不回来才是。对做 C 端 agent 的团队来说，这条比 OpenAI 的三连发更有参考价值。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/10/metas-ai-agent-muse-is-now-the-no-2-app-in-the-us/)

## 苹果秋季发布会：折叠屏 iPhone Duo 与「常听」手表

苹果发布首款折叠屏 iPhone Duo，15999 元起，铰链的制造用到了 AI 与 3D 打印；同时推出可转录环境对话的 Apple Watch、新版 Siri AI 与健康年龄评分，并用 Apple Reference Image 标记照片并非 AI 生成。

硬件之外有两条 AI 线索。一是手表的环境转录，等于把「常听」做成系统能力，隐私叙事与实际采集能力之间的张力会很快显现。二是 Reference Image，苹果试图用平台级签名回答「这张照片是不是 AI 生成的」，这是内容真实性问题上少见的硬件厂方案。

为什么重要：苹果在 AI 上依旧不追求模型领先，而是把能力塞进传感器、端侧与信任链。折叠屏是叙事，这两条才是它的立场。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/09/everything-apple-announced-at-its-fall-iphone-event-from-the-foldable-iphone-duo-to-an-always-listening-apple-watch/)

## 支付宝设 1000 万智能体奖，飞猪接入阿宝

支付宝宣布每年投入 1000 万元设立「智能体涌现奖」，开发者可用自然语言搭建智能体并接入「阿宝」，面向其 10 亿用户；飞猪同步接入，一句话即可完成机票、门票预订。

两个信息点：门槛被压到「自然语言搭建」，分发直接给到 10 亿用户。国内 agent 生态的胜负手一直不在模型，而在谁能提供交易闭环和支付通道——支付宝恰好两样都有，飞猪的接入演示了模板：订票、订门票这类高频且可直接结算的场景最先被吃下。

为什么重要：对开发者，这是比独立 App 更现实的变现路径；对平台，1000 万奖金买到的是生态定义权。接下来该盯的是接入审核与分成规则，那才是真门槛。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/osi55rJJYCUZuY7h.html)

## 蚂蚁数科发布 Agentar 金融版

蚂蚁数科推出 Agentar 金融版，提供开箱即用的金融智能体专家团、行业 Skill、MCP 与评测治理能力，覆盖智能体的开发、部署、协作与管理全流程。

和 OpenAI 的金融版对照着看很有意思：一边卖模型加买来的数据，一边卖流程与治理——行业 Skill、MCP 接入、评测。这其实对应金融客户的两类焦虑：前沿团队要更强的生成能力，而大多数机构卡在合规、可审计和内部系统对接。

为什么重要：企业级 agent 的落地瓶颈很少是智力，更多是「出了错谁负责」。评测与治理被写进产品目录，说明这个市场正从 POC 走向采购清单。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/HoBDVtC0QpjjwVfv.html)

## Clearview 测试 InquiryIQ，把身份识别升级成人生检索

WIRED 报道，此前未曝光的原型 InquiryIQ 由 Clearview 测试，调用 xAI 的 Grok 模型，基于 Clearview 的人脸识别结果，进一步梳理目标人物的社交账号与关联人脉，目前供执法机构试用。

如果说人脸识别回答的是「这个人是谁」，InquiryIQ 回答的是「这个人在网上做过什么、和谁有关」。把识别结果交给 LLM 做聚合推理，技术上并不复杂，但它把原本分散、需要人工拼接的公开信息变成了一次查询——能力提升与滥用风险在同一根轴上。

为什么重要：这条提醒我们，agent 的工具调用能力用在人身上时，效率提升得有多快，边界问题就有多尖锐。执法便利与大规模监视之间，目前看不到清晰的技术分界线。

> 原文：[WIRED](https://www.wired.com/story/clearview-ai-is-testing-an-ai-tool-that-lets-cops-instantly-unearth-your-online-activity/)

今天八条里一半以上和 agent 有关，但稀缺的从来不是智能体本身，而是运行时、数据授权、交易闭环和身份入口。当智能体开始替你议价、订票、写研报，也替警方梳理你的一生，更该问的是：它站在谁那边。