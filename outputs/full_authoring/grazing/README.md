# Grazing/底质系（P06 全样本）四面生产级表达交付包｜REP-FULL-GRAZE-001

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 批次 | REP-FULL-GRAZE-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 2 批：Grazing/底质系） |
| 输入 | (1) 基准样板＝live Stress Test R1 主页转录（例 2 烘焙样板 + Grammar 5.1 变体声明 + §7 Share 契约 + §11.4 DynamicSpatialSlot 先例 + §12 Quality 样板 + §13.1 G-T1/§13.2 B-T1/§13.3 R-T1 结构族 + §15.2 M0 配置形态）；`programaticHitFish/tmp/live_stress_main_after.md`（2026-09-10 版）(2) 首批判式与标准＝`outputs/full_authoring/guarding/`（REP-FULL-GUARD-001）(3) census registry v4＝`fish_logic_census/template_registry.yaml`（PATCH_RESOURCE_FOLLOWING 2 成员 + SINGLE_FACTOR_NORMALIZED_WEIGHT 15 成员 canonical body 复用）(4) census 归档 `fish_logic_census/batches/CENSUS-B0/B1`（湄公鲶/准白甲鱼全四面判定快照 + 盲程序体冻结 + HRQ-04/HRQ-B1-01/02 队列）(5) REP-COVERAGE-DELTA-001 判定（K3 底质/附着聚类 #1/#5/#11/#23/#25/#30/#34/#37 吸收读法）(6) `outputs/usable_forage_contract_r0/`（UsableForageAvailability 契约——Bake 输入描述复用）(7) R05/R06/R07/R09/R10 批次摘要（outputs/batches/FISH-R05*.md / FISH-R06*.md / FISH-R07*.md / FISH-R09*.md / FISH-R10.md）(8) fish-reference-20260908.csv（物种身份/习性方向锚） |
| 基线 | **SNAPSHOT_ONLY**——Notion MCP 工具在本执行环境不可用（Story DB live 未访问），全部输入为本地归档/转录/快照；P06 Pattern 页（3d7a4137d23681d6a527eef7c9f42d7d，census manifest 引用）正文不在本地，本批按 handoff 指定口径「P06＝连续基质/底质处理系」表达；live 漂移时以本 README 引用的归档版为准 |
| 交付物 | `species/*.md` 11 文件（每鱼四面：Group Routing 无路由程序显式声明 + Bake 配置/伪脚本 + Response 配置/伪脚本 + Quality 绑定/伪脚本）+ 本 README + `validate_grazing.py` 结构校验器 |
| 数值状态 | 全部阈值/窗口/资源构成/Profile 值域为 **@参数引用**（生产数值由 Profile 层定值，不冻结）；Bake 程序无 combine 步（census SINGLE/PATCH 族域——见 §2 表达读数），live 层组合算子全部 **OPERATOR UNDEFINED** 待机制侧 |

## 1. 样本口径（11 文件）

P06＝连续基质/底质处理系（FR Semantic Pattern Registry；Pattern 页正文不在本地快照——批口径按 handoff 指定）。本批收录 coordinator 分批名单（R05 六条 + R06 亚口科四条）全部 + 本地快照可证的 P06-labeled Story 一条（准白甲鱼，census PATCH 族第 2 成员——照 guarding 批「全部本地快照可证 Story」同口径收录；若 coordinator 裁定名单封闭，该文件独立可撤，结构零耦合）。

