# vLLM 推 V1，开源推理生态加速洗牌

**导语：** 今天最值得关注的，是 vLLM 从 V0 升级到 V1，首次将强化学习过程中的正确性保证作为一级考量——这直接关系到大规模 LLM 在 agentic 和 RLHF 场景下的落地可靠性。与此同时，LightSeek 发布对标 TensorRT-LLM 的 TokenSpeed，Meta 开源神经 AI 基准框架 NeuralBench，Unsloth 与 NVIDIA 联手缩短微调时间；开源推理层正在从“跑得动”转向“跑得准、跑得快、跑得稳”。

## vLLM V1：强化学习正确性优先，推理可靠性升级

vLLM 从 V0 到 V1 是一次架构级别的跃迁，核心改进在于为强化学习（RL）场景提供正确性保证。V0 已广泛应用于高吞吐推理，但在连续采样、奖励计算等 RL 步骤中，浮点误差累积可能影响策略梯度估计。V1 引入了确定性计算路径和结果校验机制，确保每次前向输出在相同输入下严格一致。这一改动的直接价值：企业可以在 vLLM 上放心跑 RLHF 流水线，不用额外写冗余校验代码。对于正在从“单轮对话”转向“多步骤 agent”的团队，V1 降低了部署复杂度。

> 原文：https://huggingface.co/blog/ServiceNow-AI/correctness-before-corrections

## LightSeek TokenSpeed：为智能体工作负载量身定制的推理引擎

TokenSpeed 是一个开源的 LLM 推理引擎，目标性能对标 NVIDIA 的 TensorRT-LLM，但专门针对 agentic workloads 优化。其设计亮点包括动态批处理策略、低预热启动和细粒度内存管理，使单次推理延迟在 agent 多轮交互（如代码生成、工具调用）中降低 30% 以上。对于预算有限的中小团队，TokenSpeed 提供了一条不依赖闭源加速库的高性能路径。LightSeek 基金会同时开放了适配主流开源模型的预编译包，降低了上手门槛。

> 原文：https://www.marktechpost.com/2026/05/07/lightseek-foundation-releases-tokenspeed-an-open-source-llm-inference-engine-targeting-tensorrt-llm-level-performance-for-agentic-workloads/

## Meta NeuralBench：神经 AI 的统一“体检”标准

Meta 开源的 NeuralBench 覆盖 36 项 EEG 任务和 94 个数据集，旨在为神经 AI（NeuroAI）模型提供可比性评估。此前该领域模型指标混乱、数据格式不统一，Benchmark 结果常无法复现。NeuralBench 提供了标准化数据处理管线、评分脚本和可复现的评估流程，覆盖注意力、认知负荷、动作意图等典型任务。对于投资人和产品经理，这意味着脑机接口（BCI）和神经界面方向的模型选型有了独立验证工具，降低技术判断的噪音。

> 原文：https://www.marktechpost.com/2026/05/07/meta-ai-releases-neuralbench-a-unified-open-source-framework-to-benchmark-neuroai-models-across-36-eeg-tasks-and-94-datasets/

## Unsloth × NVIDIA：微调效率再翻倍

Unsloth 宣布与 NVIDIA 合作，将定制的内核优化集成到最新 GPU 架构中，使 LLM 微调速度相比纯 PyTorch 实现提升 2–3 倍，内存占用减少 60%。这项合作的重点是自动识别模型中的计算瓶颈并替换为 CUDA 内核，同时保持适配器的易用性。对于需要频繁迭代的研发团队，Unsloth 提供了一个“即插即用”的高效微调选项，尤其适合在 NVIDIA 硬件上做 LoRA 或 QLoRA 微调。

> 原文：https://unsloth.ai/blog/nvidia-collab

## ds4：在 Mac 上本地运行 DeepSeek 4 Flash

知名开发者 antirez 开源了 ds4，一个基于 Apple Metal 的 DeepSeek 4 Flash 推理引擎。该引擎利用 Mac 统一内存架构和 GPU 自带的 Metal Performance Shaders，让模型在 M 系列芯片上跑出接近桌面级的速度，无需额外显卡。对于开发者而言，这意味着可以在本地安全地处理私密数据，甚至作为 agent 的离线终端。项目代码简洁，仅 3000 余行，适合学习高性能推理实现。

> 原文：https://github.com/antirez/ds4

## agent-skills：给 AI 编码代理一套“工程工具箱”

addyosmani 发布的 agent-skills 仓库，为 AI 编码代理提供了生产级技能集合，包括代码审查、安全扫描、依赖分析、测试生成等 20+ 项可调用的技能模块。每个技能以独立函数形式封装，支持被代理在生成步骤中动态调用。关键点在于它不只提供提示词模板，而是直接集成 CLI 工具（如 eslint、bandit、pytest），让代理的输出可执行、可验证。对于任何正在构建 coding agent 的团队，这是一套可以直接复用的“螺丝刀套装”。

> 原文：https://github.com/addyosmani/agent-skills

## TabPFN：表格数据的 Transformer 基座模型

PriorLabs 开源的 TabPFN 是一个基于 Transformer 的表格数据基础模型，在少样本场景（<100 样本）下表现显著优于传统树模型（如 XGBoost）和深层网络。它采用先验拟合方法，在训练阶段学习表格数据的通用分布，推理时直接给出概率预测，无需特征工程。对于数据科学团队，TabPFN 可以作为探索性数据分析的快速基线，尤其适合标注数据稀缺的业务场景。

> 原文：https://github.com/PriorLabs/TabPFN

## Local Deep Research：本地深度研究，单卡 3090 实现 95% SimpleQA

Local Deep Research 工具支持本地和云端 LLM 混合，集成 10+ 搜索引擎的实时结果，可在单张 RTX 3090 上实现约 95% 的 SimpleQA 准确率。它通过多步检索与验证循环，将搜索片段作为上下文传递给本地模型，无需联网 API。对于需要内部知识库调研或合规性要求高的团队，该工具提供了一个不依赖外部服务的深度研究替代方案。

> 原文：https://github.com/LearningCircuit/local-deep-research

**结语：** 当开源在推理正确性、效率、多样性上全面追赶闭源时，企业的选择天平正在倾斜——你准备好把生产流量切到开源推理引擎了吗？