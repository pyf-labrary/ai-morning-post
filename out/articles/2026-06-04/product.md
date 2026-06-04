# 英国出手，谷歌AI摘要可“拒收”

英国监管裁定谷歌必须允许网站退出 AI 搜索摘要，这是全球首个针对生成式搜索的强制包容权，将直接影响 AI 产品的数据合规与商业模式。同日内，Meta 的 WhatsApp AI Agent 全球商用、亚马逊搜索引入 AI 商品图——应用层竞争从能力比拼转向监管与商业化的平衡。

## 英国监管要求谷歌允许网站退出 AI 搜索摘要

英国竞争与市场管理局（CMA）裁定，谷歌必须在 AI 搜索结果中提供更清晰的来源链接，并允许英国发布商选择不被 AI 摘要收录。该裁定目前仅适用于英国，但 CMA 明确要求谷歌将机制推广到全球。核心争议在于：AI 摘要是否属于“合理使用”，以及发布商是否拥有拒绝训练数据的权利。谷歌表示将调整搜索结果页面结构，但未承诺补偿方案。这是一记政策定调：生成式搜索的免费爬取时代可能终结。
> 原文：[Ars Technica](https://arstechnica.com/tech-policy/2026/06/google-ordered-to-put-clearer-links-in-ai-search-and-let-uk-publishers-opt-out/)

## Meta 的 WhatsApp Business AI Agent 全球上线，按 token 收费

Meta 正式面向全球企业客户推出 WhatsApp Business AI 智能体，支持自动回复常见问题、营销互动，并首次采用按 token 计费模式。企业可通过 Meta 的 Business API 接入，无需额外开发。关键点：这是 Meta 在对话式商务领域的变现尝试——按 token 收费比传统 SaaS 订阅更灵活，但也考验企业对话量预估能力。对开发者而言，意味着 WhatsApp 生态从免费通信管道变成了可编程的商业入口。
> 原文：[TechCrunch](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/)

## 亚马逊搜索将显示 AI 生成的产品图片

Amazon 在搜索结果中引入 AI 生成商品图：当用户输入关键词（如“北欧风餐桌”），系统会生成符合场景的合成图片，点击后跳转至相似商品列表。本质是视觉搜索的升级——不再依赖卖家上传的静态图，而是用生成式 AI 填充“模糊需求”的视觉表达。风险在于版权和误导：AI 图与实物不符的责任归属尚未明确。但对电商运营者而言，产品图的竞争将从拍摄水平转向 Prompt 优化能力。
> 原文：[TechCrunch](https://techcrunch.com/2026/06/03/amazon-will-show-ai-product-images-when-you-search-for-some-reason/)

## Perplexity 发布混合 AI 系统：本地与云端自动切换

Perplexity 推出混合推理架构：系统根据任务复杂度、数据敏感度自动判断在设备端还是云端运行模型。例如，文档摘要强制本地执行，复杂逻辑推理则调用云端大模型。关键点是隐私与性能的工程化平衡——不依赖用户手动选择，而是通过延迟阈值和隐私策略自动决策。这对企业用户有吸引力：可降低对云端的依赖，同时满足部分合规要求。不过，本地模型的能力上限仍是瓶颈。
> 原文：[The Decoder](https://the-decoder.com/perplexity-announces-hybrid-ai-system-that-decides-what-runs-locally-or-in-the-cloud/)

## 谷歌推出 AI 工具 Dreambeans，将用户数据变成卡通故事

Google 发布名为 Dreambeans 的 AI 工具，可提取用户 Google 账户中的照片、日历事件、地图轨迹等数据，生成卡通风格的“你的一天”故事插画。名字古怪，但产品逻辑清晰：用个性化叙事降低 AI 工具的使用门槛。争议点在于数据使用权限——用户需授权访问完整个人数据。目前仅限英文地区，免费使用。对产品经理的启示：AI 个人助理的形态可以从“问答”转向“叙事”，Dreambeans 提供了新的交互范式。
> 原文：[TechCrunch](https://techcrunch.com/2026/06/03/googles-dreambeans-its-weirdest-named-ai-tool-to-date-will-turn-your-life-into-a-cartoon/)

## 微软 Codex 新升级：打通 Windows 生态，手机远程开发

Microsoft Codex 迎来重要版本更新：原生支持 Windows 环境（之前仅限于 Web 和 VS Code 扩展），并允许通过手机 App 远程启动开发任务——例如，手机端发送“修复这个 bug”，Codex 可在绑定的 PC 上自动执行代码定位与修改。关键点：微软将 agentic 开发能力嵌入操作系统生态，手机端成为“指令入口”。这直接对标字节扣子（Coze）的远程操控 Agent，但 Codex 的优势在于与 Windows 和 Azure DevOps 的深度集成。
> 原文：[InfoQ 中文](https://www.infoq.cn/article/RcDBAl3VhkNDQvPevPrd)

## 扣子 3.0 实测：手机远程遥控电脑中的 Agent

字节跳动旗下扣子（Coze）正式发布 3.0 版本，打通桌面端、电脑端和手机端：用户可在手机 App 上遥控电脑端 Agent 执行任务，例如“帮我编辑这份 PPT”或“下载那个文件到桌面”。实测反馈显示延迟较前代降低约 40%，且支持多个 Agent 并发。核心变化是从“单一聊天机器人”向“跨设备任务调度器”演进。对产品经理的启示：Agent 真正的价值在于**跨终端调度**，而非单一会话。
> 原文：[量子位](https://www.qbitai.com/2026/06/428648.html)

## 阿里云推出 OS 运维 Skills，AI Agent 自动修复数据库 P0 事故

阿里云在操作系统控制台上线运维 Skills：AI Agent 可自动检测数据库一级事故（如主从延迟、死锁），并在确认风险后执行预设修复脚本，全程无需人工介入。关键创新点是**故障自愈的闭环**——将运维经验固化为一组 Skills 模板，Agent 基于监控指标触发。目前仅支持 MySQL 和 PolarDB，未来计划扩展到网络和存储。对 CTO 而言，这标志着 AI 运维从“告警通知”进入“自动处置”阶段。
> 原文：[InfoQ 中文](https://www.infoq.cn/article/W37w3zzGlPG1UtIhLbRh)

---

当英国要求谷歌让网站“拒收”AI摘要，而亚马逊、Meta却在用AI生成商品图和客服——你更担心监管的闸门，还是数据权利的清算？