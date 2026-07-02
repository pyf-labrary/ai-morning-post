# Agent工具链密集开源，基础设施定义权之争打响

今天开源社区迎来多个Agent相关工具发布，从强化学习训练框架AReaL 2.0到Vercel的Eve框架，再到Google的agents-cli和腾讯的沙箱。这些项目从不同层面降低Agent开发门槛，但技术路线碎片化明显。谁能在标准化和生态上先行占位，将是下一阶段竞争焦点。

## AReaL 2.0开源：面向自演进AI Agent的RL基础设施

小米与社区合作开源AReaL 2.0，提供一套强化学习框架，核心目标是让AI Agent能够通过自我迭代实现能力进化。框架内置了分布式训练、环境交互、奖励建模等模块，开发者无需从头搭建RL pipeline。**关键点**：相比上一版，2.0重点降低了接入成本，支持主流Agent框架（如LangChain、AutoGPT）的即插即用。**为什么重要**：当前Agent能力提升主要依赖人类反馈或静态数据，自演进能力是更长期的竞争力来源。AReaL 2.0试图将这一能力工具化，但RL本身的高样本复杂度仍是实际部署的瓶颈。

> 原文：[量子位](https://www.qbitai.com/2026/07/442134.html)

## Vercel发布开源AI Agent框架Eve

Vercel推出Eve，一个以“开发者体验优先”为设计原则的开源Agent框架。它提供声明式API来定义Agent行为，并原生集成Vercel的边缘部署能力。**关键点**：Eve支持链式调用（chain-of-thought）、工具调用（function calling）以及记忆管理，内置模板库让开发者5分钟启动一个Agent。**为什么重要**：Vercel在前端部署领域拥有大量开发者心智，Eve试图将Agent的部署和运维体验拉到和静态网站一样简单。如果生态复制Vercel的成功，Eve可能成为Agent应用部署的默认选项之一。

> 原文：[InfoQ](https://www.infoq.cn/article/kY3j5x1kIEvedufYJ1rJ)

## Google开源agents-cli：命令行创建、评估和部署Agent

Google发布agents-cli，这是一个命令行工具，可将任意编码助手（如Cursor、Codeium）转化为能操作Google Cloud服务的Agent。**关键点**：工具本身不定义Agent逻辑，而是提供统一的CLI接口来注册工具、定义评估指标（如成功率、延迟），并能直接部署到Cloud Run上。**为什么重要**：Google的策略是“标准先行”——通过开源CLI规范Agent与云服务的交互方式，与云上资源（BigQuery、GKE等）深度绑定。对于已使用GCP的团队，agents-cli是低成本的Agent化路径。

> 原文：[GitHub](https://github.com/google/agents-cli)

## 腾讯云开源CubeSandbox：为AI Agent提供轻量沙箱

腾讯云发布CubeSandbox，一个面向Agent安全运行环境的轻量沙箱。它支持即时启动、并发执行以及资源隔离，适用于Agent测试、数据隔离和多租户场景。**关键点**：沙箱内置了文件系统、网络、环境变量的细粒度控制，支持Python脚本和容器两种模式，启动时间控制在百毫秒级。**为什么重要**：Agent失控风险是行业共识，CubeSandbox相当于为Agent加了一道安全围墙。腾讯云将其开源，意在让社区共建安全标准，同时间接推广自家云原生基础设施。

> 原文：[GitHub](https://github.com/TencentCloud/CubeSandbox)

## browser-use推出video-use：用编码Agent编辑视频

开源项目video-use让编码Agent像操作浏览器一样控制视频编辑软件（如Premiere Pro、DaVinci Resolve）。**关键点**：项目基于browser-use的“视觉-动作”映射思路，将视频时间轴、滤镜、关键帧等抽象为DOM元素，Agent通过截图+指令实现剪辑、特效添加等操作。**为什么重要**：视频编辑是高频但重复的工作流，Agent自动化能极大降低人工成本。但准确率仍依赖底层视觉模型对界面的理解，对复杂特效的支持有待完善。

> 原文：[GitHub](https://github.com/browser-use/video-use)

## Strix：开源的AI渗透测试工具，自动发现应用漏洞

Strix使用AI驱动安全测试，可自动扫描Web应用、API和数据库，结合LLM分析攻击模式并生成修复建议。**关键点**：支持自定义规则和AI增强的漏洞推理，报告输出包含PoC（概念验证）代码。**为什么重要**：传统安全测试依赖专家经验，Strix试图用AI降低门槛，使开发者在CI阶段快速自查。但AI生成漏洞报告存在假阳性偏高的问题，需要人工复核。

> 原文：[GitHub](https://github.com/usestrix/strix)

## agency-agents：全功能AI代理机构，集成多种专家Agent

开源项目agency-agents打包了一套现成的Agent集合，包括前端构建Agent、Reddit运营Agent、甚至“幽默注入Agent”。**关键点**：每个Agent有独立角色和工具集，通过统一API调用，支持编排和级联。**为什么重要**：类似“Agent商店”的概念，适合快速原型验证。但Agent质量参差不齐，实际生产力可能存疑。

> 原文：[GitHub](https://github.com/msitarzewski/agency-agents)

## Facebook开源Astryx：为Agent时代设计的可定制设计系统

Meta开源Astryx，一套面向人类与代码Agent协作的UI组件库。**关键点**：包含可复用的对话面板、工作流可视化组件、Agent状态指示器等，支持React和Vue，高度可定制主题。**为什么重要**：当Agent开始承担前端交互时，UI需要同时适配人和机器。Astryx试图定义这类界面组件规范，但Agent的UI范式仍在早期，实际采纳率待观察。

> 原文：[GitHub](https://github.com/facebook/astryx)

---

今天Agent开源工具从训练、框架、沙箱、安全到UI组件全面铺开。但核心问题还未解决：这些工具彼此不兼容，开发者该如何选型？