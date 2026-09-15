# FCF Presentation / Cue Contract Validation Lane

- 契约:R0 `FCF-PC-BASELINE-R0-20260915`(canonical 在 HitFish-Up `docs/baselines/`)+ R1 Addendum `FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16`(本目录镜像,sha256 见 run 报告)
- 实现:`fcf_v1/pc_validation.py` + `pc_validation/`(fixtures / runner / reports / baseline 记录)
- 测试:`tests/test_pc_validation.py`
- 基线:`feature/pc-cue-validation-r1` @ checkpoint commit(见 `pc_validation/baseline.json`)

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
- 不为 DEV 案例编造期望值——fixtures 仅结构骨架,期望值待从中鱼库/推导表回填(DEVSET-REGISTRY-R0 纪律)。

## 运行

```bash
python3 -m pytest -q                              # 全仓回归(含本 lane 测试)
python3 pc_validation/run_lane.py                 # 产出 reports/ JSON+Markdown
python3 pc_validation/run_lane.py --post-regression "<结果>"
```

runner 以 holdout gate 为硬前置:注册表非空或缺 provenance 时拒绝运行。

## Fixture 清单

| 文件 | 内容 | 性质 |
|---|---|---|
| `pc_validation/fixtures/devset_structural_r0.json` | DEV-001..010(R0 §12 十个 presentation 案例)结构骨架 | development;AWAITING_NOTION_BACKFILL |
| `pc_validation/fixtures/lane_selftest_cases.json` | SYN-01..16 验证器自测(含正/负路径) | synthetic;非鱼行为期望 |
| `pc_validation/fixtures/holdout_registry.json` | 封存空注册表 | gate;必须保持空 |

## UNRESOLVED semantic questions(本轮显式挂起)

1. `cue.displacement` summary semantics:net displacement vs path length(A2 PROVISIONAL)。
2. multi-target hypothesis aggregation(R0 §4 OPEN;SYN-01 中 hypotheses 权重字段显式记 `UNRESOLVED_AGGREGATION_OPEN`)。
3. typed target status → ResponseBand 映射(B2:本轮不做)。
4. `CAUSE_JUSTIFIED` 声明的正式载体与审核口径(自审 P2-7,lane 仅要求存在显式声明)。
5. PC-OPEN-01:Notion Current rebase gate 记录 `166 passed / 1 skipped`,本仓同状态实测 `126 passed / 0 failed`;差异未解释,留待 Owner/Reviewer 裁定(可能为不同工作区状态或计入非 pytest smoke)。
6. DEV-S4 边界:R0 §12「等」字覆盖的额外旧设计 story 由 Owner 认定。
7. 度量口径(协议 §6)与 Reviewer 抽查比例(≥20%/≥10)仍是 proposal,未获裁决。

## 明确拒绝发明语义的位置

- DEV fixtures 的 item/rig/technique/期望响应全部留空待回填(`AWAITING_BACKFILL` finding 强制可见);
- `LOCAL_WATER` / `GROUND` 均为合法显式 frame 取值,lane 不替 Owner 选 universal frame(A2);
- SYN fixtures 的数值/字段仅为验证器形状,标注 synthetic,不进入语义;
- 未在任何位置把 R0/R1 的 WORKING/PROPOSAL 项写成已裁决。
