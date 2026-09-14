# BATCH｜CENSUS-REBUILD-002（终局重跑 RB-2）｜REVISE→R1→R1' 三轮 APPROVE 闭环

- 输入：queue 94 项（B6 47+链族 47）；产出 commit e1adf08。
- 结果：94 全消费（76 derived+18 reused，0 挂起/0 冲突）；四态 69 MC/0 EXT/25 NEW/0 AMB；**distinct 新族 0**——25 条 NEW 全落 RB-1 提案形状（FF+16/SF+6/TB+2/FS+1，跨批独立佐证）；order_provisional 确认 31；族移动 16（含 TS→LA 锚分维判定）+ FILTER_FIELD 空置提案；RBP 同代号异种勘误（Pacu vs Piranha）。
- 审校链：REV-001（F1 curve 口径复发+F2 身份失实）→ R1（F4 处置失误制造 hash 断裂，被二轮审出）→ R1'（冻结体逐字节回滚，CRLF 口径 hash 精确复现；F2 产物层 9 处全清）→ **ARTIFACT_APPROVE**（96cf145）。
- 遗留（v10 前顺手）：批内一次性生成器常量 7 处旧口径（零即时损害，重跑才再生）。
