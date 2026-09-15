# P01 普通层第二轮（闭合）｜72 种

**Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED**

## 批次概览

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM2-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 6 批：P01 普通层第二轮——全量闭合轮） |
| 样本口径 | 72 文件。**闭合声明（本批最重要读数）**：CSV 机械回放口径——对 fish-reference-20260908.csv 全部 267 行按第一轮分组规则逐行回放，四组合格行 220 行，全部落在四类之一：第一轮已承载 59 + 姊妹批承载 36 + 本批建文件 72 + 显式排除 53 ＝ 220，**零未处理合格行**（closure_replay.py 机械复验）。**无选择步**（吸收第一轮 REV-001 F1 教训）：每行只经「是否已被承载 / 是否触发排除判据（19 类封闭判据）」两类判断；身份张力行一律「建+登记」。CSV 口径闭合 ≠ Story DB 口径闭合（逐行名单仍不在本地——双边界分立声明） |
| 三段任务 | A 段：REV-001 F1 合格跳行 17 行（9 建 8 排除）；B 段：CSV 其余合格行 61 建；C 段：R06-R10 本地可证 P01 成员全处理（R06 鲟系遗留 4 / R08 Thunnus 4+旗鱼 / 银龙鱼 P01 面等；不可证部分显式登记） |
| 基线 | SNAPSHOT_ONLY（同第一轮声明） |
| 表达读数 | Group：72/72 无路由显式声明（单一退化形）——L_group 无增长。Bake：全部落在第一轮定型 4 标签——BA-P01-AMBUSH-SINGLE ×11 / BA-P01-PURSUIT-PLAIN ×37 / BA-P01-NOCTURNAL-SINGLE ×9 / BA-P01-OPPORTUNE-SINGLE ×15——**零新族、零新枚举值**（封闭枚举 7 值不变）。Response：R-T1 单通道 ×72——**零 R-T2**（R-T2 验证第一轮已由 2 载体完成；R-T2 在 P01 域 Story 级成员维持 OPEN 不冒充收敛）。Quality：全部 QT-1。cue 轴零消费。新列结构：零 |
| 数值状态 | 全部 @参数引用；PLAIN 族 CombineRule 与 R-T2 MAX 数学 OPERATOR UNDEFINED 待机制侧；夜行组低光槽=live §11.5 判例形态 |
| 验证结果 | validate_normal2.py：selftest 35 用例 PASS（首轮零缺陷——校验器为第一轮换批号派生，族规则未动）；真实交付包 72 文件 0 违规 PASS（首轮即零缺陷）；closure_replay.py 闭合复验 PASS（220=59+36+72+53、unhandled=NONE、盘上文件 72 与名单零 mismatch） |
| 跨批登记 | 双批分工 ×4（大西洋鳕鱼/欧洲巨鲶/玻璃梭鲈/银龙鱼——P01 面 `_feeding` 后缀与姊妹批互指）；Cichla 三行不聚合；亚口科张力与点名单行不对称（白亚口鱼点名建、同科 4 行张力排除——归族重裁到达后统一重审）；口径张力行 10 行建+登记；R06-R10 逐鱼名单不可证部分登记；无 UPSTREAM_CHANGE_EVENT |
| 审核 | **REP-FULL-NORM2-REV-001 verdict: ARTIFACT_APPROVE**（reviewer 独立人工全量回放 267 CSV 行确认闭合；F1 类 0 名单 2 个非 CSV 行名漏列已修、F2 排除标签沿用 R1 时点 5 行已注——closure_replay.py 常量闭合账不受影响） |

## Species 汇总表（四文件组）

### 表 A｜伏击组（11 文件）——BA-P01-AMBUSH-SINGLE

