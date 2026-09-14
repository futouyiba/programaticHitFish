# BATCH｜REP-WORDING-ALIGN-001（B 系列表达文件语义措辞对齐批）

状态：**WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED** ｜ 停点：**INDEPENDENT_REVIEW_REQUIRED**（不自我批准；本地 commit 不 push，独立审后推）

## 1. 依据与任务

- 语义裁定来源：`fish_logic_census/hrq_decision_log.md`「语义裁定」两节（裁定 1：无合并步——渐进累积，weight = weight × step_fit 逐步乘入；三档＝最喜爱不折损 / 可接受 ×衰减 / 不居留 **×0.01 软出局返回**（非零、仍可参与下游）；绝对排除才显式返 0。裁定 2：B 系列「排除档返回 0 出局」措辞统一对齐）。
- 权威口径：`docs/authoring_work_standards.md` §6.1（§5.1 历史表述已被 §6.1 显式覆盖，本批不改该文档）。
- 任务性质：**机械措辞替换，零结构变更**。用户裁决「无论如何省不了」，即刻执行。

## 2. 范围

- 对象：`outputs/full_authoring/{guarding,grazing,migration,normal,field,normal2,patch}/species/*.md` 全部 213 件中的含伪脚本者。
- 实际修改 **195 文件**；未触碰 18 件（身份核对）：
  - guarding/marble_goby（INSUFFICIENT 退回件，无伪脚本——先例跳过）
  - grazing/giant_barb（grazing 侧撤回骨架，重建件在 field 批——撤回件不修复先例）
  - normal 4 件 BOUNDARY-DECL 无程序面文件（alligator_gar / northern_pike_strike / paddlefish_habituation / rainbow_trout）
  - field 12 件品系 L1-EQUIV 短形（无伪脚本，声明层文件）
- 修改面限定：**Bake 面（§2 配置表+§2.2/§2.4 伪脚本）+ §0 判断顺序行的出局值措辞 + 文尾标记行**。§1（Group Routing）/§3（Response）/§4（Quality）/§5（自由度声明）零改动。

## 3. 三类替换计数（脚本机械执行，计数与改动前后两次全库普查闭合）

### 第一类：早退出局值 → ×0.01 软出局（Bake 面伪脚本 + §0 行）

| 规则 | 形态 | 计数 | 批次分布 |
|---|---|---|---|
| R1a | `返回 0（EARLY_RETURN：…` → `返回 0.01 × weight（EARLY_RETURN ×0.01 软出局：非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；…原因原文保留…）` | 347 | field 36 / grazing 29 / guarding 146 / migration 24 / normal 54 / normal2 46 / patch 12 |
| R1b | `返回 0（EARLY_RETURN）`（三档枚举行内闭括号形态）→ 同上措辞 | 12 | guarding 12 |
| R1c | fence 顺序还原声明 `（返回 0，不进入后续评估）` → `（返回 0.01 × weight，非零、仍可参与下游——语义裁定 1/2[REP-WORDING-ALIGN-001]；不进入后续评估）`（含跨行变体 9 处：行尾「（返回 0，」+下一行「不进入后续评估）」） | 19（单行 10 + 跨行 9） | guarding 19 |
| R6 | §0 判断顺序行 `锚不存在格 EARLY_RETURN 出局（非「返回低值」）` → `锚不存在格 ×0.01 软出局返回（非零）`（任务例句；§0 行仅动此出局值子串，箭头链序与步名零改动） | 19 | guarding 19 |

小计 397 处。

### 第二类：合并步 / 算子占位 → 渐进累积（Bake 面）

