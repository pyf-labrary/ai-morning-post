# Step 3.7 Flash：198B视觉MoE，编程Agent迎来新对手

**导语**：今天最值得看的模型发布是StepFun的198B MoE视觉语言模型Step 3.7 Flash，以原生视觉+256k上下文直指编程Agent和搜索工作流。海光同日适配，本土化部署速度值得关注。同时Liquid AI开源8B-A1B MoE、英伟达开源Eagle视觉模型，生态持续分化。

## StepFun发布Step 3.7 Flash：198B MoE视觉语言模型

**是什么**：StepFun（阶跃星辰）推出Step 3.7 Flash，198B参数MoE（混合专家）架构，原生支持视觉输入，上下文长度256k token。模型面向编程Agent与搜索工作流场景，同日海光（Hygon）完成适配，可在国产硬件上部署。

**关键点**：参数规模为198B（含激活参数推测较低），MoE架构推理效率优于稠密模型；256k上下文在长代码、多轮搜索场景有优势；海光适配意味着国产算力闭环加速。

**为什么重要**：这是国内少数对标GPT-5级别视觉语言模型的开源/商用选择，尤其针对编程Agent这一实战场景。海光适配进一步降低了大模型国产化落地的门槛。对于技术团队，值得评估其在代码补全、RAG搜索中的实际延迟与精度。

> 原文：[StepFun releases Step 3.7 Flash](https://www.marktechpost.com/2026/05/29/stepfun-releases-step-3-7-flash-a-198b-moe-vision-language-model-for-coding-agents-and-search-workflows/)

## Liquid AI发布8B-A1B MoE模型，训练于38T tokens

**是什么**：Liquid AI推出LFM 2.5 8B-A1B，8B总参数、1B激活参数的MoE模型，训练数据量为38T tokens。模型在多项基准（MMLU, HumanEval等）表现超越同规模竞品，在Hacker News引发热议。

**关键点**：仅1B激活参数即可达到较优性能，推理成本极低；训练数据量38T远超同体量模型（如8B稠密模型通常只训练2-4T），数据质量与混合策略可能是关键差异。

**为什么重要**：对于边缘设备、实时推理场景，这类“小激活”MoE模型极具吸引力。Liquid AI延续其神经架构搜索+高效训练的路线，可能重新定义8B级别性价比上限。

> 原文：[Liquid AI LFM 2.5 8B-A1B](https://www.liquid.ai/blog/lfm2-5-8b-a1b)

## OpenAI升级GPT-5.5 Instant可读性，逐步淘汰旧模型

**是什么**：OpenAI为GPT-5.5 Instant模型提升可读性（readability），同时开始淘汰两个较老模型版本，具体版本号未披露。该升级主要改进输出文本的流畅度与逻辑连贯性。

**关键点**：可读性提升可能针对长文本生成场景（如报告、邮件）；淘汰旧模型是OpenAI惯用的模型生命周期管理，暗示GPT-5.5 Instant已稳定并进入大规模替换阶段。

**为什么重要**：对于API调用者，需关注旧模型下线时间线以避免生产环境中断。可读性提升对To C应用体验直接影响，但对技术判断而言，本次更新幅度较小，属常规迭代。

> 原文：[OpenAI gives GPT-5.5 Instant a readability upgrade](https://the-decoder.com/openai-gives-gpt-5-5-instant-a-readability-upgrade-while-phasing-out-two-older-models/)

## 英伟达发布Eagle视觉语言模型，数据驱动策略

**是什么**：NVlabs（英伟达研究）开源Eagle系列视觉语言模型，采用“数据为中心”的训练策略，即通过精心设计训练数据集（而非单纯增大模型或数据量）来提升性能。模型在多个视觉语言榜单（如MMBench、MMMU）上取得领先。

**关键点**：开源权重，社区可复现；数据积累是英伟达做多模态的核心壁垒，这次公开了部分数据策略思路；模型规模未详细公布，但侧重中等规模（7B-13B级别）。

**为什么重要**：英伟达从“算力提供商”转向“算法开源者”，Eagle的出现可能影响视觉语言模型的技术路线——数据质量比模型规模更关键。对产品经理而言，这是评估多模态能力底座的又一选择。

> 原文：[NVlabs/Eagle GitHub](https://github.com/NVlabs/Eagle)

**结语**：模型发布进入“开卷考试”阶段，198B MoE、1B激活MoE、数据驱动视觉模型——资源效率与场景专注正在取代纯参数竞赛。如果只能关注一个信号，Step 3.7 Flash的国产化适配进度值得追踪。