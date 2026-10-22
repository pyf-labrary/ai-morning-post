# 推理的毛利，被开源摊开了

今天开源板块最值得看的一条，是 DeepSeek 把生产级推理框架 DeepInfer 以 Apache 2.0 放了出来：单集群日吞吐 155 万亿 token、KVCache 保留 7 天，官方测算日入 2200 万美元、约 80% 毛利。这组数字的价值不在炫技，而在于它把推理的成本与毛利结构摊开给所有人看——过去这是各家私藏的账本。同一批更新里，Google 用 TorchTPU 拆 PyTorch 与 TPU 之间的桥、llm-d 1.0 统一 K8s 上的推理调度，再往下是 Cloudflare、Vercel、Anthropic 在 Agent 的决策、续跑与插件层补砖。开源的焦点，已经从「模型权重」整体迁移到「跑模型的管道」。

## DeepSeek 开源 DeepInfer：单集群日吞 155 万亿 token

DeepSeek 以 Apache 2.0 开源生产级推理框架 DeepInfer，直接给出生产环境的运行数据：单集群日吞吐 155 万亿 token，KVCache 可保留 7 天；官方测算对应日收入 2200 万美元、约 80% 毛利。

关键点有两个。一是 KVCache 保留 7 天，这个时长指向的不是短请求，而是长会话与 agentic 负载——缓存从「加速手段」变成了容量规划问题，显存与存储的配比要重新算。二是 80% 毛利这个数字被主动公开，等于给全行业的推理定价划了一条参考线。

为什么重要：推理框架长期是各家的成本中心与黑箱，现在有了可比基线。若框架层能把毛利做到这个水平，那么靠「帮你跑得更省」收溢价的中间层，空间会被显著压缩。

> 原文：[InfoQ](https://www.infoq.cn/article/NBXP966Bz3eqr6Qidvaf)

## Google 开源 TorchTPU，PyTorch 原生跑上 TPU

Google 与 Meta 联合开源 TorchTPU，为 Cloud TPU 提供原生 PyTorch 后端，取代此前的 PyTorch/XLA 路径。

关键点在于「原生」二字：绕开 XLA 这层转换桥，算子和编译路径更贴近 PyTorch 本体，迁移时的行为差异随之收窄。对使用者来说，换硬件的成本从「改代码」向「改配置」移动。

为什么重要：PyTorch 是事实标准，XLA 转换层长期是 TPU 的摩擦点，也是 Nvidia CUDA 生态护城河的一部分。把摩擦磨掉，是对 GPU 生态的正面冲击——但真正的门槛在算子覆盖度与编译器成熟度，开源只是起点，不是结论。值得注意的还有 Meta 的署名：买方在共同投资第二供应商，这是典型的议价动作。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu/)

## llm-d 1.0：K8s 原生的推理调度层

Google、Red Hat 与 IBM 联合发布 llm-d 1.0，新增多租户流控、零停机升级，以及面向 Agent 的路由能力，可在同一层统一调度 vLLM、SGLang、TPU 与 GPU。

关键点：多租户流控和零停机升级是企业采购的硬门槛，属于「不上这个就进不了生产」的功能，而非技术亮点。面向 Agent 的路由则说明负载假设在变——长会话、多轮工具调用，与一次性 completion 的调度模型并不相同。

为什么重要：推理的竞争重心正从单机吞吐转向集群调度。Kubernetes 是事实上的部署面，谁定义这一层的抽象——队列、配额、路由、升级——谁就掌握了推理工作负载的分发权。三家云与芯片背景不同的公司联合做这件事，说明没人愿意让这一层被单一方定义。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/)

## Cloudflare 开源 Clef：给 Agent 的判断装一个可审计的开关

Cloudflare 开源面向 AI 智能体的决策模型 Clef，用于在自动化流程中做可控、可审计的判断。

