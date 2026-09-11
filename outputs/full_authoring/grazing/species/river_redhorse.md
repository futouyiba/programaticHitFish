# 河红马鱼（River Redhorse｜Moxostoma carinatum）｜Grazing 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GRAZE-001（Grazing/底质系＝P06 全样本 第 2 批） |
| Story | FISH-R07 河红马鱼（coordinator 分批名单：R07 亚口科四条之一（REV-001 M1 修正：原名单误标 R06）；Story 页未在本地快照——身份锚为 fish-reference-20260908 行及其 Notion 资料页 3d5a4137d2368161b274d98b84915dd5；Story 正文 [需正文]） |
| 冻结 Pattern | P01 行级主 relation（live 实测，REV-001 M1）+ P06 merge-key pending（R07 FR3 DiscoveryBatch 附标签层——Cross-Batch 执行未落地） |
| 物种属性锚 | fish-reference-20260908：水温 11–19℃、最适 15℃、demersal、早晨活跃、肉食性、摄食类型=hunting macrofauna (predator)、追猎（性格）（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier B（coordinator 分批名单 + CSV 方向锚；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出；归族裁决归 census 侧判同（README §3 登记 2） |

## 0. 上游语义与底质处理形态

- 底质处理形态（方向）：亚口科底质连续吸食型捕食——底质大中型无脊椎（CSV 肉食性、hunting macrofauna、demersal）的吸食处理；「hunting macrofauna」在亚口科语境＝底栖大型无脊椎摄取（吸食式，非追击式 Pursuit）——「追猎」性格为档案方向值，程序化映射 [需正文]（若有追击语义属 Reaction/Encounter 面，不在本 Story 程序）。
- 食性注记：CSV 摄食类型=hunting macrofauna (predator) 方向锚——底质耦合的资源摄取（软体动物/底栖昆虫幼虫构成 [需正文]）。
- Group 面：按分批口径无供给拆分；若正文出现互斥供给证据则升级重审（结构变更非 Profile 重绑定）。
- 表达超集说明：Tier B 骨架按 P06 底质单因子形（census SINGLE 族）给出，仅容纳 CSV+体构方向；归族改判（PATCH/PLAIN）＝结构变更需重审；正文判无程序语义即撤回本文件。
- **判断顺序（REP-ORDER-FIX-001 顺序还原，CSV 方向级推导 [需正文]）**：判断链＝底层水层定位 → 底质栖境档位 → 大型无脊椎资源档位 → 归一化。推导来源：CSV 栖息带 demersal（底栖特化——硬定位：非底层=出局）＋肉食性 hunting macrofauna（亚口科语境=底栖大型无脊椎吸食摄取——栖境可得性先于猎物丰度评估）。分级命中：栖境档与资源档各三档（最适应=全额/可接受=削减不清零/排除=出局），档位成员与阈值全 Profile 值域不冻结 [需正文]。CSV 时段（早晨活跃）/水温锚未入链；「追猎」性格维持档案方向值不程序化。

Profile 引用清单：@RiverRedhorseSubstratePatchProfile @RiverRedhorseSubstrateSpatialProfile @RiverRedhorseSubstratePreyFields @RiverRedhorseDietClasses @RiverRedhorseSizeWindow @RiverRedhorseNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| RiverRedhorse_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生底质程序｜配置表（NormalFeeding Group）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-SUBSTRATE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；Tier B 骨架——归族裁决归 census 侧判同；**§2.2 已顺序还原（REP-ORDER-FIX-001）：early return 链+分级命中，分歧登记 README §7**） |
| FactorType(typed) | resource_patch：底质大型无脊椎资源（CSV 方向：肉食性 + hunting macrofauna + demersal——亚口科吸食式底栖摄取；软体动物/底栖昆虫构成 [需正文]） |
| FactorBinding | 常年绑定 [需正文]（CSV 无迁徙注记——若正文证实季节/阶段切换则由上游 premise 配置处理） |
| SubstratePatchProfile | @RiverRedhorseSubstratePatchProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@RiverRedhorseSubstratePreyFields；diet_classes=@RiverRedhorseDietClasses；size_window=@RiverRedhorseSizeWindow） |
| LiveLayerProjection | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot=@RiverRedhorseSubstrateSpatialProfile（coverage delta K3 吸收读法：benthic prey class + 基质 Factor；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-001】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝底层水层定位 → 底质栖境档位 → 大型无脊椎资源档位 → 归一化；每步分级命中
（全额/削减/出局），出局即 EARLY_RETURN。顺序为 CSV 方向级推导
（demersal 硬定位＋底栖大型无脊椎吸食摄取，[需正文]）——Story 正文到达后校准，
顺序/档位差异本身=LogicTemplate 判据（census 侧 SINGLE 族重跑=work standards
§5.4 行动项，分歧登记 README §7）。

