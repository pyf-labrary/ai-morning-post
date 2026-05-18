# 马斯克败诉，英伟达 CPU 交付，AI 公司格局生变

导语：今天最值得关注的是马斯克对 OpenAI 的 1340 亿美元诉讼被陪审团两小时驳回，法庭实际上认可了 OpenAI 从非营利转向商业化的合法性。与此同时，英伟达 Vera CPU 首次交付给顶尖 AI 实验室，标志着 GPU 巨头正式切入 CPU 战场；而 Anthropic 不仅收购了开发工具公司 Stainless，还计划向全球金融监管机构简报 Claude 发现的漏洞——AI 公司正在从“卖模型”走向“卖基础设施+安全服务”。

## 马斯克诉 OpenAI 败诉：1340 亿诉讼两小时驳回

**是什么：** 陪审团一致裁定马斯克对 OpenAI 的诉讼败诉，认为其未在合理期限内起诉，法官随即确认判决。该诉讼最初指控 OpenAI 及其 CEO Sam Altman 背离了创办时的非营利使命，索赔金额高达 1340 亿美元。

**关键点：** 陪审团仅用两小时就达成一致，这通常意味着案件事实清晰、法律依据薄弱。马斯克声称 OpenAI 从“为人类开发生成式 AI”的慈善组织变成了“微软的利润机器”，但法院未能采信。

**为什么重要：** 此判决为 OpenAI 的商业化路线提供了法律背书，也意味着其他试图以“使命偏离”为由挑战 AI 公司的诉讼将更难成立。OpenAI 后续可能加速 IPO 或更大规模融资，而马斯克旗下 xAI 与 OpenAI 的竞争将转入产品层面。

