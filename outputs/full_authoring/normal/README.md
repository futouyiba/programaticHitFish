# P01 普通离散目标摄食系四面生产级表达交付包（第一轮）｜REP-FULL-NORM-001

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 批次 | REP-FULL-NORM-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 4 批：P01 普通层——全库最大 Pattern 群；**第一轮 60 文件，允许拆两轮交付**，本 README 即第一轮交付） |
| 输入 | (1) 基准样板＝live Stress Test R1 主页转录 `programaticHitFish/tmp/live_stress_main_after.md`（2026-09-10 版：§13.3 R-T1/R-T2 结构族 + §17 RR-T1 Reaction 槽与 MAX 汇总 + §11.5 低光/夜摄食判例（MERGE_SUPPORTED → BA-T1 + DynamicSpatialSlot，BakeTemplate +0）+ §12 Quality 样板 + §13.1 G-T1/§13.2 B-T1 结构族）(2) 前三批判式与标准＝guarding / grazing / migration 三批交付包（REP-FULL-GUARD/GRAZE/MIGRA-001）(3) census registry v4＝`fish_logic_census/template_registry.yaml`（SINGLE 15 成员 / PLAIN 5 成员 / TYPED_TARGET_RESPONSE 27+ 成员（P01 对应族）；本批投影族＝SINGLE/PLAIN 两族 + BOUNDARY-DECL 表达层形态）(4) census 归档 `fish_logic_census/batches/CENSUS-B0/B1/B2`（本批消费 P01-labeled Story 快照全文 9 条：FGA/MDF/PIK/GAR/BLU(已承载)/RAI/BRT12/PAD34/PAD35 + OSC/CHB(已承载)）(5) cue 轴资产 `outputs/cue_axis_r1/`（@ElectroFieldProfile/@ScentCueProfile——K8 轴并入）(6) `outputs/usable_forage_contract_r0/`（UsableForageAvailability 契约——Bake 输入描述复用）(7) R05–R10 批次摘要（outputs/batches/FISH-R05*.md … FISH-R10*.md：R07 被动电感知双例（角鲨+鳐）/R07 Capture Boundary 成轴/R08 虎纹 Identity-Deferred+P01/R10 镖鲈科首例）(8) fish-reference-20260908.csv（267 鱼物种身份/习性方向锚——**本批 Tier B 名单构造的机械输入**）(9) guarding 批 marble_goby.md 退回档（笋壳鱼 P01 面预告落点+SRCHECK 引文固化记录） |
| 基线 | **SNAPSHOT_ONLY**——Notion MCP 工具在本执行环境不可用（Story DB live 未访问），全部输入为本地归档/转录/快照；**Story DB 主 relation=P01 的逐行名单不在本地**——本批名单构造方法见 §1 名单声明；live 漂移时以本 README 引用的归档版为准 |
| 交付物 | `species/*.md` 60 文件（每鱼四面：Group Routing 无路由显式声明 + Bake 配置/伪脚本 + Response 配置/伪脚本（R-T2 载体双通道展开）+ Quality 绑定/伪脚本）+ 本 README + `validate_normal.py` 结构校验器；**六文件组**（§1 表 A–F）：捕获边界 2 / 伏击 16 / 追击 16 / 夜行 10 / 机会 13 / 特殊感官 3——同目录平铺，README 分组承载 |
| 数值状态 | 全部阈值/窗口/猎物构成/Profile 值域为 **@参数引用**（生产数值由 Profile 层定值，不冻结）；PLAIN 族 CombineRule 拓扑族固定、数学 **OPERATOR UNDEFINED** 待机制侧；R-T2 MAX 汇总数学同款 UNDEFINED；夜行组低光槽=§11.5 判例形态（非作者可选算子） |

## 1. 样本口径（60 文件 / 约 60 Story 位）

P01＝Discrete Target→TargetFeeding（census registry semantic_pattern_correspondence：TYPED_TARGET_RESPONSE 族对应 P01，Frozen Input）。本批为 handoff 指定的最大群批次（估计剩余 120-150 条 Story），按亚结构分文件组、允许拆两轮——**本交付为第一轮（60 文件）**。

### 名单声明（本批最重要的诚实边界）

本地无 Story DB P01 逐行名单（Story DB live 不可访问；tmp/triage_r05 的 Pattern 关系表已散佚——仅 guarding 批工件固化其残段）。第一轮名单由三层锚构造，**分组规则可机械复验（CSV 逐行回放已通过独立审 REV-001 校验），但组内选择步含未声明判据（配额平衡/身份置信/同科样板相邻等）**——满足分组规则却排在已取行之前的合格跳行实例见排除表末尾「NORM-REV-001 F1 跳行记录」段（花骨鱼/大西洋鳕鱼/欧洲巨鲶/玻璃梭鲈/公牛鲨/江鳕/牛头鲦/白亚口鱼/黄金鲫/鲢鱼等约 17 行）。第二轮名单需 Story DB P01 导出或点名，不应以本批构造法冒充全覆盖。（REV-001 F1 修正）

