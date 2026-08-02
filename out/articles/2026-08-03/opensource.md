# Karpathy 开源 AI 研究员，科研也要自动跑了

今天的开源板块异常热闹：最值得看的不是哪个框架升级，而是 Karpathy 放出的 autoresearch——让 Agent 在单 GPU 上自动跑训练、自己迭代实验。它把「自动化科研」从概念变成了可复现的开源项目。与此同时，字节、NVIDIA、微软、Hugging Face 集体开源 Agent 基础设施，方向高度一致：Agent 正在从对话工具走向定义工作流的基础设施。

## Karpathy 开源 autoresearch：AI 自动做科研

Karpathy 的新项目展示了科研自动化的具体形态：AI Agent 在单 GPU 上自动运行 nanochat 的训练流程，并根据实验结果迭代研究方案。这不是简单的 AutoML，而是把「研究」本身当作一个可循环执行的工作流。

关键点在于：整个研究循环被显式地编码为 Agent 的思考、执行、观察过程，实验设计、训练、评估、总结每一个环节都成为 Agent 可调用的工具。单 GPU 的设定也降低了复现门槛。

这件事的重要性在于信号意义——当 Karpathy 亲自下场做「AI 研究员」，科研自动化就不再是边缘实验，而可能成为机器学习社区的新工作范式。它挑战的是「科研只能靠人」的默认假设。

> 原文：[https://github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)

## GitHub 发布多平台 Copilot SDK

GitHub 正式开放 Copilot Agent 的 SDK，开发者可以把 Copilot 的核心能力嵌入自己的应用和服务。这是 Copilot 生态从编辑器内走向全场景的关键一步。

SDK 的意义在于它提供了标准化的 API 层，让 Copilot 不再只是 GitHub 平台上的一个功能，而变成了可以被任何团队调用的 agentic 基础设施。多平台支持意味着桌面、Web、移动端都可以接入。

对于开发者来说，这意味着基于 Copilot 的二开成本大幅降低；对 GitHub 来说，这是在 AI 编程赛道建立生态壁垒的重要动作。Copilot 的竞争正在从模型能力转向平台覆盖度。

> 原文：[https://github.com/github/copilot-sdk](https://github.com/github/copilot-sdk)

## NVIDIA 开源 Molt：PyTorch 原生 Agentic RL

NVIDIA 开源了 Molt，一个约 8600 行的 PyTorch 原生 Agentic RL 框架。目标很直接：降低 Agent 强化学习研究的迭代成本。

当前 Agentic RL 研究的痛点在于框架繁琐，研究人员大量时间花在调试分布式训练代码而非算法本身。Molt 用极少代码量实现核心功能，试图把研究者从工程泥潭中解放出来。

这件事值得关注，因为它代表硬件厂商开始下场解决 agentic 训练的效率问题。当 RL 训练框架变得足够轻量，更多团队将有能力探索 Agent 的自我改进能力。8600 行本身也是一个克制而有野心的数字。

> 原文：[Marktechpost](https://www.marktechpost.com/2026/08/01/nvidia-ai-releases-molt-a-pytorch-native-agentic-reinforcement-learning-framework/)

## 字节开源 deer-flow：长任务 SuperAgent

字节推出的 deer-flow 定位是长任务 SuperAgent：集成沙箱、记忆、工具、技能与子代理，可处理从分钟级到小时级的复杂任务。

关键点在于「长任务」能力。大多数 Agent 框架擅长单轮工具调用，但真正有价值的工作流往往需要数小时持续执行，涉及状态保持、任务分解和异常处理。deer-flow 用多代理协作配合持久化记忆来解决这个问题。

为什么重要：长任务能力是 Agent 从「玩具」走向「生产力工具」的分水岭。字节这套方案选择完全开源，意味着中小团队也可以基于它构建自己的复杂任务 Agent，而不是被锁定在封闭平台。

> 原文：[https://github.com/bytedance/deer-flow](https://github.com/bytedance/deer-flow)

## Hugging Face 开源本地语音 Agent 框架

Hugging Face 发布了 speech-to-speech 框架，允许开发者完全在本地构建语音 Agent。从语音输入到语音输出，全程使用开源模型，主打隐私与可定制。

关键点是「本地」：无需把语音数据上传到云端，模型推理和 agentic 决策都在本地完成。对于医疗、金融等对数据合规敏感的行业，这是语音 Agent 落地的重要前提。可定制性意味着团队可以针对垂直场景微调语音模型。

Hugging Face 做这件事的用意明显：他们正在把 Agent 生态的各个组件逐一开源，从文本到语音，从模型到框架，试图成为 agentic AI 时代的标准层。

> 原文：[https://github.com/huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech)

## 微软开源 TRELLIS.2：结构化 3D 生成

TRELLIS.2 是微软在 3D 生成领域的新一代开源模型，使用原生且紧凑的结构化潜变量进行生成，面向高质量 3D 资产生成场景。

相比直接生成体素或点云，结构化潜变量让模型在有限的表示空间内捕获更多的几何与纹理信息，从而提升生成质量。这类技术的目标是把 3D 内容生成的成本降到游戏和影视团队可以直接使用的水平。

3D 生成是 AIGC 的下一个战场：一旦质量越过生产门槛，它对游戏、电商、影视行业的影响将是结构性的。微软选择开源 TRELLIS.2，显然是希望在这一赛道上占据定义权。

> 原文：[https://github.com/microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)

## 腾讯云开源 Agent Memory 记忆中枢

TencentDB Agent Memory 将对话、文档和代码转化为四类可复用的记忆资产，让团队内的多个 Agent 共享和治理这些记忆——相当于给 Agent 装了一个组织级的记忆中枢。

关键点在于它把记忆从「单 Agent 的私有状态」升级为「团队共享、可治理的资产」。这对企业级 Agent 落地很重要：单个 Agent 的对话记录往往是噪音，但当记忆被结构化为可查询、可授权的资产，Agent 协作的效率就会质变。

记忆正在成为 Agent 时代最核心的基础设施之一。腾讯云选择在数据库层面做这件事，也说明云厂商正在把 Agent 能力视为下一代云服务的新增长点。

> 原文：[https://github.com/TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory)

## Unsloth 本地 UI 支持 K3/Gemma 4 训练

Unsloth 更新了本地训练界面，新增对 Kimi K3、Gemma 4、Qwen3.6、DeepSeek-V4 等最新模型的支持，让开发者可以在消费级 GPU 上完成训练与推理。

这件事的价值在「本地」：最新开源模型的微调不再依赖云端集群，个人开发者在一张显卡上就能跑。这意味着模型微调的门槛继续下降，更多人可以参与 Agent 的定制化开发。

当所有人都能本地微调最新模型，竞争焦点将从「能不能跑」转向「跑出什么好东西」——数据质量和任务理解会成为新的分水岭。

> 原文：[https://github.com/unslothai/unsloth](https://github.com/unslothai/unsloth)

今天的开源列表像一份预告：Agent 不再只是对话框，而是能跑实验、做研究、建资产的引擎。留给你的问题是——下一个被 Agent 自动化的岗位，会是你所在的那一个吗？