# Cloudflare 推 OS，Agent 生态开战

今天最值得看的，是 Cloudflare 发布面向 Agents 的开放平台 Cloudflare OS。当模型层竞争趋于同质，运行环境正在成为 agent 时代的新入口。Cloudflare 这一步，把网络基础设施的优势延伸到了 agent 生态，也把平台之战拉到了新高度。

## Cloudflare OS：Agent 时代的运行层卡位

Cloudflare 发布 Cloudflare OS，定位为面向 Agents、应用和工作的开放平台，目标是把 AI 代理纳入其基础设施版图。

关键点在于，它不是模型，也不是应用，而是 agent 的运行环境。Agent 需要长期记忆、上下文管理、权限控制、工具调用，这些比「调用一次 API」复杂得多。Cloudflare 把自己最擅长的网络分发和边缘计算，升级为 agent 的运行时底座。

为什么重要：当模型能力趋同，agent 的竞争焦点转向运行层——谁能提供稳定、安全、低成本的执行环境，谁就掌握分发入口。Cloudflare 凭借全球节点和开发者生态，把 agent 拉进自己熟悉的阵地。这对云厂商和 agent 平台都是新的变量。

> 原文：[Cloudflare OS 发布公告](https://blog.cloudflare.com/cloudflare-os/)

## Prime Agent：让 Agent 学会自我改进

Prime Intellect 发布 Prime Agent，一个自我改进的强化学习 Agent，尝试让模型通过自主训练持续优化自身行为。

关键点在于，传统 Agent 使用固定权重，Prime Agent 把强化学习循环内置到运行过程里，它能基于任务反馈调整策略，不必等人重新训练、重新发版。这是从「用模型」到「模型自己改自己」的转向。代价是，奖励设计和安全对齐的难度随之上升。

为什么重要：如果多个 Agent 都能自我改进，评测和治理的速度将追不上模型迭代。「自主训练」正在从小实验室的实验变成可落地的产品方向，这本身就是一个信号。它带来的问题比答案更值得关注：当 Agent 能改写自己，谁来约束它的行为边界？

> 原文：[Prime Agent 发布说明](https://www.primeintellect.ai/blog/prime-agent)

模型决定能力上限，运行层决定分发格局。当 Agent 开始改进自己，基础设施和安全框架还跟得上吗？