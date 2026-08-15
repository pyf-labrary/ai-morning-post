# DeepSeek 开源 Harness：模型工具全插件化

今天开源圈最值得看的一件事，是 DeepSeek 正式开源了 Harness 框架，把模型、工具和 Agent Loop 全部做成插件。这标志着 Agent 基础设施的竞争从「模型能力」转向「框架生态」——当模型本身趋于同质化，谁能定义 Agent 的执行环境，谁就掌握了下一代开发者的入口。

## DeepSeek 开源 Harness：模型工具全是插件

DeepSeek 正式开源 Harness 框架，这是一套 Agent 执行环境的完整实现，核心设计是「一切皆插件」：模型、工具、Agent Loop 均以插件形式接入，框架本身不绑定任何特定模型或工具链。社区已基于该框架开发出长期记忆模块、电子宠物等玩法，官方同时发布了 awesome-deepseek-agent 资源列表，汇总了生态内的插件和示例。

关键点在于 Harness 把 Agent 运行时的三个核心组件全部抽象成可替换的插件接口，本质上是在建立一个「Agent 的 App Store」。模型插件意味着用户可以在同一框架内切换不同大模型，工具插件让 Agent 的行动能力可以按需组装，Loop 插件则允许开发者替换 agentic 推理循环的逻辑。

为什么重要：此前 Agent 框架的竞争焦点是「如何写好一个 Agent」，DeepSeek Harness 把竞争推到了「如何定义 Agent 的生态标准」层面。开源 + 插件化的组合，使其有机会成为 Agent 开发的事实基础设施。虽然生态尚在早期，但这是 Agent 领域值得关注的架构级信号。

