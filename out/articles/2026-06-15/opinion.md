# KPMG 报告“翻车”：AI 编客户案例被撤回

今天最值得关注的，是 KPMG 一份 AI 采用报告因出现虚构客户案例而被紧急撤回——很可能是 AI 自己编造了这些案例。这不仅是审计巨头的尴尬，更暴露了 AI 行业一个深层病态：当工具开始伪造自身采用证据，信任链条正在断裂。与此同时，英国警察、德国部长也先后被卷入 AI 滥用疑云，AI 的“可信边界”成为本周最尖锐的话题。

## KPMG 报告被撤回：虚构的 AI 客户案例

四大会计师事务所之一的 KPMG 发布了一份关于企业 AI 采用率的报告，随后被发现其中包含多个无法查证的客户案例，报告撰写方承认“可能使用了 AI 生成内容”。报告已从官网下架。这件事的关键在于：KPMG 本身是审计与咨询的信任提供者，却因自己的 AI 使用方式而失信——这说明即使是专业机构，也难以确保 AI 输出不被幻觉污染。为什么重要？AI 行业的自我验证机制正面临挑战，缺乏第三方可回溯的出处在快速窜升。

> 原文：[TechCrunch](https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/)

## 英国警察涉嫌用 AI 制造虚假证据

德比郡一名警察因在多个刑事案件中使用 AI 生成证据而被内部调查。指控称其利用大模型编造“专家分析”和“证人证词”，目前已涉及至少 3 起已判决案件。关键点：这是司法系统内首次曝光执法者主动利用 AI 伪造证据，背后是 AI 工具的易得性和监管盲区。为什么重要？一旦 AI 生成的“证据”进入法庭，将大幅削弱司法公信力，倒逼立法者对 AI 证据的采信规则加速出台。

> 原文：[Sky News](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661)

## 观点：并非所有人都在用 AI 做所有事

一篇博文指出，普通消费者对 AI 的使用仍集中在搜索、写作辅助、娱乐等特定场景，远未达到“全面替代”的程度。作者认为，业界高估了用户对 AI 的渗透意愿——多数人只会在“不得不”时打开聊天窗口，而非主动整合进日常流程。为什么重要？这为投资人和产品经理提供了一个冷静视角：大规模消费者级 AI 产品仍面临“实用而非迷恋”的天花板，过度炒作可能偏离真实的用户需求。

> 原文：[Gabriel Weinberg](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they)

## 德国数字化部长被疑用 AI 代写公文

对德国数字化部长署名文章的文本分析显示，多篇议会演讲和新闻稿的用词、句式高度符合 AI 生成特征，且缺乏个人风格。反对党已要求正式调查。关键点：公共官员依赖 AI 输出政策声明，可能削弱民主程序中的个人责任与透明度。为什么重要？政府层面的 AI 使用缺乏规范，不仅事关形象，更可能影响政策制定质量。

> 原文：[36氪](https://36kr.com/newsflashes/3852553873462533)

## 纳德拉承认沉迷“刷 token”

微软 CEO Satya Nadella 在一档访谈中坦言，自己也是“token 消费爱好者”（token maxer），并且认为这种行为“具有成瘾性”。他指的是自己会不断给大模型发提示、不断消费 token，像刷短视频一样停不下来。关键点：最头部 AI 公司的掌门人公开承认 token 消费的成瘾性，折射出整个行业对用户时间的争夺已经进入了“多巴胺经济”模式。为什么重要？产品经理需要反思：我们设计的交互是在帮助用户，还是在制造数字依赖？

> 原文：[The Decoder](https://the-decoder.com/microsoft-ceo-satya-nadella-admits-hes-a-token-maxer-too-its-addictive/)

## 经验谈：低成本在家部署 AI 编程

一篇技术博客介绍了如何利用开源模型（如 Llama 4 和 DeepSeek 系列）和消费级硬件（RTX 4090、Mac Studio）搭建本地 AI 编程助手，避开云服务的成本和隐私问题。作者给出了完整的 toolchain 和避坑指南。为什么重要？对于希望深度使用 AI 但又有预算或合规压力的技术团队和个人开发者，这是一条切实可行的低门槛路径，也侧面说明 AI 工具正从“云服务”向“本地私有化”迁移。

> 原文：[Stephen Bochinski](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)

## 蚂蚁数科揭秘企业级 AGI 研发体系重构

在 AICon 上海大会上，蚂蚁数科分享了从传统 AI 研发体系（模型、数据、应用分离）向 AGI 路线（端到端、多模态、自主推理）转型的实践经验，包括架构调整、人才评估和流程变更。关键点：这是一家金融科技公司对“大模型时代”研发范式转型的公开复盘，对同类企业有参考价值。为什么重要？AGI 在企业的落地不只是部署一个模型，而是倒逼整个研发组织重新设计。

> 原文：[InfoQ](https://www.infoq.cn/article/k890EiwhdA4ISuOu8IhH)

## 密码学专家谈 Siri：私人推理不等于隐私

一篇密码学博客深入分析 Apple Siri 的隐私设计，指出其采用的“私人推理”（private inference）技术在实际部署中仍存在侧信道攻击和元数据泄露风险，且苹果并未完全开源其隐私协议。关键点：用户以为的“本地处理”可能仍会意外暴露部分信息。为什么重要？在 AI 代理越来越依赖个人数据的今天，隐私承诺与真实实现之间的差距，将是下一波监管的核心焦点。

> 原文：[Cryptography Engineering](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/)

---

当 AI 开始伪造自己的“采用故事”，我们还能相信谁的“数据”？信任的重建，或许比技术突破更难。