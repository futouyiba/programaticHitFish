# FCF Presentation / Cue Contract Validation Lane

- 契约链:R0 → R1 Addendum(historical)→ R2(冻结)→ **R3 Candidate `FCF-PC-BASELINE-R3-CANDIDATE-20260916`(当前;窄 Delta 1–3)**;canonical 在 HitFish-Up `docs/baselines/`,镜像在本目录(R3 sha256 `fae0af1c…`)
- 实现:`fcf_v1/pc_validation.py` + `pc_validation/`;测试:`tests/test_pc_validation.py`(44 个)
- 分支:`feature/pc-cue-validation-r3-candidate` @ baseline `c412a6e`(R2 approved lane;ancestry → `9c2beebd`)

## 当前状态(2026-09-16,R3 FROZEN)

```text
ROUND1 = HISTORICAL BLIND EVIDENCE(closed)
R3     = WORKING VALIDATION BASELINE(FCF-PC-BASELINE-R3-20260916,FROZEN / NOT PROMOTED;sha256 f68bac2b…)
ROUND2 = NOT_YET_AUTHORIZED(holdout registry SEALED_EMPTY)
```

- Full regression:**215 passed / 1 skipped**(169 Current + 46 PC-specific,真实 inventory)。
- 33-case Development Regression:**COVERED 29 / ANNOTATION_ONLY 3 / NEW_PRIMITIVE_REQUIRED 1(H17)/ UNRESOLVED 0**。
- Freeze 修订(A–F)已应用:`cue.contact_disturbance` 收敛为纯 OrderedBand(无 composite enum、无 surface_ 前缀);`CAUSE_JUSTIFIED` 从契约/validator 移除,double-count 判定改为 cause provenance/identity;`FEEDING_TARGET_TEST_VOCABULARY` 明确为 lane 局部 test vocabulary;`cue.sound_pattern` 状态为 `EXERCISED_BY_DEVELOPMENT_CASE`(非 NECESSITY_VALIDATED);CF-MULTI-1 保持 OPEN_PENDING_EVIDENCE。
- 稳定读取位置:HitFish-Up `docs/baselines/FCF-PC-BASELINE-R3-20260916.md`(canonical)+ 本分支镜像(逐字节一致)。

## R3 三个 delta 的落点

| Delta | 落点 |
|---|---|
| 1 contact disturbance(冻结版) | `cue.contact_disturbance : OrderedBand`(movement → 既有 motion facts;duration → 既有 DurationFact/temporal_scope;无 composite enum;无 surface_ 前缀;`CONTACT_CAUSE_FAMILY` 经 cause provenance/identity 防双计;不恢复 displacement) |
| 2 composition resolver | `check_composition_resolver`(0..N sources;deterministic;identity denylist + `rig_identity`;`source_count/lure_count` NOT_ADMITTED);**CF-MULTI-1 counterfactual**(`counterfactuals.json`,OPEN_PENDING_EVIDENCE)挂起 multiplicity 准入 |
| 3 crab dictionary | `FEEDING_TARGET_TEST_VOCABULARY = {SMALL_BAITFISH, CRUSTACEAN}`(**仅 lane 局部 test vocabulary,非 canonical dictionary**);H14 复用 CRUSTACEAN(COVERED);未知成员(如 CRAB)→ `DICTIONARY_MEMBER_ADMISSION_REQUIRED`;不加值不加维度 |

不准入维持:chemical magnitude / odor concentration(H17 仅 confirmatory)、cue.displacement、strategy tokens、raw source count、new Meaning layer;pressure / cue familiarity 未验证。

## Development Regression(33 cases = 15 原有 + 18 Round 1)

```text
COVERED                29(含 DEV-010 经 Delta 1 关闭;H12/H13 经 Delta 1;H07 经 Delta 2 + counterfactual flag;H14 经 Delta 3 复用)
ANNOTATION_ONLY        3(DEV-003 / S3 / S5 不变)
NEW_PRIMITIVE_REQUIRED 1(H17,chemical magnitude DEFERRED / NOT_ADMITTED;confirmatory only)
UNRESOLVED             0
```

H10 行使 `cue.sound_pattern` → 状态 `EXERCISED_BY_DEVELOPMENT_CASE`(非 NECESSITY_VALIDATED);combined dev set unused basis = 空。

