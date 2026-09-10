# Migration/生活史系（P05 全样本）四面生产级表达交付包｜REP-FULL-MIGRA-001

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 批次 | REP-FULL-MIGRA-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 3 批：Migration/生活史系） |
| 输入 | (1) 基准样板＝live Stress Test R1 主页转录 `programaticHitFish/tmp/live_stress_main_after.md`（2026-09-10 版：§2 G2 大西洋鲑 MigrationReaction share-vector 路由样板 + §5.1 条件原子 V2/R2 变体 + §7 Share 契约 + §8.8 关闭 Feeding 缺 Typed Result 修复 + §11.3 Shad Spawn MERGE_SUPPORTED + §11.4 DynamicSpatialSlot + §11.6 Prespawn Staging NEW_TEMPLATE_NOT_PROVEN + §12 Quality 样板 + §13.1 G-T1/§13.2 B-T1/§13.3 R-T1·R-T2 结构族 + §17 RR-T1 Reaction 槽 + §15.2 M0 配置形态）(2) 首两批判式与标准＝`outputs/full_authoring/guarding/`（REP-FULL-GUARD-001）+ `outputs/full_authoring/grazing/`（REP-FULL-GRAZE-001）(3) census registry v4＝`fish_logic_census/template_registry.yaml`（SINGLE 15 成员 / PLAIN 5 成员 / HARD_GATED 2 成员 canonical body 复用；本批投影族=三族）(4) census 归档 `fish_logic_census/batches/CENSUS-B0/B1/B2`（P05 域 9 Story 全四面判定快照 + 盲程序体冻结 + HRQ/TAR 队列）(5) 15-Case C12 大西洋鲑四面归档＝`outputs/fcf_authoring_concrete_r2/four-surface-completion-r1.md`（上游生命周期分流 + Bake 明确不适用 + RS-FEED-01/RS-REACTION-01 + Q-DEFER-01）(6) REP-COVERAGE-DELTA-001 判定（#3 口孵 Cap / #6 性别 share-vector / #22 色型不分裂 / #24 剑旗鱼 2D 回归 / K6 份额拆分聚类）(7) R05–R10 批次摘要（outputs/batches/FISH-R05*.md … FISH-R10*.md：停食判例族五例链=大马哈/美洲西鲱 R06→白北鲑 R08→高首鲟 R09→狼鱼 R10；银鲫非持久性判例 R09）(8) `outputs/usable_forage_contract_r0/`（UsableForageAvailability 契约——Bake 输入描述复用）(9) fish-reference-20260908.csv（物种身份/迁徙类型方向锚） |
| 基线 | **SNAPSHOT_ONLY**——Notion MCP 工具在本执行环境不可用（Story DB live 未访问），全部输入为本地归档/转录/快照；P05 Pattern 页正文不在本地，本批按 handoff 指定口径「P05＝Lifecycle/Migration/State 系」表达；live 漂移时以本 README 引用的归档版为准 |
| 交付物 | `species/*.md` 21 文件（每鱼四面：Group Routing（含 MigrationReaction share-vector 路由或无路由显式声明）+ Bake 配置/伪脚本 + Response 配置/伪脚本（停食族双 Path 展开）+ Quality 绑定/伪脚本）+ 本 README + `validate_migration.py` 结构校验器；**两文件组**：洄游组 17 文件（§1 表 A）vs 阶段/蛰伏/状态组 4 文件（§1 表 B）——同目录平铺，README 分组承载 |
| 数值状态 | 全部阈值/窗口/阶段枚举/份额为 **@参数引用**（生产数值由 Profile 层定值，不冻结）；SINGLE/PLAIN/GATED 投影族内 CombineRule 拓扑族固定、数学 **OPERATOR UNDEFINED** 待机制侧；停食族 Feeding 关闭=Typed Result 档位语义（Cap 残值形态为 Profile 层选项） |

## 1. 样本口径（21 文件 / 21 Story）

P05＝Lifecycle/Migration/State 系（handoff 指定口径）。本批收录 handoff 分批名单点名且本地可锚的全部成员 + 全部本地快照可证的 P05-labeled census Story（照 guarding/grazing 批「全部本地快照可证 Story」同口径）。

### 表 A｜洄游组（17 文件）

