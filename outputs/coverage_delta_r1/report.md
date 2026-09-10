# REP-COVERAGE-DELTA-001｜47 条 CoverageDelta Candidate 四面表达覆盖判定

> 本文件为 worker 报告全文逐字落盘（转写者：Coordinator；来源：agent 返回结果，2026-09-10）。
> **Coordinator 转写勘误（验收 F2 澄清）**：下文「14 聚类」为全批 47 条的聚类总数（K8/K9/K10 含全部 5 条非 NO_ACTION）；42 条 NO_ACTION 分布于其中 11 个聚类（K1-K7、K11-K14）。速览文件中「42 条分 14 聚类」为转写歧义，以本句为准。
> **引用纪律（验收 F3）**：本报告引用的节号以报告头部基线声明所指归档/live 版为准；因主页存在重复编号（§7×2、§8×2），后续引用须「节号+节标题」双限定。

`Status：WORKING / REPRESENTATION COVERAGE JUDGMENT / NOT AUTHORITY / NOT PROMOTED`

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 输入来源 | (1) 47 条全名单+判定框架：tmp/covdelta_input.md；(2) 表达结构权威：live Stress Test R1 主页转录（REP-CLARITY-FIX-001 后版本）；(3) 机制裁决：outputs/batches/KNIFE-READ-001.md（Knife R0 归档）；(4) 契约样板：outputs/usable_forage_contract_r0/README.md |
| 对应执行面 | 判定跨全部四面（Group Routing / Bake / Response / Quality Selection）；本报告为判定报告，不产出新的表达工件 |
| 基线声明 | SNAPSHOT_ONLY——判定基于本地转录/归档；live 漂移时以归档版为准 |
| 判定边界 | 候选只有 Story 标题 + 模式注记，无正文；判定 = 标题语义对四面结构的映射，不重审现实语义。6 条带「需正文确认」子备注（#9/#10/#24/#31/#42/#47），均不改变主判定档位 |

**Breaker 编号映射假设（显式声明）**：「Group §22 / Quality §23」按 live 主页 §13 的转述对应 15 Case Authoring Visualization R0 页 §21–24.1 的 Breaker 结论——Group §22 = `NO_DEEP_GROUP_ROUTING_BREAKER_FOUND / GROUP_CONFIG_EXPRESSIVE_BUT_HARD_TO_READ`（→ G-T1 DECLARATIVE ROUTING VECTOR，L_group≈1）；Quality §23 = `NO_QUALITY_SEQUENCE_BREAKER_FOUND / QUALITY_PARALLEL_MODIFIERS_SUFFICIENT`（→ Q-T1，L_quality≈1）。（验收 REP-COVERAGE-DELTA-REV-001 已核对该映射三方逐字一致。）

## 1. 判定汇总

| 档位 | 计数 | 条目 |
|---|---|---|
| NEEDS_REGRESSION_SAMPLE | **3** | #24 剑旗鱼、#35 蒙古红鲌、#42 大眼金枪鱼 |
| NEW_CONFIG_COVERAGE | **2** | #13 海七鳃鳗、#47 电鳗（R05-FR3-pending 前提） |
| NO_ACTION | **42** | 其余全部（分布于 K1-K7、K11-K14 共 11 个聚类） |
| INSUFFICIENT_INFO | **0** | 无整条语义不足以判定者；6 条带子备注（见 §6.2） |

NO_ACTION 42 条的吸收面分布（主落点，一条可跨面）：

| 面 | 吸收结构 | 条数 |
|---|---|---|
| Group Routing | 条件原子 V1–V4 + RuleSet R1/R2 + 类型化状态枚举 + 多路由 Share Vector（§7/§13.1/§15.1） | 12 |
| Bake | BA-T1+DynamicSpatialSlot / BA-T2 锚模板 / BA-T5 饵群耦合 / unary-2D Profile 轴实例 / OV-T1 | 26 |
| Response | R-T1 Cap / R-T2 双通道 / 窄接受 Profile / CueFamiliarity 轴 | 若干（多与 Bake 共享） |
| Quality | Q-T1 Eligibility/Affinity Profile + 并列 Modifier | 0 条新增需求；#35 为回归样本 |

