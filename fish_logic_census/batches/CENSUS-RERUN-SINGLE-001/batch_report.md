# CENSUS-RERUN-SINGLE-001 Batch Report｜SINGLE 族受影响成员重跑（顺序还原下游后果）

status: **INDEPENDENT_REVIEW_REQUIRED**；validate PASS（programs=61 stories=61 merge_tests=211）；fixtures 12/12。
盲冻结 2026-09-11T04:39:22Z（blind_programs.jsonl 文件系统精确时刻，61 条 hash+registry_seen=false）；registry v6 读取在后（manifest 双时间戳，opened_at 为声明性下界）；program_revisions 空（判同段零 body 改动）。执行模式：B3-F-0 fresh spawn 单轮（双时间戳+hash 自证）。

## 输入

envelope CENSUS-RERUN-SINGLE-001（用户反馈 §5.4 行动项）：SINGLE 族 66 成员中 **61 有顺序还原表达文件**（REP-ORDER-FIX-001..005，七目录 grazing/migration/normal/normal2/field/guarding/patch——envelope 列 5 目录，guarding/patch 经 FIX 标记扫描确认纳入，4+3 成员）；**5 无输入**（LAM/PIN/ASR/RVS/RDS——absence_claims 登记，原批 story 证据维持归族 pending_restored_input）。输入层=表达文件 §2.2 顺序还原伪脚本（WORKING/NOT AUTHORITY，档位成员 [需正文] 未校准）——与 B0-B4 的 Story DB 输入层不同，envelope 明示授权；来源分歧（表达文件投影 vs story 证据）显式挂 HRQ-RS1-03/04。

## 核心结论：SINGLE 族拆分（重跑主发现）

**61/61 重跑链形 vs SINGLE v1 canonical（两步平铺）全部 body 结构差异**（最小集=BRANCH：三档分级命中+early return；45 例附加 GATE/OPERATOR/DEPENDENCY/COMBINE/RETURN）；SINGLE forbidden_freedoms 显式禁 gate 与多因子 combine——**族域违例佐证拆分，非轴内差异**。B1-B4 的「SINGLE 大吸收」为平铺化伪影。

### 9 个新 Bake 候选族（ΔL_bake=+9；registry v7，CANDIDATE pending HRQ-RS1-01/02）

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
| GUARD_ANCHOR_TIERED_COMBINE_CHAIN | 4 | 锚存在门→锚适配/关系/温度档×3→合并（UNDEFINED）→**Guarding** 权重 | BLU/ARA/RBP/HNC；anchor 轴 4 值（colony_nest/floodplain_fry_school/root_spawn_eggs/pebble_mound——与 Response 面 GUARD anchor 轴同源）；Bake 面护巢分布≠Response 面 ∥ 双 evaluand |

### C8：14 追击型成员 PLAIN 重归族提案（extension 轨，非新族）

TAI/BLP/GW/RFP/DS/PBF/GT/HAL/GG/POR/RKB/WIN/SMF/SAI 表达文件自投影=PLAIN 双槽+COMBINE_WEIGHTED（槽间 unordered 契约维持；槽内三档=受限还原，excluded=出局槽值非 EARLY_RETURN）。vs PLAIN v1 canonical：槽 arity 2 在 factor_set 轴域（B1-BRT 先例）、槽名=factor_type 字面；**真差异=槽内 IF3 档位→slot_tiering(FLAT|IF3_SLOT_VALUE) 新轴提案=TEMPLATE_EXTENSION_CANDIDATE**（复杂度对比入条目）。**证据分层待裁决**：表达文件投影（Tier B）vs census B1-B4 story 证据（单因子 SINGLE）来源分歧——批准前不计 PLAIN 正式成员（HNC 挂账先例）。HRQ-RS1-03。

### Discovery Curve 影响（envelope 问项）

- 本批 **ΔL_bake=+9**（B2 以来首个正增长；templates 10→19 candidate 级）。
- **B4 LOCAL_SATURATION_CANDIDATE 前提证伪**：B2+B3+B4 三连续 ΔL_bake=0 的根因=平铺输入抹平结构差异（66 Bake 全 SINGLE 吸收是伪吸收）；同 61 程序顺序还原后拆出 9 形。建议 review 撤销/降档该 candidate（HRQ-RS1-01 附带项）。
- 名义程序 162 不变（重指派非新增；批准后 SINGLE 66→5、PLAIN 5→19、9 新族 47；过渡态 SINGLE 61 成员标 moved_pending_review 双列不删）。

### 边界证据（non-match 互记）

GATED_COVER vs HARD_GATED（无 accessible-set/多槽合并；门语义=掩体存在非硬生存）；GRB/SMA vs PATCH（门先行 vs 评估先行 ORDER）；GUARD_ANCHOR vs PLAIN（RETURN/COMBINE）；CRR non-match 61 续存（同物种原程序 B1-B4 已登记，不重复追加名单——HRQ-RS1-04）。

## 待审/待办

HRQ-RS1-01（族拆分总裁决：61 成员去向+SINGLE v2 alternative[C1 视为 canonical 结构升级 vs 新族——worker 倾向 SPLIT，45/61 非单档形升级无法覆盖]+5 pending 成员最终态+饱和 candidate 处置）；HRQ-RS1-02（9 新族立族+C5b/C5c 单成员 extend-vs-split+gate_axis/anchor_type 轴声明+GUARD_ANCHOR 与 Response GUARD 的 surface 边界）；HRQ-RS1-03（slot_tiering 轴+PLAIN canonical v2[全库 PLAIN 投影文件已被统一槽内档位化]+证据分层）；HRQ-RS1-04（输入层治理：[需正文] 档位校准回写机制+envelope 目录不全+文件名≠内容标题 2 例+ASR/RVS 身份澄清路由）。TAR：零新增。

## 产物

batches/CENSUS-RERUN-SINGLE-001/：manifest/stories(61)/blind_programs(61)/programs(61)/merge_tests(211)/resolver_tests(空)/absence(5 RERUN_INPUT_UNAVAILABLE)/coverage(空)/program_revisions(空)/human_review_queue(4)/engine_report/build×2 脚本/run 脚本/worker_self_qa/batch_report + tmp_chain_dump.txt（盲输入提取留档）。仓库级：registry **v7**（19 族）、discovery_curve +CENSUS-RERUN-SINGLE-001 行。

BATCH_ID: CENSUS-RERUN-SINGLE-001
