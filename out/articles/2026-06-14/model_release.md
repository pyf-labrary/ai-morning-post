# Claude两款模型遭强制下架，国产GLM-5.2开源

今天最值得关注的是美国政府首次以国家安全为由，要求 Anthropic 全球暂停 Claude Fable 5 和 Mythos 5，理由是可被利用的越狱漏洞——这为模型发布增添了制度性风险变量。与此同时，智谱 GLM-5.2 以 MIT 协议开源，科大讯飞发布多模态大模型 X2-VL 瞄准具身智能，Count Anything 则在视觉计数这一基础能力上取得进展。

## 美国政府强制下架 Claude Fable 5 和 Mythos 5

美国商务部认定 Claude Fable 5 和 Mythos 5 存在可被利用的越狱漏洞，要求 Anthropic 在全球范围内暂停访问。Anthropic 表示不同意该决定但已服从。这是美国政府首次直接干预具体模型的部署，以国家安全为由而非通常的合规审查。先例一旦确立，模型的安全性评估将不再是内部选项，而可能成为行政许可事项，直接影响后续模型的发布节奏与合规成本。

> 原文：[Anthropic](https://www.anthropic.com/news/fable-mythos-access)

## 智谱 GLM-5.2 正式发布，下周开源

智谱宣布 GLM-5.2 面向 Coding Plan 全量用户开放，覆盖 Lite/Pro/Max/团队版，API 将于下周上线，模型遵循 MIT 协议开源。MIT 意味着商用、修改、再发布几乎不受限，对开发者和企业而言是当前最友好的开源许可之一。结合 Coding Plan 聚焦编程场景，GLM-5.2 直接对标 Codex 类产品，有望吸引大量海外与国内开发者迁移。

> 原文：[36氪](https://36kr.com/newsflashes/3851264775804160)

## 星火多模态大模型 X2-VL 发布

在无锡具身智能机器人产业链伙伴大会上，科大讯飞发布星火多模态大模型 X2-VL，定位为具身智能产业的“国产 AI 大脑”。多模态能力（视觉+语言）是机器人感知与决策的基础，具身智能赛道当前缺乏成熟的大模型支撑，X2-VL 试图补齐这一空白。科大讯飞的语音和自然语言积累可复用至人机交互，但具体性能仍需下游方案验证。

> 原文：[36氪](https://36kr.com/newsflashes/3851320295166976)

## Count Anything 模型：精准计数目标物体

新发布的 Count Anything 模型能准确统计图像中特定物体的数量。这是一个典型的“看似简单实则困难”的任务——背景杂乱、目标遮挡、尺度变化都容易导致误差。模型解决了计数泛化性问题，可用于工业质检、医学影像分析、零售盘点等场景。技术亮点在于不依赖标注密度图，而是直接输出计数结果。

> 原文：[The Decoder](https://the-decoder.com/new-ai-model-called-count-anything-does-exactly-what-it-says-and-thats-harder-than-it-sounds/)

---

今天的模型发布板块呈现两个极端：美国监管突然收紧，国产开源加速奔跑。当政府可以以“越狱漏洞”为由要求全球下架时，你的模型权限还安全吗？