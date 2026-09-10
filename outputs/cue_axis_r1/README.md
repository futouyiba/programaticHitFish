# 呈现 Cue 轴模态扩充（化学 scent + 电场 electro）表达 R1｜Config 主路径 + Narrow DSL 对照

`Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED`

| 项 | 值 |
|---|---|
| 批次 | REP-CUE-AXIS-001（B0 REPRESENTATION_RUNNING 首轮） |
| 角色 | fcf-representation-worker |
| 输入来源 | (1) 立项规格：`outputs/coverage_delta_r1/report.md` §2.3（K8 判定 NEW_CONFIG_COVERAGE，#13+#47；已过独立验收 REP-COVERAGE-DELTA-REV-001，内容零错——经 Coordinator 转达，report 头部有验收记载）；(2) #47 电轴前提闭合：`outputs/batches/FISH-R05-FR3-001R`（CD-R05-01「K8 电轴前提确认成立」，FR3 Packet CLOSED，Packet id 3d7a4137d236812a9b97dbb862f7248c）；(3) 结构参照：live Stress Test R1 主页本地转录（REP-CLARITY-FIX-001 后版本，`tmp/live_stress_main_after.md`）「§5.1 配置表 Candidate Grammar｜中文化版本」「§17. Generic Reaction Response Projection R0」之 §17.2/§17.3/§17.5；(4) 机制约束：`outputs/batches/KNIFE-READ-001.md`（Knife R0 归档，page_last_edited 2026-09-10T03:49:56Z）§11 / §15.6 / §16.5 / §16.7；(5) 工件形态样板：`outputs/usable_forage_contract_r0/`（r1 修复轮） |
| 对应执行面 | **Response**（呈现 Cue 轴：呈现侧计算事实 → unary Profile lookup → Fit 并列并入既有 Feeding/Reaction 通道）。Group / Bake / Quality 面不在本批范围 |
| 基线声明 | **SNAPSHOT_ONLY**——全部输入为本地归档/转录，本批未 re-fetch live；live 漂移时以本 README 引用的归档版为准。引用纪律循 coverage report 头部勘误：主页节引用须「节号+节标题」双限定（主页存在重复编号 §7×2、§8×2） |
| 数值状态 | 全部数值（lookup table 的 input/fit 值、事实取值域）为示例占位，**不最终定值**；本包只交付表达边界。合并算子数学保持 **OPERATOR UNDEFINED**（机制侧待定，循 live §17.2「算子标注」与 Knife §16.7「FIXED_COMBINE 数学不冻结」先例） |

## 1. 契约陈述（两轴语义边界）

本扩充回答且只回答一个问题：**当前呈现（lure/bait 状态）携带的化学味型强度与电场特征，对该 population 的触发适配（Fit）是多少**。每根轴 = 一个**上游呈现侧计算事实** → 一张**一维 Profile** 的 unary lookup → 一个 **Fit**；Fit 作为**并列输入**并入既有 RR-T1 Feeding/Reaction 通道的 FIXED_COMBINE（通道、拓扑、汇总结构全部沿用既有，不新增）。

```
ScentCueFit        = lookup(BaitScentIntensity, @ScentCueProfile)
ElectroFieldCueFit = lookup(LureElectricField,  @ElectroFieldProfile)
ChannelResult      = FIXED_COMBINE(既有通道结果, ScentCueFit, ElectroFieldCueFit)
                      // 合并数学 UNDEFINED — 机制侧待定；本包只冻结
                      // 「Fit 并列输入、拓扑固定、无作者可编辑中间依赖」
```

本扩充**不决定**：

- 气味/信息素在水体中如何**输运**、电场如何**传导衰减**——感知/环境 Resolver owner（本轴消费的是已计算好的呈现侧事实，不自行折算）；
- 鱼能否**物理感知/到达**该呈现——感知面 owner；
- 呈现是否转化为**咬口、上钩、钓获**——Encounter/Conversion owner；
- 电鳗**主动放电/远程麻痹**等结果语义——Encounter/Conversion owner（#47 边界：电轴只承载感知段）；
- 陷阱捕获（#13 的 陷阱=Encounter/装备侧 scope flag，不在本轴）。

