# Agent开源潮：Nous、YC、NVIDIA同日上新

今日开源板块最值得关注的是多个重量级Agent项目同时发布，从个人工作流到企业级框架，AI Agent生态正快速走向实用化。其中Nous Research的Hermes Agent新增/learn命令，让代理可自动生成技能文件，标志着Agent可扩展性迈出关键一步。

## Hermes Agent：自动学习技能，可扩展性升级

Nous Research开源的Hermes Agent新增`/learn`命令，可从指定目录或对话历史自动生成`SKILL.md`文件，使AI代理能够动态吸收新技能。这一机制打破了传统Agent固定技能集的限制，让代理在运行时自我扩展能力边界。

**关键点**：`/learn`命令将用户行为或文档转化为标准化技能定义，无需手动编写配置。**为什么重要**：解决了Agent长期面临的知识更新和维护痛点，为社区贡献了一个可复用的技能学习范式。

> 原文：https://github.com/NousResearch/hermes-agent

## gstack：YC CEO的Claude Code个性化配置开源

Y Combinator CEO Garry Tan开源其个人Claude Code设置`gstack`，包含23个定制工具，可模拟CEO、设计师、工程师等角色。这些工具通过自然语言调用，将复杂工作流封装为可复用命令。

**关键点**：配置本身就是一套Agentic工作流模板，展示了如何用Claude Code构建多角色协作系统。**为什么重要**：顶级创业者公开其生产力工具链，为开发者提供了高价值的参考范式，尤其适合快速原型验证场景。

> 原文：https://github.com/garrytan/gstack

## OpenMontage：全球首个开源Agent视频制作系统

OpenMontage提供12条流水线、52个工具、500+技能，将AI编码助手变为视频工作室。支持脚本生成、素材采集、剪辑合成等全流程，用户通过对话即可生成完整视频。

**关键点**：Agent能力从代码扩展到多媒体创作，且完全开源。**为什么重要**：降低了视频制作门槛，让开发者能定制自己的“AI视频工厂”，有望推动教育、营销等领域的智能化内容生产。

> 原文：https://github.com/calesthio/OpenMontage

## Voicebox：开源AI语音工作室，一栈式语音处理

Voicebox集声音克隆、实时听写、语音合成为一体，提供完整的语音AI能力。无需调用多个API，本地部署即可实现从语音输入到输出的全链路处理。

**关键点**：支持声音克隆（几秒样本即可）、实时听写（低延迟）、多风格语音合成。**为什么重要**：为语音交互应用提供了开源替代方案，尤其适合数据敏感或需要离线运行的场景。

> 原文：https://github.com/jamiepine/voicebox

## NVIDIA Skills：官方AI Agent技能库，加速企业落地

NVIDIA开源其AI代理技能集合，涵盖数据分析、系统监控、自动化运维等生产用例。每个技能封装为可独立部署的模块，支持与企业现有系统集成。

**关键点**：技能由NVIDIA官方维护，针对GPU环境优化，包含对RAG、工具调用等模式的参考实现。**为什么重要**：企业可直接复用经验证的技能，大幅缩短Agent从原型到生产的周期。

> 原文：https://github.com/NVIDIA/skills

## AWS Agent Toolkit：官方MCP服务器与技能插件

AWS开源官方Agent开发工具包，包含MCP（Model Context Protocol）服务器、技能和插件。支持与AWS服务深度集成，如S3、Lambda、Bedrock等，帮助开发者在云端构建AI代理。

**关键点**：提供标准化MCP接口，技能可跨Agent框架复用。**为什么重要**：AWS的入局定义了Agent与云服务交互的官方规范，推动生态走向兼容和可组合。

> 原文：https://github.com/aws/agent-toolkit-for-aws

## Anthropic Claude Code插件官方目录

Anthropic官方维护Claude Code插件仓库，提供经过审核的高质量插件，涵盖代码分析、文档生成、测试等场景。插件采用标准化接口，即装即用。

**关键点**：官方背书保障质量和安全性，降低开发者选择成本。**为什么重要**：标志着Claude Code生态从社区自发生长转向官方治理，插件市场雏形初现。

> 原文：https://github.com/anthropics/claude-plugins-official

## 字节跳动DeerFlow：长时SuperAgent框架

字节跳动开源DeerFlow，支持研究、编码、创作三种模式，集成沙箱、记忆、工具和子代理架构，可处理分钟级复杂任务。与普通Agent不同，DeerFlow强调长期规划和状态持续。

**关键点**：支持任务中途暂停、恢复，子代理可独立执行子任务。**为什么重要**：长时任务处理是Agent落地的核心瓶颈之一，DeerFlow提供了工程化解决方案，尤其适合自动化科研和代码开发场景。

> 原文：https://github.com/bytedance/deer-flow

---

当开源生态同时涌出八个Agent相关项目，问题已不再是“要不要用Agent”，而是“用哪个框架来组合你的Agent”。