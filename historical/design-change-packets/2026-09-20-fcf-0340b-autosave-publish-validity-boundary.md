---
document_type: HISTORICAL_DESIGN_DELTA
authority: NONE
status: READY_FOR_APPLICATION
current_authority: NOTION
do_not_use_as_current: true
lifecycle: TRANSIENT_CHANGE_PACKET_THEN_HISTORICAL_LEDGER
project: FCF
branch: 0.3.4.0-B
topic: Autosave Durability Boundary × Publish Validation
date: 2026-09-20
depends_on:
  - PR#5@2a972ccf505f1a3d9e6c294f81324e55a2bb5e48
  - PR#9@ca22c0ea5f945e653271d1aae99fd93813531cc3
  - PR#11@99e0d38804ba9385969b119a2fd0d2324610dfb8
  - PR#12@3a4305dd925569bf6db73ef7d66b78e3c21f85ac
---

# FCF 0.3.4.0-B｜Autosave Durability Boundary × Publish Validation｜Design Delta Packet

> Historical / application packet, not Current Authority.
>
> 本文件来自 autosave × Source rebase 的完整案例验证。它修正 PR #9 中“hard invalid 不进入 durable revision”的过宽表述，使 Editor durable state 真正承担 authoring truth，而 Publish 继续承担生产合法性 gate。

## 0. Validation problem

若把所有 publish-blocking error 都禁止写入 editor-state，会出现作者无法自然修复的情况：

- Temperature Source switch 后，继承的 ADD / SET 暂时让 accept/fav 顺序非法；
- 新 Species / Affinity 尚未完成全部 required fields；
- Role 先改成 CORE / SECONDARY，但 Profile 尚未补齐；
- Shared Source 更新后，某 consumer 新出现 cross-field validation error。

如果这些状态都不能 durable persist：

```text
Editor State
≠ authoring truth
```

而会退化成“只保存已经完全生产合法的快照”，迫使 UI 额外发明长期 Draft / transaction。

这与 P0 低复杂度目标相反。

---

# 1. Correction｜Durable-valid 与 Publish-valid 分开

P0 明确区分：

```text
Durable-valid
Publish-valid
```

## 1.1 Durable-valid

Authoring state 只要满足：

- schema 可序列化；
- typed value 可表示；
- identity / key 结构合法；
- 正常 UI 操作不会制造悬空引用；
- 不含 NaN / 非法类型 / 无法解析的原始控件字符串；

就可以 autosave 到 durable editor-state。

Durable state **允许携带 Validator ERROR**。

## 1.2 Publish-valid

Publish 前执行完整 Validator / Resolve。

以下可以 durable persist，但阻断 Publish：

- Temperature 边界链非法；
- required Component/Profile 暂缺；
- Role 与 Profile 组合不完整；
- failEnvCoeff 等 contract value 越界；
- Source rebase 后产生 cross-field invalid result；
- 其它 Current Contract 定义的 publish-blocking semantic error。

原则：

> **Authoring error 是可以被保存和继续修复的状态；Production publish 才要求完全合法。**

---

# 2. Raw UI invalid 与 typed authoring invalid 不同

例如 numeric input 编辑过程中：

```text
"-"
"0."
"abc"
```

只是控件 raw buffer，不是 typed authoring state。

raw input 尚未解析成功时：

- 不写 durable typed field；
- 保留 UI local buffer；
- 显示输入错误；
- 不覆盖上一个 durable typed value。

一旦形成可解析 typed value，即可进入 authoring state，即使它使跨字段 Validator 报 ERROR。

---

# 3. Autosave state machine refinement

普通编辑：

```text
UI semantic edit
→ typed authoring state
→ run diagnostics
→ debounce/coalesce
→ atomic durable persist
```

Diagnostics 不决定是否 durable write，除非 state 本身无法结构化表示。

UI 至少区分：

```text
已保存
已保存 · 有错误
保存中…
保存失败（I/O / revision conflict）
```

不要把：

```text
Validator ERROR
```

显示成：

```text
保存失败
```

两者不是一回事。

---

# 4. Publish gate

Publish：

```text
durable editor-state revision
→ full validation
→ if blocking diagnostics > 0: BLOCK
→ else Resolve / Materialize / Production Publish
```

Publish blocker 必须定位到具体：

- owner；
- Component / Policy；
- field；
- source / patch provenance；
- 需要时包含 before/after Resolve。

---

# 5. High-impact Source mutation

Shared Template edit / Source switch / Reimport 等高影响动作仍：

```text
prepare
→ before/after Impact Preview
→ explicit confirm
→ atomic durable commit
```

但若 after-state 出现 publish-blocking Validator Error：

- Preview 必须醒目标出；
- 用户仍可确认并保存该 authoring state；
- Publish 被阻断，直到修复。

这避免为了“先换 Source 再调参数”而建立 durable Draft hierarchy。

---

# 6. Source rebase example

原 Species：

```text
Source A
favMin ADD +2
favMax SET 25
```

切到 Source B 后可能得到：

```text
favMin = 27
favMax = 25
```

此时：

```text
Source switch
→ 可以 durable commit
→ diagnostics: TEMP_RANGE_ORDER_ERROR
→ Publish blocked
```

作者随后：

```text
favMin ADD +2 → ADD -1
```

修复后：

```text
diagnostic clears
→ next autosave
→ Publish enabled
```

不需要把 Source switch 和后续 field fix 强制塞进一个长期 transaction。

---

# 7. Broken ref exception

正常 UI 不允许主动创建不存在的 SourceRef。

但由于：

- 手改文件；
- merge；
- migration bug；
- 外部 corruption；

Editor 可能加载到 broken ref。

仍按 PR #9：

```text
load tolerant
diagnose BROKEN_SOURCE_REF
Publish blocked
```

该 broken state 可以被读入并在修复过程中重新持久化其它合法编辑，但 UI 不提供“选择不存在 ref”的入口。

Hard Delete guard 继续防止正常流程制造 broken ref。

---

# 8. Resolve / Preview behavior with errors

存在 blocking diagnostic 时：

- 能解析的区域继续展示；
- 不能解析的字段 / Component 显示 Error / N/A；
- 不伪造 0 / default；
- Bake Preview 若关键输入无法形成完整 Resolved Subject，则阻断该次 Bake Preview。

允许“部分可解释”，禁止“静默补齐”。

---

# 9. Alignment with Current B validation semantics

本修正与 Current 主开发需求 §7 的“发布阻断总则”一致：

- Temperature boundary/order 等属于发布前阻断；
- Soft Profile 显式越界可保存、Resolve、Publish；
- 无可用数值 / 非法类型属于输入错误；
- Runtime 不 silent clamp / fallback。

本 Packet 只明确：

> **发布前阻断不自动等于 authoring persistence 阻断。**

---

# 10. Negative Knowledge

不要：

- Validator ERROR 一律拒绝 autosave；
- 把“已保存 · 有错误”当“保存失败”；
- 为了修复跨字段错误建立长期 durable Draft；
- Source switch 必须 after-state 完全 publish-valid 才能提交；
- raw input string 直接进入 typed durable state；
- Publish 自动修复 / clamp authoring errors；
- blocking diagnostics 被转成默认值继续 Bake。

---

# 11. Application Boundary

本 Packet 是验证产生的 correction delta，不是 Current Authority。

Documentation Agent 应在 PR #12 之后应用，并以最新 Current rebase 为前提。

Application + readback PASS 后才可作为 APPLIED Historical Ledger merge。
