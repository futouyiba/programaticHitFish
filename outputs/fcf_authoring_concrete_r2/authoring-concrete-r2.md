# FCF Authoring 具体化样本 R2｜配置表、中文伪脚本与逐步结果

**状态：WORKING / PRE-GATE / 演示数据；未 Promote，未选择最终 Config Table 或 DSL。**

这份附录把表达写到可填写、可复算的程度：同一输入在表格方案中对应哪些行，在中文伪脚本中执行哪些步骤，得到哪些中间值与类型化输出。完整覆盖 C01–C15 的范围处理，并补入 G1–G3、Q1–Q3 和最新鲈鱼五群样本。文中所有阈值、曲线、乘数、分档、MAX/BLEND 的具体演示使用均是可替换的样本选择，不是新增机制 Authority。

## 1. 本轮来源与边界

Source Map：Router → Project Current → Branch Index → Simplified V0 Working Main 做最小 Rebase；最新 Representation Design Gate R1 和鲈鱼深挖尾部 Working snapshot 处理过期未决；原 C01–C15 Mapping 保留鱼类故事边界。Existing Base Check：旧15例页面已有矩阵/伪代码，但尚不足以还原完整配置；本附录保留旧投影，以新行表补齐。Gap Classification：表列/行/中间计算属于 DOCUMENTATION GAP；曲线数值与候选聚合的最终标定属于 DEFERRED / NON-BLOCKING；生产空间顺序、C13 可玩范围仍未替 Owner 决定。

