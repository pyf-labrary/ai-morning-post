# Codex 开源技能目录，谷歌补上 Agent 安全闭环

今天最值得看的不是新模型，而是两家公司不约而同把 Agent 能力组件化：OpenAI 开源 Codex 技能目录（Skills Catalog）与插件示例，谷歌开源 Mantis，让编程 Agent 自己挖洞、复现并修复漏洞。信号很直接：编码 Agent 的竞争焦点，正在从模型能力转向工具生态与安全可信度。如果你还在纠结下一个 base model，不如先读读这两个仓库的接口设计——它们正在定义 Agent 工具链的默认写法。

## Codex 技能目录开源，Agent 长尾能力开始标准化

**是什么**：OpenAI 在 GitHub 公开了官方技能目录（Skills Catalog）与插件示例仓库。其思路是把编码 Agent 的某项能力——例如代码评审、构建执行、外部工具调用——打包成