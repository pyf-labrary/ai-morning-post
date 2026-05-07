# 22万GPU算力豪赌，OpenAI组网救急

**导语**：今天最值得关注的消息不是模型发布，而是基础设施的军备竞赛。Anthropic 租下了 SpaceX/xAI 全部 22 万张 GPU，年花费 50 亿美元——这相当于直接买断算力产能，背后是对 AGI 路径的激进押注。同时 OpenAI 联合英伟达、AMD、英特尔等推出新网络协议 MRC，试图解决超算的网络瓶颈。两条消息拼在一起，能看清头部玩家对“下一个瓶颈在哪”的判断差异：Anthropic 赌算力稀缺，OpenAI 赌互联效率。

## Anthropic 与 SpaceX 达成 22 万 GPU 大单

Anthropic 已与 SpaceX/xAI 签署协议，租用其 Colossus 数据中心全部算力容量——约 22 万张 GPU，年花费约 50 亿美元。这笔交易将使 Anthropic 的可用算力直接翻倍，用于加速 Claude 模型训练与推理，缓解长期以来的算力瓶颈。关键点：这不是一台台买卡，而是整座数据中心的“独家使用权”，意味着 Anthropic 愿意为确定性支付高溢价。为什么重要：当模型能力进入深水区，算力已成为最大风险变量。Anthropic 用 50 亿美元赌的是“只要算力到位，模型能力就能再跳一阶”。这也会推高其他玩家的算力获取成本，引发新一轮规模竞赛。

> 原文：https://www.anthropic.com/news/higher-limits-spacex

## OpenAI 联合多家巨头推出开放网络协议 MRC

OpenAI 与 AMD、Broadcom、Intel、微软、英伟达共同宣布开发 Multipath Reliable Connection（MRC）协议，旨在解决 AI 超算网络中的拥塞与丢包问题。MRC 基于现有以太网标准，通过多路径冗余传输提高带宽利用率，目标是支撑训练集群的万卡规模互联。关键点：这不是闭源协议，OpenAI 将其作为开放标准贡献给社区，意在降低对英伟达 InfiniBand 的依赖。为什么重要：当前 AI 训练集群的网络瓶颈已成为比 GPU 更隐蔽的短板。如果 MRC 被广泛采用，将改变数据中心网络生态，让以太网在 AI 场景中重新获得竞争力。OpenAI 此举既为自己“救急”，也是在布局下一代网络标准的话语权。

> 原文：https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc/

## OpenAI 开始在 ChatGPT 测试广告

OpenAI 官宣将在 ChatGPT 中测试广告，以此支持免费用户的访问成本。广告会清晰标注“赞助内容”，不影响 ChatGPT 的回答独立性，也不会基于用户对话数据做个性化推荐。关键点：OpenAI 明确表示广告不会使用私人对话进行定向，而是基于当前会话的上下文做一般性推广。为什么重要：这是 OpenAI 在盈利模式上的一次重大转向——从单纯依靠订阅（ChatGPT Plus/Pro）转向广告+订阅双轮驱动。如果测试成功，ChatGPT 可能成为新的广告分发入口，直接与 Google 搜索广告竞争。但风险在于用户对广告的接受度，以及如何平衡用户体验与商业化。

> 原文：https://openai.com/index/testing-ads-in-chatgpt

## 马斯克曾试图挖角 OpenAI 创始人组建特斯拉 AI 团队

最新披露的法庭文件显示，2017 年马斯克曾计划招募 Sam Altman 或 Demis Hassabis 来领导特斯拉内部的 AI 实验室，并要求“拥有完全控制权”。该计划最终未能实现，但揭示出马斯克对 OpenAI 创始团队的长期关注。关键点：文件来自马斯克诉 OpenAI 案的相关证据链条，意图说明马斯克早期就想主导 AI 研发方向。为什么重要：这为马斯克与 OpenAI 之间持续的法律纠纷提供了新的叙事维度——不是简单的“背叛与离开”，而是一场对 AGI 控制权的长期争夺。对投资人和技术人而言，这说明顶尖人才争夺早在 2017 年就已白热化。

> 原文：https://arstechnica.com/tech-policy/2026/05/elon-musk-tried-to-hire-openai-founders-to-start-ai-unit-inside-tesla/

## Moonshot AI 以 200 亿美元估值融资 20 亿美元

中国 AI 公司 Moonshot AI（月之暗面）完成 20 亿美元融资，估值达 200 亿美元。公司月经常性收入（MRR）已超过 2 亿美元，主要源于开源 AI 模型需求暴涨。关键点：这是中国 AI 初创公司目前最高的融资估值之一，显露出全球资本对开源 AI 路线的强烈兴趣。为什么重要：Moonshot 的崛起验证了一个趋势——在基础模型竞争趋于同质化后，围绕开源生态的商业模式（如企业服务、私有化部署）正在快速放量。200 亿美元估值是否合理，关键看 MRR 的持续增长速度和毛利率。

> 原文：https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/

## 无问芯穹再获超 7 亿元融资，领跑国内 AI Infra

无问芯穹完成新一轮超 7 亿元人民币融资，联合领投方为杭州高新金投和惠远资本。公司继续稳居中国 AI 原生基础设施领域融资规模第一。关键点：无问芯穹聚焦异构计算平台，帮助开发者适配不同芯片，解决“国产算力碎片化”问题。为什么重要：在国内芯片出口限制持续收紧的背景下，“AI Infra”层的中立平台正在成为稀缺资产。无问芯穹的连续融资反映了资本对算力中间件的押注——越是在硬件受限时，软件抽象层的价值越大。

> 原文：https://www.infoq.cn/article/K1aiYMtOPSTswV999WZR

## DeepL 裁员 250 人，转型“AI 原生”组织

AI 翻译公司 DeepL 宣布裁员约 250 人，占员工总数约 20%，计划将组织重塑为“AI 原生”结构，聚焦核心 AI 能力。关键点：DeepL 表示裁员是为了减少非核心岗位（如传统本地化、运营与商务），集中资源投入 AI 模型研发和产品迭代。为什么重要：DeepL 是少数能在翻译领域与 Google、微软叫板的产品，此次裁员说明即使盈利尚可，AI 公司也必须持续“瘦身”以维持敏捷。这也暗示了“AI 原生”组织意味着摆脱传统服务模式，转为技术驱动。

> 原文：https://the-decoder.com/ai-translation-company-deepl-cuts-around-250-jobs-to-rebuild-as-an-ai-native-organization/

## Snap 与 Perplexity 的 4 亿美元交易友好终止

Snap 宣布，与 Perplexity 原计划将 AI 搜索集成到 Snapchat 的 4 亿美元交易已“友好终止”。双方未透露具体原因。关键点：这笔交易在今年 3 月宣布，本应是 Perplexity 最大的一笔 B2B 合同。友好的终止意味着可能是在商业条款或技术整合上未能达成最终一致。为什么重要：AI 搜索集成到社交平台被视为提升用户粘性的新路径，但集成难度（延迟、内容审核、成本）可能超出预期。对于 Perplexity 而言，失去这一大客户后需尽快找到新的商业化出口。

> 原文：https://techcrunch.com/2026/05/06/snap-says-its-400m-deal-with-perplexity-amicably-ended/

**结语**：今天的两条主线——Anthropic 的算力独占与 OpenAI 的协议开放——拼出了行业对下一个瓶颈的不同判断：是卡不够，还是网不够？你的答案会影响你赌哪家公司。