# ChatGPT Health上线，模型路由三连发

**今日最值得关注的是OpenAI正式推出ChatGPT Health，首次接入苹果健康数据，标志着AI助手进入个人健康管理场景。同时，Runway、Cursor同日发布模型路由工具，阿里真武超节点跑通2.4万亿参数模型——应用层正在从“选模型”转向“自动选模型”，成本与精度博弈进入新阶段。**

## ChatGPT Health：AI助手接入你的健康数据

**是什么：** OpenAI面向美国用户推出ChatGPT Health功能，允许用户授权连接医疗记录和Apple Health数据，获取个性化的健康洞察。

**关键点：** 用户需主动授权数据接入，ChatGPT将基于心率、睡眠、运动记录以及病历信息，提供健康趋势分析和建议。目前仅限美国地区，OpenAI强调数据不会用于训练模型。

**为什么重要：** 这是AI助手首次以第一方能力切入个人健康数据场景，而非通过第三方App。苹果健康数据生态拥有数亿活跃用户，但此前缺少AI层解读能力。如果ChatGPT Health在隐私合规和准确性上过关，可能重塑数字健康服务入口。

> 原文：[OpenAI - Health in ChatGPT](https://openai.com/index/health-in-chatgpt)

## Runway Media Router：自动选模型，降低生成质量不确定性

**是什么：** Runway推出Media Router工具，根据用户设定的质量、速度或成本偏好，自动为图像、视频、音频生成任务选择最优底层模型。

**关键点：** 当前生成式媒体模型数量激增，Runway Media Router相当于一个“调度层”，将请求路由到最合适的模型（如Stable Diffusion、Midjourney或Runway自家模型），不再需要开发者手动配置。

**为什么重要：** 模型碎片化是开发者痛点，Media Router试图解决“到底该用哪个模型”的选择成本。对于非技术用户，它降低了试错门槛；对于API调用方，它可能成为事实上的聚合层，影响模型提供商的议价能力。

> 原文：[TechCrunch - Runway bets on AI model routing](https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/)

## Cursor Router：代码编辑器的“成本优化器”

**是什么：** Cursor面向Teams/Enterprise用户推出Cursor Router，一个请求级分类器，自动将编码查询路由到最合适的模型（如GPT-4o vs Claude 3.5 Opus），声称可降低编码成本30-50%。

**关键点：** 分类器实时判断问题复杂度：简单重构走便宜模型，复杂架构设计走昂贵模型。与Runway类似，但聚焦代码场景。仅限企业版，个人用户暂未开放。

**为什么重要：** 代码助手成本是团队部署的核心考量。Cursor Router相当于给AI编码上了“弹性算力”，在保持前沿质量的同时大幅优化开支。如果效果验证，可能成为IDE标配功能，倒逼其他代码助手跟进。

> 原文：[MarkTechPost - Cursor releases Cursor Router](https://www.marktechpost.com/2026/07/22/cursor-releases-cursor-router-a-request-level-classifier/)

## 阿里真武超节点跑通2.4万亿参数模型：国产超节点推理迈入新量级

**是什么：** 阿里云宣布其真武M890超节点已成功运行超2万亿参数的大模型Qwen3.8（2.4万亿参数），并上线百炼平台提供推理服务。

**关键点：** 这是国产超节点首次支持万亿参数级以上模型推理，真武架构采用高速互联和统一内存池设计，解决了大模型推理的内存墙问题。Qwen3.8基于MoE架构，推理时的激活参数远小于总参数量。

**为什么重要：** 超节点适配大参数模型，意味着企业客户可以在公有云上直接调用2.4万亿参数模型的推理，无需自建集群。这对于需要极强上下文理解和生成能力的复杂任务（如长文档分析、科学计算）是基础设施级别的利好，也侧面验证了阿里云在AI基础设施上的追赶速度。

> 原文：[量子位 - 阿里真武超节点成功适配2.4万亿参数大模型](https://www.qbitai.com/2026/07/457694.html)

---

当AI能读懂你的心率，你会不会把病历交给ChatGPT？模型路由在三个不同场景同日落地，这可能不是巧合——应用层正在从“拼模型参数”转向“拼调度效率”。