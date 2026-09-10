# P03 滄食/浮游场系四面生产级表达 + 品系 L1 等效层交付包｜REP-FULL-FIELD-001

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 批次 | REP-FULL-FIELD-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 5 批：P03 滄食/浮游场系 + 品系 L1 等效层；含 REP-FULL-GRAZE-REV-001 B1 撤回件 giant_barb 重建） |
| 输入 | (1) 基准样板＝live Stress Test R1 主页转录 `programaticHitFish/tmp/live_stress_main_after.md`（2026-09-10 版：§13.3 R-T1 结构族（**Forage-Coupled Feeding：Channel=Feeding 换 Profile/Facts——Field 型读法先例** + C09–C11 FieldFeeding 输入落单通道判语）+ §10 BA-T5 Forage Field Coupling 句型（场耦合 live 参照）+ §7 Share 契约 + §12 Quality 样板 + §13.1 G-T1/§13.2 B-T1 结构族）(2) 前四批判式与标准＝guarding / grazing / migration / normal 四批交付包（REP-FULL-GUARD/GRAZE/MIGRA/NORM-001；giant_barb 撤回档+M2 Response 通道分歧登记为本批直接输入）(3) census registry v4＝`fish_logic_census/template_registry.yaml`（**FOOD_FIELD_FEEDING_RESPONSE 族 2 成员（鳙 canonical_source + 大西洋鲱）+ SINGLE 族 factor_type 轴 +food_field**（BHC/HER 场实例第 2/3 例继 B1 七鳃鳗 chemical_gradient）；本批 Bake/Response 投影族）(4) census 归档 `fish_logic_census/batches/CENSUS-B2`（BHC/HER 全四面判定快照 + 盲程序体冻结 + HRQ-B2-01 队列）(5) `outputs/usable_forage_contract_r0/`（UsableForageAvailability 契约 r1——plankton prey class + FILTERED_SUM 直接复用）(6) migration 批 README 登记项（红鲑/欧白鲑滤食 P03 复核线、登记项 4 Whitefish 通名系、灰西鲱/美洲西鲱双批分工）(7) R02–R10 批次摘要（outputs/batches/FISH-R*.md：R02 鲢/鳙双样版 + R10 收官批 Piraiba 点名）(8) fish-reference-20260908.csv（物种身份/滤食方向锚——**本批 Tier B 名单构造的机械输入**）(9) Semantic Review Context §10 Field Channel OPEN（经 census registry CUE_GUIDED related_precedent 引文承载——该页本体不在本地） |
| 基线 | **SNAPSHOT_ONLY**——Notion MCP 工具在本执行环境不可用（Story DB live 未访问），全部输入为本地归档/转录/快照；**Story DB 主 relation=P03 的逐行名单不在本地**——本批名单构造方法见 §1 名单声明；Semantic Review Context 页（§10 Field Channel OPEN）无本地快照，其判例仅经 census registry 引文承载 |
| 交付物 | `species/*.md` 24 文件：**P03 主批 12 文件**（每鱼四面：Group Routing 无路由显式声明 + Bake 配置/伪脚本（场事实→场评估器→场适应性）+ Response 配置/伪脚本（R-T1 FieldFeeding 通道完全展开）+ Quality 绑定/伪脚本）+ **品系 L1 等效层 12 文件**（短形：四面声明 + 本体指针 + Profile 重绑定清单，不展开伪脚本——R10 品系行判例）+ 本 README + `validate_field.py` 结构校验器 |
| 数值状态 | 全部阈值/窗口/场构成/Profile 值域为 **@参数引用**（生产数值由 Profile 层定值，不冻结）；Bake 程序无 combine 步（census SINGLE 族域），live 层组合算子 **OPERATOR UNDEFINED** 待机制侧；intake_semantics（持续滤食/脉冲摄入）与 field_type（plankton 场/resource patch 场/饵鱼场）均为 FOOD_FIELD 族已声明参数轴实例，非新结构 |

## 1. 样本口径（24 文件 = P03 主批 12 + 品系 L1 等效 12）

