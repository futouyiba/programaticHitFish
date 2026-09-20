---
document_type: WORKING_UI_COMPONENT_CONTRACT
authority: NONE
status: WORKING_BASELINE
current_authority: NOTION
do_not_use_as_current: true
project: FCF
branch: 0.3.4.0-B
topic: Fish Habit Editor UI Component Contract Phase 1
date: 2026-09-20
---

# FCF 0.3.4.0-B｜Fish Habit Editor UI Component Contract｜Phase 1 Working Baseline

> Working baseline only. Not Current Authority.
> 正式 Freeze 前必须对最新 Notion Current 做一次 delta review。

## 1. 产品拓扑

- 左栏：对象导航（Species / Affinity / Template）。
- 中栏：上下文总览（Component Profiles、Spatial Opportunity Policy、Validation / Affected Objects）。
- 右栏：焦点编辑。
- 中栏与右栏不得形成两套重复编辑器。

Phase 1 组件：ObjectContextHeader、ComponentCard、SourceSelector、FieldOperationControl、FieldValueRow、ValidationIndicator、AutosaveStatus、ComponentDetailEditor、RoleControl、SpatialOpportunityPolicy、TemplatePicker、TemplateWorkspace、ImpactPreview、TemperatureProfileEditor、TemperatureCurvePreview、SpeciesConcreteSourcePanel。

## 2. Structure Vertical Slice

验收故事：Template A / B → Species ADD → Affinity sourceOverride → CLEAR → ADD → SET → Follow Species → negative Effective Fit ERROR → autosave → publish block。

核心样例：
- Template A Heavy Cover：Grass 0.80、Rock 0.40、Fallen Tree 0.60。
- Template B Rocky Shore：Grass 0.90、Rock 0.70、Fallen Tree 0.10。
- Bass Species 使用 A：Grass ADD -0.20、Rock NONE、FallenTree SET 0.50。
- Bass Mature 初始继承 Species。

## 3. Source × Operation 正交

Species Source：BOUND_SOURCE。
Affinity Source：FOLLOW_SPECIES_SOURCE 或 PIN_SOURCE(sourceRef)。same-source pin 合法且有意义。

Species Operation：NONE / ADD / SET。
Affinity Operation：INHERIT / CLEAR / ADD / SET。

硬规则：
- Source change 保留 Operations。
- Operation change 保留 Source。
- Affinity ADD / SET 替换 Species Operation，不形成第三层叠加。

Resolve：NONE 直接使用 SourceValue；ADD 为 SourceValue + delta；SET 为绝对值。

## 4. FieldValueRow

折叠态只显示：字段名、当前操作摘要、Effective Value、Diagnostic。
展开态显示：Current Source、Inherited Operation、Local Operation、Effective Value、Provenance / formula。
被替代的 parent operation 只用于解释 provenance，不继续参与链式计算。

Species 用户语言：仅使用来源 / 调整 / 设置为。
Affinity 用户语言：沿用物种操作 / 仅使用当前来源 / 调整 / 设置为。
不暴露 CLEAR / Override / Reset 等工程词。

ADD→SET、SET→ADD 的 pending 默认值应尽量保持当前 Effective Value；未确认前不写 durable state。INHERIT / CLEAR 是明确语义动作，不做自动保持结果。

## 5. Tier

Tier 不是第三条计算轴。
- ADD = relative tuning intent，tier metadata 视为 CUSTOM。
- SET 可以使用 PREFERRED 1.00 / SUBOPTIMAL 0.60 / ACCEPTABLE 0.25 / REJECT 0.05 / CUSTOM。
- 禁止从裸 numeric value 自动反推 Tier。

## 6. Validation × Autosave

区分 raw input invalid、typed semantic invalid、I/O save failure。
- raw input 如 '-' / '0.' / 'abc' 不进入 typed durable state。
- typed semantic invalid 可 durable autosave，显示“已保存 · 有错误”，Publish Block。
- 保存失败只表示 I/O / revision conflict / atomic write failure。

Autosave UI：已保存 / 已保存 · 有错误 / 保存中… / 保存失败。

## 7. ComponentCard + DetailEditor

ComponentCard 只显示：Component identity、Source summary、Role badge、local operation count、diagnostic count、profile presence、source health。
不显示 mini heatmap，不直接编辑 Source，不展开完整 provenance。

ComponentDetailEditor 负责 SourceSelector、FieldValueRow × N、Filters、Diagnostics。
Structure Filter：全部 / 本层修改 / 问题。
不增加二级 Field drawer；FieldValueRow 原地展开。

