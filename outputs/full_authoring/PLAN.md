# 全库生产级表达计划（/loop 第二循环）

目标（用户原话提炼）：
1. **全部 FR story × 全部 267 鱼的 B 系列表达**——中文伪脚本完全条件展开/逻辑原子化（不是"组合适应度高"这种泛话）；配置表到生产级数据（条件原子 7 列 / 条件组合 5 列 / 分群结果 5 列——Stress Test R1 例 1 样板）。
2. **logicTemplate census 覆盖全部 story 全部鱼过 review**——具体判断顺序+early return；条件原子 and/or/括号。

## 规模评估
- 267 鱼 × 4 执行面（Group/Bake/Response/Quality）×（条件原子+组合+分群+伪脚本）≈ 每鱼 10-30 行配置+20-80 行脚本
- Story DB 已有 FR3-passed 语义锚（每鱼的 Pattern/Domain/Channel）
- Census registry v4 已有 9 族 canonical body 可复用

## 分批策略
- 按机制相似度分批（同属/同 Pattern 群组共享骨架，参数差异化）
- 批 1：Guarding 系（P04 全样本 ~15 鱼）——已有的例 1 样板直接推广
- 批 2：Grazing/底质系（P06 全样本 ~20 鱼）
- 批 3：洄游系（P05 ~30 鱼）
- 批 4-N：其余 P01/P03 群组
- Census B3+ 并行推进

## 基础设施
- 复用 Stress Test R1 的 V1-V4/W1-W3/R1-R2 列结构声明
- 复用 Census registry v4 canonical body
- 每批独立 validate + 独立审