P03＝Food Field → FieldFeeding / Field Opportunity（census registry FOOD_FIELD_FEEDING_RESPONSE semantic_pattern_correspondence，New Candidate；两层登记待 review）。**本批 Response 面统一口径：FieldFeeding 通道＝R-T1 Feeding 通道的 Field 型（Channel=Feeding，evaluand 换为食物场浓度、换 Profile/Facts——live §13.3 Forage-Coupled Feeding 读法先例；15-Case C09–C11 FieldFeeding 输入同落 R-T1 单通道）——不是新通道、不 promote Grammar（Semantic Review Context §10 Field Channel OPEN 经 census 引文登记，本批不闭合）。**

### 名单声明（诚实边界，承 normal 批先例）

本地无 Story DB P03 逐行名单。本批 P03 主批 12 文件名单由四层锚构造，全部可机械复验：

1. **Tier A（census 快照全文在案）×2**：鳙鱼（FISH-R02-S09，canonical_source）、大西洋鲱（FISH-R02-S02，第 2 成员）——census B2 stories/blind_programs 冻结。
2. **B+（批内判语/点名/live 实测）×6**：鲢鱼（census「同型对照不建体」判语在案）、欧白鲑/红鲑/美洲西鲱 P03 面（migration 批「滤食取向 P03 复核登记」兑现线+双批分工）、giant_barb（REV-001 B1 live 行级实测）、Piraiba（handoff R10 点名）。
3. **Tier B（CSV 方向锚）×4**：毛鳞鱼/湖白鲑 P03 面/日本竹荚鱼（CSV 滤食性+selective plankton feeding 机械锚）、灰西鲱 P03 面（CSV 矛盾弱锚+migration 批互指）。
4. **品系 L1 等效 ×12**：handoff 点名分组（锦鲤系 5+白化系 4+无鳞/人面/鳞白化 3），CSV 行级「同物种」标注为身份锚。

证据档：A＝census 全四面判定快照；B+＝批内判语/点名/live 行级实测锚；B＝CSV 方向锚（条件值全 @ 化，行级标签 [需核对]）；L1 等效＝CSV 同物种子行标注（R10 品系行判例）。

### 表 A｜census Tier A 组（2 文件）——BA-P03-FIELD-SINGLE + R-T1 FieldFeeding

| # | 文件 | 鱼（学名） | Story | 证据档 | 场实例 / 参数轴 |
|---|---|---|---|---|---|
| 1 | bighead_carp.md | 鳙鱼（Hypophthalmichthys nobilis） | FISH-R02-S09 滤食浮游场与水层机会（census B2）——**FOOD_FIELD 族 canonical source，本批 Tier A 样板** | A | plankton 场 / 持续滤食 |
| 2 | atlantic_herring.md | 大西洋鲱（Clupea harengus） | FISH-R02-S02 群游产卵与浮游食场（census B2）——族第 2 成员（engine 无字面差异）；**库内首个 GroupPressure=Strong/Group-only verdict 登记** | A | plankton 场（群游集聚值域承载） / 持续滤食 |

### 表 B｜同批点名+复核线兑现+CSV 锚组（10 文件）

