# 千万小时视频开源，AI 视频燃料加码

今天开源圈最值得看的，是 LAION 放出 1000 万小时视频数据集，规模直接拉高了一个量级。数据一直是视频模型的隐形军备竞赛，这个量级的公开素材能实质降低研究门槛，但清洗、版权和算力消耗也成了新的选择题。与此同时，DuckDB 2.0 官宣要分布式，本地球的数据基础设施也在换挡。

## LAION 发布 1000 万小时开放视频数据集

是什么：LAION 推出大规模开放视频数据集，包含 1000 万小时素材，供 AI 研究使用。1000 万小时折合约 1141 年连续播放，对视频模型预训练来说，这是开源领域此前少见的体量。

关键点：数据集面向 AI 研究开放；视频模态对数据的需求远高于文本，时长规模直接决定模型的泛化能力。

为什么重要：视频模型的发展长期受私有数据掣肘，公开数据集的到来能让更多团队进入视频生成与理解的研究。但大体积数据集也意味着下载、清洗与合规的成本，如何使用比「有没有」更考验资源。

> 原文：[the-decoder](https://the-decoder.com/laion-drops-massive-open-video-dataset-with-10-million-hours-of-footage-for-ai-research/)

## DuckDB 2.0 预览：从嵌入式走向分布式

是什么：DuckDB 发布 2.0 预览版，架构从嵌入式数据库向分布式演进。

关键点：DuckDB 过去以进程内、无服务器的分析查询见长，是本地数据科学家和产品集成的常用选择；分布式意味着它开始向「可以横向扩展的查询引擎」方向走。

为什么重要：如果 2.0 落地，使用方式会从「嵌在应用里的库」变成「需要部署、管理的系统」。对现有用户来说，升级路径和兼容性需要提前评估。

> 原文：[InfoQ 中文](https://www.infoq.cn/article/9YLW3ZxLvrqxOVzSh9Y1?utm_source=rss&utm_medium=article)

## Hugging Face 开源 399 美元双足机器人 Microduck

是什么：Pollen Robotics 与 Hugging Face 联合发布 Microduck，一台 25cm 高的开源双足机器人，售价 399 美元，所有动作由 MuJoCo 训练的神经网络策略驱动。

关键点：开源硬件加仿真训练（MuJoCo）是这套方案的核心——本体便宜，控制策略可以从仿真迁移到实际硬件上复现。

为什么重要：双足机器人的研发成本一向不低，Microduck 把可复现的硬件加 AI 控制方案拉到了几百美元级别，这让高校和独立开发者在真实硬件上做机器人学习实验成为可能。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/08/28/pollen-robotics-hugging-face-microduck-399-open-source-rl-biped-robot/)

## HTTPX2 发布，OpenAI Python SDK 已迁移

是什么：新一代 Python HTTP 客户端 HTTPX2 正式发布，OpenAI 的 Python SDK 已同步迁移到该库。

关键点：HTTPX 是 Python 生态里主流的异步 HTTP 客户端之一，v2 是一次大版本升级。OpenAI SDK 在发布节点上完成迁移，这个时间点的选择本身就是一种背书。

为什么重要：对 Python 开发者来说，HTTPX2 的升级路径、异步能力和性能变化，会直接影响到依赖它的工具链。底层客户端的稳定性，正在成为 API 产品体验的一部分。

> 原文：[pydantic/httpx2](https://github.com/pydantic/httpx2)

## Anthropic 官方发布 Claude Code 插件目录

是什么：Anthropic 推出由官方管理的 Claude Code 插件目录，收纳经过筛选的插件。

关键点：官方目录的价值在于信任与分发——插件不再只靠社区口口相传，而是有一个被审查和维护的入口，能降低使用者的选择成本。

为什么重要：Claude Code 正在成为 agent 工作流的重要入口，插件的生态质量决定它的边界。官方目录的建立，意味着 Anthropic 开始把插件生态当作产品能力的一部分来运营。

> 原文：[GitHub](https://github.com/anthropics/claude-plugins-official)

## Vercel 开源 WebGPU 库 vgpu

是什么：Vercel 开源其 WebGPU 库 vgpu，支持把 .wgsl 文件作为可导入的 TypeScript 模块，并能在浏览器和 Node.js 中运行。

关键点：wgsl 是 WebGPU 的着色器语言，此前在 JS/TS 工程里的处理方式比较绕；vgpu 让着色器可以像模块一样被导入、类型化和复用。

为什么重要：WebGPU 正在成为浏览器里做计算和渲染的底层接口，但工具链一直不够顺手。Vercel 开源这套库，可能让更多前端和 AI 应用团队愿意在 Web 端尝试 GPU 加速。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/08/28/vercel-vgpu-webgpu-library-open-source/)

## 20ms 将 PDF 变 Markdown，开源 OCR 快约 300 倍

是什么：一个名为 20ms 的开源 OCR 工具，官方声称 3 秒可处理 200 份 PDF，速度约为现有方案的 300 倍，输出格式是 Markdown。

关键点：PDF 转 Markdown 是 RAG、文档智能和数据管线的常见预处理步骤，速度提升直接转化为管线成本和延迟的下降。

为什么重要：解析速度一直是文档处理链路的隐性瓶颈。如果「20ms」的表现在真实场景中稳定成立，它在知识库构建和高吞吐文档场景里会很有吸引力。不过目前数据来自官方声称，需要独立验证。

> 原文：[量子位](https://www.qbitai.com/2026/08/481075.html)

## 开源项目 OpenClaw 红过爱过散了

是什么：开源项目 OpenClaw 走向终结，社区关注点转移到 Harness。

关键点：开源项目终结本身不罕见，真正值得留意的是社区注意力的去向——Harness 正在承接原本属于 OpenClaw 的关注。

为什么重要：这个转移暗示同类需求依然存在，只是实现方式或维护节奏需要更新。对使用者来说，迁移到新项目时要更仔细地评估路线图和维护活性，而不是只看功能列表。

> 原文：[量子位](https://www.qbitai.com/2026/08/480855.html)

今天的开源动静都不小：有数据，有引擎，有机器人，也有离场的故事。留下的问题是：当开源把门槛一项项拆掉，真正稀缺的是应用层还是基础设施层的判断力。