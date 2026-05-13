# NVIDIA加持的开源Agent框架14万星，Agent生态加速分化

今日开源板块最值得关注的是NVIDIA支持的Hermes Agent框架在3个月内突破14万GitHub星，标志着Agent开发范式进入“自我改进+消费级硬件部署”的新阶段。与此同时，函数调用模型、GUI自动化、安全审核等垂直方向的轻量开源项目密集涌现——这个领域正在从“做大模型”转向“做可落地的小模型+框架”，技术栈的分层与专业化趋势明显。

## NVIDIA支持下的Hermes Agent：14万星背后的Agent框架新范式

Hermes Agent是一个开源Agent框架，由NVIDIA支持开发，近期在GitHub上3个月内获得14万星。其核心特性包括自我改进（self-improvement）能力和支持在RTX PC上本地部署，降低了Agent的落地门槛。关键点在于：它并非单纯提供LLM调用，而是内置了Agent自我反思和迭代的机制，让Agent能根据执行结果自动优化行为。为什么重要——这说明业界对Agent的追求已从“能跑”转向“能自己变好”，同时NVIDIA的硬件生态正在将Agent从云端推向个人设备。  
> 原文：[https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/](https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark/)

## Needle：26M参数的函数调用模型，消费级设备提速至6000 tok/s

Cactus Compute开源的Needle模型只有26M参数，却能高精度执行工具调用（function calling），推理速度达6000 tok/s，远超同类大模型。关键点：参数极小意味着可部署在手机、IoT等边缘设备上，且速度优势让实时工具调用成为可能。为什么重要——它验证了“小模型+专用任务”路线在Agent领域的可行性，函数调用不再是大模型的专利，这将加速Agent在低算力场景的普及。  
> 原文：[https://github.com/cactus-compute/needle](https://github.com/cactus-compute/needle)

## 字节跳动开源UI-TARS：原生Agent框架自动操作GUI

字节跳动开源UI-TARS，一个专为自动化GUI交互设计的Agent框架，支持跨平台操作（桌面、移动端）。关键点：它不是简单的截图+OCR方案，而是原生的Agent框架，能理解UI元素、规划操作步骤并执行点击、拖拽等动作。为什么重要——GUI自动化是AI落地高价值场景（如测试、RPA）的核心需求，字节的开源将推动更多企业级应用基于此构建自己的Agent。  
> 原文：[https://github.com/bytedance/UI-TARS](https://github.com/bytedance/UI-TARS)

## Fastino Labs开源GLiGuard：300M参数安全审核模型，效果媲美数十倍大模型

GLiGuard以300M参数在多项安全审核任务（如色情、暴力、仇恨言论检测）上达到或超越23–90倍大模型（如Llama-3-8B）的准确率。关键点：高效的小模型意味着可以在边缘设备上实时审核，大幅降低成本。为什么重要——内容安全是AI产品的刚需，GLiGuard证明了专用小模型可以在性能上碾压通用大模型+提示词的方案，安全审核领域有望迎来一次“轻量化”变革。  
> 原文：[https://www.marktechpost.com/2026/05/13/fastino-labs-open-sources-gliguard-a-300m-parameter-safety-moderation-model-that-matches-or-exceeds-accuracy-of-models-23-90x-its-size/](https://www.marktechpost.com/2026/05/13/fastino-labs-open-sources-gliguard-a-300m-parameter-safety-moderation-model-that-matches-or-exceeds-accuracy-of-models-23-90x-its-size/)

## 高德与千问开源AGenUI：跨端AI原生UI框架，一套代码覆盖三端

高德地图与通义千问联合开源的AGenUI，是一套AI原生UI框架，支持iOS、安卓和鸿蒙三端。关键点：它并非简单的UI组件库，而是“AI驱动UI生成”——通过自然语言描述直接生成原生界面，并支持跨端一致性。为什么重要——跨端开发一直是痛点，AGenUI将AI作为设计语言的一部分，可能降低多端应用的开发成本，尤其适合AI产品快速迭代。  
> 原文：[https://www.qbitai.com/2026/05/416864.html](https://www.qbitai.com/2026/05/416864.html)

## MetaGPT多智能体框架持续迭代：模拟软件公司运作流程

MetaGPT作为一个多Agent协作框架，持续更新以模拟软件公司（产品经理、架构师、工程师等角色）的完整开发流程，降低Agent开发门槛。关键点：它提供结构化角色分工而非松散CoT，Agent之间通过标准化协议协作。为什么重要——多Agent协作是通往复杂任务自动化的关键路径，MetaGPT的持续迭代表明社区正在探索“组织级”Agent系统，而非单Agent工具。  
> 原文：[https://github.com/FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)

## Statewright：用状态机让AI Agent行为可预测、可调试

开源框架Statewright通过可视化状态机（finite state machine）为AI Agent提供确定性行为控制，让Agent的决策过程可预测、可调试。关键点：它把Agent的“思考”约束为状态转移，避免黑盒随机性，同时提供调试界面。为什么重要——当前Agent最被诟病的是不可靠和不可解释，Statewright从工程角度用成熟的状态机理论解决可靠性问题，可能成为生产级Agent的标配基础设施。  
> 原文：[https://github.com/statewright/statewright](https://github.com/statewright/statewright)

## GitHub发布Spec Kit：以规范文档驱动AI代码生成与测试

GitHub开源Spec Kit，帮助开发者以规范文档（specification）驱动AI代码生成和测试。关键点：它建立了一种“写spec → AI生成代码 → 自动测试”的流水线，强调代码质量而非速度。为什么重要——AI代码生成泛滥后，业界开始关注“可维护性”与“正确性”，Spec Kit提供了一种让人类控制需求、AI执行实现的协作范式，可能改变开发流程。  
> 原文：[https://github.com/github/spec-kit](https://github.com/github/spec-kit)

---

当14万星涌向Agent框架、26M参数模型能精准调用工具时，我们是否已站在“Agent廉价化”的前夜？下一个明天，你的AI应用可能跑在口袋里。