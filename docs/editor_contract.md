# FCF V1 编辑器 / 属性配置契约

编辑器是构建于不可变版本化交付物之上的结构模式（Schema）驱动工具。它不是运行时
行为脚本面。

## 面板与归属

| 面板 | 可编辑 | 只读 / 校验 |
|---|---|---|
| 物种能力 | 解剖剖面、感知通道、允许接触、任务上限 | `q` 变更标记为**规模变更**并要求重新校准审查 |
| 种群切片 | 队列与生命周期角色声明、滞回/最短保持 | 稳定的 `population_slice_key`；策略程序不属于身份 |
| 行为策略程序 | 栖息占位规则、动机优先级、进入机会等级规则、白名单触发器 | 所有选择必须在物种能力范围内 |
| 世界因子映射 | 中性事实绑定与解析器解释 | 不得有鱼专属的世界事实；一个物理后果 → 一个归属方 |
| 呈现编译器 | 对象真值、运动/几何与线索发射映射 | 原始物品/技巧 ID 不能作为鱼响应权威 |
| 验证追踪 | 无 | 逐阶段输入、输出、归属方、概率、账本增量 |

## 命令

```text
open_artifact(version_id)
edit(path, value)
validate() -> Diagnostic[]
preview(trace_fixture_id, seed, causal_cut_id) -> ExplainTrace
save_as_new_version(message, author)
compile() -> CompiledArtifact
export_review_report(version_id)
```

`edit` 是事务性的：校验失败时先前交付物保持不变。`save_as_new_version` 存储完整展开的
交付物、机器可读 diff 与诊断。运行时只消费 `CompiledArtifact`，从不读取编辑器草稿
状态。

## 阻止保存的诊断

```text
UNKNOWN_FIELD / DUPLICATE_ID / INVALID_Q
CAPABILITY_EXPANSION
EQUAL_PRIORITY_OVERLAP
WORLD_FACT_IS_FISH_INTERPRETATION
MISSING_SETTLEMENT_OWNER / DUPLICATE_SETTLEMENT_OWNER
ARRIVAL_T_AND_UNIT_PRODUCER_CONFLICT
UNSTABLE_REEVALUATION_TRIGGER
PROGRAM_IN_SLICE_IDENTITY
```

## ExplainTrace 最小形状

```json
{
  "fixture_id": "spawn_bass_guard",
  "artifact_version": "fcf.v1:42",
  "opportunity_id": "stable-hash",
  "stages": [
    {"name": "PERCEPTION", "inputs": {}, "outputs": {"A": 0.8}, "owner": "optical_propagation"},
    {"name": "MOTIVE", "inputs": {}, "outputs": {"motive": "DEFEND"}, "owner": "guard_program"},
    {"name": "ENTRY", "inputs": {}, "outputs": {"E": 0.7, "pi": 0.56}, "owner": "defend_entry_offer"},
    {"name": "RESERVATION", "inputs": {}, "outputs": {"q": 10, "reservation_id": "..."}, "owner": "population_ledger"}
  ],
  "ledger_delta": {"actual_supply": -10, "encounter_hold": 10}
}
```

该追踪是权威决策的解释性投影。它不得执行第二次抽取或改变状态。
