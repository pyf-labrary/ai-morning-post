# 物理AI模型开源，NVIDIA推Cosmos 3

今日模型板块最值得关注的是NVIDIA正式发布开放世界基础模型Cosmos 3，将物理AI推理与行动能力打包给开发者，标志着物理世界AI从封闭走向开放。与此同时，MiniMax M3以百万token上下文窗口挑战闭源模型，而Nemotron 3 Ultra虽成美国最强开源模型，但整体仍落后中国。

## NVIDIA Cosmos 3：物理AI的开放时刻

**是什么**：NVIDIA在GTC Taipei上发布Cosmos 3，一个开放的世界基础模型，专为物理AI设计，支持从感知到行动的全链路推理。

**关键点**：Cosmos 3并非单一大模型，而是包含多种规模的预训练权重与基准，开发者可直接用于机器人、自动驾驶等场景的仿真与规划。它整合了物理规律、空间理解与动作生成，使AI能在模拟环境中“边思考边行动”。

**为什么重要**：此前物理AI模型多为闭源或专有，Cosmos 3的开放降低了物理世界智能化的门槛，可能加速具身智能与工业自动化落地的速度。NVIDIA选择此时开源，也在与国内竞品争夺开发者生态。

> 原文：https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/

## MiniMax M3：百万token的MoE开源模型

**是什么**：MiniMax发布M3模型，采用MSA架构，支持原生多模态、代理编程以及百万token的上下文窗口，并以开放权重形式发布。

**关键点**：MSA（Multi-Scale Attention）架构在长序列处理上效率更高，百万token意味着可直接输入整本书或完整代码库进行推理。M3在多模态理解与生成任务上表现对标闭源竞品，且开源权重允许商业使用。

**为什么重要**：百万token上下文目前仍是闭源模型的“特权”（如Claude 200K、GPT-4 128K），MiniMax首次将这一能力大规模开源，可能改变长文档、代码分析、Agent任务的产品设计范式。

> 原文：https://the-decoder.com/minimax-m3-open-weight-model-with-a-million-token-context-challenges-proprietary-leaders/

## Nemotron 3 Ultra：美国最强，仍不及中国

**是什么**：NVIDIA发布的Nemotron 3 Ultra在多项基准测试中成为美国开源模型第一，但整体分数仍落后于中国开源模型（如Qwen、DeepSeek变体）。

**关键点**：Nemotron 3 Ultra在推理、数学、代码等维度表现突出，专为开发者与云端推理优化，且支持NVIDIA自家硬件加速。对比之下，中国开源模型在综合得分上领先约5%-10%。

**为什么重要**：模型竞争已进入“国家队”层面。Nemotron 3 Ultra的发布填补了美国在开源大模型头部位置的空白，但中美的技术差距正在缩小甚至局部反超，未来开源生态的“地缘”分化值得关注。

> 原文：https://the-decoder.com/nvidias-nemotron-3-ultra-becomes-the-smartest-open-us-model-but-china-still-leads/

## JetBrains Mellum2 12B MoE：编码场景的轻量专家

**是什么**：JetBrains在HuggingFace发布Mellum2，一个12B参数的混合专家（MoE）模型，专为代码理解与生成设计。

**关键点**：12B参数MoE实际激活参数更少，推理速度快于同尺寸稠密模型。Mellum2在HumanEval、MBPP等编码基准上达到接近30B模型的效果，且完全开源。

**为什么重要**：JetBrains作为IDE巨头，推出自研模型意在构建“代码助手+编辑器”的深度闭环。对于开发者而言，轻量高效的编码模型可本地部署，降低对云API的依赖。

> 原文：https://huggingface.co/blog/JetBrains/mellum2-launch

## Qwen3.7-Plus：阿里多模态升级

**是什么**：阿里发布Qwen3.7-Plus，在文本能力基础上全面升级视觉-语言能力，同时保持完整Agent能力（函数调用、工具使用）。

**关键点**：Qwen3.7-Plus支持图像字幕、视觉问答、文档理解，并在复杂多轮对话中维持一致推理。其Agent框架仍基于Function Call，可无缝对接阿里云工具链。

**为什么重要**：Qwen系列此前在中文开源模型中稳居前列，此次多模态补齐后，可覆盖电商、内容审核、教育等场景。对B端用户而言，一个模型同时处理文本、图像、工具调用，降低了部署复杂度。

> 原文：https://36kr.com/newsflashes/3835230281856390?f=rss

## 星海图G0.5：机器人零样本泛化新基线

**是什么**：星海图推出G0.5 VLA模型（Vision-Language-Action），实现零样本泛化至新物体、新环境，让机器人“边思考边行动”。

**关键点**：G0.5在未见过场景下的抓取成功率达到85%以上，无需额外微调。模型基于视觉-语言对齐，将自然语言指令直接映射为机器人动作序列，并支持实时纠错。

**为什么重要**：具身智能的“零样本泛化”是行业长期痛点。G0.5较低的部署门槛可能吸引更多中小制造商尝试机器人自动化，但距离复杂工业任务仍有距离。

> 原文：https://www.leiphone.com/category/industrynews/i8V0VCdEywlci8jo.html

当世界模型开始开源，物理世界的AI化还会远吗？而百万token的上下文窗口，是否意味着Agent即将迎来“全场景记忆”的质变？