# Brockman日记当庭读，AI巨头算力军备赛

今日最值得关注的一案：马斯克诉OpenAI庭审中，主席Greg Brockman被迫朗读个人日记，试图证明OpenAI为利润背离初心。这不仅是法律战，也是AI行业从理想主义转向商业化的缩影。同期，Anthropic、DeepSeek与Meta在算力、估值与版权合规上密集落子，行业格局加速分化。

## 马斯克诉 OpenAI 庭审：Brockman 日记被当庭宣读

马斯克律师在庭审中要求 OpenAI 主席 Greg Brockman 逐字朗读其个人日记，以证明 OpenAI 早期承诺的非营利使命已转向利润最大化。Brockman 在法庭上解释，日记中“贪婪”等措辞应结合上下文理解，但陪审团已接触到核心证据。此案的关键在于：OpenAI 是否因与微软的协议丧失了独立性。若马斯克胜诉，可能迫使 OpenAI 重构治理结构或赔偿。

> 原文：[Ars Technica](https://arstechnica.com/tech-policy/2026/05/openai-president-explains-to-jury-why-his-diary-entries-sound-greedy/)

## Anthropic 与 SpaceX 签署计算合同，获取 22 万 GPU

Anthropic 宣布租用 SpaceX 旗下 Colossus-1 数据中心，获得 22 万张 GPU 用于 Claude 的训练与推理，同时提升了代码使用上限。这笔交易标志着 AI 公司开始向太空基础设施延伸算力供应链——SpaceX 凭借低延迟卫星网络和模块化数据中心，正在成为 GPU-as-a-Service 的新玩家。对于 Anthropic，此举可缓解对 AWS/Google Cloud 的过度依赖。

> 原文：[Anthropic 官方新闻](https://www.anthropic.com/news/higher-limits-spacex)

## DeepSeek 估值逼近 450 亿美元，中国芯片基金领投

DeepSeek 即将完成首轮外部融资，估值约 450 亿美元，由国家芯片大基金领投。这不仅是 DeepSeek 首次接受外部资本，也反映出中国在自主 AI 算力生态上的战略押注。相较于 OpenAI 和 Anthropic，DeepSeek 采取更激进的模型开源策略，但估值已接近头部梯队。投资者需警惕：高估值背后是地缘政治风险与商业化路径的不确定性。

> 原文：[The Decoder](https://the-decoder.com/deepseek-nears-45-billion-valuation-as-chinas-state-chip-fund-leads-round/)

## 美国政府获五大 AI 实验室模型预发布权限

美国国防部与五大 AI 实验室（含 OpenAI、Anthropic、Google DeepMind 等）达成协议，在模型公开发布前获准进行国家安全测试。专家警告，该协议可能造成两大隐患：一是政府否决权可能延缓技术迭代，二是测试标准不透明易被利用为行政干预工具。对从业者而言，这意味着今后新模型的发布窗口期可能从“立即”变为“等待联邦放行”。

> 原文：[Ars Technica](https://arstechnica.com/tech-policy/2026/05/everything-that-could-go-wrong-with-trumps-ai-safety-tests-according-to-experts/)

## 苹果支付 2.5 亿美元和解 Siri AI 功能诉讼

苹果同意支付 2.5 亿美元，就 Siri 的 AI 功能宣传与实际延迟不符的集体诉讼达成和解。原告指控苹果在 2023–2025 年间广告中称 Siri 已具备“高级 AI 能力”，但实际功能大幅缩水。这笔赔偿覆盖美国用户，平均每位获赔约 20 美元。关键不在金额，而在于科技巨头必须为“AI 能力超前宣传”付出代价——这将成为产品营销合规的标杆判例。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/06/apple-to-pay-250m-to-settle-lawsuit-over-siris-delayed-ai-features/)

## 出版商指控 Zuckerberg 亲自授权 Meta 版权侵权

在出版商的集体诉讼文件中，原告出示邮件等证据表明 Meta CEO 马克·扎克伯格“亲自授权并鼓励”其 AI 团队使用受版权保护的书籍训练 LLaMA 模型。若指控成立，扎克伯格可能被列为共同被告，面临个人赔偿责任。此案与 OpenAI 庭审形成呼应：管理层对训练数据的知情程度，正成为版权诉讼的攻防焦点。

> 原文：[AP News](https://apnews.com/article/meta-mark-zuckerberg-ai-publishers-lawsuit-llama-5609846d4d840014974a847b01079c32)

## Anthropic 承诺五年内向 Google Cloud 投入 2000 亿美元

Anthropic 与 Google Cloud 签署五年期合同，承诺云服务支出总额达 2000 亿美元（年均 400 亿），进一步加深双方在模型训练和推理上的绑定。有趣的是，Anthropic 同日宣布与 SpaceX 达成算力合作——多供应商策略意在掌控议价权，但 2000 亿美元的承诺规模意味着 Google Cloud 仍是其核心基础设施伙伴。对于 AWS 和 Azure，这是一个明确的抢单信号。

> 原文：[The Decoder](https://the-decoder.com/anthropic-commits-200-billion-to-google-cloud-over-five-years/)

## SAP 以 11.6 亿美元收购德国 AI 实验室 Prior Labs

SAP 以 11.6 亿美元收购成立仅 18 个月的 AI 初创 Prior Labs，并宣布其企业客户 Agent 只能使用 Nvidia NemoClaw 及少量模型。Prior Labs 主攻工业场景的因果推理模型，SAP 此举意图锁定 ERP 领域 AI 话语权。限制模型选择可能引发企业 CIO 反弹，但也反映出 SAP 想构建类似“Apple 围墙花园”的 AI 生态。

> 原文：[TechCrunch](https://techcrunch.com/2026/05/05/sap-bets-1-16b-on-18-month-old-german-ai-lab-and-says-yes-to-nemoclaw/)

---

今天 AI 行业的关键词是“算力绑定”与“治理清算”。当 Brockman 的日记被逐行朗读，你猜下一个被搬上法庭的会是哪一家公司的内部文档？