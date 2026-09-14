# HRQ-MUTATION-001 批报告（registry v8→v9 裁决执行批）

- **批型**：HRQ_ADJUDICATION_EXECUTION（registry mutation 批——非普查批：无冻结 Story/无新盲程序/无新判同；盲纪律不适用）
- **授权**：fish_logic_census/hrq_decision_log.md @ commit b5088ab（HRQ-ADJUDICATION-2026-09-11：七项裁决+两组语义裁定）。**本批零新增裁决**——逐条执行决策日志文末「mutation 批执行清单」，不超出清单范围。
- **执行器**：fcf-census-worker｜**停点**：INDEPENDENT_REVIEW_REQUIRED（mutation 不自我批准；独立审通过前不 push）
- **产物**：template_registry.yaml v9（36 处锚点断言替换，脚本 apply_hrq_mutation.py 幂等留档）+ truth_rebuild_queue.jsonl（248 行）+ 本批档

## 1. 逐条裁决→落表对照

| 裁决 | 决策日志裁定 | registry 落表 | 状态 |
|---|---|---|---|
| 1 SINGLE 族 | A：拆分+234 AMB 转真形重验队列 | SINGLE status→RETIRED+retired_provenance（v1 证伪注记：RS1 61/61+渐进累积语义+饱和伪影根因）；61 moved 成员转正 9 链族（原 66 条清单保留为历史快照层）；5 无文件成员 evidence_insufficient_held（LAM/PIN/ASR/RVS/RDS 归 FR 线）；234→queue | 落表 |
| 语义 1 渐进累积 | 无合并步；×0.01 软出局 | 9 链族+HARD_GATED v2+EXTREME_TEMP+PATCH_GATED_DUAL 共 12 个 Bake canonical 全部重写：NORMALIZE_WEIGHT/COMBINE_* 终步与 OPERATOR UNDEFINED 占位关闭，每步三档乘入 running weight；GATE 硬门 EARLY_RETURN 保留（门≠三档出局） | 落表 |
| 语义 2 措辞对齐 | 排除档=×0.01 非返回 0 | canonical 内「排除档=出局/EARLY_RETURN」全部对齐为 ×0.01 软出局；B 系列表达文件与 work standards §5.1 表述更新归文档线（registry 侧注记 ruling_to_mutation_map.semantic_2） | registry 侧落表 |
| 2 顺序=族判据 | B：严格判据 | 12 个 Bake 链/门族加 order_provisional: true（基础序=模板约定；真实序待逐鱼推导，序差异=族移动） | 落表 |
| 3 C9 缓立 | A：并入重跑 | C9/PROGRESSIVE_TIERED_FUNNEL 不入 registry；queue 248 行 pending_work 全部引用重跑基准（含 PROGRESSIVE_TIERED_FUNNEL）；HRQ-RS1-05 关闭注记 | 落表 |
| 4 anchor 四形式 | A：nest/egg_mass/fry_school/host_brood+brooded 边界 | GUARD（Response 面）anchor 轴重写四形式+brooded 边界；guard_participant 轴新立（male\|biparental）；guard_action_notes 注记字段（fan/黏液/DynamicSpatialSlot/premise[fasting]/@NestStructureSet 路由）；GUARD_ANCHOR（Bake 面）anchor_type 轴同源对齐（colony_nest→nest 等 4 值映射）；28 名义重排（见 §2 对账）；pebble_mound→nest（18-vs-19 关闭）；discus_mucus→fry_school+注记 | 落表 |
| 5 HARD_GATED v2 | A：v2+肺鱼/电鳗双成员 | canonical v2 落表（BUILD+双硬门+EXIT 档因子集 unordered×4，渐进累积）；canonical_version: v2+ir_pointer→RP1 NEW_FAMILY_SOURCE.HARD_GATED_FACTOR_COMBINE_V2__PROPOSAL；LUN canonical_source_v2+EEL 第 2 成员（AMBIGUOUS 清除）；electroception_layering_note（REP-CUE-AXIS-001 分层） | 落表 |
| 6 目录卫生 | A：①PATCH 空置②PLAIN 废止③14 并队 | PATCH status→VACATED+vacated_provenance（MGC→GATED_COVER bottom_zone 第 3 实例转正/ONS→SOFT_TRIPLE 第 2 成员转正，known_instances 历史层保留）；PLAIN status→FALSIFIED+v1_falsification（0/5 证据随册：RP1 merge_tests 38 条+OSC/BRT 出族去向）；14 slot_tiering→queue（HRQ-RS1-03 轨关闭注记） | 落表 |
| 7 CRR+簿记 | A：负证据台账保留+名义打包 | CRR negative_evidence_ledger 字段（284=live 侧资产；HRQ-B2-02 关闭）+known_non_matches 补 B5/B6/B7 三行（75+52+47+110=284 闭环）；TYPED 74→248；FOOD_FIELD 2→16；Bake 名义程序 166（v8 pending 转正）；LOCAL_SATURATION_CANDIDATE 正式撤销注记（裁决 1 联动）；MGC 旧口径 reconciliation-note（TYPED v9_notes，待重跑对齐） | 落表 |

