---
document_type: HISTORICAL_DESIGN_DELTA
authority: NONE
status: READY_FOR_APPLICATION
current_authority: NOTION
do_not_use_as_current: true
lifecycle: TRANSIENT_CHANGE_PACKET_THEN_HISTORICAL_LEDGER
project: FCF
branch: 0.3.4.0-B
topic: Validation Corrections — Projection Reuse × Reference Sets × Archived Mutability
date: 2026-09-20
depends_on:
  - PR#5@2a972ccf505f1a3d9e6c294f81324e55a2bb5e48
  - PR#9@ca22c0ea5f945e653271d1aae99fd93813531cc3
  - PR#11@99e0d38804ba9385969b119a2fd0d2324610dfb8
---

# FCF 0.3.4.0-B｜Validation Corrections｜Projection Reuse × Reference Sets × Archived Mutability

> Historical / application packet, not Current Authority.
>
> 本文件来自 PR #11 之后的完整案例破坏测试。它不扩机制，只修正一条过度保守的 production projection 规则，并把 Source lifecycle 中两个此前未明确的 reference-set / archive 行为写死。

## 0. Validation finding summary

完整案例验证确认：

- SourceOverride 后保留 Species operation recipe：成立；
- CLEAR 返回当前 Effective Source raw value：成立；
- same-source explicit pin：成立；
- Shared Template mutation 的 propagation：成立；
- failEnvCoeff ADD / SET / CLEAR：成立；
- Archive / Replace：主模型成立。

但发现三处需要明确：

1. **semantic source-binding fork ≠ 必然 production-row fork**；
2. Template mutation impact 与 Replace References 操作的目标集合不同；
3. ARCHIVED Template 若仍允许直接编辑，会让“已归档但仍在改变 live consumers”语义过于模糊。

---

# 1. Correction｜显式 Source pin 不自动要求独立 Production Profile

PR #11 的保守表述曾把：

```text
explicit sourceOverride
→ semantic fork
→ own Affinity production projection
```

作为通用规则。

验证后修正为：

> **显式 Source pin 会造成继承关系分叉，但如果 Final Effective Recipe 恰好就是一个可复用 Shared Template 的完整值，且没有任何 Effective Operation，则 production 可以直接复用该 Shared Template 的 production profile。**

关键不是“当前 payload 相等”，而是：

```text
Final Effective Recipe
= Shared Template Source
+ zero Effective Operations
```

这是**显式、结构性的 intentional sharing**，不是 payload hash dedup。

---

# 2. Projection reuse algorithm｜按结构 lineage，不按 payload equality

## 2.1 Species

```text
Species Source = Shared Template
AND Species Effective Operations = none
→ reuse Template production profile

otherwise
→ Species-owned production projection
```

SpeciesConcreteSource 即使无 op，也不是 Shared Template reusable asset：

```text
SpeciesConcreteSource + no ops
→ Species-owned production projection
```

## 2.2 Affinity / Compat Mode

先 Resolve：

```text
Effective Source
Effective Operation per field
```

然后：

### Case A｜完全继承 Species Recipe

```text
no Affinity sourceOverride
no Affinity field patches
→ reuse Species projection
```

Species projection 本身可能已经复用 Shared Template。

### Case B｜Affinity 有显式 sourceOverride，但最终是纯 Shared Template

例如：

```text
Species Source = A
Species has no ops

Affinity sourceOverride = B
Affinity has no field ops
```

或：

```text
Species has ADD
Affinity sourceOverride = B
Affinity CLEAR removes all inherited ops
→ Effective Operations = none
```

若 Final Effective Recipe 为：

```text
Shared Template B + zero ops
```

则：

```text
→ reuse B production profile
```

即使 sourceOverride 是显式 pin，也不需要复制 B。

### Case C｜Affinity 最终仍含任何 Effective Operation

例如：

```text
sourceOverride = B
+ inherited Species ADD
```

或：

```text
Affinity ADD / SET
```

则：

```text
→ Affinity-owned production projection
```

因为该完整 Recipe 没有一个现成 reusable shared asset owner。

---

# 3. Equal-value SET 与 pure-source reuse 必须区分

```text
Shared Template value = 0.8
Affinity SET 0.8
```

虽然当前数值相等：

```text
SET 0.8
```

会阻断未来 Template 改值，因此：

```text
→ own projection
```

而：

```text
Affinity sourceOverride = Template A
no Effective Operations
```

表示：

> 未来继续跟随 Template A，只是不再跟随 Species 的 Source choice。

因此：

```text
→ 可以安全复用 Template A production profile
```

这两种 intent 不可混淆。

---

# 4. Revised principle｜Projection fork follows reusable recipe ownership

替代过度宽泛的：

```text
any semantic fork → own production row
```

使用：

> **Production projection 沿 Authoring 的显式共享 Recipe 复用。只有当 Final Effective Recipe 无法完整归属于一个现成 reusable upstream projection 时，才产生当前 owner 的独立 projection。**

P0 reusable upstream projection 只有：

- Shared Template production profile；
- Species projection（供完全继承 Species Recipe 的 Affinity 复用）。

禁止：

- 仅凭 payload equality 跨无关 lineage dedup；
- 为两个独立 Affinity 因“Recipe 恰好一样”自动共享 Affinity-owned row；
- 引入 content-addressed global dedup。

因此仍然不需要复杂 copy-on-write。

---