| 规则 | 形态 | 计数 | 说明 |
|---|---|---|---|
| R2 | 「第 N 步 合并：/ 合并 …Fit / 算子标注：OPERATOR UNDEFINED — 待机制侧（…）」三行块整块 → `终值：返回 running weight（渐进累积——各步 Fit 已逐步乘入，无独立合并步；原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭——合并数学=逐步乘法）` | 33 块 | guarding 33（第 5 步 30 / 第 6 步 3）；块后「返回 …SpatialDistributionWeight」行保留 |
| R3 | 独立算子标注行 `算子标注：OPERATOR UNDEFINED — 待机制侧（X）` → `算子标注：渐进累积（原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]——B 系列表达口径：合并数学=逐步乘法 weight = weight × step_fit；X）`（原括注 X 保留：census PLAIN/HARD_GATED unordered 族域注记、live §15.3 占位声明出处等） | 62 行 | guarding 4（oscar 加权块 1 + eel/lungfish/oscar §2.4 unordered 形态 3）/ migration 3 / normal 17 / normal2 37 / patch 1 |
| R4a | §2 配置表 `数学 OPERATOR UNDEFINED — 待机制侧` → `数学=渐进累积逐步乘法——原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]` | 19 行 | guarding 19（CombineRule 行；行内 census open_semantics 注记保留） |
| R4b | §2 配置表无长破折号变体 `数学 OPERATOR UNDEFINED 待机制侧` → 同 R4a 文案 | 58 行 | migration 3 / normal 17 / normal2 37 / patch 1 |
| R5 | field 批双破折号变体 `折减合成算子标注：OPERATOR UNDEFINED —— 待机制侧` → `…：渐进累积（原 OPERATOR UNDEFINED 占位经语义裁定 1 关闭[REP-WORDING-ALIGN-001]——折减合成=逐步乘法 weight = weight × step_fit）` | 12 行 | field 12 |

Bake 面（§2）审计串 `OPERATOR UNDEFINED — 待机制侧` 原有 114 处全清（33 合并块内 + R3 62 + R4a 19）；R4b/R5 为不带审计串的同义占位变体，同在 Bake 面，一并对齐（同文件内新旧并存会自相矛盾，违背批目的「语义对齐」——此延伸在本报告显式登记）。

### 第三类：文尾标记

195 文件在「顺序还原修复批次：REP-ORDER-FIX-…」行后新增一行（任务给定文案逐字）：

```
措辞对齐批次：REP-WORDING-ALIGN-001（Bake 面 ×0.01 软出局/无合并步——语义裁定 1/2 落盘；Response/Quality 面与判断顺序零改动）
```

## 4. 审计结果（原样）

### 4.1 正向审计 grep（任务验证 1）

```text
$ grep -rc "返回 0（EARLY_RETURN" .../species/*.md | awk -F: '$2>0' | wc -l
0
$ grep -rEc "第 [0-9]+ 步 合并" .../species/*.md | awk -F: '$2>0'
（无输出＝0）
$ grep -rc "OPERATOR UNDEFINED — 待机制侧" .../species/*.md | awk -F: '$2>0'
outputs/full_authoring/guarding/species/electric_eel.md:1
outputs/full_authoring/guarding/species/nile_tilapia.md:1
outputs/full_authoring/normal/species/paddlefish_electro.md:1
outputs/full_authoring/normal/species/pumpkinseed.md:1
outputs/full_authoring/normal/species/spiny_dogfish.md:1
outputs/full_authoring/normal/species/striped_bass.md:1
outputs/full_authoring/normal/species/thorny_skate.md:1
```

按 section 精确归属（python 审计）：上述 7 处**全部在 §3 Response 面**（R-T2 双通道 MAX 汇总 / FIXED_COMBINE / 双 Feeding Channel 汇总——Response 算子不在语义裁定 1 范围内，任务明确 Response 面不动）。**Bake 面（§2）残留=0**。另：§2 内任意「返回 0」字样宽检=0。

### 4.2 反向审计（防越界，任务验证 2——超额执行为 195 文件全量而非 5 抽查）

`git show HEAD:<file>` 与工作区逐文件比较（行尾规范化后字节级）：

```text
modified species files: 195
violations: 0
```

