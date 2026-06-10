# Claude Mythos 5首秀，Google三箭齐发

今日模型发布板块最值得关注的是Anthropic首次公开Mythos级模型，但仅限信任伙伴通过Glasswing访问，公众版Fable 5则带有严格护栏。Google同步推出三款模型——从4倍加速的文本扩散开源模型到实时语音翻译，再到无需编码器的多模态，两家公司的策略分化愈发明显：Anthropic走高端闭源路线，Google延续开源+生态打法。

## Anthropic发布Claude Fable 5与Mythos 5，首个公开Mythos级模型

Anthropic今日推出双旗舰：面向公众的Claude Fable 5带有严格安全护栏，而Mythos 5通过Glasswing平台向信任伙伴开放完整能力。两者在编程和科学领域均有大幅进步，尤其Mythos 5被认为是Anthropic迄今为止能力最强的模型。但高昂的API定价（传闻比前代高数倍）和访问限制引发社区争议——有开发者质疑这本质上是“能力公开但门槛极高”，可能限制实际应用场景。

> 原文：https://www.anthropic.com/news/claude-fable-5-mythos-5

## Google开源DiffusionGemma，文本生成速度提升4倍

Google DeepMind发布实验性26B MoE开源模型DiffusionGemma，采用文本扩散方法替代传统自回归生成，在NVIDIA GPU上实现高达4倍加速。NVIDIA已为其做专门优化。关键点在于，这是首个大规模开源文本扩散模型，改变了“扩散=图像”的固有认知。对于需要低延迟文本生成的应用（如聊天机器人、代码补全），该模型可能成为新的效率基准。不过，实验性质意味着生产环境稳定性仍需验证。

> 原文：https://deepmind.google/blog/diffusiongemma-4x-faster-text-generation/

## Google推出Gemini 3.5 Live Translate，实时语音翻译70+语言

Gemini 3.5 Live Translate实现流式端到端语音到语音翻译，延迟降至几秒，覆盖70多种语言。已集成到Google AI Studio、Google Translate和Google Meet。与传统的级联式系统不同，该模型直接输出翻译后语音，保留了语气和节奏，是实时通信场景的实用突破。对跨国协作工具、客服和内容本地化产品而言，这降低了进入门槛——不必再依赖多步流水线。

> 原文：https://deepmind.google/blog/fluid-natural-voice-translation-with-gemini-35-live-translate/

## Google开源Gemma 4 12B：统一无编码器多模态模型

Google DeepMind发布Gemma 4 12B，一个统一、无需视觉编码器的多模态模型，可直接处理文本和图像输入。相比需要单独视觉编码器的方案（如CLIP+LLM），该架构更简洁，训练和推理效率更高。性能优于前代Gemma 3，但12B规模仍属轻量级，适合边缘部署。对希望集成图像理解能力但受限于算力的团队来说，这是一个可立即使用的选项。

> 原文：https://deepmind.google/blog/introducing-gemma-4-12b-a-unified-encoder-free-multimodal-model/

## HiDream-O1-Image-1.5登顶中国文生图榜单，超越谷歌英伟达

智象未来（HiDream.ai）发布的商用版图像生成模型在Artificial Analysis文生图榜单上位列中国第一、全球第二，超越Google Nano Banana 2和NVIDIA等。该模型在质量、速度、多样性指标上表现均衡，且支持商用授权。这是中国团队在文生图赛道少有的全球性排名成绩，但对标顶级模型（如OpenAI DALL·E 4、Midjourney）仍有差距。投资价值在于其差异化路线——专注于高性价比的商业场景。

> 原文：https://www.qbitai.com/2026/06/434196.html

当Anthropic用价格和护栏划出“禁区”，Google用开源和生态铺开“全赛道”，接下来值得关注的是：开发者会为Mythos 5的完整能力付出多高的成本？