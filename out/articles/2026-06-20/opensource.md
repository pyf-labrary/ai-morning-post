# Netflix开源省70万；Kilo与Zero-Native发布

今天开源领域最值得关注的是 Netflix 开源的 AI Token 优化工具——砍掉 90% 冗余 token，每年省下 70 万美元推理成本。这种从底层做减法的思路，比堆算力更值得工程团队参考。

## Netflix 开源 AI Token 优化工具：砍掉 90% 冗余 token，年省 70 万美元

**是什么**：Netflix 开源了一款 AI Token 优化工具，通过识别并移除模型输出中的无用 token，将推理 token 量减少 90%，每年节省约 70 万美元推理成本。

**关键点**：该工具针对 Transformer 模型的冗余输出进行剪枝，而不会影响生成质量。Netflix 已在内部大规模部署验证，现以开源形式向社区开放，代码可集成到现有推理管线中。

**为什么重要**：Token 数量直接绑定 GPU 算力成本与响应延迟。对于高流量 AI 服务商而言，这是一个立竿见影的降本手段——无需修改模型架构，仅在后处理环节做减法即可。

> 原文：[InfoQ](https://www.infoq.cn/article/SdkcGqZQ2coEqM04xsQG)

## 开源编码代理 Kilo 发布：面向代理的全栈工程平台

**是什么**：Kilo-Org 开源了 Kilo，一个以代理（agent）为核心的工程平台，覆盖代码构建、部署和持续迭代。其内置了多个流行的开源编码代理，并支持多代理协作。

**关键点**：Kilo 提供类似“代理操作系统”的环境，开发者可通过自然语言或配置文件驱动代理完成编码、测试、CI/CD 等任务。它与 Git 工作流深度集成，允许多个代理并行处理不同模块。

**为什么重要**：Agentic engineering 正在从演示走向生产。Kilo 抽象了单个代理的管理问题，为团队提供统一的协作层，降低了引入编码代理的门槛，可能加速 AI 辅助开发的规模化落地。

> 原文：[GitHub](https://github.com/Kilo-Org/kilocode)

## Vercel 开源 Zero-Native：基于 Zig 的跨平台原生框架

**是什么**：Vercel Labs 开源了 Zero-Native，一个使用 Zig 语言编写的跨平台原生应用框架，致力于在桌面和移动端实现高性能开发。

**关键点**：Zig 以零运行时开销和与 C 的无缝互操作著称。Zero-Native 提供声明式 UI 绑定和原生编译链路，开发体验类似 React Native，但无额外运行时开销。Vercel 内部已用于部分工具链原型。

**为什么重要**：跨平台框架（Flutter、React Native）统治多年，但性能与包体积仍是痛点。Zero-Native 将 Zig 的安全性和性能带入前端场景，对于构建性能敏感的原生应用（如编辑器、图形工具）提供了新选项。

> 原文：[InfoQ](https://www.infoq.cn/article/PHO4u00H2hgWgkVzg3H4)

---

三个项目分别指向推理降本、代理工程和跨平台新语言。Netflix 的工具最直接——开源社区能复制的不只是代码，更是“从推理成本中挤利润”的工程思维。你的团队现在在哪一环上最需要这样的减法？