| # | 文件 | 鱼（学名） | Story | 机制形态 | 证据档 | Group 拓扑 | Bake（census 族投影） | Response |
|---|---|---|---|---|---|---|---|---|
| 1 | atlantic_salmon.md | 大西洋鲑（Salmo salar） | FISH-R06 鲑系洄游层 [需正文]；**G2 live 样板 + C12 15-Case 四面归档双层在案** | 溯河产卵型；停食=C12 Case 语义（实证 [需正文]） | A- | MigrationReaction share-vector（G2） | BA-MIGRATION-SINGLE（洄游位置轴） | 双 Path（Feeding/Reaction） |
| 2 | chum_salmon.md | 大马哈鱼（Oncorhynchus keta） | FISH-R06；**停食判例族首例**（摘要原文「Adults cease feeding in freshwater」） | 停食洄游 multi-path（R06/R10 FR3 分支化洄游侧） | B | 同上 | 同上 | 双 Path |
| 3 | american_shad.md | 美洲西鲱（Alosa sapidissima） | FISH-R06；**停食第 2 例**（原文「Feeding ceases during upstream spawning migration」）+ live §11.3 Shad Spawn 判例同鱼异面登记 | 停食洄游 multi-path | B | 同上 | 同上 | 双 Path |
| 4 | inconnu.md | 白北鲑（Stenodus leucichthys） | FISH-R08；**停食第 3 例跨科** | 停食洄游 multi-path | B | 同上 | 同上 | 双 Path |
| 5 | white_sturgeon.md | 高首鲟（Acipenser transmontanus） | FISH-R09；**停食第 4 例（鲟科）**；白化变体行不分裂 | 停食洄游 multi-path | B | 同上 | 同上 | 双 Path |
| 6 | arctic_char.md | 北极红点鲑（Salvelinus alpinus） | FISH-R02-S25（census B2 快照全文） | 冷水季节位移（temp/season premise 绑定） | A | 无路由声明 | BA-MIGRATION-SINGLE（近岸↔深水） | R-T1 |
| 7 | vendace.md | 欧白鲑（Coregonus albula） | FISH-R02-S04（census B2 快照全文） | 底层/水层切换（temp/season premise 绑定；滤食取向 P03 复核登记） | A | 无路由声明 | BA-MIGRATION-SINGLE（水层因子） | R-T1 |
| 8 | swordfish_diel.md | 剑旗鱼（Xiphias gladius） | FISH-R02-S23（census B2 快照全文；文件名 _diel=Story 限定） | 昼夜垂直迁移（diel premise 绑定；#24 2D 回归登记） | A | 无路由声明 | BA-MIGRATION-SINGLE（diel 水层因子） | R-T1 |
| 9 | northern_pike_spawn.md | 白斑狗鱼（Esox lucius） | B01-S19（census B2 快照全文；_spawn=Story 限定，S18/S20 不属本文件） | 淹水草地繁殖↔回深水（spawning_stage premise 绑定） | A | 无路由声明 | BA-MIGRATION-SINGLE（繁殖位置轴） | R-T1 |
| 10 | walleye_spawn.md | 玻璃梭鲈（Sander vitreus） | B01-S02（census B2 快照全文） | 繁殖浅滩季节重排（温度+食物 2 因子） | A | 无路由声明 | BA-MIGRATION-PLAIN（本批 PLAIN 唯一 Tier A） | R-T1 |
| 11 | atlantic_cod.md | 大西洋鳕（Gadus morhua） | B01-S52（census B1 快照全文） | 繁殖期性别相关水深（sex/stage premise 绑定；coverage #6 share-vector 替代读法登记） | A | 无路由声明 | BA-MIGRATION-SINGLE（深度因子） | R-T1 |
| 12 | chinook_salmon.md | 帝王鲑（O. tshawytscha） | FISH-R06 鲑科四之二 [需正文] | 非停食洄游（停食未证实——证实即升级双 Path） | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1 |
| 13 | sockeye_salmon.md | 红鲑（O. nerka） | FISH-R06 鲑科四之三 [需正文] | 非停食洄游；湖沼生活史 premise；滤食取向 P03 复核登记 | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1 |
| 14 | coho_salmon.md | 银鲑（O. kisutch） | FISH-R06 鲑科四之四 [需正文] | 非停食洄游（停食未证实） | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1 |
| 15 | alewife.md | 灰西鲱（Alosa pseudoharengus） | FISH-R06 西鲱二之二 [需正文] | 非停食洄游（同属美洲西鲱停食判例不默认继承） | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1 |
| 16 | brook_trout.md | 美洲红点鲑（Salvelinus fontinalis） | handoff 红点鲑二之二 [需正文] | 溯河型 salter↔河段（同属北极红点鲑先例读法） | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1 |
| 17 | atlantic_tarpon.md | 大西洋大海鲢（Megalops atlanticus） | handoff 点名 [需正文] | **amphidromous** 发育阶段洄游（非繁殖前奏——状态轴差异登记） | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1 |

