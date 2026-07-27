# Kimi K3开源，微软安全模型首发

月之暗面今日开源了Kimi K3模型权重与技术报告，并附带AgentENV训练框架，这是中国团队首次将前沿级模型完整开放。同时微软推出首款网络安全专用模型MAI-Cyber-1-Flash，宣称性价比碾压竞品。两个方向——开源权重的“透明化”与垂直领域的“专精化”——正在同时重塑模型发布格局。

## 月之暗面开源Kimi K3模型权重与技术报告

Moonshot AI正式发布Kimi K3开放权重模型，并公开详细技术报告，同时开源了配套的AgentENV训练框架。关键点：Kimi K3在多项基准测试中接近或达到当时闭源前沿模型水平，此次开源使得社区可以基于权重进行微调、部署和研究。AgentENV框架则针对agentic任务环境设计，可降低训练长链条推理agent的门槛。为什么重要：这是中国大模型公司首次完整地开源一个接近头部水平的模型，打破了此前仅开源小尺寸或中间版本的惯例，可能加速全球开源生态的竞争与基础模型民主化。

> 原文：https://the-decoder.com/moonshot-ai-releases-kimi-k3-open-weights-and-infrastructure-after-shaking-up-the-frontier-model-race/

## 微软发布首款网络安全模型 MAI-Cyber-1-Flash

微软推出专门为网络安全场景设计的模型MAI-Cyber-1-Flash，同时发布MDASH安全平台。关键点：该模型基于安全领域数据优化，在威胁检测、漏洞分析、事件响应等任务上声称以更低延迟和成本超越通用模型及竞品。MDASH平台集成模型部署、安全编排与自动化响应。为什么重要：这是微软首次推出垂直领域专用基础模型，意味着AI安全赛道从“用通用模型做安全”转向“安全原生模型”，可能倒逼其他安全厂商调整策略。

> 原文：https://arstechnica.com/security/2026/07/microsoft-unveils-ai-security-tools-it-says-outperform-competing-platforms/

## 蚂蚁百灵发布新款混合推理模型 Ling-3.0-Flash

蚂蚁集团旗下百灵大模型推出Ling-3.0-Flash，主打原生混合推理能力。关键点：该模型可在深度思考与快速响应之间动态切换，无需显式触发CoT，适合需要即时效用的任务。为什么重要：混合推理正在成为模型标配，Ling-3.0-Flash的发布表明蚂蚁也在这一方向追赶，但具体性能对比尚未公开，需要关注后续第三方评测。

> 原文：https://www.qbitai.com/2026/07/461149.html

## NVIDIA 发布 Cosmos-H-Dreams 手术机器人生成式仿真

NVIDIA推出实时生成式仿真模型Cosmos-H-Dreams，专为外科机器人训练设计。关键点：模型可根据输入条件实时生成高保真手术场景，用于强化学习训练，无需传统物理仿真引擎。为什么重要：生成式仿真有望大幅降低机器人训练成本，加速手术自动化落地，但伦理与临床验证仍是重大瓶颈。

> 原文：https://huggingface.co/blog/nvidia/cosmos-h-dreams

## Black Forest Labs 发布多模态流模型 FLUX 3

FLUX 3支持图像、视频、音频及机器人动作预测，首次将四种模态统一在一个流模型架构下。关键点：采用流匹配（flow matching）而非扩散，声称在生成速度和质量上优于先前的单模态模型。为什么重要：多模态统一是基础模型的关键方向，FLUX 3的扩展能力值得关注，但跨模态对齐和泛化性仍待社区验证。

> 原文：https://www.marktechpost.com/2026/07/26/black-forest-labs-releases-flux-3-a-multimodal-flow-model-for-image-video-audio-and-robot-action-prediction/

## 小米 MiMo-V2.5 登顶 OpenRouter 全球调用量双榜

小米MiMo-V2.5成为OpenRouter上周和本月调用量最高模型，单周token量突破10T。关键点：调用量领先并不意味着综合性能最强，更多反映了性价比和易用性吸引的开发者群体。为什么重要：小米模型以相对低的定价和稳定的服务赢得大量应用场景，说明在模型商品化阶段，商业策略比纯技术指标更具决定性。

> 原文：https://36kr.com/newsflashes/3913798998201732?f=rss

## Grok 4.5 发布，强化编码与 Agent 任务

SpaceXAI推出Grok 4.5，重点改进编码、agentic任务及知识工作能力。关键点：更新包括更长的上下文窗口和更好的工具调用一致性。为什么重要：Grok系列此前在编程领域口碑一般，此次升级意在缩小与Claude、GPT-4o的差距，但能否突破还需看实测数据。

> 原文：https://www.producthunt.com/products/grok

当开源模型逼近闭源前沿，闭源模型的护城河还剩多少？