§15.5 Expression Gate（中间依赖拓扑）在本批 47 条中无定向样本——没有任何标题语义要求作者编辑中间结果依赖。

## 2. 四面缺口清单

### 2.1 Group Routing 面——无缺口

全部路由语义可被现有结构吸收：条件原子 V1–V4（含窗口化计算事实的参数列，「连续均温(5天)」先例）、RuleSet R1/R2（AND/OR/NOT + 嵌套）、类型化状态枚举先例（ReproductionState / ThermalStressState / FrontPhase，§13.1）、同条件多路由 Share Vector（§7 契约 + §15.1）。性别相关水深（#6）、中心—边缘分配（#2）这类「按个体属性分位置」语义，在供给份额粒度上 = 同一条件命中下两条路由各分 share、各绑不同 Group 的 Bake——share-vector 模型天然支持，不需要逐个体属性事实。

关联残留（非四面结构缺口，live 主页已自带 TODO）：个体属性（性别/成熟度）可见性 Contract——Active Spawning §4 明文「当前没有独立 Sex / Maturity 个体属性 Contract……不借 Quality 字段代替」。#2/#3/#6/#31 的份额级表达不触发它。

### 2.2 Bake 面——无新模板/新列缺口；有上游事实族义务（登记项）

吸收清单（按聚类）：
- BA-T1 + DynamicSpatialSlot：附着/扰动斑块（K3）、预投饵斑块（#1）、低光/结构伏击（#29/#41，§11.5 先例）、礁-流过渡带（#45）、洪泛漫滩（#36）、漂浮结构饵斑（#38，§11.4 浑水先例）。
- BA-T2 繁殖/育幼锚模板：K4 全部（#3/#14/#16/#22/#26/#31）——锚差异 = 上游 Anchor Resolver 实例扩充（巢/稚鱼群/口孵群/活蚌床/岸滩产卵场），§11.2 Fry Guard 泛化与 Active Spawning §2 的 Anchor Resolver 槽已明示「新增 resolver 实例 ≠ 新结构」。
- BA-T5 Forage Field Coupling：K1/K2 移动饵群与浮游食场（ForageSchoolIntensity gate + ForageTargetAlignment；「field 可随条件移动」由上游 Forage Resolver 承担，§11.3 先例）。
- 轴实例而非结构：盐度（#27，Knife §10 已记 2D_PROFILE_PRIMITIVE_REUSE +1；落法 = unary/2D Profile 新实例，非新结构）、DO（#36/#41）、流速/水位（#25/#33/#39）。
- 底质附着 prey class（K3/K2）：UsableForageAvailability 契约的 prey_fields 绑定对「水柱场 vs 基质表面」载体无感知，两类压缩进同一契约（P06 Compression Candidate 的表达侧确认）。

上游事实族义务（建议登记 Snapshot 事实清单，非四面表达缺口）：底质扰动痕迹族（#5/#11/#23）、玩家打窝斑块族（#1）、附着生物量事实族（K3）、昼夜迁移饵场族（#24/#42 的 Resolver 读法）。这些到达时触发 forage 契约 R1 README §6 的 SNAP allowlist 收窄义务。

### 2.3 Response 面——唯一实质缺口：呈现 Cue 轴模态枚举缺「化学（味型/信息素）」与「电场」轴（NEW_CONFIG_COVERAGE，聚类 K8）

核对：live 主页全文对 味/嗅/化学/信息素/scent/odor 与 电场/electric 的出现次数为 0（验收复扫确认：唯一 scent 子串命中为「Winter Quiescent」假阳性，已排除）。现有 cue 输入枚举（从各表归纳）：拟饵尺寸/silhouette、速度、轨迹（moving/search/erratic）、水层与相对位置、振动（@VibrationProfile）、闪光（@FlashProfile）、deflection、abruptness、proximity、pursuit demand、CueFamiliarity、侵入距离/持续时间/威胁 Cue（Guard）。化学与电感知模态无对应轴。

