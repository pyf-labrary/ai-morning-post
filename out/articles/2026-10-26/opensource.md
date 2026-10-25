# 机器人标注，英伟达开源 Flora 降本 125 倍

英伟达开源 Flora，声称把机器人视频标注成本降到 GPT-6 Astra 的 1/125。这个倍数是厂商口径，实际效果取决于任务类型和数据质量，但它指向一个更实际的问题：机器人落地的瓶颈正在从模型能力转向数据标注的成本与吞吐。今天这份开源列表里，微软、AWS、Cloudflare、Anthropic 和 Cognition 发布的几乎都是 Agent 的周边能力——编排、运行时、安全审计、插件。比起模型本身，开源竞赛的重心正在转向 Agent 的基础设施。

## 英伟达开源 Flora，机器人视频标注成本降至 1/125

英伟达开源了 Flora，官方说法是它把机器人视频标注成本降到了 GPT-6 Astra 的 1/125。机器人视频标注是机器人数据管线里最耗人力的环节之一，直接影响策略训练的数据规模。关键点不在“125 倍”这个数字本身，而在于英伟达选择把标注工具开源，而不是只提供模型或算力。成本对比目前只有厂商口径，实际效果取决于任务类型和数据质量。为什么重要：如果标注成本真能下降两个数量级，机器人数据飞轮的转速会明显加快，开源工具也可能成为英伟达机器人生态的入口。对做 robot learning 的团队来说，值得先拿自己的数据试一遍，而不是直接采信倍数。

> 原文：[The Decoder](https://the-decoder.com/nvidia-open-sources-flora-to-make-robot-video-labeling-125x-cheaper-than-gpt-6-astra/)

## 微软 Agensh：用 Git 和聊天协调 1024 个 Agent

微软研究院开源了 Agensh，一个多 Agent 框架。它的设计取向很明确：不做中心编排器，Agent 之间通过 Git 仓库、聊天和发现板协作，官方称可扩展到 1024 个 Agent。多 Agent 系统常见的瓶颈在编排器——它既是单点，也是协调开销的来源；Agensh 把协作状态放到 Git 和聊天这类已有基础设施上，等于让 Agent 用“工程团队的方式”协作。为什么重要：1024 是实验规模，不代表生产可靠性，但这个思路值得关注——多 Agent 的扩展性可能不取决于更聪明的调度器，而取决于更朴素、可审计的协作介质。Git 天然带版本和 diff，对调试 Agent 行为是加分项。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/24/microsoft-agensh-multi-agent-harness-1024-agents/)

## 英伟达 OpenShell：给自主 Agent 一个安全运行时

英伟达在 GitHub 开源了 OpenShell，定位是为自主 AI Agent 提供安全、私有的运行环境。Agent 要真正干活，就得执行代码、访问文件、调用网络和内部系统；这些能力一旦放开，沙箱、权限和网络隔离就成了落地前提。OpenShell 的关键词是“安全”和“私有”，指向企业对数据不出自有环境的需求。为什么重要：Agent 运行时正在成为云厂商和芯片厂商的新战场。谁定义了 Agent 执行任务的标准环境，谁就掌握了工具接入和算力消耗的入口。同一份列表里，英伟达还开源了 Flora，两件事放在一起看，它在补的不是模型，而是机器人和 Agent 的工作环境。

