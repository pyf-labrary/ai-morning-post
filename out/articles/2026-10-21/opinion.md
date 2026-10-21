# AI 安全的定义权，正在易手

美国下令联邦文职机构移除 DeepSeek 产品，且禁令覆盖「基于其技术构建的第三方服务」——这一句比禁令本身更值得读。它意味着合规审查开始穿透供应链，不再看你调用的是谁家的 API，而看模型血缘。同一天里，Anthropic 在推一份被批评为「假安全」的法案，Altman 被曝设想「熔掉别人 GPU」的终局，微软则把企业内的 agent 归类为内鬼。四件事指向同一个问题：谁来定义「安全」，以及这个定义服务于谁。

## 联邦机构要清掉的不只是 DeepSeek

美国政府以国家安全为由，要求联邦文职机构移除 DeepSeek 产品，以及基于其技术构建的第三方服务。关键点在范围：禁令不止于直接使用，还向下穿透到二次封装的托管、微调与集成服务。这意味着采购合规的审查对象从「供应商」变成了「模型血缘」，一家本地厂商把开源权重包一层 API 卖给政府，也可能落在禁令内。对做 to B 生意的人来说，这是明确的信号——模型来源需要可追溯、可举证，并且要能在一夜之间被替换。多云、多模型不是架构洁癖，而是合规冗余。（约 200 字）

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/us-orders-federal-agencies-to-remove-chinas-deepseek-ai-from-their-systems/)

## Anthropic 的法案，被读成松绑

Anthropic 正在游说一份 AI 安全法案：名义上允许在模型可能造成 50 人以上死亡时予以封禁，但同时规定联邦机构必须先取得法官许可，才能阻止模型发布。批评者因此称之为「假安全、真松绑」——把事前阻断变成需要司法审查的动作，等于给监管装了一道很高的门槛。这里真正值得看的是行业话语的转向：安全不再是外部约束，而成为由被监管者参与起草的立法语言。当一家实验室同时是「安全」的倡导者和受益者，判断标准就应当落在条文细节上，落在发布前还是发布后，落在谁举证。（约 200 字）

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/anthropic-pitches-ai-safety-bill-that-may-block-a-model-if-50-people-could-be-killed/)

## 熔掉别人 GPU 的「终局」

媒体报道称，Sam Altman 曾向他人描述 AI 安全的三种「终局」方案，其中之一是由单一公司把其他所有公司的 GPU 熔毁。需要说清楚：这是转述中的设想，不是正式提案，不应被当作公司立场来引用。但它之所以流传，是因为它把一种隐含逻辑说穿了——以安全之名集中算力控制权。任何「终局」式方案都预设了一个判断：某一家机构比其他所有人和所有制度更可靠。这类设想值得被记录，不是因为它可行，而是因为它在闭门讨论中出现过。（约 170 字）

> 原文：[The Decoder](https://the-decoder.com/sam-altman-reportedly-pitched-three-endgames-for-ai-safety-one-involving-a-single-firm-melting-everyone-elses-gpus/)

## 微软把 agent 归入内部威胁

微软安全团队把企业内使用的 AI Agent 类比为「内部威胁」，并强调对不受 OpenAI、Anthropic 等实验室直接控制的系统要严加监控。这个类比在工程上是成立的：agent 拿到的是人类员工的权限，却不承担人类员工的责任——它不会因为「这事看起来不对」而停下。企业当前的 agent 部署普遍是「先给权限，再想审计」，而攻击面恰恰在写权限和群发半径上。可以预期的变化是，agent 身份、最小权限、操作留痕会成为落地的前置条件，而不是上线后的补丁。（约 200 字）

> 原文：[TechCrunch](https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/)

## 27 家公司的 AI 账本

The Pragmatic Engineer 分析了 27 家公司的 AI 支出与研发产出，检验高额投入是否真正转化为发布速度与 PR 数量。这份工作的价值不在结论，而在问题的设定：把「AI 到底值不值」从感受层面拉到可比指标上。同时要警惕指标本身——PR 数量是过程量，不是价值量；如果 AI 让每个工程师多开 30% 的 PR，而合并周期和缺陷率同步上升，账面上会更热闹，实际上未必更好。看这类数据时，先问它测量了什么，再问它遗漏了什么。（约 190 字）

> 原文：[The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers)

## 纪录片里的 AI 和工程现实

Hugging Face 联合创始人 Clem Delangue 公开表示，他出镜的 Netflix 纪录片《AI Gone Rogue》「彻底末日化」、与事实不符，并提醒观众别急着转发。一位被采访者反过来质疑成片，这在 AI 题材里不算孤例。大众媒体需要叙事弧线，工程现实只有灰度；两者的偏差不是谁在撒谎，而是体裁不同。对从业者的实际影响是：当家人、客户、监管者通过这些作品形成对 AI 的第一印象时，你需要在具体场景里花更多力气解释「实际会发生什么」。（约 190 字）

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/hugging-face-ceo-warns-that-netflixs-openai-hack-documentary-isnt-accurate/)

## 一个 agent 搅乱 7500 人的邮件组

一个 AI Agent 加入了 7500 人的互联网研究者邮件列表，触发 reply-all 风暴，混乱至今仍在扩散。报道点出的讽刺在于：连隐私与网络协议领域的专家，也没准备好应对一个会读、会回、会抄送全体的自动参与者。这件事的破坏力不来自模型能力，而来自它被授予的写权限和群发半径——一个 agent 加上一个 reply-all，就足以制造一场小型拒绝服务。任何把 agent 接入通讯工具、工单系统、审批流的团队，都该先给「发给谁」加一道约束。（约 200 字）

> 原文：[Wired](https://www.wired.com/story/an-ai-agent-joined-a-listserv-of-top-internet-researchers-the-reply-all-chaos-is-still-unfolding/)

## 企业 AI 的电费时刻

MIT Technology Review 借用电力普及史来观察企业 AI：从少数场景试用，转向全流程依赖，效率与成本结构将被强制重估。这个类比的要害在于，基础设施化的标志不是用得更多，而是账目方式变了——有了折旧、有了 SLA、有了故障停机成本，也有了「不用它反而更贵」的路径依赖。尝鲜阶段可以只算 API 账单，基础设施阶段必须算迁移成本、人力结构和事故代价。很多公司目前还停在第一阶段，却已经开始按第二阶段做承诺。（约 190 字）

> 原文：[MIT Technology Review](https://www.technologyreview.com/2026/10/20/1146937/the-new-economics-of-enterprise-ai/)

安全正在从技术问题变成措辞问题，而措辞的起草权，目前握在被监管者手里。今天这几条里，你更担心监管太松，还是监管被写成某一家公司的形状？