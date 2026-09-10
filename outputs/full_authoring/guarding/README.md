# Guarding 系（P04 全样本）四面生产级表达交付包｜REP-FULL-GUARD-001

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 批次 | REP-FULL-GUARD-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 1 批：Guarding 系） |
| 输入 | (1) 基准样板＝live Stress Test R1 主页转录（例 1 护巢鱼 + Grammar 5.1 V1–V4/W1–W3/R1–R2 变体声明 + §7 Share 契约 + §8.8 结构性关闭 + §11.2 BA-T2 泛化 + §12 Quality 样板 + §13.1 类型化状态枚举 + §13.3 R-T1/R-T2 + §15.x M0/M1 逐面样板 + §17 Reaction）；`programaticHitFish/tmp/live_stress_main_after.md`（2026-09-10 版）(2) `outputs/cue_axis_r1/`（cue 轴规格——本批电鳗 NormalFeeding 面消费）(3) `outputs/usable_forage_contract_r0/`（契约表达样板）(4) census 归档 `fish_logic_census/batches/CENSUS-B0/B1`（GUARD_CONFLICT_DUAL_PATH_RESPONSE 族四成员快照）(5) 15-Case C06/C07 冻结故事（outputs/fcf_authoring_concrete_r2）(6) R05–R09 FR3 triage 摘要（tmp/triage_r05…r09）(7) REP-COVERAGE-DELTA-001 判定（#3/#16/#22/#26 等）(8) fish-reference-20260908.csv（物种身份/习性方向锚） |
| 基线 | **SNAPSHOT_ONLY**——Notion MCP 工具在本执行环境不可用（Story DB live 未访问），全部输入为本地归档/转录/快照；live 漂移时以本 README 引用的归档版为准 |
| 交付物 | `species/*.md` 20 文件（每鱼四面：Group Routing 三件套 + Bake 配置/伪脚本 + Response 配置/伪脚本 + Quality 绑定/伪脚本）+ 本 README + `validate_guarding.py` 结构校验器 |
| 数值状态 | 全部阈值/窗口/结构集合成员/份额为 **@参数引用**（生产数值由 Profile 层定值，不冻结）；全部合并算子数学 **OPERATOR UNDEFINED**（照 live §15.3 / 例 3 先例占位声明） |

## 1. 样本口径（P04 全样本＝20 文件 / 21 条 Story）

P04＝Persistent Guard Condition + Relation → RelationalConflict（FR Semantic Pattern Registry，页 3d6a4137d23681dd8804d14893ed7701）。本批收录全部本地快照可证的 P04 / P04 语义 Story：

