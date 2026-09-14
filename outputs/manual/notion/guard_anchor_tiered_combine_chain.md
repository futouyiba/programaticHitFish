> **护巢锚门四步链**（`GUARD_ANCHOR_TIERED_COMBINE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：18

## 特点

护巢期分布围着「守的东西」转：锚存在性硬门→锚面适配→守卫关系→温度。

## 骨架（一行链序）

```plain text
GATE[锚存在性]：处于合法锚域？否→×0.01 软出局 → EVAL[锚面适配] 三档 → EVAL[守卫关系（核/缘/圈外）] 三档 → EVAL[局部温度] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（蓝鳃太阳鱼（guarding 表达文件·canonical 成员·已 ×0.01 对齐））

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配 → 关系评估 → 局部温度 → 合并；出局即 EARLY_RETURN（返回 0.01 × weight，
不进入后续评估——×0.01 软出局：非零、仍可参与下游[REP-WORDING-ALIGN-001]），不做「先全算再减」。推导来源（Tier A）：C06「预先建立并持续照护巢区」——
建立期选址（锚适配先行）→ 照护期占位（关系评估在后）。步序与档位成员的正文级校准 [需正文]。
与 live BA-T2 模板平铺读法（读关系→查 Profile 得单一 Fit→合并）的分歧登记 README §7。

读取 当前目标的结构 / 底质 / 深度
读取 当前目标与最近殖民地巢群锚点的关系（距离 / 朝向）
读取 当前点局部温度

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @BluegillLocalGuardAnchorEligibility
    （锚=殖民地巢群；巢群的繁殖资格已在路由面判定，本步不重复结算 premise，
      只判「当前目标是否处于合法护巢锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与护巢分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中）：
    用当前目标的巢床结构查询 @BluegillColonyNestSuitabilityProfile
    （三档分档槽=Profile 值域——档位成员与阈值不冻结）
    如果 巢床结构 ∈ 最适应档（preferred 锚面）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 锚面）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除锚面）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；不可守巢结构出局——殖民地巢群选址适配先行）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中）：
    用当前目标与巢群锚点的关系（距离 / 朝向）查询 @BluegillGuardRelationProfile
    （守卫位三档=Profile 值域不冻结）
    如果 关系 ∈ 守卫核档：
        RelationFit = 全额（守卫占位）
    否则如果 ∈ 守卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；守卫圈外无护巢占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @BluegillGuardLocalTemperatureProfile
    （护巢期局部温度三档=Profile 值域不冻结）
    如果 局部温度 ∈ 适温档：
        LocalTempFit = 全额
    否则如果 ∈ 边际档：
        LocalTempFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除档）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；护巢期排除温度带出局）

终值：返回 running weight（渐进累积——各步 Fit 已逐步乘入，无独立合并步；原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭——合并数学=逐步乘法）

返回 Guarding SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

## 配置表（真实结构·字段-值——实例文件原表）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorResolverInstance | colony_nest（集群巢床结构——蓝鳃殖民地巢床 [需正文：集群巢 vs 独巢分布]） |
| GuardAnchorEligibilityRule | @BluegillLocalGuardAnchorEligibility |
| GuardAnchorRelationProfile | @BluegillGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @BluegillColonyNestSuitabilityProfile |
| LocalTemperatureProfile | @BluegillGuardLocalTemperatureProfile |
| OnAnchorMiss | RETURN_NEAR_ZERO |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| anchor | 四形式：nest 构建型/egg_mass 附着/fry_school 移动群/host_brood 蚌宿主 |
| guard_participant | male/biparental |
| guard_action_notes | fan 扇护/黏液喂养→Response；洪水→DynamicSlot；停食→premise |
| resolver_instance | 细名（colony_nest/cave_ceiling…场内定位） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*