# FCF Presentation / Cue Contract Validation Lane

- 契约:R0 `FCF-PC-BASELINE-R0-20260915`(canonical 在 HitFish-Up `docs/baselines/`)+ R1 Addendum `FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16`(本目录镜像,sha256 见 run 报告)
- 实现:`fcf_v1/pc_validation.py` + `pc_validation/`(fixtures / runner / reports / baseline 记录)
- 测试:`tests/test_pc_validation.py`
- 分支:`feature/pc-cue-validation-r1-clean`,clean parent baseline `b8bcf77`(`fcf-v0-current-contract-rebase`,Design Owner 2026-09-16 指定)
- Provenance:`feature/pc-cue-validation-r1@0e4ea3d` 保留为 `WIP_SNAPSHOT_PROVENANCE`,**不是**实验基线

## 当前状态(2026-09-16)

```text
HARNESS_IMPLEMENTATION_READY
DEVELOPMENT_REGRESSION_PENDING   (DEV set 已执行,待 Design Owner review DEV findings)
BLIND_HOLDOUT_NOT_YET_AUTHORIZED
```

- **PC-OPEN-01 = CLOSED_BY_REPRODUCTION**:clean head `b8bcf77` 上 `python3 -m pytest -q` = `166 passed / 1 skipped`(collected 167),与 Current executable evidence 完全一致。此前 WIP 快照的 `126/0` 原因:快照早于在途会话提交的 `tests/harness/`(40 tests,`test_agent_defs.py` 6 + `test_contracts.py` 34);1 skip = `tests/harness/test_agent_defs.py:75`(workspace-root agent deploy dir 不在本机,环境条件跳过)。完整 inventory 见 `pc_validation/baseline.json`。
- origin 分支 tip 已前进到 `9c2beebd`(在途会话另有 10 commits);未被采用,因无 Current 文档指定其为更新 clean head。

## 本 lane 验证什么(结构契约)

| 契约条款 | 验证器 | 说明 |
|---|---|---|
| R0 §2.1 / A1 | `check_fish_independence` | resolver 禁读 species/mode/valuation 类输入;support-relative geometry 合法 |
| R0 §3.2 / A2 | `check_kinematic_metadata` | speed/speed_change/direction_change 必须显式 `reference_frame` + `temporal_scope`;`vertical_motion` 仅 WORLD_VERTICAL;`pause_duration` 为 upstream DurationFact 免框架声明;`cue.displacement` PROVISIONAL |
| R0 §3.2 / §7 / §9 | `check_cue_vocabulary` / `check_presentation_descriptors` | 冻结 basis 之外 token 需 admission;禁用语义字段与 SKU alias 拒绝 |
| R1 A3 / R0 §4 | `check_static_target_affinity` / `check_dynamic_feeding_preference` | StaticTargetAffinity 固定 `Species × FeedingTargetKey`,无 Mode 轴;affinity 不得吞并 motion/drift/flash/vibration quality;dynamic preference 不得复制成 Mode-specific target table |
| R1 B2 | `check_target_resolution` | `NO_SUPPORTED_TARGET` 与 `UNKNOWN / RESOLUTION_INCOMPLETE` typed 区分;非肯定状态不得映射 affinity/ResponseBand |
| R1 B1 | `check_cue_signature` / `cue_signature_identity` | versioned semantic signature;组成仅限 admitted `presentation.* / cue.*`;SKU/ItemId/TechniqueId/category/UI identity 禁入;不同 SKU 解析出同 signature ⇒ 同一 familiarity identity |
| R1 A4 | `check_classification` / `check_derived_descriptor` | primary(唯一)/requested_deltas/flags 记录结构;依赖 displacement 不得判 COVERED;确定性派生只读 admitted fish-independent facts |
| R0 §8 | `check_cause_ownership` | rule 同时消费 derived cue 与其成因 primitive 且无 `CAUSE_JUSTIFIED` 声明 ⇒ CAUSE_OWNERSHIP_CONFLICT |
| R0 §4 OPEN | `check_aggregation_smuggling` | multi-target 聚合(sum/weighted_average/max/Noisy-OR)不得偷渡 |
| R0 §12 | `HoldoutRegistry` | holdout 注册表在本仓必须 SEALED_EMPTY;真实 unseen 案例只能由独立 Reviewer / Sample Agent 带完整 provenance 封存注入 |

## 本 lane 刻意不做(不得暗中闭合)

- 不实现生产级 motion resolver / physics(A2 明确豁免);
- 不裁定 `cue.displacement` 的 net vs path 语义;
- 不实现 multi-target aggregation、ResponseBand 数值映射、SET/CAP 终局(R0 §13);
- 不自行挑选或探知 blind holdout 案例;
- 不编造任何 ResponseBand 数值——DEV regression 只证明事实需求/可表达性/所需 delta/ownership 结果。

## Development Regression(DEV set,已执行待 Owner review)

来源(均为已污染、因此 Development-legal 的旧材料):

