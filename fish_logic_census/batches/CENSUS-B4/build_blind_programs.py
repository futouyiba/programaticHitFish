# -*- coding: utf-8 -*-
"""CENSUS-B4 盲程序骨架生成器（盲纪律：registry v5 未开——程序体冻结前不读 registry 本体）。

26 条冻结 Story（FISH-R07 边界层批：鲨鳐魟电感知系/头足类边界/河鲀 CB/潮汐窗/
鲽鲆形态对照/亚口科磿螺系，FR3 CLOSED）。骨架从冻结 Story 十节正文 + P01/P04/P05
语义 pattern 页（B3 input_snapshots 快照，FR 冻结输入）独立推写。
hash: sha256(canonical_json(record minus blind_hash))[:16]

【B4-F-0 类偏差注记】加载流程管线时读过 B3 的 run_merge_tests.py——其中内嵌
registry v4 canonical IR 指针（CRR/SINGLE/TYPED/GUARD 的 op 名层面）。角色记忆 v3
已含这些族的散文描述与 B3 判例；本批 sketch 仍严格从 Story 十节正文独立推写，
未按 registry 形状定制（见 manifest bias_declaration）。

【顺序推导纪律（用户反馈 2026-09-11，authoring_work_standards §5.1）】
每个骨架显式记录顺序推导结果。本批 26 Story 的顺序扫描结论：
- 无一 Story 正文描述面内 early-return 判断链（分级命中型）；
- 出现的先后序均为 lifecycle/季节/潮汐时序（POR 海洋→南下产仔→归巢；ASR 河口
  →沿河上溯；GDE 春上溯/秋下行；CBM 冬深水不活跃；SAI 春岸/冬深；GPF 潮汐窗
  上岸产卵→返水）——按 B3 判例④（已审范式）记为 premise 配置级 position 绑定，
  不是面内 ordered branch；
- HNC 唯一例外：guard 的 intruder evaluation 携带物种型谓词（仅同种雄性触发防御）
  ——typed evaluator 变化，按 P04 契约拓扑（并行双 Path）保留，species-typing
  记入 open_semantics + premise（顺序/谓词差异本身留作判据，判同阶段裁决）。
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent
P = "https://app.notion.com/p/3d7a4137d23681"
U = {
    "POR": P + "248a12ca0c07aa0147", "SDG": P + "3987e8e5adaffe482f",
    "TSK": P + "c4bba0e651f58c29fc", "ASR": P + "3bb4ddc091e4732e0f",
    "RVS": P + "768a31c8e1a247c668", "BFS": P + "138057c6270bcbdf5a",
    "GPF": P + "838c4bec5c5353659a", "RKB": P + "b3b45fcd8e68ade468",
    "SSL": P + "39a400f025268c20b6", "BSK": P + "b9921dcad805a00e41",
    "RRH": P + "58850bd6a92a93970a", "GRH": P + "6a9256c990073eacf8",
    "SMB": P + "7cacbdd7c70d8bdafa", "GDE": P + "a68501d8a0868160ba",
    "WIT": P + "b29b49da80beef6f31", "WIN": P + "31bed9f3f0c7f7a9db",
    "YTF": P + "aa883bd78444277315", "SMF": P + "ea964ef147f5413ce8",
    "BST": P + "7fb981e316c8c683d4", "FDR": P + "9bb8bee26d21b3e0d3",
    "BSB": P + "ef9f22ce9fd16a66f6", "CBM": P + "04ac0dc5037c9e75c4",
    "SAI": P + "f5b8e3e7d59f8d57ff", "HNC": P + "12a955dcf18edc3cf39",
    "MOO": P + "e49bdfda910800fd58", "RDS": P + "aea3d1c107ba0c3f9e",
}
SP = {
    "POR": "Porbeagle", "SDG": "Spiny Dogfish", "TSK": "Thorny Skate",
    "ASR": "Atlantic Stingray", "RVS": "River Stingray (Motoro)",
    "GPF": "Grass Puffer", "RKB": "Rock Bream", "SSL": "Silver Sillago",
    "BSK": "Blue Sucker", "RRH": "River Redhorse", "GRH": "Golden Redhorse",
    "SMB": "Smallmouth Buffalo", "GDE": "Goldeye",
    "WIT": "Witch Flounder", "WIN": "Winter Flounder",
    "YTF": "Yellowtail Flounder", "SMF": "Summer Flounder",
    "BST": "Barbel Steed", "FDR": "Freshwater Drum",
    "BSB": "Blackhead Seabream", "CBM": "Chub Mackerel",
    "SAI": "Saithe", "HNC": "Hornyhead Chub", "MOO": "Mooneye",
    "RDS": "Redear Sunfish",
}
S = {k: f"CENSUS-B4-{k}" for k in U}


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


def bake_single(story, prem, sketch, profile, conf=None, opn=None):
    return rec(f"P-B4-{story}-BAKE", story, "Bake", prem, sketch,
               [{"op": "EVAL_HABITAT_FACTOR_POSITION", "deps": []},
                {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
               [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight", profile,
               confidence=conf, open_sem=opn)


def resp_typed(story, prem, sketch, profile, conf=None, opn=None):
    return rec(f"P-B4-{story}-RESP", story, "Response", prem, sketch,
               [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
                {"op": "DECIDE_RESPONSE", "deps": [0]}],
               [], "NONE", "Response(TargetFeeding)", profile,
               confidence=conf, open_sem=opn)


def resp_guard(story, prem, sketch, anchor_note, profile, conf=None, opn=None):
    """P04 guard 双 Path：守护状态 pre-existing/persistent（契约）；
    目标同时可触发摄食 Path 与关系冲突 Path（PARALLEL_SET——契约明确同时，无序）；
    COMBINE 后统一决策。物种型 intruder 谓词记入 premise/open_semantics
    （顺序推导注记：谓词 typing 非新增 branch——见模块 docstring）。"""
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
    return rec(f"P-B4-{story}-RESP", story, "Response", prem, sketch_full,
               steps, [], "DUAL_PATH_CONFLICT_AWARE",
               "Response(TargetFeeding | RelationalConflict)", profile,
               confidence=conf, open_sem=opn)


PROGRAMS = [
    # ---------------- POR 鼠鲨 ----------------
    bake_single(
        "POR",
        ["lifecycle_stage = OCEAN_PELAGIC | SOUTH_PUPPING_RUN（2000km 南下产仔洄游；标记 2370km）",
         "oophagy/子宫内营养竞争 = 繁殖内部 lifecycle premise（非空间程序分支）"],
        "海洋期广泛分布（大陆架-上层）→ 冬季成鲑 2000km 南下产仔 → 归巢。顺序推导注记：正文描述的是"
        "lifecycle 阶段时序（海洋→南下→归巢），非面内判断链——按 B3 判例④记 premise 配置级 position 绑定"
        "（鲑系洄游同型）。空间因子随阶段 premise 切换，单链归一。",
        "EndothermicOceanicRunner"),
    resp_typed(
        "POR",
        ["thermal_capability = endothermic（retia mirabilia 逆流热交换，核心体温高于水温 8–10°C——"
         "能力/生态位变量非呈现轴，Story 明言不买 Mode）"],
        "离散猎物 typed 摄食响应：『Feeds on small and medium-sized pelagic schooling species, "
        "other sharks, squid』+底层鱼（cod/haddock/hake）。温血=typed context（深水持续猎食能力"
        "『hunt in deep water for extended periods』）。顺序推导注记：正文无判断顺序描述（单 evaluator "
        "typed 上下文），单步评估→决策。电感知为类群常识 EO 不入程序。",
        "EndothermicPursuitPredator",
        opn=["鼠鲨科电感知本种引文开放（Story EO）——typed context 升级候选，不改结构"]),
    # ---------------- SDG 白斑角鲨 ----------------
    bake_single(
        "SDG",
        ["lifecycle = HIGHLY_MIGRATORY（『Highly migratory species』）",
         "temperature_related_movement = 温度相关移动（S4 MSF——水温条件 premise）",
         "school_structure = 千尾觅食群/体型性别分群（群结构事实 premise，非互斥供给）"],
        "陆架底-中-表分布 + 高洄游 + 温度相关移动。顺序推导注记：正文时序为洄游/温度驱动的分布层面"
        "（premise 配置级，B3 判例④同型），无面内判断链。单因子链：评估栖息因子位→归一。",
        "MigratorySchoolShark"),
    resp_typed(
        "SDG",
        ["electrosense = passive（『Detects weak electric fields generated by potential prey』"
         "FishBase 逐字——猎物电场为感知输入；FR3 判例①：感知端样本并入 K8 电轴，不改变机会生成结构）"],
        "广食 typed 摄食响应：『comb jellyfish, squid, mackarel and herring…benthic fishes, shrimps, "
        "crabs and even sea cucumbers』。电感知=typed evaluator input（感知模态，输入端非程序结构）。"
        "顺序推导注记：『Detects…→Feeds』检测与摄食为同一 evaluator 的输入模态，非两步程序。",
        "ElectrosenseGeneralist"),
    # ---------------- TSK 棘背钝头鳐 ----------------
    bake_single(
        "TSK",
        ["depth_band = 25–440m usually（5–1540m range）",
         "temp_band = -1°C–14°C（深冷厂适）"],
        "深冷沙泥底静态分布。顺序推导注记：正文为静态栖息事实单因子（深度带+底质），无时序无判断链。"
        "单因子链。",
        "ColdDeepBenthicRay"),
    resp_typed(
        "TSK",
        ["ontogeny = diet changes with increasing body size（『Diet changes with increasing body "
         "size』FishBase——食性随体型 premise）",
         "electrosense = passive（『Able to detect weak electric fields…may also generate its own "
         "weak electric fields』FishBase 逐字——感知端+自发电场）"],
        "底栖广食+食腐 typed 摄食响应：『Feed mainly on fish, crustaceans』+多毛/水螅/软体/头足/棘皮，"
        "『is known to be a scavenger』（腐食=食物类型非结构分支）。电感知=typed evaluator input。"
        "顺序推导注记：无判断顺序描述；体型食性变化=premise 非分支。",
        "ElectrosenseScavenger"),
    # ---------------- ASR 大西洋黄貂鱼 ----------------
    bake_single(
        "ASR",
        ["salinity_tolerance = euryhaline（Marine; freshwater; brackish——Runtime Overlay）",
         "runtime_ascent = 成鱼河口/泻湖 + 『ascend rivers』（沿河上溯 runtime 行为）"],
        "咸淡水广适底栖 + 河口→沿河上溯。顺序推导注记：正文『coastal waters, including estuaries and "
        "lagoons + ascend rivers』为 runtime overlay 型连续分布移动（盐度条件 premise 配置），非面内"
        "判断链——B3 SGA 气呼吸 runtime 条件同型。单因子链，盐度广适为因子绑定值。",
        "EuryhalineEstuaryRay"),
    resp_typed(
        "ASR",
        [],
        "底栖无脊椎 typed 摄食响应：『tube anemones, polychaete worms, small crustaceans, clams, and "
        "serpent stars』。顺序推导注记：单 typed evaluator，无判断顺序描述。电感知/毒刺 EO 不入程序。",
        "BenthivoreRay",
        opn=["电感知/毒刺本种引文开放（Story EO）"]),
    # ---------------- RVS 眼斑河魟 ----------------
    bake_single(
        "RVS",
        ["water = pure freshwater（『Found in freshwater rivers』；pH 5.0–6.0 绑定值）"],
        "纯淡水河底静态分布。顺序推导注记：静态栖息单因子，无时序无判断链。单因子链。",
        "FreshwaterRiverRay"),
    resp_typed(
        "RVS",
        [],
        "淡水底栖 typed 摄食响应（P01 PatternFit 冻结主张承载：PrimaryEvaluand=Discrete Target，"
        "ResponseChannels=TargetFeeding）。食性面 FishBase 无述（S1 EO）——程序体为 P01 默认 typed 形"
        "（MEDIUM 置信），磿/捕食机制引文开放。毒刺=搏鱼阶段处理（后钩）非 FCF 前链，S11 排除。",
        "FreshwaterBenthivoreRay",
        conf="MEDIUM",
        opn=["食性面无述（Story S1 EO）——底栖无脊椎为魟类底栖形态推断，引文闭合前 MEDIUM"]),
    # ---------------- GPF 星点东方鲀 ----------------
    bake_single(
        "GPF",
        ["tide_window = HIGH_TIDE（『During high tide, mature individuals swim ashore in large "
         "numbers and spawn on beaches』——高潮窗周期 premise）",
         "spawning_event = 上岸产卵→返水（『throw themselves onto land…then return to the water』"
         "——事件时序 premise）"],
        "沿岸砂砾底静态 + 潮汐窗上岸产卵集群。顺序推导注记：正文有显式事件时序（高潮窗→集群上岸→产卵→"
        "返水→后续高潮淹没孵化），但该时序是繁殖 lifecycle 周期（opportunity lifecycle，Story 明言），"
        "按 B3 判例④/P05 周期绑定记 premise 配置级 position（洪水周期同型），不立面内 branch。"
        "单因子链，潮汐窗为周期绑定。",
        "HighTideBeachSpawner"),
    resp_typed(
        "GPF",
        ["dentition = 齿板/喙形态事实（TTX 齿板磯食常识未引文——S2 形态事实承载 typed context）"],
        "齿板底栖 typed 摄食响应（S1 磯食细节 EO；S2 齿板形态 MSF 为依据——PAY 形态推断同型）。"
        "顺序推导注记：无判断顺序描述。TTX=捕获后处理边界（人类侧食物安全，S11 排除——FR3 判例③）。",
        "PlateToothBenthivore",
        conf="MEDIUM",
        opn=["齿板磯食行为引文开放（Story Open Question）——MEDIUM"]),
    # ---------------- RKB 条石鲷 ----------------
    bake_single(
        "RKB",
        ["ontogeny_stage = JUV_DRIFT_WEED | ADULT_REEF（幼鱼『associate with drifting seaweed』"
         "——S9 阶段 premise）"],
        "沿岸岩礁 1–10m 静态 + 幼鱼流藻阶段。顺序推导注记：幼-成两阶段栖息为 lifecycle 阶段 premise"
        "（B3 判例④同型），无面内判断链。单因子链，阶段为因子绑定。",
        "ReefJuvenileDrift"),
    resp_typed(
        "RKB",
        ["dentition = 喙齿形态事实（属名 weapon+jaw——磯食贝类常识未引文 EO）"],
        "岩礁喙齿 typed 摄食响应（磯食行为面 EO；喙齿形态事实为依据——MEDIUM）。顺序推导注记："
        "无判断顺序描述。性转换面 EO。",
        "BeakCrusherReef",
        conf="MEDIUM",
        opn=["磯食行为引文开放（S1/S2 EO）；性转换面 EO（黑鲷先例）"]),
    # ---------------- SSL 沙鮻 ----------------
    bake_single(
        "SSL",
        ["ontogeny_stage = JUV_PLANKTONIC | ADULT_BENTHIC（幼浮游-底栖——S9 阶段 premise）"],
        "海滩沙洲/河湾/红树林小溪沙底静态 + 幼体浮游阶段。顺序推导注记：静态栖息单因子+阶段 premise，"
        "无判断链。单因子链。",
        "SandflatSchooler"),
    resp_typed(
        "SSL",
        [],
        "沙底底栖 typed 摄食响应：『mainly on polychaete worms, small prawns, shrimps and "
        "amphipods』。潜沙=受扰反捕食 runtime 行为（『Adults bury themselves in the sand when "
        "disturbed』——遇鱼可见性语义，runtime 不买 Mode），非摄食程序输入。顺序推导注记：摄食面无"
        "判断顺序描述；受扰→潜沙为反捕食反应（S11 排除，CB 轴鱼侧 typed 子类）。",
        "SandflatBenthivore"),
    # ---------------- BSK 长背亚口鱼 ----------------
    bake_single(
        "BSK",
        ["flow_regime = strong current in deep (1–2.5m) chutes（急流深槽 premise 绑定值）",
         "substrate = bedrock/sand/gravel"],
        "急流深槽基石静态分布。顺序推导注记：静态栖息因子绑定（流速+底质同因子复合绑定值），"
        "无时序无判断链。单因子链。吸口形态事实（底裙式吸口）EO。",
        "SwiftChuteSucker"),
    resp_typed(
        "BSK",
        ["mouth_morphology = 亚口科底裙式吸口形态事实（吸着/底吸食推断依据——S7 EO 未逐字引文）"],
        "急流底栖 typed 摄食响应（食性面 FishBase 无述 S1 EO——吸口形态事实推断底吸食，MEDIUM，"
        "PAY 形态推断同型）。顺序推导注记：无判断顺序描述。",
        "SuctionBenthivore",
        conf="MEDIUM",
        opn=["食性/繁殖面无述（Story S1/S6 EO）——吸口底吸食为形态推断，引文闭合前 MEDIUM"]),
    # ---------------- RRH 河红马鱼 ----------------
    bake_single(
        "RRH",
        ["lifecycle = POTAMODROMOUS（河内洄游 premise）"],
        "岩池/急流静态分布（『rocky pools and swift runs of small to large rivers』）。"
        "顺序推导注记：静态栖息单因子+洄游 premise，无判断链。单因子链。",
        "RockPoolMolluskFeeder"),
    resp_typed(
        "RRH",
        ["prey_specialization = small bivalve mollusks（『feed on small bivalve mollusks』——"
         "专食 typed context）"],
        "贝食 typed 摄食响应：小型双壳贝专食。磿贝咽喉机制未逐字引文（S2 EO——机制事实不买 Mode，"
        "草鱼 R02 grazing 先例同型）。顺序推导注记：无判断顺序描述。",
        "BivalveSpecialist",
        opn=["碾贝咽喉机制引文开放（S2 EO）"]),
    # ---------------- GRH 金红马鱼 ----------------
    bake_single(
        "GRH",
        ["lifecycle = POTAMODROMOUS（河内洄游 premise）"],
        "泥底/岩底池潭+沙洲+急滩静态分布。顺序推导注记：静态栖息单因子+洄游 premise，无判断链。"
        "单因子链。",
        "PoolRunInsectivore"),
    resp_typed(
        "GRH",
        [],
        "底栖昆虫幼生 typed 摄食响应：『They feed on immature mayflies, caddisflies and midges』。"
        "与河红马鱼同属对照（Moxostoma 2/2：贝食 vs 虫食——typed context 差异非结构差异）。"
        "顺序推导注记：无判断顺序描述。",
        "InsectLarvaeBenthivore"),
    # ---------------- SMB 水牛鱼 ----------------
    bake_single(
        "SMB",
        [],
        "河湾潭果/干流/湖泊静态分布（『pools, backwaters and main channels…also in lakes and "
        "impoundments』）。顺序推导注记：静态栖息单因子，无判断链。单因子链。",
        "PoolBackwaterGrinder"),
    resp_typed(
        "SMB",
        ["grinding_mechanism = 咽喉骨板磿碎（『by grinding with the bony plates in its throat』"
         "FishBase 逐字——磿碎机制事实不买 Mode，草鱼 R02 先例同型）"],
        "贝藻 typed 摄食响应：『feed on shellfish and algae』+咽喉骨板磿碎（S2 MSF——机制为 typed "
        "context/能力事实，非程序分支）。顺序推导注记：无判断顺序描述。",
        "ThroatPlateGrinder"),
    # ---------------- GDE 金眼鱼 ----------------
    bake_single(
        "GDE",
        ["seasonal_run = 春上溯/秋下行（季节洄游 premise——P05 季节绑定）"],
        "浊河深潭/敞水河道静态 + 季节洄游。顺序推导注记：春/秋双向为季节周期 premise 配置级"
        "（B3 判例④同型），无面内判断链。单因子链。",
        "TurbidPoolNocturnal"),
    resp_typed(
        "GDE",
        ["light_regime = Mainly nocturnal（夜行 typed context——R03 低光先例不买 Night Mode）"],
        "浊河夜行广食 typed 摄食响应：『surface and aquatic insects, crustaceans, mollusks, small "
        "fishes, frogs, shrew, and mice』（含水面/落水猎物与小型哺乳——欧鲢 R05 同构）。银眼夜视 "
        "tapetum 为常识 EO。顺序推导注记：无判断顺序描述（夜行为 context 非门）。",
        "NocturnalBroadOmnivore",
        opn=["tapetum 夜视引文开放（Story EO）"]),
    # ---------------- WIT 女巫鲽 ----------------
    bake_single(
        "WIT",
        ["depth_band = usually 45–366m（18–1570m range）",
         "temp_band = 2°C–6°C（深冷）",
         "substrate = soft mud"],
        "深冷软泥底静态分布。顺序推导注记：静态栖息因子绑定（深度/水温/底质复合绑定值），"
        "无时序无判断链。单因子链。与大比目鱼 R06 深海底食同构（不同深度带——绑定值差异）。",
        "ColdDeepMudFlounder"),
    resp_typed(
        "WIT",
        [],
        "深冷泥底 typed 摄食响应：『Feeds on crustaceans, polychaetes, brittle stars』+鱼类。"
        "顺序推导注记：无判断顺序描述。",
        "ColdMudBenthivore"),
    # ---------------- WIN 美洲拟鲽 ----------------
    bake_single(
        "WIN",
        ["substrate = soft muddy to moderately hard bottoms（近岸绑定值）"],
        "近岸泥-中硬底静态分布。顺序推导注记：静态栖息单因子，无判断链。单因子链。",
        "NearshoreDiurnalFlounder"),
    resp_typed(
        "WIN",
        ["light_regime = diurnal（『feed predominantly in daytime』——日间 typed context）"],
        "日间底栖 typed 摄食响应：『feed predominantly in daytime on organisms living in, on or "
        "near the bottom』——shrimps, amphipods, crabs, sea urchins, snails。顺序推导注记：正文"
        "『daytime…on…near the bottom』为时间 context × 目标位置的复合 typed 描述，先判断时序"
        "（日间）后定位猎物（底内/底上/底近）是表述顺序而非程序门——无 early-return 链证据，"
        "记复合 typed context（GDE 夜行对偶，R03 先例不买 Night/Diurnal Mode）。右鲽形态=EO。",
        "DiurnalBottomFeeder",
        opn=["右鲽两眼同侧形态=形态事实 EO（S7）非感官程序"]),
    # ---------------- YTF 大西洋黄盖鲽 ----------------
    bake_single(
        "YTF",
        ["depth_band = 37–82m", "temp_band = 3–5°C", "substrate = sandy to muddy"],
        "中深沙泥底静态分布。顺序推导注记：静态栖息因子绑定，无判断链。单因子链。",
        "MidDepthMudFlounder"),
    resp_typed(
        "YTF",
        ["prey_specialization = polychaete main（『mainly on polychaete worms』——主食 typed "
         "context）"],
        "多毛主食 typed 摄食响应：多毛+端足/虾/等足等甲壳+偶食小鱼（sand lance/capelin）。"
        "顺序推导注记：无判断顺序描述。",
        "PolychaeteForager"),
    # ---------------- SMF 大西洋牙鲆 ----------------
    bake_single(
        "SMF",
        ["substrate = hard sandy（『prefer hard sandy substrate where they can burrow』——"
         "掘穴底质绑定值）"],
        "硬沙底掘穴+盐沼沟/海草床/沙浅滩静态分布。顺序推导注记：静态栖息单因子（掘穴底质偏好），"
        "无判断链。捊穴伏击行为面 EO（FishBase 只写 burrow 栖息）。单因子链。",
        "HardSandBurrowFluke"),
    resp_typed(
        "SMF",
        ["burrow_habitat = 掘穴栖息事实（伏击 typed context 推断依据——行为引文 EO）"],
        "硬沙底伏击 typed 摄食响应（食性面 FishBase 缺 S1 EO——掘穴栖息事实+fluke 游钓事实推断伏击"
        "捕食，MEDIUM，PAY 形态/栖息推断同型；WEL/SGA 伏击 typed context 先例）。顺序推导注记："
        "无判断顺序描述（伏击行为本身 EO，不构造伏击 branch）。左鲆形态与右鲽对照=形态差异不买 Mode。",
        "BurrowAmbushFluke",
        conf="MEDIUM",
        opn=["捊穴伏击行为引文开放（Story Open Question）；食性面无述（S1 EO）——MEDIUM"]),
    # ---------------- BST 唇䱻 ----------------
    bake_single(
        "BST",
        ["lifecycle = POTAMODROMOUS（河内洄游 premise）"],
        "东亚河川静态分布。顺序推导注记：静态栖息单因子+洄游 premise，无判断链。单因子链。",
        "RiverBarbelProbe"),
    resp_typed(
        "BST",
        [],
        "底栖无脊椎 typed 摄食响应：杂食『mainly on benthic invertebrates』。颏须形态事实"
        "（≤眼径）——随须探底行为未引文（S7 EO；长吻鮈 R03 同构——须为 typed context 候选，"
        "引文闭合前记 open）。顺序推导注记：无判断顺序描述。",
        "BarbelBenthivore",
        opn=["颏须探底行为引文开放（S7 EO）——须探底 typed context 升级候选"]),
    # ---------------- FDR 淡水石首鱼 ----------------
    bake_single(
        "FDR",
        [],
        "中大河湖底层静态分布（『bottoms of medium to large rivers and lakes』）。"
        "顺序推导注记：静态栖息单因子，无判断链。单因子链。",
        "RiverLakeBottomDrum"),
    resp_typed(
        "FDR",
        ["prey_breadth = 含同类幼鱼（『fish (especially shad and young drum)』——同类幼鱼为合法"
         "猎物类型 premise）"],
        "河湖底 typed 广食响应：『aquatic insect immatures such as mayflies, amphipods, fish…, "
        "crayfish and mollusks』。产声=潜在声学 cue（『Known to produce sound』——种内沟通/声学"
        "观察非本鱼摄食程序输入，S7 排除；鸣肌机制 EO）。顺序推导注记：无判断顺序描述。",
        "BottomBroadOmnivore",
        opn=["鸣肌产声机制 EO；产声作为钓手听觉线索引文开放（产品面 open）"]),
    # ---------------- BSB 黑鲷 ----------------
    bake_single(
        "BSB",
        ["salinity_context = brackish tolerated（湾内岩礁咸淡水绑定值）"],
        "湾内浅岩礁+咸淡水区静态分布。顺序推导注记：静态栖息单因子，无判断链。单因子链。"
        "春夏产卵=lifecycle premise（EO 细节）。",
        "BayReefBream"),
    resp_typed(
        "BSB",
        [],
        "贝/多毛 typed 摄食响应（磿碎机制 EO）。性转换（先雌后雄常识未逐字引文）=lifecycle "
        "premise EO（S6/S9）。与真鲷 R04 同科对照。顺序推导注记：无判断顺序描述。",
        "ShellfishBiter",
        opn=["性转换引文开放（S6/S9 EO）；磿贝机制引文开放（S2 EO）"]),
    # ---------------- CBM 日本鲭 ----------------
    bake_single(
        "CBM",
        ["seasonal_state = WINTER_DEEP_INACTIVE（『move to deeper water and remain inactive "
         "during the winter season』——季节 position+活动状态 premise）",
         "school_structure = 体型分级群游（『Schooling by size…initiates at approximately 3 cm』"
         "——群结构事实 premise）"],
        "沿岸 pelagic 分布 + 冬季深水不活跃（季节重排）。顺序推导注记：冬深水+不活跃为季节 premise"
        "配置级（P05 季节重排，B3 判例④同型），无面内判断链。单因子链，季节为周期绑定。",
        "SizeGradedNightSchool"),
    resp_typed(
        "CBM",
        ["light_regime = 夜捕（night feeding typed context；夜视 EO）"],
        "夜捕 typed 摄食响应：『copepods and other crustaceans, fishes and squids』。与大西洋鲭 "
        "R02 同属对照（本种无 filter 记录——双机制差异不构成本种程序）。顺序推导注记：无判断顺序"
        "描述（夜捕为 context 非门）。",
        "NightPelagicFeeder",
        opn=["夜视感官面 EO（S7）"]),
    # ---------------- SAI 绿青鳕 ----------------
    bake_single(
        "SAI",
        ["seasonal_run = 春向岸/冬向深（S4）", "migration_axis = 南北洄游（S5）",
         "school_structure = gregarious（群结构事实 premise）"],
        "岸-近海分布 + 季节岸深移动 + 南北洄游。顺序推导注记：春岸/冬深为季节周期 premise 配置级"
        "（P05 季节重排），无面内判断链。单因子链。",
        "SeasonalShoreDeepGadoid"),
    resp_typed(
        "SAI",
        ["ontogeny = 体型分级食性（小型近岸甲壳/小鱼→大型主鱼食——S9 阶段 premise）"],
        "群游掠食 typed 摄食响应：active gregarious 捕食甲壳/鱼。体型分级食性与日本鲭同构"
        "（不拆故事）。顺序推导注记：无判断顺序描述；食性随体型=premise 非分支。",
        "SizeGradedPiscivore"),
    # ---------------- HNC 双点美鱥（P04 guard）----------------
    bake_single(
        "HNC",
        [],
        "岩池小河清水静态分布。顺序推导注记：静态栖息单因子，无判断链。单因子链。",
        "ClearPoolPebbleNest"),
    resp_guard(
        "HNC",
        ["guard_condition = 雄鱼石巢丘已建成且守护中（『Males build a cup shaped depression…with "
         "pebbles…1–3 feet』+产后覆砾——persistent guard condition 在 Presentation 前存在，P04 契约）",
         "guard_target_specificity = SPECIES_TYPED_INTRUDER（『defend the nest mounds from other "
         "N. biguttatus males but not other species』逐字——intruder evaluation 谓词为物种型：仅同种"
         "雄性触发防御，异种不触发）",
         "nest_associates = 异种借巢产卵+杂交（『Other species take advantage of this defense and "
         "spawn in the nest mounds』→accidental hybridization——借巢者被容忍，负知识：不触发冲突 Path）",
         "ontogeny = 幼轮虫/桡足→成螺/螯虾/虫/鱼（S9 阶段 premise）"],
        "昼间视觉捕食 typed（『a daylight visual feeder』）+ 石巢护守：对靠近巢丘的目标，摄食 Path 与"
        "关系冲突 Path 可同时触发；冲突 Path 的 intruder 谓词是物种型的（同种雄性竞争者→防御；异种→"
        "不防御且容忍借巢产卵）。顺序推导注记：物种型谓词是 evaluator typing 变化（guard target "
        "specificity——Story 自记『P04 内部结构变量』Open Question），不是新增 branch/gate——拓扑保持"
        "P04 契约并行双 Path，谓词差异留判同阶段作 typed 轴裁决。",
        "pebble_mound（雄建石巢丘，产后覆砾）",
        "DaylightVisualFeeder_GuardSpeciesTyped",
        opn=["guard target specificity（物种型 intruder 谓词）是否=P04 typed 参数轴 vs 结构差异——"
             "Story Open Question，判同阶段对 canonical 直验裁决（候选：anchor 轴第 6 实例 "
             "pebble_mound + 新 typed 轴 guard_target_specificity）",
             "异种借巢在本产品供给中的语义开放（Story Open Question）——不改变 ResponseOwner"]),
    # ---------------- MOO 月眼鱼 ----------------
    bake_single(
        "MOO",
        ["lifecycle = POTAMODROMOUS（河内洄游 premise）"],
        "中大河湖深潭/洄水 pelagic 静态分布。顺序推导注记：静态栖息单因子+洄游 premise，无判断链。"
        "单因子链。",
        "DeepPoolPelagicMooneye"),
    resp_typed(
        "MOO",
        [],
        "深潭 pelagic typed 摄食响应（食性面 FishBase 无述 S1 EO——P01 PatternFit 冻结主张承载，"
        "MEDIUM；与金眼鱼同属对照：夜行 vs 未述）。大眼夜视常识未逐字引文（S7 EO）。"
        "顺序推导注记：无判断顺序描述。",
        "PelagicFeederMooneye",
        conf="MEDIUM",
        opn=["食性面无述（S1 EO）；夜视假说开放（S7 EO）——MEDIUM"]),
    # ---------------- RDS 小冠太阳鱼 ----------------
    bake_single(
        "RDS",
        [],
        "温水清静水植被/沉木静态分布（『warm, clear and quiet waters rich in vegetation and "
        "snags』）。顺序推导注记：静态栖息单因子，无判断链。单因子链。巢群集产卵 EO。",
        "WarmVegetatedSunfish"),
    resp_typed(
        "RDS",
        ["prey_specialization = mollusk preference（『Has a preference for mollusks as food』"
         "FishBase 逐字——贝食偏好 typed context；血吸虫螺生物防治语义）"],
        "贝食偏好 typed 摄食响应。磿螺机制（shellcracker 咽骨磿碎常识）EO 未逐字引文——"
        "偏好有原文，磿碎机制引文开放。Distinct pairing 产卵=lifecycle premise EO。"
        "顺序推导注记：无判断顺序描述。",
        "MolluskPreferringSunfish",
        opn=["磿螺机制引文开放（S2 EO——贝食偏好有原文，机制常识未引文）"]),
    # BFS 莱氏拟乌贼：头足类非鱼边界——Product Scope Deferred（FR3 判例②），
    # 无鱼响应骨架，0 程序（stories.jsonl 全面 NO_SURFACE_EFFECT + 全 S 项 excluded）。
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
    n_med = sum(1 for p in PROGRAMS if p.get("confidence") == "MEDIUM")
    print(f"frozen {len(PROGRAMS)} blind programs (Bake={n_bake} Response={n_resp} "
          f"MEDIUM={n_med}) -> {out}")
    for p in PROGRAMS:
        print(f"  {p['program_id']}: {p['blind_hash']}")


if __name__ == "__main__":
    main()
