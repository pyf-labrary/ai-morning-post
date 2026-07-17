# Kimi K3发布：2.8T开源逼近GPT-5.6

今天模型发布板块最值得关注的是Moonshot AI的Kimi K3——2.8万亿参数开源MoE，性能逼近GPT-5.6和Opus 4.8，定价却低于Sonnet 5。这不仅是国产开源模型参数量的新纪录，更意味着一线闭源模型的价格壁垒正在被开源方案打破。与此同时，Mira Murati的新公司也交出了首份作业，但表现并未超越中国团队。

## Kimi K3：2.8T参数开源MoE，性能比肩顶尖闭源

Moonshot AI 发布 Kimi K3，一个 2.8 万亿参数的 MoE 开源模型。在官方公布的基准测试中，其综合性能接近 GPT-5.6 和 Opus 4.8，但 API 定价低于 Sonnet 5。Kimi K3 采用混合专家架构（MoE），在保持高容量的同时控制推理成本。此次开源意味着任何团队都可以在本地部署或微调这一级别的模型，可能加速国产大模型在 B 端应用的渗透。

> 原文：https://www.kimi.com/blog/kimi-k3

## Inkling 发布：前OpenAI CTO首款模型，落后于中国团队

Thinking Machines Lab 由前 OpenAI CTO Mira Murati 创办，今日发布首款开源模型 Inkling（975B 参数、MoE 架构）。模型在多项国际基准上领先美国其他实验室（如 Mistral、Meta 的 Llama 系列），但在与国内模型（如 Kimi K3 等）对比时处于劣势。Inkling 的最大意义在于验证了“明星研究团队独立创业”的模式仍能快速产出高水平成果，但“追赶中国”已经成为海外新品发布时的常态。

> 原文：https://thinkingmachines.ai/news/introducing-inkling/

## Nemotron 3 Embed：NVIDIA登顶检索排行榜

NVIDIA 发布 Nemotron 3 Embed 模型，在检索基准 RTEB（Retrieval Task Evaluation Benchmark）上排名第一。该模型专注于提升智能体（agentic）应用中的检索能力，例如 RAG 场景下的段落召回和工具选择。NVIDIA 延续了“基础模型+垂直优化”的策略，在嵌入模型这一细分赛道上卡住了又一个关键入口。

> 原文：https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb

## Mobius：上海AI Lab推出非Transformer科学基座模型

上海人工智能实验室在 WAIC 2026 上发布 Mobius，一个 397B 参数的科学智能体基座模型，采用非 Transformer 架构，专注于化学、物理、生物等科学领域的任务求解。其核心设计围绕“符号推理+数值模拟”展开，与传统的大语言模型在结构上根本不同。如果 Mobius 能在特定基准上超越 Transformer 变体，可能开启一条通往科学专用模型的新路线。

> 原文：https://www.qbitai.com/2026/07/452942.html

## WITT：文远知行发布物理AI大模型，专注自动驾驶数据闭环

文远知行在 WAIC 发布物理 AI 大模型 WITT，宣称单卡每天可处理 1 万分钟视频，将行驶数据高效转化为模型能力。WITT 本质上是一个针对自动驾驶的感知-预测-规划联合训练框架，而非通用对话模型。对于 L4 量产玩家来说，数据闭环的效率直接决定迭代速度，WITT 试图用大模型压缩传统多模型 pipeline。

> 原文：https://www.qbitai.com/2026/07/452961.html

## Gemma 4静默更新：Google在不换版本号下修复工程问题

Google 在不更改版本号的情况下更新了 Gemma 4 模型，修复了工具调用（tool calling）中的 bug 以及部分场景下的响应截断问题。这类“静默更新”在开源模型领域并不罕见，但 Google 未做任何公告，只在模型卡中注明变更。对开发者而言，模型版本号无法唯一标识行为，意味着生产依赖需要更严谨的校验机制。

> 原文：https://the-decoder.com/gemma-4-gets-a-stealth-update-that-fixes-tool-calling-bugs-and-truncated-responses-under-the-same-name/

当2.8T参数开源模型开始与最贵闭源掰手腕，模型发布的核心变量正在从“谁更强”转向“谁更便宜、更好用”。你会在自己的应用里换掉GPT-5.6去跑Kimi K3吗？