核心输入：[Representation Design Gate R1](https://app.notion.com/p/3d6a4137d23681eab6cfd3a535a8938a)、[原15例页面](https://app.notion.com/p/3d6a4137d236814ea872ed6305942594)、[案例映射](https://app.notion.com/p/3d6a4137d2368151b762e50bc5ce6dfd)、[Authoring Stress Working](https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3)、[鲈鱼五群最新 Working](https://app.notion.com/p/3d6a4137d23681e2af96e873eef9411a)。这些 Working 输入没有自动提升为 Current。

本稿骨架已经落实为：共用语义 → 具体表 Schema → 每例样例行及中文脚本 → 输入/中间值/输出 → 相同修改操作 → 验证与边界。旧文的 C08/C09–C12 结构“等待 Owner”标记以最新 Gate 为准；旧独立审核不覆盖本附录。

## 2. 一屏模型：作者到底填什么

慢速世界快照 → GroupShare（同物种组成） → 已分配 FishGroup → Bake（空间权重）。既有 PresentationSession → 合法 semantic particle → Root Semantic Occurrence → OpportunityId → Evaluation Scope → 群专属 Response。Quality 使用已经选定的 Group 基准分布，读原始 facts 并列修正，归一化后交既有抽样 Owner。以上箭头表示合同依赖，不是本附录新造的完整抽签顺序。

表格作者选择固定模板、填 Profile/参数、连接 Predicate 树、填写结果行；模板内部代码是共享工程成本。中文脚本作者仍引用同一份数值表，把条件与因果关系连续写出来；本稿把每个模板实际展开，不能只用“执行某 Profile”隐藏逻辑。

ResponseStrength 是本演示的类型化归一强度标量，不等于最终中鱼概率；SpatialDistributionWeight 是空间适宜性输出，不改 Species 总量；FishGroupShareVector 仅描述物种内组成；QualityDistribution 仅是归一化分布。到生产 Typed Result 的字段映射须跟随现有合同，本文这些短字段名不是宣告新增正式 API。

## 3. 两种方案的完整物理布局

方案 A 有 **11 张作者数据表 + 1 张只读 TemplateStep 目录**。方案 B 有 **5 张共用数据表（Binding、Parameter、CurvePoint、QualityWeight、Boundary）+ 1 份 Script 文本集合**。B 把 Slot/Predicate/Member/ResponseBand/GroupShare/QualityModifier 的内容写入正文；没有消灭其逻辑与校验成本。其 Script 记录为 `binding_id, dialect_version, source`，一绑定一记录；这里 `dialect_version=CN_PSEUDO_R2`，不是已经实现的生产 DSL 编译器。两边都需模板/运行时实现，表数不是复杂度结论。

配置只接受下文列出的模板槽、算子、字段和输出；无任意循环、跳转、写世界状态或 RNG。DSL 中 `返回` 会终止该绑定；固定双通道均评价再聚合；配置 Predicate 子项换行/换序不构成新模板。修改 TemplateStep 的有语义 Gate/依赖关系是模板改动，不是调一个 Profile 或 Switch。

所有样例输入是本次快照的只读别名：slow.* 来自水体/时令 Resolver；target.* 来自空间目标 Resolver；weather.* 来自天气 Resolver；food.* 来自本 Opportunity 可用的 FoodField facts；response.* 来自既有 Scope 的鱼种/呈现匹配与刺激事实；gear.* 来自同一 Active Presentation Channel；quality_context.* 来自品质评价快照。连续 index 为[0,1]，距离m、深度m、温度°C、溶氧mg/L、光照lux，日期为1–366日，hook_size_index 是演示有序尺码。`target.cover_prey_tradeoff` 等复合量是演示输入适配别名，不能由本稿反推 Resolver 算法已经实现。输入不存在/非有限/单位错时返回 ValidationError；它不等于机制的“条件不满足”。没有隐式0、空字符串默认或二次随机。

公共曲线查询：节点 (x0,y0),(x1,y1) 间 `y=y0+(y1-y0)*(x-x0)/(x1-x0)`；范围外取端点。示例 Structure(0,1),(100,0.2)，距离25m得到0.8。表格与脚本使用同一曲线，不在脚本里偷偷增加自由算式。

## 4. 字段合同与完整全局行表

| 表 | 全列 | 去重实际行数 | 权限 |
| --- | --- | --- | --- |
| Binding | binding_id / surface / subject / template_id / status | 38 | 作者数据 |
| Slot | binding_id / slot / enabled / ref_kind / ref_id | 100 | 作者数据 |
| Parameter | parameter_id / type / value / unit | 32 | 作者数据 |
| CurvePoint | profile_id / x / y | 159 | 作者数据 |
| Predicate | node_id / kind / field / operator / parameter_id | 29 | 作者数据 |
| PredicateMember | parent_id / display_index / child_id | 17 | 作者数据 |
| ResponseBand | binding_id / priority / predicate_id / response_strength | 4 | 作者数据 |
| GroupShare | binding_id / group / predicate_id / share_kind / share_ref / input_field | 7 | 作者数据 |
| QualityWeight | binding_id / bucket / base_weight | 32 | 作者数据 |
| QualityModifier | binding_id / rule_id / predicate_id / bucket / multiplier | 64 | 作者数据 |
| Boundary | case_id / scope / reason | 3 | 作者数据 |
| TemplateStep | template_id / step / operation / input / output / failure | 46 | 只读目录 |

所有 PK/FK 和空值约定如下。Parameter 中数值二元列表使用 range<number>，BETWEEN 包含端点；列类型不是根据显示文本猜测。

### Binding

PK binding_id；surface=GROUP/BAKE/RESPONSE/QUALITY；template_id FK→只读模板目录。subject 是上游已选择的群/情景；不以字符串匹配在 Runtime 路由。status 区分演示 Working、情景及合成压力。

| binding_id | surface | subject | template_id | status |
| --- | --- | --- | --- | --- |
| C01_B | BAKE | AtlanticCod.Normal | S_FIXED | DEMO_WORKING |
| C02_B | BAKE | ChannelCatfish.Normal | S_FIXED | DEMO_WORKING |
| C05_B | BAKE | Walleye.Normal | S_FIXED | DEMO_WORKING |
| C03_R | RESPONSE | RainbowTrout.Normal | R_BANDS | DEMO_WORKING |
| C04_R | RESPONSE | BrownTrout.Normal | R_BANDS | DEMO_WORKING |
| C06_R | RESPONSE | Bluegill.Guarding | R_DEFENSE | DEMO_WORKING |
| C07_R | RESPONSE | Smallmouth.Parental | R_DEFENSE | DEMO_WORKING |
| C08_R | RESPONSE | Tilapia.Feeding | R_DUAL_FIXED | DEMO_WORKING |
| C09_R | RESPONSE | Paddlefish.FieldFeeding | R_FIELD | DEMO_WORKING |
| C10_R | RESPONSE | BigmouthBuffalo.FieldFeeding | R_FIELD | DEMO_WORKING |
| C11_R | RESPONSE | Mullet.FieldFeeding | R_FIELD | DEMO_WORKING |
| C12_N | RESPONSE | AtlanticSalmon.NormalFeeding | R_FEED | DEMO_WORKING |
| C12_M | RESPONSE | AtlanticSalmon.FreshwaterSpawningMigration | R_REACTION | DEMO_WORKING |
| C13_J | RESPONSE | Sockeye.JuvenileSuspended | R_FEED | SCENARIO_ONLY_NOT_PRODUCTION |
| C13_O | RESPONSE | Sockeye.OceanFeedingAdult | R_FEED | SCENARIO_ONLY_NOT_PRODUCTION |
| C13_S | RESPONSE | Sockeye.FreshwaterSpawningAdult | R_FEED | SCENARIO_ONLY_NOT_PRODUCTION |
| BASS_G | GROUP | LargemouthBass | G_SHARES | DEMO_WORKING |
| G1 | GROUP | G1_GuardNormal | G_SHARES | DEMO_WORKING |
| G2 | GROUP | G2_GuardNormal | G_SHARES | DEMO_WORKING |
| G3 | GROUP | SyntheticSeasonGroup | G_SHARES | SYNTHETIC_STRESS_ONLY |
| BASS_N_B | BAKE | LargemouthBass.NormalFeeding | S_FIXED | DEMO_WORKING |
| BASS_G_B | BAKE | LargemouthBass.Guarding | S_FIXED | DEMO_WORKING |
| BASS_C_B | BAKE | LargemouthBass.ColdSlow | S_COLD | DEMO_WORKING |
| BASS_S_B | BAKE | LargemouthBass.SummerStress | S_SUMMER | DEMO_WORKING |
| BASS_F_B | BAKE | LargemouthBass.ForageChase | S_FORAGE | DEMO_WORKING |
| BASS_N_R | RESPONSE | LargemouthBass.NormalFeeding | R_FEED | DEMO_WORKING |
| BASS_F_R | RESPONSE | LargemouthBass.ForageChase | R_FEED | DEMO_WORKING |
| BASS_G_R | RESPONSE | LargemouthBass.Guarding | R_DEFENSE | DEMO_WORKING |
| BASS_C_R | RESPONSE | LargemouthBass.ColdSlow | R_FEED_REACTION | DEMO_WORKING |
| BASS_S_R | RESPONSE | LargemouthBass.SummerStress | R_FEED_REACTION | DEMO_WORKING |
| BASS_N_Q | QUALITY | LargemouthBass.NormalFeeding | Q_PARALLEL | DEMO_WORKING |
| BASS_G_Q | QUALITY | LargemouthBass.Guarding | Q_PARALLEL | DEMO_WORKING |
| BASS_C_Q | QUALITY | LargemouthBass.ColdSlow | Q_PARALLEL | DEMO_WORKING |
| BASS_S_Q | QUALITY | LargemouthBass.SummerStress | Q_PARALLEL | DEMO_WORKING |
| BASS_F_Q | QUALITY | LargemouthBass.ForageChase | Q_PARALLEL | DEMO_WORKING |
| Q1 | QUALITY | IllustrativeQuality | Q_PARALLEL | DEMO_WORKING |
| Q2 | QUALITY | IllustrativeQuality | Q_PARALLEL | DEMO_WORKING |
| Q3 | QUALITY | IllustrativeQuality | Q_PARALLEL | DEMO_WORKING |

### Slot

PK(binding_id,slot)，binding FK；slot 必须属于该模板白名单。enabled 为 bool；ref_kind=PROFILE/PARAMETER/SWITCH。PROFILE/PARAMETER 开启时 ref_id 必须存在且类型匹配，关闭时 N/A。纯 SWITCH 的 ref_id 始终 N/A，唯一真值源就是 enabled，没有第二个 bool Parameter。可关 Slot 没有 Side effect，也不能调整步骤位置。

| binding_id | slot | enabled | ref_kind | ref_id |
| --- | --- | --- | --- | --- |
| C01_B | Temperature | True | PROFILE | C01_B_Temperature |
| C01_B | Anchor | True | PARAMETER | C01_B_Anchor |
| C01_B | Structure | True | PROFILE | C01_B_Structure |
| C01_B | Depth | True | PROFILE | C01_B_Depth |
| C01_B | Light | False | PROFILE | N/A |
| C01_B | ColdFront | False | SWITCH | N/A |
| C01_B | Cover | False | PROFILE | N/A |
| C01_B | Deep | False | PROFILE | N/A |
| C02_B | Temperature | True | PROFILE | C02_B_Temperature |
| C02_B | Anchor | True | PARAMETER | C02_B_Anchor |
| C02_B | Structure | True | PROFILE | C02_B_Structure |
| C02_B | Depth | True | PROFILE | C02_B_Depth |
| C02_B | Light | False | PROFILE | N/A |
| C02_B | ColdFront | False | SWITCH | N/A |
| C02_B | Cover | False | PROFILE | N/A |
| C02_B | Deep | False | PROFILE | N/A |
| C05_B | Temperature | True | PROFILE | C05_B_Temperature |
| C05_B | Anchor | True | PARAMETER | C05_B_Anchor |
| C05_B | Structure | True | PROFILE | C05_B_Structure |
| C05_B | Depth | True | PROFILE | C05_B_Depth |
| C05_B | Light | True | PROFILE | C05_B_Light |
| C05_B | ColdFront | False | SWITCH | N/A |
| C05_B | Cover | False | PROFILE | N/A |
| C05_B | Deep | False | PROFILE | N/A |
| C03_R | Default | True | PARAMETER | C03_R_Default |
| C04_R | Default | True | PARAMETER | C04_R_Default |
| C06_R | Defense | True | PROFILE | C06_R_Defense |
| C07_R | Defense | True | PROFILE | C07_R_Defense |
| C08_R | Grazing | True | PROFILE | C08_R_Grazing |
| C08_R | Suspended | True | PROFILE | C08_R_Suspended |
| C09_R | Density | True | PROFILE | C09_R_Density |
| C09_R | Suitability | True | PROFILE | C09_R_Suitability |
| C09_R | Match | True | PROFILE | C09_R_Match |
| C10_R | Density | True | PROFILE | C10_R_Density |
| C10_R | Suitability | True | PROFILE | C10_R_Suitability |
| C10_R | Match | True | PROFILE | C10_R_Match |
| C11_R | Density | True | PROFILE | C11_R_Density |
| C11_R | Suitability | True | PROFILE | C11_R_Suitability |
| C11_R | Match | True | PROFILE | C11_R_Match |
| C12_N | Match | True | PROFILE | C12_N_Match |
| C12_N | Presentation | True | PROFILE | C12_N_Presentation |
| C12_N | Familiarity | False | PROFILE | N/A |
| C12_M | Salience | True | PROFILE | C12_M_Salience |
| C12_M | Pursuit | True | PROFILE | C12_M_Pursuit |
| C13_J | Match | True | PROFILE | C13_J_Match |
| C13_J | Presentation | True | PROFILE | C13_J_Presentation |
| C13_J | Familiarity | False | PROFILE | N/A |
| C13_O | Match | True | PROFILE | C13_O_Match |
| C13_O | Presentation | True | PROFILE | C13_O_Presentation |
| C13_O | Familiarity | False | PROFILE | N/A |
| C13_S | Match | True | PROFILE | C13_S_Match |
| C13_S | Presentation | True | PROFILE | C13_S_Presentation |
| C13_S | Familiarity | False | PROFILE | N/A |
| BASS_N_B | Temperature | True | PROFILE | BASS_N_B_Temperature |
| BASS_N_B | Anchor | True | PARAMETER | BASS_N_B_Anchor |
| BASS_N_B | Structure | True | PROFILE | BASS_N_B_Structure |
| BASS_N_B | Depth | True | PROFILE | BASS_N_B_Depth |
| BASS_N_B | Light | False | PROFILE | N/A |
| BASS_N_B | ColdFront | True | SWITCH | N/A |
| BASS_N_B | Cover | True | PROFILE | BASS_N_B_Cover |
| BASS_N_B | Deep | True | PROFILE | BASS_N_B_Deep |
| BASS_G_B | Temperature | True | PROFILE | BASS_G_B_Temperature |
| BASS_G_B | Anchor | True | PARAMETER | BASS_G_B_Anchor |
| BASS_G_B | Structure | True | PROFILE | BASS_G_B_Structure |
| BASS_G_B | Depth | True | PROFILE | BASS_G_B_Depth |
| BASS_G_B | Light | False | PROFILE | N/A |
| BASS_G_B | ColdFront | False | SWITCH | N/A |
| BASS_G_B | Cover | False | PROFILE | N/A |
| BASS_G_B | Deep | False | PROFILE | N/A |
| BASS_C_B | Warmth | True | PROFILE | BASS_C_B_Warmth |
| BASS_C_B | Stability | True | PROFILE | BASS_C_B_Stability |
| BASS_C_B | Refuge | True | PROFILE | BASS_C_B_Refuge |
| BASS_S_B | OxygenMin | True | PARAMETER | BASS_S_B_OxygenMin |
| BASS_S_B | Cooling | True | PROFILE | BASS_S_B_Cooling |
| BASS_S_B | Oxygen | True | PROFILE | BASS_S_B_Oxygen |
| BASS_S_B | Tradeoff | True | PROFILE | BASS_S_B_Tradeoff |
| BASS_F_B | ForageMin | True | PARAMETER | BASS_F_B_ForageMin |
| BASS_F_B | Forage | True | PROFILE | BASS_F_B_Forage |
| BASS_F_B | Vertical | True | PROFILE | BASS_F_B_Vertical |
| BASS_F_B | OpenWater | True | PROFILE | BASS_F_B_OpenWater |
| BASS_F_B | Temperature | True | PROFILE | BASS_F_B_Temperature |
| BASS_F_B | Oxygen | True | PROFILE | BASS_F_B_Oxygen |
| BASS_F_B | ColdFront | True | SWITCH | N/A |
| BASS_F_B | Cover | True | PROFILE | BASS_F_B_Cover |
| BASS_F_B | Deep | True | PROFILE | BASS_F_B_Deep |
| BASS_N_R | Match | True | PROFILE | BASS_N_R_Match |
| BASS_N_R | Presentation | True | PROFILE | BASS_N_R_Presentation |
| BASS_N_R | Familiarity | True | PROFILE | BASS_N_R_Familiarity |
| BASS_F_R | Match | True | PROFILE | BASS_F_R_Match |
| BASS_F_R | Presentation | True | PROFILE | BASS_F_R_Presentation |
| BASS_F_R | Familiarity | True | PROFILE | BASS_F_R_Familiarity |
| BASS_G_R | Defense | True | PROFILE | BASS_G_R_Defense |
| BASS_C_R | Match | True | PROFILE | BASS_C_R_Match |
| BASS_C_R | Presentation | True | PROFILE | BASS_C_R_Presentation |
| BASS_C_R | Salience | True | PROFILE | BASS_C_R_Salience |
| BASS_C_R | Pursuit | True | PROFILE | BASS_C_R_Pursuit |
| BASS_S_R | Match | True | PROFILE | BASS_S_R_Match |
| BASS_S_R | Presentation | True | PROFILE | BASS_S_R_Presentation |
| BASS_S_R | Salience | True | PROFILE | BASS_S_R_Salience |
| BASS_S_R | Pursuit | True | PROFILE | BASS_S_R_Pursuit |

### Parameter

PK parameter_id；type=number/bool/string/set<string>；value 按 type 解析（BETWEEN 的数值二元范围见特例）；unit 必须一致。所有本批数字是 DEMO 校验值，不是生态/平衡标定。

| parameter_id | type | value | unit |
| --- | --- | --- | --- |
| C01_B_Anchor | string | stable_cover | category |
| C02_B_Anchor | string | stable_cover | category |
| C05_B_Anchor | string | stable_cover | category |
| C03_R_Default | number | 0 | 1 |
| C03_good_match_value | number | 0.7 | 1 |
| C03_drift_value | number | 0.6 | 1 |
| C03_some_match_value | number | 0.3 | 1 |
| C04_R_Default | number | 0 | 1 |
| C04_good_match_value | number | 0.7 | 1 |
| C04_some_match_value | number | 0.3 | 1 |
| guard_dates_value | range<number> | [100,160] | day_of_year |
| guard_temp_value | number | 15 | °C |
| guard_nest_value | set<string> | ["nest_cover"] | 1 |
| cold_any_value | number | 0 | 1 |
| summer_any_value | number | 0 | 1 |
| forage_state_value | bool | True | 1 |
| forage_available_value | number | 0 | 1 |
| BassGuardShare | number | 0.2 | 1 |
| g3_spring_date_value | range<number> | [80,130] | day_of_year |
| g3_warm_value | number | 12 | °C |
| g3_fall_date_value | range<number> | [250,290] | day_of_year |
| g3_cool_value | number | 18 | °C |
| G3Share | number | 0.25 | 1 |
| BASS_N_B_Anchor | string | stable_cover | category |
| BASS_G_B_Anchor | string | nest_site | category |
| BASS_S_B_OxygenMin | number | 3 | mg/L |
| BASS_F_B_ForageMin | number | 0.2 | 1 |
| q_hook_value | number | 3 | 1 |
| q_bait_value | number | 8 | cm |
| q_inactive_value | set<string> | ["inactive"] | 1 |
| q_cold_value | number | 8 | °C |
| q_night_value | set<string> | ["night"] | 1 |

### CurvePoint

PK(profile_id,x)；x 严格递增、有限，y∈[0,1]。至少两点；线性插值、两端夹持。不同 Profile 不混单位；输入量纲由固定 Slot 定义。没有未写出的 spline 或随机噪声。

| profile_id | x | y |
| --- | --- | --- |
| C01_B_Temperature | 0 | 0.2 |
| C01_B_Temperature | 10 | 1 |
| C01_B_Temperature | 20 | 0.2 |
| C01_B_Structure | 0 | 1 |
| C01_B_Structure | 100 | 0.2 |
| C01_B_Depth | 0 | 0.1 |
| C01_B_Depth | 20 | 1 |
| C01_B_Depth | 60 | 0.3 |
| C02_B_Temperature | 5 | 0.2 |
| C02_B_Temperature | 25 | 1 |
| C02_B_Temperature | 35 | 0.3 |
| C02_B_Structure | 0 | 1 |
| C02_B_Structure | 100 | 0.4 |
| C02_B_Depth | 0 | 0.2 |
| C02_B_Depth | 3 | 1 |
| C02_B_Depth | 15 | 0.3 |
| C05_B_Temperature | 0 | 0.2 |
| C05_B_Temperature | 15 | 1 |
| C05_B_Temperature | 30 | 0.1 |
| C05_B_Structure | 0 | 1 |
| C05_B_Structure | 100 | 0.2 |
| C05_B_Depth | 0 | 0.2 |
| C05_B_Depth | 8 | 1 |
| C05_B_Depth | 25 | 0.4 |
| C05_B_Light | 0 | 1 |
| C05_B_Light | 100 | 0.8 |
| C05_B_Light | 1000 | 0.2 |
| C06_R_Defense | 0 | 0 |
| C06_R_Defense | 0.5 | 0.6 |
| C06_R_Defense | 1 | 0.9 |
| C07_R_Defense | 0 | 0 |
| C07_R_Defense | 0.5 | 0.7 |
| C07_R_Defense | 1 | 1 |
| C08_R_Grazing | 0 | 0 |
| C08_R_Grazing | 1 | 0.8 |
| C08_R_Suspended | 0 | 0 |
| C08_R_Suspended | 1 | 0.9 |
| C09_R_Density | 0 | 0 |
| C09_R_Density | 1 | 0.8 |
| C09_R_Suitability | 0 | 0 |
| C09_R_Suitability | 1 | 1 |
| C09_R_Match | 0 | 0 |
| C09_R_Match | 1 | 1 |
| C10_R_Density | 0 | 0 |
| C10_R_Density | 1 | 0.8 |
| C10_R_Suitability | 0 | 0 |
| C10_R_Suitability | 1 | 1 |
| C10_R_Match | 0 | 0 |
| C10_R_Match | 1 | 1 |
| C11_R_Density | 0 | 0 |
| C11_R_Density | 1 | 0.8 |
| C11_R_Suitability | 0 | 0 |
| C11_R_Suitability | 1 | 1 |
| C11_R_Match | 0 | 0 |
| C11_R_Match | 1 | 1 |
| C12_N_Match | 0 | 0 |
| C12_N_Match | 1 | 1 |
| C12_N_Presentation | 0 | 0 |
| C12_N_Presentation | 1 | 1 |
| C12_M_Salience | 0 | 0 |
| C12_M_Salience | 1 | 0.5 |
| C12_M_Pursuit | 0 | 1 |
| C12_M_Pursuit | 1 | 0.1 |
| C13_J_Match | 0 | 0 |
| C13_J_Match | 1 | 0.8 |
| C13_J_Presentation | 0 | 0 |
| C13_J_Presentation | 1 | 1 |
| C13_O_Match | 0 | 0 |
| C13_O_Match | 1 | 1 |
| C13_O_Presentation | 0 | 0 |
| C13_O_Presentation | 1 | 1 |
| C13_S_Match | 0 | 0 |
| C13_S_Match | 1 | 0 |
| C13_S_Presentation | 0 | 0 |
| C13_S_Presentation | 1 | 1 |
| BassColdShare | 0 | 0 |
| BassColdShare | 1 | 0.3 |
| BassSummerShare | 0 | 0 |
| BassSummerShare | 1 | 0.4 |
| BassForageShare | 0 | 0 |
| BassForageShare | 1 | 0.2 |
| BASS_N_B_Temperature | 0 | 0.1 |
| BASS_N_B_Temperature | 20 | 1 |
| BASS_N_B_Temperature | 35 | 0.2 |
| BASS_N_B_Structure | 0 | 1 |
| BASS_N_B_Structure | 100 | 0.2 |
| BASS_N_B_Depth | 0 | 0.2 |
| BASS_N_B_Depth | 3 | 1 |
| BASS_N_B_Depth | 15 | 0.3 |
| BASS_G_B_Temperature | 0 | 0.1 |
| BASS_G_B_Temperature | 20 | 1 |
| BASS_G_B_Temperature | 35 | 0.2 |
| BASS_G_B_Structure | 0 | 1 |
| BASS_G_B_Structure | 10 | 0.2 |
| BASS_G_B_Depth | 0 | 0.2 |
| BASS_G_B_Depth | 3 | 1 |
| BASS_G_B_Depth | 15 | 0.3 |
| BASS_N_B_Cover | 0 | 1 |
| BASS_N_B_Cover | 100 | 0 |
| BASS_N_B_Deep | 0 | 0 |
| BASS_N_B_Deep | 1 | 1 |
| BASS_C_B_Warmth | 0 | 0 |
| BASS_C_B_Warmth | 1 | 1 |
| BASS_C_B_Stability | 0 | 0 |
| BASS_C_B_Stability | 1 | 1 |
| BASS_C_B_Refuge | 0 | 0 |
| BASS_C_B_Refuge | 1 | 1 |
| BASS_S_B_Cooling | 0 | 0 |
| BASS_S_B_Cooling | 1 | 1 |
| BASS_S_B_Oxygen | 0 | 0 |
| BASS_S_B_Oxygen | 1 | 1 |
| BASS_S_B_Tradeoff | 0 | 0 |
| BASS_S_B_Tradeoff | 1 | 1 |
| BASS_F_B_Forage | 0 | 0 |
| BASS_F_B_Forage | 1 | 1 |
| BASS_F_B_Vertical | 0 | 0 |
| BASS_F_B_Vertical | 1 | 1 |
| BASS_F_B_OpenWater | 0 | 0 |
| BASS_F_B_OpenWater | 1 | 1 |
| BASS_F_B_Temperature | 0 | 0.1 |
| BASS_F_B_Temperature | 20 | 1 |
| BASS_F_B_Temperature | 35 | 0.2 |
| BASS_F_B_Oxygen | 0 | 0 |
| BASS_F_B_Oxygen | 5 | 1 |
| BASS_F_B_Oxygen | 10 | 1 |
| BASS_F_B_Cover | 0 | 1 |
| BASS_F_B_Cover | 100 | 0 |
| BASS_F_B_Deep | 0 | 0 |
| BASS_F_B_Deep | 1 | 1 |
| BASS_N_R_Match | 0 | 0 |
| BASS_N_R_Match | 1 | 1 |
| BASS_N_R_Presentation | 0 | 0 |
| BASS_N_R_Presentation | 1 | 1 |
| BASS_F_R_Match | 0 | 0 |
| BASS_F_R_Match | 1 | 0.95 |
| BASS_F_R_Presentation | 0 | 0 |
| BASS_F_R_Presentation | 1 | 1 |
| BASS_N_R_Familiarity | 0 | 1 |
| BASS_N_R_Familiarity | 1 | 0.5 |
| BASS_F_R_Familiarity | 0 | 1 |
| BASS_F_R_Familiarity | 1 | 0.5 |
| BASS_G_R_Defense | 0 | 0 |
| BASS_G_R_Defense | 1 | 1 |
| BASS_C_R_Match | 0 | 0 |
| BASS_C_R_Match | 1 | 0.25 |
| BASS_C_R_Presentation | 0 | 0 |
| BASS_C_R_Presentation | 1 | 1 |
| BASS_C_R_Salience | 0 | 0 |
| BASS_C_R_Salience | 1 | 0.8 |
| BASS_C_R_Pursuit | 0 | 1 |
| BASS_C_R_Pursuit | 1 | 0.1 |
| BASS_S_R_Match | 0 | 0 |
| BASS_S_R_Match | 1 | 0.35 |
| BASS_S_R_Presentation | 0 | 0 |
| BASS_S_R_Presentation | 1 | 1 |
| BASS_S_R_Salience | 0 | 0 |
| BASS_S_R_Salience | 1 | 0.7 |
| BASS_S_R_Pursuit | 0 | 1 |
| BASS_S_R_Pursuit | 1 | 0.1 |

### Predicate

PK node_id；kind=ATOM/ALL/ANY/NOT。ATOM 的 field 是只读白名单字段，operator∈GE/GT/LE/EQ/BETWEEN/IN/CONTAINS_ANY；parameter_id FK。组合节点三个叶字段显式 N/A。BETWEEN 为闭区间；空集、缺失字段/类型错拒绝。

| node_id | kind | field | operator | parameter_id |
| --- | --- | --- | --- | --- |
| C03_good_match | ATOM | response.feeding_match | GE | C03_good_match_value |
| C03_drift | ATOM | response.natural_drift_fit | GE | C03_drift_value |
| C03_high | ALL | N/A | N/A | N/A |
| C03_some_match | ATOM | response.feeding_match | GE | C03_some_match_value |
| C04_good_match | ATOM | response.feeding_match | GE | C04_good_match_value |
| C04_some_match | ATOM | response.feeding_match | GE | C04_some_match_value |
| guard_dates | ATOM | slow.day_of_year | BETWEEN | guard_dates_value |
| guard_temp | ATOM | slow.recent5day_temp_c | GE | guard_temp_value |
| guard_nest | ATOM | slow.scene_structures | CONTAINS_ANY | guard_nest_value |
| guard_all | ALL | N/A | N/A | N/A |
| cold_any | ATOM | slow.cold_severity | GT | cold_any_value |
| summer_any | ATOM | slow.oxythermal_compression | GT | summer_any_value |
| forage_state | ATOM | slow.pelagic_forage_state | EQ | forage_state_value |
| forage_available | ATOM | slow.open_water_forage_availability | GT | forage_available_value |
| forage_all | ALL | N/A | N/A | N/A |
| g3_spring_date | ATOM | slow.day_of_year | BETWEEN | g3_spring_date_value |
| g3_warm | ATOM | slow.recent5day_temp_c | GE | g3_warm_value |
| g3_spring | ALL | N/A | N/A | N/A |
| g3_fall_date | ATOM | slow.day_of_year | BETWEEN | g3_fall_date_value |
| g3_cool | ATOM | slow.recent5day_temp_c | LE | g3_cool_value |
| g3_fall | ALL | N/A | N/A | N/A |
| g3_either | ANY | N/A | N/A | N/A |
| q_hook | ATOM | gear.hook_size_index | GE | q_hook_value |
| q_bait | ATOM | gear.bait_size_cm | GE | q_bait_value |
| q_big_gear | ALL | N/A | N/A | N/A |
| q_inactive | ATOM | quality_context.time_band | IN | q_inactive_value |
| q_cold | ATOM | quality_context.water_temp_c | LE | q_cold_value |
| q_night | ATOM | quality_context.time_band | IN | q_night_value |
| q_coldnight | ALL | N/A | N/A | N/A |

### PredicateMember

PK(parent_id,display_index)；parent/child FK→Predicate；ALL/ANY 至少一个子节点，NOT 恰一个；禁止环。display_index 只用于作者阅读，没有 Runtime 顺序意义；全部条件是纯读。

| parent_id | display_index | child_id |
| --- | --- | --- |
| C03_high | 1 | C03_good_match |
| C03_high | 2 | C03_drift |
| guard_all | 1 | guard_dates |
| guard_all | 2 | guard_temp |
| guard_all | 3 | guard_nest |
| forage_all | 1 | forage_state |
| forage_all | 2 | forage_available |
| g3_spring | 1 | g3_spring_date |
| g3_spring | 2 | g3_warm |
| g3_fall | 1 | g3_fall_date |
| g3_fall | 2 | g3_cool |
| g3_either | 1 | g3_spring |
| g3_either | 2 | g3_fall |
| q_big_gear | 1 | q_hook |
| q_big_gear | 2 | q_bait |
| q_coldnight | 1 | q_cold |
| q_coldnight | 2 | q_night |

### ResponseBand

PK(binding_id,priority)；仅 R_BANDS，priority 为唯一整数递增，predicate_id FK；结果 response_strength∈[0,1]。FIRST_MATCH；无命中用显式 Default。这里的 priority 是同一响应分档规则顺序，绝非 Defense/Feeding 优先级。

| binding_id | priority | predicate_id | response_strength |
| --- | --- | --- | --- |
| C03_R | 10 | C03_high | 0.8 |
| C03_R | 20 | C03_some_match | 0.25 |
| C04_R | 10 | C04_good_match | 0.8 |
| C04_R | 20 | C04_some_match | 0.25 |

### GroupShare

PK(binding_id,group)；predicate FK。share_kind=PARAMETER 时 share_ref→[0,1]标量且 input_field=N/A；PROFILE 时 ref→CurvePoint 并指定慢速输入。全部条件同快照、同时算；总和超1拒绝；Normal 不单列可编辑 Share。

| binding_id | group | predicate_id | share_kind | share_ref | input_field |
| --- | --- | --- | --- | --- | --- |
| BASS_G | Guarding | guard_all | PARAMETER | BassGuardShare | N/A |
| BASS_G | ColdSlow | cold_any | PROFILE | BassColdShare | slow.cold_severity |
| BASS_G | SummerStress | summer_any | PROFILE | BassSummerShare | slow.oxythermal_compression |
| BASS_G | ForageChase | forage_all | PROFILE | BassForageShare | slow.open_water_forage_availability |
| G1 | Guarding | guard_all | PARAMETER | BassGuardShare | N/A |
| G2 | Guarding | guard_all | PARAMETER | BassGuardShare | N/A |
| G3 | Seasonal | g3_either | PARAMETER | G3Share | N/A |

### QualityWeight

PK(binding_id,bucket)；bucket 固定 Small/Medium/Large/Rare 的演示枚举；base_weight 非负、至少一项正值。不声称这四桶已成为生产枚举，也不等同生命周期。

| binding_id | bucket | base_weight |
| --- | --- | --- |
| BASS_N_Q | Small | 50 |
| BASS_N_Q | Medium | 30 |
| BASS_N_Q | Large | 15 |
| BASS_N_Q | Rare | 5 |
| BASS_G_Q | Small | 20 |
| BASS_G_Q | Medium | 40 |
| BASS_G_Q | Large | 30 |
| BASS_G_Q | Rare | 10 |
| BASS_C_Q | Small | 55 |
| BASS_C_Q | Medium | 30 |
| BASS_C_Q | Large | 12 |
| BASS_C_Q | Rare | 3 |
| BASS_S_Q | Small | 50 |
| BASS_S_Q | Medium | 35 |
| BASS_S_Q | Large | 12 |
| BASS_S_Q | Rare | 3 |
| BASS_F_Q | Small | 25 |
| BASS_F_Q | Medium | 50 |
| BASS_F_Q | Large | 20 |
| BASS_F_Q | Rare | 5 |
| Q1 | Small | 50 |
| Q1 | Medium | 30 |
| Q1 | Large | 15 |
| Q1 | Rare | 5 |
| Q2 | Small | 50 |
| Q2 | Medium | 30 |
| Q2 | Large | 15 |
| Q2 | Rare | 5 |
| Q3 | Small | 50 |
| Q3 | Medium | 30 |
| Q3 | Large | 15 |
| Q3 | Rare | 5 |

### QualityModifier

PK(binding_id,rule_id,bucket)；predicate FK；multiplier 非负有限。命中行按桶连乘，未列桶×1；所有条件读原始快照；只归一化一次，抽样在外部。

| binding_id | rule_id | predicate_id | bucket | multiplier |
| --- | --- | --- | --- | --- |
| BASS_N_Q | BigGear | q_big_gear | Large | 1.5 |
| BASS_N_Q | BigGear | q_big_gear | Rare | 1.2 |
| BASS_N_Q | LowActivity | q_inactive | Small | 1.2 |
| BASS_N_Q | LowActivity | q_inactive | Medium | 1.2 |
| BASS_N_Q | LowActivity | q_inactive | Large | 0.7 |
| BASS_N_Q | LowActivity | q_inactive | Rare | 0.7 |
| BASS_N_Q | ColdNight | q_coldnight | Large | 0.8 |
| BASS_N_Q | ColdNight | q_coldnight | Rare | 0.8 |
| BASS_G_Q | BigGear | q_big_gear | Large | 1.5 |
| BASS_G_Q | BigGear | q_big_gear | Rare | 1.2 |
| BASS_G_Q | LowActivity | q_inactive | Small | 1.2 |
| BASS_G_Q | LowActivity | q_inactive | Medium | 1.2 |
| BASS_G_Q | LowActivity | q_inactive | Large | 0.7 |
| BASS_G_Q | LowActivity | q_inactive | Rare | 0.7 |
| BASS_G_Q | ColdNight | q_coldnight | Large | 0.8 |
| BASS_G_Q | ColdNight | q_coldnight | Rare | 0.8 |
| BASS_C_Q | BigGear | q_big_gear | Large | 1.5 |
| BASS_C_Q | BigGear | q_big_gear | Rare | 1.2 |
| BASS_C_Q | LowActivity | q_inactive | Small | 1.2 |
| BASS_C_Q | LowActivity | q_inactive | Medium | 1.2 |
| BASS_C_Q | LowActivity | q_inactive | Large | 0.7 |
| BASS_C_Q | LowActivity | q_inactive | Rare | 0.7 |
| BASS_C_Q | ColdNight | q_coldnight | Large | 0.8 |
| BASS_C_Q | ColdNight | q_coldnight | Rare | 0.8 |
| BASS_S_Q | BigGear | q_big_gear | Large | 1.5 |
| BASS_S_Q | BigGear | q_big_gear | Rare | 1.2 |
| BASS_S_Q | LowActivity | q_inactive | Small | 1.2 |
| BASS_S_Q | LowActivity | q_inactive | Medium | 1.2 |
| BASS_S_Q | LowActivity | q_inactive | Large | 0.7 |
| BASS_S_Q | LowActivity | q_inactive | Rare | 0.7 |
| BASS_S_Q | ColdNight | q_coldnight | Large | 0.8 |
| BASS_S_Q | ColdNight | q_coldnight | Rare | 0.8 |
| BASS_F_Q | BigGear | q_big_gear | Large | 1.5 |
| BASS_F_Q | BigGear | q_big_gear | Rare | 1.2 |
| BASS_F_Q | LowActivity | q_inactive | Small | 1.2 |
| BASS_F_Q | LowActivity | q_inactive | Medium | 1.2 |
| BASS_F_Q | LowActivity | q_inactive | Large | 0.7 |
| BASS_F_Q | LowActivity | q_inactive | Rare | 0.7 |
| BASS_F_Q | ColdNight | q_coldnight | Large | 0.8 |
| BASS_F_Q | ColdNight | q_coldnight | Rare | 0.8 |
| Q1 | BigGear | q_big_gear | Large | 1.5 |
| Q1 | BigGear | q_big_gear | Rare | 1.2 |
| Q1 | LowActivity | q_inactive | Small | 1.2 |
| Q1 | LowActivity | q_inactive | Medium | 1.2 |
| Q1 | LowActivity | q_inactive | Large | 0.7 |
| Q1 | LowActivity | q_inactive | Rare | 0.7 |
| Q1 | ColdNight | q_coldnight | Large | 0.8 |
| Q1 | ColdNight | q_coldnight | Rare | 0.8 |
| Q2 | BigGear | q_big_gear | Large | 1.5 |
| Q2 | BigGear | q_big_gear | Rare | 1.2 |
| Q2 | LowActivity | q_inactive | Small | 1.2 |
| Q2 | LowActivity | q_inactive | Medium | 1.2 |
| Q2 | LowActivity | q_inactive | Large | 0.7 |
| Q2 | LowActivity | q_inactive | Rare | 0.7 |
| Q2 | ColdNight | q_coldnight | Large | 0.8 |
| Q2 | ColdNight | q_coldnight | Rare | 0.8 |
| Q3 | BigGear | q_big_gear | Large | 1.5 |
| Q3 | BigGear | q_big_gear | Rare | 1.2 |
| Q3 | LowActivity | q_inactive | Small | 1.2 |
| Q3 | LowActivity | q_inactive | Medium | 1.2 |
| Q3 | LowActivity | q_inactive | Large | 0.7 |
| Q3 | LowActivity | q_inactive | Rare | 0.7 |
| Q3 | ColdNight | q_coldnight | Large | 0.8 |
| Q3 | ColdNight | q_coldnight | Rare | 0.8 |

### Boundary

PK case_id；scope=SCOPE_RESOLUTION/OUT_OF_SCOPE；reason 是作者范围说明，不是可执行 predicate。C14/C15 无 Binding 而非伪造 Response=0。

| case_id | scope | reason |
| --- | --- | --- |
| C13 | SCOPE_RESOLUTION | juvenile suspended story 不作为可玩成鱼的新 Template 证据；以下仅分别填满三个生命周期情景，排除生产 cluster 计数。 |
| C14 | OUT_OF_SCOPE | 宿主附着位于本次生成前 Response 表达范围外；没有合法 Binding/输出/运行步骤。 |
| C15 | OUT_OF_SCOPE | 响应无关的外部捕获机制；不得把锚鱼成功编成 Feeding Response。 |

### TemplateStep

PK(template_id,step)；是方案A须明确给工程/作者看的只读模板目录，不是普通配置表。operation/input/output/failure 展开固定因果；修改执行拓扑须创建/修改模板，经现有机制治理，不能让 Switch 偷改顺序。

| template_id | step | operation | input | output | failure |
| --- | --- | --- | --- | --- | --- |
| S_FIXED | 1 | 查分段线性曲线 | target.temperature_c × @Temperature | T | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FIXED | 2 | 按具名锚点读取距离，再查曲线 | target.anchor_distances_m[@Anchor] × @Structure | S | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FIXED | 3 | 查分段线性曲线 | target.depth_m × @Depth | D | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FIXED | 4 | 固定 Light Slot：关=1；开=查曲线 | target.illuminance_lux × @Light | L | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FIXED | 5 | 独立因子乘积 | T × S × D × L | BaseSpatialFit | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FIXED | 6 | 固定末端 Overlay：关=原值；开=BLEND(base,MAX(cover,deep),severity) | BaseSpatialFit / @Cover / @Deep / weather.cold_front_severity | SpatialDistributionWeight | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_BANDS | 1 | 只读同一 Opportunity Evaluation Scope | FeedingMatch / Presentation facts | facts | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_BANDS | 2 | 按显式 priority 递增测试条件；FIRST_MATCH | ResponseBand + Predicate | 第一条命中行 | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_BANDS | 3 | SET；无命中使用固定 Default Slot | response_strength 或 @Default | ResponseStrength | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_DEFENSE | 1 | 只读已准入的入侵强度 | response.intrusion_strength | intrusion | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_DEFENSE | 2 | 查 Defense 曲线 | intrusion × @Defense | ResponseStrength；立即返回 | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_DUAL_FIXED | 1 | 从同一快照评价固定 Grazing Slot | food.grazing_availability × @Grazing | G | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_DUAL_FIXED | 2 | 从同一快照评价固定 Suspended Slot | food.suspended_availability × @Suspended | S | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_DUAL_FIXED | 3 | 固定聚合 MAX（本样本的演示函数） | G,S | ResponseStrength | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FIELD | 1 | 使用已有 Session/Root/Opportunity/Scope；本模板不生成身份 | 同一 semantic particle 已准入 Scope | 只读 facts | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FIELD | 2 | 查 FoodField 的量级和适宜性 | food.density_index × @Density；food.suitability × @Suitability | DensityFit, SuitFit | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FIELD | 3 | 读取同一 Active Presentation Channel 的 FeedingMatch | response.feeding_match × @Match | PresentationFit | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FIELD | 4 | 乘积（演示函数）；不把帧数当次数 | DensityFit × SuitFit × PresentationFit | ResponseStrength | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FEED | 1 | 查匹配曲线 | response.feeding_match × @Match | F | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FEED | 2 | 查呈现曲线 | response.presentation_fit × @Presentation | P | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FEED | 3 | 固定只读 Familiarity Slot：关闭=1；开启=查曲线 | response.cue_familiarity × @Familiarity | U | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FEED | 4 | 相乘 | F × P × U | ResponseStrength | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_REACTION | 1 | 普通 Feeding 没有 Slot：分群已在上游完成 | Migration FishGroup | 只读刺激/追逐要求 | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_REACTION | 2 | 查刺激显著性与持续追逐容忍曲线 | response.trigger_salience × @Salience；response.sustained_pursuit_demand × @Pursuit | R,D | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_REACTION | 3 | 相乘；类型为 Response，不携带已证实动机 | R × D | ResponseStrength | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FEED_REACTION | 1 | 同一 Scope 评价 Feeding | response.feeding_match × @Match；response.presentation_fit × @Presentation | F=两 Fit 乘积 | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FEED_REACTION | 2 | 同一 Scope 评价 Reaction | response.trigger_salience × @Salience；response.sustained_pursuit_demand × @Pursuit | R=两 Fit 乘积 | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| R_FEED_REACTION | 3 | 固定聚合 MAX（Working Candidate 的演示实例） | F,R | ResponseStrength | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| G_SHARES | 1 | 读取同一物种的同一慢速世界快照 | GroupShare + Predicate | 各 special predicate | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| G_SHARES | 2 | 并列评价：不命中=0；命中=标量或曲线 | share_ref / input_field | special shares | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| G_SHARES | 3 | 验证每项[0,1]且和≤1 | special shares | 有效 share vector | 超限 → ValidationError；不归一化、不顺序扣减 |
| G_SHARES | 4 | 补 Normal residual | 1 − SUM(special) | FishGroupShareVector | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| Q_PARALLEL | 1 | 取已经选定的 Group 对应基准分布 | QualityWeight | base[bucket] | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| Q_PARALLEL | 2 | 所有条件只读同一原始 facts | QualityModifier + Predicate | 并列命中 modifier | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| Q_PARALLEL | 3 | 每桶原始权重乘所有命中乘数 | base[b] × PRODUCT(multipliers[b]) | raw[b] | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| Q_PARALLEL | 4 | 一次归一化 | raw / SUM(raw) | QualityDistribution | 负数/非有限/总和≤0 → ValidationError；本模板不抽签 |
| S_COLD | 1 | 查相对温暖、稳定、低能耗避难所 | target.relative_warmth × @Warmth；target.stability × @Stability；target.low_energy_refuge × @Refuge | W,S,R | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_COLD | 2 | 固定乘积 | W × S × R | SpatialDistributionWeight | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_SUMMER | 1 | 目标溶氧硬 Gate | target.oxygen_mg_l ≥ @OxygenMin | 通过目标 | 不通过 → 空间权重0并立即返回；不执行后续适宜性 |
| S_SUMMER | 2 | 查相对降温、氧余量、遮蔽/猎物折中 | target.relative_cooling × @Cooling；target.oxygen_margin × @Oxygen；target.cover_prey_tradeoff × @Tradeoff | C,O,T | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_SUMMER | 3 | 固定乘积 | C × O × T | SpatialDistributionWeight | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FORAGE | 1 | 猎物场准入 Gate | target.forage_school_intensity ≥ @ForageMin | 通过目标 | 不通过 → 空间权重0并立即返回；Overlay不得复活 |
| S_FORAGE | 2 | 猎物主锚点及垂向匹配 | target.forage_school_intensity × @Forage；target.vertical_alignment × @Vertical | F,V | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FORAGE | 3 | 温度、氧、开放水环境适宜性 | target.temperature_c × @Temperature；target.oxygen_mg_l × @Oxygen；target.open_water_context × @OpenWater | T,O,W | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FORAGE | 4 | 固定乘积 | F × V × T × O × W | BaseSpatialFit | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |
| S_FORAGE | 5 | 固定末端 ColdFront Overlay；关=原值 | base / Cover / Deep / severity | SpatialDistributionWeight | 输入缺失/类型错 → ValidationError；不抽签、不写状态 |

## 5. 每个案例：样例行 → 中文脚本 → 中间值

### C01｜大西洋鳕：普通觅食空间

T→S→D 是填满样本所选的演示顺序；Owner 的生产空间顺序未冻结。三个独立乘因子交换顺序不改变结果。

样本涉及 4 张作者表、18 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 10,
  "target.anchor_distances_m": {
    "stable_cover": 25
  },
  "target.depth_m": 20
}
```

**C01_B**
```text
表达 C01_B 用于 AtlanticCod.Normal / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @C01_B_Temperature
  Anchor = @C01_B_Anchor
  Structure = @C01_B_Structure
  Depth = @C01_B_Depth
  Light = 关闭（无引用）
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@C01_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@C01_B_Anchor]
S = 查曲线(@C01_B_Structure, AnchorDistance)
D = 查曲线(@C01_B_Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(关闭槽位（不可读取）, target.illuminance_lux) 否则 1
Base = T × S × D × L
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(关闭槽位（不可读取）, target.cover_distance_m)
Deep = 查曲线(关闭槽位（不可读取）, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "C01",
  "binding": "C01_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "stable_cover",
    "AnchorDistance": 25,
    "Structure": 0.8,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Base": 0.8
  },
  "result": 0.8
}
```

### C02｜斑点叉尾鮰：近底空间

普通近底觅食样本；气味留在 Exposure Owner，本表不再扣一次 Feeding。生产空间顺序未冻结。

样本涉及 4 张作者表、18 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 25,
  "target.anchor_distances_m": {
    "stable_cover": 50
  },
  "target.depth_m": 3
}
```

