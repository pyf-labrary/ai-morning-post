# 谷歌和苹果，开始争抢你的桌面

## 导语

今天应用产品板块最值得看的是同一件事的两面：谷歌给 Gemini 加上了直接操作 Mac 的 agent 能力，同一天苹果被曝在自研能操作 Mac 的 AI agent。两家操作系统厂商同时把手伸向「替你点鼠标」这一层，意味着桌面 agent 已经从演示走向平台竞争。配套的动向也在同一天密集出现：训练沙箱、模型路由、代码安全审计，都是围绕 agent 运转的基础设施。

## Gemini 拿到 Mac 的操作权

谷歌为 Gemini 增加了 Mac 桌面 agent 能力，可以自动整理文件、填写表单并完成多步骤工作流。

关键点在于「多步骤」和「代操作」这两个词：模型不再只是回答问题，而是直接在文件系统和应用界面上执行动作。这类产品真正的门槛不在推理能力，而在权限模型——它能读哪些目录、能否代替用户提交表单、出错后如何回滚、操作日志给谁看。这些细节决定它能不能从尝鲜功能变成日常工具。

为什么重要：Mac 是知识工作者的主力设备，拿到这一层的执行权，就等于拿到一个高频入口。对谷歌而言，这也把 Gemini 从浏览器标签页里拉出来，进入操作系统层面的竞争。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/)

## 苹果也被曝在做同一种 agent

据 TechCrunch 报道，苹果正在构建能直接操作 Mac 的 AI agent，对标 Meta Muse、Claude 与 OpenAI Dots。该消息目前属于传闻，苹果未公开确认。

值得注意的是「对标名单」本身：三个对手里有两个是外部模型厂商的产品，而不是系统自带助手。这暗示苹果对这一层的定位可能不再是语音问答，而是执行层——替用户完成跨应用的操作。

为什么重要：苹果一贯的做法是等能力成熟后把它内置成系统默认项。如果传闻属实，第三方 Mac agent 的窗口期会比想象中短；反过来说，苹果在权限与隐私上的保守，也可能让它在能力开放度上落后一轮。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/19/apple-may-be-developing-its-own-ai-agent-that-runs-your-mac/)

## Codex 从写代码延伸到审代码

OpenAI 发布 Codex Security Plugin 与 PR 扫描演示，并给出 Daybreak Red 受监督安全调查的参考架构。

这组动作的指向很明确：Codex 的能力边界从「生成代码」扩到「审查代码」。PR 扫描是最容易标准化的切入点——diff 是结构化的、上下文有限、结果可评估，天然适合 agent 反复跑。而「受监督的安全调查」这一说法也说明 OpenAI 在刻意强调人类复核环节，没有把全自动渗透测试当作卖点。

为什么重要：安全审计的边际成本一旦被压低，安全团队的工时会从「找问题」转向「定规则、复核结论」。这对中小团队是实质利好，对大厂安全部门则是流程重写。

> 原文：[OpenAI](https://openai.com/business/learn/codex-security-plugin-demo)

## Meta 的 AI 穿戴设备可能卖 300 美元

The Information 报道称，Meta 即将推出的 AI 穿戴设备 Muse Charm 定价约 300 美元；Meta 的回应只有一句「很快有更多消息」。

300 美元这个价位值得注意：它低于主流 AR 眼镜，高于普通蓝牙配件，落在一个「买来试试不心疼、但也不是随手送人」的区间。结合 Muse 这个命名与「Charm」的形态暗示，Meta 似乎在把 always-on 输入设备往更轻、更日常的方向推，而不是继续加厚眼镜这条线。

为什么重要：AI 硬件的竞争重点正在从「能不能做出 demo」转向「定价能不能进入大众换机预算」。300 美元是一次明确的价格测试，结果会直接影响其他厂商明年的产品定义。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/19/metas-new-muse-charm-device-may-cost-300/)

## Perplexity 用一个端点调度多家模型

Perplexity 推出 Orchestrator API，用单一接口接入 OpenAI、Anthropic、Google、xAI 与开源模型，支持同一模型跨供应商的故障转移，以及统一计费。

这三个特性分别解决了三类现实痛点：多模型接入的工程成本、单供应商故障导致的可用性风险、以及多份账单带来的财务对账麻烦。尤其是「同模型跨供应商故障转移」——它把「模型」和「托管方」解耦了，这是过去一年企业采购里最难处理的一环。

为什么重要：模型路由层正在变成一门独立生意，卖点是厂商中立。风险也明显：这一层技术壁垒不高，最终差异化只能落在路由策略、延迟表现和 SLA 上。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/11/19/perplexity-orchestrator-api-failover-model-routing/)

## OpenAI 用 Codex 给 ChatGPT 做性能体检

OpenAI 披露了 Performance Factory：一套由 Codex 驱动的自动化工作流，用于持续定位并修复 ChatGPT 的性能问题。

这类内部实践的信息量往往比产品发布更大。性能回归是一个典型的「高频、重复、需要上下文」的工程任务，人做起来枯燥，机器做起来刚好——定位、复现、提出修复、验证，形成闭环。OpenAI 把它做成流水线，说明 agent 已经在承担自家核心产品的维护工作。

为什么重要：这是「AI 修 AI」的早期样本。如果这套模式可复制，下一个被重构的会是所有大型在线服务的 on-call 与性能优化流程。

> 原文：[OpenAI](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)

## 谷歌造了一个「镜像互联网」训练浏览 agent

WIRED 报道，Chrome 团队搭建了一个平行的互联网沙箱，让浏览 agent 在无风险环境中训练和测试。

真实网页对 agent 训练来说有两个硬伤：不可回滚，以及有副作用——一次误点可能真的下单、真的发帖。沙箱同时解决了复现性和安全性：同一个任务可以反复跑，失败不产生外部成本。

为什么重要：浏览 agent 的瓶颈正在从模型能力转向评测环境。谁能提供稳定、覆盖面足够、且贴近真实网页复杂度的沙箱，谁就掌握了这一轮的迭代速度。这也顺带把「agent 该有多大权限」的问题提前摆上了桌面。

> 原文：[WIRED](https://www.wired.com/story/google-built-a-giant-mirror-dimension-internet-to-test-its-chrome-ai-agents/)

## 华为云用算力共享拉低具身机器人门槛

华为云以 CloudRobo 平台让一批算力卡轮流服务多家机器人公司，一次适配多方受益，减少重复造轮子的工程成本。

逻辑很朴素：具身智能公司在早期普遍面临算力利用率低、适配工作重复的问题，每家都要把同一套底层能力重新调一遍。共享算力池加上一次适配多方复用，摊薄的是固定成本而非边际成本。

为什么重要：机器人行业的竞争常被描述为模型与硬件的比拼，但中段公司真正的瓶颈往往是工程效率。这类平台如果跑通，会让一批小团队的 product-market fit 验证周期显著缩短。

> 原文：[量子位](https://www.qbitai.com/2026/11/511426.html)

## 结语

当操作系统厂商自己下场做桌面 agent，第三方产品的护城河只剩下数据和场景。问题留给你：你愿意把 Mac 的操作权交给谁——系统内置的那个，还是你挑的那个？