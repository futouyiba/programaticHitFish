# Resource Patch 系（P02 补批）四面生产级表达交付包｜REP-FULL-P02-001

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 批次 | REP-FULL-P02-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 7 批：P02 Resource Patch→Discrete Target→TargetFeeding 系——grazing 批排除线兑现） |
| 输入 | (1) grazing 批排除表＝`outputs/full_authoring/grazing/README.md` §1（草鱼「归属后续 P02 批」显式留位行 + K3 成员行）；coordinator 补批 handoff（REP-FULL-P02-001，P02 判别轴=食物载体）(2) census B1 归档＝`fish_logic_census/batches/CENSUS-B1/`（stories/programs/blind_programs/resolver_tests/human_review_queue 全文——4 条 frozen P02 Story 全四面判定快照 + 盲程序体冻结）(3) census registry v4＝`fish_logic_census/template_registry.yaml`（SINGLE 族 15 成员 + PLAIN 族 5 成员 canonical body；本批投影对象）(4) REP-COVERAGE-DELTA-001＝`outputs/coverage_delta_r1/report.md`（#5/#11/#23 四面吸收判定 + §2.1 share-vector 判例）(5) 姊妹批样板与留位＝normal 批 brown_trout.md（S12/S14 分工互指行）/ guarding 批 smallmouth.md（B01-S32 相邻故事留位行）/ field 批 albino_grass_carp.md 与 koi.md（品系 L1 等效层本体等待行）(6) normal2 批排除表类 2（「census P02/P03/K3 冻结」7 行——本批兑现其中 P02/K3 侧 5 行）(7) `outputs/usable_forage_contract_r0/`（UsableForageAvailability 契约 R1——Bake 输入描述复用）(8) fish-reference-20260908.csv（物种身份/习性方向锚）(9) live 转录 `tmp/live_stress_main_after.md`（2026-09-10 版；§7 Share 契约/§11.4 DynamicSpatialSlot/§13.2 B-T1/§13.3 R-T1/§17.2 RR-T1 Reaction 槽/§12.2 Quality 绑定） |
| 基线 | **SNAPSHOT_ONLY**——Notion MCP 工具在本执行环境不可用（Story DB live 未访问，同前六批）；P02 Pattern 页正文不在本地，本批判别轴按 handoff 指定口径「P02＝Resource Patch→Discrete Target→TargetFeeding（食物载体=离散资源斑块，对照 P06=连续基质）」+ census frozen_patterns 快照双锚表达；live 漂移时以本 README 引用的归档版为准 |
| 交付物 | `species/*.md` 5 文件（每鱼四面：Group Routing 无路由程序显式声明 + Bake 配置/伪脚本 + Response 配置/伪脚本 + Quality 绑定/伪脚本）+ 本 README + `validate_patch.py` 结构校验器 |
| 数值状态 | 全部阈值/窗口/资源构成/Profile 值域为 **@参数引用**（生产数值由 Profile 层定值，不冻结）；SINGLE 族程序无 combine 步（族域）；PLAIN 族 CombineRule 数学 **OPERATOR UNDEFINED** 待机制侧；live 层组合算子同前批待机制侧 |

## 1. 样本口径（5 文件）

P02＝Resource Patch→Discrete Target→TargetFeeding 系（本批判别轴：食物载体=离散资源斑块）。样本构成 = **census B1 全部 frozen P02 Story（4 条，Tier A）** + handoff 点名 Tier B 一条（鲤）。收录判据沿用 guarding/grazing 批「全部本地快照可证 Story 同口径收录」先例；grazing 批排除表 K3 行所称「Pattern 标签未在本地快照 [需核对]」经本批核对 census B1 stories.jsonl 为**信息不全**——黑鼓鱼 B01-S46 与小口黑鲈 B01-S32 的 frozen_patterns=["P02"] 快照在案（该排除表行仅转引 coverage delta 报告，未对照 census 归档），本批据 census 补全收录。

