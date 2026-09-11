# CENSUS-B5 Batch Report｜R08+R09 普通层双包批（52 Story）

status: **INDEPENDENT_REVIEW_REQUIRED**；validate PASS（programs=104 stories=52 merge_tests=169）；fixtures 12/12。
盲冻结 2026-09-11T08:04:47Z（blind_programs.jsonl 文件系统精确时刻，104 条 hash 全验证+registry_seen=false）；registry v8 读取在后（manifest 双时间戳）；判同产物随后写入；program_revisions 空（判同段零 body 改动）。
执行模式：重启 fresh spawn 单轮（前次运行快照抓取完成后进程退出丢失全部中间状态；本会话 SNAPSHOT_ONLY 重建——input_snapshots/ 52 story+2 packet 为全部输入，未访问 Notion live）。管线偏差（盲段见 B4 build 脚本与角色记忆中的 B4 盲体形状/族名散文）已在 manifest bias_declaration 声明+缓解。

## 输入

FISH-R08（§4 优先级 6 收尾普通补齐 26：billfish/金枪鱼 3-4 例、白鲑系、鲑科生活史多型、食人鱼科植食反差×2、石巢系第 3 例、耐冻蛰伏系、名实分离/杂交身份）+ FISH-R09（优先级 6 续 26：鲟科第 4 例、慈鲷系 4、鲫系 3 含雌核发育、稀有鳟系 3、白鲑第 5 例、身份层 4 行、拟鲤双行、鲤科鱼食反差、洪水系第 3 例、吸盘底栖、岩缝护卵）。两包均 FR3 CLOSED；对账：packet 声明 26+26=52 = input_snapshots story_*.md 实际 52（零差异）。语义输入 P01/P04/P05（B3 同 URL 冻结快照复用）+P02（story FR 解释承载，无独立快照）。
快照转写：11 份完整包裹+41 份纯正文（十节+Sweep Log 脚本核验 52/52 零缺失）；计数口径差异 1 项已记档（R08 packet 声明 P04×4 vs story 字段实际 3 例——疑 CSL 护卵+护幼分开计，按 story 字段 9 例 P04 处理）。

## 核心结论

### Registry v8 状态下裁决（本批零 registry mutation——全部挂账 HRQ；21 族不变，名义 162 不变）

| 面 | 裁决 |
|---|---|
| **Bake 52** | **AMBIGUOUS_NEEDS_EXPANSION 52**（vs SINGLE v1）：engine raw 仅 op 名字面（骨架同构平链）——但 v1 canonical 已被 RS1 61/61 证伪（HRQ-RS1-01 pending），本批 Story 层输入与 B1-B4 同层（RS1 已证明该层平铺形系统性收敛）。不 MC（不对被证伪 canonical 制造确信合并——B4 25 成员已陷 moved_pending_review 同态）；不 NEW 立族（平铺输入立族=RS1 反例）。双分支预案入 **HRQ-B5-01**：v1 保留→按 B4 先例升 MC（名义 66→118）；拆分批准→对新族全 non-match（engine 已实测 BRANCH 等真差异）+真形待 B 表达顺序还原另批。vs CRR：non-match 52（累计 127，连续第 5 批 0 成员——HRQ-B2-02 维持）。vs 11 新族（RS1 9+RP1 2）：分组 non-match（每族 52 程序 engine diff 完全一致 distinct_diff_sets=1） |
| **Response 43 typed** | **MERGE_CONFIDENT 43**（TYPED 74→117 名义 pending review）：普通层标准 typed；强实例=SAF 喙击打攻击工具 typed（Story 明言改造目标可捕获性非生成机会）/RHM 植物叶离散善件目标/ASP 桥墩堰坝结构伏食/SVT 端足类专食原文/INC+WST 停食洄游第 3/4 例（P05 状态抑制 premise 维持，动机归因 open 联动 HRQ-B3-01）；MEDIUM 推算 13 例（P01 承载 7+亲本/鲫系复用 3+形态/同属推断 3）。**HRQ-B5-03** |
| **Response 9 guard** | **TEMPLATE_EXTENSION_CANDIDATE 9**（GUARD 8→17 名义 pending review）：9/9 骨架同构直验（deps 位形/branches/RETURN 与 canonical 一致；engine raw 仅槽名/合并步标名字面——B4-HNC 同型）。anchor 9 新值提案（mouthbrooding_male 携带型/nest_pelagic_larvae/gravel_ridge 石巢系第 3 例异属/rock_nest_fan/cave_ceiling/nest_biparental/flood_spawn_male_guard/egg_mass_rock/rock_crevice_fan）+ **guard_participant(male｜biparental) NEW 轴提案**（MDC+JGC 双亲例跨属重复）+ fan 扇护子动作语义（ROB+AMK 跨科重复——供氧 typing vs 结构元素 open）。跨族互证：vs STATE_GATED（§9.2 两拓扑边界第 5 例）+ vs TYPED（单路径边界）双 non-match 维持。**HRQ-B5-02** |
| Group/Quality | ΔL_group=0 / ΔL_quality=0（群结构事实/繁殖集群/同种多型/独居全排除——52/52 显式；无 Quality 证据 B0-B4 基线） |