列级缺口规格：
(1) 新表列结构——不新增列结构，扩充两类行：Cue 轴 Profile 槽位行（挂 §17.2 Reaction Profile 表同款两列结构「配置项/含义」，加两行）：`@ScentCueProfile`｜味型/信息素强度→触发适配（化学模态轴，#13）；`@ElectroFieldProfile`｜拟饵/环境电场特征→触发适配（电感知模态轴，#47，前提成立才立项）。条件原子「事实/计算项」枚举值（Grammar 5.1 复用，V2/V3 形态即可，零新列）：`BaitScentIntensity`（当前呈现的味型/信息素强度，上游呈现侧计算事实）、`LureElectricField`（拟饵电场特征，同上）。
(2) 条件组合方式：新轴只做 Unary Profile lookup（Primitive Admission Ladder P0 阶，Knife §11），并入既有 Feeding/Reaction Channel 的 FIXED_COMBINE；气味×水流输运、电场×水体传导衰减等耦合归感知/环境 Resolver owner，不开放 2D（除非未来出现 §16.5 型不可分离样本）。
(3) 伪脚本形态示例：

```plain text
评价 Feeding Channel：
    读取当前饵 / Presentation Cue（速度、轨迹、水层与相对位置——既有轴）
    读取当前饵的味型强度（BaitScentIntensity——新轴事实）
    用 BaitScentIntensity 查询 @ScentCueProfile
    得到 ScentCueFit

    与 @FeedingProfile 的结果按模板固定规则合并
    得到 FeedingResponse
```

算子标注：合并算子 OPERATOR UNDEFINED — 待机制侧（可循 FIXED_COMBINE Working Algorithm Candidate 先例）；本规格只冻结「新轴为 Unary、Fit 并列输入、无作者可编辑中间依赖」的边界，数值与合并数学不冻结。

### 2.4 Quality 面——无缺口

零条候选要求新的品质结构。体型-阶段资源（#28/#34）由 QT-1 的 Eligibility/Affinity Profile 吸收；#35 是对既有结论（§12.3 LureSize/BaitSizeSelectivity 的非负 multiplier 并列语义）的定向回归样本，不是缺口主张。

## 3. 47 条逐条表