## 8. SourceSelector + Rebase Preview

Affinity 可“跟随物种来源”或“固定来源”。same-source pin 必须显示“当前值不变，但继承关系变化”。

Source Change 为高影响动作：candidate source → before/after resolve → Rebase Preview → explicit confirm → atomic commit。

Rebase Preview 至少展示：当前结果变化、当前结果不变、被 SET 遮罩、新增 Error、新增 Warning。Masked Source Change 不等于无影响。

## 9. Profile × Spatial Opportunity Policy

Profile 回答：这条鱼对这个环境轴是什么习性？
Role 回答：这份习性在 Spatial Opportunity 中如何被消费？

Role change 不创建 Profile、不删除 Profile、不修改 Profile 数值。

中栏集中展示 Temperature / Structure / Feeding Layer / Time Period Role 与 fail_env_coeff。ComponentCard 只显示 Role badge，不承担第二套完整 Role mutation surface。

## 10. RoleControl / fail_env_coeff Working Contract

Species Role：CORE / SECONDARY / IGNORED。
Affinity Role：沿用物种角色或本层 SET。

Working Delta：Role 的 CLEAR 在 Current 中缺少独立 Source/Base 语义；Phase 1 UI 不暴露 CLEAR。最低复杂度模型为 INHERIT / SET。

fail_env_coeff 属于 Spatial Opportunity Policy，不属于某个 Component。始终显示，不根据当前是否 Background Fish 隐藏。
Working UI 暂用：Species base / ADD / SET；Affinity INHERIT / ADD / SET。
Working Delta：fail_env_coeff CLEAR 缺少明确 Base/Source 语义，Phase 1 UI 暂不暴露。

Diagnostics ownership：Field → FieldValueRow；Profile → ComponentCard；Policy → SpatialOpportunityPolicy；Publish/global → App header / Validation Summary。

## 11. Profile lifecycle

Role = IGNORED 时不删除 Profile。Role 是消费策略，Profile 是配置事实。
P0 不建立通用 Remove Component Profile。

TimePeriod 支持合法 Empty State：Role = IGNORED 且 Profile absent。
IGNORED → CORE 可先 autosave Role；若 Profile 仍 absent，则 semantic ERROR、Publish Blocked，并 focus Setup State。

## 12. Feeding Layer

Feeding Layer 直接复用 tieredNumeric，包含 SURFACE / MIDDLE / BOTTOM，不需要新 Component 类型。

## 13. Time Period

Preset 不负责创建 Source；需先有 Source binding。
晨暮型 / 昼行型 / 夜行型属于 one-shot batch operation generator，不是 Source / Template / durable preset identity。
应用后一次生成 5 个本层 SET，可携带明确 Tier metadata；使用轻量 Batch Preview + atomic commit。

## 14. Temperature

Temperature 复用 Authoring 骨架，但使用专属 Detail Editor。

Field capability：
- acceptMin / favMin / favMax / acceptMax / threshold = numericRelative。
- falloff_shape = enumAbsolute。

P0 曲线只读：Fields → Resolve Effective Temperature Profile → render curve。
Cross-field invariant：acceptMin ≤ favMin ≤ favMax ≤ acceptMax；相等合法。非法组合可 durable 保存但 Publish Blocked。
temp_threshold 不改变曲线，只作为 CORE Gate threshold；非 CORE 时仍显示和保存，但标注当前不消费。

SpeciesConcreteSource 不伪装成 Template。生态数据 reimport 只更新 SpeciesConcreteSource payload，不自动切 current Recipe source；使用独立 Reimport Preview。

## 15. Field Capability Map

tieredNumeric：Species NONE / ADD / SET；Affinity INHERIT / CLEAR / ADD / SET；SET 可携带 affinityTier。
numericRelative：Species NONE / ADD / SET；Affinity INHERIT / CLEAR / ADD / SET。
enumAbsolute：Species NONE / SET；Affinity INHERIT / CLEAR / SET。

映射：Structure / Feeding Layer / Time Period → tieredNumeric；Temperature bounds / threshold → numericRelative；Temperature falloff_shape → enumAbsolute。

## 16. Template Workspace

Template Workspace 使用同样三栏：左模板导航 / 中模板上下文 / 右模板值编辑。
Template 是 Source Asset，不是 Recipe。Template Value Editor 直接编辑 completeValue，不出现 ADD / SET / CLEAR / INHERIT / SourceSelector。

display name / description 等 metadata 可 autosave。
Template completeValue 修改：candidate buffer → Impact Preview → explicit confirm → atomic commit。不是普通 field autosave。

