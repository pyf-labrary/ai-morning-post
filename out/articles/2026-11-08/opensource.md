# Agent 的脚手架，开源先动手了

## 导语

今天开源板块最值得看的一条，是谷歌把 `google/skills` 放上 GitHub——为自家产品栈提供标准化的 Agent Skills。它本身不产生新能力，但意味着 Skills 这个形态正在从社区约定变成大厂的分发接口。把八条放在一起看，主线很清楚：模型权重之外，agent 与数据、权限、算力之间的中间层，正在被开源一块块补齐。这对做平台和做产品的人，比对做训练的人更重要。

## 谷歌开源 Agent Skills，把自己整个产品栈交出去

谷歌在 GitHub 发布 `google/skills`，为旗下产品与技术提供标准化的 Agent Skills，并可通过 skills.sh 安装。关键点不在"技能"数量，而在标准化的动作：把"agent 该怎样调用某个谷歌产品"写成可安装、可复用的描述文件，而不是留给每个开发者自己拼 prompt 和 API 调用。这和 MCP 走的是同一条逻辑——先定义接口，再让生态围绕接口生长。为什么重要：当 Skill 成为 agent 能力的复用单位，掌握 skill 格式与分发渠道的一方，实际上掌握了 agent 访问自家产品的默认路径。谷歌用自家栈做示范，是在争夺"agent 怎么用 Google"这个问题的默认答案。

> 原文：[GitHub](https://github.com/google/skills)

## Buoyant 开源 Kinference，给 vLLM 补上控制面

Buoyant 发布 Apache 2.0 许可的 Kinference，为 Kubernetes 上的 vLLM 提供控制面：声明式路由、KV-cache 感知的负载均衡、租户级指标。官方基准称中位 TTFT 降低 95%。这条的关键词是 KV-cache 感知——推理请求的调度如果看不见缓存落在哪个副本，重复 prefill 就是纯浪费；把缓存位置纳入路由决策，是从"能跑"到"能运营"的分界线。vLLM 单机部署早已成熟，但多副本、多租户、缓存复用这一层，此前基本靠团队自己写。95% 是厂商自己的数字，需要第三方复现；但方向没问题：推理平台的价值正在从模型服务转向调度。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/07/buoyant-kinference-open-source-inference-control-plane-kubernetes-vllm/)

## Zyphra 开源 ZYFA，AMD 上的注意力 kernel 提速

Zyphra 发布 ZYFA，一个面向 AMD Instinct MI355X 的 FP8/BF16 预填充（prefill）注意力 kernel，实测比 AMD 自家的 AITER 快 1.16–1.76 倍，且误差更低。prefill 是长上下文场景的主要算力开销，注意力 kernel 的效率直接决定单位 token 成本。这条的真正意义不在倍数，而在生态位置：AMD 硬件规格不弱，但软件栈一直是采购决策里的减分项，第三方愿意为 MI355X 写高质量 kernel，说明有人真的在用它跑训练和推理。需要克制的是，单个 kernel 的领先不等于端到端（end-to-end）吞吐领先，融合、通信、并行策略都会吃掉部分收益。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/06/zyphra-zyfa-fp8-flashattention-amd-mi355x/)

## 微软开源 VibeVoice，语音这一环开始松动

微软在 GitHub 开源 VibeVoice，定位为前沿语音 AI 项目，指向高质量语音生成与合成。语音是 agent 最自然的输入输出通道，但过去一年这一层几乎被闭源 API 把持，成本、延迟、数据出境是三个绕不开的约束。前沿级模型一旦有了开源实现，团队至少可以自建、可以压延迟、可以让音频不出内网。判断上要留一手：目前公开信息里最该先确认的是许可证条款和推理成本，而不是 demo 效果——语音模型的真实门槛往往在长音频稳定性和并发成本上，而不是单条样音的听感。

> 原文：[GitHub](https://github.com/microsoft/VibeVoice)

## 英伟达开源 auto-ontology，给 agent 建图推理层

NVIDIA 发布 auto-ontology，一个 Python 框架，作用是在已有数据之上构建语义图推理层，官方定位是提升 LLM 与 agent 工作流的可解释性与检索质量。它要解决的是 RAG 的老问题：向量检索擅长"相似"，不擅长"关系"和"多跳"，也说不清一条结论是从哪几条事实推出来的。把数据组织成图，等于给检索加了一层结构约束，也让引用和溯源变得可检查。这属于"上下文工程"从调 prompt 转向调数据建模的一个样本——如果这条路走通，未来 agent 的质量差异会更多来自数据结构，而不是模型选型。

> 原文：[GitHub](https://github.com/NVIDIA/auto-ontology)

## Cloudflare 开源安全审计技能，重点是"可验证"

Cloudflare 发布 `security-audit-skill`，把编码 agent 变成多阶段的安全审计员。它值得单独拎出来的设计是输出形态：产出可独立验证、机器可读的审计发现。安全场景对 agent 的要求和其他场景相反——不怕它少说，就怕它编。一段读起来很专业的散文式报告几乎无法验收，而结构化的发现可以逐条复核、可以进 CI、可以被下一个 agent 消费。这也是 Skills 形态的一个正面样本：把 agent 塞进有验收标准的流程里，前提是先把输出约束成机器能读的东西。

> 原文：[GitHub](https://github.com/cloudflare/security-audit-skill)

## PipesHub：给 agent 的开源上下文层

PipesHub 开源了一个面向 AI agent 的上下文层，接入 Slack、Drive、Jira、GitHub 等 50 多个数据源，提供权限感知的检索与引用能力。企业 agent 落地卡住的地方，很少是模型不够聪明，而是权限：检索结果必须继承源系统的访问控制，一次越权返回就能让整个项目被安全团队否掉。所以"权限感知"不是加分项，是准入门槛。上下文层正在变成独立品类，与 MCP、各类 connector 生态有明显重叠；开源实现的价值在于把自建成本压下来，让小团队也能从"接一个数据源"起步，而不是先造一套连接器框架。

> 原文：[GitHub](https://github.com/pipeshub-ai/pipeshub-ai)

## ToyBlocks：机器人学习缺的是基准，不是模型

AllenAI 在 Hugging Face 发布 ToyBlocks，提供一个可控环境，用于机器人学习与评测，便于复现结果、比较不同策略。机器人学习长期的问题是实验不可比：环境、初始条件、随机种子一变，两篇论文的结论就无法对话。受控环境的价值就在这里——它不提升任何单个策略的上限，但让"哪个方法更好"这个问题第一次有可讨论的答案。对具身智能这条赛道来说，降低复现成本比再刷一个 SOTA 更有长期价值，因为工程团队真正缺的是能反复试错的靶场。

> 原文：[Hugging Face](https://huggingface.co/blog/allenai/toyblocks)

## 结语

今天这八条里，七条都在做同一件事：把 agent 和真实系统之间的那一层，做成可安装、可验证、可调度的开源组件。那么问题来了——当脚手架全部开源，护城河到底落在数据、权限，还是分发？