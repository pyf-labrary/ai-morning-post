# Ng开源桌面AI助手，微软阿里齐推新工具

导语：Andrew Ng 刚发布的 OpenWorker 是今天最值得关注的工具——它不跟你聊天，而是直接返回交付物，本地运行，支持 30 余种模型。这可能是“AI 同事”的第一个真正开源实现。同一天，微软 SkillOpt 让 LLM 代理学会可复用的自然语言技能，阿里巴巴开源了生产级代码审查工具。开源 AI 基础设施正在从聊天走向具体交付。

## Andrew Ng 发布开源桌面AI助手 OpenWorker

OpenWorker 采用 MIT 许可，定位为“本地优先的 AI 同事”（desktop AI coworker），核心差异在于它直接交付完成的文档、代码、报告等成品，而非一轮轮对话。用户下达任务后，OpenWorker 自主规划、执行并输出结果。它支持超过 30 种模型（包括开源模型和闭源 API），并且可以在本地完全离线运行，数据不出设备。对于隐私敏感的技术团队和独立开发者，这提供了一个可控且高效的 AI 工作流入口。

> 原文：[https://www.marktechpost.com/2026/07/23/andrew-ng-just-released-openworker-an-open-source-local-first-desktop-ai-coworker-that-returns-finished-deliverables-instead-of-chat/](https://www.marktechpost.com/2026/07/23/andrew-ng-just-released-openworker-an-open-source-local-first-desktop-ai-coworker-that-returns-finished-deliverables-instead-of-chat/)

## 微软开源 SkillOpt：文本空间优化器提升 LLM 代理技能

SkillOpt 是微软开源的一套算法框架，用于在文本空间中自动训练可重用的“自然语言技能”。核心机制：通过轨迹编辑（trajectory editing）和验证门控（verification gating）来更新冻结 LLM 的行为，无需微调模型参数。SkillOpt 可以像 Prompt 一样存储和复用技能，使代理在复杂任务中表现更稳定。这对构建自主 agent 的团队尤其有价值——不再需要反复调整提示词，而是用自动化方法“练”出技能。

> 原文：[https://github.com/microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)

## Block 开源 Buzz：人类与代理的蜂群协作平台

Block（原 Square）开源了 Buzz，一个基于中继（relay-based）的协作平台。它允许人类和 AI 代理在自定义工作空间中共同构建产品，支持工作流编排、实时通信和代理任务分配。Buzz 的设计更像“蜂群”——多个代理可以同时参与，由人类协调。对于需要人机混合团队的创业公司和开发者，Buzz 提供了一套基础框架，降低编排门槛。

> 原文：[https://github.com/block/buzz](https://github.com/block/buzz)

## OmniRoute：免费 MIT AI 网关，支持 500+ 模型

OmniRoute 是一个轻量级 AI 网关，提供统一 API 端点，汇集了 290+ 供应商、500+ 模型（其中 90+ 免费），并具备配额感知的自动路由能力。开发者只需接入一个接口，即可在多个提供商之间切换、兜底。对于管理多模型调用的工程团队，这能显著减少集成成本和故障时间——尤其适合需要平衡成本与性能的场景。

> 原文：[https://github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

## 阿里开源代码审查工具 open-code-review

阿里巴巴开源了经过大规模验证的混合架构代码审查工具 open-code-review。它结合了确定性流水线（静态分析、正则规则）和 LLM 代理，同时内置多种安全规则（SQL 注入、XSS 等）。该工具在阿里内部已用于大量审查场景，可显著减少人工 review 的重复劳动。对需要提升代码质量和安全性的团队来说，这是一个可以直接投入生产的开源方案。

> 原文：[https://github.com/alibaba/open-code-review](https://github.com/alibaba/open-code-review)

结语：当开源工具开始聚焦交付和协作，而不是停留在对话层面，AI 的落地才真正进入务实阶段。你准备让哪个工具明天进入自己的开发栈？