| # | 文件 | 鱼（学名） | Story | P04 护巢变体 | 证据档 | Group 条件原子数 | Bake（Guard / Normal） | Response（Guard / Normal） |
|---|---|---|---|---|---|---|---|---|
| 1 | bluegill.md | 蓝鳃太阳鱼（Lepomis macrochirus） | C06（+B01-S39 相邻摄食故事） | 殖民地巢群·部分雄鱼守巢 | A | 3 | BA-GUARD-ANCHOR-GATE / BA-T1 | Defense-only / R-T1 |
| 2 | smallmouth.md | 小口黑鲈（Micropterus dolomieu） | C07（+B01-S32 相邻摄食故事） | 雄鱼护卵＋护幼两段锚 | A | 4 | BA-GUARD-ANCHOR-GATE（锚切换）/ BA-T1 | Defense-only / R-T1 |
| 3 | oscar.md | 地图鱼（Astronotus ocellatus） | FISH-R05（P01+P04） | 双亲护巢：护卵 3–4 天→迁仔 6–7 天 | A | 3 | BA-GUARD-ANCHOR-GATE+Dominance / BA-T1（静水/结构/猎物） | Defense-only（census DUAL_PATH 分歧登记）/ R-T1 |
| 4 | marble_goby.md | 笋壳鱼（Oxyeleotris marmorata） | FISH-R05 | **退回：本地快照 Pattern=P01（伏击），护巢零证据** | C | — | — | — |
| 5 | lungfish.md | 南美肺鱼（Lepidosiren paradoxa） | FISH-R05（P04 语义映射 MEDIUM） | 雄鱼巢穴守护（血管化腹鳍供氧；WET 限定） | A | 4 | BA-GUARD-ANCHOR-GATE / HARD_GATED 因子组合（水面可达硬门） | Defense-only（强度证据开放）/ R-T1 |
| 6 | electric_eel.md | 电鳗（Electrophorus electricus） | FISH-R05 S6（泡沫巢雄护；FIX-001 补录） | 雄鱼筑泡沫巢护幼 | A | 4 | BA-GUARD-ANCHOR-GATE / BA-EEL-GATED-FACTORS | Defense-only / R-T1+电感知 cue 轴（REP-CUE-AXIS-001） |
| 7 | discus.md | 七彩神仙橙/白（Symphysodon aequifasciatus） | R02-S11 + R02-S12（色型不分裂，一套表达） | 双亲育幼：稚鱼群体表黏液喂养 | A | 4 | BA-GUARD-ANCHOR-GATE（fry 锚）/ BA-T1 | Defense-only / R-T1 |
| 8 | snakehead.md | 乌鳢（Channa argus） | R02-S15 | 伏击↔护幼类型化状态互斥（浮巢稚鱼群） | A | 4 | BA-GUARD-ANCHOR-GATE（fry 锚）/ BA-T1+低光槽 | Defense-only / R-T2 反应主导（coverage #26） |
| 9 | nile_tilapia.md | 罗非鱼（Oreochromis niloticus） | B01-S44 | 雌性口孵（摄食减少 Cap；幼鱼回口归世界侧） | A | 3（无结构原子——口孵无巢） | BA-GUARD-ANCHOR-GATE（退化绑定）/ BA-T1 | **Feeding-with-Cap（R-T1+Cap）**/ R-T2 双通道（例 3 绑定） |
| 10 | red_bellied_piranha.md | 红腹食人鱼（Pygocentrus nattereri） | FISH-R06（P04×3） | 树根护卵（frenzy 判例=不建组） | B | 3 | BA-GUARD-ANCHOR-GATE（root_spawn）/ BA-T1 | Defense-only / R-T1 |
| 11 | wels_catfish.md | 欧洲巨鲶（Silurus glanis） | FISH-R06（P04×3） | 雄鱼洞巢守卵 | B | 3 | BA-GUARD-ANCHOR-GATE（burrow_nest）/ BA-T1 | Defense-only / R-T1 |
| 12 | arapaima.md | 巨骨舌鱼（Arapaima gigas） | FISH-R06（P04×3） | 洪水期雄鱼环护稚鱼群（位相路由+漫滩槽） | B | 5 | BA-GUARD-ANCHOR-GATE（fry+漫滩槽）/ BA-T1 | Defense-only / R-T1 |
| 13 | hornyhead_chub.md | 双点美鱥（Nocomis biguttatus） | FISH-R07 | 石巢筑造+守护（target specificity=Open） | B | 4 | BA-GUARD-ANCHOR-GATE（stone_nest）/ BA-T1 | Defense-only（无特异性形态）/ R-T1 |
| 14 | creek_chub.md | 溪鲦＝黑斑须雅罗鱼（Semotilus atromaculatus） | FISH-R08 | 石巢守护（石巢系第 3 例跨属） | B | 4 | BA-GUARD-ANCHOR-GATE（stone_nest 跨属复用）/ BA-T1 | Defense-only / R-T1 |
| 15 | midas_cichlid.md | 米达斯慈鲷（Amphilophus citrinellus） | FISH-R09（P04×6） | 洞穴顶产卵+守护 | B | 3 | BA-GUARD-ANCHOR-GATE（cave_ceiling_spawn）/ BA-T1 | Defense-only / R-T1 |
| 16 | jaguar_cichlid.md | 淡水石斑（Parachromis managuensis） | FISH-R09（P04×6） | 浊水双亲护幼（浊度=Bake 语境轴） | B | 3 | BA-GUARD-ANCHOR-GATE（nest）+浊度轴 / BA-T1 | Defense-only / R-T1 |
| 17 | peacock_bass.md | 孔雀鲈/Cichla spp.（种级身份待核） | FISH-R09（P04×6） | 双亲护幼两段锚（卵床→稚鱼群） | B | 4 | BA-GUARD-ANCHOR-GATE（锚切换）/ BA-T1 | Defense-only / R-T1 |
| 18 | kissing_gourami.md | 接吻鲷（Helostoma temminckii） | FISH-R09（P04×6） | **骨架占位：护巢形态零本地证据，正文判无护巢关系即撤回** | C | 3（全 @ 占位） | BA-GUARD-ANCHOR-GATE（锚待正文）/ BA-T1 | Defense-only（骨架）/ R-T1 |
| 19 | lumpfish.md | 圆鳍鱼（Cyclopterus lumpus） | FISH-R09（P04×6） | 雄鱼浅水岩礁护卵（「激进」=Profile 值域方向） | B | 3 | BA-GUARD-ANCHOR-GATE（rock_spawn）/ BA-T1 | Defense-only / R-T1 |
| 20 | atka_mackerel.md | 单鳍多线鱼（Pleurogrammus monopterygius） | FISH-R09（P04×6） | 岩缝产卵+胸鳍扇卵 40–45 天（扇卵=premise 证据，不进 Response） | B | 3 | BA-GUARD-ANCHOR-GATE（crevice_spawn）/ BA-T1 | Defense-only / R-T1 |

