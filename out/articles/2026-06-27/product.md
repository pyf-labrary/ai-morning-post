# Agent浪潮：Notion弃邮件，GitHub推Copilot桌面

今日最值得关注的信号：Notion正式关停其Skiff影响的邮件应用，理由是“多数用户已用AI Agent管理收件箱”，并宣布全面押注Agent。这并非孤例——GitHub同日发布Copilot桌面应用，支持并行Agent工作流。企业级AI正在从单点工具演化为自主代理，收件箱、代码编辑器这类“传统入口”正被重新定义。

## Notion关停邮件应用，全面押注AI Agent

**是什么**：Notion宣布关停受Skiff影响的邮件应用（原Skiff Mail），原因是内部数据显示多数用户已转向使用AI Agent管理收件箱。公司决定不再维护独立邮件客户端，资源将集中投入Agent方向。

**关键点**：Notion此前收购端到端加密邮件服务Skiff后，曾尝试将其整合为Notion Mail。但用户行为变化太快——AI Agent能自动分类、摘要、回复邮件，传统邮件应用的打开率持续下降。Notion认为Agent才是“收件箱”的未来形态。

**为什么重要**：这标志着一种判断：邮件客户端作为独立产品形态正在消亡。如果连Notion这种以协作空间为核心的公司都放弃自建邮件，意味着Agent将接管大量信息交互场景。对产品经理而言，这意味着“功能入口”的思维需要向“意图驱动”转变。