| # | Story | 判定 | 一句理由与指向 |
|---|---|---|---|
| 1 | B01-S53 草鱼｜植食资源与预投饵斑块 | NO_ACTION | 植食资源=forage 契约水草 prey class；预投饵斑块=BA-T1 DynamicSpatialSlot 消费上游「打窝斑块」事实——玩家行为事实属世界侧义务 |
| 2 | B01-S14 褐鳟｜摄食位置竞争与中心—边缘资源分配 | NO_ACTION | 份额粒度=GR 同条件双路由（CoreHolders/EdgeFeeders 两 share 两 Group 各绑 BA）+ QT-1 Eligibility 关联体型档 |
| 3 | B01-S44 罗非鱼｜雌性口孵期间摄食减少与幼鱼回口 | NO_ACTION | 口孵=类型化繁殖状态路由 + BA-T2 育幼锚（§11.2 Fry Guard 泛化）+ R-T1 Cap；雌性专属由 share 表达 |
| 4 | B01-S35 鸭嘴鲟｜重复无奖励刺激的习惯化与食物恢复 | NO_ACTION | 习惯化=§5.6 CueFamiliarity Response Overlay（§17.3 已列输入轴）；恢复动态=上游窗口化计算事实 |
| 5 | B01-S46 黑鼓鱼｜翻底坑与泥云作为持续觅食痕迹 | NO_ACTION | 泥云/痕迹=上游持续世界事实 + BA-T1 DynamicSpatialSlot（§11.4 浑水先例）+ Reaction 轴消费 |
| 6 | B01-S52 大西洋鳕鱼｜繁殖期性别相关水深与未确认产卵潜水 | NO_ACTION | 性别相关水深=GR 同条件双路由 share-vector 拆分（male/female 两 Group 各绑不同深度 BA Profile）；「未确认产卵潜水」为证据分级标注 |
| 7 | B01-S34 鸭嘴鲟｜幼体电感受定位浮游猎物 | NO_ACTION | 幼体阶段=GR 阶段事实路由（C12 先例）；浮游猎物=plankton prey class；电感受定位猎物的模态归感知面 owner（区别于 #13/#47 的呈现 cue 轴缺口） |
| 8 | B01-S20 白斑狗鱼｜横咬、转向吞咽与捕获阶段 | NO_ACTION | 捕获阶段语义归 Encounter/Conversion owner（forage 契约边界表已登记）；四面份额=呈现接受，由 Response Profile 吸收 |
| 9 | B01-S07 鳐雀鳝｜取饵携行、吞咽与挂钩的阶段边界 | NO_ACTION | 同 #8：主语义归 Encounter/Conversion；[需正文]若要求阶段时序可配置，将构成 Encounter 面新槽位主张 |
| 10 | B01-S39 蓝鳃太阳鱼｜小饵低阻呈现与吐饵 | NO_ACTION | 吐饵=Conversion 拒绝；小饵低阻接受=Response 窄接受 Profile；[需正文]若「线感/阻力」为独立 cue 轴，并入 K8 轴枚举缺口 |
| 11 | B01-S32 小口黑鲈｜跟随翻底动物获取被惊出的猎物 | NO_ACTION | 跟随扰动=上游「它鱼扰动事件/斑块」事实 + DynamicSpatialSlot + Reaction 通道（erratic 触发，§17.2） |
| 12 | B01-S24 虹鳟｜鼠形表面饵的地域策略变体 | NO_ACTION | 地域变体=per-instance Profile 重绑定；鼠形表面饵=presentation cue → Response Profile |
| 13 | B01-S49 海七鳃鳗｜生殖化学线索、趋向与陷阱捕获 | NEW_CONFIG_COVERAGE | 生殖化学趋向需 Response 面呈现 cue 轴含化学味型：现有 cue 枚举装不下——列级规格见 §2.3；陷阱=Encounter/装备侧 scope flag |
| 14 | R02-S05 毛鳞鱼｜繁殖上岸与近岸资源窗口 | NO_ACTION | 繁殖窗口=GR 路由 + BA-T2 繁殖锚（岸滩 resolver 实例）+ RR-4/R-T1 Cap；近岸窗口=DynamicSpatialSlot + 时间窗条件 |
| 15 | R02-S13 东方狐鲣｜开放水层追猎与移动饵群 | NO_ACTION | BA-T5 原生样本（ForageIntensity gate + ForageTargetAlignment）；「移动」由上游 Forage Resolver 承担（§11.3） |
| 16 | R02-S11 七彩神仙鱼(橙)｜亲鱼体表黏液喂养幼鱼 | NO_ACTION | 育幼关系=BA-T2 育幼锚 + RR-T2 Defense-only 吸收（§11.2 Fry Guard 泛化先例） |
| 17 | R02-S02 大西洋鲱鱼｜群游产卵与浮游食场 | NO_ACTION | GR 繁殖路由 + plankton prey class + BA-T5/T1；群游集聚由空间 Factor 值域承载 |
| 18 | R02-S09 鳙鱼｜滤食浮游场与水层机会 | NO_ACTION | 滤食浮游场=forage 契约（plankton class + FILTERED_SUM）+ FieldFeeding 语义（C09–C11 先例）；水层机会=LayerProfile |
| 19 | R02-S07 鲢鱼｜滤食水体食物场与非目标捕获边界 | NO_ACTION | 食场同 #18；非目标捕获边界=Response 窄接受（常规呈现近零的 Profile 值域）+ 专项呈现 cue 窗；捕获概率边界归 Encounter/Conversion owner |
| 20 | R02-S01 大西洋鲭｜季节性上层鱼群与移动饵场 | NO_ACTION | GR 季节条件 + BA-T5（上层带=Alignment/Layer Profile） |
| 21 | R02-S03 日本竹荚鱼｜近岸鱼群与水层追猎 | NO_ACTION | BA-T5 + Layer/Structure Profile；近岸=空间 Factor 值域 |
| 22 | R02-S12 七彩神仙鱼(白)｜亲鱼护幼关系（色型不分裂） | NO_ACTION | 标注明示色型不分裂：与 #16 同一表达（BA-T2+RR-T2）；外观色型属资产/品质维度 |
| 23 | R02-S08 鲤鱼｜底质翻拱与资源斑块 | NO_ACTION | benthic prey class 绑定 + 基质/结构 Factor；翻拱扰动事实族义务同 #5/#11（世界侧登记项） |
| 24 | R02-S23 剑旗鱼｜昼夜垂直迁移与深层猎物追击 | NEEDS_REGRESSION_SAMPLE | 攻击 Knife §16.5 2D 判据：若正文确认鱼自身垂直节律（非纯饵群跟随），Layer 最优带随 DielPhase 系统性迁移=「最优区间迁移」型不可分离交互样本；若纯饵群跟随则 BA-T5+上游 diel 饵场吸收。[需正文]「迁移驱动」一节裁决 |
| 25 | R02-S22 准白甲鱼｜急流底质刮食资源 | NO_ACTION | 流速 Factor（@LowEnergyRefugeProfile 流速轴先例）+ 附着 benthic prey class（刮食=口径窗+附着生物量） |
| 26 | R02-S15 乌鳢｜伏击捕食与护幼关系切换 | NO_ACTION | 伏击↔护幼切换=类型化状态互斥路由（§13.1 ReproductionState 先例）+ BA-T1（植被结构 Factor）/BA-T2（育幼锚）各绑 + R-T2 反应主导 |
| 27 | R02-S20 公牛鲨｜广盐性河口进入与机会捕食 | NO_ACTION | 盐度=GR 条件原子（盐度事实 IN 区间）+ unary/2D Profile 轴实例（Knife §10 已记 Temp×Salinity=2D_PROFILE_PRIMITIVE_REUSE +1；落法=新实例非新结构） |
| 28 | 蓝鲨 Iridescent Shark｜养殖边界/体型阶段资源 | NO_ACTION | 养殖边界=population 粒度属性（forage 契约 population_id 粒度，养殖/野生=不同 population 各绑 Profile）；体型阶段资源=阶段路由（C12）+ size window |
| 29 | 鳜鱼 Mandarin Fish｜结构遮蔽+昼夜/温度 Context+移动目标 | NO_ACTION | 结构遮蔽=结构 Factor；昼夜=§11.5 低光 DynamicSpatialSlot 先例（@LowLightSpatialProfile）；温度=条件/Profile；移动目标=Reaction 通道；多 Context 为 AND 可分离 |
| 30 | 黄尾鲴 Xenocypris Davidi｜连续附着资源+Field Opportunity+离散钓获边界 | NO_ACTION | 附着资源=forage 契约附着 prey class；Field Opportunity=C09–C11；离散钓获边界=Response 窄接受窗（同 #19） |
| 31 | 高体鳑鲏 Rosy Bitterling｜活蚌鳃腔产卵+繁殖期对象依赖+雄性竞争 | NO_ACTION | 活蚌鳃腔产卵=BA-T2 繁殖锚（Anchor Resolver 实例=MusselBed；§11.2/Active Spawning §2 已泛化 resolver 槽）；[需正文]雄性竞争若需逐个体表达将落入个体属性 TODO |
| 32 | 细鳞鲑 Sharp Snouted Lenok｜冷水河流+季节性空间重排 | NO_ACTION | 温度 Factor + 时间窗条件 + 阶段路由（C12）；空间重排=条件命中下的 Profile/Bake 重绑定 |
| 33 | 鳡鱼 Yellowcheek｜中上层移动猎物+流速/水位+迁移 | NO_ACTION | 移动猎物=BA-T5；流速/水位=unary Profile 轴实例；迁移=GR 路由（G2 先例） |
| 34 | 青鱼 Black Carp｜硬壳资源 Patch+底质+季节空间 | NO_ACTION | 硬壳资源=mollusk prey class + size_window（口径 vs 壳代表尺寸）；压壳处理=handling/Conversion owner；季节空间=时间窗条件 |
| 35 | 蒙古红鲌 Mongolian Redfin｜target-size/moving-target checkpoint 候选 | NEEDS_REGRESSION_SAMPLE | 标注明示 checkpoint 候选：target-size 维度攻击 Quality §23（§12.3 LureSize/BaitSizeSelectivity 的「非负 multiplier、只读原始事实、并列不顺序」语义是否够用）；moving-target 维度回归 R-T2 固定双通道 + Reaction 输入轴（moving/erratic）覆盖 |
| 36 | 革胡子鲶 African Sharptooth Catfish｜低氧/洪泛 Context | NO_ACTION | 低氧=DO 轴（@HardDOFloor/@ColdSlowDOFloor 先例，耐受=Profile 值域）；洪泛=水位事实 GR 条件 + 漫滩 DynamicSpatialSlot；两 Context AND 可分离 |
| 37 | 鲮 Mud Carp｜连续底质/附着资源与离散捕获边界 | NO_ACTION | 同 #30：附着 prey class + Response 窄接受窗 |
| 38 | 鬼头刀 Mahi-Mahi｜Floating-Structure Bait Patch（Runtime Overlay 组合） | NO_ACTION | 标注即 Overlay 读法：漂浮结构饵斑=BA-T1 DynamicSpatialSlot / OV-T1 Overlay（§7 冷锋 Overlay + §11.4 先例）+ BA-T5 饵群耦合；不新增结构 |
| 39 | 白马切喉鳟 Cutthroat Trout｜Resident–Migratory Drift（drift lanes+lifecycle reorder） | NO_ACTION | Resident/Migratory 双型=GR 生活史状态路由（G2 先例）；drift lanes=流速+结构锚 Factor；lifecycle reorder=阶段路由（C12） |
| 40 | 美洲条纹狼鲈 Striped Bass｜Migratory Pelagic Target（schooling prey+current opportunity） | NO_ACTION | GR 迁移路由 + BA-T5 饵群耦合 + 流集聚 Factor（流隔=上游 forage/结构事实） |
| 41 | 眼鳢 Bullseye Snakehead｜Vegetated Ambush Patch（低氧耐受+普通目标摄食） | NO_ACTION | 植被伏击=结构 Factor + R-T2 反应主导；低氧耐受=DO Factor 值域；普通目标摄食=R-T1 Feeding |
| 42 | 大眼金枪鱼 Bigeye Tuna｜Deep-Diel Pelagic Target | NEEDS_REGRESSION_SAMPLE | 攻击 Knife §16.5 2D 判据：「Deep-Diel」若为鱼自身昼夜垂直节律（条件分支描述，不以该事实为真为前提），则 Layer×Diel 构成「最优带迁移」型 2D 样本；若纯饵群跟随则 BA-T5 吸收。[需正文]「垂直迁移驱动」一节裁决 |
| 43 | 蓝笛鲷 Green Jobfish｜Reef-Edge Current Break（schooling prey） | NO_ACTION | 礁缘流隔=结构+流集聚 Factor（上游事实）+ BA-T5 饵群耦合 |
| 44 | 花羔红点鲑 Dolly Varden｜Coldwater Resident–Anadromous Target | NO_ACTION | 冷水 resident/anadromous 双型=GR 生活史路由（同 #39）+ 温度 Factor |
| 45 | 黄尾鰤 Yellowtail Amberjack｜Reef-Current Bait Patch（pelagic/reef 过渡+移动猎物） | NO_ACTION | 过渡带=DynamicSpatialSlot/结构 Factor + BA-T5；移动猎物=Reaction/Feeding Profile |
| 46 | 闪光鲟 Stellate Sturgeon｜Benthic Odour Patch + Migration | NO_ACTION | 洄游=GR 路由（G2 先例）；底质斑=benthic prey class 绑定；气味定位猎物的模态归感知面 owner（非呈现 cue 轴——与 #13 区分） |
| 47 | 电鳗 Electric Eel｜Electrogenic Remote Prey Control（感官模态+非常规捕获边界+Candidate） | NEW_CONFIG_COVERAGE（前提：R05-FR3-pending，最终以 FR3 Packet 为准，判定可能翻） | 感官模态（主动电场/电击）在 Response cue 轴枚举无对应（live 主页零电场轴），与 #13 同聚类 K8——@ElectroFieldProfile 槽位规格见 §2.3；非常规捕获边界（远程麻痹）归 Encounter/Conversion owner，若需可配置将是 Encounter 面新槽位主张（UPSTREAM 登记候选）；「Candidate」具体指向[需正文] |

