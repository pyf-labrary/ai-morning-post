# Claude 4.8 超 GPT-5.5，AI 模型竞赛继续

今天最值得关注的发布来自 Anthropic：Claude Opus 4.8 在多项基准上超越 OpenAI 的 GPT-5.5，并同期推出 Dynamic Workflows 工具，支持数百子智能体并行。这削弱了 GPT-5.5 的“最强”标签，也暗示未来竞争可能从单一模型精度转向系统性协同能力。

## Claude Opus 4.8：适度改进，多项领先

Anthropic 发布 Claude Opus 4.8，官方措辞为“适度但切实的改进”。在关键基准测试中，该模型超越了 GPT-5.5（当前公认最强模型之一）。更值得关注的是配套工具 Dynamic Workflows，它允许开发者编排数百个子智能体并行协作，相当于将 agentic 能力规模化。

- **是什么**：模型版本更新 + 多智能体编排工具。
- **关键点**：多项基准领先，并非微小提升；Dynamic Workflows 将协作节点数从数十提升至数百。
- **为什么重要**：性能差距缩小，且 Anthropic 选择同时强化“单模型精度”和“多智能体协作”，可能改变企业对模型选型的优先级——不再只看单点能力，还要看部署弹性。

> 原文：[Anthropic - Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)

## GPT-5.5 Instant 可读性升级，旧模型退出

OpenAI 为 GPT-5.5 Instant 做了可读性升级，同时宣布逐步淘汰两个较旧模型版本。这是一个典型的“平稳迭代”动作：不追求榜单排名，而是在开发者调用中降低延迟、提升输出质量。

- **是什么**：GPT-5.5 Instant（低成本快速版）的模型微调。
- **关键点**：可读性改善，旧模型退役，未披露具体基准分数变化。
- **为什么重要**：OpenAI 似乎在巩固自家生态的入口，通过优化即时版来吸引更多高频调用场景（如客服、内容生成）。这也会倒逼其他模型定价与响应速度竞争。

> 原文：[The Decoder - OpenAI gives GPT-5.5 Instant a readability upgrade](https://the-decoder.com/openai-gives-gpt-5-5-instant-a-readability-upgrade-while-phasing-out-two-older-models/)

## Liquid AI 开源 8B 激活 MoE，训练达 38T tokens

Liquid AI 发布 LFM 2.5 8B-A1B，一种混合专家模型，激活参数仅 8B，但训练数据达 38T tokens。虽然绝对规模不及头部大厂，但高 token 量/参数比意味着在特定任务上可能具备竞争力。

- **是什么**：Liquid AI 推出的 8B 激活参数的 MoE 模型。
- **关键点**：训练 tokens 数 38T，激活参数仅 8B，属于“小参数大语料”路线。
- **为什么重要**：MoE 架构的性价比策略日益清晰——用更少激活参数换取更大容量。对于预算有限、追求推理效率的开发者，这类模型可能成为 GPT-5.5 或 Claude 4.8 的低成本替代。

> 原文：[Liquid AI - LFM 2.5 8B-A1B](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

---

今日三件事指向同一个问题：当头部模型的基准差距收窄到个位数百分比，你的下一项投入应该押注模型本身，还是它的协作生态与推理成本？