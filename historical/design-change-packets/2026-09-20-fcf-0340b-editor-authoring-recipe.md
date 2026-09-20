---
document_type: HISTORICAL_DESIGN_DELTA
authority: NONE
status: APPLIED
current_authority: NOTION
do_not_use_as_current: true
lifecycle: TRANSIENT_CHANGE_PACKET_THEN_HISTORICAL_LEDGER
project: FCF
branch: 0.3.4.0-B
topic: Editor Authoring Recipe × Source × Engagement Mode Patch × Production Projection
date: 2026-09-20
---

# FCF 0.3.4.0-B｜Editor Authoring Recipe × Source × Engagement Mode Patch｜Design Delta Packet

> **Historical / application packet, not Current Authority.**
>
> 本文件只记录本轮已经 Owner-aligned 闭合、需要由单一 Notion Writer 应用到 Current 文档的设计 Delta，以及为防止旧方案复活而需要保留的 Negative Knowledge。
>
> 任何当前机制判断必须重新读取 Notion Current Authority。本文不得替代 Current，不要求与未来 Current 双向同步。

## 0. Scope / Authority

### Base Authority to rebase before application

后续 Documentation Agent 必须重新读取最新 Current，再做 exact delta application：

- FCF Router  
  https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47
- FCF L0 Documentation Governance  
  https://app.notion.com/p/3cca4137d23681599731d974a9cd4f89
- 中鱼0.3.4.0-B｜开发需求 · 编辑器界面  
  https://app.notion.com/p/3dea4137d236815b9f82d5da06da3630
- 0.3.4.0-B｜编辑器持久层契约  
  https://app.notion.com/p/3dfa4137d23681769ccddd70458922b7
- 中鱼0.3.4.0-B｜开发需求 · 编辑器与 Resolve  
  https://app.notion.com/p/3dda4137d23681408e4fe0f35ced39d9
- 配置表与校验  
  https://app.notion.com/p/3dca4137d23681e28c5bc2f29c63dc16
- 中鱼0.3.4.0-B｜中鱼因子聚合逻辑化-开发需求  
  https://app.notion.com/p/3dda4137d23681c68ec3fb1944573af4
- Working Checkpoint｜Editor Authoring Model × IA Working Baseline｜2026-09-20  
  https://app.notion.com/p/3e1a4137d23681159e91e610446e1945

### Related working inputs

- GitHub Issue #2 — Editor Authoring Model × per-Component Baseline Working Delta
- GitHub Issue #4 — Production Component Profile reuse × semantic naming policy

这两个 Issue 是历史 Working Input；本 Packet 是本轮面向下游 application 的统一闭合输入。后续 Agent 不应自行从 #2/#4 重新拼设计状态。

---

# 1. Closed Decision｜Authoring 的最小核心：Recipe，不再建立 Species Baseline Asset

## 1.1 Canonical authoring primitive

每个 Component 的 Species authoring state 收敛为：

```ts
ComponentRecipe {
  source: ComponentSource
  operations: {
    [fieldKey]?: ADD(delta) | SET(value)
  }
}
```

硬规则：

- 每层、每字段最多一个最终 operation。
- 同一层不允许 `ADD + ADD`、`SET + ADD` 等 operation chain。
- 编辑动作是替换当前格的 operation，而不是继续叠链。
- Effective Value 不是 authoring truth，不持久化为 authoring source。
- 不创建 `SpeciesComponentBaseline` 独立 Asset / ID / name / registry。

Species 层仍保留，因为它承担“同一物种多个 Engagement Mode 之间的公共 tuning”；但它只是物种自己的配置槽，不是独立 Profile Asset。

## 1.2 Four Components share one persistence primitive

P0 四个 Component：

- Temperature
- Structure
- Feeding Layer
- Time Period

都使用：

```text
Source + one-op-per-field
```

不同 Component 可以使用不同编辑工具，但不因此分裂 persistence / inheritance model。

---

# 2. Closed Decision｜Component Source 分为 Shared Template 与 Species Concrete

## 2.1 Source model

```ts
ComponentSource =
  | SharedTemplateSource
  | SpeciesConcreteSource
```

