# 巴西鲷（Streaked Prochilod｜Prochilodus lineatus）｜Grazing 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GRAZE-001（Grazing/底质系＝P06 全样本 第 2 批） |
| Story | FISH-R05 巴西鲷（coordinator 分批名单：R05 P06 六条之一；Story 页未在本地快照——身份锚为 fish-reference-20260908 行及其 Notion 资料页 3d5a4137d23681f9a0dfe4870b735a0c；Story 正文 [需正文]） |
| 冻结 Pattern | P06（coordinator 分批名单归类；R05 FR3 摘要记 P06 存在 merge 建议（压回 P02，四元组 key，归 Cross-Batch）；行级 Pattern 标签未在本地快照 [需核对]） |
| 物种属性锚 | fish-reference-20260908：水温 17–27℃、最适 22℃、benthopelagic、深≥5m、全天活跃、植食性、摄食类型=grazing on aquatic plants、potamodromous、温和、温水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 审核批注 | FISH-R05-SRCHECK-001：dominant detritivorous ✓、洄游 >800-1000km ✓（Speranza et al. 2012, J Fish Biol 81(2), DOI 10.1111/j.1095-8649.2012.03358.x——Coordinator webReader 备用通道核验）；「>60% ichthyomass」数字主张未证实已降级（SRCHECK-001-FINAL）——本文件不引用该数字 |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier B（coordinator 分批名单 + CSV 方向锚 + SRCHECK 批注两行；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出；归族裁决归 census 侧判同（README §3 登记 2） |

## 0. 上游语义与底质处理形态

- 底质处理形态（方向）：优势碎屑食性（dominant detritivorous，SRCHECK 已核）——底层沉积物/碎屑与附着资源的连续摄取处理；CSV 食性=植食性、摄食类型=grazing on aquatic plants、benthopelagic、深≥5m。底泥摄取（iliophagy）与表面刮食的资源构成区分 [需正文]。
- 长距离洄游（>800-1000km，SRCHECK 已核）：potamodromous 方向锚——若 Story 正文证实洄游期因子集切换，照湄公鲶/欧鲢（MGC/CHB）先例按 lifecycle premise 配置级处理，不购买 Migration Group。
- Group 面：按分批口径无供给拆分；若正文出现互斥供给证据则升级重审（结构变更非 Profile 重绑定）。
- 表达超集说明：Tier B 骨架按 P06 底质单因子形（census SINGLE 族）给出，仅容纳 CSV+SRCHECK 方向；归族改判（PATCH/PLAIN）＝结构变更需重审；正文判无程序语义即撤回本文件。
- **判断顺序（REP-ORDER-FIX-001 顺序还原，CSV/SRCHECK 方向级推导 [需正文]）**：判断链＝近底带水层定位 → 底泥底质档位 → 碎屑资源档位 → 归一化。推导来源：CSV 栖息带 benthopelagic（软定位三档）＋深≥5m＋SRCHECK 优势碎屑食性（dominant detritivorous——资源载体=底层沉积物，底泥可承载性先于碎屑丰度评估：不可承载底质无碎屑摄入意义）。分级命中：各步三档（最适应=全额/可接受=削减不清零/排除=出局），档位成员与阈值全 Profile 值域不冻结 [需正文]。CSV 时段（全天活跃）/水温锚未入链（无 Story 空间程序证据）。

Profile 引用清单：@ProchilodSubstratePatchProfile @ProchilodSubstrateSpatialProfile @ProchilodSubstratePreyFields @ProchilodDietClasses @ProchilodSizeWindow @ProchilodNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Prochilod_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| FactorType(typed) | resource_patch：底泥碎屑/沉积有机质资源（SRCHECK 方向：dominant detritivorous；CSV 方向：植食+grazing on aquatic plants；底泥 vs 附着构成 [需正文]） |
| FactorBinding | 常年绑定 [需正文]（potamodromous 长距洄游方向锚——若正文证实洄游期切换，照 MGC/CHB 先例按 premise 配置处理） |
| SubstratePatchProfile | @ProchilodSubstratePatchProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@ProchilodSubstratePreyFields；diet_classes=@ProchilodDietClasses；size_window=@ProchilodSizeWindow） |
| LiveLayerProjection | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot=@ProchilodSubstrateSpatialProfile（coverage delta K3 吸收读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-001】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝近底带水层定位 → 底泥底质档位 → 碎屑资源档位 → 归一化；每步分级命中
（全额/削减/出局），出局即 EARLY_RETURN。顺序为 CSV/SRCHECK 方向级推导
（benthopelagic 软定位＋优势碎屑食性→底泥承载先行，[需正文]）——
Story 正文到达后校准，顺序/档位差异本身=LogicTemplate 判据
（census 侧 SINGLE 族重跑=work standards §5.4 行动项，分歧登记 README §7）。

