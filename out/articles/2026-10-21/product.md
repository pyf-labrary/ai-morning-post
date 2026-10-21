# Muse 破千万，分享功能遭暂停

Meta 的 AI 助手 Muse 上线 40 天，在美国拿到 1000 万下载，成为少数达到这一量级的 App；同一天，它把对话分享功能暂停了，因为分享会连带暴露个人与商业机密。这两件事放在一起看，是今天最值得注意的信号：AI 助手的分发曲线已经很陡，但隐私边界还没画完。其余几条也都指向同一处——ChatGPT 加了对话锁定、Yelp 让 AI 代打电话、Cloudflare 和 Exa 各自把「抽取」与「检索」做成更便宜的基础件。产品竞争的重点，正从「能不能做到」转向「边界定在哪、成本压到多低」。

## Meta Muse：增长与泄露同时到来

Meta 的 AI 助手 Muse 上线 40 天，美国下载量突破 1000 万，留存表现优于同类竞品；据 TechCrunch，此前只有 11 个其他 App 达到过这一里程碑。另一面是：用户分享对话时会暴露个人信息与商业机密，Meta 已暂停该分享功能并展开调查。

关键在于，分享恰恰是 Meta 最擅长的增长机制。当对话内容成为可传播的素材，它同时变成了泄露面——用户以为在分享一段有趣的回答，实际交出的可能是客户名、合同条款或健康信息。

对产品团队来说，这提醒了一件事：隐私不是合规附件，是需要和分享按钮一起设计的功能。功能回滚的代价不只是体验，还有刚建立起来的信任，而信任是留存的前置变量。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/metas-muse-hits-10m-u-s-downloads-in-40-days-a-milestone-reached-by-only-11-other-apps/)

## ChatGPT 新增对话锁定

OpenAI 为 ChatGPT 加入对话锁定功能，面向讨论私密话题或筹备惊喜等场景：临时把设备交给他人时，被锁定的对话不会暴露。

这是一个很轻的设计——不改变模型侧的数据处理，只在设备本地加一道授权。但它对准的是真实使用习惯：AI 对话正在变成个人数据密度最高的界面之一，涵盖工作材料、健康问题、人际关系。

放在今天看更有意思：Muse 因为分享外泄而收回功能，ChatGPT 则往内加锁。两家在同一天处理同一个问题的两端，说明「AI 对话算不算隐私空间」已经从讨论变成了产品决策。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/chatgpt-now-lets-you-lock-your-chats/)

## Yelp 让 AI 替你打电话问排队

Yelp 在 App 内嵌入多项 AI 功能，其中包括代用户致电餐厅查询等位时间，以及按记忆中记录的用户偏好生成个性化推荐。

代打电话是一个明确的 agentic 动作：从「回答问题」跨到「代替你执行」。在商户端没有 API 的地方，语音 agent 几乎是唯一可用的接口，这也让线下服务业成为 agent 最先能落地的地方。

真正需要回答的问题在另一侧：餐厅接到 AI 来电时是否知情、通话如何授权、商户体验会不会被批量的自动呼叫拖累。这些不解决，功能越顺手，外部性越大。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/yelp-can-now-call-on-your-behalf-to-check-wait-times-at-a-restaurant/)

## Cloudflare Clairic：一次前向抽字段

Cloudflare 在 Workers AI 上预览抽取模型 Clairic（原文标题写作 Clairic），一次前向即可返回带置信度的结构化字段，输入百万 token 定价 0.1 美元，输出不计费。

它的定位不是通用 LLM，而是专用抽取系统——这决定了成本和延迟结构与聊天模型完全不同。企业里大量真实需求其实就是「把文档变成字段」，用大模型做这件事长期属于过度配置。

值得关注的是价格信号：抽取这类高频、低创造性的任务，正在被专门模型和边缘部署重新定价。对做 RAG、票据、合同解析的团队，这会直接改写毛利结构。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/20/cloudflare-releases-clairic-a-system-one-extraction-model-on-workers-ai/)

## Exa 3.0：搜索 API 开始分层定价

Exa 升级到 3.0，换用更大的 embedding 模型，新增每千次 4 美元的 Exa Lite 档位与 Dynamic Highlights 能力，并称在其自跑的 8 项基准上超过 Perplexity、Brave 与 Parallel。

两个细节值得注意：一是分层定价，说明检索正在被当作商品化的基础件售卖，便宜档负责走量；二是「自跑基准」，横向对比需要打折扣，尤其是各家对检索质量的评测口径并不统一。

对 agent 产品来说，搜索 API 是决定答案质量的上游。当上游开始按价格分档，选择哪一档就变成产品定位问题，而不是技术选型问题。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/20/exa-3-0-search-api-lite/)

## 给植物当翻译：解读植物电信号

初创公司 Electric Plant 训练 AI 模型，解析植物茎秆中微弱的电流变化，试图把「植物语言」翻译成人类可读的信号。

其思路是典型的信号转标签：先用传感器采集生物电，再用模型判断对应状态。它和今天 Cloudflare 的抽取模型在方法论上其实同构——垂直领域里，把连续信号压成离散、可解释的输出。

叙事当然好听，但在看到规模化的采集成本、标注准确率和可复现的实验数据之前，更适合当作研究方向而不是产品来看。农业场景真正的门槛从来不是模型，而是传感器铺得够不够密。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/plants-can-speak-using-electricity-so-this-startup-built-an-ai-model-to-decipher-their-language/)

## Figma 联创：MCP 不完美，但都会支持

Figma 联合创始人 Dylan Field 表示，MCP 并非一个完美的协议，公司计划尽可能多地支持各类标准，同时避免把全部数据暴露出去。

这段话的价值在于它承认了一个现实：接口标准正在快速收敛，但收敛不等于成熟。对设计工具而言，文件里的图层、组件和版本历史本身就是核心资产，全量接出去等于把护城河交出去。

对做集成的产品经理，这是同一份路线图上的两个约束：不接生态会被绕开，接得太深会失去议价能力。真正的设计题是「接什么、以什么粒度接」，而不是「接不接」。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/20/figma-co-founder-dylan-field-thinks-mcp-is-not-a-perfect-protocol/)

今天所有功能更新背后，其实都是同一道题：能力已经够用，剩下的是边界和成本。你所在的产品，分享按钮旁边有没有一个「锁」？