# Opus 5 炸场 ARC-AGI-3，NVIDIA 开源 Sana

Anthropic 最新 Opus 5 在衡量真实智能的 ARC-AGI-3 基准上，以半价性能超越 Fable 5 和 GPT-5.6 Sol，这意味着模型竞争正从“堆参数比谁强”转向“效率与泛化成本双杀”。同一日，NVIDIA 开源了高效线性扩散 Transformer 图像模型 Sana，给高分辨率生成提供了新的轻量选择。

## Anthropic Opus 5 半价击败 Fable 5 与 GPT-5.6 Sol

**是什么**：Anthropic 在 ARC-AGI-3 基准上发布了 Opus 5 的评测结果，该基准被设计为衡量“真实智能”（而非语言流畅度），Opus 5 得分超过 Fable 5 和 GPT-5.6 Sol，且推理成本仅为后两者的一半。

**关键点**：ARC-AGI-3 侧重抽象推理与泛化能力，与常见的 LLM 排行榜（如 MMLU、GPQA）不同，它直面 AI 在未见任务上的适应力。Anthropic 通过架构优化（而非单纯扩大参数量）实现了这一跨越。

**为什么重要**：这重新定义了“最强模型”的评判标准——企业客户在选择时可能更看重投入产出比。若 Opus 5 的泛化优势持续，OpenAI、Fable 等对手将被迫在效率维度上跟进。

> 原文：[https://the-decoder.com/anthropics-opus-5-blows-past-fable-5-and-gpt-5-6-sol-on-the-benchmark-designed-to-measure-real-intelligence/](https://the-decoder.com/anthropics-opus-5-blows-past-fable-5-and-gpt-5-6-sol-on-the-benchmark-designed-to-measure-real-intelligence/)

## NVIDIA 开源 Sana：线性扩散 Transformer 图像模型

**是什么**：NVIDIA 实验室在 GitHub 上开源了 Sana，一个基于线性扩散 Transformer 架构的图像生成模型，主打高效、高分辨率合成。

**关键点**：Sana 采用线性注意力机制替代传统二次注意力，大幅降低计算开销，同时保持生成质量。项目包含预训练权重和推理代码，开发者可直接部署。

**为什么重要**：当前主流扩散模型（如 Stable Diffusion 3、SDXL）依赖二次注意力导致显存和延迟瓶颈。Sana 的线性方案为实时高分辨率生成（如 4K）铺平了道路，且开源生态能加速应用落地。

> 原文：[https://github.com/NVlabs/Sana](https://github.com/NVlabs/Sana)

当智能的成本被腰斩，企业选模型会优先看效率，还是泛化？