### 表 B｜阶段切换/个体发生/蛰伏/状态组（4 文件）

| # | 文件 | 鱼（学名） | Story | 机制形态 | 证据档 | Group 拓扑 | Bake | Response |
|---|---|---|---|---|---|---|---|---|
| 18 | common_chub.md | 欧鲢（Squalius cephalus） | FISH-R05-欧鲢-Size-Graded-Opportunism-Spawning-Run（census B0 快照全文；P01+P05） | 体型分级机会主义+产卵洄游配置级（CHB 先例源；停食判例族阴性对照——洄游不停食） | A | 无路由声明 | BA-MIGRATION-PLAIN（4 槽：流速/深潭/猎物/水面机会；spawn 因子集配置切换） | R-T1（evaluator 参数宽度随 size_class premise） |
| 19 | ide.md | 圆腹雅罗鱼（Leuciscus idus） | handoff 点名（Ide 食性随龄）[需正文] | 个体发生食性切换（lifecycle premise 层） | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1（参数随 premise） |
| 20 | lungfish_aestivation.md | 南美肺鱼（Lepidosiren paradoxa） | FISH-R05-南美肺鱼-Aestivation-State-Switch（census B0 快照全文）；**同 Story 双批分工**：护巢面归 Guarding 批 | 湿/干两态蛰伏切换（state switch=world/lifecycle-owned premise，census 冻结独立结论；DRY 退化体 AMBIGUOUS/TAR-01 不建体） | A | 无路由声明 | BA-MIGRATION-GATED（WET 态水面可达硬门+因子集；census HARD_GATED 在案成员） | R-T1（DRY=premise 层 rate 抑制无 body） |
| 21 | prussian_carp.md | 银鲫（Carassius gibelio） | FISH-R09 银鲫判例（§6 四问非持久性）[需正文] | 雌核种群繁殖状态=非持久性 condition（不购买 FishGroup；保守度接受） | B | 无路由声明 | BA-MIGRATION-SINGLE（骨架） | R-T1 |

证据档：A＝本地有该 Story 的全四面判定快照（census stories/programs/blind_programs 冻结）；A-＝表达样板双层在案（G2 live + C12 归档）但 Story 行级 [需核对]；B＝coordinator 分批名单点名 + 批次摘要批注/CSV 方向锚（条件值全 @ 化，阶段枚举/资源构成标 [需正文]）。

### 明确排除项（不属本批，显式记录）

| 排除项 | 理由 |
|---|---|
| 湄公鲶 FISH-R05（P05+P06） | P05 侧（个体发生 premise 切换+potamodromous 配置级）已由 Grazing 批 `mekong_giant_catfish.md` 四面承载——不重复建文件 |
| 罗非鱼 B01-S44（P05 口孵） | 已由 Guarding 批 `nile_tilapia.md` 承载（类型化繁殖状态路由退化绑定+R-T1 Cap——coverage #3 判例） |
| 狼鱼（R10 停食护卵第 5 例首例护卵型） | R10 FR3 分支化判例 relation 证实侧→**P04 承载**；Guarding 批 README 已登记补批待办——本批不冒充覆盖 |
| 电鳗 S9 幼成切换 | 已由 Guarding 批 `electric_eel.md` NormalFeeding 面绑定（evaluator_binding premise 实例） |
| 乌鳢 R02-S15 | Guarding 批 `snakehead.md`（伏击↔护幼类型化状态互斥）已承载；「蛰伏面」零本地 Story 证据——待补批对账（§4 登记项 4） |
| 笋壳鱼（塘鳢科） | Guarding 批已退回（本地 Pattern=P01 伏击）；「塘鳢蛰伏」零本地证据——待补批对账（§4 登记项 4） |
| 海七鳃鳗 B01-S49 | pattern_status=Semantic Open（非 P05 冻结）；其化学趋向 cue 轴已由 REP-CUE-AXIS-001 承载（coverage delta #13 NEW_CONFIG_COVERAGE）——不属本批 |
| 大口黑鲈等 R01 批鱼 | 非 Migration/生活史系批范围 |
| 褐鳟 B1-S14/B2-S12、蓝鳃 B1-S39、白斑狗鱼 S20/S18 等同种异 Story | census 归档 Pattern=P01/P02（非 P05）；S18/S20 见 northern_pike_spawn.md §5 Story 限定 |
| 鳙鱼/大西洋鲱（census B2） | P03 场摄食系——非 P05（红鲑/欧白鲑的滤食取向仅作参数方向锚+P03 复核登记，不收 P03 文件） |

