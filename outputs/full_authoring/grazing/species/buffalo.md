# 水牛鱼（Buffalo｜Ictiobus bubalus）｜Grazing 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GRAZE-001（Grazing/底质系＝P06 全样本 第 2 批） |
| Story | FISH-R07 水牛鱼（coordinator 分批名单：R07 亚口科四条之一（REV-001 M1 修正：原名单误标 R06）；Story 页未在本地快照——身份锚为 fish-reference-20260908 行及其 Notion 资料页 3d5a4137d23681d3ad27d6125a681736；Story 正文 [需正文]）。**种级身份注意**：本鱼=Ictiobus bubalus；15-Case C10 大口水牛鱼（Bigmouth Buffalo，Ictiobus cyprinellus，FieldFeeding 故事）为不同种——其四面表达已由 outputs/fcf_authoring_concrete_r2/four-surface-completion-r1.md 承载，本文件不重复 |
| 冻结 Pattern | P01 行级主 relation（live 实测，REV-001 M1）+ P06 merge-key pending（R07 FR3 DiscoveryBatch 附标签层——Cross-Batch 执行未落地） |
| 物种属性锚 | fish-reference-20260908：水温 21.1–33.1℃、最适 27.1℃、demersal、深≥4m、早晨活跃、肉食性、摄食类型=hunting macrofauna (predator)、孤僻（性格）、暖水（行级 AI 审核状态=待人工审核；仅作身份与习性方向锚，数值不做阈值） |
| 基线 | SNAPSHOT_ONLY（live Stress Test R1 主页转录 tmp/live_stress_main_after.md，2026-09-10 版；census registry v4 快照 fish_logic_census/template_registry.yaml） |
| 证据档 | Tier B（coordinator 分批名单 + CSV 方向锚；Story 正文 [需正文]，条件值全 @ 化） |
| 变体声明 | 条件原子：无路由条件原子（§1.1 显式无路由程序声明）；分群结果＝5 列固定；品质表＝绑定表（live §12.2 形态），本鱼无物种级品质调整表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| census 族衔接 | 骨架按 census SINGLE_FACTOR_NORMALIZED_WEIGHT（2 步）投影给出；归族裁决归 census 侧判同（README §3 登记 2） |

## 0. 上游语义与底质处理形态

- 底质处理形态（方向）：亚口科底质连续吸食——底泥/底质表面无脊椎与有机资源的吸食处理（CSV demersal、深≥4m、肉食性、hunting macrofauna——亚口科吸食式底栖摄取，非滤食式 FieldFeeding（后者为大口水牛鱼 C10 故事域，种级区分））。
- 「hunting macrofauna (predator)」在亚口科语境＝底栖大型无脊椎摄取（吸食式）——底泥无脊椎/碎屑构成 [需正文]。
- Group 面：按分批口径无供给拆分；若正文出现互斥供给证据则升级重审（结构变更非 Profile 重绑定）。
- 表达超集说明：Tier B 骨架按 P06 底质单因子形（census SINGLE 族）给出，仅容纳 CSV+体构方向；归族改判（PATCH/PLAIN）＝结构变更需重审；正文判无程序语义即撤回本文件。

Profile 引用清单：@BuffaloSubstratePatchProfile @BuffaloSubstrateSpatialProfile @BuffaloSubstratePreyFields @BuffaloDietClasses @BuffaloSizeWindow @BuffaloNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Buffalo_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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
| BakeTemplate | BA-SUBSTRATE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化；Tier B 骨架——归族裁决归 census 侧判同） |
| FactorType(typed) | resource_patch：底泥/底质表面无脊椎资源（CSV 方向：demersal + hunting macrofauna + 深≥4m——吸食式底栖摄取；底泥无脊椎/有机碎屑构成 [需正文]） |
| FactorBinding | 常年绑定 [需正文]（CSV 无迁徙注记——若正文证实季节/阶段切换则由上游 premise 配置处理） |
| SubstratePatchProfile | @BuffaloSubstratePatchProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@BuffaloSubstratePreyFields；diet_classes=@BuffaloDietClasses；size_window=@BuffaloSizeWindow） |
| LiveLayerProjection | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot=@BuffaloSubstrateSpatialProfile（coverage delta K3 吸收读法：benthic prey class + 基质 Factor；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的底质类型（泥/砂/淤）
读取 当前格子的基质资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@BuffaloSubstratePreyFields 绑定的底泥无脊椎 prey class 生物量，
      经 diet_classes=@BuffaloDietClasses 食性过滤
      与 size_window=@BuffaloSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（常年绑定；切换若正文证实则由上游 premise 配置切换，
    不在本 body 内设分支）

EVAL_TYPED_FIELD_OR_FACTOR：
    用基质资源事实查询 @BuffaloSubstratePatchProfile
    得到 SubstratePatchFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 SubstratePatchFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；typed context 约束属 PATCH 族域，硬约束属 HARD_GATED 族域，
多因子组合属 PLAIN 族域，均非本骨架）
```

### 2.3 live 层投影声明

live 侧吸收读法＝BA-T1 底板 + DynamicSpatialSlot=@BuffaloSubstrateSpatialProfile（REP-COVERAGE-DELTA-001 K3 吸收结构）。种级区分：大口水牛鱼（C10）=RS-FEED-01 FieldFeeding 输入（滤食性浮游场，P03 域故事）；本鱼=底质吸食（P06 域机制）——两种不同 Ictiobus 的表达互不覆盖。census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（例 1C 形态；R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @BuffaloNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @BuffaloNormalFeedingProfile（底泥无脊椎取向接受窗——CSV 方向锚）
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

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

- 使用的自由度：SINGLE 族投影标签；typed factor 实例语义（底泥无脊椎方向，取自 CSV）；Profile 命名；伪脚本步序（canonical 两步固定）；Bake 输入契约字段复用。
- 放弃的自由度：(1) 归族裁决权（同泰鲮）；(2) 合并算子（本程序无 combine 步；live 层组合算子 OPERATOR UNDEFINED 待机制侧）；(3) 与大口水牛鱼（C10 FieldFeeding）的合并表达（种级区分：Ictiobus bubalus ≠ I. cyprinellus，机制域 P06 底质吸食 ≠ P03 滤食场）；(4) 「孤僻」性格程序化（档案字段无 Story 证据映射，不表达）；(5) 数值与 Profile 值域不冻结。
- [需正文] 底泥无脊椎构成、深度带偏好（CSV 深≥4m 方向）、premise 切换（若有）、Response 接受窗参数方向。

BATCH_ID: REP-FULL-GRAZE-001
