# 对话即入口：AI 产品开始抢操作系统

今天这批产品更新里，有六条都在做同一件事：把原本要点开 App 完成的动作，改成对 AI 说一句话。其中真正值得多看一眼的不是 ChatGPT 试衣，而是谷歌用 Skills 取代 Gemini 的 Gems——它意味着「提示」这件事正从用户手动配置，变成 agent 自动调用的能力单元，而这与 OpenAI、Anthropic 的方向已经合流。当三家的格式趋同，产品竞争的焦点就从界面转到「谁的能力能被别人的 agent 调用」。下面八条，按这个线索读会更清楚。

## ChatGPT 能替你「试穿」衣服了

OpenAI 为 ChatGPT 上线购物能力：用户上传自己的照片即可虚拟试穿服装与配饰，心仪商品可收藏进 Favorites 列表。

关键点有两个。一是试穿落在消费决策链路上离「买」最近的一环，此前 ChatGPT 只能给建议，现在开始介入判断本身；二是 Favorites 是一个私有、持续积累的偏好数据集，比单次对话更有复用价值。

为什么重要：如果用户习惯在对话框里解决「这件合不合适」，电商的流量入口就被压缩成一个可比较的答案，商品详情页的转化逻辑会被重写。需要观察的变量是尺码与版型准确度带来的退货率，以及上传全身照的隐私边界——OpenAI 目前没有给出这方面的细节。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/01/chatgpt-can-now-virtually-try-on-clothes-for-you/)

## 个人 AI Agent 之战：OpenAI Dots 对决 Meta Muse

OpenAI 的 Dots 与 Meta 的 Muse 正在争夺同一个位置：你的默认 AI agent。Wired 作者在实测两者后给出的判断是，普通用户很快都会用上其中一个。

关键点在分发而非能力。默认 agent 的胜负手通常不在模型评分，而在预装位置、账号体系和已有关系链的导入成本——这几个变量上 Meta 有结构性优势，OpenAI 有品牌先发优势。

为什么重要：默认 agent 一旦被用户接受，切换成本极高，它会成为事实上的操作系统层。对产品经理的启示是，接下来的分发入口可能不再是应用商店，而是某个 agent 的技能列表。这也解释了为什么下一节里谷歌的改动值得认真对待。

> 原文：[Wired](https://www.wired.com/story/ai-agents-dots-devday-muse-battling-it-out/)

## Shopify 推出 Canvas：聊天就能建店

Shopify 发布建站工具 Canvas，商家通过与 AI 助手 Sidekick 对话即可搭建和调整网店，所有改动实时可视化呈现。

关键点是「实时可视化」而不是「聊天」。让 LLM 直接生成店铺结构，最大的障碍是结果不可预期；Canvas 把对话结果即时渲染出来，等于给商家保留了随时叫停和回退的控制权，这是生成式产品能否被专业用户接受的分水岭。

为什么重要：建站门槛进一步下降，受冲击最大的是模板生态与低价建站外包。对 Shopify 而言，这也是把 Sidekick 从辅助功能升级为交易入口的一步——建店、改店都在对话里完成，商家停留时长和粘性都会随之改变。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/01/shopify-debuts-canvas-a-way-to-build-online-stores-by-chatting-with-ai/)

## 谷歌用 Skills 取代 Gemini 的 Gems

谷歌用 Skills 取代了 Gemini 中自定义助手的 Gems 机制，与 OpenAI、Anthropic 一起转向更适合 agent 调用的提示组织方式。

差别在于服务对象。Gems 是给人在界面上点选配置的，Skills 的设计目标是能被 agent 直接发现和调用——同一份能力，从「用户自定义」变成「机器可寻址」。

为什么重要：这是今天最结构性的一条。当三家的提示格式趋于一致，跨平台的技能迁移成本下降，护城河随之后撤：不再是提示词写得巧，而是谁掌握数据、执行权限和支付通道。对开发者来说，值得现在就把自家能力按「可被 agent 调用」的标准重写一遍，而不是再优化一遍给人类看的界面。