读取 当前格子的水层带位置
读取 当前格子的底质类型（砾/砂/泥）
读取 当前格子的基质资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@RiverRedhorseSubstratePreyFields 绑定的底栖大型无脊椎 prey class 生物量，
      经 diet_classes=@RiverRedhorseDietClasses 食性过滤
      与 size_window=@RiverRedhorseSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（常年绑定；切换若正文证实则由上游 premise 配置切换，
    不在本 body 内设分支）

第 1 步 底层水层定位（GATE_ZONE——demersal 底栖特化硬定位）：
    用水层带位置查询 @RiverRedhorseSubstrateSpatialProfile 的水层分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 水层 ∈ 底层带档：
        进入第 2 步
    否则：
        返回 0（EARLY_RETURN：demersal 底质吸食定位不在非底层分布——
        底栖特化硬判定；若正文证实会离底取食则档位化=结构变更需重审）

第 2 步 底质栖境档位（分级命中——大型无脊椎栖境可得性）：
    用底质类型查询 @RiverRedhorseSubstratePatchProfile 的底质分档槽
    （软体动物/底栖昆虫栖境方向；档位成员=Profile 值域不冻结 [需正文]）
    如果 底质 ∈ 大型无脊椎栖境档（preferred 槽）：
        SubstrateTier = 全额保留
    否则如果 底质 ∈ 有限栖境档（tolerated 槽）：
        SubstrateTier = 削减（× Profile 衰减参数——削减但不清零）
    否则（无栖境档）：
        返回 0（EARLY_RETURN：无大型无脊椎栖境的底质出局）

第 3 步 大型无脊椎资源档位（EVAL_TYPED_FIELD_OR_FACTOR，分级命中）：
    用基质资源事实查询 @RiverRedhorseSubstratePatchProfile
    （单 typed 因子评估展开为三档分档槽=Profile 值域不冻结 [需正文]）
    如果 大型无脊椎可得性 ∈ 丰档（preferred 槽）：
        SubstratePatchIntensity = 全额强度
    否则如果 ∈ 贫档（tolerated 槽）：
        SubstratePatchIntensity = 削减强度（削减但不清零）
    否则（无资源档）：
        返回 0（EARLY_RETURN：无底栖大型无脊椎的格子出局）

第 4 步 NORMALIZE_WEIGHT：
    对 SubstrateTier × SubstratePatchIntensity 执行模板固定归一化
    （族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live 侧吸收读法＝BA-T1 底板 + DynamicSpatialSlot=@RiverRedhorseSubstrateSpatialProfile（REP-COVERAGE-DELTA-001 K3 吸收结构：benthic prey class + 基质 Factor）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @RiverRedhorseNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @RiverRedhorseNormalFeedingProfile（底栖大型无脊椎取向接受窗——CSV 方向锚）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-001 展开）：
    按三档判定 FoodEvaluation（档位成员=@RiverRedhorseNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
（连续底质吸食机会在本表达仍落离散钩饵 target——P02/P06 待检验判语原样携带）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

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

- 使用的自由度：SINGLE 族投影标签；typed factor 实例语义（底栖大型无脊椎方向，取自 CSV）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-001：demersal 硬定位先行、栖境档三档分级命中、early return 链——CSV 方向级推导 [需正文]）**；Bake 输入契约字段复用。
- 放弃的自由度：(1) 归族裁决权（同泰鲮）；(2) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(3) 合并算子（本程序无 combine 步；live 层组合算子 OPERATOR UNDEFINED 待机制侧）；(4) 「追猎」性格与 hunting 措辞的追击语义程序化（档案方向值；亚口科语境按吸食式摄取表达，追击语义若正文证实归 Reaction/Encounter 面）；(5) 水温/时段因子入链（CSV 锚无 Story 空间程序证据）；(6) 数值与 Profile 值域不冻结（含档位成员与阈值）。
- [需正文] 底栖无脊椎构成（软体动物/昆虫幼虫）、底质类型偏好、判断顺序与档位成员校准、premise 切换（若有）、Response 接受窗参数方向。

BATCH_ID: REP-FULL-GRAZE-001
顺序还原修复批次：REP-ORDER-FIX-001（§0/§2/§3/§5 修改；Bake 伪脚本 early return 链+分级命中，Response 档位展开）
