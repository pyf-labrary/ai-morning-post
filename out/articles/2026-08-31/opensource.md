# 官方Agent技能库同日上线，生态塑形

今日板块最值得关注的，不是某个模型发布，而是「技能」正在成为 Agent 生态的新接口：Anthropic 与 Google 同日上线官方维护的插件目录与技能库。另一边，vLLM v0.28.0 继续夯实推理底座，OCR 工具则据称把 PDF 转 Markdown 压到单页 20 毫秒。判断：开源竞争的注意力正在从模型层上移到能力分发层。

## vLLM v0.28.0 发布：推理引擎再升级

主流大模型推理引擎 vLLM 发布 v0.28.0，主要涉及性能与功能两方面的更新。作为自托管大模型推理的核心选择之一，vLLM 的每个版本都会直接影响部署选型、吞吐与成本基线。关键点在于，今天多数 Agent 工作流的底层都跑在 vLLM 这类引擎上，技能生态越热闹，推理底座越不能掉链子。为什么重要：在各家模型快速迭代的当下，推理引擎的稳定性与兼容性往往比跑分更决定生产环境敢不敢上。

> 原文：[GitHub Release](https://github.com/vllm-project/vllm/releases/tag/v0.28.0)

## Anthropic 上线官方 Claude Code 插件目录

Anthropic 推出官方维护的 Claude Code 插件目录，开发者可以从中发现经过验证的插件。关键点：官方目录解决的是信任与分发问题——此前插件散落在个人仓库，质量与维护状况参差不齐，目录相当于给 Claude Code 的插件生态建了一个审核入口。为什么重要：Claude Code 要成为开发者日常依赖的 Agent 入口，插件目录就是它的应用商店，这一步决定了生态能长多大。

> 原文：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

## Google 开源 Agent Skills 库

Google 在 GitHub 开源了面向自家产品与技术的 Agent Skills 集合，开发者可通过 skills.sh 一键安装到各类 Agent 工作流。关键点：与 Anthropic 同日动作，表明「Skill」正在成为跨厂商的 Agent 能力分发格式——不再只是代码片段，而是带入口、可安装、可组合的模块。为什么重要：官方背书意味着技能分发标准可能收敛，Agent 不必什么都从头学，「装技能即可干活」的开发方式正在成为现实。

> 原文：[google/skills](https://github.com/google/skills)

## 开源 OCR：20ms 将 PDF 页转 Markdown

据量子位报道，一款新开源 OCR 工具可将 PDF 页面在约 20 毫秒内转为 Markdown，3 秒处理约 200 份文档，速度比同类方案快近 300 倍。关键点：PDF 转 Markdown 是 RAG、文档解析、Agent 读取资料的高频前置步骤，过去往往要调用付费 API 或忍受分钟级处理；把这一步压缩到毫秒级且开源，直接降低了文档智能化的落地成本。为什么重要：速度数据有待实测复现，但方向明确——文档解析正在成为开源生态里被快速商品化的环节。

> 原文：[量子位报道](https://www.qbitai.com/2026/08/481075.html)

## OpenClaw 从爆红到落幕：Harness 接棒

曾风靡一时的开源 AI Agent 项目 OpenClaw 热度明显退潮，据量子位报道，社区注意力正转向 Harness 等新一代方案。关键点：Agent 框架的迭代周期已经短到以月为单位，一个项目从爆红到被替代可能只需一年——热度榜上的 star 数并不等于长期维护力。为什么重要：对技术选型者而言，拥抱 Agent 框架前要看社区迁徙方向，而非当下 star 数；对观察者而言，这是开源 Agent 生态快速洗牌的又一证据。

> 原文：[量子位相关报道](https://www.qbitai.com/2026/08/480855.html)

## LiveKit Agents：开源实时语音 AI Agent 框架

LiveKit Agents 是一个面向实时语音 AI Agent 的开源框架，支持语音、视频等多模态实时交互式智能体开发。关键点：相比多数以文本交互为主的框架，LiveKit 直接提供了实时音视频通道，把「能听会说的 Agent」的开发门槛显著降低。为什么重要：实时交互是客服、陪伴、教育等场景的商业化前提，开源意味着这类产品可以自托管，不必绑定云厂商。

> 原文：[livekit/agents](https://github.com/livekit/agents)

## scientific-agent-skills：165 个科研技能开源

scientific-agent-skills 自称排名第一的 Agent 技能库，提供 165 个即用型科研技能和 100+ 科学数据库，覆盖生物、化学、医学与药物发现等领域。关键点：通用 Agent 技能之外，垂直学科技能库正在形成「技能+数据」的组合资产——有数据库可查、有流程可跑，科研 Agent 才有实际生产力。为什么重要：当工具能力变成可安装技能，专业领域 Agent 的复制成本会显著下降，科研团队可以从造轮子转向直接调技能。

> 原文：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

## MoneyPrinterTurbo 再登 GitHub 热榜

MoneyPrinterTurbo 是开源的 AI 短视频生成工具，输入主题或关键词即可一键生成高清短视频，近期再次登上 GitHub 热门榜。关键点：它的价值不在技术独特性，而在「输入即出片」的完整流程——把视频生成过程封装成一条流水线，极大降低了短视频生产门槛。为什么重要：内容生产工具每隔一段时间就会再火一次，说明 AI 生成内容的需求始终在线；对开发者而言，它是观察 Agent 工作流封装范式的简单样本。

> 原文：[harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

今天不是模型发布日，而是技能生态的塑形日。你的 Agent 工作流，装官方技能库了吗？