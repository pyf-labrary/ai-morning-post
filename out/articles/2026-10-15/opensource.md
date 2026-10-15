# Agent 技能像 npm 一样分发

百度把长文档 OCR 做成了"一发式"：Unlimited-OCR 宣称进入长视野一次解析阶段，这比参数比拼更贴近真实文档流的痛点。同一批更新里更值得注意的是 Vercel Labs 的 npx skills——Agent 技能开始有包管理器的样子了。当"能不能跑"不再是问题，谁能定义技能的封装与分发格式，谁就掌握了下一层入口。今天的 8 条更新，基本都落在这条线上。

## 百度开源 Unlimited-OCR：把长文档解析压成"一次"

百度开源 Unlimited OCR Works，定位长程（long-horizon）文档解析，宣称进入"一发式"长视野解析时代。

关键点在"一次"：传统 OCR 流水线要切页、检测、识别、拼接，长文档上误差逐级累积，跨页表格和标题层级最容易丢；Unlimited-OCR 把这条链路压成单次解析，理论上能保住全局结构。但宣称之外，版面还原、公式、多语言混排的实测效果仍需自己验证。

为什么重要：文档解析是 RAG 与 agentic 工作流的入口环节，输入有多脏，后面检索和推理的上限就有多低。模型能力趋同时，谁能把长文档这类最难啃的输入做干净，谁就更接近企业文档场景。做知识库、合同与票据处理的团队，值得直接拉下来跑一遍。