# 5. DirectReferenceSet 与 EffectiveConsumerSet 必须分开

Shared Template A 至少存在两种不同集合。

## 5.1 DirectReferenceSet(A)

durable state 中**直接写了 A 的 source ref** 的对象：

- Species Recipe source = A；
- Affinity sourceOverride = A；
- SpeciesPreset binding = A；
- Policy Recipe / Policy sourceOverride = A（对 Policy Template 同理）。

用途：

- Replace References 的 mutation target；
- hard-delete reference guard；
- direct binding inventory。

## 5.2 EffectiveConsumerSet(A)

Resolve 后，当前 **Effective Source = A** 的所有最终 Recipe：

- 直接引用 A 的对象；
- 通过 Species 继承 A 的 Affinity；
- 其它没有 sourceOverride、当前间接消费 A 的对象。

用途：

- Template value mutation Impact Preview；
- before/after effective-value-change analysis；
- dependency / effective-source / effective-value-changed 分类。

---

# 6. Replace References 只改 DirectReferenceSet

Replace References：

```text
A → B
```

只重写 durable direct bindings。

禁止对所有 EffectiveConsumer 自动写入：

```text
sourceOverride = B
```

否则会把原本通过 parent inheritance 的 child 变成显式 pin，静默改变 authoring topology。

正确流程：

```text
enumerate DirectReferenceSet(A)
→ choose replacement B
→ rewrite direct refs only
→ keep existing operations / patches
→ re-resolve complete graph
→ show before/after Impact Preview
→ atomic commit
```

例如：

```text
Species Source = A
Affinity sourceOverride absent
```

Replace A→B 时：

```text
只改 Species Source A→B
Affinity 不新增 sourceOverride
Affinity 自然继续跟随 Species
```

---

# 7. Shared Template mutation Impact Preview uses EffectiveConsumerSet

修改 A 的 completeValue 时，不修改任何 consumer binding。

Impact query：

```text
all Final Recipes whose Effective Source = A
→ before/after Resolve
```

分类继续为：

- effective value changed；
- ADD rebased；
- SET masked / no final change；
- CLEAR uses new source raw；
- sourceOverride cut propagation。

因此：

```text
“引用数”
“Effective Source consumer 数”
“最终数值变化数”
```

是三个可不同的数字。

---

# 8. Archive refinement｜ARCHIVED = resolve-valid, new-ref-disabled, direct-edit-locked

Shared Template 生命周期仍只有：

```text
ACTIVE
ARCHIVED
```

但补充 editability：

## ACTIVE

- 可新建引用；
- 可编辑；
- 修改前 Impact Preview；
- 可 Archive。

## ARCHIVED

- existing refs 继续 Resolve / Publish；
- 不允许创建新引用；
- 不允许直接修改 completeValue；
- 允许查看、Replace References、Restore；
- 若要修改：先 Restore ACTIVE，再走正常 Impact Preview。

原因：

> “已归档但仍能直接改变 live consumers”会让 Archive 的语义过弱且难以解释。

不新增第三个 lifecycle state。

---

# 9. Hard Delete

Hard Delete 仍只允许：

```text
DirectReferenceSet(template) = empty
```

因为没有 Template→Template live inheritance，所有有效依赖最终都能追溯到 durable direct binding。

Preset direct ref 也算 live reference。

ARCHIVED 不等于可删。

---

# 10. Production projection lifecycle under Replace / Template edit

## Template edit

- Template production identity 不变；
- pure Template consumers继续复用该 row；
- Species / Affinity own projections只在 Effective Value 实际变化时更新；
- SET-masked projection可不变。

## Replace References

### Species no ops

```text
A → B
→ production ref A → B
```

不新建 Species row。

### Species has ops

```text
A + SpeciesOps
→ B + same SpeciesOps
```

semantic owner 仍是 Species：

```text
→ update existing Species projection in place
```

### Affinity own recipe

同理，source replacement 不因为换 Source 就重新分配 Affinity projection identity；只更新该 owner 的现有 projection payload。

---

# 11. Validation note｜CLEAR 是 child-patch control state

```text
absent = inherit parent operation
CLEAR  = explicitly remove parent operation
```

因此 CLEAR 必须能作为 child patch 的 durable state 存在。

它不是第三种 numeric adjustment；它是 inheritance-control operation。

旧 adjudication 中“调整方式 add/set”的持久化表述若只覆盖 numeric adjustment，不得据此删除 CLEAR 所需的 child-patch语义。Documentation Agent application 时需明确分层，避免冲突。

---

# 12. Negative Knowledge

不要：

- explicit sourceOverride 一律复制 production row；
- 把 equal-value SET 与 pure source pin 当成同一种 sharing；
- Replace References 扫 EffectiveConsumerSet 后给 child 自动写 sourceOverride；
- Template value mutation 只按 direct refs 做 Impact；
- ARCHIVED Template 继续允许直接编辑 completeValue；
- archive = delete；
- 用 payload hash 代替 structural lineage；
- 为相同 Affinity Recipe 做跨 owner 自动 dedup；
- 因 CLEAR 不是 add/set 就把它丢掉。

---

# 13. Application Boundary

本 Packet 是验证产生的 correction delta，不是 Current Authority。

Documentation Agent 应在 PR #5 / #9 / #11 之后应用本 Packet，并以最新 Current rebase 为前提。

Application + readback PASS 后才可作为 APPLIED Historical Ledger merge。
