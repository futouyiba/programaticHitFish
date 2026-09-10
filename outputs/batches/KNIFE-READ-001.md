# BATCH｜KNIFE-READ-001

- 保存说明：agent 报告逐字归档（agent 无写工具；由 Coordinator 保存，内容未改写）。
- 归档时间：2026-09-10
- 角色：fcf-fish-researcher（命名角色，正式运行）
- 状态位：FR0 RESEARCH_RUNNING

---

工具清点确认：本执行环境未挂载 Write/Edit 工具，角色记忆的增量写回无法在本批物理落盘。我不伪造写入状态——待写回内容以「记忆增量提案」形式附在报告末尾，由有写权限的代次或 Coordinator 决定持久化。以下为研究记录正文。

# 研究记录｜Summer Oxythermal Stress Representation Knife R0（KNIFE-READ-001）

## 0. 读取元数据与传输检查

| 项 | 值 | 置信度 |
|---|---|---|
| 页面 URL | https://app.notion.com/p/3d6a4137d23681d0a3a5ddbf7e352b50 | — |
| 标题 | Summer Oxythermal Stress Representation Knife R0｜2D Profile vs Structured Trade-off vs Narrow Expression | 文献支持（live 读取） |
| 页顶状态标签（原样） | `Status：WORKING / REPRESENTATION KNIFE / NOT AUTHORITY / NOT PROMOTED` | 文献支持 |
| §15、§16 各自页首状态（原样） | `Status：WORKING DELTA / NOT AUTHORITY / NOT PROMOTED` | 文献支持 |
| page_last_edited_at | 2026-09-10T03:49:56.533Z | 文献支持 |
| Notion verification | unverified | 文献支持 |
| 传输状态 | 完整（§0–§16.8，末尾 Readout 代码块闭合，无截断迹象） | 文献支持 |

漂移注记：我的角色记忆中 TEST-FR-001（约 03:24Z 核验）记录的 page_last_edited_at 为 2026-09-10T02:57:49Z；本次为 03:49:56Z，页面在过去约 52 分钟内被编辑过。**本记录代表 03:49:56Z 版本；后续引用须重对 live。**（前半为文献支持，52 分钟间隔内的编辑动作本身为推断）

与 Coordinator 预期的一个偏差：标题与 Handoff 所述为三方案对比，但页面实际比较**四**方案（§7 比较表含 Option D｜All-in Resolver）。按页面实际内容报告。

页面层级：Start Here / Agent Router → Design Branch Index → Simplified V0 Working Main → 中鱼机制 0.3.4 → **4 Logic Surface Authoring Stress Test R1**（父页）→ 本页。与记忆中拓扑捷径一致（文献支持）。

## 1. 这把刀攻击的问题陈述

页面开篇原话（§ 引言）：

> 本页只攻击一个问题：`Summer Oxythermal Stress` 这种 Temperature × DO × Refuge / Prey trade-off，是否真的需要新的 Bake DSL / Expression Tree，还是可以继续留在声明式 Config 主路径。

对 Bake/表达结构提出的具体压力（§1，文献支持，以下为页面自述）：

- 压力来源是原 BA-T4 压力测试句型的结构能力组合：`Gate` + `MIN` + `MAX` + 嵌套中间结果 + `Final Combine`。这个组合是「Structured Trade-off」的最强候选反例。
- 生态侧压力（页面转述，**无外部文献引文，未证实档**）：高温提高氧需求；严重低氧构成明显空间压力/avoidance；Temperature 与 DO 存在交互；Bass 可能因 prey/refuge/site-specific trade-off 留在次优氧区。页面结论：「短板 + 支持」的概念成立，但具体 `MIN / MAX / PRODUCT` **不是现实 Authority**。
- 因此页面明确把比较对象限定为 **Authoring 结构能力**，不是保护某个临时公式。

## 2. 四条候选路线的主张、证据与代价

### Option A｜固定专用 Structured Trade-off Template（§2）
- 主张：固定 slot 表（Hard Gate / Thermal / Oxygen / Visibility / Cover Support / Prey Support，各自绑定输入与 Profile），中间结果组合写死。
- 优点：完全固定、易 Trace、不给实例任意控制流、不需要 Expression AST。
- 代价/问题：`MIN / MAX` 很可能只是 Bass 当前故事的临时公式；下一条鱼需要另一种 `Temp × DO` 交互时又要再买一个专用 Template；Template 数量膨胀本质上是把 Expression Pattern 逐个固化。
- Verdict：**可用，但不是当前首选。**

