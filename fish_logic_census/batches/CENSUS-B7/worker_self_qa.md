# CENSUS-B7 Worker Self-QA（R2 §12）

不冒充独立审；以下为 worker 自检记录。独立审核待 reviewer。

## 1. 计数四方对账（B1 教训）

| 口径 | 值 | 来源 |
|---|---|---|
| merge_tests 条目 | 345 = MC 100 + EXT 9 + NEW 126 + AMB 110 | merge_tests.jsonl 实测 |
| MC 分解 | typed 86 + field 14 | 逐条 verdict 计数 |
| NEW 分解 | CRR 110 单条 + 新族分组 11 + C9 分组 1 + field-vs-typed 分组 1 + guard 跨族分组 2 + SOK2 1 | 同上 |
| 程序×族对 | 1682 = 110+110+110×11+110+86+9+14+14+18+1 | engine_report 各节行数求和 |
| programs | 219（= blind_programs 219，零补录） | programs.jsonl / blind_programs.jsonl |
| stories | 112（= fetch_pairs.tsv 112 行；110 双面 + WBL 仅 Bake + PAD4/SEA1 零程序） | stories.jsonl |
| discovery_curve 行 | `CENSUS-B7,112,219,100,9,0,110,0,0,0,0,0,0,0` | CSV 追加实测 |
| 基线对账 | 295 − 183 = 112（packet 声明逐包核验 + B0-B6 台账去重） | manifest baseline_reconciliation |

- n_merge_confident=100 = 条数级（含 field 14 对 FOOD_FIELD 的 MC）✓
- n_new_template_candidate=0 = distinct 新族数（B7 零新族——全部同构入既有族/挂账）✓ CSV 第 6 列 0 ✓
- n_ambiguous=110 = 程序级 AMB（Bake 全量）✓
- ΔL_group/bake/response/quality 全 0 ✓（零新族零新 resolver）

## 2. 名义账本（pending review 口径）

- TYPED：162 + 86 = 248 pending（B6 后 162）
- FOOD_FIELD_FEEDING_RESPONSE：2 + 14 = 16 pending（B2 立族后首批扩容）
- GUARD：9 EXT 候选（anchor 轴值序第 18-24 新值 7 例 + RSB 复现实证并入
  B6 已提案 mussel_brood + DIS2 与 B1-DIS canonical 既有值 fry_anchor
  [registry 行 255]的色型复用对照——覆盖关系待 HRQ-B7-02 对账；成员序
  =第 20-28 名义成员候选[修复轮 F1/F6 改述：原「vs B5 MDC 跨批复现实证」
  失实，B5 MDC 提案值为 cave_ceiling 非 discus；GUARD 第 4 成员即 B1-DIS
  色型不分裂先例]）
- SINGLE：+110 AMB（四层联动第 4 层：B4 25 + B5 52 + B6 47 + B7 110 = 234）
- registry v8 本体零改动（mutation 归独立审另批——章程）

## 3. 盲纪律

- blind_programs.jsonl 冻结 2026-09-11T13:01:45Z（mtime 精确）；registry 首
  次打开 13:08:45Z–13:08:52Z（run_merge_tests.py 定稿→engine_report 写出，
  B5 F2 区间法）——冻结严格在前 ✓
- 219/219 registry_seen_at_creation=false；program_revisions.jsonl 空 =
  判同段零改动 ✓
- bias_declaration（manifest）：B6 脚本管线+批报告+角色记忆散文的 F-0 类
  暴露如实申报；盲体语汇纪律自查（无 extension/新轴提案语汇——守护对象
  行为事实描述）✓

## 4. 覆盖纪律

- 112/112 story 四面判定（Group/Quality 全 NO_SURFACE_EFFECT 有理由；Bake
  110 + Response 109 程序化；WBL Response=boundary-only NO_SURFACE_EFFECT；
  PAD4/SEA1 零程序顶层 no_surface_reason）✓
- R03/R05 34 story Sweep Log 全解析（S1-S11 各 11 项）；R01/R02/R04 78
  story 无 Sweep Log 节（FR 线该三批无此节——不编造，B1/B2 同范式）✓
- 输入统计三标记实测（32 完整包裹 + 73 前导+包裹 + 7 纯正文 = 112；
  判定定义与分桶规则见 manifest input_channel_note——修复轮 F3 改述，
  原登记 26/73/13 的 13 桶误含 6 份中文前导+包裹文件）✓

## 5. 判同四态纪律

- MC 仅在骨架同构+raw 字面差（typed PREMISE / field OPERATOR+PREMISE）✓
- EXT 仅 guard（三字段齐全+复杂度对比+HRQ）✓
- NEW 全部 engine 真差异（BRANCH/COMBINE/DEPENDENCY/OPERATOR/RETURN 至少
  一项非 PREMISE）✓
- AMB 仅 SINGLE v1 证伪挂账（不 MC 不立族的 B5-① 范式）✓
- 分组条目全部 distinct_diff_sets=1 断言通过（engine 实测）✓
- 族完整性：无 ≥3 成员族 canonical 变更；FOOD_FIELD canonical=B2 物化版
  逐字转写（ir_pointer 不重造）✓

## 6. 已知局限 / 留 review

- SOK2（S29 动机未定）typed MC 占位：与 B3 CHU（STATE_GATED 停食门）语义
  相邻但 story 层证据档不同（动机未定 vs 停食状态明确）——互证 non-match
  记录在案，归类留 review。
- R02-S06 Lake Whitefish（Blocked-by-Identity 行 + FR3 25/25 PASS 范围）：
  消费+Medium 推算注记，合法性挂 HRQ-B7-03。
- R02-S17 vs R04-FGA4 同种双 story（佛罗里达雀鳝）：各自 MC 入 TYPED，去重
  联动注记（story 级输入口径）。
- B0 MGC『FieldFeeding 按 TYPED evaluator_channel 轴』旧处理 vs B7『field
  Response 进 FOOD_FIELD』新口径的追溯一致性——挂 HRQ-B7-03。
- 本批 docstring/print 计数初稿笔误（345 记 346、程序×族对 1463 初稿）
  已修正并重跑产物。【ARTIFACT_REVISE 修复轮 F2 补正：批内自查曾改记
  1683，独立审复核公式求和 110+110+1210+110+86+9+14+14+18+1=1682
  （engine_report 各节行数求和实测一致）——修复轮已全链改 1682（self-QA
  /批报告/生成脚本三处）】

## 7. 验证结果

- validate_batch.py：PASS（programs=219 stories=112 merge_tests=345）
- fixtures：12/12（项目 venv .venv/Scripts/python.exe）
- git：registry/curve 仅 CSV 追加一行；template_registry.yaml 零改动
