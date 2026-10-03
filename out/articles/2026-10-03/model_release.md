# 模型双雄同日对撞，价格战开打

今天最值得看的是 OpenAI 与谷歌的正面对撞：GPT-6 家族上线，并配了一份面向初创公司的选型指南，Astra Ultrafast 进入 API；几小时后谷歌跳过预热发布 Gemini 4，定价约为 Astra 的一半。两者的叙事重点并不相同——OpenAI 在讲「怎么选、怎么调、怎么编排」，谷歌在讲 RSI（递归自我改进）与价格。当模型能力的差距越来越难被外部验证，定价、可调参数与交付速度就成了可比较的竞争面。图像、语音、决策模型今天也在同步补齐，本板块值得逐条看。

## GPT-6 家族上线，OpenAI 先递了一份「选型指南」

OpenAI 上线 GPT-6 系列模型的使用指南，面向初创公司说明三件事：如何在不同型号间选型、如何调节推理强度（reasoning effort）、如何编排工具链。其中 GPT-6 Astra Ultrafast 基于 NVIDIA Blackwell GPU 加速，已登陆 OpenAI API，同时进入 ChatGPT Work 与 Codex。

关键点不在模型本身，而在发布形态：把「怎么选型」当作发布物料，说明模型家族已经细分到需要导购的程度。对技术团队来说，推理强度变成可调参数，意味着延迟、成本与效果之间多了一层显式权衡，这层权衡需要提前写进架构。对初创公司而言，选型复杂度上升本身就是一笔成本。

> 原文：[OpenAI](https://openai.com/index/practical-guide-building-gpt-6)

## Gemini 4 突然发布，价格约为 Astra 一半

谷歌没有预热，直接发布 Gemini 4，主打 RSI（递归自我改进）能力，定价约为 GPT-6 Astra 的一半。

两点值得注意。一是定价明确对标：在同一天把价格压到对手一半，抢的是正在做模型选型的团队，而不是榜单分数。二是「RSI」作为主打能力，既是技术叙事也是营销语言——它描述模型参与改进自身的能力，但外部很难快速验证其边界，采购方需要看的是实际任务上的表现，而非名词。对已经在 GPT-6 上做概念验证（PoC）的团队，这是一个值得重新算账的时点。

> 原文：[量子位](https://www.qbitai.com/2026/10/499663.html)

## Flux 3 Image：多步局部编辑，其余画面不动

Black Forest Labs 发布 Flux 3 Image，支持多步编辑：在多轮改动中只修改指定区域，画面其余部分保持不变，面向专业图像编辑工作流。

局部编辑一直是图像模型落地商业工作流的关键瓶颈——生成一张好看的图不难，难的是在客户要求「只改这块」时不把整张图重画一遍。多步编辑把这个约束显式化，意味着模型开始按「编辑会话」而不是「单次生成」来设计。对做设计工具、电商素材、广告投放的产品，这类能力直接决定返工成本。

> 原文：[The Decoder](https://the-decoder.com/black-forest-labs-launches-flux-3-image-with-multi-step-editing-that-leaves-the-rest-of-your-picture-alone/)

## 微软补上语音 Agent 的转录与 TTS

微软 AI 发布新的语音转录模型与文本转语音（TTS）模型，定位于可实时对话的语音 Agent 场景。

语音 Agent 的体验瓶颈通常在两头：听准（转录）与说自然（TTS），中间才是推理。微软这次直接补齐两端，说明它把语音 Agent 当成一条独立产品线投入，而不是语言模型的附属功能。对做客服、外呼、实时助手的团队，这意味着底层组件多了一个选择，也需要重新评估自建与调用 API 的边界。

> 原文：[The Decoder](https://the-decoder.com/microsoft-ai-releases-new-transcription-and-text-to-speech-models-for-voice-agents/)

## Cloudflare 的 Clef：把人类移出 Agent 环路

Cloudflare 发布新模型 Clef，声称可让 AI Agent 在执行任务时不再需要人工审批环节，也就是「人类不在环」（human out of the loop）。

这是今天最有争议的一条。去掉人类审批能显著提升自动化吞吐，代价是责任归属：出错时谁签字、如何回滚、如何审计，这些问题的答案不在模型里，而在部署方的流程里。Cloudflare 处在流量与策略执行的位置上，这是它敢做这个宣称的前提之一。真正的问题不是能不能去掉人类，而是哪些动作可以去掉、哪些必须保留。

> 原文：[The Decoder](https://the-decoder.com/cloudflare-says-its-new-clef-model-means-humans-no-longer-need-to-be-in-the-loop-for-ai-agents/)

## Ideogram 新模型：和 Flux 3 打同一张牌

Ideogram 发布新版图像模型，强调精准局部编辑能力：改动图像的一部分，不破坏其余画面，与同一天发布的 Flux 3 Image 正面竞争。

两家在同一天把「局部编辑不串味」当作主打，说明它已经从差异化卖点变成入场门槛。对图像模型厂商来说，单图质量的分差在缩小，竞争正转向工作流能力：多轮编辑、区域一致性、可控性。对使用者反而是好消息——选型时可以更多看价格、延迟与集成成本，而不只是看生成效果。

> 原文：[The Decoder](https://the-decoder.com/ideogram-says-its-new-model-can-edit-part-of-an-image-without-messing-up-the-rest/)

## 亚马逊入场，决策模型开始扎堆

AWS 旗下 Strand Labs 推出 Strands Decider 2B，成为近期涌现的一批「决策模型」（报道中称 Jev 类模型）的新成员。

2B 这个参数量级值得注意：决策类任务往往不需要通用大模型的全量能力，小模型在延迟与成本上更有优势，也更容易嵌进既有系统。当亚马逊这样的云厂商入场，说明该方向已从研究话题走向平台能力，更可能以云服务形式交付，而不是单独售卖。对做 agent 编排的团队，这多了一个「用哪个模型做决策」的选项。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/01/amazon-releases-its-own-jev-clone-as-decision-models-flood-the-web/)

## Utopai X 盲评全球第二，视频榜不再只有大厂

AI 影视公司 Utopai Studios 的定制视频生成模型 Utopai X，在 Artificial Analysis 文生视频盲评榜位列全球第二、全美第一。

盲评的价值在于削弱品牌与营销的影响，因此这个名次比自测 demo 更有参考性。更值得注意的是「定制模型」这个形态：一家影视公司不追求通用视频模型，而是针对自己的制作需求训练，然后在公开榜单上拿到名次——垂类定制在视频生成上已经具备竞争力。对投资人来说，值得追问的是这类优势能维持多久，以及它如何转化为收入。

> 原文：[36氪](https://36kr.com/newsflashes/4008300875141256?f=rss)

今天八条里出现频率最高的词其实是「局部」：只改一块图、去掉一道审批、用一个 2B 模型做决策。能力趋同之后，克制本身就是竞争力——那么你的选型清单，会因为半价的 Gemini 4 而改动吗？