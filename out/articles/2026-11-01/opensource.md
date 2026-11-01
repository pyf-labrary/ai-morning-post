# 智能体的周边基建，正被开源填满

## 微软开源 TokenEconomizer，编程智能体成本降三成

微软研究院与伯克利开源了一个叫 TokenEconomizer 的插件，思路不是写死压缩规则（截断、摘要、只留最近 N 轮），而是从历史会话中学习「哪些上下文可以丢」，再把学到的策略应用到新会话。在 SWE-Bench 上，它把编程智能体的 token 成本压低了 18.4%–30.9%。

值得注意的地方在于它是个插件，而不是新框架——意味着可以挂在现有 agent 上，不需要重写编排逻辑。为什么重要：编程智能体的成本结构里，上下文反复重发是最大的一块，工具调用本身反而便宜。成本降三成，等价于同样预算下多跑三分之一的活，这是比「提升几个点准确率」更直接的杠杆。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/)

## Vercel Labs 开源 agent-desktop，让智能体操作桌面

agent-desktop 以 Apache-2.0 发布，用 Rust 实现，让智能体在 macOS、Windows、Linux 上操作电脑。关键差异是它读取系统的无障碍树（accessibility tree），而不是截屏再让多模态模型找坐标。

这两种路线一直有分歧：截图派通用、视觉直观，但每步都要传图、会被分辨率与主题变化干扰；结构派省 token、定位精确，但依赖平台的无障碍实现质量。Vercel 选了后者，并且一次性把三平台都做了。为什么重要：computer use 是 agent 落地最贵的一环，现在有了一份跨平台的开源实现，这块能力从「各家自研的护城河」变成了公共品。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use/)

## LangChain 开源 deepagents：开箱即用的智能体骨架

deepagents 提供的是一个「自带电池」的 agent harness（智能体骨架），把工具调用、子智能体（subagent）、文件系统等常见编排模式封装好，开发者不必再从零拼装循环、状态与任务分解。

它的定位不是新框架，而是把已经形成共识的那部分模式沉淀成默认实现——什么该拆给子智能体、中间产物怎么落盘、上下文怎么在层级间传递。为什么重要：harness 层正在从「每家自己写一遍」变成「有一个默认答案」。对 LangChain 来说，这是守住编排层入口的动作；对开发者来说，是少写两千行胶水代码。

> 原文：[GitHub - langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)

## Anthropic 公开 Agent Skills 官方仓库

anthropics/skills 释出了 Claude 的 Agent Skills 实现，包含参考实现与示例集合。Skills 的思路是把「怎么做好某类任务」写成可被智能体按需加载的模块化说明与脚本，而不是塞进系统提示里。

官方仓库的意义不在代码量，而在标准：一套技能如果只有一家支持，它就是提示词工程的花样；如果多家能读同一份技能定义，它才成为可复用的资产。为什么重要：智能体的能力沉淀目前高度碎片化，每个人都在重写同样的「如何做代码审查」「如何写发布说明」。Anthropic 开源参考实现，是在争取这套标准的定义权。

> 原文：[GitHub - anthropics/skills](https://github.com/anthropics/skills)

## claude-mem：给智能体装上跨会话持久记忆

claude-mem 在会话过程中捕获智能体的行为记录，用 AI 做压缩后注入后续会话，让下一次对话能接上上一次的上下文。它兼容 Claude Code、Codex、Gemini 等多个客户端，不绑定单一模型。

这套做法的取舍很清楚：全量留存不现实，纯摘要又会丢细节，所以它选择「用模型压缩模型的历史」。为什么重要：跨会话记忆是目前 agent 工作流最明显的断点——每次开新窗口，之前摸索出的项目约定、踩过的坑全部归零。补上这一环，智能体才从「一次性问答」变成「有工龄的同事」。风险也在这里：压缩即失真，记错比不记更难排查。

> 原文：[GitHub - thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

## Lightpanda：专为 AI 与自动化设计的无头浏览器

Lightpanda 是一个主打轻量、低资源占用的无头浏览器（headless browser），目标场景是智能体抓取与网页自动化，用来替代 Chrome 的 headless 模式。

现有方案的痛点很实际：跑一个 headless Chrome 动辄几百 MB 内存，智能体并发开十几个实例就会把机器压垮，冷启动也慢。专门的浏览器可以把这部分开销降下来，同时只保留抓取与交互需要的能力。为什么重要：agent 的并发能力受限于最重的那个依赖，浏览器往往就是它。谁能把这一层做轻，谁就决定了单机可并行多少个智能体。

> 原文：[GitHub - lightpanda-io/browser](https://github.com/lightpanda-io/browser)

## 1GB Qwen 权重里跑起一台任天堂 NES

开发者 nesformer 用约 1GB 的 Qwen 权重实现了一台可运行的 NES 模拟器，灵感来自此前把计算机「装进」权重的 qwenputer 项目——不写模拟器逻辑，让模型直接承担 CPU 与图形管线的行为。

它当然不是实用方案：真跑游戏，任何免费模拟器都更快更准。有意思的是它作为「能力探针」的价值——模型权重里已经编码了多少关于计算机如何运作的隐式知识，能不能在给定输入输出约束下被逼出来。为什么重要：这类项目是评估模型世界模型的低成本实验，比 benchmark 分数更能说明它到底「懂」什么。

> 原文：[GitHub - dbreunig/nesformer](https://github.com/dbreunig/nesformer)

## superpowers：给编程智能体的开发方法论框架

obra/superpowers 以可组合技能（composable skills）为基础，提供一套面向编程智能体的软件开发流程与规范，涵盖任务如何拆解、何时该写计划、如何验证产出。

它卖的其实不是代码，是纪律：智能体最典型的失败模式不是不会写，而是没想清楚就开始写、写完不验证。把方法论固化成技能，等于给每次会话装上同一套工作习惯。为什么重要：这个方向的出现本身是个信号——agent 开发正在从「调提示词」进入「定工程规范」的阶段，工具之上开始长出流程与共识。

> 原文：[GitHub - obra/superpowers](https://github.com/obra/superpowers)

---

今天这八条里有七条指向同一件事：智能体的周边正在被做成公共品。真正稀缺的，恐怕只剩下你想让它干什么。