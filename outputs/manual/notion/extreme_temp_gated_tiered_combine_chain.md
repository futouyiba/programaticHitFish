> **极值门+无序因子集链**（`EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：1

## 特点

极值温度门+因子无序集（OSC 出族单成员，PROV）。

## 骨架（一行链序）

```plain text
GATE[极值温度] → 因子无序集：各因子 EXIT 档/档位乘入 → 返回 running weight
```

## 完全展开实例伪脚本（地图鱼（Normal 面·极值门+无序因子集））

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面顺序还原范围：硬门先行（极值水温出局——出局条件
先于因子评价）＋各因子分级命中（三档）。**因子间顺序不排序**：census P-OSC-BAKE open_semantics
「因子间业务顺序未由冻结证据裁决，按 unordered typed factor set 处理」原样保留——强行排序=冒充
证据（§5 放弃项 (5)，分歧登记 README §7）。

读取 当前点静水 / 流速事实
读取 当前结构（泥沙底浅沟塘 / 掩体）
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

第 1 步 水温硬门（GATE_EXTREME_TEMP）：
    用当前点水温对照排除档边界（@OscarNormalTempFloor 为边界参考）
    如果 当前点水温 ∈ 排除档（极值带）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；极值温度带出局——出局条件先于因子评价；
        从「末位算术门」还原为前置出局判定）

因子评价（因子间顺序=census unordered 原样，不排序；各因子分级命中，三档=Profile 值域不冻结）：
    用静水事实查询 @OscarStillwaterProfile：
        最适应档=StillwaterFit 全额 / 可接受档=削减（× Profile 衰减参数，不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）
    用结构查询 @OscarSubstrateStructureProfile：
        最适应档=StructureFit 全额 / 可接受档=削减（不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）
    用猎物资源查询 @OscarPreyResourceProfile：
        最适应档=PreyFit 全额 / 可接受档=削减（不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）
    用时段查询 @OscarNormalTimeProfile（全天活跃方向）：
        活跃档=TimeFit 全额 / 一般档=削减（不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）

合并步：
    合并 StillwaterFit / StructureFit / PreyFit / TimeFit
    算子标注：渐进累积（原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]——B 系列表达口径：合并数学=逐步乘法 weight = weight × step_fit；BA-T1 因子合并算子——因子顺序与合并数学均待机制侧，不因分级命中展开而隐式定义）

返回 SpatialDistributionWeight（顺序还原范围：硬门先行+分级命中已还原；因子间顺序=证据未裁决，不冒充）
```

## 配置表（真实结构·字段-值——实例文件原表）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-NORMAL-HABITAT-FIT（**§2.4 已顺序还原（REP-ORDER-FIX-002）：硬门先行＋分级命中；因子间顺序按 census open_semantics unordered 原样保留——分歧登记 README §7**） |
| StillwaterProfile | @OscarStillwaterProfile（静水偏好因子） |
| SubstrateStructureProfile | @OscarSubstrateStructureProfile（泥沙底浅沟塘结构掩体因子） |
| PreyResourceProfile | @OscarPreyResourceProfile（小鱼 / 螯虾 / 虫 / 幼虫资源因子） |
| TimeProfile | @OscarNormalTimeProfile（全天活跃方向） |
| ExtremeTemperatureGate | @OscarNormalTempFloor |
| CombineRule | Template-fixed（数学=渐进累积逐步乘法——原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]；census open_semantics：因子间业务顺序未由冻结证据裁决，按 unordered typed factor set 处理） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| temp_gate | 前置 |
| factor_set | unordered（证据未裁决序） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*