## 2. 语义边界表（吸收 / 排除）

### 吸收（且仅吸收）

| 吸收项 | 在 Config 中的落点 |
|---|---|
| 化学模态呈现 Cue 轴 | `profile_slots[]` 行 `@ScentCueProfile`（味型/信息素强度→触发适配），绑定事实 `BaitScentIntensity` |
| 电感知模态呈现 Cue 轴 | `profile_slots[]` 行 `@ElectroFieldProfile`（拟饵/环境电场特征→触发适配），绑定事实 `LureElectricField` |
| 事实枚举（Grammar 5.1 复用） | `fact_atoms[]` 两行：V2/V3 形态、零新列、上游呈现侧计算事实 |
| per-population 数值面 | `instances[]`：population × slot × profile_instance × 示例 lookup table |
| 并入既有通道 | `combine`：FIXED_COMBINE 常量、math UNDEFINED、`author_selectable=false`、joins 钉死「并入既有 RR-T1 通道、不开新通道」 |

### 排除（各归其 owner；不得在本轴配置中作为语义出现）

| 被排除语义 | Owner | 若渗入本轴，会双重结算什么 |
|---|---|---|
| capture / catch / grasp / encounter / seize / hook / swallow / bite；捕获 / 抓 / 遭遇 / 咬 / 吞 / 钩 | Encounter / Conversion | 「味型强度高 / 电场特征明显 → Fit 高」已经表达了「更愿意就饵」；若再在本轴内写咬口/上钩倾向修正，Encounter/Conversion 按捕获优势再折一次——同一次呈现→上钩过程被折价两次 |
| attack / strike / kill；攻击 / 袭击 / 扑 / 杀 | Encounter | 攻击几何/意图在本轴提前结算一次，Encounter 面再结算一次 |
| 麻痹（paralysis）/ 冻结（freeze·frozen）/ 电击（shock·electrocution）/ 击晕（stun）/ 麻木 / 眩晕 / 制服 / immobilize | Encounter / Conversion | #47 远程麻痹捕获边界：放电**结果**语义渗入**感知**轴——感知 Fit 与麻痹效果被混在同一结算里，捕获侧无从单独结算 |
| 输运/传导耦合项（味型×水流、电场×水体传导衰减） | 感知 / 环境 Resolver | 2D/嵌套耦合项把物理计算搬进 Response 面——表达侧由 AXIS（unary 准入、无第二轴、无嵌套）与 FACT（封闭枚举）**结构检查**杜绝；词干守卫不覆盖此族（结构检查是更精确的代理） |

### 排除语义的词法代理（guard）声明

`config/validate_config.py` 的 GUARD 检查族对配置**全文（键+值）**做 fail-closed 双表扫描：**英文词干表**（token 级前缀匹配，camelCase 拆分，18 条，覆盖 capture/attack/incapacitation 三族）+ **中文关键词表**（子串检查，17 条，检查面覆盖键、值、原文与 `\uXXXX` 转义解码面）。**这是语义排除承诺的词法近似，不是承诺本身**——同义词表不可能穷尽（未列入的英文同义词、未列入的中文措辞、其它语言/拼音/完全同义的重命名键都会漏过）；发现漏网即扩充词表并重跑 §6 验证。误报方向（如英文 bit- 词族、中文单字「咬/吞/钩」的任何复合词）已被 fail-closed 设计接受——本轴配置没有任何合法内容需要这些词族。

排除项命名只出现在**本 README 边界表与守卫实现（validator 源码）**中；config 与 dsl 两个契约工件本身不含排除语义的任何词干/关键词。

## 3. 轴规格表（列级）

### 3.1 Cue 轴 Profile 槽位（挂 live §17.2「Reaction Profile 配置」表同款两列「配置项/含义」，加两行）

| 配置项 | 含义 |
|---|---|
| `@ScentCueProfile` | 味型/信息素强度→触发适配 |
| `@ElectroFieldProfile` | 拟饵/环境电场特征→触发适配 |

边界扩展视图（转写 Notion 时两列原样保留，下表为边界注记，不进 §17.2 表）：

