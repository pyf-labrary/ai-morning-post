# 神经动力学芯片快 478 倍，AI 基准需重构

今天最值得看的是两件事：北大团队造出全球首款神经动力学芯片，运行速度比 GPU 快 478 倍，成果登上《科学》；另一边，UK AI 安全研究所却发现标准基准系统性低估了 AI Agent 的真实能力。硬件跃进与评估体系失灵之间的矛盾，正在加速爆发。

## 全球首款神经动力学芯片问世，比 GPU 快 478 倍

北京大学团队基于相变忆阻器研制出神经动力学芯片，突破了实时计算在硬件层面的瓶颈。该芯片不再依赖传统冯·诺依曼架构，而是模拟神经突触的可塑性，实现了毫瓦级功耗下的超高速运算。测试数据显示，在特定神经网络任务上，其能耗比和速度分别达到 GPU 的数百倍。研究成果发表于《科学》杂志，意味着中国在新型计算器件领域走到了全球最前沿。

> 原文：[36氪](https://36kr.com/newsflashes/3880779651248391)

## 华为何庭波发布“韬定律”V2 论文，补充工程数据

华为半导体负责人何庭波发布后摩尔时代缩放理论 V2 版，新增 **LogicFolding** 齿比概念和实测数据。V1 版曾提出晶体管密度增长放缓后的替代缩放路径，V2 在此基础上面向实际芯片设计提供了齿比——即逻辑单元折叠与布线的比例——的量化参考。这意味着华为正在把理论模型推向可工程落地的工具，对 SoC 架构师和投资判断 chiplet 路线都有直接参考价值。

> 原文：[36氪](https://36kr.com/newsflashes/3880931591254019)

## UK AI 安全研究所：标准基准严重低估 Agent 能力

UK AI 安全研究所（UK AI Security Institute）在最新研究指出，现有基准测试（如 GAIA、SWE-bench）系统性低估了 AI Agent 的实际能力。原因在于这些基准往往只关注独立子任务的完成率，忽略了 Agent 在上下文衔接、工具调用链和错误恢复方面的综合表现。该机构呼吁开发面向动态环境的评估方法，否则安全监管将建立在错误的能力假设之上。

> 原文：[The Decoder](https://the-decoder.com/uks-ai-security-institute-finds-standard-benchmarks-systematically-underestimate-what-ai-agents-can-actually-do/)

## AI 助长安全漏洞报告爆发

Epoch AI 监测到，自大模型开始自主挖掘漏洞以来，严重漏洞报告数量激增。AI 模型不再被动等待人工提交，而是主动扫描代码库并生成可利用的 POC（Proof of Concept），导致安全团队的工单系统不堪重负。研究强调，漏洞报告的增加既是威胁也是机会：自动发现速度远超人工修复速度，安全社区需要从“发现后修补”转向“设计时防御”。

> 原文：[The Decoder](https://the-decoder.com/security-vulnerability-reports-have-exploded-since-ai-models-started-hunting-for-bugs/)

## 26000 名学生研究：AI 学习成本两年后才显现

一项覆盖 26,000 名学生的长期研究发现，使用 AI 辅助学习带来的负面效果——如思维惰性、基础能力退化——在两年后才会完全暴露。短期（数月）内学生成绩甚至有小幅提升，但长期追踪显示过度依赖 AI 的学生在原创性和逻辑推理上显著落后。结论：AI 教育工具需要配比“无 AI 训练”周期，否则隐性成本会被系统性忽视。

> 原文：[The Decoder](https://the-decoder.com/a-26000-student-study-shows-ais-hidden-learning-cost-takes-two-full-years-to-surface/)

## NVIDIA ASPIRE：自改进机器人框架零样本提升 77%

NVIDIA 提出 **ASPIRE** 框架，让机器人能够自动编写和优化控制程序。在 LIBERO-Pro 长期任务上，ASPIRE 实现了 31% 的零样本成功率，比基线提升 77%。关键创新在于：机器人自主生成多种控制程序并交叉验证，而非依赖手工调参。这对物流、仓储等需要快速部署机器人的场景意义重大。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/03/nvidia-ai-introduces-aspire-a-self-improving-robotics-framework-reaching-31-zero-shot-on-libero-pro-long-tasks/)

## NVIDIA HORIZON：免手动 RTL 设计 Agent

NVIDIA 提出 **HORIZON** 框架，以 Git 工作流管理 RTL（Register Transfer Level）设计，达到 100% 基准完成率。工程师只需定义端口和规格，HORIZON 即可自动生成、迭代并维护 RTL 代码，通过版本控制管理多个设计分支。该框架可减少芯片设计人力投入 60% 以上，对芯片设计工具链自动化是重要一步。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/04/nvidia-horizon-a-hands-free-agent-that-evolves-git-worktrees-and-hits-100-rtl-benchmark-completion/)

## Anthropic 发布 Claude Science Beta，多 Agent 科研

Anthropic 推出 **Claude Science Beta**，专为可重现生物信息学和化学信息学设计。它采用多 Agent 协调架构：一个 Agent 负责文献检索，一个负责实验设计，一个负责数据清洗，最后统一输出可复现的实验报告。Claude Science 对比现有 AI 科研助手，强调了“可重现性”——意味着每个中间步骤和参数都会自动记录，便于同行验证。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/07/04/anthropic-launches-claude-science-beta/)

---

当芯片快 478 倍、Agent 能力和漏洞同时爆发，我们最缺的不是更快的硬件，而是与速度匹配的衡量尺度。