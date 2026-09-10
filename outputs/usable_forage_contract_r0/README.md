# UsableForageAvailability 契约表达 R1｜Config 主路径 + Narrow DSL 对照

`Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED`

| 项 | 值 |
|---|---|
| 批次 | FORAGE-CONTRACT-REP-001（B2 REPRESENTATION_REVIEW_RUNNING，**R1 修复轮**；按 Coordinator 指令在 r0 交付包目录内就地升级，目录名保留 `usable_forage_contract_r0`，工件版本串升 `r1`） |
| 角色 | fcf-representation-worker |
| 输入来源 | (1) Design Owner 经 Coordinator 批准的契约边界（handoff 原文，原样执行）；(2) 机制背景：KNIFE-READ-001 §16 / §15.2 / §15.6 / §15.7（Summer Knife R0 页 live 读取归档版，page_last_edited 2026-09-10T03:49:56Z；**本批未 re-fetch live**，若该页此后被编辑，本包引用以归档版为准）；(3) FORAGE-CONTRACT-REV-001 review verdict（F1–F6，经 Coordinator 转达） |
| 对应执行面 | **Bake**（事实生产：从同一份 Resolved Snapshot 产出 `usable_forage_availability`）。Response 面（Fish 因子对该事实做 unary profile lookup）在本契约**之外**，仅作为下游消费者提及 |
| 数值状态 | 全部数值（代表尺寸、size 窗、snapshot 键名）为示例占位，**不冻结**；本包只交付表达边界 |
| 版本历史 | r0（2026-09-10，B0 首轮交付）→ **R1**（2026-09-10，FORAGE-CONTRACT-REV-001 F1–F6 处置；逐项对照见 §7） |

## 1. 契约陈述

**UsableForageAvailability** 回答且只回答一个问题：**某个 species-population 在某个格子里，有多少「食谱之内、口径之内」的食物在场**。它把三样东西吸收成一个 Bake 输入事实：prey field（猎物场在该格子的原始生物量，直接来自 Resolved Snapshot，**未经任何感知 / 可见性 / 捕获 / 口径修正**——R1 起由机器可读字段 `contract.prey_field_semantics = "raw_biomass_uncorrected"` 声明并由 validator 强制）、diet eligibility（该 population 的食性是否包含该 prey class）、size eligibility（该 prey class 的代表尺寸是否落在该 population 的口径窗内）。它是一个纯事实，**不携带任何「值得进入 / 值得追捕」的决策**——这正是从 ForageOpportunity 收紧改名的原因：Bake 输入只交付事实，机会判断留给下游 Response 面。

```
UsableForageAvailability(population, cell)
  = Σ  biomass(c, cell)
    over c ∈ BoundPreyClasses        （prey field 绑定表）
    where c ∈ diet_classes(population)                        （食性过滤）
      and min_mm(population) ≤ representative_size_mm(c)      （口径过滤）
      and representative_size_mm(c) ≤ max_mm(population)
```

其中 `biomass(c, cell)` 只从**同一份 Resolved Snapshot** 的**原始 prey 事实族**读取；聚合形状 `FILTERED_SUM` 是契约常量，不是作者可选项。

本契约**不决定**：该格子的食物值不值得去（Response / motive）、能不能被发现（感知面）、追不追得上 / 吃不吃得到（Encounter / Conversion）、吃到的净能量是多少（Functional / Resolver）。

## 2. 吸收 / 排除边界表

### 吸收（且仅吸收）

| 吸收项 | 在 Config 中的落点 |
|---|---|
| prey field（猎物场原始生物量） | `prey_fields[]`：per prey class 的快照绑定（`snapshot_key` 强制 `resolved_snapshot.` 前缀 + **原始事实族 allowlist**，R1 新增） |
| diet eligibility（食性过滤） | `population_eligibility[].diet_classes`（允许空列表，见下方「零重叠」声明） |
| size eligibility（口径过滤） | `population_eligibility[].size_window_mm {min, max}` + `prey_fields[].representative_size_mm` |
| 组合 | `fixed_combine = FILTERED_SUM`（常量，`author_selectable=false`） |

