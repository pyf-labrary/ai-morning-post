# 模型榜首抢在 IPO 前易主

今天最值得看的一件事，是 Anthropic 在 IPO 路演当天同时放出 Fable 5.2 与 Mythos 5.2，凭借 100 万 token 上下文和 FrontierCode 2.0 的 49.1% 重回榜首。但把六条发布放在一起看，发布本身正在贬值：Google 的 Gemini 4 Carbon 快到被评论为“发布即过时”，Meta 则干脆承认 agent 的大部分活是可以用三分之一成本跑完的苦力。这一天真正的信号不是谁分数最高，而是竞争的轴心移到了档位设计、单位任务成本和任务分工上。

## Anthropic 双版本：把安全策略做成产品线

Fable 5.2 与 Mythos 5.2 是同一模型的两档安全策略，支持 100 万 token 上下文，FrontierCode 2.0 得分 49.1%，定价 8/40 美元每百万 token（输入/输出）。关键不在于多了两个名字，而在于同一套权重可以卖给风险偏好不同的客户——安全从合规成本变成定价分层的手段。选在 IPO 路演当天发布，是给投资人讲的叙事：能力领先，并且可交付。需要注意的是，这类双档设计意味着“最强版本”未必是默认版本，采购方在验收时必须先确认自己拿到的是哪一档、降级了什么。

> 原文：[The Decoder](https://the-decoder.com/claude-fable-5-2-and-mythos-5-2-cement-anthropics-ai-lead-just-before-its-ipo/)

## Gemini 4 Carbon：迭代快到“发布即过时”

DeepMind 上线 Gemini 4 Carbon，主打更强推理与更长上下文，llm-gemini 等工具链同步跟进；有评论称更新速度已快到“发布即过时”。这条最值得注意的不是参数，而是节奏带来的下游成本：模型版本的半衰期在缩短，锁定一个版本做产品，几周后就得重跑评测和回归测试。工具链同步跟进是个好信号，说明“跟上版本”正在从项目变成常规工作流，但 eval 的维护成本会实打实地压到每个应用团队头上。

> 原文：[Google DeepMind](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)

## Meta Muse Ember：小模型去干 agent 的苦力活

Meta 最小的模型 Muse Ember 面向工具调用、编码子任务与文档解析，同样支持 100 万上下文，在 Artificial Analysis 智能指数上追平 Claude Haiku 5.5，单任务成本约三分之一。agent 系统的账单大头从来不是那几次关键推理，而是高频、低难度的循环调用；用旗舰模型跑这些是纯浪费。Meta 这一定位等于把“模型路由”产品化：贵模型做决策，便宜模型做执行。竞争点因此从榜单分数转向单位任务成本，这对做 agent 产品的团队是更直接的利好。

> 原文：[The Decoder](https://the-decoder.com/meta-launches-muse-ember-a-small-ai-model-built-for-the-repetitive-work-agents-actually-do/)

## Gemini Robotics 2.5：成功率翻倍，附带一份会自曝的基准

DeepMind 推出新一代视觉-语言-动作模型 Gemini Robotics 2.5，部分任务成功率提升至两倍，并在奔驰装配试点中实现 96% 的金属件分拣，同步开源 ASIMOV-jailbreak 安全基准。96% 是特定分拣任务上的试点数据，不能外推到通用装配，但方向清晰：物理世界的 agent 一旦进入产线，失败的代价不是重试一次而是停线，因此可靠性比能力上限更值钱。一起开源的越狱基准则说明，DeepMind 希望“机器人被怎么骗”这件事在公开尺度上被测量，而不是留在实验室里。

> 原文：[Google DeepMind](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)

## 字节 Seedream 5.5：图像模型的竞争回到工程指标

新一代图像模型 Seedream 5.5 在 100 轮连续图像编辑测试中稳定性明显提升，同时提速并下调 API 价格。图像模型的单图能力差距已在收敛，真正的生产痛点是多轮编辑中的一致性——角色、风格、构图会不会漂移，而“100 轮连续编辑”这个测试设计恰好打在这里。稳定性提升叠加快和便宜，指向的是内容生产流水线，而不是演示 demo。这一档的竞争，接下来会比拼工程指标而不是惊艳度。

> 原文：[量子位](https://www.qbitai.com/2026/11/508828.html)

## 英伟达 GR00T 2：看人类视频，把自己想象成机器人

英伟达 GR00T 2 通过观看人类视频完成自我具身想象，减少对真实机器人采集数据的依赖。具身智能的瓶颈长期在数据侧：真机采集贵、慢，且难以规模化。用人类视频做预训练再迁移到机器人本体，是绕开这一瓶颈的主流思路，难点则转移到“想象出来的身体”与真实本体之间的差距上，尤其是精细操作还剩多少可迁移性。这条现在更像方法论进展，离可部署还有距离，但方向上的取舍值得记住。

> 原文：[The Decoder](https://the-decoder.com/nvidias-model-gr00t-2-watches-humans-on-video-then-imagines-itself-as-the-robot/)

六条发布里，没有一条在比谁更聪明，全在比谁更便宜、分工更细、更能上线。留给读者的问题：当同一家公司的模型分成两档安全策略来卖，你的验收标准该怎么写？