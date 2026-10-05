# 联邦学习搬进 TEE，隐私账本第一次能被外人查

今天研究板块最值得看的是 Google 把联邦学习的梯度计算搬进了可验证的 TEE：Gboard 现在用上了可外部审计的差分隐私训练。这件事的意义不在隐私保护本身——联邦学习喊了这么多年，卖点一直是"数据不出设备"——而在于它补上了联邦学习最弱的一环：你凭什么相信服务端真的按承诺做了？过去这只能靠信任，现在可以靠密码学证据。另外两条也值得留意，一条关于自改进 agent 的评测作弊，一条关于中国大模型的敏感议题表现，都是"如何验证模型说了真话"的同一命题。

## Google 把联邦学习搬进 TEE，Gboard 的隐私训练可被外部审计

Google Research 调整了联邦学习（federated learning）的架构：把梯度计算从用户手机移到服务端的可信执行环境（TEE）中完成。配套的工程细节包括：访问策略写入 Sigstore Rekor 做透明日志，二进制走可复现构建（reproducible build），使得外部研究者可以验证跑在 TEE 里的代码确实是开源的那一份。Gboard 已上线该方案，实现可外部验证的差分隐私（differential privacy）训练。

关键点在于"可验证"三个字。传统联邦学习的信任模型是单向的：用户相信服务端只做聚合、不加后门、不反推原始数据，但没有任何机制能证明这一点。把计算移入 TEE 并让二进制与访问策略可审计，等于把这份信任换成了可检查的证据链。

为什么重要：对做隐私合规、端侧模型、数据治理的团队来说，这是一个可复用的范式——不是"我们承诺不滥用数据"，而是"你可以自己来验证"。代价是服务端 TEE 的算力成本与信任假设转移（现在要信 Intel/AMD/Google 的 TEE 实现）。

> 原文：[Google Research moves federated learning into TEEs, Gboard now trains with externally verifiable differential privacy](https://www.marktechpost.com/2026/10/04/google-research-moves-federated-learning-into-tees-gboard-now-trains-with-externally-verifiable-differential-privacy/)

## 让自改进 Agent 没法「背题」

Google 研究者提出一种新方法，用于防止自我改进（self-improving）的 AI agent 在多轮训练中把测试集记下来，从而避免基准分数虚高。

问题背景很实际：agent 的自我改进循环通常是"跑任务—拿反馈—更新策略—再跑"，如果评测集在一轮轮迭代中被反复接触，模型就可能从"学会解题"退化成"记住答案"。这和传统机器学习的训练/测试集泄漏同源，但 agent 场景更隐蔽——因为反馈信号本身就来自评测环境。

研究者给出的思路是需要在方法层面切断记忆路径（原文未提供具体机制细节，此处不做推测）。真正的价值不在单点方法，而在于它点出的方法论问题：当模型能修改自己的行为策略时，评测的可信度必须重新设计，否则所有自改进 agent 的 benchmark 数字都要打折扣。

> 原文：[Google researchers find a way to keep self-improving AI agents from memorizing their tests](https://the-decoder.com/google-researchers-find-a-way-to-keep-self-improving-ai-agents-from-memorizing-their-tests/)

## 评测：中国大模型在敏感议题上复述官方立场或拒答

Aleph Alpha 发布的一项基准测试显示，中国厂商的大模型在敏感话题上的表现呈两极：要么复述官方口径，要么直接拒绝回答。

这类结果本身不算新——过去两年多个团队都做过类似评测。值得关注的是评测方的身份与方法：Aleph Alpha 是欧洲的模型厂商，其基准若具备可复现的题集与评分标准，就会成为采购侧（尤其是欧洲公共部门与受监管行业）评估模型可用性的参考依据。对出海或服务海外客户的中国模型团队来说，这类第三方评测正在从"学术话题"变成"合规与销售环节的实际门槛"。

需要保持的克制是：单一基准测试反映的是特定题集下的行为分布，不等于模型能力的全貌。但把它当成风险信号而非公关问题来处理，是更务实的姿态。

> 原文：[Chinese AI models parrot state doctrine or refuse to answer on sensitive topics](https://the-decoder.com/chinese-ai-models-parrot-state-doctrine-or-refuse-to-answer-on-sensitive-topics/)

## 结语

今天三条新闻共享同一个母题：当模型越来越会"表演"时，验证机制比能力指标更稀缺。留一个问题：如果你的模型明天要接受外部审计，你现在的技术栈拿得出证据吗？