**C02_B**
```text
表达 C02_B 用于 ChannelCatfish.Normal / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @C02_B_Temperature
  Anchor = @C02_B_Anchor
  Structure = @C02_B_Structure
  Depth = @C02_B_Depth
  Light = 关闭（无引用）
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@C02_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@C02_B_Anchor]
S = 查曲线(@C02_B_Structure, AnchorDistance)
D = 查曲线(@C02_B_Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(关闭槽位（不可读取）, target.illuminance_lux) 否则 1
Base = T × S × D × L
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(关闭槽位（不可读取）, target.cover_distance_m)
Deep = 查曲线(关闭槽位（不可读取）, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "C02",
  "binding": "C02_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "stable_cover",
    "AnchorDistance": 50,
    "Structure": 0.7,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Base": 0.7
  },
  "result": 0.7000000000000001
}
```

### C03｜虹鳟：自然漂流匹配

明确 FIRST_MATCH + 默认0；结果只到 ResponseStrength，不创建 Follow/Track/Attack 状态或后生成追击。

样本涉及 6 张作者表、14 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.feeding_match": 0.8,
  "response.natural_drift_fit": 0.7
}
```

**C03_R**
```text
表达 C03_R 用于 RainbowTrout.Normal / RESPONSE
模板 R_BANDS（固定结构，仅展开便于阅读）
配置：
  Default = @C03_R_Default
