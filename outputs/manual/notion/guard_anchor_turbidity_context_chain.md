> **护巢四步+浊度语境链**（`GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

护巢锚门四步后加一个浊度修饰步（浑水种淡水石斑/朱氏鲈）。

## 骨架（一行链序）

```plain text
GATE[锚存在性] → EVAL[锚适配] → EVAL[关系] → EVAL[温度] → EVAL[浊度] 三档（语境修饰） → 返回 running weight
```

## 完全展开实例伪脚本（淡水石斑（浊水双亲·护巢四步+浊度语境步））

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝锚存在性判定 → 锚适配 → 关系评估 → 局部温度 → 浊度语境（unary 修饰步） → 合并；
出局即 EARLY_RETURN（返回 0.01 × weight，非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；不进入后续评估），不做「先全算再减」。推导来源（Tier B）：
R09 triage 批注一句「浊水双亲淡水石斑」——浊水=语境（unary 轴实例，非路由条件、非第二轴），
巢型 [需正文]；步序与档位成员 [需正文] 校准（顺序/档位变化=census 判同输入，结构变更需重审）。
与 live BA-T2 模板平铺读法的分歧登记 README §7。

读取 当前目标的结构 / 底质 / 深度
读取 当前目标与巢锚点的关系（距离 / 朝向）
读取 当前点局部温度
读取 当前点浊度事实

第 1 步 锚存在性判定（GATE_ANCHOR_EXISTENCE）：
    用锚域事实查询 @JaguarLocalGuardAnchorEligibility
    （锚=nest（巢型待正文 [需正文]）；护巢资格已在路由面判定，本步不重复结算 premise，
      只判「当前目标是否处于巢锚的合法护巢锚域」）
    如果 当前目标处于合法锚域：
        进入第 2 步
    否则：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；锚不存在格出局——OnAnchorMiss=RETURN_NEAR_ZERO 的判断序形态；
        锚域外格子不参与护巢分布评价，非「算出低值」）

第 2 步 锚适配（EVAL_ANCHOR_SUITABILITY，分级命中）：
    用当前目标的底质结构查询 @JaguarNestSuitabilityProfile
    （锚面三档分档槽=Profile 值域——档位成员与阈值不冻结 [需正文：巢型/产卵基质]）
    如果 锚面 ∈ 最适应档（preferred 锚面）：
        AnchorSuitabilityFit = 全额
    否则如果 ∈ 可接受档（tolerated 锚面）：
        AnchorSuitabilityFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除锚面）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；排除锚面出局）

第 3 步 关系评估（EVAL_ANCHOR_RELATION，分级命中）：
    用当前目标与巢锚点的关系（距离 / 朝向）查询 @JaguarGuardRelationProfile
    （守卫位三档=Profile 值域不冻结）
    如果 关系 ∈ 守卫核档：
        RelationFit = 全额（守卫占位）
    否则如果 ∈ 守卫缘档：
        RelationFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（圈外档）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；守卫圈外无护巢占位）

第 4 步 局部温度（EVAL_LOCAL_TEMPERATURE，分级命中）：
    用当前点局部温度查询 @JaguarGuardLocalTemperatureProfile
    （护巢期局部温度三档=Profile 值域不冻结）
    如果 局部温度 ∈ 适温档：
        LocalTempFit = 全额
    否则如果 ∈ 边际档：
        LocalTempFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（排除档）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；护巢期排除温度带出局）

第 5 步 浊度语境（EVAL_TURBIDITY_CONTEXT，分级命中——unary 修饰步）：
    用当前点浊度查询 @JaguarTurbidityProfile
    （浊水语境三档=Profile 值域不冻结 [需正文：浊度档位]；unary 轴，无第二轴——
      语境适配不改变路由资格，Bake 面只读一次浊度事实）
    如果 浊度 ∈ 语境适档：
        TurbidityContextFit = 全额
    否则如果 ∈ 语境边际档：
        TurbidityContextFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（语境排除档）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；语境排除档出局 [需正文：排除档有无归 Profile 值域]）

终值：返回 running weight（渐进累积——各步 Fit 已逐步乘入，无独立合并步；原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭——合并数学=逐步乘法）

返回 Guarding SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

## 配置表（真实结构·字段-值——实例文件原表）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE（**§2.2 已顺序还原（REP-ORDER-FIX-002）：锚存在性 early return 链＋锚适配/关系/温度/浊度语境分级命中；与模板平铺读法分歧登记 README §7**） |
| GuardAnchorEligibilityRule | @JaguarLocalGuardAnchorEligibility |
| GuardAnchorResolverInstance | nest（巢型待正文 [需正文]） |
| GuardAnchorRelationProfile | @JaguarGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @JaguarNestSuitabilityProfile |
| LocalTemperatureProfile | @JaguarGuardLocalTemperatureProfile |
| TurbidityContextProfile | @JaguarTurbidityProfile（浊水语境 unary 轴实例；「浊水双亲」语境的落面，非路由条件 [需正文：浊度档位]） |
| OnAnchorMiss | RETURN_NEAR_ZERO |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| turbidity | 语境档（unary 修饰步） |
| anchor | 四形式 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*