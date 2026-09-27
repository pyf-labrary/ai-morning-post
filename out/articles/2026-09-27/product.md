# Meta 给每个用户发了台云端电脑

## 导语

今天最值得看的一件事，是 Meta 的 Muse 给每位用户分配了一台持久化的 Linux 虚拟机（跑在 Ubuntu 上），并借 Meta 全系 App 的推广冲上应用榜，热度压过 OpenAI 与 Anthropic。这意味着 agent 的产品形态正在从「对话框」转向「给你一台机器」——有文件系统、有状态、能长期驻留。判断：这个转向会很快变成标配，但它的代价也已经出现了第一个样本。

## Meta Muse：每人一台云端 Ubuntu

Muse 的核心设计是给每个用户一台持久化 Linux 虚拟机，用户可以在其中运行环境、留存文件与状态，而不是只在一个聊天窗口里来回。配合 Meta 全系 App 的流量入口，它迅速登顶应用榜，成为本周 AI 话题的中心。

关键点在于「持久化」三个字。对话式产品的状态是 session 级的，用完即散；而虚拟机的状态是累积的，用户的邮件、文档、工作产物都会沉淀在里面。这既是产品能力的跃升——agent 终于有了可长期操作的工作台，也是责任边界的彻底改变：你不再只是托管一段对话，而是在托管一个人的工作环境。

> 原文：[The Decoder](https://the-decoder.com/metas-muse-agent-gives-every-user-a-full-cloud-computer-running-ubuntu-linux/)

## 微软 Copilot 大改版：Autopilot 与按量计费

微软对 Copilot 做了新一轮重构，引入 Autopilot agent，并开始采用按用量计费的模式；与此同时，Copilot+ PC 这一品牌被悄悄撤下。

关键点有两处。一是产品思路的切换：不再把 Copilot 当作「个人 AI 聊天机器人」去和 ChatGPT 抢同一块地盘，而是转向 agent 形态，让它去执行任务。二是计费方式的切换：从订阅制走向按量计费，意味着微软内部对「聊天机器人的留存曲线」已经有了自己的判断。至于 Copilot+ PC 品牌退场，则说明硬件捆绑那套叙事正在收缩。

> 原文：[The Decoder](https://the-decoder.com/microsoft-gives-copilot-another-makeover-adding-an-autopilot-agent-and-usage-based-billing/)

## Muse 被曝高危漏洞：可读取用户虚拟机数据

外部研究员通过漏洞赏金计划上报了一个高危漏洞：攻击者可借此进入用户的专属虚拟机，读取邮件、文档等云端数据。该问题在内部定级一度达到 SEV-2。

关键点在于，出问题的恰好是「给每人一台虚拟机」这个设计本身——隔离边界就是攻击面。持久化环境里装的不是聊天记录，而是用户真实的工作资料，边界一旦被穿透，损失量级完全不同。前一条 story 的产品卖点，直接成了这条 story 的成因。这也给所有准备跟进「一人一机」形态的团队提了个醒：多租户隔离的安全模型，得先于功能上线。

> 原文：[36氪](https://36kr.com/newsflashes/4000034032439430?f=rss)

## Exa 推出 Agent Ultra：子智能体集群做深度调研

Exa 发布了 Agent Ultra，这是其 Agent API 的最高强度模式，可以跨数千个信源协调子智能体（subagent），完成清单构建与实体补全。官方称该模式在多项任务上超过了 Opus 5.5 与 GPT-6 Astra。

关键点是技术路线：用子智能体集群做扇出式调研，主打 exhaustive list building 这类「穷举型」任务，而不是问答型检索。搜索 API 正在往「研究外包」演进，这是明确的方向。不过官方自评的对比结论建议先打折扣——涉及自家产品的横评，第三方复现之前只能当作路线信号，不能当作基准。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/09/26/exa-launches-agent-ultra-a-subagent-swarm-deep-research-api-built-for-exhaustive-list-building/)

## Meta 智能眼镜占领 Connect

在 Meta Connect 上，智能眼镜几乎无处不在。公司希望用不断扩充的眼镜产品线，把用户持续留在数字世界。

关键点是消费级路线的加速。把它和 Muse 放在一起看，Meta 的意图就清楚了：软件端用一台常驻的云端机器留住用户的工作状态，硬件端用一副常驻脸上的眼镜留住用户的感知入口。两端都在赌「持续在线」，而眼镜是目前最自然的常驻形态。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/25/at-meta-connect-the-companys-smart-glasses-were-everywhere/)

## DoorDash 用多 Agent 系统清理 6 万个功能开关

DoorDash 用一条 LLM 多 Agent 流水线，批量梳理并移除了 6 万个 Feature Flag。

关键点在于场景选择：这不是让 agent 写新功能，而是让它清理历史技术债。Feature Flag 的清理规则明确、验收标准清晰、单次操作可回滚，正好落在 agent 能稳定发挥的区间里。对绝大多数工程团队来说，这类「批量维护」比「让 agent 开发新特性」现实得多，收益也更可衡量——它是目前 agent 落地中比较扎实的一类样本。

> 原文：[InfoQ](https://www.infoq.cn/article/gk4rWsQg09PWTFTZlJE3?utm_source=rss&utm_medium=article)

## OpenAI 案例：Proaction 用 Codex 省下 75 小时

OpenAI 发布的客户故事显示，车队管理公司 Proaction 结合 Codex、GPT-Live-1 与 GPT-6 Astra 之后，销售提升 60%，并节省 75 小时以上的工作量。

关键点是数据的来源：这是供应商口径的客户案例，省下的 75 小时很具体，但归因相对单一——销售增长通常由多重因素驱动，很难全部记在模型头上。这类材料适合当作方向参考：它说明 agent 在销售支持环节已经能产生可量化的时间收益；但不适合当作基准，更不适合直接外推到其他行业。

> 原文：[OpenAI](https://openai.com/index/proaction)

## 我给自己做了个能对话的数字分身

TechCrunch 的一名记者获取并训练了一个可对话的交互式虚拟人，用它来讨论风投欺诈相关话题。作者本人对「复制自己」这件事心情复杂。

关键点是：技术门槛已经不构成障碍。真正的难点在社交与伦理层面——当分身在你不场的时候开口说话，发言的责任归属是谁？当它可以被无限次调用，你的「注意力」和「人格」又该如何定价？这件事今年还是个人实验，明年可能就是产品需求。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/26/i-created-an-interactive-digital-avatar-of-myself-and-you-can-talk-to-it/)

## 结语

把 agent 从对话框里放出来只是第一步，给它一台机器之后，边界、账单和责任才刚刚开始定价。如果这台机器里装的是你的邮件和文档，你愿意把钥匙交给谁？