> 原文：[InfoQ - DeepSeek 开源 Harness](https://www.infoq.cn/article/de9AljWc4ejW2KAyW8dD)

## Lightricks 开源 LTX-2 音视频生成模型

Lightricks 发布 LTX-2 的官方 Python 推理和 LoRA 训练包，正式开源音频-视频生成模型。这意味着开发者可以在本地部署并微调该模型，而不必依赖厂商的 API 服务。

关键点是 LTX-2 将音频与视频的生成统一在一个模型框架内，LoRA 训练包的开放降低了定制化成本。此前开源视频生成模型多为单向文本到视频，音视频联合建模且附带训练工具链的开源发布，在这个赛道上并不常见。

为什么重要：视频生成模型的本地部署与微调门槛正在快速下降。LTX-2 的开源发布，让做短视频工具、游戏素材、营销内容生成的小团队有了底模选择，也意味着这一领域的竞争正式从「谁能生成」进入「谁能生成更可控」的阶段。

> 原文：[GitHub - Lightricks/LTX-2](https://github.com/Lightricks/LTX-2)

## Flue 2：给 Agent 引入 React 式 Hooks

Astro 作者打造的 Agent 框架 Flue 2 发布，核心创意是把 React Hooks 的理念引入 Agent harness。开发者可以用 useState、useEffect 这类心智模型来管理 Agent 的状态、生命周期和副作用。

关键点在于它不是在一个新名字里重复「写 prompt + 调工具」的老套路，而是尝试用「声明式 + 响应式」的方式描述 Agent 的行为。Hooks 解决了 React 组件开发中的状态管理难题，Flue 2 想把这个答案迁移到 Agent 开发中。

为什么重要：Agent 开发的体验长期停留在「调用框架 API」的层级，缺乏组件化和复用规范。Flue 2 的思路如果跑通，Agent 开发者可能获得类似 React 生态的组件复用和状态管理能力。由 Astro 作者主导，意味着这个框架在工程实践上有一定说服力。

> 原文：[Latent Space - Flue 2](https://www.latent.space/p/flue-2)

## RAGFlow：开源 RAG 引擎登顶趋势榜

RAGFlow 作为领先的开源 RAG 引擎，融合 Agent 能力为 LLM 提供上下文层，近期登上 GitHub 趋势榜。它不是一个简单的文档检索工具，而是把检索增强生成（RAG）做成了 Agent 的知识底座。

关键点是 RAGFlow 强调了「上下文层」这个概念——LLM 需要的不是更多文档，而是经过整理、与当前任务相关的上下文。它把知识库管理、检索、重排序与 Agent 的决策过程做了集成，让 RAG 不再只是「查资料」，而是 Agent 行为的一部分。

为什么重要：RAG 与 Agent 的结合正在成为开源社区的关注重点。RAGFlow 登顶趋势榜说明，开发者在为 Agent 构建可靠的知识来源时，仍缺少好用的基础设施。RAG 作为 AGI 时代最务实的落地技术之一，其开源生态的活跃度是值得长期观察的指标。

> 原文：[GitHub - infiniflow/ragflow](https://github.com/infiniflow/ragflow)

## Unsloth 本地 UI 支持 Qwen3.8 等新模型

Unsloth 的本地 UI 现可运行和训练 Qwen3.8、Kimi K3、DeepSeek-V4 等最新模型。Unsloth 以高效微调出名，其本地 UI 提供了图形化的模型加载、推理和训练入口。

关键点是 Unsloth 保持了「新模型发布即支持」的节奏，成为观察模型开发生态的一个窗口。Qwen3.8、Kimi K3、DeepSeek-V4 这几个名字出现在同一份支持列表里，说明开源模型生态已进入多强并立的密集发布期。

为什么重要：本地微调工具链对主流新模型的同步覆盖，是开源模型能否真正被采用的前提。Unsloth 的更新频率与覆盖面，直接降低了开发者在本地实验新模型的摩擦成本。它不只是工具更新，也在折射整个开源模型格局的演变速度。

> 原文：[GitHub - unslothai/unsloth](https://github.com/unslothai/unsloth)

## Needle 2：14MB 微型模型跑在手机和机器人上

Needle 2 是一个仅 14MB 的基础模型，面向手机、可穿戴设备、智能家居和机器人等小型设备。模型体积仅为传统大模型的千分之一量级，却能提供基础的自然语言推理能力。

关键点在于「基础模型」的定位——它不是大模型的蒸馏版本，而是为边缘设备原生设计的小型模型。14MB 的参数量意味着它可以直接驻留在设备端运行，无需联网、无需云端算力，天然具备低延迟和隐私保护优势。

为什么重要：当所有人的注意力都在大模型竞赛上时，Needle 2 代表了一条反向路线——把模型做小到可以嵌入任何设备。手机、家电、机器人如果都内置一个小型语言模型，AI 的覆盖场景将从「打开 App」扩展到「环境即接口」。开源意味着这条路线可以被更多硬件厂商直接采用。

> 原文：[GitHub - cactus-compute/needle](https://github.com/cactus-compute/needle)

## 开源技能库让 AI Agent 变身科学家

scientific-agent-skills 提供 161 个经过验证的科学技能和 100+ 科学数据库，被全球 17 万科学家使用。项目定位是给 AI Agent 提供做科学研究的「操作手册」。

关键点是「经过验证」——这些技能不是简单的工作流模板，而是经过真实科研场景验证的操作流程。161 个技能覆盖实验设计、文献分析、数据解读等环节，配套的 100+ 科学数据库让 Agent 在回答问题时可以调用专业数据源。

为什么重要：AI for Science 的口号喊了很多年，但通用 Agent 面对专业科学问题时往往「不知道该怎么操作」。科学技能库把隐性知识显性化，让 Agent 可以按照正规科研方法行动，而不是凭模型记忆自由发挥。17 万科学家的使用量，是这个方向可行性的一个实证。

> 原文：[GitHub - K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

## holaOS：开源一体化 AI Agent 工作区

holaOS 是开源 AI Agent 工作区，可在 100+ 工具集成和共享内存中运行 Claude Code、Codex 等任意 Agent。简单说，它是一个让多个 Agent 在一个统一环境内协作的操作系统层。

关键点是「共享内存」和「任意 Agent」两个设计。共享内存解决了多 Agent 协作时的信息传递问题，不同 Agent 可以共享上下文而不必反复传递 prompt；「任意 Agent」则意味着它不绑定特定厂商，Claude Code、Codex 等都可以在同一环境内共存运行。

为什么重要：Agent 使用者当前最大的摩擦之一，是不同 Agent 工具各自为政，上下文割裂、工具链重复配置。holaOS 想做的事情，是像操作系统统一管理进程和内存一样，统一管理多个 Agent 的生命周期与资源共享。这个方向如果得到社区认可，Agent 工作方式可能从「单工具使用」走向「多 Agent 协同」。

> 原文：[GitHub - holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS)

---

模型层竞争依旧激烈，但 harness 层正成为开源世界的新焦点——当 Agent 的「操作系统」开始标准化，应用层的创新空间或许会比我们想象的更大。