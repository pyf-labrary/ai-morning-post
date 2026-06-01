# 微软开源 MarkItDown，还有三款神器

## 导语

微软开源了文件转 Markdown 工具 MarkItDown，意味着文档处理进入通用管道时代；同期还有 Hermes Agent 的多层记忆栈 Memory OS、一键生成短视频的 MoneyPrinterTurbo，以及无分词器的多语言 TTS 模型 VoxCPM 2。四个项目覆盖知识管理、内容生产、语音交互三大热门方向，值得快速关注。

## Hermes Agent 开源记忆栈 Memory OS

**是什么**  
Memory OS 是基于 Hermes Agent 的 6 层开源记忆堆栈，实现了持久化记忆、分层检索和 Wiki 式知识库功能。开发者可直接集成到 agentic 系统中，让 AI 记住并组织跨会话信息。

**关键点**  
- 6 层结构：从短期缓存到长期向量存储，支持自动摘要与更新。  
- 分层检索：根据上下文优先级返回最相关记忆，而非简单 Top-K。  
- 内置 Wiki 模式：用户可手动编辑知识，类似个人知识库。

**为什么重要**  
当前多数 agentic 系统缺乏可靠的长期记忆，Memory OS 提供了可落地的开源方案，降低构建持久化 agent 的门槛。对于希望做知识管理工具或记忆增强型产品的团队，它是关键基石。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/06/01/meet-memory-os-a-6-layer-open-source-memory-stack-built-on-top-of-hermes-agent/)

## MoneyPrinterTurbo：一键生成短视频的开源工具

**是什么**  
基于 AI 大模型的开源工具，输入主题或文案即可自动生成高清短视频，支持字幕、背景音乐和语音合成。GitHub 上长期热门，近期更新了多语言支持。

**关键点**  
- 全流程自动化：文案 → 语音 → 配图/视频素材 → 剪辑输出，无需人工干预。  
- 支持自定义模板和风格调整。  
- 目前最活跃的短视频生成开源项目之一，社区贡献持续。

**为什么重要**  
短视频创作门槛被大幅降低，个体创作者和中小团队可快速生产内容。对于关注内容营销和 AI 赋能创意的人群，这是一个可以直接拿来用的工具。

> 原文：[GitHub repository](https://github.com/harry0703/MoneyPrinterTurbo)

## 微软 MarkItDown：文件转 Markdown 开源工具

**是什么**  
微软开源的 Python 工具 MarkItDown，能将 Office 文档（Word、Excel、PowerPoint）、PDF、HTML、图片（OCR）等众多格式转换为标准 Markdown。

**关键点**  
- 统一接口：`markitdown file.ext` 即可输出 Markdown。  
- 支持保留表格、列表、标题、链接等结构化元素。  
- 内置 OCR 模块（基于 Azure AI），可识别图片中文字后转为 Markdown 表格或文本。

**为什么重要**  
文档格式转换是长期存在的痛点，尤其在企业知识库构建、RAG（检索增强生成）数据预处理中，Markdown 是最通用的中间格式。微软开源此工具，可能成为事实上的转换标准，极大简化非结构化数据的清洗流程。

> 原文：[GitHub repository](https://github.com/microsoft/markitdown)

## VoxCPM 2：无分词器多语言 TTS 开源模型

**是什么**  
OpenBMB 开源的 VoxCPM 2，是一个不依赖文本分词器的文本转语音模型，直接以语音编码为输入，支持多语言、创意声音设计（如变声、情感控制）和语音克隆。

**关键点**  
- 无分词器设计：绕过传统 phoneme 或 grapheme 分割，减少语言适配成本。  
- 支持中英文混合及跨语言克隆。  
- 可生成非自然声音（如外星人、机器人音效），适合游戏和多媒体。

**为什么重要**  
TTS 领域长期依赖语言特定的分词器，VoxCPM 2 的架构让多语言和创意场景的扩展成本大幅降低。对于开发者而言，这是目前开源社区中最接近“万能语音生成器”的模型之一。

> 原文：[GitHub repository](https://github.com/OpenBMB/VoxCPM)

## 结语

四款工具各自瞄准了 agent 记忆、内容生产、文档转换、语音生成中的具体痛点。当开源社区同时交出这些答卷，开发者的选择不再是“有没有”，而是“怎么组合出更好的产品”。