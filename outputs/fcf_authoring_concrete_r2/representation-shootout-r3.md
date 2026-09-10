# Representation Shootout R3｜PT / Table / Step Table / Narrow DSL

**范围：** 只使用 `Reviewed Fish Mechanism Set｜Pilot-A｜Frozen at A4` 已准入的 C03、C06、C08、C09、C12 五个代表 Story；不消费 FISH-R01 的 13 条 Coverage Delta Candidate。本文验证表达能力与作者成本，不决定最终选型。

## 1. 先看结论

| 表达 | 能直接表达什么 | 需要另有固定目录/Runtime 才能成立的部分 | 本轮丢失风险 | 最适合的职责 |
| --- | --- | --- | --- | --- |
| PT（Profile/Parameter Table） | 曲线点、阈值、乘数、默认值 | 执行顺序、条件树、FIRST_MATCH、MAX、机会身份 | 高：单看参数无法知道“先 Gate 还是先 Overlay” | 调参与数值资产 |
| Table（规范化配置表） | Binding、Slot、Predicate 树、Rule Band、Group Share、Quality Modifier 的完整引用 | TemplateStep 固定目录与 Typed Result 合同 | 低：行多，但可以回放引用闭包 | 生产 Authoring 数据 |
| Step Table（有序步骤表） | Gate、读取、计算、Merge、Return 的有语义顺序 | 条件树和参数 Profile 仍需外表 | 中低：顺序清楚，跨表引用较多 | 需要审执行链的模板作者 |
| Narrow DSL（受限中文 DSL） | 同一固定模板的连续读法、条件组合、类型化返回 | 编译器 Schema、白名单、同一 Profile 表 | 中低：可读，但必须禁止任意副作用 | 规则审阅、诊断与 trace |

PT 不是 Table 的缩写版：它只有数值资产。Step Table 不是允许任意跳转的脚本：`step`、`operation`、`input`、`output`、`failure` 必须来自固定 TemplateStep 目录。Narrow DSL 也不是让作者写任意程序：只有声明式读取、条件、固定函数和 typed return。

## 2. 同一个 C08，四种写法

### 2.1 PT：只能写参数

```text
Profile: C08_R_Grazing
  (0.00, 0.00)
  (1.00, 0.80)
Profile: C08_R_Suspended
  (0.00, 0.00)
  (1.00, 0.90)
Aggregation: MAX
```

PT 能给出 `Grazing=0.60`、`Suspended=0.45` 的曲线资产，但不能仅凭这三行证明两个 Channel 都会执行，更不能表示 Food Context 不触发 Profile Selector。执行拓扑必须从 `R_DUAL_FIXED` 固定模板来。

两条 Profile 是两个固定输入槽同时存在；运行时不会根据资源条件执行 `SELECT GrazingProfile / SuspendedProfile`，也不会把其中一个当作另一个的 fallback。

### 2.2 Table：实际配置闭包

```text
Binding(C08_R, RESPONSE, Tilapia.Feeding, R_DUAL_FIXED)
Slot(C08_R, Grazing,   true, PROFILE, C08_R_Grazing)
Slot(C08_R, Suspended, true, PROFILE, C08_R_Suspended)
CurvePoint(C08_R_Grazing,   0.00, 0.00)
CurvePoint(C08_R_Grazing,   1.00, 0.80)
CurvePoint(C08_R_Suspended, 0.00, 0.00)
CurvePoint(C08_R_Suspended, 1.00, 0.90)
TemplateStep(R_DUAL_FIXED, 1, read_curve, grazing,   G)
TemplateStep(R_DUAL_FIXED, 2, read_curve, suspended, S)
TemplateStep(R_DUAL_FIXED, 3, MAX,        G,S,      ResponseStrength)
```

这就是 R2 的规范化表格行：前五行属于作者数据，后三行属于只读模板目录。作者不能通过增加 `Selector` 列改变第1–3步。

### 2.3 Step Table：顺序显式

```text
template_id=R_DUAL_FIXED
step 1 | 读取 food.grazing_availability，查 @C08_R_Grazing → G
step 2 | 读取 food.suspended_availability，查 @C08_R_Suspended → S
step 3 | MAX(G,S) → ResponseStrength
failure | 缺失输入/类型错误 → ValidationError；不抽签
```

它比 Table 少了 FK 行的分散感，但 `@C08_R_Grazing` 的曲线点仍在 Profile Table；Step Table 本身不能隐式创建 Profile。

### 2.4 Narrow DSL：连续可读版

```text
绑定 C08_R：响应 / Tilapia.Feeding / 模板 R_DUAL_FIXED
  G = 查曲线(@C08_R_Grazing, food.grazing_availability)
  S = 查曲线(@C08_R_Suspended, food.suspended_availability)
  返回 响应强度(MAX(G, S))
```

