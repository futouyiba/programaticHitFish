# CENSUS-B0 Worker Self-QA

> **计数标注（R2 顺带，2026-09-10）**：本表写于盲批时点（13 程序/23 判同）；
> FIX-001 后实际为 **15 程序 / 25 判同**（+2 非盲补录），见 manifest.fix_rounds 与
> batch_report 修复轮附录。表内结论不受计数变化影响。

按 Orchestrator Prompt R2 §12 Final Self-Attack 清单逐项自检。Self-QA 不冒充
Independent Review（status 仍为 INDEPENDENT_REVIEW_REQUIRED）。

| # | 自攻项 | 结论 | 证据 |
|---|---|---|---|
| 1 | 是否把 Audit + Census 揉成一个上下文？ | NO | 本会话只执行 CENSUS；五条 Story 为 FR3 冻结输入，未重查现实、未上网补证据 |
| 2 | 是否看了 Template Registry 后回头改 Reality Story？ | NO | Reality Baseline 只读（Story 页 fetch 一次）；无任何 Story 内容改写 |
| 3 | 是否看了 Template 后才画 Program（Fit Bias）？ | NO（有已声明的初始化暴露） | 13 条盲骨架由 build_blind_programs.py 于 run_merge_tests.py（首次开 registry）之前生成并 hash 冻结；manifest 记录 frozen_before_registry_open=true；program_revisions.jsonl 为空=零修改。初始化时对 v0 种子的暴露已记入 role_memory（种子=Method R0 §6 方法合同本身） |
| 4 | 是否先贴 PARAM_PROFILE 再跳过 Sketch？ | NO | 13 个有程序意义的单元全部先 sketch 后分类；4 个 NO_SURFACE 面（Group×5、Quality×5 等）按章程只写显式理由 |
| 5 | 是否把 Mode activation 错算进 Surface body？ | NO | 湄公鲶 stage 切换、肺鱼干湿、地图鱼/肺鱼 guard、电鳗夜行全部记为 incoming_premises；body 内无 activation 判断 |
| 6 | 是否把 Surface Gate 推给 Resolver？ | NO | 水面可达 gate 留在 Bake body（HARD_GATED 族的核心结构元素）；无 gate 外移 |
| 7 | 是否把 A→B 与 B→A 当数学等价？ | NO | 全部 SEQUENCE 保序；因子槽间顺序问题未自行裁决，提案（unordered）进 HRQ-07 待审 |
| 8 | 是否把 sequence 偷偷变 parallel set？ | NO | IR 未使用 PARALLEL_SET；DUAL_PATH 的并行是程序语义本身（双路径并行评估），非 de-instantiation 产物 |
| 9 | 是否用 Helper/Resolver 洗复杂度？ | NO | n_case_specific_resolvers=0；SubstrateResourcePatchEvaluator 标 PROVISIONAL 待第二跨 case 实例；无 XxxFishLogic 式包装 |
| 10 | 是否用相同 Feature/IO/Schema 当 Merge 证据？ | NO | 判同全部走 structural_diff（op 序列/依赖形状/branch/combine/return）；typed 槽名字面差异的轴吸收均留 engine_raw_diffs 供 review 复核 |
| 11 | 是否把 Program Instance 数当 Template 数？ | NO | 13 instances → 5 candidate families + 1 extension 判例；discovery_curve 分列 |
| 12 | 是否把 Representation Schema 复用当 LogicTemplate 复用？ | NO | 未做任何 Representation 表达判断；P0x Semantic Pattern 与 census LogicTemplate 明确两层（HRQ-05/06 登记映射待审） |
| 13 | 是否浅调研却输出 absence/saturation 强结论？ | NO | 唯一 absence claim 为欧鲢 NO_NEW_PROGRAM_CURRENT_EVIDENCE（限定 scope，S3=EO 已声明）；未输出任何 saturation signal |
| 14 | 是否让 Self-QA 冒充 Independent Review？ | NO | status=INDEPENDENT_REVIEW_REQUIRED；7 条 HRQ 待审 |
| 15 | 是否漏掉 Negative Knowledge / reason / reopen condition？ | NO | 族级 known_non_matches 已写 registry；HRQ 全部带 pending_review_questions；PATCH 族带 reopen 条件（P06 压缩联动） |

补充检查（章程/Method 特有）：
- 盲重建允许读清单遵守：只读了五条冻结 Story、P01/P04/P05/P06 Pattern 页（Frozen Input）、Method/NK（初始化）、census_engine/validate_batch（工具）；未读 registry 具体 template body 之外的任何 PT Fit/coverage 统计。
- 族完整性：HARD_GATED(2)、PLAIN(2)、TYPED(5)、DUAL(2) 每成员对 canonical 直验（merge_tests 逐条记录）；无链式相似性推导；canonical body 变更（从成员到 generic 槽命名）已在 HRQ-01/02/07 声明为待批提案并触发回归复检要求。
- Extension 三字段：HRQ-03 两条 merge_test 均带 extension_complexity_cost / new_template_complexity_cost / recommended_shape=HUMAN_DECISION。
- 越权检查：未改 CRR status；新增族全部 status=CANDIDATE；未写 Notion（本批无 envelope 授权的 census 分流页指令，Notion 全程只读）；git 未 commit（按 envelope）。
- 工具边界：census_engine 仅出结构事实，全部语义 verdict 由 worker reasoning 给出（merge_tests.reasoning 字段）。

Open（移交 review）：HRQ-01…07；TAR-01…04（见 batch_report）。
