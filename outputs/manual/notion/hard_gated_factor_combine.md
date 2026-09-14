> **双硬门因子集链**（`HARD_GATED_FACTOR_COMBINE`）｜面：Bake｜状态：CANDIDATE｜名义成员：2

## 特点

生死门前置：水面可达+温度极值双硬门，过了门才轮到因子集（肺鱼/电鳗；电感知不进 Bake）。

## 骨架（一行链序）

```plain text
GATE[水面可达]：否→×0.01 软出局 → GATE[温度极值]：否→×0.01 软出局 → 因子集：各因子档位逐步乘入（EXIT 档出局） → 返回 running weight
```

## 完全展开实例伪脚本（南美肺鱼（Normal 面·水面可达+温度极值双硬门））

```plain text
【顺序还原声明｜REP-ORDER-FIX-002】Normal 面判断链＝水面可达硬门（第一出局条件——OBLIGATE
气呼吸：无水面通道即剔除，census HARD GATE 判例「硬门前置」的判断序形态） → 水温极值硬门 →
因子评价（各三档分级命中）。**因子间顺序不排序**：census open_semantics「因子间顺序未裁决，
unordered 处理」原样保留——强行排序=冒充证据（§5 放弃项 (5)，分歧登记 README §7）。
末位算术门（水温<floor 返回极低）还原为前置出局判定。

读取 水文季节事实（本 Bake 仅 WET 态激活）
构建 当前水域可访问集
读取 当前点水面可达事实
读取 当前点静水 / 流速事实
读取 当前结构
读取 当前猎物资源事实
读取 当前点水温
读取 当前时段

第 1 步 水面可达硬门（GATE_SURFACE_ACCESS——第一出局条件）：
    用当前点水面可达事实查询 @LungfishSurfaceAccessGate
    （专性气呼吸：水面不可达即剔除——硬门，非相对排序）
    如果 水面不可达：
        从可访问集中剔除该目标，返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；OBLIGATE 气呼吸出局——
        生存硬门先于一切因子评价）
    否则：
        进入第 2 步

第 2 步 水温极值硬门（GATE_EXTREME_TEMP）：
    用当前点水温对照排除档边界（@LungfishNormalTempFloor 为边界参考）
    如果 当前点水温 ∈ 排除档（极值带）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；极值温度带出局）

因子评价（因子间顺序=census unordered 原样，不排序；各因子分级命中，三档=Profile 值域不冻结）：
    用静水事实查询 @LungfishStillwaterProfile：
        最适应档=StillwaterFit 全额 / 可接受档=削减（× Profile 衰减参数，不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）
    用结构查询 @LungfishPondStructureProfile：
        最适应档=StructureFit 全额 / 可接受档=削减（不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）
    用猎物资源查询 @LungfishPreyResourceProfile：
        最适应档=PreyFit 全额 / 可接受档=削减（不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）
    用时段查询 @LungfishNormalTimeProfile（夜间活跃方向）：
        活跃档=TimeFit 全额 / 一般档=削减（不清零）/ 排除档=返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]）

合并步：
    合并 StillwaterFit / StructureFit / PreyFit / TimeFit
    算子标注：渐进累积（原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]——B 系列表达口径：合并数学=逐步乘法 weight = weight × step_fit；census WEIGHTED_FACTORS 的权重数学未冻结——因子顺序与合并数学均待机制侧，不因分级命中展开而隐式定义）

返回 SpatialDistributionWeight（顺序还原链结束：双硬门 early return、因子分级命中；因子间顺序=证据未裁决，不冒充）
```

## 配置表（真实结构·字段-值——实例文件原表）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-LUN-WET-GATED-FACTORS（census 族成员：硬门前置 + 因子组合；非相对寻优）（**§2.4 已顺序还原（REP-ORDER-FIX-002）：双硬门先行＋分级命中；因子间顺序按 census open_semantics unordered 原样保留——分歧登记 README §7**） |
| SurfaceAccessGate | @LungfishSurfaceAccessGate（专性气呼吸：水面不可达即剔除，HARD GATE 而非排序） |
| StillwaterProfile | @LungfishStillwaterProfile（静水偏好因子） |
| PondStructureProfile | @LungfishPondStructureProfile（塘体结构因子） |
| PreyResourceProfile | @LungfishPreyResourceProfile（猎物资源因子：鱼虾螺蚌藻） |
| TimeProfile | @LungfishNormalTimeProfile（夜间活跃方向） |
| ExtremeTemperatureGate | @LungfishNormalTempFloor |
| CombineRule | Template-fixed（数学=渐进累积逐步乘法——原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]；census open_semantics：因子间顺序未裁决，unordered 处理） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| hard_gates | surface_access + 极值门 |
| factor_set | typed bounded；v2 canonical（LUN 源+EEL） |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*