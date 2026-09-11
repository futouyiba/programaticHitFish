# P01 普通离散目标摄食系四面生产级表达交付包（第二轮·全量闭合）｜REP-FULL-NORM2-001

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 角色 | fcf-representation-worker |
| 批次 | REP-FULL-NORM2-001（B0 REPRESENTATION_RUNNING，全库生产级表达 第 6 批：P01 普通层第二轮——**全量闭合轮**） |
| 输入 | (1) 第一轮交付包＝`outputs/full_authoring/normal/`（REP-FULL-NORM-001：60 文件样板 + validate_normal.py 校验器 + REV-001 验收记录——F1 跳行名单 17 行即本批 A 部分输入）(2) handoff REP-FULL-NORM2-001（点名待建约 8-10 行 + CSV 剩余合格行 + R06-R10 可证 P01 成员三段任务）(3) fish-reference-20260908.csv（267 行全库快照——本批机械回放输入）(4) 姊妹批判式＝guarding/grazing/migration/field 四批 README（已承载名单与互指边界）(5) R06-R10 批次摘要（outputs/batches/FISH-R06.md…FISH-R10.md + 各 FR3 记录）(6) live 基准转录 `tmp/live_stress_main_after.md`（2026-09-10 版——承第一轮引用不变） |
| 基线 | **SNAPSHOT_ONLY**——本 agent 无 Notion live 访问（Story DB 行级名单不在本地，同第一轮声明）；全部输入为本地归档/快照；live 漂移以本 README 引用的归档版为准 |
| 交付物 | `species/*.md` **72 文件**（每鱼四面：Group 无路由显式声明 + Bake 配置/伪脚本 + Response 配置/伪脚本 + Quality 绑定/伪脚本）+ 本 README + `validate_normal2.py` + `closure_replay.py`（闭合声明机械复验器——220 合格行四类裁决逐行回放，见 §5）；**四文件组**（§1 表 A–D）：伏击 11 / 追击 37 / 夜行 9 / 机会 15 |
| 数值状态 | 全部阈值/因子语义/Profile 值域为 **@参数引用**（生产数值由 Profile 层定值，不冻结）；PLAIN 族 CombineRule 与 R-T2 MAX 数学 **OPERATOR UNDEFINED** 待机制侧（承第一轮）；夜行组低光槽=live §11.5 判例形态 |

## 1. 样本口径（72 文件 / 全量闭合声明）

P01＝Discrete Target→TargetFeeding（承第一轮口径）。本批为 handoff 指定的**第二轮全量闭合轮**：加完本批后，P01 群组可声明——**CSV 全合格行 + Story DB 全本地可证成员均已处理（建文件）或显式排除（记理由）**。

### 1.1 闭合口径与判据（本批最重要的诚实边界）

**CSV 机械回放口径**：对 fish-reference-20260908.csv 全部 267 行按第一轮分组规则（R1 README §1，REV-001 已确认可机械复验）逐行回放：伏击＝性格∈{孤僻,躲藏}∧肉食∧非夜间；追击＝性格=追猎∧肉食∧非夜间；夜行＝夜间活跃∧肉食或杂食；机会＝性格∈{活泼,温和,撕鳍,好斗,警惕}∧未被前三组收。四组合格行 **220 行**，全部落在下列四类之一（逐行裁决可由交付包内 `closure_replay.py` 机械复验——四类承载名单+19 类排除判据入脚本常量，与 §1.4 表同源）：

| 裁决类 | 行数 | 处置 |
|---|---|---|
| 第一轮已承载（R1 60 文件覆盖的合格行） | 59 | 已建文件（含白金火箭变体行并入鳄雀鳝登记） |
| 姊妹批承载（SIB——guarding/grazing/migration/field 已承载该鱼 Normal/Feeding 摄食评价面） | 36 | 互指排除（§1.4 排除表第 0 类） |
| **本批建文件（N2）** | **72** | 本 README 表 A–D |
| 显式排除（记理由） | 53 | §1.4 排除表分类承载 |

220 = 59 + 36 + 72 + 53，**零未处理合格行**。规则外 47 行（267−220，不在四组机械分组域）不属本批 CSV 口径；其中已在 R1/本批排除表显式登记的（黄尾鲴/沙塘鳢等）见 §1.4 末注，其余为「非 CSV 分组域」——Story DB P01 名单若含规则外行，属名单到达后增补（表达层动作，不冒充闭合）。

**选择步透明声明（吸收 REV-001 F1 教训）**：第一轮的选择步含未声明判据（配额/身份置信/行序）；本批**无选择步**——四组每一合格行只经两类判断：(a) 是否已被 R1/姊妹批承载（机械比对承载名单）；(b) 未承载行是否触发排除判据（§1.4 的 19 类封闭判据表——每行一行一理由，无配额、无行序截断、无身份置信软判断；身份张力行一律「建+登记」而非「静默跳过」）。R1 候选池名单（排除表末行约 60 项）中合格行全部收齐；其中 7 行为 R1 候选池**名单遗漏行**（针牙脂鲤/大西洋牙鲆/鞍带石斑鱼/康氏马鲛/小须美鱥/真鲷/鲻鱼——R1 列池时漏记，本批逐文件 §0 注记补齐）。