关键点是把「判断」从 prompt 里拆出来，做成一个独立、可单独评估的模型。散落在提示词里的策略无法被单独测试，也无法被单独追责；抽成组件之后，判断质量变成可度量项。

为什么重要：Agent 落地的主要阻力从来不是能力上限，而是责任归属——出错时要能回溯到「哪一步判断偏了」。Cloudflare 的位置在边缘网络，它来做这件事，暗示一类策略判断未来可能下沉到靠近流量的那一层，而不是全部放在应用里。

> 原文：[InfoQ](https://www.infoq.cn/article/iqCrZLLizNkRTpfo2Jrb)

## Vercel 的 durable-harness：让编码 Agent 崩溃后接着跑

Vercel 开源 durable-harness，记录每一次模型与工具调用，使 Pi、OpenCode、Claude Code、Codex 的会话在崩溃、超时或重新部署后可以继续。

关键点：durability 是编码 Agent 从演示走向日常工具的分水岭。一次二十分钟的 agent run 中途挂掉，代价是双份 token 加双份耐心，而长时间任务恰恰是编码场景的常态。

为什么重要：它把「会话状态」当成需要持久化的一等公民。这个抽象一旦被接受，Agent 运行时就会像数据库一样被讨论 checkpoint、恢复点与幂等性——重试必须安全，否则恢复比重跑更危险。工具调用带副作用，这是设计上绕不开的约束。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/21/vercel-durable-harness-crash-proof-coding-agents/)

## orca：桌面端调度一支 Agent 舰队

stablyai 开源 orca，可以在桌面、移动与远程运行时统一调度 Grok Bot、Claude Code 等多路编码 Agent，并使用用户自己的订阅额度。

关键点：自带订阅（bring-your-own subscription），不绑定单一厂商的额度体系；调度对象是「多路 Agent」而非单次会话。

为什么重要：并行跑几个 Agent 正在成为部分团队的日常，缺的不是新模型，而是一个不别扭的控制面板——谁在跑、跑到哪、卡在什么工具上。这类工具的价值最终取决于能否成为默认入口，而默认入口的争夺，通常由「少一次切换」决定。

> 原文：[GitHub](https://github.com/stablyai/orca)

## headroom：在进模型之前先把 token 榨干

headroom 在工具输出、日志、文件与 RAG 片段进入模型之前先做压缩，官方给出的测算是编码 Agent 省约 20% token，JSON 场景省 60–95%。

关键点：压缩发生在上下文入口，而非模型或提示词侧，因此对上层几乎无感，属于典型的「装上就生效」类工具。

为什么重要：上下文是 Agent 的经常性开支，压缩对账单的杠杆比等一次模型降价更直接、更可控。但压缩即丢弃，风险在于丢掉关键字段——尤其结构化数据，一个被压掉的 ID 就足以让后续调用全盘失败。这类工具能否站住，取决于它是否提供可逆或可回查的路径，而不是只报一个压缩比。

> 原文：[GitHub](https://github.com/headroomlabs-ai/headroom)

## Anthropic 开源知识工作插件库

anthropics/knowledge-work-plugins 提供一批面向知识工作者的插件，把 Claude Cowork 变成特定岗位与团队的专业助手。

关键点：是插件而非模型——不提升能力上限，只缩短「通用助手」到「我的岗位」之间的距离。

为什么重要：这是把横向能力切成纵向场景的标准做法，也是应用层圈地的路径。插件生态的黏性来自积累的具体流程，而不来自参数规模；一旦某个团队的周报、审阅、检索都长在这些插件上，替换成本就不再由模型能力决定。对所有做垂直 Agent 的团队来说，这是一次来自平台方的位置挤压。

> 原文：[GitHub](https://github.com/anthropics/knowledge-work-plugins)

## 结语

今天这八条里，七条在修管道而不是造模型：推理框架、硬件后端、调度层、状态持久化、上下文压缩。留一个问题给各位：当管道全部开源且性能可比，链条上还能收钱的那一环，究竟在哪？