## 2. 表达读数（对模板计数的影响）

- **Group Routing**：双形态并存（本批核心读数）。**MigrationReaction share-vector 路由 ×5**（停食洄游 multi-path 组——G2 live 样板原样形态：条件原子 V2（洄游阶段 IN + 水体类型 IN）+ 规则集 R2 AND + @share 分流 + 默认行；P05 系首次出现洄游相位路由的生产级表达）+ **无路由显式声明 ×16**（其余全部——census P05 Group 面 NO_SURFACE_EFFECT 判语原样）。两形态都在 G-T1 DECLARATIVE ROUTING VECTOR 内（非退化形/退化形），**L_group 无增长**。
- **Bake**：21/21 落在 census registry v4 三个既有 Bake 族的投影：**BA-MIGRATION-SINGLE ×17**（census SINGLE 族 15 成员族的位置/水层/diel 因子型扩展骨架——Tier A 在案成员 5（ARC/VEN/SWO/PIK19/COD B1）+ Tier B 骨架 12）、**BA-MIGRATION-PLAIN ×2**（WAL Tier A 第 4 成员 + CHB census B0 在案成员 4 槽）、**BA-MIGRATION-GATED ×1**（肺鱼 WET=census HARD_GATED 在案成员）。**投影标签封闭枚举**（validator BAKEFAM 钉死，新值=规格动作）；**族边界进校验**（FAMCTX：SINGLE=单因子+NORMALIZE_WEIGHT 禁 gate/combine；PLAIN=Factor1..4+CombineRule OPERATOR UNDEFINED 禁 Normalization；GATED=SurfaceGate+FactorSet 禁 Normalization/SpatialSlot）；**PREMBIND：每文件 FactorBinding 行强制 premise 引用**（P05 批核心不变量——阶段切换永远 premise 配置级，不进 body 分支）。**census 侧 ΔL_bake=0（本批零新族）；live 侧无新句型（BA-T7 ROUTE/TRANSITION 依 §11.6 判 NEW_TEMPLATE_NOT_PROVEN 不购买——洄游空间重排全部由 BA-T1 底板+DynamicSpatialSlot 或阶段因子集切换承载）。**
- **Response**：**双 Path（P05×multi-path）×5**——停食洄游组（R06/R08/R09/R10 FR3 分支化判例洄游侧）：NormalFeeding=R-T1 Feeding（Reaction 槽 OFF）+ MigrationReaction=R-T1 单通道 Channel=Reaction（Feeding 强抑制或关闭=Typed Result 档位语义 + 「不再评价普通 Feeding」结构性关闭——§8.8 修复先例）；伪脚本双 Path 完全展开。其余 ×16=R-T1 单通道。**L_response 无增长（结构族仍=R-T1/R-T2 两个；multi-path=两 Group 各 R-T1 的 G2 分群读法，R-T2 折叠候选 OPEN——§3 登记 3）。**
- **Quality**：21/21=QT-1 绑定表形态；0 个 W1–W3 物种级品质调整表（census P05 域 Quality 面全样本 NO_SURFACE_EFFECT）；停食组 MigrationReaction 行带 Eligibility（洄游期成熟个体组成方向）。**L_quality 无增长。**
- **新列结构**：零（V2 六列条件原子/R2 三列规则集/ROUTING 5 列/BAKE 字段-值/RESP 5 列/绑定表 5 列/META 2 列——全部 live §5.1 已声明变体；bake 配置行键封闭枚举防行内键注入，由 validate_migration.py STRUCT/FAMCTX 族强制）。

