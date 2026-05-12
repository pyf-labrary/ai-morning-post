# Thinking Machines发布原生交互模型

今天最值得关注的是前OpenAI CTO翁荔创立的Thinking Machines Lab发布首款模型TML-Interaction-Small，支持全双工实时语音交互，直接跳过了传统VAD（语音活动检测）模式。这意味着AI对话能力将更接近人类的自然交谈节奏，而非“你一句我一句”的轮替。同时百度文心5.1的预训练成本压缩94%也值得留意——效率提升正在重塑模型竞争格局。

## Thinking Machines Lab：全双工语音模型打破VAD范式

翁荔的创业公司Thinking Machines Lab（原OpenAI CTO）发布了首个产品TML-Interaction-Small 276B-A12B。该模型支持全双工实时语音交互，即双方可以同时说话和倾听，不必等待对方说完。关键突破在于它绕过了传统的VAD（语音活动检测）模式，后者通常在静默后检测语音，导致交互延迟和僵硬。模型基于MoE架构（276B参数，12B活跃参数），专为交互场景优化。**为什么重要**：这是少数从底层架构设计就瞄准“实时对话”的发布，而非在已有模型上做微调。如果体验合格，可能会推动语音助手从“按钮触发”转向“随时交谈”，甚至改变智能音箱、客服系统的交互设计。

> 原文：[Thinking Machines Blog](https://thinkingmachines.ai/blog/interaction-models/)

## 百度文心5.1：预训练成本猛降94%

百度发布文心大模型5.1，声称通过架构革新（如稀疏注意力、量化训练等）将预训练成本降低94%，同时保持与顶级模型（如GPT-4级别）接近的性能。**关键点**：成本压缩接近20倍，如果真实，意味着之前需数千万美元的预训练现在只需几百万美元，但官方未披露具体评估基准和“顶级模型”的对比细节。**为什么重要**：这暗示模型效率可能不再是少数公司的壁垒，更多企业将有能力训练自己的大模型。不过，百度过去在自研芯片（昆仑）和分布式系统上有积累，能否复现成本优势还需独立验证。

> 原文：[The Decoder报道](https://the-decoder.com/baidus-ernie-5-1-cuts-94-percent-of-pre-training-costs-while-competing-with-top-models/)

## Interfaze.ai：声称高精度新架构，细节稀缺

Interfaze.ai发布博客，宣称其新模型架构在准确性和规模上均有突破，但仅提供了部分概念描述，无模型权重、基准测试或具体算力需求。**关键点**：博客标题强调“high accuracy at scale”，但文内没有给出任何可复现的指标，也未说明是否开源或API可用。**为什么重要**：在模型发布密集周期里，缺乏技术细节的声明容易沦为噪音。但Interfaze团队背景（未公开）或许有潜力，建议观望后续披露。

> 原文：[Interfaze Blog](https://interfaze.ai/blog/interfaze-a-new-model-architecture-built-for-high-accuracy-at-scale)

## MiniCPM-V 4.6：1.3B移动端视觉语言模型

面壁智能（ModelBest）推出MiniCPM-V 4.6，仅1.3B参数，专为移动设备设计，可在手机端运行多模态推理（识图、回答等）。**关键点**：团队强调高效架构（如低比特量化、紧凑注意力），实测可在旗舰手机CPU上达到实时推理。**为什么重要**：轻量级多模态模型使应用场景从云端扩展到离线终端，比如本地相册搜索、实时物体识别等。对于开发者和产品经理，这一模型可能降低AI功能嵌入移动产品的门槛。

> 原文：[Product Hunt](https://www.producthunt.com/products/minicpm-4-0)

全双工语音交互和超低成本预训练让人反思：AI能力的主战场是交互体验还是训练效率？你更关心哪一个？