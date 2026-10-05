# 稀疏激活，成了开源模型的新战场

今天模型发布板块里最值得看的是 Aleph Alpha 的 Kolibri：78.1B 参数的英德双语 MoE，每个 token 只激活 3.46B，FP8 权重以 Apache 2.0 放开。它未必是能力上限的突破，但把「大参数、小激活」走成了开源默认选项——100 万 token 上下文加上按请求可调的推理强度，是典型的工程取舍而非参数竞赛。同日美团开源视频生成模型、NASA 与 IBM 放出月球基础模型，逻辑相通：把规模藏进稀疏结构，把可用性摆到台前。

## Aleph Alpha 开源 78B 英德 MoE，每个 token 只激活 3.46B

德国 Aleph Alpha 发布 Kolibri，一个 78.1B 参数的英德双语 MoE（Mixture of Experts）模型。核心数字不是 78B，而是 3.46B——每 token 实际激活的参数量，约占总参数的 4.4%。同时支持 100 万 token 上下文、按请求调节的推理强度，FP8 权重以 Apache 2.0 协议开源。

关键点有三个。一是稀疏度做得激进，推理成本更接近 3B 级别的小模型，而不是 78B 稠密模型。二是双语定位明确，英语—德语对欧洲政企客户是刚需，这也是 Aleph Alpha 一贯的地盘。三是「按请求调节推理强度」意味着同一份权重可覆盖低延迟对话与高强度推理两种场景，不必部署两套模型。

为什么重要：开源模型的竞争焦点正在从「参数多大」转向「每 token 花多少算力、换回多少能力」。Kolibri 把这条路线和 Apache 2.0 绑在一起，对做私有化部署的团队来说，是一个值得认真评估的选项。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/04/aleph-alpha-releases-kolibri-a-78-1b-open-weight-english-german-moe-model-with-only-3-46b-active-parameters/)

## 美团把视频生成模型也开源了

美团 LongCat 团队的视频生成模型 LongCat-Video 以开源仓库形式登上 GitHub 热榜，权重与代码一并放出。目前公开信息主要是仓库本身，参数规模、生成时长等细节尚未在素材中体现。

可确认的关键点有两个。一是中国大厂的开源节奏已经从语言模型延伸到视频生成，且选择直接放权重而非只发论文或 API。二是登上 GitHub 热榜说明社区试用意愿高，但热榜反映的是关注度，不是质量——视频生成的真实水平要看时序一致性、可控性和推理成本这些指标。

为什么重要：对产品经理来说，视频生成的可选清单里多了一个「可以自部署」的条目。当权重可下载，微调、私有数据注入和成本控制的空间都随之打开，这会直接影响采购决策——是继续买 API，还是自己搭一套。

> 原文：[GitHub - meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video)

## NASA 和 IBM 把 17 年月球轨道数据炼成基础模型

NASA 和 IBM 联合开源了一个月球基础模型，训练数据来自 17 年的月球轨道器观测数据，用途包括月球科学中的水冰（water ice）探测等任务。

关键点在于范式的迁移。过去行星科学通常为单一任务单独训练模型，现在先用长期积累的遥感数据预训练一个底座，再往下接具体科学任务。17 年的轨道数据意味着时间跨度长、重复观测多，天然适合变化检测类的问题。水冰探测则直接关联未来月球驻留的资源获取与选址，是有工程后果的科学问题，不是纯粹的学术练习。

为什么重要：这是基础模型的一条外溢路径——不卷参数、不卷对话能力，而是吃掉某个垂直领域几十年的存量数据。科研机构与大厂的这种合作模式，很可能被复制到气候、海洋、地质等方向。

> 原文：[The Decoder](https://the-decoder.com/nasa-and-ibms-open-source-lunar-model-turns-17-years-of-orbiter-data-into-a-foundation-for-lunar-science/)

## 四款前沿模型横评：谁适合干什么活

一份横评把 GPT-6 Astra、GPT-6.1 Sol、Gemini 4 Argon、Claude Fable 5.1 放在一起比较。结论大致是：GPT-6 Astra 强在电脑操作（computer use），Gemini 4 Argon 在法律、金融这类专业文本上表现更好，GPT-6.1 Sol 在编码 agent 场景里性价比最高。

关键点在于选型的维度变了。过去横评看「谁分数高」，现在看「谁在你的任务上单位成本产出高」。同一个厂商内部出现 Astra 和 Sol 这样能力互补的两个型号，说明前沿模型的 SKU 化已经开始。

为什么重要：对做技术选型的人，单一「最强模型」的判断正在失效，需要按任务类型建一个矩阵。但要留意，这类横评的结论高度依赖测试集选取，法律金融、电脑操作这些方向的可复现性差异很大，把它当线索而不是结论更稳妥。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/04/gpt-6-astra-vs-gpt-6-1-sol-vs-gemini-4-argon-vs-claude-fable-5-1-which-frontier-model-fits-which-job/)

当激活参数、推理强度和单价都能按请求调，模型选型就从「选最强的」变成了「选最合适的」。你自己的工作流里，有哪个环节其实一直在用前沿模型干小模型的活？