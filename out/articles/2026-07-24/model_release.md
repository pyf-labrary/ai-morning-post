# 小模型逆袭：Poolside 碾压大模型，Flux 3 原生音频

**导语**：今日模型发布板块最值得关注的不是参数数量竞赛，而是“小模型碾压大模型”的趋势——Poolside 118B MoE 编码模型性能超越更大开源模型，且成本更低；同时 Black Forest Labs 的 Flux 3 首次实现文生视频原生音频，将多模态推入新阶段。这两个信号共同指向：下一阶段的竞争焦点正在从“堆参数”转向“工程效率与多模态能力”。

## Poolside Laguna S 2.1：118B 参数、编码任务上超越更大模型

**是什么**：Poolside 发布开源编码模型 Laguna S 2.1，仅 118B MoE 参数，但在多个编码基准测试中性能超过参数量更大的开源模型（如 DeepSeek-Coder-V2、CodeLlama 等），且推理成本更低。

**关键点**：
- 模型采用混合专家架构（MoE），虽总参数量小，但激活参数更高效。
- 在 HumanEval 等标准上取得开源模型最佳成绩，性能接近部分闭源模型。
- 强调低成本部署，可运行在单张 A100-80G GPU 上。

**为什么重要**：这再次证明了高效的模型设计和训练数据质量比单纯扩大参数规模更重要。对于企业级应用，这意味着更低算力门槛和更快迭代周期。

> 原文：[The Decoder](https://the-decoder.com/poolsides-laguna-s-2-1-is-a-small-open-weight-coding-model-that-punches-well-above-its-size/)

## Flux 3 发布：文生视频首获原生音频，最长 20 秒

**是什么**：Black Forest Labs 发布 Flux 3，文本生成视频模型首次支持同步输出原生音频（包括人声、环境音等），视频最长 20 秒，音画一致性好。

**关键点**：
- 基于其此前 Flux.1、Flux.2 的视频生成能力，新增音频生成模块，无需后期合成。
- 支持风格控制，可指定音频类型（如解说、背景音乐、自然声音）。
- 已知短板：长视频场景中音频连贯性偶有抖动。

**为什么重要**：原生音频输出消除了文生视频后的音频合成瓶颈，大幅降低视频创作门槛。对内容创作者、营销工具、虚拟角色等领域是直接利好。

> 原文：[The Decoder](https://the-decoder.com/flux-3-generates-videos-with-native-audio-up-to-20-seconds-long-a-first-for-black-forest-labs/)

## Anthropic 升级 Claude 语音模式：更强模型 + 任务执行

**是什么**：Anthropic 为 Claude 语音模式引入更强基础模型（传闻接近 Claude 4 级别），新增会议安排、邮件撰写、日历管理等原子化任务执行能力。

**关键点**：
- 语音交互不再仅是问答，可调用工具（如日历 API、邮件客户端）。
- 支持多轮对话中的状态保持，如“帮我明天下午三点约团队会议，会后给每人发一封邮件”。
- 目前仅面向付费用户，支持英文和部分西方语言。

**为什么重要**：这是 agentic 语音助手的重要一步。比起单纯语音聊天，能执行实际任务的语音交互更贴近生产力场景，可能会加速企业级语音助手落地。

> 原文：[TechCrunch](https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/)

## Cisco 开源小安全模型：声称在漏洞检测上超越 GPT-5.5

**是什么**：Cisco 发布一个小型开源网络安全模型（参数约 7B），宣称在代码漏洞检测、CVE 识别等任务上性能超过 GPT-5.5（更小成本）。

**关键点**：
- 模型专为安全领域微调，使用 Cisco 内部安全数据 + 公开漏洞库。
- 在真实漏洞检测 F1 分数上比 GPT-5.5 高约 8%，推理成本仅为 1/10。
- 模型完全开源（Apache 2.0），旨在鼓励社区贡献安全领域模型。

**为什么重要**：Cisco 展示了垂直领域专用小模型在特定任务上超越通用大模型的可行性。对于安全行业，这意味着企业内部可私有化部署高精度的漏洞检测模型，规避数据外泄风险。

> 原文：[The Decoder](https://the-decoder.com/cisco-bets-its-small-open-cybersecurity-models-can-outperform-gpt-5-5-at-vulnerability-detection-for-a-fraction-of-the-cost/)

## 阿里千问 Qwen-Image-3.0：文本输入长度提升 4.5 倍

**是什么**：阿里巴巴发布多模态模型 Qwen-Image-3.0，支持理解与生成图片，核心改进在于文本输入长度最大可达 32K tokens（较上代提升 4.5 倍），可处理更长的图文上下文。

**关键点**：
- 支持多图输入、图内文字识别（OCR）、图生图等任务。
- 文本长度提升使模型可分析整本漫画、长文档插图等场景。
- 已在阿里云平台提供 API。

**为什么重要**：长文本输入能力使多模态模型能处理更复杂的图文混合任务，如文档理解、长篇漫画解读。这对企业级文档处理、电商内容生成等场景有直接影响。

> 原文：[InfoQ](https://www.infoq.cn/article/jXQ5oQeOcEjLkuq2Qc0y)

——  
**结语**：今天的故事都在回答同一个问题：当大模型参数竞赛趋于内卷，效率、垂直领域和原生多模态能力是否才是真正的护城河？你更看好哪个方向？