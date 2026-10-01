# OpenAI 发常驻 Agent，顺手开商店

## 导语

OpenAI 在 DevDay 上一口气放出常驻型 Agent「Dots」，以及 Agents API、Decisions API、Spaces、Marketplace 和 Sign in with ChatGPT——它不再只是做一个更强的模型，而是在搭一套 Agent 的分发与身份体系。今天这个板块的其余消息，从 Meta Muse 抢入口、Manus 2.0 给 Agent 配手机号，到 DoorDash 让你发短信点餐，都落在同一条线上：Agent 正从「能干活」转向「被谁默认调用」。真正值得盯的不是能力又涨了多少，而是入口、身份和支付这些基础设施正在被平台收编。

## OpenAI DevDay：常驻 Agent 与 App 生态

OpenAI 发布常驻型 AI 智能体 Dots，同时推出 Agents API、Decisions API、Spaces、Marketplace 与 Sign in with ChatGPT，直接对标应用商店模式。官方口径下，ChatGPT 周活已达 12 亿。

关键点在打包方式：Agents API 是开发者的接入面，Marketplace 是分发面，Sign in with ChatGPT 是账号面，三者叠起来形成一套「Agent 时代的应用商店 + 身份系统」。把 Agent 称为「常驻」，指向的是它不等你提问就主动介入，这与过去一问一答的形态是两种产品。

对做 Agent 的团队来说，这直接提出了一个选择题：自建入口，还是寄生在别人的入口上。12 亿周活意味着分发效率极高，但也意味着议价权不在自己手里。

> 原文：[Wired](https://www.wired.com/story/openai-dots-always-on-ai-agents-that-proactively-help/)

## Meta Muse 与 OpenAI Dots 抢「个人代理」入口

Wired 对 Meta 的 Muse 与 OpenAI 的 Dots 做了实测，结论是两者正在争夺「个人 AI 代理」的默认入口。Truist 进一步警告，Muse 可以直接完成预订，对 Expedia、Booking 构成更大的分流威胁。

这里的差异不在体验好坏，而在权限边界：能直接完成预订，说明 Agent 手里握着交易动作，而不只是搜索结果。检索被改写顶多影响流量结构，下单被代劳则是把 OTA 从入口位置挤到履约与库存位置。

对投资人的判断提示是，评估这类 Agent 时，「能不能替用户按下确认键」比「回答得准不准」更能预示谁被替代。权限每放开一层，被绕过的中间商就多一层。

> 原文：[Wired](https://www.wired.com/story/ai-agents-dots-devday-muse-battling-it-out/)

## Manus 2.0 回归：给 Agent 配手机号和钱包

Manus 2.0 为智能体配上手机号、支付钱包，并支持拉群协作，试图把 Agent 从单机工具变成可对外联络的「数字同事」。

这三件事拆开看都普通，合起来才关键：手机号让 Agent 能接收验证码、完成注册与身份校验，钱包让它能付钱，拉群让它能进入人类协作流程。少了任何一项，Agent 都只能停在自己的沙箱里。

顺着这个方向，企业侧会先撞上一个治理问题——群里的这个账号，是人还是 Agent？以及当 Agent 可以独立完成注册与支付时，风控与合规体系里的「操作主体」定义需要重写。

> 原文：[量子位](https://www.qbitai.com/2026/09/499592.html)

## GPT-6 Astra 接上宇树 G1，自己把厨房收拾了

量子位与雷锋网的实测显示，GPT-6 Astra 可以像调用工具一样调用机器人技能，直接驱动机器人完成收拾厨房这类长流程物理任务，硬件侧为宇树 G1。

把机器人技能当作工具调用，意味着模型侧的 function calling 接口延伸到了物理世界，机器人本体退化成众多执行器之一。这条路线的意义不在单步动作有多漂亮，而在长流程：步骤越多，误差越会累积。

如果这条路走得通，机器人的瓶颈会从控制层部分转向任务理解与错误恢复——「发现盘子放错了位置该怎么办」。需要提醒的是，目前是实测演示，样本与场景都有限。

> 原文：[量子位](https://www.qbitai.com/2026/09/499493.html)

## DoorDash 上线可发短信点餐的 AI 代理

DoorDash 推出 AI 点餐 Agent，用户可以直接发消息下单，目标指向对抗 Uber Eats 与 Grubhub。

交互方式的变化很清楚：从翻菜单、比价格，变成发一句话。它改的是订单生成入口，不是履约链条。

判断是，外卖的护城河仍然在供给密度与配送网络，AI 代理降低的只是点单摩擦，很难单独构成壁垒。但它确实让「默认打开哪个 App」变得更不确定——当点餐发生在短信里，品牌曝光的那一层就被绕过去了。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/30/doordash-launches-an-ai-agent-you-can-text-to-order-food/)

## Airbnb 加入 AI 搜索与更多社交功能

Airbnb 上线 AI 搜索能力并强化社交功能，同时在部分市场试点送餐、洗衣等新服务。

AI 搜索改善的是发现与决策环节，社交与本地服务则指向「住得更久」的场景延伸。住宿本身是低频决策，压缩决策成本能直接提升转化；而送餐、洗衣这类服务是把用户在房源里的停留时间货币化。

两个方向的共同前提是当地供给密度，因此更值得关注的是它选择在哪些市场试点，而不是功能清单本身。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/30/airbnb-adds-ai-search-more-social-features/)

## 谷歌用 Skills 取代 Gems

谷歌把 Gemini 的 Gems 升级为 Skills，与 OpenAI、Anthropic 一起转向更适配智能体调用的提示与技能格式。

命名变化的背后是消费对象的迁移：Gems 面向「人来配置一个助手」，Skills 面向「Agent 调用一项能力」。前者是给人看的，后者要能被程序检索、组合、编排。

三家同时转向，说明技能与提示格式正在收敛为一种事实接口。对第三方开发者，这意味着一份技能有望在多个平台复用，是机会；同时，技能的描述方式一旦绑定某家规范，迁移成本也会随之上升。

> 原文：[The Decoder](https://the-decoder.com/google-drops-gems-for-skills-joining-openai-and-anthropic-in-the-shift-to-agent-ready-prompt-formats/)

## 火山引擎：语音也能像改文字一样改

火山引擎推出全新语音内容编辑模型，可对已录制的语音做类文本式编辑：改写内容，同时保留原声特征。

关键点是编辑对象为已录制语音的内容，而非重新合成一段新声音，「保留原声特征」正是这个能力的核心卖点。语音长期是一次性媒体，改一个字就要重录，这让播客、课程、客服录音的后期成本结构性偏高。

成本下降之后会跟上一个新问题：既然保留原声特征的改写几乎听不出接缝，取证、授权与内容标注就需要新的行业约定。技术先到位，规则通常慢半拍。

> 原文：[InfoQ](https://www.infoq.cn/article/07qzHLvyNXSW1SFNV5NV)

## 结语

今天这些动作指向同一个问题：当 Agent 有了常驻入口、手机号、钱包，甚至身体，谁来划定它替你做决定的范围？答案大概率不会由用户单方面给出。