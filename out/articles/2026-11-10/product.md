# Agent 成了同事，工位规则还没写

## 导语

今天最值得看的一条是千问办公 2.0 的「协作」：它把 Agent 正式放进了多人共享的工作空间，而不只是每个人的私人助手。这个变化听起来像功能更新，实质是办公软件从“人使用工具”转向“人机共同工作”的接口变更，权限、产物归属、责任划分都得重新定义。巧的是，同一天另外两条消息分别从采购和安全两端给出了注脚：ChatGPT Enterprise 上了 AWS Marketplace，Claude Code 的配置文件把密钥送上了 GitHub。Agent 进办公室的速度，比管理它的规则快。

## 千问办公 2.0：Agent 从助手变成协作成员

千问办公发布 2.0，上线「协作」功能，官方称这是行业首个支持多人与 Agent 协作的能力，同时推出人机共创、资料空间、自动任务和三端互联。关键点不在生成能力，而在结构：Agent 与人共享同一份资料空间和任务上下文，意味着它必须被纳入多人权限模型，而不只是挂在某个人的会话里。过去办公套件卖的是「多人协作」，这一代要卖的是「人机混合协作」，而这层的形态定义全球都还没有标准答案。判断一个这类产品是否可用，看三件事：Agent 的操作是否可审计、产物归属是否明确、以及一个人退出空间后 Agent 的权限是否同步收回。演示视频不会回答这些。

> 原文：[量子位](https://www.qbitai.com/2026/11/508694.html)

## ChatGPT Enterprise 上架 AWS Marketplace

OpenAI 宣布 ChatGPT Enterprise 可通过 AWS Marketplace 采购，企业能沿用既有的 AWS 采购与计费关系，不必新开一套供应商流程。这条新闻的信息量不在产品，而在渠道：企业采购大模型的真实摩擦往往不是价格，而是法务、安全审查、付款周期这些流程成本，云市场恰好是很多公司已经打通的那道门。模型厂商的竞争正从「谁的模型强」延伸到「谁更容易被买进去」。对 OpenAI 而言，这是把企业销售交给客户已有的采购习惯；对云厂商而言，模型成了 marketplace 里最贵的一类 SKU。这条路径一旦跑通，后来者的模型差距会被采购惯性放大。

> 原文：[OpenAI](https://openai.com/index/chatgpt-enterprise-aws-marketplace)

## Claude Code 的配置文件，把密钥送上了 GitHub

Ars Technica 报道，Claude Code 的设置文件正让大量敏感信息暴露在 GitHub 上：用户在使用过程中选择「Do not ask again」，本地配置被写入随后被提交的文件，密码、API key 等凭证随之进入公开仓库。这是典型的便捷选项与安全默认值冲突——一次「不再询问」，就把本该留在本机的凭证变成了可被 clone 的内容。更值得注意的是暴露面：agentic 编码工具会把模型 key、外部服务凭证、MCP 配置都拉到本地，比 IDE 时代的风险面大得多。对所有正在推编码 Agent 的团队，这类工具的准入清单里应该明确加上两条：默认不落盘、密钥走隔离存储。别指望 .gitignore，它已经被证明靠不住。

> 原文：[Ars Technica](https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/)

## Medium 做了一款 AI 写作应用 TK

Medium 推出写作应用 TK，把 AI 辅助直接嵌入写作过程。这条的产品看点不是「又一个 AI 写作工具」，而是介入位置：它选择在写作过程中补位，而不是替你整段生成，这既降低了产出成本，也避开了「全自动生成」最容易引发的平台内容生态争议。在一个对 AI 写作仍高度敏感的出版环境里推出这类产品，平台需要同时向作者和读者解释清楚边界在哪里。写作工具的竞争重心正从生成质量转向嵌入点——是替你写，还是在你卡住时递一句话。后者更难做，也更难被察觉，但更可能长期留在工作流里。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/09/mediums-new-tk-app-brings-ai-assistance-directly-into-the-writing-process/)

## Automattic 推出 Spacefast，接住 vibe coding 的产物

Automattic 发布 Spacefast，用于部署 vibe-coding 应用，直接对标 Lovable 这类产品。这条抓的是一个被忽略的缺口：过去一年大量的氛围编程产物堆在本地目录和聊天窗口里，缺的不是代码，而是托管、域名、部署这最后一公里——恰好是 Automattic 手里最厚的资产。如果生成代码的边际成本趋近于零，价值就会向分发与托管转移，这也解释了为什么一批老牌建站与主机公司在 AI 这轮反而重新有了位置。真正的竞争不在谁能生成得更快，而在谁的部署链路更短、更不需要用户理解服务器。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/09/automattic-debuts-a-platform-to-deploy-vibe-coding-apps-amid-a-changing-internet/)

## 百度搭子连中三家，企业智能体的采购逻辑浮出水面

百度搭子在中信建投、国家电投数科、通用数科三个项目中均排名第一，连续拿下企业智能体采购。客户的分布值得一看：一家头部券商、两家能源与央企背景的数科公司，采购语言是合规、私有化、系统集成，而不是模型榜单上的分数。这提示企业智能体正在被「项目制采购」定义，交付形态更像当年的信息化项目，而非 SaaS 订阅。对投资人来说，中标新闻本身价值有限，更该追问的是复购率、单项目交付人天，以及一个项目做完能不能沉淀成可复用的能力。企业市场和消费市场用的是两套完全不同的估值逻辑。

> 原文：[雷峰网](https://www.leiphone.com/category/industrynews/tm7T5JBmm4u6YUQi.html)

## 迪士尼选 Adobe Firefly，为的是「品牌安全」

迪士尼选择 Adobe Firefly，为其娱乐业务打造品牌安全的 AI 模型与内容创作能力。关键词是 brand-safe：对一家靠 IP 授权和形象授权吃饭的公司，训练数据的权利链是否干净、产出能否商用、风格会不会侵权，权重远高于生成质量本身。这基本勾勒出内容公司的 AI 采购标准——不选最强的模型，选责任最清楚的模型。对 Adobe 这是护城河，对通用模型厂商则是一道不靠跑分能跨过的门槛。IP 持有者的签约动作，往往比任何评测榜单更能说明版权问题在这一轮里的定价。

> 原文：[The Decoder](https://the-decoder.com/disney-bets-on-adobes-firefly-to-create-brand-safe-ai-models-for-its-entertainment-empire/)

## 结语

今天七条里有五条讲的不是模型能力，而是模型怎么被买、被管、被追责。Agent 既然坐进了工位，下一步该写的就不是它的说明书，而是工位规则。