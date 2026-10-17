# Agent 基建升温：沙箱、系统与插件标准

今天开源板块最值得看的是两条「运行时」新闻：清华开源了一套智能体操作系统，宣称任务成本降低 83%、记忆可查可改；Perplexity 则把支撑 Perplexity Computer 的沙箱平台 SPACE 放了出来，每个 agent 任务跑在独立的 Firecracker microVM 里。这两件事指向同一个判断——开源 agent 的竞争重心正在从「模型能不能做」转向「任务怎么被隔离、记忆怎么被管理、技能怎么被分发」。再加上阶跃星辰放出 600B MoE 权重、三家大厂同日上线插件目录，今天这一批更新基本把 agent 基础设施的三层同时推了一步。下面按重要性逐条看。

## 清华开源智能体操作系统，主打成本与记忆

清华开源了一套智能体操作系统，官方口径是任务成本降低 83%。关键点有两个：一是 AI 记忆可查可改，二是原生支持 MCP（Model Context Protocol）。

「可查可改的记忆」是这条里最实的部分。当前多数 agent 的记忆是上下文窗口里的黑箱，出错只能重跑；如果记忆变成可审计、可编辑的结构化对象，排障和回滚才成立，这是从 demo 走向生产的前置条件。原生支持 MCP 则说明它选择接入现有工具生态，而不是另起协议。

成本降 83% 这个数字需要独立复现，参照系（对比什么基线、什么任务分布）也未公开，先当作方向性信号看。真正值得跟踪的是它的记忆层会不会被其他框架采用——那才是操作系统级野心能否落地的标志。

> 原文：[量子位](https://www.qbitai.com/2026/10/503935.html)

## Perplexity 开源 SPACE：每个 agent 一个 microVM

Perplexity 开源了支撑 Perplexity Computer 的沙箱平台 SPACE，核心设计是每个 agent 任务运行在独立的 Firecracker microVM 中，凭证与出网流量由外部统一管控。

这两点组合起来回答的是 agent 执行代码时最要命的两个问题：爆炸半径和权限。microVM 的隔离强度高于容器，单任务被攻破不会波及其他任务；凭证不注入沙箱内部、出网流量统一管控，则切断了「agent 拿到 key 就能横向移动」的路径。

这和 Claude Code 一类本地执行的思路正好相反——SPACE 面向的是云端多租户、不可信代码的场景。对想自建 agent 平台但不愿意自己写隔离层的团队，这是一个可以直接对标甚至复用的参考实现。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents/)

## 阶跃星辰开放 Step 5 Preview 权重：600B MoE

阶跃星辰（StepFun）在 Hugging Face 与 ModelScope 放出 Step 5 Preview 的 FP8/BF16 权重：600B 总参数、27B 激活、1M 上下文，明确面向长程 agent 任务。

600B 级别的 MoE 开放权重，把「自托管一个够用的长上下文模型」的门槛又压低了一档；27B 激活意味着单次推理的算力开销可控，这是能否真正跑起来的关键。1M 上下文加 agent 定位，说明调优目标已经从刷榜转向长任务的持续性——上下文长度不再是参数表上的一行字，而是决定 agent 能否连续工作几小时的前提。

需要留意的是 FP8 权重的实际体验高度依赖推理框架的支持成熟度，社区部署反馈通常比权重发布晚一到两周才成形，别急着下结论。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/16/stepfun-releases-step-5-preview-open-weights-600b-moe-27b-active-1m-context/)

## llama.cpp 跑在破解 PS5 上，原生加载 GGUF

有开发者让 llama.cpp 在破解的 PlayStation 5 上原生运行，可直接加载任意 GGUF 模型。

技术上这不是远程调用，而是把推理运行时真正搬到了游戏主机上，GGUF 生态的模型可以原样复用。实用价值有限，但象征意义清楚：GGUF + llama.cpp 已经成了事实上的「任意硬件跑模型」抽象层，从树莓派到游戏机只需要同一套格式和运行时。

