# DeepSeek Flash 对标 Opus 4.8，Meta 商汤同日开源

今日模型发布板块最值得看的一件事：DeepSeek 推出实验性 Flash 视觉模型，据称在 agent 基准上直接对标 Opus 4.8。同一天，Meta 开源可本地运行的 agent 模型，商汤也放出了 SenseNova U1.5 Lite。一个清晰的信号是：多模态与本地化部署正成为所有主流厂商的公开战场，而开源对抗闭源的竞争，已经从对话模型烧到了 agent 与视觉领域。

## DeepSeek 发 Flash 视觉模型，对标 Opus 4.8

**是什么**：DeepSeek 发布实验性 Flash 视觉模型，补齐多模态能力，也是其在 agent 方向布局的关键一步。

**关键点**：据称在 agent 基准上可对标 Opus 4.8。「实验性」定位意味着快速迭代、抢先占领生态，而非追求稳定发布节奏。

**为什么重要**：DeepSeek 此前以文本模型见长，视觉能力补上后，其开源权重模型在 agent 工作流中的适用面会显著扩大。若性能真能对标闭源旗舰，将进一步压缩商业模型的性能溢价空间。

> 原文：[The Decoder](https://the-decoder.com/deepseek-releases-experimental-flash-vision-model-that-rivals-opus-4-8-on-agent-benchmarks/)

## Meta 开源本地 agent 模型，支持视觉与工具调用

**是什么**：Meta 发布了一款可本地运行的开源 agent 模型，原生支持视觉输入和工具调用。

**关键点**：「本地运行」意味着数据不出设备，推理成本和隐私风险都更低；「工具调用」则让模型不再停留于对话，而是可以直接驱动实际业务流程。

**为什么重要**：agent 类应用此前受限于云端 API 的成本与延迟。Meta 将视觉、工具调用和本地部署打包成开源模型，直接拉低了中小团队构建 agent 产品的门槛，延续了其以开源生态换取行业影响力的路径。

> 原文：[InfoQ](https://www.infoq.cn/article/aGfkSN1YlmLrUQMPea9L)

## 商汤开源 SenseNova U1.5 Lite，原生 4K 视觉

**是什么**：商汤正式开源 SenseNova U1.5 Lite，一个轻量级统一多模态大模型，支持超长指令与原生 4K 真实视觉创作流。

**关键点**：轻量级是部署优势，原生 4K 视觉则指向真实的图像创作场景，而非简单的图文理解。两者组合，意味着高分辨率视觉任务可以在更轻的资源条件下完成。

**为什么重要**：4K 视觉是复杂创作类 agent 落地的硬门槛，超长指令对应长流程任务的执行能力。商汤这次开源，等于在轻量多模态赛道上补上一个关键身位，给开发者多了一个值得评估的选项。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/6sNCkUYytWV6ixlf.html)

## 神秘 Ox Alpha 突袭 OpenRouter，性能超 Fable 5

**是什么**：OpenRouter 上出现代号 Ox Alpha 的模型，跑分据称超过 Fable 5，但厂商背景完全不明。

**关键点**：没有官方说明，没有技术细节，只有一个高分和一堆猜测。匿名发布模型正在成为 OpenRouter 上一种新的注意力玩法。

**为什么重要**：这件事的看点不在模型本身，而在评估体系的信任问题——当模型可以换了名字上架并制造声量，benchmark 的公信力就会被稀释。与其猜「这是谁」，不如问评测机制还剩下多少参考价值。

> 原文：[InfoQ](https://www.infoq.cn/article/3MNJh5F34GSsRQJJWJzY)

今日四条消息指向同一个趋势：视觉与工具调用，正成为模型发布的新基准线。问题是，开源已铺到这个程度，闭源模型的差异化还剩多少。