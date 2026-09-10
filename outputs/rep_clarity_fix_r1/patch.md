# REP-CLARITY-FIX-001｜Stress Test R1 主页 F1–F8 清晰度修复补丁（Notion 转写指令稿）

`Status：WORKING / REPRESENTATION PATCH DRAFT / NOT AUTHORITY / NOT PROMOTED`

本文件是给 Coordinator 转写 Notion 用的**补丁指令集**，不是已应用的变更记录。落笔时目标页面未被本角色读取（见 §0 基线声明）。

---

## 0. 转写须知（先读）

| 项 | 内容 |
|---|---|
| 目标页面 | Stress Test R1 主页：`https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3`（下称「主页」） |
| 裁决指向页 | Summer Oxythermal Stress Representation Knife R0 子页：`https://app.notion.com/p/3d6a4137d23681d0a3a5ddbf7e352b50`（下称「Knife 子页」；Notion 内请用 mention-page 链接） |
| 输入来源 | (1) 审计 REP-CLARITY-AUDIT-001（**落点定位权威**，verdict ARTIFACT_REVISE，F1–F8）；(2) KNIFE-READ-001（Knife 子页 2026-09-10T03:49:56Z 归档版全文转述——§16.7 收敛结构 / §16.8 压缩轨迹 / §16.5 判据 / §15.5 Expression Gate / §8 / §14）；(3) `outputs/usable_forage_contract_r0/README.md`（F2 三个 Eligibility 输入的措辞样板，审计认定为全集群最佳页）；(4) `outputs/fcf_authoring_concrete_r2/baseline_stress.md`（主页 2026-09-09T10:26:32Z 过时快照，仅作锚文本） |
| 基线声明 | **部分 SNAPSHOT_ONLY**：主页在该快照之后被编辑过（快照后 ≥6.4h 有编辑，且 Knife 子页 09-10 拆出后主页继续演化）。本角色无 Notion 工具，未 fetch live。快照只覆盖主页前半；审计引用的 §12–§17、BA-T 系列本地**无原文**，只能按审计描述定位 |
| 设计权威边界 | 本补丁只做**表达清晰度修复**。F1 回写方向按 Knife R0 §16.7 既有裁决转述（lookup2d(Temp,DO) + Cover/Forage/Visual 三 Unary + FIXED_COMBINE；MAX(Cover,Prey) 不冻结；B-T2 NOT CONFIRMED），**不重新裁决**；FIXED_COMBINE 数学公式维持不冻结；未定义算子一律显式标 `OPERATOR UNDEFINED — 待机制侧`，不擅自补数学 |

### 0.1 通用转写规则

1. **只插入，不删除、不改写任何既有原文**（标题、表格、伪脚本代码块内部均不动；表格不加行不加列，标注一律以表下 / 代码块后的独立段落插入）。
2. 每段插入内容**必须原样保留 provenance 行 / 尾标**：`[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]`。
3. **锚点级别**两种，均须对 live 核对：
   - `[锚·快照]`：锚文本引自主页 2026-09-09T10:26:32Z 过时快照，live 原文可能有措辞漂移；
   - `[锚·审计]`：位置仅来自审计描述，本批输入内无原文，按审计描述在 live 定位。
4. **落点核对失败即跳过**：live 与本补丁定位不符（找不到唯一位置，或该处已有等价标注 / 已被修复）→ 不插、不就近强插，在转写回执中逐条报告。
5. 主页与 Knife 子页**各有一套 §13–§16 编号**。本补丁所有落点均指主页；所有「见 §16.7 / §16.8 / §14 / §8」均指 **Knife 子页**节号（已逐处写明「Knife 子页」）。
6. 审计修复优先级（本补丁节序照此排列）：F1 → F4 → F2 → F3 → F5 → F6；F7/F8 不修。

---

## 1. F1（BLOCKER）｜三处 SUPERSEDED 回写

格式照主页 §5.5 既有先例（`[SUPERSEDED]` 标记 + 引用块说明替代关系 + 「保留旧判断仅用于追溯」）。本补丁采用**最小侵入形态**：不改标题、不删原文，把标注块插在标题后正文前（或表前），保证读者先看到 superseded 状态。若转写者判断需与 §5.5 完全同形（标题前缀 `[SUPERSEDED]`），可另行加标题前缀，两法都不删原文——二选一即可，不要叠加两块。

