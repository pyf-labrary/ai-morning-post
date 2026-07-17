# AI晨报：游戏杆掌控Agent，明星也能AI化

OpenAI 今天推出了 Codex Micro——一款可编程游戏杆控制器，让开发者用摇杆和旋钮操作编码 Agent，而非打字。与此同时，千问将 AI 眼镜升级为智能体眼镜，支持语音、眼动和第三方 Skill 调用。AI 应用正从纯软件向着硬件化、多模态交互加速演进。

## OpenAI 发布 Codex Micro：一个用于控制 AI 代理的物理游戏杆

**是什么**  
OpenAI 推出 Codex Micro，一个可编程游戏杆控制器，专为控制 AI 编码代理（Codex agent）设计，配备旋钮和 LED 指示灯。开发者可以通过物理摇杆来导航代码、选择片段、执行命令，不再依赖键盘输入。

**关键点**  
- 产品形态：类似游戏手柄，但只有摇杆、几个按钮和旋钮，极简交互。  
- 目标用户：使用 Codex 进行编程的开发者，尤其是沉浸式编码场景。  
- 定位：并非替代终端，而是为 agentic coding 提供一种更直觉的操控方式。

**为什么重要**  
这是 OpenAI 从纯软件跨入硬件的标志性一步。它暗示着 AI 代理的交互范式正在从“命令行+自然语言”向“物理控制+多模态”演进。如果成功，可能会催生一类新的开发者外设。

> 原文：https://the-decoder.com/openai-wants-developers-to-stop-typing-commands-and-start-using-a-joystick-to-control-their-ai-agents/

## Google Vids 加入 AI 化身功能，用户可“参演”视频

**是什么**  
Google Vids 推出个性化 AI 头像功能，用户可以创建自己的数字分身，并让该分身出现在生成的视频中。同时集成 Gemini Omni 工具，支持多模态内容编辑。

**关键点**  
- 用户上传几张照片即可生成数字分身，可调整表情、动作、背景。  
- 视频内容完全由 AI 生成，用户只需提供脚本或提示。  
- 集成 Gemini Omni，可同时处理文本、图像、语音，让视频制作更流畅。

**为什么重要**  
这标志着“人人皆可演”的视频生成产品化落地，降低了 UGC 视频的门槛。对于产品经理和内容创作者而言，这是快速制作个性化视频（如营销、培训）的实用工具，也展示了头部平台如何将多模态模型无缝嵌入现有产品。

> 原文：https://techcrunch.com/2026/07/16/google-vids-now-lets-you-star-in-your-own-ai-videos/

## Roblox 移动端上线 AI 一键生成游戏

**是什么**  
Roblox 在其移动应用中推出“Build”功能，用户只需输入文字提示（如“一个海盗冒险岛”），即可自动生成基础游戏场景、角色和交互逻辑。

**关键点**  
- 面向移动端用户，降低游戏创建门槛至“一句话”。  
- 生成的游戏虽为基础框架，但可后续手动调整。  
- 填补了 Roblox 在移动端无原生创作工具的空白。

**为什么重要**  
Roblox 的生态核心是 UGC 游戏，AI 生成功能可能大幅扩大创作者基数，同时改变平台内容供给结构。投资人应关注该功能是否会稀释高质量游戏占比，或带来新的 monetization 模式（如生成即变现）。

> 原文：https://techcrunch.com/2026/07/16/roblox-launches-an-ai-powered-game-creation-feature-in-its-mobile-app/

## Google AI Mode 升级：从回答问题到跨应用执行任务

**是什么**  
Google 扩展了 AI Mode 的能力，用户现在可以将其与第三方应用（如日历、邮件、购物清单等）链接，实现跨应用任务执行。例如“根据下周的会议安排，在 DoorDash 上预订午餐”。

**关键点**  
- 支持的应用列表正在扩展，首批包括 Gmail、Google Calendar、DoorDash、Spotify 等。  
- 用户授权后，AI Mode 可以直接在应用中执行操作（创建事件、下单等）。  
- 本质是 Agentic 能力的开放，将搜索从信息检索升级为行动引擎。

**为什么重要**  
这是 Google 构建“AI 操作系统”的关键一步。跨应用任务执行意味着 Google AI Mode 正在成为用户与第三方服务之间的智能中转站。对于开发者，这意味着需要为 AI Agent 准备可被调用的 API 或 action 端点。