Impact Preview 必须区分：直接引用 / 实际使用 / 最终结果变化。
Template Value Edit 的 Impact 使用 Effective Consumers；Replace References 的 mutation target 只使用 Direct References。
禁止给继承 child 自动写新的 sourceOverride。

## 17. Template lifecycle

生命周期：ACTIVE / ARCHIVED。
ARCHIVED：existing refs 继续 Resolve / Publish；不允许创建新引用；completeValue direct edit locked；可查看引用、Replace References、Restore。
Hard Delete：DirectReferenceCount > 0 时 blocked。

Extract Template from current fish：Resolve 当前 Component effective profile → create new Shared Template。
只创建资产，不自动 switch current fish source，不清 current operations，不 rewrite recipe。

## 18. Working Contract Deltas to review against Current

1. falloff_shape 是 enumAbsolute，SET only，不得 ADD。
2. affinity_tier 只适用于 tieredNumeric；Temperature 不应全局 required。
3. TimePeriod preset 是 one-shot batch SET，不是 Source / Template，不持久化 preset identity。
4. Role 的 CLEAR 当前缺少独立 Source/Base 语义；最低复杂度模型为 INHERIT / SET。
5. fail_env_coeff CLEAR 同样缺少明确 Base/Source；Phase 1 UI 暂不暴露。
6. P0 不建立通用 Remove Component Profile；只支持 TimePeriod 已有合法 Empty Setup。
7. Template completeValue 修改是高影响 staged commit，不是普通 autosave。
8. Extract Template 只创建 Template，不自动重绑当前 Recipe。

分类：1/2 = schema correction candidate；3/6/7/8 = 产品/交互 Contract；4/5 = Current ambiguity，Freeze 前必须 delta review。


## 19. Completeness Pass｜已裁定行为护栏

本节补齐 Phase 1 推演中已经形成、但首个压缩版 commit 未完整记录的行为 Contract。若本节与前文摘要粒度不同，以本节更具体的约束为准；仍须在 Freeze 前对 Notion Current 做 delta review。

### 19.1 三栏 IA 的独立 Context / Focus 状态

中栏 Context 与右栏 Focus Editor 不是同一个导航状态。

- 中栏可以切到新的 Species / Affinity / Template Context；
- 右栏可以暂时停留在此前打开的对象 / Component；
- 两边允许短暂 detached，但必须显式提示，不能让用户误以为右栏仍在编辑当前中栏对象；
- 中栏与右栏各自维护本地导航 / 返回历史，不强制同步回退；
- detached 只是一种 UI navigation state，不产生新的 durable authoring entity。

推荐提示：

- 右栏标题明确对象身份；
- detached 时出现弱警示条 / 颜色变化；
- 提供“切回当前上下文”等低成本动作。

中栏下部的 Affected Objects / Validation 区属于 Context Surface，可滚动、可调高度；不侵占 ComponentCard 主阅读区。

### 19.2 P0 durable owner：Affinity / FishEnvAffinityRef

P0 的 durable patch owner 仍是 Affinity / `FishEnvAffinityRef`。

UI / 业务语言可以使用 Engagement Mode / Compat shell，但 Phase 1 不得据此创建：

- durable `EngagementModeId`；
- Engagement Mode registry；
- 独立 Engagement Mode runtime identity；
- ModeConcreteSource。

如果未来真正出现可共享、可路由、具独立 runtime identity 的 Engagement Mode，必须作为显式 adoption / migration 处理，不能从当前 UI 名称反推 P0 已有该实体。

### 19.3 Soft Fit 完整校验语义

Soft Fit 校验看 **Effective / resolved value**，不是 ADD operand 的正负。

- Effective < 0：ERROR；durable editor-state 可保存；Publish Block；Runtime 不得接收。
- 0 ≤ Effective ≤ 1：Normal。
- Effective > 1：WARNING；Publish Allowed；Runtime 使用原 authored / resolved value，不 clamp。
- 不允许 runtime clamp / abs / shift / normalize / signed-weight adapter。
- 负 ADD delta 本身合法，只要最终 Effective ≥ 0。

`0` 不自动等于 Gate Fail。Gate 语义由 Role / Runtime evaluation 决定。

### 19.4 CORE owns Gate；不增加 Gate 开关

Authoring UI 不提供独立：

- Gate ON/OFF；
- GatePolicy toggle；
- Field-level Gate switch。

CORE Role 自带 Gate 语义；SECONDARY / IGNORED 不承担该 Gate。Role 是消费策略，不是 Profile 本体字段。