| # | 文件 | 鱼（学名） | Story | 证据档 | Bake（census 族投影） | Response |
|---|---|---|---|---|---|---|
| 1 | grass_carp.md | 草鱼（Ctenopharyngodon idella） | B01-S53｜植食资源与预投饵斑块（census CENSUS-B1-GRB 快照全文） | A | BA-P02-SINGLE（SINGLE 族**首成员** P-B1-GRB-BAKE，factor=resource_patch(plant+prebait)——首实例） | R-T1 TYPED（P-B1-GRB-RESP，面包/玉米取向参数） |
| 2 | brown_trout_position.md | 褐鳟·位置竞争面（Salmo trutta） | B01-S14｜摄食位置竞争与中心—边缘资源分配（census CENSUS-B1-BRT 快照全文；confidence MEDIUM 原样携带） | A | BA-P02-PLAIN（PLAIN 族第 3 成员 P-B1-BRT-BAKE，patch+rank 2 槽——**本批唯一 PLAIN**；HRQ-B1-04 双轴待批） | R-T1 TYPED（P-B1-BRT-RESP；conflict path 不建） |
| 3 | black_drum.md | 黑鼓鱼（Pogonias cromis） | B01-S46｜翻底坑与泥云作为持续觅食痕迹（census CENSUS-B1-DRU 快照全文；coverage delta #5） | A | BA-P02-SINGLE（P-B1-DRU-BAKE，factor=resource_patch(benthic_prey)） | R-T1 TYPED（P-B1-DRU-RESP，P02 底栖取向） |
| 4 | smallmouth_follow.md | 小口黑鲈·跟随翻底面（Micropterus dolomieu） | B01-S32｜跟随翻底动物获取被惊出的猎物（census CENSUS-B1-SMA 快照全文；coverage delta #11） | A | BA-P02-SINGLE（P-B1-SMA-BAKE，factor=resource_patch(disturbance_revealed)） | R-T1 TYPED（P-B1-SMA-RESP，被惊出猎物取向） |
| 5 | common_carp.md | 鲤（Cyprinus carpio） | FISH-R02-S08｜底质翻拱与资源斑块（coverage delta #23 吸收判定在案；Story 正文 [需正文]） | B | BA-P02-SINGLE 骨架（Tier B 投影，归族裁决移交） | R-T1 骨架（Tier B） |

证据档：A＝本地有该 Story 的全四面判定快照（census stories/programs/blind_programs 冻结）；B＝handoff 点名 + coverage delta 吸收判定 + CSV 方向锚（条件值全 @ 化，Pattern 标 [需核对]）。

### 明确排除项（不属本批，显式记录）

| 排除项 | 理由 |
|---|---|
| 鳜鱼 P02 侧（FISH-R03，census B2 frozen ['P01','P02']） | census 单一程序体（P-B2-MDF-BAKE PLAIN 第 5 成员 + P-B2-MDF-RESP TYPED）已被 normal 批 mandarin_fish.md 全量承载（P01 主面）；P02 是同一 Story 的语义标签之一，**无独立四面程序体**，本批不重复建文件。normal 批「P02 侧归后续场摄食批」表述与本批判定对账——登记项 1 转 Coordinator |
| 青鱼 R04 #34 / 黄尾鲴 R04 #30 / 鲮 R04 #37（coverage delta K3 成员） | 四面吸收判定已由 REP-COVERAGE-DELTA-001 承载（#30/#34/#37 NO_ACTION）；属 R04 成员补批域（grazing 排除表原口径），且 #30/#37 判定含 Field Opportunity（C09–C11）混合语义、#34 含 handling/Conversion owner 边界——非纯 P02 骨架，本批不冒充 |
| 鳙鱼 / 大西洋鲱（normal2 排除表类 2 同列） | P03 场系，field 批已承载 |
| 白化草鱼 / 鲤复合体品系（field 批 L1 等效层 12 文件中相关行） | 品系不分裂独立四面（field 批先例）；本批 grass_carp.md / common_carp.md 即其本体，品系重绑定清单随本体更新（单向从属） |
| 大口黑鲈等其余 R01 批鱼 | 非 Resource Patch 系补批域 |

## 2. 表达读数（对模板计数的影响）

