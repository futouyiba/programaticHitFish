# HRQ-V10-MUTATION-001 Worker Self-QA（R2 §12）

## 授权与越界检查

- [x] 零新增裁决：全部落表项可溯源至（a）三批 RB verdict 卡 APPROVE、（b）hrq_decision_log.md 裁决、（c）envelope scope 七项；无自行发明状态（envelope 两处口径与工件不符处按 B7-F2 判例「工件为准+显式披露」处理而非照抄——batch_report §4-①②）
- [x] scope 边界：无 registry 外文件越权改动——改动清单=template_registry.yaml+RB-2 三生成器 8 行（envelope 顺手项点名范围）+RB-3 .freeze_marker（同）+本批档四文件；curve 零改动（envelope 明示）
- [x] Notion 零接触（本批非普查批无 Story 消费；Notion 同步=checklist 第 2 步归后续批）

## 落表忠实性

- [x] canonical 逐字性：11 新族 canonical body 从源成员冻结真形体 ordered_steps 逐字转写（渐进累积三档语义+GATE EARLY_RETURN 门语义+无终步合并——语义裁定 1 对齐）；ir_pointer 指向 blind_programs.jsonl 冻结体
- [x] 成员清单工件性：19 个 known_instances 程序列表由脚本从三批 merge_tests.jsonl 派生（assert_family 集合断言 12 组），无手打名单漂移风险
- [x] 迁移完整性：16 个 moved_from 条目=TS 8 出+GC 6 出+FILTER 2 出=LA 4 入+FF 3 入+SF 4 入+ZS 1 入+TB 2 入+TS 2 入；23 条批级记录（7 双轨）在 provenance item2 记账
- [x] 终裁忠实：TIL3 双面/ARO 退族/CSL+CSN1 fry_school/JDP-ARA-CSL-SMA1 规则重落——措辞均锚定 HRQ-RB3-03/04/05+HRQ-RB2-07 原文与 B 文件直证字段（arapaima GuardAnchorResolverInstance=fry_school/smallmouth §11.2 实例集）
- [x] 历史保全：v9 mutation_provenance 块整体平移 v9_mutation_history 零删改；SINGLE/PLAIN/PATCH 历史层原样；FILTER_FIELD known_instances 转历史层注记不删

## 计数对账（脚本断言全过）

- [x] 名义：SF 61=28+6+27/FF 34=10+16+8/TB 4/TU 2/SL 2/FS 2/四形族各 1（新族 110=RB NEW 45+25+40）
- [x] 既有族：TS 94/GC 27/NO 24/LA 7/ZS 7/ST 3/ZD 2/GA 18（名义 182=前 RB 期 40+RB 落册 142——REV-001 F1 双轴拆分勘误；原「181 RB+MGC 1」为混轴等式）
- [x] RB 闭合：294=181 MC+110 NEW+2 AMB+1 NOS
- [x] GUARD 26：Counter{nest 11/egg_mass 7/fry_school 6/host_brood 2}+exited 2（brooded 历史层）
- [x] 活族：28 CANDIDATE（23 Bake+5 Response）——三口径 18/23/28 在 provenance 声明
- [x] 曲线零改动+幂等守卫实测 exit 1

## 已知残留（交独立审）

1. envelope SL=4 vs 工件 2（§4-①）；envelope「12 族 order_confirmed」vs 证据链 8 族（§4-②）
2. HARD_GATED/EXTREME_TEMP/PATCH_GATED_DUAL order_provisional 终态维持（无 RB 证据不翻转）
3. TGT/PEL 真形挂重验+ASR/RVS/RDS held（FR/表达线补证通道）
4. ARA 初始形式旧读法存于 RB-2 批档生成器（推导时点记录——非错误不回改；registry 层已由规则取代）
