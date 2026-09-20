---
document_type: HISTORICAL_DESIGN_DELTA
authority: NONE
status: READY_FOR_APPLICATION
current_authority: NOTION
do_not_use_as_current: true
lifecycle: TRANSIENT_CHANGE_PACKET_THEN_HISTORICAL_LEDGER
project: FCF
branch: 0.3.4.0-B
topic: Editor Autosave × Publish Boundary × Source Lifecycle
date: 2026-09-20
depends_on:
  - PR#5@2a972ccf505f1a3d9e6c294f81324e55a2bb5e48
---

# FCF 0.3.4.0-B｜Editor Autosave × Publish × Source Lifecycle｜Design Delta Packet

> **Historical / application packet, not Current Authority.**
>
> 本文件只记录 PR #5 冻结之后继续闭合的新设计 Delta。未来任何 Current 判断仍必须读取 Notion Current；本文件不得作为第二 Authority，也不要求与未来 Current 双向维护。

## 0. Scope

本轮只闭合：

1. Editor authoring state 的 autosave / persistence boundary；
2. Publish 与 autosave 的关系；
3. Shared Template / SpeciesConcreteSource 生命周期；
4. broken ref / external modification 的最小处理规则；
5. Quality / Direct Fields 的 scope clarification。

不重新设计：

- Recipe / Source / Engagement Mode Patch 主模型；
- Production projection 主模型；
- Quality Stable Data；
- Editor IA / Figma topology；
- 数据迁移；
- Pure DSL。

这些若需要 Current 语义，以 PR #5 frozen packet + 最新 Notion Current 为输入。

---

# 1. Closed Decision｜Quality 不进入本轮 Authoring 扩展

最新 B Current 已明确：

- `FishQuality Stable Data` 本版不开放，入口置灰；
- FishQuality 不对环境习性 Component Profile 做 partial override；
- FishQuality 不对 AggregationRole / Gate 做 override；
- 当前只保留 `FishQualityRef → FishEnvAffinityRef` 的 production identity / mapping；
- 若某 Quality 需要不同环境习性，使用不同 `FishEnvAffinityRef`，不是新增 Quality Recipe。

因此 P0 不新增：

- `QualityTemplate`
- `QualityRecipe`
- `QualityPatch`
- Quality-level Component operations

Quality 未来重新开放时应作为独立设计增量，不因“与 Species/Mode 对称”提前建模。

---

# 2. Closed Decision｜DIRECT_FIELDS 不是新的 Species 数据层

旧文档中的 `DIRECT_FIELDS` 属于 Component Definition 的 **editor shape**，不是一个独立 Species authoring surface。

Temperature 是典型 direct-field Component，但当前更精确的 authoring model 已收敛为：

```text
SpeciesConcreteSource / SharedTemplateSource
+ Species Recipe
+ Engagement Mode Recipe Patch
```

因此不要新增通用：

```text
SpeciesDirectFields
DirectFieldsRegistry
MiscSpeciesFields
```

作为 Recipe 之外的垃圾桶。

只有真实业务字段无法归入现有 Component / Policy 且具备独立 lifecycle 时，未来才另行准入。

---

# 3. Closed Decision｜Autosave 是产品体验，不是 per-field write-through

Editor 默认 **无需用户点击 Save**。

产品 Contract：

> 用户完成一次有效的 authoring 语义编辑后，系统自动把当前 authoring state 持久化；正常编辑流程不依赖显式 Save 按钮。

但不要求：

> 每个输入字符 / 每个字段 change event 都立即单独写磁盘。

## 3.1 Semantic edit boundary

以下动作可视为一笔 semantic edit：

- numeric field 在 Enter / blur 后形成有效值；
- slider / drag release；
- ADD / SET / CLEAR 操作确定；
- Role 下拉选择确定；
- Template / Source Picker 选择确定；
- 一次离散的 create / clone / archive / restore 操作确定。

输入控件的临时字符串状态，例如：

```text
"-"
"0."
""
```

不是 durable authoring value。

## 3.2 Autosave batching

普通 semantic edits：

```text
UI edit
→ in-memory current state
→ short debounce / coalesce
→ atomic persist
```

不锁定具体 debounce 毫秒数；实现可按 UX / I/O 测试选择。

逻辑上持久化的是：

- coherent authoring object / state snapshot

而不是：

- isolated field transaction

跨字段 invariant 必须在 durable write 时保持可解释的一致状态。

## 3.3 UI state

最小 UI 只需：

```text
已保存
保存中…
保存失败
```

不需要常驻 `Save` 按钮。

---

# 4. Closed Decision｜高影响操作不是普通即时 autosave

以下动作有传播 / 批量影响，必须：

```text
prepare
→ diff / impact preview
→ explicit confirm
→ one atomic durable commit
```

