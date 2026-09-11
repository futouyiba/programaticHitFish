# 茅尖鱼（Pike Cichlid｜Crenicichla lepidota）｜机会组四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM2-001（P01 普通层＝全库最大 Pattern 群 第 6 批：第二轮全量闭合——机会组） |
| Story | R 系批成员（批归属未在本地 [需核对]；CSV 行 178） |
| 冻结 Pattern | P01 [需核对]（CSV 方向锚归层） |
| 物种属性锚 | fish-reference-20260908：活泼、全天活跃、—（源表空）、营养级 —（源表空）、—（源表空）（行级 AI 审核状态=待人工审核；仅作方向锚） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照；第一轮交付包 outputs/full_authoring/normal/） |
| 证据档 | Tier B（CSV 方向锚；[需核对]） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| 亚结构组 | 机会组（opportunistic） |

## 0. 上游语义与摄食形态

- 摄食形态：茅尖鱼（近岸梭状机会掠食）。
- 证据边界：Story 行级 Pattern 标签不在本地 [需核对]；本文件结构为机会组样板（第一轮 Tier A 样板骨架）的表达层选择——Story 正文到达后 census 判同可能改判（换组/换 BakeTemplate＝**结构变更需重审**，validator 族边界拦截静默改写），不是 Profile 重绑定。
- 附加注记：慈鲷系（Cichla 同域不同属/孔雀鲈 guarding 批互指）——判例不继承；R1 候选池「茅尖鱼」即本行。
- Response 面：TYPED 族参数差异（小鱼拟饵/快速呈现——组样板参数——组样板语义，参数级无新拓扑）。
- Group 面 / Quality 面：组样板 NO_SURFACE_EFFECT。
- 表达超集说明：骨架参数化表达；未超出组样板族域。

- **判断顺序（REP-ORDER-FIX-004 顺序还原，Tier B）**：判断链＝（premise 读取——若有，配置级）→ 机会场食物丰度档位（丰=全额/贫=削减/枯=EARLY_RETURN）→ 归一化。结构安全/水流等次级因子未入链（CSV 活泼/温和锚无 Story 空间证据，不冒充）。

Profile 引用清单：@PKCPatchProfile @PKCPreyFields @PKCDietClasses @PKCSizeWindow @PKCNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| PKC_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-P01-OPPORTUNE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化——第一轮定型，本批零新族；**§2.2 已顺序还原（REP-ORDER-FIX-004）：early return 链+分级命中，登记 README §7**） |
| FactorType(typed) | resource_patch：近岸小鱼/无脊椎机会场轴（食性列空 [需正文]——鳃形掠食方向） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@PKCPreyFields；diet_classes=@PKCDietClasses；size_window=@PKCSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed factor（B-T1 Independent Factor Set 单因子退化形；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
【顺序还原声明｜REP-ORDER-FIX-004】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝（premise 读取——若有，配置级）→ 机会场食物丰度档位 → 归一化。机会型
第一判断＝食物丰度（跟着食物走：丰档=全额/贫档=削减不清零/枯档=出局
EARLY_RETURN），与伏击型（掩体先行）、追击型（猎物场+栖息双槽）、夜行型
（底板+光照槽）的顺序差异本身=LogicTemplate 判据。顺序来源＝CSV 方向锚级推导（[需正文]）——Story 正文
到达后校准（census 侧 SINGLE 族重跑=work standards §5.4 行动项，分歧登记 README §7）。

读取 当前格子的resource_patch事实（近岸小鱼/无脊椎机会场轴（食性列空 [需正文]——鳃形掠食方向））
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@PKCPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@PKCDietClasses 食性过滤
      与 size_window=@PKCSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 机会场食物丰度档位（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中——
  机会型第一判断：食物丰度先行）：
    用resource_patch事实查询 @PKCPatchProfile 的机会场丰度分档槽
    （近岸小鱼/无脊椎机会场轴·食性列空 [需正文]——鳃形掠食方向；档位成员=Profile 值域不冻结 [需正文]）
    如果 机会场 ∈ 丰档（preferred 槽）：
        ShorelinePatchFit = 全额
    否则如果 ∈ 贫档（tolerated 槽）：
        ShorelinePatchFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（枯竭档——无可食机会）：
        返回 0（EARLY_RETURN：无食物机会的格子出局——机会型跟着食物走）

第 2 步 NORMALIZE_WEIGHT：
    对 ShorelinePatchFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @PKCNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实（小鱼拟饵/快速呈现——组样板参数）评价 @PKCNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE（分级命中，REP-ORDER-FIX-004 展开）：
    按三档判定 FoodEvaluation（档位成员=@PKCNormalFeedingProfile 值域不冻结）：
    如果 FoodEvaluation ∈ 接受档（preferred 槽）：
        返回 Response(TargetFeeding)（全额响应）
    否则如果 FoodEvaluation ∈ 边际档（tolerated 槽）：
        返回低响应（削减但不清零）
    否则：
        返回无响应（出局）

返回 Response(TargetFeeding)

Reaction 槽 OFF
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

- 使用的自由度：SINGLE/PLAIN 族投影标签与 typed 因子实例语义；Profile 命名；顺序还原链序与档位结构（REP-ORDER-FIX-004：食物丰度档三档分级命中 EARLY_RETURN）。
- 放弃的自由度：(1) 归族裁决权移交（无 census 快照——Story 正文到达后判同可能改判，结构变更需重审）；(2) 合并算子（无 combine 步或 OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结。
- 放弃的自由度：(4) 名单身份/口径张力项的裁决权（见 §0 附加注记与 README 排除表——登记在案不冒充）。

- 放弃的自由度（REP-ORDER-FIX-004 追加）：census canonical 步序的服从（顺序还原后链与 canonical「无 gate、无 early return」判语拓扑分歧——链序/档位结构为 authoring_work_standards §5.1 顺序还原产物，登记 README §7；重跑裁决归 census 侧=§5.4 行动项）。

BATCH_ID: REP-FULL-NORM2-001
顺序还原修复批次：REP-ORDER-FIX-004（§0/§2/§3/§5 修改；Bake 伪脚本 食物丰度档三档分级命中 EARLY_RETURN，Response DECIDE 档位展开）
