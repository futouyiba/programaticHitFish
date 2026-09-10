# CENSUS-B1 Batch Report｜首个回溯批（B01×13 + FISH-R02×2）

status: **INDEPENDENT_REVIEW_REQUIRED**
validate_batch: **PASS**（programs=24 stories=15 merge_tests=38）

## 输入与纪律

- 输入：coordinator 建议清单 15 条冻结 Story（B01 的 13 条 CoverageDelta Candidate + R02 的 2 条 Compression Candidate：七彩神仙 S11、准白甲鱼 S22）+ P01/P02/P04/P05/P06 冻结语义 Pattern。
- 盲纪律：24 条盲骨架（Bake 9 / Response 15）于 **2026-09-10T13:32:49Z** 冻结（hash 落盘、registry_seen=false、manifest 时序锚定），冻结节点已回信 coordinator（可插入 commit），之后才开 registry v2 判同。零 post-registry 修改。
- B0 教训执行：机制面逐项过（program / 显式排除 / OUT_OF_SCOPE 三选一）：TIL Bake、DIS Bake 等 4 处显式排除；PIK/GAR 取饵后、BLU 吐饵、LAM 陷阱 OUT_OF_SCOPE；S12 白色型作 S11 同构对照不重复建体。
- 选样说明：envelope 15 条上限，七彩神仙取 S11（证据源）建体；R01 的 54 故事形态按 Story 粒度取样未受影响。

## 核心结论

### Registry v2→v3（8 族）

| 族 | B1 变化 | 说明 |
|---|---|---|
| CRR | +9 non-match，仍 0 成员 | **CRR 首考未至**：B1 选样无低温 refuge 类故事（coordinator 预告压力点未触发——选样使然，留 B2+） |
| PLAIN_FACTOR_COMBINE | +BRT（3 成员） | patch+rank_position 2 槽——槽位数伸缩 + **首个个体属性因子**（rank）准入待 HRQ-B1-04；rank fact 产品写回未定（TAR-05） |
| PATCH_RESOURCE_FOLLOWING | +ONS（2 成员） | **预告碰撞点裁决：MERGE**（context_type 轴：zone|current；准白甲鱼急流绑定与湄公鲶底带约束同槽）。双成员均 P06 域，PROVISIONAL 维持（ONS 行为链 Evidence Open，confidence LOW） |
| TYPED_TARGET_RESPONSE | +13（19 成员） | 12 标准（engine 无字面差异）+ PAD34 被动电感受通道（PASSIVE_ELECTROSENSE，对照 B0 电鳗主动电定位）；binding 新实例：口孵 cap / cue_history 输入 / 窄接受 |
| DUAL_PATH | +DIS（4 成员） | 七彩神仙育幼黏液喂养：fry_anchor=幼鱼群；engine 无字面差异；与 Review Context §9.2 判例一致 |
| **SINGLE_FACTOR_NORMALIZED_WEIGHT**（新） | 7 成员 | 单 typed 场/因子→归一化（2 步）：草鱼/黑鼓/鸭嘴鲟幼/小口跟随（patch）+ 鳕鱼深度/蓝鳃水层（habitat 因子）+ 七鳃鳗化学梯度场（最宽实例）。HRQ-B1-01 |
| **CUE_GUIDED_APPROACH_AVOID**（新，PROVISIONAL） | 1 成员 | 七鳃鳗非摄食化学趋向：**evaluand=环境梯度场（非离散目标）+ RETURN=Approach|Avoid（非 TargetFeeding）**——真结构差异不并入 TYPED。关联 Review Context §10 环境场判例（不自动 promote Grammar）；Product Scope Deferred（TAR-06）。HRQ-B1-03 |

### 判例与边界

