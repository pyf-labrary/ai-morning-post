# 今日研究：7B模型击败GPT-5？AI写论文融14亿

今天研究板块看点密集：AI系统独立生成数学论文被顶会接收、7B医学Agent在诊断任务上碾压GPT-5，同时企业级Agent基准揭示前沿模型准确率均未过半。小模型专精化与大模型泛化能力之间的张力愈发明显。

## ITBench-AA 基准：前沿模型在企业 IT 任务中均低于 50%

IBM 与 Artificial Analysis 联合推出首个面向企业 IT 任务的 Agent 基准 ITBench-AA，涵盖故障排查、配置管理等真实场景。测试结果令人警醒：GPT-5.5、Claude 4、Gemini 2.5 Pro 等最新模型的准确率全未超过 50%，最高分来自 Claude 4 的 48%。这暴露了当前模型在复杂多步企业任务中的系统性短板：它们善于回答但拙于执行，尤其在需要上下文追踪、多工具调用的场景下表现乏力。对这一基准的后续改进，将成为评估企业级 Agent 实用性的重要标尺。

> 原文：[https://huggingface.co/blog/ibm-research/itbench-aa](https://huggingface.co/blog/ibm-research/itbench-aa)

## 研究揭示 LLM 即使被明确警告也「相信」错误断言

一项微调实验发现，大模型对训练数据中植入的错误信息存在顽固偏差。即使后续加入“以下信息可能为假”的明确警示，模型在推理时仍倾向于重复原始错误。这种“教条主义”根源于预训练阶段嵌入的知识权重远高于后训练的纠正信号。对安全关场景（法律、医疗）而言，意味着单纯依靠 prompt 级防护难以消除错误记忆，可能需要更根本的模型架构或训练策略调整。

> 原文：[https://arstechnica.com/ai/2026/05/llms-believe-false-statements-even-after-explicit-warnings-that-theyre-false/](https://arstechnica.com/ai/2026/05/llms-believe-false-statements-even-after-explicit-warnings-that-theyre-false/)

## ESM 蛋白质世界模型发布：6.8B 蛋白、1.1B 结构

BioHub 发布 ESMFold2 与 ESMC-6B，覆盖 68 亿蛋白质序列、11 亿三维结构，成为目前最大的蛋白质语言模型。ESMFold2 在结构预测速度上比 AlphaFold3 快两个数量级，ESMC-6B 则在序列功能预测上达到 SOTA。这标志着 AI 驱动生物学从“解析已知”向“设计未知”迈进——可编程生物学的工程化平台业已成形，对合成生物学、药物发现意义深远。

> 原文：[https://www.latent.space/p/esmfold2](https://www.latent.space/p/esmfold2)

## AI 生成的 5 篇数学论文被会议接收，创业公司获 14 亿融资

00 后创始人洪乐潼的 AI 系统独立完成数学定理发现、形式化证明与论文撰写，在 8 篇投稿中有 5 篇被国际数学会议接收。其公司已获 14 亿元融资。关键点在于：系统不依赖人工修改，全程自主，且证明过程经形式化验证避免幻觉。这件事的意义不在于取代数学家，而是展示了“LLM + 形式化验证”闭环可能催生真正的科学发现 agent，颠覆传统科研范式。

> 原文：[https://www.qbitai.com/2026/05/426198.html](https://www.qbitai.com/2026/05/426198.html)

## Sakana AI 提出 DiffusionBlocks：分块训练残差网络

Sakana AI 将残差网络（ResNet）的每个块视为独立可训练的“去噪模块”，训练方式类似扩散模型的 block-wise 框架。通过随机屏蔽块间连接，使每一块学会局部去噪而非全局残差拟合，最终在 CIFAR-10、ImageNet 上以更少参数实现可比精度。这为大规模网络的分阶段训练提供了新思路，有望降低超大模型的训练显存需求。

> 原文：[https://www.marktechpost.com/2026/05/27/sakana-ai-proposes-diffusionblocks-a-block-wise-training-framework-that-converts-residual-networks-into-independently-trainable-denoising-modules/](https://www.marktechpost.com/2026/05/27/sakana-ai-proposes-diffusionblocks-a-block-wise-training-framework-that-converts-residual-networks-into-independently-trainable-denoising-modules/)

## 7B 医学 AI 智能体击败 o3、GPT-5：学会“看哪、怎么看”

一种参数量仅 7B 的医学诊断 Agent 在多个权威数据集上超越 GPT-5、o3 等大模型。其核心创新在于新型注意力机制——模型学会同时定位病灶区域（看哪）并确定诊断推理路径（怎么看），形成细粒度聚焦+逻辑链的协同。这意味着医学 AI 正从“参数军备竞赛”转向“架构效率竞赛”：小模型+结构化注意力在专科任务上可以反超大模型。

> 原文：[https://www.qbitai.com/2026/05/426150.html](https://www.qbitai.com/2026/05/426150.html)

## ICRA 2026 多机器人研究：灵巧操作、双臂协同取得进展

ICRA 2026 上，多团队展示机器人操纵新成果：李飞飞团队提出软体物体变形实时跟踪算法，新国立展示双臂自适应抓取，港中文提出力蒸馏视觉-语言-动作（VLA）模型。这些工作共同指向一个趋势：从单一刚体抓取向柔性、动态、双臂协同场景迁移，且引入语言引导与力反馈闭环。具身智能的学术前沿正从“能不能动”转向“够不够灵”。

> 原文：[https://www.leiphone.com/category/robot/sfkY58PVaS2MHomp.html](https://www.leiphone.com/category/robot/sfkY58PVaS2MHomp.html)

## 星源智发布 400 万问答对数据集，具身模型学会“先想后做”

星源智推出大规模具身问答数据集 EG-QA，涵盖 400 万条“任务-子步骤-动作”序列。配套训练框架使模型学会先推理再执行，在模拟器任务中决策性能碾压 GPT-5 的零样本版本。关键点在于：数据集不仅包含动作标签，还包含“为什么这样做”的推理链，从而赋予具身模型可解释的规划能力。这对家庭机器人、仓储拣选等场景有直接价值。

> 原文：[https://www.infoq.cn/article/zleRjMWUeNF4C9zTeX8p](https://www.infoq.cn/article/zleRjMWUeNF4C9zTeX8p)

---

今天的研究版图：大模型在通用企业任务上令人失望，但小模型专精化、AI 科学自主发现、具身推理都在突破。未来一年，你会更愿意押注“更大”还是“更巧”？