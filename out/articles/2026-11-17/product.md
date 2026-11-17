# agent 进医院，从答题走向动手

今天最值得看的一条是 OpenAI 把 computer-use agent 放进了 ChatGPT for Healthcare。医疗是错误成本最高的场景之一，却成了 agent 从"回答问题"转向"替人跑流程"的第一批真实落地场。同一天的其他动作——20 万科研人员的免费额度、Claude 在 canvas 里生成可交互网页、千问办公一次接入 10 款模型——看起来分散，指向的却是同一件事：产品竞争的重心正从模型能力本身，挪到"谁能让模型把活干完"。

## OpenAI 把 computer-use agent 送进医院

ChatGPT for Healthcare 这次加了三样东西：computer-use agent、更准确的临床回答，以及能跨多个医疗软件工作的插件。关键点在"跨软件"——医院信息系统长期是孤岛，agent 若真要替医护完成实际流程操作，就必须在不同系统之间切换，而不是在一个界面里对话。这是一次压力测试：医疗场景对错误的容忍度极低，权限边界、操作审计、责任归属都还没有行业标准。因此值得观察的不是能力上限有多高，而是 OpenAI 如何划定 agent 可以触碰的操作范围，以及出问题时流程如何回滚。

> 原文：[OpenAI](https://openai.com/index/more-ways-to-move-care-forward-with-chatgpt-for-healthcare)

## 20 万科研人员免费用前沿模型

OpenAI 扩大了 ChatGPT for Academic Researchers 计划，向全球 20 万名研究者免费开放前沿模型，同时上线科学博客，分享一线使用案例。免费额度向来不只是慈善：科研用户是模型能力最挑剔、也最能产出高价值使用样本的群体，用配额换生态与反馈，是比投广告更划算的分发。真正的问题在于这类计划的持续性——学术界的依赖一旦形成，定价权就随之后移。对研究者而言，短期是红利；对竞品而言，这是在校门口就把人拦住。

> 原文：[OpenAI](https://openai.com/index/expanding-chatgpt-for-academic-researchers)

## Claude 在 canvas 里直接生成可交互网页

Claude 现在可以在 canvas 图形内构建可交互网站，用真实 HTML 渲染，而不是生成一张截图或静态图。这让 canvas 的性质变了：从"帮你画个图、写份文档"的辅助面板，变成轻量的应用运行时。评论把它比作 Flash 时代的富交互体验，这个类比有意思——Flash 当年的普及靠的是低门槛创作加即时预览，而 Claude 走的是同一条路，只是把作者从开发者扩展到了任何会描述需求的人。接下来要看的，是产物能不能导出、能不能托管，否则它仍然停留在"演示"层面。

> 原文：[the decoder](https://the-decoder.com/claude-now-builds-interactive-websites-inside-canvas-graphics-reviving-the-flash-era-with-real-html/)

## Google Maps 用 Ask Maps 排行程

Google Maps 的 Ask Maps 现在能生成带实时信息的行程规划，从购物一日游到多日公路旅行都能逐站安排。行程规划是典型的"信息密集 + 反复修改"任务，正好落在生成式产品的甜区；而"实时信息"是关键差异——它把回答锚定在营业时间、路况、评分这类会变化的数据上，而不是凭记忆编一份看起来合理的攻略。对地图产品而言，这是从检索工具向 agent 入口的迁移，商业上也顺理成章：行程的每一站都是本地商家的潜在落点。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/16/google-maps-can-now-build-trip-itineraries-with-real-time-details-about-each-stop/)

## 豆包工作上线「工作台」，覆盖 21 个场景

豆包工作推出面向金融、医疗、教育、创意设计等 21 个专业场景的 AI 工作台，官方称是业内首个多职业定制的办公功能。路线选择很明确：不指望用户自己写 prompt，而是把行业常见的输入、输出和合规要求预先封装成模板与流程。这与通用助手的思路相反——牺牲灵活性换上手速度。"首个"是厂商表述，价值仍需使用数据验证；但这个方向值得留意，因为办公场景的付费意愿往往取决于"能不能直接交付可用结果"，而不是模型有多聪明。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/hnSL5YwUtQjerTRK.html)

## ChatGPT 上线新图像分类器围堵 CSAM

OpenAI 推出新的图像分类器与 ChatGPT 内的警示机制，对试图获取儿童性虐待内容的账号实施 24 小时封禁，并配套指南与合作伙伴计划。这类更新通常不会出现在产品头条里，但它是生成式产品得以继续存在的前提条件。技术上的难点在于，分类器是概率系统：漏报是灾难，误报则是普通用户被莫名封禁。因此除模型之外，申诉通道与人工复核的设计同样重要。对平台方来说，这部分投入只会增加，不会减少。

> 原文：[OpenAI](https://openai.com/index/strengthening-online-child-safety)

## 千问办公一次接入 10 款大模型

千问办公上线 Qwen4-Max、Kimi、GLM、DeepSeek、MiniMax 等 10 款模型，个人与企业版用户可自选模型处理不同任务。这是"模型路由"思路的产品化：不再赌单一模型在所有任务上都最优，而是把选择权交给用户或调度层——长文档、代码、创意写作各用各的长处。对办公产品来说，模型正在变成可替换的零部件，真正的差异化转移到工作流、权限管理和数据打通上。同时也说明一件事：在这个赛道，封闭生态的吸引力正在下降。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/tDhzNl3D84AjopSh.html)

## Audible 用 AI 生成有声书导读

Audible 推出 AI 生成的音频预览，用来概括书籍主题与读者评价，与真人朗读样本并列，帮助用户选书。这个切法很克制：AI 只负责"发现"环节，不碰真人朗读这一核心资产——有声书用户对合成音的容忍度，远低于对文字摘要的容忍度。它解决的是真实的转化问题：用户在不了解一本书时不愿投入十几小时，一段一分钟的导读就能降低决策成本。平台推荐位的形态，可能会因此改写。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/16/audible-turns-to-ai-to-help-users-discover-audiobooks/)

**结语**：今天这八条里，有五条的本质是同一件事——把模型塞进别人已经在用的流程里。留给读者一个问题：当 agent 开始替你点按钮，你愿意先交出哪个软件的权限？