1. **Tier A（census 快照全文在案）×8 文件**：本地有全四面判定快照的 P01-labeled Story（census B1/B2 stories.jsonl）。
2. **Tier B+（批内互指/摘要点名）×4 文件**：批内互指标定（白斑狗鱼 S18 双源互指；笋壳鱼 P01 面 guarding 批退回档+SRCHECK 引文）+ R07/R08/R10 摘要点名（白斑角鲨/棘背钝头鳐/虎纹狗鱼/彩虹镖鲈）。
3. **Tier B（CSV 方向锚机械分组）×46 文件**：按 fish-reference-20260908.csv 习性列的**机械规则**分组挑选（规则：伏击组＝性格∈{孤僻,躲藏}∧食性=肉食性∧时段≠夜间；追击组＝性格=追猎∧食性=肉食性∧时段≠夜间；夜行组＝时段=夜间活跃∧食性∈{肉食,杂食}；机会组＝性格∈{活泼,温和,撕鳍,好斗,警惕}∧未被前三组收；组内按 CSV 行序取前 N；排除项见排除表）。**该 46 文件名单是表达层构造，不是 Story DB 名单**——每文件行级 Pattern 标签 [需核对]，Story DB 名单到达后增删（§4 登记项 1/2）。

证据档：A＝census 全四面判定快照；B+＝批内互指或摘要点名锚；B＝CSV 方向锚（条件值全 @ 化，行级标签标 [需核对]）。

### 表 A｜捕获边界组（2 文件）——BA-P01-BOUNDARY-DECL（Bake 面无 Story 派生程序显式声明）

| # | 文件 | 鱼（学名） | Story | 证据档 | Response |
|---|---|---|---|---|---|
| 1 | alligator_gar.md | 鳄雀鳝（Atractosteus spatula）；白金火箭行并入 | B01-S07 取饵携行阶段边界（census B1）；携行/吞咽/Hook OUT_OF_SCOPE | A | R-T1 仅初次接受 |
| 2 | northern_pike_strike.md | 白斑狗鱼（Esox lucius）S20 | B01-S20 横咬捕获阶段（census B1）；post-instantiation OUT_OF_SCOPE | A | R-T1 仅初次接受 |

### 表 B｜伏击组（16 文件）——BA-P01-AMBUSH-SINGLE ×15 + BA-P01-PLAIN ×1

| # | 文件 | 鱼（学名） | Story | 证据档 | typed 因子 |
|---|---|---|---|---|---|
| 3 | florida_gar.md | 佛罗里达雀鳝（L. platyrhincus） | R02-S17 植被边缘伏击（census B2）——**组 Tier A 样板** | A | 植被边缘结构 |
| 4 | mandarin_fish.md | 鳜鱼（Siniperca chuatsi） | FISH-R03（census B2；P01+P02，本文件 P01 主面）——**census PLAIN 第 5 成员** | A | 结构+深度(低温绑定) |
| 5 | northern_pike_ambush.md | 白斑狗鱼 S18 | 植被伏击（census PIK 判语+migration 批 §5 双源互指） | B+ | 植被掩体结构 |
| 6 | marble_goby_ambush.md | 笋壳鱼（Oxyeleotris marmorata） | R05 P01 面（guarding 批退回档+SRCHECK 引文固化） | B+ | 洞隙/掩体结构 |
| 7 | rainbow_darter.md | 彩虹镖鲈（Etheostoma caeruleum） | R10「镖鲈科首例」点名（种身份按 CSV 唯一镖鲈科行） | B+ | 底层砾石结构 |
| 8 | yellow_catfish.md | 黄颡鱼（Tachysurus fulvidraco） | CSV 方向锚 | B | 泥底洞隙掩体 |
| 9 | topmouth_culter.md | 翘嘴红鲌（Culter alburnus） | CSV 方向锚（组间张力登记） | B | 明暗交界/掩体边缘 |
| 10 | mongolian_redfin.md | 蒙古红鲌（Chanodichthys mongolicus） | CSV 方向锚（组间张力登记） | B | 明暗交界/掩体边缘 |
| 11 | spotted_mandarin.md | 斑鳜（Siniperca scherzeri） | CSV 方向锚（同属鳜鱼方向） | B | 岩礁/砾石结构 |
| 12 | russian_sturgeon.md | 俄罗斯鲟（Acipenser gueldenstaedtii） | CSV 方向锚 | B | 河底/深槽结构 |
| 13 | spinibarbus.md | 光倒刺鲃（Spinibarbus hollandi） | CSV 方向锚 | B | 急流石隙掩体 |
| 14 | witch_flounder.md | 女巫鲽（Glyptocephalus cynoglossus） | CSV 方向锚 | B | 软泥底质掩埋 |
| 15 | freshwater_drum.md | 淡水石首鱼（Aplodinotus grunniens） | CSV 方向锚 | B | 砂砾底/深潭结构 |
| 16 | bowfin.md | 弓鳍鱼（Amia calva） | CSV 方向锚 | B | 沼泽植被掩体 |
| 17 | giant_snakehead.md | 眼鳢（Channa marulius） | CSV 方向锚（同属乌鳢互指不继承） | B | 植被表面掩体 |
| 18 | spotted_gar.md | 斑点雀鳝（Lepisosteus oculatus） | CSV 方向锚（同科 Tier A 样板相邻） | B | 植被缓流掩体 |

### 表 C｜追击组（16 文件）——BA-P01-PURSUIT-PLAIN（census PLAIN 族追击双因子投影）