- **Group Routing**：5/5 文件＝「无路由程序，默认 Normal Group」显式声明（§1.1 + §1.2 单默认行 + §1.3 Share 契约校验位）。census 4/4 Group 面 NO_SURFACE_EFFECT（判语各异但结论同构：饵区鱼多≠Group / 竞争占位≠Mode / 痕迹持续≠Mode/Field / 跟随≠RelationalConflict）。**L_group 无增长；G-T1 退化形承 grazing 批先例。**
- **Bake**：本批核心面。5 文件落在 census 两个既有族的 canonical body 投影：**BA-P02-SINGLE ×4**（草鱼/黑鼓鱼/小口黑鲈 Tier A 三成员 + 鲤 Tier B 骨架——SINGLE 族 resource_patch 轴的 P02 实例群）+ **BA-P02-PLAIN ×1**（褐鳟位置竞争——PLAIN 族第 3 成员，patch+rank 2 槽）。**投影标签封闭枚举**（validator BAKEFAM 钉死 {SINGLE, PLAIN}；**PATCH 标签本批不可表达**——census 冻结的 4 条 P02 Bake 程序零 PATCH 成员，PATCH 族翻案（HRQ-B1-02）=规格动作）；**族边界进校验**（FAMCTX：SINGLE 禁多因子行+禁 context 行、NORMALIZE 族常量；PLAIN 强制双槽+CombineRule（COMBINE_WEIGHTED+OPERATOR UNDEFINED）+禁单因子行+禁归一化行；两族同禁 PATCH 域 context 行）。P02 资源斑块的形态多样性（植食/预投饵、底栖猎物、扰动暴露、翻拱底泥、竞争位置）全部由 typed factor 实例 + Profile 重绑定承载，零新族。**census 侧 ΔL_bake=0（本批零新族零新成员——4 程序全部为 census B1 在案成员，非本批新增）；census 族↔live 句型两层 reconciliation OPEN（§3 登记 1）。**
- **Response**：5/5＝R-T1 单通道（Feeding；Reaction 槽 OFF）。Tier A 4 文件绑定 census TYPED_TARGET_RESPONSE 标准成员（P02 定义即→TargetFeeding，非 FieldFeeding——handoff 判别轴与 census 判定一致；褐鳟 conflict path 证据不足不建＝DUAL 族不消费）。**L_response 无增长。** 小口黑鲈的 coverage delta #11 Reaction 通道读法两层登记（§3 登记 2）。
- **Quality**：5/5＝QT-1 绑定表形态；0 个物种级品质调整表（census Quality 面 4/4 NO_SURFACE_EFFECT；黑鼓鱼「存在痕迹不能保底生成个体」边界语义随绑定表说明行携带）。**L_quality 无增长。**
- **新列结构**：零（复用 ROUTING 5 列/BAKE 字段-值/RESP 5 列/绑定表 5 列/META 2 列；bake 配置行键封闭枚举含 PLAIN 侧 Factor1/2/CombineRule 行——validator STRUCT/BAKEROWS 族强制）。

## 3. 跨批一致性登记

