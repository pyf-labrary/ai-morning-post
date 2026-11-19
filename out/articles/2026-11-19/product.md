# Copilot 想当工作 OS，豆包已在收钱

微软在 Ignite 上把 Word、Excel、PowerPoint 直接搬进 Copilot，并给它安了个新身份：「工作的新操作系统」。这句表述值得琢磨——过去两年 Copilot 一直是挂在 Office 侧边栏里的助手，现在两者的位置被调换了。如果这个方向成立，应用产品的竞争焦点就不再是「谁能调用更强的模型」，而是「谁占据用户一天工作的第一屏」。同一天，豆包工作交出了 DAU 800 万、企业 ARR 20 亿元的答卷，国内和海外的两条路径开始显现出不同的收钱方式。

## Copilot 把 Office 装进自己，称「工作的新 OS」

微软在 Ignite 主题演讲中宣布，将 Word、Excel、PowerPoint 嵌入 Copilot 界面，Copilot 不再作为 Office 的附属面板存在，而是反过来成为承载这些应用的容器。官方给它的定位是「工作的新操作系统」，并明确下一步是常驻 agent。

关键点在于控制权的反转。当 Office 变成 Copilot 里的一个窗口，跨文档、跨表格的上下文就落在了 Copilot 手上，常驻 agent 才有可能在不被打断的情况下连续执行任务。这也是「OS」这个说法的实质：不是 UI 层面的整合，而是拿到跨应用上下文和权限调度权。

需要注意的是，产品演示里的整合与真实工作中的权限、审计、数据边界之间还有距离。判断这件事的成败，标准不是界面好不好看，而是那个常驻 agent 究竟能读到多少东西、能替用户按下多少按钮。

> 原文：[Ars Technica](https://arstechnica.com/gadgets/2026/11/microsoft-calls-copilot-the-new-os-for-work-at-ignite-keynote/)

## 豆包工作三个月 DAU 破 800 万，企业 ARR 20 亿元

豆包工作上线三个月，日活突破 800 万，企业客户年度经常性收入（ARR）突破 20 亿元。同期上线了覆盖 21 个专业场景的「工作台」。

两个数字放在一起看才有意义：DAU 说明有真实使用频次，ARR 说明其中一部分已经转化为付费。国内 AI 办公产品过去常被质疑「有量无收」，这组数据至少提供了一个可对照的样本。21 个专业场景的工作台则透露出产品思路——不做通用对话框，而是按岗位切分预置流程，降低用户从「会聊天」到「能干活」之间的落差。

接下来要观察的是留存曲线和客单价结构：800 万 DAU 里有多少是组织强制开通，20 亿元 ARR 里有多少来自少数大客户，决定了这是个平台生意还是一门项目生意。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/cC8dbvo5f5k5tgnE.html)

## Perplexity Computer 上线多智能体，最多 16 个 agent 互相核查

Perplexity 为 Computer 增加了 Multiagent 档位：由一个主 agent 调度最多 16 个子 agent，这些子 agent 可以来自 Claude、GPT、Gemini 等不同模型，共享中间发现，并对彼此的结论做交叉检查。

这是异构模型编排的一次公开押注。以往的多 agent 方案大多在同一个模型家族内拆分角色，Perplexity 直接把不同厂商的模型放进同一个任务里互相挑错，本质是用推理成本换准确率。思路接近学术界的集成方法，但落到了产品交互里。

值得追问的是成本与收益的拐点：16 个 agent 的 token 开销显然不是线性增长的，而分歧出现时由谁裁决、裁决质量如何，决定了这套机制是「降低幻觉」还是「把幻觉平均掉」。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/17/perplexity-computer-multiagent-effort-level/)

## Claude Code 加 Code Mode，用 JavaScript 串起工具调用

Anthropic 为 Claude Code 加入实验性的 Code Mode：模型可以编写 JavaScript 来链式调用 Bash、Read、Edit 等工具，并且在长命令执行期间继续与用户对话。