**鲑科洄游排除判据（本批显式化）**：R1 排除表「其余鲑科洄游行——P05 侧归属未对账」的边界在本批取机械读法：**鲑科（Salmonidae）∧ CSV 迁徙类型列含洄游标注 → P05 对账线排除**（粉鲑）；鲑科无标注行可建（黑口红点鲑/塞凡湖鳟/花羔红点鲑/北极茴鱼——茴鱼亚科）。非鲑科行的迁徙标注（oceanodromous/potamodromous/amphidromous/anadromous）不触发排除（R1 先例：美洲条纹狼鲛 anadromous 已建）。

### 1.2 三段任务构成（对 handoff REQUESTED_ACTION）

- **A 段（REV-001 F1 合格跳行 17 行）**：9 行建文件（花骨鱼/大西洋鳕鱼/欧洲巨鲶/玻璃梭鲈/公牛鲨/江鳕/牛头鲦/白亚口鱼/黄金鲫——表 A–D 内标「F1 点名」）；8 行按 handoff 标注排除（鲢鱼→FIELD 批补批；罗非鱼/淡水石斑→guarding 已承载；泰鲮/巴西鲷→grazing 已承载；暹罗巨鲤→field 批已重建；圆腹雅罗鱼/银鲫→migration 已承载）。
- **B 段（CSV 其余合格行）**：61 行建文件（表 A–D 内标「CSV 行 N」）；其余见 §1.4 排除表。
- **C 段（R06-R10 Story DB 本地可证 P01 成员）**：本地可证成员全部处理——R06 遗留点名 4（闪光鲟/尖吻鲟/短吻鲟/红鳍狗鱼——本批建）；R08 摘要点名 5（旗鱼+Thunnus 4/4：黄旗/大眼/太平洋蓝鳍/长鳍——本批建）；R08 虎纹狗鱼/R10 彩虹镖鲈（R1 已建）；R07 电感知双例+CB 轴 2 例（R1 已建）；银龙鱼（R08 P04 边界样本——本批建 P01 面，P04 边界归 Guarding 系补批互指）。**不可证部分显式登记**（§4 登记项 1）：R06「淡水掠食 14+海水掠食 4」与「鲑系洄游 10」的逐鱼名单不在本地（migration 批登记项 1 同款）；R07 CB 轴其余 2 例、R10 名实分离三例/待人工 3 条、R08 蛰伏家族逐鱼——均不可逐鱼核对，由本批 CSV 220 行闭合兜底（CSV 合格行域内 R06-R10 成员已全覆盖；若 Story DB 行含 CSV 规则外/不合格行成员，名单到达后增补）。

### 1.3 表 A｜伏击组（11 文件）——BA-P01-AMBUSH-SINGLE

| # | 文件 | 鱼（学名） | Story 档 | typed 因子 |
|---|---|---|---|---|
| 1 | bullhead_minnow.md | 牛头鲦（Pimephales vigilax） | F1 点名（CSV 行 80） | 缓流沙泥/植被缘掩体 |
| 2 | white_sucker.md | 白亚口鱼（Catostomus commersonii；CSV 英文名 Yaqui Sucker 名实错位 [需核对]） | F1 点名（行 117；亚口科 P06 张力登记） | 砂砾底/石缘贴近 |
| 3 | grass_puffer.md | 星点东方鲀（Takifugu niphobles） | CSV 行 141 | 沙泥潮间带掩埋 |
| 4 | blackhead_seabream.md | 黑鲷（Acanthopagrus schlegelii） | CSV 行 143 | 岩礁/沙泥交错结构 |
| 5 | northern_whiting.md | 沙鮻（Sillago sihama） | CSV 行 159 | 沙底半埋掩体 |
| 6 | yellowtail_flounder.md | 大西洋黄盖鲽（Myzopsetta ferruginea） | CSV 行 176 | 软泥底掩埋伏击 |
| 7 | stellate_sturgeon.md | 闪光鲟（Acipenser stellatus） | R06 遗留点名（行 198） | 河底深槽触须贴近 |
| 8 | arctic_grayling.md | 北极茴鱼（Thymallus arcticus） | CSV 行 225（鲑科无洄游标注） | 急流砾石结构贴近 |
| 9 | silver_arowana.md | 银龙鱼（Osteoglossum bicirrhosum） | R08 P04 边界互指（行 238） | 水面植被边缘伏击 |
| 10 | atlantic_sturgeon.md | 尖吻鲟（Acipenser oxyrinchus） | R06 遗留点名（行 252） | 河口河底触须贴近 |
| 11 | shortnose_sturgeon.md | 短吻鲟（Acipenser brevirostrum） | R06 遗留点名（行 267） | 河底深槽/砾石贴近 |

