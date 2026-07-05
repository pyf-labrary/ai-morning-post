# 数小时移植经典RTS，Claude Science登场

导语：今天最值得关注的是，开发者用Claude Code和Fable仅数小时就将2003年的PC游戏《命令与征服》原生移植到iOS——这是AI辅助编码在游戏领域的高效示范。与此同时，Anthropic发布的Claude Science Beta为科研自动化提供了多智能体工作台，值得科学计算从业者关注。此外，NVIDIA的HORIZON与百度无限OCR也从不同角度展示了AI对执行类任务的渗透。

## Claude Fable数小时将《命令与征服》移植到iOS

**是什么**：开发者使用Claude Code搭配Fable，将2003年的PC游戏《命令与征服》原生移植到iPhone/iPad，全程耗时仅数小时。这不是模拟器或流式传输，而是真正的原生iOS移植。

**关键点**：Claude Code提供了代码理解和生成能力，Fable负责游戏引擎适配，两者结合使移植流程从数周压缩到几小时。

**为什么重要**：它大幅降低了经典游戏移植的技术门槛和成本；随着AI编码能力增强，未来可能形成“用自然语言描述需求→AI自动生成原生移植”的工作流，改变整个怀旧游戏产业。

> 原文：https://the-decoder.com/claude-code-and-fable-5-ported-the-2003-pc-game-command-conquer-to-native-ios-in-a-few-hours/

## Anthropic发布Claude Science Beta多智能体科学工作台

**是什么**：Anthropic推出的Claude Science Beta是一个多智能体系统，专为基因组学、蛋白质组学等科学流水线设计，内置自动评审和图表生成。

**关键点**：它并非单次问答，而是编排多个Agent协作完成实验设计、数据分析和结果验证，支持完整的工作流自动化。

**为什么重要**：对于生物信息学、药物发现等领域，这种“AI科学家”能显著缩短从假设到验证的周期；同时其内置自动评审机制，尝试解决科研AI结果可重复性的挑战。

> 原文：https://www.marktechpost.com/2026/07/04/anthropic-launches-claude-science-beta/

## Fable创建全新4D splat格式惊艳社区

**是什么**：同样是Fable生态的产出——开发者利用Fable创建了4D高斯泼溅新格式，能够渲染随时间变化的三维动态场景。

**关键点**：传统3D高斯泼溅只表示静态场景，4D splat加入时间维度，可以捕获运动、变形等动态效果，且保持高质量渲染。

**为什么重要**：在影视特效、数字孪生和AR/VR中，动态场景渲染是长期痛点；4D splat提供了一种高效且视觉质量高的新方案，可能成为下一代表征方法。

> 原文：https://adamraudonis.github.io/splats4D/

## NVIDIA发布HORIZON：全自动RTL设计Agent

**是什么**：NVIDIA推出的HORIZON是一个无需人工干预的Agent，专门用于RTL（寄存器传输级）设计。它通过Git Worktree技术管理每一个RTL问题，据称在基准测试中达到100%完成率。

**关键点**：设计空间探索和验证是芯片设计中最耗时的环节之一；HORIZON能自动化此流程，且Git Worktree确保版本管理和任务隔离。

**为什么重要**：若100%基准完成率属实，它有望大幅缩短芯片设计周期，让硬件工程师将精力聚焦在架构创新而非细节调试上，是硬件AI自动化的标志性进展。

> 原文：https://www.marktechpost.com/2026/07/04/nvidia-horizon-a-hands-free-agent-that-evolves-git-worktrees-and-hits-100-rtl-benchmark-completion/

## KiCad PCB设计工具上线浏览器版

**是什么**：开源PCB EDA套件KiCad如今支持直接在浏览器中运行，兼容Firefox和Chrome，零安装即可使用全套功能。

**关键点**：浏览器版意味着跨平台（包括Chromebook和移动设备），且保持与桌面版相同的功能，降低电子设计入门门槛。

**为什么重要**：让更多人能参与硬件原型设计；同时为云端协作工作流铺路——团队可以实时分享设计而无需安装软件，加速硬件社区的协作创新。

> 原文：https://demo.pcbjam.com/

## 百度推出‘无限OCR’：一次处理数十页文档

**是什么**：百度发布的“无限OCR”通过模拟人类遗忘机制的内存管理，实现对文档的批量识别：一次扫描即可处理数十页，而非逐页。

**关键点**：传统OCR受限于内存和上下文窗口，长文档需分页处理；百度模拟人类遗忘（类似Transformer的记忆压缩），让模型向前处理时动态遗忘旧信息以支持更长序列。

**为什么重要**：文档数字化（合同、历史文献等）场景中，效率提升可能是数量级的；不过准确率和长文本一致性仍需实际验证，但思路值得关注。

> 原文：https://the-decoder.com/baidus-unlimited-ocr-processes-dozens-of-document-pages-in-one-pass-by-treating-memory-like-human-forgetting/

## Google推出AI独立宣言广告庆美国建国250周年

**是什么**：Google为纪念美国建国250周年推出广告，主题为“国父们用Google Workspace写独立宣言”，展示AI辅助写作的历史想象。

**关键点**：广告暗示AI是现代书写工具的自然延续，旨在推广Google Workspace的AI功能（如Gemini），商业意图明显。

**为什么重要**：科技公司试图与历史叙事绑定以塑造公众认知；这种营销手法能否获得受众认可，还需观察社会对“AI改写历史”的敏感度，尤其在美国当前政治文化语境中。

> 原文：https://techcrunch.com/2026/07/04/new-google-commercial-imagines-a-declaration-of-independence-written-with-help-from-ai/

结语：今天的故事共同指向一个趋势——AI正在从“回答工具”进化为“执行工具”，无论是移植游戏、设计芯片还是处理科学流水线。留给读者的问题：当AI能独立完成这些具体任务时，人类的角色将如何重新定位？