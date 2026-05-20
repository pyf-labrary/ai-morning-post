# Google搜索全面Agent化，AI永久在线

导语：今天最值得关注的是Google I/O 上搜索正式升级为Agent驱动——用户不再需要反复查询，而是可以创建后台代理自动监控、下单和执行任务。这是搜索从“工具”向“数字员工”的质变，也是今年AI应用层最重要的产品拐点之一。下文梳理今日8条产品动态，按重要性排序。

## Google搜索全面Agent化：AI代理永久在线执行任务

Google在I/O 2026宣布搜索升级为Agent驱动，用户可创建后台代理，设定监控数据、自动下单、定期报告等长期任务。代理持续运行，在后台感知环境变化并自主行动。这意味着搜索从“你问它答”变成“你设它做”——用户不再需要主动查询，代理替你盯盘、比价、填表。这背后依赖Gemini的推理能力和长上下文，但真正突破在于“永久在线”和“可执行”的范式切换。

> 原文：[Ars Technica](https://arstechnica.com/google/2026/05/buckle-up-google-is-set-to-remake-search-with-agentic-ai-in-2026/)

## Google发布Antigravity 2.0：独立的Agent原生平台

Antigravity 2.0作为独立桌面应用发布，提供CLI、SDK、托管执行和企业级支持，全面替代此前Gemini CLI。这是Google首个专为代理（agent）设计的原生平台：开发者可用CLI创建、调试、部署代理，SDK支持Python/TypeScript，托管服务自动处理扩缩容与持久化。对于技术团队，这意味着Agent开发门槛大幅降低——不再需要自行管理基础设施，一个命令即可上线永久运行的AI worker。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/19/google-launches-antigravity-2-0-at-i-o-2026-a-standalone-agent-first-platform-with-cli-sdk-managed-execution-and-enterprise-support/)

## Google Genie世界模型结合街景，生成可探索实景世界

DeepMind将Genie世界模型与Google街景数据结合，创造基于真实地点的交互式3D模拟。用户可进入任意街景位置，自由行走、改变视角、与物体交互。这对游戏开发、机器人训练、虚拟旅游有直接价值：开发者不用手动建模，AI自动从真实场景中生成可探索的虚拟世界。本质上，这是世界模型从演示demo走向实用产品的重要一步。

> 原文：[The Decoder](https://the-decoder.com/google-pairs-its-genie-world-model-with-street-view-to-create-explorable-ai-worlds-based-on-real-places/)

## Google发布AI智能眼镜，语音交互加持Gemini

Google推出音频智能眼镜，支持语音命令直接唤醒Gemini，可实时翻译、导航、搜索，外形与普通眼镜接近，对标Meta Ray-Ban。关键差异在于：Google眼镜默认集成Gemini Live，可进行多轮对话和跨应用操作。对开发者而言，这意味着语音交互+视觉AI（眼镜内置摄像头）的软硬件入口正在成形，应用场景从“翻译器”延伸到“AI副驾”。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/19/google-takes-a-page-out-of-metas-book-announces-new-audio-powered-smart-glasses-at-io-2026/)

## Figma 加入AI助手，自然语言驱动设计

Figma发布AI agent，用户可通过自然语言指令直接生成界面、编辑元素，并自动化重复任务（如批量改样式、生成组件变体）。这是设计工具从“手动拖拽”到“口语化操控”的转折。产品经理和设计师可通过一句话快速产出线框图，开发者可要求AI生成符合设计系统的代码片段。值得关注的是Figma强调“人工确认”环节，避免完全自动化带来的失控风险。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/20/figma-adds-an-ai-assistant-to-its-collaborative-canvas/)

## Anthropic 推出Routines for Claude Code，自动化工作流

Anthropic发布Claude Code的Routines功能：用户可录制并保存一组开发操作（如代码审查、测试生成、文件重构），之后一键重复执行。这实质上是把Claude Code从一个对话助手升级为可配置的自动化Worker。对于开发者，Routines可将高频重复的编码工作流委托给AI，同时保持对每个步骤的控制。这与Google的Agent化思路类似，但更聚焦代码场景，且强调“可回放”。

> 原文：[InfoQ中国](https://www.infoq.cn/article/pqiTGU8VMOZ1fOZh8H98)

## Google Gmail 新增AI语音搜索，对话式检索邮件

Gmail引入语音AI搜索，用户可用自然语言查找邮件，例如“帮我找出上周三和财务部关于预算的邮件”或“显示所有带附件的未读邮件”。基于Gemini，支持多轮对话和上下文理解。这是搜索入口从文本转向语音的自然延伸，也意味着Google将其核心Agent能力嵌入高频应用——收发邮件，从而提高用户粘性和数据闭环。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/19/you-can-now-talk-to-your-gmail-inbox-as-seen-at-google-io-2026/)

## Cloudflare Workflows V2 支持5万并发工作流

Cloudflare推出Workflows V2，实现确定性执行和5万并发工作流，适合大规模AI任务编排（如批量数据流水线、Agent多步骤协同）。核心升级：1）内置重试和持久化，保证每个任务不丢；2）支持条件分支和循环，可编排复杂AI agent逻辑。对于工程团队，这意味着可以用较低成本运行海量AI worker，而无需管理消息队列和状态存储。

> 原文：[InfoQ中国](https://www.infoq.cn/article/6wOv9VbhvJ7D3tJAQHJH)

结语：当搜索、设计、开发工具都开始“永久在线”地替你干活，你的下一个问题可能不是“搜什么”，而是“该让代理做什么？”