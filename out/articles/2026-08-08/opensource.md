# 开源 Agent，正在集体卷基建

今日开源的共同信号：Agent 已经从“模型能力”竞争进入“工程基础设施”竞争。蚂蚁的 Avernet 最值得看——它把多智能体协作做成了可运行的操作系统层，内部 12 大业务任务完成率超 90%，意味着 Agent 协作不再停留在 demo 阶段。

## 蚂蚁开源 Avernet：多智能体协作的“操作系统”

蚂蚁集团今日正式开源 Avernet，定位为多智能体协作基础设施。它不是又一个 Agent 框架，而是试图解决智能体之间的通信、调度与协作问题，在架构层面充当“操作系统”角色。据官方披露，Avernet 已在蚂蚁内部跑通 12 大业务场景，任务完成率超过 90%。

关键点在于“跑通”二字——多智能体系统最大的瓶颈从来不是单点能力，而是多个 Agent 之间的协同效率和可靠性。Avernet 把这一层抽出来做成通用设施，等于给 Agent 生态提供了一套可复用的底层协议。

为什么重要：当头部大厂开始把内部验证过的协作基建开源，多智能体应用的门槛会显著降低，创业团队不必再从零搭一套调度系统。

> 原文：[量子位](https://www.qbitai.com/2026/08/467871.html)

## Cloudflare 开源 computer：给 Agent 一台“云电脑”

Cloudflare 开源了名为 computer 的 AI Agent 工作台，核心是一个虚拟文件系统，让代理在云端操作一台完整的“电脑”。值得注意的是，它的定位面向非开发者友好——不需要深入理解云基础设施，即可让 Agent 完成文件操作、环境搭建等任务。

关键点是这个思路很 Cloudflare：把基础设施能力包装成 Agent 可以操作的“设备”，同时绕开了本地环境的碎片化问题。对非开发者用户来说，这相当于给自己的 AI 助理配了一台永不关机的远程电脑。

为什么重要：Agent 的落地瓶颈之一是没有稳定的计算环境。Cloudflare 提供一个托管式的“电脑”，可能是 Agent 从聊天工具走向生产力工具的关键一步。

> 原文：[GitHub - cloudflare/computer](https://github.com/cloudflare/computer)

## 腾讯云开源 Agent Memory v2.0：团队记忆资产化

腾讯云今日开源 TencentDB Agent Memory v2.0，核心变化是推出四类团队级记忆资产：Chat Memory 沉淀对话上下文，Skill 沉淀可复用能力，LLM-Wiki 沉淀知识文档，Code-Graph 沉淀代码结构关系。

关键点在于“团队级”——这意味着 Agent 的记忆不再是个体会话的私有缓存，而是一个团队可以共享、累积、迭代的结构化资产。四类资产对应团队协作中最重要的信息形态，设计上经过了真实业务场景的提炼。

为什么重要：Agent 的使用瓶颈之一是“每次都要重新教”。团队级记忆基础设施如果能跑通，企业构建 Agent 时就直接站在了团队知识积累之上，而非从零开始。

> 原文：[GitHub - TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)

## 英伟达开源 NOOA：Agent 变成单一 Python 类

英伟达实验室开源 NOOA，一个模型无关的 Python Agent 框架。它的核心设计不复杂：把提示词、工具、回调和流程统一封装为一个 Python 类，让 Agent 的构建方式真正接入了 Python 的面向对象生态。

关键点是模型无关和极简抽象。当前 Agent 框架普遍追求功能丰富，NOOA 反其道而行——用一个类承载 Agent 的完整生命周期，意味着开发者不必学习繁重的框架约定，用原生 Python 心智模型即可构建和复用 Agent。

为什么重要：框架越简单越容易被采用。NOOA 这种“单一类”的设计，如果能配合 Python 生态的天然熟悉度，可能在开发工具链层面打开一条新路。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/08/07/nvidia-ai-releases-nooa-an-object-oriented-python-framework/)

## 微软开源跨语言代码测试生成 Agent

微软在 dotnet/skills 仓库开源 code-testing-generator，一个能自动阅读仓库并跨语言生成单元测试的 Agent。官方数据称任务完成率达到 92.1%，超过了 Copilot。

关键点有两层：一是跨语言，这意味着 Agent 能够理解不同编程语言的语义并生成对应测试，而非简单的模板匹配；二是它被放进 dotnet/skills 仓库而非单独发布，说明微软在把测试生成作为可复用的 Agent 技能来沉淀。

为什么重要：测试是软件工程中人力成本最高的环节之一。如果测试生成 Agent 的完成率真的稳定在 90% 以上，研发流程的效率和保障方式都将被重写。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/08/06/microsoft-open-sources-code-testing-generator/)

## Agent Skills 仓库扎堆开源：工程技能库成热点

今天多个 GitHub 热门仓库把工程最佳实践、科学工作流编码为 AI coding agent 可复用的 skills，包括 awesome-claude-skills、superpowers、scientific-agent-skills 等。

关键点是这一轮“skills 化”正在从个人技巧分享走向体系化积累。仓库不再只是收集单个 prompt，而是把完整的工作流程拆成可组合、可版本管理的技能包，本质上是在为 Agent 建立“职业培训体系”。

为什么重要：当技能库成为基础设施，Agent 的能力上限将不再取决于基础模型，而取决于工程社区积累了多厚的 skills 层。这可能是未来几个月开源生态最值得跟踪的方向之一。

> 原文：[GitHub - ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

## AWS 发布官方 Agent Toolkit：MCP 与 Skills 双轨支持

AWS 开源官方 Agent Toolkit for AWS，提供受支持的 MCP 服务器、技能和插件，帮助 AI 代理在 AWS 上构建和运维应用。与社区项目不同，AWS 强调“受支持”——意味着有官方维护和稳定性承诺。

关键点是云厂商终于下场做 Agent 工具链的标准化。MCP 提供协议层，Skills 提供能力层，插件提供扩展层，三者组合等于 AWS 为 Agent 构建了一个完整的云上操作入口。

为什么重要：AWS 是云计算事实标准之一，它的 Agent Toolkit 会直接影响大量企业开发者的工具选型。官方支持意味着企业可以放心把 Agent 接入生产环境。

> 原文：[GitHub - aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws)

## LangChain 开源 Open-SWE：异步编码 Agent 走向生产

LangChain 发布开源异步编码智能体 Open-SWE，面向长时间运行与高并发任务设计。在当前多数编码 Agent 仍是同步短任务执行的背景下，异步化直接指向生产环境中的真实场景。

关键点是 LangChain 对自己的定位正在从框架层走向应用层。Open-SWE 不只是一个 demo，而是一个提供开放方案的编码 Agent——配合异步架构，它可以同时处理多个仓库的编码任务而不互相阻塞。

为什么重要：编码 Agent 从“单任务辅助”走向“并发常态运行”，是 Agent 规模化采用的前置条件。Open-SWE 如果能在长时间任务稳定性上做出标杆，会推动行业整体向异步架构迁移。

> 原文：[GitHub - langchain-ai/open-swe](https://github.com/langchain-ai/open-swe)

---

一天的密集开源背后，是一个清晰的信号：Agent 的竞争力正在从模型层转移到工具、记忆和协作基础设施层。接下来值得追问的是——这些各自为阵的基建，会走向统一标准，还是继续在碎片化中竞争？