# CENSUS-RERUN-PLAIN-001 Batch Report｜PLAIN / HARD_GATED / PATCH 三族旧成员重跑（RS1 同构）

status: **INDEPENDENT_REVIEW_REQUIRED**；validate PASS（programs=9 stories=9 merge_tests=38）；fixtures 12/12。
盲冻结 2026-09-11T05:25:21Z（终冻；freeze_history 留两次冻结——间隔内仅 IR deps 忠实度修正，registry 零接触）；registry v7 读取在后（manifest 双时间戳，opened_at 声明性下界）；program_revisions 空。执行模式：B3-F-0 fresh spawn 单轮。

## 输入

envelope CENSUS-RERUN-PLAIN-001（ARTIFACT_URL=顺序还原后表达文件）：PLAIN 原始 5（OSC/CHB=B0，BRT=B1，WAL/MDF=B2）+ HARD_GATED 2（LUN-WET/EEL，B0）+ PATCH 2（MGC-ADULT，B0；ONS，B1）= **9/9 全部有输入文件**（absence 空）。输入层=表达文件 §2.2（migration/normal/grazing/patch）与 §2.3/§2.4 NormalFeeding 面（guarding 三文件——Bake 面不在 §2.2，目录约定记 HRQ-RP1-04）。成员清单从批档台账导出（RS1 判例④：merge_tests MERGE_CONFIDENT 记录+registry known_instances 双源核对）。

## 核心结论：三族 canonical 全部受顺序还原冲击；PATCH 双成员互斥证伪

### PLAIN：v1 平铺 canonical 经原始成员全体证伪（0/5 匹配）——slot_tiering 为唯一存活读法

- **CHB（4 槽）/WAL（2 槽）/MDF（2 槽）**：受限还原=槽值三档（excluded=出局槽值非 EARLY_RETURN）+COMBINE，槽间 unordered 族契约维持。与 RS1 C8 14 例同形（vs TAI 载体直验语义 MC）→ **TEMPLATE_EXTENSION_CANDIDATE，slot_tiering 轨并入 HRQ-RS1-03**。本批 3 例是 PLAIN 原始成员——census story 证据=多因子 PLAIN 与表达投影**同向**（无 RS1 14 例来源分歧），仅 slot_tiering 一项真差异 → canonical v2 的证据比 RS1 批更强（HRQ-RP1-03）。
- **OSC 出族**：还原形=极值水温硬门先行（末位算术门→前置出局）+EXIT 档 unordered 因子集（排除档=EARLY_RETURN）+COMBINE → 新候选族 **EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN**（单成员 PROVISIONAL）。
- **BRT 出族**：patch 存在性门（无 patch 格无竞争占位对象——存在性先行）+槽1 EXIT 档+槽2 槽值档（core-vs-edge）+COMBINE **无归一化** → 新候选族 **PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN**（单成员 PROVISIONAL；TAR-05 rank fact 退化条款携带）。

### HARD_GATED：envelope 问项——硬门变成 EARLY_RETURN 链第一步**不构成新拓扑**，构成 canonical v2 升级

- v1 canonical 本就是 BUILD→GATE→…（门本在前）。顺序还原新增的真差异：**第二道极值水温门**（末位算术门还原为前置出局）+**因子档位化**（BRANCH：排除档=EARLY_RETURN）+时段槽（3→4 因子，factor_set 轴内）。族定义「硬门前置+因子组合」保持、2/2 成员同向、无族域违例 → **canonical v2 升级提案**（v2=源成员 P-RP1-LUN-BAKE 冻结体：BUILD→GATE_SURFACE_ACCESS→GATE_EXTREME_TEMP→EXIT 档因子×4 unordered→COMBINE）。与 SINGLE v2-or-SPLIT（HRQ-RS1-01）同构但方向相反——worker 倾向升级非拆族（HRQ-RP1-01）。
- **EEL=AMBIGUOUS_NEEDS_EXPANSION**：§2.4 投影自声明缺陷——族硬门字段名 [需核对]（HRQ-02 谱系）+census B0 原体 BUILD_ACCESSIBLE_SET 未承载。Tier A story 证据支持 BUILD 存在→补回则直验并入 v2；投影缺口为真→双门无 BUILD 变体（vs LUN 真差异）。证据分层裁决挂 HRQ-RP1-01/04。

