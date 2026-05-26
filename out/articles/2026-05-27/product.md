# Copilot Cowork文件外泄，AI安全警钟再响

今日最值得关注的是微软Copilot Cowork的设计缺陷：安全公司发现其代理系统可无授权外泄用户文件。这并非孤例，而是AI agent快速落地时安全风险管理滞后的典型表现。其他看点：DuckDuckGo因用户逃离Google AI搜索安装量飙升30%，AWS正式上线MCP服务器，AI短剧出海订单预计暴增50倍——产品侧机会与风险并存。

## Microsoft Copilot Cowork存在文件外泄风险

安全公司PromptArmor披露，微软Copilot Cowork存在设计缺陷：恶意用户可通过特制提示词诱导代理系统，将目标用户的文件内容发送至外部服务器，实现无授权外泄。该漏洞根源在于代理执行逻辑未严格隔离用户上下文与系统权限，且缺乏针对代理行为的实时审计机制。对于已部署Copilot Cowork的企业，这意味着文件安全边界被意外突破。这一事件为所有集成AI代理的产品提了个醒——安全设计不能只关注模型输出，必须覆盖代理交互的每一个环节。

> 原文：[https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files](https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files)

## DuckDuckGo安装量飙升30%，用户逃离Google AI搜索

Google I/O后全面推行AI搜索，搜索结果摘要、对话式界面等特性引发部分用户反感。DuckDuckGo应用安装量环比激增30%，后者主打隐私保护和无AI干扰的搜索体验。这证明在AI普惠进程中，“不做AI”反而成为差异化卖点。对产品经理而言，这是一个信号：用户对AI的接受度并非普适，保留传统模式或提供“降级”选项可能成为获客策略。

> 原文：[https://techcrunch.com/2026/05/26/duckduckgo-installs-are-up-30-as-users-reject-being-force-fed-googles-ai-search/](https://techcrunch.com/2026/05/26/duckduckgo-installs-are-up-30-as-users-reject-being-force-fed-googles-ai-search/)

## AWS MCP服务器正式可用，支持IAM权限

AWS宣布MCP（模型上下文协议）服务器全面可用，允许AI代理通过标准API调用云资源，并内置IAM权限控制。这意味着开发者无需自建复杂的安全中间件，即可让AI agent安全操作S3、Lambda等服务。MCP作为Anthropic提出的开放协议，正被云厂商广泛采纳。对于使用AWS构建agentic产品的团队，这是降低集成成本和权限管理风险的关键一步。

> 原文：[https://www.infoq.cn/article/4gwXqyRPs4RTUIMpRte7?utm_source=rss&utm_medium=article](https://www.infoq.cn/article/4gwXqyRPs4RTUIMpRte7?utm_source=rss&utm_medium=article)

## AI短剧出海订单预计暴增50倍

受AI生成剧本、换脸、配音等技术驱动，面向海外市场的短剧定制需求爆发。目前成片产出同比增5倍，全年订单预计暴增50倍，单集收益比国内高出40%。AI降低了制作成本与语言转换门槛，让中小内容团队也能参与全球化分发。不过需注意版权风险与内容合规问题——海外平台的监管力度不亚于国内。

> 原文：[https://36kr.com/newsflashes/3826039643624064?f=rss](https://36kr.com/newsflashes/3826039643624064?f=rss)

## 阿里云发布海外AI产品官网Qwen Cloud

阿里云在新加坡推出Qwen Cloud官网，集中展示通义千问系列模型、AI Agent产品MuleRun以及编程辅助平台Qoder。此举意味着阿里云不再仅靠API接口服务海外，而是构建了从模型到工具链的全栈产品矩阵。对出海企业而言，多了可选的供应商；对阿里云来说，这是对抗AWS、Azure在AI云市场扩张的明确信号。

> 原文：[https://www.leiphone.com/category/industrynews/iIAnVv3C91pE50QK.html](https://www.leiphone.com/category/industrynews/iIAnVv3C91pE50QK.html)

## Hugging Face发布3D打印人形腿项目

Hugging Face开源了一套3D打印人形机器人腿部设计，总成本约2500美元，包含电机、传动和控制器。项目旨在降低机器人实验的门槛，让更多开发者可以复现和改造行走算法。虽然这更偏向硬件，但结合Hugging Face的AI模型生态，可成为“具身智能”实验的入门平台。对于关注AI与机器人结合的产品团队，这是低成本获取实验硬件的机会。

> 原文：[https://arstechnica.com/ai/2026/05/3d-printable-humanoid-legs-let-robotics-experiments-run-wild/](https://arstechnica.com/ai/2026/05/3d-printable-humanoid-legs-let-robotics-experiments-run-wild/)

---

结语：AI产品的安全缺陷和用户反噬，正在成为比技术本身更紧迫的产品命题——你为Agent授权时，考虑过谁在控制“控制者”吗？