1. **census 族 ↔ live 句型两层 reconciliation OPEN（承 grazing 批登记 1，本批不变）**：本批 BakeTemplate 值（BA-P02-*）是 census 族投影标签，不是 live 句型晋升；每文件 LiveLayerProjection 行记录 live 侧等价读法（BA-T1 底板 + DynamicSpatialSlot + 世界侧事实族；褐鳟=B-T1 双因子形态）。两层是否等价、SINGLE/PLAIN 是否升格 live 句型，归机制侧裁决。
2. **Response 面两层登记（本批新增；承 grazing REV-001 M2 先例）**：小口黑鲈 B01-S32——coverage delta #11 吸收读法含「Reaction 通道（erratic 触发，live §17.2 RR-T1 Optional Reaction 槽）」；census 程序体 P-B1-SMA-RESP（TYPED 12 标准成员之一）无 Reaction 步。本文件按 census 程序体表达（R-T1 OFF），两层不静默选择——live 层 RR-T1 槽位若开 Reaction 是 live 配置层动作，不是 census 程序体变更。
3. **handoff Bake 形态预判与 census 判定分歧（登记不闭合）**：handoff 预判「P02 的 Bake＝资源斑块存在性→斑块质量评估→目标接近度；census PATCH 族 canonical body 可复用」——census 实际冻结判定为 3 SINGLE + 1 PLAIN，**零 PATCH**（P02 资源斑块语义由 SINGLE 族 factor_type=resource_patch 轴实例承载；GRB 为该轴首实例）。本批按 census 判定表达。预判描述与 PATCH 族 body 的相似性（EVAL_RESOURCE_PATCH 首步）在 census 盲体中确实可见（4 程序首步 op 均=EVAL_RESOURCE_PATCH），但族判同以完整结构为准（无 typed context 步→SINGLE 非 PATCH）。PATCH↔SINGLE optional_context 边界（HRQ-B1-02 PENDING，worker 倾向 SPLIT）的 4 个当事成员本批占 3（GRB/DRU/SMA）——裁决翻案=换 BakeTemplate+增行=结构变更需重审，validator 拦截静默改写。
4. **褐鳟 rank 因子的双轴待批与两层表达（HRQ-B1-04 + TAR-05）**：槽位数伸缩（2 槽 vs canonical 4 槽，轴声明 2–6）+ EVAL_RANK_POSITION_PREFERENCE 新具名 typed 因子类型准入（首个个体属性调制因子）双轴待批；rank 因子（Bake 侧）与 share-vector（Group 侧同条件多路由，coverage delta §2.1 / live §7+§15.1）是中心—边缘分配同一现实的两个表达层，联合裁决 OPEN——census 选 Bake 侧（Group NO_SURFACE_EFFECT），本批照 census 表达；TAR-05 退化条款原样携带（产品不实现 rank 状态→程序体退化为纯 patch 形→族归属翻案）。
5. **世界侧事实供给义务登记（resolver_tests B1 原文，本批消费）**：prebait_patches（草鱼-玩家预投饵斑块）/ disturbance_events（小口黑鲈-它鱼扰动事件）/ feeding_traces（黑鼓鱼-泥云凹痕）为世界侧事实供给义务，触发上游 SNAP 事实清单登记（与 coverage_delta report §5b 同源）；鲤 R02-S08 翻拱扰动事实族义务同 #5/#11（coverage delta #23）。四者在 forage 契约 SNAP allowlist 收窄义务（契约 README §6）到达时一并处理。**预投饵 vs 自然资源斑块的关键判别（handoff 点名）：census 答案=同一 Bake 形态（SINGLE 同族同轴同一因子实例 resource=aquatic_plant+bait_patch），来源差异在世界侧事实供给层（环境资源 owner 保存），玩家行为产生资源斑块不购买新 Bake 结构**——grass_carp.md §0 展开。
6. **同种多 Story 分工互指闭合（承 normal 批登记 6 先例）**：褐鳟双文件（S12 normal 批 brown_trout.md / S14 本批 brown_trout_position.md——normal 批留位行兑现）；小口黑鲈双文件（C07 guarding 批 smallmouth.md 护巢面 / B01-S32 本批 smallmouth_follow.md 摄食面——guarding 批留位行兑现）；草鱼本体（本批 grass_carp.md）/白化草鱼 L1（field 批）；鲤本体（本批 common_carp.md）/鲤复合体品系 L1（field 批 6+ 文件）。
7. **normal2 排除表类 2 兑现对账**：「census P02/P03/K3 冻结」7 行中，黑鼓鱼(65)/草鱼(184)/鲤鱼(164) 本批建本体文件；鳙鱼(10)/大西洋鲱鱼(75) field 批已承载；青鱼(14)/鲮(9) 仍属 R04 成员补批域（§1 排除表）。

## 4. 退回与登记项（转 Coordinator）