### F1-a｜主页 §15.5 的 M3 表（五 Unary + RefugeCombine=MAX，无标注）`[锚·审计]`

**原内容定位描述**：主页 §15.5 内编号为 M3 的里程碑表，含五个 Unary Profile 输入与 `RefugeCombine=MAX` 合并行，全表无任何降级 / SUPERSEDED 标注（审计 F1 点名的三处版本漂移之一）。

**插入位置**：M3 表**正上方**（表格之前、其引导文字之后），作为独立引用块。

**插入原文（原样转写，含 provenance）**：

```text
> [SUPERSEDED] 本表「五 Unary + RefugeCombine=MAX」结构已被 Summer Oxythermal Stress Representation Knife R0 子页 §16.7（https://app.notion.com/p/3d6a4137d23681d0a3a5ddbf7e352b50 ）的收敛结论替代；原文保留仅用于追溯，不代表当前 Working Direction。现行为：lookup2d(Temp, DO) 二维交互 + Cover / Forage / Visual 三个独立 Unary + FIXED_COMBINE 固定合并（数学公式不冻结），MAX(Cover, Prey) 不再冻结为合并算子（AlternativeSupportSlot 已从最小结构删除，Knife 子页 §15.7）。
> [REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：live 主页 §15.5（注意与 Knife 子页 §15.5「Expression Gate」区分——那是另一个页面的另一节）内，找**唯一**含 `RefugeCombine=MAX` 的 M3 编号表；若该表已带 SUPERSEDED / 降级标注则跳过回报。三处 F1 中只处理本表这一处，§15.5 其余文字不动。

### F1-b｜主页 §BA-T4 节（Gate + MIN + MAX + 嵌套 + Final Combine 原句型）`[锚·审计]`

**原内容定位描述**：主页以「BA-T4」开头的节（Bake Authoring 压力测试系列），正文承载原压力句型：`Gate` + `MIN` + `MAX` + 嵌套中间结果 + `Final Combine` 的结构能力组合（Knife 子页 §1 引用的正是它）。该节现仍以「最强 Structured Trade-off 反例」地位裸呈现，无 SUPERSEDED 标注。

**插入位置**：BA-T4 节标题行之后、正文第一段之前，作为独立引用块。

**插入原文**：

```text
> [SUPERSEDED] 本节 BA-T4 压力句型（Gate + MIN + MAX + 嵌套中间结果 + Final Combine）作为「最强 Structured Trade-off 反例」的定位已被 Summer Oxythermal Stress Representation Knife R0 子页（https://app.notion.com/p/3d6a4137d23681d0a3a5ddbf7e352b50 ）§16.8 的逐轮压缩取代；原文保留仅用于追溯。现行为：该句型已收敛为 lookup2d(Temp, DO) + Cover / Forage / Visual 三 Unary + FIXED_COMBINE（Knife 子页 §16.7），SummerStress 不再需要专用 Structured Trade-off Template（B-T2 NOT CONFIRMED，Knife 子页 §8），本句型降级为 Generic Typed 2D Interaction Profile 的最强正样本（Knife 子页 §14）。
> [REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：live 主页搜索标题前缀「BA-T4」，应唯一命中一节；节内应含 Gate / MIN / MAX / 嵌套中间结果 / Final Combine 字样。若 live 该节已自带最新裁决引用则跳过回报。

### F1-c｜主页 §13.2 的 B-T2 条目（MIN / MAX / × 形态）`[锚·审计]`

**原内容定位描述**：主页 §13.2 中 B-T2（Structured Trade-off Template 候选）条目，以 `MIN` / `MAX` / `×`（乘积）组合形态描述，无 NOT CONFIRMED / SUPERSEDED 标注。

**插入位置**：§13.2 内 B-T2 条目标题（或首行）之后、该条目正文之前，作为独立引用块。

**插入原文**：

```text
> [SUPERSEDED] 本条目 B-T2（Structured Trade-off Template｜MIN / MAX / × 组合形态）为 NOT CONFIRMED：Summer Oxythermal Stress Representation Knife R0 子页（https://app.notion.com/p/3d6a4137d23681d0a3a5ddbf7e352b50 ）§8 暂不确认该模板，§16.8 压缩后它不再是最小表达；原文保留仅用于追溯。现行为：B-T1 Independent Factor Set + Generic Typed 2D Interaction Profile（lookup2d(Temp, DO)）+ FIXED_COMBINE（Knife 子页 §16.7）。
> [REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：live 主页 §13.2 内 B-T2 条目应唯一；若该条目已标 NOT CONFIRMED 且引用 Knife 子页则跳过回报。**只标 B-T2**；同节 B-T1 / B-T3 等其它条目不动（B-T3 是算子标注格式先例，勿覆盖）。

---

## 2. F4｜合并算子回填（审计点名约 10 处占位；本补丁给出 12 个可定位落点 + 扫尾规则）

原则：**能定的给算子并标 `Working Algorithm Candidate`**（标签格式照主页既有先例「`MAX` Working Candidate」与 BA-T3；若 BA-T3 原文措辞不同，以 BA-T3 为准）；**不能定的显式标 `OPERATOR UNDEFINED — 待机制侧`，不许静默留占位**。每处标注 = 表下 / 代码块后一段独立文字（伪脚本代码块内部不插入）。

### 2.1 可定算子｜SummerStress 系占位 → FIXED_COMBINE（2 处）

依据：Knife 子页 §16.7 裁决（转述自 KNIFE-READ-001）——最小结构 = `lookup2d(Temp, DO)` + Cover / Forage / Visual 三 Unary + FIXED_COMBINE；§16.7 明示 **FIXED_COMBINE 具体数学公式不冻结**，冻结的只有表达边界（Fit 并列输入、作者不得建立中间依赖）。

**落点 F4-1**：主页「Summer Oxythermal Stress｜盛夏氧热夹压模式」节（§6.3 小节，快照序）Bake 伪脚本，含行「按 SummerStress Bake Template 的固定规则合并」。`[锚·快照]`

**落点 F4-2**：主页「Bass 5-Group Representation Projection R0」§6.2 中文逻辑投影的 Summer Oxythermal Stress 代码块，含行「按 SummerStress 固定 trade-off 规则合并」。`[锚·快照]`

两处插入原文（相同）：

```text
算子标注：FIXED_COMBINE（Working Algorithm Candidate）——并列输入固定合并，具体数学公式不冻结（Knife 子页 §16.7 只冻结边界：Fit 并列输入、作者不得建立中间依赖）。最小结构 = lookup2d(Temp, DO) + Cover / Forage / Visual 三个 Unary；本块伪脚本的多中间量写法为历史形态，最小结构以 Knife 子页 §16.7 为准。
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：F4-1 = live 主页唯一含「按 SummerStress Bake Template 的固定规则合并」的代码块（其后紧跟「返回 当前约束下的相对 refuge score」）；F4-2 = 唯一含「按 SummerStress 固定 trade-off 规则合并」的代码块（其后紧跟「返回 SpatialDistributionWeight」，且同块上文有 @CoolingBenefitProfile / @DOSafetyProfile）。两处锚文本若漂移，按语义找 SummerStress 的两个 Bake 伪脚本。

### 2.2 可定算子｜BLEND / BLEND_BY_SEVERITY（3 处，数学定义草案，Candidate）

审计点名 3 处；本批输入可唯一定位其中 2 处（§7.2 表 + §7.3 脚本），第 3 处由扫尾规则定位（live 全页搜索「BLEND」应得 3 个算子使用点）。

**落点 F4-3**：主页「Cold Front Spatial Overlay」§7.2 固定模板槽位表，行 `Overlay Blend｜BLEND_BY_SEVERITY`。`[锚·快照]`
**落点 F4-4**：§7.3 中文脚本，含行「按照锋后强度 / 把 BaseSpatialFit 向 PostFrontRefugeFit 偏移」。`[锚·快照]`
**落点 F4-5**：live 其余 BLEND / BLEND_BY_SEVERITY 使用点（审计计数为第 3 处）。`[锚·审计]`

**插入原文（数学定义草案，三处共用同一份定义，可只在 F4-3 放全文、另两处放一行指针「BLEND_BY_SEVERITY 数学定义见 §7.2 表下标注」）**：

```text
算子标注：BLEND_BY_SEVERITY（Working Algorithm Candidate｜数值未冻结）——
  s = clamp01( lookup(PostFrontSeverity, @OverlayBlendWeightProfile) )
      // 未绑定 Blend Profile 时退化为 s = clamp01(PostFrontSeverity)
  FinalSpatialFit = (1 − s) · BaseSpatialFit + s · PostFrontRefugeFit
边界情形：s = 0 → 恒等返回 BaseSpatialFit（对应脚本「锋后强度很低 → 返回 BaseSpatialFit」）；s = 1 → 完全取 refuge 分布。
本定义只覆盖「Base → 单一 refuge 目标」的线性混合，不引入作者可编辑的混合拓扑；PostFrontRefugeFit = MAX(CoverRefugeFit, DepthRetreatFit) 沿用本节表内既定 MAX（两条 refuge 按替代通路处理，Working Candidate）。数学草案为表达层候选，机制侧后续裁决可推翻。
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：F4-3 表的唯一特征 = 行值 `BLEND_BY_SEVERITY` 且同表有 `Refuge Combine｜MAX` 行；F4-4 块的唯一特征 = 含「PostFrontRefugeFit = MAX(CoverRefugeFit, DepthRetreatFit)」；F4-5 按 live 搜索「BLEND」第 3 个使用点（§7.4 里「固定 Combine / Blend」的泛提不算使用点）。

### 2.3 引用型｜Quality 合并 → 指向 §12（1 处）

**落点 F4-6**：主页「Bass 5-Group Representation Projection R0」§6.4 的统一求值语义 Candidate 代码块（含行「合并 Modifier / 统一归一化」）。`[锚·快照]`

**插入原文**：

```text
算子标注：本块「合并 Modifier / 统一归一化」的品质算子语义以主页 §12（12.3 / 12.4）为准，本节写法为历史投影；若 §12.3 / 12.4 未覆盖「并列 Modifier 合并 + 单次归一化」的数学定义，则此处即 OPERATOR UNDEFINED — 待机制侧，不得当作已闭合引用。
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：live 唯一含「合并 Modifier」与「统一归一化」相邻两行的代码块（同块上文有「每条 Rule 只读取原始输入事实」）。转写时先读 live §12.3/12.4 确认覆盖与否，据实保留或改写条件句的后半句（只允许在「已定义→指向 §12」与「未定义→OPERATOR UNDEFINED」两态中选择，不许第三种措辞）。

### 2.4 OPERATOR UNDEFINED 清单（6 处）

统一格式（`<…>` 为逐处替换内容）：

```text
算子标注：OPERATOR UNDEFINED — 待机制侧（<缺口说明>）。「<原占位短语>」在本页是占位声明，不是已冻结算子。
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

| # | 落点 | 锚 | 占位短语 | 缺口说明（填入 `<缺口说明>`） |
|---|---|---|---|---|
| F4-7 | 例 3 A 配置表（双通道摄食评价）表下 | `[锚·快照]` | 汇总规则=「固定汇总」（刮食 / 悬浮颗粒摄食两行） | 同一摄食 evaluator 内双 Feeding Channel 的汇总算子未闭合；C08 的决定是「不购买 Selector」，不等于汇总数学已定 |
| F4-8 | 例 3 B 中文脚本块后 | `[锚·快照]` | 「按模板固定规则合并两个 Channel」 | 同 F4-7（同一占位的脚本侧） |
| F4-9 | 例 2 B 中文脚本块后 | `[锚·快照]` | 「合并结果」 | LT-S1 空间顺序因素模板（水层 → 结构 → 温度）的合并算子；C01 / C02 / C05 的 Runtime Order 未冻结 |
| F4-10 | Bass 5-Group 投影 §6.2 NormalFeeding 代码块后 | `[锚·快照]` | 「按照 Normal Bake 的固定合并规则」 | BA-NORMAL-HABITAT 语义程序候选的多 Factor 合并算子；BA-* 目前只是候选签名，不是已确认模板 |
| F4-11 | 同 §6.2 Guarding 代码块后 | `[锚·快照]` | 「按 Guarding Bake 固定规则合并」 | BA-GUARD-NEST 在 Nest Eligibility 之后的 Fit 合并算子 |
| F4-12 | 同 §6.2 Cold-Slow 与 ForageChase 两个代码块后（各一段，共 2 处；与上合计 6 段） | `[锚·快照]` | 「按 Cold-Slow 固定 refuge 规则合并」；「按 Forage-Chase 固定规则合并」 | BA-COLD-RELATIVE-REFUGE 的 refuge Fit 合并算子；BA-FORAGE-COUPLED 的 forage 锚定 Fit 合并算子 |

**落点核对提示**：六段各自锚文本在上表「占位短语」列，均为 live 主页唯一短语（快照序）；若 live 措辞漂移，按语义定位——例 3 双通道表 / 例 2 三因子脚本 / Bass 投影 §6.2 的 Normal / Guarding / Cold-Slow / ForageChase 四段 Bake 脚本。Note：F4-10～F4-12 的 SummerStress 块已由 F4-2 覆盖（FIXED_COMBINE），不要重复标注。

### 2.5 扫尾规则（必执行）

转写时在 live 主页全文搜索占位词干：`固定规则合并`、`固定合并规则`、`固定汇总`、`Template 的固定规则`、`固定 trade-off 规则`、`固定 refuge 规则`、`合并 Modifier`、`BLEND`。凡命中且**不在 F4-1～F4-12 清单内**的算子使用点，按同一模式处理：

- SummerStress / 氧热夹压相关 → 用 §2.1 的 FIXED_COMBINE 标注；
- BLEND / BLEND_BY_SEVERITY → 用 §2.2 的数学草案标注（或一行指针指向全文所在处）；
- 其余 → 用 §2.4 的 OPERATOR UNDEFINED 模板，缺口说明按该处语义一句写明；
- 拿不准归属的，一律 OPERATOR UNDEFINED — 待机制侧（宁显式未定义，不冒充已定义）。

审计计数「约 10 处」与本清单 12 处的出入，以 live 实测为准，逐处回执。

---

## 3. F2｜输入来源补齐

### 3.1 主页 §15.1B 伪脚本补 3 个 Eligibility 输入行 `[锚·审计]`

**原内容定位描述**：主页 §15.1B 的 Bake 伪脚本（Forage 输入侧），读取步骤组缺 3 个 Eligibility 输入声明（审计 F2 点名：共缺 3 行）。

**插入位置**：该伪脚本代码块内既有「读取 …」步骤组的末尾（最后一个既有「读取」行之后、第一个计算 / 评价 / 查询步骤之前），插入以下三行（这是本补丁唯一允许向代码块内部插入的位置——因为缺的正是脚本步骤本身）：

**插入原文（逐行，原样转写）**：

```text
读取 当前种群的猎物场绑定表（prey_fields｜只读同一份 Resolved Snapshot 的原始 prey 事实，未经感知 / 可见性 / 捕获 / 口径修正）
读取 当前种群的食性资格（diet_classes｜该种群食谱覆盖哪些 prey class；允许空集 = 零重叠显式表达）
读取 当前种群的口径资格（size_window_mm｜min / max 口径窗 × 各 prey class 代表尺寸）
```

代码块之后紧跟一行（块外）：

```text
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001｜Eligibility 三输入措辞照 UsableForageAvailability 契约 R1（全集群达标样板）]
```

**落点核对提示**：15.1B = live 主页 §15.1 内 B 编号伪脚本、且其「读取」步骤不含 prey / diet / size 三类 Eligibility 行（audit 点名的唯一缺失处）。若 live 该脚本已有部分 Eligibility 声明，只补缺失项（总数对齐 3 行）。

### 3.2 主页 §15.1 的 M5 / M7 两处补 Base 来源句 `[锚·审计]`

**原内容定位描述**：§15.1 里程碑 M5 与 M7 各使用一个 Base 值但未写来源句（审计 F2 点名，要求照 BA-T6 措辞补全）。

**诚实声明**：BA-T6 原句不在本批输入内（live 主页 §12–§17 与 BA-T 系列本地无档）。以下给出两种语义句式，**转写时按 M5 / M7 各自语境选用**；若 BA-T6 原句可得，以其措辞为准替换（语义不得变）：

- 句式 A（该处 Base 指 Fit 的输入事实）：

```text
Base 输入来源 = 同一份 Resolved Snapshot 的原始 ⟨事实族⟩ 事实（@⟨绑定⟩）；不读任何其它 Factor 的输出。
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

