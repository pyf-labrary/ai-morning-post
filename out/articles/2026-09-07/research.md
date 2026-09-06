# GPT-6 得分有争议，AI 评测也需自证

今天研究板块最值得关注的是 Artificial Analysis 在 GPT-6 Astra 得分遭广泛质疑后，重构 Intelligence Index 并重新校准模型排行。真正重要的不是某个分数修正，而是它承认：评测方法论本身可能就是最大的误差来源。基准工具终于开始像模型一样被审视了。

## 智能指数重构：被质疑的不只是 GPT-6

Artificial Analysis 这次不是做小修补，而是对 Intelligence Index 的方法论进行大修，并在新方法下重新校准整个模型排行。GPT-6 Astra 的得分之所以引发外界怀疑，说明人们对评测样本、指标权重和榜单逻辑的信任已经出现裂缝。平台选择重构方法论，等于默认公开测试本身需要“自证”。AI 能力榜单不仅是技术参照，也会影响开发者选型和企业采购判断。修复方法论的准确性，本质上是在修复榜单的公信力。

> 原文：[The Decoder — Artificial Analysis overhauls its Intelligence Index after GPT-6 Astra scoring drew skepticism](https://the-decoder.com/artificial-analysis-overhauls-its-intelligence-index-after-gpt-6-astra-scoring-drew-skepticism/)

## 七分钟对话，比事实清单更能松动信念

两项实验比较了两种干预方式：与 AI 聊天机器人深入对话约 7 分钟，或者阅读一份事实清单。结果是前者更能有效降低阴谋论信念。关键差别在于对话是双向的——AI 可以针对用户深信的具体论点逐条回应，而不是提供一份通用的反驳材料。这意味着 AI 正在被证明是一种“说服工具”。它既可以用于辟谣，也可能被用来制造更难以察觉的定制化叙事。认知干预的技术门槛正在下降，而治理工具还没有跟上。

> 原文：[The Decoder — Seven minutes with a chatbot beat a fact sheet at reducing conspiracy beliefs in two experiments](https://the-decoder.com/seven-minutes-with-a-chatbot-beat-a-fact-sheet-at-reducing-conspiracy-beliefs-in-two-experiments/)

## RPM：先给实验排队，再决定花 GPU

Meta FAIR 与牛津、UCL 合作，提出 AI 研究偏好模型（AI Research Preference Models, RPMs）。它用冻结状态的 LLM 对候选实验排序，只挑出最有希望的一项去执行，而不是全部跑一遍。它做的是研究流程中的“决策层自动化”——把研究者挑选实验方向的直觉，显式化为可排序的偏好模型。当算力预算逼近上限，研究自动化的瓶颈就不再是把实验跑完，而是如何少跑实验并找到最优解。RPM 是一个代表性思路。

> 原文：[MarkTechPost — Meta FAIR introduces AI Research Preference Models (RPMs): ranking ML experiments before spending GPU hours](https://www.marktechpost.com/2026/09/06/meta-fair-introduces-ai-research-preference-models-rpms-ranking-ml-experiments-before-spending-gpu-hours/)

## 循环 Transformer 重返焦点，阿里此前已下注

循环 Transformer（recurrent Transformer）架构概念因 GPT-6 重回讨论中心。中文媒体报道称，阿里已有两篇顶会论文提前布局该方向。报道没有证实 GPT-6 本身采用循环结构，但注意力机制在高成本长序列处理上的瓶颈一直存在。如果循环思路能在固定开销内处理更长上下文，它对现有 Transformer 主导地位可能形成真正的竞争。国内大厂提前押注，说明这个判断早在 GPT-6 引发讨论之前就已形成。

> 原文：[量子位 — GPT-6 带火循环 Transformer，阿里早已押注](https://www.qbitai.com/2026/09/484726.html)

## 具身 ICL：机器人靠长上下文快速学技能

上下文学习（in-context learning）正在从语言模型延伸到机器人领域。创业公司尝试给机器人更长的多模态 context，让它直接观察任务示范或环境描述，并快速执行新技能，既不需要重新训练，也不需要大规模微调。如果这条路走得通，机器人部署将从“每项技能都要训练”变成“在上下文中即时学会”，硬件投入和场景扩展的边际成本都会明显下降。不过目前仍处于早期探索，真实物理环境里的稳定性与泛化还没有被充分验证。

> 原文：[量子位 — 具身 ICL 成新赛道：机器人靠长上下文快速学会技能](https://www.qbitai.com/2026/09/484897.html)

## 把大模型比作“认知病毒”，值得当真的部分是什么

一篇 arXiv 论文将大模型类比为“认知病毒”，讨论其对人类思想传播和信息环境的潜在影响，相关讨论已在社区扩散。注意，它给出的更多是思考框架，而不是实证数据。真正的观察点是：当 AI 深度嵌入信息流动，思想的生产、复制和扩散速度都会发生变化。把它和上面的阴谋论实验放在同一天看，刚好是一组镜像——AI 既能松动既有信念，也可能成为新思想的超级传播者。我们还没有准备好区分这两种速度。

> 原文：[arXiv — 新论文将大模型比作“认知病毒”](https://arxiv.org/abs/2609.03344)

评测体系开始重构，架构叙事发生回摆，机器人学习方式也在寻找新的捷径——这些变化背后的共同问题只有一个：我们如何确认一个 AI 系统真的在按我们希望的方式工作？也许评测方法要比模型本身迭代得更快。