> 原文：[GitHub](https://github.com/NVIDIA/OpenShell)

## OpenMobile-2：开源手机 Agent 开始追平闭源

OpenMobile-2 给出的信号是：开源智能手机 Agent 在任务表现上可以和专有模型竞争。手机 Agent 的难点在于跨 App 操作、界面理解和长流程任务的稳定性，过去这类能力多掌握在闭源模型手里。OpenMobile-2 的价值不只是“开源”，而是把移动 Agent 的门槛往下拉了一截——团队可以复现、改造并部署自己的方案。为什么重要：手机是 Agent 最高频的入口之一，如果开源方案在常见任务上够用，差异化会从模型能力转向设备权限、App 生态和隐私架构。需要保留的判断是：“可媲美”取决于评测任务集，真实场景的长尾稳定性还要看后续复现。

> 原文：[The Decoder](https://the-decoder.com/openmobile-2-proves-open-source-smartphone-agents-can-rival-proprietary-models/)

## Cognition 把 Devin 的漏洞修复拆成 3 个 MIT 技能

Cognition 开源了 Devin 的漏洞修复插件，包含 3 个 MIT 许可的 Agent 技能，用来盘点、修补并测试 PHP、Node.js 和自管 GitLab 的 RCE 漏洞。关键点有两个：一是 MIT 许可，企业可以较自由地复用和改造；二是覆盖“自管 GitLab”，说明它瞄准的是内网和私有部署场景，而不是只服务托管代码平台。为什么重要：安全修复是 Agent 最容易证明 ROI 的场景之一——任务边界清晰、有可验证结果、人力缺口大。Cognition 把 Devin 的能力拆成技能插件，也是在把“通用编码 Agent”往“可嵌入流程的安全工人”方向推。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/24/cognition-devin-vulnerability-fixes-plugin-php2shell-nodejs-gitlab/)

## AWS 官方下场，Agent Toolkit 自带 MCP 服务器

AWS 发布了 Agent Toolkit，包含官方支持的 MCP 服务器、技能和插件，目标是让 AI Agent 在 AWS 上构建应用。关键点在于“官方支持”和 MCP：Agent 接云服务时，权限、版本和兼容性通常是最容易出问题的部分；官方维护的 MCP 服务器把这些责任收拢了，集成的不确定性会下降。为什么重要：MCP 正在成为 Agent 工具接入的通用接口，云厂商官方维护 MCP 服务器，等于把自己的服务变成 Agent 的“原生工具”。对做 Agent 产品的团队，这意味着接入 AWS 的成本下降；对云厂商，这是新的分发入口。

> 原文：[GitHub](https://github.com/aws/agent-toolkit-for-aws)

## Cloudflare 开源安全审计技能，结果要机器可读

Cloudflare 开源了一个编码 Agent 技能，可以执行多阶段安全审计，并输出可独立验证的机器可读结果。安全审计最容易卡在“信任”上：Agent 说有问题，人得复核；Agent 说修好了，CI 得能验证。这个技能把输出做成机器可读、可独立验证，等于把 Agent 的审计结论接入了自动化流程。为什么重要：Agent 进入安全流程的前提不是更会写报告，而是结果可复现、可验证、可审计。Cloudflare 的切入点是技能层，而不是又一个安全扫描器；这和 Cognition 的漏洞修复插件一起，说明 Agent 的安全能力正在被拆成可组合的技能，而不是绑在某个 Agent 产品里。

> 原文：[GitHub](https://github.com/cloudflare/security-audit-skill)

## Anthropic 开源知识工作插件库，按角色和团队定制 Claude

Anthropic 发布了面向 Claude Cowork 的开源插件库，让 Claude 能针对不同角色、团队和公司提供专业化能力。知识工作 Agent 的差异化，越来越不在模型本身，而在上下文和流程：同一个模型，给销售、法务、财务用的插件不同，产出质量差别很大。Anthropic 把插件库开源，一方面降低企业定制 Claude 的门槛，另一方面也在把“角色化知识工作”变成生态标准。为什么重要：如果插件库成为企业部署 Claude 的起点，Anthropic 锁定的就不只是模型调用量，还有工作流的分发。对做垂直 Agent 的团队，这既是模板，也是竞争——通用插件覆盖得越多，垂直产品的空间越需要靠深度数据守住。

> 原文：[GitHub](https://github.com/anthropics/knowledge-work-plugins)

今天开源的主角不是更强的模型，而是 Agent 的基础设施：标注、编排、沙箱、审计和插件。当这些基础能力都被大厂开源，创业公司的壁垒会落在哪一层？