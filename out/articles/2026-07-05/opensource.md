# 开源新招：PNG藏代码省60% token

今日开源工具板块最值得关注的是 pxpipe——它把代码文本嵌入 PNG 图片，利用模型 OCR 读取，从而大幅降低 token 消耗。视觉 token 成本远低于文本，这种反直觉思路可能成为 AI 编码效率的新法宝。同时，微软、腾讯云等大厂也在 Agent 安全治理上补齐工具链。

## pxpipe：将代码藏进 PNG，token 省 60%

**是什么**  
pxpipe 是一款开源工具，将代码或文本转换为 PNG 图片，再让 AI 模型通过 OCR 读取内容，从而绕过文本 token 计费方式。测试显示在 Claude Code 和 Fable 5 上能节约约 60% 的 token 消耗。

**关键点**  
- 原理：将文本渲染为图片，利用视觉模型的 OCR 能力还原。  
- 效果：token 成本降低 60–70%（取决于输入长度）。  
- 适用场景：连续代码补全、多轮对话中重复上下文。

**为什么重要**  
AI 编码工具按 token 计费，长上下文（如整个文件）成本高企。pxpipe 提供了一种边际成本趋近于零的“作弊”方式，可能倒逼平台调整计价策略，或催生更多类似优化 hack。

> 原文：[The Decoder](https://the-decoder.com/open-source-tool-pxpipe-hides-text-in-pngs-to-cut-claude-code-and-fable-5-token-costs-up-to-70/)

## Caveman：用原始人语让 Claude Code 省 65% token

**是什么**  
Caveman 是一个 Claude Code 的 skill 配置文件，通过限制词汇量到最基础的几百个单词（类似原始人说话）来压缩 prompt 长度。

**关键点**  
- 原理：使用极简句式（如“me hungry”代替“I am hungry”）。  
- 效果：在同等功能描述下减少约 65% token。  
- 开源 GitHub 仓库附带 prompt 模板。

**为什么重要**  
与 pxpipe 异曲同工，都指向同一个痛点：AI 编码的 token 成本敏感。Caveman 更“软”——不依赖 OCR，仅靠语言压缩。这说明行业对 token 优化已从工程 hack 延伸到 prompt 设计范式。

> 原文：[GitHub](https://github.com/JuliusBrussee/caveman)

## 微软开源 AI Agent 治理工具包

**是什么**  
Agent Governance Toolkit 是微软开源的 Agent 安全治理框架，覆盖 OWASP Agentic Top 10 威胁，提供策略执行、零信任身份、沙箱隔离等能力。

**关键点**  
- 组件：策略引擎、身份模块、沙箱运行时。  
- 适用：任何基于 LLM 的 agent 系统，支持集成。  
- 开源协议 MIT。

**为什么重要**  
Agentic 安全是 2026 年核心议题。微软此举把企业级治理能力下放到社区，意味着 agent 部署不再只能依赖云平台闭源方案，小型团队也能基于此构建合规安全代理。

> 原文：[GitHub](https://github.com/microsoft/agent-governance-toolkit)

## Hugging Face 开源本地语音 Agent 框架

**是什么**  
Speech-to-Speech 是一套完全本地、无需云端的语音 agent 框架，支持在端侧用开源模型构建端到端语音对话。

**关键点**  
- 全栈：语音识别→意图理解→语音合成均本地执行。  
- 模型支持：可选 Whisper、Moshi 等开源模型。  
- 低延迟：优化后 200ms 内响应。

**为什么重要**  
语音 agent 一直依赖云端 API，本地方案解决了隐私与延迟痛点。Hugging Face 背书意味着社区可快速基于此搭建离线语音助手，尤其适合智能硬件和边缘场景。

> 原文：[GitHub](https://github.com/huggingface/speech-to-speech)

## 腾讯云开源 CubeSandbox：AI Agent 即时沙箱

**是什么**  
CubeSandbox 为 AI Agent 提供安全、轻量、并发的隔离执行环境，支持在几毫秒内创建沙箱。

**关键点**  
- 技术：基于容器和用户态内核隔离，资源开销低。  
- 并发：单节点可支撑数千并行沙箱。  
- 场景：AI agent 执行第三方代码、访问网络等。

**为什么重要**  
Agent 执行安全是规模化部署的一大障碍。腾讯云将自家内部方案开源，填补了 agent 沙箱领域的空白，相比通用沙箱更适配 LLM 的高频创建需求。

> 原文：[GitHub](https://github.com/TencentCloud/CubeSandbox)

## OpenAI 开源 Codex 插件，供 Claude Code 使用

**是什么**  
OpenAI 发布 Codex 的 Claude Code 插件，使 Claude Code 能调用 Codex 进行代码审查和任务委派。

**关键点**  
- 互操作性：Claude Code 通过插件集成 OpenAI Codex。  
- 功能：代码审查、重构建议、子任务分配。  
- 官方维护，支持多语言。

**为什么重要**  
这是罕见的跨厂商工具协作案例。OpenAI 主动向竞争对手生态开放能力，可能推动 agent 间的互操作标准，但更可能是为了推广 Codex API 使用量。对开发者而言，可以同时利用两家模型优势。

> 原文：[GitHub](https://github.com/openai/codex-plugin-cc)

## Strix：开源 AI 渗透测试工具

**是什么**  
Strix 是一套利用 AI 自动发现应用漏洞并进行渗透测试的开源工具。

**关键点**  
- 自动化：AI 生成测试用例、执行攻击、分析结果。  
- 覆盖：OWASP Top 10 及常见逻辑漏洞。  
- 支持 CI/CD 集成。

**为什么重要**  
传统渗透测试依赖手动经验和工具链。AI 驱动的 Strix 降低了门槛，也引发了关于安全工具被恶意使用的讨论。对于 DevOps 团队，可以低成本纳入安全左移流程。

> 原文：[GitHub](https://github.com/usestrix/strix)

## Chrome DevTools MCP：让编码 Agent 调试浏览器

**是什么**  
Chrome DevTools 团队发布 MCP（Model Context Protocol）服务器，允许 AI 编码 agent 直接控制和调试浏览器（如操作 DOM、截取屏幕、检查网络请求）。

**关键点**  
- 基于 MCP 标准，兼容 Claude Code、Cursor 等 agent。  
- 能力：打开页面、点击、表单填写、截图回传。  
- 开源，Google 官方维护。

**为什么重要**  
AI agent 在浏览器自动化上长期依赖 Playwright 等工具，但缺少 DevTools 级别的诊断接口。该 MCP 服务器让 agent 能像人类开发者一样使用调试面板，大幅提升复杂网页交互的准确性。

> 原文：[GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)

---

今天的开源工具主线清晰：token 成本、Agent 安全、互操作。当大家都在堆功能时，pxpipe 选择从计价规则上“作弊”——这或许才是 2026 年最聪明的优化。你会放心把代码交给机器人，再用机器人读图片吗？