### 1.3 表 B｜追击组（37 文件）——BA-P01-PURSUIT-PLAIN

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
| 39 | european_perch.md | 赤梢鱼（Perca fluviatilis；CSV 中文名赤梢鱼、学名=欧洲河鲈 [需核对]） | CSV 行 205 | 小鱼/无脊椎+植被湖泊 |
| 40 | albacore.md | 长鳍金枪鱼（Thunnus alalunga） | R08 点名（Thunnus 4/4；行 210） | 上层鱼群+副热带开阔洋 |
| 41 | atlantic_tomcod.md | 大西洋小鳕（Microgadus tomcod） | CSV 行 213（R1 候选池列名） | 底层无脊椎/小鱼+河口浅水 |
| 42 | narrowbarred_mackerel.md | 康氏马鲛（Scomberomorus commerson） | CSV 行 214（遗漏行） | 上层鱼群+印-太近海 |
| 43 | rock_bream.md | 条石鲷（Oplegnathus fasciatus） | CSV 行 216 | 底栖硬壳猎物+岩礁 |
| 44 | black_piranha.md | 黑食人鱼（Serrasalmus rhombeus） | CSV 行 223 | 静水小鱼+浊水植被河道 |
| 45 | payara.md | 巴亚拉鱼（Hydrolycus scomberoides） | CSV 行 247 | 开阔水小鱼群+急流深潭 |
| 46 | redfin_pickerel.md | 红鳍狗鱼（Esox americanus） | CSV 行 248（R06 遗留点名联动） | 小型鱼群+植被缓流 |
| 47 | red_drum.md | 美国红鱼（Sciaenops ocellatus） | CSV 行 260 | 底层鱼群+河口沙泥底 |
| 48 | butterfly_peacock.md | 眼点丽鱼（Cichla ocellaris；Cichla 三行之一） | CSV 行 264 | 鱼群猎物+静水结构湖泊 |

### 1.3 表 C｜夜行组（9 文件）——BA-P01-NOCTURNAL-SINGLE（live §11.5 判例）

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

### 1.3 表 D｜机会组（15 文件）——BA-P01-OPPORTUNE-SINGLE

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
| 69 | speckled_peacock.md | 金目丽鱼（Cichla temensis；Cichla 三行之二） | CSV 行 154（R1 候选池列名） | 结构区鱼群机会场 |
| 70 | orinoco_peacock.md | 奥里诺科孔雀鲈（Cichla orinocensis；Cichla 三行之三） | CSV 行 209（R1 候选池列名） | 静水支流鱼群机会场 |
| 71 | red_seabream.md | 真鲷（Pagrus major） | CSV 行 187（R1 候选池列名——**首轮裁决遗漏，本批补齐**） | 底层甲壳/小鱼机会场 |
| 72 | grey_mullet.md | 鲻鱼（Mugil cephalus；P06 刮食张力 [需核对]） | CSV 行 254（R1 候选池列名——**首轮裁决遗漏，本批补齐**） | 河口泥底碎屑/藻屑机会场 |

证据档：F1 点名/R06-R08 点名/互指锚＝Tier B+（[需核对]）；CSV 行 N＝Tier B（[需核对]）。全部 72 文件无 census 全四面快照（第一轮 Tier A 快照成员已全部承载）。

### 1.4 明确排除项（53 合格行 + 规则外登记；每行一类一理由，零未声明跳行）

