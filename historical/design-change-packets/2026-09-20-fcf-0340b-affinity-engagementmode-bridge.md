---
document_type: HISTORICAL_DESIGN_DELTA
authority: NONE
status: APPLIED
current_authority: NOTION
do_not_use_as_current: true
lifecycle: TRANSIENT_CHANGE_PACKET_THEN_HISTORICAL_LEDGER
project: FCF
branch: 0.3.4.0-B
topic: Affinity Authoring Patch × Engagement Mode Compatibility Bridge
date: 2026-09-20
depends_on:
  - PR#5@2a972ccf505f1a3d9e6c294f81324e55a2bb5e48
  - PR#9@ca22c0ea5f945e653271d1aae99fd93813531cc3
---

# FCF 0.3.4.0-B｜Affinity Authoring Patch × Engagement Mode Compatibility Bridge｜Design Delta Packet

> Historical / application packet, not Current Authority.
>
> 本文件只记录 PR #5 / PR #9 之后继续闭合的一处身份与投影修正：B P0 的 durable authoring owner 仍是 Affinity / FishEnvAffinityRef；Engagement Mode Patch 只作为面向未来真实 Engagement Mode 的业务抽象与兼容语义，不在 P0 提前制造真正的 EngagementMode identity。

## 0. Scope

只闭合：

1. §148「桶可以换模板」与新 Recipe/Patch 模型之间的 bridge；
2. B P0 durable owner 到底是谁；
3. Affinity Patch 与未来 Engagement Mode Patch 的关系；
4. sourceOverride / same-source pin / production projection 在该 bridge 下的语义。

不重开：

- Recipe / Source / Operation 主语义；
- Template propagation；
- Opportunity Policy；
- Autosave / Publish；
- Source lifecycle；
- Quality；
- routing / share / condition-based mode selection。

---

# 1. Closed Decision｜B P0 durable owner = Affinity / FishEnvAffinityRef

当前 B P0 已有物理 / production-compatible owner：

```text
FishQualityRef
→ FishEnvAffinityRef
```

且 §148 已裁：

```text
桶 = §121 的 Affinity 行单位
桶可以换模板
```

因此 P0 不新增真正的：

```text
EngagementModeId
EngagementModeRecord
EngagementModeRegistry
```

作为 durable identity。

当前 authoring patch 的物理 owner 应表达为：

```ts
AffinityAuthoringPatch {
  ownerFishEnvAffinityRef
  componentPatches
  opportunityPolicyPatch?
}
```

名称可在实现里按现有 Compat Mode shell 组织，但 identity 仍锚定 FishEnvAffinityRef。

---

# 2. Closed Decision｜Engagement Mode 只承担业务抽象 / future-compatible semantics

面向设计与 UX，可以继续使用：

```text
Engagement Mode / 中鱼习性模式
```

描述“相对 Species 的一组稳定行为差异”。

但在 B P0：

```text
Engagement Mode
≈ Compat authoring shell
≈ Affinity-level patch semantics
```

不是：

```text
真正具备独立 routing / share / runtime identity 的实体
```

因此：

```text
业务语义层:
Engagement Mode Patch

B P0 durable projection:
AffinityAuthoringPatch keyed by FishEnvAffinityRef
```

这两者是同一 authoring layer 的抽象 / 物理投影关系，不是两套 truth。

---

# 3. Closed Decision｜§148 桶级换模板由 Affinity sourceOverride 承载

旧 Working Checkpoint §2.1 曾写：

```text
Affinity / 习性档案不重新绑定 Template；
来源固定为 Species Effective
```

该句已被 §148 否定。

新模型中：

```ts
AffinityComponentPatch {
  sourceOverride?: ComponentSourceRef
  operationPatches?: Partial<Record<FieldKey, FieldPatch>>
}
```

因此：

```text
桶可以换模板
=
AffinityAuthoringPatch.sourceOverride
```

而不是新增另一套：

```text
AffinityTemplateBinding
EngagementModeTemplateBinding
```

双 owner。

---

# 4. Closed Decision｜Affinity sourceOverride 后保留 Species operation recipe

若 Species：

```text
Source A
Grass ADD -0.2
```

Affinity：

```text
sourceOverride = Source B
```

则：

```text
Effective Source = B
Effective Operation = Species ADD -0.2
```

得到：

```text
B.Grass + (-0.2)
```

Source switch 不自动清 Species operation。

原因：

- Source choice 与 tuning intent 是两个独立 authoring 意图；
- 自动清除 operation 会把“换来源”偷偷变成“换来源 + 删除调参”。

因此高影响 Source switch 必须提供 Rebase Preview，但不改写 Recipe。

---

# 5. Closed Decision｜Affinity field patch 替换 Species operation，不叠第三层 delta

