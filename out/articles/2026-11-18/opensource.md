# Agent 的脚手架，正被开源补齐

今天这 8 条里有 5 条在给 agent 造零件：技能库、技能评测、交互协议、调试接口、执行沙箱。但最值得看的还是英伟达——它把托管 Kubernetes 的引擎开源了，等于告诉所有在建 AI 工厂的人：控制面你可以自己拿。这个动作的指向不在开发者，在云厂商对 GPU 集群的定价权。另一条线是 Chrome 团队把 DevTools 做成了 MCP server，编码智能体终于能看见运行时了。

## 英伟达把托管 K8s 开源了

英伟达以 Apache 2.0 开源了 NVKE（Kubernetes Engine）与 NVKR（Recipes），目标是让 AI 工厂在自有裸金属 GPU 服务器上跑起托管 Kubernetes，两者均已进入公开预览。

关键点在于「托管」二字的价值被拆开了。托管 Kubernetes 原本卖的是替你管控制面，现在控制面可以自持，且是面向 GPU 集群而非通用集群调过的。对已有裸金属 GPU 的团队，这是把编排层从采购项变成安装项。

为什么重要：卖 GPU 的公司顺手把编排层开源，压缩的是云厂商在 GPU 实例上的溢价空间。这不是一个开发者工具的发布，是基础设施商业模式的一次表态——硬件厂商希望上层越薄越好。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/17/nvidia-nvke-nvkr-managed-kubernetes-gpu/)

## 材料科学的 agent 有了工作台

MatOS 正式开源，能自动筛选材料、寻找配方、开发新模型。据发布信息，材料研发任务的成功率有明显提升。

材料研发是典型的长周期、高试错成本领域，agent 在这里的价值不是「生成」，而是缩小搜索空间——把候选配方从几千个压到几十个，剩下的交给实验台。这类任务的 ROI 比通用聊天助手好算得多。

为什么重要：科学发现是 agent 目前少数能算清账的场景，而开源意味着中小实验室不必自建平台。往后看，垂直领域的 agent 平台会先从「实验成本高、数据可结构化」的学科里长出来。

> 原文：[量子位](https://www.qbitai.com/2026/11/510652.html)

## 让 agent 自己开浏览器调试

Chrome 团队开源了 chrome-devtools-mcp，基于 MCP（Model Context Protocol），让 Claude Code、Cursor 等编码智能体直接调用 DevTools 的能力做调试。

过去编码 agent 改代码主要靠读文件和跑测试，看不到运行时——网络请求失败、控制台报错、DOM 结构变化，它都拿不到。接上 DevTools 之后，这些信号进入 agent 的观察范围。

为什么重要：调试是编码 agent 从「能写」跨到「能修」的分水岭。更值得注意的信号是浏览器厂商亲自下场写 MCP server，说明 agent 接口正在变成浏览器的一等公民，而不只是外部工具的逆向适配。

> 原文：[GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

## 阿里给代码审查加了确定性底座

阿里开源 open-code-review，采用混合架构：确定性子流程叠加 LLM Agent，支持行级精确评论，内置 NPE、线程安全、XSS、SQL 注入等规则集。

纯 LLM 做代码审查的老问题是漏报和误报都不可控，同一个 PR 跑两次结论可能不同。把可判定的部分交还给流水线，让 LLM 只处理语义层的问题，等于把「稳定」和「灵活」分到两层去解决。

为什么重要：这个分层思路比工具本身更值得抄。任何想把 LLM 塞进既有工程流程的团队，都会遇到同一个问题——哪些环节必须确定性，哪些环节才轮到模型。

> 原文：[GitHub](https://github.com/alibaba/open-code-review)

## 技能库开始跨 agent 通用

google-labs-code 发布 stitch-skills，是面向 Stitch MCP 服务器的 Agent Skills 库，遵循 Agent Skills 开放标准，兼容 Antigravity、Gemini CLI、Claude Code 与 Cursor。

一次编写、多个 agent 宿主可用，是这条最实际的部分。此前的「技能」大多绑死在某个工具上，换个客户端就得重写，本质上只是提示词的别名。

为什么重要：只有跨宿主兼容，技能才会变成可复用资产而不是配置项。另一个细节是 Google 这次推的是标准而非产品——在 agent 工具链上，先定义格式的一方通常拿走生态位。

> 原文：[GitHub](https://github.com/google-labs-code/stitch-skills)

## 给 agent 技能打分

NVIDIA 开源 SkillEvaluator，用质量门禁、语义重叠检测、合成评测集与实机评测，量化技能与插件如何改变智能体的行为。

它要解决的是一个很具体的困境：装了一堆技能，但没人知道哪个真的起了作用，哪个只是增加了上下文负担。语义重叠检测尤其实用——多个技能覆盖同一意图时，模型的行为会变得不可预测。

为什么重要：技能生态要成立，度量得先到位。否则技能库会重演依赖地狱：装得越多，系统越脆弱，而没有人能说清是哪一层出的问题。

> 原文：[GitHub](https://github.com/NVIDIA/SkillEvaluator)

## agent 与前端的协议层

ag-ui 定义了一层 agent 与用户交互的协议，让前端应用以统一方式接入智能体，最近登上 GitHub Trending。

现在每个做 agent 产品的团队都在自己写同一批胶水代码：流式输出的渲染、工具调用状态的展示、中断与重试的处理。这些逻辑跟业务无关，却占了大量工期。协议层收敛之后，前端不必知道后端跑的是哪个模型、哪个框架。

为什么重要：这是 agent 应用从 demo 走向产品的必经一步。演示阶段拼的是模型效果，产品阶段拼的是这些没人愿意写第二遍的中间层。

> 原文：[GitHub](https://github.com/ag-ui-protocol/ag-ui)

## 沙箱是 agent 的必需品

Simon Willison 撰文梳理了为编码智能体执行代码构建外部沙箱的几种新思路，核心是在隔离强度与可用性之间做权衡。

隔离越强，agent 能做的事越少、启动越慢；隔离越弱，一次误操作的爆炸半径就越大。文章的价值在于把这个连续谱摆出来，而不是给一个标准答案。

为什么重要：agent 一旦获得执行代码的能力，风险性质就变了——从「输出错误答案」变成「删掉不该删的东西」。沙箱不是安全团队的选修课，而应该写进产品设计的默认项。

> 原文：[Simon Willison's Weblog](https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/)

技能、评测、协议、沙箱在这一周同时有了开源实现，说明 agent 的工程问题已经进入了「被工具化」的阶段。接下来真正稀缺的不是能力，而是你敢把哪些权限交出去。