| # | 文件 | 鱼（学名） | Story | 证据档 | 双因子（猎物场+栖息） |
|---|---|---|---|---|---|
| 19 | tiger_musky.md | 虎纹狗鱼（E. lucius × E. masquinongy 杂交行） | R08「虎纹 Identity-Deferred+P01 区分」点名 | B+ | 猎物鱼群+开放水/植被缘 |
| 20 | lenok.md | 细鳞鲑（Brachymystax lenok） | CSV 方向锚 | B | 流急猎物+急流深潭 |
| 21 | paroon_shark.md | 巨鲶（Pangasius sanitwongsei；CSV 行名「大青鲨」名实错位） | CSV 方向锚 | B | 猎物鱼群+开放水/深潭 |
| 22 | taimen.md | 哲罗鲑（Hucho taimen） | CSV 方向锚 | B | 鱼类猎物+深潭/激流 |
| 23 | asp.md | 赤稍雅罗鱼（Leuciscus aspius） | CSV 方向锚 | B | 上层小鱼群+开放水面 |
| 24 | haddock.md | 黑线鳕（Melanogrammus aeglefinus） | CSV 方向锚 | B | 底栖猎物+砂泥底/深水 |
| 25 | porbeagle.md | 鼠鲨（Lamna nasus） | CSV 方向锚 | B | 鱼群猎物+开放水/温跃层 |
| 26 | atlantic_halibut.md | 大西洋大比目鱼（Hippoglossus hippoglossus） | CSV 方向锚 | B | 底层鱼类+砂底大陆架 |
| 27 | tiger_trout.md | 虎纹鳟（Salmo trutta × Salvelinus fontinalis 杂交行） | CSV 方向锚 | B | 猎物鱼群+深潭/结构 |
| 28 | saithe.md | 绿青鳕（Pollachius virens） | CSV 方向锚 | B | 中上层鱼群+开放水/岩礁缘 |
| 29 | lake_trout.md | 湖红点鲑（Salvelinus namaycush） | CSV 方向锚 | B | 深水饵鱼+深湖冷水层 |
| 30 | yellow_perch.md | 黄鲈（Perca flavescens） | CSV 方向锚 | B | 无脊椎/小鱼+植被缘 |
| 31 | muskellunge.md | 北美狗鱼（Esox masquinongy） | CSV 方向锚（同属白斑狗鱼三 Story 互指） | B | 猎物鱼群+植被缘掩体 |
| 32 | cutthroat_trout.md | 白马切喉鳟（Oncorhynchus clarkii） | CSV 方向锚（同属虹鳟互指不继承） | B | 流区猎物+急流/深潭 |
| 33 | chain_pickerel.md | 链纹狗鱼（Esox niger） | CSV 方向锚 | B | 猎物鱼群+植被掩体 |
| 34 | mahimahi.md | 鬼头刀（Coryphaena hippurus） | CSV 方向锚 | B | 漂浮物聚集猎物+开放水漂浮结构 |

### 表 D｜夜行组（10 文件）——BA-P01-NOCTURNAL-SINGLE（live §11.5 判例：SINGLE+低光槽）

| # | 文件 | 鱼（学名） | Story | 证据档 | Response |
|---|---|---|---|---|---|
| 35 | african_sharptooth_catfish.md | 革胡子鲶（Clarias gariepinus） | CSV 方向锚 | B | R-T1+光照 cue 参数 |
| 36 | amur_catfish.md | 土鲶（Silurus asotus） | CSV 方向锚 | B | 同上 |
| 37 | goldeye.md | 金眼鱼（Hiodon alosoides） | CSV 方向锚（光敏边界登记） | B | 同上 |
| 38 | soldatov_catfish.md | 六须鲶（Silurus soldatovi） | CSV 方向锚 | B | 同上 |
| 39 | sauger.md | 加拿大梭鲈（Sander canadensis） | CSV 方向锚（同属玻璃梭鲈互指） | B | 同上 |
| 40 | channel_catfish.md | 斑点叉尾鮰（Ictalurus punctatus） | CSV 方向锚（scent 轴不并入登记） | B | 同上 |
| 41 | american_eel.md | 美洲鳗鲡（Anguilla rostrata） | CSV 方向锚（scent 轴不并入登记） | B | 同上 |
| 42 | redtail_catfish.md | 红尾鲶（Phractocephalus hemioliopterus） | CSV 方向锚 | B | 同上 |
| 43 | tiger_sorubim.md | 虎纹鸭嘴鲇（Pseudoplatystoma fasciatum） | CSV 方向锚 | B | 同上 |
| 44 | brown_bullhead.md | 云斑鮰（Ameiurus nebulosus） | CSV 方向锚 | B | 同上 |

### 表 E｜机会组（13 文件）——BA-P01-OPPORTUNE-SINGLE ×11 + BA-P01-BOUNDARY-DECL ×2

