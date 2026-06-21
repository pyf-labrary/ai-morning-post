# OpenMontage领衔，7个开源工具齐发

今天板块最值得关注的是OpenMontage——全球首个开源代理视频制作系统，它将多智能体协作引入视频创作全流程，标志着AI视频工具的民主化迈出关键一步。与此同时，代码智能、LLM压缩、模型训练等方向也有多个高质量开源项目值得留意。

## OpenMontage：全球首个开源代理视频制作系统

**是什么：** OpenMontage是首个开源的多智能体视频制作系统，由12条流水线、52个工具和500多个代理技能构成，覆盖从脚本、拍摄到后期完整工作流。  
**关键点：** 用户可自定义代理角色（如导演、剪辑师）来协作生成视频；系统支持场景识别、多模态对齐和动态编排，显著降低专业视频创作的门槛。  
**为什么重要：** 此前Sora等闭源模型仅关注生成，而OpenMontage提供了可控的、可复现的工程化框架，对影视制作、广告、教育等领域的开源替代方案具有里程碑意义。  
> 原文：[GitHub - calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

## Codebase Memory MCP：高性能代码智能MCP服务器

**是什么：** DeusData开源了Codebase Memory MCP服务器，它将整个代码库索引为知识图谱，并暴露给AI助手使用。  
**关键点：** 支持158种编程语言，查询响应达到毫秒级；支持语义搜索、符号引用和依赖图查询，可与任何MCP兼容的AI客户端（如Cline、Continue）无缝集成。  
**为什么重要：** 对于大型项目，现有代码补全工具常缺乏全局上下文，该工具将代码理解提升到知识图谱层面，让AI能更精准地定位函数、类和依赖关系，是下一代代码智能基础设施。  
> 原文：[GitHub - DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

## Headroom：LLM压缩工具，减少60-95% tokens

**是什么：** Headroom是一个轻量级开源工具，专门压缩LLM输入中的工具输出、日志、文件和长文本，平均节省80% tokens。  
**关键点：** 采用自适应压缩算法，根据内容类型和LLM任务动态调整压缩率，官方测试显示在常见问答场景下对答案质量无显著影响。  
**为什么重要：** Token成本是LLM应用落地的主要瓶颈之一。Headroom提供了一种即插即用的优化方案，适用于agentic工作流、RAG系统和日志分析，每个开发者都可免费集成以降低成本。  
> 原文：[GitHub - chopratejas/headroom](https://github.com/chopratejas/headroom)

## Voicebox：开源AI语音工作室，支持克隆和创作

**是什么：** Voicebox是一个开源的AI语音工作室，提供语音克隆、听写和语音创作三大核心功能。  
**关键点：** 支持从少量样本（短至3秒）进行语音克隆，并可调节语调、语速和情感；听写功能支持多语言实时转写，创作模式允许用户混合多个声音源生成新语音。  
**为什么重要：** 当前语音克隆多依赖闭源API，Voicebox以MIT许可开源，使个人开发者和初创公司能够自由搭建定制化语音应用，降低音频内容制作门槛。  
> 原文：[GitHub - jamiepine/voicebox](https://github.com/jamiepine/voicebox)

## Kilo：开源全功能代理工程平台

**是什么：** Kilo是一个集成的代理工程平台，提供最流行的开源编码代理（如SWE-agent、OpenHands等），并内置工作流管理、沙盒执行和环境配置。  
**关键点：** 支持一键部署多种开源编码代理，可对比不同代理在同一任务上的表现；提供可视化调试界面和协作功能，支持跨项目重复使用代理配置。  
**为什么重要：** 编码代理是当前最活跃的AI应用方向之一，但选择和调优不同代理耗时。Kilo的集成化平台降低了评估和迭代成本，加速从实验到落地的闭环。  
> 原文：[GitHub - Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode)

## Unsloth Studio：开源AI模型训练Web UI

**是什么：** Unsloth Studio提供了一个Web图形界面，用于训练和运行Gemma 4、Qwen3.6、DeepSeek等主流开源大模型。  
**关键点：** 无需编写代码即可完成数据加载、LoRA/QLoRA配置、训练监控和模型导出；基于Unsloth优化库，训练速度比原生PyTorch快2-3倍，显存节省最高70%。  
**为什么重要：** 模型微调的门槛正在从“会写代码”降至“会点鼠标”，Unsloth Studio降低了实验成本，让更多非算法背景的从业者可以快速定制领域模型。  
> 原文：[GitHub - unslothai/unsloth](https://github.com/unslothai/unsloth)

## Slime：LLM后训练强化学习框架

**是什么：** Slime是清华THUDM开源的一个面向RL Scaling的LLM后训练框架，专为强化学习阶段设计。  
**关键点：** 支持PPO、GRPO等多种强化学习算法，提供分布式训练支持与奖励模型集成；针对大型语言模型的后训练（post-training）阶段进行优化，可复用常见开源模型。  
**为什么重要：** 预训练后的RL对齐是提升模型推理能力和安全性的关键。Slime填补了开源社区在Post-training RL框架上的空白，与DeepSpeed、TRL等现有工具互补。  
> 原文：[GitHub - THUDM/slime](https://github.com/THUDM/slime)

## STORM：LLM驱动的知识策展系统

**是什么：** 斯坦福大学开源的STORM系统，利用LLM自动研究某一主题，并生成带引用和结构的完整报告。  
**关键点：** 通过多轮对话模拟专家与记者的协作，从网文、论文等来源收集信息，最终输出含参考文献的综述；支持自定义大纲和引用格式，可集成到知识管理工具中。  
**为什么重要：** 知识策展是科研和文档工作中最耗时的环节之一。STORM将LLM的生成能力与信息检索结合，提供了从问题到完整报告的一站式开源方案。  
> 原文：[GitHub - stanford-oval/storm](https://github.com/stanford-oval/storm)

---

今天的开源工具从视频制作到代码智能，从语音克隆到模型训练，几乎覆盖了AI应用的全链路。你打算从哪一个开始试水？