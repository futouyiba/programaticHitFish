> **结构门+质量档链**（`GATED_COVER_TIER_CHAIN`）｜面：Bake｜状态：CANDIDATE｜名义成员：27

## 特点

先过一道二元结构门（门值=gate_axis 八值之一），门内再走因子档位。

## 骨架（一行链序）

```plain text
GATE[结构门]：命中→继续 / 不命中→×0.01 软出局返回 → EVAL[掩护/质量因子] 三档 → 返回 running weight
```

## 完全展开实例伪脚本（北极茴鱼（normal2 表达文件·伏击门 GATE_RIFFLE_GRAVEL·已 ×0.01 对齐））

```plain text
【顺序还原声明｜REP-ORDER-FIX-004】本伪脚本按行为判断顺序还原（authoring_work_standards §5.1）：
判断链＝GATE_RIFFLE_GRAVEL 门（急流砾石结构存在） → 掩体结构档位 → 归一化；掩体档分级命中
（最适伏击=全额/次级掩体=削减不清零/暴露=出局 EARLY_RETURN），门不成立直接
EARLY_RETURN。伏击型第一判断＝结构掩体（无掩体不伏击），与追击型（猎物场+
栖息双槽）、机会型（食物丰度先行）、夜行型（底板+光照槽）的顺序差异本身=
LogicTemplate 判据。顺序来源＝CSV 方向锚级推导（[需正文]）——Story 正文到达后校准（census 侧 SINGLE
族重跑=work standards §5.4 行动项，分歧登记 README §7）。

读取 当前格子的structure_factor事实（急流砾石结构贴近轴（漂流无脊椎+水面捕食方向））
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@AGYPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@AGYDietClasses 食性过滤
      与 size_window=@AGYSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

第 1 步 GATE_RIFFLE_GRAVEL（急流砾石结构存在——伏击型第一判断：无可用掩体不伏击）：
    用该 typed 因子轴事实查询 @AGYRiffleGravelProfile 的掩体存在分档槽
    （档位成员=Profile 值域不冻结 [需正文]）
    如果 格子存在急流砾石/卵石滩结构：
        进入第 2 步
    否则：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；格子无砾石结构——伏击型结构掩体先行判据）

第 2 步 掩体结构档位（EVAL_TYPED_FIELD_OR_FACTOR 的顺序还原形，分级命中）：
    用该 typed 因子轴事实查询 @AGYRiffleGravelProfile 的掩体伏击分档槽
    （砾石贴近质量：砾石背流面/砾石滩面；档位成员=Profile 值域不冻结 [需正文]）
    如果 掩体结构 ∈ 最适伏击档（preferred 槽）：
        RiffleGravelFit = 全额
    否则如果 ∈ 次级掩体档（tolerated 槽）：
        RiffleGravelFit = 削减（× Profile 衰减参数——削减但不清零）
    否则（暴露无掩体档）：
        返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；暴露格子不承载伏击分布）

第 3 步 NORMALIZE_WEIGHT：
    对 RiffleGravelFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（顺序还原链结束：有 early return、有分级命中；
无 combine 步——多因子组合属 PLAIN 族域非本骨架。本链与 census SINGLE 族
canonical 两步（无 gate 判语）的分歧登记 README §7，换标签/改结构=census
判同裁决后结构变更需重审）
```

## 配置表（真实结构·字段-值——实例文件原表）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化——第一轮定型，本批零新族；**§2.2 已顺序还原（REP-ORDER-FIX-004）：early return 链+分级命中，登记 README §7**） |
| FactorType(typed) | structure_factor：急流砾石结构贴近轴（漂流无脊椎+水面捕食方向） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@AGYPreyFields；diet_classes=@AGYDietClasses；size_window=@AGYSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed factor（B-T1 Independent Factor Set 单因子退化形；两层 reconciliation OPEN——README §3） |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| gate_axis | 8 值：植被缘/静水/底带/可埋底质/池潭/礁缘/斑块/扰动窗 |
| post_gate_factor | typed |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*