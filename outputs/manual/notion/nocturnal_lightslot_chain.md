> **夜行底板+低光槽链**（`NOCTURNAL_LIGHTSLOT_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：24

## 特点

夜行性打底，链中插一个光照档位槽。

## 骨架（一行链序）

```plain text
读取 夜行底板事实 → EVAL[因子] 三档 → SLOT[低光]：档位乘入 → 返回 running weight
```

## 完全展开实例伪脚本（欧洲巨鲶（Normal 面·夜行低光槽·已 ×0.01 对齐））

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水层定位（近底软定位——底栖掠食方向） →
结构 → 水温 → 时段 → 合并。推导来源：物种属性锚方向级（benthopelagic 近底＋夜间活跃＋底栖
掠食——CSV 行级方向，[需正文] 校准；无 Story 空间程序证据的因子顺序不冒充）。水温从「末位
算术门」还原为链中档位判定（排除档=EARLY_RETURN，@WelsNormalTempFloor 为排除档边界参考）。
与 live BA-T1 Independent Factor Set（因子无序合并）模板语义的分歧登记 README §7。

读取 当前水层
读取 当前结构
读取 当前点水温
读取 当前时段

第 1 步 水层定位（近底软定位，分级命中）：
    用当前水层查询 @WelsNormalLayerProfile
    （近底软定位三档=Profile 值域不冻结 [需正文：硬定位与否——底栖掠食方向]）
    如果 水层 ∈ 近底带档：
        LayerFit = 全额
    否则如果 ∈ 中间水层档：
        LayerFit = 削减（× Profile 衰减参数——不清零）
    否则（远底带档）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；远离底带格出局）

第 2 步 结构（分级命中）：
    用当前结构查询 @WelsNormalStructureProfile（三档=Profile 值域不冻结）
    如果 结构 ∈ 最适应档：
        StructureFit = 全额
    否则如果 ∈ 可接受档：
        StructureFit = 削减（不清零）
    否则：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；排除结构档出局 [需正文：排除档成员]）

第 3 步 水温（分级命中）：
    用当前水温查询 @WelsNormalTemperatureProfile（三档=Profile 值域不冻结）
    如果 水温 ∈ 适温档：
        TemperatureFit = 全额
    否则如果 ∈ 边际档：
        TemperatureFit = 削减（不清零）
    否则（排除档——@WelsNormalTempFloor 为边界参考）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；极值温度带出局）

第 4 步 时段（分级命中）：
    用当前时段查询 @WelsNormalTimeProfile（夜间三档=Profile 值域不冻结）
    如果 时段 ∈ 活跃档：
        TimeFit = 全额
    否则如果 ∈ 一般档：
        TimeFit = 削减（不清零）
    否则：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；排除时段档出局 [需正文：非活跃时段是否出局归 Profile 值域]）

终值：返回 running weight（渐进累积——各步 Fit 已逐步乘入，无独立合并步；原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭——合并数学=逐步乘法）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中）
```

## 配置表（真实结构·字段-值——实例文件原表）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT（**§2.4 已顺序还原（REP-ORDER-FIX-002）：early return 链＋分级命中；与 live BA-T1 Independent Factor Set 无序语义的分歧登记 README §7**） |
| LayerProfile | @WelsNormalLayerProfile（底栖方向） |
| StructureProfile | @WelsNormalStructureProfile |
| TemperatureProfile | @WelsNormalTemperatureProfile |
| TimeProfile | @WelsNormalTimeProfile（夜间活跃方向） |
| ExtremeTemperatureGate | @WelsNormalTempFloor |
| CombineRule | Template-fixed（数学=渐进累积逐步乘法——原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| light_slot | K14 槽三档 |
| base_factors | typed |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*