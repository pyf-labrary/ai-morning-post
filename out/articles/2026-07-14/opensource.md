# OpenManus登场，Agent安全工具井喷

**导语**：FoundationAgents 开源通用 Agent 框架 OpenManus，致敬 Manus 并支持多智能体协作，今天成为 GitHub 日榜热门。与此同时，围绕 AI 编码 Agent 的安全防护工具密集涌现——从阻断危险命令到一次性虚拟机隔离，开源社区正在快速补齐 Agent 落地的最后一块拼图。

## OpenManus：开源通用 Agent 框架，致敬 Manus

FoundationAgents 团队开源了 OpenManus——一个无堡垒、纯开放的多智能体协作框架，旨在降低复杂 Agent 应用的构建门槛。它在设计上受 Manus 启发，但完全用可审计的开源代码实现。关键点在于支持动态角色分配和任务分解，开发者可以通过配置文件快速编排多个 Agent 协同完成工作流。为什么重要：这是当前少数几个同时具备“通用性”和“完全透明”的 Agent 框架之一，适合需要自定义协作逻辑的团队，也是研究多 Agent 系统的宝贵参考实现。

> 原文：https://github.com/FoundationAgents/OpenManus

## Claude Cookbooks：官方配方合集，快速上手 Claude

Anthropic 发布了 Claude Cookbooks 开源仓库，包含大量 Jupyter Notebook 和代码示例，覆盖函数调用、工具使用、提示链等场景。关键点：每个 Notebook 都针对一个具体任务（如“用 Claude 分析 PDF 并生成摘要”），附有可直接运行的代码和解释。为什么重要：这是 Anthropic 官方直出的最佳实践库，对于希望迁移到 Claude 的开发者来説，比社区教程更权威、更完整，尤其适合快速验证产品原型。

> 原文：https://github.com/anthropics/claude-cookbooks

## Hallmark：给编码 Agent 的“反 AI 味”设计风格

Nutlope 开源的 Hallmark 是一个专为编码 Agent（如 Claude Code、Cursor）定制的设计 skill，核心主张是生成“不像 AI 写出来的”界面。关键点：它内置了完整的 CSS 排版、配色和交互模式，强调人类设计师的审美直觉，而非大模型默认的模板化输出。为什么重要：随着 AI 生成代码进入产品交付环节，“AI 味”正在成为用户体验的槽点。Hallmark 提供了一条低成本解决路径——让 Agent 在输出时自动套用一套质量更高的视觉规范。

> 原文：https://github.com/Nutlope/hallmark

## awesome-llm-apps：100+ 可运行 AI Agent 和 RAG 应用合集

Shubhamsaboo 维护的 awesome-llm-apps 仓库聚合了超过 100 个可直接克隆运行的 AI Agent 和 RAG 应用，覆盖问答、文档检索、自动化工作流等场景。关键点：每个应用都附带完整的代码和配置，通常只需设置 API Key 即可启动。为什么重要：这是目前覆盖面最广的“即用型”Agent 应用池，适合产品经理快速验证 idea 或开发者做竞品参考，省去从零搭建的重复劳动。

> 原文：https://github.com/Shubhamsaboo/awesome-llm-apps

## Destructive Command Guard：阻断 Agent 危险 shell 命令的开源防护

Dicklesworthstone 开发的 Destructive Command Guard 是一个轻量级防护工具，可以拦截 AI 编码 Agent 对危险 git 和 shell 命令的执行。关键点：它通过监听终端输出来检测“git push –force”“rm -rf /”等高风险操作，并在执行前弹出确认提示。为什么重要：GitHub 上已有多个因 Agent 误操作导致仓库损坏的案例，这类防护工具填补了 Agent 权限管理的外部监控空白，适合在开发环境中作为“最后一道防线”。

> 原文：https://github.com/Dicklesworthstone/destructive_command_guard

## 蚂蚁安全开源两大框架，填补 Claude Code 攻击面

蚂蚁安全团队开源了两个安全框架，专门针对 Claude Code 等编码 Agent 的潜在漏洞提供防护。关键点：两个框架分别聚焦“输入注入防御”和“输出安全过滤”，覆盖 Agent 在读取代码、执行命令过程中的常见攻击面。为什么重要：编码 Agent 的安全问题远不止命令执行——它在处理用户代码时可能引入恶意注入，而现有安全工具多关注运行时而非输入阶段。蚂蚁的框架是对这一空白的系统性补全。

> 原文：https://www.qbitai.com/2026/07/448925.html

## Microsoft TRELLIS.2：原生紧凑结构隐空间 3D 生成

微软开源 TRELLIS.2，一种基于结构化隐空间的 3D 生成框架。关键点：它直接用紧凑的三角网格作为隐空间输出，无需 post-processing 即可得到高质量 3D 模型，且显存占用比前代降低 40%。为什么重要：3D 生成一直是 AI 落地的难点，TRELLIS.2 在效率和品质上的提升，可能让实时 3D 内容生成从实验室走向游戏、XR 等实际应用。

> 原文：https://github.com/microsoft/TRELLIS.2

## Clawk：给编码 Agent 提供一次性 Linux 虚拟机，安全隔离

Clawk 是一个轻量工具，可以让 AI 编码 Agent 在 disposable Linux VM 中运行，执行完后自动销毁环境。关键点：它基于 KVM 实现，Agent 的每次操作都在一个干净环境中执行，不会污染宿主机文件系统或网络。为什么重要：相比沙盒或权限过滤，一次性虚拟机提供了最高级别的隔离，适合在不可信 Agent（如开源社区贡献的 Agent 插件）上使用，也能防止 Agent 残留敏感数据。

> 原文：https://github.com/clawkwork/clawk

---

**结语**：Agent 框架开始走向通用与透明，而安全工具链的快速成熟意味着行业正从“能不能用”转向“敢不敢用”。你更担心 Agent 的能力上限，还是它的失控下限？