### 零重叠的显式表达（R1 / F5）

`diet_classes: []`（空列表）= 该 population 的食谱与 `prey_fields` 绑定范围**零重叠**：契约仍为该 population 产出事实，值为 0。这与该 population 行**整行不存在**（= 该 population 不在本契约覆盖范围、下游拿不到 `usable_forage_availability` 输入）语义不同，validator 对两者区别对待（空列表合法，整表缺席不合法——`population_eligibility` 本身必须非空）。

### 排除（各归其 owner；禁止在本契约任何输入 / 键 / 注释中作为语义出现）

| 被排除语义 | Owner | 若渗入本契约，会双重结算什么 |
|---|---|---|
| CoverComplexity、refuge / shelter / 隐蔽 / ambush / structure / safety / risk | Cover 因子 | 同一份结构植被原因会在 Cover 因子加一次、在 forage 里再加一次——高结构格子的栖息价值被乘两次 |
| visibility、detectability、perception、reach、conspicuity、turbidity（光学/感知可见性） | 光学 / 感知面 | 同一水色 / 光照原因在感知面结一次、在 forage 里再结一次——清水格子的食物量被重复放大 |
| capture advantage、capture success、catch、grasp、encounter | Encounter / Conversion | 「在场的可吃生物量」被提前按捕获优势 / 捕获概率折算，Encounter / Conversion 再折一次——同一次捕获过程被折价两次 |
| attack geometry | Encounter | 同一空间几何原因（如 ambush 角度）在 Encounter 结一次、在 forage 里再结一次 |
| energetic cost、handling cost | Functional / Resolver | 获取成本在 forage 里预扣一次、Functional / Resolver 再扣一次——净能量收益被双扣 |

### 排除语义的词法代理（guard）

`config/validate_config.py` 的 GUARD 检查族对配置**全文（键+值）**做 fail-closed 双表扫描：**英文词干表**（token 级前缀匹配，camelCase 拆分，25 条）+ **中文关键词表**（子串检查，18 条，检查面覆盖键、值、原文与 `\uXXXX` 转义解码面——JSON 转义不能走私中文）。

**这是语义排除承诺的词法近似，不是承诺本身。** 残余风险声明：同义词表按 review 点名的族列示，不可能穷尽全部同义与婉曲表达——未列入词表的英文同义词、未列入的中文措辞、其它语言 / 拼音 / 完全同义的重命名键都会漏过；词表维护义务 = 发现漏网即扩充词表并重跑 §5 验证。词法代理刻意从宽（前缀 / 子串匹配会产生与语义无关的误报，如英文 see- 词族、中文单字「藏」的任何复合词），因为本契约没有任何合法内容需要这些词族。

排除项命名只出现在**本 README 边界表与守卫实现（validator 源码）**中；config 与 dsl 两个契约工件本身不含排除语义的任何词干 / 关键词（dsl 的 L_observed 元注释用「表达开销」而非「表达成本」，即为此约束的落点）。

## 3. 与 Knife §16 / §15.2 声明的对照

| Knife 声明的机制约束（KNIFE-READ-001 转述） | 本表达的落点 | 在哪里强制 |
|---|---|---|
| Bake 因子只读同一份 Resolved Snapshot | `contract.input_scope = "resolved_snapshot_only"`；每条 `snapshot_key` 强制前缀 | validator `SNAP`（配置层代理；运行层强制在 engine，本包不声称覆盖） |
| Factor 不读 Factor 输出 | `snapshot_key` 前缀检查同时拒绝 `factor.*.output` 类来源（自测用例已覆盖） | validator `SNAP` |
| prey field 是原始（未经修正）生物量 | `contract.prey_field_semantics = "raw_biomass_uncorrected"`（机器可读声明）+ 快照事实族 allowlist + 修正词干（perceiv/percep/visib/adjust/correct）键级拒绝 | validator `STRUCT` + `SNAP`（R1 / F2 新增） |
| 无作者可编辑的中间依赖 | 顶层字段白名单（`schema_version / instance / contract / prey_fields / population_eligibility / fixed_combine`），不存在 steps / depends_on 类段落 | validator `TOP` |
| 表行结构固定（防行内键注入） | `prey_fields` 行 / `population_eligibility` 行 / `size_window_mm` 行键集固定，白名单外键 fail | validator `STRUCT`（R1 / F3 新增） |
| 组合只允许 Fixed Combine | `fixed_combine.operator = "FILTERED_SUM"` 常量 + `author_selectable = false` | validator `COMBINE` |
| 排除语义不得渗入 | 英文词干 + 中文关键词双表全文守卫（词法代理，见 §2 声明） | validator `GUARD` |
| prey classes 与 eligibility 引用一致 | `diet_classes ⊆ prey_fields 绑定的 prey_class`（空列表合法 = 零重叠）；尺寸窗 `min < max`；求和单位同质 | validator `STRUCT` |
| （本包自加）数值不冻结 | `instance.note` 显式声明占位 | 文档层 |