### 19.5 FieldValueRow 的显示与 durable 细则

Affinity patch absent 时：

- Species 有 ADD：显示“沿用物种调整”；
- Species 有 SET：显示“沿用物种设置”；
- Species 无 operation：显示“仅使用来源”，不要显示空洞的“沿用物种操作”。

`CLEAR`：

- 虽然 Effective Value 可能等于 Source raw value；
- 仍然是明确的 durable local operation；
- 必须计入 localOperationCount；
- UI 文案为“仅使用当前来源”。

仅切换 Operation 菜单类型不能自动制造 durable intent：

- 不能因为选了“调整”就写 `ADD(0)`；
- 不能因为选了“设置为”就直接写 equal-value `SET(current)`；
- equal-value SET 是真实 pin，必须在用户确认 typed value 后才 durable。

### 19.6 SourceSelector 异常态

**Archived Source**

- 既有 durable 引用继续合法；
- 继续 Resolve / Publish；
- SourceSelector 显示“已归档”；
- 不允许创建新的引用；
- Picker 默认不提供 archived source 作为新选择；
- 不视为 ERROR。

**Broken Source Ref**

- load tolerant；
- 显示明确 Source Missing；
- ERROR + Publish Block；
- 禁止自动 fallback；
- 禁止自动切回 Species Source；
- 禁止自动选择默认模板 / 最近似模板；
- 必须由作者显式选择新的合法 Source。

### 19.7 Temperature：禁止 silent repair

Temperature cross-field invalid 时：

- 不自动 sort 四个 boundary；
- 不交换字段身份；
- 不 clamp 到相邻 boundary；
- 不把作者输入 silently 改成“合法值”。

非法 typed state 可 durable 保存并产生 ERROR / Publish Block。

当 profile 无法满足：

`acceptMin ≤ favMin ≤ favMax ≤ acceptMax`

曲线区不得伪造一条自动修正后的曲线。应显示 Profile 当前不可绘制 / 请修复边界关系。

Temperature 不使用 Affinity Tier；Temperature numericRelative / enumAbsolute 字段 UI 不出现 PREFERRED / SUBOPTIMAL / ACCEPTABLE / REJECT。

### 19.8 Temperature Source capability 边界

`SpeciesConcreteSource`：

- 属于当前 Species；
- 不进入 Shared Template Library；
- 其他 Species / Affinity 不得显式引用另一个 Species 的 Concrete；
- 不存在 `ModeConcreteSource`；
- 若 Concrete 值值得跨 Species 复用，应提取为 Shared Template。

Concrete reimport：

- 更新 Concrete payload；
- 不切当前 Recipe Source；
- 不产生 Recipe operation；
- 若当前 Recipe 使用该 Concrete，则下游通过正常 Resolve 传播；
- 使用独立 Reimport Preview。

### 19.9 TimePeriod 状态保持

Preset 应用后：

- 原 Source binding 仍存在；
- 即使五项均由 SET 遮罩，也不删除 / 弱化 Source；
- Preset identity 不持久化。

Role 从 CORE / SECONDARY 改回 IGNORED：

- Profile 保留；
- Source 保留；
- Operations 保留；
- 只是当前不参与计算。

IGNORED + 已配置 Profile 时，Profile 自身若存在 ERROR，仍然显示并可阻断 Publish；不能因为当前不消费而隐藏脏数据。

Phase 1 示例使用 5-member TimePeriod Catalog；稳定 key / label 以 Notion Current 为准，不由本文件重定义 Catalog Authority。

### 19.10 Publish with blocking error

Working UI decision：

- blocking ERROR 存在时，Publish action 不应仅被灰掉而没有解释；
- 用户触发 Publish 后进入 Validation Summary；
- Summary 明确列出 blocking diagnostics；
- 每条 diagnostic 可定位到 Component / Field；
- 最终 Publish execution 仍被阻断。

如果后续实现选择 disabled button，也必须提供等价且可发现的原因与定位入口；不能形成“按钮为什么不可用”的黑盒。

### 19.11 Template identity / lifecycle 护栏

Template：

- `templateId` / `stableKey` immutable；
- display name / description 可编辑；
- stableKey 若确实设计错误：创建新 Template → Replace References → Archive old；
- 不提供直接编辑 identity 的普通 UI。

Archive：

- 只需要轻量确认，不需要完整数值 Impact Preview；
- 既有 consumer 的当前结果不变。

Restore：

- ARCHIVED → ACTIVE；
- values / identity / refs 不变；
- 不需要 Impact Preview。