## 4. 跨候选聚类（14 个，覆盖全批 47 条）

| 聚类 | 成员（#） | 合并判定 | 代表样本与吸收/缺口指向 |
|---|---|---|---|
| K1 开放水/流系饵群耦合 | 15, 20, 21, 33, 38, 40, 43, 45（8） | NO_ACTION | 代表 #15：BA-T5 + GR forage 资格路由 + R-T1 + QT-1；#38 的 Overlay 读法 = OV-T1/DynamicSpatialSlot 与 BA-T5 叠加 |
| K2 浮游/滤食食场 | 7, 17, 18, 19（4） | NO_ACTION | 代表 #18：forage 契约 plankton class + FILTERED_SUM + C09–C11 + LayerProfile；#19 离散捕获边界=Response 窄接受 + Encounter owner；#7 电感受定位=感知面 owner |
| K3 底质/附着/扰动资源（P06） | 5, 11, 23, 25, 30, 34, 37（7） | NO_ACTION | 代表 #30：附着/benthic prey class（P06 判别轴在契约 prey_fields 层无载体区分，两侧压缩进同一契约）+ 基质/流速 Factor + DynamicSpatialSlot |
| K4 繁殖/育幼锚关系 | 3, 14, 16, 22, 26, 31（6） | NO_ACTION | 代表 #3：类型化繁殖状态路由 + BA-T2 锚模板（resolver 实例：巢/稚鱼群/口孵群/蚌床/岸滩）+ RR-T2 / R-T1 Cap |
| K5 洄游/生活史路由 | 27, 28, 32, 39, 44, 46（6） | NO_ACTION | 代表 #39：GR 状态/阶段路由（G2、C12 先例）+ 盐度/水位/温度/流速 = unary/2D Profile 轴实例（Knife §10 盐度先例） |
| K6 份额拆分型（性别/等级分位置） | 2, 6（2） | NO_ACTION | 代表 #6：GR 同条件多路由 Share Vector（§7 契约 + §15.1 模型）；share 是供给比例不是逐个体分类 |
| K7 捕获阶段内容（Encounter-owned） | 8, 9, 10（3） | NO_ACTION | 代表 #9：四面份额=Response 呈现接受（Profile 窄窗）；主体按 forage 契约边界表归 Encounter/Conversion owner |
| K8 呈现 cue 轴模态缺口 | 13, 47（2，#10 弱关联） | NEW_CONFIG_COVERAGE | 代表 #13：Response cue 轴枚举缺化学（scent）/电（electro）轴——列级规格 §2.3；#47 挂 R05-FR3 前提 |
| K9 垂直节律 2D 判据样本 | 24, 42（2） | NEEDS_REGRESSION_SAMPLE | 代表 #42：Knife §16.5「最优带系统性迁移」判据的定向样本；与 BA-T5+Resolver 读法二选一，正文「迁移驱动」一节裁决 |
| K10 target-size/moving-target checkpoint | 35（1） | NEEDS_REGRESSION_SAMPLE | Quality §23（§12.3 Modifier 形状）+ R-T2 双通道覆盖回归 |
| K11 习惯化/学习 | 4（1） | NO_ACTION | CueFamiliarity（§5.6 决策 + §17.3 输入轴）+ 窗口化计算事实 |
| K12 玩家行为斑块 | 1（1） | NO_ACTION | DynamicSpatialSlot 消费；上游「打窝斑块」世界事实义务 |
| K13 地域策略变体 | 12（1） | NO_ACTION | per-instance Profile 重绑定（Profile 绑定本就是实例级） |
| K14 低光/低氧/结构伏击 Context | 29, 36, 41（3） | NO_ACTION | 代表 #29：§11.5 低光先例（BA-T1 + @LowLightSpatialProfile + Cue Profile）+ DO 轴 + 结构 Factor + R-T2 |

