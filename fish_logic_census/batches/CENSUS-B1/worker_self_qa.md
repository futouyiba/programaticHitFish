# CENSUS-B1 Worker Self-QA

R2 §12 Final Self-Attack 清单逐项自检。Self-QA 不冒充 Independent Review。

| # | 自攻项 | 结论 | 证据 |
|---|---|---|---|
| 1 | Audit+Census 揉一个上下文？ | NO | 15 条 Story 只读冻结输入；未重查现实、未上网补证据（七鳃鳗 GLFC/USGS 等证据全部来自 Story 页冻结记录） |
| 2 | 看 Registry 后回头改 Reality Story？ | NO | Story 页 fetch 一次只读 |
| 3 | 看 Template 后才画 Program（Fit Bias）？ | NO | 24 条盲骨架于 2026-09-10T13:32:49Z 冻结（manifest 锚定），run_merge_tests.py 之后才跑；program_revisions.jsonl 空。注：B1 期间 registry 知识来自本 worker 维护 v0→v2 的记忆——盲重建输入自律为「冻结 Story + P0x 语义」，骨架形状全部从证据推写（如 LAM 的梯度场 evaluand、BRT 的 rank 因子均非任何既有族形状） |
| 4 | 先贴 PARAM_PROFILE 跳过 Sketch？ | NO | RAI 阴性样本也建了盲体（TYPED 标准形态）再归参数类；NO_SURFACE 面按章程写显式理由（TIL/DIS Bake 排除记录在 manifest+stories） |
| 5 | Mode activation 错算进 Surface body？ | NO | 口孵/迁移期/幼体阶段/繁殖期全部 incoming_premises；body 无 activation 判断 |
| 6 | Surface Gate 推给 Resolver？ | NO | B1 无新 gate 程序；SINGLE/PATCH 族内无 gate 外移 |
| 7 | A→B 与 B→A 当数学等价？ | NO | 全 SEQUENCE 保序；槽间顺序问题沿用 B0 HRQ-07 提案（待批） |
| 8 | sequence 偷偷变 parallel set？ | NO | 未使用 PARALLEL_SET |
| 9 | Helper/Resolver 洗复杂度？ | NO | case_specific=0；扰动事件/化学梯度场/预投饵斑块/痕迹=世界侧事实供给义务（登记 resolver_tests），未包装成 resolver |
| 10 | 相同 Feature/IO/Schema 当 Merge 证据？ | NO | 全部 structural_diff 裁决；LAM 虽与 TYPED 同为「evaluator→decide」两步，仍因 OPERATOR+RETURN 真差异判 NEW 而非按形状合并 |
| 11 | Program Instance 数当 Template 数？ | NO | 24 instances → +2 族 + 6 项既有族成员扩展；csv 分列 |
| 12 | Representation Schema 复用当 LogicTemplate 复用？ | NO | 未做表达判断；coverage_delta report 的表达侧结论（BA-T1/T2/T5 等）仅作 Story 定位背景，census 判同独立于表达结构；CUE_GUIDED 候选与 REP-CUE-AXIS 表达线显式分离（coordinator note #4） |
| 13 | 浅调研输出 absence/saturation 强结论？ | NO | 唯一 absence claim=RAI（Stable/L2 冻结证据，scope 限定）；无 saturation signal |
| 14 | Self-QA 冒充 Independent Review？ | NO | status=INDEPENDENT_REVIEW_REQUIRED；HRQ-B1-01…05 待审 |
| 15 | 漏 Negative Knowledge/reason/reopen？ | NO | 族 known_non_matches 更新（CRR+9、SINGLE↔PATCH、CUE↔TYPED）；PROVISIONAL 带 reopen 条件（P06 压缩、TAR-05/06/07） |

补充（B0 教训执行）：
- 机制面逐项过：TIL Bake（口孵无空间证据）、DIS Bake（育幼锚定仅推论）、RAI/PIK/GAR Bake（无空间新证据）显式排除；PIK/GAR 取饵后阶段、BLU 吐饵、LAM 陷阱 OUT_OF_SCOPE；S12 色型对照不重复建体——无静默丢弃（manifest coverage_discipline 段）。
- 族完整性：SINGLE 7 成员、TYPED +13、DUAL +DIS、PATCH +ONS、PLAIN +BRT 逐成员直验（merge_tests 全录）；canonical 无变更（v3 仅加实例与新族），无回归复检触发。
- Extension 三字段：HRQ-B1-02 四条全带 cost 对比 + HUMAN_DECISION。
- R2 顺带项：B0 engine_report 重生成 25 条（fix 两条 engine ADMITTED 与语义裁决一致）、worker_self_qa 计数标注、apply_fix_001.py EEL_URL 勘误（envelope 尾部多「4」的 33 位无效 ID → 32 位规范 ID，与 blind_programs 一致）。
- 越权检查：Notion 全程只读（15 Story + P02 + coverage report 定位搜索）；git 未 commit；未改任何族 status。

Open（移交 review）：HRQ-B1-01…05；TAR-05/06/07。
