# CENSUS-RERUN-SINGLE-001 Batch Report｜SINGLE 族受影响成员重跑（顺序还原下游后果）

status: **INDEPENDENT_REVIEW_REQUIRED**；validate PASS（programs=65 stories=65 merge_tests=224——REV-001 修复轮后）；fixtures 12/12。
盲冻结 2026-09-11T04:39:22Z（blind_programs.jsonl 文件系统精确时刻，61 条 hash+registry_seen=false）；registry v6 读取在后（manifest 双时间戳，opened_at 为声明性下界）；program_revisions 原空（判同段零 body 改动）——**REV-001 修复轮（2026-09-11，B1 面错配）后 8 条**（4 PROVENANCE_REWRITTEN + 4 ADDED_IN_FIX_ROUND；blind 追加 4 条 registry_seen_at_creation=true，append-only）。执行模式：B3-F-0 fresh spawn 单轮（双时间戳+hash 自证）+ REV-001 修复轮（apply_fix_rev001.py，Coordinator 修复指令）。

## 输入

envelope CENSUS-RERUN-SINGLE-001（用户反馈 §5.4 行动项）：SINGLE 族 66 成员中 **61 有顺序还原表达文件**（REP-ORDER-FIX-001..005，七目录 grazing/migration/normal/normal2/field/guarding/patch——envelope 列 5 目录，guarding/patch 经 FIX 标记扫描确认纳入，4+3 成员）；**5 无输入**（LAM/PIN/ASR/RVS/RDS——absence_claims 登记，原批 story 证据维持归族 pending_restored_input）。输入层=表达文件 §2.2 顺序还原伪脚本（WORKING/NOT AUTHORITY，档位成员 [需正文] 未校准）——与 B0-B4 的 Story DB 输入层不同，envelope 明示授权；来源分歧（表达文件投影 vs story 证据）显式挂 HRQ-RS1-03/04。**REV-001 修正**：guarding 目录 4 成员（BLU/ARA/RBP/HNC）原重跑误取 §2.2 护巢 Guard 面（物种名级文件扫描无面信息）——正确面（栖息面）重跑自 §2.4 补录（见下修复轮节）。

## 核心结论：SINGLE 族拆分（重跑主发现）

**61/61 重跑链形 vs SINGLE v1 canonical（两步平铺）全部 body 结构差异**（最小集=BRANCH：三档分级命中+early return；45 例附加 GATE/OPERATOR/DEPENDENCY/COMBINE/RETURN）；SINGLE forbidden_freedoms 显式禁 gate 与多因子 combine——**族域违例佐证拆分，非轴内差异**。B1-B4 的「SINGLE 大吸收」为平铺化伪影。
【REV-001 注记】61/61 论断经修复轮后对全 61 原成员成立：57 原重跑体 + 4 栖息面补录体（P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE，§2.4——vs SINGLE 同样 body 结构差异 BRANCH/OPERATOR/COMBINE/DEPENDENCY）；原 4 条护巢面重跑体为异面新程序（+4 名义），不计入本论断。

### 9 个新 Bake 候选族（ΔL_bake=+9；registry v7，CANDIDATE pending HRQ-RS1-01/02）+ REV-001 第 10 候选（C9）

| 新族 | 成员 | 链形 | 备注 |
|---|---|---|---|
| TIERED_SINGLE_FACTOR_CHAIN | 17 | 单因子三档（IF3_EXIT）→归一化 | 三亚群同构：premise 轴段 10（COD/PIK19/ARC/VEN/SWO/CHN/COH/BRO/ALE/TAR）+机会 4（BRT12/PB/BST/CBM）+感官 3（PAD34/SDG/TSK）；canonical=COD |
| LAYER_AXIS_DUAL_TIER_CHAIN | 2 | 水层软三档→轴段三档→积归一 | CHU+SHA 跨科独立重复；vs C1=前置水层步（OPERATOR） |
| GATED_COVER_TIER_CHAIN | 12 | 结构门（二元 EARLY_RETURN）+质量档→归一化 | envelope「伏击门形」承载族：门轴 8 值（植被/缓流/底带×2/可埋底质×4/深潭/礁缘/patch 存在/扰动窗）=gate_axis 参数轴（GUARD anchor 判例同型）；canonical=FGA；vs PATCH=门先行 ORDER 真差异 |
| NOCTURNAL_LIGHTSLOT_CHAIN | 5 | 夜行底板档（出局）+低光槽（调整器，**无出局语义**）→归一化 | WEL/FLA/BUR/GDE/MOO；槽位=live §11.5 判例原位 |
| ZONE_SUBSTRATE_RESOURCE_CHAIN | 3 | 底带硬门+底质档+资源档→积归一 | GRH/RRH/DRU（grazing 链形；同属同构+可翻性轴） |
| SOFT_TRIPLE_TIER_CHAIN | 1 | 软三档×3（无门） | BSK 单成员 PROVISIONAL（软定位 [需正文]） |
| ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN | 1 | 硬门+深度档+底质档+资源档（五步） | SMB 单成员 PROVISIONAL（链长=真差异非轴内） |
| FILTER_FIELD_ACCUMULATE_CHAIN | 2 | 水层档→场浓度档→口径档（线性累积 deps）→归一化 | BHC/HER；步间折减算子 UNDEFINED 待机制侧；vs C5b=deps 线性 vs 扇入 |
| GUARD_ANCHOR_TIERED_COMBINE_CHAIN | 4（**+4 新增名义**） | 锚存在门→锚适配/关系/温度档×3→合并（UNDEFINED）→**Guarding** 权重 | BLU/ARA/RBP/HNC；anchor 轴 4 值（colony_nest/floodplain_fry_school/root_spawn_eggs/pebble_mound）；**REV-001 改记新增**：成员=4 条 §2.2 护巢面新程序（非 B1-B4 栖息面原程序重指派——面错配修复，HRQ-RS1-05）；Bake 面护巢分布≠Response 面 ∥ 双 evaluand |
| **ORDERED_QUAD_TIER_COMBINE_CHAIN（C9）** | **4（REV-001 修复轮）** | **无门有序四步链**：水层定位三档（软/硬=档位成员归属轴）→结构三档→水温三档→时段三档→合并（UNDEFINED） | P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE（§2.4 栖息面正确重跑承载）；四成员 engine 零差异跨科独立重复（四科四属）；canonical=P-RS1-BLU-HAB-BAKE 修复轮冻结体；HRQ-RS1-05——**dL 计入按修复指令冻结本批 +9，C9 +1 位置待裁决** |