Hard Delete：

- 仅当 DirectReferenceCount = 0 才允许；
- DirectReferenceCount > 0 时必须阻断，并引导查看引用 / Replace References；
- 不做自动 Replace / fallback。

### 19.12 Template Impact / Replace References 细则

Template Context 至少区分：

- 直接引用；
- 实际使用。

Template Value Impact 至少区分：

- 最终结果发生变化；
- 当前结果未变但被本地 SET / operation 遮罩。

Masked consumer 不能被描述为“完全不受影响”。

Replace References：

- mutation target 只允许 DirectReferenceSet；
- inherited child 不写新的 sourceOverride；
- 替换 Source 时已有 ADD / SET / CLEAR 全部保留；
- 影响展示使用重新 Resolve 后的 Effective Result，而不是只 diff 两个 Template payload。

### 19.13 Explicit Negative UI Contract

Phase 1 明确不做：

- ComponentCard mini heatmap；
- Card 内直接 Source dropdown；
- Field 二级 drawer；
- operation history timeline；
- 每行永久展开完整 provenance；
- 每个字段常驻显示 Source / Species / Affinity 三层 debugger；
- 独立 Gate 开关；
- Template editor 内的 ADD / SET / CLEAR；
- 通用 Remove Component Profile；
- Temperature P0 曲线拖拽编辑。

这些不是“尚未实现”，而是当前为了控制总复杂度主动排除的交互。

### 19.14 Template inheritance 边界

Shared Template 是 complete-value asset：

- 不支持 Template → Template live inheritance；
- clone / save-as 后成为独立 Template；
- family / archetype / cluster 只用于分类、推荐、preset / bootstrap signal；
- 不构成 runtime / live inheritance parent。

不得因为模板名称或分类相似而形成隐藏继承链。

### 19.15 Structure Figma / Code 共用验收 variants

第一条 Structure vertical slice 至少覆盖：

1. Species + Shared Template + ADD；
2. Affinity Follow Species Source + inherited operation；
3. Affinity fixed different source + inherited Species operation；
4. Affinity same-source explicit pin；
5. Affinity CLEAR；
6. Affinity local ADD；
7. Affinity SET / Tier；
8. Source Change Rebase Preview；
9. Effective Soft Fit < 0 ERROR + autosave + Publish Block；
10. Effective Soft Fit > 1 WARNING + Publish Allowed；
11. Broken Source Ref；
12. Archived Source existing-reference state；
13. Publish Validation Summary / diagnostic localization。

这组状态作为 Phase 1 Figma 与 Code 的共同 acceptance story，避免两边各自重新解释 Contract。



## 20. Exhaustive Integration Guardrails｜跨 UI / Persistence / Projection 补齐

本节补齐第二轮完整性审计中发现的跨层约束。目的不是扩大 Phase 1 scope，而是防止 Figma / Code 在实现 UI Contract 时重新发明已经裁定的 persistence、projection 或 scope 语义。

### 20.1 Authoring Truth：持久化意图，不持久化 resolved value

Editor durable state 保存：

- Source binding / sourceOverride；
- Species operation；
- Affinity patch；
- Role / Policy authoring intent；
- Template completeValue；
- 必要 identity / lifecycle metadata。

Editor durable state **不把 Effective / resolved value 当第二份可编辑真相**。

Effective Value、provenance、diagnostics、Impact result 均由当前 durable authoring state + schema / resolver 派生。

因此：

- 不持久化一份独立 “resolved value cache” 作为 authoring truth；
- 不持久化 diagnostics list 作为第二真相；
- UI 上的 Effective Value 是 read-only derived result；
- equal payload 不允许反向覆盖 authoring intent。

### 20.2 Autosave 物理语义

普通 authoring mutation 使用 autosave UX，但不是 per-keystroke / per-character 同步写盘。

推荐物理行为：

```text
semantic edit
→ in-memory typed current state
→ short debounce / coalesce
→ atomic persist coherent editor-state object / revision
```

默认不提供普通 “Save” 按钮。

高影响动作例外：

- Source Change；
- Shared Template completeValue mutation；
- Concrete Reimport；
- TimePeriod batch Preset；
- Replace References。

这些动作使用：

```text
prepare candidate
→ Impact / Diff Preview
→ explicit confirm
→ one atomic durable commit
```

Preview candidate 只是短命 UI state，不形成 durable Draft Entity。

### 20.3 Preview 与 Publish 读取边界