| # | 文件 | 鱼（学名） | Story | 证据档 | Bake / Response |
|---|---|---|---|---|---|
| 45 | brown_trout.md | 褐鳟（Salmo trutta）S12 | B01-S12 普通摄食与季节脉冲（census B2）——**组 Tier A 样板** | A | OPPORTUNE-SINGLE / R-T1 |
| 46 | rainbow_trout.md | 虹鳟（Oncorhynchus mykiss）S24 | B01-S24 鼠形表面饵地域变体（census B1；**absence claim 阴性样本**） | A | BOUNDARY-DECL / R-T1 |
| 47 | paddlefish_habituation.md | 鸭嘴鲟（Polyodon spathula）S35 | B01-S35 习惯化与食物恢复（census B1；cue_history 输入轴） | A | BOUNDARY-DECL / R-T1 |
| 48 | yellowcheek.md | 鳡鱼（Elopichthys bambusa） | CSV 方向锚（食性列空） | B | OPPORTUNE-SINGLE / R-T1 |
| 49 | stone_moroko.md | 麦穗鱼（Pseudorasbora parva） | CSV 方向锚 | B | 同上 |
| 50 | japanese_seabass.md | 海鲈（Lateolabrax maculatus） | CSV 方向锚（双行关系待核） | B | 同上 |
| 51 | pale_chub.md | 宽鳍𫚭（Zacco platypus） | CSV 方向锚 | B | 同上 |
| 52 | labeo_barbel.md | 唇䱻（Hemibarbus labeo） | CSV 方向锚 | B | 同上 |
| 53 | blacktail_shiner.md | 迷人真小鲤（Cyprinella venusta） | CSV 方向锚 | B | 同上 |
| 54 | white_crappie.md | 白斑刺盖太阳鱼（Pomoxis annularis） | CSV 方向锚 | B | 同上 |
| 55 | black_crappie.md | 黑斑刺盖太阳鱼（Pomoxis nigromaculatus） | CSV 方向锚 | B | 同上 |
| 56 | pumpkinseed.md | 驼背太阳鱼（Lepomis gibbosus） | CSV 方向锚（好斗）——**R-T2 载体 1** | B | OPPORTUNE-SINGLE / R-T2 |
| 57 | striped_bass.md | 美洲条纹狼鲈（Morone saxatilis） | CSV 方向锚（好斗+4.65）——**R-T2 载体 2** | B | OPPORTUNE-SINGLE / R-T2 |

### 表 F｜特殊感官组（3 文件）——BA-P01-SENSE-SINGLE（K8 cue 轴并入）

| # | 文件 | 鱼（学名） | Story | 证据档 | cue 轴 |
|---|---|---|---|---|---|
| 58 | paddlefish_electro.md | 鸭嘴鲟 S34 | B01-S34 幼体电感受定位（census B1；PASSIVE_ELECTROSENSE 通道实例） | A | @ElectroFieldProfile（被动侧） |
| 59 | spiny_dogfish.md | 白斑角鲨（Squalus acanthias） | R07 被动电感知双例之一（点名） | B+ | @ElectroFieldProfile（被动侧） |
| 60 | thorny_skate.md | 棘背钝头鳐（Amblyraja radiata） | R07 被动电感知双例之二（点名；种身份三候选 [需核对]） | B+ | @ElectroFieldProfile（被动侧） |

### 明确排除项（不属本批第一轮，显式记录）

| 排除项 | 理由 |
|---|---|
| 蓝鳃 S39 / 电鳗 S9 / 地图鱼 P01 面 / 欧鲢 P01 面 | 已由 guarding/migration 批承载（§3 登记 6 互指） |
| 青鱼（R04 #34）/ 鲤鱼 S08 / 鲮（#37）/ 黄尾鲴（#30） | REP-COVERAGE-DELTA-001 K3 底质/附着聚类成员——吸收判定已由该报告承载，另立 R04 成员补批（grazing 批先例） |
| 黑鼓鱼 / 草鱼 / 鳙鱼 / 大西洋鲱 | census 冻结 Pattern=P02/P03——归后续批 |
| 毛鳞鱼 / 高体鳑鲏 | K4 繁殖/产卵锚聚类成员，无 guard relation、P01 归属无证据（guarding 批排除表） |
| 大口黑鲈 | Story DB 0 Story（guarding 批排除表 Identity 隔离） |
| 莱氏拟乌贼 | R07 光 cue 候选但头足类 Product Scope Deferred |
| 海七鳃鳗 / 西方七鳃鳗 | 七鳃鳗系：海七鳃鳗 Semantic Open（非 P01 冻结，cue 轴已由 REP-CUE-AXIS-001 承载）；西方七鳃鳗身份待核——归 cue 轴线澄清 |
| 大西洋狼鱼 | R10 停食护卵第 5 例＝guarding 批登记补批成员（P04 侧）——P01 面待对账避免双批踩踏（§4 登记项 5） |
| whitefish 通名系（湖白鲑/驼背白鲑/高白鲑）、粉鲑、其余鲑科洄游行 | P05 侧归属未对账（migration 批登记项 1/4）——P01 面待 Story DB 名单到达一并处理（§4 登记项 5） |
| 大口牛胭脂鱼 | 15-Case C10 四面已由 four-surface-completion-r1 承载（grazing 批先例） |
| 白金火箭（白化鳄雀鳝）/ 白化高首鲟 / 白化叉尾鮰 / 镜鲤(白化) 等变体行 | 变体行不分裂先例（并入本体文件登记或本体批承载） |
| 硬头鳟 / 红鲑鱼（CSV 行） | 同种异行（=虹鳟海型 / =红鲑）——本体文件已建 |
| 常见拟鲤 / 湖拟鲤双行 | R09「拟鲤双行同批证据对」——身份先对账再收录（§4 登记项 5） |
| 斑点黑鲈 / 绿太阳鱼 / 岩钝鲈 / 日本鲭 / 真鲷 / 鲻鱼 / 蓝鲨 / 镜鲤 / 红罗非 / 金目丽鱼 / 奥里诺科孔雀鲈 / 眼点丽鱼 / 枯叶鱼 / 茅尖鱼 / 短扁口鲶 / 常见鮈鱼 / 白化草鱼 / 大理石倒立鱼 / 眼斑河魟 / 大西洋黄貂鱼 / 大西洋小鳕 / 条石鲷 / 黑食人鱼 / 巴亚拉鱼 / 红尾梭鱼 / 长吻鲍氏脂鲤 / 花鮨 / 巨狼鱼 / 黑牛胭脂鱼 / 丁鱥 / 美洲拟鲽 / 巴西马鲛 / 双线无须鳕 / 大眼金枪鱼 / 黄尾鰤 / 太平洋蓝鳍金枪鱼 / 长鳍金枪鱼 / 蓝笛鲷 / 高体鰤 / 赤梢鱼 / 美国红鱼 / 旗鱼 / 条纹四鳍旗鱼 / 东方狐鲣 / 裸狐鲣 / 牛港鲹 / 黄旗金枪鱼 / 鬼头刀外金枪鱼系 / 金鳟 / 塞凡湖鳟 / 黑口红点鲑 / 花羔红点鲑 / 红鳍狗鱼 / 北极茴鱼 / 沙塘鳢 / 葛氏鲈塘鳢 / 斑点叉尾鮰外鮰鲶系余量 / 黑斑须雅罗鱼（=溪鲦） / 大青鲨外巨鲶余量 / 美洲条纹狼鲈外狼鲈系 / 鲱形余量 等 | **第二轮候选池**——CSV 机械分组未入组（组配额行序后段）或身份待核；不冒充覆盖，待 Story DB 名单或第二轮收录（§4 登记项 2） |

