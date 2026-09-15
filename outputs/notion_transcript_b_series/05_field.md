# P03 沄食系+品系 L1｜24 种

**Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED**

## 批次概览

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 5 批：P03 沄食/浮游场系 + 品系 L1 等效层；含 grazing 批 REV-001 B1 撤回件 giant_barb 重建） |
| 样本口径 | 24 文件＝P03 主批 12（四面完整表达）+ 品系 L1 等效层 12（短形：四面声明+本体指针+Profile 重绑定清单，不展开伪脚本——R10 品系行判例）。主批名单四层锚：Tier A×2（鳙鱼 canonical source / 大西洋鲱）+ B+×6 + Tier B×4 |
| 基线 | SNAPSHOT_ONLY（Story DB P03 逐行名单不在本地；Semantic Review Context §10 Field Channel OPEN 仅经 census registry 引文承载） |
| Response 统一口径 | FieldFeeding 通道＝R-T1 Feeding 通道的 Field 型（Channel=Feeding，evaluand 换为食物场浓度——live §13.3 Forage-Coupled Feeding 读法先例）——不是新通道、不 promote Grammar |
| 表达读数 | Group：12/12 无路由显式声明（HER=库内首个 GroupPressure=Strong/Group-only verdict 登记但 census 层无 routing body 证据——语义层判定与 census 正交）——L_group 无增长。Bake：12/12 落 census SINGLE 族 factor_type 轴 food_field 场实例投影 BA-P03-FIELD-SINGLE——场实例三型：plankton 场 ×9 / resource patch 场 ×1（giant_barb 重建）/ 饵鱼场 ×1（piraiba）——census 侧 ΔL_bake=0。Response：12/12＝R-T1 单通道（Channel=FieldFeeding；零 R-T2）；intake_semantics 参数轴实例：持续滤食 ×10 + 脉冲摄入 ×2——L_response 无增长。Quality：全部 QT-1。新列结构：零；**品系 L1-EQUIV 短形＝本批新表达层形态** |
| 数值状态 | 全部 @参数引用；Bake 程序无 combine 步（族域）；intake_semantics 与 field_type 均为 FOOD_FIELD 族已声明参数轴实例，非新结构 |
| 验证结果 | validate_field.py：selftest 33 用例 PASS；真实交付包 24 文件 0 违规 PASS（工件缺陷 2 类：品系文件中性 Profile 误写 @token ×12 文件批量修复、双批文件标题可读性 ×5——均修复工件） |
| 跨批登记 | Field 通道两层 reconciliation OPEN（FOOD_FIELD 族 New Candidate / HRQ-B2-01 / TAR-09 全程可见）；rohu 场化复核线（grazing 批 M2 联动→转 Coordinator）；双批分工面互指（欧白鲑/红鲑/灰西鲱/美洲西鲱 P05↔P03）；无 UPSTREAM_CHANGE_EVENT |
| 审核 | **REP-FULL-FIELD-REV-001 verdict: ARTIFACT_APPROVE**（3 minor 均文本级已修；giant_barb 重建三步全过；品系 L1-EQUIV 合理；R-T1 Field 型双 live 锚支撑） |

## Species 汇总表

### 表 A｜census Tier A 组（2 文件）——BA-P03-FIELD-SINGLE + R-T1 FieldFeeding

| # | 文件 | 鱼（学名） | Story | 证据档 | 场实例 / 参数轴 |
|---|---|---|---|---|---|
| 1 | bighead_carp.md | 鳙鱼（Hypophthalmichthys nobilis） | FISH-R02-S09（census B2）——FOOD_FIELD 族 canonical source，本批 Tier A 样板 | A | plankton 场 / 持续滤食 |
| 2 | atlantic_herring.md | 大西洋鲱（Clupea harengus） | FISH-R02-S02（census B2）——族第 2 成员；库内首个 GroupPressure=Strong/Group-only verdict 登记 | A | plankton 场（群游集聚值域承载） / 持续滤食 |

### 表 B｜同批点名+复核线兑现+CSV 锚组（10 文件）

