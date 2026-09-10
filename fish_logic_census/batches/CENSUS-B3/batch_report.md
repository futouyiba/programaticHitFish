# CENSUS-B3 Batch Report｜R06 洄游/掠食批（28 Story）

status: **INDEPENDENT_REVIEW_REQUIRED**；validate PASS（programs=54 stories=28 merge_tests=82）；fixtures 12/12。
盲冻结 2026-09-10T20:42:21Z（blind_programs.jsonl 文件系统精确时刻，54 条 hash+registry_seen=false）；registry v4 读取 ~20:45Z；判同产物 20:46-20:47:31Z。
**执行模式偏差（B3-F-0）**：fresh spawn 单轮，B2 的「冻结→回执→coordinator commit 锚定→判同」分段不可插入 commit——改为双时间戳+内容 hash 自证（blind 文件内容判同段零改动，program_revisions 空）；coordinator commit 后 VCS 时序可复核。此偏差需 reviewer 认可。

## 输入

FISH-R06 全量 28 Story（FR2 两轮 REVISE 闭轮+FR3 CLOSED AUTO_CONTINUE，ARTIFACT_APPROVE）：鲑系洄游 10+淡水掠食 14+海水掠食 4。语义输入 P01/P04/P05 pattern 页+FR3 裁决包（判例①停食洄游/判例②frenzy 负知识）。
**输入通道注**：本机 census worker 工具白名单无 Notion MCP——经 coordinator 已配置的 claude CLI headless（读已授权 notion MCP fetch）只读获取快照 35 份入 input_snapshots/（fetch_notion.sh）；headless 转写核验 28/28（标题+BatchID+Sweep Log 完整；3 份 properties 标点差异/2 份省略头已注明）。Snapshot 标注纪律遵守（非 live Authority 冒充）。

## 核心结论

### Registry v4→v5（10 族，名义 58→112 程序）

| 族 | B3 变化 |
|---|---|
| **STATE_GATED_MULTI_PATH_RESPONSE**（新） | 2 成员（CHU canonical+SHA 直验）——**停食洄游双 Path（FR3 判例①）**：状态 IF 门互斥切换摄食 Path/非摄食攻击 Path，RETURN=TargetFeeding \| NonFeedingStrike；engine 6-diff 真结构差异立族；与 GUARD 族双向互记 non-match（∥ 同刻并行 vs IF 门互斥——§9.2 multi-path 的两种拓扑）；HRQ-B3-01 |
| GUARD_CONFLICT_DUAL_PATH | +3（4→7）：ARA 沙巢/RBP 树根卵/WEL 雄巢——**envelope 压力点裁定：GUARD 扩容 not PLAIN**（骨架同构：deps 位形 [ [],[],[0,1],[2] ] 与 canonical 一致，engine raw 仅槽名/合并步标名字面）；intruder_evaluator_context 轴新实例 sand_nest/tree_root_eggs/male_built_nest；HRQ-B3-02（FR3 P04 三问抽验联动） |
| SINGLE | +26（15→41）：P05 阶段/周期/季节绑定 position 15（洄游系+洪水周期+季节重排）+静态 structure 11（B2 FGA 同型） |
| TYPED | +23（27→50）：强实例 TAR 水面取向/TAI+GW 陆生水面呈现/PBF 温血 typed fact/AST 鲟科须探第 3 例/GT 夜礁缘；PAY/SHO/DS 形态-同属-同科推算（MEDIUM） |
| CRR | +26 non-match（累计 50）仍 **0 成员**——洄游/掠食层无 refuge 形（HRQ-B2-02 维持人类裁决） |

- **ΔL_group=0 / ΔL_bake=0 / ΔL_response=+1 / ΔL_quality=0**；merge_confident=52、extension=0、ambiguous=0；LAUNDERING=NO。
- **连续第二个 ΔL_bake=0 批**（B2+B3 两宽度层 36 条 Bake 全 SINGLE 吸收）——LOCAL_SATURATION_CANDIDATE 素材累计，仍未宣称。
- envelope 三压力点全部落定：①停食洄游双例→STATE_GATED 新族（§9.2 同构但不并入 GUARD——拓扑真差异）；②P04 护巢组→GUARD 扩容（anchor 轴内）；③鲑科洄游 10 条 lifecycle premise 配置级（Bake 全 SINGLE position 绑定，migration 表达与 representation 线 MIGRA 批正交——非 census 新结构）。
- FR3 判例②执行：RBP frenzy 负知识（S3 排除映射+Group 面 NO_SURFACE 理由，不买 Group Mode）。

### 待审/待办

HRQ-B3-01（STATE_GATED 新族+P05 判例①两层+两 multi-path 族家族关系）、HRQ-B3-02（GUARD 扩容+anchor 轴+P04 三问抽验回归联动）、HRQ-B3-03（成员扩展备案）。TAR-10（停食洄游 strike 动机归因+钓法引文——升级三条件之①）、TAR-11（ARA 换气暴露 opportunity/呈现语义）、TAR-12（PBF 热生理呈现面意义）。

## 产物

batches/CENSUS-B3/：manifest/stories(28 含 S1-S11 逐项映射)/blind_programs(54)/programs(54)/merge_tests(82)/resolver_tests/absence(空)/coverage(空)/program_revisions(空)/human_review_queue(3)/engine_report/build×3 脚本/worker_self_qa/batch_report + input_snapshots/（fetch 脚本+35 快照）。仓库级：registry **v5**（10 族）、discovery_curve +B3 行。

BATCH_ID: CENSUS-B3