> 原文：[Ars Technica](https://arstechnica.com/tech-policy/2026/05/elon-musk-loses-trial-accusing-sam-altman-openai-of-stealing-a-charity/)

## OpenAI 与 Dell 推出企业级 Codex 部署方案

**是什么：** OpenAI 与戴尔达成合作，将 AI 编码助手 Codex 带入混合云和企业本地环境，企业可以在自己的数据中心或私有云中运行 Codex，无需将代码或数据发送到 OpenAI 的公共 API。

**关键点：** 此方案侧重于安全性、数据驻留和与现有 DevOps 工具的集成，目标客户是金融、医疗、国防等对监管敏感的行业。戴尔负责提供硬件（服务器、存储）和部署服务，OpenAI 提供模型和 API 网关。

**为什么重要：** 这是 OpenAI 继 ChatGPT Enterprise 之后，在垂直场景中推进“私有化部署”的关键一步。Codex 原本是编程辅助工具，将其落地到混合云可以大幅降低企业采用门槛，同时让戴尔在 AI 时代重拾硬件话语权。

> 原文：[OpenAI](https://openai.com/index/dell-codex-enterprise-partnership)

## 英伟达 Vera CPU 交付给顶级 AI 实验室

**是什么：** NVIDIA 宣布其首款自研 CPU——Vera——已开始向 Anthropic、OpenAI、SpaceXAI 和 Oracle Cloud 等客户交付。Vera 基于 ARM 架构，专为 AI 训练和推理工作负载优化。

**关键点：** 英伟达此前主要提供 GPU（如 H100/B100）和网络设备，Vera 是其在 CPU 市场的首秀。官方称它能在同样功耗下提供 2.5 倍于现有 ARM 服务器的性能，尤其擅长数据预处理和模型分发任务。

**为什么重要：** 英伟达正在从“GPU 供应商”转变为“全栈 AI 基础设施公司”。Vera 的交付意味着英伟达可以直接与 Intel Xeon 和 AMD EPYC 竞争，更重要的是，它能让生态绑定更紧密——客户可以选择“NVIDIA GPU + Vera CPU”的单一架构，简化采购和运维。

> 原文：[NVIDIA Blog](https://blogs.nvidia.com/blog/vera-cpu-delivery/)

## Anthropic 收购开发者工具公司 Stainless

**是什么：** Anthropic 收购了纽约初创公司 Stainless，该公司专门为 API 提供 SDK 自动生成和维护服务，客户包括 OpenAI、Google、Cloudflare 等。

**关键点：** Stainless 的工具体系可以自动创建 Python、TypeScript、Java 等语言的 SDK，并持续跟踪 API 更新。收购后，Stainless 团队将加入 Anthropic，专注于改善 Claude API 的开发者体验。

**为什么重要：** 这是一个典型的“倒买掉铲子”策略——Stainless 曾经是 OpenAI 和 Google 的供应商，现在被竞争对手收购，意味着 Anthropic 不仅获得了成熟的技术能力，还切断了对手的一部分基础设施。开发者体验成为 AI 公司争夺生态的关键战场。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/)

## Anthropic 将向全球金融监管机构简报 Claude 发现的漏洞

**是什么：** 通过名为 Project Glasswing 的内部安全项目，Claude 模型在分析金融系统（如交易平台、清算网）时发现了多项漏洞。Anthropic 计划近期向全球金融监管机构进行简报。

**关键点：** 这些漏洞并非常见软件 bug，而是系统级设计缺陷，可能被用于洗钱、操纵市场或引发系统性风险。Claude 通过模拟攻击路径和审查协议文本实现了主动发现。

**为什么重要：** “AI 发现金融漏洞”正在从概念走向实际应用。Anthropic 主动与监管合作，既展示了 Claude 在安全审计方面的能力，也为自己树立了“负责任 AI”的形象。未来金融监管机构可能要求模型厂商定期提交漏洞报告。

> 原文：[The Decoder](https://the-decoder.com/anthropic-to-brief-global-financial-regulators-on-cyber-flaws-found-by-claude-mythos/)

## AI 初创公司年收入 800 亿美元，但集中度惊人

**是什么：** 一份行业报告显示，2026 年全球 AI 创业公司总收入将达到 800 亿美元，但其中约 95% 由 Anthropic 和 OpenAI 两家贡献。

**关键点：** 除了这两家巨头，其他 AI 公司的收入规模几乎可以忽略不计，二级梯队（如 Cohere、Mistral、AI21 Labs）合计仅占约 5%。收入结构高度集中，意味着资本和人才继续向头部聚集。

**为什么重要：** 800 亿美元的总盘子说明 AI 确实创造了巨大的商业价值，但集中度如此之高，意味着大多数 AI 初创公司可能面临“要么被收购，要么转型做垂直应用”的结局。对投资人而言，依赖通用模型 API 的薄钱包应用风险极高。

> 原文：[The Decoder](https://the-decoder.com/ai-startup-revenue-hits-80-billion-but-anthropic-and-openai-take-almost-all-of-it/)

## SandboxAQ 将药物发现模型引入 Claude 平台

**是什么：** SandboxAQ（从 Alphabet 分拆的 AI 公司）将其药物发现 AI 模型集成到 Anthropic 的 Claude 平台中，科学家可以通过自然语言对话方式来运行复杂的生物计算任务，无需底层编码技能。

**关键点：** SandboxAQ 的模型此前需要用户具备计算化学或高性能计算背景才能使用；现在通过 Claude 的对话界面，药物化学家可以直接说“模拟这个分子与靶点的结合能”，而不必写 Python 脚本。

**为什么重要：** 这标志着“AI for Science”正在从“专业工具”走向“自然语言驱动”。SandboxAQ 选择 Claude 而不是自己的 UI，说明他们更看重模型的理解与对话能力，而非自己造轮子。未来更多垂直行业 AI 工具可能被集成到通用助手里。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/18/sandboxaq-brings-its-drug-discovery-models-to-claude-no-phd-in-computing-required/)

## 新纪元能源 670 亿美元收购道明尼，瞄准 AI 电网需求

**是什么：** 美国最大公用事业公司新纪元能源（NextEra Energy）以 670 亿美元收购道明尼能源（Dominion Energy），整合后将成为全美最大的电网运营商。交易明确是为了应对 AI 算力设施激增的电力需求。

**关键点：** AI 数据中心耗电量正在爆发式增长，多家科技公司抱怨电网老旧、审批慢。新纪元能源计划利用此次收购建设专供数据中心的高压输电线路，并加快可再生能源并网进度。

**为什么重要：** AI 的瓶颈正在从芯片转向电力。这笔交易表明，公用事业公司开始主动将 AI 算力需求视为核心增长动力。未来科技公司可能直接入股电网或自建电厂，能源与 AI 的融合将成为新投资主题。

> 原文：[36氪](https://36kr.com/newsflashes/3814800262373120?f=rss)

---

当 AI 收入高度集中、GPU 巨头开始造 CPU、监管者开始拥抱模型能力，下一个打破格局的会是 Anthropic 的收购组合、英伟达的全栈，还是电力公司的电网？投资者需要重新定义“AI 基础设施”。