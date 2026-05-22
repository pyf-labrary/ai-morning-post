# Gemini 3.5 深夜发布，速度4倍成本省10亿

谷歌在 I/O 大会后突然发布 Gemini 3.5，性能显著提升且声称可节省 10 亿美元成本。这一动作表明，模型产品已从单纯拼能力转向拼性价比，可能挤压中小厂商的竞争力空间。

## Gemini 3.5 深夜发布，4 倍速度节省 10 亿美元

**是什么**：谷歌在 I/O 后悄然推出 Gemini 3.5 模型，CEO 宣布性能大幅提升，推理速度比前代快 4 倍，同时预计可为谷歌节省超 10 亿美元运营成本。  
**关键点**：延迟降低 75%，成本降至原来的 1/5 左右，且在多项基准测试中超越 GPT-4o、Claude 3.5。  
**为什么重要**：这是谷歌首次将成本与速度作为宣传核心，意味着大模型竞争进入“每 token 成本”精细化阶段，也给业界定了新性价比基准——谁能在保持性能的同时将成本拉至同量级，谁才能持续服务企业级客户。  
> 原文：[InfoQ](https://www.infoq.cn/article/COda3jCSAliReaA4YVJc)

## Qwen3.7-Max 发布：百万 Token 上下文窗口

**是什么**：阿里云推出 Qwen3.7-Max，具备 1M Token 上下文窗口和扩展思考模式，定位最强 Agent 模型。  
**关键点**：支持在百万 Token 内进行长程推理，可一次性处理长达 300 页文档，且内置思考链（Chain-of-Thought）能力；同时优化了工具调用（function calling）的准确率。  
**为什么重要**：1M 上下文窗口让它在合同审查、代码库分析等需长期依赖任务的场景具备差异化优势，这是目前开源模型中最大的上下文能力之一。  
> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/21/qwen-introduces-qwen3-7-max-a-reasoning-agent-model-with-a-1m-token-context-window/)

## Cohere 发布 Command A+：218B 稀疏 MoE 模型可跑在 2 张 H100 上

**是什么**：Cohere 开源 Command A+，218B 参数的稀疏 MoE（Mixture of Experts）模型，支持 48 种语言，首次适配 Agentic workflow。  
**关键点**：推理时仅激活部分专家，使得单次推理成本大幅降低；官方称最低可工作在 2 张 H100 上，部署门槛远低于同参数规模的密集模型。  
**为什么重要**：Cohere 长期深耕企业多语言场景，此次开源让中小团队也能在本地部署大参数模型用于 Agent 任务，降低了对云端 API 的依赖。  
> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/21/cohere-releases-command-a-a-218b-sparse-moe-model-for-agentic-workflows-that-runs-on-as-few-as-two-h100-gpus/)

## 微软 Fara1.5 浏览器 Agent 开源，性能超 Operator 和 Gemini

**是什么**：微软开源 Fara1.5 系列（4B/9B/27B），专注于浏览器和计算机控制 Agent。在 Online-Mind2Web 基准上超越 OpenAI Operator 和 Gemini 2.5 Computer Use。  
**关键点**：27B 版本在所有尺寸中均取得最高分，4B 版本在极低算力下仍可完成大部分浏览任务；模型支持自我纠错（self-correction）和长程规划分解。  
**为什么重要**：浏览器 Agent 被视为下一代个人助理，微软用开源+小体积+高性能的组合直接挑战闭源方案，可能加速该领域落地。  
> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/22/microsoft-releases-fara1-5-a-family-of-browser-computer-use-agents-4b-9b-27b-that-outperform-openai-operator-and-gemini-2-5-computer-use-on-online-mind2web/)

## 智谱代码生成速度达 400 tokens/s

**是什么**：智谱宣布在代码生成任务中达到每秒 400 tokens 的推理速度，自称“顶流最快”。  
**关键点**：该速度基于其自研 GPU 集群和优化的推理引擎实现，主要面向代码补全和纠错场景。  
**为什么重要**：对开发者工具而言，延迟比模型准确率更影响体验；400 tokens/s 意味着每次补全几乎无感知，可能重新定义代码助手类产品的性能门槛。  
> 原文：[量子位](https://www.qbitai.com/2026/05/422511.html)

---

模型发布密度和多样性在加速，但核心竞争已从“谁更强”转向“谁更省、谁更稳”。当 Gemini 3.5 把成本拉低一个量级，Agent 模型是否会迎来真正的规模落地？