- 句式 B（该处 Base 指上游程序的既有结果，如 BaseSpatialFit / 基础品质分布）：

```text
Base 来源 = ⟨上游程序名⟩ 的求值结果（同一份 Resolved Snapshot 输入下的既有输出）；本步不重新求值、不读其它 Factor 输出。
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**插入位置**：M5、M7 条目内 Base 值首次出现行的紧后（条目内一行）。`⟨…⟩` 由转写者按 live 原文填实。

**落点核对提示**：M5 / M7 = live 主页 §15.1 内编号 M5、M7 的两个条目（audit F2/F5 双点名，M7 另见 §5.3）。两句式均不改写既有文字，只补来源行。

---

## 4. F3｜schema 变体声明（Grammar 5.1 附近）+ G3 ConditionGroup 一行定义

按审计处置：**不强行统一既有表**（侵入过大），用显式声明消歧。

### 4.1 「本页允许的列结构变体」声明块 `[锚·快照]`

**插入位置**：Grammar 5.1（「条件原子」小节）「推荐字段」代码块之后、「### 5.2 条件组 / RuleSet」标题之前。快照锚：推荐字段块末行为「比较值 3」。

**插入原文（原样转写）**：

```text
本页允许的列结构变体（显式声明）：Grammar 5.1 的推荐字段是超集推荐，不逐表强制；但每张条件 / 品质 / 规则集表必须能对上下列某个变体，后续新表要么复用已声明变体，要么先扩充本声明再上新列结构——列结构未对上任何变体的表视为表达漂移（审计 F3）。

