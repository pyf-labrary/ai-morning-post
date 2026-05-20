# Google连发双子星，阿里云Agent对打

**导语**：2026年5月21日，模型发布板块迎来久违的密集轰炸。Google在I/O上同时亮出Gemini 3.5 Flash（速度4倍提升、成本减半）和全能模型Omni（支持视频生成），直奔“更快、更便宜、更多模态”而去。阿里云则用Qwen3.7-Max专攻Agent场景，意图精准锁定企业需求。如果你在选型或投资，这三款模型定调了未来半年的竞争节奏。

## Gemini 3.5 Flash：速度4倍、成本减半，即日可用

**是什么**：Google在I/O 2026上正式发布Gemini 3.5 Flash，声称推理速度提升4倍，API成本较前代降低50%，在编程和智能体（agentic）基准测试上超越上一代模型。即日起全球可用。**关键点**：速度提升直接降低了用户延迟敏感型应用的调用门槛，成本减半则可能引发新一轮价格战。**为什么重要**：对于开发者和B端客户，Flash系列本就主打低成本、高吞吐，Gemini 3.5 Flash的升级意味着更多实时对话、代码补全和Agent编排场景可以商业落地，Google试图用“性价比”挤压竞争对手——尤其是Claude和GPT-4o mini的市场空间。

> 原文：[Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

## Gemini Omni：从任意输入到视频生成，多模态再进一步

**是什么**：Google发布Gemini Omni，一个能从文本、图像、音频甚至视频输入生成任意输出内容（包括视频）的全能模型。**关键点**：它是Google多模态能力的“天花板”产品，首次实现了“输入视频→输出视频”的端到端生成，意味着用户可以直接用一段视频作为Prompt生成新视频，而不必经过文本中间态。**为什么重要**：这标志着基础模型从“多模态理解”跨入“多模态原生生成”，对游戏、短视频、虚拟制作等行业可能产生结构性冲击。Gemini Omni与Flash形成高低搭配：Flash跑量和跑敏捷，Omni探索边界。投资者应关注后续API定价——如果成本可控，它可能重定义AI内容生产流程。

> 原文：[DeepMind Blog](https://deepmind.google/models/gemini-omni/)

## 阿里云Qwen3.7-Max：Agent专长，中国企业级市场新锚点

**是什么**：阿里云发布旗舰模型Qwen3.7-Max，专门针对Agent任务（工具调用、多步推理、记忆管理等）进行优化，性能在相关基准上领先。同步升级全栈AI产品体系。**关键点**：这是国内首个明确为Agent场景设计的旗舰模型，而非通用大模型。阿里云把Agent能力作为核心卖点，侧面呼应市场上“模型同质化”的焦虑——当基础语言能力趋同，任务执行准确率才是差异点。**为什么重要**：对于企业客户，Agent是落地AI的“高频入口”。Qwen3.7-Max如果真能在实际部署中表现出更低的错误率和更稳定的上下文保持，将直接挑战海外模型在国内的生态优势。同时也暗示阿里云的模型策略从“追参数”转向“抓场景”。

> 原文：[Qwen Blog](https://qwen.ai/blog?id=qwen3.7)

## Stable Audio 3.0：6分钟歌曲，开源权重可本地运行

**是什么**：Stability AI发布Stable Audio 3.0，支持生成最长6分钟的音乐作品，同时发布小型模型版本并开放权重，允许本地部署。**关键点**：6分钟意味着从“片段生成”跨越到“歌曲级创作”，并且开放权重让音乐AI真正进入可复现、可定制的阶段。小型模型能跑在消费级GPU上。**为什么重要**：开源策略延续了Stability AI在图像领域的路线，进一步挤压闭源音乐生成工具（如MusicLM）的空间。对于BGM、游戏配乐、个人创作者，这是成本最低的AI音乐选项。但版权合规和音频质量仍是商用前的门槛。

> 原文：[The Decoder](https://the-decoder.com/stability-ai-launches-stable-audio-3-0-with-up-to-six-minute-tracks-and-open-weights/)

## Deepseek 开发代码工具 Deepseek Code，直指Claude Code

**是什么**：Deepseek正在构建类似Claude Code和OpenAI Codex的AI编程助手，内部项目代号Deepseek Code，意图进入开发者工具市场。**关键点**：目前尚无具体发布时间或demo，但此举表明Deepseek从“基础模型供应商”向“应用层工具”延伸。**为什么重要**：开发者工具是一个黏性极强的入口，如果Deepseek Code能复用其模型在代码基准上的优势（如DeepSeek-Coder系列），并在价格或本地部署上做差异化，可能威胁当前Claude Code的份额。对中国开发者市场，Deepseek Code可能成为GitHub Copilot之外的国产替代选项。

> 原文：[The Decoder](https://the-decoder.com/deepseek-wants-to-take-on-claude-code-and-openais-codex-with-deepseek-code/)

---

结语：一天之内，Google占尽风头，但阿里云和Deepseek的“Agent+工具”战术同样值得盯紧——当模型本身趋于同质，哪一家能在真实场景中少出Bug，哪一家就可能赢下企业级市场。