- Inline / local Preview 可以读取当前最新、typed-valid 的 in-memory candidate；
- Publish 只读取成功 durable persist 的 editor-state revision；
- raw input 尚未形成 typed mutation 时不得参与 Publish；
- 若存在尚未确认的 staged high-impact candidate，Publish 不得偷偷把 candidate 当 durable truth。

### 20.4 Revision conflict

Editor persistence 使用 optimistic conflict detection：

- load 时保留 expected revision / hash；
- commit 时只在 expected revision 仍匹配时写入；
- external editor-state change 发生后，禁止 last-write-wins；
- 禁止静默 auto-merge；
- 进入 reload / compare / reconcile 路径。

“生产配置外部变化”与“Editor State revision conflict”是两类不同问题，不得混为同一个保存失败原因。

### 20.5 Source capability matrix

P0 不要求所有 Component 支持所有 Source kind。

**Structure**

- Species：SharedTemplateSource；
- Affinity：follow Species 或 pin 合法 SharedTemplateSource。

**Feeding Layer**

- Species：SharedTemplateSource；
- Affinity：follow Species 或 pin 合法 SharedTemplateSource。

**Time Period**

- Species：SharedTemplateSource；
- Affinity：follow Species 或 pin 合法 SharedTemplateSource；
- Profile 可以在特定合法 Empty State 下 absent。

**Temperature**

- Species：SharedTemplateSource 或当前 Species 自己的 SpeciesConcreteSource；
- Affinity：follow Species，或 pin 当前 Species 可合法使用的 Temperature Source；
- 不得 pin 另一个 Species 的 Concrete。

不要为了统一 SourceSelector 而给 Structure / Feeding / TimePeriod 发明 Concrete Source。

### 20.6 SourceOverride 的语义

`sourceOverride` 只固定 Source Choice，不冻结全部配置。

因此：

- Affinity pin Source 后，若 patch absent，仍可继承 Species operation；
- SourceOverride 不自动 SET 全部字段；
- SourceOverride 不清 Existing Operations；
- same-source pin 是真实 authoring intent；
- 解除 pin = 删除 sourceOverride，重新跟随 Species Source。

### 20.7 Species field edit 的 Impact 强度

不是所有传播修改都需要 Modal。

**普通 Species field ADD / SET**

- 可在当前 Row 附近显示下游影响摘要；
- 正常 autosave；
- 不要求每次二次确认。

推荐摘要：

```text
将改变 3 个档案
1 个档案有本层覆盖，不受当前结果影响
```

**Component Source Change**

- 必须 Rebase Preview + explicit confirm。

**Shared Template Value Change**

- 必须 Effective Consumer Impact Preview + explicit confirm。

用不同强度对应不同 blast radius，避免所有编辑都被重型确认拖慢。

### 20.8 fail_env_coeff 数值 Contract

`fail_env_coeff` 的 ADD 是 **绝对数值 delta**，不是百分比，也不是 multiplier。

例如：

```text
0.01 + 0.01 → 0.02
```

不是：

```text
0.01 × 1.01
```

当前生产有效范围：

```text
0 ≤ fail_env_coeff ≤ 0.10
```

越界是 ERROR + Publish Block，不是 WARNING。

UI 文案优先使用“调整 / 相对调整”，避免向策划暴露 ADD 工程词。

Editor 没有 FishPond Context，因此：

- 不根据当前对象臆测 Background Fish；
- fail_env_coeff 始终可以查看；
- 背景鱼实际 Gate Fail 使用 Opportunity Seed / envCoeffMin 的 runtime 规则，不由本 Editor 隐藏字段来表达。

### 20.9 Role inheritance 的 mutation 语义

在当前 Working Contract 下，Affinity Role：

```text
patch absent
→ inherit Species Role

local SET
→ use Affinity Role
```

“恢复为物种角色”应实现为删除 local SET / 恢复 absence，而不是写另一个等值 SET。

不要根据数值 / enum 相等自动推断“已恢复继承”。

### 20.10 Profile presence 的 P0 capability

Phase 1 Authoring capability：

```text
Temperature   profileCanStartAbsent = false
Structure     profileCanStartAbsent = false
FeedingLayer  profileCanStartAbsent = false
TimePeriod    profileCanStartAbsent = true
```

如果 Bootstrap / migration 后前三者缺失，应作为迁移 / 数据错误处理，不应因为 Role=IGNORED 就把它包装成常规空态。

TimePeriod 是当前明确支持 Empty Setup 的 Component。

### 20.11 TimePeriod Setup transaction

当 TimePeriod Profile absent 时：