| # | 文件 | 鱼（学名） | Story | 证据档 | 特殊登记 |
|---|---|---|---|---|---|
| 3 | silver_carp.md | 鲢鱼（H. molitrix） | FISH-R02-S07——census「同型对照不建体」判语在案 | B+ | BHC 骨架参数差异化（浮游植物主向）；行级 Pattern [需核对] |
| 4 | vendace_field.md | 欧白鲑 P03 面 | migration 批复核线兑现 | B+ | 双批分工（P05/P03 互指） |
| 5 | sockeye_field.md | 红鲑 P03 面 | migration 批复核线兑现 [需正文] | B | 双批分工；停食判例族不默认继承 |
| 6 | american_shad_field.md | 美洲西鲱 P03 面 | FISH-R06 摄食期面（停食面归 migration 批双 Path） | B+ | 双批分工；CSV 矛盾 |
| 7 | alewife_field.md | 灰西鲱 P03 面 | FISH-R06 [需正文] | B | 双批分工；CSV 矛盾 |
| 8 | capelin.md | 毛鳞鱼（Mallotus villosus） | handoff 点名；K4 排除=繁殖面口径（澄清） | B | CSV 滤食锚；产卵面归后续批 |
| 9 | lake_whitefish_field.md | 湖白鲑 P03 面 | migration 批登记项 4 兑现 | B | CSV 滤食锚；通名系种级区分 |
| 10 | jack_mackerel.md | 日本竹荚鱼（Trachurus japonicus） | CSV 滤食锚行 [需正文] | B | 混合食性张力登记 |
| 11 | giant_barb.md | 暹罗巨鲤（重建） | FISH-R05——live 行级实测：ResponseChannels=[FieldFeeding]、PrimaryEvaluand=[Resource Patch]、P05+P06 双 relation | B+ | REV-001 B1 撤回件重建：resource patch 场化 |
| 12 | piraiba.md | 短扁口鲶（Brachyplatystoma filamentosum） | FISH-R10 收官批成员（handoff 点名）[需正文] | B+ | 饵鱼场 / 脉冲摄入 |

### 表 D｜品系 L1 等效层（12 文件）——L1-EQUIV 短形

| # | 文件 | 品系（学名） | 本体 | 本体四面状态 |
|---|---|---|---|---|
| 13 | koi.md | 锦鲤（Cyprinus rubrofuscus） | 鲤复合体 | 未建（K3/P02 补批登记）；种级行名实注记 |
| 14 | koi_kohaku.md | 红白锦鲤（Var. Kohaku） | 普通鲤鱼 | 未建 |
| 15 | koi_shiro_utsuri.md | 四白锦鲤（Var. Shiro Utsuri） | 普通鲤鱼 | 未建 |
| 16 | koi_goromo.md | 圆点五色锦鲤（Var. Goromo） | 普通鲤鱼 | 未建 |
| 17 | koi_ogon.md | 橙黄金锦鲤（Var. Ogon） | 普通鲤鱼 | 未建 |
| 18 | albino_grass_carp.md | 白化草鱼（Var. Albino） | 草鱼 | 未建（P02 批登记——已由 patch 批 grass_carp.md 兑现） |
| 19 | albino_white_sturgeon.md | 白化高首鲟 | 高首鲟 | 已建（migration 批）——重绑定即刻生效 |
| 20 | albino_channel_catfish.md | 白化叉尾鮰 | 斑点叉尾鮰 | 已建（normal 批）——重绑定即刻生效 |
| 21 | albino_mirror_carp.md | 镜鲤（白化） | 普通鲤鱼 | 未建 |
| 22 | leather_carp.md | 无鳞鲤（Var. Nudus） | 普通鲤鱼 | 未建 |
| 23 | human_face_carp.md | 鳞鲤（人面鲤） | 普通鲤鱼 | 未建 |
| 24 | albino_scale_carp.md | 鳞鲤（白化） | 普通鲤鱼 | 未建 |