| 配置项 | 模态 | 事实绑定 | 阶 | 并入 |
|---|---|---|---|---|
| `@ScentCueProfile` | chemical_scent | BaitScentIntensity | P0_unary_profile_lookup | 既有 RR-T1 通道 FIXED_COMBINE |
| `@ElectroFieldProfile` | electric_field_sensing | LureElectricField | P0_unary_profile_lookup | 既有 RR-T1 通道 FIXED_COMBINE |

### 3.2 条件原子「事实/计算项」枚举值（Grammar 5.1 复用，V2/V3 形态即可，零新列）

| 事实/计算项 | 语义 | 语法形态 | 新列数 |
|---|---|---|---|
| `BaitScentIntensity` | 当前呈现的味型/信息素强度（上游呈现侧计算事实） | V2/V3 复用 | 0 |
| `LureElectricField` | 拟饵电场特征（上游呈现侧计算事实） | V2/V3 复用 | 0 |

V2/V3 形态示例行（对照 live §5.1 声明的列结构变体；RuleSet 引用时按既有 R1/R2 规则集形态，均零新列）：

```plain text
V2 单值形态（列：条件组/条件/事实·计算项/参数/比较符/比较值）
  S1 | S1.C1 | BaitScentIntensity  | —  | >= | @ScentGateThreshold
V3 无参数形态（列：条件组/条件/事实·计算项/比较符/比较值）
  E1 | E1.C1 | LureElectricField   | >= | 电场特征存在档
```

### 3.3 组合边界（本批冻结的全部内容）

1. **两轴只做 Unary Profile lookup**（Primitive Admission Ladder P0 阶，Knife §11）：单事实输入、无嵌套、无第二轴、无 2D——validator AXIS 检查族逐项强制（arity 钉 unary、ladder 钉 P0、fact_atom 拒绝列表形态与 Profile 引用、行内键第二轴形态拒启、lookup 输入拒绝 Profile 引用）。
2. **Fit 并列并入既有 Feeding/Reaction Channel 的 FIXED_COMBINE**：不开新通道、不改合并拓扑（validator COMBINE 检查族钉死 operator=FIXED_COMBINE、joins 声明、author_selectable=false）。
3. **合并算子数学 OPERATOR UNDEFINED**——机制侧待定（循 FIXED_COMBINE Working Algorithm Candidate 先例）；本规格只冻结「新轴为 Unary、Fit 并列输入、无作者可编辑中间依赖」的边界，数值与合并数学不冻结。
4. **输运/传导耦合归感知/环境 Resolver owner，不开 2D**（除非未来出现 §16.5 型不可分离样本）。

### 3.4 实例绑定

沿用 Profile 实例级绑定既有机制（coverage report K13 先例：per-instance Profile 重绑定）；`instances[]` 即此形态。本批示例实例：

| population | 槽位 | Profile 实例 | 语义限定 |
|---|---|---|---|
| sea_lamprey_migratory_spring | @ScentCueProfile | @SeaLampreyMigratoryScentCue | #13 海七鳃鳗生殖化学趋向——**只做感知/适配语义**；陷阱捕获归 Encounter/装备侧 |
| electric_eel_sensing | @ElectroFieldProfile | @ElectricEelElectroSense | #47 电鳗感知段——**只做感知语义**；主动放电/远程麻痹边界归 Encounter/Conversion |

## 4. 与 §17.2 既有 cue 轴的并入方式

- **落点**：live「§17.2 Config 表达」的 Reaction Profile 配置表（两列「配置项/含义」）**加两行**（§3.1）；不新增列、不新增表、不新增构件种类。既有行（@AbruptnessProfile / @DeflectionProfile / @VibrationProfile / @FlashProfile / @ProximityProfile / @PursuitDemandPenalty / @ReactionCap）不动。
- **消费路径**：live §17.3 中文伪脚本的「读取」清单加两行。规格 §2.3 伪脚本原样：

```plain text
评价 Feeding Channel：
    读取当前饵 / Presentation Cue（速度、轨迹、水层与相对位置——既有轴）
    读取当前饵的味型强度（BaitScentIntensity——新轴事实）
    用 BaitScentIntensity 查询 @ScentCueProfile
    得到 ScentCueFit

    与 @FeedingProfile 的结果按模板固定规则合并
    得到 FeedingResponse
```

  电轴同构（LureElectricField → @ElectroFieldProfile → ElectroFieldCueFit）。两轴 Fit 与既有通道结果的合并循 RR-T1 固定规则；**汇总数学 UNDEFINED**（live §17.2 算子标注原样沿用，本批不定义）。