1. Role 可以先从 IGNORED 改成 CORE / SECONDARY，并形成 semantic ERROR；
2. Detail Editor 自动进入 Setup State；
3. 作者选择合法 Source；
4. 建立完整 Recipe / Source binding；
5. 缺 Profile ERROR 消失；
6. 作者随后可继续逐字段操作或应用 one-shot Preset。

不能创建一条 required Source / identity 为 null 的半成品 Profile record。

### 20.12 TimePeriod Preset Preview

Preset batch preview 至少显示：

- 5 个 period before / after；
- 将替换多少已有 local operations；
- 将新增多少 local operations；
- 是否新增 ERROR / WARNING。

确认后 5 项作为一个 atomic authoring commit。

Preset 选择本身不成为长期 mode；应用后每个 period 独立编辑。

### 20.13 Temperature Curve / Threshold 展示

TemperatureCurvePreview 是 derived visualization。

- P0 不可直接拖拽编辑；
- CORE 时可显示 threshold 参考线并说明 Gate active；
- SECONDARY / IGNORED 时 threshold 仍显示 / 保存，但标记“当前不参与 Gate”；
- threshold 不改变 curve shape；
- cross-field invalid 时曲线进入 Invalid Profile state，而不是 auto-repair。

### 20.14 Template candidate edit 生命周期

Shared Template completeValue 修改可在 UI 中暂存多项 candidate edit。

推荐状态：

```text
N 项待审查修改
[撤销] [审查修改]
```

candidate：

- 不自动 durable；
- 离开 Workspace 时若仍存在，应显式丢弃 / 留在当前 session，不得悄悄持久化为 Draft Entity；
- confirm 后一次 atomic commit；
- Impact Preview 以 candidate resolved result 对比 current durable result。

### 20.15 Template direct references 必须包含非鱼对象引用

DirectReferenceSet 不只包括 Species / Affinity。

凡 durable ref 显式指向 Template，都计入 hard-delete / replace guard，例如：

- Species sourceRef；
- Affinity sourceOverride；
- Preset 内的 sourceRef（若 Current 存在该引用形式）；
- 其他 Current 明确定义的 direct durable refs。

因此 hard delete 的 “DirectReferenceCount = 0” 必须覆盖这些 ref owner，不能只扫描鱼。

若 Preset 指向已 ARCHIVED Source：

- Preset 不得静默 fallback；
- 不得跳过该字段后继续应用；
- 应阻断 apply 并明确 source 已归档 / 不可用于新引用。

### 20.16 Production projection boundary

Production 是 Editor Authoring 的 runtime projection，不是 Authoring Graph 镜像，也不能用 payload equality 反向决定 authoring topology。

Projection reuse 依照结构化 authoring intent：

- Species 使用 Shared Template 且无 effective local operation：可复用该 Template 的 production profile；
- Affinity 完全 follow Species：可复用 Species projection；
- Affinity explicit sourceOverride 到 Shared Template 且无 effective local operation：可复用该 Shared Template projection，即使 Source Choice 是显式 pin；
- 任意 effective ADD / SET 存在：该 owner 需要 own projection；
- equal-value SET 仍是 pin，因此不能因为 payload 相同就 collapse；
- SpeciesConcreteSource 即使无 operation，仍是 Species-owned projection；
- 不允许把互不相关 owner 仅因当前 payload hash 相等就全局 dedup。

Production profile identity 应稳定；owner recipe 改变时优先原位更新其 projection。若 local semantic fork 被删除并重新 collapse 到 parent projection，旧 own row 才成为 orphan candidate。

Production profile `name` 只是人类可读 label，不是 identity / join / reuse key。

### 20.17 Spatial Opportunity Policy 的 production projection

Spatial Opportunity Policy 不是第五个 Component Profile。

Role / fail_env_coeff 等 Policy authoring state 在 Publish 时投影到既有 runtime / FishEnvAffinity physical fields。

UI / code 不应为了统一 ComponentCard 而制造一个新的 “Policy Component Profile” production asset。

### 20.18 Bootstrap / Production→Editor P0 boundary

当前 release 的 Production→Editor 能力只包含 **one-time Initial Bootstrap**：

```text
existing Production config
→ bootstrap / seed editor durable state
→ thereafter Editor State is authoring truth
```

P0 不提供持续的 Production→Editor bulk reconcile / adopt production values。

允许的 P0 后续能力最多是 read-only drift detection / status；不得在 Fish Habit Editor 中出现：

- Adopt Production；
- Import Production Changes；
- bulk reverse reconcile；
- 从 Production 反推 Template / Species / ADD / Concrete authoring intent。

