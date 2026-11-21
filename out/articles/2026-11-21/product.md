# Agent 开始接管桌面，隐私先出事了

今天的应用产品板块，最值得看的一件事是谷歌让 Gemini 直接操作 Mac 应用、在后台跑完多步工作流。这条不是功能更新，而是入口迁移：AI 从「你问它答」的对话框，挪到了「你说它做」的操作系统层。同一批消息里，苹果被曝在做同类 agent，Meta 的 Muse 撞上隐私事故，Signal 则干脆把截屏通道关掉。能力、平台、防护三件事同时到达，说明 agent 的产品设计已经从「能做什么」进入「边界在哪」。

## Gemini 开始替你操作 Mac

谷歌更新 Gemini，让它能操控 Mac 上的应用、整理文件、填写表单，并在后台完成多步工作流。关键点在「后台」和「多步」：这类任务不是单轮生成，而是拆解成一系列点击与输入，由模型串起来执行，用户中途不一定要盯着屏幕。为什么重要：这是 AI 助手第一次实质性跨过「生成内容」与「改变系统状态」的分界线。一旦 agent 能写文件、提交表单，产品的核心指标就从准确率变成可撤销性与可审计性——用户需要知道它做了什么、能不能回滚、出错时谁负责。这三项目前都还没有行业标准答案。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/)

## 谷歌搜索首页去掉了搜索按钮

谷歌搜索首页改版，移除了那个标志性的搜索按钮，并加入 AI 聊天历史侧栏。前者是符号层面的改变，后者是结构层面的：历史侧栏意味着搜索开始以「会话」为单位组织，而不是一次性的查询框。为什么重要：搜索产品的交互范式正在从「发起查询」转向「继续对话」，而对话是有上下文、有留存、可被持续追踪的。对广告业务来说，这既是新的位置，也是新的风险——答案页挤压点击，会话页则要求广告融入对话流。这次改版更像是在为后一种形态腾地方。

> 原文：[Ars Technica](https://arstechnica.com/ai/2026/11/googles-latest-search-page-redesign-drops-the-search-button-adds-ai-sidebar/)

## 苹果被曝研发控制 Mac 的 AI Agent

苹果被曝正在研发能控制 Mac 的 AI Agent，直接对标 Meta 的 Muse、Claude 与 OpenAI 的同类能力，同时据报道在设置新的壁垒。这条的重点不在「苹果也做了」，而在「壁垒」二字：操作系统厂商掌握辅助功能（accessibility）、屏幕录制、自动化脚本这些底层权限，第三方 agent 能做什么，最终由平台决定。为什么重要：桌面 agent 的竞争不会只在模型能力上分胜负，更在谁能拿到稳定的系统权限、谁被卡在门外。如果平台把关键 API 收紧到「自家 agent 优先」，这个赛道会迅速复制移动应用商店的结构。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/)

## Meta 的 Muse 把不同用户的对话搞混了

据报，Meta 的 AI Agent Muse 混淆了不同用户之间的对话，甚至向用户显示了他人关于育儿、职业建议的内容以及银行余额。这不是「模型说错话」级别的 bug，而是会话隔离失效——多租户系统里最基本的一道墙。为什么重要：agent 产品普遍在加记忆（memory）和跨会话上下文，以换取更好的连续性，代价是状态管理复杂度指数级上升。一旦记忆层与身份层耦合出错，故障就从「回答不准」升级成「数据泄露」。这条与今天其他几条放在一起看，几乎是一次及时的警告：给 agent 更多权限之前，先证明它分得清谁是谁。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/)

## Signal 直接关掉了截屏这条路

Signal 在 iOS 27 与 Android 上阻止截屏，理由是防止 AI Agent 读取私聊内容。逻辑很直白：端到端加密保护的是传输与存储，但屏幕是明文出口，任何具备屏幕读取能力的 agent 都能在这里绕过加密。为什么重要：这可能是第一个主流应用把「agent 读屏」当作需要防御的威胁模型，而不是当作要适配的新交互方式。代价也清楚——用户自己的截屏、无障碍工具、客服取证都会受影响。这是一次立场表态，也是一次与平台权限体系的正面摩擦，后续能否在两端系统上稳定生效，比功能本身更值得观察。

> 原文：[The Decoder](https://the-decoder.com/signal-blocks-screenshots-on-ios-27-and-android-to-stop-ai-agents-from-reading-private-chats/)

## Perplexity 用一个端点路由所有模型

Perplexity 推出 Orchestrator API，用单一端点路由 OpenAI、Anthropic、Google、xAI 与开源模型，并支持同一模型内的故障切换（failover）。关键点在于「故障切换」：这意味着路由层不只是做选型，而是在做可用性与成本的实时调度。为什么重要：模型路由正在从内部工程细节变成独立产品。它的价值随着模型数量增加而上升，但天花板同样明显——上游厂商随时可以把多模型调度做成自家 SDK 的默认能力，抽象层被吞掉是这类中间件的老剧本。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/19/perplexity-orchestrator-api-failover-model-routing/)

## Meta 新穿戴设备或定价 300 美元

Meta 新款 AI 穿戴设备 Muse Charm 被曝售价约 300 美元，公司称将很快公布更多信息。价格是本条里唯一有信息量的部分：300 美元落在一个「非冲动消费、但也不需要认真决策」的区间，比纯实验性质的硬件更容易铺量。为什么重要：穿戴设备在这个阶段的作用不是替代手机，而是给 agent 提供持续的输入通道——看见什么、听到什么、在什么场景。今天 Meta 在软件侧刚出隐私事故，硬件侧却要继续推进「常开传感器」，这个矛盾会是它接下来最难讲清的一件事。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/19/metas-new-muse-charm-device-may-cost-300/)

## 蚂蚁灵光把连接数堆到 54 项

蚂蚁集团的 AI 助手灵光新增企业微信、腾讯文档、腾讯会议等 7 项外部连接能力，可连接的外部服务增至 54 项。这 7 项的共同点很明确：都是办公协作场景里的高频入口，且分属腾讯生态。为什么重要：国内 agent 的竞争目前集中在「能连多少服务」这一维度，因为连接数直接决定任务能否闭环——不能读文档、不能进会议，agent 就只是个聊天框。真正的分水岭在于连接之后：是简单的读取调用，还是能代为执行并承担后果。54 这个数字好看，但下一步该看的是其中有几项支持写操作。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/walzAUin5QxPaCOQ.html)

## 结语

这一批消息拼出的图景是：agent 的能力边界在往前推，防护边界也在同步划线，中间那块地还没人定价。留一个问题给你——当桌面 agent 出错删了文件，你希望产品给你一个撤销键，还是一个责任主体？