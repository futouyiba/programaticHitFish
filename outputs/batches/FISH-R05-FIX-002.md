# BATCH｜FISH-R05-FIX-002（FR2 REVISE 修复，researcher tab）

- 5 项全完成 + 1 项超范围（23 处 Evidence 坏链接全修，含电鳗 3 处）：F05-01 包页 15+15 链接节；F05-02 域分布重算 43 标签（原 50 失真）；F05-03 累计口径 **114 distinct 行**（B01/R01=25, R02=25, R03=25, R04=24, R05=15——live DB 权威，推翻此前 82/97 估算）；F05-04 Hub R05 条目 + 包页 FR2 修复轮节；F05-05 链接伪影。
- **坏链接根因（Coordinator 教训）**：代写 payload 时 `[URL（注记）](URL（注记）)` 形态被 Notion 拆 href——今后代写链接一律「简洁文本 + 纯净 URL + 注记在链接外」。
- 过程事故 2 起（update_content 误替换 Handoff 节、记忆标题行）均同轮补救 readback 确认。
- R01 在 DB 内 BatchID 为 legacy 名 B01（Hub 有 canonical rename 说明）。
- 下一步：FISH-R05-FR2-R2 窄域复核（电鳗页+链接节+统计复算，Evidence Reviewer tab 首个任务）→ PASS 则 FR3。FISH-MAINT-FIX-001b 仍在 researcher 队列。
