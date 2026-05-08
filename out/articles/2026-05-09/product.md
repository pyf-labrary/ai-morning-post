# 零误报挖洞：AI抓虫Firefox 271个

今天最值得关注的是 Mozilla 利用 Anthropic 的 Claude Mythos Preview 实现了自动化漏洞挖掘流水线，在 Firefox 中发现 271 个此前未知漏洞，且声称几乎无误报。这一成果表明 AI 驱动的安全测试已从概念验证走向生产级规模化应用，误报率控制达到实用水平。对于关注 AI 工程化和安全自动化的团队，这组数据提供了可复现的参考基准。

## Mozilla 用 Claude Mythos 挖出 271 个零误报漏洞

**是什么：** Mozilla 安全团队基于 Anthropic Claude Mythos Preview 构建了一条全自动漏洞挖掘流水线，在 Firefox 浏览器中发现了 271 个从未被记录的安全漏洞，且报告中几乎无任何误报。

**关键点：** 该流水线并非简单提示模型生成测试用例，而是结合了定向 fuzzing 与 agentic 验证机制。Claude 能主动探索代码路径、构造 PoC，并自动过滤无效结果，使最终输出直接可被开发团队复现与修复。

**为什么重要：** 传统自动化漏洞挖掘面临高误报率与低覆盖率的矛盾，AI agent 的介入将两者同时优化。271 个漏洞的实绩证明，LLM 在代码安全审计中已具备替代部分人工的潜力，且“零误报”意味着可直接接入 CI/CD 管线，无需二次人工筛选。

> 原文：[Mozilla Hacks](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

## OpenAI 为 Codex 推出 Chrome 扩展，可操作网页应用

**是什么：** OpenAI 发布 Codex Chrome 扩展，使 AI 编码 Agent 能够直接与已登录的网页会话（如 LinkedIn、Salesforce、Gmail）及 Chrome DevTools 进行交互，大幅提升自动化操作的广度。

**关键点：** 该扩展绕过传统 API 限制，直接通过浏览器 DOM 与页面元素交互，支持登录态保持、表单填写、数据抓取等操作。Agent 在开发环境下可访问内部工具页面，实现端到端工作流自动化。

**为什么重要：** 这标志着 AI 编码 Agent 从“生成代码”向“操纵环境”演进。对 SaaS 产品团队而言，这意味着自动化测试、数据迁移、日常运维等方式将被重新定义；对平台方，则可能引发关于安全与策略合规的新讨论。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/05/08/openai-adds-chrome-extension-to-codex-letting-its-ai-agent-access-linkedin-salesforce-gmail-and-internal-tools-via-signed-in-sessions/)

## Google AI Overviews 增加更多来源链接

**是什么：** Google 宣布将在 AI Overviews 中更突出地显示来源链接，包括站内引用卡片和侧边栏源列表，以提升答案的透明度与可追溯性。

**关键点：** 新设计将引用从过去的浮动标签改为固定位置卡片，用户可一键跳转至原文；侧边栏新增“来源”模块，按相关性排序并显示域名权威度。此改动面向移动端与桌面端同步推送。

**为什么重要：** AI 生成的摘要一直因“黑箱”和“来源不明”而受诟病。Google 此举既是为了应对监管压力与媒体抗议，也是试图在保持流量分配的同时维持用户信任。对内容创作者而言，站长工具的可见性可能提升，但流量分配结构仍不透明。

> 原文：[Ars Technica](https://arstechnica.com/google/2026/05/google-will-put-more-links-to-websites-in-ai-overviews/)

## Perplexity Personal Computer 全面开放 Mac 版

**是什么：** Perplexity 的 AI 助手 Perplexity Personal Computer 现已在 Mac 上对所有用户开放，能够控制桌面应用、执行多步任务，类似一个系统级的 agent 助手。

**关键点：** 该助手通过辅助功能 API 与 macOS 交互，可自动打开应用、执行文件操作、搜索本地内容，并调用 Perplexity 的在线知识库。支持用户自定义工作流，例如自动整理截图、生成周报等。

**为什么重要：** 此前仅限邀请，全面开放意味着 Perplexity 正式向个人用户提供“AI 操作系统”体验。与 OpenAI Codex 的浏览器扩展逻辑不同，Perplexity 更侧重于本地桌面自动化，两者互补性较强。对于产品经理，这是观察 AI agent 在个人数字空间中落地形态的案例。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/07/perplexitys-personal-computer-is-now-available-everyone-on-mac/)

