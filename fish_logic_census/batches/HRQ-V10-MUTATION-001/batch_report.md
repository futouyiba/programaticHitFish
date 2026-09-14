# HRQ-V10-MUTATION-001 批报告（registry v9→v10 终局重跑统一落册 mutation）

- **批型**：HRQ_ADJUDICATION_EXECUTION（registry mutation 批——非普查批：无冻结 Story/无新盲程序/无新判同；盲纪律不适用）
- **授权**：RB-1/2/3 三批全部 ARTIFACT_APPROVE（批档+审校卡在案：d0db89b / 2c3bc94 / 8196719 首轮）+ `fish_logic_census/hrq_decision_log.md` 全部裁决。**本批零新增裁决**——逐条执行 LT_ENDGAME_CHECKLIST.md 第 3 步 scope，不超出清单范围。
- **执行器**：fcf-census-worker｜**停点**：INDEPENDENT_REVIEW_REQUIRED（mutation 不自我批准；独立审通过前不 push）
- **产物**：template_registry.yaml v10（脚本 apply_v10_mutation.py：幂等守卫 exit 1+锚点 count 断言+**写盘前** yaml.safe_load 全文结构/计数断言——MUT-001 判例①写盘顺序纪律执行）+ RB-2 生成器常量 8 行同步 + RB-3 追溯 freeze_marker + 本批档。discovery_curve.csv **零改动**（RB 三行已在——envelope 明示）。

## 1. 逐项 scope→落表对照

