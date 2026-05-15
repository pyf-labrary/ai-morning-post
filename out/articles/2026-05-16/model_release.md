# Granite R2登顶小模型检索，MoE扩散首次落地

今天IBM在HuggingFace发布Granite Embedding Multilingual R2，以不足1亿参数在检索任务上达到最佳质量，支持32K上下文且开源Apache 2.0。这一定位表明小模型嵌入仍有优化空间，尤其多语言场景下企业级应用无需依赖大参数量。同时Zyphra推出首个MoE扩散模型ZAYA1-8B，用离散扩散替换自回归解码，推理加速最高7.7倍。

## Granite Embedding R2：小参数、长上下文、多语言检索新标杆

IBM发布Granite Embedding Multilingual R2，是面向多语言的文本嵌入模型，参数规模小于100M，支持32K上下文窗口，采用Apache 2.0许可开源。模型在多项检索基准上达到同规模最佳质量（state-of-the-art for sub-100M），多语言覆盖主流语言，适合企业级RAG系统，尤其对长文档检索有利。在嵌入模型领域，参数量并非越大越好——IBM证明小模型通过数据质量和训练策略仍能领先，这对预算有限或需本地部署的团队是务实选择。Apache 2.0许可进一步降低商用门槛。

> 原文：[HuggingFace Blog](https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2)

## ZAYA1-8B：首个MoE扩散模型，推理加速可达7.7倍

Zyphra发布ZAYA1-8B-Diffusion-Preview，将预训练的自回归MoE（Mixture of Experts）语言模型（8B总参数，激活参数约2.5B）转换为离散扩散模型。推理时不再逐个token自回归生成，而是通过多步噪声去除并行生成，实现最高7.7倍速度提升。模型权重已在HuggingFace开放，转换方法保留了原MoE架构的知识但改变解码范式。扩散模型在图像生成中主导，而ZAYA1-8B是首个将其引入MoE语言模型的尝试，可能开辟非自回归文本生成新路径，尤其适合低延迟场景。但预览版生成质量与一致性尚需社区验证。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/15/zyphra-releases-zaya1-8b-diffusion-preview-the-first-moe-diffusion-model-converted-from-an-autoregressive-llm-with-up-to-7-7x-speedup/)

小模型嵌入和扩散语言模型都在挑战“更大=更好”的定势——当效率提升10倍，哪类场景会最先拥抱新范式？