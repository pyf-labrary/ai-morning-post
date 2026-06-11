# DeepMind开源DiffusionGemma，速度提升4倍

今天最值得关注的是Google DeepMind开源了文本扩散模型DiffusionGemma，推理速度最高提升4倍，经NVIDIA优化后已可在GPU上高效运行。这标志着非自回归生成路线从实验走向实用，可能重塑开源模型的推理成本格局。此外，Cohere、Decart、智象未来和小米也分别发布了各有特色的新模型。

## DiffusionGemma：文本扩散路线提速4倍

Google DeepMind开源了DiffusionGemma，采用文本扩散技术替代传统自回归解码，在GPU上实现最高4倍速度提升，并已获得NVIDIA优化适配。该模型保留了Gemma的核心能力，但生成方式完全改变：一次性生成整个序列而非逐token预测。

- **关键点**：速度优势显著，尤其适合长文本或批量生成场景；开源权重，开发者可自行部署；NVIDIA优化暗示了硬件层面的协同。
- **为什么重要**：文本扩散模型此前多限于图像领域，DiffusionGemma将其引入语言生成，证明了非自回归路线在质量与速度上可与主流方案竞争。若被广泛采用，可能降低大规模推理的算力门槛。

> 原文：[Google DeepMind Blog](https://deepmind.google/blog/diffusiongemma-4x-faster-text-generation/)

## Cohere North Mini Code：30B MoE编码模型，3B活跃参数

Cohere发布了首个面向开发者的编码模型North Mini Code，采用30B参数MoE（混合专家）架构，但仅需3B活跃参数即可运行。支持256K上下文，可在单张H100 GPU上部署。针对agentic coding场景优化，能处理复杂代码生成与调试任务。

- **关键点**：稀疏激活设计大幅降低推理成本；专门为编码设计，与通用模型差异化；256K上下文利于长文件或项目级理解。
- **为什么重要**：编码模型赛道已有CodeLlama、StarCoder等，Cohere的MoE方案在保持性能的同时显著降低资源需求，可能让更多中小团队在单卡上运行高质量编码助手。

> 原文：[Marktechpost](https://www.marktechpost.com/2026/06/11/meet-north-mini-code-coheres-30b-open-weight-mixture-of-experts-model-with-3b-active-parameters-for-agentic-coding/)

## Decart Oasis 3：世界模型生成逼真驾驶场景

Decart推出Oasis 3世界模型，能够实时生成数小时逼真的驾驶场景，专为自动驾驶测试设计。开发者可通过API调用，模拟多种路况和天气条件。TechCrunch指出该模型存在一些局限性，但整体画质和连贯性有显著提升。

- **关键点**：数小时连续生成而非短片段，对自动驾驶仿真意义重大；API形式降低了使用门槛；但仍需注意生成内容的物理合理性。
- **为什么重要**：世界模型被视为自动驾驶训练的关键基础设施，Oasis 3展示了生成式AI在模拟环境中的能力，可能减少对真实路测数据的依赖。

> 原文：[TechCrunch](https://techcrunch.com/2026/06/10/decarts-new-world-model-can-simulate-hours-of-photorealistic-driving-with-some-caveats/)

## HiDream-O1-Image-1.5：中国文生图榜单第二

智象未来（HiDream）的HiDream-O1-Image-1.5在Artificial Analysis文生图榜单上取得中国第一、全球第二，超越了Google和NVIDIA的模型。该模型采用改进的扩散架构，在图像质量、提示遵循度等方面表现突出。

- **关键点**：中国模型首次进入全球文生图前三；超越海外巨头但未披露具体训练数据和算力；可能受益于大规模中文标注数据。
- **为什么重要**：文生图领域的竞争从开源模型向榜单排名转移，HiDream的突破表明中国团队在视觉生成上的追赶速度加快，可能影响企业对供应商的选择。

> 原文：[量子位](https://www.qbitai.com/2026/06/434196.html)

## 小米开源千Token每秒大模型

小米开源了其最快大模型，吞吐量超过1000 Tokens/秒，参数规模达1T，但可在通用GPU上运行。该模型支持Vibe Coding（一种交互式编程范式），强调实际生产环境下的低延迟推理。

- **关键点**：1T参数但吞吐量极高，说明使用了量化或稀疏技术；专为Vibe Coding优化，面向开发者实时协作场景；开源进一步丰富了中国大模型生态。
- **为什么重要**：小米入局大模型开源，且聚焦推理速度而非纯粹参数规模，可能吸引注重性价比的开发者。但具体架构和基准测试未公布，需后续验证。

> 原文：[量子位](https://www.qbitai.com/2026/06/434225.html)

结语：文本扩散能否成为下一代生成范式？DiffusionGemma已给出一个有力的答案；而Cohere、Decart等模型则在细分赛道上展示了效率与场景的深度结合。