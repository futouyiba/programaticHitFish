# FCF Authoring 具体化样本 R2

先打开 [图形化阅读页](index.html)。搜索 C08、C12、BASS 或 Q3，左侧可展开每张配置表的全部相关行，右侧是等义中文伪脚本和实际计算结果。

- [完整中文文档](authoring-concrete-r2.md)：12 份表的全列、字段合同、全局样例行、逐案例脚本、输入与中间结果。
- `tables/`：11 张作者数据表 + 1 张只读模板目录，共 12 个 CSV 文件。
- [完整表数据](tables.json)、[全部中文伪脚本](scripts.json)、[27 个唯一案例/情景](cases.json)、[逐步结果](traces.json)。
- [复算记录](verification.json)：38 项通过。
- [独立审查](independent-review.md)：保留首轮 ARTIFACT_REVISE 和修订后的 ARTIFACT_APPROVE；批准范围为本次完整 R2 bundle。
- [四路表达成本账本](representation-cost-r3.md)：量化同一修改在 PT / Table / Step Table / Narrow DSL 中要改的单元、行和步骤；[独立审查](cost-independent-review.md)最终为 ARTIFACT_APPROVE。
- [Notion 原文档](https://app.notion.com/p/3d6a4137d236814ea872ed6305942594)：末尾 §25 为本次具体化附录，含完整表、脚本和独立审核记录。历史投影保留。

本轮共 38 个 Binding、27 个案例/情景记录，覆盖 C01–C15 的范围处理、G1–G3、Q1–Q3 和鲈鱼五群及其 Group Routing。

所有演示阈值、曲线、乘数、候选聚合均已明确标识。它们用来使样本能完整填写和复算，不是生产参数冻结。结果仍为 WORKING / PRE-GATE，未决定最终 Config Table / DSL 选型，未 Promote。

HTML 的手机/桌面显示、案例筛选、搜索、左右视图切换和表格展开已验证。复算器没有实现独立 DSL 解析器，也没有验证生产系统的 Root 幂等；不能把样本通过扩大成这两项已完成。

- [四面补齐包 R1.1](four-surface-completion-r1.md)：C01–C15 的 Group / Bake / Response / Quality 逐 Case×Surface 投影。

- [四面覆盖 Preflight](four_surface_preflight.py)：检查 C01–C15 的 60 个 Case×Surface 单元。

- [Current State Snapshot](current-state-snapshot.md)：Gate、覆盖、审核、结论和 TODO。
- [Representation Artifact Index](representation-artifact-index.md)：Notion 页面、R1/R2 版本关系与全部本地路径索引。
