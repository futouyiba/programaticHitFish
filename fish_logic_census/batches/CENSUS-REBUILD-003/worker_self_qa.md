# CENSUS-REBUILD-003 (RB-3) Worker Self-QA

状态：WORKING / NOT AUTHORITY / NOT PROMOTED ｜ Self-QA（R2 §12）——独立审前的工序自检，不冒充独立审核。

## 1. 盲纪律时间线（§2.1）

- 118 真形体首冻：**2026-09-14T06:18:50Z**（build_blind_programs.py；sha256[:16] 逐条记入 blind_hash）。
- REV-RB3-001（registry 开后判同准备期发现）：4 特例条目 surface/return_type 契约标注修正（queue 4 特例条目 surface 登记全为 Bake——首版误标 Response；ARO-RESP return 命名对齐 GA Bake 投影风格）——face 标注非判同信息（body 结构零变更）→ 二冻 **2026-09-14T06:21:24Z**；program_revisions.jsonl + manifest freeze_history 双留痕；判同四态前后不变论证（修正只涉 face 标签/命名契约，body 步序/轴/分支/return 语义域不变）。
- stories.jsonl/manifest 写出 06:19:32Z（盲段收尾产物）。template_registry.yaml 首次打开=run_merge_tests.py 运行时（判同段，只读——sha256 前后一致断言在脚本内）。
- 盲体语汇扫描：118 条 sketch/premise/open_sem 无族名/提案/立族语汇（F4 纪律——程序化扫描 0 命中）。

## 2. 覆盖与计数对账（四方一致）

- queue 输入 118 = AMB 第 4 层 110 + C9 4 + brooted 2 + form_hold 2 ✓（queue_ids.json 逐条映射，species_id 全集断言）
- 118 = derived 116 + reused 2（FGA4←RB-2 FGA / RHM2←RB-1 RHM——双 story 内容近似复用轨）✓
- 118 = MC 77 + NEW 40 + NOS 1 + AMB 0 + EXT 0 ✓（merge_tests.jsonl 118 行）
- MC 77 = TS 50（轴段 29+field 场浓度 19+RHM2 复用 1+TIL3-RESP 1）+ NO 8 + GC 7（6+FGA4 复用）+ GA 9（第 4 层 7+CSL/CSN1-RESP 2）+ ZS 1 + ST 1 + LA 1 ✓
- NEW 40 = FF 8 + SF 27（RB-1 提案形状累积，related_proposal=HRQ-RB1-02）+ C9 4 新形状 + BROOD 1 退化链形状 ✓
- curve 行：118,118,77,0,5,0,...——n_new_template=5 为 distinct 口径（C9 4+brooded 1；FF/SF 35 条为 RB-1 提案形状累积不占 distinct——RB-2 口径沿用，随行声明于 build_census_outputs.py 注释与 HRQ-RB3-02）✓
- validate_batch PASS；fixtures 12/12（项目 venv）✓
- registry v9 零改动（run_merge_tests 内 sha256 前后断言+判同后复测）✓；discovery_curve.csv 幂等追加 1 行 ✓

## 3. 逐鱼推导工序抽检（§5/§6.2）

- 全部 118 项 derived/reused 均有 basis 顺序推导逻辑（主句语序/CSV 锚/B 文件因子集+特化锚三源至少一源直证；0 order_undetermined——R01-R05 残余 story 均有可用主句）。
- 抽检 5 条：WAL2（视觉生理特化先行→NO 槽形）/BKC（食物载体先行 FF）/RED2（两独立维 LA）/CSN1（B 文件 §0 锚点直证 GA）/TNS（identity-only 低置信 TS 单步）——各条 basis 与 body 步序一致。
- B 文件序声明（约定序）零直接采用：凡引用 B 层处均标注「受限还原不采/因子集可用/独立同序确认」三者之一；C9 四鱼与 RS1 冻结体对照均为重排产物。

## 4. 同鱼对账（envelope 指令）

- 品系轨 4（KOI/MIR/WRC/RTL）+鲫系 2（GCR/WCR2）：TS 同形——RB-2 品系开放项闭合（KOI 本体补证同形）。
- 双 story 复用 2（FGA4/RHM2，reused_from 留痕）；双 story 独立消费+去重联动 10 组（见 HRQ-RB3-01）。
- CLC 双 story 分层（B5 NO 形/R03 TS 形）=证据分层记录（非冲突）挂 HRQ-RB3-01。
- **冲突数 0**（envelope 目标达成）。

## 5. 特例产出（registry 零改动）

- C9 终裁提案（HRQ-RB3-03）：原 C9 候选族撤案（4/4 分散）；4 新形状证据（BLU 结构先行四步/RBP 三步温度中置/HNC 门化四步结构先行/ARA 门化四步温度次置——HNC vs ARA 为 ORDER 差异）。
- brooted 终裁提案（HRQ-RB3-04）：ARO=退化链维持（携带型锚同构罗非；B5 全链盲形降级为契约套用；口哺期摄食张力留开放项）；TIL3=分面记账读法修正（雌口哺 brooded 边界确认/雄领地非 brooded TS）。
- form_hold 终裁提案（HRQ-RB3-05）：CSL/CSN1=anchor 形式 fry_school（larvae 直证/B 文件 §0 直证；egg 阶段 open 保留——与 MUT 批 nest 落位注记分歧以 story 直证为准）。
- GAR1=Bake 面显式无程序（BOUNDARY-DECL 直证；absence_claims 记录——非四态单列，报告计数明示）。

## 6. 已知边界/移交独立审

- MRG 的 GC→NO 结构变更=B 文件自身边界条款兑现路径（「换 NOCTURNAL 标签=结构变更需重审」——本批兑现即该重审，独立审复核点）。
- C9 四形中 RBP/HNC/ARA 的 engine 同签名（ST/ZD）语义层 non-match 判法（轴类别序列）——沿用 RB-2 判例，独立审确认。
- CSL egg 阶段形式 open（HRQ-RB3-05 开放项）。
- v10 mutation 待独立审另批：RB-1 6 提案+RB-2 16 移动/FILTER_FIELD 空置+RB-3 C9 4 形状+brooded 1 形状+TIL3 分面+CSL/CSN1 anchor 落位（fry_school 3→5）可并案。

## 7. 停点

Self-QA+validate PASS+fixtures 12/12 → batch_report → INDEPENDENT_REVIEW_REQUIRED → 停。
