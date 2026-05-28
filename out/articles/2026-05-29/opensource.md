# 微软开源 Agent 治理，Anthropic 双连击

导语：今天最值得关注的是微软开源的 Agent Governance Toolkit，它把 OWASP Top 10 安全规范直接嵌入 AI Agent 治理，给行业提供了一套可落地的信任基础设施。同时 Anthropic 连发两个开源项目（知识插件 + 技能系统），Perplexity 则用新 Tokenizer 把推理延迟砍了 5 倍——开源社区正在加速定义 Agent 时代的工程标准。

## 微软开源 Agent Governance Toolkit，覆盖 OWASP Top 10

微软发布了一个治理工具包，为 AI Agent 提供策略执行、零信任身份、沙箱执行与可靠性工程能力。它将 OWASP Top 10 安全风险映射到 Agent 开发与运行阶段，用户可以开箱即用业界最佳实践。关键点在于这套工具并非论文概念，而是可直接集成到现有 CI/CD 管道和运行时中。对于 CISO 与平台工程师来说，这填补了 Agent 从实验到生产之间缺失的“护栏层”。

> 原文：https://github.com/microsoft/agent-governance-toolkit

## Perplexity 开源 Unigram Tokenizer，延迟降低 5 倍

Perplexity AI 开源了重写的 Unigram 分词器，P50 推理延迟降低 5 倍，CPU 利用率减少 5-6 倍。核心改进在于重新组织了分词表的搜索结构，使排序阶段无需全量遍历。相比 Hugging Face Tokenizers 的实现，这个版本对长文本的推理效率提升尤其显著。对于需要高频调用 LLM 的 Agent 或 RAG 应用，这个 Tokenizer 可以快速降低响应成本。

> 原文：https://www.marktechpost.com/2026/05/28/perplexity-ai-open-sources-unigram-tokenizer-that-achieves-5x-lower-p50-latency-than-hugging-face-tokenizers-crate/

## SQLite 新增 AGENTS.md，规范 AI 代码助手行为

SQLite 项目在主仓库中增加了一个 `AGENTS.md` 文件，为 AI 代码助手提供专属开发指南。它明确了当 AI 工具（如 Copilot、Claude Code）修改代码时应遵循的项目惯例、编码风格和测试要求。这件事的意义超出文件本身：它标志着主流开源项目开始主动“驯化”AI 协作，而不是被动接受补丁。

> 原文：https://github.com/sqlite/sqlite/blob/master/AGENTS.md

## Anthropic 开源 Knowledge Work Plugins，让 Claude 变领域专家

Anthropic 发布了知识工作插件套件，用户可以将 Claude 定制为特定角色（如工程师、分析师）、团队或公司内部的专家助手。插件封装了检索、验证、记忆与行动链路，让 Claude 不再只是通用问答，而是能基于企业知识库做专业决策。对产品经理和开发者而言，这是低成本构建垂直 Agent 的“乐高积木”。

> 原文：https://github.com/anthropics/knowledge-work-plugins

## Anthropic 发布 Agent Skills 开源仓库

Anthropic 同时开源了 Agent Skills 实现，提供一套标准化的技能系统供 Claude 等 Agent 使用。技能是可组合、可复用的行为单元——比如“读取数据库”“发送邮件”“生成报告”——Agent 可以按需调用。这实际上是 Agent 操作系统的“微服务”层，有助于不同 Agent 之间共享能力，降低重复开发。

> 原文：https://github.com/anthropics/skills

## NVIDIA 开源 Polar 框架：用强化学习训练代码 Agent

NVIDIA 发布了 Polar，一个基于 GRPO 的 token 忠实 rollout 框架，支持在 Codex、Claude Code、Qwen Code 等模型上训练语言 Agent。它确保强化学习过程中生成的 token 序列与实际策略完全一致，避免 “作弊”偏差。对于想用 RL 微调代码 Agent 的团队，这提供了一个可信的训练基础设施，尤其适用于需要高准确性的自动化编程场景。

> 原文：https://www.marktechpost.com/2026/05/27/nvidia-releases-polar-a-token-faithful-rollout-framework-for-grpo-training-across-codex-claude-code-and-qwen-code/

## 开源项目 stop-slop：移除 AI 写作中的“机器味”

GitHub 项目 stop-slop 提供技能文件，用于清理 AI 文本中常见的陈词滥调、冗余连接词和过度礼貌用语，让输出更像人类。关键点在于它不依赖额外模型，而是基于规则和模板替换，适合作为 Agent 输出的后处理步骤。对于需要面向终端用户生成内容的产品（如邮件助手、报告生成器），这个小工具可以显著改善用户体验。

> 原文：https://github.com/hardikpandya/stop-slop

## Heretic：全自动消除语言模型审查的对抗工具

Heretic 利用对抗技术自动移除 LLM 中的审查限制，通过可微优化找到绕过安全过滤器的 prompt 模式。它引起了显著的伦理争议——一方面，它揭示了现有审查机制在对抗攻击下的脆弱性；另一方面，它可能被滥用于产生有害内容。对于安全研究者，这是一个压力测试工具；对于平台方，它提醒审查系统需要更强的鲁棒性。

> 原文：https://github.com/p-e-w/heretic

结语：当 Agent 工具链越来越完备，治理与去审查同时开源——你更担心 Agent 不够安全，还是太安全？