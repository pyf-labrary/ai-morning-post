# 开源 Agent 开始卷 Token 成本

今天开源板块最值得看的是「降本」这条线。AWS Strands 团队开源通用 Agent Harness，在准确率相当的前提下把 Token 成本降低约 28%；NVIDIA 的 SoL-Pi 则用 AI 在 535 个环境中自动搜出 4 个 harness 机制，把编码 Agent 的 Token 流量最多削减 49%。两条工作彼此独立，却指向同一件事：agent 走进生产之后，竞争焦点正从「能不能跑通」转向「单任务成本」。其余几条补的是另外两块拼图——交互界面，和能动手的身体。

## NVIDIA 发布 Isaac ROS 5.0

NVIDIA 推出 Isaac ROS 5.0，面向具身智能（embodied AI）与 agentic 机器人开发，提供新的物理 AI 模型与工具链，并延续开源路线。

关键点在于覆盖面。Isaac ROS 是建在 ROS 2 之上的加速层，5.0 把物理 AI 模型和工具链一并给出，目标人群从传统机器人工程师，扩展到做 agent 的软件团队。

为什么重要：机器人大概是 agent 落地链条里最难的一环——感知、仿真、控制、硬件彼此耦合，缺一环都跑不起来。NVIDIA 用开源把这几层标准化，短期降低了准入门槛，长期是把开发者留在自己的算力与仿真栈里。对做具身智能的团队，这基本是一套绕不开的基线。

> 原文：[NVIDIA Blog](https://blogs.nvidia.com/blog/isaac-ros-5-0-agentic-open-source-robotics/)

## AWS 开源通用 Agent Harness

AWS Strands Agents 团队开源了通用 Agent Harness，在准确率相当的前提下把 Token 成本降低约 28%。

所谓 Harness，指的是包在模型外面那一圈：循环控制、工具调用、上下文拼装与裁剪、失败重试。这块过去每个团队各写各的，质量参差，而它直接决定账单厚度。

为什么重要：agent 落地的真实瓶颈往往不在模型能力，而在这一层的工程量。AWS 把它开源，相当于把「自研 agent loop」的默认答案摆上桌——先用现成的跑通，再谈改造。对正在评估自建还是采购的团队，这是一个成本极低的对照基准，也是今天降本主线里最可直接复用的一条。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/09/21/aws-strands-agents-team-releases-strands-harness/)

## Meta 开源 Astryx：给 Agent 做界面

Meta 开源 Astryx，一套专为 Agent 场景设计的 React 设计系统，帮助开发者快速构建智能体交互界面。

关键点在「为 Agent 场景设计」这个限定。对话式 UI 的组件库早已泛滥，但 agent 的交互形态还没定型：一次任务里的多步过程、工具调用的结果、用户中途干预，都缺少共识性的呈现方式。

为什么重要：设计系统是典型的基础设施型开源，用的人越多，交互范式越收敛。Meta 在这一层出手，抢的不是模型能力，而是开发者的默认选择。对做 agent 前端的产品团队来说，值得先看一眼再决定要不要自己造轮子。

> 原文：[InfoQ](https://www.infoq.cn/article/He6bUhlNIuPEa99GGRYC?utm_source=rss&utm_medium=article)

## SoL-Pi：让 AI 去调优编程 Agent

NVIDIA 研究者发布 SoL-Pi，其 4 个 harness 机制由 AI 在 535 个环境中自动搜索得出，可将 Pi 编码 Agent 的 Token 流量削减最多 49%。

关键点在「自动搜索」。以往这类优化靠人肉试 prompt、试上下文策略；SoL-Pi 把 harness 的策略空间交给搜索过程，用环境反馈来筛选。

为什么重要：和上面 AWS 那条放在一起看，信号就很清楚了——harness 层本身已经成为可优化、且可被自动优化的对象。模型能力趋同时，谁的循环设计更省 token、更少绕路，谁的单位成本就更低。做编码 agent 的团队，49% 这个数字值得动手复现。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/09/21/nvidia-researchers-have-released-sol-pi/)

## Anthropic 开源金融业参考 Agent

Anthropic 在 GitHub 开源了一套面向金融服务业的参考 Agent、技能（skills）与数据连接器，覆盖投行、股票研究、私募与财富管理。

关键点是「参考实现 + 连接器」的组合。参考 Agent 给出工作流骨架，skills 定义可复用的能力单元，连接器负责接上行业数据源——这三件恰好是垂直 agent 落地时最耗时的部分。

为什么重要：金融是付费意愿最强、同时对准确性与可审计性要求最高的行业之一。把这一层模板开源，Anthropic 走的是「让行业先跑起来」的路径，和卖 API 并不冲突——跑起来的每一步都在消耗 token。对其他垂直行业，这套结构本身比代码更值得抄。

> 原文：[GitHub](https://github.com/anthropics/financial-services)

## browser-use：让 Agent 直接操作浏览器

browser-use 提供让 Agent 真正操作浏览器的开源方案，持续位居 GitHub 趋势榜。

关键点在定位的克制：它不做模型，也不做具体业务流程，只解决「把网页变成 agent 可操作的界面」这一件事。没有 API 的系统，浏览器就是最后的通用接口。

为什么重要：agent 落地最常见的死结不是推理不行，而是系统之间没有接口。浏览器操作绕开了对接成本，代价是速度与稳定性。这条路线能否撑起生产级负载尚无定论，但持续挂在趋势榜上说明需求侧缺口真实存在——它是 agent 的「手」里最通用的一只。

> 原文：[GitHub](https://github.com/browser-use/browser-use)

## Transformers 可直接加载 llama.cpp 量化模型

Hugging Face 的 Transformers 新增对 llama.cpp 量化格式的支持，量化权重可以直接在 Transformers 中加载运行。

关键点是打通两套此前割裂的工具链。llama.cpp 的量化格式在本地推理生态里是事实标准，但它和 Transformers 的训练、微调、评测流程长期各走各的，想在两边搬权重，往往要转换、对齐，甚至重做一遍。

为什么重要：这不是性能新闻，是工程效率新闻。同一份量化权重既能本地推理，又能进现有 Python 流程，省掉的是每个团队都要重复一次的那几天。对做端侧或私有化部署的团队，属于立即可兑现的收益。

> 原文：[Hugging Face](https://huggingface.co/blog/transformers-llama-cpp-quants)

## cua：computer-use 的驱动与基准

trycua/cua 提供跨操作系统 fleet、开源驱动与训练评测基准，目标是支撑规模化的 computer-use 2.0。

关键点是三件套的组合方式：驱动让 agent 真的去操作机器，fleet 把一批机器管起来，基准负责衡量做得好不好。单看每一件都不新鲜，但打包成一套开源栈的项目不多。

为什么重要：computer-use 当前最大的问题之一是缺少公认评测口径，各家报的数字彼此不可比。有人把驱动和基准一起开源，这个方向才有可能从演示走向可对比的工程。它和 browser-use 一样在补 agent 的手，差别在于它管的是整片机器。

> 原文：[GitHub](https://github.com/trycua/cua)

今天最密集的动作集中在 harness 与操作层，也就是模型之外的那一圈。模型能力还在涨，但决定 agent 能否规模化上线的，越来越是这些不太性感的部分——不妨问一句：你们团队的 token 账单里，有多少花在了循环设计上？