证据档：A＝本地有该 Story 的全四面判定快照（census stories / 15-Case / coverage 判定）；B＝本地有 triage 批注一行（条件值全 @ 化，结构集合成员/亲鱼组成标 [需正文]）；C＝护巢语义零本地证据（退回或骨架占位）。

### 明确排除项（不属 P04，显式记录）

| 排除项 | 理由 |
|---|---|
| 大口黑鲈（Micropterus salmoides） | Story DB 0 Story（Identity 隔离，FISH-R06-FR2 F-1 复核）；其护巢表达已由 live 基准样板承载（例 1 + §15.3 M1，即本批所有文件的模板来源）——不重复建文件 |
| 毛鳞鱼（R02-S05）、高体鳑鲏（R02-S31） | K4 繁殖/育幼锚聚类成员，但语义=产卵锚（岸滩/蚌床），无 guard relation——P04 不受理（R06 FR3「guard relation 未证实即归属=False FIT」判例） |
| 停食洄游双例（大马哈鱼/美洲西鲱） | R06 FR3 已裁：P05 状态×Response multi-path，**拒 P04** |
| 电鳗 S9 幼成食性切换 | P01 typed 摄食故事；其 typed evaluator 已由本批 electric_eel.md NormalFeeding 面绑定承载 |
| R10 收官批（49 行） | 本地无快照（R09 后下发）；若含 P04 新样本需补批登记，不在本批冒充覆盖 |

## 2. 表达读数（对模板计数的影响）

