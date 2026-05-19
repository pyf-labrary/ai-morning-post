# Cursor 2.5追平GPT-5.5，谷歌多线出击

昨天应用产品领域最值得关注的两条线：Cursor用十分之一成本追上最强推理模型，Google I/O则一口气发布了独立agent平台、全天候个人助手、全面改造的搜索和新的订阅体系。模型层的成本曲线在陡峭下探，应用层的平台战争正式开打。

## Cursor 发布 Composer 2.5，性能追平 Opus 4.7 和 GPT-5.5

**是什么**：Cursor推出Composer 2.5模型，在编程agent评测中达到甚至超越Opus 4.7和GPT-5.5的水平，但推理成本仅为后者的十分之一。

**关键点**：该模型在复杂多步骤编程任务上的表现突出，意味着当前AI编程工具的性价比拐点已经到来——低成本模型正在逼近甚至持平顶级闭源模型的能力。

**为什么重要**：对于正在做技术选型的技术团队和投资前沿模型的机构，Cursor 2.5的数据信号很明显：模型本身的壁垒正在被压缩，产品体验、生态集成和成本控制将成为新的竞争关键。

> 原文：https://cursor.com/blog/composer-2-5

## 谷歌推出 Antigravity 2.0：独立 agent 平台

**是什么**：Google I/O 2026上发布了Antigravity 2.0，包括桌面应用和CLI工具，支持agent编排和企业级部署。

**关键点**：这是Google将agent作为独立平台而非附属于搜索或助手的重要一步。桌面端和CLI双模态覆盖了开发者和普通用户，企业级部署能力则对标AWS Bedrock或Azure AI。

**为什么重要**：Google终于补上了“agent基础设施”这一环，未来可能通过GCP和Workspace生态快速渗透企业市场，与Anthropic的Managed Agents形成直接竞争。

> 原文：https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/

## 谷歌推出 Gemini Spark：全天候 agent 个人助手

**是什么**：基于Gemini模型和Antigravity框架的24/7 agentic个人助手，集成Gmail、购物、日历等。

**关键点**：Gemini Spark能持续运行任务（如监控邮件并自动处理），与手机、桌面深度绑定。这是Google对“AI私人管家”类产品的正式回应，直接对标三星/苹果的类似方向。

**为什么重要**：对于产品经理和投资人，这意味着“常驻agent”从理念进入规模化部署阶段，而Gmail和购物数据的打通将带来隐私与便利的新平衡点。

> 原文：https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/

## 谷歌全面改造搜索：AI 结果取代链接列表

**是什么**：Google Search升级为AI驱动的对话式、agentic体验，引入信息agent、统一购物车等功能。

**关键点**：传统蓝色链接几乎消失，搜索直接生成答案或执行任务（如比价、下单），用户不再需要跳转网站。

**为什么重要**：这是Google搜索引擎历史上最激进的转型。电商、内容出版、SEO行业将面临重新洗牌，而agent购物车可能重塑在线零售基础设施。

> 原文：https://blog.google/products-and-platforms/products/search/search-io-2026/

## 谷歌推出 AI 订阅三档计划，起价 $10/月

**是什么**：Google重构AI订阅体系，新增AI Ultra档（$100/月），提供5倍用量和Antigravity 2.0。

**关键点**：三档分别为基础（$10/mo）、增强（$20/mo）、Ultra（$100/mo），Ultra用户可率先使用Antigravity 2.0桌面版和CLI。

**为什么重要**：定价策略明确指向“高端专业用户”，与OpenAI的Pro层（$200/mo）形成竞争。$100/月档位兼顾开发者与企业需求，可能加速agent工具的普及。

> 原文：https://the-decoder.com/google-overhauls-its-ai-subscriptions-at-i-o-2026-with-three-tiers-starting-at-10-a-month/

## 谷歌发布 Android CLI，助力 agent 编程

**是什么**：Google推出Android命令行工具，支持Claude Code、OpenAI Codex等agent直接构建应用并部署到Android。

**关键点**：开发者可以用自然语言让agent编写Android app，然后通过CLI一键编译、签名、安装到设备。

**为什么重要**：Android开发门槛进一步降低，但更重要的是，agent编程从“脚本生成”升级到“完整应用交付”。移动端将成为agent编程的主战场之一。

> 原文：https://techcrunch.com/2026/05/19/agentic-app-coding-gets-an-upgrade-with-googles-release-of-android-cli/

## Cloudflare：Anthropic Mythos 发现此前未发现的漏洞链

**是什么**：Cloudflare报告Anthropic的Mythos预览版能自动发现复杂漏洞链，超越此前所有frontier模型。

**关键点**：Mythos在真实漏洞挖掘任务中展现出“链式推理”能力，能够组合多个看似无关的缺陷形成攻击路径。

**为什么重要**：安全是agent最被质疑的能力之一。Mythos的正向结果既验证了深层推理的价值，也带来新的担忧——如果攻击者用同样的模型优势，安全会变成博弈加速器。

> 原文：https://blog.cloudflare.com/cyber-frontier-models/

## Anthropic 为 Claude Managed Agents 增加自托管沙箱和 MCP 隧道

**是什么**：Anthropic为Claude Managed Agents推出自托管沙箱和MCP安全隧道功能。

**关键点**：企业可以将agent运行在自有基础设施上，并通过MCP隧道加密通信，解决数据驻留和安全审计需求。

**为什么重要**：企业采用agent的最大障碍是数据隐私。这一更新直接回应了合规要求，可能推动更多金融、医疗等行业客户入场。

> 原文：https://the-decoder.com/anthropic-adds-self-hosted-sandboxes-and-mcp-tunnels-to-claude-managed-agents/

---

当模型能力接近、平台生态就位的今天，你打算把第一个“全天候agent”派去做什么事？