# 马斯克败诉，Karpathy 转投 Anthropic

今天最值得关注的是，Elon Musk 诉 OpenAI 及 Sam Altman 的 1340 亿美元诉讼被陪审团驳回，法官维持判决，Musk 称因“日历技术问题”逾期并已上诉。与此同时，OpenAI 联合创始人 Andrej Karpathy 宣布加入 Anthropic 预训练团队。一退一进之间，AI 行业的人才争夺与法律博弈正在升级。

## 陪审团一致裁决：马斯克起诉 OpenAI 太迟，败诉

**是什么：** 2024 年 Musk 起诉 OpenAI 及 CEO Sam Altman 违反非营利初衷、转向闭源获利，索赔 1340 亿美元。陪审团在审理后一致驳回，法官随即确认判决。

**关键点：** 驳回理由是原告提起诉讼过晚（timeliness），Musk 本人的证词中承认“知道某些事实但未及时行动”。Musk 已表示将上诉，称这是“日历技术问题”。

**为什么重要：** 该案曾被视为 AI 开源与闭源博弈的标杆诉讼，但法院未就 OpenAI 是否违背非营利使命作出实体裁决，而是程序性驳回。这意味着 OpenAI 在应诉层面的风险暂时解除，但未来类似诉讼中时效抗辩是否总有效，仍存疑问。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/)

## OpenAI 联创 Andrej Karpathy 加入 Anthropic 预训练团队

**是什么：** 前 OpenAI 联合创始人、前特斯拉 AI 总监 Andrej Karpathy 在离开 OpenAI 近两年后，选择加入 Anthropic，负责大规模预训练（pre-training）工作。

**关键点：** Karpathy 长期以来是全球顶尖的深度学习研究者，尤其在语言模型预训练和强化学习方面有深厚积累。Anthropic 正加速推进下一代基础模型，Karpathy 的加入将直接强化其预训练能力。

**为什么重要：** 这是继 Ilya Sutskever 离开 OpenAI 创立 Safe Superintelligence 之后，又一关键人才的离去。Anthropic 借此获得了在预训练阶段就可对齐模型的技术路线，可能拉开与 OpenAI 在下一代模型（如 GPT-5）的竞争距离。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/)

## Mistral AI 收购维也纳物理 AI 创企 Emmi AI

**是什么：** 法国 AI 公司 Mistral AI 收购了总部位于维也纳的物理 AI 初创公司 Emmi AI，具体金额未披露。

**关键点：** Emmi AI 专注于将物理仿真与机器学习结合，用于机器人、自动驾驶等需要理解物理交互的场景。Mistral 此前以语言模型闻名，收购后预计将构建“语言+物理”的多模态能力。

**为什么重要：** 大模型厂商正从纯文本转向物理世界建模。Mistral 通过收购而非自研快速补齐短板，表明欧洲 AI 公司也在抢夺物理 AI 人才与资产，与美国的 Meta、Google 形成竞争。

> 原文：[Emmi AI 官方公告](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai)

## OpenAI 联合多家公司推广内容溯源与 SynthID 水印

**是什么：** OpenAI 宣布采用 C2PA 标准（内容来源与真实性联盟）和 Google 的 SynthID 水印技术，并推出新的内容验证工具，帮助用户识别 AI 生成内容。

**关键点：** 新工具将内置于 ChatGPT 和 DALL·E 输出中，标记元数据和水印，且通过开放 API 供第三方集成。OpenAI 同时与 Adobe、微软、Google 等公司联合推进该标准。

**为什么重要：** 随着 AI 生成内容泛滥，溯源成为监管和用户信任的核心。OpenAI 带头拥抱行业标准，既是为应对欧盟 AI 法案等合规要求，也是在抢夺“可信 AI”的话语权。

> 原文：[OpenAI 官方博客](https://openai.com/index/advancing-content-provenance)

## 百度无人车周订单破 35 万，李彦宏称开始单城盈利

**是什么：** 百度 Apollo 自动驾驶出租车（Robotaxi）周订单量达到 35 万单，累计落地全球 27 个城市。李彦宏表示部分城市已实现单个城市盈利。

**关键点：** 35 万周订单意味着日均 5 万单，规模效应下补贴成本下降。百度强调“单城盈利”是扣除运营成本和车辆折旧后的正向现金流，但目前未披露具体城市和利润率。

**为什么重要：** 百度成为全球第一家宣布 Robotaxi 单城盈利的公司，比 Waymo、Cruise 更早实现财务转折点。如果可持续，证明 L4 级无人驾驶的商用闭环可能在中国率先跑通。

> 原文：[量子位](https://www.qbitai.com/2026/05/419597.html)

## Anthropic 发事故报告：三项产品调整导致 Claude Code 质量下降

**是什么：** Anthropic 发布事故调查报告，承认其代码生成工具 Claude Code 在过去六周内质量明显下降，经过排查定位到三项产品变更。

**关键点：** 三项变更分别是：调整了代码补全的采样温度、修改了上下文窗口截断策略、以及一次不成功的 prompt 优化。Anthropic 已回滚相关改动并修复，模型质量恢复正常。

**为什么重要：** 大模型产品往往难以预测变更对下游任务的影响。本次报告坦承了“小修改导致大滑坡”的案例，对行业有警示意义：即使是大公司，一次不审慎的产品调优也可能带来数周的用户体验损害。

> 原文：[InfoQ](https://www.infoq.cn/article/yxuH0IZNUvwPGdAEKCFX)

## Anthropic 首次揭秘下一代 Claude 训练方式：用户反馈直接用于模型训练

**是什么：** Anthropic 公开了下一代 Claude 模型的训练流程，核心是直接利用用户反馈和模型“做梦”（dreaming）产生的合成数据进行强化学习。

**关键点：** 所谓“做梦”数据是让模型在无标注情况下自主生成推理过程，然后筛选高质量轨迹作为训练数据。用户“吐槽”（用户标记不满意输出）则被实时收集并用于偏好微调。Anthropic 强调该流程已在安全测试中通过了红队评估。

**为什么重要：** 这是业界首次大规模将用户实时反馈直接回注到训练循环中，可能大幅缩短模型迭代周期。同时，合成数据的使用减少了对人工标注的依赖，能更高效地扩展能力。如果成功，其他公司可能跟进，改变现有 RLHF 范式。

> 原文：[InfoQ](https://www.infoq.cn/article/8AFM65dK2wFMypqoz6ok)

当诉讼尘埃落定，人才的流向或许才是真正决定未来的暗流——Karpathy 的倒戈会让 Anthropic 更快抵达下一代模型吗？