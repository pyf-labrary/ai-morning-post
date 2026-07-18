# 无反向传播训练突破，EEG基础模型开源

**导语**：今天研究板块最值得关注的是Sakana AI提出的Error Diffusion方法——它无需反向传播即可训练符合Dale原则的神经网络，在MNIST和CIFAR-10上跑出合理性能，这可能动摇深度学习的基础假设。同时，Zyphra发布了380M参数的EEG基础模型ZUNA1.1，支持变长输入并完全开源，为脑电研究提供了便捷的预训练工具。

## Sakana AI 发布无反向传播训练方法，突破生物限制

Sakana AI 提出了 Error Diffusion，一种无需反向传播即可训练神经网络的新方法。核心在于它兼容 Dale 原则（神经元释放单一类型神经递质）的双流网络架构，通过误差扩散机制替代梯度回传。在 MNIST 上达到 96.7%，CIFAR-10 上 61.7% 的准确率，虽然远逊色于反向传播训练的 SOTA，但证明了“生物合理”学习路径的可行性。

**为什么重要**：反向传播虽是当前深度学习基石，却被认为与生物神经元学习机制相悖。Error Diffusion 展示了一条无需全局梯度计算、更贴近生物硬件的替代路线。如果后续能提升性能，可能催生低功耗、高并发的神经形态计算方案，对 AI 硬件架构产生深远影响。

> 原文：[MarkTechPost - Sakana AI's Error Diffusion](https://www.marktechpost.com/2026/07/17/sakana-ais-error-diffusion-trains-dale-compliant-dual-stream-networks-reaching-96-7-mnist-and-61-7-cifar-10-without-backpropagation/)

## Zyphra 发布 EEG 基础模型 ZUNA1.1，支持变长输入

Zyphra 开源的 ZUNA1.1 是一个 380M 参数的 EEG 基础模型，采用 Apache 2.0 许可。最大亮点是支持 0.5 到 30 秒的变长输入，无需对原始信号进行固定长度裁剪或填充。模型基于 Transformer 架构，在多个脑电基准上表现优异，可直接用于睡眠分期、癫痫检测等下游任务的微调。

**为什么重要**：EEG 数据往往长度不一，传统方法需强制对齐，导致信息丢失或引入噪声。ZUNA1.1 的变长设计节省了预处理时间，降低了入门门槛。考虑到 Apache 2.0 开源协议，研究团队可以在商业场景中直接使用，有助于加速脑机接口和神经科学应用的落地。

> 原文：[MarkTechPost - Zyphra Releases ZUNA1.1](https://www.marktechpost.com/2026/07/17/zyphra-releases-zuna1-1-an-apache-2-0-eeg-foundation-model-with-variable-length-inputs-from-0-5-to-30-seconds/)

**结语**：当无反向传播训练开始触及 MNIST 时，EEG 基础模型已准备好被更多人用起来——你更看好哪个方向先落地？