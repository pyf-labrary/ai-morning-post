# AISI：GPT-5.5 网络攻击能力比肩 Mythos

英国 AI 安全研究所公开报告，GPT-5.5 在多项网络攻击任务上与 Anthropic 的 Mythos 持平甚至更优，完成专家级任务仅需 11 分钟、成本 1.73 美元。这是继模型能力竞赛后，安全评估首次正面碰撞——当攻击成本降到不足一杯咖啡的价格，红队与防御者的天平正在倾斜。

## GPT-5.5 与 Mythos：攻击能力接近，成本悬殊

AISI 的报告测试了 GPT-5.5 在自动化渗透测试、漏洞利用、社会工程等任务上的表现。结果显示，GPT-5.5 在多个指标上与 Mythos 不相上下，但在生成可执行代码的成功率上略高。一个原本需要 12 小时的人类专家任务，GPT-5.5 平均用 11 分钟完成，总 API 成本仅 1.73 美元。AISI 强调，这并不意味着模型是“危险”的——但能力门槛下降意味着需建立新的护栏。

> 原文：https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities

## DeepMind 发布 AI co-clinician：与医生联合问诊

Google DeepMind 推出 AI co-clinician，目标是作为医生辅助工具，而非替代品。该模型能够实时分析患者对话、提取关键症状、提供鉴别诊断建议，并自动生成结构化病历。关键点在于它被设计为“聆听后提出建议”，医生保留最终决策权。重要性在于：AI 在临床流程中的角色从“辅助读取影像”进化为“参与诊疗对话”，对医疗信息化产品形态有直接影响。

> 原文：https://deepmind.google/blog/ai-co-clinician/

## xAI 正式发布 Grok 4.3，性能提升但细节保留

xAI 发布 Grok 4.3，宣称在推理、编码和多轮对话上进一步优化，但未公开参数量、训练数据规模或评估基准的具体结果。对比前序版本，此次更新重点放在减少幻觉和长上下文处理上。对于技术从业者，缺乏透明度的发布意味着无法直接横向对比；但对 xAI 生态而言，Grok 4.3 仍可能是 X 平台嵌入 agentic 功能的核心动力。

> 原文：https://docs.x.ai/developers/models/grok-4.3

## IBM 开源 Granite 4.1：8B 参数对标 32B MoE 性能

IBM 发布 Granite 4.1 系列开源模型，其中 8B 版本在多个基准上接近或匹敌 32B MoE 级别的模型。核心技术包括改进后的混合注意力机制和更高效的 tokenizer。根据 IBM 公开数据，8B 模型在 MMLU、GSM8K 上分别达到 78.2% 和 84.5%，推理速度是同级模型的 2-3 倍。重要性在于：它证明参数精简路线依然有效，中小型团队可用更低成本部署高性能模型。

> 原文：https://research.ibm.com/blog/granite-4-1-ai-foundation-models

## NVIDIA 发布 Gemma-4 量化版：RTX 5090 本地跑 50K 上下文

NVIDIA 推出 Gemma-4-26B-A4B-NVFP4，基于 Google 的 Gemma-4 进行 4-bit 量化，混合 NVFP4 格式精度。在 RTX 5090 上可运行约 50K token 上下文，而精度损失在 1-2% 以内。该模型适合本地部署场景（敏感数据处理、离线推理），对个人开发者和企业边缘计算有实际意义。

> 原文：https://huggingface.co/nvidia/Gemma-4-26B-A4B-NVFP4

## 社区实测：Gemma 4 31B 编码速度远快于 Qwen 3.6 27B

Reddit 用户对比测试两个本地模型制作贪吃蛇游戏的编程能力。Gemma 4 31B 仅用约 40 秒生成可运行代码，而 Qwen 3.6 27B 耗时近 3 分钟——但后者生成了更多 token 和更详细的注释。该测试不具备科学严谨性，但反映了实际用户体验中速度与完整度的权衡。

> 原文：https://v.redd.it/s0czzkm85fyg1

当最先进的模型可以 1.73 美元完成一次网络入侵，防御者需要重新思考“安全阈值”——是模型能力本身，还是我们部署护栏的速度？