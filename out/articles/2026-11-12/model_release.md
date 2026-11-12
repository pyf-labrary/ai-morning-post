# 价格战与安全分层，同一天到来

今天最值得看的一条，是 Gemini 4 Carbon 全面开放：官方给出的定价约为 Fable 5.2 的四分之一。这个数字比任何 benchmark 都更能改变开发者的行为——原本因为成本不敢放开的 agentic 循环，突然变得可以承受。同一天，Anthropic 把安全防护做成两档 SKU，DeepMind 把机器人越狱评测开源成基准。能力和价格之外，模型正在被拆成更多可售卖的维度。

## Gemini 4 Carbon 开放：价格是四分之一

Google DeepMind 宣布 Gemini 4 Carbon 全面可用。官方给的例证颇为具体：它能在一夜之间重写 OpenCode 桌面应用——这更像在强调长上下文与 agentic 编码的耐力，而不是某个单点分数。定价约为 Fable 5.2 的四分之一，第三方工具 llm-gemini 已同步支持，生态跟进速度本身就是信号。

为什么重要：当旗舰模型把价格压到对手的四分之一，压力不只在同行定价表上，更在开发者的架构选择上。多轮工具调用、失败重试、长上下文反复读取，这些过去要精打细算的动作，现在可以放开跑。但便宜四倍不等于便宜——如果单位任务需要两次重试，账就要重算。接下来该看的是真实负载下的每任务成本，而不是发布会上的 token 单价。

> 原文：[Google DeepMind](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)

## Fable 5.2 与 Mythos 5.2：把安全做成 SKU

Anthropic 发布 Fable 5.2 与 Mythos 5.2，两者实为同一模型的两套安全防护等级。Fable 5.2 在 FrontierCode 2.0 上得分 49.1%，定价 8/40 美元每百万 token（输入/输出），支持 100 万 token 上下文。

为什么重要：同一套权重、两个名字，意味着「安全」从合规成本变成了产品分层。对企业客户是好事——可以按场景挑防护强度，不必为一个高敏场景牺牲全部体验。对评测生态则是麻烦：同一模型会存在两个分数，榜单若不标注防护档位，横向比较就会失真。这也把一个老问题摆上台面——我们评测的到底是模型能力，还是「模型加一层策略之后」的可用性。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/10/anthropic-claude-fable-5-2-mythos-5-2-release/)

## Gemini Robotics 2.5：成功率翻倍，越狱基准开源

DeepMind 发布 Gemini Robotics 2.5，官方称部分任务成功率提升到原来的两倍；同一天还开源了安全基准 ASIMOV-jailbreak，用于评测机器人模型被越狱的风险。

为什么重要：机器人模型长期缺一把公共的安全标尺，「能否被诱导做出危险动作」往往只在论文附录里讨论。开源基准把这件事变成可复现、可比较的指标，客户和监管方终于有了参照物。另一面是话语权——谁定义基准，谁就定义「安全」的边界。成功率翻倍是宣传点，基准才是长期资产；把两者放在同一天发布，本身是一种姿态。

> 原文：[Ars Technica](https://arstechnica.com/google/2026/11/deepmind-reveals-gemini-robotics-2-5-and-open-safety-benchmark-asimov-jailbreak/)

## Fish Audio Live 3：边说边听，186 毫秒

Fish Audio 发布全双工（full-duplex）语音模型 Live 3，能在说话的同时持续监听，并区分「嗯哼」这类附和与真正的打断，最低 186 毫秒响应，首发仅支持英文。

为什么重要：语音交互的分水岭不在音色，而在轮转（turn-taking）。半双工模型像对讲机——你说完我才能说；全双工才接近电话。186 毫秒已落在人类对话的间隙区间内，而「附和 vs 打断」的判定是真正的工程难点：判早了抢话，判晚了迟钝，两者的体感差异远大于音质差异。仅英文首发说明这类模型对语料与韵律标注的依赖仍然很重，中文场景还要等。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/10/fish-audio-live-3-full-duplex-voice-model/)

## 结语

四条新闻指向同一件事：模型本身正在变成标配件，价格、防护档位、交互形态才是新的差异化战场。留一个问题——当同一个模型能按四分之一的价格、两种安全等级卖给你，你为「能力」付的那笔钱，究竟买到了什么？