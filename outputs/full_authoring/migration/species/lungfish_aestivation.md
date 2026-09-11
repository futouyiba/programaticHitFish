# 南美肺鱼（South American Lungfish｜Lepidosiren paradoxa）｜湿干两态蛰伏切换四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批：蛰伏组） |
| Story | FISH-R05-南美肺鱼-Aestivation-State-Switch（Story 页 3d7a4137d23681f9b62bdd65f610ffb4；census CENSUS-B0 快照全文在案）。**文件分工声明**：同一 Story 的护巢面（P04 语义映射 WET 限定）已由 Guarding 批承载（outputs/full_authoring/guarding/species/lungfish.md——Guarding Group 路由+BA-GUARD-ANCHOR-GATE+Defense-only）；本文件承载 P05 主面——湿/干两态 state switch 与蛰伏（DRY）态，两文件互补不重复，批间关系登记 README §3.6 |
| 冻结 Pattern | P05（census B0 stories.jsonl 快照；FR 冻结侧仅 P05——护巢段 P04 映射是 census 跨层 caveat，归 guarding 批文件） |
| 物种属性锚 | fish-reference-20260908：水温 24–28℃、最适 26℃、demersal、夜间活跃、杂食性、孤僻、淡水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B0 全四面判定快照 + 盲程序体冻结；DRY 蛰伏态程序 AMBIGUOUS/TAR-01 原样携带） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；吸吮 typed；Reaction 槽 OFF）；DRY 蛰伏态响应由 premise 层 rate 参数抑制，无 body（census 冻结判语） |
| census 程序 | P-LUN-BAKE-WET（HARD_GATED_FACTOR_COMBINE 成员，registry v4 在案：水面可达硬门+因子组合）+ P-LUN-BAKE-AESTIVATION（AMBIGUOUS，TAR-01）；P-LUN-RESP-FEEDING（TYPED 族成员，吸吮 evaluator） |

## 0. 上游语义与蛰伏形态

- 蛰伏形态：湿/干两态时序互斥、个体级切换（season_regime=WET/DRY 由 world 水文上游决定，个体不同时双态）；无并发供给拆分（census Group 面 NO_SURFACE_EFFECT 原样——FishMode=Weak）。
- **state switch 判例（census 冻结独立结论，本批核心判语）**：蛰伏态程序体角度，state switch 本身是 world/lifecycle-owned premise，不是 surface 自有程序——与 FR3 语义判例一致。即：两态切换不进任何面的程序体，由 premise 配置承载。
- Bake 面：湿态（WET）=HARD_GATED 因子组合（水面可达是绝对约束而非相对寻优——专性气呼吸 air_breathing=OBLIGATE 物种常量；census P-LUN-BAKE-WET registry 成员）；干态（DRY）=蛰伏 anchor 退化体，**AMBIGUOUS 不建体**（playable S10=EO 存疑，TAR-01 裁决队列——本文件不冒充 playable）。
- Response 面：常态（WET）=TYPED 吸吮 evaluator（census P-LUN-RESP-FEEDING）；DRY 蛰伏态响应由 premise 层 rate 参数抑制，无 body（census 冻结判语原样——蛰伏不是 Response 程序结构差异，是 premise 级抑制）。
- Quality 面：census NO_SURFACE_EFFECT（吸吮口器=typed evaluator 参数；腹鳍供氧=guard condition 参数，均归 guarding 批文件）。
- 表达超集说明：无（本文件未超出 census 冻结程序语义范围；DRY 态 AMBIGUOUS 状态全程可见）。
- **判断顺序（REP-ORDER-FIX-003 顺序还原，census 冻结语义层推导——GATED 族链序保留）**：本鱼 Bake 属 census HARD_GATED 族（水面可达硬门前置+因子集），族 canonical 本身有顺序（gate 前置——census 冻结判语「水面可达是绝对约束而非相对寻优」），链序还原=gate 前置原样+**硬门判定显式 EARLY_RETURN 化**（水面不可达=程序级出局）+ premise 门（WET/DRY）语义显式化（DRY=不进入本程序——程序级 early return 形态，premise 配置级非 body 分支）+ 每槽因子评估展开为三档分档槽判定（preferred=全额/tolerated=削减不清零/excluded=槽值出局——族域内槽无独立 gate 语义，出槽值仍进 COMBINE）。Response 面 DECIDE_RESPONSE 档位展开+DRY 门控 early return 语义显式化。档位成员与阈值全 Profile 值域不冻结 [需正文]。