| # | 排除类（封闭判据） | 行（CSV 行号） |
|---|---|---|
| 0 | 姊妹批承载（SIB——该鱼 Normal/Feeding 摄食评价面已在姊妹批文件承载，互指不重复建） | 36 行：蓝鳃太阳鱼(92)/黑鼓鱼外乌鳢(129)/南美肺鱼(173)/电鳗(206)/巨骨舌鱼(220)/圆鳍鱼(193)/单鳍多线鱼(204)/小口黑鲈(118)/双点美鱥(130)/黑斑须雅罗鱼(242)/七彩神仙鱼橙(138)/白(181)/美洲红点鲑(99)/灰西鲱(127)/白北鲑(146)/剑旗鱼(165)/大西洋鲑鱼(219)/帝王鲑(227)/红腹食人鱼(228)/北极红点鲑(230)/大马哈鱼(232)/银鲑(244)/美洲西鲱(137)/欧白鲑(151)/欧鲢(83)/圆腹雅罗鱼(46)/银鲫(72)/高首鲟(263)/大口牛胭脂鱼(266)/罗非鱼(17)/淡水石斑(39)/泰鲮(38)/巴西鲷(57)/暹罗巨鲤(42)/金草鱼/溪鲦（行号略——姊妹批承载名单按各批 README 表） |
| 1 | FIELD 批补批（handoff 指定） | 鲢鱼(7) |
| 2 | census P02/P03/K3 冻结（R1 维持） | 黑鼓鱼(65)/草鱼(184)/鳙鱼(10)/大西洋鲱鱼(75)/青鱼(14)/鲤鱼(164)/鲮(9) |
| 3 | K4 繁殖锚聚类（R1 维持） | 毛鳞鱼(87) |
| 4 | 品系/变体行不分裂（L1-EQUIV 层——field 批先例） | 锦鲤(16)/荷包红鲤(19)/镜鲤(23)/红罗非(28)/工程鲫(49)/鳞鲤白化(79)/鳞鲤人面鲤(161)/四白锦鲤(172)/镜鲤白化(183)/红白锦鲤(191)/白化草鱼(203)/无鳞鲤(207)/圆点五色锦鲤(208)/橙黄金锦鲤(217)/白化高首鲟(250)/白化叉尾鮰(251) |
| 5 | Carassius 属种群对账线（黄金鲫=handoff 点名行除外） | 野生鲫鱼(18)/金鲫(67) |
| 6 | 同种异行（虹鳟种复合体——硬头鳟先例） | 金鳟(100)/硬头鳟(257) |
| 7 | 植食/滤食→P06/P03 对账线（P01 捕食方向证据弱；鲢鳙草鲱先例同族） | 淡水白鲳(30)/美洲锐唇鲷(97)/红钩鱼(195)/日本竹荚鱼(171)/湖白鲑(239) |
| 8 | 亚口科 P06 Pattern 张力（grazing 批登记项 1 对账线；白亚口鱼=handoff 点名单行例外，见 §3 登记 7） | 水牛鱼(128)/金红马鱼(139)/河红马鱼(170)/黑牛胭脂鱼(111) |
| 9 | whitefish 系 P05 对账（R1 维持） | 驼背白鲑(152)/高白鲑(169) |
| 10 | 鲑科洄游行 P05 对账（§1.1 机械判据） | 粉鲑(235) |
| 11 | 七鳃鳗系（Semantic Open/身份待核——cue 轴线，R1 维持） | 海七鳃鳗(74)/西方七鳃鳗(104) |
| 12 | Story DB 0 Story（Identity 隔离，R1 维持） | 大口黑鲈(103) |
| 13 | P04 补批对账（R10 停食护卵首例护卵型——guarding 补批线，R1 维持） | 大西洋狼鱼(158) |
| 14 | 头足类 Product Scope Deferred（R1 维持） | 莱氏拟乌贼(211) |
| 15 | 鳐身份三候选待澄清（R1 维持） | 大西洋黄貂鱼(215)/眼斑河魟(234) |
| 16 | R09 拟鲤双行对账（R1 维持） | 常见拟鲤(180)/湖拟鲤(192) |
| 17 | 花鲈种复合体双行对账（R1 维持） | 海鲈鱼(168) |
| 18 | P03 场化承载互指（field 批 piraiba 滤食场面已承载）+机会组从紧（R1 先例） | 短扁口鲶(153) |
| 19 | 名实错位待核（CSV 学名与俗名指向不同类群） | 枯叶鱼(174) |

排除表行级核对：53 合格行 = 类 0 的 36 行中规则合格部分 + 类 1–19 的 33 行中规则合格部分（类 0 内金草鱼/溪鲦等部分行不在四组合格域，类 2 黄尾鲴为规则外行——此三类按承载/登记口径入表不计入 53）。**规则外登记**（267−220=47 行中显式登记过的）：黄尾鲴（K3 R04 成员——R1 排除表）/沙塘鳢（食性空+性格组外+蛰伏名单联动——migration 批登记项 3）；其余规则外行未逐行登记=R1「非 CSV 分组域」口径原样（Story DB 名单到达后处理）。

### 1.5 第一轮名单勘误（本批核对发现，登记不改动 R1 工件）

- R1 候选池名单遗漏 7 行（本批补齐建文件，逐文件 §0 注记）：针牙脂鲤(156)/大西洋牙鲆(157)/鞍带石斑鱼(160)/康氏马鲛(214)/小须美鱥(125)/真鲷(187)/鲻鱼(254)。
- CSV 行名 vs R1 文件名三处名字差（承载关系更正，非新行）：虎纹鳟鱼(77)=R1 tiger_trout；虎纹梭鱼(85)=R1 tiger_musky；红尾鲶鱼(162)=R1 redtail_catfish。

## 2. 表达读数（对模板计数的影响）