条件原子（4 种）
- V1 双值全列：条件组 / 条件 / 事实·计算项 / 参数1 / 比较符 / 比较值1 / 比较值2——适用：需被 RuleSet 以 Condition 逐条引用、且使用双比较值（BETWEEN / CONTAINS_ANY）。既有实例：例 1、G1、G3。
- V2 单值形态：条件组 / 条件 / 事实·计算项 / 参数 / 比较符 / 比较值——适用：被 RuleSet 引用，单参数、单比较值。既有实例：G2。
- V3 无参数形态：条件组 / 条件 / 事实·计算项 / 比较符 / 比较值——适用：被简单 RuleSet 引用、无参数列。既有实例：Q1。
- V4 无编号形态：条件 / 事实·计算项 / 比较符 / 比较值——适用：单条件直接被品质规则引用、无 RuleSet 中间层。既有实例：Q2。

品质表（3 种）
- W1 调整结果形态：命中条件 / 调整对象 / 调整方式 / 参数——适用：命中条件直接引用同节条件编号。既有实例：例 4。
- W2 品质规则形态：品质规则 / 命中条件 / 调整对象 / 调整方式 / 参数——适用：带规则名列，命中条件引用 RuleSet / 条件。既有实例：Q1、Q2。
- W3 内联条件形态：规则集 / 条件 / 调整对象 / 调整方式 / 参数——适用：条件以文字表达式内联、无独立 RuleSet 层。既有实例：Q3。