持续 Reconcile 属于下一 release / 后续显式设计。

### 20.19 Bootstrap 与 Phase 1 UI 的关系

`BootstrapSurface` 可由并行实现处理，但不改变 Phase 1 Authoring Contract。

Roundtrip smoke test 应验证：

```text
Production
→ Initial Bootstrap
→ Editor
→ no authoring edits
→ Publish
→ Production semantic parity
```

这用于验证迁移完整性，不意味着 Production 重新成为持续 authoring truth。

### 20.20 Quality P0 scope guard

Quality / Fish Quality 虽然业务上可能未来需要自己的编辑面，但当前 B P0 的 Quality Stable Data / Quality Recipe / Quality Template 不在本 Phase 1 Editor scope。

因此 Figma / Code 不应在本阶段：

- 新建 Quality Template library；
- 把 Quality 作为第五个 habit Component；
- 为 XP / coin / length / weight 引入新的 Source / Recipe / Patch 链。

若后续 Current 明确启用 Quality authoring，再作为独立增量进入。

### 20.21 Object navigation Phase 1 scope

左栏 Phase 1 可按两大类组织：

- Fish / Species / Affinity objects；
- Template objects，并按 Component Type 分组。

DSL 不作为 Phase 1 左栏主导航对象。

Template referencers / affected objects 放在中栏 Context 下部，而不是把引用关系树塞进主导航。

### 20.22 Production drift 与 save conflict 必须区分 UI 文案

至少区分：

**保存冲突**

```text
当前 Editor State revision 已被外部修改
→ reload / compare
```

**Production drift**

```text
Production config 与当前 editor projection 不一致
→ P0 read-only diagnostic
```

不能把二者都显示成“保存失败”。

### 20.23 Temperature / TimePeriod / Template acceptance variants

除 Structure 13 个 variants 外，Phase 1 至少保留以下验收状态。

**Temperature**

1. Shared Template Source；
2. SpeciesConcrete Source；
3. Affinity inherited；
4. Affinity explicit Source Override；
5. numericRelative ADD / SET；
6. enumAbsolute SET；
7. cross-field ERROR / Invalid Curve；
8. CORE threshold active；
9. non-CORE threshold inactive-but-preserved；
10. Concrete Reimport Preview。

**Time Period**

1. legal IGNORED + Profile absent；
2. CORE + Profile absent ERROR；
3. Source selected / zero local ops；
4. Preset Batch Preview；
5. 5 SET after preset；
6. IGNORED-but-configured；
7. Profile error while IGNORED；
8. Source Change with all SET values masked。

**Template Workspace**

1. ACTIVE clean；
2. ACTIVE with staged candidate edits；
3. Template Value Impact Preview；
4. Replace References Impact Preview；
5. ARCHIVED read-only；
6. Restore；
7. Hard Delete blocked by direct refs；
8. Extract Template without automatic rebind。

### 20.24 No hidden coupling rules

Phase 1 不允许以下 silent coupling：

- Source Change → 自动改 Role；
- Role Change → 自动换 Source；
- Role IGNORED → 自动删 Profile；
- Template Reimport / Concrete Reimport → 自动切 Recipe Source；
- Preset Apply → 自动创建长期 preset identity；
- equal value → 自动转 inherit；
- same source → 自动删除 sourceOverride；
- Profile payload equality → 自动合并 authoring owners；
- Archived Source → 自动 fallback；
- Broken Source → 自动 fallback。

所有 topology / intent 变化都必须来自明确 authoring action。

### 20.25 Complete negative knowledge summary

Phase 1 追求的是“最低总复杂度”，不是视觉控件数量最少。以下复杂度迁移也视为失败：

- 为了少一个 Source 类型，给所有 Component 强行加入 Concrete；
- 为了统一字段编辑器，让 enum 支持伪 ADD；
- 为了统一 Card，把 Policy 做成第五个 Component；
- 为了减少 ERROR state，偷偷 clamp / sort / repair；
- 为了减少 Profile 数量，按 payload hash 全局 dedup；
- 为了让空态整齐，把全部 Component 都做 optional；
- 为了看起来省操作，把 Source change、Role change、Operation change 合成一个隐式 mutation。



## 21. Phase 1 Freeze Boundary

下一步：Current delta review → classify UI-only vs schema/current changes → Freeze Contract → Figma Structure vertical slice → Code Structure vertical slice。
本文件仍是 Working Baseline，不得直接作为 Figma / Implementation 最终 Authority。