## 2. 表达读数（对模板计数的影响）

- **Group Routing**：60/60 文件＝「无路由程序，默认 Normal Group」显式声明（§1.1 无路由声明 + §1.2 单默认行 + §1.3 伪脚本保留 Share 契约校验位）。这印证 handoff 预判「P01 绝大部分无路由（Normal Group）」——census P01 域 Group 面全样本 NO_SURFACE_EFFECT（9/9 快照）+ 本批全部退化形。**L_group 无增长**；与前三批双形态（routed/no-route）相比本批单一退化形。
- **Bake**：本批核心面。60 文件落在 census registry v4 两个既有 Bake 族的投影 + 一个表达层声明形态：**BA-P01-AMBUSH-SINGLE ×15**（census SINGLE 族结构因子侧——FGA Tier A 样板）、**BA-P01-OPPORTUNE-SINGLE ×11**（census SINGLE 族资源 patch 侧——BRT12 Tier A 样板）、**BA-P01-NOCTURNAL-SINGLE ×10**（census SINGLE 族低光侧——live §11.5 判例：MERGE_SUPPORTED → BA-T1 + DynamicSpatialSlot，**BakeTemplate +0**；VISIBILITY-LIMITED-FEEDING 家族候选）、**BA-P01-SENSE-SINGLE ×3**（census SINGLE 族感官梯度/感官 patch 侧——PAD34/LAM chemical_gradient 先例）、**BA-P01-PURSUIT-PLAIN ×16**（census PLAIN 族追击双因子——MDF 第 5 成员同族）、**BA-P01-PLAIN ×1**（census PLAIN 在案成员直投——MDF）、**BA-P01-BOUNDARY-DECL ×4**（**本批新表达层形态**：Bake 面无 Story 派生程序显式声明——census PIK/GAR/RAI/PAD35 Bake 面判语「Static Habitat 无空间新证据」的显式化；无程序≠省略面）。**投影标签封闭枚举**（validator BAKEFAM 钉死 7 值，新值=规格动作）；**族边界进校验**（FAMCTX：SINGLE 系单因子+NORMALIZE_WEIGHT 禁 combine/多因子；NOCTURNAL 强制 LowLight 槽且槽位仅此族可用；PLAIN 系双因子+CombineRule OPERATOR UNDEFINED 禁归一化/槽；BOUNDARY-DECL 禁一切程序行）。**census 侧 ΔL_bake=0（本批零新族）；live 侧无新句型（低光=§11.5 判例 +0 读法原样；BOUNDARY-DECL 是声明形态不是句型）。**
- **Response**：**R-T1 单通道（Feeding；Reaction 槽 OFF）×58 + R-T2 固定双通道（Feeding+Reaction）×2**（pumpkinseed/striped_bass——本批 P01 域 R-T2 形态表达验证载体，选择依据=CSV 好斗方向锚，Story 级证据 [需正文]）。R-T2 伪脚本双通道完全展开：固定 Feeding Channel + 固定 Reaction 通道 + MAX 汇总 + 算子标注 OPERATOR UNDEFINED（live §17 同款）。夜行组光照/低光 cue 并入 Feeding 评价参数（§11.5 判例原样：RR-1 Feeding-only + LightAvailability/Cue Profile——低光不另开通道）。cue 轴消费：@ElectroFieldProfile ×3（被动侧）；@ScentCueProfile ×0（嗅觉仅 ctx 文案——无 Story 证据不冒充，§4 登记项 3）。**L_response 无增长（结构族仍＝R-T1/R-T2 两个）。**
- **Quality**：60/60=QT-1 绑定表形态；0 个 W1–W3 物种级品质调整表（census P01 域 Quality 面全样本 NO_SURFACE_EFFECT）。**L_quality 无增长。**
- **新列结构**：零（分群结果 5 列/BAKE 字段-值/RESP 5 列/绑定表 5 列/META 2 列——全部 live 已声明变体；bake 配置行键封闭枚举防行内键注入，由 validate_normal.py STRUCT/FAMCTX 族强制）。