规则集（2 种）
- R1 全列形态：规则集 / 组合方式 / 显示顺序 / 引用类型 / 引用——适用：需显式引用类型（Condition / ConditionGroup / RuleSet）与显示顺序。既有实例：例 1、G1、G3。
- R2 紧凑形态：规则集 / 组合方式 / 引用——适用：单一组合方式、引用列内以逗号并列多条。既有实例：G2、Q1（BigGear）。

[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：live 主页 Grammar 5.1 的「推荐字段」清单若仍以「比较值 3」收尾即锚定成功；若 live 已改 Grammar，则插在 5.1 小节末尾（5.2 标题前）不动其它。声明中既有实例的对应关系按快照表核对（快照内四张条件原子表 / 三张品质表 / 两张规则集表形态与上列一致）；live 若新增了第 5 种条件原子列结构，把它补进声明后再收尾（这是声明义务，不是统一义务）。

### 4.2 G3 规则集表的 ConditionGroup 一行定义 `[锚·快照]`

**原内容定位描述**：G3（复杂分群）的规则集表用了引用类型 `ConditionGroup`（引用 SpringPath / FallPath），但全页无该类型定义（审计 F3 点名）。

**插入位置**：G3 规则集表（含行 `R_Spring｜AND｜1｜ConditionGroup｜SpringPath`）正下方，一行。

**插入原文**：

```text
引用类型说明：Condition = 单条条件原子；ConditionGroup（条件组）= 同名分组的条件原子集合，组内按 AND 连接求值、作为一个整体被 RuleSet 引用（本 Case 中文逻辑的「（春季 AND 适温 AND 草区）OR（秋季 AND 降温 AND 深坑）」即 R_Spring / R_Fall 两个 ConditionGroup 的 OR）；RuleSet = 规则集整体。［REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001］
```

**落点核对提示**：live 主页唯一以 `ConditionGroup` 为引用类型值的表 = G3 规则集表（快照序：规则集 / 组合方式 / 显示顺序 / 引用类型 / 引用 五列）。定义从该页自身中文逻辑归纳（组内 AND 有页内证据），不引入新机制。

---

## 5. F5｜取值域定义

### 5.1 「启用」列取值域（§7.2 实例绑定示意表后）`[锚·快照]`

**原内容定位描述**：主页 Cold Front Spatial Overlay §7.2「实例绑定示意」表的「启用」列出现 `ON`、`LOW / OFF candidate`、`OFF / LOW candidate`、`OPEN`、`ON candidate`，取值域无定义（审计 F5）。

**插入位置**：该表正下方，一段。

**插入原文**：

```text
「启用」列取值域：ON = 该 Group 绑定本 Overlay 且进入求值；OFF = 不启用（该 Group 的 Base 结果不经本 Overlay 修正）；LOW = 启用但弱修正档（强度数值由 Overlay 参数 / Profile 承载，本列不承载数值语义）；OPEN = 未裁决（启用与否待后续证据，本页不默认方向）；candidate（后缀）= 该取值本身是候选而非 Working Decision（如「ON candidate」= 倾向启用、未裁决）；斜杠并列（如「LOW / OFF candidate」）= 并列候选之间尚未裁决，整串为单一未决状态，不是多值同时生效。
[REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001]
```

**落点核对提示**：live 主页唯一含「启用」列且取值混有 OPEN / candidate 的表 = §7.2 实例绑定示意表（快照序：FishGroup / 启用 / Overlay Ref / 备注 四列，行含 @BassPostFrontRefuge）。若 live 其它绑定表（如 §17.3）也有「启用」列，本定义块仍只插 §7.2 表下，其余表用 5.2 的一行指针。

### 5.2 §17.3 绑定表斜杠并列取值一行 `[锚·审计]`

**插入位置**：主页 §17.3 绑定表（审计认定的达标样板节）正下方，一行。

**插入原文**：

```text
取值说明：本表斜杠并列取值 = 并列候选之间尚未裁决（单一状态，非多值同时生效）；各取值含义见 §7.2「启用」列取值域说明。［REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001］
```

**落点核对提示**：live §17.3 为审计点名的绑定表；只加这一行，不动该节其它内容（审计已认定 §17.3 达标，勿顺手改写）。

### 5.3 §15.1 M7 裸 threshold 一行 `[锚·审计]`

**原内容定位描述**：主页 §15.1 里程碑 M7 使用裸 threshold 值，无取值域 / 单位 / 冻结状态说明（审计 F5）。

**插入位置**：M7 条目内 threshold 值所在行紧后，一行。

**插入原文（`⟨…⟩` 按 live 原值填实）**：

```text
取值说明：M7 本行 threshold（⟨原值⟩）为示例占位值，未冻结；取值域与单位随其绑定的事实项（⟨事实项名⟩），比较语义按 Grammar 5.1 条件原子字段解释。［REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001］
```

**落点核对提示**：M7 = §15.1 内编号 M7 条目（与 §3.2 的 Base 来源句同条目、不同行——两句各自独立插入，不合并）。

---

## 6. F6｜旧节品质算子指针（例 4 / Q1 / Q2 / Q3，各一行）

统一插入文本（四处在「调整对象 / 调整方式」语义首次成表的地方各插一行）：

```text
本节品质调整（上调 / 下调相对权重）的算子语义见 §12（12.3 / 12.4）；本节写法为历史形态。［REP-CLARITY-FIX-001｜2026-09-10｜审计 REP-CLARITY-AUDIT-001］
```

| # | 落点 | 锚 | 插入位置（唯一性特征） |
|---|---|---|---|
| F6-1 | 例 4（抽中 FishGroup 以后再决定品质） | `[锚·快照]` | 「品质调整结果」表正下方——该表四列（命中条件 / 调整对象 / 调整方式 / 参数），行值「Q1 AND Q2」「Q3」，参数 @BigGearBoost / @AdultInactivePenalty |
| F6-2 | Q1（大钩 + 大饵） | `[锚·快照]` | 品质规则表（Q_BigGear 行）正下方——五列含「品质规则」列，行值 Q_BigGear / @BigGear |
| F6-3 | Q2（成年低活性时段） | `[锚·快照]` | 品质规则表（Q_AdultInactive / Q_AdultInactive_Small 两行）正下方——行值 @AdultInactivePenalty / @JuvenileRelativeBoost |
| F6-4 | Q3（复合条件） | `[锚·快照]` | 规则集表（R_BigGear / R_ColdNightAdult 两行）正下方——条件列内联文字「大钩 AND 大饵」「夜间 AND 低温」 |

**落点核对提示**：四张表在快照内互不重名、行值各异（见上表）；live 若已给某表加过指针则该处跳过。注意「§12」指主页 §12（品质算子语义的家，审计达标样板），不是 Knife 子页编号。

---

## 7. F7 / F8｜不修，后续建议（仅记录，本批零改动）

审计裁定 F7（局部展开粒度低于 Authoring Projection Protocol 自设标准）与 F8（页内两套 §5–§8 重复编号放大漂移）侵入过大、本批不动。后续建议两条：

1. **F7**：后续单独一批，为 Bass 投影 §6.2 五个 Bake 程序的中间量（RelativeWarmth、溶氧安全余量、ForageSchoolIntensity 等）按 Authoring Projection Protocol R0（`https://app.notion.com/p/3d6a4137d23681799bf0e688169c049d`）补齐展开粒度；不要与本批语义修补混批。
2. **F8**：下一个结构整理 Pass 统一重编号（页内现存两套 §5–§8 系列），重编号时**同步更新本补丁新增的全部指针**（§5.1、§7.2、§12、§12.3/12.4 引用），并全页校验交叉引用；重编号批次不得夹带任何语义修改。

---

## 8. 本批表达工件登记

| 项 | 内容 |
|---|---|
| BATCH_ID | REP-CLARITY-FIX-001 |
| 执行面 | 文档层补丁（对象 = 主页表达）；条目分布：F1 / F4 主要 Bake，F2 Bake，F3 跨面 Grammar，F5 Overlay 绑定 + Bake，F6 Quality |
| 使用的自由度 | SUPERSEDED 标注块与「现行为」摘要句措辞（对齐 Knife §16.7/§16.8/§8/§14 转述）；算子标注行格式（照页内「`MAX` Working Candidate」/ BA-T3 先例）；变体命名 V/W/R 系；取值域条目措辞；BLEND_BY_SEVERITY 线性混合数学草案形状（Coordinator 授权的 Candidate 草案，机制侧可推翻）；Eligibility 三输入措辞照 forage 契约 R1 样板 |
| 放弃的自由度 | 不改机制结论（FIXED_COMBINE 公式维持不冻结；B-T2 维持 NOT CONFIRMED；未定义算子不擅自给数学）；不统一既有表列结构（以变体声明代替）；不重编号（F8 留后续批）；不删除任何原文；不 fetch / 不写 Notion；M5 / M7 来源句措辞让位 BA-T6 原句（如可得） |
| 边界声明 | 表达清晰度修复 ≠ 机制 promotion ≠ Freeze；本补丁应用与否、顺序与分批由 Coordinator 决定；F1「现行为」句为 Knife 既有裁决的转述对齐，非本批新裁决；BLEND 数学草案与 §12 条件句均为 Candidate / 双态模板，机制侧后续裁决优先 |
| 转写回执要求 | 逐处回报：插入成功 / 跳过（原因：定位不符 / 已有标注 / 锚点漂移）；F4 扫尾的 live 实测处数；§2.3 条件句最终取态（指向 §12 还是 OPERATOR UNDEFINED）；M5/M7 选用的句式与 BA-T6 原句（若读到） |

BATCH_ID: REP-CLARITY-FIX-001