## 3. 跨批一致性登记

1. **census 族 ↔ live 句型两层 reconciliation OPEN（承 grazing 批登记 1）**：本批投影标签（BA-MIGRATION-SINGLE/PLAIN/GATED）是 census LogicTemplate 族的批投影标签，不是 live 句型晋升；live 侧等价读法=BA-T1 底板+DynamicSpatialSlot（§11.4）或 B-T1 Independent Factor Set（§13.2）+Optional Gate。洄游专用句型的 escape condition（§11.6：path/transition 顺序直接进入 SpatialDistributionWeight 且上游 Resolver 无法产出）在本批 21 Story 中零命中——BA-T7 维持 NEW_TEMPLATE_NOT_PROVEN。两层是否等价归机制侧裁决，本批不闭合。
2. **Tier B 归族裁决权移交（承 grazing 批登记 2）**：12 个 Tier B 文件的 SINGLE 骨架是表达层选择（容纳 handoff 点名+CSV 方向的最低结构）；Story 正文到达后 census 侧判同可能改判 PLAIN（多因子）/GATED（硬约束）/停食升级 MigrationReaction 双 Path——届时换 BakeTemplate 值 + 增/删行/增 Group 路由=**结构变更需重审**（validator 族边界拦截静默改写），不是 Profile 重绑定。同属判例（灰西鲱×美洲西鲱停食；美洲红点鲑×北极红点鲑 SINGLE）只是读法一致性，不是判同结论——行级证据到前不继承。
3. **停食判例族的 Response 拓扑 OPEN（R-T2 折叠）**：本批双 Path 按 G2 分群语义表达（两 Group 各 R-T1 单通道，每时刻鱼只在一 Group）；live §13.3 自身注明「C12 大西洋鲑也可能映射到 R-T2（固定 Feeding/Reaction 双 Channel），取决于最终是否保留」——两表达是否折叠归机制侧。停食的 Typed Result 双形态（档位关闭 vs Cap 残值）同为 OPEN：@MigrationReactionProfile 值域内 Profile 层选，本批不冻结。
4. **P05 域待裁项原样携带**：肺鱼 DRY 蛰伏退化体 AMBIGUOUS/TAR-01（不建体不冒充 playable——裁决到达即结构动作）；剑旗鱼 coverage #24 NEEDS_REGRESSION_SAMPLE（2D 定向判据留 representation 线）；大西洋鳕 coverage #6 share-vector 替代读法（census 主判定=配置级——同是 G-T1 域内表达层选择，非结构分歧）；白斑狗鱼 Active Spawning Group+Cap 替代读法（同登记）；红鲑/欧白鲑滤食取向 P03 复核线（Response 族判定若升级=族变更需重审）。
5. **与前两批的分工与互指**：湄公鲶（P05+P05 个体发生+potamodromous 配置级）→ grazing 批承载；罗非鱼口孵（P05 阶段 Cap）→ guarding 批承载；狼鱼（停食判例 P04 侧）→ guarding 批补批待办；电鳗 S9（幼成切换）→ guarding 批承载。**同一 Story 双批分工首例：肺鱼**——P05 湿干两态主面（本批 lungfish_aestivation.md）/护巢面（guarding 批 lungfish.md）；两文件引用同一 census 快照不同程序子集，WET 态 Normal 面 Bake 语义一致（本批 BA-MIGRATION-GATED 投影 vs guarding 批 BA-LUN-WET-GATED-FACTORS 命名），批间标签 reconciliation 归两层登记（本条）。
6. **蛰伏组组级判语**：state switch 本身是 world/lifecycle-owned premise，不是 surface 自有程序（census 肺鱼冻结独立结论，与 FR3 语义判例一致）——本批蛰伏/阶段/状态组全部按此表达（Group 无路由+Bake premise 绑定+Response 参数级/无 body）；乌鳢/笋壳鱼「蛰伏面」零证据成员不冒充（§4 登记项 4）。
7. **UsableForageAvailability 契约复用（承 grazing 批登记 4）**：每文件 Bake 输入契约行三过滤引用；洄游型跨水体（海/河）的 prey class 值域由 prey_fields Profile 承载，不改契约结构。