### C8：14 追击型成员 PLAIN 重归族提案（extension 轨，非新族）

TAI/BLP/GW/RFP/DS/PBF/GT/HAL/GG/POR/RKB/WIN/SMF/SAI 表达文件自投影=PLAIN 双槽+COMBINE_WEIGHTED（槽间 unordered 契约维持；槽内三档=受限还原，excluded=出局槽值非 EARLY_RETURN）。vs PLAIN v1 canonical：槽 arity 2 在 factor_set 轴域（B1-BRT 先例）、槽名=factor_type 字面；**真差异=槽内 IF3 档位→slot_tiering(FLAT|IF3_SLOT_VALUE) 新轴提案=TEMPLATE_EXTENSION_CANDIDATE**（复杂度对比入条目）。**证据分层待裁决**：表达文件投影（Tier B）vs census B1-B4 story 证据（单因子 SINGLE）来源分歧——批准前不计 PLAIN 正式成员（HNC 挂账先例）。HRQ-RS1-03。

### Discovery Curve 影响（envelope 问项）

- 本批 **ΔL_bake=+9**（B2 以来首个正增长；templates 10→19 candidate 级）。
- **B4 LOCAL_SATURATION_CANDIDATE 前提证伪**：B2+B3+B4 三连续 ΔL_bake=0 的根因=平铺输入抹平结构差异（66 Bake 全 SINGLE 吸收是伪吸收）；同 61 程序顺序还原后拆出 9 形。建议 review 撤销/降档该 candidate（HRQ-RS1-01 附带项）。
- **名义程序 162 + 4 = 166 pending HRQ（REV-001 修正）**：原「162 不变（重指派非新增）」对 C7 的 4 条不成立——护巢面 4 程序为异面新程序被记作重指派（守恒破坏，独立审 B1 实证）；修正后 4 个栖息面原程序的正确重指派由 §2.4 补录体承载（批准后 SINGLE 66→5、PLAIN 5→19、9 新族 47 不变、GUARD_ANCHOR +4 新增成员、C9 4 成员）。C9 候选族 dL_bake +1 的计入位置按修复指令冻结（本批维持 +9），挂 HRQ-RS1-05 裁决。

### 边界证据（non-match 互记）

GATED_COVER vs HARD_GATED（无 accessible-set/多槽合并；门语义=掩体存在非硬生存）；GRB/SMA vs PATCH（门先行 vs 评估先行 ORDER）；GUARD_ANCHOR vs PLAIN（RETURN/COMBINE）；CRR non-match 61 续存（同物种原程序 B1-B4 已登记，不重复追加名单——HRQ-RS1-04）。**REV-001 追加（C9 边界，engine_report_rev001.json）**：C9 vs SOFT_TRIPLE（链长 4 vs 3+终步 COMBINE vs NORMALIZE——C5c 判例同型）；C9 vs EXTREME_TEMP（前置极值门+无序因子集 vs 无门有序链——GATE=结构元素非轴）；C9 vs PLAIN/C8（有序链+EXIT 档 vs 无序槽+槽值档）；C9 vs GUARD_ANCHOR（**同物种对侧面级边界直证**：BLU §2.2 护巢 vs §2.4 栖息=两个程序）；C9 vs CRR（non-match 续存）。

## REV-001 修复轮（B1 面错配，2026-09-11，apply_fix_rev001.py）

