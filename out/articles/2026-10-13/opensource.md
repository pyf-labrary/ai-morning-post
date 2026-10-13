# 模型不再生成文本，只做决策

今天开源板块最值得看的是两个决策模型：Cloudflare 基于 Qwen3-Omni 放出 Apache-2.0 的 Clef-omni，vLLM Semantic Router 同期更新 Decision 3.0 系列，共同点是一次调用只输出选择、判断和打分，不生成文本。这意味着 agent 流水线里长期靠提示词和分类器硬凑的"路由层"，正在被当成独立的模型品类来做。其余七条大多指向同一件事：把 agent 的某一层拆出来，做成可替换的零件——编码入口、技能目录、3D 表示、显存瓶颈、语音出口。开源在卷的不是更大的模型，而是更便宜的装配方式。

## free-claude-code：一次接入 9 种编码 agent

开源项目 free-claude-code 把 Claude Code、Codex、OpenCode 等 9 种编码 agent 收进同一个入口，终端、IDE、浏览器都能用，宣称提供 13 亿+ 免费 token。

关键点在"聚合"而非"自研"：用户不必为每个 agent 单独准备账号与额度，切换成本被抹平，多 agent 对比试用的门槛降到接近于零。

判断上要克制：这类项目的价值上限取决于上游的额度策略与合规边界，"免费 token"更像获客手段而不是商业模式。作为个人尝试多 agent 工作流的入口值得一用，但不适合放进团队级基础设施的依赖清单里——它的可用性不在自己手上。

> 原文：[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)

## 决策模型：不生成文本，只做选择

Cloudflare 发布基于 Qwen3-Omni 的 Apache-2.0 决策模型 Clef-omni（30B-A3B），vLLM Semantic Router 同期放出 Decision 3.0 系列，两者都能在一次调用中完成选择、判断与打分，且不生成自然语言文本。

为什么重要：agent 系统里"该调用哪个模型、该走哪条工具链、这次结果值多少分"这类裁决，过去靠提示词、规则或小分类器凑合。把它做成模型，输出从 token 流变成结构化决策，延迟和成本都可控。

30B-A3B 的 MoE 形态意味着总参数 30B、激活约 3B，适合常驻在多模型流水线的入口。如果这条路走通，agent 的成本结构会变：贵的模型只处理难题，日常裁决交给便宜的一层。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/11/cloudflare-clef-omni-multimodal-decision-model/)

## 微软开源 TRELLIS.2：3D 生成回到"表示"这一层

微软开源 TRELLIS.2，核心是面向 3D 生成的原生紧凑结构化潜变量表示（structured latent），目标是在提升三维资产生成质量的同时压住算力开销。

关键点：3D 生成长期借用 2D 或视频模型的表示去逼近三维，先天受限。把结构化先验做进 latent，相当于在数据表示层面为几何与拓扑留出位置，而不是让模型从零学出空间关系。

为什么重要：3D 资产质量一旦跨过某条线，游戏、影视、电商的建模流程会被重写。这类改动通常先出现在开源权重里，而不是闭源 API 的更新日志里。

> 原文：[microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)

## Anthropic 开源知识工作插件库

Anthropic 在 GitHub 开源 knowledge-work-plugins，定位是让知识工作者在 Claude Cowork 中把模型定制成特定岗位、团队与公司的"专家"。

关键点：交付物不是提示词合集，而是可复用的插件包，把岗位知识、流程约束和公司上下文打包进同一层。使用者拿到的是一份可以直接装上的岗位配置。

为什么重要：企业落地大模型的主要摩擦，一直是"每次都重新交代背景"。插件化是把这部分成本一次性收敛的做法。

判断：这更像把咨询交付物产品化。谁掌握岗位知识的结构化方式，谁就掌握客户迁移到别家模型的成本。

> 原文：[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

## rea：让 agent 从应用行为逆向到原生二进制

开源项目 rea 让 AI agent 自动做软件逆向工程，从应用行为分析一路深入到原生二进制层面，已登上 GitHub Trending。

关键点：逆向工程最贵的环节是"理解"——识别协议、恢复数据结构、判断函数语义，这些恰是 agent 擅长、而传统反编译工具不擅长的部分。工具负责反汇编，agent 负责给出假设并验证。

为什么重要：对安全研究、漏洞挖掘和遗留系统迁移，这是明确的效率工具；反过来说，逆向的门槛被显著拉低，攻击面审计、恶意软件分析与竞品拆解的成本曲线都会跟着变。这类能力的扩散速度，通常快于配套规则的出现速度。

> 原文：[morluto/rea](https://github.com/morluto/rea)

## AirLLM：4GB 显存跑 70B 模型

AirLLM 通过分层加载（layer-by-layer）让单张 4GB 显卡完成 70B 量级模型的推理，为大模型本地部署提供了一条低成本路径。

关键点：思路是把权重留在内存或磁盘，逐层调入显存计算，用时间换空间。代价是访存带宽成为瓶颈，吞吐会明显低于权重常驻显存的方案。

为什么重要：本地推理的门槛从"买得起卡"变成"忍得了慢"。对隐私敏感、离线运行、预算有限的场景，这是有意义的选项。需要说清楚的是，它解决的是"能不能跑起来"，不是"能不能服务生产流量"——这两件事之间的差距，往往比显存数字更大。

> 原文：[lyogavin/airllm](https://github.com/lyogavin/airllm)

## awesome-claude-skills：技能生态进入目录阶段

Composio 维护的 awesome-claude-skills 汇总了 Claude Skills 相关资源与工具，方便用户定制 Claude 的工作流。

单看内容，它只是一个索引，价值有限。但它是生态信号：当一个平台的扩展能力需要第三方来整理目录时，说明供给密度已经超过官方文档能覆盖的范围。

判断：技能与插件的分发层，往往先于收费层出现。早期值得关注的不是某个具体 skill 好不好用，而是谁在维护目录、按什么标准筛选、排序依据是什么——这些细节会实质性决定后来者的默认选择。

> 原文：[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

## VoiceStudio：本地的 ElevenLabs 替代

VoiceStudio 提供完全本地运行的语音克隆、音色设计、视频配音、听写与有声书制作，支持 646 种语言，无需云服务。

关键点：它把配音、听写、有声书这几条常用链路收进一个本地工具，等于掐断了语音数据的出口。这是云端 API 结构上做不到的合规优势，不是性能优势。

为什么重要：语音克隆今天的约束早已不是技术，而是授权与肖像权。本地化把"能不能用"的判断权从厂商转移给使用者，规则成本和责任也一并转移。对内容团队是自由，对法务是新的工作量。

> 原文：[debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

## 结语

今天这批项目指向同一个趋势：agent 的每一层都正在被拆成可替换的零件，从决策、技能到显存和声音。当每一层都有免费替代品，你愿意为什么付费？