## R2 语义 delta 在 lane 中的落点

| 裁决 | 落点 |
|---|---|
| D1 displacement NOT_ADMITTED | `CUE_BASIS` 移除(12 项);`NOT_ADMITTED_CUES` 常量;vocabulary 级 `NOT_ADMITTED_CUE` violation;依赖它判 COVERED = violation;合法路径 = UNRESOLVED + admission request(SYN-17) |
| D2 DEV-006 重分类 | fixture 改用 admitted cues(flash/direction_change/speed_change/speed)→ **COVERED**;不再因 displacement UNRESOLVED |
| D3 DEV-010 Known Gap | `UNRESOLVED` + flag `KNOWN_DEV_GAP_CONTINUOUS_BOTTOM_CONTACT_MECHANICAL_CAUSE`;report 新增 `known_dev_gap_cases`;不阻塞 holdout;永不做 blind evidence |
| D4 chemical 暂不准入 | DEV-003/DEV-S5 保持 `CHEMICAL_INTENSITY_GAP_WATCH`;candidate extension 不入 core |
| D5 Walleye LINT | flag 更名 `LINT_WATCH_DOUBLE_COUNT`;D5 规则原文入 provenance;无新 primitive |
| D6 sound_pattern | report `unused_basis_cues` 以 `{"cue.sound_pattern": "UNEXERCISED_BY_CURRENT_DEVSET"}` 呈现;不删不证 |

## Development Regression 最终分布(15 案,R2)

```text
COVERED               11  (DEV-001/002/004/005/006/007/008/009, S1, S2, S4)
ANNOTATION_ONLY       3   (DEV-003, S3, S5 — chemical_signature / prey_stage / dictionary member admission)
UNRESOLVED            1   (DEV-010 = KNOWN_DEV_GAP_CONTINUOUS_BOTTOM_CONTACT_MECHANICAL_CAUSE,非阻塞)
```

特别报告(run 报告 `development_regression` 段,自动计算):breaking = 仅 DEV-010(typed known gap);displacement 依赖 = 无(D2 已解除);chemical 缺口 = DEV-003/DEV-S5;ownership watch = DEV-S4;未使用 basis = cue.sound_pattern(UNEXERCISED_BY_CURRENT_DEVSET);Fish×Descriptor resurfacing = DEV fixtures 无 Response rules,不可测(如实标注)。

## 本 lane 验证什么 / 不做什么

验证:A1 边界、A2 框架元数据、A3 表轴、A4 分类协议、B1 签名、B2 typed zero、D1 NOT_ADMITTED、§8 双计、§4 聚合偷渡、holdout SEALED_EMPTY 硬门。
不做:生产 physics/motion resolver、displacement 语义(已 NOT_ADMITTED)、multi-target aggregation、ResponseBand 映射、SET/CAP 终局、挑选/探知 holdout、编造 ResponseBand 数值。

## 运行

```bash
python3 -m pytest -q                               # 全仓(210/1)
python3 pc_validation/run_lane.py                  # 报告(devset_r2_backfilled 优先)
```

## Fixture 清单

| 文件 | 内容 | 性质 |
|---|---|---|
| `devset_r2_backfilled.json` | 15 案(R2 裁决后) | development regression(current) |
| `devset_r1_backfilled.json` / `devset_structural_r0.json` | R1 回填 / 前身 | historical provenance |
| `lane_selftest_cases.json` | SYN-01..17 | synthetic 自测 |
| `holdout_registry.json` | SEALED_EMPTY | gate;必须保持空 |

## UNRESOLVED(不阻塞本轮 Holdout;不得由 Harness 自行闭合)

DEV-010 的 D3 问题(continuous-contact 表达缺口);multi-target aggregation;ResponseBand 数值映射;SET/CAP 终局;`CAUSE_JUSTIFIED` 正式载体;metric spot-check ratio;DEV-S5 物种归属;chemical intensity/odor concentration 准入(D4 条件未满足)。

## 拒绝发明语义的位置

affinity/未定值一律 `UNKNOWN_FROM_SOURCE`;无 ResponseBand 数字;species 不确定不猜;frame 只声明不替 Owner 选;WORKING/PROPOSAL 不写成已裁决;provenance 分支(r1-clean/r1)保留不删。
