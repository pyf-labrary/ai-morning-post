# 首个“关键”安全级模型来了

OpenAI 预告 Astra 成为首个达到其准备框架“关键”网络安全能力阈值的模型。模型能自主发现并利用未知漏洞，同时也意味着安全风险等级的跃升。今天模型发布的焦点，不只是更强的能力，还有能力分级、开放边界与成本竞争。

## OpenAI 预告 Astra：首个“关键”安全级网络模型

OpenAI 发布 Astra 前预告，称其将成为首个达到公司准备框架中所谓“关键”网络安全能力阈值的模型。该模型能够自主发现并利用未知漏洞，能力显著超过此前版本。

为控制风险，OpenAI 将限制 Astra 的访问范围，仅向合作伙伴提前开放，并在正式发布前持续评估。官方未披露具体发布日期。

这标志着前沿模型安全分级从概念走向实操：当模型具备自主挖掘漏洞的能力时，单点攻击的门槛大幅下降，应对策略也从“事后修补”转向“提前设限”。

> 原文：[OpenAI](https://openai.com/index/path-to-astra)

## Anthropic 发布 Claude Fable 5.1：降价与减限

Anthropic 推出 Claude Fable 5.1，已上线 API 与主要云平台。模型在编程和研究任务上的能力有所提升，token 成本最高下降 45%，限制性拦截也更少。

Fable 5.1 与受限版本 Mythos 5.1 并行存在，说明 Anthropic 在追求更开放的应用场景的同时，仍保留对高风险用途的约束。降价叠加减限，面向开发者与企业的吸引力明显增强，也是 Anthropic 在商业化和模型安全之间走出的新平衡。

> 原文：[TechCrunch](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/)

## 谷歌 Gemini 引入智能体式视频理解

DeepMind 为 Gemini 新增 agentic video understanding 能力，模型不再只是“看”视频，还能对视频内容进行智能体式理解与操作，比如定位关键帧、追踪对象状态并执行后续动作。

这项能力扩展了多模态 agent 的边界：视频从训练素材变成实时交互界面，模型可以基于动态画面做出决策。对机器人、自动驾驶、内容审查等场景，这可能是基础能力的又一次前移。

> 原文：[DeepMind](https://deepmind.google/blog/introducing-agentic-video-in-gemini/)

## MiniMax H3 Max Live 上线：视频生成快过播放

Fal 平台上线 MiniMax 的 H3 Max Live，视频生成速度突破实时门槛，生成速度比播放速度更快。MiniMax 借此打开 AI 视频实时生成的可能性——从离线渲染转向即时交互。

如果生成质量能够匹配速度，直播、游戏、虚拟社交等场景将直接受益。实时视频生成是通往“视频版 ChatGPT”的关键一步，但算力成本与产品形态仍是商业化翻越的门槛。

> 原文：[Latent Space](https://www.latent.space/p/ainews-fals-h3-max-live-breaks-the)

## DeepSeek V4 多模态开源，Harness 框架同步更新

雷锋网拆解显示，DeepSeek V4 系列开源多模态模型，并同步更新了 Harness 开源框架，后者围绕后训练与代理自进化展开。

多模态开源加上自进化框架，意味着社区可以基于 DeepSeek V4 构建更复杂的 agentic 工作流，而不只是单向调用模型。开源模型的能力重心正从“更强的回答”转向“更自主的闭环”。

> 原文：[雷锋网](https://www.leiphone.com/category/yanxishe/dufRSsU0sr3hCOII.html)

## 阿里开源 Qwen3.8-27B，登顶开源榜但 Agent 适配待补

阿里开源 Qwen3.8-27B 后登顶全球开源模型榜。该模型实测性能表现强劲，然而 Agent 适配仍有短板，工具调用与任务拆解的能力需要社区补课。

基准登顶与实用落地之间存在差距。对开发者来说，模型参数再强，缺乏成熟的 agent 生态支撑，依然是“木桶短板”；对阿里来说，开源策略的下一步重心或许不在模型本身，而在工具链。

> 原文：[雷锋网](https://www.leiphone.com/category/yanxishe/jjqYW7SvQ8B6BH2u.html)

## Google 发布 TimesFM-3：330M 参数的时序预测基础模型

Google Research 发布 330M 参数的 TimesFM-3，零样本支持多变量时间序列预测，一次前向即可对多条相关序列进行预测。

时序预测是金融、供应链、能源等领域的高频需求，但传统模型往往需要定制训练。TimesFM-3 走基础模型路线，有望把多变量预测变成开箱即用的通用能力，对中小团队尤其友好。

> 原文：[MarkTechPost](https://www.marktechpost.com/2026/08/31/google-ai-releases-timesfm-3-a-330m-parameter-zero-shot-foundation-model-for-multivariate-time-series-forecasting/)

当安全能力突破“关键”阈值，AI 边界不再只由基准分数定义，而由使用权定义。你会先把哪项能力放进生产环境，又会对哪一项保持谨慎？