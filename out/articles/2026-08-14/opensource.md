# 开源 Woxi：Rust 重写 Wolfram 语言，图什么？

今天最值得看的是 Woxi：一款用 Rust 重新实现 Wolfram 语言的开源解释器，自带兼容 GUI 与多语言绑定。它的意义不只是“又一个解释器”，而是给长期被商业授权和闭源生态绑定的 Wolfram 语言，开了一条开放与可嵌入的岔路。另外两个项目分别补位 AI Agent 持久记忆和终端 AI 编程，也都是“轻量、本地优先”的思路。以下逐一拆解。

## Woxi：Rust 重写 Wolfram 语言，兼容 GUI + 多语言绑定

是什么：Woxi 是一个以 Rust 重新实现 Wolfram 语言的开源解释器，项目主页宣称提供兼容 GUI 与多语言绑定。

关键点：Rust 实现让它在内存安全和性能上有天然优势；多语言绑定则方便其他技术栈直接调用 Wolfram 语言逻辑。对依赖符号计算和数学表达式的开发者来说，这是一个脱离商业闭源环境的潜在选项。

为什么重要：Wolfram 语言长期由 Wolfram Research 一家掌控，Woxi 诞生于开源社区，等于把这类计算能力开放到 Rust 生态。虽然目前成熟度未知，但对做科学计算、教育工具或想内嵌公式引擎的团队，这是一个值得盯住的方向。

> 原文：[Woxi](https://woxi.ad-si.com)

## MCP Memory：给 AI Agent 装上持久记忆

是什么：MCP Memory 是一个面向 MCP（Model Context Protocol）架构的开源项目，结合 Google OKF 与 SQLite FTS5，为 Agent 提供本地持久记忆和快速全文检索。

关键点：AI Agent 的记忆一直是落地短板，而这个项目把记忆做成可插拔组件：本地存储、SQLite FTS5 做索引，速度快且无需额外基础设施。Google OKF 的具体协作方式需要看代码，但方向很明确——本地、轻量、可控。

为什么重要：Agent 能不能从“一次问答”进化为“长期协作”，记忆是关键。MCP Memory 降低了开发者自建记忆模块的成本，属于基础设施型项目。对投资人和技术决策者来说，这类组件会逐步撑起 Agent 应用层真正的复杂场景。

> 原文：[MCP Memory GitHub](https://github.com/fellowgeek/mcp-memory)

## Hax：C 语言写的极简终端 AI 编程 agent

是什么：Hax 是一个用 C 语言实现的开源终端 AI 编程 agent，主打极简、原生终端工作流。

关键点：当主流 AI 编程工具都在卷 IDE 插件和复杂 GUI 时，Hax 选择回到终端，依赖极少、启动快，符合 Unix 哲学。C 语言实现意味着对系统有更强掌控，也更容易被开发者读透和修改。

为什么重要：不是所有人都需要千篇一律的图形界面。Hax 代表一种“Agent 也可像终端工具一样内嵌在 workflow 里”的路线。对开发者它是可学习的参考实现，对产品经理则提示：AI 编程产品的形态不该只有 VS Code 一种答案。

> 原文：[Hax](https://usehax.dev/)

今天三个项目都在用更开放或更底层的方式，挑战主流形态。你会把 Woxi 或 Hax 放进自己的工具箱吗？