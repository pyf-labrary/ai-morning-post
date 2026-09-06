# 开源Agent的一天：技能、体检与平台

当 Anthropic 把 Agent Skills 规范开源、NVIDIA 转头就送上安全扫描器，这个板块正在从“单点工具”走向“生态基建”。今天最值得关注的不是某一个模型跑得多快，而是开源的 AI Agent 供应链——从标准、验收到训练平台——在同一天集体补位。

## FreeToken：RTX 4060 跑 35B 模型，消费级推理再进一步

UC Berkeley 与 MIT 联合开源的 FreeToken 宣称可在 RTX 4060 上以约 39 Token/秒的速度运行 35B 参数模型。相比同类方案动辄需要 24GB 以上显存，FreeToken 在显存优化上做文章，把旗舰模型的本地推理门槛拉到了主流甜品卡区间。

关键点在于：它不是量化妥协，而是在推理路径上做显存调度优化。39 Token/秒对交互式对话勉强可用，对批量任务则相当从容。消费级显卡跑 35B 不再是“能跑但没法用”。

对大模型本地化部署而言，硬件墙是比算法墙更现实的瓶颈。FreeToken 如果真如论文所示具备泛化性，将直接扩大开源模型的端侧应用场景——从个人助手到离线分析，都值得重新算一笔账。

