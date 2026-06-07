# OpenAI终结聊天：ChatGPT进化Agent

导语：今天最震撼的消息是OpenAI正式宣告“聊天已死”，计划将ChatGPT彻底重构成一个能自主完成任务的AI Agent平台。这不仅是产品形态的转变，更宣告AI交互范式从“人问机答”转向“机代人劳”——投资人应关注Agent的定价权和生态锁，产品经理则要重新思考用户体验的底层逻辑。

## OpenAI称“聊天已死”，将ChatGPT改造成Agent

OpenAI计划对ChatGPT进行根本性重构，从传统聊天机器人升级为能够自主规划和执行复杂任务的AI Agent平台。这不仅仅是功能叠加，而是底层架构的重新设计——让模型能够调用工具、管理多步骤流程、甚至自主决策。

关键点：OpenAI认为“聊天”这个交互范式本身已经过时，用户不再需要逐轮对话，而是希望AI直接完成一项工作（如订票、写报告、管理日程）。ChatGPT将变成“代理人”，用户只需给出目标。

为什么重要：这是OpenAI迄今为止最激进的战略转向。如果成功，它将重新定义AI产品的用户价值——从“陪聊”到“干活”。对行业而言，所有对话式AI产品都需要重新审视自己的定位，否则可能被Agent浪潮淘汰。

> 原文：[the-decoder.com](https://the-decoder.com/openai-says-chat-is-dead-and-plans-to-rebuild-chatgpt-as-a-full-blown-agent-app/)

## ChatGPT新增Lockdown模式防提示注入

OpenAI为ChatGPT推出Lockdown Mode（锁定模式），允许用户禁用网页访问、文件上传等功能，以保护敏感数据免受提示注入攻击。该模式特别适用于企业内部使用场景，防止恶意用户通过Prompt哄骗AI泄露机密信息。

关键点：Lockdown Mode本质上是安全隔离——关闭所有向外请求，让ChatGPT仅基于内置知识库回答。管理员可以精细控制哪些功能可用。

为什么重要：随着Agent能够执行更多操作（如发送邮件、访问数据库），安全风险急剧上升。Lockdown Mode解决了企业部署AI agent时的核心顾虑——数据泄露。它是Agent从玩具走向企业级工具的必要基础设施。

> 原文：[the-decoder.com](https://the-decoder.com/chatgpts-new-lockdown-mode-lets-you-disable-web-access-and-more-to-protect-sensitive-data-from-prompt-injection/)

## Perplexity推出Search as Code，AI自写搜索管道

Perplexity发布“Search as Code”功能，使AI模型能够编写自己的搜索管道，而不是调用固定的API接口。模型可动态决定搜索策略——从哪个数据源查询、如何组合结果、何时进行二次检索。

关键点：传统的搜索API是固定的：给定参数返回结果。而Search as Code让AI像程序员一样编写搜索代码（如Python脚本），实时生成最优查询逻辑。这极大提升了实时信息检索的灵活性和深度。

为什么重要：对于需要依赖网络信息的Agent而言，搜索能力是核心。Perplexity的这个方案意味着AI agent不再受限于预定义的API，而是可以根据任务自由设计搜索流程，这相当于给Agent装上了“可编程的搜索引擎”。

> 原文：[the-decoder.com](https://the-decoder.com/perplexitys-search-as-code-lets-ai-models-write-their-own-search-pipelines-instead-of-calling-fixed-apis/)

## Meta Hatch AI Agent月费最高200美元

Meta即将推出代号为Hatch的AI Agent产品，定位为付费订阅服务，月费可能高达200美元。这是Meta首个直接向用户收费的AI产品，标志着其从免费分发模型转向商业模式探索。

关键点：Hatch的定价远超主流AI助手（如ChatGPT Plus 20美元/月），暗示其目标用户为企业或高价值场景。Meta内部将其视为“数字员工”，能完成诸如数据分析、内容创作等专业任务。

为什么重要：200美元的定价直接引发了“AI Agent值多少钱”的讨论。如果市场接受，将打开Agent商业化的天花板；如果失败，则说明当前Agent能力还不足以支撑高价。这对所有AI产品定价策略都有参考意义。

> 原文：[the-decoder.com](https://the-decoder.com/metas-hatch-ai-agent-could-cost-up-to-200-a-month-and-marks-its-first-paid-ai-product/)

## Notion恢复对Anthropic集成访问

Notion产品负责人就此前中断Anthropic集成访问的事件公开回应，称对大量转发感到惊讶，目前服务已恢复正常。此前用户发现Notion中Anthropic相关功能无法使用，引发社区猜测。

关键点：集成中断的具体原因未明说，但Notion方面表示是“服务中断”而非战略调整。恢复后Anthropic模型仍可在Notion AI中使用。

为什么重要：这起小风波暴露了第三方AI集成面临的不稳定性风险——当核心AI能力依赖外部供应商时，任何配置变更都会影响用户体验。产品经理需要为此准备预案（如多模型切换）。

> 原文：[techcrunch.com](https://techcrunch.com/2026/06/07/notion-restores-access-to-anthropic-after-service-disruption/)

## 小米机器人或随小米17T发布会首秀

卢伟冰在探班视频中不经意间展示了小米机器人手臂的画面，外界猜测该机器人可能将在小米17T发布会（预计6月）上正式亮相。小米此前已在AI和机器人领域有布局，但消费级产品尚未面世。

关键点：视频中机器人手臂看似具备一定精密度，能完成抓取、摆放等动作。如果发布会当天确有机器人产品，将标志着小米正式进入具身智能赛道。

为什么重要：硬件厂商切入AI robot是趋势——小米拥有供应链和生态链优势，若推出面向家庭场景的机器人，可能复制小米在手机和IoT市场的性价比打法。但具体定位（家用/商用）仍未知。

> 原文：[36氪](https://36kr.com/newsflashes/3842624097569288)

## 得物AI Harness实现AI标准化生产

得物技术团队公开分享了其内部AI Harness平台，该平台将AI开发从随意的编码过程转变为目标驱动的标准化流程。通过定义“行为规范”和“质量门禁”，让AI应用像传统软件一样可测试、可度量、可复制。

关键点：AI Harness的核心是“契约化”——开发者只需描述目标（如“识别商品真伪”），平台自动生成数据管道、评估指标和部署模板。这降低了AI开发的门槛，同时保证了产出质量。

为什么重要：当AI agent开始承担关键任务（如交易、审核），标准化生产成为刚需。得物的实践提供了一个可参考的工程化方案，尤其适合需要合规与审计的行业。

> 原文：[infoQ](https://www.infoq.cn/article/pOwoNlmEL9zV0aodLVB9)

结语：当ChatGPT不再需要你“聊天”，Meta的Agent卖200美元/月，你准备好为AI的自主权买单了吗？