至少包括：

- 修改 Shared Template complete value；
- Replace References；
- SpeciesConcreteSource reimport；
- 批量 source rebinding；
- 其它会改变多个 consumer resolved result 的 source mutation。

这里的 preview buffer 是短生命周期 UI state，不是 durable Draft Entity。

不要引入：

- SpeciesDraft
- ModeDraft
- TemplateDraft
- per-panel durable draft

---

# 5. Closed Decision｜Publish 是显式、批量、独立动作

Autosave 只改变 Editor authoring durable state。

Publish 才执行：

```text
current durable editor-state revision
→ full validation
→ resolve
→ materialize
→ production XLSX / JSON
```

硬边界：

- Autosave ≠ Publish
- Autosave ≠ Git commit
- Git commit ≠ Publish
- Publish 必须由用户显式触发
- P0 不做 per-species / per-mode 局部 production publish
- 实现可以只重写受影响物理行，但语义上是一次 consistent production snapshot

建议发布产物记录等价于：

```text
publishedFromEditorRevision
```

具体使用 revision integer / content hash / Git SHA 由实现决定，不升格为机制语义。

---

# 6. Closed Decision｜Preview 消费当前内存态；Publish 消费 durable state

Resolve Preview / Bake Preview 可以读取当前内存中的最新合法 authoring state，使作者无需等待 autosave I/O 才能预览。

Publish 不应悄悄消费未成功持久化的临时输入。

若 autosave 失败 / durable state 落后：

```text
Publish
→ BLOCK
→ 先解决持久化失败
```

不要在 Publish 按钮里隐式执行不可见 Save。

---

# 7. Closed Decision｜Autosave conflict model = optimistic detection, no auto-merge

P0 不实现多人实时协同 merge。

打开 editor-state 时记录 base revision / equivalent content identity。

每次 durable commit：

```text
disk/current revision == expected revision
→ atomic write
→ advance revision

disk/current revision != expected revision
→ BLOCK
→ report external modification
→ reload / reconcile explicitly
```

具体 revision 技术实现由 CC 决定。

禁止 silent last-write-wins。

## 7.1 Production source change 与 editor-state conflict 分开

- editor-state 被外部修改：属于 autosave conflict，阻断覆盖；
- production XLSX/JSON 被外部修改：不自动反向覆盖 editor-state authoring truth。

Production source change 只触发 diagnostics / reconcile / reimport workflow，不自动 reseed Recipe。

---

# 8. Closed Decision｜Shared Template lifecycle = ACTIVE / ARCHIVED

不要建立复杂状态机。

```text
ACTIVE
ARCHIVED
```

足够。

## 8.1 ACTIVE

- 可被新 Species / Mode / Preset 引用；
- 可编辑；
- 正常 Resolve。

## 8.2 ARCHIVED

语义：

> 不再允许创建新的引用，但已有引用继续合法 Resolve / Publish。

Archive 不：

- 自动改引用；
- 自动 fallback；
- 自动找相似模板；
- 自动复制 payload。

Archived Template 默认从普通 Source Picker 隐藏 / 降级展示。

允许 Restore：

```text
ARCHIVED → ACTIVE
```

---

# 9. Closed Decision｜Replace References 是独立高影响操作

从 Template A 切到 Template B：

```text
select old source
→ select replacement
→ enumerate consumers
→ rebase existing operations onto new source
→ before/after resolve
→ impact preview
→ confirm
→ atomic rebind
```

保持现有 Recipe operations。

禁止为了“保持旧 Effective Value”自动生成 SET。

若用户未来需要“切换来源并固定当前结果”，只能作为显式工具另行设计。

---

# 10. Closed Decision｜Template identity immutable

Shared Template：

```text
templateId
stableKey
displayName
```

其中：

- `templateId` / `stableKey` 创建后 immutable；
- `displayName` 可修改；
- display rename 不等于 identity rename。

若 stableKey 真的错误：

```text
create new template
→ Replace References
→ archive old template
```

不提供 identity rename。

---

# 11. Closed Decision｜Hard Delete 仅允许 zero-live-ref Template

只要存在 durable live reference，就禁止 hard delete。

至少检查：

- Species Component Recipe source；
- Engagement Mode sourceOverride；
- SpeciesPreset；
- 其它 durable authoring asset reference。

删除前必须显式解除 / replace 所有引用。

Archive 不要求 zero refs。

---

# 12. Closed Decision｜Preset 引用 Archived Source 时不可 Apply

Preset 是 one-shot bootstrap，不是 live parent，但它自身仍然是 durable authoring asset。

如果 Preset 指向 Archived Template：

```text
Preset
→ invalid-for-apply
```

UI 必须明确指出哪个 Source 已归档。