执行：
读取 本次 Scope 的只读 facts
按以下 priority 顺序，第一条满足就返回 指定响应强度
优先级 10：若 (response.feeding_match GE @C03_good_match_value AND response.natural_drift_fit GE @C03_drift_value)：返回 响应强度(0.8)
优先级 20：若 response.feeding_match GE @C03_some_match_value：返回 响应强度(0.25)
否则 返回 响应强度(@C03_R_Default)
```

本例结果：
```json
{
  "case": "C03",
  "binding": "C03_R",
  "template": "R_BANDS",
  "intermediate": {
    "C03_high": true
  },
  "result": 0.8
}
```

### C04｜褐鳟：普通摄食响应

明确 FIRST_MATCH + 默认0；结果只到 ResponseStrength，不创建 Follow/Track/Attack 状态或后生成追击。

样本涉及 5 张作者表、9 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.feeding_match": 0.8
}
```

**C04_R**
```text
表达 C04_R 用于 BrownTrout.Normal / RESPONSE
模板 R_BANDS（固定结构，仅展开便于阅读）
配置：
  Default = @C04_R_Default
执行：
读取 本次 Scope 的只读 facts
按以下 priority 顺序，第一条满足就返回 指定响应强度
优先级 10：若 response.feeding_match GE @C04_good_match_value：返回 响应强度(0.8)
优先级 20：若 response.feeding_match GE @C04_some_match_value：返回 响应强度(0.25)
否则 返回 响应强度(@C04_R_Default)
```