P0 allowlist：

```text
TEMPERATURE
  SHARED_TEMPLATE
  SPECIES_CONCRETE

STRUCTURE
  SHARED_TEMPLATE

FEEDING_LAYER
  SHARED_TEMPLATE

TIME_PERIOD
  SHARED_TEMPLATE
```

不要为了抽象对称让所有 Component 都提前支持所有 SourceKind。

## 2.2 Shared Template

Shared Template：

- 是完整值资产，不是 delta；
- 不允许 Template → Template live inheritance；
- 可以 Clone / Save As 创建新 Template，但创建后生命周期独立；
- 使用 stable key + display name；
- display name 改名不应自动造成 production semantic identity 变化；
- family / cluster / archetype 只可作为分类、推荐、聚类输入或 Preset 线索，不进入 live Resolve 链。

Template admission 原则：

> 如果差异可以用少量 Species operations 清楚表达，不新建 Template；只有形成真正可复用的完整模式，才升格 Shared Template。

## 2.3 Species Concrete

`SpeciesConcreteSource` 是 **species-owned concrete ecological data**，P0 明确用于 Temperature。

典型来源：

- 《钓鱼元素周期表》导入；
- 调研资料人工录入；
- 专家校准；
- 其它正式生态数据源。

它不是共享 Template，不进入 Template Library，也不能被其它 Species 引用。

Identity 可以逻辑上由：

```text
(speciesId, componentType)
```

确定，不要求再建立独立 reusable asset identity。

### Temperature provenance

Temperature canonical profile 目前含：

```text
temp_accept_min
temp_fav_min
temp_fav_max
temp_accept_max
temp_threshold
falloff_shape
```

前四项可能来自真实生态数据；`temp_threshold / falloff_shape` 更可能是游戏计算参数。

Importer / editor 必须允许字段级 provenance 差异，不能假装六个字段都来自研究数据。

### Research correction vs game tuning

必须区分：

```text
研究事实修正
→ 更新 SpeciesConcreteSource

游戏调参
→ 保持 Source，写 Species operation
```

例如：

```text
生态 Source favMax = 27
游戏想要 25
→ Species SET 25
```

而不是修改研究事实。

### Reimport

周期表重新导入时：

```text
External data
→ Candidate Source Update
→ Diff Preview
→ Update SpeciesConcreteSource
```

既有 Species operations 和 Engagement Mode patches 保留，随后重新 Resolve。

此前“Importer 默认生成一组 SET”的模型被本轮收敛替代：如果外部数据本身被认可为 Species ecological source of truth，应更新 Concrete Source，而不是伪装成 tuning operation。

---

# 3. Closed Decision｜Engagement Mode 继承 Recipe，不叠第三层 Value Delta

## 3.1 Recipe Patch

Engagement Mode 每个 Component 独立拥有可选 Patch：

```ts
EngagementModeComponentPatch {
  sourceOverride?: ComponentSourceRef
  operationPatches?: {
    [fieldKey]?: CLEAR | ADD(delta) | SET(value)
  }
}
```

字段 patch 缺省（absent）表示：

```text
follow Species operation
```

因此 Mode 继承的是 Species Recipe，而不是 Species Effective Value。

## 3.2 Operation replacement semantics

例：

```text
Template = 0.8

Species:
ADD -0.2
→ 0.6

Mode:
ADD -0.1
→ 0.7
```

Mode 的 `ADD -0.1` **替换** Species 的 `ADD -0.2`。

禁止解释成：

```text
0.8 - 0.2 - 0.1
```

或：

```text
Template + Species Delta + Mode Delta
```

Resolver 始终收敛成：

```text
Effective Source + Effective Operation = Effective Value
```

## 3.3 CLEAR semantics

Mode field patch：

```text
absent
→ 跟随 Species operation

CLEAR
→ 清除 inherited Species operation
→ 回到当前 Effective Source 的原值

ADD / SET
→ 替换 Species operation
```

因此两个 UX 动作必须区分：

```text
跟随物种配置
恢复为来源值
```

不能合并成一个模糊的“恢复”。

## 3.4 Equal value does not imply inherit

