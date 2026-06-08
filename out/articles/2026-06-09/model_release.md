# 大模型新战局：速度、精度与生态齐飞

今天最值得关注的是两大信号：小米MiMo v2.5-Pro-UltraSpeed以1T参数实现每秒千token，将推理速度推至新量级；DeepSeek V4 Pro则在第三方测试中精度超越GPT-5.5 Pro，开源模型首次在关键指标上压制闭源巨头。Apple同时抛出Core AI框架，选择与Gemini深度整合——模型层竞争已从单一指标转向综合生态。

## 小米MiMo v2.5-Pro-UltraSpeed：千token/s的规模奇迹

**是什么**：小米今日发布超大规模模型MiMo v2.5-Pro-UltraSpeed，参数量达1T，声称推理速度达到每秒1000个token。官方博客展示的benchmark显示，该模型在标准生成任务中延迟低于1秒。

**关键点**：1T参数与千token/s的组合在业界尚属首次。此前千亿级模型（如GPT-4）推理速度通常在几十到几百token/s，而小米通过架构优化（推测采用MoE或稀疏注意力）将速度提升一个数量级。社区热议的焦点在于：如此高速是否以精度为代价？官方未提供side-by-side的精度对比数据。

**为什么重要**：推理速度是模型落地的核心瓶颈。如果千token/s属实，意味着实时对话、代码补全等场景可无缝使用1T参数模型，这将改变大模型部署的性价比公式。对于投资人而言，小米在端侧AI积累的基础上，正通过云侧大模型补齐产品线。

> 原文：[MiMo官方博客](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

## DeepSeek V4 Pro精度超越GPT-5.5 Pro：开源的反击

**是什么**：据第三方评测机构RuntimeWire发布的最新报告，DeepSeek V4 Pro在多项精度测试（涵盖数学推理、代码生成、长文本理解）中平均得分超过OpenAI的GPT-5.5 Pro，领先幅度约2.3%。

**关键点**：这是开源模型首次在通用精度上系统性超越闭源旗舰。测试细节显示，DeepSeek V4 Pro在需要多步推理的任务（如MATH、HumanEval）上优势明显，而在创意写作类任务中仍略逊于GPT-5.5 Pro。该模型采用MoE架构，激活参数仅约200B，但总参数达到1.8T，效率极高。

**为什么重要**：精度是模型能力的“金标准”。DeepSeek的突破意味着开源路线的技术积累已进入收割期——用更低的训练成本（推测约500万美元）实现了接近甚至超越数亿美元训练投入的闭源模型的效果。这对依赖API的创业公司是利好，但对闭源云厂商构成直接压力。

> 原文：[RuntimeWire评测报告](https://runtimewire.com/article/deepseek-v4-pro-beats-gpt-5-5-pro-on-precision)

## Apple发布Core AI框架：与Gemini深度绑定的新生态

**是什么**：在WWDC 2026上，Apple正式推出Core AI框架，并透露其AI架构基于Google Gemini模型，允许开发者在iOS/macOS上直接调用本地+云端混合推理能力。

**关键点**：Core AI并非Apple自研基础模型，而是以Gemini为底层模型，通过on-device适配层实现隐私保护（差分隐私、端侧推理）。框架提供统一的API，覆盖文本、图像、语音，并支持Siri快捷键、Xcode IntelliSense等场景。Apple特别强调，所有数据经过“本地优先”处理，默认不上传云端。

**为什么重要**：Apple选择与Google合作而非自研大模型，折射出模型层研发的高门槛。对开发者而言，Core AI降低了集成成本，但生成了对单一模型供应商的依赖。对小模型厂商来说，Apple的生态壁垒可能进一步挤压第三方AI应用的生存空间——用户会习惯系统级AI，类似当年Spotlight取代第三方搜索插件。

> 原文：[Apple Developer Documentation](https://developer.apple.com/documentation/coreai/)

---

当开源模型在精度上突破、小米在速度上轰鸣、Apple在生态上筑墙，留给自研通用大模型创业公司的时间窗口还剩多少？