Profile 引用清单：@LungfishSurfaceAccessGate @LungfishWetFactorSetProfile @LungfishAestivationSuppressionRate @LungfishPreyFields @LungfishDietClasses @LungfishSizeWindow @LungfishNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样——湿/干两态时序互斥、个体级切换 world 水文决定，无并发供给拆分；state switch 是 world/lifecycle-owned premise，不是 surface 自有程序）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| LungfishAestivation_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件
（season_regime premise=WET/DRY 由 world 水文上游决定，不构成本面路由输入——
两态时序互斥、个体级切换，state switch 是 world/lifecycle-owned premise，
不是 surface 自有程序——census 冻结独立结论原样）

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由；WET 态全额、DRY 态由 premise 层抑制实际生成）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例；DRY 蛰伏期的可钓性抑制不落在 Share——归 premise 层 rate，§3.2）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group，WET 态绑定；census HARD_GATED 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-GATED（本批投影标签＝census HARD_GATED_FACTOR_COMBINE，registry v4；硬门前置+因子集→固定组合；本鱼湿态 P-LUN-BAKE-WET 为族在案成员；**§2.2 已顺序还原（REP-ORDER-FIX-003）：gate 前置原样+硬门 EARLY_RETURN 显式化+槽内三档——登记 README §7**） |
| SurfaceGate | @LungfishSurfaceAccessGate（专性气呼吸水面可达硬门：水面不可达即剔除——HARD GATE 而非相对排序，与 CRR 判别结构不同，census 冻结判语） |
| FactorSet(typed) | 静水偏好/塘体结构/猎物资源（typed 因子集——census P-LUN-BAKE-WET 冻结因子集） |
| FactorBinding | lifecycle premise：season_regime 配置级切换（WET=本程序绑定实例 / DRY=蛰伏退化体不建体——census AMBIGUOUS/TAR-01 原样，见 §2.3） |
| HabitatFactorProfile | @LungfishWetFactorSetProfile |
| CombineRule | Template-fixed COMBINE_WEIGHTED（族常量拓扑；数学 OPERATOR UNDEFINED 待机制侧——census open_semantics 因子间顺序 unordered） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@LungfishPreyFields；diet_classes=@LungfishDietClasses；size_window=@LungfishSizeWindow） |
| LiveLayerProjection | B-T1 Independent Factor Set + Optional Gate（§13.2 结构族：Optional Gate 槽即硬门——两层 reconciliation OPEN，README §3 登记） |

### 2.2 中文伪脚本（完全展开；WET 态）

