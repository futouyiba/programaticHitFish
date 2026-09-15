# P02 Resource Patch 补批｜5 种

**Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED**

## 批次概览

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 7 批：P02 Resource Patch→Discrete Target→TargetFeeding 系——grazing 批排除线兑现） |
| 样本口径 | 5 文件＝census B1 全部 frozen P02 Story（4 条 Tier A）+ handoff 点名 Tier B 一条（鲤）。P02 判别轴（handoff 指定口径）：食物载体=离散资源斑块（对照 P06=连续基质）。grazing 批排除表 K3 行所称「Pattern 标签未在本地快照」经核对 census B1 stories.jsonl 为信息不全——黑鼓鱼/小口黑鲈 frozen P02 快照在案，本批据 census 补全收录 |
| 基线 | SNAPSHOT_ONLY（P02 Pattern 页正文不在本地；按 handoff 口径 + census frozen_patterns 快照双锚表达） |
| 表达读数 | Group：5/5 无路由显式声明（census 4/4 Group 面 NO_SURFACE_EFFECT——判语各异但结论同构：饵区鱼多≠Group / 竞争占位≠Mode / 痕迹持续≠Mode/Field / 跟随≠RelationalConflict）——L_group 无增长。Bake：BA-P02-SINGLE ×4（草鱼/黑鼓鱼/小口黑鲈 Tier A + 鲤 Tier B 骨架——SINGLE 族 resource_patch 轴 P02 实例群）+ BA-P02-PLAIN ×1（褐鳟位置竞争——PLAIN 族第 3 成员 patch+rank 2 槽）——**零 PATCH**（handoff 预判「PATCH 族 canonical body 可复用」与 census 冻结判定 3 SINGLE+1 PLAIN 分歧，按 census 表达、分歧登记不闭合）；投影标签封闭枚举 {SINGLE, PLAIN}，PATCH 标签本批不可表达（validator 钉死）；族边界进校验——census 侧 ΔL_bake=0（4 程序全部为 census B1 在案成员）。Response：5/5＝R-T1 单通道（P02 定义即→TargetFeeding 非 FieldFeeding；褐鳟 conflict path 证据不足不建）——L_response 无增长。Quality：全部 QT-1。新列结构：零 |
| 数值状态 | 全部 @参数引用；SINGLE 族程序无 combine 步（族域）；PLAIN 族 CombineRule 数学 OPERATOR UNDEFINED 待机制侧 |
| 验证结果 | validate_patch.py：selftest 32 用例 PASS（含 BAKEFAM fires on PATCH label 专项——枚举外值+不可表达标签双重钉死；PLAIN 正例控制）；真实交付包 5 文件 0 违规 PASS（首轮物种校验零缺陷——validator 先行策略） |
| 跨批登记 | census 族↔live 两层 reconciliation OPEN；小口黑鲈 Response 两层登记（coverage delta #11 live 层 RR-T1 Optional Reaction 读法 vs census 程序体无该步——按 census 表达不静默选层）；HRQ-B1-02 PATCH↔SINGLE 边界 4 当事成员本批占 3；褐鳟 rank 因子双轴待批（HRQ-B1-04+TAR-05）；世界侧事实供给义务（prebait_patches / disturbance_events / feeding_traces）；同种多 Story 分工互指闭合（褐鳟双文件/小口黑鲈双文件/草鱼-白化草鱼 L1/鲤-品系 L1）；无 UPSTREAM_CHANGE_EVENT |
| 审核 | **REP-FULL-P02-REV-001 verdict: ARTIFACT_APPROVE**（第四批直接通过；核心声明经 census B1 冻结快照第一手证据独立成立；MINOR-1 计数修正） |

## Species 汇总表（5 文件）