## 4. 交付文件

| 文件 | 执行面 | 输入来源 | 使用 / 放弃的自由度 |
|---|---|---|---|
| `config/usable_forage.config.json` | Bake（事实生产） | 批准边界 + KNIFE-READ-001 §16 + REV-001 F2 | 使用：字段命名、prey class 分类粒度（4 类）、每类单代表尺寸标量、per-population 表、`prey_field_semantics` 声明值。放弃：聚合算子可选性（钉死 FILTERED_SUM）、软尺寸窗（渐变归 Response 的 unary profile）、per-cell 覆写、任何交互项、能量/热量加权（纯生物量）、修正后 prey 口径（钉死 raw） |
| `config/validate_config.py` | Bake（表达验证） | 同上 + §15.2 + REV-001 F1/F2/F3/F5 | 使用：词干 / 中文关键词表选取、事实族 allowlist 模式设计（占位键自洽）、行级键集固定、检查族划分。放弃：无（校验器不引入语义） |
| `dsl/usable_forage.dsl.txt` | 对照（NOT ADMITTED — comparison / L_observed only） | 同上 + Knife §5 Option C 表达式风格 | 使用：表达式形状。放弃：不把它当契约输入（不声明键 / 绑定 / 新语义） |
| `accounting.md` | 记账（跨面） | 同上 + §15.6 / §15.7 + REV-001 F4 | 见该文件 |
| `README.md`（本文件） | 边界文档 | 同上 + REV-001 verdict | — |

## 5. 验证记录（命令与输出原样）

命令 1——真实配置校验（R1 后重跑）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/usable_forage_contract_r0/config/validate_config.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/usable_forage_contract_r0/config/usable_forage.config.json"

