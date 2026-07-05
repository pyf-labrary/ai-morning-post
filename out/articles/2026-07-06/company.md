# Codex推理令牌争议，阿里禁Claude Code

今天最值得关注的是OpenAI Codex因推理令牌聚类被曝性能退化，社区质疑其设计决策；同时Anthropic Claude Code出现会话泄漏漏洞，Alibaba内部禁用Claude Code，操作系统级安全担忧蔓延。此外亚马逊停止Mechanical Turk新客户，数据众包时代终结——这些动态指向AI工具在实际部署中的关键风险。

## OpenAI Codex推理令牌聚类引发性能退化争议

GitHub Issue #30364 曝光：GPT-5.5 Codex 在推理时采用令牌聚类（token clustering）策略，将相关推理步骤压缩为集群以减少开销，但实测显示该机制在长上下文或复杂任务中会导致响应质量下降，甚至产生逻辑断裂。社区用户提交了多个基准测试复现案例，认为这是2026年以来Codex最严重的回归。OpenAI尚未正式回应。

**为什么重要：** 如果推理令牌聚类的优化方向被证实有系统性问题，将动摇当前主流大模型部署中广泛使用的“推理压缩”范式。这不仅是Codex的问题，也是整个LLM推理效率与质量权衡的缩影。

> 原文：https://github.com/openai/codex/issues/30364

## Anthropic Claude Code发现会话/缓存泄漏漏洞

安全研究人员在 Claude Code 工作区中发现：当多个实例在同一宿主机运行时，会话令牌和模型缓存数据可能被其他进程读取，导致跨用户信息泄漏。漏洞编号 #74066，已提交至 Anthropic 官方仓库。目前尚无补丁，风险等级被标记为“高”。

**为什么重要：** Claude Code 作为 agentic 编程工具，常被赋予对代码仓库和 API 密钥的访问权限。若缓存泄漏真实存在，意味着使用 Claude Code 的企业可能面临凭据泄漏和机密代码暴露风险。这一漏洞与同期阿里对 Claude Code 的禁用决策形成呼应。

> 原文：https://github.com/anthropics/claude-code/issues/74066

## AI模型系统提示大规模泄露，涉及多家厂商

GitHub 仓库 `asgeirtj/system_prompts_leaks` 公开了包括 Anthropic、OpenAI、Google、xAI 等主流模型的最新系统提示原文，部分内容揭示了模型的安全过滤策略和底层工具调用逻辑。泄露源于部分开发者将生产环境下的系统提示附加至公开 Issue 或 PR 中。

**为什么重要：** 系统提示本是模型的“黑盒”行为边界，一旦公开，攻击者可针对性绕过安全限制或逆向工程模型决策逻辑。这标志着AI安全从算法层面扩展到供应链层面——提示工程已成为新的攻击面。

> 原文：https://github.com/asgeirtj/system_prompts_leaks

## 亚马逊停止接受Mechanical Turk新客户

亚马逊宣布自2026年7月5日起不再接受 Mechanical Turk（MTurk）新客户注册，现有客户可继续使用至2027年，届时服务将完全关闭。MTurk曾是AI训练数据标注的主力平台，近年因众包质量下降和替代方案（如自动化标注、合成数据）兴起而逐渐式微。

**为什么重要：** MTurk的关停是AI数据众包时代的标志性终点。合成数据、RLHF人工反馈等新范式已占据主导，劳动力密集型数据标注模式彻底退出历史舞台。对依赖众包数据的中小团队而言，数据获取成本将显著上升。

> 原文：https://techcrunch.com/2026/07/05/amazon-will-stop-accepting-new-customers-for-mechanical-turk/

## 阿里巴巴禁止员工使用Claude Code

阿里将 Claude Code 列为“高风险软件”，内部禁止用于任何工作场景。理由是该工具会访问本地文件系统、命令行和网络，存在数据外泄隐患。此举引发国内开发者对国产替代方案的讨论，如 CodeGeeX、通义灵码等。

**为什么重要：** 阿里是国内第一家明确禁用 Claude Code 的科技巨头。这反映出企业对 agentic 工具安全性的担忧已超越技术尝鲜热情。同时，禁令可能加速国内AI编程工具的合规化演进和生态封闭。

> 原文：https://techcrunch.com/2026/07/04/alibaba-reportedly-bans-employees-from-using-claude-code/

## Meta考虑推出AI算力租赁服务Meta Compute

扎克伯格在内部会议上称“模型可以慢，但GPU必须盈利”，Meta计划将闲置的AI算力以租赁形式对外提供，服务名称暂定 Meta Compute。此举旨在提升H100等GPU集群的利用率，同时与AWS、Google Cloud竞争算力市场。

**为什么重要：** Meta 从模型研发者转向算力供应商，意味着大型科技公司正在重新评估“GPU即资产”的策略。若 Meta Compute 正式推出，将改变AI算力的竞争格局——自建集群不再只为训练自家模型，也能直接变现。

> 原文：https://www.qbitai.com/2026/07/443339.html

## OpenAI发布Codex插件，实现Claude Code与Codex协同

OpenAI 开源了一款名为 `codex-plugin-cc` 的插件，允许开发者从 Claude Code 中直接调用 Codex 进行代码审查、自动修复和任务委托。该插件基于 WebSocket 协议实现跨工具通信，目前支持 VS Code 和 JetBrains IDE。

**为什么重要：** 这是 OpenAI 首次主动开放 Codex 接口与其他 agentic 工具协作。打破闭源壁垒的行为或暗示其希望 Codex 成为编程 agent 的“底层推理引擎”，而非单一IDE插件。这也给 Claude Code 用户提供了“不换工具也能用OpenAI能力”的选择。

> 原文：https://github.com/openai/codex-plugin-cc

## Midjourney要求好莱坞片方披露AI使用详情

在针对涉及生成式AI的版权诉讼中，Midjourney 要求迪士尼、华纳兄弟、Netflix 等三大制片厂公开其在影视制作中“明确使用了哪类AI工具、生成内容占比多少以及训练数据来源”。片方以商业秘密为由拒绝。

**为什么重要：** 这起诉讼将 AI 在创意产业中的“使用透明度”推至法庭。如果法院支持 Midjourney 的请求，好莱坞将被迫量化 AI 对剧本、视觉特效、配音的介入程度，可能催生行业级AI使用披露标准。

> 原文：https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/

---

结语：今天的故事都在追问同一个问题：当AI工具从实验进入生产，「安全」和「透明度」的账该由谁埋单？