### Option B｜2D Interaction Profile + Independent Factor Set（§3）
- 主张：Temperature × DO 的交互不让 Authoring 编辑表达式，而作为**稳定的二维 Response Surface** 配置（`@BassSummerOxythermal`，Editor 可表现成二维表/heatmap，页面明确不冻结数值）。
- 实例能配置：2D Profile 数值面、各一维 Profile、DO Hard Floor、Support Profile Ref。实例**不能**配置：任意 Operator Tree、任意嵌套、Step Order、Next/Jump、中间变量依赖。
- 代价：需新增 Authoring Primitive Candidate `lookup2d / 2D Profile Editor`；页面自认不能因 Bass 一例直接 Promote，应统计复用率。
- Verdict：**CURRENT PREFERRED CANDIDATE。**

### Option C｜Narrow Expression Layer（§5）
- 主张：如 `return product(lookup2d(temp, do, @OxythermalProfile), lookup(visibility, @VisibilityProfile), max(lookup(cover, @CoverProfile), lookup(prey, @PreyProfile)))`。
- 优点：表达极短；新 trade-off 不需要新建 Template；数学结构直接可见。
- 代价：开放 MIN/MAX/PRODUCT/SUM/CLAMP/lookup/lookup2d/任意嵌套，等于购买完整 Expression AST（Operator Node / Operand Node / Profile Call / Nested Tree / Validation / Trace / Editor / Compiler Error）。
- Verdict：**NOT ADMITTED YET。** 重新打开条件四条（原样）：(1) 多个已审案例需要不同、不可压缩的 operator nesting；(2) 固定 Template / typed slot 数明显增长；(3) 2D Profile / Resolver 无法合法吸收交互；(4) Narrow Expression 能显著降低**总维护复杂度**而非只减少页面行数。

### Option D｜把整个 Habitat Quality 交给 Resolver（§6）
- 主张：`BioenergeticHabitatQualityResolver(temperature, DO, prey, cover, visibility) → HabitatQualityPotential`，Bake 只做 lookup。
- 拒绝理由：Fish-specific Authoring 复杂度迁到 Resolver；策划看不出各因子贡献；Resolver 易成不可审计黑盒；违反 Resolver Complexity Guardrail 的风险高于 2D Profile。例外：若未来独立 World/Bioenergetics 系统本来稳定产出该事实，Bake 才应消费。
- Verdict：**REJECT AS AUTHORING SHORTCUT。**

§7 四方案比较表（Authoring 自由度 / 新增基础设施 / Trace / 模板膨胀风险 / 判断）原样确认：A 可用非首选、B Preferred、C 暂不准入、D 拒绝捷径。

**重要：页面存在叙事内演化。** §4 曾引入固定构件 `AlternativeSupportSlot`（N 个独立 Support Factor，固定 Combine=MAX），§12 起被列为「未闭点」，§13 用现实侧论证否定 MAX 冻结，§15.7 最终 `AlternativeSupportSlot → 从最小结构删除`，§16.7 的最小句型退回 Cover/Forage 各自 Unary。**引用本页任何结构主张时必须锁定节号与时间戳**（文献支持：以上均为页面文本直接内容；「§4→§16 是同一页面内的先后演化」为推断，依据是各节 Verdict 相互覆盖且 §16.8 给出压缩轨迹）。

## 3. 判定标准 / Signature / 验收方式（页面声明的）