| # | 文件 | 鱼（学名） | Story 档 | typed 因子 |
|---|---|---|---|---|
| 1 | bullhead_minnow.md | 牛头鲦（Pimephales vigilax） | F1 点名（CSV 行 80） | 缓流沙泥/植被缘掩体 |
| 2 | white_sucker.md | 白亚口鱼（Catostomus commersonii；CSV 英文名 Yaqui Sucker 名实错位 [需核对]） | F1 点名（行 117；亚口科张力登记） | 砂砾底/石缘贴近 |
| 3 | grass_puffer.md | 星点东方鲀（Takifugu niphobles） | CSV 行 141 | 沙泥潮间带掩埋 |
| 4 | blackhead_seabream.md | 黑鲷（Acanthopagrus schlegelii） | CSV 行 143 | 岩礁/沙泥交错结构 |
| 5 | northern_whiting.md | 沙鮻（Sillago sihama） | CSV 行 159 | 沙底半埋掩体 |
| 6 | yellowtail_flounder.md | 大西洋黄盖鲽（Myzopsetta ferruginea） | CSV 行 176 | 软泥底掩埋伏击 |
| 7 | stellate_sturgeon.md | 闪光鲟（Acipenser stellatus） | R06 遗留点名（行 198） | 河底深槽触须贴近 |
| 8 | arctic_grayling.md | 北极茴鱼（Thymallus arcticus） | CSV 行 225（鲑科无洄游标注） | 急流砾石结构贴近 |
| 9 | silver_arowana.md | 银龙鱼（Osteoglossum bicirrhosum） | R08 P04 边界互指（行 238） | 水面植被边缘伏击 |
| 10 | atlantic_sturgeon.md | 尖吻鲟（Acipenser oxyrinchus） | R06 遗留点名（行 252） | 河口河底触须贴近 |
| 11 | shortnose_sturgeon.md | 短吻鲟（Acipenser brevirostrum） | R06 遗留点名（行 267） | 河底深槽/砾石贴近 |

### 表 B｜追击组（37 文件）——BA-P01-PURSUIT-PLAIN

