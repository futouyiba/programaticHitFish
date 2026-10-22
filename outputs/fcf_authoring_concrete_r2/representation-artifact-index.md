# Representation 具体化 Artifact Index

更新时间：2026-09-10

## Notion 文档

| 层级 | 文档 | 用途 | 地址 |
|---|---|---|---|
| Stress Test R1 | 4 Logic Surface Authoring Stress Test R1｜分群 / 烘焙 / 响应 / 品质选择 | GPT 对话版本的四面微调模板、分群表、烘焙表、Response 表、Quality 表与中文脚本样例；当前为 Working / Fast Design Lane，不是 Authority | https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3 |
| 原始十五案例 | 15 Case Authoring Visualization R0｜中文逻辑 + 配置表投影（Pre-Gate） | C01–C15 原始案例映射、Runtime Order、LogicTemplate、早期中文伪脚本与配置表投影；后续 R2 具体化附录也写在此页末尾 | https://app.notion.com/p/3d6a4137d236814ea872ed6305942594 |
| 案例映射 | 表达验证案例映射｜Pilot-A｜REP-R1｜C01–C15 | Frozen Story 到 Representation Case 的输入映射，不是完整配置实现 | https://app.notion.com/p/3d6a4137d2368151b762e50bc5ce6dfd |
| Representation Package | Representation Review Package | Pilot-A 的正式 Representation Review Package 与交付指针 | https://app.notion.com/p/3d6a4137d2368165b064dab4b0db8f60 |
| Design Gate | Representation Design Gate R1｜15 Case R1 语义裁决 | C06–C13 设计决策、路由收紧与后续具体化边界 | https://app.notion.com/p/3d6a4137d23681eab6cfd3a535a8938a |
| Hub | FCF Research Orchestration Hub R2 | A4/B4 状态、Frozen Set、Artifact Registry 与流程路由 | https://app.notion.com/p/3d6a4137d236814e9f35e6ae2a761927 |
| Authoring Hub | FCF Representation Authoring Hub R1｜四面模板与具体化样本集成入口 | FCF Simplified V0 分支下的 representation 协同入口、快速入口与归集治理规则 | https://app.notion.com/p/3d7a4137d236814c9bebe037709bd71b |
| Matrix | Representation Matrix R1｜按执行面 × 表达类型归集 | 按分群 / 烘焙 / 响应 / 品质选择和 PT / Config / Step Table / Narrow DSL 归集所有来源 | https://app.notion.com/p/3d7a4137d23681568a5ff2a6b531b319 |
| Compendium | Representation Working Compendium R1｜跨文档统一阅读稿与治理目录 | 按方法、案例、Breaker、Runtime 契约、Review 分章阅读 representation 材料；不复制来源正文 | https://app.notion.com/p/3d7a4137d23681c4a6a6e5ae9ff1683d |
| Bass 专项 | FCF Simplified V0｜Concrete Discussion Spec / 具体讨论规格 R1｜Largemouth Bass / 大口黑鲈 | 大口黑鲈早期具体化样本；作为历史 Working 来源纳入 Matrix，不直接作为当前 Canonical Projection | https://app.notion.com/p/3cda4137d236819198fecae3c69570b5 |
| Bass 机制基线 | 大口黑鲈｜Largemouth Bass | 大口黑鲈机制与行为来源；约束 Bass 专项 representation 的语义边界 | https://app.notion.com/p/3d6a4137d23681108cf8e4f4d5dff510 |

## 本地文件

根目录：`/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/`

| 版本/用途 | 文件 |
|---|---|
| R2 完整压缩包 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/FCF-Authoring-Concrete-R2.zip` |
| R2 完整中文文档 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/authoring-concrete-r2.md` |
| R2 图形化入口 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/index.html` |
| R2 表数据 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/tables.json` 与 `tables/*.csv` |
| R2 中文伪脚本 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/scripts.json` |
| R2 逐步结果 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/traces.json` |
| R2 PT/Table/Step Table/Narrow DSL 对比 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/representation-shootout-r3.md` |
| R2 成本账本 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/representation-cost-r3.md` |
| R2 等义/引用检查 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/representation-equivalence-r3.md` |
| R1 四面补齐包 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/four-surface-completion-r1.md` |
| R1 四面预检 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/outputs/fcf_authoring_concrete_r2/four_surface_preflight.json` |
| 原始十五案例速览 | `/Volumes/Mac DS - Data/SharedProjects/programaticHitFish/representation-pilot-a-overview.html` |

## 版本关系

- **R1（四面补齐）**：逐 Case × Surface 补齐 Group / Bake / Response / Quality 的输入、绑定、固定执行、中文脚本、Typed Result、边界；没有单独 ZIP，已纳入 R2 ZIP。
- **R2（具体化样本）**：在 R1 基础上展开实际字段、配置行、Profile、Predicate、TemplateStep、脚本、计算轨迹和复算器；这是当前最完整的本地具体化包。
- **Stress Test R1**：GPT 对话侧的独立四面压力测试和模板候选来源；不能直接覆盖 R2 的 Frozen Story 或把候选值提升为 Authority。
- **15 Case R0**：原始案例投影与历史追溯页；具体化内容不只在正文早期段落，也在该页末尾的 §25 R2 附录及 §30–§32 R1.1/预检记录。
- **Bass Concrete Spec R1**：确认存在大口黑鲈专门具体化文档；当前定位为历史 Working 样本，后续按 Matrix 拆回 Group / Bake / Response / Quality 四面再与 C01–C15 做同维度比较。
- **Representation Matrix R1**：新增的统一索引层；后续新增或修订 representation 时先登记 Matrix，再扩展具体来源页。
- **Representation Working Compendium R1**：新增的读者向汇总层；只组织章节和结论，不成为第二个可编辑 Source of Truth。
