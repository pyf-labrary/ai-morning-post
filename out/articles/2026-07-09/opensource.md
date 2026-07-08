# 具身模型VLA 2.0开源，多芯片推理加速

蚂蚁灵波今日开源LingBot-VLA 2.0，支持20种机器人构型、预训练6万小时数据，是具身智能领域最大规模的开源基座模型之一。与此同时，法国AI初创ZML发布了免费的多芯片推理加速软件LLMD，目标直接对准AI运行成本。这两条新闻分别指向“模型能力扩展”和“推理效率提升”，构成今日开源工具板块的核心看点。

## 蚂蚁灵波开源LingBot-VLA 2.0具身基座模型

是什么：蚂蚁灵波（Ant LingBot）开源第二代视觉-语言-动作（VLA）模型，覆盖20种不同机器人构型，预训练数据量达6万小时。关键点：这是目前公开可用的、支持最多机器人形态的VLA基座模型。开源意味着开发者可以在自己的硬件上直接微调或部署，无需从头预训练。为什么重要：具身智能的落地依赖多样的本体硬件，一个统一的开源VLA有望大幅降低行业试错成本，尤其对中小机器人公司而言是基础设施级别的利好。

> 原文：[https://www.leiphone.com/category/industrynews/4583hFHXszrX7fky.html](https://www.leiphone.com/category/industrynews/4583hFHXszrX7fky.html)

## ZML开源LLMD软件，加速多芯片推理

是什么：法国AI初创公司ZML发布免费软件ZML/LLMD，可在多块AI芯片之间并行加速推理，无需修改现有模型。关键点：LLMD软硬件协同优化，支持跨卡、跨节点通信，专门针对大模型推理场景。ZML此前因自研芯片架构备受关注，这次转而提供纯软件方案。为什么重要：大模型推理成本一直是企业采用AI的核心障碍。LLMD若能做到即插即用、显著提升吞吐量，将在降低单位请求成本的同时，缓解对单一高端芯片的依赖。

> 原文：[https://techcrunch.com/2026/07/08/hot-french-startup-zml-releases-free-product-to-speed-inference-across-lots-of-ai-chips/](https://techcrunch.com/2026/07/08/hot-french-startup-zml-releases-free-product-to-speed-inference-across-lots-of-ai-chips/)

## Liquid AI开源Antidoom方法，减少推理模型死亡循环

是什么：Liquid AI发布Antidoom，一种针对推理模型“死亡循环”（doom loop）的修正方法，基于最终token偏好优化（FTPO）。关键点：推理模型在长链思考时容易陷入低效循环，Antidoom通过调整采样偏好来跳出该状态。FTPO是Liquid AI自研的强化学习策略。为什么重要：doom loop是当前推理模型（如o1、DeepSeek-R1等）部署时的常见痛病。Antidoom提供了一种可插拔的开源方案，能直接提升推理链的可靠性和效率。

> 原文：[https://www.marktechpost.com/2026/07/07/liquid-ai-antidoom-doom-loops-ftpo/](https://www.marktechpost.com/2026/07/07/liquid-ai-antidoom-doom-loops-ftpo/)

## sqlite-utils 4.0发布，新增数据库模式迁移

是什么：Simon Willison发布sqlite-utils 4.0，这是该工具首次重大版本升级。关键点：新版本支持数据库模式迁移（schema migration），包括自动检测表结构变化并生成迁移脚本。为什么重要：sqlite-utils是数据工作者处理SQLite的常用CLI工具，模式迁移是呼声最高的功能。这一更新使开发者无需手动编写ALTER TABLE语句，对数据管道迭代效率有明显提升。

> 原文：[https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything)

## OfficeCLI开源：AI代理办公套件命令行工具

是什么：OfficeCLI是首个专为AI代理设计的Office文件（Word/Excel/PPT）读写编辑开源工具，单二进制文件，无需安装Office套件。关键点：它提供强大的命令行界面，支持格式转换、内容提取和文档生成。为什么重要：AI代理在执行任务时常需要操作Office文件，过去依赖第三方库或云API，OfficeCLI将这一能力本地化、轻量化，是Agent工具链的重要补充。

> 原文：[https://github.com/iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)

## 腾讯云CubeSandbox开源，支持Arm架构

是什么：腾讯云开源CubeSandbox，一个提供即时、并发、安全的Agent沙箱，现已支持Arm架构。关键点：沙箱可用于安全运行AI Agent代码，支持隔离和资源限制。并发性能是亮点，且新增Arm64平台支持。为什么重要：在AI Agent安全风险日益受关注的当下，一个开源、跨架构的沙箱方案能帮助开发者在本地或边缘设备上安全运行不可信代码，降低供应链风险。

> 原文：[https://github.com/TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)

## Anthropic发布官方Claude Skills目录

是什么：Anthropic在GitHub上发布官方Claude Code Plugins目录及skills仓库。关键点：该仓库收集了社区与官方贡献的、可复用的Claude能力模块，涵盖编程、数据分析等场景。为什么重要：这是Claude生态向Agent复用迈出的关键一步。类比GPTs Store，Skills目录降低了开发者构建自定义Claude Agent的门槛，但也需要关注其质量管控和扩展性。

> 原文：[https://github.com/anthropics/skills](https://github.com/anthropics/skills)

## NousResearch开源Hermes Agent

是什么：NousResearch发布Hermes Agent，一个可成长的AI代理框架。关键点：它支持记忆扩展、工具调用顺序学习和持续自我优化，强调“agent成长”而非静态配置。为什么重要：当前Agent框架多采用静态prompt，Hermes Agent尝试引入动态学习机制，如果效果稳定，可能成为下一代Agent系统的基础组件。

> 原文：[https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

---

今天的开源工具既有VLA 2.0这样的具身智能基座，也有Antidoom、LLMD等推理优化方案。当模型能力与运行效率双双开源开放时，谁是第一批吃到红利的工程团队？