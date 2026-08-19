# Mojo 1.0 落地，AI 基建再添一把火

Modular 今天正式发布 Mojo 1.0，这是该语言诞生以来最重要的一个版本节点。对 AI 基础设施开发者而言，Mojo 的稳定版意味着 Python 生态与高性能计算之间，终于有了一个值得认真评估的桥梁。

## Mojo 编程语言发布 1.0 正式版

Modular 宣布 Mojo 1.0 正式可用。Mojo 是一种面向 AI 基础设施开发者的编程语言，设计上兼容 Python 语法，但底层编译为高性能机器码，目标是在保持 Python 生态易用性的同时，提供接近 C/C++ 和 CUDA 的执行效率。

1.0 版本的核心价值在于 API 稳定性和工具链完备性。此前 Mojo 处于快速迭代期，API 变动频繁，生产环境采用风险较高。现在语言规范、标准库和编译器行为已经冻结，Modular 同步提供了完整的文档、调试工具和 IDE 支持，降低了团队评估和试用的门槛。

Mojo 的定位很明确：不是要取代 Python，而是吃掉 AI 基础设施中那些 Python 性能不够、C++ 开发效率太低的中间地带。如果你所在的团队正在做推理引擎、数据处理管道或模型服务层，Mojo 1.0 值得放进技术选型的候选清单。但也要注意，Mojo 的生态和社区仍在早期，第三方库的丰富程度远不及 Python 和 Rust，这可能是实际落地时最大的阻力。

> 原文：[Modular: Mojo 1.0 is here](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here)

## Woxi：用 Rust 重写 Wolfram 语言

Woxi 是一个用 Rust 实现的开源 Wolfram Language 解释器，附带类似 Mathematica 的 notebook GUI。项目已经公开发布，代码和文档均可在官网获取。

这个项目值得关注的点有两个：一是 Wolfram 语言本身闭源且授权费用昂贵，Woxi 提供了一个开源兼容层；二是实现方式选择了 Rust，这意味着内存安全和性能都有较好的基础保证。目前 Woxi 对 Wolfram 语言标准的覆盖程度尚不完全，适合作为学习工具或轻量替代方案，但如果你在跑重度符号计算或依赖 Wolfram 专有算法库，现阶段的 Woxi 还撑不起来。

对开源社区来说，这个项目更像是一个起点——用现代系统语言重写经典计算工具的可行性证明。后续如果 Woxi 的兼容性和性能持续提升，它有可能成为 Wolfram 生态之外的一个真正可用的替代品。目前值得观望，值得 Star。

> 原文：[Woxi](https://woxi.ad-si.com)

## 教程：macOS 虚拟机 GPU 直通加速 llama.cpp

trycua 发布了一篇技术指南，演示如何在 Apple Silicon 的 macOS 虚拟机中启用 GPU 直通（GPU passthrough），从而显著提升 llama.cpp 的 LLM 推理性能。

GPU 直通通常与 Linux 和 PCIe 设备相关，Apple Silicon 的虚拟机此前受限于虚拟化层的 GPU 访问方式，性能和灵活性都打了折扣。这篇教程的实操价值在于：它给出了一条明确路径，让开发者可以在 macOS 虚拟机里跑出接近宿主机的推理速度。对于需要隔离环境、多版本测试或团队协作场景下跑本地模型的人来说，这解决了一个很实际的问题。

不过教程的适用范围有限——需要 Apple Silicon 硬件、合适的虚拟机软件版本，以及一定的配置耐心。它更适合已经熟悉虚拟化和 LLM 工具链的中高级开发者。如果你偶尔在 macOS 上跑 llama.cpp 并觉得速度不够，这篇指南值得花十分钟读完。

> 原文：[GPU passthrough for macOS VMs (llama.cpp)](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md)

## Hax：用 C 写的极简终端 AI 编程智能体

Hax 是一个用 C 语言实现的终端原生 coding agent，主打极简、低依赖和快速响应。项目已开源，官方页面展示了其基本用法和设计理念。

在大模型编程助手普遍走「重客户端 + 插件生态」路线的当下，Hax 走了另一个极端：一个 C 文件级别的单二进制，不依赖 Node.js 或 Python 运行时，启动即用。对于 SSH 到远端服务器、容器内开发或对系统资源敏感的场景，这种轻量方案有天然的吸引力。

Hax 的定位显然不是替代 Cursor 或 Copilot，而是服务于「快速、临时、终端内」的代码辅助需求。它的能力上限取决于底层调用的模型和 prompt 策略，C 实现的优势更多体现在启动速度和资源占用上。如果你对 agent 类工具的性能开销敏感，或者需要在没有图形界面的环境里干活，Hax 值得一试。

> 原文：[Hax](https://usehax.dev/)

---

Mojo 终于从「等它稳定」变成了「可以试用」，但真正的考验才刚刚开始。与此同时，Woxi 用 Rust 重新诠释 Wolfram，Hax 则用 C 语言的极简回应重客户端潮流——这两条支线或许都在提醒我们：语言生态的竞争，从来不只是性能之争。