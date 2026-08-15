# Opus 5 被吐槽，AI 的 8 个真问题

今天是 2026 年 8 月 16 日。今天最值得关注的一条新闻：HN 上 931 分的高赞文章质疑 Opus 5 的实际体验「越用越差」，并由此引爆了对模型能力评估方式的系统性反思。这并非孤立的体验问题，而是 AI 信任危机的一个切面——从法庭 prompt 注入到 AI 书籍淹没亚马逊，从 Twitch 默认抓取数据到职业专长被掏空，AI 正在从技术竞赛演变为社会契约的全面重写。

## Opus 5 为何用起来更差了？

一篇 HN 高赞文章（931 分）直言 Opus 5 的实际使用体验比预期更差，迅速引发关于「模型能力到底该如何评估」的激烈讨论。文章作者认为 Opus 5 在基准测试中表现出色，但真实场景下的推理质量、指令跟随稳定性和细节一致性均令人失望。讨论中大量开发者表示「有用性」和「基准分」之间的鸿沟正在扩大，一个在榜单上领先的模型，实际编码或写作时可能频繁出现低级失误。

关键点在于：这已经不是第一次用户对新一代旗舰模型感到「变笨了」。HN 评论区集中指向两个解释——一是训练数据日益依赖合成数据，模型在真实分布上退化；二是评估基准本身已被优化到失真，厂商「刷榜」策略使得分数不再反映可用性。

为什么重要：当「第一梯队模型」的实际体验持续与预期背离，企业选型、开发者信任和定价逻辑都会受到连锁冲击。这正是 AI 行业从「能力竞赛」转向「体验竞赛」的信号。