- **实例绑定**：循 §17.2「实例绑定示例」表的既有机制（Behavior Mode / Feeding Profile / Reaction Profile 旁按实例重绑定的同款做法）；不新设绑定表列结构（绑定差异 = per-instance Profile 重绑定，零结构增量）。
- **模板计数**：对 live §17.5 的 RR-T1/T2/T3 压缩结论**无影响**——两轴只给既有通道加并列输入，不新增 Behavior Mode、不新增 Channel、不新增 Response 模板。

## 5. 交付文件

| 文件 | 执行面 | 输入来源 | 使用 / 放弃的自由度 |
|---|---|---|---|
| `config/cue_axis.config.json` | Response（呈现 Cue 轴） | 立项规格 §2.3 + live 转录 §17.2/§5.1 + CD-R05-01 | 使用：槽位命名（规格钉死）、事实枚举名（规格钉死）、含义文案（zh）、模态分类值、示例实例选取（lamprey/eel）、lookup table 行值。放弃：第二输入轴 / 2D（钉死 unary）、嵌套 lookup、可换算子、新通道、新表列、把输运/传导耦合写进本轴（全部归 owner 或后续规格动作） |
| `config/validate_config.py` | Response（表达验证） | 同上 + forage r1 validator 模式（词干+中文关键词+转义三面+行级白名单+封闭枚举） | 使用：检查族划分（TOP/STRUCT/AXIS/FACT/COMBINE/GUARD）、词表选取、封闭集钉死。放弃：无（校验器不引入语义） |
| `dsl/cue_axis.dsl.txt` | 对照（NOT ADMITTED — comparison / L_observed only） | 同上 + Knife §5 Option C 表达式风格 | 使用：表达式形状。放弃：不把它当契约输入（不声明键/绑定/新语义） |
| `accounting.md` | 记账（跨面） | 同上 + KNIFE-READ-001 §11/§15.6/§16.5/§16.7 | 见该文件 |
| `README.md`（本文件） | 边界文档 | 同上 + coverage report §2.3/§5/§6 | — |

## 6. 验证记录（命令与输出原样）

命令 1——真实配置校验：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/cue_axis_r1/config/validate_config.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/cue_axis_r1/config/cue_axis.config.json"

