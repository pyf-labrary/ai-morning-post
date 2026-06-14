# GPT-5.5上Bedrock，GLM-5.2抢眼

今天是模型厂商集中出牌的一天：OpenAI将GPT-5.5与Codex模型直接挂在Amazon Bedrock上，企业调用门槛骤降；智谱AI的GLM-5.2在Hacker News刷屏，性能提升显著。同时微软、Google在垂直领域（物体计数、text-to-SQL）推出新模型，而1500美元训出的1B参数模型HRM则暗示了低成本训练的可行性。模型生态正在从“比谁大”过渡到“比谁稳、谁专、谁省”。

## GPT-5.5 和 Codex 上线 Bedrock，AWS 用户可直调

OpenAI的GPT-5.5与代码生成模型Codex已正式通过Amazon Bedrock提供服务。企业用户无需自己部署推理集群，即可在AWS生态内直接调用API。关键点在于：这是OpenAI首次将旗舰模型（而非小模型或老旧版本）深度绑定到第三方云平台，意味着模型分发模式正向“云原生+托管”加速转移。对企业而言，合规、延迟、成本控制都更灵活。对AWS来说，增加了对抗Azure + OpenAI联盟的筹码。

> 原文：https://www.infoq.cn/article/FuhAEYbk8T0b0GQZyq4c

## GLM 5.2 发布，Hacker News 热度超过700

智谱AI今日正式发布GLM-5.2，该模型在多项基准测试（包括MMLU、C-Eval、HumanEval等）上表现强劲，具体提升幅度尚未完全公开，但已引发Hacker News社区超过700点的讨论热度。为何重要：国产大模型与GPT-4级模型的距离在缩小，GLM-5.2可能是目前国内首个在通用推理与代码能力上同时接近GPT-5.5水平的开源模型。对技术选型者而言，又多了一个高性价比选项。

> 原文：https://twitter.com/jietang/status/2065784751345287314

## Count Anything：专精物体计数的AI模型

微软研究院与外部合作者推出Count Anything模型，专门针对图像中任意物体的精确计数任务。传统目标检测模型（如YOLO、SAM）能识别物体但计数精度有限，而Count Anything通过新的视觉-语言对齐策略，将计数任务转化为类似“小样本回归”问题，显著提升了复杂场景下的计数准确性。为什么值得关注：工业场景中（库存盘点、细胞计数、交通流量）计数是刚需，此前缺乏专用模型，这个小而精的方向可能被低估。

> 原文：https://the-decoder.com/new-ai-model-called-count-anything-does-exactly-what-it-says-and-thats-harder-than-it-sounds/

## Gemini-SQL2 大幅领先 text-to-SQL 基准

Google Research发布Gemini-SQL2，在Spider、WikiSQL等主流text-to-SQL基准测试上以显著优势刷新纪录。该模型的创新在于引入了“结构化思维链”（Structured Chain-of-Thought），将自然语言查询先映射为数据库Schema图，再逐步生成SQL。关键影响：text-to-SQL是自然语言与数据库交互的瓶颈，Gemini-SQL2若落地，将大幅降低非技术人员使用SQL的门槛，对数据分析平台和BI工具带来直接冲击。

> 原文：https://the-decoder.com/google-researchs-gemini-sql2-tops-text-to-sql-benchmarks-by-a-wide-margin/

## 里约城市AI模型被质疑为“套壳”合并

巴西里约热内卢市政府发布的Rio3.5模型在部分基准上声称超越Qwen3.7，但开发者社区（GitHub issue）发现其权重文件与多个已有模型（如LLaMA、Qwen的分支）存在高度相似性，疑似将多个模型合并、微调后重新命名。该事件暴露了“城市AI”竞赛中的透明度问题。为什么重要：开源模型的可复现性正在被滥用，用户需要更严格的来源验证机制，否则类似争议会削弱整个社区的信任。

> 原文：https://github.com/nex-agi/Nex-N2/issues/4

## HRM：1500美元训练出1B参数模型，获HuggingFace CEO点赞

一篇技术文章披露，名为HRM（Hi-Res Model）的1B参数模型仅用1500美元预算完成训练（含数据和算力成本），在推理任务上达到与同规模模型相近的水平。该文获得HuggingFace CEO Clement Delangue的公开点赞。为何重要：1B参数模型是边缘端和云端轻量部署的黄金尺寸，1500美元成本意味着初创团队甚至个人都能负担模型研发。如果数据质量和训练策略得当，未来“微预算训模型”可能成为常态。

> 原文：https://www.qbitai.com/2026/06/435483.html

---

今日推送的六个模型/技术，覆盖了顶级大模型商业化、垂直领域突破、低成本实验和透明性争议。你可以从中看到三个信号：云端模型即服务成为主航道，中小参数模型的性价比正在飙升，而“套壳”争议则提醒行业——模型能力评估不能只看benchmark，更要看架构可信度。问题留给读者：当训练成本降到1500美元，你会选择自己训一个，还是继续调用API？