排除项要点：红鲑等 P05 面（migration 批）；rohu（grazing 批资产不重写）；鸭嘴鲟 P03 面（候选池）；大西洋鲭/鲻鱼（弱锚/归属未对账）；荷包红鲤/镜鲤本体品系行（候选池）；大口水牛鱼/桨鱼（15-Case 密封包）。

## 完整示例（Tier A 样板：bighead_carp.md 全文）

> FOOD_FIELD_FEEDING_RESPONSE 族 canonical source——展示「场事实→场评估器→场适应性」的 Bake 场链与 FieldFeeding 通道。

# 鳙鱼（Bighead Carp｜Hypophthalmichthys nobilis）｜滤食浮游场系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（P03 沄食/浮游场系＝第 5 批：滤食/食物场组） |
| Story | FISH-R02-S09｜鳙鱼｜滤食浮游场与水层机会（census CENSUS-B2 全四面判定快照 + 盲程序体冻结在案） |
| 冻结 Pattern | P03（census B2 stories.jsonl 快照） |
| 物种属性锚 | fish-reference-20260908：benthopelagic、早晨活跃、杂食性名义行、potamodromous、营养级 2.83（CSV 食性列与滤食语义口径差以 census 快照为准） |
| 基线 | SNAPSHOT_ONLY（live 转录 2026-09-10 版；census registry v4 快照） |
| 证据档 | Tier A（census B2 全四面判定快照——FOOD_FIELD_FEEDING_RESPONSE 族 canonical source） |
| 变体声明 | 无路由条件原子（显式声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（FieldFeeding——R-T1 Feeding 通道的 Field 型；Reaction 槽 OFF） |
| census 程序 | P-B2-BHC-BAKE（SINGLE 族 factor_type 轴 +food_field 场实例）+ P-B2-BHC-RESP-FIELD（FOOD_FIELD_FEEDING_RESPONSE canonical source） |
| 亚结构组 | 滤食型——本组 Tier A 样板 |

## 0. 上游语义与食物场形态

- 食物场形态：滤食浮游场（场 evaluand——分布式浓度场：浮游动物/浮游植物/悬浮颗粒浓度，水柱分布；census incoming premise 原样）。滤食与钩饵响应并非同一现实机制（Story 明言——census 判语原样）。
- Bake 面：食物场浓度单链（EVAL_FOOD_FIELD_CONCENTRATION → NORMALIZE_WEIGHT；SINGLE 族 food_field 轴——场实例第 2/3 例继 B1 七鳃鳗 chemical_gradient）。高生产力水层定位＝场评估的自然输出。
- Response 面：FOOD_FIELD_FEEDING_RESPONSE 族 canonical source（evaluand=食物场浓度非离散目标 + RETURN=FieldFeeding；与 TYPED 通道轴不可互吞——B1-LAM 判例同型）。产品捕获方式＝Product Scope TAR-09 Open。
- Group 面：census NO_SURFACE_EFFECT（FishMode Weak）。Quality 面：census NO_SURFACE_EFFECT。
- 表达超集说明：无。

Profile 引用清单：@BhcPlanktonFieldEvaluatorProfile @BhcPlanktonPreyFields @BhcDietClasses @BhcSizeWindow @BhcFieldIntakeProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 退化形：空 Special 集 + 默认路由；census Group 面 NO_SURFACE_EFFECT（FishMode Weak）原样）。

### 1.2 分群结果（5 列固定）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Bhc_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