| # | scope 项 | 落表 | 状态 |
|---|---|---|---|
| 1a | RB-1 六族入册 | SPACE_FIRST_DUAL_TIER_CHAIN（61 名义）/FORAGE_FIRST（34）/GATE_SUBSTRATE_TEMPBAND（4）/GUARD_ANCHOR_TURBIDITY（2）/STRUCTURE_LIGHTSLOT（2）/HABITAT_FORAGE_FLOODSLOT（2）——全部渐进累积语义 canonical（源成员冻结真形体逐字转写）+推导证据引用（ir_pointer→RB 批 blind_programs+merge_tests）+provenance sha_chain 指向三批 verdict 卡 | 落表 |
| 1b | RB-3 五形入册 | STRUCTURE_FIRST_QUAD_TIER_CHAIN（BLU 结构先行四步）/LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN（RBP 三步温度中置）/GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN（HNC 门化结构先行）/GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN（ARA 门化温度次置）/BROODED_DEGENERATE_TWO_STEP_CHAIN（ARO）——命名=RB-3 批档 target_family 去 __RB3 后缀；**C9 原候选形 ORDERED_QUAD_TIER_COMBINE_CHAIN 撤案注记**（STRUCTURE_FIRST_QUAD.c9_withdrawal_note——约定序伪影，HRQ-RS1-05/HRQ-RB3-03 终裁链） | 落表 |
| 2 | 族移动执行 23 条 | 23 条记录（RB-1 7+RB-2 16，其中 7 条双轨确认）落为 **16 个成员条目迁移**：TS→LA×4（CHN/COH/BRO/ALE）/TS→FF×3（BRT12/PB/SDG）/TS→SF×1（TSK）/GC→ZS×1（SNS）/GC→SF×3（SSL/FDR/BSB）/GC→TB×2（WIT/YTF）/FILTER_FIELD→TS×2（BHC/HER）——逐条 moved_from 注记+终局真形体指针；源族留迁出面包屑注记（GATED_COVER 6 成员/TIERED_SINGLE 8 成员重排——计数见 §2） | 落表 |
| 3 | FILTER_FIELD→VACATED | status→VACATED+vacated_provenance（HRQ-RB2-01/RB2-03：单步场浓度=factor_type=field 轴值读法——B2 判例复活；known_instances 2 条=历史层）；PATCH VACATED 先例同型 | 落表 |
| 4 | order_provisional 清零 | **8 链族**→order_confirmed: true（证据链=RB-1 7 族 35 MC[HRQ-RB1-06]+RB-2 31 尾在册成员复核[HRQ-RB2-01]——注：RB-2 §3.3 详表为 8 族 31 尾，摘要「9 族」为该批转述笔误）；FILTER_FIELD 随空置以 order_resolution 关闭；**3 族（HARD_GATED/EXTREME_TEMP/PATCH_GATED_DUAL）如实保留 order_provisional+order_final_note**（成员不在 truth_rebuild_queue——RP1 重跑体为 canonical 源，无逐鱼推导覆盖） | 落表（含 envelope 口径偏离披露，见 §4） |
| 5a | TIL3 分面记账修正 | GUARD 族 P-B7-TIL3-RESP 注记改双面：雌口哺=brooded 退化链边界成员（BROODED 族 boundary_note 记账，无独立程序体）/雄领地=TS 轴段独立（终局真形体 P-RB3-TIL3-BAKE/P-RB3-TIL3-RESP-RESP）；membership→exited_v10_split_face_bookkeeping（历史层不计 GUARD 名义）；Semantic Open 随分面读法闭合 | 落表 |
| 5b | ARO 退化链族成员 | BROODED_DEGENERATE_TWO_STEP_CHAIN 入册（canonical=P-RB3-ARO-RESP-RESP）；GUARD 族 P-B5-ARO-RESP 注记退族（membership→exited_v10_brooded_degenerate 历史层；B5 全链盲形=P04 契约模板套用降级；口哺期摄食张力开放项保留） | 落表 |
| 5c | CSL/CSN1→fry_school | 两成员 anchor: form_hold→fry_school（HRQ-RB3-05：CSL=pelagic larvae 直证/CSN1=snakehead §0 直证；egg/浮巢初始阶段 open 保留）；fry_school 3→5（net 至 6 见 5d） | 落表 |
| 5d | 跨阶段 anchor 取值规则统一 | GUARD four_form_disposition.cross_stage_anchor_rule 声明（HRQ-RB2-07 终裁：**以主形式/直证为准**）：JDP 维持 fry_school（裁决 4 落位表直证）/ARA nest→fry_school（主形式=洪水季稚鱼群伴游+B 文件 GuardAnchorResolverInstance=fry_school 直证——初始沙底巢=相邻阶段 open）/CSL 直证 fry_school/SMA1 实例集记法（B 文件 §11.2 两阶段{nest_bed,fry_school}无单值主形式——计 nest 初始实例+后阶段注记）；GUARD_ANCHOR（Bake 面）anchor_type 轴同规注记；MUT 批『按初始形式』读法经规则取代 | 落表 |
| 5e | KOI 品系闭合注记 | TIERED_SINGLE v10_notes.strain_track_closure（KOI/MIR/WRC+RTL TS 同形——RB-2 品系『亲本 R03 轨补证后可升档』开放项经 RB-3 KOI 本体同形闭合，0 冲突） | 落表 |
| 6a | RB-2 生成器常量同步 | 7 处点名（build_census_outputs L103/L110、build_stories_and_manifest L74/L75、run_merge_tests L152/L200/L321）+邻行 title L107 同步=共 8 行——RBP 同代号异种/JSB↔ASB 同属参照措辞，对齐 REV-001/R1 已修产物文本（防重跑再生旧口径）；ARA 初始形式措辞（run_merge_tests L151）**不改**（推导时点记录非事实错误——registry 层由规则取代） | 落表 |
| 6b | RB-3 追溯 freeze_marker | .freeze_marker 补建：blind_frozen_at=2026-09-14T06:21:24Z（二冻终态）/blind_sha256_16=6171ed89cbb82a4e（现盲文件实测）/retrospective=true 标注+first_freeze=06:18:50Z（RB-3 审校 F1 兑现） | 落表 |
| 7 | mutation_provenance 全记录+HRQ 关闭对账 | v10 provenance 块（batch/kind/date/previous_version 9/authorization_chain 三批 SHA/previous_state/rebuild_completion/scope_items 六项/nominal_member_reconciliation/active_family_calibers 三口径/envelope_discrepancies/closed_hrqs/review_gate）；v9 原块整体平移为 v9_mutation_history（内容零删改）；HRQ 对账表=本报告 §3 | 落表 |

## 2. 计数对账