== A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/cue_axis_r1/config/cue_axis.config.json ==
[OK]   TOP     no author-invented top-level sections (no intermediate-dependency or axis-pairing surface)
[OK]   STRUCT  structure + referential consistency (identity pinned, fixed row schemas, declared facts/slots, every slot bound)
[OK]   AXIS    unary-only axis admission (closed slot set, single fact atom, P0 stage, no nesting, no second axis, no 2D)
[OK]   FACT    closed fact enum (2 presentation-side computed facts, Grammar 5.1 V2/V3 reuse, zero new columns)
[OK]   COMBINE FIXED_COMBINE into existing RR-T1 channel, operator_math UNDEFINED, author_selectable=false
[OK]   GUARD   no excluded semantic stem or zh keyword in any key or value (capture/attack/incapacitation families; stems: captur, catch, grasp, encounter, seiz, hook, swallow, bit, attack, strike, kill, paraly, stun, freez, froz, electrocut, shock, immobil; zh keywords: 17, table in source)
== result ==
PASS (6 check families, 0 violations)
EXIT=0
```

命令 2——守卫 / 检查族自测（证明每个检查族、**每一条英文词干、每一条中文关键词**真的会对坏输入触发——词表条目拼错会静默失效，逐条 probe 是词表自身的质量门）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/cue_axis_r1/config/validate_config.py" --selftest

== selftest ==
[OK  ] baseline fixture passes unchanged
[OK  ] a second population may bind the same slot (slot is reusable)
[OK  ] GUARD fires on stem 'attack' (probe 'attack')
[OK  ] GUARD fires on stem 'bit' (probe 'bites')
[OK  ] GUARD fires on stem 'captur' (probe 'capture')
[OK  ] GUARD fires on stem 'catch' (probe 'catches')
[OK  ] GUARD fires on stem 'electrocut' (probe 'electrocution')
[OK  ] GUARD fires on stem 'encounter' (probe 'encounters')
[OK  ] GUARD fires on stem 'freez' (probe 'freezing')
[OK  ] GUARD fires on stem 'froz' (probe 'frozen')
[OK  ] GUARD fires on stem 'grasp' (probe 'grasps')
[OK  ] GUARD fires on stem 'hook' (probe 'hooked')
[OK  ] GUARD fires on stem 'immobil' (probe 'immobilized')
[OK  ] GUARD fires on stem 'kill' (probe 'kills')
[OK  ] GUARD fires on stem 'paraly' (probe 'paralysis')
[OK  ] GUARD fires on stem 'seiz' (probe 'seizes')
[OK  ] GUARD fires on stem 'shock' (probe 'shock')
[OK  ] GUARD fires on stem 'strike' (probe 'strikes')
[OK  ] GUARD fires on stem 'stun' (probe 'stunned')
[OK  ] GUARD fires on stem 'swallow' (probe 'swallowing')
[OK  ] GUARD fires on zh keyword '捕获'
[OK  ] GUARD fires on zh keyword '抓取'
[OK  ] GUARD fires on zh keyword '遭遇'
[OK  ] GUARD fires on zh keyword '咬住'
[OK  ] GUARD fires on zh keyword '吞下'
[OK  ] GUARD fires on zh keyword '上钩'
[OK  ] GUARD fires on zh keyword '攻击'
[OK  ] GUARD fires on zh keyword '袭击'
[OK  ] GUARD fires on zh keyword '扑咬'
[OK  ] GUARD fires on zh keyword '击杀'
[OK  ] GUARD fires on zh keyword '麻痹'
[OK  ] GUARD fires on zh keyword '冻结'
[OK  ] GUARD fires on zh keyword '电击'
[OK  ] GUARD fires on zh keyword '击晕'
[OK  ] GUARD fires on zh keyword '眩晕'
[OK  ] GUARD fires on zh keyword '麻木'
[OK  ] GUARD fires on zh keyword '制服'
[OK  ] GUARD fires on key with capture stem (slot row allowlist co-fires)
[OK  ] GUARD fires on value with attack stem
[OK  ] GUARD fires on camelCase token (AttackWindowProfile)
[OK  ] GUARD fires on zh keyword in a fact_semantics value
[OK  ] STRUCT fires on unknown key inside a profile_slots row
[OK  ] STRUCT fires on unknown key inside a fact_atoms row
[OK  ] STRUCT fires on unknown key inside an instances row
[OK  ] STRUCT fires on unknown key inside a lookup table row
[OK  ] STRUCT fires on axis_semantics drift
[OK  ] STRUCT fires on missing contract.input_scope
[OK  ] STRUCT fires on slot fact_atom not declared in fact_atoms
[OK  ] STRUCT fires on instance bound_slot outside the declared slots
[OK  ] STRUCT fires on duplicate (population, slot) binding
[OK  ] AXIS fires on fact_atom as a list (two input axes = not unary)
[OK  ] AXIS fires on fact_atom referencing a Profile (no nested lookup; STRUCT co-fires on undeclared fact)
[OK  ] AXIS fires on arity drift (binary)
[OK  ] AXIS fires on ladder_stage drift (typed 2D is P1, not admitted)
[OK  ] AXIS fires on axis_pair key in a slot row (second-axis surface; row allowlist co-fires)
[OK  ] AXIS fires on the same fact feeding two slots (completeness STRUCT co-fires)
[OK  ] AXIS fires on lookup input referencing another Profile (no nested lookup)
[OK  ] AXIS fires on a declared slot missing from profile_slots (STRUCT co-fires on the unbound instance)
[OK  ] STRUCT fires on a declared slot left without any instance binding
[OK  ] FACT fires on fact atom outside the closed enum (slot + table mutated consistently)
[OK  ] FACT fires on columns_added drift (a new column would be a new column structure)
[OK  ] FACT fires on grammar_form drift (no new column variants)
[OK  ] FACT fires on computed_by drift (world-side computation is not this batch's fact)
[OK  ] COMBINE fires on author-chosen operator
[OK  ] COMBINE fires on silently-defined combine math (must stay visibly UNDEFINED)
[OK  ] COMBINE fires on author_selectable=true
[OK  ] COMBINE fires on joins drift (a new channel is not admitted)
[OK  ] TOP fires on author-invented steps section
[OK  ] TOP fires on author-invented axis_pairs section (the 2D pairing surface is not a section)
== result ==
SELFTEST PASS (69 cases)
EXIT=0
```

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器为纯标准库，任何 Python 3 均可运行（内部强制 stdout 为 UTF-8，与控制台代码页无关）。