Share 语义：live §7 契约（Species 基础供给权重的无量纲分配比例）。

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族 food_field 场投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例；2 步场评估→归一化；本组 Tier A 样板文件） |
| FieldType(typed) | food_field：plankton 场（场 evaluand——浮游动物/浮游植物/悬浮颗粒浓度场，水柱分布；census P-B2-BHC-BAKE 实例常量） |
| FieldEvaluatorProfile | @BhcPlanktonFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@BhcPlanktonPreyFields——契约 FILTERED_SUM 聚合与原始事实族口径直接复用；diet_classes=@BhcDietClasses；size_window=@BhcSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed food-field factor（B-T1 单因子退化形；场耦合 live 参照读法=§10 BA-T5 Forage Field Coupling 句型——两层 reconciliation OPEN） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的食物场事实（浮游浓度场——水柱分布的浓度事实）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@BhcPlanktonPreyFields 绑定的 plankton prey class 生物量，
      经 diet_classes=@BhcDietClasses 食性过滤
      与 size_window=@BhcSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_FOOD_FIELD_CONCENTRATION：
    用食物场浓度事实查询 @BhcPlanktonFieldEvaluatorProfile
    得到 FieldSuitability（场适应性——场浓度评估，非离散 patch、非结构因子）

NORMALIZE_WEIGHT：
    对 FieldSuitability 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单场因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，typed context 属 PATCH 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN；场耦合句型的 live 参照＝BA-T5（ForageSchoolIntensity 类场事实——live 侧尚未按 plankton 场实例化，本文件不冒充句型晋升）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=FieldFeeding；census FOOD_FIELD_FEEDING_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） | @BhcFieldIntakeProfile | 返回 FieldFeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前食物场事实（浮游浓度场——上游 premise/Bake 供给的事实，非离散钩饵目标）

EVAL_FOOD_FIELD_INTAKE：
    用食物场浓度评价 @BhcFieldIntakeProfile
    （场摄入评估——持续滤食摄入语义；
      intake_semantics=持续滤食——FOOD_FIELD_FEEDING_RESPONSE 族参数轴实例）
    得到 FieldIntakeEvaluation

DECIDE_FIELD_FEEDING：
    按 FieldIntakeEvaluation 决定场摄食响应档位

返回 Response(FieldFeeding)

Reaction 槽 OFF
（evaluand=食物场非离散目标——与 TYPED 族通道轴不可互吞（B1-LAM 判例同型）；
 离散钩饵捕获通道属产品捕获方式 Product Scope——TAR-09 Open，本文件不表达）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile）；census Quality 面 NO_SURFACE_EFFECT |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（恒为 NormalFeeding——无 Special Group）

对每个品质：
    读取该品质的 GroupEligibilityFactor（查 @NeutralEligibility）
    读取该品质的 GroupAffinityFactor（查 @NeutralAffinity）
    读取当前 lure / bait / hook / context 等原始事实
    评价所有适用的 Presentation Modifier / Context Modifier（只读原始事实）

    原始品质权重 =
        基础品质权重
        × GroupEligibilityFactor
        × GroupAffinityFactor
        × 所有适用 Modifier

汇总所有品质的原始权重

如果总权重 > 0：
    统一归一化
    输出 QualityWeightVector
否则：
    当前 FishQuality × FishGroup 不产生可实现候选
```

## 5. 自由度、边界与放弃项

- 使用的自由度：census SINGLE 族 food_field 轴投影标签与场实例语义（plankton 场）；FOOD_FIELD_FEEDING_RESPONSE 族投影（canonical source）；intake_semantics 参数轴取值（持续滤食）；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：(1) 离散钩饵捕获通道表达（产品捕获方式 TAR-09 Open——不预购买）；(2) 合并算子（单场因子链无 combine 步；OPERATOR UNDEFINED）；(3) 鱼群供给路由（census 判 NO_SURFACE_EFFECT，handoff 候选行级 [需核对]）；(4) 数值与 Profile 值域不冻结。
- 同型对照：鲢鱼 R02-S07 同型（census「同型对照不建体」）——silver_carp.md 按本骨架参数差异化。

BATCH_ID: REP-FULL-FIELD-001

（示例完）

## Provenance

- 本地路径：`A:\Projs\FCF-Harness-Handoff\programaticHitFish\outputs\full_authoring\field\`（README.md + validate_field.py + species\ 24 文件）
- GitHub：https://github.com/futouyiba/programaticHitFish （commit `ebc4ba7`，工作树干净）
- 审核 verdict：REP-FULL-FIELD-REV-001 = **ARTIFACT_APPROVE**。转录批次：2026-09-11
