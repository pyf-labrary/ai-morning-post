# MoE 开源双响：激活参数变小成新赛点

开源模型进入「稀疏激活」效率赛段，今日两条消息都指向同一个趋势。Thinking Machines 的 276B MoE 模型把激活参数压到 12B，能在单张 B300 上跑，值得今天多看一眼。AMD 另一边放出的 16B 完全开源模型，则说明硬件厂商正从训练侧直接切入模型生态。参数竞赛没有结束，但算力门槛的竞争先来了。

## Thinking Machines 开源 276B MoE 模型 Inkling-Small

是什么：Thinking Machines Lab 发布并开源 Inkling-Small，总参数 276B、每 token 激活 12B 的多模态 MoE 模型，可视为其 Inkling 模型的小体量版本。

关键点：总参 276B 的模型能落在单张 B300 上运行，靠的是 MoE 的稀疏激活机制——每次推理只动用 12B 参数。官方称其以约四分之一的体量对标 Inkling，意味着开源社区可以用近一个数量级更低的硬件成本获得接近大参数量模型的能力。

为什么重要：这条发布把「开源」和「可部署」绑在了一起。过去「开源 276B」往往意味着只有少数团队能用得起；Inkling-Small 的单卡可运行，等于把多模态 MoE 的试验场拓宽到了个人开发者。它是开源模型在工程效率上的一种表态，也回应了推理成本持续走高的行业焦虑。

> 原文：[Thinking Machines Lab Releases Inkling-Small: 276B Open-weights Multimodal MoE Model](https://www.marktechpost.com/2026/08/02/thinking-machines-lab-releases-inkling-small-276b-open-weights-multimodal-moe-model/)

## AMD 发布 Instella-MoE：16B 完全开源模型

是什么：AMD 推出 Instella-MoE-16B-A3B，总参数 16B、每 token 激活 2.8B，全部权重开放，模型由 AMD Instinct GPU 从头预训练完成。

关键点：与常见「基于开源模型微调」不同，这是一个独立训练产物；从头训练的事实，加上完全开放的权重，说明 AMD 补齐的是从芯片到模型的整条链路。2.8B 的激活参数也意味着该模型在推理时对计算资源的需求极低，适合在边缘设备或消费级硬件上部署。

为什么重要：硬件厂商直接发布模型，正在改变开源生态的供给结构。此前英伟达、AMD 更多停留在「卖芯片 + 优化框架」的层面，Instella-MoE 的出现则展示了 AMD 用自家 GPU 训练大模型的硬实力。对开发者来说，多了一个可自由修改、不受云厂商绑定的基座选择。

> 原文：[AMD Instella-MoE: 16B-A3B Fully Open Mixture-of-Experts LLM](https://www.marktechpost.com/2026/08/01/amd-instella-moe-16b-a3b-fully-open-mixture-of-experts-llm/)

开源 MoE 本轮拉低的究竟是部署成本线，还是模型能力的天花板？至少今天，答案偏向前者。