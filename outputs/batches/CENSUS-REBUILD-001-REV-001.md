# BATCH｜CENSUS-REBUILD-001（终局重跑 RB-1）｜ARTIFACT_REVISE→修复→APPROVE 闭环

- 输入：truth_rebuild_queue 91 项（B4 25+B5 52+slot_tiering 14）；产出 commit 9e58bb6。
- 结果：82 尾真形（80 derived+2 order_undetermined）+3 held；四态 35 MC/0 EXT/45 NEW/2 AMB；**6 新族提案**（SPACE_FIRST 28/FORAGE_FIRST 10/TB 2/TU 2/SL 2/FS 1——顺序镜像对为核心发现）；族移动 7；order_provisional 确认 7 族；slot_tiering 14/14 关闭。
- 一轮审（REVISE）：判同本体无 false fit；F1 blocker=curve 列口径漂移（45→6）+F2-F6 minor（GW 键/dead-branch 标签/引文溯源×2/模板幂等）。
- 修复轮（5bf0694）：六项全闭（重生成 82/35/45/2 零变化；program_revisions 3 条留痕；validate PASS）。
- 闭合复审：**ARTIFACT_APPROVE**（2026-09-14）。
- 留 v10/HRQ：F7 external gates（LAYER_AXIS 重推回溯依赖、SF 逐尾规则适用记录——挂 HRQ-RB1-02）。
