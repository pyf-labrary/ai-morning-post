# Google 开源 agent 编排层，底座战开打

## 导语

今天开源板块最值得看的一件事，是 Google 把内部的 agentic 编排运行时以 ax 之名放了出来——它管的是多智能体与工具链路的统一调度，而不是又一个模型。其余 7 条几乎都在同一方向上补位：让 agent 能操作软件（CLI-Anything、Univer）、能记住代码（codebase-memory-mcp）、能被装进行业流程（Anthropic 金融参考 agent）。把这 8 条放在一起看，竞争焦点已经明显从模型层下移到了运行时与工具层。

## Google 开源 agentic 编排运行时 ax

Google 将内部使用的 agentic 编排运行时开源，项目名为 ax，核心职责是统一调度多智能体与工具调用链路。这不是一个 agent 框架的「Hello World」示例，而是运行时（runtime）层面的东西——负责谁在什么时候调用哪个工具、多个 agent 之间怎么交接。

**为什么重要**：编排层是 agent 从 demo 走向生产之间那段最难走的路。模型能力可以买 API，但调度、重试、状态管理、工具权限这些工程问题得自己扛。Google 把它开源，等于把竞争轴线从「谁的模型更聪明」拉到「谁的运行时更可靠」。参考 Kubernetes 的路径，谁定义了编排的事实标准，谁就握住了上层生态的入口。

> 原文：[GitHub - google/ax](https://github.com/google/ax)

## Anthropic 开源金融服务参考 agent

Anthropic 放出一套面向金融行业的参考 agent，覆盖投行、股票研究、私募与财富管理四类场景，同时提供配套的 skills 与数据连接器。所谓「参考」意味着它不是产品，而是可被抄的作业：把 Claude 在金融工作流里该怎么接数据、怎么拆任务、怎么约束输出，直接示范出来。

**为什么重要**：垂直行业的 agent 落地，难点从来不在模型，而在数据接入与合规边界。Anthropic 选择用开源模板替代销售讲解，是把「行业 know-how」产品化的标准打法。对做金融科技的人来说，这套代码的价值不在能直接上线，而在于它给出了一个可被审计的流程骨架。

> 原文：[GitHub - anthropics/financial-services](https://github.com/anthropics/financial-services)

## 清华联合无问芯穹开源具身智能平台 RLark

清华与无问芯穹联合开源具身智能平台 RLark，官方口径是 5 分钟完成机器人纳管、10 秒启动跨集群任务，把训练与调度做成云原生架构。「纳管」和「跨集群任务」这两个词是关键——它解决的是把异构机器人接进统一调度体系的问题，而不是某个具体模型的训练效果。

**为什么重要**：具身智能目前的瓶颈有相当一部分在工程侧。每换一款机器人就要重写一遍接入层，训练任务又要跟推理任务抢资源，这类脏活此前很少被开源项目正面处理。RLark 如果真能把接入时间压到几分钟级别，降低的是整个领域的实验门槛。数字为官方说法，实际效果需要自己验证。

> 原文：[量子位 - RLark 报道](https://www.qbitai.com/2026/09/496767.html)

## Univer：给 agent 用的 Office 运行时

Univer 把表格、文档、幻灯片、画布、关系表与 PDF 收进同一个运行时，定位从「开源在线表格」调整为「AI agent 的办公操作底座」。这个转向值得注意：它面向的调用者不再是人类用户，而是需要可编程文档对象的 agent。

**为什么重要**：agent 要进办公室，缺的不是理解能力，而是能改的东西。主流 Office 套件的对象模型封闭、API 覆盖不全，agent 想「把第三季度数据填进这张表并调整格式」很容易卡在权限和接口上。一个开源、结构统一、可被直接操纵的文档运行时，恰好是这类任务缺失的那一层。真正的考验在于格式兼容与协作体验，不在功能清单长度。

> 原文：[GitHub - dream-num/univer](https://github.com/dream-num/univer)

## superpowers：给编码 agent 的方法论

superpowers 用一组可组合的 skills，为编码 agent 定义了一套完整的软件开发方法论——从需求理解到实现到验证，每个环节都对应一个可插拔的技能单元。它卖的不是工具，而是流程。

**为什么重要**：agent 技能框架正处于井喷期，多数项目的差异只在封装壳上。superpowers 的赌注是「方法论比工具更稀缺」：同一个模型，配上不同的流程约束，产出质量可以差出量级。这也是当前 agent 工程的一个真问题——能力已经过剩，缺的是让能力稳定复现的纪律。

> 原文：[GitHub - obra/superpowers](https://github.com/obra/superpowers)

## strands-agents 开源 agent harness SDK

strands-agents 发布 agent harness SDK，同时提供 Python 与 TypeScript 版本，主打端到端掌控 harness，并支持任意模型、任意云。harness 指的是包裹模型的执行框架——负责循环、工具注入、上下文管理与停止条件。

**为什么重要**：企业对模型锁定和云锁定的敏感度正在上升，把 harness 单独抽出来做成可替换的一层，是对这种焦虑的直接回应。对技术团队而言，这意味着可以保留自己的编排逻辑，同时随时换掉底下的模型供应商。SDK 能否胜出不取决于功能多少，而取决于迁移成本够不够低。

> 原文：[GitHub - strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)

## 港大 CLI-Anything：让软件「agent 原生」

HKUDS 的 CLI-Anything 试图把任意命令行软件包装成 agent 可直接调用的能力，路线是绕开逐个软件写专用适配，直接复用 CLI 这个最通用的接口层。目标很直白：让所有软件都能被 agent 操作。

**为什么重要**：给每个软件写 MCP server 是线性成本，而 CLI 是几十年来沉淀下来的统一抽象。这条路径的优势是覆盖面，风险也明显——命令行的输出非结构化、错误信息不友好、权限边界模糊，包装层要处理的脏数据比想象中多。它能否成立，取决于包装质量能否稳定到可以无人值守。

> 原文：[GitHub - HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

## codebase-memory-mcp：把代码库索引成知识图谱

codebase-memory-mcp 是一个 MCP 服务，把代码库索引成持久化的知识图谱，官方称支持 158 种语言、亚毫秒级查询，并可减少约 99% 的 token 消耗。后一个数字来自项目自述，属于典型的营销口径，需要按自己仓库实测。

**为什么重要**：上下文成本是编码 agent 当前最实在的支出项，每次对话重新读一遍代码库既不经济也不稳定。「索引一次、查询多次」本质是把 RAG 的思路用在代码结构上，而且图谱比向量检索更适合表达调用关系这类结构化知识。如果延迟真能压到亚毫秒，它对 agent 交互形态的影响会大于省下的 token 钱。

> 原文：[GitHub - DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

## 结语

今天这 8 个项目没有一个是新模型，全都在抢 agent 的基础设施位置。

值得留给自己的问题是：当编排、技能、记忆三层都已被开源填满，模型厂商的护城河还剩下多宽？