- **Group Routing**：全部 20 文件落在 G-T1 DECLARATIVE ROUTING VECTOR（§13.1）；条件原子 3–5 个/鱼；规则集全部 R1 单层 AND（无嵌套、无 OR 路径——未出现 G3 型多路径）；Share 契约（§7）逐文件落实（SpecialShareTotal>1 → Validation Error，不静默归一化）。**L_group 无增长。**
- **Bake**：Guard 面 20 文件全部收敛到 **1 个模板**（BA-GUARD-ANCHOR-GATE＝BA-T2 泛化「Parental Guard Anchor Template」，§11.2 MERGE_SUPPORTED 判例的实证）：巢守型（nest 类锚实例 ×11）、育幼型（fry_school ×3）、两段切换（×2）、退化绑定（口孵 ×1）、构建型（stone/foam ×3，巢体存在事实原子）。护巢形态多样性（树根/洞巢/石巢/洞穴顶/岩缝/泡沫/口孵/洪水稚鱼群）**全部由锚实例 + Profile 重绑定承载，零新 BakeTemplate**。Normal 面 BA-T1（+电鳗 HARD_GATED 族成员绑定 + 乌鳢低光槽 + 巨骨舌鱼漫滩槽——均为既有槽位/族实例）。**L_bake_base 无增长。**
- **Response**：Guard 面 19/20 用 Defense-only（RR-DEFENSE-01/§17.5 RR-T2；结构族 R-T1 Channel=Defense；§8.8 结构性关闭由伪脚本「不再评价普通 Feeding」+ Program Binding 验证）；唯一例外罗非鱼 Brooding=Feeding-with-Cap（R-T1+Cap，判定句即「摄食减少」）。Normal 面 R-T1 ×17、R-T2 ×3（乌鳢反应主导 / 罗非双通道）。**Response 结构族仍＝2（R-T1/R-T2），L_response 无增长。**
- **Quality**：全部 QT-1（绑定表形态）；0 个 W1–W3 物种级品质调整表（护巢资格全部由 Eligibility Profile 表达——§12.6「资格与 Response 分开」防双 boost 逐文件落实）。**L_quality 无增长。**
- **新列结构**：零（全部复用 V1/R1/分群结果 5 列/绑定表/例 1C 5 列/字段-值 2 列；无未声明变体——由 validate_guarding.py VARIANT/VARIANT_COLS/STRUCT 族强制）。

## 3. 跨批一致性登记

1. **census ↔ live 表达分歧（显式登记于 oscar/lungfish/electric_eel/discus 四文件 §0）**：census GUARD_CONFLICT_DUAL_PATH_RESPONSE 族（4 成员：地图鱼 canonical HIGH / 肺鱼 MEDIUM / 电鳗 S6 补录 / 七彩神仙 HIGH）的护巢 body 是「食物∥入侵者双路径并行评估 + COMBINE_DUAL_PATH」；live V0 取舍为 Guarding Group 只评 Defense（例 1C）。本批按 live V0 表达；DUAL_PATH 真值与 COMBINE_DUAL_PATH 数学（OPERATOR UNDEFINED）归 census/机制侧，两线 reconciliation 不在本批闭合。
2. **与 R0 四面补齐包的差异**：four-surface-completion-r1 曾记 C06/C07 Bake=明确不适用（当时 Story 为 Response 面故事）；本批按 live §15.3 M1（BA-GUARD-NEST-GATE）生产先例补齐 Guarding Group Bake。这是表达层先例更新（R0 表 Stress 表范围限定），不是机制裁决。
3. **census caveat 原样携带**：肺鱼 LUN→P04 为 census 跨层映射（FR 冻结侧仅 P05，F-9）；电鳗 S6 为非盲补录（bias_declaration 在案）；地图鱼 Bake 因子 unordered / anchor 主导判例 open_semantics 原样保留。
4. **cue 轴消费**：electric_eel.md NormalFeeding 面消费 @ElectroFieldProfile（REP-CUE-AXIS-001 资产），边界（主动放电/远程麻痹归 Encounter/Conversion）随该批声明。

## 4. 退回与登记项（转 Coordinator）

