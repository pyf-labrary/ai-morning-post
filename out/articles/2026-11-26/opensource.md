# 一百行的 agent 打到了 74%

今天开源板块最值得看的一条，是 mini-swe-agent：约 100 行代码，在 SWE-bench Verified 上超过 74%，没有巨型 monorepo，也没有层层配置。它和同日的 Laminar 恰好构成一组对照——一个在应用侧证明「脚手架可以极简」，一个在训练侧把 rollout、训练与权重同步拆开，用工程解耦换来吞吐。这两件事共同指向一个判断：agent 的竞争正在从「谁封装的抽象更多」转向「谁砍掉的耦合更多」。对做基础设施的团队来说，这是一个值得重估自家技术栈复杂度的信号。

## 字节 Seed 与港大开源 Laminar：把异步 RL 拆成三段

港大与字节 Seed 开源了 Laminar，一个面向 RL 后训练（post-training）的异步框架。它的核心动作是把三件事解耦：rollout（采样）、训练、以及权重同步。在同步式流水线里，三者互为等待，长尾样本会拖住整批更新；拆开之后，采样与训练可以并行推进，权重同步则成为一个独立的工程问题。

效果上，团队把 Qwen3-Coder-30B-A3B 在 SWE-bench Verified 上推到 52.2%。

为什么重要：代码类 agent 的 RL 后训练，瓶颈往往不在算法而在吞吐与稳定性。Laminar 的价值不在于提出新目标函数，而在于给出一个可复用的工程切分方式——尤其是「权重同步」被单独拎出来当作一等公民，说明这套框架是奔着大规模跑得动去的。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/24/bytedance-seed-laminar-async-rl-post-training-framework/)

## mini-swe-agent：约 100 行代码，SWE-bench 超 74%

SWE-agent 团队放出的 mini-swe-agent，用大约 100 行代码完成「读 issue、改代码、跑测试」的闭环，在 SWE-bench Verified 上通过率超过 74%。它刻意去掉了两样东西：庞大的配置文件体系，以及巨型 monorepo 式的工程结构。

关键点在于取舍。它没有自建复杂的工具调用协议、没有多层抽象，而是把 agent 循环压到最小可运行形态，让基础模型自身的能力承担主要工作。

为什么重要：这是一次针对「agent 工程复杂度」的反证。过去一年大量项目靠堆脚手架提升分数，而 mini-swe-agent 说明，当基座模型足够强时，脚手架的正确方向可能是减重而非加层——它同时也是一份极好的教学样本，能让人看清 agent 循环里到底哪几行是必要的。

> 原文：[GitHub: SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent)

## CLI-Anything：把现有软件变成 agent 的原生接口

HKUDS 推出 CLI-Anything，目标不是再做一个 agent，而是给 agent 补上一层「手」：把现有软件统一封装成 agent 可直接调用的命令行接口，并配套 CLI-Hub 做分发。

关键点在于路径选择。CLI 是软件世界最稳定、最古老的接口形态，几乎每个工具都有；相比为每个应用单独写适配层，统一封装成 CLI 意味着 agent 可以复用几十年的工具生态。CLI-Hub 则承担「去哪儿找这些封装」的问题。

为什么重要：agent 落地的一大阻力不是推理能力，而是「操作不了真实软件」。这条路与 MCP（Model Context Protocol）式的协议接入形成互补——一个管能力发现与调用约定，一个管把存量软件批量接进来。真正的考验在于封装的覆盖面与稳定性，而不是概念本身。

