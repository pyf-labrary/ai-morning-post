# ChatGPT Work上线，Agent自主工作流

OpenAI 今日将 Codex 更名为 ChatGPT Work，推出可独立运行数小时的自主工作流 Agent。这不是又一款对话工具，而是 AI 从“问答”到“执行”的关键跃迁——它能在后台操作本地文件、串联多步任务，真正开始代替人“做事”。此外，OpenAI 砍掉仅八个月的 Atlas 浏览器、人形机器人完成首例活猪手术等动态，共同勾勒出 agentic 时代的产品竞争格局。

## ChatGPT Work上线：Agent 从“对话”走向“执行”

原 Codex 正式更名为 ChatGPT Work，定位为“可独立工作”的 Agent。用户只需描述目标，它就能在后台持续运行数小时，自主调用工具、操作本地文件、完成完整工作流——例如自动整理数据、生成报告并发送邮件。关键点在于：这不是简单的指令-响应循环，而是具备长时记忆与任务拆解能力的自主执行单元。这对产品经理而言意味着 Workflow 类产品的设计范式将被改写；对技术人而言，agentic 架构的可靠性、权限控制与失败回滚成为新挑战。

> 原文：[Ars Technica](https://arstechnica.com/ai/2026/07/openai-wants-its-new-tool-to-do-your-work-for-you-and-with-you/)

## OpenAI 关停 Atlas 浏览器，Agent 浏览功能并入桌面端

推出仅八个月的 AI 浏览器 Atlas 被砍。OpenAI 承认独立浏览器策略未达预期，但其核心的 Agent 浏览能力——如自动填表、跨站信息收集——已转移到 ChatGPT 桌面应用及 Chrome 扩展。这一调整表明 OpenAI 在 Agent 入口上更倾向于“嵌入现有生态”而非另起炉灶。对于投资人和产品经理，这是重要的战略转向信号：Agent 的“前端”不需要是独立浏览器，而是无处不在的插件或桌面伴侣。

> 原文：[TechCrunch](https://techcrunch.com/2026/07/09/openai-is-shutting-down-atlas-but-its-ai-browser-ambitions-are-still-growing/)

## 人形机器人完成全球首例活猪手术，远程控制验证可行性

外科医生通过远程控制人形机器人，成功对活猪执行手术操作。这是全球首次人形机器人独立完成活体手术——机器人不仅完成了切割、缝合等精细动作，还能根据实时影像自主微调力反馈。关键点在于：机器人并非预设程序，而是由人类医生远程实时操控，验证了“人机协同手术”的可行性。对于医疗 AI 产品而言，这打开了远程手术、手术培训等场景的商业想象空间。

> 原文：[Ars Technica](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/)

## 百度搭子升级企业版，日均提问增 20 倍

百度通用智能体“百度搭子”发布企业版，同时个人版新增智能路由、多端共享记忆等功能。官方称日均提问量同比增长 20 倍，背后逻辑是：Agent 从“通用对话”转向“场景化助手”，企业版可对接内部知识库与审批流程。对国内产品团队而言，这意味着 Agent 的商业化落地正从 C 端娱乐转向 B 端生产力，而“记忆共享”能力是形成用户粘性的关键。

> 原文：[量子位](https://www.qbitai.com/2026/07/447681.html)

## Google 要求所有 AI 生成广告必须标注

Google 更新广告政策，要求广告主披露广告内容中任何由 AI 合成或修改的部分，新规已开始执行。此前 AI 生成的超逼真图像、视频已被广泛应用于宣传，消费者难以辨别。该政策旨在提升透明度，也为合规团队和广告技术公司带来新问题：如何在不降低转化率的前提下完成标注？对产品经理来说，这预示着更多平台将跟进类似规定，AI 生成内容的标识会成为标配功能。

> 原文：[TechCrunch](https://techcrunch.com/2026/07/09/google-will-now-disclose-which-ads-are-made-with-ai/)

## Claude 上线 Reflect 仪表盘，可视化 AI 使用模式

Anthropic 为 Claude 推出 Reflect 功能，以仪表盘形式展示用户与 AI 的交互记录——包括使用频率、话题偏好、回答长度等。表面上是“帮你了解自己用 AI 的习惯”，实质上是在潜移默化强化用户对 Claude 的依赖：数据越积累，迁移成本越高。对竞品而言，这是 Anthropic 在用户留存上的暗棋；对产品设计者，Reflect 是“数据即护城河”的教科书案例。

> 原文：[TechCrunch](https://techcrunch.com/2026/07/09/anthropics-new-claude-feature-is-quietly-selling-you-on-ai/)

## 字节跳动发布 10 亿参数 AI 华语歌模型

字节跳动宣布从零预训练的华语歌音乐生成模型，10 亿参数规模，大幅提升了中文歌词与旋律的自然契合度，告别早期 AI 生成歌曲的“机械感”。关键点：模型专门针对华语音乐的数据分布优化，而非通用音乐模型的中文适配。这意味着字节正在用“垂直优化”策略切 AI 音乐市场——对产品经理，这是如何选择“大而全 vs 专而精”路线的直接案例。

> 原文：[量子位](https://www.qbitai.com/2026/07/447602.html)

## 智能体 PC 端侧部署 35B 模型进 32GB 内存

英特尔联合多家厂商展示智能体 PC，在端侧成功运行 35B 参数大模型，仅占 32GB 内存。这意味着下一代 PC 可以在无网络环境下本地执行复杂 AI 任务，隐私与延迟问题得到缓解。对于技术从业者，端侧部署的模型压缩、量化技术是关键看点；对投资人与产品经理，这进一步压缩了“云+端”的边界，Agent PC 可能成为可落地的消费级产品。

> 原文：[雷锋网](https://www.leiphone.com/category/chips/JCZ1098a28zh4gsH.html)

---

当 Agent 可以独立工作数小时、手术机器人开始活体试验、终端设备本地运行 35B 模型——AI 产品的边界正在从“工具”滑向“伙伴”。你准备好重新定义“人机协作”了吗？