| # | 文件 | 鱼（学名） | Story | 证据档 | 特殊登记 |
|---|---|---|---|---|---|
| 3 | silver_carp.md | 鲢鱼（H. molitrix） | FISH-R02-S07——census 判语「同型对照不建体」在案 | B+ | BHC 骨架参数差异化（浮游植物主向）；行级 Pattern [需核对] |
| 4 | vendace_field.md | 欧白鲑（Coregonus albula）P03 面 | migration 批 vendace.md §3.2「P03 域复核」兑现线（P05 面已由 migration 批承载） | B+ | 双批分工（P05/P03 互指） |
| 5 | sockeye_field.md | 红鲑（Oncorhynchus nerka）P03 面 | migration 批 sockeye_salmon.md 复核线兑现（[需正文]） | B | 双批分工；停食判例族不默认继承 |
| 6 | american_shad_field.md | 美洲西鲱（Alosa sapidissima）P03 面 | FISH-R06 停食第 2 例的**摄食期面**（停食面归 migration 批双 Path） | B+ | 双批分工；停食期 FieldFeeding 挂起归 P05 资产；CSV 矛盾 |
| 7 | alewife_field.md | 灰西鲱（A. pseudoharengus）P03 面 | FISH-R06 西鲱二之二（P05 面已承载；[需正文]） | B | 双批分工；CSV 矛盾（肉食性行 vs 属级滤食） |
| 8 | capelin.md | 毛鳞鱼（Mallotus villosus） | handoff 点名「鲱/西鲱/毛鳞鱼等浮游场系」；K4 排除=繁殖面口径（§3 登记 5 澄清） | B | CSV 滤食锚；产卵面归后续批 |
| 9 | lake_whitefish_field.md | 湖白鲑（Coregonus artedi）P03 面 | migration 批登记项 4 Whitefish 通名系 CSV 行（P05 面零证据不冒充） | B | CSV 滤食锚；通名系种级区分（inconnu §0 先例） |
| 10 | jack_mackerel.md | 日本竹荚鱼（Trachurus japonicus） | CSV 滤食锚行（[需正文]） | B | 混合食性张力登记（CSV 滤食 vs 鲹科 piscivore 倾向） |
| 11 | giant_barb.md | 暹罗巨鲤（Catlocarpio siamensis）**重建** | FISH-R05——**live 行级实测（REV-001 B1）：ResponseChannels=[FieldFeeding]、PrimaryEvaluand=[Resource Patch]、P05+P06 双 relation** | B+ | 见 §1 表 C |
| 12 | piraiba.md | 短扁口鲶（Brachyplatystoma filamentosum） | FISH-R10 收官批成员（handoff 点名「Piraiba 鲶顶级（R10）」；[需正文]） | B+ | 饵鱼场 / 脉冲摄入（顶级 piscivore 场跟随） |

### 表 C｜giant_barb 重建专记（REV-001 B1 撤回件重写）

撤回原因（grazing 批 REV-001）：原 BA-SUBSTRATE-SINGLE + R-T1 TargetFeeding 骨架被 live 行级证据证**结构反向**。本批重建要点：(1) Response 主线＝Field 通道（R-T1 FieldFeeding，evaluand=Resource Patch 食物场——非 TargetFeeding、不并联）；(2) Bake＝resource patch **场化**（BA-P03-FIELD-SINGLE 的 food_field:resource patch 场实例——底质/附着资源作为场 evaluand 进入，原「底质单因子」形态随撤回档废弃）；(3) P05 面（potamodromous 洄游）lifecycle premise 配置级保留（MGC/CHB 先例）；(4) P06 面被场化吸收（底质处理=PrimaryEvaluand=Resource Patch 的载体语义）。撤回档保留于 grazing 批目录（WITHDRAWN 标注），不删。

### 表 D｜品系 L1 等效层（12 文件）——L1-EQUIV 短形（四面声明+本体指针+Profile 重绑定清单）

