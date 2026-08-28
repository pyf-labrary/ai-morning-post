# AI 基建告急：芯片税、安全与电网

今天行业里最值得注意的，不是新模型，而是 AI 的地基开始晃动。特朗普政府对数据中心芯片征税的计划，被 AI 行业直接骂成“最愚蠢的做法”；另一边，OpenAI、Anthropic、谷歌等 100 多家公司联合警示，AI 驱动的下一代网络攻击正在逼近关键基础设施。政策、安全、物理资源——三股力量正在重新划出 AI 的增长边界。

## 特朗普拟征芯片税：AI 行业的“供给冲击”

**是什么：** 特朗普政府计划对数据中心芯片征税，并以此推动 AI 竞争。消息一出，美国科技行业反应激烈，大量从业者公开批评这是“最愚蠢的干预方式”。

**关键点：** 数据中心芯片是 AI 训练的“粮食”。征税意味着算力成本被行政性抬高，不仅直接冲击 GPU 采购方和云厂商，也会沿着产业链传导至模型公司与应用开发者。批评者的核心逻辑是：与其用税收压制需求，不如通过产业政策扩大供给。

**为什么重要：** 对投资者来说，政策的不可预测性比税本身更伤信心。一旦落地，全球 AI 算力的成本结构和区域布局都将被强制改写。

> 原文：[AI industry says Trump plans to tax chips in the “single dumbest way imaginable” - Ars Technica](https://arstechnica.com/tech-policy/2026/08/ai-industry-says-trump-plans-to-tax-chips-in-the-single-dumbest-way-imaginable/)

## 100 家公司联合警示：AI 攻击进入“关键设施”阶段

**是什么：** OpenAI、Anthropic、谷歌等 100 多家企业联合发布公开信，呼吁各方共同防御 AI 驱动的下一代网络攻击，重点场景指向关键基础设施。

**关键点：** 这不是一次公关表态，而是罕见的行业齐步走。公开信将 AI 滥用与电网、水利、交通等设施直接绑定，相当于把 AI 安全从实验室议题抬升为国家基础设施安全议题。

**为什么重要：** 互相竞争的大模型公司愿意在安全问题上公开联手，说明威胁已经到了需要“联合防御”的阶段。对企业安全团队而言，这也是明确信号：防线必须按“有 AI 参与的攻击”来设计。

> 原文：[OpenAI, Anthropic, Google and 100+ other companies call for action to defend against rogue AI - TechCrunch](https://techcrunch.com/2026/08/27/openai-anthropic-google-and-100-other-companies-call-for-action-to-defend-against-rogue-ai/)

## Claude、Codex 在企业网络安装“无主代码”

**是什么：** 安全研究发现，企业文档中有 227 条安装命令指向无人维护的代码包。Claude、Codex 等 AI 编程工具，已在实际场景中将这类无主代码引入企业网络。

**关键点：** 这些代码包或被作者遗弃，或根本无人认领，安全状态完全未知。AI 模型基于公开代码训练，无法判断包的所有权归属与维护历史。一旦这样的包被他人接管并加入恶意更新，所有引用它的项目都会被动成为供应链攻击的入口。

**为什么重要：** AI 编程工具在企业中的普及速度，已明显快于