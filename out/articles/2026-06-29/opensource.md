# DeepSeek 开源 DSpark，V4 生成提速 85%

今天开源板块最值得关注的是 DeepSeek 发布的推测解码框架 DSpark，它让 V4 模型每用户生成速度提升 60-85%。这套框架通过并行草稿分支和马尔可夫头绕过传统 MTP 的串行瓶颈，意味着推理效率不再是大模型部署的硬约束，边缘侧与云端协同的推理成本有望进一步下探。

## DeepSeek 开源 DSpark，加速 V4 生成至 85%

DeepSeek 发布的 DSpark 是一套推测解码框架，核心思路是让草稿模型与主模型并行工作，其中的“马尔可夫头”能根据上下文预测多个 token，而非逐个生成。关键点在于，相比之前 MTP 方案，DSpark 将每用户生成速度提升 60-85%，且无需重新训练原模型。为什么重要：高吞吐低延迟是当前 LLM 产品化最实际的痛点，DSpark 提供了一个可直接复用的开源方案，未来更多推理场景可能会从“等结果”变成“边生成边确认”。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/06/27/deepseek-releases-dspark-a-speculative-decoding-framework-that-accelerates-deepseek-v4-per-user-generation-60-85-over-mtp-1/)

## 百度开源整书级 OCR 模型

百度发布的新 OCR 模型基于前 DeepSeek 研究员的工作，能够一次处理整本书籍内容。关键点包括：模型采用端到端架构，无需分页识别，对整个文档布局有全局理解；名字暂未公布，但代码和模型权重已在 GitHub 开源。为什么重要：传统 OCR 需要逐页扫描、排版修复，整书级模型直接输出结构化文本，对数字图书馆、古籍整理、财务票据批量处理等场景是质的提升。

> 原文：[量子位](https://www.qbitai.com/2026/06/439464.html)

## Anthropic 开源 Skills 仓库，推动 Agent 技能标准化

Anthropic 在 GitHub 上发布了 skills 项目，提供一组标准化的 Agent 技能实现，例如文件读写、API 调用、网页抓取等。关键点：每个技能都是可独立调用、可组合的模块，开发者可直接使用或提交新技能。为什么重要：Agent 技术正在从“调一个模型”转向“编排多个专业技能”，Anthropic 试图定义一套通用接口，降低碎片化风险，类似早期 LangChain 但更聚焦于技能而非链。

> 原文：[GitHub - anthropics/skills](https://github.com/anthropics/skills)

## OpenCode：开源编码 Agent 框架

OpenCode 是一个面向编程任务自动化的开源框架，支持代码生成、测试、调试等。关键点：它不绑定某家大模型，而是提供插件式后端，允许开发者接入本地或云端 LLM。为什么重要：编程 Agent 竞争激烈，OpenCode 的开放架构让团队可以自由选择推理引擎，同时内置了代码执行沙箱和安全控制，适合企业级场景。

> 原文：[GitHub - anomalyco/opencode](https://github.com/anomalyco/opencode)

## AWS 推出 Agent Toolkit for AWS，集成 MCP 和 Skills

AWS 官方发布 Agent Toolkit，提供 MCP（模型上下文协议）服务器、预置 Skills 和插件系统，方便 AI 代理在 AWS 基础设施上构建应用。关键点：Toolkit 支持快速集成 S3、Lambda、DynamoDB 等云服务，开发者只需几行配置即可让 Agent 读写 AWS 资源。为什么重要：这是云厂商第一次以第一方身份推出 Agent 工具包，意味着 Agent 从“实验项目”变成“云原生产品”，MCP 和 Skills 的互操作性标准有望加速落地。

> 原文：[GitHub - aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws)

## 一行命令克隆任意网站：AI Website Cloner 开源

GitHub 上的 AI Website Cloner Template 允许用户输入 URL 后一键生成整站副本。关键点：它使用浏览器截图 + 代码生成模型，输出可直接运行的 HTML/CSS/JS，但暂无法处理动态交互。为什么重要：对前端开发者而言，这意味着快速获取设计灵感；对非技术人员，可能成为搭建个人页面的“捷径”。但版权争议值得注意——克隆工具会模糊“学习”与“盗用”的边界。

> 原文：[GitHub - JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)

## Wayfinder Router：本地与云端 LLM 查询确定性路由

Wayfinder Router 是一个开源路由器，可根据规则（如 token 成本、延迟要求、隐私等级）将查询分发到本地或托管 LLM。关键点：规则可编程，支持条件判断、负载均衡、降级策略；无状态设计，可嵌入现有推理系统。为什么重要：混合部署（部分本地、部分云端）正在成为企业标配，Wayfinder 填补了“如何决策路由”这一环节的空缺，让成本与性能的权衡自动化。

> 原文：[GitHub - itsthelore/wayfinder-router](https://github.com/itsthelore/wayfinder-router)

## AMD Strix Halo RDMA 集群搭建指南开源

社区开发者发布了在 AMD Strix Halo 平台上使用 vLLM 搭建分布式推理集群的教程，重点覆盖 RDMA 网络配置。关键点：Strix Halo 是 AMD 集成高性能 NPU 的 APU，配合 vLLM 可实现低成本算力横向扩展；教程包含从 BIOS 设置到 vLLM 启动的完整步骤。为什么重要：AMD 在推理生态的追赶速度超出预期，这份开源指南降低了开发者尝试 AMD 硬件的门槛，尤其是在多节点部署场景中，RDMA 的稳定性往往是传统弱势。

> 原文：[GitHub - kyuz0/amd-strix-halo-vllm-toolboxes](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes/blob/main/rdma_cluster/setup_guide.md)

---

今天开源社区的动向像一个“工具箱”集中爆发：推理加速、Agent 技能、整书 OCR、路由决策、集群搭建……底层逻辑是，2026 年的开源不再只是“放代码”，而是在定义标准与接口。你真正在意的，是哪个框架会活下来成为事实标准？