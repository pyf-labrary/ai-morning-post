# Copilot漏洞窃取2FA，AI助手安全风险凸显

今日晨报聚焦三件事：Copilot 全新漏洞被用于窃取用户二因素认证码，AI 助手的安全边界再次被拷问；Anthropic 紧急暂停 Claude Agent SDK 的 Token 计费改革，上下游博弈暗流涌动；Meta 推出 Facebook AI Mode，平台数据聚合的野心浮出水面。产品迭代加速，但安全与定价才是下半年 AI 行业的主线。

## Copilot 漏洞遭利用，可窃取用户 2FA 验证码

SearchLeak 攻击利用 Copilot 安全缺陷，黑客可通过精心构造的提示词，诱使 Copilot 返回用户浏览器中缓存的二因素认证码。关键点在于该漏洞不依赖传统网络钓鱼，而是利用 AI 对系统权限的“过度信任”。为什么重要：当 AI 助手深度集成浏览器、邮件等权限后，传统基于隔离的安全模型失效。开发者需重新评估 AI 代理的权限边界。

> 原文：https://arstechnica.com/security/2026/06/critical-copilot-vulnerability-allowed-hackers-to-seal-2fa-code-from-users/

## Meta 推出 Facebook AI Mode，聚合旗下平台公开数据

Facebook 新 AI 模式直接从 Instagram、WhatsApp 等 Meta 旗下平台读取公开信息，为用户提供个性化助手。关键点在于 Meta 不再仅依赖 Facebook 单一数据源，而是构建跨平台知识图谱。为什么重要：这意味着 AI 助手竞争从模型能力转向数据网络的广度与深度，Meta 拥有其他玩家无法复制的社交数据护城河。

> 原文：https://techcrunch.com/2026/06/15/metas-new-ai-mode-on-facebook-pulls-from-public-info-across-its-platforms/

## Anthropic 暂停 Claude Agent SDK 的 Token 计费改革

Anthropic 原计划周一生效的基于 Token 计费方案被暂停，此前曾引发高用量客户成本暴涨的担忧。关键点在于暂停而非取消，反映 Anthropic 在模型定价与市场接受度之间的摇摆。为什么重要：AI agent 的计费模式尚未成熟——按 token 还是按任务收费，直接影响企业客户的采用成本。

> 原文：https://arstechnica.com/ai/2026/06/anthropic-pauses-token-based-billing-for-its-claude-agent-sdk/

## Android 17 正式发布，深度集成 Gemini AI

Google 发布 Android 17，带来全新的多任务工具和 Gemini 能力扩展，同时推出 Pixel Drop 更新。关键点是 Gemini 不再仅作为独立应用，而是嵌入系统级交互。为什么重要：AI 从插件进化为操作系统底层能力，将推动应用层开发的范式转变。

> 原文：https://techcrunch.com/2026/06/16/android-17-launches-with-new-multitasking-tools-as-google-expands-gemini-features/

## Copilot Cowork 改用按用量计费，或接入 DeepSeek

Microsoft 调整 Copilot Cowork 计费模式，从固定订阅转向按用量计费，并考虑引入 DeepSeek 模型作为备选。关键点在于这一变化可能为了应对客户对价格柔性的要求，同时引入多模型选择增加竞争力。为什么重要：Microsoft 在 AI 定价上的调整往往是行业风向标，按用量计费可能成为企业级 AI 服务的标准模式。

> 原文：https://the-decoder.com/microsofts-copilot-cowork-moves-to-usage-based-billing-and-may-tap-deepseek/

## Plaud AI 记事本软件业务 ARR 超 1 亿美元

Plaud 宣布已出货超过 200 万 AI 记事本，软件年经常性收入突破 1 亿。关键点在于硬件是引子，订阅才是利润中心。为什么重要：这验证了“AI 硬件+软件订阅”模式在消费级市场的可行性，为其他 AI 硬件创业公司提供了参考路径。

> 原文：https://techcrunch.com/2026/06/16/plaud-says-its-software-business-topped-100m-in-arr-after-shipping-over-2m-ai-notetakers/

## NVIDIA XR AI 公测，驱动 AR 眼镜多模态代理

NVIDIA 发布 XR AI 框架公测版，允许开发者构建适用于 AR 眼镜和 XR 设备的多模态 AI agent。关键点在于该框架结合了视觉、语音和环境理解。为什么重要：AR 眼镜是 AI 代理的下一个理想载体，NVIDIA 试图从底层工具链切入，抢占生态主导权。

> 原文：https://blogs.nvidia.com/blog/nvidia-xr-ai/

## 鸿蒙小艺 AI 助手新升级：会思考、能调度

华为鸿蒙小艺与朱广权同台说脱口秀，展示多元能力，AI 助手进入新阶段。关键点在于小艺被定位为“会思考、能调度”的系统级代理，而非简单语音助手。为什么重要：华为在受限生态中持续迭代 AI 代理，将推动其与鸿蒙设备的深度协同。

> 原文：https://www.qbitai.com/2026/06/435953.html

AI 产品竞赛正从模型参数转向安全、定价与生态整合。当漏洞、定价改革与数据聚合同步发生，你的产品在哪个维度做好了准备？