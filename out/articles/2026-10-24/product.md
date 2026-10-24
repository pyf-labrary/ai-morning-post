# Agent 开始要工牌、要机房、要证明

*2026-10-24 · 应用产品板块*

今天应用板块最值得看的不是哪个新功能，而是 Google 给每个 Gemini Agent 分配了一台硬件隔离的 microVM。把它和 1Password「代登录但不给密码」放在一起看，会发现行业正在同时解决两件事：Agent 的行为要能被隔离，Agent 的权限要能被收窄。应用层这边，Anthropic 亲自下场做 Claude Duet、Uber 把 3 万人一次性搬上 ChatGPT Work，是在验证需求侧到底接不接得住。我的判断是：Agent 的竞争重心正从「能做什么」转向「敢让它做什么」。

## Claude Duet：模型厂商开始自己造 Agent 的壳

Anthropic 推出 Claude Duet，以候补名单（waitlist）形式向 Pro/Max 订阅用户开放，定位是面向 Agent 场景的新应用。

关键点在于它不是一次模型发布，而是一次应用发布。灰度对象是已经付费的 Pro/Max 用户：这批人任务量大、容忍度相对高，是打磨 Agent 产品最合理的起点，因为多步任务的失败模式只有真实工作量才能暴露出来。

为什么重要：模型厂商自己做应用，等于把「Agent 的壳」这一层收回自营，而这层过去一年被普遍视为创业公司的窗口。当壳被订阅关系捆绑，独立产品能拿出来竞争的只剩垂直数据、交付能力和合规资质。对产品经理来说，接下来值得观察的不是 Duet 能做多少事，而是它在任务中途失败时怎么收场。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/22/claude-duet-app-is-anthropics-bet-on-agents/)

## Google 给每个 Agent 一台独立 microVM

Google Cloud 推出 Agent Compute Engine，为每个 AI Agent 提供硬件隔离的 microVM（微虚拟机），运行环境内部不存放凭证，目前已用于 Gemini Agent。

关键点是两个设计选择。一是隔离粒度落在硬件层，而不是容器或进程：传统多租户的前提是「代码行为基本可预期」，而 Agent 会自主发起动作，属于不可信负载，容器边界不够用。二是凭证被移出运行环境——Agent 在虚拟机里跑，钥匙不在里面，即使运行环境被攻破，也带不走长期凭证。

为什么重要：这很可能成为 Agent 基础设施的默认范式。定义「一 Agent 一机器 + 身份外置」这套标准的一方，握住的其实是 Agent 时代的虚拟化入口。云厂商在这件事上有天然优势，因为它们本来就在卖隔离。

> 原文：[The Decoder](https://the-decoder.com/googles-agent-compute-engine-gives-every-gemini-agent-its-own-hardware-isolated-micro-virtual-machine/)

## 1Password：Agent 可以替你登录，但拿不到密码

1Password 推出新功能，允许 AI Agent 代替用户登录个人账户，同时不向 Agent 暴露底层密码和其他私密凭证。

关键点是它把「秘密」和「授权」拆开了。过去让 Agent 操作你的账号，最直接的做法是把密码交给它；现在 Agent 得到的是登录能力本身，接触不到密码。本质上是在凭证和 Agent 之间插了一层代理。

为什么重要：账号权限是 Agent 落地最现实的拦路虎，在企业与合规场景尤其如此——很少有人愿意为一个会自动执行动作的程序，签一张无限期的密码授权书。这块需求足够刚性，会长出一个「Agent 身份与授权」的中间层。也要留意另一面：当代理层成为必经之路，它同时也就握住了 Agent 经济的收费口。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/22/1password-launches-a-way-for-ai-agents-to-log-in-on-your-behalf-without-seeing-your-password/)

## Uber 把 3 万人一次性搬上 ChatGPT Work

Uber 将 ChatGPT Work 从试点扩展至全公司 3 万名员工，企业级 Agent 部署规模再上一个量级。

关键点是从「试点」到「全员」的决策本身。企业采购 AI 很少一步到位，能走到全量，通常意味着内部有一套说得清的评估口径，而不只是高层表态。