| # | 文件 | 鱼（学名） | Story | 证据档 | Bake（census 族投影） | Response |
|---|---|---|---|---|---|---|
| 1 | grass_carp.md | 草鱼（Ctenopharyngodon idella） | B01-S53｜植食资源与预投饵斑块（census CENSUS-B1-GRB 快照全文） | A | BA-P02-SINGLE（SINGLE 族首成员 P-B1-GRB-BAKE，factor=resource_patch(plant+prebait)——首实例） | R-T1 TYPED（P-B1-GRB-RESP，面包/玉米取向参数） |
| 2 | brown_trout_position.md | 褐鳟·位置竞争面（Salmo trutta） | B01-S14｜摄食位置竞争与中心—边缘资源分配（census CENSUS-B1-BRT；confidence MEDIUM 原样携带） | A | BA-P02-PLAIN（PLAIN 族第 3 成员 P-B1-BRT-BAKE，patch+rank 2 槽——本批唯一 PLAIN；HRQ-B1-04 双轴待批） | R-T1 TYPED（P-B1-BRT-RESP；conflict path 不建） |
| 3 | black_drum.md | 黑鼓鱼（Pogonias cromis） | B01-S46｜翻底坑与泥云作为持续觅食痕迹（census CENSUS-B1-DRU；coverage delta #5） | A | BA-P02-SINGLE（P-B1-DRU-BAKE，factor=resource_patch(benthic_prey)） | R-T1 TYPED（P-B1-DRU-RESP，P02 底栖取向） |
| 4 | smallmouth_follow.md | 小口黑鲈·跟随翻底面（Micropterus dolomieu） | B01-S32｜跟随翻底动物获取被惊出的猎物（census CENSUS-B1-SMA；coverage delta #11） | A | BA-P02-SINGLE（P-B1-SMA-BAKE，factor=resource_patch(disturbance_revealed)） | R-T1 TYPED（P-B1-SMA-RESP；两层登记：live 层 RR-T1 Optional Reaction 读法） |
| 5 | common_carp.md | 鲤（Cyprinus carpio） | FISH-R02-S08｜底质翻拱与资源斑块（coverage delta #23 吸收判定在案；Story 正文 [需正文]） | B | BA-P02-SINGLE 骨架（Tier B 投影，归族裁决移交） | R-T1 骨架（Tier B） |

排除项要点：鳜鱼 P02 侧（census 单一程序体已被 normal 批全量承载，无独立四面程序体——登记项 1 转 Coordinator 对账）；青鱼/黄尾鲴/鲮（R04 成员补批域）；鳙鱼/大西洋鲱（field 批）；白化草鱼/鲤品系（L1 等效层单向从属）。

## 完整示例（Tier A 样板：grass_carp.md 全文）

> census SINGLE 族首成员（P-B1-GRB-BAKE，resource_patch 轴首实例）——含「预投饵斑块 vs 自然资源斑块」关键判别的表达答案。

# 草鱼（Grass Carp｜Ctenopharyngodon idella）｜Resource Patch 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（Resource Patch 系＝P02 补批 第 7 批） |
| Story | B01-S53｜草鱼｜植食资源与预投饵斑块（census CENSUS-B1-GRB 快照全文在案；Story 页 3d6a4137d23681168a18f10342e09a94） |
| 冻结 Pattern | P02（census B1 stories.jsonl 快照 frozen_patterns；handoff 要求核对的行级 Pattern relation——快照层冻结在案，live 行级 SNAPSHOT_ONLY 见 README §4） |
| 物种属性锚 | fish-reference-20260908 行 185：benthopelagic、植食性、早晨活跃、温和、potamodromous、营养级 2（仅方向锚） |
| 基线 | SNAPSHOT_ONLY（live 转录 2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B1 全四面判定快照 + 盲程序体冻结 P-B1-GRB-BAKE/P-B1-GRB-RESP） |
| 变体声明 | 无路由条件原子（显式声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 程序 | P-B1-GRB-BAKE（SINGLE 族首成员：resource_patch 轴首实例，factor=resource_patch(plant+prebait)；盲体首步 op=EVAL_RESOURCE_PATCH）+ P-B1-GRB-RESP（TYPED 标准成员：面包/玉米取向参数） |
| 相邻文件 | field 批 albino_grass_carp.md（白化草鱼 L1 等效层）以本文件为本体——单向从属 |

## 0. 上游语义与资源斑块形态

- P02 判别轴（本批口径）：食物载体=离散资源斑块（Resource Patch→Discrete Target→TargetFeeding），对照 P06=连续基质处理——判别轴=食物载体，非栖息带或食性。
- 资源构成：植食资源+预投饵斑块双构成（census 盲体实例常量 resource="aquatic_plant+bait_patch"，原样）。
- 关键判别（预投饵斑块 vs 自然资源斑块——handoff 点名）：census 判定两者为同一 Bake 形态——同族（SINGLE）同轴（factor_type=resource_patch）同一因子实例；差异不在鱼程序结构，而在世界侧事实供给层：prebait_patches（玩家预投饵行为产生的资源斑块）是世界侧事实供给义务（环境资源 owner 保存；census resolver_tests 登记），自然资源斑块同为上游事实。玩家行为产生资源斑块不购买新 Bake 结构、不购买 Mode/Group。
- Group 面：census NO_SURFACE_EFFECT 原样（Story Competing 明言：饵区鱼多不证明必须 Group；P02：Patch 不自动购买 Mode/Group）。
- Response 面：TYPED 标准成员（P02 语义=patch 背景下离散 TargetFeeding；面包/玉米取向参数——参数级，无新拓扑）。
- Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无。