- §1（条件原子/规则集/分群表）、§3（Response 全部，含 §3.2 伪脚本）、§4（Quality）**字节级零改动**
- §0 行级零改动（唯一例外=R6 目标子串）；§0 各行箭头链 token 序（→ … →）逐一比对全等
- 人眼抽查 5 文件 diff 复核：bluegill（guarding 标准形）/ asp（normal PLAIN COMBINE 块）/ common_chub（migration 受限还原）/ vendace_field（field 折减算子）/ oscar（guarding 加权合并特例）——均仅含预期三类改动

### 4.3 Validator（任务验证 3——零改动，全部既有规则首轮即绿）

```text
guarding:  PASS (20 species files, 0 violations)
grazing:   PASS (11 species files, 0 violations)
migration: PASS (21 species files, 0 violations)
normal:    PASS (60 species files, 0 violations)
field:     PASS (24 species files, 0 violations)
normal2:   PASS (72 species files, 0 violations)
patch:     PASS (5 species files, 0 violations)
normal2 closure_replay.py: PASS（闭合账不受影响）
```

新措辞未误伤任何 BAN/文案规则，无需修工件表述。

## 5. 判定边界登记（本批明确不改的相邻形态，供独立审裁决）

1. **§5 放弃项 191 处**「(2) 合并算子（OPERATOR UNDEFINED…）」等历史自由度记录保留：不在 §2、不含审计串；语义=「当时放弃定义合并数学」（历史记录，同 README §7 历史批次不动先例）。本批文尾标记已声明 Bake 面落盘；若需清理 §5 与新口径的表述差，属独立后续批。
2. **PLAIN/HARD_GATED 受限还原的「出局槽值（excluded——非 EARLY_RETURN）」保留**：语义裁定 1 钉的是「软出局**返回**」形态（return 0.01 × weight）；受限族域 excluded 档**不返回、槽值进 COMBINE**，其槽值是否同样取 0.01 无明文裁决——**OPEN 登记**（槽值数值归 Profile/机制侧；本批不擅自钉死）。
3. **§0 行与 fence 声明中的动作名形态保留**（「无夜行底板=EARLY_RETURN」「/出局 EARLY_RETURN」「排除档=EARLY_RETURN，…」等约 150 处）：无「返回 0」值主张，EARLY_RETURN 作为提前返回动作名在新语义下仍准确；出局值语义由伪脚本返回语句（已改）承载。§0 行链尾「→ 合并」链描述词同理保留（任务：§0 顺序与步名零改动）。
4. **oscar「第 5 步 加权合并」步保留**：Dominance 加权合并是 census 判例结构，吃块替换=改结构（违反禁区「链形/步数零改动」）；仅其算子标注行对齐乘法口径（Dominance 权重读作逐因子乘入系数）。§0 行「→ 加权合并」同理保留。
5. **越界哨兵 8 处不改**：§3 Response 面 7 处（见 4.1）+ §5 walleye_spawn 1 处。
6. `marble_goby`（退回件）等 18 件不适用原因见 §2。

## 6. 并行声明（必读）

**CENSUS-REBUILD-001（RB-1，91 项）正在读取这批文件作证据**——本批只改退出值措辞与合并步表述，§0 判断顺序行 / 链形 / Response 面零改动（反向审计 195/195 机械证实：§0 箭头链 token 序全等、§3 字节级全等），**RB-1 的顺序推导不受影响**；其 manifest 已声明以读取时文本为准。

## 7. 执行方式与 provenance

- 脚本：`tmp/rep_wording_align_001/apply_wording_align.py`（批量替换，幂等键=文尾标记；CRLF/LF 逐文件保留；tmp/ 在 .gitignore——审计由 4.1/4.2 的独立命令复验，不依赖脚本存续）。
- 改动前后各做一次全库形态普查（改前普查计数与 dry-run 计数、实际写入计数三方一致；幂等重跑 195 skipped / 0 modified）。
- commit：见 git log（本批只 add `outputs/full_authoring/` 与本报告；并行批 RB-1 在途文件 `fish_logic_census/` 未纳入）。
- 输入来源：B 系列 7 批表达文件（BATCH_ID 各批 README）；对应执行面：Bake（§2）；自由度取舍：无新增（纯措辞对齐，零结构变更）。