> 原文：[Ars Technica](https://arstechnica.com/gadgets/2026/06/notion-killing-skiff-influenced-email-app-since-most-users-use-ai-agents-instead/)

## GitHub发布Copilot桌面应用，支持并行Agent

**是什么**：GitHub推出Copilot桌面应用，核心亮点是“并行Agent”——开发者可以同时运行多个AI代理，分别处理不同子任务，如代码审查、测试生成、文档编写，最终合并结果。

**关键点**：这与当前主流的单线程Agent（一次只做一件事）模式不同。并行Agent要求更精细的任务编排和上下文隔离，GitHub通过引入“工作流拓扑”来实现。桌面应用还集成本地文件系统、终端和Git操作，让Agent直接操作开发环境。

**为什么重要**：Copilot从“代码补全”进化为“多Agent协作平台”，意味着AI编程正式进入“团队级”协作阶段。对技术领导者而言，架构设计需考虑Agent并发、资源隔离与一致性问题；对投资人，这可能是下一代IDE形态的雏形。

> 原文：[InfoQ](https://www.infoq.cn/article/GaAsWkrJQW2NFf06kgyG)

## 豆包推出专业版，定位AI工作搭子

**是什么**：字节跳动旗下豆包发布基于豆包2.1大模型的专业版，专注办公场景，强调深度写作、代码生成与推理能力，定位“AI工作搭子”而非通用聊天助手。

**关键点**：专业版与免费版区分：付费用户可获得更长上下文（128K tokens）、专属Agent技能（如写周报、做数据透视表）以及企业级数据隔离。豆包2.1模型在代码和逻辑推理多项基准上超越GPT-4o，但未公布具体评测数据。

**为什么重要**：字节跳动在办公AI领域的正式入局，意味着国内办公AI市场将进入“模型+场景”的深度竞争。Notion押注Agent，豆包押注“工作搭子”，两者殊途同归——都在试图定义人与AI在办公中的新交互范式。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/G8Tqx355YsGfzxVy.html)

## AWS推出Agent Toolkit，助力AI构建AWS应用

**是什么**：AWS发布官方Agent Toolkit，提供MCP（Model Context Protocol）服务器、预置技能和插件，让AI Agent能直接操作AWS资源（如EC2、Lambda、S3），实现自动化运维、部署和监控。

**关键点**：Toolkit包含多个MCP服务器实现，例如“AWS Cloud Control MCP Server”支持通过自然语言管理云资源。开发者可将Agent连接到自家AWS账户，构建“DevOps Agent”或“FinOps Agent”。所有组件开源在GitHub仓库。

**为什么重要**：AWS此举实质上是为Agent生态提供“云操作系统”级别的接口。当Agent能直接调用云API，传统“工具调用”将演变为“平台编排”。这会影响所有基于AWS的SaaS产品——未来Agent可能取代大部分运维脚本和手动操作面板。

> 原文：[GitHub](https://github.com/aws/agent-toolkit-for-aws)

## 大晓机器狗在上海7×24小时自主巡逻

**是什么**：大晓机器人旗下晓途机器狗进驻上海西岸片区，实现全天候无人自主巡逻执勤。该机器狗搭载多模态感知与自主导航系统，可完成安防巡检、异常告警等任务，进入商业运营。

**关键点**：这是国内首个“机器狗+园区治安”的常态化运营案例。机器狗无需充电站轮换，通过自主回桩补电实现连续7×24小时续航。大晓表示，已经与多家物业、园区签约，2026年目标部署超2000台。

**为什么重要**：机器狗从演示走向商业闭环。相比轮式机器人，四足形态更适合复杂地形（台阶、草地）。对产品经理而言，这类“硬件+AI Agent”的结合体正在定义物理世界的新服务入口——未来“机器人巡逻”可能像监控摄像头一样普及。

> 原文：[雷锋网](https://www.leiphone.com/category/ai/8So3cLimLEfWaVm4.html)

## RoboScience发布通用具身大模型Visics

**是什么**：RoboScience机器科学发布通用具身大模型Visics，首次展示VLOA（Vision-Language-Object-Action）双引擎架构。该模型将视觉、语言、对象识别和动作规划统一到一个框架中，使机器人能理解并执行复杂物理任务。

**关键点**：VLOA双引擎指一个“理解引擎”（VLM，视觉语言模型）和一个“执行引擎”（动作策略网络）。机器人通过理解引擎解析指令与环境，再由执行引擎生成精细操作。RoboScience声称Visics在桌面级操作（抓取、组装、放置）上成功率超85%。

**为什么重要**：具身智能是AI的下一个前沿。Visics的“双引擎”设计解决了大模型在物理世界落地时的“认知-行动”割裂问题。这对机器人行业意味着：通用操作能力可能不再需要针对每个任务单独编程，而由模型直接驱动。

> 原文：[雷锋网](https://www.leiphone.com/category/robot/Kwpq9tYiIohzAJ7f.html)

## Google Finance终于推出Android应用

**是什么**：谷歌在20年后终于推出Google Finance Android应用，并融入了AI功能。该应用提供实时行情、新闻摘要、组合跟踪，承诺后续推出iOS版本。

**关键点**：新应用内置“AI解读”功能——用户点击任意股票可获取由大模型生成的当日走势总结、关键事件分析。谷歌还整合了搜索趋势数据，显示个股的搜索热度变化。该应用目前在美国率先上线。

**为什么重要**：Google Finance作为老牌桌面产品，在移动时代长期缺位。此次推出虽然迟到，但以AI功能为差异化，意图挑战Yahoo Finance、Robinhood等竞品。对投资者而言，这是一个值得关注的新入口，但尚需观察用户留存——毕竟20年的等待早已让用户习惯了替代品。

> 原文：[Ars Technica](https://arstechnica.com/google/2026/06/google-finance-finally-gets-a-mobile-app-as-ai-powered-overhaul-leaves-beta/)

## MOVA割草机器人出货突破50万台

**是什么**：MOVA智能割草机器人累计出货量超过50万台，增速全球登顶，并获2026红点设计大奖，巩固其在高端市场（均价$1500+）的地位。

**关键点**：MOVA采用RTK+视觉融合导航，无需预埋边界线。其核心竞品是Segway的割草机器人。MOVA声称其用户复购推荐率（NPS）为行业最高（未公布具体数值），且已覆盖北美、欧洲、日本市场。

**为什么重要**：50万台对割草机器人来说是一个里程碑——说明高端消费级机器人正在从“尝鲜品”变成“刚需产品”。对产品经理而言，这意味着家庭服务机器人需要同时在硬件可靠性、软件智能化（路径规划、避障）和设计美学上竞争，MOVA的红点奖恰恰证明了后者的重要性。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/2J73t9lAS4yr7Gnw.html)

---

今天的8条新闻，都在指向同一个问题：当AI Agent开始接管数字世界的入口（邮件、代码、云管理）和物理世界的任务（巡逻、割草、操作物体），你准备好重新设计自己的产品交互了吗？