| # | 文件 | 鱼（学名） | Story | 机制形态 | 证据档 | Bake（census 族投影） | Response |
|---|---|---|---|---|---|---|---|
| 1 | mekong_giant_catfish.md | 湄公鲶（Pangasianodon gigas） | FISH-R05-湄公鲶-Ontogenetic-Feeding-Rebuild（P05+P06；census B0 快照全文） | 成体底部碎屑/藻 patch→底带 zone 约束→归一化；幼→成 premise 切换（非 Group/非 body 分支） | A | BA-SUBSTRATE-PATCH（PATCH 族创始成员 P-MGC-BAKE-ADULT，zone 侧） | R-T1（TYPED 族创始成员 P-MGC-RESP-FEEDING，evaluator 随 premise 切换） |
| 2 | onychostoma.md | 准白甲鱼（Onychostoma simum） | FISH-R02-S22 急流底质刮食资源（P06 Compression Candidate；census B1 快照全文，confidence LOW） | 急流石底附着藻/碎屑 patch→流速 current context→归一化 | A | BA-SUBSTRATE-PATCH（PATCH 族第 2 成员 P-B1-ONS-BAKE，current 侧） | R-T1（P-B1-ONS-RESP，刮食口径窗） |
| 3 | rohu.md | 泰鲮（Labeo rohita） | FISH-R05（名单：P06 六条之一；正文 [需正文]） | 植食性水草/底质附着资源连续刮取 | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 4 | streaked_prochilod.md | 巴西鲷（Prochilodus lineatus） | FISH-R05（同上；SRCHECK 两行批注在案） | 优势碎屑食性（dominant detritivorous，SRCHECK 已核）底泥/沉积资源连续处理 | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 5 | chiselmouth.md | 美洲锐唇鲷（Gila alutacea） | FISH-R05（同上） | demersal 硬基质表面附着生物膜/藻刮取 | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 6 | giant_barb.md | 暹罗巨鲤（Catlocarpio siamensis） | FISH-R05（同上） | 杂食性底质/附着混合资源连续处理 | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 7 | wuchang_bream.md | 团头鲂（Megalobrama amblycephala） | FISH-R05（同上；SRCHECK「不毁草」条件化在案） | 沉水植物连续啃食（Hydrilla 抑制/Vallisneria 选择——Profile 值域） | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 8 | blue_sucker.md | 长背亚口鱼（Cycleptus elongatus） | FISH-R06（名单：亚口科四条之一；正文 [需正文]） | 亚口科底质吸食（表面/间隙无脊椎） | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 9 | river_redhorse.md | 河红马鱼（Moxostoma carinatum） | FISH-R06（同上） | 亚口科底质吸食（大型无脊椎，吸食式） | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 10 | golden_redhorse.md | 金红马鱼（Moxostoma erythrurum） | FISH-R06（同上） | 亚口科底质吸食（底栖无脊椎） | B | BA-SUBSTRATE-SINGLE | R-T1 |
| 11 | buffalo.md | 水牛鱼（Ictiobus bubalus） | FISH-R06（同上；与大口水牛鱼 C10 种级区分在案） | 亚口科底泥吸食（无脊椎/有机资源） | B | BA-SUBSTRATE-SINGLE | R-T1 |

证据档：A＝本地有该 Story 的全四面判定快照（census stories/programs/blind_programs 冻结）；B＝coordinator 分批名单 + CSV/SRCHECK 方向锚（条件值全 @ 化，资源构成/底质偏好/Pattern 行级标签标 [需正文]/[需核对]）。

### 明确排除项（不属本批，显式记录）

| 排除项 | 理由 |
|---|---|
| 鲤鱼 R02-S08 / 黑鼓鱼 B01-S46 / 小口黑鲈跟随 B01-S32 / 青鱼（R04 #34）/ 黄尾鲴（R04 #30）/ 鲮（R04 #37） | REP-COVERAGE-DELTA-001 K3 底质/附着/扰动聚类成员（Pattern 标签未在本地快照 [需核对]）——其四面吸收判定已由该报告承载（benthic prey class + 基质/流速 Factor + DynamicSpatialSlot），不在本批重复建文件；如需生产级四面展开，另立 R04 成员补批 |
| 草鱼 B01-S53（census P-B1-GRB-BAKE＝SINGLE 族第 1 成员） | Story 冻结 Pattern=P02（植食资源 patch）；与本批 SINGLE 投影同族但 Pattern 域不同——归属后续 P02 批 |
| 鳙鱼 / 大西洋鲱（census B2 food_field 场实例） | 滤食浮游场系（P03），非底质系——批 4-N 或另批 |
| 大口水牛鱼（Ictiobus cyprinellus，15-Case C10） | 其四面表达已由 outputs/fcf_authoring_concrete_r2/four-surface-completion-r1.md 承载（RS-FEED-01 FieldFeeding）；与 R06 水牛鱼为不同种（见 buffalo.md §0 种级区分） |
| 大口黑鲈等 R01 批鱼 | 非 Grazing/底质系 |

