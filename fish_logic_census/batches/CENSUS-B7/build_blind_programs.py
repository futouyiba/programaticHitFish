# -*- coding: utf-8 -*-
"""CENSUS-B7 盲程序骨架生成器（盲纪律：template_registry.yaml 未开——程序体冻结前不读 registry 本体）。

112 条冻结 Story（census 基线收尾批：R01 残余 38 + R02 残余 17 + R03 残余 24 +
R04 全 23 + R05 残余 10；全部 FR3-passed——R01/R02/R03/R04/R05 packet +
FR3 packet 快照见 input_snapshots/）。骨架从各 Story 正文（十节完整形，R04 为
英文压缩十节）独立推写；语义输入=各 story 正文 FCF Interpretation 节的比较
pattern（P01/P02/P03/P04/P05/P06/B01/B02 语义随 story 冻结文本承载）。
hash: sha256(canonical_json(record minus blind_hash))[:16]

【B7-F-0 类偏差注记（bias_declaration 同文）】本会话盲段加载流程管线时读过 B6
的 build_blind_programs.py / build_stories.py / run_merge_tests.py /
build_census_outputs.py（B6 94 盲体的 SINGLE 链与 TYPED/guard 形态 op 名层面
——B7 脚本管线直接沿用其骨架）与 B6 batch_report/manifest（族名与计数散文）；
角色记忆 v5 亦含各族散文描述与 B0-B6/RS1/RP1 判例。template_registry.yaml
本体（v8）在盲冻结前未读。缓解：本批 219 条 sketch 严格从 112 份 Story 正文
+ story 内冻结 FCF Interpretation 独立推写，每条含顺序推导注记；guard 6 例
按 P04 契约拓扑（PARALLEL_SET 依据=B3 pattern 快照契约文本）非按 registry
形状；field Response（滤食/连续场）按 story 正文行为描述（场评估单步+决策）
推写，不参照任何 registry 族形；未按 registry 形状定制。

【盲体语汇纪律（B5 F4 判例，强制执行）】盲 sketch/premise/open_semantics
只描述观察到的行为结构——不携带 extension/新轴/anchor 轴值提案等判同段框架
语汇（判同提案只出现在判同产物 merge_tests/HRQ）。守护对象以行为事实描述
（『雄鱼守巢并照护幼鱼至离巢』），不预写轴名。

【顺序推导纪律（authoring_work_standards §5.1）】112 Story 逐条顺序扫描结论：
- 无一 Story 正文描述面内 early-return 判断链（分级命中 if/elif/else 型）；
  策略层的『先找位置再选呈现』（如 S01 玻璃梭鲈先改水层再选 jig/浮漂）是
  Bake→Response 的面间顺序，不是单一面内 branch 链。
- 出现的先后序均为 lifecycle/洄游/昼夜/ontogeny/繁殖期——S48 七鳃鳗三阶段
  （幼体埋栖滤食→寄生→生殖停食）、S13/S25 定居-海行生态型、S09/S54 产卵
  迁移窗、AEL1/笋壳鱼/六须鲶 夜行、S03/S08/S106 幼成食谱切换、守巢期
  （S31/S38/S41/S43/乌鳢/云斑鮰/鳑鲏）——按 B3 判例④记 premise 配置级
  position 绑定，不是面内 ordered branch。
- S15/S51（求偶竞争）story FR 层明言『P04 守巢不自动覆盖 courtship』——
  繁殖竞争语境记 premise+open_semantics，不立面内双 Path。
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent
SNAP = BATCH_DIR / "input_snapshots"

# ---- story 文件映射（fetch_pairs.tsv 行号）+ URL ----
PAIRS = {}
for ln in (SNAP / "fetch_pairs.tsv").read_text(encoding="utf-8").splitlines():
    fid, url, title = ln.split("\t")
    PAIRS[int(fid[6:])] = (url, title)


def U(code):
    return CODE2NUM[code] and PAIRS[CODE2NUM[code]][0]


def TITLE(code):
    return PAIRS[CODE2NUM[code]][1]


ORDER_NOTE = "顺序推导注记"

# ---- 形态表 ----
# kind: T=typed, G=guard, F=field, B=bake-only, N=zero-program
# (code, kind, species_en, profile, premises, sketch_resp, sketch_bake, conf, open_sem)
# sketches 下放正文压缩语义；premises 为 incoming_premises。

R01 = [
    ("WAL2", "T", "Walleye Low-Light", "WalleyeLowlightTyped",
     ["light_context = 晨昏浅区/低光遮蔽/浑水可摄食（视觉适应 Context，非夜行 Mode）"],
     "低光/遮蔽/浑水语境下的离散饵评估与响应（视觉适应=Context）。",
     "低光与遮蔽因子下的位置权重（白天深水/结构、晨昏浅区）。", None, None),
    ("CRA1", "T", "Black Crappie Ontogeny", "CrappieOntogenyTyped",
     ["ontogeny = 幼体浮游→较大个体食鱼（体型/阶段 Context）"],
     "体型/阶段语境下的离散饵评估（幼浮游-成鱼食性为阶段配置）。",
     "清水/植被/结构因子位置权重。", None, None),
    ("CRA2", "G", "Black Crappie Nest Guard", "CrappieNestGuard",
     ["guard_state = 繁殖期雄鱼筑巢护卵至孵化（本种证据）"],
     "守巢雄鱼的目标评估：食物意义与巢防御意义并存候选。",
     "巢区/植被结构位置权重。", "Semantic Open（story：对玩家饵的冲突路径尚待行为证据）",
     ["冲突路径行为证据待验证（story FR 层 Semantic Open）"]),
    ("GAR1", "T", "Alligator Gar Slow Take", "GarSlowTakeTyped",
     ["prey_type = 鱼类猎物；take_style = 取饵缓慢谨慎（初始接受与挂钩不同事件）"],
     "缓慢取饵语境下的离散鱼饵评估与接受。",
     "缓流/植被水域位置权重。", None, None),
    ("GAR3", "T", "Alligator Gar Flood Spawn", "GarFloodSpawnTyped",
     ["lifecycle = 温度+淹水浅滩通达触发的繁殖入口（年度成功不连续）"],
     "普通捕食响应（繁殖入口为 lifecycle premise 配置）。",
     "淹水浅滩/植被通达季节位置权重。", None, None),
    ("YEP1", "T", "Yellow Perch Size Diet", "PerchOntogenyTyped",
     ["ontogeny = 浮游→底栖无脊椎/鱼（吞整只猎物）"],
     "体型阶段语境下的小饵离散评估。",
     "植被/掩体/水层匹配位置权重。", None, None),
    ("YEP2", "T", "Yellow Perch Spawn Run", "PerchSpawnTyped",
     ["lifecycle = 适底质/植被产卵（胶状卵带）+水域入口调查限定"],
     "普通摄食响应（产卵迁移为 lifecycle premise）。",
     "产卵底质/植被水域位置权重。", None, None),
    ("BIB1", "T", "Bigmouth Buffalo Filter", "BuffaloFilterTyped",
     ["field_channel = 滤取浮游食物（typed FoodField evaluator 候选——行为证据链未闭合）"],
     "浮游资源场语境的评估（滤食机会输入，钩线捕获罕见）。",
     "开放水体/浮游资源位置权重。", None,
     ["滤食行为因果链未闭合（密度/动作/连续机会）——story Evidence Open"]),
    ("BIB2", "T", "Bigmouth Buffalo Flood Spawn", "BuffaloFloodTyped",
     ["lifecycle = 温度+水位上升进入浅水沼泽繁殖（卵无人照护）"],
     "普通滤食/摄食响应（水位繁殖为 premise）。",
     "浅水沼泽季节通达位置权重。", None, None),
    ("BRT3", "T", "Brown Trout Residency", "BrownTroutEcotypeTyped",
     ["lifecycle = 定居淡水/海行生态型共存（同河共存繁殖）"],
     "普通离散摄食响应（生态型为 lifecycle premise）。",
     "定居河段/河口-海区分野位置权重。", None, None),
    ("BRT4", "T", "Brown Trout Courtship", "BrownTroutCourtshipTyped",
     ["reproduction = 繁殖期雌鱼选择与雄鱼支配竞争（配对结果改变）"],
     "普通摄食响应（求偶竞争为繁殖 Condition premise，非守巢）。",
     "繁殖河段位置权重。", None,
     ["求偶/对手关系与摄食的冲突路径无 Nest guard 前提（story：P04 仅竞争参照）"]),
    ("RED1", "T", "Red Drum Tailing Patch", "RedDrumPatchTyped",
     ["resource_patch = 底栖甲壳/小鱼斑块（尾露=觅食痕迹非攻击信号）"],
     "底质斑块语境下的虾/蟹模仿离散评估。",
     "浅水草区/底质斑块位置权重。", None, None),
    ("RED2", "T", "Red Drum Tide Habitat", "RedDrumTideTyped",
     ["lifecycle = 幼鱼海湾/成鱼外海；runtime = 潮位温度改变日内水深"],
     "普通离散摄食响应（潮位/鱼龄为 premise）。",
     "湾区/浅滩/深水潮位位置权重。", None, None),
    ("PIK1", "T", "Northern Pike Ambush", "PikeAmbushTyped",
     ["habitat = 植被边缘伏击；approach = 从下方接近（视觉伏击，夜间少咬）"],
     "植被边缘仿鱼饵/伤鱼呈现的离散评估。",
     "植被边缘/结构遮蔽位置权重。", None, None),
    ("MUL1", "T", "Mullet Substrate Processing", "MulletSubstrateTyped",
     ["substrate = 底泥/附着物/水气界面颗粒捕获与吐出（圈养观察区分动作）"],
     "基质层位颗粒呈现的离散评估（连续处理动作与离散钩饵分开）。",
     "底质层位/基质位置权重。", None,
     ["连续基质处理压缩候选（story FR 层 P06→P02 压缩候选，未闭合）"]),
    ("MUL2", "T", "Mullet Ocean Spawning", "MulletOceanSpawnTyped",
     ["lifecycle = 成鱼成群外海繁殖、幼体近岸河口生长（空间分离）"],
     "普通摄食响应（繁殖迁移为 premise）。",
     "近岸生长区/外海分离位置权重。", None, None),
    ("RAI2", "T", "Rainbow Trout Drift Pulse", "TroutDriftTyped",
     ["food_pulse = 鲑卵/尸体来源季节脉冲（自然漂流呈现）"],
     "漂流卵/肉模仿物的离散评估（流速与食物类型为 Context）。",
     "水层/配重近底位置权重。", None, None),
    ("RAI3", "T", "Rainbow Trout Steelhead", "TroutEcotypeTyped",
     ["lifecycle = 定居虹鳟/海行钢头鳟同种生活史（可重复繁殖）"],
     "普通离散摄食响应（生态型为 premise）。",
     "湖泊/返河时序分野位置权重。", None, None),
    ("AEL1", "T", "American Eel Nocturnal", "EelNocturnalTyped",
     ["diel = 白天隐蔽/夜间摄食（昼夜 Context 非夜行 Mode）"],
     "昼夜窗口语境下的甲壳/虫/蠕虫/鱼离散评估。",
     "植物/倒木隐蔽结构位置权重。", None, None),
    ("AEL2", "T", "American Eel Catadromy", "EelMigrationTyped",
     ["lifecycle = 海洋幼体→沿岸淡水生长→返 Sargasso 繁殖（连通性影响通达）"],
     "普通离散摄食响应（降海洄游为 premise）。",
     "生长区/迁移通达分野位置权重。", None, None),
    ("SOK1", "T", "Sockeye Plankton Filter", "SockeyeFilterTyped",
     ["field_channel = 浮游摄食鳃耙证据（阶段不确定——幼鱼食谱/海行/kokanee 不互替）"],
     "浮游资源语境的评估（阶段条件保留，滤食动作切换未闭合）。",
     "湖海浮游层位置权重。", None,
     ["filter/particulate 动作切换证据未闭合（story Evidence Open）"]),
    ("SOK2", "T", "Sockeye Run Motivation", "SockeyeRunTyped",
     ["lifecycle = 返河繁殖；capture_motivation = 未定（摄食/冲突/线接触不可辨）"],
     "普通评估响应占位（捕获动机未定——story Semantic Open）。",
     "返河河段/季节位置权重。", "Semantic Open（捕获动机未定）",
     ["返河个体的捕获归属未定（主动响应 vs 线接触——story FR 层 B02/P05 均未接受）"]),
    ("SAL1", "T", "Atlantic Salmon Run", "SalmonRunTyped",
     ["lifecycle = 淡水生长/海洋摄食阶段食物不同；返河摄食非绝对零（支流样本分歧）"],
     "普通离散摄食响应（返河阶段为 premise，无绝对关断）。",
     "河海阶段分野位置权重。", None, None),
    ("SMA1", "G", "Smallmouth Bass Nest Guard", "SmbNestGuard",
     ["guard_state = 繁殖雄鱼守巢护幼（饱食处理与防御行为下降相关，补食降弃巢）"],
     "守巢雄鱼的目标评估：食物意义与防御意义并行候选。",
     "巢区/近岸硬底位置权重。", None, None),
    ("PAD1", "T", "Paddlefish Filter Boundary", "PaddlefishFilterTyped",
     ["field_channel = 滤食与颗粒选择输入（圈养 filter/particulate 无固定切换规律）"],
     "浮游场语境的评估（滤食输入边界，snagging 另列）。",
     "开放水体/浮游层位置权重。", None,
     ["滤食能力不当作咬钩证据（snagging 捕获另列边界 story）"]),
    ("PAD5", "T", "Paddlefish Upstream Spawn", "PaddlefishSpawnTyped",
     ["lifecycle = 开放水体生长/繁殖季上移产卵地（觅食与通达分开）"],
     "普通滤食评估响应（上溯繁殖为 premise）。",
     "开放水体/上游产卵通达位置权重。", None, None),
    ("BLU2", "G", "Bluegill Nest Guard Forage", "BluegillNestGuard",
     ["guard_state = 护巢雄鱼存在替代繁殖策略；filial_cannibalism = 食卵受亲子状态影响"],
     "巢区小饵的评估：摄食与防御攻击两种意义（钓获不可单独识别原因）。",
     "巢区/浅水硬底位置权重。", None,
     ["父本食卵非『外部食物+守护』并发的证明（story 竞争解释）"]),
    ("CCF1", "T", "Channel Catfish Chemo-Tactile", "CatfishSensorTyped",
     ["sensory = 味/嗅/触觉寻找（气味扩散=sensory Context）；ontogeny = 成幼食谱水层昼夜不同"],
     "气味线索语境下的多样食物离散评估。",
     "底层/昼夜水层位置权重。", None, None),
    ("CCF2", "G", "Channel Catfish Cave Guard", "CatfishCaveGuard",
     ["guard_state = 雄鱼洞巢照护卵幼（受扰时可食卵）"],
     "洞巢雄鱼的目标评估：照护与食卵/防御意义候选。",
     "洞巢/底质结构位置权重。", "Semantic Open（story：照护→lure-defense 映射无可靠证据）",
     ["洞巢照护译为防御策略的证据缺失（story FR 层 Semantic Open）"]),
    ("TIL2", "T", "Nile Tilagus Resuspend", "TilapiaSubstrateTyped",
     ["substrate = 刮食+黏液截留+再悬浮动作（动作存在≠切换条件闭合）"],
     "颗粒尺度/位置语境的离散评估（环境颗粒变化与响应分 owner）。",
     "植被/缓水基质位置权重。", None,
     ["五种摄食动作不构成五个模式（story：刮食可尝试压缩未证失败）"]),
    ("TIL3", "G", "Nile Tilapia Territory", "TilapiaTerritory",
     ["territory = 雄鱼繁殖领地（雌鱼取卵离巢口孵——领地与幼体非同一关系对象）"],
     "领地雄鱼的目标评估：食物与驱逐意义候选（领地≠护卵）。",
     "繁殖领地/浅水位置权重。", "Semantic Open（story：P04 仅竞争参照，先区分领地与护卵）",
     ["雄性驱逐行为到玩家假饵的映射无直接证据（story FR 层）"]),
    ("BDR2", "T", "Black Drum Tactile Benthos", "BlackDrumBenthosTyped",
     ["sensory = 触须找底栖猎物（咽齿处理）"],
     "底栖无脊椎离散评估（触须搜寻=sensory Context）。",
     "底质/湾底位置权重。", None, None),
    ("SEA2", "T", "Sea Lamprey Stage Switch", "LampreyStageTyped",
     ["lifecycle = 幼体埋栖滤食→变态寄生→成体繁殖消化退化停食（分阶段）"],
     "幼体场输入语境的评估占位（阶段条件保留；寄生交实例化后 owner）。",
     "细沉积低坡幼体栖位/阶段通达位置权重。", None,
     ["分阶段资源/栖位差异（幼体 field input 与实例化后寄生分别交适当 owner——story）"]),
    ("COD1", "T", "Atlantic Cod Discrete", "CodDiscreteTyped",
     ["prey_type = 鱼类+无脊椎；habitat = 体型/栖位影响食谱"],
     "多样猎物离散评估（底层环境为 Context）。",
     "底层/栖位位置权重。", None, None),
    ("COD2", "T", "Atlantic Cod Courtship Sound", "CodSoundTyped",
     ["reproduction = 发声与求偶/竞争联系（圈养）；sound ≠ 万能进食/产卵指标"],
     "普通离散摄食响应（发声求偶为繁殖 Condition premise）。",
     "繁殖场/底层位置权重。", None,
     ["P04 守巢不自动覆盖 courtship（story FR 层 Semantic Open）"]),
    ("GRA2", "T", "Grass Carp Flowing Spawn", "GrassCarpSpawnTyped",
     ["lifecycle = 流动水+水位变化产卵；fasting_hint = 临产亲鱼减少/停止进食（养殖语境限定）"],
     "普通植食离散评估（繁殖通达与亲鱼停食为 premise 限定）。",
     "河流通达/流水位位置权重。", None, None),
]

R02 = [
    ("MAC1", "F", "Atlantic Mackerel Moving Field", "MackerelField",
     ["field = 季节性沿陆架移动的浮游/饵鱼资源场（群体=找鱼线索非供给模式）"],
     "移动饵场/水层语境的场评估响应（FieldFeeding）。",
     "陆架移动饵场/水层位置权重。", None, None),
    ("JCK1", "F", "Jack Mackerel Nearshore", "JackMackerelField",
     ["field = 近岸浮游/饵鱼场（水温潮流改变分布）"],
     "潮流/礁缘/水层语境的场评估响应（FieldFeeding）。",
     "近岸潮流层位置权重。", None, None),
    ("CAP1", "F", "Capelin Spawning Window", "CapelinField",
     ["field = 浮游+小型底栖资源场；lifecycle = 繁殖季近岸/岸滩聚集（短窗口）"],
     "近岸窗口场评估响应（FieldFeeding；繁殖聚集为 premise）。",
     "近岸滩/潮位时间窗位置权重。", None, None),
    ("LWF1", "T", "Lake Whitefish Identity-Blocked", "WhitefishBenthicTyped",
     ["identity = 学名串种风险隔离（Coverage 行 Blocked by Identity；story 保留 Evidence Open）"],
     "底栖资源离散评估（身份隔离语境，机制按记录面推算承载）。",
     "湖底/近底季节深浅位置权重。", "Medium（identity-blocked 推算）", None),
    ("SIL1", "F", "Silver Carp Filter Field", "SilverCarpField",
     ["field = 水柱浮游/悬浮有机物滤食场；boundary = 特殊接触捕获走 Capture Boundary（非摄食证明）"],
     "分布式食物场评估响应（FieldFeeding；跳跃等偶发非模式）。",
     "水柱浮游层位置权重。", None,
     ["非目标接触捕获=边界 owner 处理（story：滤食不证明咬钩）"]),
    ("CAR1", "T", "Common Carp Substrate Turbulence", "CarpSubstrateTyped",
     ["substrate = 底泥翻拱摄食（浑水/气泡/扰动痕迹=搜索线索）"],
     "底质翻拱区离散饵评估（翻拱痕迹为机会背景）。",
     "底质/预投饵区位置权重。", None, None),
    ("TEN1", "T", "Tench Weed Edge", "TenchWeedgeTyped",
     ["habitat = 静水植被边缘软底；season = 暖季活动明显"],
     "植被边缘底层离散评估。",
     "植被边缘/软底位置权重。", None, None),
    ("DIS2", "G", "White Discus Brood Care", "DiscusBroodGuard",
     ["guard_state = 亲鱼护幼（幼鱼体表黏液摄食）；color_morph = 白色型（与橙型同语义，色型不分裂）"],
     "护幼亲鱼的目标评估：接近/干扰的意义评估（黏液喂养关系）。",
     "静水植被/缓流位置权重。", "Low（色型复用推算）", None),
    ("BON1", "F", "Striped Bonito Pelagic Chase", "BonitoField",
     ["field = 移动小鱼/头足类资源场（高速追猎型）"],
     "移动饵群/流线水层场评估响应（FieldFeeding+下游离散目标）。",
     "开放水层/流线位置权重。", None, None),
    ("SBS1", "T", "S. sinensis Flow Window", "SinensisFlowTyped",
     ["habitat = 河流溪流关联（急缓流交界/砾砂底/深潭边缘候选）；eo = 流速-底质-季节链未闭合"],
     "底层离散评估（流速窗口=候选 Context，Evidence Open）。",
     "急缓流交界/砾砂底位置权重。", "Medium（Evidence Open 推算）", None),
    ("CSN1", "G", "Snakehead Brood Guard", "SnakeheadBroodGuard",
     ["guard_state = 繁殖期亲鱼守护卵和幼鱼（伏击型捕食者双语境）"],
     "护幼期目标评估：饵料选择与幼鱼团防御并存（非繁殖期纯伏击摄食）。",
     "植被/浅水结构位置权重。", None, None),
    ("BBR1", "G", "Brown Bullhead Nest Guard", "BullheadNestGuard",
     ["diel = 低光/夜间嗅觉触须取食；guard_state = 巢穴照护卵幼"],
     "巢区接近的评估：底层气味摄食与防御/干扰意义并存。",
     "底层/巢穴结构位置权重。", None, None),
    ("RST1", "T", "Russian Sturgeon Anadromy", "RussianSturgeonTyped",
     ["lifecycle = 河海洄游繁殖回河；protection = 捕获合法性/保护=Boundary"],
     "底层软体/甲壳/小鱼离散评估（洄游为 premise）。",
     "底层通道/迁移入口位置权重。", None,
     ["保护限制为产品边界（story：非机制语义）"]),
    ("SBH1", "T", "S. hollandi Mountain Stream", "HollandiSubstrateTyped",
     ["habitat = 山溪底质关联（流速/底质/深潭候选）；eo = 底层摄食-流速-底质链未闭合"],
     "底层离散评估（刮食/杂食斑块候选，Evidence Open）。",
     "山溪底质/深潭位置权重。", "Medium（Evidence Open 推算）", None),
    ("BSH1", "T", "Bull Shark Euryhaline", "BullSharkEuryhalineTyped",
     ["salinity = 强广盐性海/河口/淡水通道；prey = 机会性捕食"],
     "离散猎物评估（盐度梯度通达为 premise）。",
     "河口通道/盐度梯度位置权重。", None, None),
    ("WCF1", "T", "Wels Catfish Night Benthic", "WelsNightTyped",
     ["diel = 夜间底层捕食（深槽/缓流/遮蔽）"],
     "大体型离散目标/气味评估（昼夜窗口为 premise）。",
     "深槽/回水/浑水位置权重。", None, None),
    ("SZE1", "T", "Sauger Turbid Lowlight", "SaugerTurbidTyped",
     ["habitat = 大河浑水/沙砾底/低光窗口（晨昏夜间）"],
     "贴底/近底离散评估（浑水低光为 Context）。",
     "河道结构/浑水边界位置权重。", None, None),
]

R03 = [
    ("RTL", "T", "Red Tilapia Hybrid", "RedTilapiaHybridTyped",
     ["strain = 杂交/选育标签（亲本/投喂史/驯化改变表现——品系身份限定）"],
     "温水杂食离散评估（资源机会低强度承载）。",
     "温暖淡水/底质植物位置权重。", "Low（杂交标签推算）", None),
    ("LNK", "T", "Sharp-snouted Lenok", "LenokColdwaterTyped",
     ["habitat = 冷水河流急流/深潭；lifecycle = 季节性上溯（Evidence Open）"],
     "冷水移动/漂流离散目标评估。",
     "急流深潭/季节上溯位置权重。", None, None),
    ("TPC", "T", "Topmouth Culter", "CulterPelagicTyped",
     ["habitat = 河湖中上层；runtime = 水位流速季节重排（群聚=发现层线索）"],
     "中上层移动离散目标评估。",
     "中上层/流速变化位置权重。", None, None),
    ("SPS", "T", "Spotted Steed", "SpottedSteedTyped",
     ["habitat = 河流底层砾石/砂底（流速边界+底质遮蔽）"],
     "底层小型无脊椎离散评估。",
     "底质/河段结构位置权重。", None, None),
    ("WRC", "T", "Wuyuan Red Carp", "WuyuanStrainTyped",
     ["strain = 地方鲤品系（红表型不购买独立机制）"],
     "鲤类底层杂食离散评估（品系继承承载）。",
     "底层/底质资源位置权重。", "Low（品系推算）", None),
    ("MRF", "T", "Mongolian Redfin", "RedfinPelagicTyped",
     ["habitat = 河湖中上层离散猎物（群聚=发现层压力）"],
     "中上层移动猎物离散评估。",
     "水层/流速位置权重。", None, None),
    ("IRS", "T", "Iridescent Shark", "IridescentSharkTyped",
     ["lifecycle = 洄游/繁殖空间变化（洪水季节相关）；size = 体型阶段食物谱"],
     "河流杂食离散评估（迁移为相邻 lifecycle 证据）。",
     "河段/水位季节位置权重。", None, None),
    ("BRC", "T", "Barbel Chub", "BarbelChubTyped",
     ["habitat = 河湖流速/底质/季节食物供应（机会条件）"],
     "流速底质语境离散评估。",
     "流速/底质位置权重。", None, None),
    ("WCR2", "T", "Wild Crucian Carp", "WildCrucianTyped",
     ["identity = 与观赏金鱼/养殖鲫保持边界（品系驯化差异 Evidence Open）"],
     "浅水底层杂食离散评估（野生基线承载）。",
     "浅水/底质资源位置权重。", None, None),
    ("KOI", "T", "Koi", "KoiStrainTyped",
     ["strain = 观赏鲤品系（机制继承普通鲤；投喂史不外推）"],
     "鲤类底层杂食离散评估（品系继承承载）。",
     "底层/底质资源位置权重。", "Low（品系推算）", None),
    ("MIR", "T", "Mirror Carp", "MirrorStrainTyped",
     ["strain = 鳞被表型品系（外观差异不购买独立机制）"],
     "鲤类底层杂食离散评估（品系继承承载）。",
     "底层/底质资源位置权重。", "Low（品系推算）", None),
    ("CLC", "T", "Chinese Longsnout Catfish", "LongsnoutCatfishTyped",
     ["habitat = 河流底层；sensory = 触须/低光/夜间待验证 Context"],
     "底层机会性离散评估（夜触须为待验证 Context）。",
     "底层/遮蔽位置权重。", None, None),
    ("HMB", "T", "Humpback Culter", "HumpbackTyped",
     ["habitat = 河湖中上层小型猎物（近缘资料不外推）"],
     "中上层小型猎物离散评估。",
     "近岸结构/水层位置权重。", None, None),
    ("BKC", "T", "Black Carp Mollusc Patch", "BlackCarpMolluscTyped",
     ["resource = 螺/蛤硬壳资源 Patch（重要资源层）；lifecycle = 季节迁移注记"],
     "硬壳无脊椎离散评估（碾压处理=typed context）。",
     "硬壳资源集中/底质水流位置权重。", None, None),
    ("ASC2", "T", "African Sharptooth Catfish", "ClariasTyped",
     ["habitat = 低氧/洪泛边缘/泥底（辅助空气呼吸=现实边界）；lifecycle = 洪泛迁移繁殖"],
     "资源场+离散目标机会评估（体型食谱随阶段）。",
     "低氧/洪泛边缘/泥底位置权重。", None, None),
    ("CHS", "T", "Chinese Hook Snout Carp", "HooksnoutTyped",
     ["habitat = 浅水流速边界/遮蔽（溪流鱼不自动=快流模式）"],
     "浅水小型猎物离散评估。",
     "浅水/流速边界位置权重。", None, None),
    ("RSB", "G", "Rosy Bitterling Mussel Brood", "BitterlingMusselGuard",
     ["relation = 卵产入活淡水蚌鳃腔、胚胎贝内发育（繁殖外部关系对象）；reproduction = 繁殖期配偶竞争"],
     "贝宿主存在语境的评估：繁殖机会依赖活蚌（产卵管行为）。",
     "河湖缓流/蚌栖息底质位置权重。", None,
     ["关系对象为活蚌（非巢/穴附着型载体）；普通摄食不属于本 story 语义"]),
    ("LJB", "T", "Long-jawed Baelama", "BaelamaTyped",
     ["habitat = 大河中上层（身份可核、行为字段稀疏——Evidence Open）"],
     "水层小型猎物离散评估（低强度承载）。",
     "河流水层位置权重。", "Medium（薄资料推算）", None),
    ("MDC2", "F", "Mud Carp Field", "MudCarpField",
     ["field = 藻类/附着生物/有机碎屑连续资源场（缓流环境）"],
     "连续底质资源场评估响应（FieldFeeding）。",
     "缓流/附着资源底质位置权重。", None, None),
    ("YCK", "T", "Yellowcheek", "YellowcheekTyped",
     ["habitat = 中上层移动猎物/流速季节水位（追猎强度证据开放）"],
     "移动离散目标评估。",
     "水层/流速边界位置权重。", None, None),
    ("STM", "T", "Stone Moroko", "MorokoTyped",
     ["habitat = 浅水缓流植被边缘；prey = 小无脊椎/鱼卵/幼体（入侵扩散=资源场非模式）"],
     "浅水小目标离散评估。",
     "植被边缘/小型水体位置权重。", None, None),
    ("XCD", "F", "Xenocypris Davidi Field", "DavidiField",
     ["field = 底质附着资源连续场（食物组成/季节边界稀疏）"],
     "连续附着资源场评估响应（FieldFeeding）。",
     "附着资源/底质位置权重。", "Medium（薄资料推算）", None),
    ("GCR", "T", "Golden Crucian", "GoldenStrainTyped",
     ["strain = 杂交/选育鲫标签（身份不稳定）"],
     "鲫鱼基线杂食离散评估（品系继承承载）。",
     "浅水/底质资源位置权重。", "Low（杂交标签推算）", None),
    ("YCF", "T", "Yellow Catfish", "YellowCatfishTyped",
     ["habitat = 底层河湖通道/巢穴石缝（守巢另列独立候选不在本链）"],
     "底层昆虫/软体/鱼离散评估。",
     "底层/石缝结构位置权重。", None,
     ["守巢为独立 Relation/Guard 候选（story：不在本普通摄食 story 响应链内）"]),
]

R04 = [
    ("FGA4", "T", "Florida Gar (R04)", "FloridaGarR04Typed",
     ["habitat = 浅植被/缓水伏击道（与 R02-S17 同种跨批双 story——内容近似）"],
     "伏击道离散仿鱼目标评估。",
     "植被边缘/静水位置权重。", None, None),
    ("MUS", "T", "Muskellunge", "MuskellungeTyped",
     ["habitat = 大型猎物/掩体边缘（target-size/presentation context）"],
     "大目标型离散评估（掩体边缘穿越打击道）。",
     "掩体边缘位置权重。", None, None),
    ("SIH", "T", "Silver Hake", "SilverHakeTyped",
     ["habitat = 大陆架中底水层；lifecycle = 深度季节重排"],
     "活动深度带离散饵评估。",
     "大陆架深度带位置权重。", None, None),
    ("BET", "T", "Bigeye Tuna", "BigeyeTyped",
     ["habitat = 深度昼夜移动大洋；runtime = 温度/深度/饵痕"],
     "活动层离散目标评估（移动机会=控制问题）。",
     "温深层/饵痕位置权重。", None, None),
    ("BWF", "T", "Bowfin", "BowfinTyped",
     ["habitat = 植被静水/结构（无通用夜间规则）"],
     "植被结构离散动物型目标评估（停顿呈现）。",
     "掩体边缘/低流结构位置权重。", None, None),
    ("SB2", "T", "Spotted Bass", "SpottedBassTyped",
     ["habitat = 水流/岩石/掩体（接近目标机会为主变量）"],
     "流缝/岩石掩体离散移动或停顿目标评估。",
     "流缝/岩石位置权重。", None, None),
    ("WCR3", "T", "White Crappie", "WhiteCrappieTyped",
     ["habitat = 淹没结构+季节深度变化（schooling=Context 信号）"],
     "结构/活动深度带小型离散目标评估。",
     "结构/深度带位置权重。", None, None),
    ("CTT", "T", "Cutthroat Trout", "CutthroatTyped",
     ["lifecycle = 定居/洄游型；habitat = 冷水流漂流道"],
     "漂流道小型离散目标评估（匹配当前食场）。",
     "冷水流/漂流道位置权重。", None, None),
    ("RSB2", "T", "Red Seabream", "RedSeabreamTyped",
     ["resource = 礁底/硬底猎物斑块"],
     "礁缘斑块离散饵评估（近摄食层）。",
     "硬底/礁缘位置权重。", None, None),
    ("BSN", "T", "Bullseye Snakehead", "BullseyeTyped",
     ["habitat = 密植被/低氧胁迫区（空气呼吸改变栖息持续性非摄食通道）"],
     "植被伏击道离散目标评估。",
     "密植被边缘/浅水机会区位置权重。", None, None),
    ("RTB", "T", "Red Tail Barracuda", "BarracudaTyped",
     ["habitat = 河道/开放水清可见移动目标"],
     "清水饵道可见移动离散目标评估。",
     "流缘/清水道位置权重。", None, None),
    ("RHM2", "T", "Redhook Myleus", "RedhookTyped",
     ["resource = 洪泛植物/果实斑块（item-level feeding 非连续放牧）"],
     "资源边缘离散果实型目标评估。",
     "洪泛资源边缘位置权重。", None, None),
    ("STB", "T", "Striped Bass", "StripedBassTyped",
     ["lifecycle = 河口海岸河川间移动；runtime = 流/温/饵集中"],
     "活动深度离散目标评估（迁移改变机会暴露）。",
     "流温/饵集中深度位置权重。", None, None),
    ("DVK", "T", "Dolly Varden", "DollyVardenTyped",
     ["lifecycle = 定居/溯河型；habitat = 冷水系食场漂流"],
     "活动道离散目标评估（形态先变 Context）。",
     "冷水通道/漂流位置权重。", None, None),
    ("GJC", "T", "Green Jobfish", "JobfishTyped",
     ["resource = 礁缘流隔饵集中（schooling prey）"],
     "流隔结构离散目标评估（饵集中处）。",
     "流隔/礁缘位置权重。", None, None),
    ("WBL", "B", "Western Brook Lamprey", "WesternLampreyBake",
     ["lifecycle = 幼体埋栖滤食/成体非寄生；boundary = 不强并入 Target/Field 直到 product scope 显式"],
     None,
     "细沉积物/低坡度栖息+迁移通达位置权重（lifecycle/state story）。", None,
     ["Response 无程序：boundary-only/Product Scope Deferred（story FR 层 Semantic Open）"]),
    ("CPT", "T", "Chain Pickerel", "PickerelTyped",
     ["habitat = 植被边缘（控制停顿的离散猎物目标）"],
     "植被边缘离散仿鱼目标评估（打击道通达为主决策）。",
     "植被边缘位置权重。", None, None),
    ("BIC", "T", "Bicuda", "BicudaTyped",
     ["habitat = 河道边缘/移动水道"],
     "河道边缘离散小猎物目标评估。",
     "河道边缘/流水道位置权重。", None, None),
    ("SS2", "T", "Stellate Sturgeon", "StellateTyped",
     ["resource = 底质气味猎物斑块；lifecycle = 海河洄游"],
     "近底离散饵评估（栖息选择后目标层）。",
     "迁移通达/底质斑块位置权重。", None, None),
    ("TNS", "T", "Tennessee Shiner", "ShinerTyped",
     ["eo = 物种级公开证据稀疏（研究线索非玩家面向事实）"],
     "浅流小目标离散评估占位（低信心）。",
     "浅流栖息位置权重。", "Low（稀疏证据占位）", None),
    ("MAH", "T", "Mahi-Mahi", "MahiTyped",
     ["resource = 漂浮结构+饵鱼集中（瞬态斑块）"],
     "活动层快速离散目标评估（结构暴露机会）。",
     "漂浮结构/饵集中位置权重。", None, None),
    ("YTA", "T", "Yellowtail Amberjack", "YellowtailTyped",
     ["resource = 流隔饵鱼聚集；runtime = 流改变暴露与深度"],
     "移动打击道离散目标评估。",
     "流隔/饵聚集位置权重。", None, None),
    ("BBF", "T", "Black Buffalo", "BlackBuffaloTyped",
     ["resource = 软底/流过渡带底栖物质（季节河川移动改变通达）"],
     "摄食层离散饵评估（资源 Context 改变暴露）。",
     "软底/流过渡带位置权重。", None, None),
]

R05 = [
    ("ROH", "F", "Rohu Monsoon Grazing", "RohuField",
     ["field = 季风洪泛河段植物资源场；lifecycle = 季风产卵窗"],
     "植物基底层场评估响应（连续基质处理候选）。",
     "季风洪泛窗河道中游位置权重。", None, None),
    ("MRC", "F", "Mrigal Column-Bottom", "MrigalField",
     ["field = 底中食物场（拾取 vs 滤机制未闭合）"],
     "底中场评估响应（机制开放留给证据闭合）。",
     "底中层位置权重。", None,
     ["拾取 vs 滤食机制未闭合（story：不从浮游食性推导滤食）"]),
    ("SPR", "F", "Streaked Prochilod Illiophagy", "ProchilodField",
     ["field = 有机泥层连续资源场（illiophagous 口特化吸食）；lifecycle = 800-1000km 洄游"],
     "底栖腐屑场评估响应（连续基质处理候选）。",
     "洄游窗聚集/腐屑场位置权重。", None, None),
    ("CHM", "F", "Chiselmouth Diatom Plate", "ChiselmouthField",
     ["field = 附着藻层（下颌硬板刮食）；ontogeny = 幼水面昆虫→成藻食"],
     "附着藻层场评估响应（刮食候选）。",
     "砂砾底池-急流位置权重。", None, None),
    ("SHB", "F", "Sharpbelly Upper Field", "SharpbellyField",
     ["field = 上层悬浮/漂流物场（浮游/虫/藻/腐屑）"],
     "上层场评估响应（虫类拾取含次级离散目标）。",
     "大溪流/水库上层位置权重。", None, None),
    ("GTB", "F", "Giant Barb Floodplain Window", "GiantBarbField",
     ["field = 洪泛季果实/藻/腐屑窗（季节性斑块）；lifecycle = 幼成栖息分异（沼泽支流/大河深潭）"],
     "洪泛果实窗场评估响应（连续处理候选）。",
     "洪泛林/阶段栖息分野位置权重。", None, None),
    ("STL", "T", "Sterlet Barbel Tactile", "SterletTactileTyped",
     ["sensory = 吻下四长须底栖触觉搜寻；lifecycle = 冬穴聚集/春溯砾石滩"],
     "底栖触须搜寻离散目标评估（patch 背景兼容）。",
     "大河深水/冬穴-春滩位置权重。", None,
     ["触须用途行为学未闭合（形态证实，S2=EO）"]),
    ("WCB", "F", "Wuchang Bream Grazing", "WuchangField",
     ["field = 沉水草床连续资源场（选择性放牧控草）"],
     "沉水草床场评估响应（连续基质处理候选；钩饵仍可离散目标）。",
     "湖泊 5-20m 草床位置权重。", None, None),
    ("MRG", "T", "Marble Goby Nocturnal Ambush", "MarbleGobyTyped",
     ["diel = 夜行伏击/日藏石草；habitat = 深软沙掘穴半埋（穴=持续结构占用）"],
     "夜间结构伏击离散目标评估（小鱼虾/螺蟹）。",
     "深软沙/穴掩体位置权重。", None, None),
    ("IDE", "T", "Ide Ontogenetic Piscivory", "IdeOntogenyTyped",
     ["ontogeny = 幼沿岸→成深水鱼食（Large individuals feed mainly on fishes）；lifecycle = 支流产卵洄游"],
     "成体深水鱼食离散评估（阶段差异为 premise）。",
     "沿岸→深水/支流位置权重。", None, None),
]

# 零程序 story（Response 无 FCF 程序 + Bake 无空间主张）
ZERO_PROGRAM = [
    ("PAD4", "B01-S36 鸭嘴鲟锚挂",
     "Response=B02 捕获边界（story：Contact/capture owner 不依赖主动响应路径，"
     "FCF feeding 不添加新 Channel）；Bake 无空间主张（捕获方式 story，栖息面"
     "由同鱼 S33/S37 story 承载）——0 程序 story，顶层 no_surface_reason。"),
    ("SEA1", "B01-S47 七鳃鳗附着寄生",
     "Response=实例化后关系 owner（story：持续 attachment 交实例化后关系 owner，"
     "前链最多负责宿主相关机会——post-instantiation 边界）；Bake 无空间主张"
     "（寄生行为 story 无栖息因子）——0 程序 story，顶层 no_surface_reason。"),
]

CODE2NUM = {}
_num = 0
for code, kind, sp, profile, prem, sk_r, sk_b, conf, opn in (R01 + R02 + R03 + R04 + R05):
    _num += 1
    CODE2NUM[code] = _num
# R01 表少了 2 个零程序条目占位：R01 有 38 story，其中 S36/S47 零程序——
# 上表 36 条对应 fetch 行 1-38 中除 26(S36)/34(S47) 外的顺序需要校准。
# 重新按 fetch_pairs 行号精确映射：
_CODE_ORDER = [c for c, *_ in (R01 + R02 + R03 + R04 + R05)]
# fetch_pairs: 1-38=R01（26=S36→零, 34=S47→零）, 39-55=R02, 56-79=R03,
# 80-102=R04, 103-112=R05
_r01_codes = [c for c, *_ in R01]
_slot = [n for n in range(1, 39) if n not in (26, 34)]
CODE2NUM = dict(zip(_r01_codes, _slot))
_off = 38
for seg in (R02, R03, R04, R05):
    for c, *_ in seg:
        _off += 1
        CODE2NUM[c] = _off


def rec(pid, story_code, surface, premises, sketch, steps, branches, combine,
        return_type, profile, confidence=None, open_sem=None):
    r = {"program_id": pid, "story_id": f"CENSUS-B7-{story_code}",
         "species_id": story_code, "surface": surface,
         "incoming_premises": premises,
         "human_readable_sketch": sketch, "ordered_steps": steps,
         "branches": branches, "combine": combine, "return_type": return_type,
         "instance_noise": {"species": None, "profile": profile,
                            "constants": {}},
         "helpers": [], "source_evidence_ids": [U(story_code)],
         "open_semantics": open_sem or []}
    if confidence:
        r["confidence"] = confidence
    return r


def bake_single(code, prem, sketch, profile):
    return rec(f"P-B7-{code}-BAKE", code, "Bake", prem,
               sketch + "｜" + ORDER_NOTE + "：Story 正文无面内判断链（时序为"
               "lifecycle/昼夜/阶段 premise 配置级），单因子链。",
               [{"op": "EVAL_HABITAT_FACTOR_POSITION", "deps": []},
                {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
               [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight", profile)


def resp_typed(code, prem, sketch, profile, conf=None, opn=None):
    return rec(f"P-B7-{code}-RESP", code, "Response", prem,
               sketch + "｜" + ORDER_NOTE + "：单评估步无分支（繁殖/昼夜/阶段"
               "语境为 premise）。",
               [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
                {"op": "DECIDE_RESPONSE", "deps": [0]}],
               [], "NONE", "Response(TargetFeeding)", profile,
               confidence=conf, open_sem=opn)


def resp_guard(code, prem, guard_note, profile, conf=None, opn=None):
    """P04 guard 双 Path：守护状态 pre-existing/persistent（契约）；
    目标同时可触发摄食 Path 与关系冲突 Path（PARALLEL_SET——契约明确同时，
    无序）；COMBINE 后统一决策。守护对象以行为事实记 premise+
    open_semantics；不预写判同段框架语汇（盲体语汇纪律）。"""
    steps = [
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
        {"op": "EVAL_NEST_INTRUDER_RELATION", "deps": []},
        {"op": "COMBINE_CONFLICT_AWARE", "deps": [0, 1]},
        {"op": "DECIDE_RESPONSE", "deps": [2]},
    ]
    sketch_full = (guard_note + "｜守护面=" + prem[0] +
                   "｜Path 结构：摄食 Path ∥ 关系冲突 Path（PARALLEL_SET，"
                   "P04 契约『当前目标可同时触发摄食与关系冲突路径』）→ 冲突"
                   "感知合并 → 统一响应决策（§9.2 one-program-multi-path：不拆"
                   "两 Mode supply）｜" + ORDER_NOTE + "：守护状态先存持续，"
                   "非面内时序分支。")
    return rec(f"P-B7-{code}-RESP", code, "Response", prem, sketch_full,
               steps, [], "DUAL_PATH_CONFLICT_AWARE",
               "Response(TargetFeeding | RelationalConflict)", profile,
               confidence=conf, open_sem=opn)


def resp_field(code, prem, sketch, profile, conf=None, opn=None):
    """P03/P06 场评估响应：story 行为=评估分布式食物场并响应（单场评估步+
    决策——场与离散目标共享响应结构）。"""
    return rec(f"P-B7-{code}-RESP", code, "Response", prem,
               sketch + "｜" + ORDER_NOTE + "：场评估单步无分支（资源场连续"
               "机会，无面内判断链）。",
               [{"op": "EVAL_FIELD_AS_FOOD_TYPED", "deps": []},
                {"op": "DECIDE_RESPONSE", "deps": [0]}],
               [], "NONE", "Response(FieldFeeding)", profile,
               confidence=conf, open_sem=opn)


PROGRAMS = []
for code, kind, sp, profile, prem, sk_r, sk_b, conf, opn in R01:
    PROGRAMS.append(bake_single(code, prem, sk_b, profile))
    if kind == "T":
        PROGRAMS.append(resp_typed(code, prem, sk_r, profile, conf, opn))
    elif kind == "G":
        PROGRAMS.append(resp_guard(code, prem, sk_r, profile, conf, opn))
    elif kind == "F":
        PROGRAMS.append(resp_field(code, prem, sk_r, profile, conf, opn))
for code, kind, sp, profile, prem, sk_r, sk_b, conf, opn in (R02 + R03):
    PROGRAMS.append(bake_single(code, prem, sk_b, profile))
    if kind == "T":
        PROGRAMS.append(resp_typed(code, prem, sk_r, profile, conf, opn))
    elif kind == "G":
        PROGRAMS.append(resp_guard(code, prem, sk_r, profile, conf, opn))
    elif kind == "F":
        PROGRAMS.append(resp_field(code, prem, sk_r, profile, conf, opn))
for code, kind, sp, profile, prem, sk_r, sk_b, conf, opn in R04:
    PROGRAMS.append(bake_single(code, prem, sk_b, profile))
    if kind == "T":
        PROGRAMS.append(resp_typed(code, prem, sk_r, profile, conf, opn))
    elif kind == "G":
        PROGRAMS.append(resp_guard(code, prem, sk_r, profile, conf, opn))
    elif kind == "F":
        PROGRAMS.append(resp_field(code, prem, sk_r, profile, conf, opn))
    # kind B（WBL）：仅 bake，无 Response 程序
for code, kind, sp, profile, prem, sk_r, sk_b, conf, opn in R05:
    PROGRAMS.append(bake_single(code, prem, sk_b, profile))
    if kind == "T":
        PROGRAMS.append(resp_typed(code, prem, sk_r, profile, conf, opn))
    elif kind == "G":
        PROGRAMS.append(resp_guard(code, prem, sk_r, profile, conf, opn))
    elif kind == "F":
        PROGRAMS.append(resp_field(code, prem, sk_r, profile, conf, opn))

# instance_noise.species 回填（表内英文种名）
SP_MAP = {c: sp for c, kind, sp, *_ in (R01 + R02 + R03 + R04 + R05)}
for p in PROGRAMS:
    p["instance_noise"]["species"] = SP_MAP[p["species_id"]]


def blind_hash(rec_dict):
    core = {k: v for k, v in rec_dict.items() if k != "blind_hash"}
    s = json.dumps(core, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":"))
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def main():
    out = BATCH_DIR / "blind_programs.jsonl"
    lines = []
    for p in PROGRAMS:
        p["registry_seen_at_creation"] = False
        p["blind_hash"] = blind_hash(p)
        lines.append(json.dumps(p, ensure_ascii=False))
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    n_resp_t = sum(1 for p in PROGRAMS if p["program_id"].endswith("-RESP")
                   and p["combine"] == "NONE"
                   and p["return_type"] == "Response(TargetFeeding)")
    n_resp_g = sum(1 for p in PROGRAMS if "RelationalConflict" in p["return_type"])
    n_resp_f = sum(1 for p in PROGRAMS if "FieldFeeding" in p["return_type"])
    n_bake = sum(1 for p in PROGRAMS if p["surface"] == "Bake")
    print(f"blind programs: {len(PROGRAMS)} "
          f"(bake={n_bake} typed={n_resp_t} guard={n_resp_g} field={n_resp_f})")
    # sanity: 每个 code 的 URL/title 可回查
    assert len(CODE2NUM) == len(R01) + len(R02) + len(R03) + len(R04) + len(R05)
    print("stories covered:", len(CODE2NUM), "+ zero-program:", len(ZERO_PROGRAM))
    assert len(CODE2NUM) + len(ZERO_PROGRAM) == 112


if __name__ == "__main__":
    main()
