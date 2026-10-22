# 笔记本上的编码模型，开始自己造自己

今天模型发布板块最该看的是 Recursive 的 Flint：总参数 40B、推理只激活 2.5B 的开源编码模型，SWE-bench Verified 报 74.2%，在 M4 Pro 上跑到 125+ tok/s。把它和后面几条放在一起看，会发现发布的重心正在从「谁的能力更强」转向「同样的能力要花多少延迟、多少成本、离数据多远」。另一个细节更值得留意：Recursive 称 Flint 的大部分构建过程由自家 AI 研究系统参与。自我进化开始出现在产品说明里，而不只是论文标题里。

## Recursive Flint：把 74.2% 装进一台笔记本

Recursive 发布 Flint，Apache 2.0 开源，40B 总参数的 MoE，推理时仅激活 2.5B；官方给出的 SWE-bench Verified 成绩为 74.2%，M4 Pro 上达到 125+ tok/s。

三个数字叠在一起才有了意义。激活参数小，显存与延迟可控，本地常驻成为可能；74.2% 落在云端主力编码模型的区间，说明「能跑」和「能用」的差距在收窄；Apache 2.0 则打开了企业内网部署与二次改造的门。Recursive 同时表示，Flint 的大部分构建由自家 AI 研究系统参与。

为什么重要：编码 agent 的部署形态可能出现分工，云端大模型负责规划与评审，本地小模型负责读代码、改文件、跑测试，代码不出内网。而「AI 参与造模型」若真成立，迭代周期和成本结构都要重写。只是目前披露的颗粒度还不足以判断，这是方法论还是一次叙事包装。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/)

## MiniMax M3.1 Flash：Agent 榜第一，成本低 88 倍

MiniMax 新版本 M3.1 Flash 在 Agent 类任务上冲到国产模型首位，官方称其推理成本比 Claude Opus 5.5 低约 88 倍，多家中文媒体已跟进实测。

关键点在「Agent 类任务」这个限定词。Agent 的成本结构和聊天完全不同：一次任务要经历多轮工具调用、长上下文回填和失败重试，token 消耗是对话的数倍到数十倍，单位 token 价格会被放大成单位任务成本。88 倍这个数字来自厂商口径，需要独立复现，但方向是清楚的。

为什么重要：agentic 产品的单位经济模型一直卡在成本上，能否把单次任务的推理开销压到用户愿意付的价格以下，决定了这类产品是 demo 还是生意。竞争指标正从榜单分数转向「跑完一个任务花多少钱、多少秒」，这比排名对做产品的人更有参考价值。

> 原文：[InfoQ](https://www.infoq.cn/article/7Twa7KBWIzi8JGOdVwCK)

## Mistral Voxtral 3：转写、TTS 和语音 Agent SDK 一起给

Mistral 这次放出的是一组组件：3 个转写模型、1 个 TTS 模型，以及一个基于 LiveKit 的语音 Agent SDK。其中 Voxtral Small Transcribe 3 在 Artificial Analysis 的转写排名中位列第三。

关键点不在单个模型，而在打包方式。语音 agent 的真实瓶颈很少是识别准确率，而是端到端延迟、打断处理和实时音频传输的衔接。直接把 LiveKit 集成进 SDK，等于替开发者干掉了「模型接进通话链路」这段最脏的活。

为什么重要：语音正在成为 agent 的主要入口之一，这一层的竞争已经不是比谁转写更准，而是比工程栈的完整度。选型时要问的问题也变了：不是哪个模型分数高，而是哪套方案能把首字延迟和打断体验做到可用。排名第三意味着它不是最强的那个，但可能是最省事的那个。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/20/mistral-voxtral-3-speech-models-voice-agent-sdk/)

## Inception Mercury 3：用扩散路线换延迟

Inception 称其扩散式（diffusion）模型 Mercury 3 在多项任务上超过 GPT-6 Luna 与 Claude Haiku 5.5，同时等待时间只有后者的一小部分。

看点在于路线。主流大模型是自回归逐 token 生成，延迟随输出长度增长；扩散式语言模型并行去噪，理论上能把生成时间压到与长度弱相关。这是「等待时间只有一小部分」这一说法的技术来源。

为什么重要：如果低延迟成立且质量不塌，受益的是对交互节奏敏感的场景，语音对话、实时代码补全、交互式 agent——在这些地方，200ms 和 2s 是两种产品。但需要保留判断：以上均为厂商自述，尚无第三方复现；扩散语言模型在长文本连贯性和工具调用上的历史表现并不好。这条更适合进「待验证清单」，而不是当作今天的结论。

> 原文：[The Decoder](https://the-decoder.com/inceptions-mercury-3-diffusion-model-claims-to-beat-gpt-6-luna-and-claude-haiku-5-5-at-a-fraction-of-the-wait/)

## IBM Granite Speech 5.0：转写之外，补上「谁说的」

IBM 将 Granite Speech 更新到 5.0，在转写、翻译以及说话人与属性溯源的准确性上做了提升，同时加快了推理速度。

关键点是「溯源」。多数开源语音模型解决的是「说了什么」，企业场景还要回答「谁说的」：会议纪要要区分发言人，客服录音要能审计，合规场景要能回溯。把这部分做进模型而不是外挂管道，能减少集成环节的信息损失。

为什么重要：语音数据是企业内网里最敏感的一类，开源权重加本地部署是刚需。IBM 这条线的竞争力不在榜单分数，而在能否进入受监管行业的采购清单。转写准确率提升几个点是加分项，可溯源性才是准入项。

> 原文：[Hugging Face Blog](https://huggingface.co/blog/ibm-granite/granite-speech-5)

今天这五条里有四条在回答同一个问题：同样的能力，能不能更便宜、更近、更快地拿到。也许该换个指标看发布，不再是榜首分数，而是跑完一个真实任务要花多少钱、多少秒。