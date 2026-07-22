# 谷歌 Gemini 3.6 Flash 降价 17%，agentic 时代定价战打响

今天模型发布板块最值得关注的是谷歌一次性推出三款闪存系模型，专为 agentic 工作负载优化并降价，同时透露 Gemini 4 已进入训练。这一动作说明大模型竞争正从「参数军备」转向「性价比+场景适配」，agentic 应用的成本拐点可能提前到来。

## 谷歌发布 Gemini 3.6 Flash 系列，降价 17% 押注 Agent

Google DeepMind 在 7 月 22 日发布了 Gemini 3.6 Flash、3.5 Flash-Lite 和 3.5 Flash Cyber 三款模型。核心变化是输出价格降低 17%，同时增强长上下文与工具调用能力，专为 agentic 工作负载（如多步推理、API 调用）优化。3.5 Flash Cyber 侧重安全防御场景。官方还透露正在训练 Gemini 4，但未给出时间表。这意味着谷歌正在用更便宜的「闪存」系列抢占 agent 开发者的心智，与 OpenAI 的 GPT-4o mini 路线类似。

> 原文：[DeepMind 博客](https://deepmind.google/blog/introducing-gemini-36-flash-35-flash-lite-and-35-flash-cyber/)

## 百度文心助手任务 Agent 首登国际榜首

百度旗下文心助手任务 Agent 在 PinchBench v2 评测中以 94.6% 的最高分超越 Claude、GPT 等模型，成为首个以正式产品形态登顶总榜的国产智能体系统。评测涵盖多轮任务规划、工具使用和错误修复。虽然单点基准不能代表通用能力，但「产品即成绩」的路径值得关注——这意味着百度在 agent 落地的工程化上走到了前沿。

> 原文：[量子位](https://www.qbitai.com/2026/07/457117.html)

## 阿里千问发布 Qwen-Image-3.0，输入长度提升 4.5 倍

Qwen-Image-3.0 大幅扩展了文本输入长度（提升至原先的 4.5 倍），强化多模态理解能力。对于需要长文本描述+图像联合推理的场景（如文档分析、图表问答）有直接帮助。阿里在视觉语言模型上继续做「加长上下文」的差异化，方向与谷歌 Gemini 的 1M token 输入类似。

> 原文：[InfoQ](https://www.infoq.cn/article/jXQ5oQeOcEjLkuq2Qc0y)

## Cisco 开源 Antares 安全模型，小模型精准定位漏洞

Cisco 发布 Antares 350M 和 1B 两个开放权重模型，专门用于代码仓库中已知漏洞的局部定位。在多个基准上超越 GPT-5.5，且模型大小仅为千亿级模型的千分之一。该模型专为企业安全审计设计，开源意味着中小团队也能获得高质量的代码安全分析能力，可能改变 DevSecOps 的落地成本结构。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/21/cisco-foundation-ai-releases-antares-350m-and-1b-open-weight-models-that-localize-known-vulnerabilities-inside-real-codebases/)

## Poolside 发布 Laguna S 2.1，开源编码模型逼近头部

Poolside 发布 118B MoE 模型 Laguna S 2.1，仅用 8B 活跃参数和 1M 上下文窗口，在 SWE-Bench Multilingual 上的表现接近闭源头部模型。对需要私有化部署的编码团队来说，这是一个性价比极高的选择。值得一提的是，该模型使用 Apache 2.0 许可证开源，适合企业二次开发。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/21/poolside-releases-laguna-s-2-1/)

---

当谷歌、百度、阿里同时砸向 agent 场景，你准备好为「每调用一次」的成本重新规划架构了吗？