对边缘推理和爱好者生态来说，这是成本最低的实验路径，也侧面说明模型权重的分发格式已经基本收敛。风险同样明确——依赖破解固件，不具备任何产品化前提，当作技术趣味和格式生态的注脚看更合适。

> 原文：[GitHub](https://github.com/cobanov/PS5LM)

## Claude、Cursor、Android 同日上线官方插件目录

Anthropic 的 claude-plugins-official、Cursor 的插件规范、以及 android/skills 在同一天出现，三家同时开始做 agent 技能与插件的官方目录。

信号很强：agent 的能力扩展正在从「个人 prompt 技巧」变成「官方分发渠道」。谁的标准被写得最多、被第三方适配得最广，谁就掌握生态入口——这层逻辑和当年 IDE 插件市场的争夺几乎一模一样。Android 的加入尤其值得注意，说明这套玩法正在从编码工具外溢到移动端。

对开发者而言，代价也立刻显形：同时维护三套插件格式的成本已经开始出现。短期内务实的做法是抽象出与格式无关的技能描述，再按平台做薄适配层。

> 原文：[GitHub](https://github.com/anthropics/claude-plugins-official)

## Agent Skills 社区框架混战：Superpowers、ECC 等

围绕编码 agent 的技能框架与上下文优化层正在快速迭代，Superpowers、ECC、context-mode 等项目集中出现在 GitHub trending 榜上。

这一层的共同目标是把「怎么教 agent 做事」工程化：技能如何组织、上下文如何压缩、哪些信息该常驻、哪些该按需加载。标准尚未确定，工具层先卷了起来，说明需求真实存在。

这类项目的生命周期通常不长，但它们的价值在于替整个生态做实验——哪些技能真的提升成功率、哪些上下文压缩方式不损伤效果，答案会先出现在这里，再被官方插件目录吸收。选型时建议看能否迁移到官方格式、以及是否有可复现的评测，而不是看 star 数。

> 原文：[GitHub](https://github.com/obra/superpowers)

## VoiceStudio：完全本地的开源 ElevenLabs 替代

VoiceStudio 是一个完全本地运行的开源语音工具，覆盖声音克隆、语音设计、配音、听写、转录与有声书生成，宣称支持 646 种语言。

语音是数据敏感度最高的模态之一：用云端 TTS，等于把原始音频和说话人特征交出去，很多企业内网和合规场景根本不允许。全本地运行直接绕开了这一层，这是它相对商业方案的核心差异点，而不是音质。

646 种语言的覆盖面如果成立，对小语种内容生产是实质性变化——商业 API 在这类语言上通常质量参差甚至缺席。不过覆盖语言数与各语言的实际质量分布是两回事，落地前需要按目标语种实测。

> 原文：[GitHub](https://github.com/debpalash/VoiceStudio)

## 模域 ModelSphere：开源一站式生产级 AI 部署平台

范式智能联合睿思智联推出开源生产级 AI 部署平台「模域 ModelSphere」，瞄准的是模型上线的工程化门槛。

这层市场长期被两端夹着：云厂商的托管服务省事但绑定，Kubernetes 手搓方案灵活但要求团队有 MLOps 能力。开源部署平台想填的是中间那段——「有模型、有场景，但没有专职平台团队」。

评估这类平台的标准其实很单一：能否在不改模型代码的前提下接入现有推理引擎，以及扩缩容、灰度、监控这些生产必需项是否开箱可用。这一层的竞争不在功能列表长度，而在生态适配的广度——支持多少个推理后端，决定了它能被多少团队真正用起来。

> 原文：[InfoQ](https://www.infoq.cn/article/VZPlIIdGRg062mgwJe5y?utm_source=rss&utm_medium=article)

结语：今天这批更新里最稀缺的不是模型权重，而是把 agent 关进笼子的那套基础设施。留一个问题：你更愿意让 agent 跑在自己的 microVM 里，还是跑在别人的插件目录里？