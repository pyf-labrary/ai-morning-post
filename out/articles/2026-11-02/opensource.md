# DeepSeek 开源 Agent 底座，技能层开始拥挤

## 导语

今天开源板块最值得看的一条，是 DeepSeek 用 MIT 协议放出了 Router-Worker 架构的编程 agent 底座 dsh-superagent，官方自测把 p95 任务完成时间从 29.5 分钟压到 15.7 分钟。比起这个数字，更值得留意的是它开源的位置——不是模型，而是调度层。同一天里，Agent Skills、跨会话记忆、代码知识图谱几个项目同时升温，说明竞争重心正从「谁的模型强」转向「谁的 harness 好用」。底座一旦开源，差异化就只能落在技能、记忆和上下文组织上。

## DeepSeek 开源 Router-Worker 编程 Agent

DeepSeek 以 MIT 协议开源了 dsh-superagent，一个 Router-Worker 结构的编程 agent：由 Router 把 GitHub、飞书这类入口进来的请求拆成多个并行会话，再分发给 Worker 执行。官方给出的自测数据是 p95 任务完成时间从 29.5 分钟降至 15.7 分钟。

关键点有两个。一是架构选择——并行会话拆分本质上把 agent 的并发调度当成基础设施来做，而不是靠单条长上下文硬扛。二是协议，MIT 意味着它可以被直接嵌进商业产品，这对想自建内部 coding agent 的团队是低门槛起点。

需要保留的判断是：这是官方自测，p95 改善有多少来自并行、多少来自 prompt 与工具链调优，外部还缺少复现。但方向清楚——agent 工程的竞争，正在从模型能力转向编排能力。

> 原文：[量子位](https://www.qbitai.com/2026/10/506904.html)

## Agent Skills 成为 GitHub 新风口

anthropics/skills 公开了 Claude 的 Skill 实现，围绕「给编码 agent 装技能」形成一波开源热潮，superpowers、mattpocock/skills、impeccable 等个人与团队仓库同步上涨。

值得注意的是形态：Skill 不是库，也不是插件 API，而是用自然语言加少量脚本描述的「能力包」。它比 MCP server 更轻，比 prompt 模板更结构化，恰好卡在可分发的粒度上。

如果这个形态站住，Skill 会变成 agent 时代的包管理单元——有作者、有版本、有组合，也就必然出现质量分层和供应链问题。现在这批仓库还是草莽期，先看谁能定义约定，而不是谁先堆数量。

> 原文：[anthropics/skills](https://github.com/anthropics/skills)

## claude-mem：把跨会话记忆做成外挂

claude-mem 做的事情很直接：记录 agent 会话内容，用 AI 压缩后回注到后续会话，让 agent 在下次开工时还记得上次干了什么。项目兼容 Claude Code、Codex、Gemini 等多个客户端。

它的存在本身就是一个信号——主流编码 agent 客户端至今没把持久记忆做成一等公民，才留出了插件的位置。压缩再回注的路径成本低、见效快，但失真也是结构性的：压缩阶段丢掉的东西，后面永远找不回来。

短期它是个好用的补丁，长期看，记忆该由客户端还是外挂来管，会是 agent 产品的一个分水岭。

> 原文：[claude-mem](https://github.com/thedotmack/claude-mem)

## Lightpanda：为 agent 重写的无头浏览器

Lightpanda 是一个面向 AI 与自动化场景重写的无头浏览器，主打更低的资源占用和更快的页面操作，而不是兼容完整浏览器生态。

这个选题的合理性在于：agent 做网页任务时，真正的开销常常不在模型调用，而在拉起一个完整 Chromium 的成本和延迟。为自动化裁剪掉渲染、扩展、多媒体这些用不上的部分，是很自然的一步。

风险同样明显——真实网页会惩罚任何「不完整」的浏览器。它能跑通多少长尾站点，决定了它是省钱工具还是玩具。如果你的 agent 要批量抓取或操作页面，值得先拿自己的目标站点做一轮通过率测试。

> 原文：[lightpanda-io/browser](https://github.com/lightpanda-io/browser)

## PR Agent 重回视野，先划清与商业版的界线

PR Agent 在 GitHub 趋势榜回升，项目在介绍里强调自己是「最初的」开源 PR 审查器，并与 Qodo 的商业版本明确划清界限。

这类项目的技术叙事已经不新鲜，真正有意思的是它的定位动作：在一个开源项目被商业公司接手、再分叉的常见剧本里，主动声明血统和边界，是在保住社区信任这块资产。

对使用者的实际提醒是——选这类工具时，看清你装的是哪条线：社区维护版还是商业发行版，更新节奏和 roadmap 归属不同。开源 PR 审查这个赛道的功能趋同已经很明显，剩下的差异主要在治理。

> 原文：[The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent)

## graphify：用确定性 AST 建可查询的代码知识图谱

graphify 把代码库和文档变成可查询的知识图谱，以 Skill 形式接入 Claude Code、Cursor、Codex。技术路线上它做了明确取舍：本地确定性 AST 解析建图，强调每条边都可解释，且不依赖向量库。

这是一条与 RAG 主流相反的路线。向量检索擅长模糊召回，但在代码这种强结构、强关系的语料上，经常给出「看起来相关」却断链的结果。图结构能回答「谁调用了谁、改这里会波及什么」这类问题，且结论可追溯。

代价是建图成本与语言覆盖，以及面对自然语言文档时图能表达多少。值得关注的是它的表态——「不依赖向量库」正在变成一个新的营销坐标。

> 原文：[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

## datasette-llm 0.1a9：为 Datasette Agent 的大改铺路

Simon Willison 发布了 datasette-llm 0.1a9，为 Datasette Agent 的多项较大改动作铺垫。版本号还在 alpha，功能面不算大新闻。

之所以把它列进来，是因为这个组合代表了一种被低估的范式：把 LLM 调用抽象成数据库里可调用的函数，让 agent 直接对结构化数据做 SQL 式的操作，而不是把数据塞进 prompt。

这类「小版本、长路线」的项目通常不会上头条，但它们决定 agent 能不能落到真实的数据栈里。关注 Datasette Agent 接下来的动作，比关注这个 alpha 本身更有价值。

> 原文：[Simon Willison's Weblog](https://simonwillison.net/2026/Oct/31/datasette-llm/)

## 结语

模型在收敛，工程在分叉——今天这七条里，六条都在造底座之上的那一层。留给读者一个问题：你的 agent 栈里，真正留住你的是模型，还是记忆和技能那几层？