| # | 文件 | 品系（学名） | 本体 | 本体四面状态 |
|---|---|---|---|---|
| 13 | koi.md | 锦鲤（Cyprinus rubrofuscus） | 鲤复合体 | 未建（K3/P02 补批登记）；名实注记（种级行 vs Var. 行） |
| 14 | koi_kohaku.md | 红白锦鲤（C. carpio Var. Kohaku） | 普通鲤鱼 | 未建（同上） |
| 15 | koi_shiro_utsuri.md | 四白锦鲤（Var. Shiro Utsuri） | 普通鲤鱼 | 未建 |
| 16 | koi_goromo.md | 圆点五色锦鲤（Var. Goromo） | 普通鲤鱼 | 未建 |
| 17 | koi_ogon.md | 橙黄金锦鲤（Var. Ogon） | 普通鲤鱼 | 未建 |
| 18 | albino_grass_carp.md | 白化草鱼（Ctenopharyngodon idella Var. Albino） | 草鱼 | 未建（P02 批登记——B01-S53 census SINGLE 第 1 成员） |
| 19 | albino_white_sturgeon.md | 白化高首鲟（Acipenser transmontanus） | 高首鲟 | **已建**（migration 批 white_sturgeon.md）——重绑定即刻生效 |
| 20 | albino_channel_catfish.md | 白化叉尾鮰（Ictalurus punctatus） | 斑点叉尾鮰 | **已建**（normal 批 channel_catfish.md）——重绑定即刻生效 |
| 21 | albino_mirror_carp.md | 镜鲤（白化）（Var. Specularis Albino） | 普通鲤鱼 | 未建 |
| 22 | leather_carp.md | 无鳞鲤（Var. Nudus） | 普通鲤鱼 | 未建；映射注记（俄4映射列=镜鲤≠本体判定） |
| 23 | human_face_carp.md | 鳞鲤（人面鲤）（Var. Human Face） | 普通鲤鱼 | 未建 |
| 24 | albino_scale_carp.md | 鳞鲤（白化）（Var. Albino） | 普通鲤鱼 | 未建 |

### 明确排除项（不属本批，显式记录）

| 排除项 | 理由 |
|---|---|
| 红鲑/欧白鲑/灰西鲱/美洲西鲱的 P05 面 | migration 批已承载（本批只建 P03 面 *_field.md 双批分工互指） |
| rohu 泰鲮 P03 场化重写 | grazing 批 M2 登记 rohu live 实测同 FieldFeeding 但「骨架不必翻、注记待对照更新」——grazing 批资产，本批不重写（登记项 2 联动） |
| 鸭嘴鲟 P03 面（CSV filtering plankton 唯一行） | P01 面已由 normal 批承载（S34/S35 两文件）；P03 主 relation Story 本地零证据，不冒充——**候选池**（Story DB 名单到达后补批） |
| 大西洋鲭（CSV 杂食+variable）/ 鲻鱼（15-Case C11 FieldFeeding 先例但 K3/P02 侧归属未对账） | 滤食方向弱锚/归属未对账——候选池 |
| 青鱼（R04 #34 K3 成员） | K3 底质/附着聚类——归 R04 成员补批（normal 批排除表先例） |
| 鲱形余量（沙丁/鳀系等 CSV 无行） | CSV 无行、Story DB 名单不在本地——缺口登记（登记项 1） |
| 荷包红鲤 / 镜鲤（本体品系行） | handoff 品系名单字面为「锦鲤系 5+白化系 4+无鳞/人面/鳞白化 3」——荷包红鲤/镜鲤两行不在点名名单内；**候选池**（登记项 4） |
| 大口水牛鱼（C10）/桨鱼（C09） | 15-Case 四面已由 four-surface-completion-r1 承载（RS-FEED-01 FieldFeeding 输入）——密封包不重复 |
| 斑点叉尾鮰×白化叉尾鮰等本体-品系重复行 | 品系不分裂（L1 等效——本体文件是唯一四面 owner） |

## 2. 表达读数（对模板计数的影响）