| 项 | 内容 |
|---|---|
| 登记项 1（鳜鱼 P02 侧对账） | normal 批 mandarin_fish.md 写「P02 侧归后续场摄食批」——本批判定：census 对 FISH-R03（frozen P01+P02）只有单一程序体（PLAIN 第 5 成员+TYPED，已被该文件全量承载），**P02 标签无独立四面程序体**，本批不建文件。若机制侧认定 P02 侧需独立表达（如结构资源斑块巡游语义），是 census 新 Story/新程序判定（机制侧动作），不是本批表达动作。需 Coordinator 与 normal 批口径对齐 |
| 登记项 2（鲤 Pattern [需核对]） | R02-S08 行级 Pattern relation 未在本地快照（census 无该 Story 归档；live 不可达）；本文件按 handoff 判别轴读法（底泥离散猎物斑块→P02 侧）收录，Pattern 标 [需核对]。正文到达后若判 P06（连续基质）翻案=结构变更需重审；判无程序语义即撤回 |
| 登记项 3（草鱼行级 Pattern 核对） | handoff 要求「草鱼 P02 归属需核对 Story DB 行级 Pattern relation」——census B1 快照 frozen_patterns=["P02"] 在案（快照层冻结）；live 行级 relation 本环境不可达（SNAPSHOT_ONLY）。快照与行级若冲突，以 live 核对为准——本批不冒充已核对 |
| 登记项 4（grazing 排除表信息不全回写建议） | grazing README §1 排除表 K3 行称黑鼓鱼/小口黑鲈「Pattern 标签未在本地快照 [需核对]」——census B1 stories.jsonl 实有 frozen P02 快照（该行仅转引 coverage delta 未对照 census）。本批已据 census 补全收录；grazing README 该行是否加互指注记由 Coordinator 决定（本角色不改其它批交付物） |
| 登记项 5（HRQ-B1-02 当事成员密度） | PATCH↔SINGLE optional_context 边界裁决（PENDING）的 4 个 2 步 patch 成员中 3 个在本批（GRB/DRU/SMA；第 4 个 PAD34 鸭嘴鲟 P01 已由 normal 批承载）。裁决 SPLIT（维持两族）→本批零变更；裁决 MERGE（PATCH optional_context 吸收）→本批 3 文件换 BakeTemplate 值+增行=结构变更需重审 |
| [需正文] 批量项 | 鲤 R02-S08 的猎物构成/基质偏好/premise 切换（若有）/Response 接受窗方向（common_carp.md §5 列出）；Tier A 4 文件数值全 @ 化待 Profile 层定值 |
| [需核对] 身份项 | 褐鳟 CSV 学名 Salmo trutta 行 262（pelagic-neritic 栖息带与 S14 位置竞争 Story 的底质语境张力——仅方向锚不进程序）；鲤 CSV「肉食性」为底栖无脊椎取向方向的宽标签（census 未判，不构成 diet_classes 定值） |
| 无 UPSTREAM_CHANGE_EVENT | 本批未发现机制侧问题；handoff 的 PATCH 预判与 census 分歧（§3 登记 3）是登记项不是机制缺陷主张；表达层全部落在既有 census 族/livable 结构槽位内 |

## 5. 验证记录（命令与输出原样）

命令（selftest）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/patch/validate_patch.py" --selftest
```

命令（真实交付包校验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/patch/validate_patch.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/patch"
```

### selftest 输出（32 用例）

```
[OK  ] baseline passes unchanged
[OK  ] HEADER fires on missing NOT AUTHORITY
[OK  ] HEADER fires on missing BATCH_ID line
[OK  ] SECTIONS fires on missing Bake section
[OK  ] NOROUTE fires when 1.1 block loses declaration
[OK  ] SHARE fires on missing default route
[OK  ] SHARE fires on missing validation block
[OK  ] REFS fires on @ruleset hit with no ruleset table
[OK  ] BAKEFAM fires on value outside closed enum
[OK  ] BAKEFAM fires on PATCH label (zero PATCH projection this batch)
[OK  ] BAKEFAM fires on missing BakeTemplate row
[OK  ] FAMCTX fires on SINGLE missing FactorType row
[OK  ] FAMCTX fires on SINGLE carrying Factor1Type row (PLAIN domain)
[OK  ] FAMCTX fires on SINGLE carrying CombineRule row
[OK  ] FAMCTX fires on SINGLE carrying ContextConstraint row (PATCH domain)
[OK  ] FAMCTX fires on SINGLE carrying context profile row
[OK  ] FAMCTX fires on PLAIN missing Factor2Type row
[OK  ] FAMCTX fires on PLAIN missing CombineRule row
[OK  ] FAMCTX fires on PLAIN CombineRule without OPERATOR UNDEFINED
[OK  ] FAMCTX fires on PLAIN carrying single FactorType row (SINGLE domain)
[OK  ] FAMCTX fires on PLAIN carrying Normalization row (no normalize step in PLAIN body)
[OK  ] PLAIN variant of fixture passes (positive control)
[OK  ] NORMALIZE fires on missing Normalization row
[OK  ] CONTRACT fires on missing forage contract reference
[OK  ] PROFILES fires on used-but-unlisted token
[OK  ] PROFILES fires on listed-but-unused token
[OK  ] BAN fires on forbidden phrase
[OK  ] BAN fires on unannotated merge phrase in fence
[OK  ] RT1OFF fires on missing Reaction-slot-OFF marker
[OK  ] STRUCT fires on stray table
[OK  ] STRUCT fires on unknown bake config field
[OK  ] exempt INSUFFICIENT_LOCAL_EVIDENCE file only needs header markers
== selftest ==
SELFTEST PASS
```

