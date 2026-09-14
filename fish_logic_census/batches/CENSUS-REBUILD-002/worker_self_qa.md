# CENSUS-REBUILD-002 worker Self-QA（R2 §12 范式）

## A. 盲纪律自查
1. **判同前未读 registry**：盲体（含复用体语义内容）冻结于 05:37:14Z / REV 后 05:41:12Z；template_registry.yaml 首次打开 05:38Z 后（run_merge_tests 只读+sha256 前后断言）。✓
2. **REV-RB2-001 披露**：BHC/HER return_type 修正发现于 registry 开后（读 RS1 批档触发）——按 BIAS_RISK 全留痕（program_revisions+freeze_history）；该字段非判同信息（结构/顺序/族形零变更，判同四态前后不变：两体均不匹配 FILTER_FIELD 三步 canonical）。✓（HRQ-RB2-03 裁决点）
3. **盲体语汇**：76 条自主体扫描 0 族名/提案语汇泄漏（脚本核验）；18 条复用体保留 RB-1 冻结 basis 原文（5 条含 queue 元数据归族引用=输入层非 registry——manifest bias_declaration 声明，不改写复用文本）。✓
4. **推导方向学**：真形序全部从 story 主句/形态生态/CSV 锚独立推导；B 层样板语义还原（CHN/COH/BRO/ALE 自述『样板链优先』）一律不采并逐鱼记分歧（AST/SNS 轴分歧挂 HRQ-RB2-04）；新增 CSV 锚分维判定标准已公布于 manifest（可复现）。✓

## B. 覆盖与计数对账
1. queue 94 项全消费：94 盲程序=94 merge_tests=94 programs=94 coverage；0 held（absence_claims 空）/0 order_undetermined/0 AMB。✓
2. 四态：MC 69+EXT 0+NEW 25+AMB 0=94（Counter 实测）；MC 分族 28+13+12+6+4+4+1+1=69；NEW 分形状 16+6+2+1=25。✓
3. RS1 轨：确认 31+移动 16=47（逐条列表 engine_report）；B6 轨：MC 31+NEW 16=47。✓
4. curve 行 n_new_template=0（distinct 口径——本批无 RB-1 六提案外新形状；NEW 25 全部 related_proposal=HRQ-RB1-02）；n_stories_consumed=94（queue 条目口径，随行声明）。✓
5. registry 零改动：run_merge_tests.py sha256 前后断言通过；discovery_curve.csv 追加幂等（重跑 skip）。✓

## C. 同鱼对账（envelope 衔接指令）
1. 复用 18：17 同鱼同面（一致性核验=RB-1 basis 事实逐条存在于 B4 快照——抽样全 17 核对）+WS2↔WST 同种品系。✓
2. RBP 异面处理：RB-1 摄食面真形不适用于护卵面项——独立推导（面级守恒判据）。✓
3. 冲突序 0：RB-1 移动提案 7 成员的 RS1 轨复核全部同向（BSB FDR SSL SDG TSK WIT YTF）。✓
4. 批内去重：JSB↔ASB（同 URL 同种——真形同体推导+双 queue 项独立记账）/AGC↔GRB（同种品系——真形复用）。✓

## D. 程序体纪律（章程）
1. 渐进累积语义：全部 body 无终步 combine（NONE_PROGRESSIVE）；三档=全额/×衰减/×0.01 软出局；GATE 二元 EARLY_RETURN（裁决 1）。✓
2. 顺序从 Story 正文推导（§5 纪律）：分级命中展开为三档 branches（IF3_PROGRESSIVE）；31 确认+16 移动=47 在册成员全部完成序比对专项待办。✓
3. incoming_premises vs surface_owned_logic 分离：洄游/性转换/停食/护卵期/时段窗/品系复用/夜行窗口全部落 premise。✓
4. IR 节点：SEQUENCE/EVAL/Gate/Slot/GATE_ANCHOR——无 PARALLEL_SET（无契约无序面）。✓
5. De-instantiation：axis 携物种事实为证据引文（非 Profile 名）；instance_noise 记物种。✓

## E. 边界
1. NEW/移动/空置提案全挂 HRQ（RB2-01..06）——不自我批准、registry 零 mutation。✓
2. 表达线分歧（AST/SNS 轴、BHC/HER 步数）只记档不替表达线改文件。✓
3. 品系/杂交分辨率处理显式（HRQ-RB2-05）——亲本批补证通道开放。✓

## F. 残余风险（供独立审）
1. FF/SF 两提案形状的成员归属以 RB-1 提案批准为前提（若独立审拆改提案形状，本批 25 NEW 需随动重判——挂 HRQ-RB2-02 合并裁决）。
2. BHC/HER 单步读法 vs B 层三步展开（HRQ-RB2-03）与 AST/SNS 轴分歧（HRQ-RB2-04）为 census/表达线两层读法差异——按 EEL 判例②证据分层不静默归并。
3. 8 鲤品系单因子真形分辨率低（Deferred/Low）——亲本 R03 轨不在重跑队列，升档复核通道开放（HRQ-RB2-05）。
