# CENSUS-REBUILD-002（RB-2）batch report

状态：WORKING / NOT AUTHORITY / NOT PROMOTED ｜ batch_type=TRUTH_REBUILD_RERUN ｜ status=INDEPENDENT_REVIEW_REQUIRED

## 0. 摘要

终局全库顺序还原重跑第二批（HRQ-REBUILD-SCOPE-001 用户裁决授权；RB-1 同工序范式）。输入=truth_rebuild_queue 两组 94 项：**AMB 四层链第 3 层（B6 47）+ 链族在册 order_provisional 成员（47——registry 9 链族的 P-RS1-* 在册成员）**。94 项全消费（0 held、0 order_undetermined）：76 尾逐鱼顺序推导 + 18 尾 RB-1 复用（17 同鱼同面 B4 起源 + WS2↔WST 同种品系）。四态：**MC 69 / EXT 0 / NEW 25（distinct 新族=0——全部落 RB-1 六提案形状，related_proposal=HRQ-RB1-02）/ AMB 0**；order_provisional 确认（清零提案证据）**31 尾**；族移动提案 **16 条** + FILTER_FIELD 空置提案；同鱼冲突 **0**。registry v9 **零改动**（v10 mutation 待独立审另批）。

## 1. 输入与证据分层

- queue 94 项（B6 47：P-B6-*-BAKE AMB vs SINGLE v1 转真形重验；RS1 47：链族在册成员 order_provisional 终裁轨）。
- 证据层：A=census 冻结 story 快照（B6/B3/B4 input_snapshots；R10 压缩四节按 B6 判例①直接消费）；A12=B1/B2 无 story 文本档→B1/B2 冻结盲体 sketch（Tier C story 派生事实）；B=B 系列表达文件 §0/§2（REP-WORDING-ALIGN-001 **已完成**——对齐后文本直接引用，无并行批影响）；C=CSV 形态生态；RB1=CENSUS-REBUILD-001 冻结真形（复用轨）。
- 推导方向学承 RB-1（食性主句先行=FF／栖息复合主句信息密度高=SF／口器生理特化=门先行／证据分辨率决定链长）；**本批新增操作化标准（manifest csv_anchor_standard）**：CSV 栖息带锚入步的分维判定——demersal 硬定位=独立底层步（INC/WST 判例）；benthopelagic/pelagic-neritic 软定位=仅当与 story 主体轴为独立维度时入步（COD/ARC/VEN/SWO 轴段与栖息带同维度不另立防双计；CHN/COH/BRO/ALE 水平廊道+垂直层两维两步）。
- 同鱼对账（envelope 指令）：17 复用+1 同种品系复用；RBP **同代号异种**（REV-001 F2 勘误：RB-1 P-RB1-RBP=B5 FISH-R08 淡水白鲳摄食面/本批=B3 FISH-R06 红腹食人鱼护卵面——代号复用不同物种；独立记账理由=异种，推导结论不变）；批内 JSB↔ASB 同属参照（REV-001 F2 勘误：JSB=maculatus/ASB=japonicus——源数据层 FishBase 同、Story 页/Species 条目层不同，B6 判例①域声明）、AGC↔GRB 同种品系去重联动；**冲突序 0**（RB-1 移动提案成员的 RS1 轨复核全部一致）。

## 2. 盲纪律时间线

- 94 真形体首冻：**2026-09-14T05:37:14Z**（sha256[:16]=24438c0e77d0e7a7）。
- REV-RB2-001（registry 开后判同准备期发现）：BHC/HER return_type FieldFeeding→SpatialDistributionWeight（Bake 面契约——RS1 C6 冻结体同证；顺序/结构/族形零变更，判同四态前后不变）→ 二冻 **2026-09-14T05:41:12Z**（sha256[:16]=1a43453f38dcec61）；program_revisions.jsonl + manifest freeze_history 双留痕。
- stories.jsonl/manifest 写出 05:42:01Z；template_registry.yaml 首次打开：05:38Z 后（run_merge_tests.py 只读——sha256 前后一致断言）。
- 76 条自主体盲语汇扫描 0 泄漏（无族名/提案语汇）；18 条复用体携带 RB-1 冻结 basis 原文（其中 5 条含 queue 元数据归族引用——非 registry 读，manifest 声明不改写复用文本）。

## 3. 判同结果（详表=merge_tests.jsonl / engine_report.json）

### 3.1 MERGE_CONFIDENT 69
| 族 | 成员 | n |
|---|---|---|
| TIERED_SINGLE_FACTOR_CHAIN | B6 品系 8（SUK GRK KHK OGK LCP AMC ASC HFC）+AMN BLT BMB DBC DCL GDB LFB PCC PKC+RS1 COD PIK19 ARC VEN SWO TAR PAD34 BST CBM+BHC HER（factor_type=field 轴值读法——FILTER_FIELD 移入） | 28 |
| GATED_COVER_TIER_CHAIN | B6：AGC WAG HYS WS2 ATC AWF RSS＋RS1：FGA SGA AST GRB SMA GPF | 13 |
| NOCTURNAL_LIGHTSLOT_CHAIN | B6：WCC ACA BBH BCF WHC STS TGS＋RS1：WEL FLA BUR GDE MOO | 12 |
| LAYER_AXIS_DUAL_TIER_CHAIN | CHU SHA（canonical 源复验）+CHN COH BRO ALE（TS 移入） | 6 |
| GUARD_ANCHOR_TIERED_COMBINE_CHAIN | BLU ARA RBP（护巢面三尾——canonical 源 BLU 复验）+HNC | 4 |
| ZONE_SUBSTRATE_RESOURCE_CHAIN | DRU+GRH RRH（复用）+SNS（GC 移入） | 4 |
| SOFT_TRIPLE / ZONE_DEPTH | BSK / SMB（复用复验） | 1+1 |

