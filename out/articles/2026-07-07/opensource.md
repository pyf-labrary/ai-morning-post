# 具身智能基模型开源，Agent 技能生态爆发

大晓机器人今日发布并开源统一具身基模型 ACE-Brain-0.5，登顶 DRACO 榜单，标志着具身智能领域的大模型开始走向开源统一。与此同时，AI 编码 Agent 的技能生态在 GitHub 上快速扩张，几十个新技能仓库涌现，开发者可像安装插件一样复用能力——Agent 开发范式正在被重写。

## 大晓机器人开源统一具身基模型 ACE-Brain-0.5

大晓机器人发布并开源首个统一具身基模型 ACE-Brain-0.5，在多项 DRACO 基准测试中取得第一。该模型融合视觉、语言和动作控制，支持多种机器人形态的零样本迁移。关键点在于：模型权重与训练代码一并开源，降低了研究者和创业公司进入具身智能的门槛。为什么重要？此前具身智能模型多被少数大厂垄断，ACE-Brain-0.5 的开源可能加速机器人通用大脑的普及，并推动行业标准竞争。

> 原文：[大晓机器人开源统一具身基模型 ACE-Brain-0.5，登顶 DRACO 榜单](https://www.leiphone.com/category/ai/YTCPIZ2kIbjtt6CX.html)

## AI 编码 Agent 技能生态爆发，数十个新技能仓库涌现

GitHub 上近期出现大量针对 Claude Code、Codex 等 AI Agent 的技能与插件仓库，涵盖代码审查、营销文案、产品原型等垂直领域。关键点：这些技能以标准化接口封装，可被 Agent 直接调用，形成类似“App Store”的生态系统。为什么重要？技能生态的成熟将让 AI Agent 从通用问答转向专业化任务执行，降低开发者定制成本，并催生新的技能市场。

> 原文：[GitHub - alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

## HuggingFace 发布 LeRobot v0.6.0，强化机器人训练

HuggingFace 推出 LeRobot v0.6.0，新增 Imagine、Evaluate、Improve 三个模块，简化机器人学习从仿真到部署的流程。关键点：Imagine 模块支持自动生成训练数据，Evaluate 提供标准化评测，Improve 支持强化学习迭代。为什么重要？LeRobot 降低了机器人学习工程的复杂度，与 ACE-Brain 形成互补——一个提供模型，一个提供工具链，共同推动具身智能开源生态。

> 原文：[HuggingFace 博客：LeRobot v0.6.0 发布](https://huggingface.co/blog/lerobot-release-v060)

## HuggingFace Kernels 重大更新

HuggingFace 对 Kernels 进行重大更新，提升模型推理与训练性能。关键点：优化了 Flash Attention 实现、内核编译策略，支持更多硬件后端。为什么重要？Kernels 是 Transformer 模型计算效率的底层基石，这次更新直接惠及所有使用 HuggingFace 生态的开发者，尤其对长序列推理场景（如 Agent 长上下文）有显著加速。

> 原文：[HuggingFace 博客：Revamped Kernels](https://huggingface.co/blog/revamped-kernels)

## OfficeCLI：让 AI Agent 直接处理 Office 文件

开源项目 OfficeCLI 提供命令行工具，允许 AI 智能体读取和编辑 Microsoft Office 文档（Word、Excel、PowerPoint）。关键点：基于 Python 编写，支持纯文本接口调用，与 LangChain、AutoGPT 等框架兼容。为什么重要？Office 文档是企业管理中最常见的非结构化数据，OfficeCLI 填补了 Agent 处理这些文件的空白，有望在办公自动化场景中被广泛集成。

> 原文：[GitHub - iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)

## sqlite-utils 4.0rc3 发布

Simon Willison 发布 sqlite-utils 4.0 第三个候选版本，改进大量细节与兼容性。关键点：新增 `--csv` 导出增强、更好的类型检测、修复了多个与 SQLite 3.46+ 的兼容问题。为什么重要？sqlite-utils 是 Python 生态中操作 SQLite 最受欢迎的工具库之一，4.0 稳定版预计很快发布，值得关注其新特性对数据管线的影响。

> 原文：[Simon Willison 博客：sqlite-utils 4.0rc3](https://simonwillison.net/2026/Jul/6/sqlite-utils/#atom-everything)

## HuggingFace 推出语音转语音开源工具

HuggingFace 发布 speech-to-speech 开源库，支持用开源模型构建本地语音智能体。关键点：提供从语音输入到语音输出的完整管线，集成 Whisper、CosyVoice 等模型，支持实时流式处理。为什么重要？语音是 Agent 交互的自然入口，该库使开发者能快速搭建本地、低延迟的语音对话系统，避免依赖云端 API，对隐私敏感场景意义重大。

> 原文：[GitHub - huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech)

## OpenSquilla 0.5.0 Preview 发布，登顶 DRACO 双榜

OpenSquilla 发布预览版 0.5.0，集成多模型并在 DRACO 基准测试中取得双榜第一。关键点：该版本支持视觉、语言、动作多模态融合，并在机器人操作和导航两个榜单上夺冠。为什么重要？OpenSquilla 与 ACE-Brain 同为具身智能基模型，但后者来自国内团队，前者来自海外，两者开源竞争将加速行业迭代。DRACO 双榜冠军表明 OpenSquilla 在特定任务上具有竞争力。

> 原文：[OpenSquilla 0.5.0 Preview 发布，登顶 DRACO 双榜](https://www.qbitai.com/2026/07/443863.html)

---

今天开源工具板块的核心信号是“具身智能基模型开源竞赛”和“Agent 技能生态标准化”。当基模型和技能都可以像积木一样自由组合，下一个问题或许是：谁将成为这个新生态的“应用商店”和“操作系统”？