- **Group Routing**：72/72＝「无路由程序，默认 Normal Group」显式声明（单一退化形——承 R1 全样本读数）。**L_group 无增长。**
- **Bake**：72 文件全部落在第一轮已定型的 4 个投影标签：**BA-P01-AMBUSH-SINGLE ×11 / BA-P01-PURSUIT-PLAIN ×37 / BA-P01-NOCTURNAL-SINGLE ×9 / BA-P01-OPPORTUNE-SINGLE ×15**。**零新族、零新枚举值**（封闭枚举 7 值不变，本批落值 4 种——BOUNDARY-DECL/SENSE-SINGLE/PLAIN 第一轮已承载成员，本批零新成员）；族边界校验同第一轮（FAMCTX 全族域）。**census 侧 ΔL_bake=0；live 侧零新句型（§11.5 判例原样复用）。**
- **Response**：**R-T1 单通道 ×72**（Feeding；Reaction 槽 OFF；夜行组光照 cue 参数并入 ×9——§11.5 判例原样）。**零 R-T2**：R-T2 结构验证第一轮已由 2 载体（pumpkinseed/striped_bass）完成；本批好斗/撕鳍方向锚行（斑点黑鲈/绿太阳鱼/岩钝鲈/Cichla 三行/蓝鲨/日本鲭/常见鮈鱼）统一 R-T1——**R-T2 在 P01 域的 Story 级成员维持 OPEN**（R1 §3 登记 3 原样，不因批量大而冒充收敛）。**L_response 无增长。**
- **Quality**：72/72=QT-1 绑定表；0 个 W1–W3 物种级表。**L_quality 无增长。**
- **cue 轴**：零消费（本批无电感知/嗅觉 Story 证据成员——@ElectroFieldProfile/@ScentCueProfile 维持第一轮消费计数；鲶系嗅觉/月眼鱼光敏仅 ctx 方向文案，不冒充）。
- **新列结构**：零（全部 live 已声明变体；validate_normal2.py STRUCT/FAMCTX 强制同第一轮）。

## 3. 跨批一致性登记

1. **census 族 ↔ live 句型两层 reconciliation OPEN（承 R1 登记 1）**：本批投影标签为 census 族批投影，非 live 句型晋升；两层等价归机制侧，本批不闭合。
2. **Tier B 归族裁决权移交（承 R1 登记 2，72 文件全量适用）**：全部文件为 CSV 方向锚/点名锚的最低结构表达；Story 正文到达后 census 判同可能改判（换组/换 BakeTemplate/换 Response 拓扑＝结构变更需重审，validator 拦截静默改写）。同属/同科互指（狗鱼系/鲟系/红点鲑系/鮰系/鲽系/太阳鱼系/Cichla/美鱥系/慈鲷系等——逐文件 §0 注记）只是读法一致性，不继承。
3. **R-T2 P01 域成员维持 OPEN（R1 登记 3 原样）**。
4. **全量闭合口径的双边界**：(a) 闭合域=fish-reference-20260908.csv 四组机械规则合格行 220/220——**CSV 口径闭合**；(b) Story DB P01 逐行名单仍不在本地——**Story DB 口径未闭合**（本地可证成员已全部处理，见 §1.2 C 段；R06-R10 逐鱼名单不可证部分登记 §4 登记项 1）。两层口径分立声明，不以 CSV 闭合冒充 Story DB 闭合。
5. **双批分工 ×4 文件**：大西洋鳕鱼（P05 面 migration 批 atlantic_cod.md / P01 面本批 atlantic_cod_feeding.md）、欧洲巨鲶（P04 面 guarding 批 wels_catfish.md / P01 面本批 wels_catfish_feeding.md）、玻璃梭鲈（P05 面 migration 批 walleye_spawn.md / P01 面本批 walleye_feeding.md）、银龙鱼（P01 面本批 silver_arowana.md / P04 边界归 Guarding 系补批对账线）——同种多 Story 多文件先例（白斑狗鱼三文件/鸭嘴鲟两文件/肺鱼双批）第 4-7 例；批间面互斥由文件名后缀 `_feeding` 与 §0 注记双承载。
6. **Cichla 三行不聚合**：金目丽鱼/奥里诺科孔雀鲈/眼点丽鱼按 CSV 三 distinct 行建三文件（同属逐行处理——R1 Pomoxis 两行先例）；guarding 批孔雀鲈 P04 面（Cichla spp. 种级身份待核）互指不继承——种级身份裁决到达若合并，= 结构变更（减文件）需重审。
7. **亚口科张力与点名单行不对称**：白亚口鱼按 handoff 点名建（P01 面），同科水牛鱼/金红马鱼/河红马鱼/黑牛胭脂鱼按 P06 张力排除——不对称源于「点名优先于族级张力登记」的 handoff 指令顺序，非判族结论；grazing 批登记项 1 行级核对到达后四行+白亚口鱼统一重裁（改判=结构变更需重审）。
8. **UsableForageAvailability 契约复用（承 R1 登记 7）**：72 文件 Bake 输入契约行三过滤引用。
9. **口径张力行显式登记（本批新形态）**：CSV 习性列值与物种现实矛盾的行（锦鲤——排除；蓝鲨/大理石倒立鱼/鲻鱼/黄金鲫/茅尖鱼/白亚口鱼/日本鲭——建+张力注记）按「建+登记不冒充」处理；CSV 源表口径修正（AI 审核状态=待人工审核）到达后按 Profile 重绑定或结构变更分轨处理。