| 项 | v9 | v10 | 构成 |
|---|---|---|---|
| registry 条目 | 21（18 CANDIDATE+3 退役态） | 32（28 CANDIDATE+RETIRED 1+FALSIFIED 1+VACATED 2） | +11 新族−1（FILTER_FIELD 转VACATED） |
| 活族三口径 | 18 在册（CANDIDATE） | **18→28 终态** | 23 Bake（13−1+11）+5 Response；envelope「23 过审」口径=Bake 终态数 |
| 新族名义 | — | **110** | SF 61=28+6+27 / FF 34=10+16+8 / TB 4=2+2 / TU 2 / SL 2 / FS 2 / 五形各 1×5 |
| 既有族 RB 落册 | — | **181+MGC=182** | TS 94（RS1 存留 9+迁入 2+RB-1 16+RB-2 17+RB-3 50）/GC 27（存留 7+RB-1 6+RB-2 7+RB-3 7）/NO 24（5+4+7+8）/LA 7（2+迁入 4+RB-3 1）/ZS 7（3+迁入 1+RB-1 2+RB-3 1）/ST 3（2+RB-3 1）/ZD 2（1+RB-1 1）/GA 18（4+RB-1 5+RB-3 9） |
| RB 三批闭合 | 294 真形体 | =181 MC+110 NEW+AMB 2（TGT/PEL 挂重验）+NOS 1（GAR1） | 82+94+118=294 ✓ |
| GUARD（Response） | 28（四形式 24+brooded 2+form_hold 2） | **26**（nest 11/egg_mass 7/fry_school 6/host_brood 2） | fry_school 3→6（+CSL/CSN1 终裁+ARA 规则重落）；nest 12→11（ARA 出）；brooded 2 退族历史层 |
| 迁移成员条目 | — | 16（moved_from 注记，脚本断言=16） | 23 条批级移动记录（7 条 RB-1/RB-2 双轨） |
| order 状态 | 12 族 order_provisional | 8 order_confirmed+1 随空置关闭+3 维持 provisional | envelope「12 族 order_confirmed」偏离披露见 §4-② |
| curve | 13 数据行 | 13（零改动） | RB 三行已在（85/94/118——n_new=6/0/5） |
| 名义复算（脚本断言） | — | SF=61/FF=34/TB=4/TU=2/SL=2/FS=2/四形各 1；TS=94/GC=27/NO=24/LA=7/ZS=7/ST=3/ZD=2/GA=18；GUARD anchor Counter{11,7,6,2}=26；CANDIDATE=28（Bake 23+Response 5）；moved_from=16 | apply_v10_mutation.py 输出+断言全过 |

## 3. HRQ 全队列关闭对账（RB1-01..06/RB2-01..07/RB3-01..05 = 18 条全 resolved）

| HRQ | 裁决/处置 | v10 落点 |
|---|---|---|
| RB1-01（7 族移动） | 批准（d0db89b） | WIT/YTF/FDR/BSB/SSL/SDG/TSK 七条迁移落表（TB/SF/FF 接收——与 RB-2 双轨一致注记） |
| RB1-02（6 新族） | 批准（含 op 字面归一读法+canonical 源指定） | 六族入册；SF canonical=RKB（ask 建议首选）；op 归一读法落 canonical 注 |
| RB1-03（GC 轴域三点） | 批准 | INC/WST gate→forage 参数读法（GC known_instances 注）；ARO gate_axis=surface_zone 轴值登记（P-RB1-ARO-BAKE 条目） |
| RB1-04（B5 EXT 四例） | 批准 | MDC/LMP/AMK/CRC anchor 值兑现（GA 成员）；JGC→TU 族（canonical 源）；KGO 面级重指派（SF 成员——guard 面承载撤销注记） |
| RB1-05（挂起/held） | 批准（处置=立案挂起） | TGT/PEL 真形挂重验+3 held 维持——provenance rebuild_completion 记账（非并入任何族；通道=FR/表达线） |
| RB1-06（order 确认 7 族） | 批准 | 7 族+LA（RB-2 证据）=8 族 order_confirmed |
| RB2-01（16 移动+空置） | 批准（2c3bc94） | 16 条迁移+FILTER_FIELD VACATED 落表 |
| RB2-02（提案形状扩充） | 批准（并入 RB1-02） | FF+16/SF+6/TB+2/FS+1 成员名单入册（34/61/4/2 名义） |
| RB2-03（field 轴域读法） | 批准（维持轴域读法） | TS factor_type=field 轴域注记（v10_notes.field_axis_reading）；BHC/HER 迁入；FILTER_FIELD 空置 |
| RB2-04（AST/SNS Tier A 优先） | 批准（确认 Tier A 读法） | AST GC 成员（gate→forage 读法注记）；SNS→ZS 迁移（B 层分歧记档随迁） |
| RB2-05（品系轨分辨率） | 批准 | 8 品系入 TS+KOI 品系闭合注记（RB-3 终态） |
| RB2-06（同鱼对账备查） | 备查记录 | 生成器措辞同步（RBP 同代号异种/JSB 同属参照——REV-001 F2 口径防再生） |
| RB2-07（跨阶段 anchor 规则） | 终裁（v10 envelope：主形式/直证） | cross_stage_anchor_rule 声明+JDP/ARA/CSL/SMA1 四成员重落（§1-5d） |
| RB3-01（同鱼对账+CLC） | 备查记录 | 品系闭合注记+CLC 分层注记（NO 族 RB-3 条目） |
| RB3-02（FF/SF 累积） | 批准（并入 RB1-02） | FF 34/SF 61 名义入册（RB-3 27/8 尾成员列表） |
| RB3-03（C9 终裁：撤案+4 形状） | 批准（8196719） | C9 撤案注记+四形状族入册（BLU/RBP/HNC/ARA 各 1） |
| RB3-04（brooded 终裁） | 批准 | ARO 退化链维持（BROODED 族+GUARD 历史层）；TIL3 分面记账双面注记 |
| RB3-05（form_hold 终裁） | 批准 | CSL/CSN1→fry_school（fry_school 3→6 net）；GAR1 无程序面处理随 rebuild_completion 记账 |