1. **Primitive Admission Ladder（§11）**：P0 Unary Profile → P1 Typed 2D Interaction Profile → P2 Stable Mechanistic Resolver → P3 Fixed Typed Composite Slot → P4 Structured Specialized Template → P5 Narrow Expression/DSL Escape。排序依据是 **Authoring 自由度与长期维护成本**，不是功能强弱。
2. **Expression Gate 一句话准入（§15.5）**：「不看输入变量有几个，也不看 Profile 有几张；只看策划是否必须编辑中间结果之间的依赖拓扑。」Breaker 定义为 `IntermediateDependency = YES` 且该依赖**必须由 Authoring 直接编辑**。明确否决「超过 N 张 2D Profile 就升级 DSL」的数量阈值。
3. **Pairwise Breaker——2D Profile 准入（§16.5）**：不是「两个因素互相有关」，而是**不可分离交互**：如低 Forage 时 High Cover > Low Cover 而高 Forage 时方向反转，或 Cover 最佳区间随 ForageAvailability 系统性移动。「二者都重要」不构成 2D 证据。
4. **2D Profile 准入约束（§10.3，由 Light × Turbidity 反例得出）**：2D Profile 用于「Species/Group 真正需要配置的双变量 Response Surface」，不用于替代本应由稳定 Resolver 负责的物理/感知计算。
5. **Cross-case Reuse Test（§10）**：Temp×DO = `REUSE_SUPPORTED`（页面声称覆盖 Largemouth Bass / Striped Bass / Landlocked Atlantic Salmon——**无引文，未证实档，页面断言**）；Temp×Salinity = `2D_PROFILE_PRIMITIVE_REUSE +1`；Drift-feeding trout = `3PLUS_VARIABLE_COMPLEXITY_FOUND`，但被合法 Resolver Boundary 收住（满足 Resolver Admission Test：语义稳定、跨案例复用、作者不编辑内部控制流、同一 Snapshot 确定输出）。
6. **SurfaceLogicSignature / B-T1 executor 约束（§15.2）**：所有 Fit 只读同一份 Resolved Snapshot；Factor A 不读 Factor B 输出；Factor 顺序无 Authoring 语义；禁 Next/Jump/Loop、任意算子、任意中间变量、可变 Final Combine 拓扑。Profile 数量不同不拆 Signature。
7. **复杂度记账（§15.6，防 `L_bake=1` 假简化）**：建议 Harness 追加统计 `N_2D_Profile_Bindings`、`N_Unique_Axis_Pair_Families`、`2D_Profile_ControlPoint_Volume`、`N_Fixed_Composite_Slot_Kinds`、`N_Distinct_Dependency_Graphs`；若 B-T1=1 但每条鱼配大量独特 2D Surface + case-specific Resolver，仍判**复杂度迁移**而非简化。
8. **对 L_bake 的影响（§8）**：B-T2 Structured Trade-off Template 暂不确认；`L_bake_base_candidate` 可能从 ≈2 向 ≈1 收敛，前提三条：2D Profile 非 Bass 专属、AlternativeSupportSlot 非假通用构件（注：此后已被删除）、横向案例不要求自由 operator nesting。

无传统 Merge Test 措辞；验收以 Readout 代码块表达（全大写 snake case，见 §16.8：`CONFIG_MAIN_PATH_STRENGTHENED / LOCAL_SUPPORT_2D_NOT_ADMITTED / FORAGE_FACT_BOUNDARY_NARROWED / EXPRESSION_BREAKER_NOT_FOUND`）。

## 4. 页面引用的输入（被引页面本批不展开）

| 引用 | URL | 访问时间 | 状态 |
|---|---|---|---|
| 父页：4 Logic Surface Authoring Stress Test R1｜分群/烘焙/响应/品质选择（BA-T4 原句型所在层级，即 Bass 投影/Stress Test 载体） | https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3 | 2026-09-10T03:49:56Z（仅拓扑确认，全文未读） | 未展开 |
| §15.7 末 mention-page（无 title 属性；依紧邻正文，是「现实/Behavior Mode 数量增加不直接增加 L_bake，只有控制拓扑、IO Contract 或 Authoring-visible Intermediate Dependency 改变才形成新 Logic Signature」的边界页） | https://app.notion.com/p/3d6a4137d23681049e3dc602d9e784c4 | 2026-09-10T03:49:56Z（仅捕获引用） | 未展开 |
| 概念级输入（无独立 URL，正文引用名）：BA-T4 压力句型、B-T1/B-T2、`L_bake`、Resolver Admission Test、Resolver Complexity Guardrail、Bass Summer Stress Story | — | — | 定义应在其上游 Stress Test R1 / Working Main |

注：页内生态断言（跨物种 oxythermal 复用、植被密度改变 search/ambush tactic 等）**全部无外部文献链接**，属页面断言，不构成本记录的文献支持档。

## 5. 页面自己声明的 open questions 与下一步

1. **§16 当前最高优先（下一条窄 Knife）**：闭合 `ForageOpportunity（收紧为 UsableForageAvailability）Semantic Contract × CoverComplexity Ownership Boundary`。候选 Contract：只表达「这里有多少我能吃的东西」（可吸收 prey field / diet eligibility / size eligibility），明确不吸收 CoverComplexity、capture advantage、visibility、attack geometry、capture success、energetic cost——否则 Fish Bake 再用 Cover/Visibility 会重复结算同一原因。
2. **§12 未闭点**：`AlternativeSupportSlot = MAX(CoverFit, PreyFit)` 是 gameplay/representation candidate 而非生态公式；是否存在真实案例要求 Support 为 SUM / weighted mix / conditional substitution 且不能被 Profile/Resolver 合法收掉。
3. **§14 下一轮真正值得找的**：交互不能被一到数个独立 2D Profile + stable Resolver 分解、且策划确实需要直接编辑 3+ 变量中间依赖的案例——只有这类才重新成为 Expression/DSL 强正证据。
4. **§9 Cross-case Breaker 清单**：A. Temp×DO 之外的双变量交互；B. 3+ 变量共同交互、2D 明显不够；C. Alternative Support 非 MAX 组合；D. Factor B 必须读 Factor A 中间结果。A 多则 Config+2D 增强，B/C/D 增则重开 Expression Gate。
5. **§15.6**：复杂度记账指标落地到 Harness。
6. **§16.7**：`FIXED_COMBINE` 具体数学公式不冻结，本刀只冻结 Representation Boundary（Fit 并列输入、禁作者建立中间依赖）。