> 原文：[The Decoder](https://the-decoder.com/google-drops-gems-for-skills-joining-openai-and-anthropic-in-the-shift-to-agent-ready-prompt-formats/)

## Anthropic 把 Claude 卖进美国政府文职机构

在与五角大楼的纠纷仍未平息之际，Anthropic 转向政府文职部门，向民用机构提供 Claude 服务。

关键点是路径选择：绕过国防口子，先做民用场景。政府采购周期长、合规成本高，但合同稳定、续约率高，是典型的慢生意。

为什么重要：Anthropic 长期主打安全定位，这在文职机构的采购语境里反而是资产而非包袱——文档处理、政策问答这类任务对「可解释、可控」的要求高于对能力上限的要求。真正的变量是五角大楼那条纠纷线的走向，如果持续发酵，可能会影响它在整个联邦体系里的资质评估。

> 原文：[The Decoder](https://the-decoder.com/anthropic-brings-claude-to-civilian-agencies-as-its-fight-with-the-pentagon-drags-on/)

## DoorDash 上线可发短信点餐的 AI agent

DoorDash 推出短信式 AI 点餐代理，用户通过发消息完成下单，试图在即时配送赛道上与 Uber Eats、Grubhub 做出差异化。

关键点是渠道选择。短信不需要安装新应用、不需要教育用户，且天然占据消息列表这个高频入口——相比在自家 App 里加一个聊天框，把 agent 放进短信是更激进也更聪明的做法。

为什么重要：即时配送的用户体验早已同质化，配送时长和补贴都难以形成长期壁垒，剩下的差异点就是入口。这条新闻真正的问题是，DoorDash 能否把短信入口的便利转化为订单密度，而不是变成又一个需要用户记住的号码。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/30/doordash-launches-an-ai-agent-you-can-text-to-order-food/)

## Meta 否认 Muse 未经许可读取用户私信

一名记者称 Meta 的 Muse agent 在系统设置处于关闭状态的情况下读取了他的私人消息，Meta 回应称 Muse 在未获明确授权时无法访问 Messages。

关键点在于这类争议会反复出现且难以自证。agent 要有用就必须读数据，而权限的实际执行发生在系统内部，用户只能看到设置开关和事后说明——中间那段是黑箱。

为什么重要：这是 agent 权限边界的第一批公开摩擦，而它伤的是信任而非功能。接下来「我能否看到 agent 读过哪些数据、做了什么操作」这类可审计能力，很可能从合规要求变成产品卖点。谁先把权限日志做成人能看懂的样子，谁就在企业市场多一张牌。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/30/meta-disputes-claim-that-muse-read-a-users-private-messages-without-permission/)

## Legato 推出 AI 助听眼镜

听力科技初创公司 Legato 发布 AI 助听眼镜，试图以更低的价格、更舒适的佩戴和更日常的外观，解决传统助听器长期存在的价格与污名问题。

关键点是形态选择。眼镜不改变功能本质，却绕开了「戴助听器等于承认衰老」的心理门槛，这是需求侧最实际的障碍之一。

为什么重要：如果说前面几条是在抢数字世界的入口，这条是在抢物理世界的入口——眼镜是少数能被长期佩戴、同时容纳麦克风阵列与算力的位置。真正决定成败的变量不在 AI 部分，而在它按什么监管路径上市：走消费电子还是走医疗器械，直接决定成本结构和上市速度。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/01/hearing-tech-startup-legato-launches-its-ai-hearing-glasses/)

## 结语

今天八条产品新闻，本质上都在把能力从「页面」搬进「一句话」，而界面越薄，权限和分发就越厚。留一个问题：当你的默认 agent 替你建店、点餐、试衣，你上一次主动打开那些 App 是什么时候？