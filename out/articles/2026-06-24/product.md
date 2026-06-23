# Claude Tag潜入Slack，Agent工具链加速

今年Agentic的工具生态开始从“写代码”向“内化组织知识”迁移。Anthropic让AI队友持续学习Slack上下文，意味着企业级Agent不再只是问答工具，而是成为主动协作的一部分。同时，多家公司围绕Agent编程、工具调用和端侧推理密集发布新品——竞争正从模型层转向产品体验层。

## Anthropic Claude Tag上线Slack，持续学习企业语境

**是什么**：Anthropic推出Claude Tag，一个嵌入Slack的AI队友，能持续学习企业组织知识、工作流和上下文，提高团队生产力。

**关键点**：Claude Tag不是一次对话就忘的通用Agent，它会随着时间推移吸收Slack频道中的历史消息、文档片段和团队协作模式，形成针对该企业的工作记忆。

**为什么重要**：企业AI应用的瓶颈往往不是模型能力，而是缺乏对组织上下文的理解。Claude Tag的做法让AI从“外挂”变成“内部人”，可能重新定义团队协作软件中的AI定位。

> 原文：[TechCrunch](https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/)

## Dropbox开源Nova，内部AI编程Agent平台正式亮相

**是什么**：Dropbox宣布其内部平台Nova——用于大规模运行AI编程智能体——现已开源。

**关键点**：Nova被设计为可编排多个Agent协作完成复杂编程任务，支持沙箱隔离、资源调度和结果校验。Dropbox声称该平台已在其内部服务数千名工程师。

**为什么重要**：越来越多的科技公司选择将内部Agent基础设施开源，意在主导工具生态。Nova的推出可能加速各企业在AI编程Agent上的自主构建。

> 原文：[InfoQ](https://www.infoq.cn/article/5UOHryk6C66376bCULb)

## Google默认Interactions API，统一Gemini Agent调用

**是什么**：Google宣布Interactions API成为Gemini模型和智能体的默认接口，简化开发者在多轮对话和工具调用上的使用。

**关键点**：此前开发者需要在不同API间切换来支持对话历史、函数调用和状态管理，Interactions API将这些封装为单一协议，并内置了上下文窗口管理。

**为什么重要**：统一接口意味着更低的学习成本和更少的bug。Google此举是在降低Agent开发门槛，直接与OpenAI的Assistants API竞争。

> 原文：[The Decoder](https://the-decoder.com/google-makes-interactions-api-the-default-interface-for-gemini-models-and-agents/)

## xAI推出Grok Skills新功能，升级工具调用API

**是什么**：xAI发布Grok Skills功能，允许开发者构建技能，同时更新了用于工具调用的Responses API，增强Agent能力。

**关键点**：Skills类似于可插拔的能力模块，开发者可以为Grok编写特定功能（如查询数据库、调用第三方API），并通过Responses API以标准化方式触发。xAI强调低延迟和细粒度权限控制。

**为什么重要**：Grok作为后起之秀，正快速补全Agent开发的基础设施。Skills功能使其生态系统更接近OpenAI的Plugins或Google的Extensions。

> 原文：[InfoQ](https://www.infoq.cn/article/hmME4JhKTJUYJy9DNEJ2)

## 腾讯QQ邮箱内测Agently Mail，专为AI Agent设计

**是什么**：腾讯宣布QQ邮箱开始内测Agently Mail，这是一款独立于个人邮箱、可由AI Agent自主收发邮件的功能，确保安全可控。

**关键点**：Agently Mail不是让Agent直接操作你的收件箱，而是创建一个独立邮箱空间，Agent可在此范围内发送邮件、解析附件、执行自动化流程（如自动回复客户咨询）。

**为什么重要**：邮箱是Agent最自然的“行动接口”之一。腾讯此举既满足企业对Agent通信安全性的需求，也为Agent从聊天进入工作流铺平道路。

> 原文：[36氪](https://36kr.com/newsflashes/3865694185804804)

## 火山引擎Force大会：豆包商业化加速，边缘Agent平台发布

**是什么**：火山引擎在Force大会上公布豆包大模型商业化成绩，同时发布边缘Web与AI Agent托管平台EdgeOne Makers。

**关键点**：EdgeOne Makers允许开发者在边缘节点部署轻量级Agent，提供低延迟推理、本地数据缓存和与CDN网络的无缝集成。豆包商业化方面，火山引擎透露其API调用量环比增长超过两倍。

**为什么重要**：边缘Agent托管将AI能力下沉到靠近用户的位置，适用于IoT、实时互动等对延迟敏感的场景。火山引擎在AI基础设施上的布局显示出其全栈打法的野心。

> 原文：[雷锋网](https://www.leiphone.com/category/CorporateServices/ZfxxMFp9Ad0A4EWq.html)

## Google LiteRT-LM让Gemma 4在端侧推理速度翻倍

**是什么**：谷歌发布LiteRT-LM，通过多token预测将Gemma 4的本地推理速度提升最高2.2倍，适用于移动设备。

**关键点**：传统自回归模型一次预测一个token，LiteRT-LM采用多token并行预测策略，结合模型结构优化和移动端硬件适配，在Pixel手机上实测Gemma 4（2B）的推理速度提升显著。

**为什么重要**：端侧推理速度提升2倍以上意味着更流畅的用户体验和更低能耗，这直接决定了Agent能否作为真正的“随身助理”存在于手机和可穿戴设备中。

> 原文：[InfoQ](https://www.infoq.cn/article/lv6xh4HeBfWaYubLv54y)

---

当Agent开始学会读Slack、发邮件、跑代码，下一个问题或许是：谁来确保这些“队友”之间的协作不出错？