Profile 引用清单：@GrbHerbivorePatchProfile @GrbPreyFields @GrbDietClasses @GrbSizeWindow @GrbNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT 原样：饵区鱼多不证明必须 Group，P02 Patch 不自动购买 Mode/Group）。

### 1.2 分群结果（5 列固定）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Grb_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P02-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT；2 步单 typed 因子→归一化——本标签本批 4 文件之一） |
| FactorType(typed) | resource_patch：植食资源+预投饵斑块轴（census P-B1-GRB-BAKE 实例常量 resource="aquatic_plant+bait_patch"；预投饵斑块 prebait_patches=世界侧事实供给义务，resolver_tests 登记非鱼程序结构） |
| FactorBinding | 常年绑定（无 lifecycle/season premise 切换证据） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@GrbPreyFields；diet_classes=@GrbDietClasses；size_window=@GrbSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot（live §11.4 预投饵先例——玩家投放资源斑块的槽位语义；两层 reconciliation OPEN） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的植食资源+预投饵斑块轴事实
    （双构成：水生植物资源事实 + prebait_patches 玩家预投饵斑块事实——
      两者同为世界侧上游事实；预投饵斑块的保存与衰减归环境资源 owner）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@GrbPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@GrbDietClasses 食性过滤
      与 size_window=@GrbSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR：
    用植食资源+预投饵斑块轴事实查询 @GrbHerbivorePatchProfile
    得到 HerbivorePatchFit（单 typed 因子评估；
      census 盲体首步 op=EVAL_RESOURCE_PATCH——族判同的实例化名，同构）

NORMALIZE_WEIGHT：
    对 HerbivorePatchFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；typed context 中间步属 PATCH 族域，多因子组合属 PLAIN 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层（BA-T1+DynamicSpatialSlot）reconciliation OPEN；预投饵斑块的 §11.4 先例是 live 侧槽位语义，不是 census 族晋升。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @GrbNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）
读取 局部食物背景 premise（resource_context 上游 fact——patch 背景参数）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @GrbNormalFeedingProfile
    （面包/玉米等饵取向参数——census 盲体实例常量 bait="bread/corn"；
      P02 语义：patch 背景下的离散目标食物评价，参数级无新拓扑）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
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

- 使用的自由度：census SINGLE 族投影标签与 typed 因子实例语义（resource_patch(plant+prebait)——census 冻结实例常量原样）；Profile 命名；伪脚本步序（canonical 两步固定）；预投饵资源的世界侧归属层选择（census 判语照录）。
- 放弃的自由度：(1) 饵区聚集的 Group 化（census 判语：饵区鱼多不证明必须 Group，Patch 不自动购买 Mode/Group）；(2) 预投饵斑块的鱼侧程序化（世界侧事实供给义务——玩家投放语义不进鱼 Bake/Response 结构；live §11.4 槽位归属两层 reconciliation OPEN）；(3) 数值与 Profile 值域不冻结；(4) PATCH↔SINGLE optional_context 边界（HRQ-B1-02）与 census↔live 两层 reconciliation 的裁决权（归机制侧）。
- CSV 习性锚仅方向锚；potamodromous 若 Story 正文证实洄游期因子切换，照 MGC/CHB 先例按 lifecycle premise 配置级处理，不购买 Migration Group。

BATCH_ID: REP-FULL-P02-001

（示例完）

## Provenance

- 本地路径：`A:\Projs\FCF-Harness-Handoff\programaticHitFish\outputs\full_authoring\patch\`（README.md + validate_patch.py + species\ 5 文件）
- GitHub：https://github.com/futouyiba/programaticHitFish （commit `ebc4ba7`，工作树干净）
- 审核 verdict：REP-FULL-P02-REV-001 = **ARTIFACT_APPROVE**。转录批次：2026-09-11
