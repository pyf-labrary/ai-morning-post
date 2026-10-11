# 办公 Agent 有了自己的账号

谷歌今天发布的办公 Agent，最值得注意的不是它能干什么，而是它的身份设定：独立账号、可以创建子 Agent、甚至能调用 Claude 等其他模型。这等于把 Agent 从"对话框里的工具"重新定义为"通讯录里的成员"——有身份、有权限、有汇报关系。当 Agent 能互相派活，办公自动化的瓶颈就从模型能力转向组织设计与权限治理。

## 谷歌办公 Agent：@ 一下就能派活

谷歌发布办公场景 Agent，给它配了独立账号，支持创建子 Agent，并且能调用 Claude 等其他厂商的模型。

关键点在三处：独立账号意味着它有明确身份与权限边界，可以进入协作工具、被同事 @ 派活；子 Agent 意味着任务可被拆解并向下分发；跨模型调用则说明这套东西不打算绑定 Gemini。

为什么重要：过去的 Agent 是"你打开它、你使用它"，现在是"它在群里、你指派它"。这会让权限模型、操作审计、成本归属这些此前属于 IT 管理范畴的问题，第一次成为产品设计问题。评估标准也随之变化——单轮回答质量不再关键，任务编排与失败恢复才是。

> 原文：[InfoQ](https://www.infoq.cn/article/490gIS9Bk0NmylN7GIt1?utm_source=rss&utm_medium=article)

## Anthropic 发布免费开源安全扫描器

Anthropic 推出一款面向开源项目的免费 AI 安全扫描工具，帮助维护者自动发现代码漏洞与供应链风险。

关键点有两个：一是免费，二是瞄准开源维护者这一特定人群。开源项目的使用量与维护者投入长期严重倒挂，安全审计往往是"知道该做但没人力做"的环节。

为什么重要：把安全扫描的成本压到接近零，实际是在给整个开源供应链补一层基础设施。对 Anthropic 而言，这也是一次位置卡位——从模型供应商向开发者工具链上游延伸，比单纯比拼模型分数更能形成黏性。

> 原文：[The Decoder](https://the-decoder.com/anthropic-launches-a-free-ai-scanner-for-open-source-projects/)

## CLAUDE.md 之后，配置文件也不用写了

围绕 CLAUDE.md 与 AGENTS.md 的路线之争，Anthropic 给出了自己的答案：未来不需要手写这类配置文件，Agent 的上下文管理将走向自动化。

关键点在于对"配置文件"性质的重新判断。CLAUDE.md、AGENTS.md 本质是人肉上下文工程——把项目约定、命令、禁忌写成文本喂给模型，属于过渡期产物。

为什么重要：如果上下文能由 Agent 自行推断与维护，工程实践的着力点会整体位移。团队该优化的不再是"文档写得多齐整"，而是仓库结构是否可被自动发现、工具接口是否清晰、约束是否能被机器验证。配文件只是症状，可被机器理解的项目结构才是解药。

> 原文：[InfoQ](https://www.infoq.cn/article/MAo3KoDWm9FGIcKau9AK?utm_source=rss&utm_medium=article)

## 住在短信里的 AI Agent 盘点

TechCrunch 汇总了当前值得关注的短信形态 AI Agent，覆盖通用助手，以及面向家庭、差旅和工作场景的专用代理。

关键点：短信（SMS）意味着零安装、零学习成本的分发渠道——用户不需要下载 App、不需要新建账号，Agent 直接进入已有通讯录。

为什么重要：这是"渠道即产品"这个老命题在 Agent 时代的重演。对话式交互抹平了 UI 差异，让分发渠道重新成为竞争核心；代价则是富媒体能力弱、会话缺乏结构，复杂任务很难只靠短信完成。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/10/all-the-ai-agents-that-can-live-in-your-text-messages/)

## 10 秒视频很惊艳，AI 拍短剧为何还是难

文章拆解了 AI 视频生成在短剧场景的落地困境：单镜头质量已经可用，但跨镜头一致性、叙事结构与制作流程仍撑不起一部完整剧集。

关键点在于能力断层的位置。生成一段 10 秒画面，和讲一个有角色、有场景延续性的故事，是两类不同难度的问题。角色外貌、服装、光线、空间关系在镜头之间保持一致，目前仍需大量人工干预。

为什么重要：这提醒我们，视频模型的评测指标（画质、时长、物理合理性）与内容生产的真实需求（一致性、可控编辑、可返工）之间存在系统性偏差。谁能解决"可编辑的一致性"，谁才真正进入影视工业。

> 原文：[InfoQ](https://www.infoq.cn/article/8g9tlaqJFUPrb4oGO00A?utm_source=rss&utm_medium=article)

## 金融监管落地 Harness：让 Agent 稳定跑起来

一篇实践分享介绍了金融监管场景下的 Harness 架构，通过知识与数据双驱动，让 Agent 在高合规要求环境中稳定运行。

关键点："Harness"指围绕模型构建的外围工程——约束、检索、校验、评测、回滚。金融监管对可追溯、可复现的要求极高，单靠模型自身的不确定性输出无法满足，必须把模型包进确定性流程里。

为什么重要：这才是 to B 落地的真实形态。价值不在模型本身，而在把模型嵌入受控流程的工程能力。对于做企业级 Agent 的团队，值得直接对照的是：你的 Harness 里，知识、数据、校验、审计这四层分别由谁负责。

> 原文：[InfoQ](https://www.infoq.cn/article/SuqGY4FQ95AVzs1S0KSV?utm_source=rss&utm_medium=article)

## Product Hunt 新品：科研 Agent、纯离线手机 AI

本周 Product Hunt 值得关注的 AI 产品有三款：面向科学智能体的搜索引擎 Lune、iPhone/Android 上的纯离线私有 AI 应用 KernelAI，以及从统一收件箱接管 Claude Code 与 Codex 的 AgentDock。

三个产品恰好指向三个方向：垂直研究检索、端侧隐私、多 Agent 调度。其中端侧纯离线最值得留意——它服务的是一批云端模型结构上无法覆盖的场景，隐私敏感、网络受限或数据不允许出境的用户。

为什么重要：AgentDock 类产品的出现，说明开发者同时使用多个编码 Agent 已成常态，"统一入口 + 任务分派"开始成为独立产品品类。这与谷歌办公 Agent 的思路同源：Agent 多了之后，编排层本身就是机会。

> 原文：[Product Hunt](https://www.producthunt.com/products/lune-research)

## 结语

当 Agent 有了账号、能互相派活，"这件事谁负责"第一次变得不那么显而易见。你的组织架构图里，准备把 Agent 画进去了吗？