## 6. 对「攻击面」的初步研究观察（推断档，供 Evidence Reviewer 攻击）

- **这把刀试图证伪的假设**：「声明式 Config 主路径（B-T1 Independent Factor Set + Profile）足以表达 Summer Oxythermal Stress——这个曾被当作最强 Structured Trade-off Breaker 的案例——无需购买 Expression DSL 或专用 Template。」执行方式是**主动攻击自己的最强正证据**：逐轮压缩 BA-T4 的 Gate+MIN+MAX+PRODUCT 嵌套，检验每层结构是否真有不可替代性。
- **结果是反向加强**（§16.8 压缩轨迹）：BA-T4 → 2D Oxythermal + AlternativeSupport MAX → 2D Oxythermal + LocalSupport2D → 2D Oxythermal + Cover/Forage/Visual 三个 Unary + Fixed Combine。真正经过压力测试留下来的非一维 Authoring Primitive 只剩 `Generic Typed 2D Interaction Profile`；SummerStress 从「最强 Structured Trade-off Breaker」**降级**为「2D Interaction Profile 的最强正样本」（§14 原话）。
- **同页暗含的第二重防御**：这把刀同时防「假简化」——压低 L_bake 但把复杂度迁移成大量 2D Surface / case-specific Resolver / 隐蔽 Typed Slot 词汇表（§15.1 明确反对 `OxythermalProfileNode` 式逐故事造 Slot；§15.6 记账指标即为此设）。即它攻击的不仅是「需要 DSL」假设，也在攻击「L_bake 变小 = 简化成功」的度量假设。
- **Missed Story 声明（覆盖范围）**：本记录只覆盖该页 live 全文（03:49:56Z 版本）。未覆盖：父页 Stress Test R1 全文（BA-T4 原始定义与 Bass 投影卡）、mention-page 3d6a41…e784c4 的 Logic Signature 边界原文、页面评论/discussion（本批 fetch 未含 include_discussions）、02:57Z→03:49Z 之间的编辑 diff（Notion 不提供）。生态断言的外部文献核验未做——页面自己也把这些标为非 Authority，若 Evidence Reviewer 需要 REUSE_SUPPORTED 的现实证据，须另开外部文献批次。

## 记忆增量提案（本环境无 Write/Edit 工具，未能物理写回 role_memory/fcf-fish-researcher.md；内容如下供持久化）

- 拓扑捷径追加：Summer Knife R0（3d6a4137…7e352b50）结构 = §0 Verdict First / §1 原句型问题 / §2–§6 四方案（A Template、B 2D Profile、C Narrow Expression、D All-in Resolver，标题只列前三）/ §7 比较表 / §8 L_bake / §9–§14 Cross-case / §15 B-T1 Boundary Delta / §16 Forage×Cover Owner Boundary Knife；§15、§16 是后缀 WORKING DELTA，**页内后节 Verdict 覆盖前节**，引用必须带节号；Readout 为全大写 snake case。KNIFE-READ-001 已读全文，版本 page_last_edited_at 2026-09-10T03:49:56Z（对比 TEST-FR-001 时 02:57:49Z 有漂移）。
- 拓扑捷径追加：页内 mention-page 3d6a4137d23681049e3dc602d9e784c4（无 title）= Logic Signature / L_bake 边界页，候选下轮读取。
- 来源可信度追加：Summer Knife R0 页 Notion verification = unverified；页内生态断言（跨物种 oxythermal、Cover/Prey tactic 等）无外部文献引文且页面自声明 NOT AUTHORITY，引用按「页面断言（未证实）」处理。

## 来源清单

1. Summer Oxythermal Stress Representation Knife R0｜2D Profile vs Structured Trade-off vs Narrow Expression — https://app.notion.com/p/3d6a4137d23681d0a3a5ddbf7e352b50 — live fetch，2026-09-10T03:49:56.533Z，page_last_edited_at 2026-09-10T03:49:56.533Z
2. 父页（拓扑确认，未展开）：4 Logic Surface Authoring Stress Test R1 — https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3
3. 页内被引页（未展开）：Logic Signature / L_bake 边界页 — https://app.notion.com/p/3d6a4137d23681049e3dc602d9e784c4

BATCH_ID: KNIFE-READ-001