字段级：

```text
Affinity patch absent
→ inherit Species operation

CLEAR
→ remove inherited Species operation
→ current Effective Source raw value

ADD / SET
→ replace Species operation
```

例：

```text
Source = 0.8
Species ADD -0.2
Affinity ADD -0.1
→ 0.7
```

不是：

```text
0.8 - 0.2 - 0.1
```

---

# 6. Closed Decision｜same-source explicit pin 必须保留

若：

```text
Species Source = Template A
Affinity explicit sourceOverride = Template A
```

当前结果与“跟随 Species Source”相同，但语义不同：

```text
no sourceOverride
→ future Species source change follows

explicit sourceOverride = A
→ stay pinned to A
```

禁止：

```text
sourceOverride == parent source
→ auto-remove
```

这与：

```text
no SET
vs
SET current-equal-value
```

同属“当前 payload equality 不等于 authoring intent equality”。

---

# 7. Closed Decision｜Production projection follows semantic ownership fork

B P0 production projection owner ladder：

```text
Shared Template semantic owner
Species semantic owner
Affinity semantic owner
```

显式 Affinity sourceOverride / field patch 都可构成 Affinity semantic fork，即使 resolved payload 当前与 parent 相等。

因此：

```text
explicit same-source pin
explicit equal-value SET
explicit equal-value ADD/patch
```

不得因为当前数值相同自动 collapse 为 parent projection。

P0 不以 payload hash equality 驱动跨 lineage dedup。

---

# 8. Closed Decision｜Future true Engagement Mode adoption

未来只有在真正引入至少一类以下能力时，才创建真实 Engagement Mode identity：

- Mode Share；
- Quality → multiple Mode routing；
- condition-based Mode selection；
- Runtime / Resolve 需要持有独立 Mode identity；
- 一个 Mode 跨多个现有 Affinity / physical rows 的独立 durable lifetime。

届时 adoption 目标：

```text
AffinityAuthoringPatch
→ EngagementModeComponentPatch
```

尽量保持：

- sourceOverride semantics；
- operation patch semantics；
- ADD / SET / CLEAR semantics；
- provenance；
- production materialization rules。

但这是未来 Explicit Adoption / Migration，不在 B P0 自动发生。

---

# 9. Terminology Bridge

P0 文档应区分：

```text
业务心智 / UX:
Engagement Mode / 中鱼习性模式（Compat）

durable authoring owner:
Affinity / FishEnvAffinityRef

runtime / production identity:
FishQualityRef → FishEnvAffinityRef
(no EngagementMode identity)
```

避免写成：

```text
young bucket = real Engagement Mode
mature bucket = real Engagement Mode
```

Bucket 只是当前 B P0 Affinity 分组 / 物理 owner，不应冒充长期业务 Mode identity。

---

# 10. Negative Knowledge

不要：

- 在 B P0 新造 EngagementModeId / registry；
- 把 Affinity bucket 等同真正 Engagement Mode identity；
- 同时保存 AffinityTemplateBinding 与 EngagementMode sourceOverride 两套 truth；
- Source switch 自动清掉 Species operations；
- Affinity ADD 与 Species ADD 做第三层数值叠加；
- 因 same-source / same-value 自动删显式 pin；
- 因 payload equality 自动跨 lineage dedup；
- 把未来 Engagement Mode routing 反向塞进 B P0。

---

# 11. Documentation Delta Targets

Documentation Agent rebase Current 后重点处理：

1. 开发需求 · 编辑器与 Resolve
   - 明确 B P0 durable owner = FishEnvAffinityRef / Compat Mode
   - 解释 Affinity ↔ Engagement Mode compat bridge
   - sourceOverride semantics
   - runtime no EngagementMode identity

2. 编辑器持久层契约
   - Affinity-level sourceOverride + operation patch
   - same-source pin / equal-value explicit override preservation
   - 不新增 EngagementMode durable identity

3. 编辑器界面
   - UX 可以继续显示 Engagement Mode / Compat Mode
   - 避免 bucket = real Engagement Mode 的文案暗示
   - Source switch 显示 Rebase Preview

4. 配置表与校验
   - physical mapping 仍落 FishEnvAffinityRef
   - no new runtime Mode identity

5. Working Checkpoint
   - 保留历史正文
   - 对 §2.1 stale sentence 加 supersession/status note
   - 不重写历史

---

# 12. Application / Review Boundary

本 Packet 是 Owner-aligned Working Delta，不是 Current Authority。

如果最新 Current 已出现与本桥接不兼容的新裁定，停止在 Human/Owner boundary。

Application + readback PASS 后，才能将本 Packet 作为 APPLIED Historical Ledger merge。
