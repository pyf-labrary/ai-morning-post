# 谷歌Gemini 3.5快4倍，英伟达开源光速模型

今天的模型战场，速度成为唯一主线。谷歌 Gemini 3.5 将推理成本砍掉近一个量级，英伟达用扩散架构挑战自回归霸权，而阿里与 Anthropic 则各自展示了“自主运行”与“漏洞发现”这两面镜子——模型能力的边界在快速外扩，但维护责任也在同步膨胀。

## 谷歌深夜发布Gemini 3.5：速度提升4倍，年省超10亿美元

谷歌CEO皮查伊亲自站台，宣布 Gemini 3.5 正式发布。核心卖点是推理速度比前代快4倍，直接换算成基础设施成本，每年可节省超10亿美元。据内部消息，该模型已替代旧版本支撑谷歌内部多个核心业务线。

关键点在于：速度提升来自架构级优化而非简单堆算力。这意味着中小团队若无法复现这种效率，将在大规模推理场景中失去竞争力。对投资者而言，“年省10亿”不仅仅是成本故事——它暗示着谷歌在模型商业化的边际成本上已拉开身位。

> 原文：[InfoQ - 谷歌CEO皮查伊亲自介绍Gemini 3.5](https://www.infoq.cn/article/COda3jCSAliReaA4YVJc)

## 英伟达开源Nemotron扩散语言模型，文本生成速度接近“光速”

NVIDIA 发布 Nemotron-Labs 扩散语言模型，采用扩散方法替代自回归，将文本生成速度推至接近理论极限。Hugging Face 官方博客称该模型在长文本生成任务上延迟降低一个数量级。

关键点：扩散模型在图像生成领域早已成熟，但在语言模型上一直受限于离散 token 的采样效率。Nemotron 证明了扩散路径在语言上同样可行，且能显著提速。对开发者而言，这意味着实时对话、流式输出等场景的部署成本可能大幅下降——英伟达正在从卖 GPU 转向卖模型架构标准。

> 原文：[Hugging Face Blog - NVIDIA Nemotron-Labs Diffusion](https://huggingface.co/blog/nvidia/nemotron-labs-diffusion)

## 阿里Qwen模型自主运行35小时，优化自研芯片代码

阿里公布最新进展：其 AI 模型 Qwen 连续自主运行 35 小时，为自家定制芯片优化底层代码，未有人工干预。据 The Decoder 报道，该模型在编译开关、内存布局等环节进行了数千次尝试，最终生成性能提升明显的补丁。

关键点：这是“软件定义硬件”的典型实践——模型不仅能写代码，还能针对特定硬件架构做编译器级别的优化。对芯片厂商而言，AI 驱动芯片设计自动化（AI for Chip）的成熟速度可能快于预期。但需警惕：自主运行 35 小时不等于完全可靠，依赖度需长期验证。

> 原文：[The Decoder - Alibaba's AI model ran autonomously for 35 hours to optimize code for its own custom chip](https://the-decoder.com/alibabas-latest-ai-model-ran-autonomously-for-35-hours-to-optimize-code-for-its-own-custom-chip/)

## Anthropic发布Claude Mythos预览版：捉bug速度超过修复能力

Anthropic 推出 Claude Mythos Preview，专攻代码漏洞发现。实测中其发现 bug 的数量和速度远超开发团队修复能力，导致安全团队被迫优先排序漏洞等级，甚至需要暂停部分功能以避免补丁堆积。

关键点：这不是模型能力翻车，而是效率失衡带来的安全悖论——漏洞发现速率远超修复流水线规模。对 CISO 和工程管理者来说，这意味着需要重新审视安全操作流程：自动化发现工具必须与自动化修复工具联动，否则只会制造“半开的后门”。Claude Mythos 或许会成为安全运维中的一个新标杆，但也暴露出工具矩阵不配套的短板。

> 原文：[The Decoder - Anthropic warns Claude Mythos Preview finds bugs faster than developers can patch them](https://the-decoder.com/anthropic-warns-claude-mythos-preview-finds-bugs-faster-than-developers-can-patch-them/)

---

速度决定成本，成本决定规模，规模决定生态——今天发布的每一个模型，都在尝试重新定义这三个变量的关系。你的团队准备好迎接“漏勺式”工具链了吗？