禁止：

- 静默跳过该 Component；
- 自动 fallback；
- 自动选 nearest template。

---

# 13. Closed Decision｜Broken Source Ref = hard diagnostic, no fallback

可能因手工编辑、merge、migration bug 等产生：

```text
sourceRef → missing asset
```

行为：

- Editor 允许加载，以便修复；
- 产生精确 `BROKEN_SOURCE_REF` diagnostics；
- Resolve / Publish 不允许把它当 inherit / default / fallback；
- Publish hard block；
- diagnostics 至少指出 owner / component / broken source ref。

原则：

```text
load tolerant
publish strict
```

---

# 14. Closed Decision｜SpeciesConcreteSource lifecycle

SpeciesConcreteSource 是 species-owned ecological data，不是 library asset。

P0 不需要：

```text
ACTIVE / ARCHIVED
```

只有：

```text
exists
absent
```

它可以：

- 当前被 Species Recipe 使用；
- 存在但当前 Recipe 改用 Shared Template；
- 被 reimport / update；
- 在未被当前 Recipe 使用时显式删除。

切换当前 Recipe Source：

```text
Concrete → Shared Template
```

**不删除 Concrete data**。

研究数据与当前游戏配置选择是两个不同意图。

---

# 15. Closed Decision｜Concrete reimport 不改变当前 Source choice

即使 Species 当前使用 Shared Template，周期表 / research reimport 仍可更新该 Species 的 Concrete Source。

Reimport：

```text
update concrete ecological data
```

不等于：

```text
switch current Recipe source to concrete
```

Source selection 继续由作者显式决定。

---

# 16. Source Picker P0

Species Temperature：

```text
当前物种生态数据（若存在）
Shared Temperature Templates
```

Species Structure / Feeding Layer / Time Period：

```text
Shared Templates
```

Engagement Mode：

```text
跟随物种
Shared Templates
```

Mode 不把 SpeciesConcreteSource 当通用 picker asset。

若 Species 当前使用 Concrete，Mode 通过“跟随物种”自然继承。

---

# 17. Validation / persistence closure

本轮机制层只锁以下行为，不锁实现细节：

- atomic durable write；
- optimistic conflict detection；
- hard invalid 不进入新的 durable revision；
- soft warning 可持久化；
- high-impact source mutation 先 preview 再 commit；
- broken refs 可加载但不可 Publish；
- Publish 必须基于成功 durable 的 editor-state revision。

具体：

- JSON / CSV / multiple files；
- debounce interval；
- revision integer / content hash / Git SHA；
- temp-file + rename / journal / fsync；
- exact module boundaries；

全部交实现侧。

---

# 18. Negative Knowledge

后续 Agent 不应重新引入：

- per-character / per-field synchronous write-through 作为产品 Contract；
- 长生命周期 durable Draft entity；
- panel-level Save transaction；
- autosave 自动 Publish；
- Save 自动 Git commit；
- Publish 自动隐式修复持久化失败；
-多人实时协同 merge；
- last-write-wins 覆盖外部 editor-state 修改；
- Archived Template 自动改 consumer refs；
- broken source 自动 fallback；
- stableKey rename；
- referenced Template hard delete；
- archive 时自动 delete Concrete data；
- Concrete reimport 自动切 Recipe Source；
- 因 editor shape = DIRECT_FIELDS 新造独立 Species Direct Fields 数据层；
- 因结构对称给 Quality 提前造 Recipe/Template。

---

# 19. CC Specification Closure Task Boundary

CC 可以直接推导并产出：

1. editor-state revision / autosave state machine；
2. atomic-write strategy；
3. persistence schema exact delta；
4. Template lifecycle schema；
5. `BROKEN_SOURCE_REF` 与 archive/preset diagnostics；
6. field/source reference validator；
7. source replace impact query；
8. test matrix；
9. recovery / external modification cases；
10. Figma / UI 状态所需的最小 view-model delta。

CC 不应自行裁：

- 新增 source kind；
- 新增 lifecycle state；
- Quality authoring model；
- 新增 draft hierarchy；
- 新增 partial publish semantics；
- 改变 Recipe / Mode Patch contract；
- 改变 Notion Authority 状态。

若现有代码结构无法以合理复杂度实现这些 Contract，回报 blocker，不通过扩机制绕开。

---

# 20. Application Boundary

后续 Documentation Agent application 时：

- 先 rebase 最新 Notion Current；
- 保持 Current 文档只写现行 Contract，不复制历史推演；
- 本 Packet 与 PR #5 都是 Delta input，不是 Authority；
- 若最新 Current 已出现冲突裁定，停在 Owner/Human boundary；
- application + readback PASS 后才可把本 Packet 作为 APPLIED historical record merge 到 main。