| # | 文件 | 鱼（学名） | Story 档 | 双因子（猎物场+栖息） |
|---|---|---|---|---|
| 12 | spotted_steed.md | 花骨鱼（Hemibarbus maculatus） | F1 点名（行 22） | 底栖无脊椎/小鱼+砾石潭渊 |
| 13 | atlantic_cod_feeding.md | 大西洋鳕鱼（Gadus morhua） | F1 点名（行 84；双批分工：P05 面=migration 批 atlantic_cod.md） | 底层鱼类+砂泥大陆架 |
| 14 | blackmouth_char.md | 黑口红点鲑（Salvelinus confluentus；CSV 英文名 Blackmouth Salmon 名实错位 [需核对]） | CSV 行 76（鲑科无洄游标注） | 冷水饵鱼+深潭结构 |
| 15 | sevan_trout.md | 塞凡湖鳟（Salmo ischchan） | CSV 行 145（鲑科无洄游标注） | 湖沼饵鱼+开阔湖面/深水 |
| 16 | tench.md | 丁鱥（Tinca tinca） | CSV 行 119 | 底栖猎物+泥底植被潭 |
| 17 | sailfish.md | 旗鱼（Istiophorus platypterus） | R08 点名（行 120；喙击打 strike seam 判例） | 上层鱼群+开阔大洋 |
| 18 | giant_trevally.md | 牛港鲹（Caranx ignobilis） | CSV 行 132 | 礁缘鱼群+礁盘开放水 |
| 19 | yellowfin_tuna.md | 黄旗金枪鱼（Thunnus albacares） | R08 点名（Thunnus 4/4；行 135） | 中上层鱼群+温跃层 |
| 20 | striped_marlin.md | 条纹四鳍旗鱼（Kajikia audax） | CSV 行 140 | 上层鱼群+温带开阔洋 |
| 21 | chinese_sleeper.md | 葛氏鲈塘鳢（Perccottus glenii） | CSV 行 144（耐冻系蛰伏面零证据互指） | 静水小鱼/无脊椎+植被泥底池塘 |
| 22 | striped_bonito.md | 东方狐鲣（Sarda orientalis） | CSV 行 148 | 上层鱼群+近海开阔水 |
| 23 | biara.md | 针牙脂鲤（Rhaphiodon vulpinus） | CSV 行 156（R1 候选池遗漏行） | 小鱼群+急流河道 |
| 24 | summer_flounder.md | 大西洋牙鲆（Paralichthys dentatus） | CSV 行 157（遗漏行） | 底层小鱼+砂底大陆架 |
| 25 | giant_grouper.md | 鞍带石斑鱼（Epinephelus lanceolatus） | CSV 行 160（遗漏行；伏击倾向 [需正文]） | 礁区猎物+岩礁洞穴 |
| 26 | dogtooth_tuna.md | 裸狐鲣（Gymnosarda unicolor） | CSV 行 163 | 深水鱼群+礁缘开阔洋 |
| 27 | winter_flounder.md | 美洲拟鲽（Pseudopleuronectes americanus） | CSV 行 177（R1 候选池列名） | 底栖无脊椎/小鱼+近岸砂泥 |
| 28 | giant_wolffish.md | 巨狼鱼（Hoplias aimara；≠大西洋狼鱼 Anarhichas——排除行） | CSV 行 179 | 小鱼/无脊椎+急流岩礁河道 |
| 29 | serra_mackerel.md | 巴西马鲛（Scomberomorus brasiliensis） | CSV 行 185 | 上层鱼群+西大西洋礁缘 |
| 30 | silver_hake.md | 双线无须鳕（Merluccius bilinearis） | CSV 行 186 | 底层鱼群+大陆架深水 |
| 31 | bigeye_tuna.md | 大眼金枪鱼（Thunnus obesus） | R08 点名（Thunnus 4/4；行 188） | 深水鱼群+温跃层下 |
| 32 | yellowtail_amberjack.md | 黄尾鰤（Seriola lalandi） | CSV 行 189 | 中上层鱼群+礁缘开阔水 |
| 33 | bicuda.md | 长吻鲍氏脂鲤（Boulengerella cuvieri） | CSV 行 190 | 水面小鱼+急流开阔河道 |
| 34 | pacific_bluefin.md | 太平洋蓝鳍金枪鱼（Thunnus orientalis） | R08 点名（Thunnus 4/4；行 194） | 跨洋鱼群+温带开阔洋 |
| 35 | green_jobfish.md | 蓝笛鲷（Aprion virescens） | CSV 行 196 | 礁缘鱼群+清澈礁盘深水 |
| 36 | redtail_barracuda.md | 红尾梭鱼（Acestrorhynchus falcatus） | CSV 行 197 | 开阔水小鱼群+静水河道 |
| 37 | anthias.md | 花鮨（Anthias anthias；CSV 英文名 Grouper 错位 [需核对]） | CSV 行 199 | 底层无脊椎/小鱼+岩礁 |
| 38 | greater_amberjack.md | 高体鰤（Seriola dumerili） | CSV 行 202 | 礁缘鱼群+深水结构 |
| 39 | european_perch.md | 赤梢鱼（Perca fluviatilis；学名=欧洲河鲈 [需核对]） | CSV 行 205 | 小鱼/无脊椎+植被湖泊 |
| 40 | albacore.md | 长鳍金枪鱼（Thunnus alalunga） | R08 点名（Thunnus 4/4；行 210） | 上层鱼群+副热带开阔洋 |
| 41 | atlantic_tomcod.md | 大西洋小鳕（Microgadus tomcod） | CSV 行 213（R1 候选池列名） | 底层无脊椎/小鱼+河口浅水 |
| 42 | narrowbarred_mackerel.md | 康氏马鲛（Scomberomorus commerson） | CSV 行 214（遗漏行） | 上层鱼群+印-太近海 |
| 43 | rock_bream.md | 条石鲷（Oplegnathus fasciatus） | CSV 行 216 | 底栖硬壳猎物+岩礁 |
| 44 | black_piranha.md | 黑食人鱼（Serrasalmus rhombeus） | CSV 行 223 | 静水小鱼+浊水植被河道 |
| 45 | payara.md | 巴亚拉鱼（Hydrolycus scomberoides） | CSV 行 247 | 开阔水小鱼群+急流深潭 |
| 46 | redfin_pickerel.md | 红鳍狗鱼（Esox americanus） | CSV 行 248（R06 遗留点名联动） | 小型鱼群+植被缓流 |
| 47 | red_drum.md | 美国红鱼（Sciaenops ocellatus） | CSV 行 260 | 底层鱼群+河口沙泥底 |
| 48 | butterfly_peacock.md | 眼点丽鱼（Cichla ocellaris；Cichla 三行之一） | CSV 行 264 | 鱼群猎物+静水结构湖泊 |