- **Group Routing**：12/12 主批文件＝「无路由程序，默认 Normal Group」显式声明（§1.1 声明 + §1.2 单默认行 + §1.3 伪脚本 Share 契约校验位）。census 判语：BHC＝NO_SURFACE_EFFECT（FishMode Weak）、HER＝**库内首个 GroupPressure=Strong/Group-only verdict**（census 层无 routing body 证据——摄食群与产卵群重叠非同态、无统一触发器；语义层判定与 census 正交）。handoff「鲢/鳙鱼群供给路由候选」本地无行级证据——全批无路由退化形 + 登记项 1。**L_group 无增长；品系 12 文件＝Group 面声明复用（无新 Group）。**
- **Bake**：12/12 主批文件落在 census SINGLE 族 factor_type 轴 **food_field** 场实例投影：**BA-P03-FIELD-SINGLE ×12**（鳙 canonical + 鲱 + 参数差异化 10）。伪脚本展开为「**场事实→场评估器→场适应性**」（EVAL_FOOD_FIELD_CONCENTRATION → NORMALIZE_WEIGHT——非「基质→Profile→Fit」的 substrate 形）。场实例三型：plankton 场 ×9（鳙/鲱/鲢/欧白鲑/红鲑/灰西鲱/美洲西鲱/毛鳞鱼/湖白鲑/竹荚鱼——计 10 减 giant_barb/piraiba）、resource patch 场 ×1（giant_barb 重建）、饵鱼场 ×1（piraiba）。**投影标签封闭枚举**（validator BAKEFAM 钉死单值，新值=规格动作）；**族边界进校验**（FAMCTX：强制 FieldType(typed) 含 food_field + FieldEvaluatorProfile 行 + NORMALIZE_WEIGHT 族常量；禁 combine/槽/因子集行——STRUCT 字段白名单为第一层）。**census 侧 ΔL_bake=0（food_field 轴为 B2 既有轴实例，本批零新族）；live 侧 L_bake_base 无增长——BA-T5 Forage Field Coupling 为场耦合 live 参照读法（§10 既有句型），两层 reconciliation OPEN（§3 登记 1）。**
- **Response**：**12/12＝R-T1 单通道（Channel=FieldFeeding；Reaction 槽 OFF）——批统一拓扑，零 R-T2**（validator FIELDRESP 钉死 FieldFeeding 通道标记 + Reaction 槽 OFF + canonical 三步 EVAL_FOOD_FIELD_INTAKE → DECIDE_FIELD_FEEDING → Response(FieldFeeding) fence 强制；R-T2 出现即违规）。intake_semantics 参数轴实例：持续滤食 ×11 + 脉冲摄入 ×1（giant_barb/piraiba——见各文件）。**L_response 无增长（FieldFeeding＝R-T1 Feeding 通道的 Field 型——live §13.3 Forage-Coupled Feeding 读法，不是新通道）；census FOOD_FIELD 族 New Candidate 状态原样（HRQ-B2-01/TAR-09），本批不 promote Grammar。**
- **Quality**：12/12 主批＝QT-1 绑定表形态；0 个 W1–W3 物种级品质调整表（census BHC/HER Quality 面均 NO_SURFACE_EFFECT）。**L_quality 无增长。** 品系 12 文件＝QT-1 复用声明 + 品系重绑定位（@*QualityProfile）——品系级品质 Modifier 无 Story 证据不表达。
- **新列结构**：零（分群结果 5 列/BAKE 字段-值/RESP 5 列/绑定表 5 列/META 2 列——全部 live 已声明变体；bake 配置行键封闭枚举 {BakeTemplate, FieldType(typed), FieldEvaluatorProfile, FactorBinding, Normalization, Bake输入契约, LiveLayerProjection} 防行内键注入，validator STRUCT 强制）。**品系 L1-EQUIV 短形＝本批新表达层形态**（四面声明段落 + 本体指针行 + 重绑定清单行；无表格无伪脚本——validator L1EQUIV 族强制形态要素，非省略面）。

## 3. 跨批一致性登记

