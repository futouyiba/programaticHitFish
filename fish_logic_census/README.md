# FCF Fish Logic Census

数什么：现实机制真正需要多少种 LogicTemplate（程序函数体族）——不是 Mode 数、不是 Story 数、不是 Program 实例数、更不是 Representation Schema 数。

- 方法合同：https://app.notion.com/p/3d7a4137d23681aa9640f14a997a9f23（Method R0）
- 执行合同：https://app.notion.com/p/3d7a4137d23681938302d08dcb0ba060（Orchestrator Prompt R2，Stage 隔离）
- 输入：FR campaign 冻结故事（FR3-passed，Story DB 只读）
- 关键纪律：盲重建（骨架先冻结再开 registry）、四态判同、族完整性、负知识保存
- 权威文件：template_registry.yaml / resolver_registry.yaml / discovery_curve.csv / batches/*/
- 停止：每批止于 INDEPENDENT_REVIEW_REQUIRED；饱和只能报 SATURATION_SIGNAL，由 Review/Gate 裁决

## discovery_curve.csv 列语义（计数基，F-6）

- `n_stories_consumed` = 去重 story 数（同一 story 的多面程序不重复计；**rerun/修复轮新增的面级程序只进 `n_sketches`**——REV-001-PATCH-001 F1 口径，与 B5 行 52 story/104 sketch 同构）
- `n_merge_confident` = merge_tests.jsonl 中语义裁决为 MERGE_CONFIDENT 的**条数**（program×template 对级，含修复轮补录；非族数、非程序数）
- `n_extension_candidate` = 同上**条数**级（同一 extend-vs-split 判例的多个成员程序各计一条）
- `n_new_template_candidate` = 本批新立候选**族数**（registry template 级）
- `n_ambiguous` = 程序级 AMBIGUOUS 数
- `ΔL_group/bake/response/quality` = 本批 registry 新增该 surface 候选族数
- `n_sketches` = 盲冻结程序数 + 修复轮补录程序数（两者分记于 batch manifest 的 blind_freeze 与 fix_rounds）

## 修复轮（FIX round）补录程序落位约定（REV-001-PATCH-001 F2）

存在两种合法落位，按修复对象选其一并在 manifest fix_round 节声明：
1. **不进盲文件**（B0-FIX-001 先例）：修复仅涉既有程序的登记/叙事——补录进 programs/merge_tests，blind_programs.jsonl 不动。
2. **append + 标记**（RS1-REV-001 先例）：修复需新增程序体（如面级补录）——追加进 blind_programs.jsonl，逐条 `registry_seen_at_creation=true` + fix_round 标记 + program_revisions 留痕；**禁止改写既有冻结行**（append-only + hash 守恒）。

角色：FCF-CENSUS-WORKER（持久 tab，Registry Segment B）。
