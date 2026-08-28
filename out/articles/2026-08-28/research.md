# AI 评测进入双盲时代

今天研究板块的头条不在模型，而在评测方法。DeepMind 开全球先河，试点双盲 AI 评估——被评审方与评审方互不知情，目标是让偏见从评测流程里退场。这套源自循证医学的方法论如果跑通，可能直接重写 AI 榜单的可信度。

## DeepMind 试点双盲评估：让偏见无处下手
**是什么**：DeepMind 宣布，将试点全球首个双盲 AI 评估方法。所谓双盲，就是被评审的模型开发方与评审人员互不知晓对方身份与意图，从流程上切断主观偏向。

**关键点**：目前主流评测依赖人类评分与偏好反馈，评审者只要知道模型出自哪家公司，几乎无法避免先入为主。DeepMind 引入双盲，是希望将循证医学常用的方法迁移到 AI 评测，降低人为偏见对结论的影响。

**为什么重要**：评测标准直接决定模型发布节奏、融资与安全监管的走向。双盲试点若能跑通并推广，AI 排行榜与基准测试的可信度将从根基上被重构。

> 原文：[DeepMind](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations/)

## OpenAI 千名学生研究：ChatGPT 提升原创性
**是什么**：OpenAI 公布一项超 1000 名学生的随机对照研究，主题是 ChatGPT 与批判性思维训练。

**关键点**：研究发现，ChatGPT 配合批判性思维训练，能提升真实课程作业中的表现与原创性。重点在于“配合训练”——没有干预的依赖式使用，与经过设计的认知辅助，结果可能截然不同。

**为什么重要**：教育是 AI 落地最敏感的领域之一，随机对照研究这类证据最能左右学校与监管者的判断，也会直接影响 AI 学习产品的设计方向。

> 原文：[OpenAI](https://openai.com/index/what-students-gain-from-chatgpt-critical-thinking-training)

## AI 购物代理：能比价，还不能下单
**是什么**：一项实测研究对主流 AI 购物代理设置真实购买任务，结论是它们尚不适合全权代理消费。

**关键点**：在比价、搜索环节表现尚可，但涉及价格核实、库存判断和支付售后时，出错率明显偏高。长尾商品信息与平台规则，是 agentic 产品在交易场景的普遍短板。

**为什么重要**：agentic AI 的叙事正从信息助手走向交易执行。谁能率先解决安全兜底与异常处理，谁才可能真正拿下“替你花钱”的场景。

> 原文：[The Decoder](https://the-decoder.com/ai-shopping-agents-arent-ready-to-buy-on-your-behalf-study-finds/)

## GlucoFM：0.72M 参数的血糖基础模型
**是什么**：Google Research 与 UNSW 联合推出 GlucoFM，一个仅 0.72M 参数的连续血糖监测基础模型。

**关键点**：模型采用双流设计，对连续血糖监测（CGM）数据做自监督学习。参数规模远小于主流大语言模型，适合在可穿戴设备端运行。

**为什么重要**：数字健康场景对低功耗、端侧推理的需求，让“小而专”的基础模型路线越来越有说服力。GlucoFM 为这一路线提供了新的样本。

> 原文：[Marktechpost](https://www.marktechpost.com/2026/08/26/google-research-introduces-glucofm-a-0-72m-parameter-dual-stream-foundation-model-for-continuous-glucose-monitoring/)

## AI 蛋白质设计：从计算到湿实验的检验
**是什么**：一项基于 Anthropic 的 1440 个 AI 设计蛋白数据的分析，横向对比了 10 种结构预测器。

**关键点**：目标身份、表达滴度和共识评分，被证明是影响实验成功率的关键因素。结构预测与湿实验之间的落差，正是当前 AI 蛋白设计的真实瓶颈。

**为什么重要**：AI 蛋白质设计正从“能生成”迈向“能验证”。只有把计算指标与实验成功率对齐，药物研发和生物制造才会真正买单。

> 原文：[Marktechpost](https://www.marktechpost.com/2026/08/27/from-in-silico-to-wet-lab-evaluating-ai-protein-design-performance/)

## ECCV 2026 议程揭晓：LeCun 压轴，小模型成亮点
**是什么**：ECCV 2026 完整议程公布，图灵奖得主 Yann LeCun 将做压轴演讲。

**关键点**：一个来自中国团队、仅 71M 参数的小模型成为议程亮点。大模型与小模型同台，折射出视觉社区对效率的重新重视。

**为什么重要**：小参数模型在顶会获得关注，是产业算力成本压力的直接映射。对小团队和初创公司而言，小而精意味着更低的入场门槛。

> 原文：[雷峰网](https://www.leiphone.com/category/private/jGUPgQOqPQyCJMMw.html)

从双盲评测到湿实验验证，AI 研究正在多一层“自证”。下一个值得追问的问题是：这些更严格的标准，何时会传导到你我正在使用的产品里？