计数核对：8+4+7+6+6+2+3+2+2+1+1+1+1+3 = 47。

## 5. 建议

值得立 B 线新批次（1 个）：
1. 呈现 Cue 轴模态扩充（K8）：小批次、边界清楚——一个新轴（scent，#13 无前提争议）+ Unary + FIXED_COMBINE 先例复用 + 事实枚举两行（§2.3 规格）；#47 电轴部分待 R05-FR3 Packet 后并入或另立。可循 forage 契约批次的工件形态（README + config + validator + dsl 对照）。
2. K9（#24/#42）不立表达批次：送下一轮 2D Profile 判据验证（若机制侧开 Knife R1 / 2D reuse 盘点，带上这两条作判据样本）；所需输入是两条 Story 的「迁移驱动」一节。
3. #35 不立批次：送 Quality §12.3 Modifier 形状回归；所需输入是正文 target-size/moving-target 的具体语义。

NO_ACTION 归档（42 条），带四类登记备注（建议 Hub Coverage Delta Pack Registry 逐条字段化）：
- a. Encounter/Conversion lane 输入登记：#8/#9/#10（捕获阶段主语义）、#19（捕获概率边界）、#47（远程麻痹捕获边界）
- b. Snapshot 事实族义务登记：#1（打窝斑块）、#5/#11/#23（扰动痕迹族）、K3 附着生物量族、#24/#42（diel 饵场，Resolver 读法）——到达时触发 forage 契约 SNAP allowlist 收窄义务（R1 README §6）
- c. 感知面 owner 登记：#7（电感受定位）、#46（气味定位）、K8 的输运/传导耦合
- d. 个体属性 TODO 关联：#2/#3/#6/#31 ↔ live 主页 Active Spawning §4 已登记的 Sex/Maturity TODO

