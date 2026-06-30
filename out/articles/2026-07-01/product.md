# Anthropic出招：科研工作台，而非新模型

今日最值得关注的不是另一个更强大的模型，而是**Anthropic为科学家打造的AI工作台Claude Science**——它绕过“模型军备竞赛”，试图通过工作流整合成为科研基础设施。与此同时，开源Agent项目OpenClaw登陆手机，Agent开始真正渗透日常使用场景；Acti则把Agent塞进手机键盘，用自然语言定义快捷操作。产品层面的Agent化正在从“演示”走向“可用”。

## Claude Science：AI不再只是聊天，而是科研工作台

Anthropic今日发布Claude Science，一个专为科学家设计的AI工作台。它不是一个新的模型版本，而是整合了数据库、计算管道和工具链的平台，旨在辅助计算研究的全流程。**关键点**：Claude Science聚焦于“工作流”而非模型能力，允许科学家直接在其环境中运行脚本、管理数据、调用API，并与Claude对话式交互。**为什么重要**：科研领域长期以来面临工具碎片化问题，Claude Science试图成为统一的AI副驾驶，降低研究者使用AI的门槛。这种“平台化”策略可能比单纯提升模型参数更实际，尤其对于需要复现性和可审计性的学术工作。

> 原文：https://techcrunch.com/2026/06/30/anthropics-claude-science-bets-on-workflow-not-a-new-model-to-win-over-scientists/

## OpenClaw移动端上线：开源Agent进入口袋

OpenClaw正式登陆Android和iOS，将开源Agent能力带入手机。此前OpenClaw主要在桌面端运行，移动端版本保留了核心的自主执行与工具调用功能。**关键点**：用户可在手机上配置Agent完成自动化任务，如日程管理、信息检索、API触发等；代码完全开源，支持自定义行为。**为什么重要**：这是开源Agent首次大规模进入移动生态，打破了封闭厂商对手机Agent的垄断。对于开发者而言，可以在手机上运行自研Agent，极大降低实验和部署成本。

> 原文：https://techcrunch.com/2026/06/30/openclaw-is-finally-available-on-android-and-ios/

## Acti推出AI键盘Agent：自然语言即快捷键

Acti让用户通过自然语言创建AI快捷键，嵌入手机键盘直接调用Agent操作不同应用。**关键点**：用户输入例如“一键翻译当前屏幕并发送给同事”，Acti会生成对应的Agent快捷方式；支持跨应用链式操作。**为什么重要**：键盘是移动端最底层的交互入口，Acti把Agent“压缩”成快捷键，降低了Agent的使用摩擦。这意味着Agent不再需要独立的App或网页界面，而是融入系统级输入体验。

> 原文：https://techcrunch.com/2026/06/30/acti-puts-ai-agents-directly-into-your-smartphone-keyboard/

## X推出MCP服务器：降低AI工具接入门槛

X（原Twitter）发布托管MCP（Model Context Protocol）服务器，使开发者能更轻松地将AI应用与X API集成。**关键点**：MCP是Anthropic提出的开放协议，允许AI模型直接调用外部工具和API；X的MCP服务器封装了数据读写、发推、搜索等能力。**为什么重要**：社交媒体平台主动拥抱AI协议，意味着Agent可以更顺畅地抓取、发布和交互社交媒体数据。对于构建社交类Agent或监控工具的产品，集成成本将显著下降。

> 原文：https://techcrunch.com/2026/06/30/x-now-offers-an-mcp-server-to-make-its-platform-easier-for-ai-tools-to-use/

## Cursor移动App：远程监督编码Agent

Cursor发布手机应用，允许开发者远程监督和引导编码Agent。**关键点**：用户可在手机上查看Agent生成的代码变更、接受或拒绝建议、添加注释提示；支持与桌面端Cursor同步。**为什么重要**：编码Agent的“无人值守”场景一直被诟病——开发者无法时刻在电脑旁。移动App提供了轻量级遥控能力，让Agent可以在后台持续工作，而开发者通过手机审查控制，提升了Agent作为编码伙伴的实用性。

> 原文：https://techcrunch.com/2026/06/29/cursor-now-has-a-mobile-app-for-guiding-your-coding-agent-on-the-go/

## Tidal打击AI音乐：切断AI生成曲目收益

Tidal宣布使用自动工具检测并移除冒充艺术家的AI生成音乐，停止其变现。**关键点**：Tidal将标识出音色、风格与特定真人艺术家高度相似的AI生成曲目，并阻止其上传和获得流媒体分成。**为什么重要**：音乐平台开始主动清退AI擦边球内容。这预示着AI音乐创作的版权与原创性争议将进一步激化，对AI音乐生成器和音乐平台的政策走向具有示范效应。

> 原文：https://techcrunch.com/2026/06/29/tidal-cracks-down-on-ai-music-by-cutting-off-monetization/

## Proton AI聊天机器人Lumo升级至2.0

Proton的隐私AI聊天机器人Lumo推出2.0版，主要更新包括更长的上下文记忆、支持文档上传分析以及更强的端到端加密。**关键点**：Lumo 2.0承诺用户对话数据仅存储在本地，Proton无法查看；增加了对PDF、Office文档的处理。**为什么重要**：在主流AI聊天工具普遍依赖云端分析的背景下，Lumo坚守隐私底线。对于注重数据安全的团队（如律所、医疗），Lumo提供了与GPT类产品不同的替代选项。

> 原文：https://techcrunch.com/2026/06/30/lumo-protons-privacy-focused-ai-chatbot-gets-an-upgrade/

## Google Gemini个性化图像生成向美国免费用户开放

Google允许美国免费用户基于个人数据生成个性化图像——例如根据用户相册中的照片风格生成新图像。**关键点**：用户可上传自己的照片或授权Google使用其相册数据，Gemini会学习面部特征、风格偏好，生成融入个人元素的图像。**为什么重要**：这是Google将大模型与个人数据结合的一次大众化尝试，可能推动“个人化AI创作”走向主流。但隐私风险和数据使用边界问题也值得关注。

> 原文：https://techcrunch.com/2026/06/29/geminis-personalized-ai-image-generation-is-now-free-for-u-s-users/

---

当Agent从“对话”进化到“工作台+键盘+移动监督”，你准备好让AI替你管理科研、社交和代码审查了吗？