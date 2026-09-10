# BATCH｜FORAGE-CONTRACT-REP-001（+R1）

- 保存说明：agent 报告要点归档（全文见会话 transcript）；R1 修复轮同目录。
- 角色：fcf-representation-worker（命名角色，两轮）
- 产物：outputs/usable_forage_contract_r0/（README/config/validate/dsl/accounting）
- 首版：validate PASS（5 族）+ selftest 13 例；design decisions：守卫扫描全文、硬窗不软窗、diet×size 可分离不购 2D。
- R1（处置 FORAGE-CONTRACT-REV-001 F1–F6）：英文词干 5→25；中文关键词表 18 条（键+值+\uXXXX 解码面子串检查）；prey_field_semantics 机器可读不变量 + SNAP 事实族 allowlist + 修正词干拒绝；行级 allowlist；accounting 输入侧义务 §2b + §15.7 external gate；空 diet_classes 合法；README 措辞修正。最终 validate PASS + selftest 66 用例。修复自查记录两处失误（perceiv/percep 词干漏网由 probe 用例抓出；selftest set 比较恒 False 假 FAIL）。
- BATCH_ID: FORAGE-CONTRACT-REP-001 / -R1