- **ΔL 全零**（group/bake/response/quality）——但 ΔL_bake=0 的性质与 B2-B4 不同：52 AMBIGUOUS 是归族挂起（blocked by HRQ-RS1-01）而非饱和证据；absence_claims 记 BAKE_MEMBERSHIP_PENDING_SPLIT_RULING（非强宣称）。
- **顺序推导纪律执行**（§5.1）：52 Story 逐条顺序扫描，无一面内 early-return 判断链；时序均为 lifecycle/季节/洪水/昼夜 premise 配置级（判例④/P05 状态抑制——INC/WST 停食洄游按 P05 判例不落 P04）。每条骨架含顺序推导注记。
- R09 身份层 4 行（虎纹鳟/工程鲫杂交+湖拟鲤双行+常见拟鲤 A 行保留）全部按机制复用推算 MEDIUM 或同种同源处理，身份裁决归 FR 线；CMR/LKR 同种双行两程序去重联动注记（Cross-Batch）。

### 待审/待办

HRQ-B5-01（Bake 52 归族挂账：HRQ-RS1-01 联动双分支预案+B4 25 成员同态联动+新族 non-match 含义限定）；HRQ-B5-02（GUARD 9 例 extension：anchor 9 值+participant 轴+fan 语义+携带型 anchor 语义域+非建造 anchor 类一致性）；HRQ-B5-03（TYPED 43 扩容备案：MEDIUM 13 分层+停食 2 例 STATE_GATED 升级条件联动+双行 2 例+身份 4 例+packet 口径差异+顺序纪律确认）。TAR：零新增（TAR-01..12 沿用；9 例 S1-EO 为 FR 线已知 open 非 census 受阻——不立 TAR）。

## 产物

batches/CENSUS-B5/：manifest/stories(52 含 S1-S11 逐项映射 572 项)/blind_programs(104)/programs(104)/merge_tests(169=52 AMB+65 NEW[52 CRR 单条+11 新族分组+2 guard 跨族分组]+43 MC+9 EXT)/resolver_tests(NO_NEW_RESOLVER)/absence(归族挂账说明 1 条)/coverage(空)/program_revisions(空)/human_review_queue(3)/engine_report/build×3 脚本/build_stories/run_merge_tests/worker_self_qa/batch_report + input_snapshots/（fetch 脚本+日志+packet×2+52 story+urls×2）。仓库级：registry **零改动**（v8 维持——章程：mutation 由独立审通过后另批）、discovery_curve +B5 行。

## 独立审交接

- **scope**：CENSUS-B5 批档全部产物（52 Story/104 盲程序/169 merge_tests/3 HRQ/absence 1/engine_report/manifest 与脚本）+ discovery_curve B5 行。
- **baseline**：registry v8（21 族 CANDIDATE，名义 162 程序/466 判同——本批零 mutation）；B4/RS1/RP1 判例链与 authoring_work_standards §2/§5。
- **proves**：52 Story 逐 S 项全覆盖无静默丢弃；盲冻结时序可证（双时间戳+hash+program_revisions 空）；engine raw 全量留痕（含 11 新族 572 程序族对逐对实测+一致性断言）；计数四方对账一致。
- **does_not_prove**：Bake 52 程序的真实程序体形态（Story 层平链是收敛形——真形需 B 表达顺序还原输入，RS1 范式）；9 guard extension 的轴属正确性；MEDIUM 13 例的食性引文闭合。
- **open_findings**：HRQ-RS1-01 与本批 Bake 归族的双向联动（本批裁决依赖其结论）；GUARD anchor 轴膨胀速度（B4 +1 → B5 +9 候选）是否触发轴域重审；packet P04 计数口径差异。
- **verdict**: 待独立审（independent-narrow-reviewer）。

BATCH_ID: CENSUS-B5
