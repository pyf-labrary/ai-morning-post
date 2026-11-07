# 开放权重扎堆，视频生成降价三成

今天这个板块最值得看的不是某一个模型，而是同一时间发生的两件事：谷歌把 720p 视频生成降到每秒 0.07 美元，比原来便宜 30%；同时，从 Thinking Machines Lab 到百度、再到 Ripple，开放权重的旗舰模型一次发布三个。价格战从文本模型转向视频，参数规模战则在开放权重阵营中继续升温。对做产品的人来说，今天的信号是：可以默认“便宜”会持续，但“选哪个模型”会变得更难。

## Gemini Omni 1.2 Flash：视频按秒算钱

谷歌 DeepMind 发布 Gemini Omni 1.2 Flash，核心能力是原生 15 秒视频生成和多轮对话式编辑，同时把 720p 视频价格下调 30%，至每秒 0.07 美元。

多轮对话式编辑是这次比较容易被低估的一点。一次性生成一段视频，改变的是创作方式；但反复对话修改，改变的是成本结构：一段成片的成本不再等于一次调用，而是等于十几次迭代。这也解释了为什么降价要和能力同批发布——按秒计价的模型，如果单价不降，编辑器式的工作流根本跑不起来。

对下游应用的含义比较直接：视频生成开始进入“可以浪费几次”的价格区间，产品设计可以假设用户会反复重生成，而不必用配额把用户拦住。

> 原文：[Google DeepMind](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/)

## GPT-6 Cyber：攻防一体的发布时机

OpenAI 推出网络安全模型 GPT-6 Cyber，特点是双向能力：既能尝试突破系统，也能给出修复建议。

放在这个时间点看，发布本身和模型能力同样重要。AI 实验室的网络安全能力正受到更严格审视，而这类模型最难处理的地方恰在于它无法只做防守——同一个能力，攻与防是同一套权重。OpenAI 选择把修复建议作为产品叙事的一部分，等于承认了这一点，并试图把讨论从“会不会被滥用”引向“能不能用于加固”。

接下来值得观察的不是榜单，而是采购侧：企业安全团队会不会接受一个同时具备攻击能力的模型进入自己的内网，这决定这类模型的商业形态。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/)

## Inkling 2 Small：594B 参数，68 小时训完

Thinking Machines Lab 发布 Inkling 2 Small，594B 参数 MoE、17B 激活参数，在 68 小时内用 12T token 训练完成，并计划以 Apache 2.0 开放权重。

三个数字里，最有信息量的其实是训练时长：68 小时。它把“训练一个前沿规模模型需要多久”这个以往只存在于内部文档里的量级，摆到了公开叙述中。594B 总参数、17B 激活的稀疏结构，也说明大厂之外做 MoE 已经是一条成熟路径，不再是工程奇迹。

计划用 Apache 2.0 开放权重，则把它直接放进西方开放权重模型的头部竞争里。需要留意的是“计划”二字——权重真正落地前，许可条款和实际可复现性都还有变数。

> 原文：[The Decoder](https://the-decoder.com/thinking-machines-inkling-2-small-claims-top-spot-among-western-open-weight-models/)

## 百度开源 ERNIE 5.5 Flash Base：开源的是“基础”

百度发布 ERNIE 5.5 Flash Base，280B 稀疏 MoE、14B 激活参数，在 33.5T token 上训练，并在中期训练（mid-training）和后训练之前就开源了基础模型。

这条的关键在于开源发生在哪个阶段。多数“开源模型”交出来的是已经做完对齐的成品，用起来顺，但很难改动；ERNIE 5.5 Flash Base 交的是底座，下游团队要自己做后训练。对有能力做领域数据的研究者和企业，这比一个开箱即用的对话模型价值更高；对只想调 API 的团队，则几乎用不上。

把基础模型而非成品开源，是一种明确的选择：换取生态与研究影响力，而不是换取直接的开发者调用量。

> 原文：[The Decoder](https://the-decoder.com/baidu-releases-ernie-5-5-flash-base-with-280-billion-parameters-as-an-open-source-foundation-model/)

## Ripple-65B Preview：许可干净比参数更重要

Ripple-65B Preview 以完全 Apache 2.0 许可发布，定位为美国开源模型，并在智能体编程（agentic coding）任务上给出了较强结果。

65B 在今天不算大，但“完全 Apache 2.0”这个定语值得单独拎出来。开放权重模型的实际可用性，长期被各种附加条款卡住——商用限制、用户量门槛、署名要求。许可干净意味着法务可以直接放行，这在小模型上往往比多几十 B 参数更能决定采用率。

agentic coding 的定位也很实际：这是目前最容易产生付费意愿、同时对模型规模要求相对可控的场景。

> 原文：[The Decoder](https://the-decoder.com/ripple-65b-preview-delivers-strong-agentic-coding-results-as-a-fully-apache-2-0-open-us-model/)

## NVIDIA Cosmos 3：为具身智能补数据

NVIDIA 在 Hugging Face 发布 Cosmos 3 系列开放模型，面向交互式世界模拟，帮助开发者构建和测试具身（embodied）与仿真场景。

卖算力的公司开源仿真模型，逻辑并不复杂：机器人缺的是数据，而数据缺的是能大规模生成和验证环境的工具。世界模拟模型越开放，愿意做具身智能的团队就越多，对训练和推理算力的需求也越大。

短期看，这类模型的使用者是研究与仿真团队，不是普通应用开发者；但从卡位角度，它补的是整条链路上最薄的一环。

> 原文：[Hugging Face](https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation)

## Underdog 的 32MB 语音模型：端侧的另一种答案

Underdog 演示了一个仅 32MB 的语音模型，体积很小，但可同时生成语音和音乐。

在动辄几百 B 参数的一周里，32MB 是个反向指标，但它指向的问题很真实：不是所有语音能力都需要走 API。端侧、离线、低延迟的场景——耳机、车机、玩具、无障碍工具——对模型体积的敏感度远高于对音质上限的敏感度。

一个模型同时覆盖语音与音乐，也意味着编解码和生成范式的复用。它未必会成为产品，但会持续挤压“小任务也要调大模型”的惯性。

> 原文：[TechCrunch](https://techcrunch.com/2026/11/06/underdog-shows-off-a-32mb-speech-model-in-new-demo/)

今天的发布里，一半在比谁更开放，一半在比谁更便宜，方向都很清楚。倒是留一个问题：你手上那个场景，真的需要 594B 吗？