## 4. 执行偏离与独立审确认点（透明披露，均非新增裁决）

1. **STRUCTURE_LIGHTSLOT 名义数**：envelope/checklist 记 4，工件实数 **2**（RB-1 GT/GW；RB-2/RB-3 merge_tests 对该族零新增）。按工件入册 2（B7-F2 判例：工件为准）；envelope 口径疑将 GT/GW 的 B3 原体（slot_tiering 前历史层 P-B3-GT/GW-BAKE）计入名义。差额口径（2 vs 4）留独立审确认——registry envelope_discrepancies 已声明。
2. **「12 族 order_confirmed」**：v9 持 order_provisional 的 12 族中，工件证据链（RB-1 7 族+RB-2 31 尾=8 族）仅覆盖 8 链族；FILTER_FIELD 以 VACATED 关闭序问题；HARD_GATED/EXTREME_TEMP/PATCH_GATED_DUAL 三族成员不在 truth_rebuild_queue（RP1 重跑体为 canonical 源）——无逐鱼推导证据，如实保留 provisional+order_final_note 终态注记（envelope 自身「残留未确认成员如实保留标注」条款适用）。
3. **RB-2 §3.3「9 族」摘要笔误**：详表为 8 族 31 尾（TS 9/LA 2/GC 6/NO 5/ZS 3/ZD 1/ST 1/GA 4）——本批按详表口径执行并在 §1-4 注记。
4. **ARA 跨阶段重落（nest→fry_school）**：依据=HRQ-RB2-07 终裁规则（主形式/直证）+B 文件 GuardAnchorResolverInstance=fry_school 直证（guarding/arapaima.md §2.2）+裁决 4 轴文（arapaima 洪水→DynamicSpatialSlot 置于 fry_school 项下）；RB-2 推导时点的「按初始形式落 nest」读法为被取代的旧规则产物（批档不改写——生成器同步仅限事实性身份错误，见 §1-6a）。
5. **GUARD brooded 2 条目处置**：保留在 known_instances（anchor: brooded 不动）+membership→exited_v10_*——历史层不删（provenance 留档纪律）；26 名义计数排除该 2 条（脚本断言）。
6. **curve 零改动**：RB-1/2/3 三行已在册（本批无新增判同故无新行——envelope 明示）。

## 5. 验证

- 改动前基线：git HEAD=8196719（registry v9 sha256_16=6867cc1ebc74541a——脚本首行读取后未再断言前值，锚点 count 断言承担等价防护）
- 脚本执行：全部锚点 count 断言通过（含 chain order line 9 处/单例锚 1 处）；**写盘前** yaml.safe_load+结构断言全过（version 10/32 条目/名义计数 19 族/GUARD anchor Counter/statuses Counter/order 标志 8+3/moved_from=16）
- 幂等守卫：二跑 exit 1（GUARD: registry already at v10）实测 ✓
- validate_batch HRQ-V10-MUTATION-001：PASS（0 程序空批——manifest 声明非普查批）
- fixtures：12/12 passed（.venv/Scripts/python.exe -m pytest——项目 venv）
- RB-2 生成器同步后语法检查：三文件 py_compile 通过；同步文本与 REV-001/R1 已修产物（human_review_queue/engine_report/manifest）逐字一致

## 6. 停点

**status=INDEPENDENT_REVIEW_REQUIRED**。独立审通过后：①push（mutation 批审后推送）；②LT_ENDGAME_CHECKLIST 第 2 步 Notion 轻量同步+第 5 步 v15 终版全家桶（用户明确要求 Notion 上传不可忘记——归 Coordinator/文档线，非本批 scope）；③角色记忆增量更新。

BATCH_ID: HRQ-V10-MUTATION-001