## 2. 表达读数（对模板计数的影响）

- **Group Routing**：11/11 文件＝「无路由程序，默认 Normal Group」显式声明（§1.1 无路由条件原子声明 + §1.2 分群结果单默认行 + §1.3 伪脚本保留 Share 契约校验位）。这印证 handoff 预判「grazing 系多无独立 Group 路由」——Grazing 系全样本零 Special Group，G-T1 DECLARATIVE ROUTING VECTOR 的退化形（空 Special 集）即完整表达。**L_group 无增长；条件原子变体（V1–V4）本批零使用**（validator 已裁撤条件原子检查族，若后续批次出现 P06 带条件路由＝扩充 validator 而非放宽，同 forage SNAP allowlist 收窄先例）。
- **Bake**：本批核心面。11 文件全部落在 census registry v4 两个既有 Bake 族的 canonical body 投影：**BA-SUBSTRATE-PATCH ×2**（census PATCH_RESOURCE_FOLLOWING 双成员全样本——湄公鲶 zone 侧 + 准白甲鱼 current 侧，context_type 轴两侧各一）+ **BA-SUBSTRATE-SINGLE ×9**（census SINGLE_FACTOR_NORMALIZED_WEIGHT 15 成员族的底质型扩展骨架）。**投影标签封闭枚举**（validator BAKEFAM 钉死 {SINGLE, PATCH}，新值＝规格动作）；**族边界进校验**（PATCHCTX：PATCH 强制 PROVISIONAL 标记 + ContextConstraint 行 + zone XOR current 单侧；SINGLE 禁一切 context 行——census forbidden_freedoms 的表达层执行）；NORMALIZE_WEIGHT 族常量钉死。底质形态多样性（碎屑/附着藻/水草/底泥无脊椎/急流砾石）全部由 typed factor 实例 + Profile 重绑定承载，零新族。**census 侧 ΔL_bake=0（本批零新族）；live 侧 L_bake_base 无增长——但 census 族↔live 句型两层 reconciliation OPEN（§3 登记 1），本批不把投影标签写成 live 句型晋升。**
- **Response**：11/11＝R-T1 单通道（Feeding；Reaction 槽 OFF——validator RT1OFF 钉死）。Tier A 两文件显式绑定 census TYPED_TARGET_RESPONSE 投影（湄公鲶 evaluator 随 lifecycle premise 切换＝族 evaluator_binding 轴 premise 实例；准白甲鱼刮食口径窗参数）。**L_response 无增长（结构族仍＝R-T1/R-T2 两个，本批全部落在 R-T1 侧）。**
- **Quality**：11/11＝QT-1 绑定表形态；0 个 W1–W3 物种级品质调整表（census Quality 面全样本 NO_SURFACE_EFFECT——湄公鲶齿系重塑归 encounter/conversion 层 typed 参数，不进品质程序体）。**L_quality 无增长。**
- **新列结构**：零（复用 ROUTING 5 列/BAKE 字段-值/RESP 5 列/绑定表 5 列/META 2 列；无未声明变体——由 validate_grazing.py STRUCT/BAKEROWS 族强制，bake 配置行键封闭枚举防行内键注入）。

## 3. 跨批一致性登记

