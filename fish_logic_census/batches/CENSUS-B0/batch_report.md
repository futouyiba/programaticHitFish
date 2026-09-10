# CENSUS-B0 Batch Report｜FISH-R05 五故事校准批

status: **INDEPENDENT_REVIEW_REQUIRED**
validate_batch: **PASS**（programs=13 stories=5 merge_tests=23）

## 输入与纪律

- 输入：FISH-R05 五条 FR3-passed 冻结 Story（湄公鲶/南美肺鱼/地图鱼/电鳗[仅感知段]/欧鲢[阴性对照]）+ P01/P04/P05/P06 冻结语义 Pattern（Frozen Input）。
- 盲纪律执行：13 条程序骨架先于 registry 开启冻结（`build_blind_programs.py` → `blind_programs.jsonl`，sha256 落盘，registry_seen=false），之后才运行判同（`run_merge_tests.py`）。零 post-registry 修改（program_revisions.jsonl 空）。初始化阶段对 v0 种子的暴露已在 role_memory 声明。
- 电鳗按 envelope 限定只重建感知段；攻击段（Attacker-Generated Opportunity）与捕获边界 OUT_OF_SCOPE 留痕。

## 核心结论

### Owner 边界判例（coordinator 三问）

1. **湄公鲶个体发生切换**：Group 面还是 Bake 面？——**都不是**。切换属 **lifecycle premise 层**（体型驱动的缓慢单调单向发育，同时刻单态，无并存互斥供给）：Group 无路由程序（P05 判例不购买）；Bake body 内无 IF-juvenile 分支（evaluator/patch 绑定随 premise 配置切换）。B0 程序证据：P-MGC-BAKE-ADULT 单 body、premise 记 binding。
2. **肺鱼蛰伏态**：incoming premise 还是 surface-owned 程序？——**premise**。干湿 regime 由 world 水文上游决定；蛰伏（钻泥/封泥/代谢下调）是 lifecycle-owned state switch + 行为产物（burrow_anchor fact）。与 FR3 语义判例（FishMode Weak→None）从程序体角度独立得出同结论。剩余问题：干态 playable 性（S10=EO）→ TAR-01，AMBIGUOUS 悬置不立族。
3. **地图鱼 Guard×Feeding 双 Path 程序体**：`EVAL_TARGET_AS_FOOD_TYPED ∥ EVAL_TARGET_AS_INTRUDER_TYPED → COMBINE_DUAL_PATH → DECIDE_RESPONSE`。guard_state 是 persistent condition premise（presentation 前已存在且持续，P04 语义）；双路径并行评估+合并是 Response 自有程序。立族 GUARD_CONFLICT_DUAL_PATH_RESPONSE（2 成员：地图鱼 canonical + 肺鱼雄护直验同构）。envelope 所引「Method §9.2 Brown Trout 判例」文本未见 → TAR-04（本重建未依赖它，独立成立；若判例存在且口径不同需复核）。

### Census 产出（registry v0→v1）

| 族（surface） | 成员 | 状态 |
|---|---|---|
| CONSTRAINED_RELATIVE_REFUGE（Bake，v0 种子） | +0；B0 Bake 程序判同 = 5 non-match + 1 AMBIGUOUS（LUN-AESTIVATION playable 未决，不计 non-match；F-3 勘误）；non-match 判别结构 RelativeRank(reference_set=FeasibleSet) 缺失 → 反向增强其判别力 | CANDIDATE 不变 |
| PLAIN_FACTOR_COMBINE（Bake）新 | OSC、CHB | CANDIDATE（HRQ-01） |
| HARD_GATED_FACTOR_COMBINE（Bake）新 | LUN-WET、EEL（gate 均为专性气呼吸的水面可达） | CANDIDATE（HRQ-02） |
| PATCH_RESOURCE_FOLLOWING（Bake）新 | MGC-ADULT（单成员 PROVISIONAL，与 P06 压缩测试联动） | CANDIDATE（HRQ-04） |
| TYPED_TARGET_RESPONSE（Response）新 | MGC/LUN/OSC/CHB/EEL-SENSE（5 成员；EEL 走 evaluator_channel 轴=EXPOSURE_ACCESS） | CANDIDATE（HRQ-05） |
| GUARD_CONFLICT_DUAL_PATH_RESPONSE（Response）新 | OSC-GUARD（canonical）、LUN-GUARD | CANDIDATE（HRQ-06） |

- **Extension 判例（HRQ-03）**：HARD_GATED↔PLAIN 差异=前置 hard gate（真结构差异，不可 MERGE）。extend（PLAIN 加 hard_constraint_gate: NONE|typed 轴）vs split（独立族）已做 Total Complexity Compare，recommended_shape=**HUMAN_DECISION**（worker 倾向 SPLIT：gate 是结构元素而非因子参数）。
- **阴性对照（欧鲢）成立**：Bake 与地图鱼在 factor_set 轴内直验同构、Response 为 TYPED 标准成员；体型分级落参数、洄游落 P05 配置级因子集切换；absence claim=NO_NEW_PROGRAM_CURRENT_EVIDENCE（限定 scope）。
- Discovery Curve B0 行：stories=5, sketches=13, merge_confident=12(语义层；engine 字面层 7), extension=2(同一判例两成员), new_template=5, ambiguous=1, **ΔL_group=0, ΔL_bake=3, ΔL_response=2, ΔL_quality=0**, ΔN_resolver=0, case_specific=0, full_expansion=0。

