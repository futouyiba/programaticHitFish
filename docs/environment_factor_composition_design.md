# FCF V1 环境因子组合设计（Design-only）

本文件解决一个比单因子公式更容易出错的问题：温度、DO、流速、深度
分别看都合理，但组合后可能对同一个物理后果重复扣减。V1 采用“事实先
合并、后果再分归属方（Owner）”的顺序。

## 0. 快速阅读

**概念**：环境组合不是把多个乘数（multiplier）相乘，而是把规范事实
（canonical facts）映射为不重复的物理后果（physical consequences）。

**整体机制**：温度、DO、流、光学、深度等事实并行进入后果映射；每个后果
绑定唯一归属方，再按明确剖面生成栖息占位（Occupancy）或任务动作（Task）
等输出。

**配置方式**：配置事实/剖面引用、单位、范围、UNKNOWN 策略、
`consequence_id`、归属方和下游阶段；禁止没有归属方的总分公式。

**中文机制描述**：先确认多个环境事实是否描述同一个物理原因，再决定由谁
结算；同一个后果只扣一次，不因“因子更多”就自动变成更难咬。

```mermaid
flowchart LR
  A[温度/DO/流/光/结构事实] --> B[Derived Facts]
  B --> C[Consequence 去重与 owner 审计]
  C --> D[Occupancy 输出]
  C --> E[Task/Arrival/Perception 输出]
```

## 1. 三层对象不可混淆

```text
Raw observation        传感器/模型原始观测
Canonical World Fact   校准后的物理事实 snapshot
Semantic consequence   对某个阶段有意义的物理后果
```

例如“高温使 DO 饱和度变化”可以在数据校准层发生；这不自动意味着高温
和低 DO 各自都能在进入/转化再扣一次。

## 2. 因果图的唯一方向

```text
observations
  → canonical facts (T, O₂, flow, depth, light, ...)
  → local derived facts (thermal band, oxygen band, current load)
  → one named physical consequence
  → one authoritative owner
  → downstream stage
```

派生事实（Derived fact）可以组合多个环境输入，但必须声明其输入和唯一
后果。禁止从同一个派生事实再生成多个同义惩罚。

## 3. 归属方（Owner）矩阵

| 物理后果 | 允许归属方 | 下游 | 禁止的第二次表达 |
|---|---|---|---|
| 节点长期适居性 | 栖息占位 | 种群分配 | 进入/E 再扣“鱼不在” |
| 当前爆发/耐力预算 | 遭遇转化任务动作剖面 | 追击/冲刺/恢复 | 栖息占位再扣同一体能后果 |
| 明确致死风险 | 安全/生命周期 | 阻断进入/声明迁移 | 栖息占位迁移 + 安全再迁移 |
| 几何遮挡/可达性 | 策略程序/生命周期（语义归属方） | 感知消费 A | T/E 再扣同一距离后果 |
| 到达时机 | 到达/T | 机会时序 | 栖息占位再扣同一到达延迟 |
| 资源消耗/恢复债务 | 历史/未来 | END-CUT 状态 | 转化再扣同一历史变化 |

一个因子可以影响多个归属方，前提是它产生的是可区分的物理后果：
例如温度同时影响长期分布和已在场鱼的爆发预算；这不是同一个“鱼不想
靠近”后果。追踪（trace）必须分别列出 consequence_id。

## 4. 组合顺序

### 4.1 数据层组合

温度、盐度、压力可以参与 DO 的测量校准；校准后只产生一个
`DissolvedOxygenFact`。校准输入不再作为独立行为惩罚下发。

### 4.2 栖息占位层组合

对每个节点 × 切片，只有在每个权重都来自独立、已命名的长期适居后果
剖面时，才允许组合：

```text
w_node = base_occupancy
         × w_thermal
         × w_oxygen
         × w_current
```

每个 `w_*` 必须声明 profile_id、输入单位、闭区间边界、UNKNOWN 行为和
consequence_id，输出为 `[0,1]` 无量纲长期权重。若两个权重表达同一后果
（例如温度和 DO 都只是“代谢压力”），必须先合并为一个剖面，不能双乘。
关键栖息占位事实为 UNKNOWN 时，V1 不向该节点新增质量，保留已有切片，
并在追踪写入原因。分配器统一负责归一化、上限和 PSU 守恒。

### 4.3 转化层组合

```text
task_budget = task_budget_profile(
  canonical_facts={temperature, DO, flow, depth}, task_id, acclimation/history
)
```

V1 由一个声明的 `task_budget_profile` 一次性消费各规范事实，输出带单位的
预算、时长或恢复债务，并声明输入字段、边界、缺失策略和 consequence_id。
不能把栖息占位权重带入转化，也不能让任务动作剖面改写机会或源 PSU；
默认不允许用链式乘法实现。

### 4.4 安全层优先级

```text
DEFINITE lethal fact
  > HYPOXIA_RISK / thermal-risk safety block
  > normal occupancy/policy evaluation
```

安全阻断是运行时禁止新进入的唯一归属方。它不追溯销毁候选，也不自动
产生第二次迁移/终结结算；后续迁移必须由生命周期契约明确接管。

## 5. UNKNOWN / 不确定性组合

因子质量状态不能被平均成一个“看起来正常”的数字：

- 任一关键致死边界不确定 → 对应安全输出 `*_RISK`，阻断新进入；
- 只有栖息占位事实不确定 → 保守不增加新可用质量，保留已有切片；
- 只有任务动作剖面不确定 → 使用声明的保守表现剖面，不改变 PSU；
- `UNKNOWN` 默认不生成新候选，并在追踪标记具体缺失因子。

不确定性本身不是随机数，也不能通过高频采样提高进入机会。

## 6. 反例推理

1. **温度→代谢、DO→代谢**：若两者最后都表示冲刺预算下降，必须合并为一个
   任务动作剖面归属方；只有可区分的耐力/恢复后果才可拆分。
2. **深度→低 DO→鱼离开**：深度只是定位输入，低 DO 的安全/栖息占位归属方
   负责后果；不能深度先扣 A、DO 再扣 E。
3. **流速→补氧→耐力**：若补氧变化已体现在规范 DO，流速不能再扣同一个
   用力惩罚；若流速另有水动力阻力，则必须声明不同任务动作后果。
4. **一个因子跨阶段**：温度影响栖息占位和任务动作表现可以成立，但必须
   展示两个 consequence_id，不得都命名为 `thermal_stress`。
5. **安全与预分配竞争**：栖息占位零权重不能触发迁移；安全/生命周期才能
   阻断运行时进入或执行声明迁移。

## 7. 编辑器要求

环境组合编辑器不允许只显示最终乘数，必须显示一张可审计图：

```text
fact inputs → derived fact → consequence_id → owner → stage
```

保存时检查：

- consequence_id 唯一归属方；
- 派生事实的输入修订版本完整；
- 同一输入未连接到同义后果；
- 安全边优先级高于正常栖息占位；
- 组合函数的单位和范围可验证；
- 任何新增交互都生成审查差异，而不是静默改变旧剖面。

## 8. 最小闭合结论

环境因子组合不是“把更多数相乘”，而是：

```text
canonical facts
→ distinct physical consequences
→ one owner per consequence
→ deterministic downstream effect
```

在归属方图和反例未闭合前，不应实现跨因子的总乘数。