本例结果：
```json
{
  "case": "C04",
  "binding": "C04_R",
  "template": "R_BANDS",
  "intermediate": {
    "C04_good_match": true
  },
  "result": 0.8
}
```

### C05｜玻璃梭鲈：低光空间

Light 是 S_FIXED 预定义 Slot；本例开启。没有新建昼夜 Runtime Mode，生产空间顺序未冻结。

样本涉及 4 张作者表、21 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 15,
  "target.anchor_distances_m": {
    "stable_cover": 0
  },
  "target.depth_m": 8,
  "target.illuminance_lux": 100
}
```

**C05_B**
```text
表达 C05_B 用于 Walleye.Normal / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @C05_B_Temperature
  Anchor = @C05_B_Anchor
  Structure = @C05_B_Structure
  Depth = @C05_B_Depth
  Light = @C05_B_Light
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@C05_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@C05_B_Anchor]
S = 查曲线(@C05_B_Structure, AnchorDistance)
D = 查曲线(@C05_B_Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(@C05_B_Light, target.illuminance_lux) 否则 1
Base = T × S × D × L
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(关闭槽位（不可读取）, target.cover_distance_m)
Deep = 查曲线(关闭槽位（不可读取）, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "C05",
  "binding": "C05_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "stable_cover",
    "AnchorDistance": 0,
    "Structure": 1,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Light": 0.8,
    "Base": 0.8
  },
  "result": 0.8
}
```

### C06｜护巢蓝鳃太阳鱼

Previous: Defense/Feeding precedence 未决 → Updated: 上游 Guarding 分群，只评价 Defense 并返回。普通 Feeding Slot 不存在；不声称现实绝不摄食。

样本涉及 3 张作者表、5 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.intrusion_strength": 0.5
}
```

**C06_R**
```text
表达 C06_R 用于 Bluegill.Guarding / RESPONSE
模板 R_DEFENSE（固定结构，仅展开便于阅读）
配置：
  Defense = @C06_R_Defense
执行：
Defense = 查曲线(@C06_R_Defense, response.intrusion_strength)
返回 响应强度(Defense)
// 此模板没有普通 Feeding Slot，也没有 Defense/Feeding 优先级。
```

本例结果：
```json
{
  "case": "C06",
  "binding": "C06_R",
  "template": "R_DEFENSE",
  "intermediate": {
    "Defense": 0.6
  },
  "result": 0.6
}
```

### C07｜亲护小口黑鲈

Previous: Defense/Feeding precedence 未决 → Updated: 上游 Guarding 分群，只评价 Defense 并返回。普通 Feeding Slot 不存在；不声称现实绝不摄食。

样本涉及 3 张作者表、5 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.intrusion_strength": 0.5
}
```

**C07_R**
```text
表达 C07_R 用于 Smallmouth.Parental / RESPONSE
模板 R_DEFENSE（固定结构，仅展开便于阅读）
配置：
  Defense = @C07_R_Defense
执行：
Defense = 查曲线(@C07_R_Defense, response.intrusion_strength)
返回 响应强度(Defense)
// 此模板没有普通 Feeding Slot，也没有 Defense/Feeding 优先级。
```

本例结果：
```json
{
  "case": "C07",
  "binding": "C07_R",
  "template": "R_DEFENSE",
  "intermediate": {
    "Defense": 0.7
  },
  "result": 0.7
}
```

### C08｜罗非鱼：固定双通道

Previous: SELECT Profile candidate/结构未决 → Updated: 单 evaluator + 两固定 Slot 已闭合。MAX 只是本样本固定聚合函数，具体数值/聚合生产标定未完成；不是结构 blocker。

样本涉及 3 张作者表、7 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "food.grazing_availability": 0.75,
  "food.suspended_availability": 0.5
}
```

**C08_R**
```text
表达 C08_R 用于 Tilapia.Feeding / RESPONSE
模板 R_DUAL_FIXED（固定结构，仅展开便于阅读）
配置：
  Grazing = @C08_R_Grazing
  Suspended = @C08_R_Suspended
执行：
G = 查曲线(@C08_R_Grazing, food.grazing_availability)
S = 查曲线(@C08_R_Suspended, food.suspended_availability)
返回 响应强度(MAX(G, S))
// G、S 总是都算。没有按资源条件 SELECT Profile。
```

本例结果：
```json
{
  "case": "C08",
  "binding": "C08_R",
  "template": "R_DUAL_FIXED",
  "intermediate": {
    "Grazing": 0.6,
    "Suspended": 0.45
  },
  "result": 0.6000000000000001
}
```

### C09｜匙吻鲟：既有 Opportunity 的 FieldFeeding

Previous: 独立 FieldOpportunity 合同未决 → Updated: EXISTING_OPPORTUNITY_CONTRACT_REUSED。数值是呈现适配的演示输入；C09 使用不兼容呈现得到0，不从滤食或锚鱼记录推导钩饵接受。

样本涉及 3 张作者表、10 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "food.density_index": 0.75,
  "food.suitability": 0.5,
  "response.feeding_match": 0
}
```

**C09_R**
```text
表达 C09_R 用于 Paddlefish.FieldFeeding / RESPONSE
模板 R_FIELD（固定结构，仅展开便于阅读）
配置：
  Density = @C09_R_Density
  Suitability = @C09_R_Suitability
  Match = @C09_R_Match
执行：
// 外层已有 Opportunity；此处不创建 FieldOpportunity 或计时器。
D = 查曲线(@C09_R_Density, food.density_index)
S = 查曲线(@C09_R_Suitability, food.suitability)
M = 查曲线(@C09_R_Match, response.feeding_match)
返回 响应强度(D × S × M)
// M 来自同一 Session / Active Presentation Channel，不从“有食物”推导钩饵可接受。
```

本例结果：
```json
{
  "case": "C09",
  "binding": "C09_R",
  "template": "R_FIELD",
  "intermediate": {
    "Density": 0.6,
    "Suitability": 0.5,
    "Match": 0
  },
  "result": 0.0
}
```

### C10｜大口胭脂鱼：既有 Opportunity 的 FieldFeeding

Previous: 独立 FieldOpportunity 合同未决 → Updated: EXISTING_OPPORTUNITY_CONTRACT_REUSED。数值是呈现适配的演示输入；C09 使用不兼容呈现得到0，不从滤食或锚鱼记录推导钩饵接受。

样本涉及 3 张作者表、10 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "food.density_index": 0.75,
  "food.suitability": 0.5,
  "response.feeding_match": 0.5
}
```

**C10_R**
```text
表达 C10_R 用于 BigmouthBuffalo.FieldFeeding / RESPONSE
模板 R_FIELD（固定结构，仅展开便于阅读）
配置：
  Density = @C10_R_Density
  Suitability = @C10_R_Suitability
  Match = @C10_R_Match
执行：
// 外层已有 Opportunity；此处不创建 FieldOpportunity 或计时器。
D = 查曲线(@C10_R_Density, food.density_index)
S = 查曲线(@C10_R_Suitability, food.suitability)
M = 查曲线(@C10_R_Match, response.feeding_match)
返回 响应强度(D × S × M)
// M 来自同一 Session / Active Presentation Channel，不从“有食物”推导钩饵可接受。
```

本例结果：
```json
{
  "case": "C10",
  "binding": "C10_R",
  "template": "R_FIELD",
  "intermediate": {
    "Density": 0.6,
    "Suitability": 0.5,
    "Match": 0.5
  },
  "result": 0.15000000000000002
}
```

### C11｜鲻鱼：既有 Opportunity 的 FieldFeeding

Previous: 独立 FieldOpportunity 合同未决 → Updated: EXISTING_OPPORTUNITY_CONTRACT_REUSED。数值是呈现适配的演示输入；C09 使用不兼容呈现得到0，不从滤食或锚鱼记录推导钩饵接受。

样本涉及 3 张作者表、10 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "food.density_index": 0.75,
  "food.suitability": 0.5,
  "response.feeding_match": 0.8
}
```

**C11_R**
```text
表达 C11_R 用于 Mullet.FieldFeeding / RESPONSE
模板 R_FIELD（固定结构，仅展开便于阅读）
配置：
  Density = @C11_R_Density
  Suitability = @C11_R_Suitability
  Match = @C11_R_Match
执行：
// 外层已有 Opportunity；此处不创建 FieldOpportunity 或计时器。
D = 查曲线(@C11_R_Density, food.density_index)
S = 查曲线(@C11_R_Suitability, food.suitability)
M = 查曲线(@C11_R_Match, response.feeding_match)
返回 响应强度(D × S × M)
// M 来自同一 Session / Active Presentation Channel，不从“有食物”推导钩饵可接受。
```

本例结果：
```json
{
  "case": "C11",
  "binding": "C11_R",
  "template": "R_FIELD",
  "intermediate": {
    "Density": 0.6,
    "Suitability": 0.5,
    "Match": 0.8
  },
  "result": 0.24000000000000005
}
```

### C12｜大西洋鲑：上游分群后使用两个绑定

两个 Binding 分别被已分配的 Group 调用，同一鱼不连续执行两个 Binding。Migration 演示选择普通 Feeding 关闭；Reaction 不声称已证明领地攻击或任一单一生物动机。

样本涉及 3 张作者表、15 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.trigger_salience": 0.8,
  "response.sustained_pursuit_demand": 0.2
}
```

**C12_N**
```text
表达 C12_N 用于 AtlanticSalmon.NormalFeeding / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C12_N_Match
  Presentation = @C12_N_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C12_N_Match, response.feeding_match)
P = 查曲线(@C12_N_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C12",
  "binding": "C12_N",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.8,
    "Presentation": 0.75,
    "Feeding": 0.6000000000000001
  },
  "result": 0.6000000000000001
}
```

**C12_M**
```text
表达 C12_M 用于 AtlanticSalmon.FreshwaterSpawningMigration / RESPONSE
模板 R_REACTION（固定结构，仅展开便于阅读）
配置：
  Salience = @C12_M_Salience
  Pursuit = @C12_M_Pursuit
执行：
R = 查曲线(@C12_M_Salience, response.trigger_salience)
D = 查曲线(@C12_M_Pursuit, response.sustained_pursuit_demand)
返回 响应强度(R × D)
// 上游 Migration 分群；普通 Feeding 关闭。不读取 Runtime Stage Predicate。
```

本例结果：
```json
{
  "case": "C12",
  "binding": "C12_M",
  "template": "R_REACTION",
  "intermediate": {
    "Salience": 0.4,
    "Pursuit": 0.82,
    "Reaction": 0.328
  },
  "result": 0.328
}
```

### C13｜红鲑：三个独立情景，先解决范围

J 展示浮游/小型悬浮猎物 feeding；O 的 FeedingMatch 输入可覆盖浮游与较大猎物；S 演示停食取0。三者由上游 lifecycle 情景绑定，未证明 J 是正常可钓场景，不作 breaker、不加 Runtime Selector。

样本涉及 3 张作者表、24 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75
}
```

**C13_J**
```text
表达 C13_J 用于 Sockeye.JuvenileSuspended / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C13_J_Match
  Presentation = @C13_J_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C13_J_Match, response.feeding_match)