### 真实交付包校验输出

```
[PASS] black_drum.md
[PASS] brown_trout_position.md
[PASS] common_carp.md
[PASS] grass_carp.md
[PASS] smallmouth_follow.md
== result ==
PASS (5 species files, 0 violations)
```

（README 补齐后重跑，物种文件 5/5 PASS、README 对账 0 违规；首轮物种校验零缺陷——本轮先立 validator 族边界（FAMCTX 含 PLAIN 正例控制）后写工件，未出现 grazing 批的转义竖线/未登记 token 类笔误。）

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器纯标准库，内部强制 stdout UTF-8。

## 6. 边界声明

- 本包只做 P02 Resource Patch 系四面的生产级表达（census 族投影配置 + 中文伪脚本完全展开）；表达验证通过 ≠ 机制 promotion ≠ Freeze；不覆盖 live 主页 / census registry 任何 Verdict。
- 全部数值不冻结（@参数引用，Profile 层定值）；SINGLE 族程序无 combine 步、PLAIN 族 CombineRule 数学 OPERATOR UNDEFINED（族域边界）；census PATCH↔SINGLE 边界（HRQ-B1-02）/ PLAIN 轴扩容（HRQ-B1-04）/ TYPED 成员备案（HRQ-B1-05）状态全程可见。
- 每文件 §5 记录使用/放弃的自由度（含归族裁决权移交、两层 reconciliation OPEN、痕迹/扰动/预投饵的世界侧归属、conflict path 不建、退化条款）。
- 未 commit（提交由 Coordinator / 用户决定）。

BATCH_ID: REP-FULL-P02-001

---

## REP-FULL-P02-REV-001 验收记录（2026-09-11）

- verdict: **ARTIFACT_APPROVE**（第四批直接通过）。核心声明经 census B1 冻结快照第一手证据独立成立。MINOR-1 计数修正。

---

## 7. REP-ORDER-FIX-001 顺序还原修复批次记录（2026-09-11）

**依据**：docs/authoring_work_standards.md §5.1（用户反馈修正，最高优先级——B 系列伪脚本顺序缺陷：平铺结构丢失真实判断顺序）+ fcf-representation-worker 章程产出规则第一条（commit 66713d8）。**修复对象**：本批全部 5 文件。修复方法与 grazing 批（REP-ORDER-FIX-001 同批姊妹面）一致：判断链从证据推导（Tier A=census 盲体 sketch 行为提取；Tier B=CSV/coverage delta 方向级推导标 [需正文]）、平铺改 early return 链、单一 Fit 展开为三档分级命中（preferred 全额/tolerated 削减不清零/excluded 出局）。

### 每文件修复内容（顺序变化 + 新增 early return + 分级命中展开）