### 3.2 NEW_TEMPLATE_CANDIDATE 25（distinct 新族=0——全部 RB-1 提案形状，related_proposal=HRQ-RB1-02）
| RB-1 提案形状 | 本批证据 | n |
|---|---|---|
| FORAGE_FIRST（FF） | B6 13（ASB BHM BTS EUP GDS JSB PKS PLC PRB PSH RSC RUF SSM）+RS1 3（BRT12 PB+SDG 复用复核） | 16 |
| SPACE_FIRST（SF） | B6 2（CGD RBD——B6 首证栖息复合先行）+RS1 4（SSL FDR BSB TSK 复用复核） | 6 |
| GATE_SUBSTRATE_TEMPBAND（TB） | WIT YTF（RB-1 提案同鱼 RS1 轨双轨确认，+0 新增） | 2 |
| HABITAT_FORAGE_FLOODSLOT（FS/BAS） | SLM 银斑鲫第 2 实证——单成员 PROV 升 2 成员 | 1 |

### 3.3 order_provisional 确认（清零提案）31 尾
TS 9（COD PIK19 ARC VEN SWO TAR PAD34 BST CBM）/LA 2（CHU SHA）/GC 6（FGA SGA AST GRB SMA GPF）/NO 5（WEL FLA BUR GDE MOO）/ZS 3（GRH RRH DRU）/ZD 1（SMB）/ST 1（BSK）/GA 4（BLU ARA RBP HNC）——v10 降级提案随独立审。

### 3.4 族移动提案 16 条（HRQ-RB2-01）
TS→LA×4（CHN COH BRO ALE：垂直层步独立维度）/TS→FF×3（BRT12 PB SDG）/TS→SF×1（TSK）/GC→ZS×1（SNS：软底质原文步）/GC→SF×3（SSL FDR BSB）/GC→TB×2（WIT YTF）/**FILTER_FIELD→TS×2（BHC HER：单步场浓度链——B 层三步展开无 story 级顺序证据；FILTER_FIELD 移空→空置提案，PATCH VACATED 先例）**。

### 3.5 复用对账（envelope 衔接指令）
reused_from=RB-1 共 18：17 同鱼同面（BSK BST CBM GDE GPF GRH HNC MOO RRH SMB 确认类 + BSB FDR SSL TSK SDG WIT YTF 移动类）+WS2 同种品系（WST）。RBP 异面独立推导。同鱼冲突 0。

## 4. RB-1 提案形状累积证据（HRQ-RB2-02）
FF 10→26 名义（+16）/SF 28→34（+6）/TB 2→2（+0 新增，双轨确认）/FS 1→2（+1，SLM 升格证据）/其余两提案（TU/SL）本批无新证。**本批 curve n_new_template=0**（无 RB-1 六提案外新形状——判同只对 registry v9 活族 18，RB-1 提案形状全按 related_proposal 备注累积）。

## 5. REV-RB2-001 留痕（HRQ-RB2-03）
BHC/HER return_type 契约修正（FieldFeeding→SpatialDistributionWeight）——registry 开后发现，非判同信息（顺序/结构/族形零变更）；program_revisions.jsonl+manifest freeze_history 双记录；判同四态前后不变（FILTER_FIELD canonical 均不匹配）。

## 6. 计数对账
- queue 94 = 推导 76 + 复用 18 ✓（0 held / 0 order_undetermined / 0 AMB）
- 94 真形 = MC 69 + NEW 25 + EXT 0 + AMB 0 ✓（merge_tests.jsonl 94 行）
- MC 69 = 8 族（28+13+12+6+4+4+1+1）✓；NEW 25 = 4 个 RB-1 提案形状（16+6+2+1）✓
- RS1 47 = 确认 31 + 移动 16 ✓；B6 47 = MC 31 + NEW 16（FF 13+SF 2+FS 1）✓；RS1 47 = MC 38 + NEW 9（FF 3+SF 4+TB 2）✓；MC 69=31+38、NEW 25=16+9 ✓
- curve 行：n_new_template=0（distinct 口径——本批无新形状）✓；n_stories_consumed=94（queue 条目口径）
- registry/template_registry.yaml 零改动（sha256 断言）；discovery_curve.csv 追加 1 行（幂等守卫）✓

## 7. 停点
Self-QA（worker_self_qa.md）+ validate_batch + fixtures 通过 → INDEPENDENT_REVIEW_REQUIRED → 停。BATCH_ID: CENSUS-REBUILD-002