P = 查曲线(@C13_J_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C13",
  "binding": "C13_J",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.64,
    "Presentation": 0.75,
    "Feeding": 0.4800000000000001
  },
  "result": 0.4800000000000001
}
```

**C13_O**
```text
表达 C13_O 用于 Sockeye.OceanFeedingAdult / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C13_O_Match
  Presentation = @C13_O_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C13_O_Match, response.feeding_match)
P = 查曲线(@C13_O_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C13",
  "binding": "C13_O",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.8,
    "Presentation": 0.75,
    "Feeding": 0.6000000000000001
  },
  "result": 0.6000000000000001
}
```

**C13_S**
```text
表达 C13_S 用于 Sockeye.FreshwaterSpawningAdult / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @C13_S_Match
  Presentation = @C13_S_Presentation
  Familiarity = 关闭（无引用）
执行：
F = 查曲线(@C13_S_Match, response.feeding_match)
P = 查曲线(@C13_S_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(关闭槽位（不可读取）, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "C13",
  "binding": "C13_S",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.0,
    "Presentation": 0.75,
    "Feeding": 0.0
  },
  "result": 0.0
}
```

### C14｜七鳃鳗寄生附着

宿主附着位于本次生成前 Response 表达范围外；没有合法 Binding/输出/运行步骤。 表中用显式 OUT_OF_SCOPE；不使用空字符串或虚构的0响应。

Boundary 表中已列出，执行表与脚本均不适用。

### C15｜匙吻鲟锚鱼

响应无关的外部捕获机制；不得把锚鱼成功编成 Feeding Response。 表中用显式 OUT_OF_SCOPE；不使用空字符串或虚构的0响应。

Boundary 表中已列出，执行表与脚本均不适用。

### BASS-C｜大口黑鲈 ColdSlow

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。

样本涉及 8 张作者表、52 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 20,
  "target.anchor_distances_m": {
    "stable_cover": 25,
    "nest_site": 2.5
  },
  "target.depth_m": 3,
  "target.cover_distance_m": 20,
  "target.adjacent_deep_access": 0.9,
  "weather.cold_front_severity": 0.5,
  "target.relative_warmth": 0.8,
  "target.stability": 0.9,
  "target.low_energy_refuge": 0.75,
  "target.oxygen_mg_l": 5,
  "target.relative_cooling": 0.8,
  "target.oxygen_margin": 0.75,
  "target.cover_prey_tradeoff": 0.6,
  "target.forage_school_intensity": 0.8,
  "target.vertical_alignment": 0.75,
  "target.open_water_context": 1,
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.cue_familiarity": 0.4,
  "response.intrusion_strength": 0.8,
  "response.trigger_salience": 0.9,
  "response.sustained_pursuit_demand": 0.1,
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "active",
  "quality_context.water_temp_c": 20
}
```

**BASS_C_B**
```text
表达 BASS_C_B 用于 LargemouthBass.ColdSlow / BAKE
模板 S_COLD（固定结构，仅展开便于阅读）
配置：
  Warmth = @BASS_C_B_Warmth
  Stability = @BASS_C_B_Stability
  Refuge = @BASS_C_B_Refuge
执行：
W = 查曲线(@BASS_C_B_Warmth, target.relative_warmth)
S = 查曲线(@BASS_C_B_Stability, target.stability)
R = 查曲线(@BASS_C_B_Refuge, target.low_energy_refuge)
返回 空间权重(W × S × R)
```

本例结果：
```json
{
  "case": "BASS-C",
  "binding": "BASS_C_B",
  "template": "S_COLD",
  "intermediate": {
    "Warmth": 0.8,
    "Stability": 0.9,
    "Refuge": 0.75
  },
  "result": 0.54
}
```

**BASS_C_R**
```text
表达 BASS_C_R 用于 LargemouthBass.ColdSlow / RESPONSE
模板 R_FEED_REACTION（固定结构，仅展开便于阅读）
配置：
  Match = @BASS_C_R_Match
  Presentation = @BASS_C_R_Presentation
  Salience = @BASS_C_R_Salience
  Pursuit = @BASS_C_R_Pursuit
执行：
F = 查曲线(@BASS_C_R_Match, response.feeding_match) × 查曲线(@BASS_C_R_Presentation, response.presentation_fit)
R = 查曲线(@BASS_C_R_Salience, response.trigger_salience) × 查曲线(@BASS_C_R_Pursuit, response.sustained_pursuit_demand)
返回 响应强度(MAX(F, R))
// 两通道均评价；强短刺激与持续高速追逐是两个独立输入。
```

本例结果：
```json
{
  "case": "BASS-C",
  "binding": "BASS_C_R",
  "template": "R_FEED_REACTION",
  "intermediate": {
    "Match": 0.2,
    "Presentation": 0.75,
    "Salience": 0.72,
    "Pursuit": 0.91,
    "Feeding": 0.15000000000000002,
    "Reaction": 0.6552000000000001
  },
  "result": 0.6552000000000001
}
```

**BASS_C_Q**
```text
表达 BASS_C_Q 用于 LargemouthBass.ColdSlow / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "BASS-C",
  "binding": "BASS_C_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 55,
      "Medium": 30,
      "Large": 18.0,
      "Rare": 3.5999999999999996
    }
  },
  "result": {
    "Small": 0.5159474671669794,
    "Medium": 0.28142589118198874,
    "Large": 0.16885553470919326,
    "Rare": 0.03377110694183865
  }
}
```

### BASS-F｜大口黑鲈 ForageChase

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。 Forage 的食物场强度只在 Bake 使用，Response 不再乘同一密度。

样本涉及 8 张作者表、66 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 20,
  "target.anchor_distances_m": {
    "stable_cover": 25,
    "nest_site": 2.5
  },
  "target.depth_m": 3,
  "target.cover_distance_m": 20,
  "target.adjacent_deep_access": 0.9,
  "weather.cold_front_severity": 0.5,
  "target.relative_warmth": 0.8,
  "target.stability": 0.9,
  "target.low_energy_refuge": 0.75,
  "target.oxygen_mg_l": 5,
  "target.relative_cooling": 0.8,
  "target.oxygen_margin": 0.75,
  "target.cover_prey_tradeoff": 0.6,
  "target.forage_school_intensity": 0.8,
  "target.vertical_alignment": 0.75,
  "target.open_water_context": 1,
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.cue_familiarity": 0.4,
  "response.intrusion_strength": 0.8,
  "response.trigger_salience": 0.9,
  "response.sustained_pursuit_demand": 0.1,
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "active",
  "quality_context.water_temp_c": 20
}
```

**BASS_F_B**
```text
表达 BASS_F_B 用于 LargemouthBass.ForageChase / BAKE
模板 S_FORAGE（固定结构，仅展开便于阅读）
配置：
  ForageMin = @BASS_F_B_ForageMin
  Forage = @BASS_F_B_Forage
  Vertical = @BASS_F_B_Vertical
  OpenWater = @BASS_F_B_OpenWater
  Temperature = @BASS_F_B_Temperature
  Oxygen = @BASS_F_B_Oxygen
  ColdFront = 开启
  Cover = @BASS_F_B_Cover
  Deep = @BASS_F_B_Deep
执行：
若 target.forage_school_intensity < @BASS_F_B_ForageMin：返回 空间权重(0)
F = 查曲线(@BASS_F_B_Forage, target.forage_school_intensity)
V = 查曲线(@BASS_F_B_Vertical, target.vertical_alignment)
T = 查曲线(@BASS_F_B_Temperature, target.temperature_c)
O = 查曲线(@BASS_F_B_Oxygen, target.oxygen_mg_l)
W = 查曲线(@BASS_F_B_OpenWater, target.open_water_context)
Base = F × V × T × O × W
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(@BASS_F_B_Cover, target.cover_distance_m)
Deep = 查曲线(@BASS_F_B_Deep, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "BASS-F",
  "binding": "BASS_F_B",
  "template": "S_FORAGE",
  "intermediate": {
    "Forage": 0.8,
    "Vertical": 0.75,
    "Temperature": 1.0,
    "Oxygen": 1.0,
    "OpenWater": 1,
    "Base": 0.6,
    "Cover": 0.8,
    "Deep": 0.9,
    "Refuge": 0.9
  },
  "result": 0.75
}
```

**BASS_F_R**
```text
表达 BASS_F_R 用于 LargemouthBass.ForageChase / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @BASS_F_R_Match
  Presentation = @BASS_F_R_Presentation
  Familiarity = @BASS_F_R_Familiarity
执行：
F = 查曲线(@BASS_F_R_Match, response.feeding_match)
P = 查曲线(@BASS_F_R_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(@BASS_F_R_Familiarity, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "BASS-F",
  "binding": "BASS_F_R",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.76,
    "Presentation": 0.75,
    "Familiarity": 0.8,
    "Feeding": 0.5700000000000001
  },
  "result": 0.45600000000000007
}
```

**BASS_F_Q**
```text
表达 BASS_F_Q 用于 LargemouthBass.ForageChase / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "BASS-F",
  "binding": "BASS_F_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 25,
      "Medium": 50,
      "Large": 30.0,
      "Rare": 6.0
    }
  },
  "result": {
    "Small": 0.22522522522522523,
    "Medium": 0.45045045045045046,
    "Large": 0.2702702702702703,
    "Rare": 0.05405405405405406
  }
}
```

### BASS-G｜大口黑鲈 Guarding

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。

样本涉及 8 张作者表、51 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 20,
  "target.anchor_distances_m": {
    "stable_cover": 25,
    "nest_site": 2.5
  },
  "target.depth_m": 3,
  "target.cover_distance_m": 20,
  "target.adjacent_deep_access": 0.9,
  "weather.cold_front_severity": 0.5,
  "target.relative_warmth": 0.8,
  "target.stability": 0.9,
  "target.low_energy_refuge": 0.75,
  "target.oxygen_mg_l": 5,
  "target.relative_cooling": 0.8,
  "target.oxygen_margin": 0.75,
  "target.cover_prey_tradeoff": 0.6,
  "target.forage_school_intensity": 0.8,
  "target.vertical_alignment": 0.75,
  "target.open_water_context": 1,
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.cue_familiarity": 0.4,
  "response.intrusion_strength": 0.8,
  "response.trigger_salience": 0.9,
  "response.sustained_pursuit_demand": 0.1,
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "active",
  "quality_context.water_temp_c": 20
}
```

**BASS_G_B**
```text
表达 BASS_G_B 用于 LargemouthBass.Guarding / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @BASS_G_B_Temperature
  Anchor = @BASS_G_B_Anchor
  Structure = @BASS_G_B_Structure
  Depth = @BASS_G_B_Depth
  Light = 关闭（无引用）
  ColdFront = 关闭（无引用）
  Cover = 关闭（无引用）
  Deep = 关闭（无引用）
执行：
T = 查曲线(@BASS_G_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@BASS_G_B_Anchor]
S = 查曲线(@BASS_G_B_Structure, AnchorDistance)
D = 查曲线(@BASS_G_B_Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(关闭槽位（不可读取）, target.illuminance_lux) 否则 1
Base = T × S × D × L
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(关闭槽位（不可读取）, target.cover_distance_m)
Deep = 查曲线(关闭槽位（不可读取）, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "BASS-G",
  "binding": "BASS_G_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "nest_site",
    "AnchorDistance": 2.5,
    "Structure": 0.8,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Base": 0.8
  },
  "result": 0.8000000000000003
}
```

**BASS_G_R**
```text
表达 BASS_G_R 用于 LargemouthBass.Guarding / RESPONSE
模板 R_DEFENSE（固定结构，仅展开便于阅读）
配置：
  Defense = @BASS_G_R_Defense
执行：
Defense = 查曲线(@BASS_G_R_Defense, response.intrusion_strength)
返回 响应强度(Defense)
// 此模板没有普通 Feeding Slot，也没有 Defense/Feeding 优先级。
```

本例结果：
```json
{
  "case": "BASS-G",
  "binding": "BASS_G_R",
  "template": "R_DEFENSE",
  "intermediate": {
    "Defense": 0.8
  },
  "result": 0.8
}
```

**BASS_G_Q**
```text
表达 BASS_G_Q 用于 LargemouthBass.Guarding / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "BASS-G",
  "binding": "BASS_G_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 20,
      "Medium": 40,
      "Large": 45.0,
      "Rare": 12.0
    }
  },
  "result": {
    "Small": 0.17094017094017094,
    "Medium": 0.3418803418803419,
    "Large": 0.38461538461538464,
    "Rare": 0.10256410256410256
  }
}
```

### BASS-N｜大口黑鲈 NormalFeeding

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。

