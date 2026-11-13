# AWS 让 AI 写了 200 个云服务

## 导语

今天开源板块最值得看的一件事，是 AWS 用自主 AI agent 生成了 `aws-emulator` 的全部代码：438 个 API 模型、200 多项服务，发布时 42857 项保真测试通过率 56.6%。「AI 写了 200 个服务」是噱头，「56.6%」才是信息量——它把「agent 能不能大规模产出可用代码」这个问题，第一次量化地摆到了台面上。剩下的几条也沿着同一条暗线展开：Codex Security、OpenBot 1.0、Agent Skills 在补「信任与治理」，PyTorch on TPU、LiteRT 在拆「硬件适配」这堵墙。开源正在从「放出代码」转向「放出可被 agent 消费的接口」。

## AWS 用 AI agent 生成 200 多项云服务模拟器

AWS 发布 `aws-emulator`，采用 CC0 协议，基于 438 个 API 模型在本地复刻 200 多项 AWS 服务。关键点有两个：一是全部代码由自主 AI agent 编写，二是发布时 42857 项保真测试通过率 56.6%。本地云模拟解决的是一类具体问题：离线开发、CI 里跑集成测试不该依赖真云。过去这类项目靠人工逐个服务补齐，覆盖面永远是短板；这次用 API 模型驱动批量生成，把广度一次性拉满。但 56.6% 的保真度意味着近一半行为与真实云不一致，把它当测试替身要防假阴性和假阳性。更值得跟踪的是方法论：模型驱动生成 + 保真测试作验收，这套闭环能不能把 56.6% 推到 90%，比 200 这个数字更能说明 agent 的工程价值。

> 原文：[GitHub](https://github.com/aws/aws-emulator)

## OpenAI 开源 Codex Security，找漏洞也改漏洞

OpenAI 把 Codex Security 的 CLI 与 TypeScript SDK 开源，并同步上架 npm，能力覆盖漏洞的自动发现、验证与修复。「验证」这个词比「发现」更重要——安全扫描工具最大的成本从来不是漏报，而是误报淹没工程师。把它做成 CLI 和 SDK 而非只留在产品内，意图很清楚：进 CI 流水线。但自动修复留下了未解的问题：补丁由谁 review、修复引入回归谁负责。实际用法上，先把它当高召回扫描器加建议补丁，跑在非生产仓库，而不是一上来就设成阻断门禁。

> 原文：[GitHub](https://github.com/openai/codex-security)

## CopilotKit 开源 OpenBot 1.0，给 AI 同事上审计

OpenBot 1.0 采用 MIT 协议、支持自托管，企业自带模型与 agent。它真正的差异点不在「AI 同事」这个概念，而在约束：每个 Bot 动作都必须通过策略校验，并写入审计日志。企业部署 agent 的卡点通常不是能力不足，而是不可问责——谁批准了这次操作、出了事查哪条记录。自托管加自带模型则解决数据出域问题。接下来的观察点是策略引擎的表达力够不够覆盖真实权限模型，以及审计日志能否支撑事后追责而不只是留痕。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/12/copilotkit-openbot-1-0-open-source-ai-coworker/)

## PyTorch 原生跑上 TPU，选框架和选硬件解耦

谷歌打通了 PyTorch 对 TPU 的原生支持，开发者不必再绕道 JAX 或 XLA 适配层，社区的反应是「早该如此」。这件事的分量在于它拆开了一个长期绑定的决策：过去选 TPU 往往意味着迁移训练栈，迁移成本高到足以抵消硬件本身的价格优势。原生支持把这道成本削平后，TPU 的性价比才第一次可以和其他加速器放在同一张表上比。但要确认「原生」到什么程度——算子覆盖、分布式训练、调试工具链，这三项决定它是生产可用还是 demo 可用。

> 原文：[InfoQ](https://www.infoq.cn/article/Fikt82HLToqb6ZANB2xj?utm_source=rss&utm_medium=article)

## Anthropic 公开 Agent Skills 实现代码

Anthropic 开源了 Claude 的 Agent Skills 实现仓库，供开发者参照该标准为自己的 agent 复用技能模块。agent 生态当下最缺的不是模型能力，而是可移植的中间层：技能包能不能跨框架流转，决定生态是碎片化还是形成分工。Anthropic 主导的标准天然带自家偏向，是否被其他模型厂商采纳是它能否成立的关键。务实建议是把它当参考实现读，理解技能描述、加载与调用的契约设计，而不是当稳定 API 直接依赖。

> 原文：[GitHub](https://github.com/anthropics/skills)

## shadcn 的 improve：强模型审，弱模型写

`improve` 是一个 agent 技能：用最强的模型审计代码库并产出实施计划，再交给更便宜的模型执行，目的是压低高质量重构的成本。这是 token 经济学在工程侧最朴素的一次落地——把「想」和「做」分配给不同价位的模型。它的隐患也很明确：计划与执行之间的信息损耗。便宜模型偏离计划时，靠谁发现？实践上必须给执行阶段配强校验（测试、lint、类型检查），否则省下的推理成本会以 review 成本的形式还回去。这个思路对所有 agent 工作流都成立，不止重构。

> 原文：[GitHub](https://github.com/shadcn/improve)

## 谷歌 LiteRT Tensor API，降低端侧模型改造门槛

谷歌发布 LiteRT Tensor API，用于在端侧构建、定制与优化机器学习模型，面向移动与嵌入式设备。端侧模型的真实瓶颈常常不是算力，而是「改不动」：量化、算子支持、内存布局每一项都需要专门知识，导致多数团队只能用预训练模型，做不了设备级定制。把它 API 化，等于把硬件适配的复杂度收进框架层。这和 PyTorch 原生支持 TPU 是同一条线——把「适配硬件」从应用团队的活变成框架的活。

> 原文：[InfoQ](https://www.infoq.cn/article/joYjCTbwWFSkbACK5lje?utm_source=rss&utm_medium=article)

## Meta 开源 astryx，设计系统开始面向 agent

Meta 开源设计系统 astryx，强调完全可定制，并且面向 agent 使用场景：让自动化工具也能消费和生成一致的界面组件。这个定位点出了一个正在发生的变化——设计系统过去只服务人类开发者，现在还要服务 agent，意味着组件需要机器可读的契约：属性、语义、变体约束都得显式化，不能靠默契。目前「agent-ready」的设计系统项目多、共识少，astryx 是否被主流工具链采纳，比它自身的组件数量更值得看。

> 原文：[GitHub](https://github.com/meta/astryx)

## 结语

今天这 8 条里，大半主角都不是模型本身，而是让模型被信任、被复用、被问责的那层壳。留一个问题：56.6% 保真度的云模拟器，你会放进 CI 吗？