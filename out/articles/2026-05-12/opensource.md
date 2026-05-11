# 自改进 Agent 登顶，字节加入桌面 Agent 战局

今天最值得关注的是 Nous Research 开源自改进 Agent Hermes Agent 以 2240 亿日 Token 量登顶 OpenRouter 全球排名，超越此前领先的 OpenClaw——这直接表明 self-improving agent 正从实验室走向生产，开始吃掉推理市场的真实份额。与此同时，字节跳动、Anthropic、Addy Osmani 等纷纷开源 Agent 栈和技能包，开源 Agent 基础设施的拥挤程度已达到前所未有的水平。

## Hermes Agent 超越 OpenClaw 登顶 OpenRouter 全球日 Token 排名

Nous Research 开源自改进 Agent Hermes Agent 自上周发布后，日 Token 消耗量迅速攀升至 2240 亿，登顶 OpenRouter 平台。它通过自动生成训练数据、自我纠错和迭代微调实现性能提升，而非依赖手动 RLHF。关键点在于：Token 用量直接反映了开发者对模型能力的信任——这不是刷榜分数，而是真实的推理需求。为什么重要：自改进范式可能打破“更大模型更好”的假设，让中等规模 Agent 通过自我对齐持续优化，从而降低推理成本。

> 原文：https://github.com/NousResearch/hermes-agent

## 字节跳动开源 UI-TARS-desktop 多模态 Agent 栈

字节跳动开源的 UI-TARS-desktop 提供了一个完整的多模态 AI Agent 堆栈，涵盖 GUI 理解、视觉 grounding、动作规划等模块，可直接对接前沿 VLM 模型。关键点在于：它内置了跨桌面应用的操控能力（如鼠标、键盘模拟），并支持动态 UI 元素定位。为什么重要：这降低了企业构建“屏幕 agent”的门槛——以前需要自研从图像到动作的 pipeline，现在可以开箱即用，加速了 RPA 和桌面自动化的 AI 化进程。

> 原文：https://github.com/bytedance/UI-TARS-desktop

## Anthropic 开源金融服务业专用 Agent 技能包

Anthropic 开源的 Claude for Financial Services 项目，提供面向投行、股权研究、合规等场景的参考 Agent、技能模板和数据连接器（Bloomberg、FactSet 等）。关键点：技能包内嵌了金融领域特定的提示工程模式（如 DCF 模型推导、并购分析中的可比公司筛选），减少了从零设计的试错成本。为什么重要：金融服务业对合规和可解释性要求极高，Anthropic 将这些实践开源，等于向行业示范了“Claude 如何安全地处理敏感工作流”。

> 原文：https://github.com/anthropics/financial-services

## Addy Osmani 发布生产级 Agent 技能集合

Google 工程师 Addy Osmani 亲笔开源的 agent-skills，浓缩了其在 Chrome 性能和 AI 工具开发中的最佳实践，为 AI 编码 Agent 提供高质量技能模板（如 Git 工作流、代码审查、测试生成）。关键点：每个技能模板都附带可测试的提示模板和失败回溯逻辑，并非简单的 prompt 汇总。为什么重要：当大部分开源 Agent 仍停留在“玩具”阶段时，这份技能集合直接给出了生产环境下的设计模式，尤其适合 CI/CD 集成场景。

> 原文：https://github.com/addyosmani/agent-skills

## Memori：Agent 原生内存基础设施实现持久多会话

Memori 提供 LLM 无关的持久化内存层，将 Agent 执行轨迹和对话转化为结构化状态，支持跨会话回忆与共识构建。关键点：它不只是缓存原始对话，而是通过语义压缩和关系图维护长期上下文，且不与任何特定模型绑定。为什么重要：当前多数 Agent 在长对话或任务中断后会丢失上下文，Memori 补上了这一缺失的“记忆层”，使得面向复杂工作流的 agentic system 成为可能。

> 原文：https://github.com/MemoriLabs/Memori

## GLM-OCR 开源：高精度快速 OCR 模型

智谱开源 GLM-OCR 模型，宣称在准确率、速度和全面性上达到新高度，尤其擅长多语言和复杂版面（表格、数学公式）识别。关键点：该模型基于 GLM 架构，通过专门设计的编码器-解码器 pipeline 优化了非标准字体和低质量图片的识别效果。为什么重要：OCR 是很多文档智能流程的瓶颈，GLM-OCR 开源后给开发者提供了一个无需调用付费 API 的高精度选项，尤其适合中文场景。

> 原文：https://github.com/zai-org/GLM-OCR

## 9Router：无限免费 AI 编码路由工具

9Router 支持通过 40+ 提供商免费调用 Claude、GPT、Gemini 等模型，提供自动故障转移、请求合并和 Token 优化（声称节省 40%）。关键点：它不限制免费层调用次数，但会通过队列和缓存策略平衡负载。为什么重要：对于预算敏感的独立开发者和小团队，9Router 大幅降低了多模型实验的试错成本，但也可能面临稳定性风险（依赖第三方免费额度）。

> 原文：https://github.com/decolua/9router

## Open WebUI：用户友好的本地 AI 界面

Open WebUI 持续更新，是目前最受欢迎的开源本地 AI 管理界面，支持 Ollama 和 OpenAI API 的统一控制面板，可管理多模型、多会话和文件上传。关键点：它不依赖任何专有服务，全部本地部署，且内置知识库 RAG 功能。为什么重要：对于注重隐私和离线需求的企业用户，Open WebUI 是连接本地推理后端与最终用户的默认选择，生态插件持续增长。

> 原文：https://github.com/open-webui/open-webui

当每一个 Agent 框架都声称自己是基础设施时，真正的差异化可能不在模型能力，而在记忆与技能的可复用性上。