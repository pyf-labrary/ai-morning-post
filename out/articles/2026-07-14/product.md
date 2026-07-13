# Claude Code 浏览器上线，AI 自主操作网页

AI 应用产品今日迎来「工具化」关键拐点：Claude Code 新增内置浏览器，AI 首次能像人类一样读取、点击、输入外部网页；同时阶跃星辰发布全球首款大模型原生智能体手机 STEPX Neo，终端 OS 从人机交互转向 Agent 自主交互。这意味着 AI 应用正从「会话」走向「执行」。

## Claude Code 内置浏览器，AI 可自主操作外部网页

Anthropic 旗下开发工具 Claude Code 新增内置浏览器功能。现在，AI 可以读取任意公开网页、定位页面元素、模拟点击并输入文本——就像一个人在使用浏览器。这意味着开发者可让 Claude 自动完成表单填写、数据抓取、SaaS 操作等复杂流程。此前 Claude Code 主要处理代码文件，现在能力外延至网页交互，大幅扩展了自动化边界。

> 原文：https://the-decoder.com/claude-code-now-has-a-built-in-browser-that-lets-the-ai-read-click-and-type-on-external-websites/

## 阶跃星辰发布智能体手机 STEPX Neo，OS 原生支持 Agent

阶跃星辰推出全球首个大模型原生智能体终端 STEPX Neo，搭载自研 Step AOS（Agentic-native OS）和智能体「阶跃 Amoo」。与传统手机不同，这台设备的系统层直接整合了语言模型与上下文感知能力，第三方应用可通过统一 Agent 接口调用。本质上是将一个端侧大模型作为操作系统的「核心调度器」，而非单纯的语音助手插件。这指向一条不同于苹果和安卓的硬件路线：先定义 Agent 交互范式，再适配应用生态。

> 原文：https://36kr.com/newsflashes/3894017412726018?f=rss

## Waze 集成 Gemini AI，增强导航个性化

Google 旗下导航应用 Waze 正在利用 Gemini 模型推出 AI 驱动的个性化导航功能，包括根据驾驶习惯推荐路线、实时路况预测、以及更自然的语音交互。这是 Waze 在 Google Maps 和 Apple Maps 之间维持差异化的重要动作。对于应用产品团队而言，这说明 AI 正在从「聊天界面」渗透到传统工具型 App 的核心体验层。

> 原文：https://techcrunch.com/2026/07/13/waze-adds-new-ai-powered-features-and-customization-updates/

## Siri AI 升级为苹果「万能工具」，iOS 27 公测开放

重新设计后的 Siri 在 iOS 27 公测版中不再只是语音助手：它成为 iPhone 的系统级 AI 骨干，可以跨应用执行复杂任务（如从邮件中提取事件创建日历项，再通过短信发送通知）。苹果采用了端侧推理优先、云端为辅的架构。关键变化在于，Siri 现在可以「看到」屏幕内容，并基于上下文操作非 Apple 原生应用。这对第三方开发者的接入策略和用户隐私预期都会产生深远影响。

> 原文：https://www.wired.com/story/siri-ai-is-now-apple-everything-tool/

## Claude Code 与 OpenCode token 开销对比：差距超 4 倍

开发者社区实测发现，在相同 Prompt 下，Claude Code 在读取提示前会发送约 33k 个 token（含系统提示、上下文等），而开源方案 OpenCode 仅发送约 7k 个 token。虽然 Claude Code 提供了更强大的内置能力（如浏览器、沙箱），但对于高频调用的开发者，token 开销直接对应成本。这一对比提示：选择 AI 生产力工具时，不应只看输出质量，隐形的 token 预填充成本也需评估。

> 原文：https://systima.ai/blog/claude-code-vs-opencode-token-overhead

## OpenAI 更新提示指南：别再过度思考，直接从结果出发

OpenAI 发布新版官方提示工程指南，核心建议是「从期望结果开始写提示」，而非让 AI 逐步推理（chain-of-thought）。新方法认为，直接描述输出格式、内容结构和风格，比让模型「思考每一步」更高效。这反映出模型本身推理能力增强后，用户「过度引导」反而画蛇添足。对产品经理和开发者而言，这意味着需要重新训练团队怎么写 Prompt，而不是盲目堆砌「请一步步思考」。

> 原文：https://the-decoder.com/openais-new-prompting-guide-tells-users-to-stop-overthinking-and-start-with-the-result/

## Agent 专用搜索登顶 Product Hunt，由中国团队打造

一款名为「Agent Search」的搜索引擎产品登上 Product Hunt 日榜第一，由国内团队开发，专为 AI Agent 设计。核心卖点包括更低的 token 消耗和更高的结果相关性——在调用大模型前，该搜索先对网页进行结构化处理，压缩无效内容。对于正在构建 Agent 的团队，这可能是一个降低 API 成本的有效基础设施。

> 原文：https://www.qbitai.com/2026/07/449327.html

---

AI 的能力天花板正在被「与真实网页交互」的实际操作所打破。问题是：当 Agent 可以替你填表、导航、甚至操作手机，开发者准备好让出控制权了吗？