**关闭的 HRQ**（随裁决落表）：RS1-01/RS1-04⑥/RS1-05/RS1-03、B4-01（饱和撤销）/B4-02、B5-01/B5-02、B6-01/B6-02、B7-01/B7-02、B2-02。**移交重跑批**：248 行 queue+brooded[ARO/TIL3]+C9 终裁。

## 2. 计数对账

| 项 | v8 | v9 | 构成 |
|---|---|---|---|
| registry 条目 | 21（全 CANDIDATE） | 21（18 CANDIDATE+RETIRED 1+FALSIFIED 1+VACATED 1） | 裁决 6「活族 21→19」=条目口径（移出 PLAIN/PATCH 两个 Bake 空壳；19 含挂 5 held 成员的 RETIRED SINGLE）；CANDIDATE 活族 18 |
| TYPED 成员 | 74 | 248 | +B5 43+B6 45+B7 86（MC[typed] 逐 program_id 数组入册） |
| FOOD_FIELD 成员 | 2 | 16 | +B7 14（MC[field]） |
| GUARD 名义 | 8（7+HNC 挂账） | 28 | +B5 9+B6 2+B7 9 全部转正；四形式正式 26[nest 14/egg_mass 7/fry_school 3/host_brood 2]+brooded 挂起 2[ARO/TIL3] |
| GUARD anchor 轴值 | 6+1（pebble_mound pending）+18 候选挂账 | 4+1 边界 | nest/egg_mass/fry_school/host_brood+brooded（退化边界不入族） |
| CRR non-match | 75（册内） | 284 | +B5 52+B6 47+B7 110 |
| Bake 链/门族成员 | — | 53 | 9 链族 49（TIERED 17/LAYER 2/GATED_COVER 13[+MGC]/NOCTURNAL 5/ZONE_SUB 3/SOFT_TRIPLE 2[+ONS]/ZONE_DEPTH 1/FILTER 2/GUARD_ANCHOR 4）+EXTREME_TEMP 1+PATCH_GATED_DUAL 1+HARD_GATED 2（v2 双成员） |
| SINGLE | 66 名义（过渡双列） | 5 held（RETIRED） | 61 moved 转正链族/C8；LAM/PIN/ASR/RVS/RDS evidence_insufficient_held |
| truth_rebuild_queue | — | 248 行 | B4 25[22 重跑体关联+3 held]+B5 52+B6 47+B7 110+slot_tiering 14（POR/RKB/WIN/SMF/SAI 双轨互引显式注记） |
| order_provisional 族 | 0 | 12 | 9 链族+HARD_GATED+EXTREME_TEMP+PATCH_GATED_DUAL |
| Bake 名义程序 | 166 pending | 166 正式 | B0-B4 冻结 162+RS1 REV-001 4 HAB；B5-B7 Bake 209 条全在 queue 不占族名义；CRR non-match 209 不适用 |

## 3. 执行偏离与独立审确认点（透明披露，均非新增裁决）