| 项 | 内容 |
|---|---|
| 退回 1（笋壳鱼） | 本地快照 Pattern=P01（伏击），护巢语义零证据；handoff 点名与快照冲突——需 Story DB 行标签或 Story 页正文后补写（marble_goby.md §2） |
| 退回 2（接吻鲷） | 仅名单成员资格，护巢形态零证据；骨架占位可装结构，正文判无护巢关系即撤回（kissing_gourami.md §0 撤回条件） |
| [需正文] 批量项 | Tier B 11 文件的结构集合成员/亲鱼组成/浊度档位/洪水位相成员/Cichla 种级身份/口孵期空间偏好（逐文件 §5 列出）；Story 正文到达后只填 Profile 语义，不改结构 |
| R10 尾批 | 收官批 49 行本地无快照；P04 对账待其归档 |
| 无 UPSTREAM_CHANGE_EVENT | 本批未发现机制侧问题；表达层全部落在既有模板/变体/槽位内 |

## 5. 验证记录（命令与输出原样）

命令（selftest）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/outputs/full_authoring/guarding/validate_guarding.py" --selftest
```

命令（真实交付包校验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/outputs/full_authoring/guarding/validate_guarding.py" \
    "A:/Projs/FCF-Harness-Handoff/outputs/full_authoring/guarding"
```

输出：见下方两个代码块（原样粘贴，未改测试凑通过；首轮真实校验抓出 3 处真实缺陷——arapaima 结构原子遗漏/丢失引用闭合、lungfish 未用清单项、tilapia 清单缺 @ResponseCap——均修复工件而非改校验器）。

### selftest 输出

```
[OK  ] baseline passes unchanged
[OK  ] HEADER fires on missing NOT AUTHORITY
[OK  ] HEADER fires on missing BATCH_ID line
[OK  ] SECTIONS fires on missing Bake section
[OK  ] VARIANT fires on missing V-tag
[OK  ] VARIANT_COLS fires on wrong V1 columns
[OK  ] REFS fires on undeclared condition ref
[OK  ] REFS fires on undeclared ruleset in routing
[OK  ] PROFILES fires on used-but-unlisted token
[OK  ] PROFILES fires on listed-but-unused token
[OK  ] THRESHOLD fires on bare numeric threshold
[OK  ] BAN fires on forbidden phrase
[OK  ] BAN fires on unannotated merge phrase
[OK  ] DEFENSE fires on missing closure phrase
[OK  ] SHARE fires on missing default route
[OK  ] SHARE fires on missing validation block
[OK  ] STRUCT fires on stray table
[OK  ] exempt INSUFFICIENT_LOCAL_EVIDENCE file only needs header markers
== selftest ==
SELFTEST PASS
```

### 真实交付包校验输出

```
[PASS] arapaima.md
[PASS] atka_mackerel.md
[PASS] bluegill.md
[PASS] creek_chub.md
[PASS] discus.md
[PASS] electric_eel.md
[PASS] hornyhead_chub.md
[PASS] jaguar_cichlid.md
[PASS] kissing_gourami.md
[PASS] lumpfish.md
[PASS] lungfish.md
[PASS] marble_goby.md
[PASS] midas_cichlid.md
[PASS] nile_tilapia.md
[PASS] oscar.md
[PASS] peacock_bass.md
[PASS] red_bellied_piranha.md
[PASS] smallmouth.md
[PASS] snakehead.md
[PASS] wels_catfish.md
== result ==
PASS (20 species files, 0 violations)
```

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器纯标准库，内部强制 stdout UTF-8。

## 6. 边界声明

- 本包只做 Guarding 系四面的生产级表达（Config 三件套 + 中文伪脚本完全展开）；表达验证通过 ≠ 机制 promotion ≠ Freeze；不覆盖 live 主页 / census registry 任何 Verdict。
- 全部数值不冻结（@参数引用，Profile 层定值）；全部合并算子数学 OPERATOR UNDEFINED 待机制侧。
- 每文件 §5 记录使用/放弃的自由度（含 Defense/Feeding arbitration 的 live V0 取舍、census 双路径分歧、Suski 2003 禁用项、扇卵/回口/吸盘等行为归属边界）。
- 未 commit（提交由 Coordinator / 用户决定）。

BATCH_ID: REP-FULL-GUARD-001