脚本中的 `MAX`、`查曲线`、`返回` 都是白名单运算；编译器仍必须回到同一 Slot、CurvePoint、TemplateStep 和 Typed Result 检查。四种写法的预期结果完全相同：`G=0.60, S=0.45, ResponseStrength=0.60`。

## 3. 五个代表 Story 的最小差异对照

| Story | PT 需要填 | Table 需要填 | Step Table 需要确认 | Narrow DSL 关键句 | 真正不能省略的语义 |
| --- | --- | --- | --- | --- | --- |
| C03 Rainbow Trout | `match≥0.7`、`drift≥0.6`、default 0、response 0.8/0.25 | Predicate `ALL(good_match, drift_fit)`、两个 Band、Default Slot | `FIRST_MATCH` 先于 Default Return | `若 match≥0.7 AND drift≥0.6：返回0.8；否则若 match≥0.3：返回0.25；否则0` | Band priority 与默认值；不是 Drift Mode |
| C06 Bluegill Guard | Defense 曲线 (0.5→0.6) | Binding→R_DEFENSE、Defense Slot | 只读 intrusion→查曲线→Return | `Defense=查曲线(@Defense,intrusion_strength);返回 Defense` | 没有 Feeding Slot，不存在优先级 |
| C08 Tilapia dual | 两条 Profile＋MAX | 两 Slot＋曲线点＋固定模板 | 两 Channel 都执行，再 MAX | `G=…; S=…; 返回 MAX(G,S)` | 不写 `if grazing else suspended` |
| C09 Paddlefish Field | Density/Suitability/Match 曲线 | 既有 Opportunity 绑定、Field 输入、三 Profile | 先读已有 Scope，再乘三 Fit | `// 不创建 FieldOpportunity；D×S×M→Return` | RootOccurrence/Opportunity 只消费不新建 |
| C12 Salmon migration | Normal 与 Reaction 两组参数 | 两个 Group Binding，各自 Template | 上游选 Group 后只执行对应 Binding | `Migration：普通 Feeding 关闭；评价 Reaction` | 不写绝对不摄食，不写单一攻击动机 |

## 4. 同一修改在四种表达中的落点

| 修改动作 | PT | Table | Step Table | Narrow DSL | 是否改变模板 |
| --- | --- | --- | --- | --- | --- |
| C06 的 x=.5 Defense y 从 .60→.65 | 改一行 CurvePoint | 同一 CurvePoint 行 | 不改步骤 | 不改脚本，只换共享 Profile | 否 |
| C03 增加一个 AND 条件 | 不能独立完成；只能添阈值 | 新 Parameter + Predicate + Member | 不改 R_BANDS 步骤，但要更新条件输入目录 | 在条件表达式加一项，并通过 Schema | 否 |
| C08 MAX→平均 | PT 不能完成 | 修改固定 TemplateStep/实现 | 修改 step3 operation 并复算 | 修改固定聚合句并复算 | 是，候选模板变更 |
| C09 两个 frame 合成一个 Root | PT 无位置 | 不新建行；沿现有 Identity Contract | step1 输入 Scope 不变 | 注释/输入说明变更，不增加 opportunity | 否 |
| Summer 氧门从3.0降到2.5 | 改 Parameter | 改 Parameter 引用 | Gate 位置不动 | 改 `@OxygenMin` 数值表 | 否 |

## 5. 生产桥接与验证

四种表达共享一个受限语义层：

```text
PT / Table / Step Table / Narrow DSL
        ↓ 解析、FK、类型、冲突与白名单校验
Condition AST → Typed IR → 固定 Runtime Template
        ↓
Trace(input snapshot, matched predicate, intermediate, typed result)
```

编译失败条件包括：未知 Slot、Profile 单位错、重复 Band priority、Predicate 环、缺少 Default、Group Share 总和超过1、Quality 总和不正、任意跨 Owner 写入。运行时输入缺失返回 `ValidationError`；条件不满足才返回合法的 typed zero/gate result；C14/C15 是 `OUT_OF_SCOPE`，不伪造零值。

本轮回归已核对：C08 四种写法的两个 Channel 与 `MAX` 结果一致；C06 的 DSL 没有 Feeding 分支；C09 的四种写法没有 `FieldOpportunity` 表；C12 的两个 Binding 没有同一 Runtime Stage Selector；所有 R2 绑定仍可由表行生成一个具名中文脚本。该回归证明表达映射的一致性，不证明生产编译器已实现，也不决定最终采用哪一种表达。

## 6. 当前路由与未决边界

当前 Frozen Set 仍只允许 Pilot-A 既定 Story。FISH-R01 已通过 Evidence Review 的 13 条候选仍需 FR3 Semantic Triage，不能用本 shootout 越级进入 Representation。B4 仍是 `DESIGN_REVISE`；本文件只是 R3 具体对照，状态为 `WORKING / PRE-GATE / NOT PROMOTED`。
