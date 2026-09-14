# CENSUS-REBUILD-001（RB-1）batch report

状态：WORKING / NOT AUTHORITY / NOT PROMOTED ｜ batch_type=TRUTH_REBUILD_RERUN ｜ status=INDEPENDENT_REVIEW_REQUIRED

## 0. 摘要

终局全库顺序还原重跑第一批（HRQ-REBUILD-SCOPE-001 用户裁决授权）。输入=truth_rebuild_queue.jsonl 三层共 91 项（B4 25 + B5 52 + slot_tiering 14）；6 组同鱼双轨合并（POR/RKB/WIN/SMF/SAI=B4↔RS1、CSL=B5↔RS1-DS）后 82 尾鱼逐鱼顺序推导（渐进累积语义），3 尾 held（queue 裁决 ASR/RVS/RDS）。四态：**MC 35 / EXT 0 / NEW 45（6 distinct 新族提案）/ AMB 2**；族移动提案 7；canonical order_provisional 确认证据 7 族；slot_tiering 轨 14/14 关闭归真形。registry v9 **零改动**（v10 mutation 待独立审另批）。

## 1. 输入与证据分层

- queue 91 项（layer：AMB 四层链第 1 层 25/第 2 层 52/slot_tiering 14）；3 held 不推导（absence_claims）。
- 证据三层：A=census 冻结 story 快照（Tier A）；B=B 系列表达文件 §0+§2（Tier B 受限还原——只对照不照抄）；C=fish-reference-20260908.csv 形态/生态行。
- B 层 Normal 面约定序一律不采：真形序从 story 主句（食性主句先行=开放水跟随型 / 栖息复合主句高信息密度=结构先行 / 口器生理特化=门或特化轴先行）+ CSV 锚推导；证据分辨率决定链长与轴类型；不足=order_undetermined（PEL/TGT）。
- 8 份纯正文型快照（无 content 包裹）按整文读入（B5 判例④形态）。
- REP-WORDING-ALIGN-001 并行（Coordinator 通知）：仅改 ×0.01 措辞不动顺序行/链形——本批零影响，引文按读取时文本标注（manifest bias_declaration 已声明）。

## 2. 盲纪律时间线

- 82 真形体全部推导完成并冻结：**2026-09-14T05:04:02Z**（blind_programs.jsonl sha256[:16] 记 manifest；registry_seen=false）。
- stories.jsonl/manifest（含 bias_declaration）写出：05:04:32Z。
- 首次打开 template_registry.yaml（判同）：05:06Z 后（run_merge_tests.py 只读——sha256 前后一致断言）。
- 零 post-registry 盲体改动（program_revisions.jsonl 空）。

## 3. 判同结果（详表=merge_tests.jsonl / engine_report.json）

### 3.1 MERGE_CONFIDENT 35
| 族 | 成员 | n |
|---|---|---|
| TIERED_SINGLE_FACTOR_CHAIN | CBM BST STL SVT PRC HYC MHS RHM RBP HBW AKB APA GOT GIT HLL RVC（单步链无序判据适用） | 16 |
| GATED_COVER_TIER_CHAIN | GPF SMF LMD INC WST ARO（INC/WST=gate→forage 参数读法；ARO gate_axis=surface_zone 新值——HRQ-RB1-03） | 6 |
| GUARD_ANCHOR_TIERED_COMBINE_CHAIN | HNC CRC MDC LMP AMK（anchor：nest 2/egg_mass 3；B5 EXT 轨值提案由真形 MC 兑现） | 5 |
| NOCTURNAL_LIGHTSLOT_CHAIN | GDE MOO CLC RTC（夜行轴证据分层注记：GDE=story 原文/余=CSV 锚） | 4 |
| ZONE_SUBSTRATE_RESOURCE_CHAIN | RRH GRH（canonical 源=GRH 真形复验） | 2 |
| ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN | SMB（canonical 源复验） | 1 |
| SOFT_TRIPLE_TIER_CHAIN | BSK（canonical 源复验） | 1 |

