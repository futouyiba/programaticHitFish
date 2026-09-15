# FCF Presentation / Cue Contract Validation Lane

- 契约链:R0 `FCF-PC-BASELINE-R0-20260915` → R1 Addendum `FCF-PC-BASELINE-R1-ADDENDUM-2026-09-16`(historical)→ **R2 Development Review Delta `FCF-PC-BASELINE-R2-20260916`(current,D1–D6)**;canonical 在 HitFish-Up `docs/baselines/`,镜像在本目录(R1 sha256 `5b6f9eff…`,R2 sha256 `e5c7c1e5…`)
- 实现:`fcf_v1/pc_validation.py` + `pc_validation/`(fixtures / runner / reports / baseline 记录)
- 测试:`tests/test_pc_validation.py`(41 个)
- 分支:`feature/pc-cue-validation-r2-clean`,clean parent `9c2beebd`(`fcf-v0-current-contract-rebase`,Design Owner 2026-09-16 指定;`b8bcf77…` 降为 PRIOR_CLEAN_BASELINE_PROVENANCE)

## 当前状态(2026-09-16,R2 执行完毕)

```text
HARNESS_IMPLEMENTATION_READY
DEVELOPMENT_REGRESSION_EXECUTED_UNDER_R2
BLIND_HOLDOUT: 待独立 reviewer PASS + R2 hash 冻结确认后 AUTHORIZED
```

- 9c2 基线实测:**169 passed / 1 skipped(170 collected)**——非沿用 166/1;+3 来自在途会话 post-b8bcf77 commits(vertical_slice 15、editor 8)。inventory 钉在 [baseline.json](../../pc_validation/baseline.json)。
- Post-change 实测:**210 passed / 1 skipped**(169 + 41 PC);未为凑数调测试。

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