为什么重要：企业软件的分发逻辑正在变。过去是买 license 再培训员工，现在是给每个人配一个 Agent 席位，采用率天然更高，但计费与治理也更难。3 万席位的公开部署是这个品类目前少见的规模样本，对投资人来说，企业 AI 的竞争指标正从「模型好不好」变成「组织渗透率有多高」。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/22/uber-puts-all-30000-employees-on-chatgpt-work/)

## 微软的医疗突破，功劳可能不在产品层

Mustafa Suleyman 称微软新的 AI 诊断系统在 Science 研究的疑难病例上优于全科医生，同时他表示正在追求医疗方向的「超级智能」。

关键点是他自己给出了归因：提升主要来自底层模型。这句话比结论更值得记——它等于承认产品层的增量有限，收益是租来的。

为什么重要：这是对整个垂直 AI 产品赛道的提醒。很多「行业模型」的领先，本质是在吃基座模型迭代的红利，基座一换代，产品的护城河就被冲掉一层。真正能沉淀的是工作流集成、责任划分和数据闭环。另外注意场景限定：疑难病例是经过挑选的高难度样本，与日常门诊的分布不是一回事。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/22/microsofts-mustafa-suleyman-says-its-ai-outperforms-doctors-on-hard-cases-as-he-chases-medical-superintelligence/)

## 千问Go! 把「说话搭应用」接到了部署

千问Go! 上线「我的应用」，用户无需编程，用自然语言即可搭建生活、工作、学习场景的专属应用，支持分享和持续更新，并接入阿里云 Meoo 完成自动部署。

关键点在于它把最后一公里包了。此前同类产品大多停在「生成一个能跑的页面」，卡在托管、域名、更新这些杂事上；接上自动部署之后，从描述到可访问的链接是一条完整链路。

为什么重要：vibe coding 的竞争焦点正从生成质量转向分发与运维，而这恰好是云厂商的强项——它卖的是算力和托管。对产品经理来说，真正的考验不在生成，而在留存：一次性生成的小工具没人维护，长尾供给很容易变成一次性玩具。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/rTNQlAtTr6ROkXI1.html)

## 美团免费送 AI 店长，平台开始做商家侧的公共设施

美团外卖发布「妙手外卖版·袋鼠管家」，覆盖经营诊断、门店巡检、商品运营等环节，将免费提供给全国商家，部分试用商家增长超过 30%。

关键点是免费 + 全国铺开。这说明美团把它当作商家侧的运营基础设施，而不是一条 SaaS 收入线：目标是抬高整个供给侧的经营效率，同时加深商家对平台的依赖。

为什么重要：当平台把经营诊断这类能力零成本送出，独立商家工具厂商的定价空间会被直接压缩，尤其是在诊断、选品这些与平台数据强相关的环节。需要克制看待的是那个 30%——它来自「部分试用商家」，不是全量平均，样本选择偏差通常不小。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/tZI7pYBhiFduVfr6.html)

## Claude 一边写代码，一边给出安全证明

Anthropic 称 Claude 现在可以在编写代码的同时自动生成安全性证明，把形式化验证（formal verification）引入日常编码流程。

关键点在于成本结构。形式化验证此前只用于内核、密码学这类容错为零的场景，因为它太贵、太依赖专家；如果能随代码自动产出证明，验证的边际成本会被压到接近零。

为什么重要：这可能是 Agent 写代码被企业真正接受的前提——不是「我相信它」，而是「我能验证它」。但下一步要看的不是演示，而是证明的成色：它证明的是内存安全、类型约束，还是业务逻辑？证明器本身可不可信？这些问题决定它是工程突破还是一次漂亮的展示。

> 原文：[The Decoder](https://the-decoder.com/anthropics-claude-now-writes-code-and-proves-it-safe-automatically/)

八条拼起来是一幅很具体的图景：Agent 已经走到要工位、要权限、要机房、还要第三方证明的阶段。留一个问题——当上游把隔离、授权和部署都收走之后，应用层还剩下什么是可以卖的？