1. **census 族 ↔ live 句型两层 reconciliation OPEN（承 grazing/migration/normal 批登记 1）**：本批 Bake 投影标签（BA-P03-FIELD-SINGLE）是 census SINGLE 族 food_field 轴实例的批投影标签，不是 live 句型晋升；live 侧等价读法＝BA-T1 底板 + typed food-field factor（B-T1 单因子退化形）+ BA-T5 场耦合句型参照（ForageSchoolIntensity 类场事实）。Response 面 FOOD_FIELD_FEEDING_RESPONSE 是 census CANDIDATE 族（HRQ-B2-01 PENDING；产品捕获方式 TAR-09 Open；P03 语义层 New Candidate——registry provisional_note「census 族独立性不自动 promote Grammar」原样携带）。两层是否等价、Field 通道是否升格 live 句型，归机制侧裁决，本批不闭合。**Semantic Review Context §10 Field Channel OPEN**（该页无本地快照，经 census registry CUE_GUIDED related_precedent 引文承载）——本批按 OPEN 登记处理。
2. **grazing 批 M2 处置联动（rohu 场化复核线）**：giant_barb 重建（本批）证实 P06 行级 Story 的 ResponseChannels=FieldFeeding 读法在 resource patch 场实例上成立；rohu 同登记（M2：live 实测 FieldFeeding、骨架不必翻、注记待对照更新）——本批不重写 rohu（grazing 批资产），其 P03 场化复核按 giant_barb 重建先例转登记项 2（Coordinator 决定 rohu 是否照 giant_barb 路线重建或维持 M2 注记方案）。
3. **双批分工面互指（本批第 2 例——承 migration 批「同 Story 双批分工首例」）**：欧白鲑/红鲑/灰西鲱/美洲西鲱 P05 面归 migration 批、P03 面归本批（*_field.md 后缀文件，白斑狗鱼多 Story 多文件先例）。停食语义边界：美洲西鲱摄食期 FieldFeeding（本批）/溯河停食期挂起（migration 批双 Path）——两面正交不冲突；红鲑溯河停食与否 [需正文]，停食判例族不默认继承（migration 批同属不继承判语原样）。
4. **Tier B/B+ 归族裁决权移交（承前四批登记 2）**：10 个非 Tier A 文件的 BA-P03-FIELD-SINGLE 骨架是表达层选择（CSV 锚/批内判语的最低结构）；Story 正文到达后 census 侧判同可能改判（PLAIN 多因子/其它族）＝**结构变更需重审**（validator 族边界拦截静默改写），不是 Profile 重绑定。鲢鱼的「同型对照」是 census 侧给的判语（B+）但仍属可改判范围。
5. **K4 排除口径澄清（guarding/normal 批与本批的关系）**：毛鳞鱼在 guarding/normal 批被排除的依据是 K4 繁殖/产卵锚聚类（无 guard relation、P01 归属无证据）——排除的是繁殖面在 P04/P01 批的冒充收录，不是滤食面的 P03 归属。本批按 CSV 滤食锚+handoff 点名收录其 P03 面（capelin.md §0 登记）；两面互不冒充。
6. **UsableForageAvailability 契约复用（承前四批登记）**：12/12 主批文件 Bake 输入契约行引用三过滤（plankton/resource patch/baitfish prey class 均走同一契约——FILTERED_SUM 常量聚合 + 原始事实族口径直接复用，r1 契约不变量原样）。「场浓度 vs prey class 生物量」的口径关系＝场评估器的输入侧（场事实读取行），契约输出仍是 per-cell 在场可食生物量——两层口径不冲突（场评估器消费契约输出的方向登记，收窄义务同 r1 契约 §6）。
7. **品系 L1 等效层与「变体行不分裂」先例的关系**：normal 批排除表「镜鲤(白化) 等变体行：变体行不分裂先例（并入本体文件登记或本体批承载）」——本批 L1-EQUIV 文件是该先例的**实现形式**（不分裂四面：四面复用本体+声明层文件只承载重绑定清单）。10 个本体未建文件是**绑定声明**（不冒充本体已存在）；2 个本体已建文件重绑定即刻生效。本体到达时品系文件连带更新（单向从属）。
8. **15-Case C09–C11 FieldFeeding 先例关系**：four-surface-completion-r1（密封包）的 C09 桨鱼/C10 大口水牛鱼/C11 鲻鱼以 RS-FEED-01 承载 FieldFeeding 输入（live §13.3 同页判语「均有机会落在同一 Single-channel topology」）——本批 R-T1 Field 型读法与其同构；密封包不重开，本批不引用其内部结构只引判语。

## 4. 退回与登记项（转 Coordinator）