- **LAM 边界判例**（本批最重要）：同形两步（evaluator→decide）不构成合并证据——evaluand 对象类型（离散目标 vs 环境梯度场）与 RETURN 语义是结构判据（R2 §6 精神的执行）。
- **SINGLE↔PATCH 族间边界**（HRQ-B1-02）：typed context 中间步的存在是业务结构（2 步 vs 3 步真 DEPENDENCY 差异）；extend（optional_context 槽）vs split 交 review，worker 倾向 SPLIT（与 B0 HRQ-03 gate 轴同型，可合并裁决）。
- **阴性样本（虹鳟 RAI）成立**：纯 Profile/参数重绑定，TYPED 标准成员 engine 无字面差异；absence=NO_NEW_PROGRAM_CURRENT_EVIDENCE（scope 限定）。
- Discovery Curve B1：stories=15, sketches=24, merge_confident=23, extension=4, new_template=**2**, ambiguous=0；**ΔL_group=0, ΔL_bake=+1, ΔL_response=+1, ΔL_quality=0**；resolver 0 新族、case_specific=0、full_expansion=0；COMPLEXITY_LAUNDERING_RISK=NO。
- 族谱现况：Bake 5 族（CRR/PLAIN/HARD_GATED/PATCH/SINGLE），Response 3 族（TYPED/DUAL/CUE_GUIDED）；成员 3+4（rank 待批）+2+2+7 / 19+4+1。

### 待 Human Review（human_review_queue.jsonl）

HRQ-B1-01 SINGLE 族（factor_type 轴宽度：资源场/habitat 因子/化学梯度场同槽？）｜HRQ-B1-02 PATCH optional_context extend-vs-split（倾向 SPLIT）｜HRQ-B1-03 CUE_GUIDED 族（evaluand 边界+§10 关联+product deferred）｜HRQ-B1-04 PLAIN 轴扩容（槽位数伸缩+rank 因子类型；与 share-vector 表达层联合裁决）｜HRQ-B1-05 常规成员扩展备案（TYPED+13/DUAL+DIS/PATCH+ONS）。

### TARGETED_AUDIT_REQUEST

- **TAR-05**（褐鳗 BRT）：rank fact（优势等级）是否产品化持久写回？影响 BRT Bake 族归属（不实现则退化为 SINGLE 形）与 PLAIN 因子轴。
- **TAR-06**（海七鳃鳗）：诱捕/化学趋向是否进 playable scope？若不进，CUE_GUIDED_APPROACH_AVOID 候选冻结归档（SINGLE 族 LAM-BAKE 的梯度场因子同此裁决）。
- **TAR-07**（鸭嘴鲟 S34/S35）：电呈现输入的产品契约（由谁提供/是否纳入）与 cue_history 状态契约（键/写入/保持；Input Contract Open）。

### R2 顺带项（REV-002，并入本批收尾）

1. B0 engine_report 重生成至 **25 条**（fix 两条 engine ADMITTED，与语义裁决一致）✓
2. B0 worker_self_qa 计数标注（15/25，表结论不受影响）✓
3. apply_fix_001.py EEL_URL 勘误：envelope 原文尾部多「4」（33 位无效 ID）→ 32 位规范 ID（与 blind_programs/stories.jsonl 一致）✓

## 产物清单（fish_logic_census/batches/CENSUS-B1/）

manifest.yaml｜stories.jsonl（15）｜blind_programs.jsonl（24，hash 冻结）｜programs.jsonl（24）｜merge_tests.jsonl（38）｜resolver_tests.jsonl｜absence_claims.jsonl（1）｜human_review_queue.jsonl（5）｜coverage.jsonl（空）｜program_revisions.jsonl（空）｜engine_report.json｜build_blind_programs.py｜run_merge_tests.py｜build_census_outputs.py｜update_registry_v3.py｜worker_self_qa.md｜batch_report.md
仓库级：template_registry.yaml v3｜discovery_curve.csv +B1 行。git 未 commit（coordinator 收尾）。上下文余量约 12%——下批前建议 coordinator 评估是否需要压缩交接。

BATCH_ID: CENSUS-B1