### 守卫词表（词法代理表，完整列示）

英文词干 `EXCLUDED_SEMANTIC_STEMS`（18 条，token 级 fail-closed 前缀匹配，camelCase 拆分后 `CaptureWindow` / `capture_window` / `captureWindow` 全落网）：

| 排除族 | 词干 |
|---|---|
| capture（Encounter/Conversion owner） | captur, catch, grasp, encounter, seiz, hook, swallow, bit |
| attack | attack, strike, kill |
| incapacitation（麻痹/冻结/#47 远程麻痹） | paraly, stun, freez, froz, electrocut, shock, immobil |

词干 `freez` 与 `froz` **必须并列**：`freezing = freez+…` 而 `frozen/froze = froz+…`，单取其一必漏一支（selftest 各有独立 probe；与 forage 契约 perceiv/percep 双词干同类教训）。

中文关键词 `EXCLUDED_SEMANTIC_ZH`（17 条，对键 + 值 + 原文 + `\uXXXX` 解码面做子串检查）：

| 排除族 | 关键词 |
|---|---|
| capture | 捕获, 抓, 遭遇, 咬, 吞, 钩 |
| attack | 攻击, 袭击, 扑, 杀 |
| incapacitation | 麻痹, 冻结, 电击, 击晕, 眩晕, 麻木, 制服 |

单字条目（抓/咬/吞/钩/扑/杀）按子串过度匹配任何复合词——fail-closed 设计接受，因为本配置的合法中文内容仅两条含义文案与两条事实语义文案，均不含这些字。

**残余风险声明（与 §2 一致）**：双表是语义排除承诺的词法近似，不是承诺本身；发现漏网即扩充词表并重跑本节验证。

### 修复过程自查记录（诚实记录，未改测试凑通过）

1. 自测首轮抓出 3 个实现缺陷：(a) 槽位枚举 elif 链吞掉 `slot_names.append` 副作用，导致「第二槽位绑定同一事实」用例缺 STRUCT 共启；(b) 事实枚举同型缺陷（`declared_facts.append` 被 elif 链吞掉）；(c) 词干 `freez` 单取漏 `frozen`（英语形态学：freeze→freezing 走 freez-，froze/frozen 走 froz-），补 `froz` 双词干。三处修复后 69 用例全过。
2. 守卫曾在**本包自己的 config**上开火：占位声明的「not frozen」（数值不冻结的状态用语）命中 `froz` 词干（本批的「冻结」是定住鱼类语义）。处置：config 措辞改为「not final, not binding」（语义不变），不是改词表放行——状态用语换词合法，排除语义不能放行。
3. 为使 §2「config 与 dsl 工件本身不含排除语义的任何词干/关键词」在中文子串级严格成立，dsl 元注释的「拓扑」全部改写为「结构」（「拓扑」含关键词单字「扑」；与 forage 契约 F6「表达成本→表达开销」同类处置）。机械复验：对 config 与 dsl 全文按全部 18 词干 + 17 关键词 grep，零命中（README 与 validator 源码按约定允许出现排除项命名）。

## 7. 边界声明