即使：

```text
Species ADD -0.2
Mode explicit ADD -0.2
```

当前数值相同，也不能自动删除 Mode patch，因为显式 override 表达独立 tuning intent。

同理：

```text
Species Source = Template A
Mode explicit SourceOverride = Template A
```

也仍然表达“Mode pin 在 A；以后 Species 换 Source 时 Mode 不跟”。

禁止从当前 payload equality 推断 inheritance。

---

# 4. Closed Decision｜Engagement Mode 可以逐 Component 独立换 Source

Mode 不使用整体 Source Bundle 作为 live parent。

它可以只在某一个 Component 上：

```text
sourceOverride = another Shared Template
```

其它 Component 继续跟随 Species。

例如：

```text
Temperature   follow Species
Structure     follow Species
FeedingLayer  follow Species
TimePeriod    sourceOverride = NightPredator
```

## 4.1 Rebase semantics

换 Source 时，默认：

> 保留继承下来的 tuning recipe，并在新 Source 上重新 Resolve。

例：

```text
Species:
Source WarmPredator
Grass ADD -0.2

Mode:
SourceOverride HeavyCoverPredator

HeavyCoverPredator.Grass = 0.9
→ 0.9 - 0.2 = 0.7
```

不要为了保持旧 Effective Value 静默生成一堆 SET。

Source change 必须提供 Result / Rebase Preview。

如果未来需要“切换来源并固定当前结果”，应作为显式工具，而不是 Source change 的默认语义。

## 4.2 Species Concrete restrictions

- 同 Species 的 Mode 默认通过 inheritance 使用 Species Concrete。
- Mode 不应把自己的 Species Concrete 显式当成共享 Source 选择项。
- 其它 Species / 其它物种的 Mode 禁止引用某 Species 的 Concrete Source。
- 如果某 concrete profile 值得跨物种复用，应显式提取为 Shared Template。
- P0 不新增 `ModeConcreteSource`；Mode 特殊差异用 Recipe Patch 表达。
- Mode 可以从 Species Concrete 显式切到 Shared Template；仍按 rebase + preview 规则执行。

---

# 5. Closed Decision｜Template / Source 修改传播规则

Source Change 只改变 Source Value，不改写 downstream Recipe。

传播：

```text
Source Change
  ↓
保持 Species / Mode Recipe 原样
  ↓
重新确定 Effective Source + Effective Operation
  ↓
Resolve
```

Operation 响应：

```text
ADD
→ 在新 Source 上重新计算

SET
→ 保持 pin value

CLEAR
→ 使用新 Source 原值

Mode absent patch
→ 跟随 Species operation

SourceOverride
→ 如果 Effective Source 已切走，则切断原 Source change 的传播
```

## 5.1 Impact Preview

Shared Template 修改默认流程：

```text
Edit Draft
→ Impact Preview
→ author confirm
→ Save Template
→ re-resolve
→ materialize affected production projections
```

Impact Preview 必须基于 before/after Resolve，不得只数引用关系。

至少区分：

1. Direct inherit changed
2. ADD re-resolved changed
3. SET blocked final change
4. SourceOverride cut propagation

需要区分：

```text
dependent
effective-source consumer
effective-value changed
```

不要把所有结构关联对象都宣称为真正受影响。

Shared Template 修改是一次全局作者确认，不制造逐引用 review debt。

---

# 6. Closed Decision｜Template Library / Family / Preset

## 6.1 No Template→Template live inheritance

禁止：

```text
FamilyTemplate
→ Template delta
→ Species delta
→ Mode patch
```

Template 自己保存 complete value。

## 6.2 Family / cluster role

所谓 family / archetype 可以保留为：

- Template category / tag
- clustering signal
- recommendation signal
- SpeciesPreset 的组织维度

但不成为 live inheritance parent。

聚类用途：

```text
existing fish profiles
→ clustering
→ candidate template
→ human review
→ Shared Template
```

而不是：

```text
cluster
→ runtime inheritance
```

## 6.3 SpeciesPreset

Preset 是一次性 bootstrap recipe：

```text
Temperature source
Structure source
Feeding Layer source
Time Period source
Opportunity Policy source
```