变化在于工具调用的颗粒度。传统 agent 是「一次调用、一次返回」，多次往返既慢又容易在中途丢失上下文；改成写一段脚本，等于把编排逻辑交给代码，一次提交完成一串操作。长命令运行时不阻塞对话，则解决了编译、安装依赖这类耗时任务的体验断点。

这条路线的隐含前提是模型写代码比模型逐条选工具更可靠——目前这仍是需要验证的假设。若成立，agent 产品的竞争点会从「工具数量」转向「运行时设计」。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/17/anthropic-claude-code-code-mode-javascript-tool-calls/)

## 谷歌给 Gemini 和 AI 搜索加隐私开关与无痕模式

Google 将 Gemini 的「数据用于训练」与聊天历史拆成两个独立开关，用户可以保留历史记录的同时拒绝数据被用于模型训练。Google Search 的 AI 模式则新增临时线程，对话结束后不进入搜索历史。

拆开这两个开关看似细节，实际改变的是默认契约。此前用户往往要在「保存便利」和「不被训练」之间二选一，现在两者解耦，企业采购时关于数据治理的质询也少了一个卡点。

隐私正在从合规条款变成产品功能，且开始具备差异化价值。对面向 B 端的 AI 产品来说，这类开关的设计颗粒度，可能比模型跑分更早影响客户的采购决策。

> 原文：[Ars Technica](https://arstechnica.com/ai/2026/11/google-will-let-you-opt-out-of-ai-training-in-gemini-without-losing-your-history/)

## 千问办公电商版上线品牌知识库

千问办公电商版推出品牌知识库功能：商家上传网店链接、图片素材和设计规范后，Agent 可以理解品牌的视觉与语言风格，在生成图片、视频和文案时保持调性统一。

电商素材生产的真实痛点从来不是「生成不出来」，而是「生成出来不像自己」。单张图好看、整套物料风格割裂，是品牌方最常拒绝 AI 产出的理由。把品牌规范作为知识库前置注入，相当于给生成过程加了一层约束。

这也是 Agent 产品从「通用能力展示」走向「行业工作流嵌入」的典型动作。有品牌资产可上传的商家会先受益，而缺乏规范沉淀的中小卖家，未必能立刻用上这套能力。

> 原文：[雷锋网](https://www.leiphone.com/category/industrynews/DEwlGyHOnFTL6jRy.html)

## Snapchat 让开发者用 Claude Code、Cursor 做 AR 滤镜

Snapchat 宣布 Lens 创作者可以用自然语言描述需求，由 Claude Code、Cursor 这类 AI 编程助手端到端完成 AR Lens 的构建。

这是把专业开发工具下放给创作者的一步。AR 滤镜此前需要专门的脚本与工具链知识，门槛把大量有创意但没工程背景的人挡在外面；引入 AI 编程助手后，平台赌的是创意供给量会发生跃升。

风险同样明确：AI 生成的 Lens 质量是否稳定、审核成本会不会随之上升、平台是否要为生成结果承担更多责任。对 Snap 而言，这是一次用开发者体验换内容生态密度的尝试。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/18/snapchat-now-lets-developers-build-ar-lenses-with-ai-coding-assistants-like-claude-code-and-cursor/)

## Hugging Face 接入 OpenRouter，按价格或速度路由模型

Hugging Face 现在可以通过 OpenRouter 路由模型请求，自动选择价格更低或速度更快的提供商。

路由层的价值在成本敏感型应用里最直接：同一个模型在不同提供商处的定价和延迟差异，过去需要工程团队自己维护对照表，现在被抽象成一次配置。对把 AI 功能当水电用的产品团队，这是实打实的毛利改善。

更长远的影响在议价结构。当调用方可以无痛切换供应商，模型提供商之间的竞争会进一步向价格和吞吐靠拢，而中间的路由层则逐渐沉淀为基础设施——谁掌握路由，谁就掌握分发。

> 原文：[The Decoder](https://the-decoder.com/hugging-face-now-routes-model-requests-through-openrouter-for-the-best-price-or-speed/)

入口、编排、路由，今天这八条其实在回答同一个问题：价值正在从「模型有多强」转移到「谁拿着调用它的那一层」。你所在的产品，站在哪一层？