## 3. 跨批一致性登记

1. **census 族 ↔ live 句型两层 reconciliation OPEN（承 grazing/migration 批登记 1）**：本批投影标签（BA-P01-*）是 census LogicTemplate 族的批投影标签，不是 live 句型晋升；live 侧等价读法=BA-T1 底板+B-T1 单/双因子形态（§13.2）+ §11.5 DynamicSpatialSlot（夜行组）。两层是否等价归机制侧裁决，本批不闭合。
2. **Tier B 归族裁决权移交（承 grazing/migration 批登记 2）**：46 个 Tier B 文件的组归属与 BakeTemplate 是表达层选择（CSV 方向锚的最低结构）；Story 正文到达后 census 判同可能改判（换组/换标签/换 Response 拓扑）＝**结构变更需重审**（validator 族边界拦截静默改写），不是 Profile 重绑定。同属/同科互指（斑鳜×鳜鱼、斑点雀鳝×佛罗里达雀鳝、北美狗鱼×白斑狗鱼、湖红点鲑×红点鲑系、白马切喉鳟×虹鳟等）只是读法一致性，不是判同结论——行级证据到前不继承。
3. **R-T2 在 P01 域的成员选择 OPEN**：handoff 预判「R-T2 双通道（Reaction on）」形态存在于 P01 域；本地无一条已审 P01 Story 支持 R-T2（census TYPED 族成员全为单通道形态）。本批以 2 个 CSV 好斗锚文件（pumpkinseed/striped_bass）作表达验证载体——R-T2 结构在 P01 域的 Story 级成员、MAX 汇总语义、与 RR-T1（Feeding+Optional Reaction）的折叠关系全部 OPEN（live §17.5 压缩候选本身未闭合）。
4. **K8 cue 轴消费边界**：@ElectroFieldProfile 被动侧消费 ×3（paddlefish_electro=census PASSIVE_ELECTROSENSE 通道实例；spiny_dogfish/thorny_skate=R07 Delta Candidate 双例）——产品电呈现输入契约 TAR-07 未定，全部按轴占位消费。scent 轴零消费：鳗/鮰嗅觉灵敏、金眼鱼光敏仅为 ctx 方向文案，不并入 @ScentCueProfile（无 Story 证据不冒充；cue 轴消费需 Story 级证据——REP-CUE-AXIS-001 规格）。
5. **BOUNDARY-DECL 新表达形态**：Bake 面「无 Story 派生空间程序」的显式声明（census Static Habitat 判语的显式化）是本批新表达形态（承 grazing 批「无路由程序显式声明」同型先例——退化形/无程序≠省略面）；×4 文件（alligator_gar/northern_pike_strike/rainbow_trout/paddlefish_habituation）。捕获边界亚组（R07「Capture Boundary 首次成轴」）的 Response 语义=仅初次接受（post-instantiation OUT_OF_SCOPE owner 边界逐文件声明）。
6. **同种多 Story/多批分工互指闭合**：白斑狗鱼三 Story 三文件三批（S18 本批 ambush/S20 本批 strike/S19 migration 批 spawn）互指不重复；鸭嘴鲟两 Story 两文件（S34 electro/S35 habituation）；笋壳鱼双批分工（P01 本批/P04 候选 guarding 批退回档）；鳜鱼 P01+P02（本批 P01 主面，P02 归后续批）。handoff 六亚结构分组中「鱼食性/体型分级型 ~15」**作为参数维度映射**（营养级 ≥4.0 piscivore 的 size_window/evaluator 参数宽度标记），不设独立文件组——欧鲢先例（migration 批 size_class premise）+ CHB 判例的读法（README §2 表 C 标记）。
7. **UsableForageAvailability 契约复用（承 grazing/migration 批登记）**：SINGLE/PLAIN 系 56 文件 Bake 输入契约行三过滤引用；BOUNDARY-DECL 4 文件无程序故无契约行（validator CONTRACT 族对 BOUNDARY 豁免）。

## 4. 退回与登记项（转 Coordinator）