Apply 后退出 resolve 生命周期，不是 parent，不形成长期 dependency。

---

# 7. Closed Decision｜Opportunity Policy 复用 Recipe/Patch，但不是第五个 Component

Opportunity Policy 继续独立于四个 Component Profile。

Shared Policy Template：

```text
temperatureRole
structureRole
feedingLayerRole
timePeriodRole
failEnvCoeff
```

它使用同一 authoring primitive：

```text
Source
+ one operation per field
+ Engagement Mode Recipe Patch
```

但 Production topology 不同：

- 不生成 ProductionPolicyProfile；
- 不分配 policy profile id/name；
- Resolve 后直接 materialize 到 FishEnvAffinity 的 4 个 role columns + fail_env_coeff。

## 7.1 AggregationRole

```text
Species:
INHERIT / SET

Mode:
absent / CLEAR / SET
```

Role 不允许 ADD。

## 7.2 fail_env_coeff

本轮最终裁定：

```text
Species:
INHERIT / ADD / SET

Mode:
absent / CLEAR / ADD / SET
```

ADD 有真实业务语义：

```text
Policy Source = 0.01
Species ADD +0.01
→ 0.02
```

表达“相对这一类标准 Policy 更宽松一点”。

SET 则表达绝对 pin。

规则：

- ADD 是绝对数值增量，不是百分比 / multiplier；
- 最终 resolved value 仍必须满足 Current Contract 合法范围；
- 越界由 Validator 报错；
- 禁止 silent clamp。

---

# 8. Closed Decision｜Editor terminology

底层 Contract / schema 保持：

```text
INHERIT
ADD
SET
CLEAR
```

策划 Editor 的用户语言推荐：

```text
INHERIT → 跟随
ADD     → 调整 / 相对调整
SET     → 设置为
CLEAR   → 恢复为来源值
```

在 Mode 层需要显式区分：

```text
跟随物种配置
恢复为来源值
调整
设置为
```

不建议用户界面直接写 `ADD` 或“加减”。

典型展示：

```text
来源值       0.80
相对调整    -0.20
当前值       0.60
```

---

# 9. Closed Decision｜Production Component Profile Projection

Production 表是 Runtime Projection，不是 Authoring Graph 镜像。

## 9.1 Demand-driven materialization

只为当前 Runtime 实际需要的 final semantic profile 按需物化 production row。

不要因为 Template / Species authoring node 存在，就提前强制创建对应 production row。

## 9.2 Reuse criterion = intentional authoring sharing

Production Profile ref 沿 Authoring lineage 的显式共享关系复用。

禁止仅因为 resolved payload 当前相等就跨无关 lineage 自动 dedup。

```text
intentional sharing
≠
accidental numeric equality
```

## 9.3 Semantic fork, not numeric fork

新 production projection 的准入不是“当前数字不同”，而是：

> authoring semantic ownership / lineage 是否发生分叉。

例如：

```text
Template Grass = 0.8
Species SET 0.8
```

当前 payload 相同，但 Species 已表达独立 pin intent，因此必须成为独立 semantic projection。

建议 normalization：

```text
ADD 0
→ remove op / inherit
```

而：

```text
SET same-value
→ preserve explicit fork
```

## 9.4 Projection lifecycle

```text
无当前层有效 semantic fork
→ reuse parent projection ref

首次产生 semantic fork
→ allocate own projection

own recipe changes
→ update existing projection in place

移除当前层最后一个 fork，重新完全跟随 parent
→ collapse to parent projection ref
→ old own row becomes orphan candidate
```

不要按 payload hash 每次重新 allocate ID。

## 9.5 Policy fields do not fork Component Profile

仅修改：

- AggregationRole
- fail_env_coeff

不会创建新的 Component production profile，因为这些字段属于 FishEnvAffinity policy surface，不属于 Temperature / Structure / Layer / Time Profile payload。

---

# 10. Closed Decision｜Production naming

Production Profile 的 `name`：

- 应尽量有业务表意；
- 只用于人类阅读 / 调试；
- 不作为 join key / ownership key / reuse 判据 / authoring identity；
- 系统关联走 id/ref；
- provenance 留在 Editor persistence / diagnostics。

