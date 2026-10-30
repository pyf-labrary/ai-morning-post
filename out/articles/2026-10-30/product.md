# Agent 搬出对话框

今天最值得看的一条是 Google 向第三方 AI Agent 开放 Android 开发，并配套新的 Gemini API。它和 Cursor 的 Agent SDK、蚂蚁灵光接入支付宝钉钉、Alexa 接管订阅与配送，指向同一个方向：Agent 正从对话框里的功能，变成系统、账户和工作流里的一层接口。入口一旦被接口化，竞争的标的就从模型能力换成了调用权限与分发位置。

## Google 把 Android 交给第三方 Agent

Google 开放第三方 AI Agent 参与 Android 开发，同时推出新的 Gemini API，让 Agent 更深入地接入系统与应用生态。

关键点在两个层面：开发侧，Agent 被允许进入 Android 的开发流程；运行侧，新 API 把系统与应用能力暴露给 Agent 调用。两者叠加，Agent 从“App 内的一个功能”向“系统的一等公民”移动。

为什么重要：Android 是覆盖最广的终端分发面。Agent 一旦拿到系统级调用权，竞争焦点就从“谁的模型更强”转向“谁能拿到系统接口”。对开发者，这是新的适配成本，也是新的入口红利；对 Google，这是用开放换生态粘性，把 Gemini 变成 Agent 时代的默认底座。

> 原文：[the-decoder](https://the-decoder.com/google-opens-android-development-to-third-party-ai-agents-and-unveils-new-gemini-apis/)

## Cursor 把编码 Agent 做成 SDK

Cursor 发布 Agent SDK，开发者可以把它的编码 Agent 能力集成进自有产品和工作流。

关键点是从 IDE 工具转为能力供应商。过去 Cursor 卖的是编辑器里的体验，现在卖的是可嵌入的编码 Agent 运行时——客户关系从个人开发者扩展到企业工作流，交付形态从产品变成依赖。

为什么重要：编码是 Agent 目前商业闭环最清晰的场景。SDK 化意味着 Cursor 想在模型厂与 IDE 之间占住中间层：上游模型可替换，下游工作流被锁定。但这条路上它要正面对上 GitHub Copilot 和各家的自研 IDE，护城河不在模型，而在上下文与工程集成做得多深。

> 原文：[Cursor Blog](https://cursor.com/blog/agent-sdk)

## 蚂蚁灵光 2.0 接进支付宝与钉钉

灵光 2.0 扩展跨平台连接，原生接入支付宝生态和钉钉 CLI 等数十项外部工具，从聊天走向“能管事”。

关键点在选择了两条链路：交易与办公。数十项外部工具的接入意味着它不再靠对话质量取胜，而是靠能实际完成多少动作——付款、审批、流程发起。

为什么重要：国内 Agent 的差异化不在模型参数，而在“事能不能办成”。支付宝和钉钉是少数能形成完整闭环的场景，接住交易与审批，才有留存和复访。但工具接得越多，权限、责任边界和失败回滚的设计就越难，这也是“能管事”必须付的代价。

> 原文：[雷峰网](https://www.leiphone.com/category/industrynews/eigNbrwrLkMYpiwN.html)

## OpenAI 提额，顺手把用户导向 API

OpenAI 将 Pro 套餐使用上限翻倍，并向符合条件的 ChatGPT 订阅用户提供 API credits。

关键点是一手提额、一手给额度：前者守订阅留存，后者把 C 端用户往开发者侧导。两件事同时做，说明它把订阅用户视作 API 生态的潜在供给。

为什么重要：在 Anthropic 竞争加剧的背景下，这是防守型动作——用额度换留存，用 credits 换工作流迁移。补贴本身不是壁垒，真正的壁垒是用户把提示词、工具链和数据沉淀在谁的平台上。这笔成本买的是迁移摩擦。

> 原文：[the-decoder](https://the-decoder.com/openai-doubles-usage-limits-on-pro-plans-as-competition-with-anthropic-heats-up/)

## 豆包工作把国产模型摆上同一货架

豆包工作面向团队和企业订阅版开放第三方大模型，首批接入 Kimi 3.1 Pro、GLM 5.3、DeepSeek V4.1 Flash。

关键点是企业版变成多模型路由层：同一个工作台里，用户按任务选模型。对客户是灵活性，对模型厂是被比较、被切换。

为什么重要：企业采购决策里，工作台的分量正在超过单个模型。字节用开放换企业渗透，是典型的平台打法，代价是把自己家的模型也放进了同一场比价。这条路成立的前提是路由做得足够聪明、切换成本足够低，否则“开放”只是把定价权交了出去。

> 原文：[雷峰网](https://www.leiphone.com/category/industrynews/bMidAUlVn5zmruyD.html)

## Meta 低调上线 AI 穿搭应用 Style Sketch

Meta 推出 AI 时尚应用 Style Sketch，可连接 Instagram 照片生成虚拟衣橱，也支持拍照、视频或上传图片添加单品。

关键点是冷启动方式：靠 Instagram 的既有图片资产起步，场景锁定在衣橱管理与穿搭，而非通用助手。低调上线，说明这是一次小成本试水。

为什么重要：Meta 做 AI 应用的独特优势不在模型，而在社交资产。时尚是少数能直接从图片资产里长出个性化体验的垂直场景，变现路径也清晰——指向电商与品牌合作。但“连接 Instagram 照片”同时把隐私与图片使用边界摆到了台面上，这会是它规模化前必须先回答的问题。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/29/meta-quietly-launches-an-ai-fashion-app-called-style-sketch/)

## Alexa 开始动你的订阅和配送

亚马逊更新 Alexa，可创建和管理购物清单、订阅，以及修改配送指令。

关键点是从问答进入账户与订单层。管理订阅、改配送说明，都是会真实改变交易状态的操作，容错要求远高于“今天天气怎样”。

为什么重要：语音助手的价值长期停在信息层，只有碰到账户和订单才算进入事务层。这一步把 Alexa 直接接进电商主链路，也意味着它的考核指标从活跃度转向 GMV 贡献。风险同样明显：语音误识别造成的下单或续订，责任归谁，需要产品层面给出答案。

> 原文：[TechCrunch](https://techcrunch.com/2026/10/29/amazon-updates-alexa-to-help-you-manage-shopping-lists-and-subscriptions-and-update-delivery-instructions/)

## TRAE 宝押注“长期上下文”

AI 开发产品 TRAE 推出双层助理体系 TRAE 宝，持续理解开发者的长期项目、任务与决策，而非只响应单次指令。

关键点是卖点的位移：从“响应质量”转向“记忆与项目状态”。它要记住的不只是当前这轮对话，而是几个月里这个项目的技术选择和权衡。

为什么重要：编码 Agent 的下一段竞争在上下文管理。记忆做厚，替换成本就高，产品叙事也从“工具”升级为“同事”。但落地取决于两件苦活：上下文召回的准确率，以及长期记忆带来的 token 成本。这两项不过关，“懂你的项目”就只是一句宣言。

> 原文：[雷峰网](https://www.leiphone.com/category/industrynews/VtaDCTK8rnfs2sSX.html)

## 结语

今天八条动作指向同一件事：Agent 正在被接进系统、账户和工作流，而不是留在对话框里。当每家都把它做成接口，用户最后记住的会是入口，还是模型？