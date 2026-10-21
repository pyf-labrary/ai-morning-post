# 价格战没停，模型开始比速度和落地

## 导语

MiniMax 把 428B 参数的 M3.1 Flash 定到 $0.15/$0.60 每百万 tokens，还带 1M 上下文与 10 月 23 日的权重开放——这个价格已经很难再被当作差异化优势。同一天里 Mercury 3 用扩散架构喊出 1068 tokens/秒，Mistral 把语音做成全栈，Meta 拉苹果做本地运行：竞争轴线正从“每 token 多便宜”转向“多快、能不能落地到具体场景”。降价是入场券，不再是卖点。

## MiniMax M3.1 Flash：428B MoE，价格再探底

MiniMax 发布 M3.1 Flash，428B 参数 MoE、约 23B 激活、1M 上下文，API 定价 $0.15/$0.60 每百万 tokens，官方称其在 Agent 类任务上居国产模型首位，权重 10 月 23 日放出。

关键点在组合而非单点：MoE 把激活参数压到 23B，长上下文撑住 agentic 任务的多轮工具调用与长文档输入，价格则直接压到行业底部区间。加上权重开放，团队可以在“调 API”和“自己部署”之间做成本比较——这对有合规要求或需要微调的企业是实质选项。

值得留意的是“Agent 类任务第一”这类自评口径，缺少第三方复现前只能当方向参考。真正要验证的是长上下文下的有效召回率与工具调用稳定性，这两项决定它在生产环境里能不能省钱，而不只是看起来便宜。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/19/minimax-m3-1-flash-release/)

## Mercury 3：扩散式 LLM 跑到 1068 tokens/秒

Inception 发布扩散式大模型 Mercury 3，宣称推理速度达 1068 tokens/秒、支持 1M 上下文，并在其自评的 12 项基准中有 8 项领先 GPT-6 Luna 与 Claude Haiku 5.5。

扩散式语言模型的核心差异在解码方式：不走逐 token 自回归，而是并行去噪生成，理论上把延迟曲线压平。1068 tokens/秒这个数字如果能在真实负载下站住，对实时字幕、语音对话、代码补全这类“等待即流失”的场景是结构性变化。

需要克制的是基准口径——12 项里 8 项领先，且是厂商自评，对比对象还选了偏轻量的 Haiku 档位。扩散模型在长文本一致性与精确指令遵循上的历史短板，也不是速度能自动解决的。下一步该看的是第三方在 agentic 长链任务上的复测。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/19/inception-mercury-3-diffusion-llm/)

## GPT-6 补课 COBOL 与 Fortran

OpenAI 称 GPT-6 显著提升了对 COBOL、Fortran 等遗留语言的代码理解与迁移能力，目标指向企业现代化改造中长期存在的老系统维护需求。

这是个不性感但极贵的方向。金融、保险、航空、政府系统里堆积着几十年 COBOL 代码，懂的人正在退休，替换成本高到很多项目选择不动。模型若能读懂并做语义级迁移，切入的是预算充足、痛点明确的市场——比通用编程榜单更接近付费场景。

风险同样明显：遗留系统缺少测试覆盖，迁移错误的代价不可逆。所以这类能力真正落地时，瓶颈更可能在验证工具链和人来把关的环节，而非模型本身的理解力。对做企业服务的团队，这是值得提前押注的切口。