> 原文：[GitHub - baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

## Vercel 开源 npx skills：Agent 技能有了分发层

vercel-labs 发布开放 Agent 技能工具 skills，核心是一条 `npx` 命令即可安装和分发 Agent 技能包。

关键点是"包"这个抽象：技能被封装成可版本化、可依赖、可复用的单元，而不是散落在各家 prompt 模板和一次性脚本里。这和 npm 早期解决 JavaScript 依赖问题的路径很像——先有分发协议，才可能有生态。

为什么重要：过去一年 agent 竞争集中在模型能力，技能的分发、发现与版本管理始终没有标准答案。Vercel 用 npx 这个已进入开发者肌肉记忆的入口切入，迁移成本极低，也贴合它一贯的部署叙事。风险同样清楚：能否成为事实标准，取决于有多少技能愿意按这个格式打包，而非工具本身多优雅。要评估的话，先看它的包格式，再看命令行。

> 原文：[GitHub - vercel-labs/skills](https://github.com/vercel-labs/skills)

## APUS 开源 Reflex Agent：主打速度与"无限上下文"

APUS AI 开源了 Personal Agent 产品 Reflex Agent，官方口径是比 Claude Code 快 3 倍，并具备真正无限上下文。

两个卖点恰好是当前 coding agent 最常被抱怨的短板：等待时间长，长任务中途丢状态。但"快 3 倍"与"无限"都是厂商自述，公开信息里没有说明测试条件——任务类型、模型后端、上下文规模都未交代，读者宜把它们当作待验证的宣称，而不是结论。

为什么重要：agent 的差异化正在从"能不能用"转向"用起来累不累"。响应速度和上下文管理直接决定一个 agent 能否被长期挂在后台跑。开源的价值在于它的上下文策略与调度实现可被审查，这比产品页上的对比图有信息量。建议关注它如何做上下文压缩与检索，而不是跑分数字。

> 原文：[量子位 - APUS 开源 Reflex Agent](https://www.qbitai.com/2026/10/503165.html)

## NVIDIA 开源 PersonaPlex：给全双工语音加上"人设"

NVIDIA 开源 PersonaPlex，面向全双工（full-duplex）对话语音模型，提供声音与角色控制能力，权重已在 HuggingFace 发布。

关键点有两个：全双工意味着模型可以边听边说，而不是 ASR → LLM → TTS 的串行三段式；在此之上，PersonaPlex 增加了声音与角色两个控制维度，让同一底座稳定扮演不同说话人，而不必每换一个音色就换一套模型。

为什么重要：语音交互的瓶颈正从"听得准"转向"像不像在跟人对话"。打断、抢话、语气一致性，都是三段式流水线很难做好的。NVIDIA 把权重直接放上 HuggingFace，等于替语音 agent 团队省掉了最贵的自研环节。接下来值得对比的是它与自研 TTS 方案在延迟、音色稳定性上的差距。

> 原文：[GitHub - NVIDIA/personaplex](https://github.com/NVIDIA/personaplex)

## SGLang 推出 sglang-omni：补齐音频侧推理服务

SGLang 生态新增 sglang-omni，一个面向 TTS、ASR 与统一多模态模型的高性能推理服务框架。

关键点：SGLang 此前的主场是 LLM 推理调度，音频侧一直是空白。sglang-omni 把 TTS、ASR 与多模态统一进同一套服务框架，意味着语音链路可以复用已有的批处理、缓存和调度能力，不必再为语音单独维护一套服务。

为什么重要：语音 agent 落地时的摩擦往往不在模型，而在工程——两套服务、两套扩容逻辑、两套监控，运维成本翻倍。把音频推理纳入统一的 serving 层是务实的一步。对已经在用 SGLang 跑 LLM 的团队，这是低成本扩展语音能力的入口；但动手前先确认它覆盖的模型清单是否匹配自己的技术栈。

> 原文：[GitHub - sgl-project/sglang-omni](https://github.com/sgl-project/sglang-omni)

## AirLLM：4GB 显卡跑 2.8T 参数模型

AirLLM 通过分层（layer-wise）加载，让超大规模模型在消费级显存上完成推理，项目继续在 GitHub 趋势榜走热。

关键点在于空间换时间：模型按层拆分，逐层从内存或磁盘调入显存，用完即释放，峰值显存只与单层规模相关，而非全部参数量。所以"4GB 显存跑 2.8T 参数模型"成立，但它衡量的是可行性，不是可用速度。

为什么重要：它降低了大模型本地实验的门槛，让没有 A100/H100 的个人开发者也能观察超大模型的行为。要进入生产环境，还得看吞吐与延迟的实测数字。把它当作调研和验证工具而非部署方案，预期会更合理。

> 原文：[GitHub - lyogavin/airllm](https://github.com/lyogavin/airllm)

## VoiceStudio：完全本地的 ElevenLabs 替代

VoiceStudio 是开源、完全本地运行的语音工作台，定位 ElevenLabs 的替代方案，覆盖声音克隆、音色设计、视频配音、听写、转写与有声书制作，宣称支持 646 种语言。

关键点：一是"本地"，音频素材不出机器，这对配音、医疗、法律等对素材敏感的行业是硬需求；二是"全流程"，从克隆到成片配音在一个工具内完成，而不是拼三四个开源项目。

为什么重要：语音合成过去一年由云端 API 主导，成本与合规是两座山。本地方案把边际成本压到接近电费，同时绕开数据出境问题。代价也清楚：推理依赖本地算力，音质与稳定性通常落后云端旗舰一段。要不要迁移，取决于你的场景里"像不像"和"数据在谁手里"哪个更重要。

> 原文：[GitHub - debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

## pg_vectorsearch：Timescale 挑战 pgvector 的索引

Timescale 推出 pg_vectorsearch，一个 Postgres 向量检索索引，宣称速度超过 pgvector 的 IVFFlat 与 HNSW 两种主流索引。

关键点：pgvector 长期是 Postgres 做向量检索的默认答案，其索引在召回率与构建开销上的取舍一直是讨论焦点。Timescale 以时序数据库出身切入这一领域，宣称速度领先——但向量检索的对比必须连同召回率、数据集规模、索引构建时间一起看，单看"更快"容易失真。

为什么重要：向量检索正从独立数据库回流到 Postgres。对已经在 Postgres 上跑业务数据的团队，能在同一套事务与备份体系里做向量搜索，比引入专用向量库省太多事。这类项目值得盯，但选型前先在自己的数据上跑一次 recall 对比。

> 原文：[GitHub - timescale/pg_vectorsearch](https://github.com/timescale/pg_vectorsearch)

今天这 8 条解决的多是"用不起来"，而不是"跑不动"。当分发格式、显存门槛和数据归属开始决定选型，你栈里下一个被开源替换掉的组件会是谁？