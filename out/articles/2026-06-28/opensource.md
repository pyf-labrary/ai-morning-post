# DeepSeek开源DSpark，推理加速60%+

今日开源板块最值得关注的是DeepSeek开源的DSpark推测解码框架，将V4用户端生成速度提升60-85%。这意味着大模型部署的推理效率可能迈过商业化门槛，而Meta、Google、AWS同日发布的Agent工具链则暗示：开源生态正在从“模型基础设施”转向“Agent原生工具”的竞争。

## DeepSeek开源DSpark推测解码框架，加速推理60-85%

DeepSeek正式开源DSpark框架，这是一种针对DeepSeek-V4的推测解码（speculative decoding）方案，能够在用户端生成场景下实现60%–85%的速度提升。项目同时发布了详细论文和技术报告，解释了如何通过小模型提前“推测”大模型输出，减少实际推理步数。关键点在于：DSpark直接与官方MTP-1对比，数据公开可复现。对技术团队而言，这意味着若使用DeepSeek-V4，可以大幅降低单次推理延时，从而支撑更高并发的实时应用。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/06/27/deepseek-releases-dspark-a-speculative-decoding-framework-that-accelerates-deepseek-v4-per-user-generation-60-85-over-mtp-1/)

## Meta开源Astryx设计系统，AI Agent可用

Meta发布Astryx，一个基于StyleX的React设计系统，其核心亮点是提供CLI和MCP（Model Context Protocol）服务器。这意味着AI Agent可以通过标准化API直接读取和操作设计令牌（tokens），实现与人类工程师完全相同的接口。关键点：Astryx不是传统组件库，而是设计系统即引擎，Agent能按需生成样式一致的前端。为什么重要：当Agent开始使用设计系统生成代码时，UI一致性不再依赖人工协调，前端开发流程可能被根本重构。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/06/27/metas-astryx-brings-a-cli-and-mcp-server-to-an-open-source-react-design-system-agents-can-read/)

## Google Labs发布DESIGN.md规范，视觉身份可控

Google Labs提出DESIGN.md格式，一种在代码仓库中以Markdown文件描述视觉标识（如色彩、间距、字体）的规范。它让编码Agent能够对设计系统进行持久、结构化的理解，而不仅仅是读取最终样式代码。关键点：DESIGN.md最直接的好处是跨项目复用——一个仓库的“设计DNA”可以被Agent自省式读取，无需依赖零散的手写文档。对产品经理和设计师而言，这意味着设计变更后，Agent能自动感知并调整生成代码。

> 原文：[GitHub (google-labs-code/design.md)](https://github.com/google-labs-code/design.md)

## OpenMontage：首个开源Agent视频制作系统

OpenMontage项目开源发布，它是一个用AI编码助手改造为视频制作工作室的Agent系统，提供12条管线、52个工具以及500+预置Agent技能。关键点：用户可通过自然语言指令完成从脚本撰写、素材搜索、剪辑到配音的全流程，所有工具在单一CLI界面下调用。为什么重要：视频制作过去依赖多款商业软件，OpenMontage证明AI Agent可以把复杂多步骤创作封装成一个开源管道，大幅降低内容生产门槛。

> 原文：[GitHub (calesthio/OpenMontage)](https://github.com/calesthio/OpenMontage)

## AWS发布Agent Toolkit，支持MCP服务

亚马逊AWS官方推出Agent Toolkit for AWS，包含MCP服务器、技能和插件，目的是让AI Agent能直接在AWS上构建和运行。关键点：Toolkit提供了与Lambda、S3、Bedrock等核心服务对接的现成工具，Agent可以像操作CLI一样调用云资源。对开发者而言，这意味着部署Agent应用不再需要手写繁杂的IAM权限和SDK调用。AWS正在将Agent视为新的“运维单元”。

> 原文：[GitHub (aws/agent-toolkit-for-aws)](https://github.com/aws/agent-toolkit-for-aws)

## vLLM：高吞吐LLM推理引擎持续更新

vLLM项目在GitHub上保持活跃迭代，继续优化其内存高效的推理服务引擎。关键点：最新更新聚焦于更高并发下的显存管理和PagedAttention的增强，支持最新模型的快速适配。为什么重要：作为开源社区最流行的LLM推理框架之一，vLLM的改进直接影响到自建推理服务团队的成本和延迟，是DeepSeek DSpark等专用方案之外的通用选择。

> 原文：[GitHub (vllm-project/vllm)](https://github.com/vllm-project/vllm)

## gstack：Garry Tan的Claude Code配置开源

知名投资人、Y Combinator前CEO Garry Tan将其个人使用的Claude Code自定义工具集合gstack开源，包含23个针对CEO、设计师、工程经理等角色的工具。关键点：每个工具都封装了特定角色的提示词与API调用链，可直接套用或修改。为什么重要：它展示了一个顶级实践者对AI Agent的“角色定义”，为团队如何将Agent嵌入工作流程提供了可复用的模板，而非理论讨论。

> 原文：[GitHub (garrytan/gstack)](https://github.com/garrytan/gstack)

## Agent-Reach：零API费用访问全网社交媒体

Agent-Reach是一个开源工具，让AI Agent通过单一CLI读取和搜索Twitter、Reddit、YouTube等社交媒体，无需支付任何平台API费用。关键点：它通过模拟用户行为或利用公开接口实现数据抓取，风险在于可能违反平台服务条款。对数据分析师和Agent开发者而言，它提供了一条低成本的“数据管道”，但使用前需评估合规性。

> 原文：[GitHub (Panniantong/Agent-Reach)](https://github.com/Panniantong/Agent-Reach)

---

当每个Agent都能直接调用设计系统、操作社交媒体、甚至制作视频，人类开发者是否会很快变成Agent的“提示师”而非“执行者”？