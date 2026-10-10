# 企业级 Agent 底座开始拥挤

## 导语

今天开源板块最值得看的不是某个工具本身，而是「Agent 基础设施」这条赛道一天内挤进了三个玩家：openJiuwen 开源企业级 AgentOS，微软发布跨 Python/.NET 的 agent-framework，Anthropic 则从安全扫描和岗位插件两侧包抄。同一时间，Windows-MCP 和 claude-mem 在补 Agent 的手和记忆。工具层正在快速标准化，真正的差异化会转移到数据、权限与运维上。

## openJiuwen 开源企业级 AgentOS

国产团队 openJiuwen 发布并开源了面向企业的 Agent 操作系统，核心卖点是多 Agent 协同与「自我进化」，目标是把 Agent 从 demo 推向企业规模化部署。所谓 AgentOS，本质上是把模型调用、工具编排、状态管理、权限与观测收敛成一层运行时，让企业不必自己拼装框架。这个方向并不新鲜，但开源的企业级实现仍然稀缺——大多数方案要么停在 SDK 层面，要么绑定单一云厂商。值得关注的是「自进化」如何被工程化：如果指的是基于运行反馈自动调整 prompt 或工具选择，它带来的可观测性和回滚需求会远超普通框架。对企业而言，选型时应先看治理能力，而不是 demo 效果。

> 原文：[量子位](https://www.qbitai.com/2026/10/502106.html)

## Anthropic 免费开源项目 AI 安全扫描器

Anthropic 推出了一款面向开源项目的免费 AI 安全扫描工具，帮助维护者发现代码中的漏洞。开源维护者长期处于「无预算、有责任」的状态，安全审计工具的商业化产品对个人项目基本不可及，免费扫描器切中的正是这个缺口。这一动作也有战略意味：让安全能力成为模型厂商与开源社区之间的接口，既积累代码语料与漏洞样本，也绑定开发者心智。实际价值取决于两点——误报率能否压住，以及是否支持主流语言与 CI 集成。若两者成立，它会成为很多仓库的第一道门禁。

> 原文：[The Decoder](https://the-decoder.com/anthropic-launches-a-free-ai-scanner-for-open-source-projects/)

## Anthropic 开源 Claude 岗位插件库

Anthropic 在 GitHub 开源了 knowledge-work-plugins，思路是把 Claude 从通用助手改造成特定岗位、团队乃至具体公司的专家。插件库的意义不在代码量，而在它示范了一种知识组织方式：把岗位 SOP、内部术语、常用流程封成可复用的包，而不是每次靠长 prompt 临时拼。对企业来说，这可能是比「自建 Agent 平台」更轻的落地路径——先固化知识，再谈自动化。风险也明显：插件与内部系统对接后，权限边界和数据外泄面会迅速扩大，需要配套的审计机制。

> 原文：[GitHub](https://github.com/anthropics/knowledge-work-plugins)

## 微软开源 agent-framework

微软发布 agent-framework，同时支持 Python 与 .NET，用于构建、编排和部署 AI Agent 及多 Agent 工作流。双语言支持是它最实际的区别点：.NET 在企业后端占比很高，而此前主流 Agent 框架几乎清一色 Python，导致 .NET 团队要么跨栈、要么放弃。微软把框架开源，也是在为 Azure 上的 Agent 部署铺路。需要观察的是它与其他微软 Agent 组件（如 Semantic Kernel 生态）的边界——框架层重复建设对开发者是负担，收敛速度会决定采用率。

> 原文：[GitHub](https://github.com/microsoft/agent-framework)

## Windows-MCP：让 Agent 操作 Windows 桌面

CursorTouch 开源 Windows-MCP，为 computer-use 类 Agent 提供 Windows 环境下的 MCP 服务端。MCP（Model Context Protocol）正在成为 Agent 调用外部能力的通用接口，但在桌面自动化这块，此前主要围绕 macOS 和浏览器展开，Windows 的空白对企业场景尤其刺眼——大量内网系统、老旧客户端只存在于 Windows 桌面上。把桌面操作抽象成 MCP 工具，意味着 Agent 不必依赖私有 API 就能接管流程。随之而来的是安全与合规问题：谁能授权 Agent 点击、输入、读取屏幕，需要明确的策略层。

> 原文：[GitHub](https://github.com/CursorTouch/Windows-MCP)

## Whistle：16.9MB 的本地语音转文字

Cactus Compute 发布 Whistle，一套仅 16.9MB 的语音转文字方案，主打极小体积下的本地推理。这个体量意味着它可以被塞进移动端或边缘设备，不依赖网络、不上传音频，对隐私敏感场景和离线环境都是直接解法。语音转文字本身已不稀奇，稀缺的是「足够小且够用」的工程实现。需要验证的是它在口音、噪声、专业术语上的准确率代价——如果只在安静环境可用，适用面会大幅收窄。

> 原文：[Cactus Compute](https://cactuscompute.com/blog/whistle)

## Saluki 27B：2-bit 量化在工具调用上反超原模型

Underdog Saluki 27B 是 Qwen3.8-27B 的 2-bit GGUF 版本，体积仅 7.89GB，却在工具调用上超过了 54GB 的原模型，但数学与推理能力有所让步。这个结果值得细看：工具调用更依赖格式遵循与结构化输出，量化损失对这类任务相对宽容，而对多步推理的伤害则更直接。它提示了一个实用结论——如果业务主要是「模型选工具、填参数」，小量化模型可能已经够用，本地部署成本能降一个数量级。但不要把单点跑分外推到通用能力，选型时仍要按任务分档测试。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/10/09/meet-the-underdog-saluki-27b-a-2-bit-qwen3-8-27b-that-beats-the-original-at-tool-calling/)

## claude-mem：给 Agent 加跨会话持久记忆

claude-mem 开源了一套跨会话记忆方案，记录并压缩 Agent 每次会话的行为，再把相关上下文注入后续会话，兼容 Claude Code、Codex、Gemini 等。记忆是当前 Agent 最明显的短板：每次开新会话都从零开始，用户反复交代背景，团队经验也无法沉淀。claude-mem 的思路是「记录—压缩—检索」，难点在压缩策略与检索精度——记太多会污染上下文，记太少等于没记。它同时暴露了一个更根本的问题：记忆该属于工具、属于模型，还是属于组织？眼下的答案还是各自为政。

> 原文：[GitHub](https://github.com/thedotmack/claude-mem)

## 结语

Agent 的手（MCP）、记忆（claude-mem）和底座（AgentOS、agent-framework）今天同时被开源补位，真正没被解决的仍是权限与责任归属——当 Agent 替你点下那个按钮，出错时算谁的？