== A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/usable_forage_contract_r0/config/usable_forage.config.json ==
[OK]   TOP    no author-invented top-level sections (no intermediate-dependency surface)
[OK]   STRUCT structure + referential consistency (fixed row schemas, diet refs, windows, homogeneous units, prey_field_semantics declared)
[OK]   SNAP   snapshot-only sourcing + raw fact-family allowlist (no Factor output, no correction-semantics key)
[OK]   COMBINE fixed combine constant FILTERED_SUM, author_selectable=false
[OK]   GUARD  no excluded semantic stem or zh keyword in any key or value (stems: cover, refuge, shelter, hid, ambush, structur, safe, risk, conceal, visib, detectab, perceiv, percep, reach, conspicu, turbid, see, captur, catch, grasp, encounter, energ, cost, handl, geometr; zh keywords: 18, table in source)
== result ==
PASS (5 check families, 0 violations)
EXIT=0
```

命令 2——守卫 / 检查族自测（R1 后重跑；证明每个检查族、**每一条英文词干、每一条中文关键词**真的会对坏输入触发——词表条目拼错会静默失效，逐条 probe 是词表自身的质量门）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/usable_forage_contract_r0/config/validate_config.py" --selftest

== selftest ==
[OK  ] baseline fixture passes unchanged
[OK  ] zero-overlap population (empty diet_classes) is a legal explicit row
[OK  ] raw_ prefixed fact family passes the snapshot allowlist
[OK  ] GUARD fires on stem 'ambush' (probe 'ambush')
[OK  ] GUARD fires on stem 'captur' (probe 'capture')
[OK  ] GUARD fires on stem 'catch' (probe 'catches')
[OK  ] GUARD fires on stem 'conceal' (probe 'concealment')
[OK  ] GUARD fires on stem 'conspicu' (probe 'conspicuous')
[OK  ] GUARD fires on stem 'cost' (probe 'costly')
[OK  ] GUARD fires on stem 'cover' (probe 'cover')
[OK  ] GUARD fires on stem 'detectab' (probe 'detectable')
[OK  ] GUARD fires on stem 'encounter' (probe 'encounter')
[OK  ] GUARD fires on stem 'energ' (probe 'energy')
[OK  ] GUARD fires on stem 'geometr' (probe 'geometry')
[OK  ] GUARD fires on stem 'grasp' (probe 'grasp')
[OK  ] GUARD fires on stem 'handl' (probe 'handling')
[OK  ] GUARD fires on stem 'hid' (probe 'hidden')
[OK  ] GUARD fires on stem 'perceiv' (probe 'perceived')
[OK  ] GUARD fires on stem 'percep' (probe 'perception')
[OK  ] GUARD fires on stem 'reach' (probe 'reachable')
[OK  ] GUARD fires on stem 'refuge' (probe 'refuge')
[OK  ] GUARD fires on stem 'risk' (probe 'risk')
[OK  ] GUARD fires on stem 'safe' (probe 'safety')
[OK  ] GUARD fires on stem 'see' (probe 'seen')
[OK  ] GUARD fires on stem 'shelter' (probe 'shelter')
[OK  ] GUARD fires on stem 'structur' (probe 'structure')
[OK  ] GUARD fires on stem 'turbid' (probe 'turbidity')
[OK  ] GUARD fires on stem 'visib' (probe 'visible')
[OK  ] GUARD fires on zh keyword '躲避'
[OK  ] GUARD fires on zh keyword '藏匿'
[OK  ] GUARD fires on zh keyword '庇护所'
[OK  ] GUARD fires on zh keyword '掩体'
[OK  ] GUARD fires on zh keyword '结构'
[OK  ] GUARD fires on zh keyword '安全'
[OK  ] GUARD fires on zh keyword '风险'
[OK  ] GUARD fires on zh keyword '埋伏'
[OK  ] GUARD fires on zh keyword '可见'
[OK  ] GUARD fires on zh keyword '察觉'
[OK  ] GUARD fires on zh keyword '感知'
[OK  ] GUARD fires on zh keyword '修正'
[OK  ] GUARD fires on zh keyword '浑浊'
[OK  ] GUARD fires on zh keyword '抓捕'
[OK  ] GUARD fires on zh keyword '捕获'
[OK  ] GUARD fires on zh keyword '遭遇'
[OK  ] GUARD fires on zh keyword '代价'
[OK  ] GUARD fires on zh keyword '成本'
[OK  ] GUARD fires on key with cover stem (snake_case; row allowlist co-fires)
[OK  ] GUARD fires on value with visib stem
[OK  ] GUARD fires on camelCase token (CoverComplexity)
[OK  ] GUARD fires on captur stem inside combine rule text
[OK  ] GUARD fires on geometr stem in a value
[OK  ] GUARD fires on energ stem in a key (row allowlist co-fires)
[OK  ] STRUCT fires on unknown key inside a prey_fields row
[OK  ] STRUCT fires on unknown key inside an eligibility row
[OK  ] STRUCT fires on unknown key inside size_window_mm
[OK  ] STRUCT fires on prey_field_semantics drift
[OK  ] STRUCT fires on missing prey_field_semantics
[OK  ] STRUCT fires on diet class not bound in prey_fields
[OK  ] STRUCT fires on inverted size window (min >= max)
[OK  ] STRUCT fires on heterogeneous units
[OK  ] SNAP fires on correction-semantics stem in a snapshot key (GUARD perceiv co-fires)
[OK  ] SNAP fires on correction-semantics stem 'correct' in a snapshot key (key-level only, not in the global guard table)
[OK  ] SNAP fires on fact segment outside the allowed raw-prey family
[OK  ] SNAP fires on Factor-output sourcing
[OK  ] COMBINE fires on author-chosen operator
[OK  ] TOP fires on author-invented steps section
== result ==
SELFTEST PASS (66 cases)
EXIT=0
```