```plain text
【顺序还原声明｜REP-ORDER-FIX-003】本伪脚本按 authoring_work_standards §5.1 顺序还原
（GATED 族链序保留形）：census HARD_GATED 族 canonical 本身有顺序（硬门前置——冻结
判语「水面可达是绝对约束而非相对寻优」），gate 前置原样；还原内容＝硬门判定显式
EARLY_RETURN 化（水面不可达=程序级出局）+ WET/DRY premise 门语义显式化（DRY=不进入
本程序——程序级 early return，premise 配置级非 body 分支，state switch 判语原样）+
每槽因子评估展开为三档分档槽判定（preferred=全额/tolerated=削减不清零/excluded=
槽值出局——族域内槽无独立 gate 语义，出槽值仍进 COMBINE）。档位成员=Profile 值域
不冻结 [需正文]。

读取 当前水文季节 premise（WET / DRY——world 水文上游决定）
如果 premise = DRY：
    蛰伏退化体不建体（census AMBIGUOUS/TAR-01——见 §2.3）——
    不进入本程序（程序级 EARLY_RETURN：DRY 态下本 Bake 程序整体不激活；
    这不是 body 内阶段分支——premise 配置级选择程序绑定实例，census 冻结判语原样）
否则（premise = WET，本程序绑定实例）：

构建 当前水域可访问集
读取 当前格子的水面可达事实（专性气呼吸——air_breathing=OBLIGATE 物种常量）
读取 当前格子的静水/流速事实
读取 当前格子的塘体结构事实
读取 当前格子的猎物资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@LungfishPreyFields 绑定的杂食谱 prey class 生物量，
      经 diet_classes=@LungfishDietClasses 食性过滤
      与 size_window=@LungfishSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 GATE_HARD_VIABILITY（硬门前置——顺序还原后显式 EARLY_RETURN 形）：
    如果 当前点水面不可达（@LungfishSurfaceAccessGate 不成立）：
        返回 0（EARLY_RETURN：从可访问集中剔除该目标——硬门，非相对排序；
        与 CRR 判别结构不同——水面可达是绝对约束而非相对寻优，census 冻结判语；
        本步即族 canonical gate 步的 early return 显式化，拓扑不变）

槽 2 EVAL_HABITAT_FACTOR_TYPED（静水偏好，分级命中）：
    用静水/流速事实查询 @LungfishWetFactorSetProfile 的静水分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 静水条件 ∈ 静水档（preferred 槽）：
        StillwaterFit = 全额
    否则如果 ∈ 缓流过渡档（tolerated 槽）：
        StillwaterFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（急流排除档）：
        StillwaterFit = 出局槽值（excluded——非独立 EARLY_RETURN，
        族域内槽无独立 gate 语义，出槽值仍进 COMBINE）

槽 3 EVAL_HABITAT_FACTOR_TYPED（塘体结构，分级命中）：
    用塘体结构事实查询 @LungfishWetFactorSetProfile 的结构分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 塘体结构 ∈ 充分档（preferred 槽）：
        StructureFit = 全额
    否则如果 ∈ 有限档（tolerated 槽）：
        StructureFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（无结构档）：
        StructureFit = 出局槽值（excluded——同上族域边界）

槽 4 EVAL_RESOURCE_FACTOR_TYPED（猎物资源，分级命中）：
    用猎物资源事实查询 @LungfishWetFactorSetProfile 的资源分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 猎物可得性 ∈ 丰档（preferred 槽）：
        PreyFit = 全额
    否则如果 ∈ 贫档（tolerated 槽）：
        PreyFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（无资源档）：
        PreyFit = 出局槽值（excluded——同上族域边界）

COMBINE_WEIGHTED：
    按模板固定组合规则合并 StillwaterFit / StructureFit / PreyFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（census HARD_GATED 族 COMBINE_WEIGHTED
    数学未冻结；因子间顺序 unordered，open_semantics 原样）

返回 SpatialDistributionWeight（gate 后因子集结束：硬门 EARLY_RETURN+槽内分级命中；
gate 后相对寻优属 CRR 族域 forbidden；本程序硬门=绝对可行性约束——族 canonical
拓扑不变，档位化展开登记 README §7）
```

### 2.3 DRY 蛰伏态｜退化体不建体（显式声明）

census P-LUN-BAKE-AESTIVATION 判定 **AMBIGUOUS**（blind_hash 12890e5fdca83c26 在案）：干季蛰伏=burrow anchor 退化体；playable 存疑（S10=EO）——TAR-01 人类裁决队列未闭合。本文件不为其建体、不预判 playable；TAR-01 裁决到达后：判 playable=新增 DRY 配置实例（结构变更需重审）；判 not playable=本节维持登记。**state switch 本身（WET↔DRY）是 world/lifecycle-owned premise，不进任何面程序体**（census 冻结独立结论——与 FR3 语义判例一致，本批蛰伏组的组级判语）。

### 2.4 live 层投影声明