## 4. 退回与登记项（转 Coordinator）

| 项 | 内容 |
|---|---|
| 登记项 1（「鲑科四」名单读法） | handoff「鲑科四」按字面收录大西洋鲑/帝王鲑/红鲑/银鲑四条；CSV anadromous 鲑科另有粉鲑/硬头鳟/细鳞鲑/褐鳟/虹鳟/白马切喉鳟等——R06「鲑系洄游 10」的具体构成未在本地逐行列出。若 Story DB 有其余鲑科 P05 行，补批对账；本批不冒充全覆盖 |
| 登记项 2（P05 行级标签） | 16 个非 census 文件的行级 Pattern 标签未在本地快照（handoff 点名 + 摘要批注为收录依据）；[需核对] |
| 登记项 3（蛰伏/耐冻/塘鳢/蛇鹈） | handoff NOTES 点名「蛰伏型（肺鱼/塘鳢/黑鱼/耐冻系）」「阶段切换（蛇鹈/慈鲷系阶段）」：肺鱼 Tier A 已收录；**塘鳢（笋壳鱼已退回 P01）/乌鳢蛰伏面/耐冻系/蛇鹈四项零本地 Story 证据**——「蛇鹈」名实无法闭合（Anhinga 为鸟名，疑笔误：蛇鮈/蛇鲈？）——需 coordinator 澄清名单；零证据成员不建文件，待 Story 归档后补批 |
| 登记项 4（洄游系未入库成员） | Whitefish 通名系（湖白鲑/驼背白鲑/高白鲑）、鲟系其它（俄罗斯鲟/尖吻鲟/短吻鲟/闪光鲟/小体鲟/白化高首鲟变体行）、北美狗鱼/链纹狗鱼等 non-migratory 红点鲑对照（湖红点鲑）——CSV 行在但 P05 Story 零本地证据；归档后补批 |
| 登记项 5（R09/R10 P05 对账） | R10 收官 49 行中 P05 per-fish 明细未在本地；停食判例族五例已覆盖（大马哈/美洲西鲱/白北鲑/高首鲟+狼鱼 P04 侧）；其余 P05 行若有，补批对账（同 guarding 批 R10 尾批处理） |
| [需正文] 批量项 | 17 Tier B 文件的洄游阶段枚举/水体类型集合/Share 档位/Provocation Cue 构成/停食实证细读（逐文件 §5 列出）；Tier A 文件的 Profile 值域定值 |
| [需核对] 身份项 | 大西洋鲑 CSV 水温带 2–9℃（偏窄，疑源表口径——仅方向锚不引用数值）；白北鲑 CSV 英文名 Whitefish 通名；硬头鳟=虹鳟海型同种异行关系；湖拟鲤/常见拟鲤双行先例与本批无涉 |
| 无 UPSTREAM_CHANGE_EVENT | 本批未发现机制侧问题；表达层全部落在既有 census 族（SINGLE/PLAIN/HARD_GATED）/live 结构槽位（G-T1 路由向量+BA-T1+DynamicSpatialSlot+R-T1）内。R-T2 折叠与两层 reconciliation（§3 登记 1/3）是登记项不是机制缺陷主张 |

## 5. 验证记录（命令与输出原样）

命令（selftest）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/migration/validate_migration.py" --selftest
```

命令（真实交付包校验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/migration/validate_migration.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/migration"
```

输出：见下方两个代码块（原样粘贴，未改测试凑通过）。缺陷史：selftest 首轮抓出 fixture 自身真实缺陷 3 处（伪 token @Profile ×2 处、routed 拓扑判定过宽导致 no-route 基线误报、Profile 清单缺 ruleset token——另 2 个 mutation 用例串因 fixture 演进失配，属用例构造修正）；真实校验分三轮抓出真实工件缺陷 2 类 3 处（atlantic_salmon.md §0 引用 G2 判语原文带出禁词 ×1；northern_pike_spawn.md 先例引用误用 @ 前缀 ×2 处——§2.3 与 §0 各一，分两轮修复）——均修复工件而非改校验器。

### selftest 输出

