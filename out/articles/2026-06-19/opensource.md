# 编码Agent开源：Continue与UI-TARS看点

今天开源板块最值得关注的是 **Continue** 作为 Claude Code 替代品获得广泛关注，以及字节跳动开源的 **UI-TARS-desktop** 桌面多模态 Agent 栈。两个项目分别代表了编码 Agent 的两种路径：灵活框架与完整底座方案。此外，Netflix 开源了一款 Token 优化工具，年省 70 万美元，提醒我们成本控制也是 Agent 落地的重要一环。

## Continue：开源编码Agent框架获广泛关注

**是什么**：Continue 是一款开源 AI 编码助手，定位为 Claude Code 等商业工具的替代品。

**关键点**：它支持接入多种大模型（如 GPT-4、Claude、本地模型），并允许用户通过配置文件自定义 Agent 行为，从系统提示词到工具调用逻辑均可深度定制。

**为什么重要**：在编码 Agent 日益同质化的当下，Continue 提供了一种“自己掌控”的选择——开发者不必被单一模型或服务锁定，可以根据成本、隐私、性能灵活切换底座模型。这种开放性可能成为企业导入 AI 编码助手时的首选。

> 原文：[GitHub - continue.dev](https://github.com/continuedev/continue)

## UI-TARS-desktop：字节跳动开源桌面多模态AI Agent栈

**是什么**：字节跳动开源 UI-TARS-desktop，这是一套从模型到 Agent 基础设施的完整开源栈，专门面向桌面端多模态交互场景。

**关键点**：它内置视觉感知（UI 截图、元素识别）和操作执行（鼠标、键盘控制）能力，开发者可以直接将其作为桌面自动化 Agent 的骨架，无需从零搭建视觉模型与控制管线。

**为什么重要**：桌面端 Agent 长期缺乏高质量开源底座，UI-TARS-desktop 填补了这一空白。对于需要构建“看+点”类自动化流程（如软件测试、RPA 改造）的团队，这是一个起点较高、可以快速复用的工程化方案。

> 原文：[GitHub - bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)

## Superpowers：为编码Agent提供可组合技能框架

**是什么**：Superpowers 是一套 Agent 软件开发方法论，核心是一组可组合技能（composable skills），旨在提升 AI 编码能力。

**关键点**：它不只是一个工具库，而是一套编程范式——将编码任务拆解为独立、可测试、可组合的技能单元，Agent 通过组合这些技能完成复杂需求。项目附带详细文档和示例，降低了学习曲线。

**为什么重要**：当编码 Agent 从“补全几行代码”升级为“写整个函数/模块”时，技能组合是保证质量和可维护性的关键。Superpowers 让开发者能像拼乐高一样构建 Agent 的程序能力。

> 原文：[GitHub - obra/superpowers](https://github.com/obra/superpowers)

## OpenMontage：Agent驱动的自动化视频生产系统

**是什么**：OpenMontage 号称世界首个开源 agentic 视频制作系统，包含 52 个工具和 500 多个技能。

**关键点**：它将 AI 编码助手的概念扩展到视频领域——Agent 能自动解析分镜脚本、调用图像生成/字幕合成/剪辑工具，完成从素材到成片的完整流程。项目全部开源，提供本地运行方案。

**为什么重要**：Agent 的应用范围正在从代码生成扩大到创意生产。OpenMontage 证明了编码 Agent 可以成为“视频工作室”的中控大脑，为内容创作自动化打开新路径。

> 原文：[GitHub - calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

## RAGFlow：领先的检索增强生成引擎全面开源

**是什么**：RAGFlow 将前沿 RAG（检索增强生成）技术与 Agent 能力深度结合，为 LLM 提供高质量上下文层。

**关键点**：它支持多源文档解析（PDF、网页、数据库等）、语义分块、混合检索（稀疏+稠密），并内置简单的 Agent 编排能力，可让模型按需调用检索结果。

**为什么重要**：开源 RAG 引擎不少，但 RAGFlow 侧重“上下文质量”——它通过智能分块和反馈循环，降低检索噪声，减少 LLM 幻觉。对于企业知识库问答、智能客服等场景，是直接可用的基础设施。

> 原文：[GitHub - infiniflow/ragflow](https://github.com/infiniflow/ragflow)

## RD-Agent：微软开源AI驱动的研发自动化工具

**是什么**：Microsoft RD-Agent 是一款专注于数据与模型研发自动化的工具，旨在加速工业级 AI 研究。

**关键点**：它自动管理实验流程（数据探索、特征工程、模型选择、超参数调优），并记录每一步的元数据与复现方案。开源版本包含常见 ML 场景的示例模板。

**为什么重要**：AI 研发中的“重复劳动”占用了大量时间。RD-Agent 将这部分自动化，让研究人员专注于提出假设和设计新架构。开源使得中小团队也能采用微软内部的研发效率工具。

> 原文：[GitHub - microsoft/RD-Agent](https://github.com/microsoft/RD-Agent)

## VoxCPM2：无需分词器的多语言高质量语音合成

**是什么**：OpenBMB 发布 VoxCPM2，支持多语言语音生成、创意声音设计和逼真语音克隆，且无需传统 Tokenizer。

**关键点**：它绕过了音素/子词级别的分词步骤，直接对语音信号建模，从而减少信息损失，合成更加自然流畅的声音。

**为什么重要**：语音合成领域的“无Token化”是近期趋势，VoxCPM2 降低了多语言语音生成的门槛，尤其适合需要合成多种口音或进行声音克隆的创业产品。

> 原文：[GitHub - OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)

## Netflix开源工具：砍掉90%冗余Token，年省70万美元

**是什么**：Netflix 开源了一款 AI Token 优化工具，通过消除冗余词元（如重复的标点、无用格式、无效上下文），大幅降低 API 调用成本。

**关键点**：该工具在 Netflix 内部已带来年省 70 万美元的效果，且它对模型输出质量的影响极小。开源版本可直接集成到 LLM 调用链路中。

**为什么重要**：Token 成本正成为大规模部署 LLM 的巨大隐形支出。Netflix 的实践表明，通过纯后处理优化的方式就能显著降本，而无需调整模型或改动业务逻辑。这对任何将 LLM 投入生产的团队都有直接参考价值。

> 原文：[InfoQ - Netflix 开源 Token 优化工具](https://www.infoq.cn/article/SdkcGqZQ2coEqM04xsQG)

---

开源社区正在用速度回应商业化 Agent 的壁垒——但堆栈越来越多，你需要的是框架，还是完整的解决方案？