> 原文：https://techcrunch.com/2026/07/16/googles-ai-mode-now-lets-you-link-and-interact-with-select-apps/

## DoorDash 推出命令行工具 dd-cli，专为 AI Agent 设计

**是什么**  
DoorDash 开放 dd-cli 公测，允许开发者通过终端搜索餐厅、构建购物车并直接下单。该工具尤其是为 AI Agent（如代码代理、自动化脚本）设计的。

**关键点**  
- 支持 `doordash search "pizza"`, `doordash add-item`, `doordash checkout` 等命令。  
- 输出结构化 JSON，方便 Agent 解析。  
- 旨在让 AI 能够代表用户完成外卖点餐这一高频任务。

**为什么重要**  
这代表了消费级服务在 Agentic 时代的基础设施建设——为 AI 提供可编程接口。DoorDash 主动适配 AI Agent 的趋势，可能成为其他本地生活服务的范本。对于技术从业者，这意味着可以自定义自动化流程（如“下班时自动点餐”）。

> 原文：https://techcrunch.com/2026/07/16/yes-you-can-now-order-doordash-from-the-command-line/

## Google NotebookLM 正式更名 Gemini Notebook，开放搜索应用集成

**是什么**  
Google 将 NotebookLM 重新品牌为 Gemini Notebook，并将底层的搜索应用能力开放给第三方集成，允许其他应用使用其多模态搜索与摘要功能。

**关键点**  
- 命名统一到 Gemini 品牌下，增强认知一致性。  
- 开放的搜索应用 API 允许开发者将 Notebook 的搜索+推理能力嵌入自己的产品。  
- 原有用户数据、笔记功能不受影响。

**为什么重要**  
更名意味着 Google 正在将 NotebookLM 从实验性产品升级为平台级能力。第三方集成可能催生知识管理、企业文档搜索等场景的新应用。产品经理可以思考如何利用 Gemini Notebook 的底层能力提升自家产品的信息处理效率。

> 原文：https://the-decoder.com/google-rebrands-notebooklm-as-gemini-notebook-and-opens-its-search-app-to-third-party-integration/

## 千问 AI 眼镜升级为智能体眼镜，支持全双工语音与眼动追踪

**是什么**  
千问宣布其 AI 眼镜升级为“智能体眼镜”（Agent Glasses），支持按需调用第三方 Skill 和 Agent，新增全双工语音交互、眼动追踪等功能。

**关键点**  
- 全双工语音：用户无需唤醒词即可持续对话。  
- 眼动追踪：可通过视线选择菜单、确认操作。  
- 第三方 Agent/Skill 生态：类似手机应用商店，但面向眼镜场景（如导航、翻译、购物）。

**为什么重要**  
这是 AI 可穿戴设备从“AI 助手”向“AI 代理平台”演变的一个实例。与 OpenAI 的游戏杆不同，千问选择眼镜作为 Agent 的物理载体，强调“解放双手”场景。产品经理可关注其第三方生态如何构建，以及能否复制手机应用商店的飞轮效应。

> 原文：https://www.leiphone.com/category/industrynews/JDlu3Gqj7atcWniy.html

## OpenAI 推出 ChatGPT 品牌篮球（没错，是篮球）

**是什么**  
OpenAI 发布了一款印有 ChatGPT 标志的篮球，这是其首个“硬件”产品（非 Codex Micro），售价不明。该产品引发社交媒体热议和困惑。

**关键点**  
- 与篮球无关，与 AI 无关，纯粹是品牌周边。  
- 可能是营销噱头，也可能是对“AI 硬件”概念的一种解构。  
- 引发“OpenAI 为什么卖篮球”的讨论，热度远超实际价值。

**为什么重要**  
对于一家估值数千亿美元的公司来说，推出周边产品通常意味着品牌建设进入快车道。但相比 Codex Micro 的严肃硬件，篮球更像一个信号：OpenAI 愿意尝试非理性营销，以扩大品牌大众认知。投资人不必过度解读，但它提醒我们：AI 公司也需要“文化符号”。

> 原文：https://techcrunch.com/2026/07/16/why-is-openai-selling-a-chatgpt-basketball/

---

今天的产品线清晰地分为三条路：AI 控制硬件（游戏杆、眼镜）、AI 化身/生成（Vids、Roblox）和 AI 行动引擎（Google AI Mode、dd-cli）。你会为哪个场景写第一行代码？