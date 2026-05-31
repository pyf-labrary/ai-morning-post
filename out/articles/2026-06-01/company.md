# 微软与英伟达联手开发AI PC，自研CPU曝光

今天最值得看的是微软与英伟达合作打造运行AI agent的PC，英伟达自研CPU被曝光。这意味着AI PC竞争从软件层下沉到芯片级定制，未来本地AI体验将不再依赖通用CPU+GPU组合，而是为agent工作负载设计的专用硬件。与此同时，GitHub Copilot改token计费引发开发者强烈反弹，Anthropic安全部署细节曝光——两条故事共同指向一个信号：AI平台正在从“跑马圈地”进入精细化运营与基础设施竞争阶段。

## 微软与英伟达联手开发AI PC，自研CPU曝光

据媒体报道，微软与英伟达正合作开发一款面向AI agent的PC，英伟达将提供自研CPU，整机设计类似MacBook Pro的定位。这台设备的核心不再是运行Copilot这样的聊天助手，而是直接承载能够自主执行任务的agent。关键点在于英伟达的CPU角色——此前英伟达在PC端以GPU为主，自研CPU将挑战x86生态。为什么重要：如果成真，AI PC的硬件定义权将向英伟达倾斜，微软则获得一个从芯片到操作系统完全定制化的agent平台，摆脱对Intel/AMD的依赖。

> 原文：[The Decoder](https://the-decoder.com/microsoft-and-nvidia-reportedly-team-up-on-ai-pcs-that-run-actual-agents-instead-of-copilot/)

## GitHub Copilot改token计费，开发者怨声载道

GitHub宣布Copilot将采用基于token的新计费模式，取代之前的固定月费订阅。开发者社群迅速发酵不满情绪，有用户称这是“黄金时代的终结”。关键点：token计费意味着使用量越大成本越高，对于重度依赖Copilot的团队而言，月度支出可能急剧上升。为什么重要：这一变化反映了AI编程助手从“获客补贴”转向“盈利优先”，但代价是开发者信任。如果其他平台跟进，整个AI开发工具定价范式可能改变，迫使企业重新评估ROI。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/30/what-a-joke-github-copilots-new-token-based-billing-spurs-consternation-among-devs/)

## OpenRouter完成1.13亿美元B轮融资

AI模型聚合平台OpenRouter宣布获得1.13亿美元B轮融资，加速模型接入与推理服务扩张。OpenRouter的核心价值在于统一API接口，让开发者一次接入即可调用数十家模型（OpenAI、Anthropic、Google等）并按需切换。关键点：这轮融资发生在模型供应碎片化加剧、推理成本持续波动的时间点。为什么重要：OpenRouter的崛起意味着中间层（模型聚合与路由）正在成为AI基础设施的关键环节；当模型本身商品化，路由与调度能力可能成为真正的护城河。

> 原文：[OpenRouter公告](https://openrouter.ai/announcements/series-b)

## 软银斥资750亿欧元在法国建设AI数据中心

软银宣布最高投入750亿欧元在法国建设大型AI计算集群，这将是欧洲最大规模的数据中心项目。关键点：软银选择法国而非其他欧洲国家，与法国政府近期的AI投资优惠政策和核电稳定性直接相关。为什么重要：数据中心投资规模激增，预示着AI算力需求仍处于爆发期；同时，地缘政治格局下欧洲正加速本土算力建设，减少对美国的依赖。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/30/softbank-says-it-will-invest-up-to-e75-billion-to-build-french-data-centers/)

## Anthropic官方披露如何安全部署Claude

Anthropic发布技术博客，详细介绍了在多产品环境中如何安全隔离和管控Claude模型，提升沙箱透明度。关键点：他们设计了多层次的权限隔离、输入输出审计以及行为监控机制，避免模型在跨产品调用时发生数据泄露或越权行为。为什么重要：随着Claude被集成到更多企业级产品中，安全透明化成为赢得机构客户信任的必要条件；Anthropic主动披露技术细节，既是对竞争对手的差异化，也呼应了监管对AI安全的关注。

> 原文：[Anthropic Engineering](https://www.anthropic.com/engineering/how-we-contain-claude)

## Anthropic超越OpenAI成估值最高AI创企

消息称Anthropic的估值已超过OpenAI，成为全球最有价值的AI创业公司。关键点：尽管OpenAI在C端知名度更高，但Anthropic依靠Claude的企业级部署和安全性定位，在融资和估值上反超。为什么重要：这反映了资本对AI安全路线和“可控性”的偏好正在升温；同时也说明，在模型能力趋同的背景下，商业策略与信任建设成为差异化关键。

> 原文：[Qazinform](https://qazinform.com/news/anthropic-surpasses-openai-to-become-worlds-most-valuable-ai-startup)

## DDIM之父宋佳铭宣布离职

扩散模型关键人物、DDIM（Denoising Diffusion Implicit Models）提出者宋佳铭将离开当前职位，消息引发行业关注。关键点：宋佳铭在扩散模型领域贡献显著，DDIM将扩散逆过程从数千步压缩至几十步，是稳定扩散等技术高效落地的基石。为什么重要：顶尖研究者的去留通常预示着技术方向的调整或创业意向；宋佳铭的下一步动向可能影响生成式AI底层建模的演进路径。

> 原文：[量子位](https://www.qbitai.com/2026/05/427104.html)

## Anthropic禁止面试中使用AI工具

Anthropic宣布在招聘面试中禁止使用AI工具，以真实评估候选人的思考能力。关键点：面试官不能打开Copilot或ChatGPT辅助提问或评估答案，候选人也不能借助AI生成回答。为什么重要：作为一家AI公司，Anthropic此举似乎在强调“人类思考的不可替代性”——但更务实的原因是，AI工具会引入评分偏差，让面试结果失真。这一政策可能成为技术公司招聘的风向标。

> 原文：[The Decoder](https://the-decoder.com/anthropic-bans-ai-tools-during-job-interviews-to-see-how-candidates-actually-think/)

结语：当AI公司开始警惕自己的产品被用于面试时，或许我们应当重新审视“AI无处不在”的边界。