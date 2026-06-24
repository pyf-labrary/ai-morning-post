# Gemini 3.5 Flash：AI代理操控电脑

今天最值得关注的是谷歌DeepMind为Gemini 3.5 Flash新增的computer use功能——模型不再只是“看”屏幕，而是能直接点击、输入、完成任务。这或许是AI从聊天助手向真正代理跨越的关键一步，将重新定义人机交互的边界。此外，Cursor发布自研模型和Git平台、Mistral OCR 4升级结构化提取、字节30秒视频生成也值得留意。

## 谷歌DeepMind发布Gemini 3.5 Flash电脑操控能力

**是什么**：Gemini 3.5 Flash新增computer use功能，可理解屏幕截图中的UI元素，并模拟鼠标点击、键盘输入等操作，端到端执行任务。这是主流多模态模型首次集成完整的GUI操控能力。

**关键点**：模型通过屏幕截图“看到”按钮、文本、菜单，结合自然语言指令自动生成操作序列。DeepMind展示了跨应用完成订票、填写表单等场景，无需插件或API绑定。

**为什么重要**：AI代理从概念走向实用。开发者可构建自动化工作流替代RPA，普通用户能用自然语言“指挥”电脑。但安全与可靠性仍是瓶颈——误操作、权限控制、复杂界面下的失败率有待验证。这是今年最值得跟踪的技术方向之一。

> 原文：[DeepMind博客](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/)

## Cursor发布自有AI模型及Git平台、移动App

**是什么**：代码编辑器Cursor宣布推出自研AI模型（未公开参数量），同时推出全新Git托管平台和移动端应用，试图扩展为开发者全栈工具生态。

**关键点**：自研模型可能针对代码补全、重构、调试深度优化，减少对第三方模型的依赖与延迟。Git平台直接对标GitHub，移动App支持代码浏览和轻量编辑。

**为什么重要**：Cursor从“套壳工具”走向平台化，自研模型可控制成本并提升差异化。但Git平台需要解决用户迁移成本和社区生态问题，移动端功能有限，短期可能难以撼动GitHub。关注其模型在代码生成质量上的实际表现。

> 原文：[The Decoder](https://the-decoder.com/cursor-announces-its-own-ai-model-a-new-git-platform-and-a-mobile-app/)

## Mistral发布OCR 4，支持结构化文档提取

**是什么**：Mistral OCR 4模型可输出包含边界框、置信度的结构化文本，适用于RAG（检索增强生成）和企业搜索场景。

**关键点**：Mistral宣称在72%的盲测案例中胜出对手，支持多语言、表格、公式、手写体。输出为JSON格式，含每个字符或单词的坐标和置信度，便于下游解析。

**为什么重要**：企业级文档数字化的痛点在于非结构化数据难以被检索。OCR 4的结构化输出能直接提升RAG系统的召回精度，减少“幻觉”。Mistral延续开源策略，可能推动企业搜索和文档自动化应用加速落地。

> 原文：[The Decoder](https://the-decoder.com/mistrals-new-ocr-model-beats-competitors-in-72-percent-of-blind-test-cases-company-says/)

## 字节跳动Seedance 2.5突破30秒视频生成

**是什么**：Seedance 2.5将AI视频生成时长延长至30秒以上，同时提升时序一致性和画质。

**关键点**：此前多数模型限制在10秒内，30秒意味着可生成完整产品演示、短叙事片。字节跳动着重优化角色一致性、运动平滑度和画面稳定性。

**为什么重要**：长视频生成是内容创作、广告、影视预演的高价值场景。但30秒内的剧情连贯性和细节控制仍是挑战，需观察实际评测中的翻车率。若质量达标，可能催生新的视频生产工具。

> 原文：[The Decoder](https://the-decoder.com/bytedances-seedance-2-5-breaks-the-30-second-barrier-for-ai-video-generation/)

今天最值得关注的是AI代理的落地信号——Gemini学会了用电脑。当AI能直接操作屏幕，你的下一个“助手”可能不再只是聊天窗口。