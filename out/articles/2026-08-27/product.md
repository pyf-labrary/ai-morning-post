# Perplexity 出电脑，AI 应用押注本地化

今天同时值得注意的并非某一款新品，而是一个集中出现的信号：AI 应用正在从云端向本地端侧迁移。Perplexity 发布基于 NVIDIA DGX Spark 的便携 AI 电脑，苹果强化 Mac mini/Studio 的本地推理能力，WhatsApp 也开始用设备端模型做反诈。当算力、数据与推理都能在本地闭环，应用层的竞争逻辑可能要变。

## Claude 共享记忆：Chat 与 Cowork 终于打通

Anthropic 给 Claude 增加了跨 Chat 与 Cowork 的共享记忆能力。用户不再需要在每次对话或协作任务中重复交代项目背景、偏好和上下文，Claude 能记住之前在 App 里透露过的信息，跨会话延续使用。

关键点是记忆从「单次会话」升级为「跨场景持久化」，而这也是 agent 类产品从工具走向协作者的核心前提。此前用户对 AI 助手最大的抱怨之一就是「每次都要从头教」，共享记忆直接消解了这层摩擦。

对产品设计而言，记忆能力将成为 AI 应用的用户粘性护城河。谁先让用户觉得「它懂我」，谁就更难被替换。

> 原文：[TechCrunch](https://techcrunch.com/2026/08/25/claude-cowork-finally-remembers-what-you-told-the-app-in-chat/)

## Perplexity 便携电脑：零 token 成本的本地宣言

Perplexity 推出基于 NVIDIA DGX Spark 的便携式 AI 电脑，内置本地 Harness 和 OS 级沙箱环境，主打本地 AI 工作流，并强调本地步骤的「零 per-token 成本」。

这款产品本质上是把「AI 工作台」做成了实体硬件。开发者可以在本地跑推理、搭沙箱、执行多步任务，按 token 计费的模式在本地环节被消除。加上 OS 级沙箱，安全边界也比普通应用层方案更硬。

它释放的信号不只是硬件新品，而是 AI 应用层对成本结构的重新思考：如果本地推理已经足够好，为什么每个请求都要经过云端？Perplexity 在用硬件形态，押注「本地优先」会成为下一阶段的工作流默认选项。

> 原文：[MarkTechPost](https://marktechpost.com/2026/08/25/perplexity-ships-portable-computer-on-nvidia-dgx-spark-local-harness-os-enforced-sandbox-and-zero-per-token-cost-for-local-steps/)

## ChatGPT for Teachers 覆盖 55 个美国学区

OpenAI 将 ChatGPT for Teachers 推广至 55 个美国学区，为超过 10 万名教育工作者提供安全 AI 工具与配套培训。

重点不在于「又有学区接入」，而在于 OpenAI 开始用标准化产品+培训的组合进入教育这个高门槛行业。工具本身之外，大规模教师培训意味着 OpenAI 在认真处理「AI 进课堂」的责任问题，也为其争取教育采购预算铺路。

教育场景的特点是决策链条长、数据敏感、预算稳定。一旦形成标杆案例，ChatGPT for Teachers 就有机会像 Google Workspace 之于学校那样，成为下一代教育基础设施。对竞品而言，这是一个需要警惕的卡位。

> 原文：[OpenAI](https://openai.com/index/bringing-chatgpt-for-teachers-to-more-us-school-districts)

## 苹果 Mac mini/Studio：本地推理的算力宣言

苹果更新 Mac mini 与 Mac Studio，重点强化本地 AI 推理能力。多家外媒将其解读为对英伟达算力霸权的新一波施压。

过去苹果芯片更多强调能效和创作场景，这代产品则明确把「本地跑大模型」作为核心卖点。开发者可以在不依赖云端 GPU 的情况下完成推理任务，隐私和延迟优势随之而来。

这件事对应用层的影响是基础设施层面的：如果 Mac 能轻松跑动主流模型，端侧 AI 应用的技术门槛会进一步降低。英伟达主导的云端算力叙事，正在被「每个人的桌面都是算力」的叙事分流。对创业团队来说，这或许意味着一个新的开发目标平台已经出现。

> 原文：[Ars Technica](https://arstechnica.com/apple/2026/08/with-new-mac-studio-and-mac-mini-apple-leans-hard-into-local-ai-inference/)

## Radar 让 13 万播客成为 AI agent 可调用的数据源

Particle 推出 Radar 服务，转录并分析超过 13 万档播客内容，提供可搜索网页以及 API/MCP 接口，使播客不再只是「听」的内容，而能被 AI agent 直接调用。

播客一直是信息密度高但极难检索的媒介。Radar 把它结构化以后，等于为 AI agent 打开了巨大的语音知识库。更关键的是 MCP 接口的接入——agent 生态的数据源正在从网页、文档扩展到音频内容。

对应用产品来说，这类「非结构化内容转结构化数据」的服务会越来越多。先打通优质数据源的玩家，有机会成为 agent 生态里的基础设施层。

> 原文：[TechCrunch](https://techcrunch.com/2026/08/26/radar-makes-podcasts-searchable-and-usable-by-ai-agents/)

## 即梦 AI 推「即梦片场」，押注 AI 影视发行

即梦 AI 宣布推出「即梦片场」，成立影视内容厂牌，面向电影和剧集项目公开征集，提供算力、技术、资金与行业资源支持。

这不是一个简单的「AI 视频工具」活动，而是一次内容产业链的纵深切入。从创作工具延伸到制作投资与发行，即梦 AI 想让 AI 生成内容直接进入传统影视工业的流通环节。

影视行业的核心资源是资金、渠道和信任。即梦 AI 用算力和技术换项目入场券，是在赌 AI 生成内容能批量产出商业级作品。如果跑通，AI 视频的变现路径就不只是卖工具，而是参与内容分成。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/bVlL8Bsgh6GURrf7.html)

## 「豆包工作」+飞书：企业 Agent 的形态雏形

深度体验显示，字节跳动「豆包工作」与飞书整合后的企业智能体方案，是目前最接近落地的产品形态之一。

它的特别之处在于 AI 不是独立入口，而是生长在飞书的 IM、文档、日历和审批流之上。企业用户的真实工作场景被直接转化为 agent 的调用上下文，比单独做一个「AI 办公应用」要自然得多。

这也回应了一个争论：企业 agent 的终局是独立应用，还是嵌入现有工作流？字节的答案显然是后者。飞书提供了场景和数据，豆包工作提供模型和自动化，两者叠加出来的体验，可能比很多「从零搭建」的 agent 平台更接近日常使用习惯。

> 原文：[量子位](https://www.qbitai.com/2026/08/479348.html)

## WhatsApp 设备端 AI 反诈：隐私与安全不再二选一

WhatsApp 正在测试设备端 AI 欺诈检测能力，在不把消息内容上传云端的前提下，识别可疑对话和诈骗行为。

关键技术在于「设备端」三个字。端到端加密通信产品一直面临安全与隐私的两难——要检测诈骗就得看内容，看内容就可能破坏加密承诺。WhatsApp 把 AI 推理放到手机本地，绕开了这个矛盾。

这件事对应用产品有普遍参考意义：很多敏感场景（医疗、金融、办公）都在等「不上云也能智能」的方案。设备端推理一旦成熟，隐私保护就不再是产品能力的上限，反而可能成为差异化卖点。

> 原文：[InfoQ](https://www.infoq.cn/article/wAVlMqVg7fqPjXAyFDjC)

当记忆、算力和安全都开始走向端侧，真正值得追问的或许只剩一个：你的用户，凭什么还要为一个云端中转买单？