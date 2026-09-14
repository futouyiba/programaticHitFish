# CENSUS-REBUILD-001 worker self-QA

R2 §12 自查 + 本批专项。结论：PASS（1 项流程内自纠已留痕）。

## 1. 盲纪律（最高优先）
- [x] 判同前零 registry 读取：82 真形体冻结（05:04:02Z）→ stories/manifest（05:04:32Z）→ 首次读 registry（run_merge_tests 05:06Z+）。时序由 .freeze_marker+文件 mtime+manifest 双时间戳自证。
- [x] 零 post-registry 盲体改动：program_revisions.jsonl 空；merge_tests 只读 registry（sha256 前后断言）。
- [x] B 层约定序不照抄：每鱼 order_basis 记录推导依据（story 主句/CSV 锚）；与 B 层样板分歧显式记录（SSL/FDR/BSB/WIT/YTF/GDE 系=证据分层）。

## 2. 覆盖与计数
- [x] queue 91 项全覆盖（87 FISH queues+4 补遗+3 held absence=coverage.jsonl 85 行+FISH 82 行）。
- [x] 补遗留痕：HAD/BPB/RVC/CRC 4 尾在分批清单中一度遗漏，补推导后合并——过程在 tmp 工作区（rb1_truth_b11.py）非静默。
- [x] 四态对账：merge_tests 82 行 = MC 35+NEW 45+AMB 2；NEW distinct=6=curve n_new_template；散文（batch_report §3）与 engine_report 一致。
- [x] 双轨 6 组以最新真形为准（POR/RKB/WIN/SMF/SAI/CSL）——stories.jsonl queue_ids 载两轨。

## 3. 语义裁决自查
- [x] 同签名 [E,E] 三族区分（LAYER_AXIS/FF/SF）走语义层非 engine——engine raw 留 same_signature_families 供复核。
- [x] 顺序=族判据：FF/SF 序镜像不并（§2.3 唯一读法）。
- [x] GATE 语义保留（EARLY_RETURN）+三档=×0.01 软出局（§6.1）——真形体 tiers 字段全例核查。
- [x] AMB 不升格：TGT/PEL 保持 AMBIGUOUS（散文无 non-match 化）。
- [x] held 不并族（queue 裁决维持）。
- [x] 盲体语汇纪律：truth body 无 extension/新轴提案语汇（anchor 四形式值/participant=裁决 6.3 要求的记录字段）；提案语汇只在 merge_tests/HRQ。

## 4. 证据与分层
- [x] 每鱼 order_basis 带 A/B/C 层引文（story 引文原句/CSV 字段/表达文件节）。
- [x] 弱证据步显式标注（weak_evidence 字段：RKB 硬壳猎物/BSK 资源/JGC JDP 锚适配）+ open_semantics 挂起（食性补证后可能升链 6 例）。
- [x] 纯正文型快照 8 份整文读入（无 content 包裹 fallback）。
- [x] CSV 匹配修正留痕：ARG（'arg' 子串误中大口鲶 Largemouth）→精确匹配逻辑；HYC/CCR 中文名精确等值；LKT 补键——修正后全表复核。
- [x] TGT 的 CSV 行（reef-associated 海水）与淡水杂交种不符——显式不采信注记。

## 5. 流程内自纠（1 项）
- manifest post_registry 段初版有未格式化占位符（{mc}）——写出后即发现重写该段（git 历史可查）；无裁决/计数影响。

## 6. 并行批影响
- [x] REP-WORDING-ALIGN-001：manifest bias_declaration 声明并行+引文按对齐前文本标注——零顺序影响（该批不动 §0 顺序行/链形/步序）。

## 7. 边界
- 本批零 TAR（无现实缺口新增——挂起项走 HRQ-RB1-05 重验通道）；零 Notion 写回；registry/curve 之外零仓库改动（curve 追加 1 行+批档新增）。
- validate_batch.py=PASS（82/82/82）；fixtures 12/12 passed（census_engine+validator 断言）。

## 8. 结论
PASS → INDEPENDENT_REVIEW_REQUIRED。