live 结构族 B-T1 Independent Factor Set + Optional Gate（§13.2）的 Optional Gate 槽即水面可达硬门（B-T1 可合法吸收清单「Reproductive Anchor: Eligibility Gate」「Cold Refuge: DO Gate」同款）；census HARD_GATED 族与 live B-T1+Gate 的对齐（HRQ-03 与 PLAIN 的 extend-vs-split）归两层 reconciliation（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影；WET 态绑定）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding；吸吮 typed evaluator；DRY 态由 premise 层 rate 抑制） | @LungfishNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前水文季节 premise（WET / DRY）
如果 premise = DRY：
    蛰伏态响应由 premise 层 rate 参数抑制（@LungfishAestivationSuppressionRate），
    无 body——蛰伏不是 Response 程序结构差异，是 premise 级抑制
    （census 冻结判语原样；DRY 态不评价任何 Response——
    程序级 EARLY_RETURN：DRY 态下本 Response 程序整体不激活，
    这不是 body 内阶段分支——state switch 是 world/lifecycle-owned premise）

否则（premise = WET）：
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @LungfishNormalFeedingProfile（吸吮式 typed food evaluator——census 判语）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-003 展开）：
    按三档判定 FoodEvaluation（档位成员=@LungfishNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
（护巢期 DUAL_PATH 护卫响应归 Guarding 批文件（guarding/lungfish.md §3）——
本文件只承载 P05 主面，两文件互补）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；census Quality 面 NO_SURFACE_EFFECT |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（恒为 NormalFeeding——无 Special Group）

对每个品质：
    读取该品质的 GroupEligibilityFactor（查 @NeutralEligibility）
    读取该品质的 GroupAffinityFactor（查 @NeutralAffinity）
    读取当前 lure / bait / hook / context 等原始事实
    评价所有适用的 Presentation Modifier / Context Modifier（只读原始事实）

    原始品质权重 =
        基础品质权重
        × GroupEligibilityFactor
        × GroupAffinityFactor
        × 所有适用 Modifier

汇总所有品质的原始权重

如果总权重 > 0：
    统一归一化
    输出 QualityWeightVector
否则：
    当前 FishQuality × FishGroup 不产生可实现候选
```

## 5. 自由度、边界与放弃项

- 使用的自由度：census HARD_GATED 族投影标签与冻结因子集/硬门实例（P-LUN-BAKE-WET registry 在案成员）；Profile 命名；**顺序还原的 GATED 形态（REP-ORDER-FIX-003：gate 前置原样+硬门 EARLY_RETURN 显式化+WET/DRY 程序级门语义显式化+槽内三档+Response 档位展开——推导依据 §0 判断顺序行）**；槽序 unordered、Combine 拓扑族固定。
- 放弃的自由度：(1) DRY 蛰伏态建体（census AMBIGUOUS/TAR-01 未闭合——不冒充 playable，裁决到达后结构变更需重审）；(2) state switch 程序化（world/lifecycle-owned premise，census 冻结独立结论——不进任何面程序体；程序级门=premise 配置级选择程序绑定实例，非 body 分支）；(3) DRY 态 Response body（premise 层 rate 抑制，census 判语原样）；(4) 槽内独立 gate 语义（族域内槽无独立 gate——excluded 档落槽值出局进 COMBINE）；(5) 护巢面表达（归 Guarding 批文件，P04 语义映射 caveat 随批）；(6) 合并算子数学（OPERATOR UNDEFINED 待机制侧）；(7) 数值与 Profile 值域不冻结（含档位成员）。
- 跨批登记：同一 Story 双批分工（本文件=P05 湿干两态主面 / guarding 批=护巢面）——两文件引用同一 census 快照的不同程序子集，WET 态 Normal 面 Bake 语义一致（本批 BA-MIGRATION-GATED 投影 / guarding 批 BA-LUN-WET-GATED-FACTORS 命名），批间标签 reconciliation 登记于本批 README §3.6。
- [需核对] TAR-01 裁决状态（DRY playable）；蛰伏抑制 rate 值域（Profile 层）。

BATCH_ID: REP-FULL-MIGRA-001
顺序还原修复批次：REP-ORDER-FIX-003（§0/§2/§3/§5 修改；Bake 硬门 EARLY_RETURN 显式化+WET/DRY 程序级门语义+槽内三档，Response 档位展开+DRY 门控 early return 显式化）
