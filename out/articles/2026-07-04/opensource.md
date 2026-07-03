# OpenAI 开源 Codex 插件，Agent 协作时代来了？

今天是 2026 年 7 月 4 日，开源工具板块最值得关注的是 OpenAI 正式发布 Codex Plugin for Claude Code——让两个最火的编码 Agent 工具直接互通。这不是简单的适配，而是 Agent 间互操作走向标准化的信号：当头部玩家开始主动开放接口，工具链的“单打独斗”阶段可能正在过去。

## OpenAI 开源 Codex Plugin for Claude Code

**是什么**：OpenAI 在 GitHub 上开源了 Codex Plugin for Claude Code，允许用户在 Claude Code（Anthropic 的编码 Agent 工具）中直接调用 Codex 进行代码审查、任务委派等操作。插件由 OpenAI 官方维护，类似一个双向桥接器。

**关键点**：这不是用户自己拼装的 hack 方案，而是两家公司（OpenAI 与 Anthropic）在 Agent 生态上的首次官方协作。插件让 Claude Code 能调用 Codex 的代码补全与审查能力，反之亦然——但当前版本更侧重“从 Claude 调用 Codex”。

**为什么重要**：标志 Agent 工具从“各自为政”走向“互操作性”。对于开发者来说，不再被单一 Agent 绑定；对于平台方来说，开源降低了第三方接入门槛。这可能是 Agent 生态标准化协议的开端。

> 原文：[GitHub - openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

## 开源 AI 渗透测试工具 Strix 火爆

**是什么**：Strix 是一个基于 AI 的渗透测试工具，能够自动扫描应用漏洞并提出修复建议。它在 GitHub 上迅速积累关注，成为本周热门项目。

**关键点**：Strix 的核心是“自动化攻击 + 修复建议”闭环。它利用 LLM 理解漏洞上下文，而非简单匹配规则库。目前已支持常见 Web 漏洞和部分 API 安全测试。

**为什么重要**：安全运维的自动化是刚需，但此前 AI 渗透工具多偏向攻击方。Strix 兼顾检测与修复，降低了安全团队的门槛。若能持续维护，可能成为 DevSecOps 的开源标配。

> 原文：[GitHub - usestrix/strix](https://github.com/usestrix/strix)

## Superpowers：可组合的编码 Agent 技能框架

**是什么**：Superpowers 是一套面向编码 Agent 的开发方法论和可复用技能集合。它提供类似“微服务”的模块化设计，让 Agent 开发人员可以像搭积木一样组合技能。

**关键点**：框架定义了一套标准接口，技能（skill）之间通过松散耦合的协议通信。官方示例包括代码审查、文档生成、测试编写等常用 Agent 技能。项目仍处于早期阶段（0.1.x）。

**为什么重要**：当前 Agent 开发重复造轮子严重。Superpowers 试图建立技能复用标准，类似 React Hooks 之于前端。如果社区采纳，可能加速 Agent 开发效率一个数量级。

> 原文：[GitHub - obra/superpowers](https://github.com/obra/superpowers)

## Chrome DevTools 发布 MCP 协议，Agent 可调试网页

**是什么**：Chrome DevTools 团队开源了 MCP（Model Context Protocol）实现，使得 AI 编码 Agent 可以直接控制 Chrome 的调试工具，实现自动化页面调试、DOM 检查和网络分析。

**关键点**：MCP 原本是 Anthropic 提出的协议，用于 Agent 与外部工具交互。Chrome 官方采用意味着该协议获得主流浏览器厂商支持。Agent 现在可以像人类一样操作 DevTools 面板。

**为什么重要**：前端自动化调试一直是 Agent 的盲区——之前 Agent 只能通过 Puppeteer 进行黑盒操作，无法利用 DevTools 的深度诊断信息。MCP 让 Agent 获得和白盒一样的洞察力，尤其适合自动化跨浏览器测试和性能分析。

> 原文：[GitHub - ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

## Google 开源 agents-cli：一键部署 Agent 到云

**是什么**：Google 发布 agents-cli 命令行工具，允许开发者用任何编码助手（如 Cursor、Copilot）创建 AI Agent，并一键部署到 Google Cloud 上。

**关键点**：工具链从“编写代码”到“部署运行”全流程集成，支持评估和版本管理。目标用户是已经使用编码助手生成 Agent 代码的开发者。

**为什么重要**：Google 在 Agent 部署环节抢占入口。相比手动配置云资源，agents-cli 降低了部署门槛，但生态绑定较强（仅支持 Google Cloud）。对于云服务商竞争，Agent 部署的丝滑体验可能成为新卖点。

> 原文：[GitHub - google/agents-cli](https://github.com/google/agents-cli)

## Nous Research 开源 Hermes Agent：强化学习驱动

**是什么**：Hermes Agent 是一个基于强化学习的自改进 Agent 框架。它能通过环境反馈自动优化自身行为，目标是“越用越强”。

**关键点**：核心是 RL 训练 loop，Agent 在执行任务后收到奖惩信号，更新策略。项目开源了训练代码和预训练权重，强调 reproducibility。

**为什么重要**：大部分编码 Agent 目前依赖 prompt engineering 或 fine-tuning 静态提升。Hermes 引入在线学习，让 Agent 能动态适应任务变化。如果RL pipeline 足够轻量，可能开启“Agent 终身学习”范式。

> 原文：[GitHub - NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

## NVIDIA 官方发布 AI Agent 技能库 skills

**是什么**：NVIDIA 在 GitHub 上开源了一组官方验证过的 AI Agent 技能（skills），涵盖图像处理、视频分析、科学计算等 NVIDIA 擅长的领域。

**关键点**：技能库采用标准化接口（类似 Superpowers 的理念），每个技能都附带测试和性能基准。目前首个版本包含 10 个技能，主要面向 GPU 加速场景。

**为什么重要**：NVIDIA 的加入为 Agent 技能标准提供了硬件层面的背书。当技能需要调用 GPU 资源，NVIDIA 的技能库可确保最佳性能。这既是对开源生态的贡献，也是对自家硬件软生态的布局。

> 原文：[GitHub - NVIDIA/skills](https://github.com/NVIDIA/skills)

## Simon Willison 发布 llm-coding-agent 实验版本

**是什么**：知名 Python 开源作者 Simon Willison 发布了 llm-coding-agent 的 0.1a0 版本，一个基于其 llm 工具库的编码 Agent 脚本。

**关键点**：该工具非常轻量，主要是用 LLM 调用和 shell 命令组合实现简单的“阅读代码-生成修改-应用”。目前只是实验性质，文档尚不完整。

**为什么重要**：Simon 的 llm 库在 Python 社区有广泛用户，这个 Agent 实验可能成为“从零开始造一个 Agent”的经典教程。但当前版本成熟度很低，不建议生产使用，但值得关注其后续演进思路。

> 原文：[Simon Willison's blog](https://simonwillison.net/2026/Jul/2/llm-coding-agent/#atom-everything)

---

今天八条 story 几乎都在做同一件事：让 Agent 更好用、更智能、更互联。当巨头们争相开源自己的 Agent 基础设施，下一个值得问的问题是——谁能率先让这些开源组件拼出一个真正可信任的生产级 Agent？