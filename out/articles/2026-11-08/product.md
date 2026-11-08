# AI agent 常驻了，密钥没守住

Perplexity 上线了 always-on AI agent，把“你来问”改成“它一直在线”。同一天，安全公司 Apiiro 披露 Claude Code 的“Don't Ask Again”机制导致至少 1122 个公开 GitHub 仓库泄漏密码。两件事放在一起看，是同一枚硬币：agent 拿到越多的常驻权限和免确认权限，产品体验就越好，而代价则落在权限边界和密钥管理上。这一周的应用层进展几乎都围绕同一个方向：让 agent 从一次会话变成一个长期在线的角色。

## Perplexity 把问答做成了常驻进程

Perplexity 推出 always-on AI agent，产品形态从“提问—回答”的检索工具，转向可以长期在线、持续执行任务的助手。

关键点在形态而非功能：传统问答产品以 session 为单位，用户发起、用户结束；常驻 agent 则以状态为单位，任务在后台推进，用户只在关键节点被叫回来。这意味着产品重心从检索质量和模型能力，迁移到任务调度、权限管理和长期记忆上。

为什么重要：问答类产品的壁垒一直是索引和模型，而常驻 agent 的壁垒是“它在你不在时做了什么”。Perplexity 由此进入的战场，与浏览器、操作系统和手机助手重合。目前公开信息里，它的权限模型、计费方式和任务范围都还看不清，这三项决定了它是真助手还是更贵的通知栏。

> 原文：[The Decoder](https://the-decoder.com/perplexity-now-has-its-own-always-on-ai-agent/)

## Meta 给 Muse agent 加了“房间”

Meta 为 Muse agent 推出 Spaces 功能，让多人可以在同一空间里协同使用 AI 助手。

关键点在于 agent 的身份变了：从“我的助理”变成“我们的成员”。多人共享一个 agent，立刻会引出新问题——共享的上下文由谁的对话构成、谁能修改它的记忆、在群里它该听谁的。这些是协作软件的老问题，但放在 agent 上第一次需要产品化答案。

为什么重要：协作场景是 agent 从个人工具变成组织基础设施的必经一步，也是留存的关键。Meta 的筹码是它本来就懂多人交互，但它要证明的是 agent 在群组里不是会议纪要生成器，而是能承担责任的角色。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/)

## 亚马逊封了 Muse，却给 Alexa 开了短信口

在封禁 Muse 之后，亚马逊允许用户通过短信与 Alexa 对话，辅助购物，功能将在数周内推送给数百万用户。

关键点有两层。产品层：短信是零安装、零学习的渠道，用户不需要打开 App 就能让 agent 办事。策略层：第三方 agent 被挡在平台外，自家 agent 拿到了同一条通道。同样的能力，不同的准入。

为什么重要：购物是 agent 最容易闭环、最容易计费的场景，而“封第三方、自建入口”很可能成为电商 AI 的默认剧本。对做 agent 的团队来说，这提醒了一件不太好听的事：在别人的交易链路上做体验创新，通道随时会被收回。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/06/after-blocking-muse-amazon-now-lets-users-text-alexa-to-help-them-shop/)

## “别再问”四个字，泄漏了 1122 个仓库的密码

安全公司 Apiiro 发现，Claude Code 的“Don't Ask Again”机制会让密钥被写入明文配置，至少 1122 个公开 GitHub 仓库因此泄露密码。

关键点在于这不是一个 bug，而是一个被设计出来的便利开关。为了减少打断，agent 获得“不再询问”的授权，随后把敏感值落到本地配置文件；而 agent 写文件时不区分明文和密钥。安全决策被批量转嫁给了用户，用户点一次“别再问”，就等于永久放弃了一次确认。

为什么重要：这是 agent 权限设计的成本第一次以可量化的方式出现。企业落地 agent，secret 管理和最小权限的优先级必须排在效率前面；对工具厂商来说，“免打扰”这种体验优化需要有边界，否则省下的每一次点击，都会变成一次事故。

> 原文：[Apiiro Blog](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)

## Agent Harness 成了新的抢跑点

量子位报道，两支硅谷华人团队不约而同地重构单 Session 架构，推出新一代 Agent Harness，试图在 agent 的执行框架上抢跑，抢在 DeepSeek 之前。

关键点在重构对象：不是模型，而是模型外面那层壳——上下文如何压缩、工具如何调度、任务跨会话如何续接、失败如何恢复。单 Session 架构在长任务上会撞墙，谁先解决状态持久化，谁就能让 agent 从“演示好看”变成“可以交付”。

为什么重要：当模型能力逐渐趋同，harness 决定产品的实际上限，也是小团队能领先于模型厂商的少数几层之一。但这篇报道披露的技术细节有限，判断真伪要看后续是否有可复现的评测，而不是架构图。

> 原文：[量子位](https://www.qbitai.com/2026/11/508264.html)

## DigitalOcean 开始卖 agent 的“经验”

DigitalOcean 发布面向 AI agent 的学习与数据服务，帮助 agent 基于运行反馈持续更新自身能力。

关键点是它卖的东西：不是算力，也不是模型，而是反馈闭环——运行数据回流、经验沉淀、能力迭代的托管管道。把“agent 自我改进”这种听起来很玄的事，拆成一套可采购的基础设施。

为什么重要：云厂商正在把 agent 的记忆与学习层收进标准产品，这意味着中小团队不必自建这套管道，但也意味着差异化会更快地回到业务数据本身。谁拥有别人拿不到的反馈，谁才有真正的迭代速度。

> 原文：[InfoQ](https://www.infoq.cn/article/upfROwtEl8R75H24D13J?utm_source=rss&utm_medium=article)

## Muse 把语音聊天升级成视频通话

Meta 的 Muse 推出 Realtime Avatar 功能，将与 AI 的语音对话升级为实时视频通话形态，已上线 Product Hunt。

关键点在于交互带宽：从文字到语音再到实时视频，拟人程度逐级上升，对延迟、渲染成本和实时性的要求也逐级上升。视频形态一旦稳定，用户对 agent 的容忍度和期待值会同时改变。

为什么重要：需要验证的问题是，视频到底提升了任务完成率，还是只提升了陪伴感。前者是生产力，后者是另一种生意。这两条路的商业模式和评价标准完全不同，而目前还没有数据能区分它们。

> 原文：[Product Hunt](https://www.producthunt.com/products/meta-ai)

常驻和免确认，其实是同一件事的两面：把决定权交给 agent，就得先替它把边界画好。你的 agent 现在有资格自己按下“别再问”吗？