### 待 Human Review（human_review_queue.jsonl）

HRQ-01 PLAIN 族（factor_set 轴边界）｜HRQ-02 HARD_GATED 族｜HRQ-03 gate 轴 extend-vs-split（HUMAN_DECISION）｜HRQ-04 PATCH 族（P06 联动）｜HRQ-05 TYPED 族（evaluator_channel 轴；P01 两层登记）｜HRQ-06 DUAL_PATH 族（P04 两层登记）｜HRQ-07 因子槽间顺序 unordered 提案（ORDER 判定的适用边界）。

### TARGETED_AUDIT_REQUEST（现实/产品缺口，回 FR 线，不自己补证据）

- **TAR-01**（肺鱼）：干季蛰伏是否进 playable scope（S10=EO）？若进：anchor-Bake 退化体与响应抑制需 targeted audit + 可能 full expansion；若不进：LUN-AESTIVATION 永久 AMBIGUOUS 归档。
- **TAR-02**（湄公鲶）：幼体（肉食期）空间/响应程序证据缺失；stocked 湖 playable 尺寸段内幼体是否可达？
- **TAR-03**（地图鱼）：护巢期钓法效应（S10=EO）——不影响结构裁决，影响 DUAL_PATH 族的验证用例。
- **TAR-04**（方法引用）：envelope 所引「Method §9.2 Brown Trout 判例」在 Method R0 页未见对应编号内容；请提供指针或确认指 Representations 关系节，以便校准 DUAL_PATH 判例口径。

### 复杂度守恒

n_case_specific_resolvers=0；COMPLEXITY_LAUNDERING_RISK=NO（gate 留在 Bake body、双路径留在 Response body、无 case-specific helper 升族）。

## 产物清单（fish_logic_census/batches/CENSUS-B0/）

manifest.yaml｜stories.jsonl｜blind_programs.jsonl（13，hash 冻结）｜programs.jsonl（15）｜merge_tests.jsonl（25）｜resolver_tests.jsonl｜absence_claims.jsonl｜human_review_queue.jsonl（7）｜coverage.jsonl（空：FR3 已冻结，census 不重做）｜program_revisions.jsonl（2：FIX-001 补录留痕）｜engine_report.json｜build_blind_programs.py｜run_merge_tests.py｜build_census_outputs.py｜apply_fix_001.py｜worker_self_qa.md｜batch_report.md
仓库级：template_registry.yaml v2｜discovery_curve.csv +B0 行。git 未 commit（按 envelope，coordinator 收尾）。

## 修复轮附录｜CENSUS-B0-FIX-001（2026-09-10）

驱动：独立审 CENSUS-B0-REV-001 REVISE。修复后 validate_batch PASS（programs=15 stories=5 merge_tests=25）。

- **F-1（blocker，选 a 补 sketch）**：EEL S6 泡沫巢雄护 → P-EEL-RESP-GUARD（DUAL_PATH 第三成员，engine 直验无字面差异，intruder_evaluator_context=foam_nest 入轴）；S9 幼成切换 → P-EEL-RESP-FEEDING（TYPED 族 evaluator_binding 第二 premise 实例，首个=MGC）。两程序为修复轮**非盲**补录（registry_seen_at_creation=true，程序形状自冻结 Story 证据重建、fit 风险由 provenance 声明并交 reviewer 复检）；program_revisions.jsonl 留痕。
- **F-2（blocker）**：MGC ResponseChannel FieldFeeding（幼体肉食期）按 TYPED 族 evaluator_channel/binding 轴 premise 实例处理（语义层 P0x 对应指针待确认——coordinator 修复信中「P03 轴」未核实，census 侧不引用未读 pattern）；potamodromous 洄游照 CHB 先例按 P05 配置级处理。
- **F-3**：计数勘误「六个 non-match」→「5 non-match + 1 AMBIGUOUS」（LUN-AESTIVATION 不得被散文升格）。
- **F-4**：六族补 helper_dependencies / resolver_dependencies 显式字段（PATCH 带 SubstrateResourcePatchEvaluator，余为空列表）。
- **F-5**：HRQ-06 补双路径槽间顺序 unordered 提案（与 HRQ-07 同判例族）。
- **F-6**：README 补 discovery_curve 列语义与计数基。
- **F-8**：build_blind_programs.py docstring generated_at 笔误勘误。
- **F-9**：HRQ-06 补 caveat：LUN/EEL→P04 对应为 census 新增跨层映射（FR 冻结 patterns 分别仅 P05 / 空），未经 FR3 语义侧确认。
- 计数更新：n_sketches 13→15、n_merge_confident 12→14；族数不变（DUAL 3 成员、TYPED 6 成员）；registry v1→v2。

BATCH_ID: CENSUS-B0-FIX-001