## 4. 退回与登记项（转 Coordinator）

| 项 | 内容 |
|---|---|
| 登记项 1（R06-R10 逐鱼名单不可证） | R06「淡水掠食 14+海水掠食 4+鲑系洄游 10」/R07 CB 轴 4 例其余 2 例/R08 蛰伏家族/R10 名实分离三例+待人工 3 条——逐鱼名单均不在本地快照。本批 CSV 220 行闭合已兜底覆盖其合格行部分；**需 Story DB P01 导出（鱼名+Story+relation）做行级核对**（R1 登记项 1 同款请求，第 6 批后再挂） |
| 登记项 2（Story DB 口径未闭合声明） | 本批闭合=CSV 机械规则域闭合（§3 登记 4）；Story DB 名单若含 CSV 规则外行（47 行域外）或与 CSV 习性锚冲突的行，增删文件=表达层动作。不以本批声明 Story DB 全覆盖 |
| 登记项 3（口径张力行清单） | 锦鲤（排除——品系+口径双张力 [需核对]）；白亚口鱼/蓝鲨/大理石倒立鱼/鲻鱼/黄金鲫/茅尖鱼/日本鲭/黑口红点鲑/花鮨/赤梢鱼（建+张力注记 [需核对]——CSV 行值 vs 物种现实）；裁决到达=Profile 层或结构层分轨 |
| 登记项 4（品系/变体 16 行的 L1-EQUIV 层归属） | 类 4 的 16 行（锦鲤系 8 行+鲤系 5 行+罗非/鲫杂交系 3 行）归品系等效层（field 批 L1-EQUIV 先例）——**本体文件不在本批范围**（锦鲤本体行被本批排除——若品系层需要本体，归后续品系补批点名） |
| 登记项 5（scent 轴 P01 成员维持零消费） | 鲶系/鳗系嗅觉方向锚已有 R1 登记；本批鮰系 5 文件同为 ctx 文案不冒充（R1 §3 登记 4 原样） |
| [需正文] 批量项 | 72 文件的猎物构成/因子细节/Response 参数方向（逐文件 §0 已列）；Cichla 攻击性/鞍带石斑鱼伏击-追击倾向/R-T2 好斗锚升级线 |
| 无 UPSTREAM_CHANGE_EVENT | 本批未发现机制侧问题；表达层全部落在既有 census 族/live 结构槽位（G-T1 退化形+BA-T1+DynamicSpatialSlot+R-T1+QT-1）内。名单构造方法修正（无选择步全量裁决）是流程改进不是机制主张 |

## 5. 验证记录（命令与输出原样）

命令（selftest）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2/validate_normal2.py" --selftest
```

命令（真实交付包校验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2/validate_normal2.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2"
```

命令（闭合声明机械复验）：

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2/closure_replay.py"
```

（输出粘贴于下方两块——原样记录，未改测试凑通过。缺陷史：selftest 全绿基线一次通过（校验器为第一轮 validate_normal.py 换批号原样派生，族规则未动）；真实校验一次通过 72/72——首轮即零缺陷（R1 教训 1-13 全部前置规避：生成器 assert 无残留占位符/无畸形 token，伪脚本步序全部模板固定）。闭合复验同版一次 PASS。）

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
[PASS] albacore.md
[PASS] anthias.md
[PASS] arctic_grayling.md
[PASS] atlantic_cod_feeding.md
[PASS] atlantic_sturgeon.md
[PASS] atlantic_tomcod.md
[PASS] biara.md
[PASS] bicuda.md
[PASS] bigeye_tuna.md
[PASS] black_bullhead.md
[PASS] black_piranha.md
[PASS] blackhead_seabream.md
[PASS] blackmouth_char.md
[PASS] blue_catfish.md
[PASS] bull_shark.md
[PASS] bullhead_minnow.md
[PASS] burbot.md
[PASS] butterfly_peacock.md
[PASS] chinese_sleeper.md
[PASS] chub_mackerel.md
[PASS] common_gudgeon.md
[PASS] dogtooth_tuna.md
[PASS] dolly_varden.md
[PASS] european_perch.md
[PASS] flathead_catfish.md
[PASS] giant_grouper.md
[PASS] giant_trevally.md
[PASS] giant_wolffish.md
[PASS] golden_crucian.md
[PASS] grass_puffer.md
[PASS] greater_amberjack.md
[PASS] green_jobfish.md
[PASS] green_sunfish.md
[PASS] grey_mullet.md
[PASS] headstander.md
[PASS] iridescent_shark.md
[PASS] mooneye.md
[PASS] narrowbarred_mackerel.md
[PASS] northern_whiting.md
[PASS] orinoco_peacock.md
[PASS] pacific_bluefin.md
[PASS] payara.md
[PASS] pike_cichlid.md
[PASS] red_drum.md
[PASS] red_seabream.md
[PASS] redfin_pickerel.md
[PASS] redtail_barracuda.md
[PASS] river_chub.md
[PASS] rock_bass.md
[PASS] rock_bream.md
[PASS] sailfish.md
[PASS] serra_mackerel.md
[PASS] sevan_trout.md
[PASS] shortnose_sturgeon.md
[PASS] silver_arowana.md
[PASS] silver_hake.md
[PASS] speckled_peacock.md
[PASS] spotted_bass.md
[PASS] spotted_steed.md
[PASS] stellate_sturgeon.md
[PASS] striped_bonito.md
[PASS] striped_marlin.md
[PASS] summer_flounder.md
[PASS] tench.md
[PASS] walleye_feeding.md
[PASS] wels_catfish_feeding.md
[PASS] white_catfish.md
[PASS] white_sucker.md
[PASS] winter_flounder.md
[PASS] yellowfin_tuna.md
[PASS] yellowtail_amberjack.md
[PASS] yellowtail_flounder.md
== result ==
PASS (72 species files, 0 violations)
```