1. **census 族 ↔ live 句型两层 reconciliation OPEN（本批最大登记项）**：census 侧 PATCH/SINGLE 是 LogicTemplate 族（registry v4，含 PROVISIONAL 状态）；live 侧 BA 句型层（BA-T1..T6/B-T1/B-T2 结构族）现无底质单链句型，coverage delta K3 的吸收读法＝BA-T1 底板 + DynamicSpatialSlot + 基质/流速 Factor。本批按 handoff 指定（「Bake 面是 census SINGLE 族主战场」）以 census canonical body 投影表达，每文件 LiveLayerProjection 行记录 live 侧等价读法；**两层是否等价、PATCH/SINGLE 是否升格 live 句型、还是统一压入 B-T1 单因子退化形，归机制侧裁决**——同 guarding 批 census↔live DUAL_PATH 分歧登记先例，不在本批闭合。BakeTemplate 值（BA-SUBSTRATE-*）是本批投影标签，不是 live 晋升。
2. **Tier B 归族裁决权移交**：9 个 Tier B 文件的 SINGLE 骨架是表达层选择（容纳 CSV 机制方向的最低结构）；Story 正文到达后 census 侧判同可能改判 PATCH（带 typed context）/PLAIN（多因子）——届时换 BakeTemplate 值 + 增/删行＝**结构变更需重审**（validator 族边界会拦截静默改写），不是 Profile 重绑定。
3. **census PROVISIONAL/待裁项原样携带**：PATCH 族双成员 PROVISIONAL（P06 压缩测试联动，HRQ-04/HRQ-B1-02 PENDING）；context_type 轴（zone|current）待批（本批两侧各表达一鱼，轴裁决到达后不改结构）；PATCH↔SINGLE optional_context 边界（HRQ-B1-02，worker 倾向 SPLIT——本批按两族分立表达，SPLIT/PENDING 状态可见）；准白甲鱼行为链 Evidence Open（confidence LOW）；P06 Compression Candidate（压回 P02，merge key 四元组）FR 线未闭合——本批按 P06 现标签表达，压缩裁决不改 Bake 程序体。
4. **UsableForageAvailability 契约复用**：每文件 Bake 输入契约行引用 prey_fields/diet_classes/size_window 三过滤（契约 R1 交付）；「水柱场 vs 基质表面」载体无区分、两类压缩进同一契约＝coverage delta 已确认的表达侧事实，本批沿用不重开。附着生物量事实族到达时触发契约 SNAP allowlist 收窄义务（契约 README §6 已登记）。
5. **与 guarding 批的模板关系**：本批 Group 面首次出现「无路由程序」显式声明形态（guarding 20 文件全部有 Guarding Group 路由）——两形态都在 G-T1 声明式路由向量内（退化形/非退化形），不是新 Group 结构。
6. **湄公鲶幼体通道指针**：幼体 FieldFeeding 的 P0x 语义层对应指针待 coordinator 确认（census fix_notes：coordinator 修复信中「P03 轴」引用未核实，census/表达侧不引用未读 pattern）——mekong_giant_catfish.md §5 原样携带。

## 4. 退回与登记项（转 Coordinator）

| 项 | 内容 |
|---|---|
| 登记项 1（Pattern 口径张力） | R06 亚口科四条：coordinator 分批名单按 P06 归类，但本地 R06 FR3 摘要（FISH-R06-FR3-001.md）记「P06 零新样本（merge 建议维持 R05 状态）」——两种口径不能同真（除非四鱼 Story 为 Existing P06 而「零新样本」指 pattern-level 新成员，或四鱼为 P02/P03 底质机制族跨 Pattern 收录）。需 Story DB 行级 Pattern 标签核对；本批按机制族收录，四文件头 Pattern 标 [需核对]，不改分批决定 |
| 登记项 2（R05 五条同款） | 泰鲮/巴西鲷/锐唇鲷/暹罗巨鲤/团头鲂：行级 Pattern 标签未在本地快照（R05 FR3 摘要仅记 P06 merge 建议存在）；[需核对] |
| 登记项 3（R07 P06 DiscoveryBatch +4） | FISH-R07-FR3-001.md 记「P06 DiscoveryBatch +4」——4 个样本的鱼名/Story 行未在本地任何快照。不在本批冒充覆盖；其归档后补批登记 |
| 登记项 4（R09/R10 P06 对账） | R09（26 鱼）/R10（49 行收官）批本地摘要无 P06 per-fish 明细；若含 P06 样本需补批对账（同 guarding 批 R10 尾批处理） |
| [需正文] 批量项 | Tier B 9 文件的资源构成（水草/附着/碎屑/底泥无脊椎比例）、底质类型偏好、premise 切换（若有）、Response 接受窗参数方向、蓝吸/红马/水牛的种级资源区分（逐文件 §5 列出）；Story 正文到达后只填 Profile 语义，结构变更需重审（§3 登记 2） |
| [需核对] 身份项 | 团头鲂最大体长 200cm 疑源错（FISH-R05 批发现，行标待人工确认，文件不引用）；锐唇鲷 CSV 学名 Gila alutacea（行级 AI 审核状态=待人工审核） |
| 无 UPSTREAM_CHANGE_EVENT | 本批未发现机制侧问题；表达层全部落在既有 census 族/livable 结构槽位内。census↔live 两层 reconciliation（§3 登记 1）是登记项不是机制缺陷主张 |