| 项 | 内容 |
|---|---|
| 登记项 1（名单构造方法+行级核对） | **Story DB 主 relation=P03 的逐行名单不在本地**。P03 主批 12 文件中 4 个 Tier B 的名单=CSV 滤食性/浮游方向机械锚构造；鲢/鳙鱼群供给路由候选（handoff 提示「核 Story DB 行级」）本地无行级证据，全批无路由表达。需 Story DB P03 导出（鱼名+Story+relation）或行级标签核对表；核对后增删/路由升级=表达层动作（结构变更需重审）。估 15-20 种 vs 本批 12 文件——缺口构成：鲱形余量（沙丁/鳀系 CSV 无行）、鸭嘴鲟 P03 面、大西洋鲭候选池（§1 排除表），全部 [需核对] 待名单 |
| 登记项 2（rohu 场化复核线——grazing 批 M2 联动） | giant_barb 已按 live 实测重建（Field 主线）；rohu 同登记（live 实测 FieldFeeding、骨架未翻）——Coordinator 裁定 rohu 走 giant_barb 重建路线还是维持 M2 注记方案。另：giant_barb 的 P05+P06 双 relation 行级 Story 正文逐句核对（REV-001 B1 门已开——live 对照义务） |
| 登记项 3（CSV 矛盾清单） | 灰西鲱/美洲西鲱（食性=肉食性 hunting macrofauna vs Alosa 属滤食方向——方向锚取弱，构成 [需正文]）；日本竹荚鱼（CSV 滤食 vs 鲹科 piscivore 倾向）；鳙鱼（CSV 杂食性名义行 vs census 滤食判语——以 census 为准已处理）；鲢鱼行级 Pattern（census「同型对照」判语 vs 行级标签） |
| 登记项 4（品系名单口径） | handoff 品系名单字面「锦鲤系 5+白化系 4+无鳞/人面/鳞白化 3」=12 行已全收；CSV 另有荷包红鲤（Var. Wuyuanensis）/镜鲤（Var. Specularis 本体品系行）两行不在点名名单——候选池待 Coordinator 裁定（同 K3/P02 本体批联动）。锦鲤行学名 C. rubrofuscus（种级行）名实注记已登记 [需核对] |
| 登记项 5（Semantic Review Context §10 Field Channel OPEN） | 该页无本地快照（经 census registry 引文承载）；Field 通道两层登记待 review 的裁决到达后本批文件零结构改动（声明层引用不变） |
| [需正文] 批量项 | 4 个 Tier B 文件的场构成（浮游/混合比例）、premise 切换细节（若有）、Response 接受窗参数方向（逐文件 §5 已列）；红鲑溯河停食与否；Piraiba R10 Story 行；鲱鱼群游语义层 Group pressure 与 census 无 routing body 的正交登记（HRQ 后续） |
| 无 UPSTREAM_CHANGE_EVENT | 本批未发现机制侧问题；表达层全部落在既有 census 族（SINGLE food_field 轴/FOOD_FIELD 族已声明参数轴）与 live 结构槽位（G-T1 退化形+BA-T1+B-T1+R-T1 Field 型+QT-1）内。BA-P03-FIELD-SINGLE/L1-EQUIV 短形是表达层标签/形态，不是机制主张 |

## 5. 验证记录（命令与输出原样）

命令（selftest）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/field/validate_field.py" --selftest
```

命令（真实交付包校验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/field/validate_field.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/field"
```

输出：见下方两个代码块（原样粘贴，未改测试凑通过）。缺陷史：selftest 首轮抓出用例期望族错误 1 处（FAMCTX 禁行用例的 CombineRule 行先被 STRUCT 字段白名单拦截——纵深防御第一层，期望族改为 STRUCT，非放宽检查）；生成器占位符两轮替换缺陷 1 处（name_note 后注入占位符不再被替——教训 9 变体，render 改两轮循环）；工件缺陷 2 处（品系文件 §4 附带提及的中性 Profile 写成 @token——PROFILES 闭包误命中，去 @ 前缀修复 12 文件；双批文件标题双括号可读性缺陷批量修复 5 文件）——均修复工件/校验器期望而非改检查语义。

### selftest 输出

