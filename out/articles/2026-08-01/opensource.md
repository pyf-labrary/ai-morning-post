# qm开源：多Agent协作的新框架

今天最值得看的是 yc-software 开源的 qm——一个让多个 AI Agent 协作完成任务的 harness 框架，目前已在 GitHub 上热度高涨。多 Agent 协作正在从概念走向工程化，编排层的体验将决定 agentic 应用的落地效率。此外，29GB 内存跑 Kimi K3、Grafana 的 Go LLM SDK 等几条动态也各有看点。

## qm：多 Agent 协作的开源 harness

**是什么：** yc-software 今日开源 qm，一个编排多个 AI Agent 协作完成任务的 harness 框架，在 GitHub 上热度高涨。

**关键点：** qm 让多个 Agent 在统一调度下分工，各自承担独立角色，再汇总结果。相比单 Agent 直连模型，这种结构更适合多步骤、需要交叉验证的复杂任务。框架的稳定性与扩展性还有待验证，但工程化方向已经明确。

**为什么重要：** 当基础模型的能力差距在缩小，多 Agent 协作的编排层正在成为新的竞争焦点。qm 这类项目决定了 agentic 应用的开发体验，值得保持关注。

> 原文：[GitHub - yc-software/qm](https://github.com/yc-software/qm)

## waste：29GB 内存跑 Kimi K3

**是什么：** 开源项目 waste 展示了仅用 29GB 内存运行 Kimi K3 模型的可行性，代价是生成速度只有 0.50 token/s。

**关键点：** 0.50 token/s 意味着每生成一个 token 要等 2 秒，距离交互式使用有量级差距。它的价值不在实用，而在验证——大模型在 29GB 内存水位下也能加载运行，只是要接受极慢的速度。

**为什么重要：** 低资源推理是开源社区长期关注的话题。waste 提供了一个极端边界样本，为内存受限场景下的模型部署留下了一个可复现的参考起点。

> 原文：[GitHub - sqliteai/waste](https://github.com/sqliteai/waste)

## SimpleEnglish：让 Agent 写规范技术英语

**是什么：** SimpleEnglish 为 Agent 提供一项专项技能，把文档自动改写为 ASD-STE100 简化技术英语。这是航空航天行业的技术写作标准，对词汇、句式和术语有严格限定。

**关键点：** 这不是通用润色，而是一套行业规范被编码成 Agent 能力。项目以“技能”形式交付，意味着它可以挂载到不同 Agent 工作流中使用。

**为什么重要：** 行业标准驱动的文档处理，是 Agent 离实际业务价值最近的场景之一。航空航天之外，重工、军工等领域也存在类似合规书写需求，这类项目验证了一个可复制的方向。

> 原文：[GitHub - AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish)

## Grafana 发布 Go LLM SDK

**是什么：** Grafana 发布 Go 语言 LLM SDK，并配套一个 React 前端库，用于对接支持流式输出与工具调用（tool calling）的 AI 后端。

**关键点：** Go 生态里高质量的 LLM 客户端封装一直是稀缺资源，多数团队转向 Python 或 TypeScript。Grafana 自身是 Go 的重度用户，这套 SDK 大概率先服务内部需求，再对外开放。

**为什么重要：** 流式与工具调用是 agentic 应用的两项基础能力。有了 Grafana 的工程背书，Go 开发者做 LLM 集成时多了一个值得优先评估的选项。

> 原文：[GitHub - grafana/ai-sdk](https://github.com/grafana/ai-sdk)

## claude-account：Claude Code 账号一键切换

**是什么：** claude-account 是一个开源 CLI 工具，让你在多个 Claude Code 账号之间一键切换，不需要反复登出再登录。

**关键点：** 它解决的是一个非常具体的痛点——一台开发机上工作账号与个人账号并存时的环境隔离问题。CLI 设计让它可以轻松写进脚本，配合 dotfiles 统一管理。

**为什么重要：** 工具虽小，但说明 agentic 开发工具链正在快速成熟。“账号切换”这类基础设施问题开始有人认真解决，本身就是生态繁荣的信号。

> 原文：[GitHub - hamzarehmandeveloper/claude-account](https://github.com/hamzarehmandeveloper/claude-account)

## 预测性 KV 复制：