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

## 19. Phase 1 Freeze Boundary

下一步：Current delta review → classify UI-only vs schema/current changes → Freeze Contract → Figma Structure vertical slice → Code Structure vertical slice。
本文件仍是 Working Baseline，不得直接作为 Figma / Implementation 最终 Authority。