运行环境：repo venv `programaticHitFish/.venv`（Python 3.14.5）；校验器纯标准库，内部强制 stdout UTF-8。

### 闭合复验输出（closure_replay.py）

```
ambush: total=36 R1=15 N2=11 SIB=4 EXCL=6
pursuit: total=79 R1=20 N2=37 SIB=14 EXCL=8
nocturnal: total=26 R1=11 N2=9 SIB=2 EXCL=4
opportune: total=79 R1=13 N2=15 SIB=16 EXCL=35
grand total eligible rows: 220 (expected 220)
rows out of grouping scope (not adjudicated by CSV rules): 47
unhandled eligible rows: NONE — FULL CLOSURE
species files on disk: 72 (expected 72)
N2 set vs disk mismatch: missing_on_disk=NONE unmapped_files=NONE
== closure replay ==
PASS
```

## 6. 边界声明

- 本包只做 P01 普通离散目标摄食系四面第二轮（全量闭合轮）的生产级表达；表达验证通过 ≠ 机制 promotion ≠ Freeze；不覆盖 live 主页 / census registry 任何 Verdict。
- 全部数值不冻结（@参数引用，Profile 层定值）；SINGLE 链无 combine 步（族域边界）；PLAIN 链 CombineRule OPERATOR UNDEFINED 待机制侧；R-T2 P01 成员、census↔live 两层 reconciliation、scent 轴消费全程 OPEN 可见。
- CSV 口径闭合 ≠ Story DB 口径闭合（§3 登记 4 双边界分立——Story DB 名单核对请求维持 OPEN）。
- 每文件 §5 记录使用/放弃的自由度（含归族裁决权移交、口径张力裁决权移交、喙击打 Encounter/Conversion 边界、Cichla 种级不聚合）。
- 未 commit（提交由 Coordinator / 用户决定）。参数化生成器脚手架 `_gen/` 用后已删除；`closure_replay.py` 为正式工件保留（闭合声明的自证工具，非脚手架）。

BATCH_ID: REP-FULL-NORM2-001

---

## 7. REP-ORDER-FIX-004 顺序还原修复批次记录（2026-09-11，第二批 72 文件）

**依据**：docs/authoring_work_standards.md §5.1 + fcf-representation-worker 章程产出规则第一条（commit 66713d8）+ REP-ORDER-FIX-001/002/003 已定型方法 + 第一批 normal README §7（组级链形设计同批复用）。**修复对象**：本批全部 72 文件的 Bake §2.2 伪脚本 + Response §3.2 DECIDE 占位；就地修改五处+文件尾修复批次行。

### 组级链形（承第一批判型，零新组形）

| 组（文件数） | 顺序还原链 | 组级第一判断 | early return | 分级命中 |
|---|---|---|---|---|
| 伏击 AMBUSH-SINGLE（11） | 门（存在性/定位）→ 掩体结构档位 → 归一化 | 结构掩体（无掩体不伏击） | 门不成立=EARLY_RETURN；暴露档=EARLY_RETURN | 掩体三档 |
| 追击 PURSUIT-PLAIN（37） | 受限还原：每槽三档分档槽判定+COMBINE 维持（census PLAIN unordered/HRQ-07——槽间顺序不主张，改槽序=结构变更需重审） | 猎物场+栖息双槽（vs 伏击掩体先行/机会丰度先行） | 无（槽 excluded=出局槽值进 COMBINE≠EARLY_RETURN——族域边界） | 每槽三档 |
| 夜行 NOCTURNAL-SINGLE（9） | 夜行底板栖息档位 → 低光/夜相槽档位（槽位置=§11.5 判例原位） → 归一化 | 光照+时段+底板 | 无底板=EARLY_RETURN；槽亮水档=极低削减不清零（槽=调整器非 gate） | 底板三档+槽内三档 |
| 机会 OPPORTUNE-SINGLE（15） | （premise 读取——配置级）→ 机会场食物丰度档位 → 归一化 | 食物丰度（跟着食物走） | 枯竭档=EARLY_RETURN | 丰/贫/枯三档 |