```
[OK  ] baseline (field-single) passes unchanged
[OK  ] baseline (l1-equiv variant) passes unchanged
[OK  ] HEADER fires on missing NOT AUTHORITY
[OK  ] HEADER fires on missing BATCH_ID line
[OK  ] SECTIONS fires on missing Bake section
[OK  ] GROUPFORM fires when 1.1 loses no-route declaration
[OK  ] GROUPFORM fires on Special Group route row
[OK  ] SHARE fires on missing default route row
[OK  ] SHARE fires on missing validation block
[OK  ] BAKEFAM fires on value outside closed enum
[OK  ] BAKEFAM fires on missing BakeTemplate row
[OK  ] FAMCTX fires when FieldType loses food_field axis
[OK  ] FAMCTX fires on missing FieldEvaluatorProfile row
[OK  ] STRUCT fires on FIELD carrying CombineRule row (whitelist is first layer)
[OK  ] FAMCTX fires when bake fence loses canonical step
[OK  ] PREMBIND fires on binding without premise
[OK  ] CONTRACT fires on missing forage contract row
[OK  ] FIELDRESP fires when topology loses FieldFeeding channel
[OK  ] FIELDRESP fires when Reaction slot ON marker missing
[OK  ] FIELDRESP fires on R-T2 topology declared
[OK  ] FIELDRESP fires when canonical intake step missing
[OK  ] FIELDRESP fires when canonical RETURN missing
[OK  ] QUALITYCOV fires when binding table emptied
[OK  ] PROFILES fires on used-but-unlisted token
[OK  ] PROFILES fires on listed-but-unused token
[OK  ] BAN fires on forbidden phrase LifecycleCohort
[OK  ] BAN fires on unannotated merge phrase in fence
[OK  ] STRUCT fires on stray table
[OK  ] STRUCT fires on unknown bake config field
[OK  ] L1EQUIV fires when variant loses a declaration section
[OK  ] L1EQUIV fires when variant loses base-species pointer row
[OK  ] L1EQUIV fires when variant loses rebinding list
[OK  ] PROFILES fires on variant listed-but-unused token
== selftest ==
SELFTEST PASS
```

### 真实交付包校验输出

```
[PASS] albino_channel_catfish.md
[PASS] albino_grass_carp.md
[PASS] albino_mirror_carp.md
[PASS] albino_scale_carp.md
[PASS] albino_white_sturgeon.md
[PASS] alewife_field.md
[PASS] american_shad_field.md
[PASS] atlantic_herring.md
[PASS] bighead_carp.md
[PASS] capelin.md
[PASS] giant_barb.md
[PASS] human_face_carp.md
[PASS] jack_mackerel.md
[PASS] koi.md
[PASS] koi_goromo.md
[PASS] koi_kohaku.md
[PASS] koi_ogon.md
[PASS] koi_shiro_utsuri.md
[PASS] lake_whitefish_field.md
[PASS] leather_carp.md
[PASS] piraiba.md
[PASS] silver_carp.md
[PASS] sockeye_field.md
[PASS] vendace_field.md
== result ==
PASS (24 species files, 0 violations)
```

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器纯标准库，内部强制 stdout UTF-8。

## 6. 边界声明

- 本包只做 P03 滄食/浮游场系四面生产级表达（第一轮）+ 品系 L1 等效层声明；表达验证通过 ≠ 机制 promotion ≠ Freeze；不覆盖 live 主页 / census registry 任何 Verdict；FOOD_FIELD 族 New Candidate / HRQ-B2-01 / TAR-09 状态全程可见。
- 全部数值不冻结（@参数引用，Profile 层定值）；Bake 无 combine 步（族域边界）；live 层组合算子 OPERATOR UNDEFINED 待机制侧；Field 通道两层 reconciliation、Semantic Review Context §10 OPEN、名单构造核对、rohu 复核线、品系本体从属全程 OPEN 可见。
- 每文件 §5 记录使用/放弃的自由度（含归族裁决权移交、TAR-09 不预购买、同属判例不继承、视觉层不程序化、本体未建不冒充）。
- 未 commit（提交由 Coordinator / 用户决定）。

BATCH_ID: REP-FULL-FIELD-001
