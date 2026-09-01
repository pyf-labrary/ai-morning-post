# OpenClaw 史上最大更新，浏览器即开即用

今天开源圈最值得看的不是某个新框架，而是 OpenClaw 迎来史上最大更新：933 名贡献者、超 1.6 万次 PR，并将运行门槛降到「打开浏览器即可」。当 agentic 工具的能力密度和易用性同时拐弯，开源 Agent 就不再只是开发者的玩具，而可能成为下一轮应用生态的底座。与此同时，AWS、Hugging Face、browser-use 等团队接连开源内部工具，今天这 8 条 story 几乎都与 Agent 有关——方向已经很明确了。

## OpenClaw 更新：Agent 进入「零安装」时代

OpenClaw 发布史上最大更新，累计 933 名贡献者、超 1.6 万次 PR，并支持直接在浏览器中运行。这意味着用户不再需要配置本地环境或依赖 GPU 集群，打开网页即可体验完整的 Agent 能力。

关键点在于：这不仅是功能迭代，而是分发模式的改变。浏览器即运行时，让 agentic 工具的触达范围从开发者扩展到普通用户，也降低了生态参与的门槛。

为什么重要：OpenClaw 之前是开源 Agent 领域最活跃的项目之一，此次更新加上庞大的贡献者基数，已经在事实上成为 agentic 生态的基础设施候选。当一个工具从「装环境才能跑」变成「打开就能用」，它的扩散曲线会完全不同。