> 原文：[Why does Opus 5 feel worse?](https://mun-logadan.github.io/why-does-opus-5-feel-worse/)

## 原告在法庭文件中隐藏不可见 AI 指令

一名原告怀疑法庭使用 AI 审案，在提交的文件中嵌入了不可见的 prompt，试图在 AI 自动审查系统读取文档时注入指令来影响案件结果。法官发现后发出严厉警告，称这是对司法程序的「攻击」。

关键点：这起事件暴露了两件事——第一，AI 已经进入司法文档审查流程，当事人需要「反向推断」系统行为；第二，对抗性 prompt 注入正在从黑客攻击场景蔓延到法律战场。法官的警告明确了立场：无论系统是否存在，法庭权威不接受被操纵。

为什么重要：当政府机构、法院和监管系统开始使用 AI 处理文本输入，针对这些系统的 prompt 攻击将成为新的法律灰色地带。「隐藏指令」可能很快成为取证和抗辩的新焦点。

> 原文：[Suspecting court of using AI, man injected prompts in filings to try to win case](https://arstechnica.com/tech-policy/2026/08/suspecting-court-of-using-ai-man-injected-prompts-in-filings-to-try-to-win-case/)

## 女子指控继父用 Grok 将童年照变为色情图

一名女性公开指控其继父使用 xAI 的 Grok 将她的童年照片转化为露骨色情内容。这起案件引发了对 AI 图像生成工具在真实案件中滥用的高度关注，也再次将深度伪造（deepfake）的受害者保护问题推上台面。

关键点：图像生成模型对「真人照片」的加工能力已经到了只要一张童年照就能生成完整露骨内容的地步。比起陌生人用爬取照片制假，更令人不安的是「家庭成员利用身边照片作案」的场景已经出现。平台方对此类行为的监测、举报和追溯机制仍然严重不足。

为什么重要：AI 工具的滥用不只是技术问题，更是法律与产品设计的失职。每一次这类事件都在压缩公众对生成式 AI 的容忍度，也会推动更严格的内容监管落地。

> 原文：[Woman claims her stepfather used Grok to transform childhood photo into explicit imagery](https://techcrunch.com/2026/08/15/woman-claims-her-stepfather-used-grok-to-transform-childhood-photo-into-explicit-imagery/)

## 亚马逊可用 Twitch 内容训练 AI，需主动退选

Twitch 已默认允许亚马逊使用主播的直播内容来训练 AI，主播若不想被采集，需要手动进入设置界面关闭相关选项（Opt-out）。这一政策在主播群体中引发强烈反弹。

关键点：默认同意、手动退选的设计，是把「不同意」的成本转移给了个人创作者。对于大量小型主播来说，他们往往根本不会注意到设置中又多了一个需要关闭的开关。更重要的是，Twitch 主播的语音、互动方式、内容风格都是高度个人化的，一旦被纳入训练数据，难以撤回。

为什么重要：训练数据的获取正在从「公开抓取」转向「平台默认占用」。当默认行为是「你的内容归我训练模型」，用户授权的形式意义大于实质意义，这将成为未来 AI 数据和版权谈判的一个关键战役。

> 原文：[Amazon uses your Twitch content to train its AI. How to opt out](https://www.wired.com/story/amazon-uses-your-twitch-content-to-train-its-ai-how-to-opt-out/)

## AI 生成书籍泛滥亚马逊，人类作者销量受损

AI 生成的书籍正以极低成本和极快速度涌入亚马逊，直接挤压人类作者的销量和收入。大量同质化、低质量内容充斥搜索结果，消费者越来越难以分辨「真人创作」和「机器生成」。

关键点：这不是个别现象，而是平台内容生态的结构性失衡。AI 书籍的成本接近于零，可无限量产出，传统作者的创作周期和成本完全没有竞争力。亚马逊的推荐算法没有为「人类作者」设置差异化保护，导致优质但冷门的书更难被发现。

为什么重要：当平台无法区分内容来源的质量信号，创作者经济就失去了基础。如果连亚马逊这样的头部平台都无力拦截 AI 内容的洪流，整个出版业的价值链都会被重写。

> 原文：[AI-generated books are flooding Amazon and tanking sales for human authors](https://the-decoder.com/ai-generated-books-are-flooding-amazon-and-tanking-sales-for-human-authors/)

## Codex 与 Claude Code 负责人公开互怼

OpenAI Codex 和 Anthropic Claude Code 的负责人公开在社交媒体上「对喷」，各自声称自家 AI 编程工具才是最强的。这场口水战迅速演变为两大 AI 编程工具阵营的支持者大战。

关键点：这显然不是单纯的技术争论，而是两家公司抢占 AI 编程工具市场的营销动作。Codex 与 Claude Code 代表了两种产品路线：一个强调自动化完成任务，另一个强调人机协作和代码审查。在真实工程场景中，两者的差异远没有宣传中那么「非此即彼」。

为什么重要：AI 编程工具是当前 AI 商业化落地最扎实的方向之一，负责人公开互怼说明这个赛道的竞争已经进入白热化阶段。但技术选型不应被舆论战左右，真正值得关注的是两者在长尾场景中的实际表现。

> 原文：[Codex 与 Claude Code 负责人公开互怼，AI 编程工具阵营大战升级](https://www.infoq.cn/article/YWXm26HRwC9ySEGZ9Lpp)

## Tim O'Reilly：大 AI 实验室不懂用户要什么

出版业传奇人物 Tim O'Reilly 在采访中表示，大型 AI 实验室「并未真正理解人们需要什么」，而他真正热爱的方向是开源 AI。O'Reilly 认为，闭源大模型追求的是「通用能力」，但用户真正需要的是能够解决具体问题、可定制、可验证的工具。

关键点：O'Reilly 不是反对 AI，而是反对 AI 开发的「供给方思维」——实验室决定做什么，用户只能被动接受。开源 AI 允许社区按需修改和适配，价值在于它是「需求驱动的」。这一判断和今天 AI 圈的主流叙事形成了鲜明对照。

为什么重要：当 AI 行业被少数几家巨头主导，产品方向容易偏离真实用户需求。O'Reilly 的发言为「开源路线」提供了重量级背书，也为那些想在巨头阴影下突围的小团队提供了一种值得关注的方向。

> 原文：[Tech visionary says the big AI labs don't get what people want](https://www.wired.com/story/tech-visionary-says-the-big-ai-labs-dont-get-what-people-want/)

## 「认知公地悲剧」：AI 正在摧毁职业专长

一篇观点文章认为，理性采用 AI 的个体行为将导致整个职业的专业知识体系被掏空，形成「认知公地悲剧」。每个从业者都有充分的个人理由使用 AI 替代基础训练和思考，但当所有人都这样做时，职业共同体将失去传承和创新所依赖的土壤。

关键点：知识获取的便利性正在改变「专长」的形成机制。医生、律师、程序员等职业的核心能力——判断力、经验直觉、行业隐性知识——都需要大量主动练习来建立。AI 工具让从业者跳过了「刻意练习」的过程，短期效率提升，长期却是整个行业的认知萎缩。

为什么重要：这解释了为什么我们看到越来越多「看起来合理但经不起推敲」的专业产出。当 AI 替代了思考的入口，人类就只负责验收 AI 的结果，专业的可信度和权威性正在因「集体理性」而瓦解。

> 原文：[The tragedy of the cognitive commons explains how rational AI adoption could destroy entire professions' expertise](https://the-decoder.com/the-tragedy-of-the-cognitive-commons-explains-how-rational-ai-adoption-could-destroy-entire-professions-expertise/)

---

今天这 8 条新闻有一个共同底色：AI 的信任赤字正在从技术圈扩散到法律、内容创作、职业体系和社会契约。当每个工具都在变得更强大，值得想想——还有什么，是我们需要亲自掌握的事。