### PATCH：envelope 问项——zone/current 中间步**不对称还原**，双成员互斥证伪 canonical → 族空置提案

- **MGC（zone 侧）**：context 常量 zone=bottom 还原为**首道二元定位判定**（无过渡档）——GATE_ZONE→资源档→NORMALIZE=门先行 vs canonical 评估先行（ORDER 真差异，RS1 GRB/SMA 判例同型）。重指派 **GATED_COVER_TIER_CHAIN**（gate_axis=bottom_zone 第 3 实例，AST/SNS 同值；deps 位形全同，语义 MC）。
- **ONS（current 侧）**：context 常量 fast_flow_stone **拆为流速档+石底档两步且均展开三档分级命中**（流速档含过渡削减带=非二元门）+附着资源档=三档×3 四步链。重指派 **SOFT_TRIPLE_TIER_CHAIN**（vs BSK deps 位形全同，语义 MC；族 1→2 跨科独立重复——单成员 PROVISIONAL 升格候选）。
- 即：zone→二元门（否，未展开三档）；current→三档+拆步（是）。两成员落**不同形** → PATCH 评估先行 canonical 证伪，重指派批准后**族空置**（P06 压缩候选联动 HRQ-04/HRQ-B1-02 PENDING 不受影响，归并裁决一并处置——HRQ-RP1-02）。

### 计数与曲线

**ΔL_bake=+2**（顺序还原后第二个正增长批——进一步佐证 LOCAL_SATURATION_CANDIDATE 前提证伪，处置仍归 HRQ-RS1-01）。registry **v7→v8：21 族 CANDIDATE**（19+2）；**名义 162 不变**（重指派/出族全挂账 pending，过渡双列不删）。verdict：MC 8 / EXT 3 / NEW 25（含边界 11+CRR 续存 9）/ AMBIGUOUS 2。

## 边界证据（non-match 互记，11 条）

OSC vs HARD_GATED_v2（门数/BUILD=结构非轴）；OSC vs GATED_COVER（因子集+COMBINE vs 单档+NORMALIZE）；OSC vs C8 载体（门+EXIT 语义 vs 槽值出局——slot_tiering 族域边界）；BRT vs GATED_COVER/C8/OSC 源（三向）；LUN v2 vs GATED_COVER（v2 方向续存）；MGC vs HARD_GATED/ZONE_SUBSTRATE（反向+档位步数 1 vs 2）；ONS vs ZONE_SUBSTRATE（首步三档 vs 二元门=gate-kind 判据）/ZONE_DEPTH（链长 4 vs 5）。CRR non-match 9 例 engine 证据留档、registry 名单不重复登记（HRQ-RS1-04 判例延续）。

## 待审/待办

HRQ-RP1-01（HARD_GATED canonical v2 升级 vs 拆族+EEL BUILD 证据分层+hard_constraint_gate 门序列轴声明）；HRQ-RP1-02（2 新族立族[各含 extend-vs-split 复杂度对比——worker 裁 NEW：门数/BUILD/归一化缺失=结构元素非 typed 轴]+MGC/ONS 重指派+SOFT_TRIPLE 升格+PATCH 空置处置[联动 P06]）；HRQ-RP1-03（slot_tiering 轨并入 HRQ-RS1-03 联合裁决+PLAIN v1 证伪+OSC/BRT 出族+名义计数过渡）；HRQ-RP1-04（EEL [需核对] 字段回写+guarding 目录 §2.3/§2.4 输入定位约定+ONS confidence LOW 重申+CRR 不重复登记记档）。TAR：零新增。

## 产物

batches/CENSUS-RERUN-PLAIN-001/：manifest/stories(9)/blind_programs(9)/programs(9)/merge_tests(38)/resolver_tests(空)/absence(空)/coverage(空)/program_revisions(空)/human_review_queue(4)/engine_report/build×2 脚本/run 脚本/worker_self_qa/batch_report。仓库级：registry **v8**（21 族）、discovery_curve +CENSUS-RERUN-PLAIN-001 行。

BATCH_ID: CENSUS-RERUN-PLAIN-001