读取 当前格子的水层带位置
读取 当前格子的底质类型（泥/沙/砾）
读取 当前格子的基质资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@ProchilodSubstratePreyFields 绑定的碎屑/沉积有机质 prey class 生物量，
      经 diet_classes=@ProchilodDietClasses 食性过滤
      与 size_window=@ProchilodSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（常年绑定；洄游期切换若正文证实则由上游 premise 配置切换，
    不在本 body 内设分支）

第 1 步 近底带水层定位（分级命中，软定位——CSV benthopelagic 底中两层）：
    用水层带位置查询 @ProchilodSubstrateSpatialProfile 的水层分档槽
    （档位成员=Profile 值域不冻结 [需正文]；深≥5m CSV 方向锚）
    如果 水层 ∈ 近底带档（preferred 槽）：
        LayerTier = 全额保留
    否则如果 水层 ∈ 中下水层档（tolerated 槽）：
        LayerTier = 削减（× Profile 衰减参数——削减但不清零）
    否则（远离底带档）：
        返回 0（EARLY_RETURN：底泥碎屑摄食定位不在远底水层分布）

第 2 步 底泥底质档位（分级命中——碎屑载体可承载性）：
    用底质类型查询 @ProchilodSubstratePatchProfile 的底质分档槽
    （细泥/淤泥承载碎屑方向，SRCHECK；档位成员=Profile 值域不冻结 [需正文]）
    如果 底质 ∈ 可承载碎屑档（preferred 槽——如细泥/淤泥）：
        SubstrateTier = 全额保留
    否则如果 底质 ∈ 部分承载档（tolerated 槽——如沙质混泥）：
        SubstrateTier = 削减（削减但不清零）
    否则（不可承载档——如硬砾无沉积）：
        返回 0（EARLY_RETURN：无碎屑承载的底质出局）

第 3 步 碎屑资源档位（EVAL_TYPED_FIELD_OR_FACTOR，分级命中）：
    用基质资源事实查询 @ProchilodSubstratePatchProfile
    （单 typed 因子评估展开为三档分档槽=Profile 值域不冻结 [需正文]）
    如果 碎屑/沉积有机质可得性 ∈ 丰档（preferred 槽）：
        SubstratePatchIntensity = 全额强度
    否则如果 ∈ 贫档（tolerated 槽）：
        SubstratePatchIntensity = 削减强度（削减但不清零）
    否则（无沉积资源档）：
        返回 0（EARLY_RETURN：无碎屑资源的格子出局）

第 4 步 NORMALIZE_WEIGHT：
    对 LayerTier × SubstrateTier × SubstratePatchIntensity 执行模板固定归一化
    （族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

live 侧吸收读法＝BA-T1 底板 + DynamicSpatialSlot=@ProchilodSubstrateSpatialProfile（REP-COVERAGE-DELTA-001 K3 吸收结构）。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @ProchilodNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @ProchilodNormalFeedingProfile（碎屑/植食取向接受窗——SRCHECK+CSV 方向锚）
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-001 展开）：
    按三档判定 FoodEvaluation（档位成员=@ProchilodNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
（连续底质处理机会在本表达仍落离散钩饵 target——P02/P06 待检验判语原样携带）
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

- 使用的自由度：SINGLE 族投影标签；typed factor 实例语义（碎屑食性方向，取自 SRCHECK+CSV）；Profile 命名；**顺序还原链序与档位结构（REP-ORDER-FIX-001：近底带软定位、底泥承载档先行、碎屑资源三档分级命中、early return 链——CSV/SRCHECK 方向级推导 [需正文]）**；Bake 输入契约字段复用。
- 放弃的自由度：(1) 归族裁决权（同泰鲮——census 侧判同可改判）；(2) census canonical 步序的服从（顺序还原后链与 canonical 两步「无 gate 判语」拓扑分歧——登记 README §7，裁决归 census 侧族重跑）；(3) 合并算子（本程序无 combine 步；live 层组合算子 OPERATOR UNDEFINED 待机制侧）；(4) 洄游期 Group（potamodromous 方向锚，照 MGC/CHB 先例 premise 配置级）；(5) 未证实的生物量占比数字（SRCHECK 降级项不引用）；(6) 水温/时段因子入链（CSV 锚无 Story 空间程序证据）；(7) 数值与 Profile 值域不冻结（含档位成员与阈值）。
- [需正文] 底泥 vs 附着资源构成、判断顺序与档位成员校准、洄游期因子集（若有）、Response 接受窗参数方向。

BATCH_ID: REP-FULL-GRAZE-001
顺序还原修复批次：REP-ORDER-FIX-001（§0/§2/§3/§5 修改；Bake 伪脚本 early return 链+分级命中，Response 档位展开）