```
[OK  ] baseline (routed) passes unchanged
[OK  ] baseline (no-route) passes unchanged
[OK  ] HEADER fires on missing NOT AUTHORITY
[OK  ] HEADER fires on missing BATCH_ID line
[OK  ] SECTIONS fires on missing Bake section
[OK  ] GROUPFORM fires when 1.1 loses both topologies
[OK  ] GROUPFORM fires when NO-ROUTE file gains a Special Group route
[OK  ] GROUPFORM fires when routed file loses MigrationReaction Group
[OK  ] SHARE fires on missing default route
[OK  ] SHARE fires on missing validation block
[OK  ] SHARE fires on non-@ MigrationReaction share parameter
[OK  ] REFS fires on undeclared ruleset reference
[OK  ] BAKEFAM fires on value outside closed enum
[OK  ] BAKEFAM fires on missing BakeTemplate row
[OK  ] FAMCTX fires on SINGLE carrying CombineRule row
[OK  ] FAMCTX fires on PLAIN missing Factor2 row
[OK  ] FAMCTX fires on GATED missing SurfaceGate row
[OK  ] PREMBIND fires on missing FactorBinding row
[OK  ] PREMBIND fires on binding without premise
[OK  ] REACTPATH fires on missing suppression statement
[OK  ] REACTPATH fires on missing structural Feeding closure
[OK  ] RT1OFF fires on missing Reaction-slot-OFF marker
[OK  ] QUALITYCOV fires when binding table misses a routed Group
[OK  ] PROFILES fires on used-but-unlisted token
[OK  ] PROFILES fires on listed-but-unused token
[OK  ] BAN fires on forbidden phrase LifecycleCohort
[OK  ] BAN fires on forbidden phrase Runtime Stage Selector
[OK  ] BAN fires on unannotated merge phrase in fence
[OK  ] STRUCT fires on stray table
[OK  ] STRUCT fires on unknown bake config field
[OK  ] exempt INSUFFICIENT_LOCAL_EVIDENCE file only needs header markers
== selftest ==
SELFTEST PASS
```

### 真实交付包校验输出

```
[PASS] alewife.md
[PASS] american_shad.md
[PASS] arctic_char.md
[PASS] atlantic_cod.md
[PASS] atlantic_salmon.md
[PASS] atlantic_tarpon.md
[PASS] brook_trout.md
[PASS] chinook_salmon.md
[PASS] chum_salmon.md
[PASS] coho_salmon.md
[PASS] common_chub.md
[PASS] ide.md
[PASS] inconnu.md
[PASS] lungfish_aestivation.md
[PASS] northern_pike_spawn.md
[PASS] prussian_carp.md
[PASS] sockeye_salmon.md
[PASS] swordfish_diel.md
[PASS] vendace.md
[PASS] walleye_spawn.md
[PASS] white_sturgeon.md
== result ==
PASS (21 species files, 0 violations)
```

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器纯标准库，内部强制 stdout UTF-8。

## 6. 边界声明

- 本包只做 Migration/生活史系（P05）四面的生产级表达（census 族投影配置 + 中文伪脚本完全展开；停食族 Response 双 Path 展开）；表达验证通过 ≠ 机制 promotion ≠ Freeze；不覆盖 live 主页 / census registry 任何 Verdict。
- 全部数值不冻结（@参数引用，Profile 层定值）；SINGLE 链无 combine 步（族域边界）；PLAIN/GATED 链 CombineRule 拓扑族固定、数学 OPERATOR UNDEFINED 待机制侧；R-T2 折叠、停食 Cap/关闭双形态、census↔live 两层 reconciliation 全程 OPEN 可见。
- 每文件 §5 记录使用/放弃的自由度（含归族裁决权移交、同属判例不继承、state switch 不程序化、DRY 退化体不建体、滤食 P03 复核线、amphidromous 状态轴差异）。
- 未 commit（提交由 Coordinator / 用户决定）。

BATCH_ID: REP-FULL-MIGRA-001

---

## REP-FULL-MIGRA-REV-001 验收记录（2026-09-11）

- verdict: **ARTIFACT_APPROVE**（全批首次直接通过）。
- minor-1：行级 Pattern 抽核 2/2=P01+P05 复合——文件 R-T1 Feeding Path 覆盖 P01 面无 false fit；live 可批量核 [需核对]。
- minor-2：ide.md 批次归属 live 闭合。minor-3：数字修正。minor-4：停食族 Reaction 通道来源=FR3 triage 判例层非 Story 行级标签。