### 表 C｜夜行组（9 文件）——BA-P01-NOCTURNAL-SINGLE（live §11.5 判例）

| # | 文件 | 鱼（学名） | Story 档 | 夜行底板轴 | Response |
|---|---|---|---|---|---|
| 49 | wels_catfish_feeding.md | 欧洲巨鲶（Silurus glanis） | F1 点名（行 35；双批分工：P04 面=guarding 批 wels_catfish.md） | 洞穴/深潭夜行底板 | R-T1+光照 cue |
| 50 | walleye_feeding.md | 玻璃梭鲈（Sander vitreus） | F1 点名（行 115；双批分工：P05 面=migration 批 walleye_spawn.md） | 低光开阔湖底/结构缘 | 同上 |
| 51 | bull_shark.md | 公牛鲨（Carcharhinus leucas） | F1 点名（行 241） | 河口浑水夜行巡猎 | 同上 |
| 52 | burbot.md | 江鳕（Lota lota） | F1 点名（行 245） | 石底深潭冬夜底板 | 同上 |
| 53 | mooneye.md | 月眼鱼（Hiodon tergisus；同属金眼鱼光敏登记联动） | CSV 行 221 | 开阔水面夜行表层 | 同上 |
| 54 | white_catfish.md | 白鲶鱼（Ameiurus catus；R1「鮰鲶系余量」本批收齐） | CSV 行 237 | 泥底池沼夜行底板 | 同上 |
| 55 | blue_catfish.md | 蓝鲶鱼（Ictalurus furcatus） | CSV 行 249 | 大河道深水夜行底板 | 同上 |
| 56 | black_bullhead.md | 黑鮰（Ameiurus melas） | CSV 行 258 | 泥底植被池沼夜行底板 | 同上 |
| 57 | flathead_catfish.md | 铲鮰（Pylodictis olivaris） | CSV 行 262 | 深潭/木石结构夜行底板 | 同上 |

### 表 D｜机会组（15 文件）——BA-P01-OPPORTUNE-SINGLE