### 3.2 NEW_TEMPLATE_CANDIDATE 45（6 distinct 新族提案——HRQ-RB1-02）
| 新族提案 | 序 | 成员 | n |
|---|---|---|---|
| FORAGE_FIRST_DUAL_TIER_CHAIN | forage→habitat | POR SAI SDG SAF YFT STM ALB SPM BIA PBF | 10 |
| SPACE_FIRST_DUAL_TIER_CHAIN | space→forage | ARG ASP BLP BPB BSB CCR CMR CSL DTN FDR GAJ GG GSF HAD HAL KGO LKR LKT RFP RKB ROB SPC SPK SSL TAI TMU TSK WIN | 28 |
| GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN | 门(底质)→复合带→资源 | WIT YTF | 2 |
| GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN | 护巢四步+浊度修饰 | JGC JDP | 2 |
| STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN | 结构→夜槽→猎物 | GW GT | 2 |
| HABITAT_FORAGE_FLOODSLOT_CHAIN | habitat→forage→洪泛槽尾 | BAS（单成员 PROVISIONAL） | 1 |

同签名 [E,E] 三族语义区分：LAYER_AXIS_DUAL_TIER（第二步=premise 轴段，轴域限定）≠ FF/SF（两空间因子序镜像——ORDER=族判据不并）。SPACE_FIRST 族内 op 字面（STRUCTURE vs HABITAT_FACTOR）归一读法挂 HRQ。

### 3.3 AMBIGUOUS_NEEDS_EXPANSION 2
- TGT（亲本系复用未消解+CSV 行不可信）；PEL（三态×三型泛化无链序证据）——挂真形重验（HRQ-RB1-05）。

### 3.4 held 3
ASR/RVS/RDS 维持 evidence_insufficient_held（无表达文件——FR/表达线补证通道）。

## 4. 族移动提案（HRQ-RB1-01，7 条）
WIT/YTF（RS1 GATED_COVER→TB 新族）；FDR/BSB/SSL（RS1 GATED_COVER→SF：story Tier A 证伪伏击门样板——FDR=Bottom Omnivore/BSB 无二元原文/SSL 潜沙=反捕食 overlay）；SDG（RS1 TIERED_SINGLE→FF：裁决 4 电感知分层后真形=双因子）；TSK（RS1 TIERED_SINGLE→SF：深冷主句先行）。依据=证据分层（Tier A story vs Tier B 样板）——EEL 判例②同型不静默归并。

## 5. slot_tiering 轨关闭（裁决 6-③ 落地）
14/14 真形归属：TAI/BLP/RFP/DS(CSL)/HAL/GG/POR/RKB/WIN→SF；PBF/SAI→FF；GT/GW→SL；SMF→GATED_COVER MC。「表达文件自投影受限还原（Tier B vs story 证据分层）」经本批 Tier A 重推消解。

## 6. B5 EXT guard 轨处置（HRQ-RB1-04）
- MC 兑现 4：MDC/LMP/AMK/CRC（anchor 值提案→成员资格）。
- 升级结构差异 1：JGC（+浊度修饰步=TU 新族）。
- 面级重指派 1：KGO（story S6=SN 无 P04——真形回归 Normal 面 SF；B5 guard 面承载=骨架占位 Tier C 零证据，撤销提案）。

## 7. order_provisional 确认（HRQ-RB1-06）
7 族（GATED_COVER/ZONE_SUBSTRATE/ZONE_DEPTH/NOCTURNAL/GUARD_ANCHOR/SOFT_TRIPLE/TIERED_SINGLE）获本批 Tier A 逐鱼推导的真形序确认证据——v10 降级提案（registry 零改动纪律下随独立审）。

## 8. 计数对账
- queue 91 = 推导 82（含 6 双轨合并对象）+ held 3 ✓
- 82 真形 = MC 35 + NEW 45 + AMB 2 ✓（merge_tests.jsonl 行数 82）
- NEW 45 = 6 distinct 族（10+28+2+2+2+1）✓
- curve 行：n_new_template_candidate=6（distinct 新族口径——REV-001 F1：原误填程序级 NEW 数 45，已改）；n_stories_consumed=85=queue 条目口径（82 真形+3 held）✓
- registry/template_registry.yaml 零改动（sha256 断言）；discovery_curve.csv 追加 1 行 ✓
- 双轨 6 组两轨条目状态互引记录（stories.jsonl queue_ids 合并承载）✓

## 9. 停点
Self-QA（worker_self_qa.md）+ validate_batch + fixtures 通过 → INDEPENDENT_REVIEW_REQUIRED → 停。BATCH_ID: CENSUS-REBUILD-001