## Google 发布无屏 Fitbit Air 与 Google Health 应用

**是什么：** Google 推出无屏幕的健身追踪器 Fitbit Air（售价 100 美元），并同步发布全新的 Google Health 应用，旨在彻底取代旧的 Fitbit 平台，整合 AI 健康洞察。

**关键点：** Fitbit Air 无屏设计，通过触控区域与手机应用交互，重点在于全天候心率、睡眠和活动追踪。Google Health 应用则集成了来自 Fitbit、Pixel Watch 等设备的数据，利用 AI 提供个性化健康建议与风险评估。

**为什么重要：** 无屏手环重回百元价位，是 Google 在可穿戴市场的中低端渗透策略。同时，Google Health 应用标志着其健康数据从“记录”向“洞察”升级，AI 健康建议的规范化与可靠性将成为竞争焦点。

> 原文：[Ars Technica](https://arstechnica.com/gadgets/2026/05/google-unveils-screenless-fitbit-air-and-google-health-app-to-replace-fitbit/)

## Spotify AI DJ 新增法语、德语等四种语言

**是什么：** Spotify AI DJ 功能扩展至法语、德语、意大利语和巴西葡萄牙语，同时允许用户将以 Codex 或 Claude Code 生成的播客直接导入平台。

**关键点：** AI DJ 可基于用户听歌历史和当天情绪生成整点混音，并加入开场白与过渡评论。新增的播客导入功能可接受程序化生成的音频文件（如通过 AI 脚本+TTS 生成的播客），上传后自动纳入推荐算法。

**为什么重要：** 多语言支持扩大了 AI DJ 的用户基数，而播客导入功能则降低了内容创作者门槛——任何人可以用 Codex 或 Claude 生成脚本，再通过工具制作播客。这本质上是 UGC 生态的 AI 扩音器，可能改写播客行业的供给结构。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/07/spotifys-ai-dj-now-supports-french-german-italian-and-brazilian-portuguese/)

## 火山引擎与中国移动推出机密模型服务

**是什么：** 在 2026 移动云大会上，火山引擎与中国移动联合发布“移动引擎机密模型服务”，提供豆包大模型 MaaS 和 Agent 工具，结合 TEE（可信执行环境）技术保障数据安全。

**关键点：** 该服务将豆包大模型部署在中国移动的机密计算节点中，客户数据在模型推理过程中全程加密，云端无法窥探。同时提供 Agent 编排工具，支持企业快速构建安全合规的 AI 应用。

**为什么重要：** 数据隐私是政企客户采用大模型的核心障碍。TEE 结合 MaaS 的模式，为金融、医疗、政务等敏感行业提供了可行的合规路径。火山引擎借此打入基础设施层的“安全即服务”赛道，中国移动则强化了自身的云计算服务能力。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/qMyCzGke8pn9Ddrk.html)

## 百度搭子 DuMate 登顶 PinchBench，超越 Anthropic 和 OpenAI

**是什么：** 百度 AI 助手 DuMate 在 PinchBench 智能体评测中超越 Anthropic 和 OpenAI 获得第一，在 DeepResearch 分榜同样位列榜首。

**关键点：** PinchBench 是业界通用的 agent 能力评测基准，涵盖任务规划、工具调用、多轮对话等维度。DuMate 在总得分上超过 Claude Sonnet 和 GPT-4o，尤其在“长程推理”与“多工具编排”子项中表现突出。

**为什么重要：** 这是中国公司首次在主流 agent 评测中位居全球第一，直接对标 OpenAI 和 Anthropic。虽然评测本身存在数据与任务集的局限性（可能偏向中文场景），但结果仍具有信号意义——中国大模型的工程化落地能力已进入第一梯队。对投资人和产品经理而言，需要关注 DuMate 在海外市场的实际表现与评测的复现性。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/Oh9CnFrZHHOodA9n.html)

---

当 AI 既能零误报挖掘漏洞，又能帮你操控浏览器与桌面应用时，你的团队今天正在重新定义哪些自动化边界？