1. Presentation Adapter Development Set Manifest v1(frozen 2026-08-25,Notion `3c7a4137d23681b7adc7cafa9f444b6b`);
2. Response Language Contract Delta R0 §14 Expression Pressure Test(2026-09-05,Notion `3d0a4137d2368168b678ccfafc85583c`);
3. R0 §12 枚举 + Design Owner 2026-09-16 裁决(新增 Walleye)。

15 案(DEV-001..010 + DEV-S1 Bass jerk-pause / S2 Bass spawn guard / S3 Trout match hatch / S4 Walleye low-light hydro-acoustic / S5 scent feeder(Carp 归属 UNKNOWN_FROM_SOURCE))。真实分布(run 报告 `development_regression` 段):

```text
COVERED               10
ANNOTATION_ONLY       3   (DEV-003, DEV-S3, DEV-S5 — descriptor/dictionary admission)
UNRESOLVED            2   (DEV-006, DEV-010 — displacement PROVISIONAL;另 DEV-010 scrape setter)
```

特别报告(run 报告自动计算):

- 打穿 R1 baseline 的旧 case:DEV-006(Spoon oscillating,steady↔oscillating 判别依赖 displacement 未决语义)、DEV-010(Soft worm bottom drag,Manifest 本身标注 scrape/displacement unresolved);
- 未被任何 DEV case 使用的 basis 字段:`cue.sound_pattern`;
- displacement 未决语义依赖:DEV-006、DEV-010;
- chemical intensity 缺口暴露:DEV-003、DEV-S5(`cue.chemical_intensity?` 仍为未准入 candidate);
- ownership lint watch:DEV-S4(Walleye,light 与 Exposure/LocalOpportunity 潜在双计,14.1 已记录为 lint 事项);
- Fish×Descriptor resurfacing:DEV fixtures 未含 Response rules,**不可测**——已在报告中如实标注,待 rules 编写后按 R0 §9 监控。

## 运行

```bash
python3 -m pytest -q                               # 全仓回归(含本 lane 测试)
python3 pc_validation/run_lane.py                  # 产出 reports/ JSON+Markdown
python3 pc_validation/run_lane.py --post-regression "<结果>"
```

runner 以 holdout gate 为硬前置;报告分列 Current baseline regression / PC-specific tests / post-change full regression,不报混合总数。

## Fixture 清单

| 文件 | 内容 | 性质 |
|---|---|---|
| `pc_validation/fixtures/devset_r1_backfilled.json` | DEV-001..010 + S1..S5,含 provenance/classification/ownership 期望 | development regression(激活) |
| `pc_validation/fixtures/devset_structural_r0.json` | 回填前的结构骨架 | provenance(已被取代,保留) |
| `pc_validation/fixtures/lane_selftest_cases.json` | SYN-01..16 验证器自测 | synthetic;非鱼行为期望 |
| `pc_validation/fixtures/holdout_registry.json` | 封存空注册表 | gate;必须保持空 |

## UNRESOLVED semantic questions(本轮显式挂起)

1. `cue.displacement` summary semantics:net displacement vs path length(A2 PROVISIONAL;DEV-006/010 阻塞于此)。
2. DEV-010 mechanical-scrape temporal-pattern admission(Manifest:不得由单 case 新增 setter)。
3. multi-target hypothesis aggregation(R0 §4 OPEN)。
4. typed target status → ResponseBand 映射(B2:本轮不做)。
5. `CAUSE_JUSTIFIED` 声明的正式载体与审核口径(自审 P2-7,lane 仅要求存在显式声明)。
6. `cue.chemical_intensity?` / odor concentration 是否需要独立影响 Response(Pressure Test 14.1 保持 optional candidate;DEV-003/S5 已暴露该缺口)。
7. DEV-S5 scent-feeder verdict 的物种归属(Carp 系 R0 §12 记录,14.1 未点名物种)——UNKNOWN_FROM_SOURCE。
8. 度量口径(协议 §6)与 Reviewer 抽查比例(≥20%/≥10)仍是 proposal,未获裁决。
9. origin `fcf-v0-current-contract-rebase` tip `9c2beebd` 是否应成为更新 clean head——待 Current 文档指定。

## 明确拒绝发明语义的位置

- DEV fixtures 的 affinity 数值一律 `UNKNOWN_FROM_SOURCE`;无任何 ResponseBand 数字;
- species 无法从来源确定的(DEV-003/DEV-004/S5)标 `UNKNOWN_FROM_SOURCE`,不猜;
- `LOCAL_WATER` / `GROUND` 均为合法显式 frame 取值,lane 不替 Owner 选 universal frame(A2);DEV-007 的 LOCAL_WATER 是 fixture 级声明;
- 未在任何位置把 R0/R1 的 WORKING/PROPOSAL 项写成已裁决;
- blame-free 迁移:lane 文件逐字迁移自 provenance 分支,未触碰 Current rebase 的任何 authoring/compiler/editor 文件。