1. **GUARD 落位表未点名 8 成员**（CSL/ROB/CRA2/SMA1/BLU2/CCF2/CSN1/BBR1）：按裁决 4 四形式定义直接分类（巢构建型→nest；洞巢利用型→egg_mass+suitability；跨阶段成员按初始存在形式落 nest+跨阶段注记留重跑终裁）——registry four_form_disposition.ruling 已标注「独立审复核点」。
2. **guard_target_specificity 轴缝隙**：决策日志收官关闭清单含「B4-01（饱和撤销）」，但七项裁决未显式处置该轴（裁决 4 仅涉 anchor 轴系；「饱和」语境疑为 B4-02 的 LOCAL_SATURATION 立案）。本批维持该轴 pending HRQ-B4-01 标注并在轴注记显式留独立审确认点——不擅自关闭/转正。决策日志记录本身未改动。
3. **EXTREME_TEMP/PATCH_GATED_DUAL 两新族 status**：决策日志七项裁决未点名（HRQ-RP1-02 仅 PATCH 族重指派部分经裁决 6-① 关闭）——两族维持 PROVISIONAL/单成员现状，仅语义裁定 1 的 canonical 渐进累积对齐+order_provisional 标注。
4. **GUARD participant 值**：仅对有文本证据的成员填（14 例：story 标题/提案文本直证 male 或 biparental），其余不虚构、留重跑补全。
5. **queue B4 层 3 条 held**（ASR/RVS/RDS）：占位行显式标 evidence_insufficient_held（裁决 1-④：归 FR/表达线补证后才可重跑）——234 计数与 envelope 对齐。
6. **TIL3 罗非落 brooded 挂起**：依据裁决 4 brooded 边界原文点名「罗非退化链先例」+银龙盲形冲突登记；领地型 anchor 轴内一致性问题随重跑重审（HRQ-B7-02 的该 pending question 随轴系关闭，但成员归属按 brooded 边界挂起处理）。
7. **registry 既有 YAML 重复键形态**：v8 mutation_provenance 下三个重复 batch 键（PyYAML 后者覆盖）整体平移为 v8_mutation_history，内容零删改、解析行为不变——嵌套重构留待 hygiene 批。

## 4. 验证

- 改动前基线：validate_batch B7 PASS（219/112/345）+RS1 PASS+fixtures 12 全过（**项目 venv .venv/Scripts/python.exe——12 passed；hermes venv 无 pytest，run_fixtures 输出 pass_line=? 且 subprocess 静默失败，勿以该 venv 判定**）
- 期间并行提交：95d67fc（governance: 章程固化——standing docs only，与 census 工件零交叠，本批基线/验证不受影响；本批 commit parent=95d67fc）
- 脚本守卫：36 处替换全部锚点唯一断言通过（1 处计数错误被守卫拦截后修正：review_queue HRQ-RS1-01/02 实为 7 处非 6——FILTER_FIELD 漏数）；写盘前 YAML safe_load 验证（第一次运行 YAML 引号错误在写盘后被检出→git checkout 回滚→修复后重跑，最终态为验证后写盘）
- 改动后：validate_batch HRQ-MUTATION-001 PASS（0 程序空批，manifest 声明非普查批）+B7 复验 PASS（无回归）+fixtures 12 exit 0
- 结构断言：version 9；21 条目 id 唯一；SINGLE/PLAIN/PATCH = RETIRED/FALSIFIED/VACATED；TYPED 248/FOOD_FIELD 16/GUARD 28/CRR 284（§2 全对账）
- 幂等守卫：重跑 exit 1 拒绝（GUARD: registry already at v9）
- 泄漏检查：%s/PLACEHOLDER/FALSITED/brooted 拼写残留 0

## 5. 停点

**status=INDEPENDENT_REVIEW_REQUIRED**。独立审通过后：①push（mutation 批审后推送）；②文档线 v13+work standards §5.1 措辞对齐（语义裁定 2 待办）；③重跑批以 truth_rebuild_queue.jsonl 248 行为输入清单（逐鱼顺序推导必做工序；C9 与 brooded 终裁）。

BATCH_ID: HRQ-MUTATION-001