> 原文：[InfoQ](https://www.infoq.cn/article/tij5T0vJ1Yk0s7Uov7SE?utm_source=rss&utm_medium=article)

## Anthropic 开源 Agent Skills 官方仓库：Claude 技能有了标准形态

Anthropic 正式公开 Agent Skills 公共仓库，提供 Claude 技能的标准定义与参考实现。开发者可以将可复用的指令、工具调用链与工作流打包为“技能”，在 Claude Code 及其他支持 agentic 模式的环境中直接挂载使用。

这个仓库的价值不在于代码量，而在于它定义了技能的目录结构、描述格式与调用约定——相当于给 AI Agent 生态补上了一层“包管理规范”。此前各家 agent 的能力复用基本靠复制提示词，现在有了官方参考模板。

Agent 开发正在从“写 prompt”演进到“组装技能”。Anthropic 作为头部模型厂商主动制定这一层标准，意图显然是抢占开发者心智。开源的另一个好处是：社区贡献的技能反过来也在为 Claude 生态做数据飞轮。

> 原文：[GitHub](https://github.com/anthropics/skills)

## NVIDIA 开源 SkillSpector：给 Agent 技能做安全体检

就在 Anthropic 发布 Agent Skills 之后，NVIDIA 释出了 SkillSpector——一个专门扫描 Claude Code、Codex 及 MCP 技能的安全工具。它检测提示注入、数据外泄风险和供应链攻击面，能在技能安装前给出“体检报告”。

技能生态的爆发必然伴随投毒风险。恶意技能可能藏在看似正常的指令里，诱导 agent 输出敏感数据或执行危险操作。SkillSpector 的切入点正是这个新兴攻击面：把技能当作第三方依赖来审计。

这标志着 Agent 安全开始从“模型行为对齐”走向“供应链治理”。当技能市场出现，安全扫描就是基础设施，不是可选项。NVIDIA 这步棋，既补了生态缺口，也给自己在 Agent 开发工具链上占了个位置。

> 原文：[GitHub](https://github.com/NVIDIA/SkillSpector)

## UC Berkeley 发布 CUA-Lite：computer-use agent 的统一训练场

CUA-Lite 将沙箱环境、数据集、评测基准和强化学习框架整合进一个开源平台，目标是让 computer-use agent（能操作电脑完成任务的智能体）的训练与对比不再各自为政。研究者无需自行搭建 GUI 环境或拼接评测管线。

computer-use agent 的痛点从来不是模型结构，而是数据与评测的碎片化。CUA-Lite 这类平台的意义在于：它提供了统一的“度量衡”，让不同 agent 在同等条件下被比较，也让训练数据可以标准化地共享和迭代。

当 agent 开始操作真实软件界面，安全沙箱和可复现评测就变成了行业公共品。这个平台如果被学术界和工业界采纳，会显著压缩 computer-use agent 从论文到产品的周期。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/09/05/uc-berkeley-researchers-release-cua-lite-an-open-platform-unifying-sandboxes-data-evaluation-and-rl-for-computer-use-agents/)

## Nous Research 开源 hermes-agent：主打个人化成长的智能体

Nous Research 发布 hermes-agent 开源仓库，核心定位是“随用户使用持续演进”的个人化 agent。它会记录交互反馈、调整行为偏好，在长周期使用中逼近用户个人工作习惯——你可以把它理解为一个越用越懂你的本地智能体。

个人化 agent 此前的挑战在于长期记忆和持续学习还停留在论文阶段。hermes-agent 选择直接开源实现，让社区可以直接使用和二次开发。Nous Research 在开源社区的号召力意味着它有机会快速积累真实使用数据。

通用 agent 拼的是能力上限，个人化 agent 拼的是陪伴深度。一旦“越用越懂你”形成体验壁垒，转换成本会非常高。这条赛道上，开源先发者的优势不容小觑。

> 原文：[GitHub](https://github.com/NousResearch/hermes-agent)

## opencode 登趋势榜：自托管编码 Agent 需求仍在爬坡

开源编码智能体 opencode 在 GitHub Trending 上热度上升。作为可自托管的编程助手，opencode 直接对标 Copilot 类的闭源产品，让开发团队把代码补全和 agentic 编程能力部署在自己的基础设施内。

代码数据是很多企业不愿外送的核心资产。opencode 这类工具的持续走热说明：开发者对“代码助手用自己的数据训练”这件事的诉求，不是小众偏好，而是结构性需求。

编码 agent 的竞争正在从“模型能力”转向“工作流整合”。opencode 的热度验证了自托管路线的市场空间，但能否在插件生态和 IDE 体验上追平商业产品，是它接下来要过的关。

> 原文：[GitHub](https://github.com/anomalyco/opencode)

## VoiceStudio：本地运行的开源 ElevenLabs 替代品

VoiceStudio 是一个可完全本地运行的开源语音工具包，支持语音克隆、声音设计、视频配音与转录，覆盖 646 种语言。对隐私敏感或需要大批量配音的用户来说，它提供了不依赖云 API 的另一种选择。

本地运行意味着零推理费用和数据不出域。646 种语言的覆盖面也让它不只是“玩具级”替代品，而是一个有实际生产力的工具集。语音克隆的伦理风险也让开源社区多了一份责任——好在代码公开意味着监管和审计也能跟上。

语音赛道长期被闭源 API 主导，VoiceStudio 这类项目正在把“配音权”还给用户。成本结构改变会催生新的应用形态：播客本地化、视频二创、无障碍阅读都能以更低门槛落地。

> 原文：[GitHub](https://github.com/debpalash/VoiceStudio)

## OmniVoice：600+ 语言的高质量语音克隆 TTS

OmniVoice 同样是主打多语言的语音克隆与合成系统，覆盖 600 多种语言。与 VoiceStudio 偏工具链不同，OmniVoice 更侧重 TTS 模型的训练与推理能力，目标是把小语种语音合成成本拉下来。

大型语言模型对小语种的文本支持已经不错，但语音侧一直是洼地。OmniVoice 这类开源项目出现，意味着小语种内容创作者不必再等商业公司“排期”支持自己的语言。

两个语音项目同日上榜，指向同一个趋势：语音正在从“封闭 API”走向“开源可训练”。当合成质量跨过可用线，多语言音频内容的生产成本会直线下降——这是内容出海和本地化服务可以立刻利用的变量。

> 原文：[GitHub](https://github.com/k2-fsa/OmniVoice)

---

Agent 的“技能—体检—训练—发行”闭环在今天一天之内被开源项目补齐了四块拼图。接下来值得追问的是：当技能可以像 pip install 一样安装，谁会先造出那个中毒的包？

> 原文汇总：[FreeToken](https://www.infoq.cn/article/tij5T0vJ1Yk0s7Uov7SE?utm_source=rss&utm_medium=article) · [Agent Skills](https://github.com/anthropics/skills) · [SkillSpector](https://github.com/NVIDIA/SkillSpector) · [CUA-Lite](https://www.marktechpost.com/2026/09/05/uc-berkeley-researchers-release-cua-lite-an-open-platform-unifying-sandboxes-data-evaluation-and-rl-for-computer-use-agents/) · [hermes-agent](https://github.com/NousResearch/hermes-agent) · [opencode](https://github.com/anomalyco/opencode) · [VoiceStudio](https://github.com/debpalash/VoiceStudio) · [OmniVoice](https://github.com/k2-fsa/OmniVoice)