不建议：把 K1/K3/K4 的物种多样性记成新模板或新批次——它们恰是 §11.8「次线性增长」的横向验证样本，建议在 Hub 按已有字段记 CanBindExistingTemplate=YES + Reason（§11.9 字段集）。

## 6. 诚实边界与前提

### 6.1 判定基础
输入=标题 + 模式注记，无 Story 正文；所有判定是「标题语义 × 四面结构对照」，不构成对现实语义的复审。物种生物学断言在判定中只作条件分支描述，判定结论不以其为真为前提。表达基线为本地转录/归档（SNAPSHOT_ONLY）；live 漂移时节号指向以归档版为准。§22/§23 编号映射为显式假设（验收已核对一致）。

### 6.2 「需正文」子备注清单（不改变主判定档位）
| # | 需要正文哪一节 | 若正文确认 X |
|---|---|---|
| 9 | 捕获阶段是否需可配置时序 | Encounter 面新槽位主张（非四面） |
| 10 | 「阻力/线感」是否独立 cue 轴 | 并入 K8 轴枚举缺口 |
| 24 / 42 | 垂直迁移驱动（饵群跟随 vs 自身节律） | 自身节律→§16.5 样本成立；跟随→改判 NO_ACTION（BA-T5） |
| 31 | 雄性竞争是否需逐个体表达 | 触发个体属性 TODO 立项 |
| 47 | 「Candidate」具体指向 + FR3 Packet | 电轴槽位立项/撤回；捕获边界转 Encounter lane |

### 6.3 本报告不做的事
不把 NO_ACTION 写成机制 promotion 或 Freeze；不覆盖 live 主页/Knife 子页任何 Verdict；不产出新表达工件（K8 批次立项后的工件另批交付）。

BATCH_ID: REP-COVERAGE-DELTA-001