| # | 文件 | 鱼（学名） | Story 档 | resource_patch 轴 |
|---|---|---|---|---|
| 58 | golden_crucian.md | 黄金鲫（Carassius auratus hybrid；Carassius 属对账注记） | F1 点名（行 3） | 静水缓流杂食机会场 |
| 59 | iridescent_shark.md | 蓝鲨（Pangasianodon hypophthalmus；CSV 撕鳍/肉食口径 [需核对]） | CSV 行 25 | 开阔河道机会场 |
| 60 | spotted_bass.md | 斑点黑鲈（Micropterus punctulatus） | CSV 行 102（R1 候选池列名） | 结构区小鱼机会场 |
| 61 | green_sunfish.md | 绿太阳鱼（Lepomis cyanellus） | CSV 行 116（R1 候选池列名） | 浅水植被无脊椎机会场 |
| 62 | rock_bass.md | 岩钝鲈（Ambloplites rupestris） | CSV 行 134（R1 候选池列名） | 岩礁结构小龙虾/小鱼机会场 |
| 63 | chub_mackerel.md | 日本鲭（Scomber japonicus；field 批大西洋鲭 P03 候选池联动） | CSV 行 150（R1 候选池列名） | 上层浮游/小鱼机会场 |
| 64 | common_gudgeon.md | 常见鮈鱼（Gobio gobio） | CSV 行 155（R1 候选池列名） | 沙底底栖无脊椎机会场 |
| 65 | pike_cichlid.md | 茅尖鱼（Crenicichla lepidota） | CSV 行 178（R1 候选池列名） | 近岸小鱼/无脊椎机会场 |
| 66 | headstander.md | 大理石倒立鱼（Abramites hypselonotus；CSV 肉食口径 [需核对]） | CSV 行 231（R1 候选池列名） | 缓流底层机会场 |
| 67 | river_chub.md | 小须美鱥（Nocomis micropogon；遗漏行） | CSV 行 125 | 缓流无脊椎/漂饵机会场 |
| 68 | dolly_varden.md | 花羔红点鲑（Salvelinus malma；鲑科无洄游标注） | CSV 行 200（R1 候选池列名） | 冷水无脊椎/小鱼机会场 |
| 69 | speckled_peacock.md | 金目丽鱼（Cichla temensis；三行之二） | CSV 行 154（R1 候选池列名） | 结构区鱼群机会场 |
| 70 | orinoco_peacock.md | 奥里诺科孔雀鲈（Cichla orinocensis；三行之三） | CSV 行 209（R1 候选池列名） | 静水支流鱼群机会场 |
| 71 | red_seabream.md | 真鲷（Pagrus major） | CSV 行 187（R1 候选池列名——首轮裁决遗漏，本批补齐） | 底层甲壳/小鱼机会场 |
| 72 | grey_mullet.md | 鲻鱼（Mugil cephalus；P06 刮食张力 [需核对]） | CSV 行 254（R1 候选池列名——首轮裁决遗漏，本批补齐） | 河口泥底碎屑/藻屑机会场 |

排除表要点（53 合格行，19+1 类封闭判据）：类 0 姊妹批承载 36 行；类 1 FIELD 批补批（鲢鱼）；类 2 census P02/P03/K3 冻结 7 行；类 4 品系/变体 16 行（L1-EQUIV 层）；类 8 亚口科 P06 张力 4 行；类 10 鲑科洄游行（粉鲑）；类 13 大西洋狼鱼（P04 补批）；其余名实错位/对账线各 1-2 行——每行一类一理由，零未声明跳行。

## 完整示例（F1 点名代表：atlantic_cod_feeding.md 全文）

> 本批无 census Tier A（第一轮 Tier A 成员已全部承载）——选 REV-001 F1 合格跳行点名首例、双批分工代表（P05 面=migration 批 atlantic_cod.md，本文件=P01 摄食面 `_feeding` 后缀）。

# 大西洋鳕鱼（Atlantic Cod｜Gadus morhua）｜追击型四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM2-001（P01 普通层 第 6 批：第二轮全量闭合——追击组） |
| Story | REV-001 F1 跳行点名（REP-FULL-NORM2-001 handoff 转录；CSV 行 84） |
| 冻结 Pattern | P01 [需核对]（CSV 方向锚归层） |
| 物种属性锚 | fish-reference-20260908：追猎、全天活跃、肉食性、营养级 4.09、benthopelagic（仅方向锚） |
| 基线 | SNAPSHOT_ONLY（live 转录 2026-09-10 版；census registry v4 快照；第一轮交付包） |
| 证据档 | Tier B+（点名锚；[需核对]） |
| 变体声明 | 无路由条件原子（显式声明）；分群结果＝5 列固定；品质表＝绑定表 |
| Response 拓扑 | NormalFeeding=R-T1 单通道（Feeding；Reaction 槽 OFF） |
| 亚结构组 | 追击型（pursuit/forage-coupled typed） |