- 本包只做呈现 Cue 轴模态扩充（两轴）；不铺 15 Case，不改 `fcf_v1/`，不动密封包，不 commit。
- 表达验证通过 ≠ 机制 promotion ≠ Freeze；本包不覆盖 Knife 页或 live 主页任何 Verdict。合并算子数学保持 OPERATOR UNDEFINED 待机制侧。
- **#47 电轴语义限定**：只承载感知段（电场特征→触发适配）；主动放电/远程麻痹捕获边界归 Encounter/Conversion owner（FISH-R05-FR3-001R owner 分解；coverage report §5-a 已登记 Encounter lane 输入）。
- **#13 scent 轴语义限定**：生殖化学趋向的感知/适配语义；陷阱捕获归 Encounter/装备侧 scope flag（coverage report #13 判定行）。
- **事实口径不冻结**：BaitScentIntensity / LureElectricField 的取值域、档位、量化由上游呈现侧产出契约决定，不在本批输入内；本包交付的是枚举名 + 口径语义（上游呈现侧计算事实）+ 封闭绑定结构。若上游日后交付「修正口径」事实（如按传导衰减折算后的电场特征），属上游事实族登记事项（类比 forage 契约 R1 README §6 的 SNAP allowlist 收窄义务），届时 FACT 封闭枚举随之收窄，不在本轴配置内自行折算。
- **后续加轴 = 规格动作**：SLOT_ENUM / FACT_ENUM 在 validator 中封闭钉死本批两轴；未来新增 cue 轴（如 #10 的「线感/阻力」若正文确认）走新规格/新批次，不是作者在 config 内自行扩充。
- 发现任何机制侧问题将登记 `UPSTREAM_CHANGE_EVENT` 退回，不在本包内改机制。

## 8. 来源 provenance 链

| 环节 | 出处 |
|---|---|
| K8 缺口判定 + 本批列级规格 | `outputs/coverage_delta_r1/report.md` §2.3（Response 面——唯一实质缺口）、§5 建议 1、§6.2（#10/#47 需正文子备注）；47 条判定全表见同文 §3 |
| 独立验收（规格输入已审） | REP-COVERAGE-DELTA-REV-001（内容零错；breaker 映射核对一致——report 头部记载；本批由 Coordinator 确认三层闭合） |
| #47 电轴前提闭合 | `outputs/batches/FISH-R05-FR3-001R`：CD-R05-01「K8 电轴前提确认成立」，FR3 Packet CLOSED（Packet 3d7a4137d236812a9b97dbb862f7248c），「下一步：K8 Cue 轴批次立项（worker）」 |
| §17.2 表结构 / 算子标注 / §17.3 伪脚本 / §17.5 模板计数 / §5.1 Grammar V1–V4 | live Stress Test R1 主页本地转录（REP-CLARITY-FIX-001 后版本，2026-09-10；`tmp/live_stress_main_after.md`）——SNAPSHOT_ONLY，未 re-fetch |
| P0 阶 / §15.6 指标 / §16.5 判据 / §16.7 数学不冻结 | `outputs/batches/KNIFE-READ-001.md`（Summer Knife R0 归档，page_last_edited 2026-09-10T03:49:56Z） |
| 工件形态与 validator 模式 | `outputs/usable_forage_contract_r0/`（FORAGE-CONTRACT-REP-001 R1 修复轮） |

BATCH_ID: REP-CUE-AXIS-001

---

## 附录：验收与修复记录（2026-09-11）

- **REP-CUE-AXIS-REV-001**：ARTIFACT_APPROVE（五 minor：F1' 英文词干转义面缺口/F2' 主动放电自名族无词法条目/F3' fact_semantics 未钉/F4' Notion 镜像 schema 失真/F5' 镜像 provenance 领先本地）。
- F1'-F3' 已修入 validate_config.py（英文面加 \uXXXX 解码面=zh 三面镜像；discharg/electrogen/放电 入表；fact_semantics 钉死含 forage R1 F2 先例注）；自测 69 例全过（2 例改 zh-in-note / co-fire 期望）。
- F4' 镜像 §2 schema 已勘误（7 键）；F5' 本地 README 特此补记：**R07 FR3 CD-R07-01 被动电感知双例（白斑角鲨+棘背钝头鳐）已并入本轴 K8**（FISH-R07-FR3-001 Packet 3d7a4137d236814d90e7f882fef36168），与 CD-R05-01 发电端构成同轴双向语义。
- 源码 guard_violations 现为英文双面（raw+unescaped）+中文三面（walked+raw+unescaped）。