| 项 | 内容 |
|---|---|
| 登记项 1（名单构造方法——本批最大登记项） | **Story DB 主 relation=P01 的逐行名单不在本地**。第一轮 60 文件中 46 个 Tier B 的名单=CSV 习性列机械分组构造（§1 名单声明规则），**不是 Story DB 名单**。需 coordinator 提供 Story DB P01 导出（鱼名+Story+relation）或行级标签核对表；核对后增删文件=表达层动作（结构变更需重审），本批不冒充全样本 |
| 登记项 2（第一轮/第二轮拆分说明） | handoff 估计 P01 剩余 120-150 条 vs 第一轮 60 文件。缺口构成：(a) CSV 机械分组未入组的第二轮候选池（排除表末行，约 50+ 行）；(b) Story DB 名单中可能有 CSV 之外/身份冲突的 Story；(c) handoff 亚结构配额（机会组 40-60/鱼食性分级 15）远大于第一轮实际（机会 13/分级=维度映射）——机会组 CSV 锚信号弱（活泼/温和行多为鲤科场食/刮食型，P01 主面证据待名单），第一轮从紧不冒充。第二轮输入=Story DB 名单或 coordinator 点名 |
| 登记项 3（组间张力与 cue 轴边界） | CSV 习性行与 census/组结构的张力清单：翘嘴红鲌/蒙古红鲌（CSV 躲藏 vs 上层追击常见读法）；褐鳟/虹鳟（CSV 追猎 vs census 机会组判定——census 优先先例）；棘背钝头鳐（夜行 vs 感官组）；斑点叉尾鮰/美洲鳗鲡（嗅觉方向 vs scent 轴零消费）。scent 轴在 P01 域的 Story 级成员待 Story DB 名单（有则补 @ScentCueProfile 消费文件） |
| 登记项 4（名实/身份待核清单） | 「大青鲨」行名实错位（英文名软骨鱼/学名巨鲶）；海鲈/海鲈鱼双行（花鲈种复合体）；白金火箭=白化鳄雀鳝变体行（并入 alligator_gar 登记）；虎纹狗鱼 R08 Identity-Deferred 杂交行；「鳐」三候选（棘背钝头鳐承载+大西洋黄貂鱼/眼斑河魟待澄清）；彩虹镖鲈=R10 镖鲈科首例按 CSV 唯一行承载；虎纹鳟杂交行；鳡鱼/海鲈/唇䱻食性列空行 |
| 登记项 5（排除项的后续归属） | 大西洋狼鱼 P01 面（P04 补批对账后处理）；whitefish 系/粉鲑/鲑科余量（migration 批登记项 1/4 联动——P01+P05 双面名单一起对）；拟鲤双行（R09 证据对先裁）；K3 四鱼（R04 成员补批）；七鳃鳗系身份（cue 轴线） |
| [需正文] 批量项 | 46 个 Tier B 文件的猎物构成/因子细节/Response 参数方向（逐文件 §0/§5 已列）；R-T2 两载体的 Reaction 通道证据；夜行组光照 cue 的产品侧输入契约 |
| 无 UPSTREAM_CHANGE_EVENT | 本批未发现机制侧问题；表达层全部落在既有 census 族（SINGLE/PLAIN）/live 结构槽位（G-T1 退化形+BA-T1+B-T1+DynamicSpatialSlot+R-T1/R-T2+QT-1）内。BOUNDARY-DECL/R-T2 载体/名单构造方法是登记项不是机制缺陷主张 |

## 5. 验证记录（命令与输出原样）

命令（selftest）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal/validate_normal.py" --selftest
```

命令（真实交付包校验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal/validate_normal.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal"
```

输出：见下方两个代码块（原样粘贴，未改测试凑通过）。缺陷史：selftest 首轮抓出 validator 真实实现缺陷 1 处（check_file 丢失 bake 表检查调用——重写事故）+ fixture 派生缺陷 3 处（PLAIN/NOCTURNAL/RT2 三个 fixture 的 Profile 清单未随伪脚本替换更新——教训 9 复现），均修复校验器/fixture 而非改检查语义；真实校验首轮抓出真实工件缺陷 3 处（american_eel/channel_catfish §5 先例引用误写 @ScentCueProfile 前缀 ×2——教训 11 第二击；rainbow_trout BOUNDARY 形态 Profile 清单多余三契约 token ×1）——均修复工件而非改校验器。

### selftest 输出

```
[OK  ] baseline (single) passes unchanged
[OK  ] baseline (plain/pursuit) passes unchanged
[OK  ] baseline (nocturnal) passes unchanged
[OK  ] baseline (rt2) passes unchanged
[OK  ] baseline (boundary-decl) passes unchanged
[OK  ] HEADER fires on missing NOT AUTHORITY
[OK  ] HEADER fires on missing BATCH_ID line
[OK  ] SECTIONS fires on missing Bake section
[OK  ] GROUPFORM fires when 1.1 loses no-route declaration
[OK  ] GROUPFORM fires on Special Group route row
[OK  ] SHARE fires on missing default route row
[OK  ] SHARE fires on missing validation block
[OK  ] BAKEFAM fires on value outside closed enum
[OK  ] BAKEFAM fires on missing BakeTemplate row
[OK  ] FAMCTX fires on SINGLE carrying CombineRule row
[OK  ] FAMCTX fires on PLAIN missing Factor2 row
[OK  ] FAMCTX fires on PLAIN carrying Normalization row
[OK  ] FAMCTX fires on NOCTURNAL missing LowLight slot
[OK  ] FAMCTX fires on non-nocturnal carrying slot row
[OK  ] FAMCTX fires on BOUNDARY carrying program row
[OK  ] PREMBIND fires on binding without premise
[OK  ] CONTRACT fires on missing forage contract row
[OK  ] REACTFORM fires when both topologies declared
[OK  ] REACTFORM fires when neither topology declared
[OK  ] REACTFORM fires on R-T2 missing MAX aggregate
[OK  ] REACTFORM fires on R-T2 missing operator annotation
[OK  ] REACTFORM fires on cue profile without fact read
[OK  ] QUALITYCOV fires when binding table emptied
[OK  ] PROFILES fires on used-but-unlisted token
[OK  ] PROFILES fires on listed-but-unused token
[OK  ] BAN fires on forbidden phrase LifecycleCohort
[OK  ] BAN fires on unannotated merge phrase in fence
[OK  ] STRUCT fires on stray table
[OK  ] STRUCT fires on unknown bake config field
[OK  ] exempt INSUFFICIENT_LOCAL_EVIDENCE file only needs header markers
== selftest ==
SELFTEST PASS
```

