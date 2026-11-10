# Agent 的脚手架，正在集体开源

导语：Anthropic 把 Claude 的 skills 实现放上 GitHub，并指向一份 Agent Skills 标准——这是今天开源板块里最值得看的一条。单看代码量它并不惊人，但它试图把「一个 agent 会做什么」从提示词里的自由文本，变成可分发、可版本化的构件。同一天上榜的还有面向 agent 的 Git 服务器、沙箱运行时、安全 harness 和「agent-ready」设计系统，方向出奇一致：模型能力之外的工程层，正在被一批开源项目快速填满。

## Anthropic 开源 Agent Skills 仓库

Anthropic 在 GitHub 公开了 Agent Skills 仓库，其中包含 Claude 的 skills 实现，并明确指向 Agent Skills 标准。

关键点在于定位：这不只是一个示例集合，更像标准的一份参考实现。技能被当作独立于模型版本的封装单元，可以单独维护、替换和分发。一旦「技能」有了公共格式，围绕它的工具链——分发、评测、权限控制——才有地方挂载。

为什么重要：过去一年 agent 的能力主要靠提示词工程和工具调用临时拼接，复用性差、难以审计。把技能标准化，是让 agent 行为可被审查、可被组合的前提。判断：真正的分水岭不在这个仓库本身，而在有多少团队愿意按这套约定去写技能。

> 原文：[anthropics/skills](https://github.com/anthropics/skills)

## Aspen：给 Agent 用的 Git 服务器

Reason Machines 开源了自托管的 Git 服务器 Aspen，面向 AI Agent 场景，遵循 OpenAI Pando 的设计；按其公司内部测试，单台 8 核服务器可达到每秒 567 次 push。

这个数字值得琢磨，因为它改写了前提。人类开发者的 push 频率以天计，agent 的频率以秒计；而现有托管平台的配额、限流和 review 流程，全都是按人的节奏设计的。

为什么重要：agent 写代码的瓶颈正在从「生成」转向「提交与协作」。如果 agent 成为主要提交者，仓库就需要新的分支策略、审计粒度和冲突处理方式。Aspen 是少数直接改 Git 服务端的项目，接下来要看它能否被现有 CI 生态接住，而不是长成一座孤岛。

> 原文：[Reason Machines open-sources Aspen](https://www.marktechpost.com/2026/11/09/reason-machines-aspen-open-source-git-server-ai-agents/)

## 0sec Labs 开源 AI 安全 harness「0」

0sec Labs 开源了 AI 安全测试框架「0」，覆盖代码审查、渗透测试、逆向工程与修复，提供 Web UI、CLI 和 MCP 三种接口，并支持本地运行自有模型。

两个设计选择透露了它的判断：MCP 被当作主要接口，说明默认调用方已经是 agent 而非人；允许本地自有模型，则直接回应企业最在意的数据边界——漏洞细节不必出内网。

为什么重要：把进攻性安全能力打包成 harness，意味着渗透测试有机会进入 CI 流程。风险也在这里：同一套能力既能用于修复也能用于攻击，开源之后，护栏设计比功能列表更值得审视。

> 原文：[0sec Labs open-sources 0](https://www.marktechpost.com/2026/11/08/0sec-labs-open-sources-0-ai-security-harness/)

## Meta 开源设计系统 astryx

Meta 开源了设计系统 astryx，完全可定制，并针对 Agent 使用场景做了准备。

「agent-ready」是这份仓库最值得注意的标签。设计系统的消费者正从人扩展到 agent，组件需要的不只是视觉规范，还需要可被程序理解的结构化约定——否则 agent 改前端只能靠猜。

为什么重要：如果 agent 要参与写 UI，它首先得读懂设计系统。谁的设计系统先对机器友好，谁在「agent 写界面」的时代就更占便宜。目前这还只是一个仓库，但方向值得记一笔，尤其值得前端团队留意。

> 原文：[meta/astryx](https://github.com/meta/astryx)

## OpenSandbox 开源 Agent 沙箱运行时

OpenSandbox 开源了一个面向 AI Agent 的沙箱运行时，主打安全、快速、可扩展。

把它和前几条连起来看，agent 执行面的拼图开始成形：Aspen 管「写」——代码落在哪里；0sec 管「查」——行为是否越界；OpenSandbox 管「跑」——执行环境如何隔离。

为什么重要：沙箱是 agent 从 demo 走向生产的前置条件，也是最容易被低估的一环。项目尚处早期，评估重点应放在隔离强度、冷启动开销、以及与现有容器编排的兼容性上，而不是功能清单有多长。

> 原文：[OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)

## OpenBMB 开源无分词器 TTS VoxCPM2

OpenBMB 开源了 VoxCPM2，一种无分词器（tokenizer-free）TTS，支持多语言语音生成、创意音色设计和拟真声音克隆。

无分词器是一条明确的路线选择：不在音频与文本之间插入离散 token 层，其主张是避开量化带来的信息损失。三项能力里，音色设计与声音克隆最容易被产品化，也最快会被拿去和闭源方案比价。

为什么重要：语音正在成为 agent 的默认输出之一，TTS 的竞争点也从「像不像人」转向可控性与成本。开源把这条线的门槛继续压低，同时把声音克隆的滥用风险一并放大——能力已经开源，授权与溯源机制还没有跟上。

> 原文：[OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)

今天这六条拼在一起，指向同一件事：agent 的竞争正从模型参数转到它脚下的地面。留一个问题——如果技能、仓库、沙箱都被标准化了，下一个被商品化的会是什么？