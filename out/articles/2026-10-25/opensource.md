# Agent 沙盒，一天开源了两个

今天这份开源清单里，最值得看的是 Anthropic 把 Claude Code 背后的 OS 级沙盒 srt 开源了。它绕开容器，直接用 macOS Seatbelt 和 Linux bubblewrap 限制 Agent、MCP server 与 CLI 工具的文件与网络访问——把隔离做薄，才有可能默认开启。同一批里 NVIDIA 的 OpenShell 也指向 agent 执行层，方向撞车不是巧合：模型能力之外，权限边界正在成为 Agent 落地的真正瓶颈。其余几条，从长文档 OCR 到树模型推理引擎，都值得技术团队花十分钟扫一眼。

## Anthropic 开源 sandbox-runtime：不用容器也能隔离 Agent

Anthropic 把 Claude Code 背后的 OS 级沙盒 srt（sandbox-runtime）开源了。

关键点在实现路径：不走容器，而是用 macOS 的 Seatbelt 与 Linux 的 bubblewrap 做进程级限制，约束对象明确列了三类——Agent 本身、MCP server、以及被调用的 CLI 工具，管的是文件访问与网络访问这两条最要命的边界。

为什么重要：Agent 真正进生产时，阻力往往不是模型够不够聪明，而是敢不敢给它读文件、发请求的权限。容器方案隔离得干净，但重、与开发机上的日常工作流摩擦大，结果常常是"先关掉沙盒跑通再说"。用操作系统原生机制把隔离做薄，是把安全从"可选加固"变成"默认配置"的前提。MCP server 被纳入限制范围这点尤其值得注意——第三方工具是目前整条链路里最不可控的一环。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/24/anthropic-sandbox-runtime-ai-agent-sandbox/)

## 英伟达开源 OpenShell，给自主 Agent 一个安全运行时

NVIDIA 开源了 OpenShell，定位是面向自主 AI agent 的安全、私密运行时，补齐 agent 执行层的隔离与权限边界。

目前公开信息主要在仓库本身，细节还有待展开，但定位足够清晰：它要占的是 agent 与宿主环境之间那一层。

为什么重要：把它和上一条放在一起看——两家在同一个板块里给出了同一个判断，即 agent runtime 正在从"每个团队自己糊一层"变成独立的基础设施品类。对使用方来说，短期是多一个选项；中期要警惕的是执行层被单一大厂绑定，而这恰恰是 Anthropic 那套"薄、依赖 OS 原生机制"的方案更值得盯的原因。可以预期，未来一年 agent 运行时会像当年的容器运行时一样，被拿出来单独比较。

> 原文：[GitHub: NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)

## 百度开源 Unlimited-OCR，主打一次性长文档解析

百度放出了 Unlimited-OCR，宣称能以单次前向完成长程文档解析。

关键点是范式变化：不再把文档逐页切开分别识别、再靠规则或模型拼接，而是把长上下文一体化处理。

为什么重要：做 RAG 和文档 agent 的团队都清楚，上游 OCR 是最容易被低估的瓶颈。分页会切断跨页表格，页眉页脚变成噪声，版面层级关系在切片那一刻就丢了——后面再怎么清洗、重排、加 rerank，也只是在错误的基础上做补救。如果"单次前向"真能成立，省下的不只是工程链路长度，更是错误传播的源头。当然，"宣称"两个字要保留，长文档场景的实测结果才是分水岭。

> 原文：[GitHub: baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR)

## Anthropic 开源知识工作插件库，把 Claude 变成岗位专家

anthropics/knowledge-work-plugins 是一个面向知识工作者的插件集合，可以为不同角色、团队乃至具体公司定制 Claude 的专业能力。

关键点是颗粒度：不是教用户怎么写出更好的 prompt，而是把某一类岗位的专业做法直接打包成可安装的制品。

