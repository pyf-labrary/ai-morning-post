# GPT-5.6家族亮相，AI价格战升级？

今天要看的第一个信号：OpenAI 一口气推出三款 GPT-5.6 变体和一个可独立运行数小时的代理产品 ChatGPT Work。模型能力持续提升的同时，成本却在下降，而 SpaceXAI 的 Grok 4.5 直接把价格打到 $2/百万 token。价格战已成主旋律，但「代理化」才是这一波更新的深层叙事。

## OpenAI 发布 GPT-5.6 系列，同步推出 ChatGPT Work

**是什么：** OpenAI 推出 GPT-5.6 模型家族，包含 Luna、Terra、Sol 三款变体，性能提升且推理成本降低。同时发布 ChatGPT Work，一个无需持续在线介入即可自主执行任务的代理。  
**关键点：** Luna 侧重推理效率，Terra 面向平衡任务，Sol 主打长上下文。ChatGPT Work 可运行数小时，标志着 OpenAI 正式从对话工具向 agentic 工作流转型。  
**为什么重要：** 这不仅是模型迭代——ChatGPT Work 意味着 AI 从“回答问题”变成“完成任务”，对 SaaS、企业流程自动化等领域的冲击可能被低估。  

> 原文：[OpenAI](https://openai.com/index/gpt-5-6)

## SpaceXAI 推出 Grok 4.5，价格仅为竞品几分之一

**是什么：** xAI 发布 Grok 4.5，基于 Cursor 训练数据，在编码和知识任务上表现突出，定价仅 $2/百万 token。  
**关键点：** 对比 GPT-5.5（约 $15/百万 token）和 Fable 5，Grok 4.5 价格低了一个数量级。训练数据引入 Cursor 的交互轨迹，提升了代码生成的真实性。  
**为什么重要：** 价格战正在重塑 API 市场格局。如果 Grok 4.5 在编码能力上接近竞品，开发者和企业可能大规模转向，迫使其他模型降价或差异化竞争。  

> 原文：[Latent Space](https://www.latent.space/p/ainews-spacexai-launches-grok-45)

## OpenAI 发布 GPT-Live，全双工语音模型实现实时对话

**是什么：** GPT-Live 采用全双工架构，可以同时听和说，并将搜索与推理任务委托给 GPT-5.5，实现更自然的语音交互。  
**关键点：** 全双工意味着用户无需等待模型说完即可打断，延迟降低到接近人类对话节奏。整体对话由 GPT-5.5 在后台完成检索和推理，前端 GPT-Live 负责实时音频流。  
**为什么重要：** 语音交互的体验瓶颈正在解除，对智能音箱、车载助手、客服场景是质变。OpenAI 正在补齐多模态交互的“听-说”闭环。  

> 原文：[OpenAI](https://openai.com/index/introducing-gpt-live/)

## Meta 发布 Muse Spark 1.1，以低价冲击 AI 编码市场

**是什么：** Meta Superintelligence Labs 推出 Muse Spark 1.1，拥有百万 token 上下文窗口，专注于大型代理任务和代码迁移，API 定价极具竞争力。  
**关键点：** 百万上下文窗口使其能处理整个代码库的迁移、重构。定价对标开源模型，意图抢占企业级编码工具市场。  
**为什么重要：** 编码是当前 LLM 变现最快的场景之一。Meta 的低价策略配合超大上下文，可能威胁 Claude、GPT-5.5 在编码领域的份额，尤其适合需要整库迁移的遗留系统。  

> 原文：[Meta AI](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)

## Mistral 发布 Robostral Navigate，8B 模型引导机器人

**是什么：** Mistral AI 进入机器人领域，推出 Robostral Navigate，一个仅需单摄像头即可驱动机器人导航的 80 亿参数模型。  
**关键点：** 模型端侧运行，无需激光雷达或深度传感器，通过单目视觉直接输出导航指令。专用于室内环境，能耗低。  
**为什么重要：** 80 亿参数模型在边缘设备上实现视觉导航，降低了机器人部署成本。Mistral 选择从垂直场景切入，避开与通用模型的正面竞争。  

> 原文：[The Decoder](https://the-decoder.com/mistral-enters-robotics-with-robostral-navigate-an-8b-model-that-steers-robots-using-just-one-camera/)

## NVIDIA Nemotron 3 Ultra 与 LangChain 深度集成，性能领先

**是什么：** NVIDIA 发布 Nemotron 3 Ultra，在 LangChain Deep Agents 基准上实现领先性能，且成本低于 GPT-5.5 等顶级闭源模型。  
**关键点：** 深度集成 LangChain 的 agent 框架，支持工具调用和多步推理。性能超越同级开源模型，在部分 agent 任务上与 GPT-5.5 持平。  
**为什么重要：** NVIDIA 正在从基础设施向模型层延伸，通过 LangChain 生态绑定开发者。如果推理成本持续降低，开源生态可能在 agent 场景中形成竞争力。  

> 原文：[NVIDIA Blog](https://blogs.nvidia.com/blog/nemotron-langchain-agents-open-stack/)

## NVIDIA 发布压缩版 Nemotron Puzzle 75B，吞吐量提升 2 倍

**是什么：** NVIDIA 推出 Nemotron-Labs-3-Puzzle-75B-A9B，通过结构压缩和知识蒸馏，服务器吞吐量提升 2.03 倍。  
**关键点：** 将 75B 模型压缩为混合专家架构（MoE）变体，参数量减少但保持推理质量。适合批处理和高并发的生产环境。  
**为什么重要：** 对于大规模部署，吞吐量翻倍意味着成本直接减半。NVIDIA 同时在追求“更大”和“更轻”，以满足不同部署需求。  

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/09/meet-nemotron-labs-3-puzzle-75b-a9b/)

## 原力灵机 DM0.5 登场，15 万小时数据驱动 Zero-Shot 提升 31%

**是什么：** 中国团队发布原力灵机 DM0.5，在 Zero-Shot 任务上提升 31%，展现泛化涌现能力。  
**关键点：** 基于 15 万小时自监督数据训练，模型在未见过的任务中表现显著改善。团队强调“泛化涌现”，而非单纯堆参数量。  
**为什么重要：** 这是国内少有的在 zero-shot 泛化上有可量化突破的工作。31% 的提升意味着小模型也有机会在未见场景中发挥作用，值得关注其方法论是否能被复现。  

> 原文：[量子位](https://www.qbitai.com/2026/07/447508.html)

---

今天的信息量很大，但主线清晰：模型能力还在涨，价格却在跌，代理正在成为新默认交互范式。当 API 价格低到可以忽略，你的产品准备好接住 agent 的调用了吗？