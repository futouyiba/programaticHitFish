# -*- coding: utf-8 -*-
"""CENSUS-B3 盲程序骨架生成器（盲纪律：registry v4 未开）。

28 条冻结 Story（FISH-R06 洄游/掠食批，FR3 CLOSED AUTO_CONTINUE）。
骨架从冻结 Story 十节正文 + P01/P04/P05 语义 pattern 页（FR 冻结输入）独立推写。
hash: sha256(canonical_json(record minus blind_hash))[:16]
程序构成：Bake 26（PAY/SHO 栖息面 EO 不建体）+ Response 28
  - Response 内含：停食洄游双 Path 2（CHU/SHA，FR3 判例① §9.2 multi-path）
                  P04 guard 双 Path 3（ARA/RBP/WEL）
                  TYPED 标准形 23
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent
P = "https://app.notion.com/p/3d7a4137d23681"
U = {
    "CHU": P + "19a9f5d989bdc45d69", "CHN": P + "1118c8ef343364842cc",
    "COH": P + "1f69852d289431b5b4e", "PIN": P + "1079adade547927f727",
    "BRO": P + "1c4bf59e84d346dfc1f", "SHA": P + "1b69e47fbebf2cc32c8",
    "ALE": P + "1c5aa6ccca76f36194f", "AST": P + "1ec8d9cee1b18f94433",
    "SNS": P + "16d87aed91103e57d08", "TAR": P + "117b633ca9489deba5a",
    "TAI": P + "116b10bd6a57cda0918", "ARA": P + "143bac4e90316a3d30a",
    "PB":  P + "1d689a0cad9c01238f3", "RBP": P + "10aa17cc50b9a8a82e7",
    "BLP": P + "1158d19c15e89293ffe", "WEL": P + "1efb57bfddbb6244c95",
    "FLA": P + "17498bde36dddb7c010", "BUR": P + "1c6a586fed7f45ec901",
    "GW":  P + "169aad0cf9a77ee983f", "PAY": P + "1afa38dff9f6996823a",
    "SGA": P + "19cad80e83f734f570e", "SHO": P + "1ec8becdfb49235454d",
    "RFP": P + "186bcb9c28aaeae987a", "DS":  P + "149a3d2ff515b130aa6",
    "PBF": P + "15ea656c9eba32e0668", "GT":  P + "1528208fa95cfd9445e",
    "HAL": P + "1d181acc21a51b448e4", "GG":  P + "1bc84b4fcbce9ac8c6a",
}
SP = {
    "CHU": "Chum Salmon", "CHN": "Chinook Salmon", "COH": "Coho Salmon",
    "PIN": "Pink Salmon", "BRO": "Brook Trout", "SHA": "American Shad",
    "ALE": "Alewife", "AST": "Atlantic Sturgeon", "SNS": "Shortnose Sturgeon",
    "TAR": "Atlantic Tarpon", "TAI": "Siberian Taimen", "ARA": "Arapaima",
    "PB": "Orinoco Peacock Bass", "RBP": "Red-bellied Piranha",
    "BLP": "Black Piranha", "WEL": "Wels Catfish", "FLA": "Flathead Catfish",
    "BUR": "Burbot", "GW": "Giant Wolf Fish", "PAY": "Payara",
    "SGA": "Spotted Gar", "SHO": "Shoal Bass", "RFP": "Redfin Pickerel",
    "DS": "Dark Sleeper", "PBF": "Pacific Bluefin Tuna", "GT": "Giant Trevally",
    "HAL": "Atlantic Halibut", "GG": "Giant Grouper",
}
S = {k: f"CENSUS-B3-{k}" for k in U}


def rec(pid, story, surface, premises, sketch, steps, branches, combine,
        return_type, profile, confidence=None, open_sem=None):
    r = {"program_id": pid, "story_id": S[story], "species_id": story,
         "surface": surface, "incoming_premises": premises,
         "human_readable_sketch": sketch, "ordered_steps": steps,
         "branches": branches, "combine": combine, "return_type": return_type,
         "instance_noise": {"species": SP[story], "profile": profile,
                            "constants": {}},
         "helpers": [], "source_evidence_ids": [U[story]],
         "open_semantics": open_sem or []}
    if confidence:
        r["confidence"] = confidence
    return r


def bake_single(story, pid_suffix, prem, sketch, op, profile, conf=None, opn=None):
    return rec(f"P-B3-{story}-{pid_suffix}", story, "Bake", prem, sketch,
               [{"op": op, "deps": []}, {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
               [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight", profile,
               confidence=conf, open_sem=opn)


def resp_typed(story, prem, sketch, profile, conf=None, opn=None):
    return rec(f"P-B3-{story}-RESP", story, "Response", prem, sketch,
               [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
                {"op": "DECIDE_RESPONSE", "deps": [0]}],
               [], "NONE", "Response(TargetFeeding)", profile,
               confidence=conf, open_sem=opn)


def resp_guard(story, prem, sketch, anchor_note, profile, conf=None, opn=None):
    """P04 guard 双 Path：守护状态 pre-existing；目标同时可触发摄食 Path 与
    关系冲突 Path（PARALLEL_SET——契约明确同时，无序）；COMBINE 后统一决策。"""
    steps = [
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
        {"op": "EVAL_NEST_INTRUDER_RELATION", "deps": []},
        {"op": "COMBINE_CONFLICT_AWARE", "deps": [0, 1]},
        {"op": "DECIDE_RESPONSE", "deps": [2]},
    ]
    sketch_full = (sketch + "｜anchor=" + anchor_note +
                   "｜Path 结构：摄食 Path ∥ 关系冲突 Path（PARALLEL_SET，P04 契约"
                   "『当前目标可同时触发摄食与关系冲突路径』）→ 冲突感知合并 → 统一响应决策"
                   "（§9.2 one-program-multi-path：不拆两 Mode supply）")
    return rec(f"P-B3-{story}-RESP", story, "Response", prem, sketch_full,
               steps, [], "DUAL_PATH_CONFLICT_AWARE",
               "Response(TargetFeeding | RelationalConflict)", profile,
               confidence=conf, open_sem=opn)


def resp_fasting(story, prem, sketch, profile, opn=None):
    """停食洄游双 Path（FR3 判例①）：停食=P05 状态抑制 Feeding Path；
    洄游期非摄食可钓性=Response 面 multi-path（§9.2）。IF 形状态门。"""
    steps = [
        {"op": "EVAL_MIGRATION_FASTING_STATE", "deps": []},
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": [0]},
        {"op": "EVAL_STRIKE_NON_FEEDING", "deps": [0]},
        {"op": "DECIDE_MULTI_PATH_RESPONSE", "deps": [1, 2]},
    ]
    branches = [{"kind": "IF", "guard": "migration_stage==FASTING_RUN",
                 "else": "OCEAN_FEEDING"}]
    sketch_full = (sketch + "｜Path 结构：海洋期摄食 Path（typed 目标 evaluator）与"
                   "洄游期非摄食攻击 Path（停食下仍可咬钩——动机归因开放，FR3 F-3）由"
                   "洄游停食状态 IF 门互斥切换（P05 状态抑制 Feeding Path；非摄食可钓性"
                   "=Response multi-path，§9.2 one-program-multi-path）")
    return rec(f"P-B3-{story}-RESP-FASTING", story, "Response", prem,
               sketch_full, steps, branches, "STATE_GATED_MULTI_PATH",
               "Response(TargetFeeding | NonFeedingStrike)", profile,
               open_sem=opn)


PROGRAMS = [
    # ============ 洄游系 10 ============
    # CHU 大马哈鱼：溯河停食洄游（判例①源例）
    bake_single("CHU", "BAKE",
        ["migration_stage = OCEAN | ESTUARY | UPSTREAM_RUN（上游 lifecycle；精准归巢）",
         "semelparity = 产后死亡（lifecycle premise）"],
        "海洋期广泛分布 → 溯河迁移 → 精准归巢产卵场：位置因子随洄游阶段 premise 配置"
        "切换（P05 配置级；海期浮游/小鱼食性为海洋期背景）。产卵后死亡不产生空间分支。",
        "EVAL_HABITAT_FACTOR_POSITION", "AnadromousRun"),
    resp_fasting("CHU",
        ["migration_stage = OCEAN | FASTING_RUN（上游 lifecycle fact）",
         "fasting = 溯河期完全停食（P05 状态抑制 Feeding Path——FR3 判例①）"],
        "海洋期：离散猎物（浮游/鱿/小鱼）typed 摄食响应；溯河停食期：停食事实+洄游期"
        "可钓事实 → 咬钩为非摄食攻击响应（『Adults cease feeding in freshwater』逐字核）。",
        "AnadromousFastingRun",
        opn=["strike 动机归因开放（攻击/领地/护巢——FR3 判例①升级三条件之①引文闭合前"
             " NonFeedingStrike Path 语义为最小骨架）"]),
    # CHN 帝王鲑：长距离洄游+生活史多型
    bake_single("CHN", "BAKE",
        ["life_history_type = ocean-type | stream-type | jack（上游 lifecycle）",
         "migration_stage = 海期 | 4827km 溯河（lifecycle premise）"],
        "生活史型分化（ocean/stream/jack）与长距离溯河重排空间：位置因子随生活史型+"
        "洄游阶段 premise 配置切换（P05：阶段差异不并发拆分 Group——B01 大西洋鲑负例同构）。",
        "EVAL_HABITAT_FACTOR_POSITION", "PolymorphicLongRun"),
    resp_typed("CHN", [],
        "海期离散鱼目标 → typed food evaluator（幼期甲壳/昆虫→成期鱼食=个体发生参数）"
        "→ 决定响应。搏鱼表现（aggressive on the hook）为后钩阶段非前链。",
        "OceanPiscivore"),
    # COH 银鲑：猎物升级+洄游
    bake_single("COH", "BAKE",
        ["lifecycle_stage = 淡水 1-2 年 | 海期 | 溯河（上游 lifecycle；夜行降海）"],
        "淡-海-归巢三段位置切换：位置因子随 lifecycle 阶段 premise 配置（P05）。",
        "EVAL_HABITAT_FACTOR_POSITION", "PreyEscalationRun"),
    resp_typed("COH", [],
        "海期猎物升级（浮游甲壳→水母/鱿/鱼）→ typed food evaluator（猎物尺寸/类型为"
        "typed prey context 参数）→ 决定响应。",
        "PreyEscalation"),
    # PIN 粉鲑：两年固定周期+洪水触发
    bake_single("PIN", "BAKE",
        ["cycle_phase = 18 月海期 | 溯河产卵（两年固定周期，上游 lifecycle）",
         "flood_trigger = 洪水触发上溯（世界侧机会窗口 fact；opportunity lifecycle 表达）"],
        "固定两年海-河切换：位置因子随周期阶段 premise 配置；上溯时机由洪水触发"
        "（世界侧机会窗口，非鱼侧程序分支——Story Lowest-Power 明言 opportunity lifecycle）。",
        "EVAL_HABITAT_FACTOR_POSITION", "FixedTwoYearCycle",
        opn=["奇偶年种群隔离的供给语义（若产品需奇偶年并存）——P05 层 open，非本面程序"]),
    resp_typed("PIN", [],
        "离散猎物（浮游→端足/磷虾/鱼随生长升级）→ typed food evaluator → 决定响应；"
        "淡水期可能不摄食（活动 condition premise 非程序分支）。",
        "CycleRunFeeder"),
    # BRO 美洲红点鲑：salter/定居双型
    bake_single("BRO", "BAKE",
        ["life_form = salter | resident（同种双生活史型，上游 lifecycle）",
         "spring_temperature_rise = 春温触发入海（世界侧触发 fact，salter 型）"],
        "salter 型春温入海近河口 ≤3 月 vs 定居型留河：位置因子随 life_form premise "
        "配置切换（P05：同种不同生活史不并发拆分 Group；GroupPressure=Possible 记语义层）。",
        "EVAL_HABITAT_FACTOR_POSITION", "SalterResident",
        opn=["salter 型供给语义（产品若需两型并存）——P05 层 open"]),
    resp_typed("BRO", [],
        "广食（虫/蛭/甲壳/软体/鱼/两栖/小哺乳）→ typed food evaluator（极端广食=类型"
        "参数域宽）→ 决定响应。",
        "Generalist"),
    # SHA 美洲西鲱：溯河停食洄游（判例①重复例）
    bake_single("SHA", "BAKE",
        ["migration_stage = OCEAN | UPSTREAM_RUN（上游 lifecycle；630km 溯河）"],
        "海洋分布 → 630km 溯河产卵段：位置因子随洄游阶段 premise 配置切换（P05）。",
        "EVAL_HABITAT_FACTOR_POSITION", "AnadromousRun"),
    resp_fasting("SHA",
        ["migration_stage = OCEAN | FASTING_RUN（上游 lifecycle fact）",
         "fasting = 溯河产卵洄游期停食（『Feeding ceases during upstream spawning "
         "migration』逐字核；P05 状态抑制 Feeding Path——FR3 判例①）"],
        "海期浮游食性为背景（非垂钓主体）；洄游停食期咬钩为非摄食攻击响应"
        "（停食+洄游可钓两事实推论，与 CHU 跨科独立重复）。",
        "AnadromousFastingRun",
        opn=["strike 动机归因开放（同 CHU，FR3 判例①升级三条件之①）"]),
    # ALE 灰西鲱：双生活史型
    bake_single("ALE", "BAKE",
        ["life_form = anadromous | landlocked（同种双型，上游 lifecycle）"],
        "海型溯河 vs 陆封型留湖：位置因子随 life_form premise 配置切换（P05 阶段语义）。",
        "EVAL_HABITAT_FACTOR_POSITION", "DualLifeHistoryForm"),
    resp_typed("ALE", [],
        "离散猎物（幼浮游硅藻/桡足→成虾/小鱼随鳃耙发育切换）→ typed food evaluator"
        "（个体发生参数）→ 决定响应。非 gamefish 与程序体正交。",
        "OntogeneticShifter"),
    # AST 尖吻鲟：底栖须探+溯河
    bake_single("AST", "BAKE",
        ["migration_stage = 幼河/咸水 2-5 年 | 海期 | 春季上溯（上游 lifecycle；"
         "雌 3-5 年一产）"],
        "底层取向恒定 + 溯河产卵段切换：位置因子随洄游阶段 premise 配置（底层为因子"
        "绑定值，非独立分支——鲟科第三例，小体鲟 R05/闪光鲟 R04 同构）。",
        "EVAL_HABITAT_FACTOR_POSITION", "BarbelBottomRun", conf="MEDIUM"),
    resp_typed("AST", ["benthic_probing = 底栖须探摄食（4 须触底探测，形态事实）"],
        "底栖无脊椎（甲壳/虫/软体）→ typed food evaluator（须探底质 substrate relation "
        "为 typed context）→ 决定响应。",
        "BarbelBenthivore", conf="MEDIUM",
        opn=["游钓供给边界（VU/CITES II）与 snag 边界为产品/捕获面非程序面（S10/S11 注记）"]),
    # SNS 短吻鲟：夜行软底质插食+河口半洄游
    bake_single("SNS", "BAKE",
        ["estuary_phase = 河口/海湾 | 偶入海（上游 lifecycle）"],
        "河口/海湾软底质分布（软底质为栖息因子绑定值）：位置因子随河口阶段 premise "
        "配置（P05）。夜行为活性 condition 非 Bake 分支。",
        "EVAL_HABITAT_FACTOR_POSITION", "EstuarySoftBottom"),
    resp_typed("SNS", ["nocturnal_activity = 夜行主活跃（活性 condition premise）"],
        "夜行软底质插食（幼甲壳/虫→成加软体）→ typed food evaluator（夜行+底质插探 "
        "typed context）→ 决定响应。CITES I 禁捕为捕获边界非程序面（S10/S11 OPS）。",
        "NocturnalProber"),
    # TAR 大海鲢：气呼吸水面掠食+amphidromous
    bake_single("TAR", "BAKE",
        ["amphidromous_stage = leptocephalus 入河口 | 幼体后湾 | 成体沿岸/河口"
         "（上游 lifecycle）"],
        "幼体湾-成体沿岸阶段分布：位置因子随 amphidromous 阶段 premise 配置（P05）；"
        "跨洋扩散（巴拿马运河 80 年）为分布事实非程序分支。",
        "EVAL_HABITAT_FACTOR_POSITION", "AmphidromousCoastal"),
    resp_typed("TAR",
        ["obligate_air_breathing = 专性气呼吸（runtime persistent 条件——低氧耐受优势，"
         "鳃肺形态事实；南美肺鱼 R05 先例：P05+runtime 条件不买 Mode）"],
        "群游小鱼（沙丁/鳀/鲻/鲈形目）→ typed food evaluator（上翘大口水面取向=水面"
        "呈现 typed context）→ 决定响应。跳跃搏鱼=后钩阶段非 FCF 前链（Story 明言）。",
        "SurfaceSchoolingPredator",
        opn=["气呼吸 runtime 条件的呈现面语义（换气周期是否入 opportunity——肺鱼先例未闭合）"]),
    # ============ 淡水掠食 14 ============
    # TAI 哲罗鲑：深潭领域顶级+陆生猎物
    bake_single("TAI", "BAKE",
        ["territorial_deep_pool = 深潭领域 anchor（Static Habitat，home range 23km）",
         "potamromous_spawn_run = 上溯产卵（lifecycle premise，短距）"],
        "成体领域深潭（急流/瀑布下深穴）为静态结构因子：结构因子评估 → 归一化；"
        "上溯产卵为 lifecycle premise（potamodromous，不另立空间分支）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "DeepPoolTerritory",
        opn=["领域供给语义（同潭共存多尾）——Story Open Question，供给密度非程序面"]),
    resp_typed("TAI", [],
        "鱼+陆生脊椎（鼠/鸟落水）→ typed food evaluator（陆生猎物=水面呈现 typed "
        "context，欧鲢 R05 同构）→ 决定响应。mouse pattern 飞钓为玩家策略。",
        "TerrestrialSurfacePredator"),
    # ARA 巨骨舌鱼：洪水周期+气呼吸+巢护（P04 组①）
    bake_single("ARA", "BAKE",
        ["flood_phase = 低水产卵 | 洪泛季幼鱼成长 | 干季孤立湖（上游 lifecycle，"
         "洪水周期）"],
        "洪水周期阶段重排：低水产卵场→洪泛平原→干季湖顶级掠食；位置因子随 flood_phase "
        "premise 配置切换（P05 配置级）。",
        "EVAL_HABITAT_FACTOR_POSITION", "FloodPulseCycle",
        opn=["换气暴露（distinctive gulp 有噪声水面周期）=可预测水面机会——opportunity "
             "lifecycle 表达，呈现侧契约未闭合（TAR 判同注记同源）"]),
    resp_guard("ARA",
        ["guard_state = ACTIVE（沙巢筑成+护卵护幼，Presentation 前存在且持续——P04）",
         "air_breathing_surface_cycle = 专性气呼吸换气（runtime 条件 premise）"],
        "杂食掠食（鱼/甲壳/果/虫/岸边小兽）typed 摄食 Path；守护状态下目标接近巢/幼"
        "同时触发关系冲突 Path。",
        "沙巢（约 15cm 深 50cm 宽）+ 卵/幼鱼",
        "FloodPulseGuarder",
        opn=["护幼（guards the young）与护卵的 relation 对象差异——参数级，guard 状态"
             "单 premise 承载；FR3 P04 抽验三问转 Cross-Batch（三问框架）"]),
    # PB 孔雀鲈：浅渊追猎
    bake_single("PB", "BAKE",
        ["lagoon_habitat = 浅水近岸渊湾/缓流河段（Static Habitat）"],
        "浅水渊湾结构因子（静态）→ 归一化权重。繁殖面 FishBase 无描述（EO）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "ShallowLagoon", conf="MEDIUM"),
    resp_typed("PB", [],
        "小型 characiform 鱼食 → typed food evaluator（浅水追猎 typed context）→ "
        "决定响应。Cichla 双亲护巢常识未核验不写（EO——Story 明言）。",
        "PursuitPiscivore", conf="MEDIUM",
        opn=["繁殖/护巢面 EO：若未来证实双亲护巢则 P04 第三组样本候选（FR 线已记 open）"]),
    # RBP 红腹食人鱼：frenzy 校正+树根护卵（P04 组②）
    bake_single("RBP", "BAKE",
        ["vegetated_habitat = 植被区（Static Habitat）"],
        "植被区结构因子（静态）→ 归一化权重；群游=防御性集聚（遇鱼分布背景，非互斥 "
        "Group 程序——Wikipedia 无证据形态否定协作捕猎，FR3 判例② Negative note）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "VegetatedPool"),
    resp_guard("RBP",
        ["guard_state = ACTIVE（树根护卵，Presentation 前存在且持续——P04）",
         "size_phase_temporal_partition = 体型分级时段（大鱼黄昏/夜、小鱼日间）——"
         "condition premise 非程序分支"],
        "黄昏/夜时段离散猎物（虫/蠕虫/鱼+腐食机会性）typed 摄食 Path；守护状态下目标"
        "接近树根卵团触发关系冲突 Path。听觉（highly evolved auditory）=呈现面感官"
        "线索（typed context 参数）。",
        "树根卵团（eggs laid on tree roots and guarded）",
        "RootGuardFeeder",
        opn=["交替换牙连续进食（S2）为形态能力事实非程序步；群游防御为 Negative "
             "Knowledge（不得以 frenzy 购 Group Mode——FR3 判例②）"]),
    # BLP 黑食人鱼：急流胆怯机会性
    bake_single("BLP", "BAKE",
        ["rapids_deep_habitat = 急流区+主河深水区（Static Habitat）"],
        "急流/深水结构因子（静态）→ 归一化权重。繁殖面无描述（EO）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "RapidsDeepZone", conf="MEDIUM"),
    resp_typed("BLP", [],
        "机会性肉食（小鱼/蟹/哺乳/蜥蜴/甲虫）→ typed food evaluator（胆怯机会性="
        "入口条件参数；与 RBP frenzy 传说双否定群体捕猎语义）→ 决定响应。",
        "TimidOpportunist", conf="MEDIUM"),
    # WEL 欧洲巨鲶：洞穴夜行+雄巢守护（P04 组③）
    bake_single("WEL", "BAKE",
        ["hole_ambush_habitat = 河床洞穴/沉木遮蔽（Static Habitat，日藏）"],
        "洞穴/沉木结构因子（静态遮蔽，夜行近底/水柱觅食）→ 归一化权重。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "HoleAmbush"),
    resp_guard("WEL",
        ["guard_state = ACTIVE（雄鱼筑巢守护至幼虫孵出，Presentation 前存在且持续——P04）",
         "nocturnal_activity = 夜行主活跃（condition premise）",
         "hearing_smell_dominant = 听嗅主导狩猎（感官 typed context——黄颡鱼 R03 低光触须同构）"],
        "夜行底栖/水柱离散猎物（幼无脊→成鱼/水生脊椎；引入地鼠/鸭+beaching 捕鸽=水面"
        "呈现 typed context，哲罗鲑同构）typed 摄食 Path；守护状态下目标接近雄巢触发"
        "关系冲突 Path。",
        "雄巢（males guard the nests until larvae emerge）",
        "HoleAmbushNestGuard",
        opn=["beaching 捕鸽的呈现语义（水面攻击边界）——呈现面 open"]),
    # FLA 铲鮰：倒木潭底栖
    bake_single("FLA", "BAKE",
        ["log_pool_habitat = 倒木/碎屑潭（Static Habitat）"],
        "倒木潭结构因子（静态）→ 归一化权重。夜行/伏击行为面 FishBase 未述（EO 不写）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "LogPoolBenthic", conf="MEDIUM"),
    resp_typed("FLA", ["ontogeny = 幼虫栖 insect→成螯虾/贝/鱼（个体发生 premise）"],
        "底栖离散猎物 → typed food evaluator（底质结构 typed context；云斑鮰 R02/"
        "WELS 本批同构）→ 决定响应。",
        "BenthicPiscivore", conf="MEDIUM"),
    # BUR 江鳕：夏深冬活动重排
    bake_single("BUR", "BAKE",
        ["season_phase = 夏季深水 | 冬季活动（季节绑定，上游 condition）"],
        "夏深冬活动季节重排：位置因子随季节 premise 绑定切换（B2 ARC 冷水季节位移"
        "同构形态）；岩缝/树根为冬季活动期结构绑定值。",
        "EVAL_HABITAT_FACTOR_POSITION", "WinterActiveReorder"),
    resp_typed("BUR", ["crepuscular_nocturnal = 黄昏夜行（condition premise）"],
        "底栖离散猎物（小个体虫幼/螯虾/软体→大个体鱼）→ typed food evaluator（颏须"
        "底探+低光 typed context）→ 决定响应。冬夜产卵球=繁殖集群非摄食群（不买 "
        "Group——Story 明言）。",
        "CrepuscularBenthic"),
    # GW 巨狼鱼：逆流黄昏伏击
    bake_single("GW", "BAKE",
        ["counter_current_habitat = 干流/溪流逆流区（Static Habitat）"],
        "逆流区结构因子（静态）→ 归一化权重。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "CounterCurrentAmbush", conf="MEDIUM"),
    resp_typed("GW", ["dusk_night_activity = 黄昏夜行（condition premise）"],
        "鱼+落水陆生无脊椎 → typed food evaluator（逆流结构+黄昏夜+水面呈现 typed "
        "context——哲罗鲑同构）→ 决定响应。无气呼吸记载（对照 ARA/TAR/SGA）。",
        "CounterCurrentPredator", conf="MEDIUM"),
    # PAY 巴亚拉：獠牙鱼食（栖息 EO，Bake 不建体）
    resp_typed("PAY", [],
        "獠牙鱼食（『probably ichthyophagous』形态事实推断）→ typed food evaluator"
        "（獠牙犬齿=猎物类型参数）→ 决定响应。栖息/洄游/繁殖面全 EO（Story 明言）。",
        "FangToothIchthyophage", conf="MEDIUM"),
    # SGA 斑点雀鳝：洄湾伏击+兼性气呼吸
    bake_single("SGA", "BAKE",
        ["backwater_habitat = 静水澄清洄湾/牛轭湖/沼泽（Static Habitat）"],
        "静水洄湾结构因子（静态）→ 归一化权重。鳄雀鳝 B01 同构。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "BackwaterAmbush"),
    resp_typed("SGA",
        ["facultative_air_breathing = 兼性气呼吸（runtime 条件 premise，非专性）"],
        "广食 voracious（鱼/甲壳）→ typed food evaluator（静水结构 typed context）→ "
        "决定定响应。",
        "BackwaterVoracious"),
    # SHO 浅滩鲈：同属默认（栖息 EO，Bake 不建体）
    resp_typed("SHO", [],
        "同属黑鲈掠食同构（斑点黑鲈 R04 P01 先例；属内 2/4 有 Story 不构成全属先例——"
        "Story 明言）→ typed food evaluator → 决定响应。河流湍流区常识栖息未引源不写。",
        "CongenericDefault", conf="MEDIUM"),
    # RFP 红鳍狗鱼：植被静水小鱼伏击
    bake_single("RFP", "BAKE",
        ["vegetated_pool_habitat = 植被缓静水池/湖/湿地（Static Habitat）"],
        "植被静水结构因子（静态）→ 归一化权重。狗鱼属 4/4 同构（白斑 B01/北美 R04/"
        "链纹 R04/本例）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "VegetatedPool", conf="MEDIUM"),
    resp_typed("RFP", [],
        "小鱼离散猎物 → typed food evaluator（植被静水 typed context）→ 决定响应。"
        "散卵不护（guard neither eggs nor young）——狗鱼属无 guard 语义对照",
        "VegetatedAmbusher", conf="MEDIUM"),
    # DS 沙塘鳢：底栖小型伏击
    bake_single("DS", "BAKE",
        ["benthic_habitat = 终生淡水+孵化即底栖（Static Habitat）"],
        "底栖结构因子（静态，孵化即底栖）→ 归一化权重。食性/繁殖无描述（EO）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "BenthicSleeper", conf="MEDIUM"),
    resp_typed("DS", [],
        "底栖小型伏击（同科笋壳鱼 R05 P01 先例；trophic 3.2 同科推算）→ typed food "
        "evaluator（底栖 typed context）→ 决定响应。",
        "BenthicSmallAmbush", conf="MEDIUM"),
    # ============ 海水掠食 4 ============
    # PBF 蓝鳍：温血跨洋洄游
    bake_single("PBF", "BAKE",
        ["migration_phase = 跨太平洋东西岸 | 季节近岸（上游 lifecycle；幼-成分布差异）",
         "endothermy = 温血（retia mirabilia 逆流热交换，体温可高水温 20°C——"
         "runtime 热生理能力 fact，非空间程序分支）"],
        "跨太平洋洄游+季节近岸：位置因子随洄游阶段 premise 配置切换（P05）；温血扩展"
        "温度耐受域与泳速=环境/能力变量（大眼金枪鱼 R04 runtime overlay 同构注记）。",
        "EVAL_HABITAT_FACTOR_POSITION", "EndothermicMigrator"),
    resp_typed("PBF", [],
        "群游小鱼/鱿（兼蟹）→ typed food evaluator（上层洋区+群游猎物 typed context；"
        "温血=热生理 typed fact 不构成行为程序包——FR3 §7 admission 击穿点全不成立）"
        "→ 决定响应。",
        "SchoolingEpipelagic",
        opn=["热生理在呈现面的具体意义（Story Open Question——呈现侧 open）"]),
    # GT 牛港鲹：夜间礁缘
    bake_single("GT", "BAKE",
        ["life_stage_habitat = 幼鱼河口 | 成鱼礁外沙岩/泻湖（上游 lifecycle）"],
        "幼河口-成礁外阶段分布：位置因子随 life_stage premise 配置切换（P05）。",
        "EVAL_HABITAT_FACTOR_POSITION", "ReefEdgeStage"),
    resp_typed("GT", [],
        "夜间离散猎物（甲壳：蟹/龙虾+鱼）→ typed food evaluator（夜间低光+礁沙岩结构 "
        "typed context——R03 教训不买 Night Mode）→ 决定响应。ciguatoxic=人类侧食物"
        "安全 Capture Boundary（S11，非程序面）。",
        "NocturnalReefEdge"),
    # HAL 大比目鱼：深冬底栖
    bake_single("HAL", "BAKE",
        ["season_spawn_depth = 常规 50-2000m 底栖 | 12-4 月 300-700m 深海产卵"
         "（季节绑定，上游 condition/lifecycle）"],
        "深海底栖+冬季深海产卵重排：深度因子随季节/产卵阶段 premise 绑定切换。",
        "EVAL_HABITAT_FACTOR_POSITION", "DeepWinterDemersal"),
    resp_typed("HAL", [],
        "底栖离散猎物（鳕/黑线鳕/玉筋鱼/鲱/毛鳞鱼+头足+大甲壳）→ typed food evaluator"
        "（深度+底质 typed context；伏击行为面 EO 未写）→ 决定响应。",
        "DemersalPiscivore"),
    # GG 鞍带石斑：礁洞沉船顶级
    bake_single("GG", "BAKE",
        ["cave_wreck_habitat = 礁洞/沉船结构（Static Habitat；幼鱼礁内隐蔽）"],
        "礁洞/沉船结构因子（静态）→ 归一化权重。产卵聚集面 FishBase 仅链接无描述（EO）。",
        "EVAL_HABITAT_FACTOR_STRUCTURE", "CaveWreckApex"),
    resp_typed("GG", [],
        "广食顶级（龙虾/鱼/小鲨/鳐/幼海龟/甲壳）→ typed food evaluator（礁洞结构 "
        "typed context——石斑类先例同构）→ 决定响应。ciguatoxic=Capture Boundary"
        "（S11，非程序面）。",
        "CaveAmbushApex"),
]


def blind_hash(record):
    body = {k: v for k, v in record.items() if k != "blind_hash"}
    return hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True)
                          .encode("utf-8")).hexdigest()[:16]


def main():
    out = BATCH_DIR / "blind_programs.jsonl"
    lines = []
    for p in PROGRAMS:
        p["registry_seen"] = False
        p["registry_seen_at_creation"] = False
        p["blind_hash"] = blind_hash(p)
        lines.append(json.dumps(p, ensure_ascii=False))
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    n_bake = sum(1 for p in PROGRAMS if p["surface"] == "Bake")
    n_resp = sum(1 for p in PROGRAMS if p["surface"] == "Response")
    print(f"frozen {len(PROGRAMS)} blind programs (Bake={n_bake} Response={n_resp})"
          f" -> {out}")
    for p in PROGRAMS:
        print(f"  {p['program_id']}: {p['blind_hash']}")


if __name__ == "__main__":
    main()