## 0. 上游语义与摄食形态

- 摄食形态：大西洋鳕鱼（砂泥大陆架底层追击）。
- 证据边界：Story 行级 Pattern 标签不在本地 [需核对]；本文件结构为追击组样板（第一轮 Tier A 样板骨架）的表达层选择——Story 正文到达后 census 判同可能改判（换组/换 BakeTemplate/换 Response 拓扑＝结构变更需重审，validator 族边界拦截静默改写），不是 Profile 重绑定。
- 附加注记：双批分工——migration 批 atlantic_cod.md 承载 B01-S52 P05 繁殖期深度面；本文件＝CSV 行 P01 摄食面（同种多 Story 多文件先例：白斑狗鱼三文件）。
- Response 面：TYPED 族参数差异（底层大饵/慢速拖行呈现——组样板语义，参数级无新拓扑）。
- Group 面 / Quality 面：组样板 NO_SURFACE_EFFECT。
- 表达超集说明：骨架参数化表达；未超出组样板族域。

Profile 引用清单：@ACFForageProfile @ACFHabitatProfile @ACFPreyFields @ACFDietClasses @ACFSizeWindow @ACFNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| ACF_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census PLAIN 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-PURSUIT-PLAIN（本批投影标签＝census PLAIN_FACTOR_COMBINE；因子集→组合——追击型双因子投影，第一轮定型，本批零新族） |
| Factor1Type(typed) | forage_factor：底层鱼类猎物场轴（鳕科群游追击方向） |
| Factor2Type(typed) | habitat_factor：砂泥大陆架深水结构轴 |
| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@ACFPreyFields；diet_classes=@ACFDietClasses；size_window=@ACFSizeWindow） |
| LiveLayerProjection | B-T1 Independent Factor Set 双因子形态（§13.2 结构族读法；两层 reconciliation OPEN） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的 forage_factor 事实（底层鱼类猎物场轴）
读取 当前格子的 habitat_factor 事实（砂泥大陆架深水结构轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@ACFPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@ACFDietClasses 食性过滤
      与 size_window=@ACFSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR（槽1）：
    用 forage_factor 事实查询 @ACFForageProfile
    得到 DemersalForageFit

EVAL_TYPED_FIELD_OR_FACTOR（槽2）：
    用 habitat_factor 事实查询 @ACFHabitatProfile
    得到 ShelfGroundHabitatFit

COMBINE_WEIGHTED：
    合并两个 FactorFit
    算子标注：OPERATOR UNDEFINED — 待机制侧（多因子合并算子；live §15.3 同款占位声明）

返回 SpatialDistributionWeight（因子集链结束：无归一化步、无 gate——族边界）
```

### 2.3 live 层投影声明

census PLAIN 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @ACFNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实（底层大饵/慢速拖行呈现——组样板参数）评价 @ACFNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

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

- 使用的自由度：SINGLE/PLAIN 族投影标签与 typed 因子实例语义；Profile 命名；伪脚本步序（canonical 固定）。
- 放弃的自由度：(1) 归族裁决权移交（无 census 快照——Story 正文到达后判同可能改判，结构变更需重审）；(2) 合并算子（无 combine 步或 OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结；(4) 名单身份/口径张力项的裁决权（登记在案不冒充）。

BATCH_ID: REP-FULL-NORM2-001

（示例完）

## Provenance

- 本地路径：`A:\Projs\FCF-Harness-Handoff\programaticHitFish\outputs\full_authoring\normal2\`（README.md + validate_normal2.py + closure_replay.py + species\ 72 文件）
- GitHub：https://github.com/futouyiba/programaticHitFish （commit `ebc4ba7`，工作树干净）
- 审核 verdict：REP-FULL-NORM2-REV-001 = **ARTIFACT_APPROVE**（reviewer 独立人工全量回放 267 行确认闭合；F1/F2 修正已并入）。转录批次：2026-09-11
