# 推理重器与 Agent 技能堆栈同时开始开源

今天开源板块最值得关注的是一条主线：DeepSeek 开源 DeepInfer，把推理侧优化再次变成公共品；同时，围绕 Agent 的“技能层”正在快速工具化，MiniMax、英伟达、GitHub、Infini-AI-Lab 在同一天不同方向上分别开工。判断是：模型能力的竞争正在下沉到推理效率与工程规范层，谁的中间层更早标准化，谁就更容易被别人的工作流默认采用。这也意味着，单点工具的开源热度会很快被“生态位”之争稀释。

## DeepSeek 开源 DeepInfer：把推理优化做成公共品

DeepSeek 开源了推理项目 DeepInfer，雷锋网对其推理优化技术做了拆解，并把它称为“又一开源重器”。关键点在于：DeepSeek 此前已经用开源模型确立了工程口碑；这次把推理侧优化单独拿出来开源，实际上是在交付一套可直接复用的部署知识，而不只是一个模型权重。对做推理服务、算力成本敏感的团队来说，这类项目的参考价值往往高于又一个新的 benchmark 分数——它直接影响单位 token 的成本曲线。为什么重要：当训练侧的差距被拉平，推理效率就是产品定价权的来源，开源则让这种优势迅速扩散成行业基线。

> 原文：[雷锋网](https://www.leiphone.com/category/ai/HecXToP0EHbPjPd0.html)

## MiniMax 开源 MCode Stack：把 Agent 技能写成文件

MiniMax 以 MIT 协议开源 MCode Stack，包含 17 个 SKILL.md 技能和 5 份清单，覆盖代码审查、子 Agent 拆分、上下文预算等方向。值得注意的是它的形态——技能以 Markdown 文件和清单交付，而不是代码 SDK，这意味着技能可以被阅读、被 diff、被组合，也更容易跨 Agent 框架迁移。上下文预算这类条目进入技能库，说明实践者已经把“省 token”当成需要显式管理的工程约束，而不是模型能力问题。为什么重要：Agent 的可靠性瓶颈正从模型转向流程约定；谁定义了技能的标准写法，谁就掌握了下一层的事实标准。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/28/minimax-open-sources-mcode-stack-agent-skills/)

## 英伟达开源 SkillSpector：技能也要做安全扫描

NVIDIA 发布 SkillSpector，用于扫描 Claude Code、Codex 和 MCP 技能中的漏洞、恶意模式、提示注入与数据外泄风险。它针对的问题很具体：当技能、提示词和 MCP 工具从外部引入时，Agent 实际上在执行一段来源不可信的指令，传统代码审计覆盖不到这一层。SkillSpector 把这类风险显式列为扫描对象，等于承认“技能供应链”已经成立。为什么重要：企业把 Agent 接入内部系统时，安全团队需要的正是这种能出具检查结果的工具；这类项目落地速度，往往决定 Agent 能不能过合规这一关。

> 原文：[GitHub](https://github.com/NVIDIA/SkillSpector)

## GitHub 开源 spec-kit：规范驱动开发的入门套件

GitHub 推出 spec-kit，帮助开发者上手规范驱动开发（SDD）等流程。这是 GitHub 在“AI 写代码”语境下的一次方向表态：重点仍放在先写清规范，再让模型执行，而非单纯提高生成速度。对团队来说，spec-kit 的价值不在于提供了多少功能，而在于把“规范先行”从方法论口号变成可 clone 的骨架，降低了流程改造的启动成本。为什么重要：编码 Agent 的产出质量强依赖于输入的约束强度，规范资产正在成为比提示词技巧更持久的团队护城河。

> 原文：[GitHub](https://github.com/github/spec-kit)

## 百度开源 Unlimited-OCR：长文档一次解析

百度发布 Unlimited-OCR，主打一次性长文档解析，探索长程 OCR 新范式。常规 OCR 流程往往需要先切分页面再逐段识别，长文档容易在切分处丢失结构信息；这个项目试图用单次处理覆盖整篇文档，把版面与上下文关系保留下来。它的实际意义在 RAG 与文档审阅场景中最直接——解析质量决定了后续检索的上限。为什么重要：在 Agent 处理真实世界文件的过程中，OCR 是最容易被低估、也最容易卡住流程的一环。

> 原文：[GitHub](https://github.com/baidu/Unlimited-OCR)

## Infini-AI-Lab 开源 Hermit：不改模型，只训外层

Infini-AI-Lab 发布 Apache-2.0 框架 Hermit，可从任务反馈中训练外部指令层、技能层、记忆层与工具层，且不改动 Agent 模型和 harness。这是一个明确的工程取舍：把学习信号留在外层，模型保持原样，因而可以随时替换底座模型，而不会让已积累的适配资产失效。对正在选型的团队来说，这种做法降低了被单一模型供应商锁定的风险。为什么重要：Agent 的持续改进如果只能靠在模型上微调，替换成本会高得难以承受；Hermit 这类框架试图把“经验”变成可迁移资产。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/29/infini-ai-lab-hermit-harness-adapter-framework/)

## Superpowers：给编码 Agent 一套方法论

obra/superpowers 开源了一套面向编码 Agent 的技能框架与软件开发方法论，核心主张是技能的可组合性。它和 MCode Stack 属于同一趋势的不同表达：把“怎么让 Agent 干活”沉淀为结构化的可复用单元，而不是每次重写提示词。这类项目的价值需要用项目实际效果来证明，但它们的出现本身说明，社区已经开始把 Agent 使用经验当作可以版本化的工程资产管理。为什么重要：方法论一旦开源，就会反过来影响工具的设计取向。

> 原文：[GitHub](https://github.com/obra/superpowers)

## VoiceStudio：全本地语音工作室

VoiceStudio 开源了一个完全本地运行的语音工作室，支持语音克隆、语音设计、视频配音、听写、转写和有声书制作，覆盖 646 种语言。定位很清楚：作为 ElevenLabs 的本地替代方案，把数据留在本地、把成本压到硬件侧。对内容团队与有隐私约束的场景，这比多几个音色更有吸引力；同时，语音克隆能力的本地化也意味着滥用风险随之下放，配套的合规与授权机制需要自行补齐。为什么重要：语音是最先被“本地化开源”攻破的生成式模态之一，API 生意的护城河正在变浅。

> 原文：[GitHub](https://github.com/debpalash/VoiceStudio)

今天八条里有五条在争夺“Agent 技能层”的定义权——真正的问题不是谁家技能更多，而是谁的写法会先被别人抄走。