> 原文：[InfoQ：OpenClaw 迎来史上最大更新，浏览器即可运行](https://www.infoq.cn/article/9RS84kmpRvz4IqRUbNoe)

## Hugging Face 发布 200+ WebGPU Kernel，浏览器跑 AI 再进一步

Hugging Face 发布 `@huggingface/kernels`，包含 200 多个 WebGPU 内核，用于在浏览器中加速本地 AI 推理，涵盖矩阵运算、注意力机制等常见算子。

关键点：WebGPU 内核的覆盖度和优化程度，直接决定了浏览器端大模型的上限。此前浏览器跑模型主要受限于算力和算子效率，这批内核试图从底层补齐这个短板。

为什么重要：结合 OpenClaw 的浏览器运行，可以嗅到一条清晰的趋势：AI 和 Agent 正在把「浏览器」当作新的操作系统。Hugging Face 在做的是为这个操作系统提供底层加速能力。

> 原文：[Hugging Face：WebGPU Kernels](https://huggingface.co/blog/webgpu-kernels)

## 亚马逊云科技开源内部 Agent 工作台

亚马逊云科技将内部 Agent 工作台开源，该项目由 3 名开发者从副业做起，半年内用户冲到 4 万。此前它一直被用作 AWS 内部团队的 Agent 开发环境。

关键点：一个「副业项目」在半年内达到 4 万用户，且背后是 AWS 的工程文化——说明 agentic 工作流已经不再是实验室概念，而是内部基建。开源意味着 AWS 想把外部开发者纳入同一个生态。

为什么重要：大厂把内部工具开源，通常标志着这个赛道已经过了「验证期」，进入「圈地期」。对开发者而言，这是低门槛使用大厂 Agent 工程实践的机会；对竞争者而言，这是一个需要认真对待的信号。

> 原文：[InfoQ：亚马逊云科技开源内部 Agent 工作台](https://www.infoq.cn/article/Um4rVTweSFXAiwdGLFVB)

## 架构图 Agent archify 走红 GitHub

GitHub 热榜上的 archify 宣称能一键生成架构图，并且图表可以校验、随代码实时更新。它把「画图」从手工活变成了 agentic 任务。

关键点：架构图最大的问题是「画完就过期」。archify 的价值主张是让图表与代码保持同步——生成只是开始，持续更新才是真正的卖点。

为什么重要：如果它能真正做到与代码同步，架构图就从「文档」变成了「活的可视化状态」。这在大型项目协作和合规审计中具备实际价值，也代表着 Agent 在工程效率工具上找到了一个确切的落点。

> 原文：[GitHub：archify](https://github.com/tt-a1i/archify)

## browser-use 开源 video-use：编码 Agent 开始剪视频

browser-use 团队开源 video-use，让编码 agent 直接编辑视频。项目基于 browser-use 的浏览器自动化能力，把视频处理纳入 agent 的「工具集」。

关键点：这不是又一个 AI 视频生成工具，而是让 agent 能理解、定位并操作视频帧与时间轴。路径不同于生成式 AI，属于「Agent 操作媒体」的路线。

为什么重要：Agent 的能力正在从操作网页、代码，延伸到操作视频这类非结构化内容。这意味着 agentic 自动化可以进入视频制作、内容审核、后期处理等重人工场景，边界比我们想象的要大。

> 原文：[GitHub：browser-use/video-use](https://github.com/browser-use/video-use)

## 实测吴恩达开源 OpenWorker：为什么它不 Work？

雷锋网对吴恩达团队开源的 OpenWorker 进行了实测，结论是：它在实际使用中并不如预期那样 Work，存在任务完成度不稳、复杂场景下表现拉胯等问题。

关键点：OpenWorker 发布时备受关注，但实测揭示了「展示效果」与「真实可用性」之间的落差。雷锋网的测试方法值得参考：用真实任务，而非 demo 场景。

为什么重要：开源社区已经被「发布即高潮」透支了太多次信任。OpenWorker 的案例提醒我们，对于 agentic 工具，别只看 README，要看实测。这也会倒逼团队在发布前多做真实场景测试。

> 原文：[雷锋网：实测吴恩达开源 OpenWorker](https://www.leiphone.com/category/yanxishe/HIGpHGf3ko6B1osw.html)

## 拆解 1.1 万个 DeepSeek Harness 插件：官方治理缺位

雷锋网拆解了 1.1 万个 DeepSeek Harness 插件，发现官方几乎没有建立插件治理机制——缺少审核、安全检测、权限分级和版本管理。

关键点：1.1 万个插件说明生态足够繁荣，但数量不等于质量。没有治理机制的插件生态，意味着恶意插件、数据泄露、供应链投毒等风险完全暴露给用户。

为什么重要：插件生态是 Agent 平台的核心护城河，但治理缺位会迅速侵蚀用户信任。这不是 DeepSeek 一家的问题，而是整个 agentic 生态正在面临的集体考题——在「鼓励创新」和「守住底线」之间，官方不能缺席。

> 原文：[雷锋网：拆解 1.1 万个 DeepSeek Harness 插件](https://www.leiphone.com/category/yanxishe/nTnT9RZW5p5Q23hG.html)

## OpenMontage 号称首个开源 agentic 视频生产系统

OpenMontage 自称是「全球首个开源 agentic 视频生产系统」，提供 12 条生产管线与 700+ agent 技能，覆盖从剧本到成片的完整流程。

关键点：「首个」和「自称」需要分开看。700+ agent 技能看起来是很大的数字，但实际效果取决于每个技能的质量和管线之间的配合，而不是数量。

为什么重要：视频生产是 AI 应用最拥挤的赛道之一，但大多数产品聚焦在单点生成。OpenMontage 试图用 agentic 的方式打通全流程，方向正确，只是还需要更多独立测试来验证「全球首个」是否名副其实。

> 原文：[GitHub：OpenMontage](https://github.com/calesthio/OpenMontage)

今天开源 Agent 的工具链已经铺到了浏览器、视频、架构图和插件生态，但 OpenWorker 的翻车和 DeepSeek 插件的治理缺位也在提醒我们：跑通 demo 和跑进生产环境，中间隔着一整个工程化的距离。留给你的问题是：当 Agent 能剪视频、画架构图、写代码的时候，你的工作流里最先被替代的是哪个环节？