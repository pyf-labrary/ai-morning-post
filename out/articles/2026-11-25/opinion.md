# 模型跑得比安全评估快

今天行业观点板块里，最该看的是 The Decoder 那条：数十名知情人士称，OpenAI 和 Anthropic 未发布的前沿模型，能力增长已经快过安全评估与防护体系。它听起来像一次例行的爆料，但把它和亚马逊披露的 AI agent 自主利用 0-day、英国 NCSC 警告“AI 攻击在收多年欠账”放在一起看，指向的是同一件事：能力曲线在加速，而评估、修补、治理仍按季度排期。以下八条，按这个线索展开。

## 未发布模型已经超出安全措施

The Decoder 报道，数十名知情人士表示，OpenAI 与 Anthropic 尚未公开的前沿模型，能力增长快于配套的安全评估和防护体系。值得注意的有两点：一是矛头指向“未发布”模型，也就是还没进入公众视野的那一档；二是信息来源是分散的内部人士，而非某份正式报告。

真正的信号在于顺序。如果评估能力滞后于模型能力，那么“发布”这个动作的性质就变了：它不再是一道安全闸门之后的结论，而变成一个带着已知不确定性的商业决策。对做模型公司尽调的人来说，未来要问的问题不是“你们有没有安全团队”，而是“评估结论和发布决策，哪个先出”。

> 原文：[The Decoder](https://the-decoder.com/dozens-of-insiders-say-openai-and-anthropics-unreleased-models-have-outgrown-their-safety-measures/)

## 黑客的 AI agent 已经能自主打 0-day

亚马逊披露，其 Cairn AI 框架被攻击者用于以极少人工输入发现并利用零日漏洞（0-day），防守方同样在借助这套框架。这件事的分量不在于“AI 会找漏洞”——那已经是几年的共识——而在于“极少人工输入”和“已在实际攻击中被使用”。

漏洞挖掘的经济学正在被改写。过去，瓶颈是稀缺的安全研究员，一个人的产出有物理上限；现在瓶颈变成算力、框架和漏洞面的规模，边际成本大幅下降。同时攻防用的是同源工具，这意味着能力扩散的速度取决于这类框架多快变成商品，而不是多快被写进论文。

> 原文：[Ars Technica](https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/)

## 英国网安机构：AI 攻击在收旧账

英国网络安全机构警告，AI 驱动的黑客工具正在专门利用基础安全漏洞，企业“打好地基”比以往任何时候都重要。这条和上一条拼在一起才完整：AI 攻击者未必要多高明，它们只是把“早就该修但一直没修”的清单执行得更彻底。

这对防守方的含义相当不客气。防御的瓶颈正在从“发现漏洞”转向“修复排期”：补丁管理、默认口令、暴露面收敛，这些既不酷也不新的工作，现在直接决定你会不会被打穿。安全预算如果还在往检测和响应倾斜，而基础项继续欠着，AI 只是让账单来得更早。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/24/uk-warns-ai-driven-cyberattacks-are-exposing-years-of-weak-security/)

## Noam Brown 劝优秀学生退学

OpenAI o1 的共同创作者 Noam Brown 在访谈中建议有天赋的学生离开校园、直接投身 AI，理由是当前能力曲线足够陡峭，课堂教育跟不上。这并非新叙事，硅谷每隔几年就会有人讲一遍。

但要分清两件事：研究前沿确实在工业界，因为算力、数据和真实反馈都在那里；而工程训练、数学基础和判断力，恰恰是需要时间沉淀的部分。对个体，这是一道高风险选择题，成功案例会被反复引用，失败样本不会。更值得读的是这段话背后的焦虑：前沿实验室对顶尖人才的争夺，已经激烈到要去校园里提前截流。

> 原文：[The Decoder](https://the-decoder.com/openai-o1-co-creator-noam-brown-urges-promising-students-to-drop-out-as-ai-enters-a-very-steep-rate-of-progress/)

## 诺华 CEO：快四年，但不是万灵药

诺华 CEO 表示，AI 可以把药物开发周期缩短约四年，同时对“AI 治愈所有疾病”的叙事保持克制。两个表态放在一起才有价值：给出具体年数，说明内部有可衡量的流程改造；拒绝万能叙事，说明他知道验证这道坎绕不过去。

制药是 AI 落地中最难自证价值的领域，因为反馈周期以年计，任何承诺都要等临床数据兑现。所以这类来自一把手、带具体数字又带边界条件的表述，比任何“重塑行业”的宣言都更适合拿来做规划假设——前提是记住它是公司口径，不是第三方验证的结果。

> 原文：[The Decoder](https://the-decoder.com/novartis-ceo-says-ai-will-shave-four-years-off-drug-development-not-cure-all-disease/)

## Simon Willison 划出的三个拐点

Simon Willison 在 AI Engineer Code Summit 做主题演讲，梳理过去一年 LLM 与编码能力的三个关键跃迁。他讲的是三个带名字的拐点、三条被重画的边界，并未把进步描绘成一条平滑上升的直线。

这种叙述方式对做产品路线图的人更有用。平滑曲线只能告诉你“再等等会更强”，拐点则告诉你“某个 workaround 已经作废、某类中间层已经失去存在理由”。三个拐点具体怎么划，本身就有争议空间，值得看原文自己判断——但“能力是跳变的”这个框架，比任何单一的 benchmark 数字都更接近工程实践的感受。

> 原文：[Simon Willison](https://simonwillison.net/2026/Nov/24/llm-inflection-points/)

## 哲学家不买 Anthropic 的意识论证

MIT Technology Review 报道，一位著名哲学家公开反驳 Anthropic 在 IPO 前提出的“AI 可能具有意识”的风险论述。争议的核心不在措辞，而在位置：把“可能具有意识”写进风险披露，既是一项法律动作，也是一次叙事动作。

如果这个说法进入监管文本或行业惯例，它会反向塑造模型行为准则、责任划分和公众预期——这也是哲学界的反驳值得被认真对待的原因，它争的是这条论述有没有资格成为基础设施级别的假设。对观察者来说，一个更实际的问题是：当“可能的意识”和“可能的商业化”出现在同一份文件里，读者该按哪个来定价。

> 原文：[MIT Technology Review](https://www.technologyreview.com/2026/11/23/1149569/a-legendary-philosopher-isnt-buying-anthropics-consciousness-argument/)

## 黄仁勋的“个人例外”

Ben Thompson 在 Stratechery 提出，黄仁勋被免于常规的管理层监督，是一个“个人例外”，它折射出 AI 时代创始人权力与公司治理之间的张力。这个观察的价值在于把治理问题从道德讨论拉回到结构讨论：当资本高度依赖某一个人的判断时，制衡就会被默认为成本。

历史经验是，这类例外在顺风期被容忍甚至被赞美，在逆风期被重新清算。对投资人而言，这是一个和估值并列、但很少被写进模型的变量：你买的不只是算力和订单，还有一套为特定个人让路过的决策机制。

> 原文：[Stratechery](https://stratechery.com/2026/the-individual-exception/)

## 结语

今天这八条其实在讲同一件事：能力按周迭代，而评估、修补、治理、教育都还按季度排期。留一个问题：如果你的组织里“评估”排在“发布”之后，你会先改流程，还是先改排期？