本批零 BOUNDARY-DECL/SENSE-SINGLE/PLAIN/R-T2 文件（第一轮已承载）；组间顺序差异与张力登记（夜行槽位置/追击槽间序）见第一批 README §7——两批同判型不重复登记。

### 伏击组每鱼门类型清单（11 文件——两批合计 26 门形）

| 门类型 | 文件 | 门语义（第一判断） |
|---|---|---|
| GATE_ZONE（底层定位 3+表层 1） | white_sucker / stellate_sturgeon / atlantic_sturgeon / shortnose_sturgeon；silver_arowana（表层定位——表层掠食特化） | 底层（或表层）水层定位——非定位水层=出局 |
| GATE_BURYABLE_SUBSTRATE（3） | grass_puffer / northern_whiting / yellowtail_flounder | 可埋沙泥/沙底/软泥底质（掩埋伏击特化——不可埋=出局） |
| GATE_EDGE_COVER（1） | bullhead_minnow | 缓流沙泥/植被缘掩体存在（小型底栖伏击） |
| GATE_REEF_EDGE / RIFFLE_GRAVEL（2） | blackhead_seabream / arctic_grayling | 岩礁沙缘过渡/急流砾石结构存在 |

### Response 面修复（72/72）

DECIDE_RESPONSE 占位全部展开三档分级命中（接受档=全额/边际档=低响应/无响应=出局）；本批零 R-T2，全 R-T1（承批口径）。

### 顺序推导来源分级

本批全部 Tier B+/Tier B（无 census 快照成员——第一轮 Tier A 已全承载）：F1 点名 9/R06 遗留点名 3/R08 点名 5/R08 互指 1=批内互指/点名锚方向级推导（[需正文]）；CSV 行 N 其余 54=CSV 方向锚级推导（[需正文]）——Story 正文到达后校准（结构变更需重审）。

### 分歧登记（UPSTREAM 级——承第一批判型）

顺序还原链与 census SINGLE 族 canonical 两步「无 gate」判语拓扑分歧：census 侧零改动、标签不静默改写；SINGLE 族受影响成员重跑=work standards §5.4 行动项归 census/coordinator（本批 35 个 SINGLE 链形=重跑表达侧输入第二批）。Tier B 归族裁决权移交（§3 登记 2）对顺序链同样适用——Story 正文到达后换组/换链形=结构变更需重审。

### 验证记录（重跑，命令与输出原样）

```
$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2/validate_normal2.py" --selftest
== selftest ==
SELFTEST PASS

$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2/validate_normal2.py" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2"
== result ==
PASS (72 species files, 0 violations)

$ "A:/Projs/FCF-Harness-Handoff/programaticHitFish/.venv/Scripts/python.exe" \
    "A:/Projs/FCF-Harness-Handoff/programaticHitFish/outputs/full_authoring/normal2/closure_replay.py"
== closure replay ==
PASS
```

（72 文件逐 PASS 行与首轮验证记录同形，此处不重复粘贴。）缺陷史：本批修复零缺陷（第一轮 BAN 词撞车的教训 3/7 变体在批前已内化为模板措辞）——首轮即 72/72 全绿，校验器零改动，closure_replay 复验同版 PASS（闭合账不受顺序修复影响）。

顺序还原修复批次：REP-ORDER-FIX-004（第二批 normal2 72 文件；第一批 normal 60 文件见该批 README §7）

---

## REP-FULL-NORM2-REV-001 验收记录（2026-09-11）

- verdict: **ARTIFACT_APPROVE**（reviewer 独立人工全量回放 267 CSV 行确认闭合：220=59+36+72+53 零未处理；19+1 类排除判据封闭无未声明步）。
- F1 修正：README 类 0 名单 2 个非 CSV 行名（金草鱼/溪鲦）漏列 2 个实际 SIB 行（大西洋大海鲢/米达斯慈鲷）——数字巧合掩盖构成差；closure_replay.py 常量闭合账不受影响。
- F2 修正：排除类 2/3/7 中 5 行（鳙鱼/鲱/毛鳞鱼/竹荚鱼/湖白鲑）排除标签沿用 R1 时点——field 批已承载其 P03 面；行级处置正确。