| 文件 | 修复前（平铺） | 修复后（顺序还原链） | 新增 early return | 分级命中展开 |
|---|---|---|---|---|
| grass_carp.md | 读事实→EVAL→归一化 | 斑块存在性 → 斑块质量档位 → 归一化（P02 判别轴推论：斑块追随程序先验=斑块存在；canonical 单步展开为存在门+质量档） | 无斑块格（EARLY_RETURN）；质量排除档（EARLY_RETURN） | 斑块质量三档；双构成（水草/预投饵）同源评估不分叉（§0 关键判别维持） |
| brown_trout_position.md | 读事实→槽1→槽2→组合 | patch 存在性 → patch 强度档位 → rank 位置档位 → 加权组合（无 patch 格无竞争占位语义，存在性先行） | 无食物 patch（EARLY_RETURN）；强度排除档（EARLY_RETURN） | patch 强度三档 + **rank 档三档由 census 实例常量 core-vs-edge 直接支持**（优势=中心全额/中间=中间带/次级=边缘带削减不清零）；COMBINE_WEIGHTED 与 OPERATOR UNDEFINED 保留；退化条款（TAR-05）保留 |
| black_drum.md | 读事实→EVAL→归一化 | 底层水层定位 → 底质可翻性档位 → 底栖猎物丰度档位 → 归一化（demersal 硬定位＋翻底物理依赖：可翻性先于猎物丰度） | 非底层（EARLY_RETURN）；不可翻底质（EARLY_RETURN）；无底栖猎物（EARLY_RETURN） | 可翻性/猎物丰度各三档（档位成员 [需正文]，方向示例泥/泥沙/岩盘由 Profile 定值）；痕迹边界声明保留 |
| smallmouth_follow.md | 读事实→EVAL→归一化 | 扰动机会存在性 → 暴露猎物机会档位 → 归一化（**动态机会语义=事件驱动：无扰动事件即无机会斑块，存在门先行**；常态分布归该鱼其它程序面，非本 Story 程序） | 扰动窗口内无事件（EARLY_RETURN）；残余暴露档（EARLY_RETURN） | 暴露猎物三档 |
| common_carp.md | 读事实→EVAL→归一化 | 近底带水层定位（软定位） → 底质可拱性档位 → 底栖猎物斑块丰度档位 → 归一化（benthopelagic 软定位＋翻拱物理依赖：可拱性先于斑块丰度；Tier B 方向级 [需正文]） | 远离底带（EARLY_RETURN，硬定位与否 [需正文]）；不可拱底质（EARLY_RETURN）；无斑块猎物（EARLY_RETURN） | 水层/可拱性/斑块丰度各三档；翻拱痕迹边界声明保留 |

共性：每文件 §2.2 头部加【顺序还原声明】、§2.1 BakeTemplate 值单元格加尾注、§0 加「判断顺序」语义行、§5 自由度记录同步更新；Response 面 §3.2「DECIDE_RESPONSE」未展开占位一并修为三档分级命中（接受/边际低响应/无响应——与 §3.1 配置表两列语义对齐）。

### 不修面与理由

- **Group 面（§1）**：任务边界明示条件原子/组合/分群表不变——零改动。
- **Quality 面（§4）**：既有伪脚本已是完整程序（循环乘因子→汇总→条件归一化/无候选分支），无平铺问题。
- **褐鳟 PLAIN 族配置行**：Factor1/Factor2/CombineRule 行结构不动（FAMCTX 族边界维持——槽序在伪脚本内重排为判断序，配置表零改动）。

### 顺序差异与 census 的分歧登记（UPSTREAM 级，本批不闭合）

顺序还原后链与 census registry v4 canonical body 判语（SINGLE 两步/PLAIN 组合，「无 gate、无 early return」）**拓扑分歧**。处置同 grazing 批 README §7：本批不改 census 文件、BakeTemplate 投影标签不静默改写；**census 侧受影响族重跑（SINGLE 族成员数可能低估）为 work standards §5.4 行动项归 census/coordinator 侧**；Tier A 4 文件顺序=census 盲体行为提取的判断序还原、Tier B（鲤）=方向级推导 [需正文] 校准；水温/光照/时段未入任何链（无 Story 空间程序证据，不冒充 work standards §5.1 通用模板的因子）。

### 验证记录（重跑，命令与输出原样）

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/patch/validate_patch.py" --selftest
== selftest ==
SELFTEST PASS

$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/patch/validate_patch.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/patch"
[PASS] black_drum.md
[PASS] brown_trout_position.md
[PASS] common_carp.md
[PASS] grass_carp.md
[PASS] smallmouth_follow.md
== result ==
PASS (5 species files, 0 violations)
```

本批首轮即 PASS（grazing 批 @Profile 伪 token 教训先吸收——§0 文案直接写「Profile 值域」不带 @）。validator 零改动。

BATCH_ID: REP-ORDER-FIX-001（P02 面）
