# 开源 Agent 基建开始收口

今天开源板块最值得看的不是某个模型，而是八条里有五条在解决同一个问题：怎么把 Agent 从 demo 变成能干活的工具。腾讯的 BrowserSkill、阿里的 open-code-review、Cloudflare 的安全审计技能，分别从浏览器操作、代码审查、安全审计三个具体工种切入，路径一致——用确定性的工程外壳，约束 LLM 的不确定性。这轮开源的竞争点已经从"能不能做"转向"敢不敢用在生产"，谁先把可靠性做出来，谁就先拿到企业侧的真实数据与反馈。对技术团队来说，现在值得动手实测的窗口期比三个月前更明确了。

## MiniMax 开源 Code CLI，命令行入口成为新战场

MiniMax 发布 Code CLI v0.4.12，采用 MIT 许可证面向全球开放，正式进入编码 Agent 的命令行赛道。产品形态是 CLI，意味着它直接嵌入开发者的终端工作流，而不是另开一个 IDE 插件。

关键点在于许可证选择。MIT 是宽松许可里最彻底的一档，允许商用、修改、闭源衍生，配合 MiniMax 自身的模型服务，本质是用开源工具链换取模型调用入口。

为什么重要：编码 Agent 的 CLI 层正在被快速商品化。Claude Code、Gemini CLI 之后，国内厂商开始同步跟进，工具本身不再是护城河，能否在真实仓库规模下稳定跑通才是分水岭。开发者短期是受益方，可以横向比较不同 CLI 在长任务上的完成率。

> 原文：[36Kr](https://36kr.com/newsflashes/3988920115460873?f=rss)

## 英伟达晒 IMO 金牌方案：1.5TB 显存堆出来的正确率

英伟达公开了其在国际数学奥林匹克（IMO）中取得金牌成绩的技术方案，核心做法是依靠 1.5TB 显存进行大规模并行推理，被国内媒体调侃为 AI 版"推恩令"。

关键点是路线选择。这套方案没有追求单次推理的智能密度，而是用算力换采样数量与验证轮次，在数学这种可自动验证的领域里，暴力搜索是有效的。

为什么重要：它再次暴露了当前推理能力的真实来源。数学竞赛的分数提升未必来自模型变得更"聪明"，而可能来自更多候选解与更强的验证器。这条路径留给中小团队的空间很小，1.5TB 显存本身就是准入线。

> 原文：[雷峰网](https://www.leiphone.com/category/ai/XpCc8XUGypadWNGt.html)

## 阿里开源 open-code-review：确定性流水线加 LLM

阿里把内部大规模使用的代码审查工具 open-code-review 开源，架构上是确定性流水线与 LLM Agent 的混合模式，支持行级精准评论和多语言规则集。

关键点在"确定性"三个字。规则引擎负责可枚举的检查项，LLM 负责语义层面的理解，两者分工明确，避免了让模型独自承担全部审查职责带来的漏报与幻觉。

为什么重要：这是大厂第一次把内部规模化验证过的审查流水线完整放出来。对中小团队而言，直接复用的价值高于自己从零搭一套 prompt。更值得关注的是它的架构思路——哪些环节该交给规则、哪些交给模型，这份切分本身就是经验资产。

> 原文：[GitHub - alibaba/open-code-review](https://github.com/alibaba/open-code-review)

## 腾讯开源 BrowserSkill：让 Agent 用你的真实浏览器

腾讯发布 BrowserSkill，形态是 CLI 加浏览器扩展。它允许 AI Agent 操控用户已登录的真实浏览器，并且强调不打断用户正在进行的工作。

关键点是"已登录"和"不打断"这两个约束。前者绕开了自动化中最难啃的登录态与验证码问题，后者则指向一个被忽视的工程细节：Agent 与人在同一个浏览器里共存时的资源调度。

为什么重要：浏览器是绝大多数知识工作的实际载体，谁能让 Agent 安全地接管一部分浏览器操作，谁就打开了 SaaS 类任务自动化的大门。风险同样明显——凭证、Cookie、会话数据都在这个容器里，权限边界的设计会成为落地的前置条件。

> 原文：[GitHub - Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)

## Cloudflare 开源安全审计技能

Cloudflare 发布 security-audit-skill，把编码 Agent 包装成一个分阶段执行、结论可独立验证的安全审计员。

关键点是"可独立验证"。安全审计的结论必须能被复现和交叉检查，否则在真实的安全流程里没有采用价值。这套技能把审计拆成分阶段流程，每一阶段的产出都可以单独核对。

为什么重要：安全领域对幻觉的容忍度接近零，这是 LLM 落地最难的场景之一。Cloudflare 用流程约束替代对模型可靠性的期待，这个思路对金融、合规等同样高风险的领域有直接参考意义。

> 原文：[GitHub - cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

## Addy Osmani 的 agent-skills：把工程规范固化成技能

Addy Osmani 开源 agent-skills 仓库，汇集面向 AI 编码 Agent 的生产级工程技能，目标是把工程规范沉淀为可复用的能力单元。

关键点是它解决的不是模型能力问题，而是组织问题。团队里资深工程师的判断标准——如何写测试、如何组织提交、如何做代码分层——过去只存在于文档和评审意见里，现在试图写成 Agent 能直接执行的形式。

为什么重要：Agent 在团队中落地，瓶颈往往不是模型不够强，而是它不知道这个团队的规矩。技能库这种载体如果能形成事实标准，会显著降低 Agent 接入既有工程体系的成本。

> 原文：[GitHub - addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

## 腾讯开源 WeKnora：文档到 RAG 再到自维护 Wiki

WeKnora 是腾讯开源的知识平台，把原始文档转化为三层产物：可查询的 RAG、具备自主推理能力的 Agent，以及自动维护的 Wiki。

关键点在第三层。RAG 和 Agent 已是常规组合，自动化维护的 Wiki 意味着知识库不再是静态索引，而会随新文档的进入自我更新结构。

为什么重要：企业知识管理的长期痛点是文档腐化——知识库建好之后没人维护，半年后就没人用了。如果 WeKnora 的自维护机制在真实场景里站得住，它解决的是 RAG 项目最常见的死法。

> 原文：[GitHub - Tencent/WeKnora](https://github.com/Tencent/WeKnora)

## Anthropic 开源知识工作者插件库

Anthropic 发布 knowledge-work-plugins，面向 Claude 的知识工作场景，目标是让 Claude 适配特定岗位、团队乃至公司的工作方式。

关键点是粒度的设定。插件不是通用能力增强，而是按岗位和团队做定制，这实际上把 prompt 与上下文工程下沉为可分发、可共享的插件形态。

为什么重要：模型厂商开始直接供给"工作方式"而非仅仅供给模型能力，这会挤压一批做中间层定制服务的公司。同时它也提出了一个问题——当插件库足够丰富时，企业还需要自己搭 Agent 框架吗？

> 原文：[GitHub - anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

今天的八条里，有六条在给 Agent 装"护栏"而不是装"大脑"。真正值得追问的是：当护栏足够厚时，我们评估的到底是模型能力，还是这套工程规范的质量？