# 开源模型与编码 Agent 都在转向节省与记忆

今天开源板块最值得看的是百度 Unlimited-OCR：一个 1.3B 参数模型主打「一次性长程解析」并登顶 OCR 榜单，说明视觉模型的开源竞争已经推进到具体任务上，不再靠参数规模吸引注意。与此同时，微软的 TokenEconomizer、Prime Intellect 的 Mega MoE 反向内核、claude-mem 的跨会话记忆，指向同一个现实问题：编码 Agent 的能力不再只取决于模型本身，还取决于 token 成本、训练效率和上下文管理这些工程细节。以下 8 条，按重要性排列。

## 百度开源 Unlimited-OCR，1.3B 登顶 OCR 榜

百度在 GitHub 开源 Unlimited-OCR，主打一次性长程解析能力，1.3B 参数规模在 OCR 榜单上登顶。关键点有两层：一是「unlimited」指向长文档、多页连续输入的解析场景，并非单张图片识别；二是 1.3B 这个量级，意味着它可以在单卡或消费级硬件上部署，对做文档处理流水线的团队来说，部署成本比能力上限更值得关注。为什么重要：OCR 长期是闭源商业 API 的稳定收入来源，一个轻量开源模型登顶，会直接压薄文档解析这一环节的定价空间；同时它也说明国产开源视觉模型正从通用榜单转向具体任务，不再争夺通用榜单的第一。

> 原文：[GitHub - baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

## 微软开源 TokenEconomizer，编码 Agent 降本三成

微软研究院与 UC Berkeley 联合发布开源插件 TokenEconomizer，思路是从 Agent 的历史会话中学习，压缩并复用上下文，而不是每次重新发送完整对话。在 SWE-Bench 上，它把编码 Agent 的 token 成本降低 18.4%–30.9%。关键点在于它做的是「成本侧优化」而非能力提升：不改模型、不改任务定义，只改上下文如何被喂进去。为什么重要：编码 Agent 大规模铺开之后，token 账单会从实验成本变成运营成本，这类「同样效果、更少输入」的插件会像当年的缓存层一样，成为 Agent 基础设施的标准组件。

> 原文：[Microsoft TokenEconomizer: cost control for coding agents](https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/)

## Prime Intellect 为 Mega MoE 内核补上反向传播

Prime Intellect 开源了针对 DeepSeek 融合 Mega MoE 内核的可训练版本，核心工作是补上反向传播，让这套原本只用于推理的高效内核能够参与训练。在 Qwen3 MoE 上，训练步最高提速 34%。关键点：MoE 的专家路由与融合内核长期存在「推理快、训练难」的割裂，反向传播的实现质量直接决定能否复用。为什么重要：训练侧的算子优化通常掌握在少数团队手里，开源一个可训练的融合内核，等于把 MoE 训练的门槛往下压了一档，对自研 MoE 的中小团队是实打实的利好。

> 原文：[Prime Intellect open-sources trainable fused Mega MoE kernel](https://www.marktechpost.com/2026/10/29/prime-intellect-prime-mega-moe-fused-moe-kernel-training/)

## 英伟达开源 H3 视频增强，支持 4K 重生成

英伟达与 MIT 在 Hugging Face 发布 Open-H3-Regenerate-2K 权重，基于 MiniMax H3 实现视频增强与重生成，最高支持 4K。关键点在于「regenerate」而非传统超分：它不只是插值放大像素，而是让模型重新生成细节内容，这对老片修复、低清素材再上院线这类场景意义不同。为什么重要：视频增强是少数能直接折算成内容资产价值的方向，英伟达选择开源权重而非只开放 API，是在为自家硬件生态锁定下游工作负载。同时这类模型的实际效果高度依赖输入质量，落地时仍需按素材类型分别评估。

> 原文：[英伟达开源 H3 视频增强方案](https://www.qbitai.com/2026/10/506743.html)

## GitHub 开源 spec-kit，规范驱动开发落地为工具

GitHub 发布 spec-kit 工具包，用于支持规范驱动开发（SDD，Spec-Driven Development）流程的启动与落地。关键点：SDD 的主张是先写清楚规范，再让 Agent 或人生成实现，而 spec-kit 把这件事从方法论变成了脚手架，包括规范模板、目录结构与工作流约定。为什么重要：编码 Agent 当前最大的失败模式并不是写不出代码，而是写出的代码与真实意图偏离，规范前置是少数能够系统性抑制这个问题的手段。GitHub 亲自发布工具，说明它希望把规范格式的话语权掌握在平台侧，而非让其在各家 prompt 工程实践中各自演化。

> 原文：[GitHub - spec-kit](https://github.com/github/spec-kit)

## HKUDS 开源 DeepTutor，做终身个性化辅导

香港大学数据科学团队（HKUDS）开源 DeepTutor，定位是终身个性化 AI 辅导，项目已登上 GitHub Trending。关键点在于「终身」二字：它强调的是跨时间、跨学科的持续学习者建模，而非一次性问答或单门课程助手。为什么重要：教育是 Agent 落地最容易被低估的场景，因为它要求长期记忆、学习者状态建模与教学策略三件事同时成立，恰好是当前 Agent 架构最薄弱的部分。HKUDS 近年在开源 Agent 与检索方向上产出密集，这个项目值得作为「长期记忆 + 个性化」的参考实现来读。

> 原文：[GitHub - HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

## claude-mem 让 Agent 跨会话保留记忆

开源项目 claude-mem 捕获 Agent 会话内容，压缩后注入未来会话，从而形成跨会话的持久记忆，支持 Claude Code、Codex、Gemini 等多家工具。关键点：它不做模型层改动，而是在会话边界上做「写入—压缩—召回」的外部记忆层，压缩策略是成败关键，因为原始会话直接注入会迅速耗尽上下文。为什么重要：跨会话记忆是编码 Agent 从「一次性工具」变成「长期协作者」的必要条件，而目前各大厂商都还没有统一方案，社区自建记忆层很可能会先跑出事实标准。

> 原文：[GitHub - thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

## obra/superpowers 给编码 Agent 一套技能框架

开源项目 obra/superpowers 提供可组合的技能（skills）与软件开发方法论，目标是让编码 Agent 按完整流程工作，而不是在单点上响应指令。关键点：它把「技能」做成可组合单元，并配套流程约束，本质是用结构化方法约束 Agent 的行为边界。为什么重要：这与 GitHub spec-kit 是同一趋势的两个侧面——行业正在从「更好的 prompt」转向「更好的流程与规范」。当 Agent 能力趋同时，工程化程度会变成团队之间的主要差距。

> 原文：[GitHub - obra/superpowers](https://github.com/obra/superpowers)

## 结语

今天这批项目没有一个是靠参数规模取胜的，它们的价值全在「省下来的 token、补上的反向传播、记住的上下文」这些不显眼的地方。真正的问题或许是：当编码 Agent 的框架与记忆层开始标准化，你的团队优势还剩在哪一层？

（说明：标题「节省与记忆」取自 TokenEconomizer 与 claude-mem 两条主线，若需更贴 OCR 头条可改为「1.3B 模型登顶 OCR 榜」。）