为什么重要：这是 prompt 工程的一次资产化。过去两年，团队里最懂业务的那些人把经验写进提示词，散落在各人的对话框里，无法版本管理、无法交接、无法复用。插件把这个过程产品化之后，企业的门槛从"会不会写 prompt"变成"选不选得对插件"，而 Anthropic 拿到的是一个标准化的生态卡位。对做垂直 agent 的创业公司来说，这类官方插件库也划出了一条需要重新确认的边界：哪些能力会很快变成平台的默认项。

> 原文：[GitHub: anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

## StartLux 开源 Prism，决策模型推理单卡提速 5.3 倍

StartLux 开源了 Prism，一个专用于决策模型（如 GBDT、树模型）的推理引擎，官方称单卡最高可提速 5.3 倍。

关键点是它填的空白：决策模型长期缺少专用推理引擎，多数团队直接跑在通用框架上。

为什么重要：过去两年推理优化的注意力几乎全给了 LLM 和 GPU 集群，但线上真正跑量最大的模型，很多仍然是树模型——风控评分、推荐排序、广告 CTR。这部分推理被"够用就行"地对待了很多年，优化空间反而没被认真挖过。5.3 倍这个数字必须在自家负载上验证，特征工程、批量大小、稀疏度都会大幅改变结论；但方向本身值得留意：推理效率不只是大模型的事，省下来的算力账单可能来自最不起眼的那一层。

> 原文：[InfoQ](https://www.infoq.cn/article/reksyo9EBAcP11Ns2GTO?utm_source=rss&utm_medium=article)

## Cloudflare 开源安全审计技能，让编码 Agent 当审计员

cloudflare/security-audit-skill 是一个执行多阶段安全审计的 agent skill。

关键点不在"用 Agent 做审计"，而在输出契约：结论要求可机器读取、且能被独立验证，而不是生成一份读起来很像那么回事的自然语言报告。

为什么重要：安全是 agent 输出里最不能"看起来对"的领域——一个措辞笃定但无法复核的漏洞结论，比不给结论更危险。把可验证性写进 skill 的输出规范，是这类组件从"提示词合集"走向"有接口契约的零件"的标志。这也是判断一个 agent skill 是否值得接入的实用标准：它交付的是结论，还是可被另一套工具复核的证据。

> 原文：[GitHub: cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

## OpenBMB 开源 VoxCPM2：无分词器的多语种 TTS

OpenBMB 开源了 VoxCPM2，走 tokenizer-free 路线做多语种语音生成，支持创意音色设计与高保真声音克隆。

关键点是路线选择：跳过离散 tokenizer，直接建模连续语音表示。

为什么重要：tokenizer 环节一直是 TTS 里信息损失与延迟的来源之一——把连续波形压成离散单元，再还原回去，细节和韵律都在这一步被削掉。近两年 tokenizer-free 与 token-based 的路线之争，本质是在"可控性"和"自然度"之间换位置。而多语种加音色克隆这个组合，对应的正是出海产品、内容本地化、有声内容生产的真实需求，开源意味着这块能力不再是大厂语音团队的专属。

> 原文：[GitHub: OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)

## Corgi：把 Agent 与终端多路复用到一起的小工具

Corgi 是一个来自 Show HN 的 agent/terminal 多路复用器，围绕日常高频操作优化交互体验；作者称已连续数周把它作为主力工具使用。

关键点是小而具体：它解决的不是能力问题，而是人和 agent 抢同一块终端屏幕的问题。

为什么重要：这类项目的信息价值常常高于它的技术深度——它暴露了当前 agent 工作流的真实形态：人还在终端里，agent 也在终端里，两者并行、互相打断、上下文彼此污染。tmux 解决了人与人之间的会话复用，但"人 + 多个 agent"的复用还没人认真设计过。谁把这块日常交互理顺，谁就在事实上定义人机协同的手感。值得装上试一天，感受比读 README 准。

> 原文：[corgi.computer](https://corgi.computer/)

---

今天开源的不是更强的模型，是笼子和接口。留一个问题：当隔离、审计、运行时都被开源，"Agent 可信"会变成开箱即用的默认配置，还是又一堆需要自己拼起来的零件？