建议按当前 semantic owner 生成稳定可读名：

```text
Cover_WarmPredator
Cover_LargemouthBass
Cover_LargemouthBass_Mature

Temp_WarmPredator
Temp_LargemouthBass
Temp_LargemouthBass_Mature
```

不要把完整 inheritance chain 塞进 name。

Template displayName 改名不应强迫 production name 大面积变化；production token 应优先基于稳定 semantic key。

---

# 11. Negative Knowledge｜本轮明确不要重新引入

后续 Agent 不应自行恢复以下方案：

- Effective Value 作为 authoring truth。
- `SpeciesComponentBaseline` 独立 entity / registry / name。
- `LocalProfile` / `LOCAL_PROFILE` source mode，仅为了 Temperature Import。
- 元素周期表导入默认生成一组 SET，若该数据本身就是正式物种生态事实。
- Template→Template live inheritance。
- Family / cluster 作为长期 authoring parent。
- Preset 作为 live dependency。
- Engagement Mode 在 Species Effective 上继续追加第三层 delta。
- 同层同字段保存多个 operation。
- Mode source bundle 必须整套切换。
- Affinity/Mode 任意引用其它 Species 的 Concrete Source。
- ModeConcreteSource。
- payload-equality global dedup。
- Production name 承担 identity。
- Opportunity Policy 被建模成第五个 Component Profile。
- Role 进入 Component Profile。
- Shared Template edit 后产生逐 consumer review debt。
- invalid resolved value silent clamp。

---

# 12. Documentation Delta Targets｜交给单一 Notion Writer

Documentation Agent 应先 rebase 最新 Current，然后逐篇判定 exact delta，不得把本 Packet 原样复制进生产需求文档。

重点检查：

1. **编辑器持久层契约**
   - Authoring Recipe / Source / operation persistence
   - SpeciesConcreteSource
   - Engagement Mode Recipe Patch
   - CLEAR / absent semantics
   - per-field one-op rule
   - semantic projection ledger / lifecycle

2. **开发需求 · 编辑器界面**
   - Source presentation
   - Temperature concrete-data UX
   - 跟随 / 调整 / 设置为 / 恢复来源值
   - Mode per-component source override
   - Rebase Preview
   - Template Impact Preview
   - difference summary

3. **编辑器与 Resolve**
   - Effective Source + Effective Operation resolver
   - Mode patch replacement semantics
   - Source change propagation
   - SET / ADD / CLEAR behavior

4. **配置表与校验**
   - field operation allowlist
   - fail_env_coeff ADD / SET
   - validator behavior / no silent clamp
   - production projection semantics where appropriate

5. **主开发需求**
   - only when required for cross-document consistency;
   - keep the production requirement clean and concise;
   - do not inject design-history narrative.

Application requirements:

- 不修改 Pure DSL sibling。
- 不重开已闭合设计。
- 不做 Promotion，除非另有明确授权。
- 遵循 Write Hygiene：Current 文档只保留当前 Contract，不复制本 Packet 的历史推演。
- 写后逐项 readback。
- 若最新 Current 与本 Packet 存在真实冲突，停在 Human/Owner adjudication boundary，不自行覆盖 Current。

---

# 13. Open / Human Boundary

本 Packet 的上述主模型已作为 Owner-aligned Working Decision 闭合。

Documentation Agent 的职责是 rebase + exact application，不是重新设计。

如果 rebase 后发现：

- Current 已出现与本 Packet 不兼容的新裁定；
- 某一 Delta 会破坏其它 Current Contract；
- 需要跨 Branch adoption / migration；
- 需要 Promotion；

则停止并回报，不自行裁决。

---

# 14. Ledger semantics

本文件在 application 前状态为：

```text
READY_FOR_APPLICATION
```

当单一 Notion Writer 完成：

```text
Rebase
→ exact delta application
→ readback PASS
```

后，才应将本 Packet 作为 **APPLIED historical ledger record** 合入默认分支。

未来设计必须重新从 Notion Current rebase；不得从本历史文件继续维护“当前设计”。

