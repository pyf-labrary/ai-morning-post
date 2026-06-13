# Kimi K2.7-Code开源，编程模型性价比碾压

今天最值得关注的是 Moonshot AI 开源 Kimi K2.7-Code 编程模型，在 Kimi Code Bench v2 上性能提升 21.8%，推理 token 减少 30%，价格仅为 GPT-5.5 的 1/12。这一数据意味着开源编程模型在性价比上已逼近甚至部分超越闭源巨头，开发者加速选型开源将成为近期主旋律。同时，Agent 技能标准化、Apple 容器等动态也在拓宽开源生态的边界。

## Moonshot 开源 Kimi K2.7-Code，性能与成本双杀

Moonshot AI 正式开源 Kimi K2.7-Code，基于 K2.6 架构改进。核心提升在于推理效率：token 消耗降低 30%，同时在自研的 Kimi Code Bench v2 上取得 21.8% 的性能跃升。更值得关注的是价格策略——每 token 成本仅 GPT-5.5 的 1/12，成为目前市场上最具竞争力的编程模型之一。对于追求成本效益的团队而言，这将直接改变编程模型的选型决策。

> 原文：[The Decoder](https://the-decoder.com/moonshots-open-model-kimi-k2-7-code-undercuts-gpt-5-5-and-claude-by-up-to-12x-on-price-per-token/)

## Agent Skills 框架兴起，Anthropic 推动标准化

Anthropic 发布 skills 仓库，旨在规范 AI 编码代理的技能描述与复用。社区迅速跟进，涌现出 superpowers、agent-skills、PM Skills 等多个开源项目，从项目管理到任务拆解均有所覆盖。标准化的意义在于让不同 agent 之间能共享技能模块，降低重复开发成本，也使得技能审计和安全扫描（如 NVIDIA SkillSpector）成为可能。

> 原文：[GitHub](https://github.com/anthropics/skills)

## 小米 MiMo Code 开源引争议：5k 星但 bug 频出

小米开源 AI 编程模型 MiMo Code，5 人团队 2 周打造，迅速收获 5k+ GitHub Stars。但开发者反馈代码质量堪忧，bug 频发，社区争议集中于“营销大于实质”。该项目说明开源门槛降低后，模型质量与开发者预期之间的落差正在放大，社区对“快速秀肌肉”型项目的审慎态度值得关注。

> 原文：[InfoQ](https://www.infoq.cn/article/GTYmDTKIy8f79604Jz1V)

## NVIDIA 发布 SkillSpector：AI Agent 技能安全扫描器

NVIDIA 开源 SkillSpector，专门检测 AI Agent 技能中的安全漏洞、恶意模式及其他隐患。随着 Agent 技能数量激增，安全审计成为刚需。SkillSpector 提供静态分析能力，可嵌入 CI/CD 流水线，为代理生态的可信度提供基础设施级保障。

> 原文：[GitHub](https://github.com/NVIDIA/SkillSpector)

## LMCache：用最快 KV 缓存层加速 LLM 推理

LMCache 开源项目宣称通过高效的 KV 缓存层大幅提升 LLM 推理效率，尤其适用于长上下文场景。其核心思路是复用历史推理计算，减少重复计算开销。对于部署大规模对话系统的团队，这一技术可能成为降低推理成本的关键组件。

> 原文：[GitHub](https://github.com/LMCache/LMCache)

## Apple 开源 container：在 Mac 上运行 Linux 容器

Apple 开源 container 工具，利用轻量级虚拟机在 Mac（特别是 Apple Silicon）上创建和运行 Linux 容器。这与 Docker Desktop 等方案不同，Apple 的底层实现更贴近硬件加速，性能表现值得期待。对于跨平台开发和测试场景，这一工具填补了原生容器支持的空白。

> 原文：[GitHub](https://github.com/apple/container)

当开源编程模型成本降至 GPT-5.5 的 1/12，闭源模型的护城河还剩下什么？这是每一个开发者今天应该重新思考的问题。