### 真实交付包校验输出

```
[PASS] african_sharptooth_catfish.md
[PASS] alligator_gar.md
[PASS] american_eel.md
[PASS] amur_catfish.md
[PASS] asp.md
[PASS] atlantic_halibut.md
[PASS] black_crappie.md
[PASS] blacktail_shiner.md
[PASS] bowfin.md
[PASS] brown_bullhead.md
[PASS] brown_trout.md
[PASS] chain_pickerel.md
[PASS] channel_catfish.md
[PASS] cutthroat_trout.md
[PASS] florida_gar.md
[PASS] freshwater_drum.md
[PASS] giant_snakehead.md
[PASS] goldeye.md
[PASS] haddock.md
[PASS] japanese_seabass.md
[PASS] labeo_barbel.md
[PASS] lake_trout.md
[PASS] lenok.md
[PASS] mahimahi.md
[PASS] mandarin_fish.md
[PASS] marble_goby_ambush.md
[PASS] mongolian_redfin.md
[PASS] muskellunge.md
[PASS] northern_pike_ambush.md
[PASS] northern_pike_strike.md
[PASS] paddlefish_electro.md
[PASS] paddlefish_habituation.md
[PASS] pale_chub.md
[PASS] paroon_shark.md
[PASS] porbeagle.md
[PASS] pumpkinseed.md
[PASS] rainbow_darter.md
[PASS] rainbow_trout.md
[PASS] redtail_catfish.md
[PASS] russian_sturgeon.md
[PASS] saithe.md
[PASS] sauger.md
[PASS] soldatov_catfish.md
[PASS] spinibarbus.md
[PASS] spiny_dogfish.md
[PASS] spotted_gar.md
[PASS] spotted_mandarin.md
[PASS] stone_moroko.md
[PASS] striped_bass.md
[PASS] taimen.md
[PASS] thorny_skate.md
[PASS] tiger_musky.md
[PASS] tiger_sorubim.md
[PASS] tiger_trout.md
[PASS] topmouth_culter.md
[PASS] white_crappie.md
[PASS] witch_flounder.md
[PASS] yellow_catfish.md
[PASS] yellow_perch.md
[PASS] yellowcheek.md
== result ==
PASS (60 species files, 0 violations)
```

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器纯标准库，内部强制 stdout UTF-8。

## 6. 边界声明

- 本包只做 P01 普通离散目标摄食系四面的生产级表达（第一轮；配置表 + 中文伪脚本完全展开；R-T2 载体双通道展开）；表达验证通过 ≠ 机制 promotion ≠ Freeze；不覆盖 live 主页 / census registry 任何 Verdict。
- 全部数值不冻结（@参数引用，Profile 层定值）；SINGLE 链无 combine 步（族域边界）；PLAIN 链 CombineRule 与 R-T2 MAX 汇总数学 OPERATOR UNDEFINED 待机制侧；R-T2 成员选择、census↔live 两层 reconciliation、cue 轴 scent 侧消费、名单构造方法核对全程 OPEN 可见。
- 每文件 §5 记录使用/放弃的自由度（含归族裁决权移交、同属判例不继承、捕获边界 OUT_OF_SCOPE、变体行不分裂、scent 轴不冒充）。
- 未 commit（提交由 Coordinator / 用户决定）。

BATCH_ID: REP-FULL-NORM-001

---

## REP-FULL-NORM-REV-001 验收记录（2026-09-11）

- verdict: ARTIFACT_REVISE（60 文件本体零改动；修复面全在 README——名单声明/Tier 计数/文本瑕疵）。
- F1 修正：名单「全部可机械复验」改为「分组规则可机械复验+选择步含未声明判据」——约 17 行合格跳行记录于 §1（花骨鱼/大西洋鳕鱼/欧洲巨鲶/玻璃梭鲈/公牛鲨/江鳕/牛头鲦/白亚口鱼/黄金鲫/鲢鱼等）。
- F2 修正：Tier B+ ×6→×4、Tier B ×46→×48（tiger_musky/rainbow_darter 自标 B 但 README 授 B+；保守方向簿记修正）。
- F3 修正：channel_catfish 登记项编号、tiger_musky 名映射注记。
- F4 external：reviewer Notion 接入 Stephen Song's Workspace（产品 Story 页 404）——Story DB 行级对照保持 OPEN 由有权限者补做。R-T2/scent 轴/身份五项维持 OPEN。
- BOUNDARY-DECL 四处判语逐字核实=声明属实；R-T1/R-T2 与 RR-T1/RR-T2 为两套 taxonomy（非标签错乱）。
