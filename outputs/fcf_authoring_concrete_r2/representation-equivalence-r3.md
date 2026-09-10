# Representation Equivalence R3｜表格闭包 ↔ 中文脚本

这是对 R2 具体化样本的一项 **token-level / 引用级** 一致性检查，不是生产 DSL 编译器，也不解析中文语法树。检查器读取 `tables.json` 与 `scripts.json`，逐个 Binding 核对：Binding ID、Template ID、每个启用 Slot 的具体引用、关闭 Slot 的关闭语义、所有 `@引用` 是否来自已登记 Parameter/Profile，以及 ResponseBand / GroupShare / QualityModifier 的每条规则是否在脚本中留下可读声明。

## 检查结果

```text
Bindings checked: 38
Checks: 297
Failures: 0
```

代表回归绑定：`C03_R`、`C06_R`、`C08_R`、`C09_R`、`C12_N`、`C12_M`。它们分别确认 FIRST_MATCH/Default、Defense-only、双固定 Channel、既有 Opportunity 输入、上游 NormalFeeding 分流和 Migration Reaction 分流都能在两种表达中找到对应的具名结构。

## 这项检查能证明什么

- 在本检查器定义的 token-level 规则下，表格中没有被脚本遗漏的具名 Binding、Template、启用 Profile/Parameter 或关闭 Slot。
- Table 中的 Band、Group Share、Quality Modifier 行都留下了可读 token，且脚本没有未知的 `@引用`。
- R2 当前 38 个 Binding 的脚本集合完整，且固定模板标识一致。

## 这项检查不能证明什么

- 脚本不是独立编译器；它由同一套样本模板展开，因此不证明两个生产实现已经语义等价，也不证明条件运算、分支顺序或结果值的双向语义等价。
- 它不证明曲线、MAX/BLEND、空间顺序或任何生产参数已冻结。
- 它不消费 FR3 候选，不改变 Frozen Set、B4 Gate 或最终 Config/DSL 选型。

可复核命令：`python3 representation-equivalence-r3.py`。机器输出保存在 `representation-equivalence-r3.json`，297 项明细均为 `PASS`。
