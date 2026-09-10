# CENSUS-B2 Batch Report｜CRR 首考批（thermal/季节/Field）

status: **INDEPENDENT_REVIEW_REQUIRED**；validate PASS（programs=20 stories=10 merge_tests=32）
盲冻结 2026-09-10T14:10:54Z（coordinator commit 6928aed 锚定）；判同段经「直接继续」指令执行。
分段执行模式：盲重建段（选样+fetch+冻结）→ 节点回执 → commit 锚定 → 判同段。

## 输入

B01 thermal/季节 ×3（狗鱼 S19 产卵深水回流/玻璃梭鲈 S02 季节重排/褐鳟 S12 季节脉冲）+ R02 ×6（北极红点鲑 S25/欧白鲑 S04/佛雀鳝 S17/剑旗鱼 S23[2D 定向样本]/鳙鱼 S09/鲱鱼 S02）+ R03 鳜鱼 ×1。**R03 输入状态裁决**（coordinator，依据 FISH-R03-RECON-001+FISH-MAINT-FIX-001）：可用；DB 属性 Independent PASS 为权威，正文 REVISE 为历史残留（清理转 researcher 队列）；MDF 两程序 frozen_status_confirmed 留痕（programs/program_revisions/manifest）。
鲢鱼 S07 与鳙鱼同型对照不建体；库内无 Pike Winter Relative Refuge Story（结构性发现，见 HRQ-B2-02）。

## 核心结论

### Registry v3→v4（9 族）

| 族 | B2 变化 |
|---|---|
| CRR | +10 non-match，**仍 0 成员**——三批累计 25 non-match；**真首考输入通道问题转人类裁决（HRQ-B2-02）**：Pike/Bass 深挖产物是方法页非 Story，wild 库 thermal 类全部 premise 绑定切换形态，无 FeasibleSet→RelativeRank 形 |
| SINGLE | +8（habitat 因子多型 + **food_field 场实例**继 B1 chemical_gradient） |
| PLAIN | +2（WAL、MDF；槽位数 2 在轴内） |
| TYPED | +8（MDF=motion-triggered 强实例：静止不触发/移动触发追捕） |
| **FOOD_FIELD_FEEDING_RESPONSE**（新） | 2 成员（鳙鱼 canonical+鲱鱼直验无字面差异）——**evaluand=食物场+RETURN=FieldFeeding**（B1-LAM 判例同型真差异）；与 CUE_GUIDED 互记 non-match（同场 evaluand、程序目的不同）；P03 两层登记；HRQ-B2-01 |

- **ΔL_group=0 / ΔL_bake=0 / ΔL_response=+1 / ΔL_quality=0**；merge_confident=20、extension=0、ambiguous=0、full_expansion=0；LAUNDERING=NO。
- **LOCAL_SATURATION_CANDIDATE 素材**（不宣称）：B2 的 10 条 Bake 全被 SINGLE/PLAIN 吸收、ΔL_bake=0——与 B1（+1）相比 Bake 面出现首个零增长批（素材来源=thermal/季节/场类宽度样本；非 adversarial 批，饱和信号未达）。
- 剑旗鱼 2D 定向样本（coverage #24）：迁移驱动未闭合（正文无裁决节），骨架按 premise 绑定切换处理，2D 判据留 representation 线。
- 鲱鱼 GroupStrong/Group-only（库内首个）：census 层无 routing body 证据，语义层判定与 census 正交（记录）。

### 待审/待办

HRQ-B2-01（FIELD 族+P03 两层+opportunity lifecycle）、HRQ-B2-02（**CRR 输入通道，人类裁决**）、HRQ-B2-03（成员扩展备案）。TAR-09（鳙鱼/鲢鱼滤食捕获方式 Product Scope）。

## 产物

batches/CENSUS-B2/：manifest（status 更新见下）/stories(10)/blind_programs(20)/programs(20)/merge_tests(32)/resolver_tests/absence(空)/coverage(空)/program_revisions(1：MDF 状态澄清)/human_review_queue(3)/engine_report/build×2 脚本/run 脚本/worker_self_qa/batch_report。仓库级：registry **v4**、discovery_curve +B2 行。

上下文余量 ~6%——**建议 B3 前换会话续接**（角色记忆+registry v4+批档为恢复锚点；本会话已三批+两修复轮，上下文压缩整理已做过一次）。

BATCH_ID: CENSUS-B2
