# 模型发布潮：微软NVIDIA阿里同日亮剑

今天最值得关注的是三家巨头同日发布重磅模型：微软推出推理与代码模型MAI，NVIDIA开源物理世界模型Cosmos 3，MiniMax开源百万Token上下文多模态M3。竞争格局清晰分化：美国企业在推理和物理AI上加速，中国公司在长上下文和多模态上保持领先。开源与闭源界限愈发模糊，开发者的模型选择正在爆炸式增长。

## 微软发布MAI推理与代码模型，挑战前沿

微软推出MAI-Thinking-1（350亿活跃参数推理模型）与MAI-Code-1-Flash代码模型，性能对标业界最强。MAI-Thinking-1采用稀疏激活架构，在数学推理等任务上表现优异；MAI-Code-1-Flash专注代码生成，效率突出。微软在推理模型领域补上关键拼图，与OpenAI形成双线竞争。对开发者而言，多了一个高性价比的推理选项，尤其适合需要链式思考的复杂任务。

> 原文：https://microsoft.ai/news/introducing-mai-thinking-1/

## NVIDIA发布Cosmos 3，推进物理AI世界模型

NVIDIA开源Cosmos 3全模态世界模型，结合Agent Toolkit补齐物理AI工具链。该模型支持文本、图像、视频、动作等多模态输入，能够模拟物理世界因果规律。开源降低了机器人、自动驾驶等领域的研发门槛。物理AI被认为是下一个前沿，NVIDIA通过开源模型和工具链试图成为底层基础设施，但模型复杂度和实际应用可靠性仍是挑战。

> 原文：https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/

## MiniMax M3开源：百万Token上下文+多模态

MiniMax发布M3模型，采用稀疏注意力架构，支持百万Token上下文与原生图像视频理解。在LongBench等长上下文基准上表现突出，稀疏注意力机制保障了推理效率，多模态能力原生集成无需额外适配。百万Token上下文成为主流趋势，MiniMax开源让中小团队也能尝试超长文档理解。中国创业公司在开源赛道持续输出高影响力模型，与巨头同台竞技。

> 原文：https://www.together.ai/blog/serving-minimax-m3-for-efficient-inference-unlocking-1m-token-context-and-multimodality-without-regrets

## NVIDIA Nemotron 3 Ultra成为最强开源美国模型

Nemotron 3 Ultra在多项基准超过Llama 4等模型，成为美国开源模型最强；但中国模型仍整体领先。该模型基于Nemotron系列，优化了推理和多语言能力。结果显示中美开源模型差距缩小，但中国在长上下文和多模态上仍占优。对开发者而言，Nemotron 3 Ultra提供了新的基线选择，也说明开源生态已全面国际化。

> 原文：https://the-decoder.com/nvidias-nemotron-3-ultra-becomes-the-smartest-open-us-model-but-china-still-leads/

## 阿里发布Qwen3.7-Plus：多模态智能体新基座

Qwen3.7-Plus视觉和文本能力大幅提升，跻身Vision Arena前五，支持一键复刻专业软件。阿里在视觉-语言模型上持续迭代，不仅能理解图像，还能生成代码来自动化操作专业软件界面。多模态智能体落地进入加速期，阿里通过强基座模型降低应用开发门槛。Vision Arena排名证明其视觉能力已达全球第一梯队，对自动化办公场景有直接价值。

> 原文：https://www.qbitai.com/2026/06/427730.html

## JetBrains开源Mellum2：12B MoE专业模型

JetBrains发布专为多模型AI流水线设计的Mellum2，12B参数MoE架构，遵循Apache 2.0许可。该模型定位专业工具链模型，强调与现有IDE集成和推理效率。参数规模适中，但MoE设计使其在特定任务上效率高。JetBrains从IDE厂商切入模型层，显示工具厂商对AI重组的思考，但影响力有限，适合对集成度有要求的开发者细看。

> 原文：https://huggingface.co/blog/JetBrains/mellum2-launch

## 百度文心PaddleOCR-VL-1.6刷新文档解析SOTA

PaddleOCR-VL-1.6准确率达96.33%，已上线官网支持网页端和API调用。该模型在文档OCR和版面分析上表现优异，适合发票、合同等场景。百度将能力产品化，降低使用门槛。文档数字化需求持续旺盛，细分领域的SOTA仍有商业价值，但比起前面的大模型发布，这一步属于迭代优化。

> 原文：https://www.qbitai.com/2026/06/427754.html

今天模型发布的密度和质量都创下新高，开源与闭源的界限正在消融。未来一年，你最看好哪条技术路线？