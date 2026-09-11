# BATCH｜CENSUS-B5-REV-001（ARTIFACT_REVISE → 修复闭环）

- scope：CENSUS-B5 全批档 + curve B5 行；baseline=registry v8 + B4 先例 + 判例库。绑定 commit 3455cf5。
- proves：四态 169=43 MC+9 EXT+65 NEW+52 AMB 实数；名义扩容可复算（TYPED 117/GUARD 17/CRR 127）；盲体-终体 hash 104/104 守恒；AMBIGUOUS 双拒绝与 B4 先例同态；anchor 值 Story 可推导。
- findings：F1（blocker）manifest 输入构成 11/41 失实（实测 45 包裹+7 纯正文——笔误撞数）；F2 registry_opened_at 无值；F3 HRQ 指针不一致；F4 盲体提案语汇残留（观察）。
- 修复：fix commit 4f4b016（F1-F3 登记+词例修正；裁决与计数零改动；validate PASS 104/52/169 + fixtures 12/12）。coordinator git 核 diff 后闭合，未另起 PATCH 复审（登记轮零数据面）。