> 原文：[The Decoder](https://the-decoder.com/openai-says-gpt-6-is-much-better-with-legacy-programming-languages-such-as-cobol-and-fortran/)

## Mistral Voxtral 3：把语音做成一条完整流水线

Mistral 推出 Voxtral 3，将语音识别、推理与语音合成打包为可实时“听—想—说”的全栈语音 Agent 方案。

过去做语音 Agent，团队要自己拼接 ASR、LLM、TTS 三段，串联带来的延迟、打断处理与话轮管理往往是体验崩坏的根源。Voxtral 3 把三段收进同一套栈，卖的是端到端延迟和一致性，而不是单个环节的指标。

这是欧洲厂商少见的平台化动作：不跟前沿模型硬拼参数，而是占住“实时交互”这一层。挑战在于客户是否愿意把语音链路整体交给一家，以及它在多语种、口音与嘈杂环境下的实际鲁棒性——这块的评测比文本难得多。

> 原文：[The Decoder](https://the-decoder.com/mistral-ai-launches-voxtral-3-a-full-voice-agent-stack-that-listens-thinks-and-talks-in-real-time/)

## Meta 开源 Muse Spark，还拉上苹果做本地运行

Meta 发布开源模型 Muse Spark，同时宣布与苹果合作，让模型能在本地设备上直接运行。

开源模型的竞争早就不是榜单，而是分发与运行位置。拉上苹果意味着模型可能进入设备侧推理路径：隐私敏感任务不出端、无网络可用、按次调用零边际成本——这三条正好对上手机端助手的核心约束。

难点在工程而非公告：端侧内存、功耗、量化后的能力折损，以及苹果生态对第三方模型的开放程度，都会决定这件事是发布会句子还是真实产品。若成立，最先被冲击的是云端小模型 API 的轻量调用场景。

> 原文：[Stratechery](https://stratechery.com/2026/muse-spark-open-meta-apple-thin-and-thick/)

## ElevenLabs 加码 speech-to-speech

ElevenLabs 发布两款面向实时 AI 对话的 speech-to-speech 模型，主打低延迟的自然语音交互。

speech-to-speech 与“ASR→文本→TTS”的级联方案差别在于：不把语音先压成文本，语气、停顿、情绪这些副语言信息得以保留，对话听起来更像人。代价是可控性与可观测性下降，出错时也更难定位。

这一步让 ElevenLabs 与 Mistral 这类全栈玩家正面相遇。它的优势是语音数据与产品经验的积累，短板在推理层——语音体验的上限越来越取决于“想”的那一段，而这正是它在补的部分。

> 原文：[The Decoder](https://the-decoder.com/elevenlabs-releases-two-new-speech-to-speech-models-designed-for-real-time-ai-conversations/)

## Claude 新模型动向：调试不再套模板

中文社区曝光 Claude 新模型动向，称其在代码调试上不再局限于既有思路，能够跳出思维定势，做到治标也治本地定位问题。

需要说明：目前是社区曝光，非官方发布，能力描述缺乏可复现的评测支撑，宜当作信号而非结论。

之所以值得关注，是因为“修 Bug”是 agentic coding 真正的瓶颈。生成代码已经不难，难的是在陌生仓库里提出假设、证伪、再提出下一个假设——按固定套路走的模型会反复在同一个错误方向上打转。若模型真能主动跳出既有假设，价值不在写得更快，而在减少人类兜底的次数。这也是编码 Agent 从“能用”到“敢放权”的分界线。

> 原文：[量子位](https://www.qbitai.com/2026/10/504314.html)

## 可灵 4.0：视频生成开始补音频课

快手可灵 AI 升级至 4.0，新增立体声音频、多语种口型同步，并推出更轻量的 Flash 版本。

口型同步与立体声指向同一件事：视频生成正从“画面可用”走向“成片可用”。多语种口型意味着同一段素材可以低成本本地化投放，这对营销与短剧类客户是直接的成本项；而 Flash 版本则是把生成成本分层，覆盖批量试错的需求。

这个方向上的竞争已经不只是画质，而是音画一致性与可控性的工程细活。短板也在这里：口型与音频的对齐在近景、遮挡、快语速下最容易露馅，真实生产环境的容错率远低于演示视频。

> 原文：[The Decoder](https://the-decoder.com/kling-ai-drops-version-4-0-with-stereo-audio-multilingual-lip-sync-and-a-lighter-flash-variant/)

## 结语

今天的八条里，降价只占一条，其余都在抢“更快、更近、更专用”的位置。留给读者一个问题：当 1M 上下文卖到 $0.15，你所在的产品里，还有哪部分成本是真正值得为之付费的？