### 守卫词表（词法代理表，完整列示）

英文词干 `EXCLUDED_SEMANTIC_STEMS`（25 条，token 级 fail-closed 前缀匹配，camelCase 拆分后 `cover_x` / `CoverX` / `coverX` / `visible` / `energy_density` 全落网）：

| 排除族 | 词干 |
|---|---|
| cover | cover, refuge, shelter, hid, ambush, structur, safe, risk, conceal |
| visibility | visib, detectab, perceiv, percep, reach, conspicu, turbid, see |
| capture | captur, catch, grasp, encounter |
| energetic | energ, cost, handl |
| attack geometry | geometr |

词干 `perceiv` 与 `percep` **必须并列**：`perceived = perce+iv…` 而 `perception = perce+p…`，单取其一必漏一支（selftest 各有独立 probe）。

中文关键词 `EXCLUDED_SEMANTIC_ZH`（18 条，对键 + 值 + 原文 + `\uXXXX` 解码面做子串检查）：

| 排除族 | 关键词 |
|---|---|
| cover | 躲避, 藏, 庇护, 掩体, 结构, 安全, 风险, 埋伏 |
| visibility / 修正 | 可见, 察觉, 感知, 修正, 浑浊 |
| capture | 抓, 捕获, 遭遇 |
| energetic | 代价, 成本 |

**残余风险声明（与 §2 一致）**：以上双表是语义排除承诺的**词法近似**，不是承诺本身——同义词表不可能穷尽（未列入的英文同义词、未列入的中文措辞、其它语言、拼音、完全同义的重命名键都会漏过）；发现漏网即扩充词表并重跑本节验证。误报方向（英文 see- 词族、中文单字「藏」的复合词）已被 fail-closed 设计接受。

### SNAP 事实族 allowlist（R1 / F2）

```
^resolved_snapshot\.(raw_)?prey(_biomass)?(_density)?\.[a-z0-9_]+$
```

键级修正词干（出现即 SNAP fail）：`perceiv, percep, visib, adjust, correct`。其中 perceiv/visib 与 GUARD 全文表重叠（纵深防御，SNAP 侧给出键级精确报错），adjust/correct 为键级特有。

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器为纯标准库，任何 Python 3 均可运行（内部强制 stdout 为 UTF-8，与控制台代码页无关）。

## 6. 边界声明

- 本包只做 UsableForageAvailability 一个契约；不铺 15 Case，不改 `fcf_v1/`，不动 `outputs/fcf_authoring_concrete_r2/`（密封包），不 commit。
- 表达验证通过 ≠ 机制 promotion ≠ Freeze；本包不覆盖 Knife 页任何 Verdict，也不覆盖 FORAGE-CONTRACT-REV-001 之外的新语义。
- snapshot 键名（`resolved_snapshot.prey_biomass_density.*`）为占位：真实 Resolved Snapshot 键表不在本批输入内，交付物是声明式绑定结构，不是键名本身。**R1 起的收窄义务（F2）：真实键表到达后，SNAP 事实族 allowlist 必须随之收窄**为对真实原始 prey 事实族的精确匹配（并保持对 `perceived/visible/adjusted/corrected` 修正词干的键级拒绝）；收窄后的引用侧由 STRUCT 检查兜住（`diet_classes ⊆ prey_fields` 绑定一致性 + 修正语义键 fail + `prey_field_semantics` 声明）。届时本条更新为真实键表引用。
- 发现任何机制侧问题将登记 `UPSTREAM_CHANGE_EVENT` 退回，不在本包内改机制。

## 7. FORAGE-CONTRACT-REV-001 逐项处置对照（R1）

