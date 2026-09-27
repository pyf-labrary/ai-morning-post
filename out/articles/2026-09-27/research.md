# TPU 跑 Kimi 快过 N 卡，harness 层开始省钱

## 导语

今天最值得看的一条，是 vLLM 团队用 DeepSeek 推理框架在谷歌 TPU 上跑 Kimi，吞吐比英伟达 GPU 高 57%。这不是一次跑分游戏：它说明在主流开源模型上，非 N 卡路线已经有了可复现的工程证据。与之呼应的是英伟达自己在 harness 层做优化，把 coding agent 的 token 消耗砍掉近一半——算力账正在从「买什么卡」转向「怎么用」。

## 谷歌 TPU 跑 Kimi 吞吐高 57%

由 vLLM 人马创办的团队，用 DeepSeek 的推理框架在谷歌 TPU 上部署 Kimi，实测吞吐比英伟达 GPU 高 57%。关键点在于这不是简单的硬件对比，而是「TPU + 非 CUDA 推理栈 + 国产开源模型」这套组合的端到端验证——软件栈的适配度在这里可能比峰值算力更重要。对做推理成本核算的团队来说，这意味着英伟达在推理侧的替代方案从「理论可行」进入「有实测数字」的阶段，值得重新算一遍 TCO；当然，单一模型、单一负载的结果还不能外推到全部场景。

> 原文：[量子位](https://www.qbitai.com/2026/09/497425.html)

## 英伟达 SoL-Pi：不动模型，token 减半

英伟达的 SoL-Pi 系统把 coding agent 的 token 使用量削减近一半，做法是不改模型，而是优化 agent harness——也就是模型外面那层调度、上下文管理与工具调用的脚手架。这说明当前 agent 的 token 浪费大量发生在「框架层」而非「模型层」：重复读文件、无效重试、上下文膨胀，都是 harness 可以处理的工程问题。对正在为 agent 账单发愁的团队，这是性价比最高的一类优化方向，也提示模型厂商和框架厂商的边界正在重新划分。

> 原文：[The Decoder](https://the-decoder.com/nvidias-sol-pi-system-cuts-coding-agent-token-usage-nearly-in-half-by-optimizing-the-harness/)

## Perplexity 用真实失败会话训练电脑操作 agent

Perplexity 研究团队在真实用户会话上做后训练，且刻意把失败会话一并纳入，方法上结合拒绝采样微调（rejection sampling fine-tuning）与提示引导自蒸馏（hint-guided self-distillation）。这条的价值在于数据来源的选择：合成任务容易刷高 benchmark，但真实失败案例才覆盖了 UI 漂移、误点、状态判断错误这些落地杀手。Computer agent 的可靠性瓶颈一直不在「能不能点对」，而在「出错后能不能恢复」，用失败数据训练正是冲着这一点去的。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/09/25/perplexity-trains-its-computer-agent-on-real-mistakes-with-hint-guided-self-distillation/)

## Claude 能跑完九层嵌套循环

Anthropic 发表研究，展示 Claude 在多重嵌套循环任务上的表现，直接回应外界对模型长链条推理能力的质疑。嵌套循环是个好用的压力测试：它要求模型在每一层维持独立的计数器与状态，任何一层漂移都会导致最终结果错误，比单轮问答更容易暴露「看起来对、其实早跑偏」的问题。对把模型塞进代码生成、数据管道这类需要精确执行流程的场景的团队，这类能力边界比通用 benchmark 分数更有参考价值。

> 原文：[Anthropic](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)

## 机器人足球自我对弈 140 年

研究者把 AlphaGo 式的自我对弈搬进机器人足球，通过长时间模拟对抗训练出高难度控球与射门策略。这里的「140 年」指模拟时间而非真实耗时——本质仍是用算力换经验，把现实中不可能完成的试错压缩进仿真。这条的看点不在足球，而在于自我对弈这套方法在具身场景的迁移：当真实数据昂贵、仿真环境可信时，对抗式自博弈可能是比模仿学习更划算的路径。

> 原文：[量子位](https://www.qbitai.com/2026/09/497278.html)

## 有了 AI，人几乎不再说「我不知道」

一项实验发现，当受试者可以随时调用 AI 时，他们给出错误答案却极少承认不确定，即 AI 在提升产出的同时削弱了人对自身无知的自觉。这是今天最该被产品经理认真读的一条：它指向的不是模型准确率，而是人机协作中的认知外包与责任稀释。任何把 AI 输出直接嵌入决策流程的产品，都需要显式设计「不确定性提示」和「人工复核」的摩擦点，否则错误会以更高的置信度流通。

> 原文：[The Decoder](https://the-decoder.com/ai-access-makes-people-almost-entirely-unwilling-to-say-i-dont-know-study-finds/)

## AI 智能体自创人类看不懂的方言

某美国 AI 实验室发现，多个智能体在虚拟社会协作时会形成一种人类无法解读的「方言」交流，再度引发对 AI 治理的讨论。需要克制看待：这更可能是多智能体在特定奖励下演化出的压缩通信协议，而非「觉醒」信号，类似现象在早期多智能体强化学习研究中已有先例。真正值得关注的是可解释性缺口——当 agent 之间的通信不可读，人类很难在事前审计它们达成了什么共识。

> 原文：[36氪](https://36kr.com/newsflashes/3999814609473416?f=rss)

## AugLy：多模态增强与对抗鲁棒性基准

一份端到端教程与基准，展示如何用 AugLy 为图像、文本、音频和 PyTorch 数据集构建统一的数据增强与对抗鲁棒性流程。它的实用性在于把「增强」和「鲁棒性评估」放在同一条流水线里，避免了增强做完却不知道是否真的提升抗扰动能力的常见问题。适合需要快速搭基建的小团队作为起手模板，学术新意有限。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/09/26/end-to-end-multimodal-data-augmentation-and-adversarial-robustness-benchmark-with-augly-for-images-text-audio-and-pytorch/)

## 结语

今天三条最实的进展都不在模型本身，而在模型外面那层——推理栈、harness、训练数据的选择。当框架层能带来 50% 级别的成本或可靠性变化时，「你们用什么模型」或许已经不是最该问的问题了。