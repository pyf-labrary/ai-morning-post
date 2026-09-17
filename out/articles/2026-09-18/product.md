# 巨头同日出手，AI 从工具变入口

今天最值得看的一件事是 OpenAI 面向律所推出 Astra for Law——前沿模型能力、定制工作流、法律数据源连接，加上面向保密客户资料的合规管控，一整套打包卖给受监管的专业服务市场。同一天，Anthropic 把 Cowork 并回 Claude 并原生支持文档与 PPT，vivo 和百度则把 Agent 往操作系统层压。把这些消息放在一起读，模型能力的差距在收窄，分水岭正在从「谁的模型强」转向「谁占住了工作流和入口」；广告那条，是同一逻辑在变现侧的落子。

## OpenAI 把模型卖给律所

OpenAI 推出 Astra for Law，面向律所提供前沿模型能力、定制工作流、法律数据源连接，以及面向保密客户资料的合规管控。

关键点在最后一项。法律是典型的高价值、强合规、按小时计费的专业服务市场，付费能力强，但对数据边界极度敏感。OpenAI 把合规管控和行业数据源连接单独列出来，说明要解决的是「敢不敢把客户资料交出去」这个前置问题，而不是模型能不能写合同。如果律所这一关跑通，会计、审计、医疗等受监管行业就是可复制的模板。反过来，对法律科技创业公司来说，底层供应商变成直接竞品，这道账得重新算。

> 原文：[OpenAI](https://openai.com/index/astra-for-law)

## AI 广告换了个形态：Sponsored Agents

OpenAI 上线 AI 驱动的广告新体验，包括 Sponsored Agents 与面向营销人员的工具，并接入 HubSpot 和 Shopify。

广告不再是 banner，而是以 agent 形态出现。接入 CRM 与电商平台，意味着从曝光到转化的链路可被追踪，广告主买的是「帮你把事情办完」的位置，而不是一块版面。这是 OpenAI 在订阅之外补商业化短板最直接的一条路，先打中小商家的营销预算，HubSpot 和 Shopify 的生态正好覆盖这批人。但同一枚硬币的另一面是：当助手开始推荐并代你下单，中立性就成了必须回答的产品问题。

> 原文：[OpenAI](https://openai.com/index/reimagining-advertising-with-ai)

## Claude 合并入口，补齐 Office

Anthropic 把 Claude Cowork 与聊天合并为统一的 Claude 入口，并原生支持文档与 PPT 处理。

入口收敛通常意味着产品侧已经验证过一轮，知道用户在哪一步流失——不必再让人先判断「这件事该用聊天还是用 Cowork」。更实质的是文档与 PPT 的原生处理：AI 助手从「给建议」推进到「交产物」。办公是当前竞争最激烈的战场，微软把 Copilot 绑在 Office 里，Google 把 Gemini 放进 Workspace，Anthropic 没有自己的办公套件，只能靠文件格式兼容和体验赢。硅谷的 AI 办公大战，又添了一把火。

> 原文：[Claude](https://claude.com/blog/cowork-is-now-claude)

## Claude Code 让任务跑在云端

Claude Code 重构 Projects：由 Claude 充当协调者，可并行开启多个云端会话，关掉电脑后任务仍在后台继续执行。

从「串行对话」到「并行任务编排」，这是 coding agent 形态上的一次位移：人不再逐轮驱动，而是派活、验收。云端执行是脱离本地终端的前提，也让算力消耗变得可持续计量——并行会话越多，token 消耗越结构化。真正需要提前想的是协作层面的事：多个 agent 同时改同一个仓库时的冲突处理、变更审计和回滚，目前还没有成熟答案。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/09/17/anthropic-launches-claude-code-projects-in-beta-parallel-cloud-sessions-that-keep-running-after-you-close-your-laptop/)

## 谷歌把 Agent 装进家庭

谷歌推出实验性家庭智能体 CC，家庭成员可共享数据，让 Agent 帮忙做计划、订行程并完成日常任务。

家庭是消费级 Agent 最难也最有价值的场景：多人、多设备、权限关系复杂，而语音又是天然入口。谷歌手里的牌是 Android、Nest、日历和 Gmail，CC 真正在测的是「共享上下文」这个产品命题——同一个 Agent 该知道谁的日程、能替谁做决定。需要提醒的是它仍属实验项目，别按成品预期。但如果这个形态成立，家庭账户会成为下一个被重新定义的入口。

> 原文：[Ars Technica](https://arstechnica.com/google/2026/09/google-announces-new-experimental-cc-ai-agent-for-families/)

## vivo 把 Agent 下沉到系统层

vivo 发布 AgentOS 预览版，将智能体下沉到操作系统层，开放 6000 多项原子技能供调用，让手机从「会回答」走向「会办事」。

技能原子化加系统级开放调用，意味着 Agent 可以跨 App 完成动作，而不是困在某一个应用里。这对手机厂商是好消息，护城河从硬件参数转向「谁能替用户操作 App」；对超级 App 则是坏消息，入口地位第一次被从系统层绕过。接下来最该盯的指标不是技能数量，而是这 6000 多项技能里有多少第三方愿意真正接进来——开放程度决定了它是平台还是自嗨。

> 原文：[InfoQ](https://www.infoq.cn/article/hbZAEa6iQbq5rcUWbUi4?utm_source=rss&utm_medium=article)

## 百度智能云做产业智能体底座

百度智能云推出面向产业的智能体操作系统，试图用统一的 Agent 底座打通企业流程，形成 AI 的商业与技术飞轮。

卖底座而不是单点应用，是国内 To B 的常规路径，百度想复制云时代的打法。但「统一底座」和「流程打通」之间隔着大量交付工作，实际效果取决于行业 Know-how，而非模型本身——这也是过去几年企业 AI 项目最容易卡住的地方。飞轮能不能转起来，看的是首批行业客户是否愿意把核心流程放上去，而不是发布会的完整度。

> 原文：[InfoQ](https://www.infoq.cn/article/jXliIdDVTYDAtm73EoSU?utm_source=rss&utm_medium=article)

## 蚂蚁全员接入千问办公

蚂蚁集团正式把千问办公作为全公司的智能办公 Agent 底座，全员使用，成为大型企业规模化落地 AI 办公的样板。

全员铺开验证的其实不是模型能力，而是组织接受度：权限怎么划、数据怎么隔离、员工愿不愿意改工作习惯。蚂蚁是金融科技公司，合规要求高于一般互联网公司，它跑通的流程对同业更有参照价值。反过来说，这类「全员接入」的样本也值得追问一句：是真日常使用，还是停留在账号开通层面。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/U3X9WHILcYX0kh4l.html)

## 结语

八条消息合起来看，模型厂商正同时往两头走：一头扎进律所、广告这类高价值变现场景，一头把 Agent 压进操作系统和办公底座。留一个问题给你——当 Agent 能替你起草、下单、操作 App，你所在行业的那道「入口」还握在谁手里？