样本涉及 8 张作者表、61 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 20,
  "target.anchor_distances_m": {
    "stable_cover": 25,
    "nest_site": 2.5
  },
  "target.depth_m": 3,
  "target.cover_distance_m": 20,
  "target.adjacent_deep_access": 0.9,
  "weather.cold_front_severity": 0.5,
  "target.relative_warmth": 0.8,
  "target.stability": 0.9,
  "target.low_energy_refuge": 0.75,
  "target.oxygen_mg_l": 5,
  "target.relative_cooling": 0.8,
  "target.oxygen_margin": 0.75,
  "target.cover_prey_tradeoff": 0.6,
  "target.forage_school_intensity": 0.8,
  "target.vertical_alignment": 0.75,
  "target.open_water_context": 1,
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.cue_familiarity": 0.4,
  "response.intrusion_strength": 0.8,
  "response.trigger_salience": 0.9,
  "response.sustained_pursuit_demand": 0.1,
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "active",
  "quality_context.water_temp_c": 20
}
```

**BASS_N_B**
```text
表达 BASS_N_B 用于 LargemouthBass.NormalFeeding / BAKE
模板 S_FIXED（固定结构，仅展开便于阅读）
配置：
  Temperature = @BASS_N_B_Temperature
  Anchor = @BASS_N_B_Anchor
  Structure = @BASS_N_B_Structure
  Depth = @BASS_N_B_Depth
  Light = 关闭（无引用）
  ColdFront = 开启
  Cover = @BASS_N_B_Cover
  Deep = @BASS_N_B_Deep
执行：
T = 查曲线(@BASS_N_B_Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@BASS_N_B_Anchor]
S = 查曲线(@BASS_N_B_Structure, AnchorDistance)
D = 查曲线(@BASS_N_B_Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(关闭槽位（不可读取）, target.illuminance_lux) 否则 1
Base = T × S × D × L
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(@BASS_N_B_Cover, target.cover_distance_m)
Deep = 查曲线(@BASS_N_B_Deep, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)
```

本例结果：
```json
{
  "case": "BASS-N",
  "binding": "BASS_N_B",
  "template": "S_FIXED",
  "intermediate": {
    "Anchor": "stable_cover",
    "AnchorDistance": 25,
    "Structure": 0.8,
    "Temperature": 1.0,
    "Depth": 1.0,
    "Base": 0.8,
    "Cover": 0.8,
    "Deep": 0.9,
    "Refuge": 0.9
  },
  "result": 0.8500000000000001
}
```

**BASS_N_R**
```text
表达 BASS_N_R 用于 LargemouthBass.NormalFeeding / RESPONSE
模板 R_FEED（固定结构，仅展开便于阅读）
配置：
  Match = @BASS_N_R_Match
  Presentation = @BASS_N_R_Presentation
  Familiarity = @BASS_N_R_Familiarity
执行：
F = 查曲线(@BASS_N_R_Match, response.feeding_match)
P = 查曲线(@BASS_N_R_Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(@BASS_N_R_Familiarity, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。
```

本例结果：
```json
{
  "case": "BASS-N",
  "binding": "BASS_N_R",
  "template": "R_FEED",
  "intermediate": {
    "Match": 0.8,
    "Presentation": 0.75,
    "Familiarity": 0.8,
    "Feeding": 0.6000000000000001
  },
  "result": 0.4800000000000001
}
```

**BASS_N_Q**
```text
表达 BASS_N_Q 用于 LargemouthBass.NormalFeeding / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "BASS-N",
  "binding": "BASS_N_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 50,
      "Medium": 30,
      "Large": 22.5,
      "Rare": 6.0
    }
  },
  "result": {
    "Small": 0.4608294930875576,
    "Medium": 0.2764976958525346,
    "Large": 0.2073732718894009,
    "Rare": 0.055299539170506916
  }
}
```

### BASS-ROUTING｜鲈鱼：五群并列 Share

四项特殊 share 与 normal residual 共5群。为暴露 overlap 验证，此演示快照同时置入冷/夏压力；是合成测试，不声称典型水体会同时如此。

样本涉及 6 张作者表、33 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "slow.day_of_year": 120,
  "slow.recent5day_temp_c": 18,
  "slow.scene_structures": [
    "nest_cover"
  ],
  "slow.cold_severity": 0.5,
  "slow.oxythermal_compression": 0.25,
  "slow.pelagic_forage_state": true,
  "slow.open_water_forage_availability": 0.5
}
```

**BASS_G**
```text
表达 BASS_G 用于 LargemouthBass / GROUP
模板 G_SHARES（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
读取 同一份 slow_snapshot
Guarding = 若 (slow.day_of_year BETWEEN @guard_dates_value AND slow.recent5day_temp_c GE @guard_temp_value AND slow.scene_structures CONTAINS_ANY @guard_nest_value) 则 @BassGuardShare 否则 0
ColdSlow = 若 slow.cold_severity GT @cold_any_value 则 查曲线(@BassColdShare, slow.cold_severity) 否则 0
SummerStress = 若 slow.oxythermal_compression GT @summer_any_value 则 查曲线(@BassSummerShare, slow.oxythermal_compression) 否则 0
ForageChase = 若 (slow.pelagic_forage_state EQ @forage_state_value AND slow.open_water_forage_availability GT @forage_available_value) 则 查曲线(@BassForageShare, slow.open_water_forage_availability) 否则 0
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。
```

本例结果：
```json
{
  "case": "BASS-ROUTING",
  "binding": "BASS_G",
  "template": "G_SHARES",
  "intermediate": {
    "guard_all": true,
    "cold_any": true,
    "summer_any": true,
    "forage_all": true
  },
  "result": {
    "Guarding": 0.2,
    "ColdSlow": 0.15,
    "SummerStress": 0.1,
    "ForageChase": 0.1,
    "Normal": 0.45000000000000007
  }
}
```

### BASS-S｜大口黑鲈 SummerStress

Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。

样本涉及 8 张作者表、54 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "target.temperature_c": 20,
  "target.anchor_distances_m": {
    "stable_cover": 25,
    "nest_site": 2.5
  },
  "target.depth_m": 3,
  "target.cover_distance_m": 20,
  "target.adjacent_deep_access": 0.9,
  "weather.cold_front_severity": 0.5,
  "target.relative_warmth": 0.8,
  "target.stability": 0.9,
  "target.low_energy_refuge": 0.75,
  "target.oxygen_mg_l": 5,
  "target.relative_cooling": 0.8,
  "target.oxygen_margin": 0.75,
  "target.cover_prey_tradeoff": 0.6,
  "target.forage_school_intensity": 0.8,
  "target.vertical_alignment": 0.75,
  "target.open_water_context": 1,
  "response.feeding_match": 0.8,
  "response.presentation_fit": 0.75,
  "response.cue_familiarity": 0.4,
  "response.intrusion_strength": 0.8,
  "response.trigger_salience": 0.9,
  "response.sustained_pursuit_demand": 0.1,
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "active",
  "quality_context.water_temp_c": 20
}
```

**BASS_S_B**
```text
表达 BASS_S_B 用于 LargemouthBass.SummerStress / BAKE
模板 S_SUMMER（固定结构，仅展开便于阅读）
配置：
  OxygenMin = @BASS_S_B_OxygenMin
  Cooling = @BASS_S_B_Cooling
  Oxygen = @BASS_S_B_Oxygen
  Tradeoff = @BASS_S_B_Tradeoff
执行：
若 target.oxygen_mg_l < @BASS_S_B_OxygenMin：返回 空间权重(0)
C = 查曲线(@BASS_S_B_Cooling, target.relative_cooling)
O = 查曲线(@BASS_S_B_Oxygen, target.oxygen_margin)
T = 查曲线(@BASS_S_B_Tradeoff, target.cover_prey_tradeoff)
返回 空间权重(C × O × T)
```

本例结果：
```json
{
  "case": "BASS-S",
  "binding": "BASS_S_B",
  "template": "S_SUMMER",
  "intermediate": {
    "Cooling": 0.8,
    "Oxygen": 0.75,
    "Tradeoff": 0.6
  },
  "result": 0.36000000000000004
}
```

**BASS_S_R**
```text
表达 BASS_S_R 用于 LargemouthBass.SummerStress / RESPONSE
模板 R_FEED_REACTION（固定结构，仅展开便于阅读）
配置：
  Match = @BASS_S_R_Match
  Presentation = @BASS_S_R_Presentation
  Salience = @BASS_S_R_Salience
  Pursuit = @BASS_S_R_Pursuit
执行：
F = 查曲线(@BASS_S_R_Match, response.feeding_match) × 查曲线(@BASS_S_R_Presentation, response.presentation_fit)
R = 查曲线(@BASS_S_R_Salience, response.trigger_salience) × 查曲线(@BASS_S_R_Pursuit, response.sustained_pursuit_demand)
返回 响应强度(MAX(F, R))
// 两通道均评价；强短刺激与持续高速追逐是两个独立输入。
```

本例结果：
```json
{
  "case": "BASS-S",
  "binding": "BASS_S_R",
  "template": "R_FEED_REACTION",
  "intermediate": {
    "Match": 0.28,
    "Presentation": 0.75,
    "Salience": 0.63,
    "Pursuit": 0.91,
    "Feeding": 0.20999999999999996,
    "Reaction": 0.5733
  },
  "result": 0.5733
}
```

**BASS_S_Q**
```text
表达 BASS_S_Q 用于 LargemouthBass.SummerStress / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "BASS-S",
  "binding": "BASS_S_Q",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 50,
      "Medium": 35,
      "Large": 18.0,
      "Rare": 3.5999999999999996
    }
  },
  "result": {
    "Small": 0.46904315196998125,
    "Medium": 0.3283302063789869,
    "Large": 0.16885553470919326,
    "Rare": 0.03377110694183865
  }
}
```

### G1｜Group 条件：日期 AND 温度 AND 巢区

复用同一 guard_all 条件树；不复制 Owner 决策。

样本涉及 5 张作者表、13 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "slow.day_of_year": 120,
  "slow.recent5day_temp_c": 18,
  "slow.scene_structures": [
    "nest_cover"
  ],
  "slow.cold_severity": 0.5,
  "slow.oxythermal_compression": 0.25,
  "slow.pelagic_forage_state": true,
  "slow.open_water_forage_availability": 0.5
}
```

**G1**
```text
表达 G1 用于 G1_GuardNormal / GROUP
模板 G_SHARES（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
读取 同一份 slow_snapshot
Guarding = 若 (slow.day_of_year BETWEEN @guard_dates_value AND slow.recent5day_temp_c GE @guard_temp_value AND slow.scene_structures CONTAINS_ANY @guard_nest_value) 则 @BassGuardShare 否则 0
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。
```

本例结果：
```json
{
  "case": "G1",
  "binding": "G1",
  "template": "G_SHARES",
  "intermediate": {
    "guard_all": true
  },
  "result": {
    "Guarding": 0.2,
    "Normal": 0.8
  }
}
```

### G2｜Group 同快照回退：不满足巢区

Guard share=0；Normal=1。回退是剩余份额，不是 Defense vs Feeding fallback。

样本涉及 5 张作者表、13 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "slow.day_of_year": 120,
  "slow.recent5day_temp_c": 18,
  "slow.scene_structures": [
    "open_water"
  ],
  "slow.cold_severity": 0.5,
  "slow.oxythermal_compression": 0.25,
  "slow.pelagic_forage_state": true,
  "slow.open_water_forage_availability": 0.5
}
```

**G2**
```text
表达 G2 用于 G2_GuardNormal / GROUP
模板 G_SHARES（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
读取 同一份 slow_snapshot
Guarding = 若 (slow.day_of_year BETWEEN @guard_dates_value AND slow.recent5day_temp_c GE @guard_temp_value AND slow.scene_structures CONTAINS_ANY @guard_nest_value) 则 @BassGuardShare 否则 0
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。
```

本例结果：
```json
{
  "case": "G2",
  "binding": "G2",
  "template": "G_SHARES",
  "intermediate": {
    "guard_all": false
  },
  "result": {
    "Guarding": 0,
    "Normal": 1
  }
}
```

### G3｜合成压力样本：(春 AND 温) OR (秋 AND 凉)

用于把嵌套条件的实际存法填出来，不升级为已被鱼类证据确认的深层 Group breaker。

样本涉及 5 张作者表、20 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "slow.day_of_year": 270,
  "slow.recent5day_temp_c": 15
}
```

**G3**
```text
表达 G3 用于 SyntheticSeasonGroup / GROUP
模板 G_SHARES（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
读取 同一份 slow_snapshot
Seasonal = 若 ((slow.day_of_year BETWEEN @g3_spring_date_value AND slow.recent5day_temp_c GE @g3_warm_value) OR (slow.day_of_year BETWEEN @g3_fall_date_value AND slow.recent5day_temp_c LE @g3_cool_value)) 则 @G3Share 否则 0
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。
```

本例结果：
```json
{
  "case": "G3",
  "binding": "G3",
  "template": "G_SHARES",
  "intermediate": {
    "g3_either": true
  },
  "result": {
    "Seasonal": 0.25,
    "Normal": 0.75
  }
}
```

### Q1｜品质并列修正 Q1

大钩且大饵：Large×1.5、Rare×1.2。

样本涉及 6 张作者表、29 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "active",
  "quality_context.water_temp_c": 20
}
```

**Q1**
```text
表达 Q1 用于 IllustrativeQuality / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "Q1",
  "binding": "Q1",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare"
    ],
    "raw": {
      "Small": 50,
      "Medium": 30,
      "Large": 22.5,
      "Rare": 6.0
    }
  },
  "result": {
    "Small": 0.4608294930875576,
    "Medium": 0.2764976958525346,
    "Large": 0.2073732718894009,
    "Rare": 0.055299539170506916
  }
}
```

### Q2｜品质并列修正 Q2

低活性：Small/Medium×1.2，Large/Rare×0.7。桶与成体关系只是演示映射，不声称小=幼体、大=成体的生物同一性。

样本涉及 6 张作者表、29 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "gear.hook_size_index": 1,
  "gear.bait_size_cm": 3,
  "quality_context.time_band": "inactive",
  "quality_context.water_temp_c": 20
}
```

