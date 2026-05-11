# 陶哲轩亲测ChatGPT：17分钟论文级推理

今天最值得关注的是菲尔兹奖得主陶哲轩亲测ChatGPT 5.5 Pro，17分钟内产出论文级数学推理成果。他明确强调消化理解仍属于人类——这提醒我们，AI在特定领域已接近专家水平，但人类的“吃掉、消化”能力仍是认知壁垒，而技术投资人更应关注后续人机协作的落地门槛。

## Meta与斯坦福提出Fast BLT：推理加速超50%

Meta FAIR与斯坦福合作提出Byte Latent Transformer的三种推理方法，在不使用子词分词的前提下，减少内存带宽开销超过50%。该工作直击LLM推理的显存瓶颈——传统方法依赖tokenization，但Byte级模型因序列更长导致内存访问密集。Fast BLT通过优化注意力计算与内存布局，将字节级模型的实用性大幅提升。

> 原文：https://www.marktechpost.com/2026/05/11/meta-and-stanford-researchers-propose-fast-byte-latent-transformer-that-reduces-inference-memory-bandwidth-by-over-50-without-tokenization/

## Sakana AI与NVIDIA用L1稀疏化实现20%加速

研究显示，L1正则化可在前馈层诱导超99%稀疏性，配合定制CUDA内核将稀疏性转化为真实吞吐提升。实验证明，推理提速20.5%，训练提速21.9%。关键点在于：传统稀疏化方法往往仅减少计算量，却因稀疏访问模式导致内存带宽未改善；而TWELL（该工作命名）通过CUDA内核专门优化稀疏矩阵乘法，使之匹配硬件特性。

> 原文：https://www.marktechpost.com/2026/05/11/sakana-ai-and-nvidia-introduce-twell-with-cuda-kernels-for-20-5-inference-and-21-9-training-speedup-in-llms/

## 陶哲轩亲测ChatGPT 5.5 Pro：17分钟论文级数学推理

菲尔兹奖得主陶哲轩使用ChatGPT 5.5 Pro，在17分钟内完成论文级数学推理任务。他评价该模型能生成复杂的推理链条、构建反例、甚至提出新引理，但强调“人类必须消化理解它给出的材料”——模型擅长输出，却缺乏对回答的深层自信与判断力。对于产品经理而言，这意味着AI可作为“超强协作者”，而非自动结论引擎。

> 原文：https://www.qbitai.com/2026/05/415186.html

## 具身大模型迎来R1时刻：LIBERO基准突破99.9%

新具身大模型在LIBERO基准上达到99.9%成功率，首次在隐空间实现物理推理新范式。这意味着模型不再依赖显式符号规划，而是通过感知-行动联合嵌入直接生成机器人操作策略。该结果挑战了“具身智能需要结构化知识”的假设，为通用机器人从仿真走向真实场景提供了可复现路径。

> 原文：https://www.qbitai.com/2026/05/415065.html

## 浙大发布AI角色扮演框架：四通道消息驱动沉浸式交互

浙江大学提出角色扮演框架，支持四通道消息流（语言、动作、表情、环境），实现如福尔摩斯探案等沉浸式交互体验。该工作针对现有角色扮演AI对话单一、缺乏上下文感知的痛点，通过多模态消息调度让AI agent同时管理多条叙事线索。对产品经理来说，这是打造“高代入感”虚拟角色引擎的具体技术方案。

> 原文：https://www.qbitai.com/2026/05/415048.html

当AI能在17分钟完成论文级推理，数学家的角色会从解题者变成鉴赏家吗？