# IBM开源32K嵌入模型，多语言检索新选择

今天最值得关注的是 IBM 开源了 Granite Embedding Multilingual R2，Apache 2.0 许可，在子 1 亿参数模型中达到最佳检索质量。对于技术团队而言，这意味着获得了一个高性价比的多语言文本嵌入方案，尤其适合需要处理长上下文（32K）的检索增强生成（RAG）场景。IBM 通过开源策略在嵌入模型领域建立影响力，可能推动更多企业采用其生态系统。

## IBM Granite 多语言嵌入模型：小参数、长上下文、Apache 2.0

**是什么**：IBM 发布 Granite Embedding Multilingual R2，采用 Apache 2.0 开源许可，支持 32K 上下文窗口。模型名中的“R2”代表第二代，主要针对多语言检索任务优化。

**关键点**：参数规模低于 1 亿（子 1 亿），但在公开 benchmarks（如 MTEB 多语言子集）上取得了该量级的最佳检索质量。支持包括中文在内的多种语言，32K 上下文长度使其能处理长文档级输入，直接适配 RAG pipeline 中的文档切片与查询匹配。

**为什么重要**：1. 开源授权降低企业合规成本，适合内部部署或私有化微调。2. 小参数量意味着更低的推理成本和更快的向量生成速度。3. 32K 上下文目前在开源嵌入模型中较为稀缺（多数仍为 512～8K 长度），这为长文档检索、法律/医疗领域的多语言应用提供了新选择。4. IBM 以 Granite 系列构建开源生态，可能改变嵌入模型市场格局（以往由 Cohere、OpenAI 的闭源模型主导）。

> 原文：[Hugging Face 博客](https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2)

IBM 用开源小模型撬动检索基础设施的意图明显。你的 RAG 系统是否已经测试过 Granite 的表现？