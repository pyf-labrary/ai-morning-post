# AI Agent技能生态集中爆发

今天开源圈最值得看的不是某个新模型，而是 Agent Skills（智能体技能）这个新层开始成形：Anthropic 与 Google 不约而同公开官方技能库，NVIDIA 随即补上安全扫描工具。技能生态有潜力成为 Agent 能力分发的下一个主战场，而围绕它的治理与安全，也在同一时间被提上日程。

## Anthropic 与 Google 同日公开 Agent Skills

两家巨头几乎在同一时间亮出了自己的官方技能仓库：Anthropic 在 GitHub 发布 skills 仓库，Google 也发布了面向自家产品的技能集，二者均旨在为 Claude、Codex 等智能体提供可复用技能。表面看是“示例代码”，实质是各自主导 Agent 技能生态的落子。

技能比 prompt 更结构化，比插件更轻量，一旦形成事实标准，第三方生态就会跟着某个方向走。两家同日公开，竞争信号很强：Agent 能力的竞争正在从模型本身，延伸到技能的定义、分发与复用环节。

> 原文：[Anthropic Skills GitHub 仓库](https://github.com/anthropics/skills)

## FreeToken：让 35B 模型在 RTX 4060 上跑起来

据 InfoQ 报道，这个来自伯克利/MIT 的开源推理项目 FreeToken，在 RTX 4060 上跑通了 35B 参数的模型，速度约为每秒 39 Token。这个数字谈不上惊艳，但它把“本地运行大模型”的硬件门槛又压低了一档。

关键不在于一块消费级显卡多能打，而在于推理优化正在成为开源社区的主攻方向。当 35B 级模型不再依赖数据中心级硬件，开发者在本地做验证、跑 agentic 任务的成本会显著下降。这对中小团队和独立开发者尤其重要。

> 原文：[InfoQ 报道：FreeToken 让 RTX 4060 运行 35B 模型](https://www.infoq.cn/article/tij5T0vJ1Yk0s7Uov7SE)

## SkillSpector：给 agent 技能做安全扫描

NVIDIA 开源的 SkillSpector，能在安装前检测 Claude Code、Codex 以及 MCP 技能中的漏洞、恶意模式和提示注入风险，目标很明确：防范供应链攻击。技能生态刚有起色，安全问题就跟着来了。

当 skill 像 npm 包一样被 agent 安装和执行，它就成了新的攻击面——恶意技能可以伪造工具行为、注入指令、窃取上下文。SkillSpector 的价值不只是工具本身，而是提醒开发者：agent 技能需要当作有完整生命周期的软件资产来治理。

> 原文：[NVIDIA SkillSpector GitHub 仓库](https://github.com/NVIDIA/SkillSpector)

## DeepMind 开源 WeatherNext 2 全球天气模型代码

Google DeepMind 在 GitHub 上发布了 WeatherNext 2 的代码，覆盖中期全球大气预报与热带气旋预测，官方场景明确写着“可用于气象研究与业务”。气象大模型此前多为闭源或受限发布，这次开源意味着第三方可以验证、微调并尝试落地。

对气象领域来说，代码开源比模型演示更有价值——研究机构不用再停留在“读论文、看榜单”，可以直接在真实预报任务上测试效果。这也给其他科学计算类 AI 项目开了一个不错的头。

> 原文：[DeepMind WeatherNext GitHub 仓库](https://github.com/google-deepmind/weathernext)

## Ponytail：AI 的最高准则，是少写代码

一个名为 Ponytail 的 Agent skill 在 GitHub 与 Product Hunt 双热。它的核心理念很反直觉：让 AI 像一个“最懒的资深工程师”，把不写新代码当作最高准则，优先减少无用代码生成。这不是一个能力型工具，更像是给 agent 立行为规矩。

它走红的背景不难理解：代码型 Agent 的普遍问题是“写得多不等于写得好”——重构引入风险、改动越界、维护负担变大。Ponytail 提醒我们，agent 的技能不只是“会更聪明”，也包括“知道什么不该做”。

> 原文：[Ponytail GitHub 仓库](https://github.com/DietrichGebert/ponytail)

技能生态正在重演应用商店早期的故事，谁掌握分发与安全，谁就离定义标准更近一步。接下来的悬念是：Agent 技能会走向开放协议，还是形成新的围墙花园？