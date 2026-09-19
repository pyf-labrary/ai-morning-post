# 六个开源项目在给 Agent 修路和设卡

今天开源板块最值得看的是 Browserbase 的 Stagehand：它把 Playwright 的速度和 token 账单同时往下压，宣称提速一倍、token 降八成——这类数字来自项目自述，需要自己复现，但方向已经很清楚。把它和 Anthropic 的角色插件库、Cloudflare 与 NVIDIA 的安全扫描、微软的 agent 训练器放在一起看，8 条里有 6 条在补 Agent 的外围：能操作浏览器、能被训练、能被审计。模型能力的边际收益在下降，工具链和治理层的竞争才刚开始。

## Anthropic 开源知识工作插件库，把 Claude 变成岗位专家

Anthropic 开源 knowledge-work-plugins，面向 Claude Cowork，用插件把 Claude 定制成特定角色、团队与公司的专家，目标用户是知识工作者而非开发者。

关键点在于"公司"这一层：当插件承载的是团队流程与私有上下文，配置本身就成了可分发资产。开源这套结构，相当于把"如何把通用模型调教成岗位专家"的模板交出来，任何团队都能照着搭自己的版本。风险也在同一处——插件里装入什么上下文，决定了它能做什么、能碰到什么数据。对有合规要求的公司，权限界定会比插件本身更花时间。

> 原文：[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

## Browserbase 开源 Stagehand：Playwright 快 2 倍、token 省 80%

Browserbase 发布浏览器自动化项目 Stagehand，称在保持能力的前提下让 Playwright 运行速度提升一倍、token 消耗降低 80%，面向 AI Agent 的网页操作场景。

浏览器操作是当前 agent 落地最贵的环节之一：每一步都要把 DOM 或截图喂给模型，token 与延迟直接决定任务能否规模化。如果 token 降 80% 这一项成立，单位任务的成本曲线会被重画，web agent 从 demo 走向批量运行的门槛也随之下降。需要提醒的是，这是项目自述数据，基准怎么设、在哪些站点上测，都会显著影响结论。对于在做 web agent 的团队，这是今天最该亲自跑一遍的项目。

> 原文：[browserbase/stagehand](https://github.com/browserbase/stagehand)

## Cloudflare 开源 security-audit-skill：把编码 Agent 变安全审计员

Cloudflare 发布 security-audit-skill，让编码智能体执行多阶段安全审计，产出可独立验证的机器可读结论，并隔离各阶段操作。

两个设计细节值得注意：一是"机器可读 + 可独立验证"，这是 agent 输出进入 CI 与合规流程的前提，否则审计结果只能给人看，无法被流水线消费；二是阶段隔离，本质是在限制 agent 的权限扩散，避免一次审计变成一个全权限会话。由基础设施厂商来做这件事，说明"agent 做安全审计"正在从演示走向工程问题。

> 原文：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

## 腾讯开源 BrowserSkill：让 Agent 用你的已登录浏览器

腾讯推出 BrowserSkill，通过 CLI 加浏览器扩展，让任意支持 shell 的 AI Agent 在用户真实、已登录的浏览器上操作，且不打断用户手头的工作。

已登录状态是 agent 触达真实网页的分水岭：省掉了登录、验证与风控，代价是把用户的会话凭证交到 agent 手里。"不打断手头工作"意味着共享同一个浏览器实例，权限边界与误操作回滚必须在设计层面回答，而不只是靠提示词约束。今天有三个浏览器 agent 项目同时出现，说明这个位置还没有事实标准，谁的权限模型更让人放心，谁就更可能被采用。

> 原文：[Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

## NVIDIA 开源 SkillSpector，扫描 Agent 技能里的提示注入

NVIDIA 发布 SkillSpector，用于在安装前扫描 Claude Code、Codex、MCP 技能中的漏洞、恶意模式、提示注入、数据外泄与供应链风险。

技能与插件生态的扩张速度已经超过人工审查的能力，而一条被投毒的 skill 就足以在用户机器上执行动作。把扫描放在"安装前"，是把防线前移到供应链入口，这也是 npm、PyPI 生态过去十年反复验证过的思路。结合今天的角色插件库和审计 skill 一起看：agent 生态正在长出属于自己的一层安全工具，而且第一波就来自厂商而非社区。

> 原文：[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

## 微软开源 agent-lightning：给 AI Agent 做训练器

微软发布 agent-lightning，定位为"点亮 AI 智能体"的绝对训练器，帮助开发者训练和强化各自的 agent 系统。

此前改进 agent 主要靠两条路：换更强的模型，或者改 prompt 和工具编排。有了训练框架，团队可以把自有的执行轨迹变成权重，把改进沉淀在模型侧而不只是提示词里——别人改 prompt 时你能改权重。代价是数据与算力门槛，收益是护城河。微软在模型层之外开源训练层，和它在 agent 生态中的整体站位是互补的。

> 原文：[microsoft/agent-lightning](https://github.com/microsoft/agent-lightning)

## Unsloth 更新：本地跑与训 LLM 的 UI

Unsloth 推出本地运行与训练大模型及扩散模型的图形界面，兼容 GGUF、MLX，并支持 Qwen3.8、DeepSeek-V4、MiniMax-H3、Gemma 4、FLUX 等模型。

Unsloth 原本以微调加速著称，这次把"跑"和"训"收进同一个图形界面，等于把本地实验的门槛又降一档：不用再在推理引擎和训练脚本之间来回切换。对不愿把数据送出内网的团队，这类工具正在变成默认选项。需要注意的是模型支持列表更新极快，具体可用性以仓库当前状态为准，别按二手信息做技术选型。

> 原文：[unslothai/unsloth](https://github.com/unslothai/unsloth)

## datasette-auth-github 发布 1.0

Simon Willison 的 Datasette GitHub 登录插件发布 1.0 正式版，为 Datasette 实例提供基于 GitHub 的身份认证。

1.0 的意义是接口稳定，可以放心依赖，不必担心升级时被破坏性变更打断。对内部数据集的发布流程而言，"用 GitHub 账号登录"往往是最省事的权限方案：不额外维护账号体系，直接复用团队已有的身份。单看是一条小新闻，但它代表开源里那类真正做完了的基础设施——没有发布会，只有版本号。

> 原文：[datasette-auth-github 1.0](https://simonwillison.net/2026/Sep/19/datasette-auth-github/)

今天开源的主角不是模型，是给 agent 修路和设卡的人。当技能可以安装、浏览器可以共享、审计可以自动化，你愿意把哪一步交给它？