**Q2**
```text
表达 Q2 用于 IllustrativeQuality / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "Q2",
  "binding": "Q2",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "LowActivity/Small",
      "LowActivity/Medium",
      "LowActivity/Large",
      "LowActivity/Rare"
    ],
    "raw": {
      "Small": 60.0,
      "Medium": 36.0,
      "Large": 10.5,
      "Rare": 3.5
    }
  },
  "result": {
    "Small": 0.5454545454545454,
    "Medium": 0.32727272727272727,
    "Large": 0.09545454545454546,
    "Rare": 0.031818181818181815
  }
}
```

### Q3｜品质并列修正 Q3

BigGear 与 ColdNight 同时命中。后者只读原始水温/时段，不读前者改完的分布。

样本涉及 6 张作者表、29 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "gear.hook_size_index": 3,
  "gear.bait_size_cm": 10,
  "quality_context.time_band": "night",
  "quality_context.water_temp_c": 6
}
```

**Q3**
```text
表达 Q3 用于 IllustrativeQuality / QUALITY
模板 Q_PARALLEL（固定结构，仅展开便于阅读）
配置：
  无 Profile Slot；使用下列具名规则与共享数值表
执行：
Base = 当前 Group 的 QualityWeight
并列修正 BigGear/Large：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Large 乘 1.5
并列修正 BigGear/Rare：若 (gear.hook_size_index GE @q_hook_value AND gear.bait_size_cm GE @q_bait_value)，则 Rare 乘 1.2
并列修正 LowActivity/Small：若 quality_context.time_band IN @q_inactive_value，则 Small 乘 1.2
并列修正 LowActivity/Medium：若 quality_context.time_band IN @q_inactive_value，则 Medium 乘 1.2
并列修正 LowActivity/Large：若 quality_context.time_band IN @q_inactive_value，则 Large 乘 0.7
并列修正 LowActivity/Rare：若 quality_context.time_band IN @q_inactive_value，则 Rare 乘 0.7
并列修正 ColdNight/Large：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Large 乘 0.8
并列修正 ColdNight/Rare：若 (quality_context.water_temp_c LE @q_cold_value AND quality_context.time_band IN @q_night_value)，则 Rare 乘 0.8
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。
```

本例结果：
```json
{
  "case": "Q3",
  "binding": "Q3",
  "template": "Q_PARALLEL",
  "intermediate": {
    "hits": [
      "BigGear/Large",
      "BigGear/Rare",
      "ColdNight/Large",
      "ColdNight/Rare"
    ],
    "raw": {
      "Small": 50,
      "Medium": 30,
      "Large": 18.0,
      "Rare": 4.800000000000001
    }
  },
  "result": {
    "Small": 0.48638132295719844,
    "Medium": 0.2918287937743191,
    "Large": 0.17509727626459146,
    "Rare": 0.04669260700389106
  }
}
```

## 6. 身份、失败边界与最小生产桥接

这份交付的程序只用于复算纸面样本，不接入游戏，也没有实现一个新的 FCF Runtime。生产需要的桥接是：现有 Resolver 提供只读事实 → 表格加载器/受限 DSL 前端做相同类型与引用校验 → 同一评价语义 → 现有 Typed Result。每个例子的输入和数值输出可作为两种前端的共同验收样本。

身份 Worked Example：现有 Session S_demo 的 Active Channel 是 lure_A；一个已准入 Pause 对应 Root R_demo，系统已分配 Opportunity O_demo。packet 1 和 packet 2 引用同一 R_demo，即同一个 O_demo；外部现有 resolution owner 对该 Root 只结算一次。R_FIELD 仅消费传入 Scope，读同一 lure_A 的 FeedingMatch 与 FoodField。切换一个 frame 或重发 packet 不创建新 O、不重新抽签；新的被准入语义颗粒才由原 Owner 提供新身份。Static Bottom/Float 的一个合法静止姿态颗粒同理。本文不规定新 ID 拼接法、计时器、Reservation 或 Session 写回，不证明生产的幂等实现已经通过测试。

Gate 拒绝是有效类型结果0；输入缺失/非法表引用是 ValidationError；C14/C15 是范围外，不运行、更不伪造0。质量总和0、负权重、重复优先级、Predicate 环、非法 Slot 均是配置错误。表格与 DSL 同样不得写 Actor/World/FishGroup 状态，不得生成 RNG；Response 输出由既有下游消费，不创建 Follow/Attack 行为。播放器反馈可沿当前 trace 暴露“哪项条件失败/哪条 Channel 贡献最大”，但玩家是否看到这些诊断由产品层决定，本稿不添加新玩家按钮。

## 7. 用同一修改任务核对成本

这些是实际样本的编辑定位，不是测得的工时。共享 Parameter 修改会影响所有引用，Clone Profile 则必须改具名引用；两种表达都应显示受影响绑定。

| 修改 | 配置 A 的实际位置 | 中文脚本 B 的实际位置 | 语义约束 |
| --- | --- | --- | --- |
| C06 入侵0.5对应0.6改为0.65 | CurvePoint(profile=C06_R_Defense,x=0.5).y 一格 | 同一共享 CurvePoint 一格；脚本不变 | 调 Profile，不加 Feeding |
| C03 漂流阈值0.6改为0.7 | Parameter C03_drift_value.value 一格 | 同一 Parameter 一格；脚本不变 | 不改 FIRST_MATCH 顺序 |
| C03 高响应再加一个 AND 条件 | 新 Parameter + ATOM + PredicateMember，共3行 | 新 Parameter 1行 + 高响应条件表达式加一项 | 只能读白名单输入；不能凭添加字段假定上游已提供 |
| C08 两通道输入相同，将 MAX 换成平均 | 改 R_DUAL_FIXED 模板聚合步骤1行及实现/验证 | 改固定聚合语句及实现/验证 | 属候选聚合设计变更；不能假装 Profile 参数能改拓扑 |
| Q1 大装备 Large乘数1.5改1.6 | QualityModifier(Q1,BigGear,Large).multiplier 一格 | Q1 对应并列修正语句1处 | 不改其它桶、不读取中间分布 |
| C05 关闭低光 Slot | Slot(C05_B,Light) enabled=false 且 ref_id=N/A，同一行2格 | 配置 Light=关闭；固定分支仍留在模板 | 不交换 Runtime Order |
| 鲈鱼夏季目标氧门提前返回 | 本例已有 S_SUMMER step1；不能挪到归一化/Overlay之后 | 已有首条“若氧<阈值返回0” | 真正顺序意义来自提前返回和后续步骤的执行边界 |

算法差异与排版差异：C01 的 T×S×D 因子独立，调换计算次序仍同结果，不把印刷顺序冒充 L 增长证据；S_SUMMER 的 Gate 先失败即返回，后续适宜性不应执行。Cold 和 Summer 的因果链不同，即使一份通用脚本都能写出来，也不能据此宣称它们自动是同一固定模板。

## 8. 样本目录与设计统计的边界

本稿的固定模板名是可运行演示目录，不是重新裁决 L_final。按四个 Surface 分开计数并排除 C13 情景与 G3 合成例，样本使用：Group=1、Bake=4、Response=7、Quality=1。这些是 `N_fixture_templates`，不能改写成 `L_confirmed`：C01/C02/C05 的生产 Spatial Runtime Order 尚未定，C08 的结构已定但具体聚合待标定，Cold/Summer 的 MAX 和 ColdFront BLEND 也仍是 Working Candidate。没有把 C08/C09–C12 的过期结构未决重新打开。

共用关系已在 Binding 行上落实：C01/C02/C05/鲈鱼Normal/Guard 共享 S_FIXED（不同 Profile 与开关）；C03/C04 共享 R_BANDS；C06/C07/鲈鱼Guard 共享 R_DEFENSE；C09–C11 共享 R_FIELD；C12 Normal/鲈鱼Normal/Forage 共享 R_FEED；鲈鱼Cold/Summer 共享 R_FEED_REACTION；各群 Quality 共享 Q_PARALLEL、只换基准与修正；所有 Group 样例共享 G_SHARES。

PT3 未因双 Profile 或上游 Lifecycle 分群成为 REQUIRED；PT4 未因 Guard 产生 Defense vs Feeding precedence 压力。FIRST_MATCH 响应分档的行 priority 是模板内部既定比较语义，不是新买 PT4。C13 仍按范围解决，不制造特殊 Template。本稿完成具体表达，不替 Owner 做最终 DSL/Config 选型、生产参数冻结或全项目 closure。

## 9. 本次复算

静态引用/槽位/Predicate 无环/数值范围校验，加上独立手算预期值对照。中文文本是同一模板的展开显示，尚无独立 DSL 解析器，所以这些复算证明的是样本表及展示计算的一致性，不能声称两套生产编译器已经语义等价。

| check | actual | expected | status |
| --- | --- | --- | --- |
| C01_B | 0.8 | 0.8 | PASS |
| C02_B | 0.7 | 0.7 | PASS |
| C03_R | 0.8 | 0.8 | PASS |
| C04_R | 0.8 | 0.8 | PASS |
| C05_B | 0.8 | 0.8 | PASS |
| C06_R | 0.6 | 0.6 | PASS |
| C07_R | 0.7 | 0.7 | PASS |
| C08_R | 0.6 | 0.6 | PASS |
| C09_R | 0 | 0 | PASS |
| C10_R | 0.15 | 0.15 | PASS |
| C11_R | 0.24 | 0.24 | PASS |
| C12_N | 0.6 | 0.6 | PASS |
| C12_M | 0.328 | 0.328 | PASS |
| C13_J | 0.48 | 0.48 | PASS |
| C13_O | 0.6 | 0.6 | PASS |
| C13_S | 0 | 0 | PASS |
| BASS_N_B | 0.85 | 0.85 | PASS |
| BASS_G_B | 0.8 | 0.8 | PASS |
| BASS_C_B | 0.54 | 0.54 | PASS |
| BASS_S_B | 0.36 | 0.36 | PASS |
| BASS_F_B | 0.75 | 0.75 | PASS |
| BASS_C_R | 0.6552 | 0.6552 | PASS |
| BASS_S_R | 0.5733 | 0.5733 | PASS |
| 五群同快照剩余份额 | {"Guarding":0.2,"ColdSlow":0.15,"SummerStress":0.1,"ForageChase":0.1,"Normal":0.45000000000000007} | {"Guarding":0.2,"ColdSlow":0.15,"SummerStress":0.1,"ForageChase":0.1,"Normal":0.45} | PASS |
| Q1 | {"Small":0.4608294930875576,"Medium":0.2764976958525346,"Large":0.2073732718894009,"Rare":0.055299539170506916} | {"Small":0.4608294930875576,"Medium":0.2764976958525346,"Large":0.2073732718894009,"Rare":0.055299539170506916} | PASS |
| Q2 | {"Small":0.5454545454545454,"Medium":0.32727272727272727,"Large":0.09545454545454546,"Rare":0.031818181818181815} | {"Small":0.5454545454545454,"Medium":0.32727272727272727,"Large":0.09545454545454546,"Rare":0.031818181818181815} | PASS |
| Q3 | {"Small":0.48638132295719844,"Medium":0.2918287937743191,"Large":0.17509727626459146,"Rare":0.04669260700389106} | {"Small":0.48638132295719844,"Medium":0.2918287937743191,"Large":0.17509727626459146,"Rare":0.04669260700389105} | PASS |
| Q3 交换 Modifier 行仍等义 | {"Small":0.48638132295719844,"Medium":0.2918287937743191,"Large":0.17509727626459146,"Rare":0.04669260700389106} | {"Small":0.48638132295719844,"Medium":0.2918287937743191,"Large":0.17509727626459146,"Rare":0.04669260700389106} | PASS |
| Q3 反转 Modifier 后 | {"Small":0.48638132295719844,"Medium":0.2918287937743191,"Large":0.17509727626459146,"Rare":0.04669260700389105} | {"Small":0.48638132295719844,"Medium":0.2918287937743191,"Large":0.17509727626459146,"Rare":0.04669260700389106} | PASS |
| 夏季硬 Gate 零 | 0 | 0 | PASS |
| Forage Gate 不被 Overlay 复活 | 0 | 0 | PASS |
| 低 salience 仍计算另一 Channel | 0.9 | 0.9 | PASS |
| 双阈值无命中使用 default | 0 | 0 | PASS |
| 缺失必需输入拒绝 | KeyError (specimen ValidationError boundary) | error | PASS |
| Group Share 超1拒绝 | ShareOverflow | error | PASS |
| 27个案例ID唯一 | 27 | 27 | PASS |
| ColdFront纯开关关闭返回Base | 0.8 | 0.8 | PASS |
| 未执行通道不伪造0值Trace | absent | absent | PASS |