| Finding | 级别 | 处置内容 | 落点 |
|---|---|---|---|
| F1 GUARD 词干表同义词洞 + 非 ASCII 盲区 | blocker | 英文词干表 5→25 条，覆盖 review 点名全部族（cover: refuge/shelter/hid/ambush/structur/safe/risk/conceal；visibility: detectab/perceiv+percep/reach/conspicu/turbid/see；capture: catch/grasp/encounter；energetic: cost/handl）；新增中文关键词表 18 条，对键+值+原文（含 `\uXXXX` 解码面）做子串检查；README §2/§5 措辞由「排除可执行化 / 宁误报不漏报」降级为「词法代理 + 残余风险声明」；selftest 为每条英文词干、每条中文关键词各补 1 触发用例（25+18，另加 2 条结构走私双族用例） | `config/validate_config.py`（EXCLUDED_SEMANTIC_STEMS / EXCLUDED_SEMANTIC_ZH / guard_violations / _walk_strings / _unescape_u / selftest）；`README.md` §2/§5 |
| F2 prey field 原始性不变量 | blocker | config contract 段新增机器可读 `prey_field_semantics: "raw_biomass_uncorrected"`（STRUCT 强制等于该值）；SNAP 新增事实族 allowlist（`^resolved_snapshot\.(raw_)?prey(_biomass)?(_density)?\.[a-z0-9_]+$`，按占位键命名自洽设计）+ 键级修正词干拒绝（perceiv/percep/visib/adjust/correct 出现即 fail）；README §6 补真实键表到达后的 allowlist 收窄义务（STRUCT 引用检查兜住） | `config/usable_forage.config.json`（contract 段 +1 字段）；`config/validate_config.py`（CORRECTION_SEMANTIC_STEMS / SNAPSHOT_FACT_ALLOWLIST / STRUCT prey_field_semantics 检查）；`README.md` §3/§5/§6 |
| F3 嵌套行内键注入 | minor | prey_fields 行、population_eligibility 行、size_window_mm 行键集固定（白名单外键 STRUCT fail）；selftest 中 2 个受影响 GUARD 用例的期望由单族改为双族 {GUARD, STRUCT} 并在用例名标注 co-fire，另补 3 个行级白名单单族用例 | `config/validate_config.py`（ALLOWED_PREY_FIELD_KEYS / ALLOWED_ELIGIBILITY_KEYS / ALLOWED_WINDOW_KEYS / _check_row_keys）；selftest 期望更新 |
| F4 accounting 输入侧义务 + external gate 标注 | minor | 新增「输入侧义务」小节：契约对上游 Snapshot 施加 N_prey_classes × N_cells 字段量义务（示例 4 × N_cells），且义务是**原始口径**（raw，修正口径键 fail）；「不新增 Logic Signature」处标注 external gate——依赖未展开的 §15.7 边界页（3d6a4137d23681049e3dc602d9e784c4），主张待后续批次裁决 | `accounting.md`（§2b 新小节 + §3.1 标注） |
| F5 允许空 diet_classes | minor | validator 停止强制 `diet_classes` 非空（保留 list 类型 / 去重 / 引用一致检查）；README §2 声明「零重叠 = 空 diet_classes 显式表达（事实产出、值 0），与整行不存在（population 不在覆盖范围、不产出事实）语义不同」；selftest 补正例 | `config/validate_config.py`（STRUCT diet 检查）；`README.md` §2；selftest 正例 |
| F6 README §2 措辞 | minor | 措辞改为「排除项命名只出现在 README 边界表与守卫实现中，config 与 dsl 工件本身干净」；为使该声明在中文关键词子串级严格成立，dsl 元注释的「表达成本」改为「表达开销」（2 处） | `README.md` §2；`dsl/usable_forage.dsl.txt`（L10 / L45） |

R1 修复过程自查记录：修复中发现并改正 2 个自引入缺陷——(a) selftest 族比较 list vs set 恒 False（回归）；(b) 词干最初误用单一 `percep`，`perceived`（perce+iv）不命中，遂按 `perceiv`/`percep` 双词干修正（reviewer 点名 `perceiv` 为准）。两处修正后全部用例通过，验证输出见 §5。
