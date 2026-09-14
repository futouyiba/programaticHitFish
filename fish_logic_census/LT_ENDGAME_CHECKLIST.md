# LT 线收官清单（持久驱动——任何会话恢复后从本文件继续）

状态基线：RB-1/2/3 全部 APPROVE 已推送 ｜ registry v9（18 活族+3 退役）｜ 终局重跑 303/303 全消费完毕
用户指示（2026-09-14）：RB-3 跑完 → 全部审完 → 统一 v10 mutation；Notion 上传不可忘记。

## 待办（按序）

- [x] **1. RB-3 独立审** ✅ 首轮 ARTIFACT_APPROVE（8a5bf47+6a47078+F2/F4 卫生已推 0fdee44；审校卡在案；F1 追溯 freeze_marker 留 v10 补）
- [ ] **2. 轻量 Notion 同步**（RB-3 过审后，用户已确认要）：入口页文字数字更新（RB 系列结果、族数口径 18/23/28）——不重传 embed
- [x] **3. v10 统一 mutation** ✅ 已执行（commit 1f9f5fd；批档 batches/HRQ-V10-MUTATION-001/；停点 INDEPENDENT_REVIEW_REQUIRED——审后随第 4 步推送）：
  - RB-1 六族入册（FF 34/SF 61 名义/TB 4/TU 2/SL 2/FS 2——含 RB-2/3 累积；**SL 工件实数 2 非 4**——envelope 口径 vs 工件偏差已在 batch_report §4 披露留独立审）
  - RB-3 五新形入册（BLU 结构先行/HNC 门化/RBP 三步/ARA 门化温度次置/BROODED 退化链族）+ C9 撤案注记
  - 族移动执行：RB-2 16 条 + RB-1 7 条（23 条记录=16 成员条目迁移，moved_from 注记）
  - FILTER_FIELD 空置（VACATED）
  - order_provisional 解析：8 链族 order_confirmed + 3 族无 RB 证据如实保留 provisional（envelope「12 族」口径偏离已披露）
  - TIL3 分面记账修正（雌退化/雄领地）、ARO 退化链确认、CSL/CSN1→fry_school（fry_school 3→6 net：+CSL/CSN1+ARA 规则重落）
  - 跨阶段 anchor 取值规则统一（HRQ-RB2-07 主形式/直证：JDP/ARA/CSL/SMA1）
  - KOI 品系闭合注记（RB-2 开放项）
  - RB-2 批内生成器常量 7 处旧口径顺手同步（防重跑再生）+ RB-3 追溯 freeze_marker 补建
  - mutation_provenance 全记录；HRQ 全队列关闭对账（18 条全 resolved——batch_report §3）
  - 活族终态 28（Bake 23+Response 5）；curve 零改动；validate PASS+fixtures 12/12+幂等守卫实测
- [x] **4. v10 独立审** ✅ 三轮闭环 APPROVE（1f9f5fd→4ccf8a1→e49c436 已推；审校卡在案）
- [x] **5. v15 终版全家桶** ✅（仪表盘 v15 §10 总表+§11 详情已推 69ba74e；手册主页+28 子页+总表已建；入口页终版+embed v15+总表已更新）：HTML 重生成（终族数/成员数/终裁结论/三批 RB 曲线）→ 上传附件 → Notion 三页更新 + embed 换新（**用户明确要求不可忘记**）→ 审校卡补齐
  - **用户验收标准（2026-09-14 追加，硬性）**：
    a. 进度 Notion 文档与速览 HTML 均含「逻辑模板类型总表」——**一行一型**（类型名/面/成员数/中文特点），中文可读懂每型大概什么样
    b. 表内每行**可点链接直达**该型的 中文伪脚本章节 与 配置表章节——Notion 用每型一子页（手册子页树+mention-page 链接），HTML 用同页锚点（#type-id）跳到该型详情段（详情段含中文伪脚本[渐进累积体]+配置表[参数轴/字段]）
    c. 数据源=registry v10 canonical+axes（确定性生成，不手写漂移）
- [x] **6. LT 线收官报告** ✅（入口页 What's New 收官版；本地 v15 推送后闭环）（终态数字 + 方法论沉淀）

## 已完成（勿重做）

对齐批 APPROVE 已推（dfab826/506231d）｜ RB-1 APPROVE 已推（9e58bb6/5bf0694/d0db89b）｜ RB-2 APPROVE 已推（e1adf08…96cf145/2c3bc94）｜ HRQ 裁决 8 项+语义裁定已固化（章程/§6/角色记忆三层）
