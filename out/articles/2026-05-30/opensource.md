# 完全 AI 写代码的训练框架开源了？

面壁智能开启开源周，发布全球首个完全由 AI 编写的训练框架，性能超越英伟达基线。这标志着AI生成代码的质量已可挑战人类顶尖优化，同时Anthropic、微软等公司也在Agent工具链上密集开源，行业标准化与安全防护同步提速。

## 面壁智能开源周：首个AI自写训练框架面世
面壁智能发布多款开源模型和工具，最大亮点是**全球首个完全由 AI 编写的训练框架**，其训练速度超过英伟达官方基线。这意味着AI不仅用于辅助开发，开始直接从零生成生产级框架。团队在开源周内还将陆续放出更多组件，值得关注的是该框架的架构设计是否具备通用性。

> 原文：https://www.qbitai.com/2026/05/426542.html

## Anthropic 定义 Agent技能标准
Anthropic 开源 Skills 仓库，定义了一套 agent 技能（skill）的标准规范。该仓库支持 Claude Code、Codex、Cursor 等主流 agent 平台，旨在让开发者编写一次技能即可跨平台复用。这相当于为 Agent 生态确立一个“插件格式”，有助于降低碎片化风险。

> 原文：https://github.com/anthropics/skills

## 微软开源RAMPART：Agent安全测试框架
微软发布 RAMPART，一个基于 pytest 的**原生安全测试框架**，专为 Agentic AI 应用设计。它允许开发者编写自动化测试用例来检测 agent 的权限滥用、提示注入、工具误调用等安全隐患。在 agent 部署前引入安全测试，能减少“AI越狱”类事件在生产环境中的影响。

> 原文：https://github.com/microsoft/RAMPART

## MOSS-TTS 开源：高保真语音生成全家桶
MOSI.AI 与 OpenMOSS 团队联合开源 MOSS-TTS 家族，覆盖长语音、多语言及高表现力场景。模型支持零样本声音克隆，在情感合成和语音自然度上表现突出。对于需要定制语音助手的开发者，这是一个无需闭源API即可本地部署的选项。

> 原文：https://github.com/OpenMOSS/MOSS-TTS

## Claude Code 动态工作流深度解析
有开发者深入分析 Claude Code 的源代码，披露了文档未写明的**大量可配置项**，包括动态工作流调度、上下文窗口管理以及自定义工具链的底层接口。这些发现让高阶用户能够绕过 API 限制，直接调整 agent 的行为细节——但也提醒用户注意版本兼容风险。

> 原文：https://buildingbetter.tech/p/i-read-the-claude-code-source-code

## Datasette 1.0a31 小版本更新
Datasette 发布 1.0alpha31，带来两个新功能：插件可定义导出格式的方式被简化，以及新的数据预览可视化组件。对于 SQLite 数据探索爱好者，这是一个持续改进的“小而美”工具，但本次更新没有破坏性变更。

> 原文：https://github.com/simonw/datasette/releases/tag/1.0a31

---

今天的开源消息集中在“AI写代码”与“Agent标准化”两个方向：AI自产的训练框架是否真的能替代人类？当每一家公司都开始定义自己的 agent 技能标准，碎片化与兼容性之间的矛盾将如何解决？