## 5. 验证记录（命令与输出原样）

命令（selftest）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/grazing/validate_grazing.py" --selftest
```

命令（真实交付包校验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/grazing/validate_grazing.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/grazing"
```

输出：见下方两个代码块（原样粘贴，未改测试凑通过；首轮真实校验抓出 4 处真实工件缺陷——湄公鲶/准白甲鱼 Bake 配置表单元格内的转义竖线破坏行宽 ×2、准白甲鱼未登记先例 token @LowEnergyRefugeProfile ×1、团头鲂伪 token @Profile ×1——均修复工件而非改校验器）。

### selftest 输出

```
[OK  ] baseline passes unchanged
[OK  ] HEADER fires on missing NOT AUTHORITY
[OK  ] HEADER fires on missing BATCH_ID line
[OK  ] SECTIONS fires on missing Bake section
[OK  ] NOROUTE fires when 1.1 block loses declaration (marker only in script fence)
[OK  ] SHARE fires on missing default route
[OK  ] SHARE fires on missing validation block
[OK  ] REFS fires on @ruleset hit with no ruleset table
[OK  ] BAKEFAM fires on value outside closed enum
[OK  ] BAKEFAM fires on missing BakeTemplate row
[OK  ] PATCHCTX fires on PATCH without PROVISIONAL marker
[OK  ] PATCHCTX fires on PATCH missing ContextConstraint row
[OK  ] PATCHCTX fires on SINGLE carrying ContextConstraint row
[OK  ] PATCHCTX fires on SINGLE carrying context profile row
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
[PASS] blue_sucker.md
[PASS] buffalo.md
[PASS] chiselmouth.md
[PASS] giant_barb.md
[PASS] golden_redhorse.md
[PASS] mekong_giant_catfish.md
[PASS] onychostoma.md
[PASS] river_redhorse.md
[PASS] rohu.md
[PASS] streaked_prochilod.md
[PASS] wuchang_bream.md
== result ==
PASS (11 species files, 0 violations)
```

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器纯标准库，内部强制 stdout UTF-8。

## 6. 边界声明

- 本包只做 Grazing/底质系四面的生产级表达（census 族投影配置 + 中文伪脚本完全展开）；表达验证通过 ≠ 机制 promotion ≠ Freeze；不覆盖 live 主页 / census registry 任何 Verdict。
- 全部数值不冻结（@参数引用，Profile 层定值）；Bake 程序无 combine 步（族域边界）；live 层组合算子 OPERATOR UNDEFINED 待机制侧；census PATCH/SINGLE PROVISIONAL 状态全程可见。
- 每文件 §5 记录使用/放弃的自由度（含归族裁决权移交、两层 reconciliation OPEN、种级区分、性格档案字段不程序化、未证实数字不引用）。
- 未 commit（提交由 Coordinator / 用户决定）。

BATCH_ID: REP-FULL-GRAZE-001
