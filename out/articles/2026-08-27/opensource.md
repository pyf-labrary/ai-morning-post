# 智能体基础设施，正在被开源拆开

今天开源圈最值得关注的信号，是 DeepSeek 开源的 Harness。它把 agent 的编排层独立成基础设施，意味着智能体领域开始出现明确的模块化分工。相比某个框架本身，这种“拆开再拼装”的趋势，更值得开发者和投资者留意。

## DeepSeek 开源 Harness，把编排层从智能体里“拎”出来

DeepSeek 发布 Harness，用于构建和编排 AI 智能体。与以往一体化 agent 框架不同，Harness 聚焦于编排层，把任务调度、上下文管理、工具调用等职责独立出来。

关键点在于，这反映了 agentic 基础设施开始向“模块化分工”演进。正如数据库和消息队列成为独立基础设施一样，编排层也开始成为可插拔的组件。对开发者而言，这意味着不必再被某个全栈框架绑死，可以按需组合。

更值得关注的是，DeepSeek 此时开源 Harness 的时机。当主流 agent 框架还在比拼模型能力时，DeepSeek 选择在编排层发力，可能是在押注“下一代应用不再需要关心 agent 如何被组织”。这个判断如果成立，早期一体化框架将面临重塑压力。

> 原文：[InfoQ](https://www.infoq.cn/article/vS7tpsLPdevZhMKdtxei)

## Claude 插件生态上线，官方与社区双市场齐发

Anthropic 发布官方 Claude 插件目录，同时推出社区插件市场，为 Claude Code 和 Cowork 扩展能力。这意味着 Claude 从单一工具向平台化方向迈出关键一步。

官方与社区双市场并存，是这套机制的最大看点。官方目录保证核心质量和安全性，社区市场则提供长尾创新空间。插件生态的繁荣程度，将直接决定 Claude Code 能否成为开发者工作流的默认选择。

对开发者而言，插件市场降低了定制成本，但也要留意新的依赖风险——当你的工作日流程高度依赖某个社区插件时，它的维护状态和安全性就需要纳入筛选标准。

> 原文：[GitHub - anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

## Liquid AI 开源 Pipette，端侧评测告别“玄学”

Liquid AI 开源 Pipette，一个可复现的端侧模型评测套件，能同时测量模型、量化、运行时与硬件四个维度。这套工具解决了设备端模型“性能难预测”的长期痛点。

以前的端侧评测往往只看模型跑分，但实际体验会因硬件差异而大相径庭。Pipette 把量化、运行时和硬件放在同一基准下测量，结果更贴近真实部署。这意味着开发者能在开发早期判断“这颗芯片上跑不跑得动”，而不是等上线后再去填坑。

大模型竞争从云端走向端侧，评测工具的完善程度会是这波效率竞赛的基础设施。

> 原文：[MarkTechPost](https://marktechpost.com/2026/08/25/liquid-ai-open-sources-pipette-a-reproducible-benchmarking-suite-that-measures-on-device-models-quantization-runtime-and-hardware-together/)

## GPT-Image-2 提示词模板库登 GitHub 热榜

awesome-gpt-image-2 收录了 530+ 逆向工程案例和 20+ 工业级模板，把提示词当作代码工程来管理。这个项目登上了 GitHub 热榜，本身就是一个信号。

当文生图进入工业化生产阶段，提示词不再是随手的“灵感”，而是需要版本管理、模式复用和质量控制的资产。这个模板库把散落在各个案例中的技巧结构化、产品化，降低了团队的试错成本。

值得追问的是，当模板越来越标准化，使用者的差异化优势在哪里？工具变好并不是坏事，但依赖模板的团队需要更快建立自己的方法论。

> 原文：[GitHub - freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)

## Apache Maka：给 AI Agent 装上“审计黑匣子”

Apache Maka 是一个本地优先的 AI Agent 工作区，用 append-only 日志记录模型消息、工具调用和权限决策。所有交互记录不可篡改，为 agent 行为提供完整追溯链。

在 agent 自主行动越来越频繁的今天，可审计性是从实验到生产的关键一步。企业不敢放权给 agent，很大程度上不是因为能力不足，而是因为“不可解释”。Maka 的 append-only 设计让每一项决策都有据可查，为治理和合规留出了空间。

它目前处于 Apache 孵化阶段，路线图和社区活跃度还有待观察，但“本地优先 + 全量审计”的思路值得整个行业参考。

> 原文：[GitHub - apache/maka](https://github.com/apache/maka)

## TradingAgents：多智能体上阵炒股，靠谱吗？

TradingAgents 是开源的金融交易框架，由多个 LLM 智能体协作完成选股、分析和交易策略生成，近期登上了 GitHub 趋势榜。

它模拟的是一个投研团队的协作流程：不同智能体负责信息收集、观点碰撞、风险控制和最终决策，而非单模型直接给出买卖建议。这种多头决策机制在理论上有助于降低单点误判的风险。

但金融交易的复杂性远不止于信息分析，它还涉及资金管理、市场流动性和合规约束。开源框架提供了技术基础，但距离“可信赖的交易系统”还有很长一段路。把它当作研究和回测工具，远比直接接上实盘更理性。

> 原文：[GitHub - TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

## Pipecat：实时语音 Agent，等着被“拼”进应用

Pipecat 是一个开源 Python 框架，支持实时语音 agent、多模态应用和实时 AI 交互，由 Daily 和社区共同维护。

在语音交互产品中，开发者最头疼的是音频流处理、打断检测和低延迟响应这些工程问题，而不是模型本身。Pipecat 把这些实时通信能力封装成可复用模块，让开发者可以跳过重复造轮子的环节。

实时语音 agent 正处于“基建先行、应用观望”的窗口期。Pipecat 的生态活跃度，可以作为观察这个赛道热度的参考指标。

> 原文：[GitHub - pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)

今天的开源故事，几乎都在讲“拆开”和“拼装”：把 agent 拆成模块，把能力拼成产品。当工具趋于齐全，留给你的真正壁垒，会是什么？