> 原文：[GitHub: HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

## Together AI 开源 Hurdle：给自家 API 跑 agent 评测

Hurdle 是 Together AI 开源的一个 npm 库，用来评测 agent 在「你的 API、技能与文档」上的表现。做法是让 Claude Code 与 Codex 去跑真实任务，再用三重手段打分：代码检查、guard（护栏校验）以及 LLM 评审。

关键点在于评测对象的转变——不是评模型在通用榜单上的分数，而是评模型在你自己的 API 和文档上能不能把事办成。对提供 API 的团队来说，这直接对应一个具体问题：文档写得够不够 agent 读懂。

为什么重要：随着编码 agent 成为 API 的主要「读者」之一，文档质量开始具备可测量的商业含义。Hurdle 把这件事变成了可重复的跑分，也让「换模型」这个决策第一次有了自家场景下的对照数据。

> 原文：[Together AI Blog](https://www.together.ai/blog/introducing-hurdle-run-agent-evals-on-your-api-skills-and-docs)

## superpowers：把编码 agent 的开发方法论做成可组合 skills

superpowers 这个仓库做的事，是把一组可组合的 skills 组织成完整的软件开发方法论，让编码 agent 的工作流程可复用、可约束。

关键点在于「方法论」被当作代码资产来管理。单个 skill 只是能力片段，真正的难点是流程编排：什么时候该调研、什么时候该写测试、什么时候该收敛。仓库试图用可组合的方式把这些阶段固化下来。

为什么重要：这代表了一类正在成型的实践——agent 的能力上限，越来越取决于流程约束而非提示词技巧。它也带来了新的问题：方法论一旦被固化成 skills，迁移成本和锁定风险由谁承担。对团队而言，值得先当作参考读物，再决定是否照搬。

> 原文：[GitHub: obra/superpowers](https://github.com/obra/superpowers)

## FreeVideo：8GB 显存本地跑 MiniMax H3 生成视频

FreeVideo 把视频生成拉到消费级硬件：最低 8GB 显存加 16GB 内存，就能在普通电脑上本地跑 MiniMax H3，并会按硬件情况自动选择加速路径。

关键点在于「自动选路」。不同显卡、不同内存条件下，可用的加速方案并不一样，这个项目把适配逻辑收进了工具里，降低了下限用户的门槛。

为什么重要：视频生成的讨论长期集中在大厂集群和云端 API，本地可跑意味着成本结构和隐私边界都变了——试错不再按次计费，素材也不必出本机。当然，8GB 显存能跑的是否等于能用于生产，是另一个问题；但门槛每降一档，创作者侧的实验密度就会上一个台阶。

> 原文：[GitHub: FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo)

## minimind：两小时从零训出一个 64M 小模型

minimind 是一个教学向项目，把「从零训练一个小语言模型」的完整流程压缩到两小时，产出一个 64M 规模的模型。

关键点在于完整性。它覆盖的是预训练全链路——数据准备、模型结构、训练循环、评估——而不是只给一段训练脚本。对没跑过预训练的人来说，这条链路本身就是知识。

为什么重要：在大模型语境里，「训过模型」和「调用过模型」是两种不同层次的直觉。两小时的上手成本，让后者向前者迁移变得现实。它不产出可用的产品，但能显著改善工程师对 loss 曲线、数据质量和规模律的体感，这类体感在评审技术方案时往往比文档更管用。

> 原文：[GitHub: jingyaogong/minimind](https://github.com/jingyaogong/minimind)

## Cursor 开放插件规范，并开源官方插件集

Cursor 发布插件规范，同时开源了官方插件集，覆盖主流开发工具、框架与 SaaS 产品。

关键点在于从产品走向平台。规范定义了「插件如何被 Cursor 调用」，官方插件集则给出参考实现——两者一起，等于把第三方接入的说明书和样例代码同时交出去。

为什么重要：编辑器正在成为 agent 的分发入口，谁定义插件规范，谁就在事实上定义 agent 与工具生态的握手方式。对 SaaS 厂商来说，这可能很快变成一份「要不要支持」的清单问题；而对 Cursor 自身，生态广度将是它与通用编码 agent 拉开差距的关键变量。

> 原文：[GitHub: cursor/plugins](https://github.com/cursor/plugins)

## 结语

今天这八条里，最反直觉的是：把 agent 做得更强的那批人，正在删代码、拆耦合、砍配置。留一个问题——如果你现在重写手里的 agent 项目，第一刀会砍在哪里？