独立审 CENSUS-RERUN-SINGLE-REV-001（verdict=ARTIFACT_REVISE）B1 blocker：GUARD_ANCHOR 4 成员的 rerun_of 所指原 SINGLE 成员经直读 B1-B4 原盲体证实**全部为栖息/洄游分布面程序**，而重跑体取的是同文件 §2.2 护巢 Guard 面（行为面不同；输入映射=物种名级文件扫描无面信息，tmp_chain_dump.txt 行 193 佐证）。后果（独立审四点）：①61/61 body 差异对原程序面不成立；②HRQ-RS1-01 拆分名单 4/61 错位；③守恒破坏（+4 新增被记作重指派）；④零披露（对照 C8 处理梯度倒挂）。C7 族链形同构本身经独立审确认真实无瑕（4 文件 Guard 面直验成立）——问题全在外部映射与记账。

修复处置（Coordinator 修复指令，apply_fix_rev001.py 落盘）：

1. **补正确面重跑**：4 个物种从表达文件 §2.4（栖息面）盲推补录 P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE（FIX 非盲补录范式 CENSUS-B0-FIX-001：registry_seen_at_creation=true + program_revisions 留痕 + manifest bias_declaration 补段全 disclosure）。判同实测（engine 实跑 engine_report_rev001.json）：四成员互证 engine 零差异（跨科独立重复四科四属）；vs registry v8 相关族全部 body 结构差异 → **C9 ORDERED_QUAD_TIER_COMBINE_CHAIN 新候选族（第 10 个，worker 裁 NEW——不预设、以实测为准；extend-vs-split 复杂度对比入 merge_tests）**；vs SINGLE v1 差异与原 57 例同向 → 61/61 论断经补录后成立。
2. **§2.2 护巢面 4 程序改记新增**：P-RS1-BLU/ARA/RBP/HNC-BAKE 的 rerun_of=null（program_revisions PROVENANCE_REWRITTEN ×4），GUARD_ANCHOR 族成员仍 4 个=这 4 条护巢面程序（+4 名义，registry 入册挂 HRQ 批准后另批）；B1-B4 的 4 个栖息面原程序保持 SINGLE moved_pending_review 不变（归宿=§2.4 重跑结果联动 HRQ-RS1-01/05）。
3. **数字与名单修正**：名义 162+4=166 pending HRQ；HRQ-RS1-01 拆分名单补正（4/61 原栖息面成员归宿改「§2.4 重跑结果联动」）；curve RS1 行 n_stories/n_sketches/n_merge_confident 61→65（dL_bake=+9 按修复指令冻结——C9 +1 计入位置挂 HRQ-RS1-05 开放问题）；registry **v8 零改动**（章程：mutation 由独立审另批）。
4. **披露与 M2**：manifest bias_declaration 补「C7 面错配修复轮」全段（含四行对照表）；M2 同步——build_census_outputs.py 内嵌 manifest 模板 registry_opened_at 由精确版（04:41:30Z）改为磁盘声明性弱化版，并加 REV-001 守卫（修复已应用即拒绝执行）+ registry v6→v7 历史段幂等守卫，防幂等重跑回退。

## 待审/待办

HRQ-RS1-01（族拆分总裁决：61 成员去向[REV-001 补正：4 席由 C7 改挂 C9 联动]+SINGLE v2 alternative[C1 视为 canonical 结构升级 vs 新族——worker 倾向 SPLIT，45/61 非单档形升级无法覆盖]+5 pending 成员最终态+饱和 candidate 处置+REV-001 +4 名义批准）；HRQ-RS1-02（9 新族立族+C5b/C5c 单成员 extend-vs-split+gate_axis/anchor_type 轴声明+GUARD_ANCHOR 与 Response GUARD 的 surface 边界+REV-001 +4 名义入册）；HRQ-RS1-03（slot_tiering 轴+PLAIN canonical v2[全库 PLAIN 投影文件已被统一槽内档位化]+证据分层）；HRQ-RS1-04（输入层治理：[需正文] 档位校准回写机制+envelope 目录不全+文件名≠内容标题 2 例+ASR/RVS 身份澄清路由+REV-001⑥guarding 目录节级面定位约定）；**HRQ-RS1-05（REV-001 修复轮备案：C9 ORDERED_QUAD_TIER_COMBINE_CHAIN 立族+GUARD_ANCHOR provenance 改记+名义 166 pending+dL_bake +1 计入位置）**。TAR：零新增。

## 产物

batches/CENSUS-RERUN-SINGLE-001/：manifest（含 REV-001 fix_round 节+bias_declaration 补段）/stories(65)/blind_programs(65——61 原冻 append-only + 4 HAB 补录)/programs(65)/merge_tests(224=211+13)/resolver_tests(空)/absence(5 RERUN_INPUT_UNAVAILABLE)/coverage(空)/program_revisions(8)/human_review_queue(5——RS1-01/02/04 补正+RS1-05)/engine_report+engine_report_rev001/build×2 脚本+run 脚本+**apply_fix_rev001.py**（修复轮脚本，幂等）/worker_self_qa/batch_report + tmp_chain_dump.txt（盲输入提取留档——REV-001 面错配佐证原样保留）。仓库级：registry v7（原批）——REV-001 修复轮 **v8 零改动**、discovery_curve RS1 行修正（65/65/65/14/9，dL_bake=+9 冻结）。

BATCH_ID: CENSUS-RERUN-SINGLE-001
