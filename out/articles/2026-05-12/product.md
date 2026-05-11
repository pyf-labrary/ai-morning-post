# AI 笔记工具引爆律师圈隐私雷，38 万应用因 AI 编码裸奔

AI 的应用产品赛道正经历“能力放量与安全合规”的剧烈拉扯。今天最值得关注的是律师群体对 AI 笔记工具的集体紧张——行业自律与监管空白下的数据隐私危机，比技术本身更先成为决定产品生死的关键变量。与此同时，AI 编程工具暴露内网、Chrome AI 吃光用户空间等事件，都在提醒：速度与安全的天平，正在向后者倾斜。

## 律师用 AI 笔记工具，隐私合规成新雷区

越来越多的律师开始用 AI 笔记工具记录会议、整理案件摘要，但纽约时报报道指出，这类工具在处理高度机密的客户信息时存在严重法律风险。美国律师协会的职业道德规则要求律师对客户信息尽到“合理审慎”义务，而第三方 AI 服务的训练数据留存、云存储位置、甚至提示词 logs 都可能构成泄露。目前已有律所禁止律师使用 ChatGPT、Otter.ai 等通用工具，但行业缺乏针对法律场景的专用 AI 笔记合规标准。

> 原文：[https://www.nytimes.com/2026/05/09/business/dealbook/ai-notetakers-legal-risk.html](https://www.nytimes.com/2026/05/09/business/dealbook/ai-notetakers-legal-risk.html)

## Mistral 为 Le Chat 补上远程智能体，企业协作能力升级

Mistral 更新其对话产品 Le Chat，新加入“远程智能体”和“Work 模式”。简单说，用户现在可以创建常驻后台的智能体，自动处理邮件总结、会议安排、跨系统数据查询等任务。Work 模式则面向团队，支持在对话中共享上下文、指派任务并追踪进度。这补上了 Le Chat 在企业级协作上的短板，使其更像一个“轻量级 AI 工作流平台”，而非单纯的聊天工具。

> 原文：[https://www.infoq.cn/article/14UTzo6myptzQ1GqBdOG](https://www.infoq.cn/article/14UTzo6myptzQ1GqBdOG)

## 网易智企发布 CodeWave，想治 AI 编码“叫好不叫座”

AI 编程工具能提升代码生成速度，但很多企业发现利润并未同步增长——问题出在代码质量维护、安全审查和后续适配的成本被低估。网易智企推出 CodeWave 平台，核心思路是“从生成到交付”全链路管理：自动生成代码后立即进行安全扫描、合规检查，并强制经过人工审核才会进入生产环境。本质是把 AI 编码从“替代码农”变成“辅助审核+自动化测试”的组合拳，试图解决提效不增收的痛点。

> 原文：[https://www.infoq.cn/article/qFyHzWVe3SrEwbwzGtCq?utm_source=rss&utm_medium=article](https://www.infoq.cn/article/qFyHzWVe3SrEwbwzGtCq?utm_source=rss&utm_medium=article)

## AI 编程工具把内网暴露了：38 万应用裸奔，2000+ 泄密

一项调查显示，使用 AI 编程工具生成的开发环境配置中，有大量默认开启公网访问的漏洞，导致 38 万个本应仅内网可见的应用暴露在公网。更严重的是，其中超过 2000 个应用已被确认发生数据泄露，包括数据库、API 密钥和内部文档。问题根源在于 AI 模型训练时大量使用了“不设防”的公开仓库代码，生成的模板也沿用了这种不安全习惯。这是 AI 辅助开发“默认不安全”的典型警示。

> 原文：[https://www.infoq.cn/article/j8rolcojYjAakoeJ3FhS?utm_source=rss&utm_medium=article](https://www.infoq.cn/article/j8rolcojYjAakoeJ3FhS?utm_source=rss&utm_medium=article)

## 360 启动“龙虾计划”：每人发 1 亿 Token，推动全员人机协同

360 公司内部启动“龙虾计划”，向全体员工每人发放 1 亿 Token，用于使用内部 AI 智能体平台“360 安全龙虾”。员工可以用这些 Token 调用不同智能体完成报告撰写、代码调试、安全分析等任务，Token 消耗数据会用于优化模型和分配权限。这本质是一场企业内部“AI 普惠运动”，希望通过全员使用倒灌数据、发现真场景——也是 360 将自己定位为“AI 安全底座”的产品预演。

> 原文：[https://www.leiphone.com/category/industrynews/ovhSH6doEiluAvyZ.html](https://www.leiphone.com/category/industrynews/ovhSH6doEiluAvyZ.html)

## Chrome 内置 AI 功能吃掉 4GB 用户存储，用户抱怨“不请自来”

谷歌 Chrome 浏览器内置的 Gemini Nano 等 AI 功能被发现会占用高达 4GB 的用户本地存储空间，用于缓存模型和推理数据。问题是很多用户并不知道浏览器默默下载了这些模型，且无法通过常规设置清理。这个功能原本是为了离线运行 AI 翻译、写作辅助等，但“不默认告知”加上“空间膨胀”激发了用户的不满，社交媒体上已有大量“Chrome 变成存储杀手”的控诉。

> 原文：[https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features](https://www.theverge.com/tech/924933/google-chrome-4gb-gemini-nano-ai-features)

## Digg 重启：从社交新闻元老变身 AI 新闻聚合器

老牌社交新闻网站 Digg 尝试第三次回归，这次定位是“AI 驱动的新闻聚合器”。新版本不再依赖用户投票排序，而是由 AI 模型从数千个信源中筛选出“有影响力”的内容，并附上不同立场的声音摘要。创始人表示，目标是解决信息茧房和标题党，但业内质疑：AI 如何定义“影响力”？数据训练集是否引入偏见？Digg 的转型能否成功，取决于它能否在算法推荐和人工编辑之间找到新平衡。

> 原文：[https://techcrunch.com/2026/05/11/digg-tries-again-this-time-as-an-ai-news-aggregator/](https://techcrunch.com/2026/05/11/digg-tries-again-this-time-as-an-ai-news-aggregator/)

---

当 AI 产品从“能做什么”迈向“能安全地做什么”，你更担心用户不知情地被消耗，还是开发者不自知地暴露？