# -*- coding: utf-8 -*-
"""CENSUS-B5 盲程序骨架生成器（盲纪律：template_registry.yaml 未开——程序体冻结前不读 registry 本体）。

52 条冻结 Story（FISH-R08 普通补齐收尾批 + FISH-R09 普通层续批，FR3 CLOSED；
packet + 逐鱼 story 快照见 input_snapshots/）。骨架从 Story 十节正文独立推写；
语义输入=P01/P04/P05 pattern 页（B3 input_snapshots 同 URL 冻结快照复用——
P04 契约『守巢/护幼状态在 Presentation 前存在且持续；当前目标可同时触发摄食
与关系冲突路径』；P05 洞见『停食→P05 状态抑制 Feeding Path，不落 P04』）；
P02=ResourcePatch 背景语义（RHM/RBP story FR 冻结解释承载，无独立快照）。
hash: sha256(canonical_json(record minus blind_hash))[:16]

【B5-F-0 类偏差注记（bias_declaration 同文）】盲段加载流程管线时读过 B4 的
build_blind_programs.py / build_stories.py（B4 26 鱼盲体的 SINGLE 链与 TYPED
形态 op 名层面）与角色记忆 v5（各族散文描述与判例）。template_registry.yaml
本体未读。缓解：本批 104 条 sketch 严格从 52 份 Story 十节正文独立推写，每条
含顺序推导注记，未按 registry 形状定制。

【顺序推导纪律（用户反馈 2026-09-11，authoring_work_standards §5.1）】
每个骨架显式记录顺序推导结果。本批 52 Story 逐条顺序扫描结论：
- 无一 Story 正文描述面内 early-return 判断链（分级命中 if/elif/else 型）；
- 出现的先后序均为 lifecycle/季节/洪水周期/昼夜时序——STL 海-河可重复溯河、
  INC 融冰触发停食上溯、WST 产卵前停食+4-11 年间隔、AKB 温升上溯、GAJ 夏季
  近岸产卵、SVT/LMP/CMR 季节深浅移动、BAS/JDP 洪水事件机会繁殖、LKT/CCR 夜行
  ——按 B3 判例④/P05 契约记 premise 配置级 position 绑定，不是面内 ordered
  branch（INC/WST 停食=P05 状态抑制 Feeding Path，判例明言不落 P04 不立结构）；
- 9 例 P04 guard（ARO 口哺/CSL 护卵幼/CRC 砾巢脊/ROB 雄巢扇护/MDC 洞顶双亲/
  JGC 浊水双亲/JDP 洪水护卵/LMP 卵块激进/AMK 岩缝扇护）按 P04 契约拓扑
  （并行双 Path——PARALLEL_SET 依据=契约明言『可同时触发』）；anchor 值
  （mouthbrood/gravel_ridge/cave_ceiling/biparental/fan 型等）与双亲 vs 雄性
  单亲、扇护子动作记 open_semantics 留判同阶段裁决，不预裁结构差异。
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent
P = "https://app.notion.com/p/3d7a4137d23681"
U = {
    # R08
    "SAF": P + "119b6aaf8457de89541", "ARO": P + "1f2b556def8bd21ff9a",
    "CSL": P + "1d3a9c6ca05ecbadac6", "AKB": P + "15ebb30d511f8bab74b",
    "MHS": P + "181a4d4fdd6f64bebcd", "SPM": P + "179bf16e7b791f5ab3f",
    "YFT": P + "1d888a4cd74dce4054a", "STM": P + "17999923cd392bfc0f0a",
    "ALB": P + "181a585d84a7f8aa4b4", "STL": P + "1f28078f0a1e7e33d7a",
    "ARG": P + "1c49e17eb4573c4c867", "LKT": P + "145b413ff9f36b5ac8e",
    "RHM": P + "17eb518fae0be954105", "RBP": P + "1018e5fceb06333f0d5",
    "TMU": P + "133bf92dec11cd68662", "SPK": P + "17c84b1fa57bdf2f261",
    "DTN": P + "1b0b2c9d9b4412ad818", "GAJ": P + "193a31defe1eca576cb",
    "HAD": P + "107afcbf98c58e257a0", "BPB": P + "1e6a00fdd24fdca6535",
    "RVC": P + "12da391def70534e735", "CRC": P + "150beaaef2c28407ff4",
    "INC": P + "1c9bbb9c6c60cc3671d", "HBW": P + "145bce1f564a311de52",
    "CLC": P + "1d6b645f7b5bc07a13b", "RTC": P + "1098c55e5705ef95962",
    # R09
    "WST": P + "13187adddcd69543f07", "ROB": P + "118a72cf8959f9bd1b0",
    "KGO": P + "1b68b31d8c5b9599e00", "LMD": P + "1bb8fd0d8734eb329b2",
    "MDC": P + "1bdb8d9caf7e494d0a4", "JGC": P + "184a040d081eee7d919",
    "SPC": P + "187ad00e324e1380b54", "TGT": P + "1d79933d7ffd8993431",
    "HYC": P + "1f2ad7ee79384e1e421", "PRC": P + "176a3e3dd6402dae8ba",
    "CCR": P + "191b66eed0bad664c99", "APA": P + "19db21adddce653b2e1",
    "GOT": P + "18bbf6dc0f9aedb4643", "GIT": P + "12a8564fe14934880c6",
    "SVT": P + "12c94eef4acbd36b2c0", "PEL": P + "1698c3ec857e0f936ba",
    "CMR": P + "1d8a4a9d0fc32c41407", "LKR": P + "152a0ecd8b5939cab48",
    "ASP": P + "1ea892ffc8e9715678f", "BIA": P + "1698a9cc1805a8f7425",
    "HLL": P + "183a3f2d34097ae916e", "BAS": P + "1459c6afea8475b6ad5",
    "JDP": P + "11ebb5aefb0cbcac9a0", "LMP": P + "11ebec0cc6c0640ef44",
    "AMK": P + "19d8b05fa1bb6a6f16e", "GSF": P + "1a99a88d40a0a11075b",
}
SP = {
    "SAF": "Sailfish", "ARO": "Silver Arowana", "CSL": "Chinese Sleeper",
    "AKB": "Alaska Blackfish", "MHS": "Marbled Headstander",
    "SPM": "Spanish Mackerel", "YFT": "Yellowfin Tuna", "STM": "Striped Marlin",
    "ALB": "Albacore", "STL": "Steelhead", "ARG": "Arctic Grayling",
    "LKT": "Lake Trout", "RHM": "Redhook Myleus", "RBP": "Red-bellied Pacu",
    "TMU": "Tiger Muskellunge", "SPK": "Sacramento Pikeminnow",
    "DTN": "Dogtooth Tuna", "GAJ": "Greater Amberjack", "HAD": "Haddock",
    "BPB": "Butterfly Peacock Bass", "RVC": "River Chub",
    "CRC": "Creek Chub", "INC": "Inconnu", "HBW": "Humpback Whitefish",
    "CLC": "Chinese Largemouth Catfish", "RTC": "Redtail Catfish",
    "WST": "White Sturgeon", "ROB": "Rock Bass", "KGO": "Kissing Gourami",
    "LMD": "Leopard Mandarin", "MDC": "Midas Cichlid", "JGC": "Jaguar Cichlid",
    "SPC": "Speckled Peacock", "TGT": "Tiger Trout",
    "HYC": "Hybrid Crucian", "PRC": "Prussian Carp", "CCR": "Crucian Carp",
    "APA": "Apache Trout", "GOT": "Golden Trout", "GIT": "Gila Trout",
    "SVT": "Sevan Trout", "PEL": "Peled", "CMR": "Common Roach",
    "LKR": "Roach (Lake Row)", "ASP": "Asp", "BIA": "Biara",
    "HLL": "Halfline Leporinus", "BAS": "Basa", "JDP": "Jade Perch",
    "LMP": "Lumpfish", "AMK": "Atka Mackerel", "GSF": "Green Sunfish",
}
S = {k: f"CENSUS-B5-{k}" for k in U}

ORDER_NOTE = "顺序推导注记"


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


def bake_single(story, prem, sketch, profile, opn=None):
    return rec(f"P-B5-{story}-BAKE", story, "Bake", prem, sketch,
               [{"op": "EVAL_HABITAT_FACTOR_POSITION", "deps": []},
                {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
               [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight", profile,
               open_sem=opn)


def resp_typed(story, prem, sketch, profile, conf=None, opn=None):
    return rec(f"P-B5-{story}-RESP", story, "Response", prem, sketch,
               [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
                {"op": "DECIDE_RESPONSE", "deps": [0]}],
               [], "NONE", "Response(TargetFeeding)", profile,
               confidence=conf, open_sem=opn)


def resp_guard(story, prem, sketch, anchor_note, profile, conf=None, opn=None):
    """P04 guard 双 Path：守护状态 pre-existing/persistent（契约）；
    目标同时可触发摄食 Path 与关系冲突 Path（PARALLEL_SET——契约明确同时，无序）；
    COMBINE 后统一决策。anchor 值/守护参与者（双亲 vs 雄）/扇护子动作记入
    premise + open_semantics（顺序推导注记：子动作与参与者 typing 非新增
    branch/gate——拓扑保持 P04 契约并行双 Path，差异留判同阶段作轴裁决）。"""
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
    return rec(f"P-B5-{story}-RESP", story, "Response", prem, sketch_full,
               steps, [], "DUAL_PATH_CONFLICT_AWARE",
               "Response(TargetFeeding | RelationalConflict)", profile,
               confidence=conf, open_sem=opn)


PROGRAMS = [
    # ================= R08 =================
    # ---------------- SAF 旗鱼 ----------------
    bake_single(
        "SAF",
        ["lifecycle = OCEANIC_HIGHLY_MIGRATORY（高洄游）",
         "thermocline_band = 温跃层上层洋面分布带（epipelagic）"],
        "温跃层上层洋面分布+高洄游。" + ORDER_NOTE + "：正文时序为洄游/lifecycle 阶段"
        "（premise 配置级 position 绑定，B3 判例④），无面内判断链。单因子链，分布带"
        "为因子绑定值。",
        "OceanicBillfishRunner"),
    resp_typed(
        "SAF",
        ["bill_tool = 喙击打攻击工具（tapping 短距/slashing 横向大距——『改造目标个体"
         "可捕获性』非电鳗式生成机会，Story 明言留 P01 typed context；FishMode=Weak）",
         "sail_posture = 攻击时帆背鳍展开姿态 overlay（reduce sideways oscillations of "
         "the head——攻击姿态变量）"],
        "群鱼离散目标 typed 摄食响应：『Feeds mainly on fishes, crustaceans and "
        "cephalopods』；攻击行为=喙击打猎物群（每次攻击伤约 2 尾、捕获率 24%——工具"
        "效率数据为 typed context 非程序分支）；帆展开=攻击时刻姿态。" + ORDER_NOTE +
        "：正文『击打→捕获』为工具使用的事件描述非面内判断链——单 typed evaluator，"
        "工具与姿态记 typed context。",
        "BillStrikeSchoolHunter",
        opn=["喙击打语义 vs 电鳗 Candidate（攻击者生成机会）异同裁决=Story Open "
             "Question（Representation 层，census 不预裁）；钓法引文开放"]),
    # ---------------- ARO 银龙鱼 ----------------
    bake_single(
        "ARO",
        ["surface_layer = 水面层绑定（上口位+水面捕食）",
         "hypoxia_tolerance = 低氧耐受（runtime 生理条件 premise）"],
        "静水水面层/悬岸+洪泛林（黑/白水系）分布。" + ORDER_NOTE + "：静态栖息+水面层"
        "绑定，无时序无判断链。单因子链。",
        "SurfaceLayerRiverPredator"),
    resp_guard(
        "ARO",
        ["guard_condition = 雄鱼口哺携带卵/幼近 6 周（『carries eggs, larvae and early "
         "juveniles in his mouth』——携带型持续守护，Presentation 前已存在，P04 契约）",
         "guard_anchor = MOUTHBROODING_MALE（口哺=携带型 anchor 提案）"],
        "水面跳跃 typed 摄食（『jumps out of the water to feed on large insects』水猴"
        "跳跃；上口位自下向上抓取；螺/甲壳/虫/蜘蛛/小鱼）+ 雄鱼口哺守护：对水面目标"
        "摄食 Path ∥ 对携带卵幼的威胁评估 Path。" + ORDER_NOTE + "：跳跃捕食无判断顺序"
        "描述（单 evaluator 水面 typed）；口哺守护按 P04 契约并行双 Path，携带型 vs "
        "结构型 anchor 差异留判同阶段。",
        "mouthbrooding_male（雄口哺携带卵/幼 6 周）",
        "SurfaceJumperMouthbrooder",
        opn=["口哺 guard 与巢 guard 的 P04 表达差异=Story Open Question（anchor 轴"
             "新值提案 mouthbrooding_male——携带型语义 vs 结构型语义）；钓法引文开放"]),
    # ---------------- CSL 葛氏鲈塘鳢 ----------------
    bake_single(
        "CSL",
        ["hibernation_state = FROZEN_DORMANT_MUD（『survive in dried out or "
         "completely frozen water bodies by digging itself into mud where it "
         "hibernates』钻泥蛰伏——P05 状态 premise，肺鱼/江鳕蛰伏判例同类）",
         "habitat = 静水植被 lentic（『avoids river stretches』）"],
        "静水植被区分布+冻结/干涸钻泥蛰伏状态重排。" + ORDER_NOTE + "：蛰伏为季节/状态"
        "周期 premise 配置级（P05 状态抑制，B3 判例④），无面内判断链。单因子链。",
        "VegetatedPondDormantSleeper"),
    resp_guard(
        "CSL",
        ["guard_condition = 雄鱼护卵+浮游幼体持续（『Males guard the eggs and pelagic "
         "larvae』——守护对象跨卵+浮游幼两阶段，P04 契约 pre-existing/persistent）",
         "guard_anchor = NEST_PELAGIC_LARVAE（巢+浮游幼守护对象）"],
        "静水伏击贪婪捕食 typed（『voracious predatory fish…wide variety of "
        "invertebrates, tadpoles and fish』）+ 护卵幼守护：对靠近目标摄食 Path ∥ 巢/"
        "幼威胁评估 Path。" + ORDER_NOTE + "：伏击无判断顺序描述（静水植被 typed "
        "context）；守护按 P04 契约并行双 Path。入侵种群 extirpate 生态影响为 Story "
        "Open 非程序面。",
        "nest_pelagic_larvae（雄护卵+浮游幼）",
        "PondAmbushSleeperGuarder",
        opn=["入侵种（欧洲 extirpate）供给语义=Story Open Question（OPS 层）"]),
    # ---------------- AKB 阿拉斯加黑鱼 ----------------
    bake_single(
        "AKB",
        ["freeze_tolerance = -20°C 40 分钟存活/部分体冻结数日存活（生理耐受 typed "
         "context——非捕获语境，Story S11 归 SN）",
         "air_breathing = 食管辅助呼吸兼性气呼吸（『Uses its esophagus as auxiliary "
         "breathing organ』——runtime 生理条件 premise，肺鱼/雀鳝气呼吸判例不买 Mode）",
         "spawn_trigger = 温升 10-15°C 上溯产卵（季节温度触发 premise）"],
        "沼泽植被小水体分布+温升上溯产卵。" + ORDER_NOTE + "：正文时序（温升→上溯→"
        "产卵）为季节触发生 lifecycle premise 配置级，无面内判断链。单因子链。",
        "SwampFreezeSurvivor"),
    resp_typed(
        "AKB",
        [],
        "沼泽底栖 typed 摄食响应（食性面 FishBase 无述 S1 EO——程序体为 P01 冻结主张"
        "承载：PrimaryEvaluand=Discrete Target，MEDIUM 置信）。" + ORDER_NOTE + "：无"
        "判断顺序描述。耐冻/气呼吸=runtime 生理条件不入程序。",
        "SwampBenthivore",
        conf="MEDIUM",
        opn=["食性面无述（Story S1 EO）——引文闭合前 MEDIUM；耐冻生理机制细节开放"]),
    # ---------------- MHS 大理石倒立鱼 ----------------
    bake_single(
        "MHS",
        ["habitat = 悬岸静水（overhanging banks 静水绑定）"],
        "悬岸静水分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "OverhangingBankStillwater"),
    resp_typed(
        "MHS",
        ["head_down_posture = 头下位姿态假说（headstander 科名暗示但 FishBase 页未述"
         "——EO 不写为事实；若证实为摄食姿态=posture grain 内变量不买 Mode）"],
        "杂食 typed 摄食响应：『Adults feed on worms, crustaceans, insects and plant "
        "matter』（trophic 2.9）。" + ORDER_NOTE + "：无判断顺序描述；头下位姿态假说"
        "为 Story Confidence Medium 来源但 EO 不构程序输入（记 open）。",
        "HeadstanderOmnivore",
        opn=["头下位姿态行为引文开放（科名暗示页内未述）——posture grain 内变量"]),
    # ---------------- SPM 康氏马鲛 ----------------
    bake_single(
        "SPM",
        ["lifecycle = LENGTHY_LONGSHORE_MIGRATION（『undertake lengthy long-shore "
         "migrations』沿岸长程洄游 premise）",
         "turbidity_salinity = 低盐高浊浅海绑定（often of low salinity and high "
         "turbidity）"],
        "陆架缘-浅海低盐高浊分布+沿岸长程洄游。" + ORDER_NOTE + "：洄游为 lifecycle "
        "premise 配置级，无面内判断链。单因子链，低盐高浊为因子绑定值。",
        "CoastalSoloHunterMackerel"),
    resp_typed(
        "SPM",
        ["solo_hunting = 单独猎击（『hunts alone in shallow coastal waters』——"
         "负知识：非群游协作）"],
        "小鱼/鱿/虾 typed 摄食响应：『Feed primarily on small fishes like anchovies, "
        "clupeids, carangids, also squids and penaeoid shrimps』+高速追击单独猎击 "
        "typed（鳡鱼 R03 中上层追猎同构先例）。" + ORDER_NOTE + "：无判断顺序描述。",
        "SoloFastStrikeHunter"),
    # ---------------- YFT 黄旗金枪鱼 ----------------
    bake_single(
        "YFT",
        ["lifecycle = OCEANIC_HIGHLY_MIGRATORY",
         "school_structure = 体型分级群游（『Adults school primarily by size』）+"
         "海豚/漂浮物关联（FAD 型遇鱼分布）——群结构事实 premise 非互斥 FishGroup 供给"],
        "温跃层上下洋面分布+高洄游。" + ORDER_NOTE + "：洄游/洄游阶段为 premise 配置"
        "级，无面内判断链。单因子链。体型分级群游与 FAD 关联=群结构事实（SDG/CBM "
        "同型判例）。",
        "OceanicSizeSchoolTuna"),
    resp_typed(
        "YFT",
        [],
        "鱼/甲壳/鱿 typed 摄食响应：『Feed on fishes, crustaceans and squids』。"
        + ORDER_NOTE + "：无判断顺序描述（洋面群鱼 typed 单 evaluator）。",
        "OceanicPelagicPredator",
        opn=["海豚关联/漂浮物 FAD 供给语义=Story Open Question"]),
    # ---------------- STM 条纹四鳍旗鱼 ----------------
    bake_single(
        "STM",
        ["temp_affinity = 善冷水偏好（比黑/蓝马林偏冷水——因子绑定值）",
         "nearshore_rule = 近岸仅在深陡降处（near shore only where deep drop-offs）"],
        "温跃层上层洋面+冷水偏好+近岸深陡降分布。" + ORDER_NOTE + "：静态栖息因子绑定"
        "（温度带+深度规则），无时序无判断链。单因子链。与旗鱼 SAF 同构（不同温度带"
        "绑定值）。",
        "CoolerWaterBillfish"),
    resp_typed(
        "STM",
        [],
        "鱼/甲壳/鱿 typed 摄食响应：『Feed on fishes, crustaceans and squids』。喙击打"
        "行为本种页未述（S2 EO——不构本种 typed context，旗鱼属例不外推）。" +
        ORDER_NOTE + "：无判断顺序描述。",
        "CoolerBillfishHunter",
        opn=["本种喙击打行为引文 EO（旗鱼 SAF 例不外推——typed context 需本种证据）"]),
    # ---------------- ALB 长鳍金枪鱼 ----------------
    bake_single(
        "ALB",
        ["depth_range = 上层-600m 分布带",
         "mixed_school = 与 skipjack/yellowfin/bluefin 混群+马尾藻漂浮物关联（多物种"
         "同场供给+漂浮物——群结构事实 premise）"],
        "洋面-600m 分布+混群。" + ORDER_NOTE + "：分布带为因子绑定，无时序无判断链。"
        "单因子链。雌雄分离分布=lifecycle 分布 premise。",
        "MixedSchoolAlbacore"),
    resp_typed(
        "ALB",
        [],
        "鱼/甲壳/鱿 typed 摄食响应：『Feed on fishes, crustaceans and squids』。"
        + ORDER_NOTE + "：无判断顺序描述。金枪鱼属第 4 例同构（typed context 差异"
        "非结构差异）。",
        "RunfightOceanicTuna"),
    # ---------------- STL 硬头鳟 ----------------
    bake_single(
        "STL",
        ["life_history_type = ANADROMOUS_ITEROPAROUS 同种双型（steelhead 海-河 vs "
         "虹鳟定居『genetically identical but separated by life history "
         "strategies』——生活史策略 premise；可重复产卵 iteroparity）"],
        "海-河双阶段分布（海期近岸+溯河产卵往返多次）。" + ORDER_NOTE + "：海-河往返"
        "时序为 lifecycle premise 配置级（P05：真实生命周期差异≠必须预分供给），无面"
        "内判断链。单因子链。",
        "AnadromousIteroparousTrout"),
    resp_typed(
        "STL",
        [],
        "海期鱿/甲壳/小鱼 typed 摄食响应：『their diet typically consists of squid, "
        "crustaceans, and small fish including anchovies, herring, and sardines』。"
        + ORDER_NOTE + "：无判断顺序描述。双型不拆 Group（遗传同种）。",
        "OceanPhaseSalmonid",
        opn=["双型共存供给语义=Story Open Question（P05 判例域）"]),
    # ---------------- ARG 北极茴鱼 ----------------
    bake_single(
        "ARG",
        ["habitat = 冷水高氧清河湖敞水（clear, cold, medium to large rivers and lakes）",
         "seasonal_move = 季节领土/下游移动（P05 季节 premise）"],
        "冷水清河湖敞水分布+季节移动。" + ORDER_NOTE + "：季节领土/下游为季节周期 "
        "premise 配置级，无面内判断链。单因子链。",
        "ColdClearWaterGrayling"),
    resp_typed(
        "ARG",
        ["surface_presentation = 水面呈现 typed（surface insects + 落水猎物——旅鼠"
         "lemmings 为水面/落水输入）",
         "dorsal_display = 大背鳍求偶展示（『displaying his large dorsal fin, curving "
         "it over her』——繁殖信号非捕食程序输入，S6 排除）"],
        "水面昆虫+鱼+旅鼠 typed 摄食响应：『feed mainly on surface insects but also "
        "take in fishes, fish eggs, lemmings, and planktonic crustaceans』。无 redd=产卵"
        "行为变量（lifecycle）：" + ORDER_NOTE + "：无面内判断顺序描述（水面 typed "
        "单 evaluator）；背鳍展示为求偶信号不入摄食程序。",
        "SurfaceInsectFeederGrayling",
        opn=["旅鼠水面捕食语义=Story Open Question（水面落物输入 vs 陆基猎物）"]),
    # ---------------- LKT 湖红点鲑 ----------------
    bake_single(
        "LKT",
        ["depth_band = 深湖 18-53m 绑定"],
        "深湖 18-53m 分布。" + ORDER_NOTE + "：静态栖息单因子（深度带绑定），无时序"
        "无判断链。单因子链。",
        "DeepLakeChar"),
    resp_typed(
        "LKT",
        ["light_regime = 夜行（S7 MSF——低光 typed context，R03 先例不买 Night Mode）",
         "spawn_timing = 夜行产卵黄昏-22 时高峰+雄先到清岩（繁殖时段/准备行为 "
         "lifecycle premise 非护巢证据）"],
        "深湖广食 typed 摄食响应：『feed on a variety of organisms such as freshwater "
        "sponges, crustaceans, insects, fishes』+夜行 context。" + ORDER_NOTE + "：无"
        "判断顺序描述（夜行=时间 context 非门）；雄清岩为产卵准备行为（S6）非持续"
        "守护证据，不构 P04。",
        "DeepLakeNocturnalFeeder"),
    # ---------------- RHM 红钩鱼 ----------------
    bake_single(
        "RHM",
        ["habitat = 主河静水悬岸植被区（『calm zones of main rivers where the "
         "vegetation hangs over the river banks』——ResourcePatch P02 背景语义）"],
        "主河静水悬岸植被区分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。"
        "单因子链。植被区=Resource Patch 背景语义（P02 两层登记非 census 族）。",
        "OverhangingVegetationHerbivore"),
    resp_typed(
        "RHM",
        ["herbivory = 河岸植物叶取食（『Adults feed on the leaves of river plants』"
         "trophic 2.0——离散善件型植物目标 typed；食人鱼科 Serrasalmidae 植食反差例；"
         "植食不买 Mode 草鱼 R02 grazing 先例）"],
        "植物叶取食 typed 摄食响应。" + ORDER_NOTE + "：无判断顺序描述（单 typed "
        "evaluator 植物叶目标）。Traumatogenic 强齿=形态事实非程序。",
        "LeafFeedingSerrasalmid",
        opn=["植食行为细节开放（Story Open Question）"]),
    # ---------------- RBP 淡水白鲳 ----------------
    bake_single(
        "RBP",
        ["lifecycle = POTAMODROMOUS（河内洄游 premise）"],
        "河湖分布。" + ORDER_NOTE + "：静态栖息单因子+洄游 premise，无判断链。单因子链。",
        "RiverLakePacu"),
    resp_typed(
        "RBP",
        ["juvenile_mimicry = 幼体拟态红腹食人鱼（Pygocentrus nattereri 拟态——反捕食"
         "策略非摄食程序，S9 premise）"],
        "虫+腐植物杂食 typed 摄食响应：『Adults feed on insects and decaying plants』"
        "（trophic 2.5）。" + ORDER_NOTE + "：无判断顺序描述。幼体拟态=反捕食（S7/S9 "
        "排除）。",
        "InsectDetritusPacu",
        opn=["幼体拟态行为引文开放（Story Open Question）"]),
    # ---------------- TMU 虎纹梭鱼 ----------------
    bake_single(
        "TMU",
        ["identity = STERILE_HYBRID（库锚学名即杂交式 E. lucius × E. masquinongy——"
         "Identity Deferred premise；机制复用亲本狗鱼属）",
         "stocked_supply = 人工投放供给（多州 stocked——非自然分布 premise）"],
        "狗鱼系植被静水分布（亲本型复用推算）。" + ORDER_NOTE + "：静态栖息单因子（亲本"
        "型绑定），无判断链。单因子链。投放供给=人工引入型遇鱼分布（Story Open）。",
        "EsoxAmbushHybrid"),
    resp_typed(
        "TMU",
        ["identity = STERILE_HYBRID（杂交身份边界——红罗非 R03 先例同型；机制复用"
         "亲本狗鱼属伏击型）"],
        "狗鱼系伏击 typed 摄食响应（亲本复用推算——本种页无独立食性引文，杂交种机制"
        "复用亲本 Esox 伏击型 P01）。" + ORDER_NOTE + "：无判断顺序描述（伏击 typed "
        "单 evaluator）。身份/供给语义留裁决。",
        "EsoxAmbushHybridResp",
        conf="MEDIUM",
        opn=["杂交种身份边界裁决=Identity Deferred（FR 线）；人工投放供给语义=Story "
             "Open；亲本复用推算非本种引文——MEDIUM"]),
    # ---------------- SPK 萨克拉门托大斑狗鱼 ----------------
    bake_single(
        "SPK",
        ["habitat = 岩沙池潭（rocky and sandy pools and runs）"],
        "岩沙池潭分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。"
        "名实分离（中文名大斑狗鱼/学名鲤科 Ptychocheilus）——机制照实际分类学。",
        "RockyPoolPikeminnow"),
    resp_typed(
        "SPK",
        ["ontogeny = 幼-成相食（幼鱼微生境受大鱼重提——幼鱼为合法猎物类型 premise）"],
        "狗鱼型掠食 typed 摄食响应：成鱼『voracious pike-like habits』（鲤科大型掠食"
        "——名实分离样本，鳡鱼 R03 鲤科掠食同型）。" + ORDER_NOTE + "：无判断顺序描述。",
        "PikeLikeCyprinidPredator"),
    # ---------------- DTN 裸狐鲣 ----------------
    bake_single(
        "DTN",
        ["habitat = 礁栖（『An offshore species found mainly around coral reefs』——"
         "金枪鱼科内栖息反差例：礁栖 vs 洋栖）"],
        "珊瑚礁分布（礁栖金枪鱼型）。" + ORDER_NOTE + "：静态栖息单因子（礁绑定），无"
        "时序无判断链。单因子链。",
        "ReefResidentTuna"),
    resp_typed(
        "DTN",
        [],
        "小群鱼/鱿 typed 摄食响应：『Preys on small schooling fishes such as "
        "Decapterus, Caesio, Nasio...and squids』（猎物群游取向 typed）。" +
        ORDER_NOTE + "：无判断顺序描述。ciguatoxic=人类侧食物安全 S11 排除（CB 轴）。",
        "ReefSchoolFishHunter",
        opn=["礁栖 vs 洋栖供给语义=Story Open Question"]),
    # ---------------- GAJ 高体鰤 ----------------
    bake_single(
        "GAJ",
        ["habitat = 深礁 18-72m 绑定",
         "summer_spawn = 夏季近岸产卵（Spawning happens during the summer, in areas "
         "near the coast——季节繁殖 premise 重排）"],
        "深礁分布+夏季近岸产卵重排。" + ORDER_NOTE + "：夏季近岸产卵为季节繁殖周期 "
        "premise 配置级（P05），无面内判断链。单因子链。",
        "DeepReefAmberjack"),
    resp_typed(
        "GAJ",
        [],
        "鱼主食 typed 摄食响应：『They feed primarily on fishes such as the bigeye "
        "scad, also on invertebrates』。" + ORDER_NOTE + "：无判断顺序描述。"
        "ciguatera=CB 轴 S11 排除。",
        "DeepReefPiscivore"),
    # ---------------- HAD 黑线鳕 ----------------
    bake_single(
        "HAD",
        ["depth_band = 80-200m 绑定", "temp_band = 4-10°C",
         "substrate = 岩/沙/砾/贝壳底"],
        "中深岩沙贝壳底分布。" + ORDER_NOTE + "：静态栖息因子绑定（深度/水温/底质复合"
        "绑定值），无时序无判断链。单因子链。",
        "MidDepthBottomGadoid"),
    resp_typed(
        "HAD",
        [],
        "底栖小生物 typed 摄食响应：『feed mainly on small bottom-living organisms "
        "including crustaceans, mollusks, echinoderms, worms and fishes』。" +
        ORDER_NOTE + "：无判断顺序描述。鳕科第 2 例（大西洋鳕 B01 同构）。",
        "BottomForagerGadoid"),
    # ---------------- BPB 眼点丽鱼 ----------------
    bake_single(
        "BPB",
        ["habitat = 急流+静水中深岩底（in the rapids, in quiet waters with medium "
         "depth and rocky substrates）"],
        "急流/静水中深岩底分布。" + ORDER_NOTE + "：静态栖息复合绑定，无时序无判断链。"
        "单因子链。",
        "RapidsRockCichlid"),
    resp_typed(
        "BPB",
        [],
        "纯鱼食 typed 摄食响应：『Food consists of only small fish, especially "
        "threadfin shad, mosquito fish, tilapia and bluegill』。" + ORDER_NOTE + "："
        "无判断顺序描述。Cichla 属第 2 例（与奥里诺科 R07 对照）；成群=遇鱼分布背景"
        "非互斥供给。",
        "ExclusivePiscivoreCichlid"),
    # ---------------- RVC 小须美鱥 ----------------
    bake_single(
        "RVC",
        ["habitat = 岩池急流（rocky runs and flowing pools of small to medium rivers）"],
        "岩池急流分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "RockyRunChub"),
    resp_typed(
        "RVC",
        ["stone_nest_hypothesis = 石巢行为本种页未述（同属 Nocomis biguttatus R07 石巢"
         "先例——EO 假说不写为事实，不构 P04 程序）"],
        "底栖 typed 摄食响应（食性面 FishBase 无述 S1 EO——P01 冻结主张承载，trophic "
        "3.2 推算，MEDIUM）。" + ORDER_NOTE + "：无判断顺序描述；石巢假说 EO 不立面。",
        "CongenericChubDefault",
        conf="MEDIUM",
        opn=["食性无述（S1 EO）——MEDIUM；本种石巢行为引文 EO（同属先例假说，若证实"
             "则 P04 同型——不预立）"]),
    # ---------------- CRC 黑斑须雅罗鱼 ----------------
    bake_single(
        "CRC",
        ["habitat = 头源小溪岩沙池潭（Mostly found in tiny, intermittent streams）"],
        "头源小溪分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "HeadwaterCreekChub"),
    resp_guard(
        "CRC",
        ["guard_condition = 雄鱼砾巢脊连续建造+护巢（『digs a pit…removing mouthful "
         "of gravel』产卵后覆石→紧邻下游再挖新坑→形成 long ridge of gravel——连续"
         "建造持续守护，P04 契约 pre-existing/persistent）",
         "guard_anchor = GRAVEL_RIDGE（巢脊 anchor 提案——石巢系第 3 例：双点美鱥 "
         "R07 Nocomis + 本例 Semotilus 独立属独立演化重复）",
         "ontogeny = 幼无脊椎→成鱼/螯虾（阶段 premise）"],
        "头源掠食 typed 摄食（Young feed on small aquatic invertebrates while adults "
        "consume small fish, crayfish and other large invertebrates）+ 雄鱼砾巢脊守护："
        "对靠近目标摄食 Path ∥ 巢脊威胁评估 Path。" + ORDER_NOTE + "：幼-成食性变化="
        "ontogeny premise 非分支；巢脊建造时序（挖坑→覆石→再挖）为建造行为事件序列"
        "非面内判断链——守护按 P04 契约并行双 Path。",
        "gravel_ridge（雄砾巢脊连续建造）",
        "GravelRidgeGuarderChub",
        opn=["巢脊 vs 双点美鱥巢丘的 P04 表达差异=Story Open Question（anchor 轴值"
             "提案 gravel_ridge——脊形连续建造 vs 丘形单体）"]),
    # ---------------- INC 白北鲑 ----------------
    bake_single(
        "INC",
        ["lifecycle = ANADROMOUS_FASTING_RUN（『During spawning migration, it feeds "
         "little if at all』溯河洄游期几乎停食——停食洄游第 3 例：P05 状态抑制 "
         "Feeding Path，判例明言不落 P04 不立新结构）",
         "ice_break_trigger = 融冰触发上溯（Upstream migration begins at ice "
         "break-up——季节触发 premise）"],
        "河-海分布+融冰上溯洄游。" + ORDER_NOTE + "：融冰→上溯→停食→黄昏夜产为 "
        "lifecycle 阶段时序 premise 配置级（P05 状态抑制——停食是洄游期状态非面内"
        "分支），无面内判断链。单因子链。",
        "FastingRunWhitefish"),
    resp_typed(
        "INC",
        ["fasting_state = 洄游期停食（P05 状态抑制 Feeding Path——停食期咬钩非摄食"
         "响应，动机归因开放）",
         "ontogeny = 幼虫幼/浮游甲壳→成小鱼（阶段 premise）"],
        "成鱼食小鱼 typed 摄食响应：『Adults feed mostly on small fishes; young eat "
        "aquatic insect larvae and planktonic crustaceans』。" + ORDER_NOTE + "：无"
        "判断顺序描述；停食状态为 P05 premise（状态抑制），非程序分支。",
        "PiscivoreWhitefish",
        opn=["停食咬钩动机归因=Story Open Question（P05 判例：洄游期非摄食可钓性="
             "multi-path 语义留 Representation 裁决）"]),
    # ---------------- HBW 驼背白鲑 ----------------
    bake_single(
        "HBW",
        ["lifecycle = 1200KM_INLAND_SPAWNING_RUN + 部分种群不出海（『some never go "
         "to sea at all』——同种生活史多样 premise，硬头鳟双型判例第 3 例）",
         "habitat = 近岸/河下/大湖/洪泛湖/河口成淡水多生境"],
        "多生境分布+1200km 溯河产卵。" + ORDER_NOTE + "：溯河/不出海型为生活史策略 "
        "premise 配置级（P05：真实生命周期差异≠必须预分供给），无面内判断链。单因子链。",
        "DualMigrationWhitefish"),
    resp_typed(
        "HBW",
        [],
        "底栖 typed 摄食响应：『Adults feed mostly on mollusks, crustaceans and "
        "chironomid larvae』。" + ORDER_NOTE + "：无判断顺序描述。",
        "BenthivoreWhitefish",
        opn=["双型共存供给语义=Story Open Question"]),
    # ---------------- CLC 大口鲶 ----------------
    bake_single(
        "CLC",
        ["endemism = 长江中游特有（Silurus meridionalis 分布绑定）"],
        "长江中游分布。" + ORDER_NOTE + "：静态栖息单因子（地域特有绑定），无时序无"
        "判断链。单因子链。",
        "YangtzeCatfish"),
    resp_typed(
        "CLC",
        ["congeneric_inference = 同属 Silurus 推算（trophic 4.2——欧洲巨鲶 R06 伏击"
         "型先例；食性面本种无述）"],
        "同属推算伏击 typed 摄食响应（食性面 FishBase 无述 S1 EO——同属推算承载，"
        "MEDIUM）。" + ORDER_NOTE + "：无判断顺序描述；夜行为同属假说（S7 EO）不构"
        "typed context。",
        "SilurusAmbushDefault",
        conf="MEDIUM",
        opn=["食性/繁殖面无述（S1/S6 EO）——同属推算 MEDIUM；夜行同属假说（S7 EO）"]),
    # ---------------- RTC 红尾鲶 ----------------
    bake_single(
        "RTC",
        ["lifecycle = POTAMODROMOUS（河内洄游 premise）"],
        "亚马逊/奥里诺科河底分布。" + ORDER_NOTE + "：静态栖息单因子+洄游 premise，无"
        "判断链。单因子链。",
        "RiverBottomCatfish"),
    resp_typed(
        "RTC",
        ["fruit_input = 果实=沉水植物果实输入（『Adults feed on fish, crabs and "
         "fruits』——暹罗巨鲤 R05 果食窗同型输入：果实为 typed 猎物类型）"],
        "鱼/蟹/果杂食 typed 摄食响应。" + ORDER_NOTE + "：无判断顺序描述（杂食 typed "
        "单 evaluator，果实为猎物类型非分支）。",
        "OmnivoreGameCatfish",
        opn=["果实摄食季节面开放（Story Open Question）"]),
    # ================= R09 =================
    # ---------------- WST 高首鲟 ----------------
    bake_single(
        "WST",
        ["lifecycle = ANADROMOUS（『Spends most of its time in the sea, usually "
         "close to shore』+『Enters estuaries…moves far inland to spawn』海-河洄游 "
         "premise）",
         "pre_spawn_fasting = 产卵前停食（『Feeding ceases just before spawning』——"
         "停食洄游判例第 4 例：P05 状态抑制，不落 P04 不立新结构）",
         "spawn_interval = 4-11 年产卵间隔（lifecycle 节奏 premise）"],
        "海近岸-河口-大河分布。" + ORDER_NOTE + "：海→河口→上溯→停食→产卵为 lifecycle "
        "阶段时序 premise 配置级（P05 状态抑制），无面内判断链。单因子链。",
        "GiantAnadromousSturgeon"),
    resp_typed(
        "WST",
        ["ontogeny = 体型分级鱼食（『Individuals larger than 48.3 cm feed mainly on "
         "fishes』小个体摇蚊/甲壳/虫/软体——阶段 premise）"],
        "体型分级鱼食 typed 摄食响应（成体主鱼食）。" + ORDER_NOTE + "：无判断顺序"
        "描述；体型分级为 ontogeny premise 非分支。VU/CITES II=产品供给面边界。",
        "SizeGradedPiscivoreSturgeon",
        opn=["产卵前停食机制开放（Story Open Question）；保护边界=OPS 层"]),
    # ---------------- ROB 岩钝鲈 ----------------
    bake_single(
        "ROB",
        ["habitat = 岩区浅水（rocky areas in shallow water of lakes…lower, warm "
         "reaches of streams）"],
        "湖泊岩区+溪流温暖下游浅水分布。" + ORDER_NOTE + "：静态栖息单因子（岩区+浅水"
        "复合绑定），无时序无判断链。单因子链。",
        "RockShallowSunfish"),
    resp_guard(
        "ROB",
        ["guard_condition = 雄鱼巢护卵约 14 天+护幼（『males fan and defend the "
         "nests』扇护+防御复合持续守护，P04 契约 pre-existing/persistent）",
         "guard_anchor = ROCK_NEST_FAN（雄巢扇护 anchor 提案——太阳鱼系巢护型）",
         "mating_system = 一巢多雌（繁殖系统注记 premise——多雌产卵于同巢）"],
        "小甲壳/虫/鱼 typed 摄食（『Feeds on small crustaceans, insects and fish』）+ "
        "雄鱼巢扇护守护：对靠近目标摄食 Path ∥ 巢/幼威胁评估 Path。" + ORDER_NOTE +
        "：扇护（fan）与防御（defend）为守护 Path 内复合子动作（供氧+御敌）非新增"
        "branch——拓扑保持 P04 契约并行双 Path，扇护子动作记 open。",
        "rock_nest_fan（雄巢扇护+防御 14 天）",
        "RockNestGuarderSunfish",
        opn=["fan 扇护子动作（供氧行为）是否=guard Path 内 typed 子步 vs 新结构元素"
             "——留判同阶段裁决；一巢多雌=mating system premise 非程序"]),
    # ---------------- KGO 接吻鲷 ----------------
    bake_single(
        "KGO",
        ["habitat = 静水植被",
         "air_breathing = 气呼吸（runtime 生理条件 premise，肺鱼先例不买 Mode）"],
        "静水植被分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "StillwaterVegetationGourami"),
    resp_typed(
        "KGO",
        ["kissing_behavior = 接吻行为（『habit of sucking its lips and kissing other "
         "fishes, plants and other objects』——觅食器官功能假说争议 EO 不写为事实；"
         "口部动作变量非新机会语义）"],
        "绿藻/浮游/水面昆虫杂食 typed 摄食响应。" + ORDER_NOTE + "：无判断顺序描述；"
        "接吻器功能假说 EO 不构程序输入（Story Confidence Medium 来源，记 open）。",
        "LipKissingOmnivore",
        opn=["接吻器功能假说引文（觅食器官 vs 展示/领地——功能争议未决）"]),
    # ---------------- LMD 斑鳜 ----------------
    bake_single(
        "LMD",
        ["habitat = 同属岩区推断（Siniperca 属栖息推断——食性/栖息面本种 DD）"],
        "同属岩区分布（推断）。" + ORDER_NOTE + "：静态栖息推断绑定，无时序无判断链。"
        "单因子链。DD 数据缺。",
        "SinipercaRockHabitat"),
    resp_typed(
        "LMD",
        ["congeneric_inference = 同属推算（trophic 4.0——鳜鱼 R03 伏击鱼食先例；食性"
         "面本种无述）"],
        "同属推算伏击 typed 摄食响应（食性面 EO——鳜属结构伏击同构推算，MEDIUM）。"
        + ORDER_NOTE + "：无判断顺序描述。",
        "CongenericAmbushMandarin",
        conf="MEDIUM",
        opn=["食性面无述（S1 EO 同属推算）——MEDIUM；DD 数据补全开放"]),
    # ---------------- MDC 米达斯慈鲷 ----------------
    bake_single(
        "MDC",
        ["habitat = 岩壁运河（box-cut canals with rocky vertical sides）/岩礁"],
        "岩壁运河/岩礁分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。"
        "单因子链。",
        "CanalRockCichlid"),
    resp_guard(
        "MDC",
        ["guard_condition = 双亲护卵幼数周（biparental——双亲持续守护，P04 契约 "
         "pre-existing/persistent）",
         "guard_anchor = CAVE_CEILING（『Spawn preferentially on the ceiling of "
         "natural caves』洞顶产卵 anchor 提案——洞穴变体）",
         "guard_participant = BIPARENTAL（双亲参与——vs 雄性单亲，参与者轴值）"],
        "aufwuchs/螺/小鱼杂食 typed 摄食 + 洞顶产卵双亲守护：对靠近目标摄食 Path ∥ "
        "洞顶卵幼威胁评估 Path。" + ORDER_NOTE + "：产卵位选择（洞顶）为 anchor 绑定"
        "非程序分支；双亲参与=守护参与者轴值——拓扑保持 P04 契约并行双 Path，差异"
        "留判同阶段。",
        "cave_ceiling（洞顶产卵双亲护）",
        "CaveCeilingBiparentalGuarder",
        opn=["P04 洞穴变体表达差异（anchor 轴值提案 cave_ceiling + participant 轴值"
             "biparental）=Story 自记『P04 内部结构多样性』——参数轴 vs 结构差异留"
             "判同阶段裁决"]),
    # ---------------- JGC 淡水石斑 ----------------
    bake_single(
        "JGC",
        ["habitat = 浊水富营养湖泥底（turbid waters and mud bottoms of the highly "
         "eutrophic lakes）"],
        "浊水湖泥底分布。" + ORDER_NOTE + "：静态栖息单因子（浊度+泥底复合绑定），无"
        "时序无判断链。单因子链。",
        "TurbidLakeCichlid"),
    resp_guard(
        "JGC",
        ["guard_condition = 双亲护卵幼（5000-10000 卵——biparental 持续守护，P04 "
         "契约）",
         "guard_anchor = BIPARENTAL_PAIR（双亲 anchor——anchor 轴值提案）",
         "guard_participant = BIPARENTAL"],
        "浊水湖小鱼/大型无脊椎 typed 摄食（『Highly predaceous, feeding mainly on "
        "small fishes and macroinvertebrates』）+ 双亲守护：对靠近目标摄食 Path ∥ "
        "卵幼威胁评估 Path。" + ORDER_NOTE + "：无面内判断顺序描述；双亲参与=参与者"
        "轴值（与米达斯同型）——拓扑保持 P04。",
        "biparental_pair（双亲护卵幼）",
        "TurbidBiparentalPredator",
        opn=["双亲 participant 轴值（与 MDC 同型）——参数轴 vs 结构差异留判同阶段"]),
    # ---------------- SPC 金目丽鱼 ----------------
    bake_single(
        "SPC",
        ["habitat = 深湾湖岸（deep bays and lake shore zones）"],
        "深湾湖岸分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "DeepBayCichla"),
    resp_typed(
        "SPC",
        [],
        "characid 鱼食 typed 摄食响应：『mainly on small fish (especially characids "
        "measuring <10 cm SL)』。" + ORDER_NOTE + "：无判断顺序描述。Cichla 属第 3 例"
        "（奥里诺科 R07/眼点 R08/本例——同构重复）。护巢未述（S6 EO）不构 P04。",
        "CharacidPiscivoreCichla"),
    # ---------------- TGT 虎纹鳟鱼 ----------------
    bake_single(
        "TGT",
        ["identity = STERILE_HYBRID（库锚学名即杂交式 Salmo trutta × Salvelinus "
         "fontinalis——Identity Deferred premise；机制复用亲本鲑鳟系）",
         "stocked_supply = 人工投放供给 premise"],
        "亲本系栖息分布（鲑鳟溪流复用推算）。" + ORDER_NOTE + "：静态栖息推断绑定，无"
        "判断链。单因子链。虎纹梭鱼 R08 判例第 2 例。",
        "HybridSalmonidStocked"),
    resp_typed(
        "TGT",
        ["identity = STERILE_HYBRID（杂交身份边界——虎纹梭鱼 R08 判例第 2 例；机制"
         "复用亲本系 P01）"],
        "亲本系 P01 复用 typed 摄食响应（伏击/漂流推算——本页无独立食性引文）。" +
        ORDER_NOTE + "：无判断顺序描述。身份/投放语义留裁决。",
        "ParentalSalmonidDefault",
        conf="MEDIUM",
        opn=["杂交身份裁决=Identity Deferred；投放供给语义=Story Open；亲本复用推算"
             "非本种引文——MEDIUM"]),
    # ---------------- HYC 工程鲫 ----------------
    bake_single(
        "HYC",
        ["identity = TRIPLOID_ENGINEERED（库锚 Carassius auratus (triploid) 三倍体"
         "工程杂交——Identity Deferred premise；机制复用鲫系）",
         "aquaculture_supply = 养殖供给 premise"],
        "鲫系底栖分布（养殖型复用推算）。" + ORDER_NOTE + "：静态栖息推断绑定，无判断"
        "链。单因子链。与银鲫自然三倍对照（自然 vs 工程）。",
        "EngineeredCrucian"),
    resp_typed(
        "HYC",
        ["identity = TRIPLOID_ENGINEERED（工程三倍体身份边界——杂交第 3 例；机制"
         "复用鲫系 P01 底栖杂食）"],
        "鲫系 P01 底栖杂食复用 typed 摄食响应（复用推算）。" + ORDER_NOTE + "：无判断"
        "顺序描述。三倍体不育=lifecycle premise。",
        "CrucianBottomOmnivore",
        conf="MEDIUM",
        opn=["工程鲫身份裁决=Identity Deferred；复用推算非本种引文——MEDIUM"]),
    # ---------------- PRC 银鲫 ----------------
    bake_single(
        "PRC",
        ["gynogenesis = 雌核发育（『Able to reproduce from unfertilized eggs "
         "(gynogenesis)』+精寄生 sperm parasites——繁殖系统变量 premise 非程序分支；"
         "欧洲种群三倍体全雌）",
         "tolerance = 低氧/污染耐受（runtime 生理条件 premise）"],
        "广适底层多生境分布。" + ORDER_NOTE + "：雌核发育/三倍全雌为繁殖系统 lifecycle "
        "premise 配置级，无面内判断链。单因子链。",
        "GynogeneticAllFemale"),
    resp_typed(
        "PRC",
        [],
        "底栖杂食 typed 摄食响应：浮游/底栖无脊椎/植物/腐屑。" + ORDER_NOTE + "：无"
        "判断顺序描述。雌核发育=繁殖系统变量（R09 FR 判例：非呈现轴）。",
        "BottomOmnivorePrussian",
        opn=["雌核发育供给语义=Story Open Question"]),
    # ---------------- CCR 金鲫 ----------------
    bake_single(
        "CCR",
        ["dormancy = 干冬钻泥（dried-out winter mud-burrowing——蛰伏家族第 5 例："
         "P05 状态 premise，肺鱼/塘鳢判例同类）",
         "habitat = 植被静水"],
        "植被静水分布+干冬钻泥状态重排。" + ORDER_NOTE + "：干冬钻泥为季节/状态周期 "
        "premise 配置级（P05 状态抑制），无面内判断链。单因子链。",
        "MudBurrowerCrucian"),
    resp_typed(
        "CCR",
        ["light_regime = 夜行（『mainly at night』——低光 typed context，R03 先例"
         "不买 Night Mode）"],
        "夜行底栖杂食 typed 摄食响应：浮游/底栖无脊椎/植物/腐屑。" + ORDER_NOTE + "："
        "无判断顺序描述（夜行=时间 context 非门）。鲫系 3 例同构。",
        "NocturnalBottomCrucian"),
    # ---------------- APA 阿帕奇鳟 ----------------
    bake_single(
        "APA",
        ["habitat = 2500m+ 山地源头清冷溪流（clear, cool mountain headwaters）",
         "conservation = CR（95% 河段减少——OPS 产品供给面边界 premise）"],
        "高山源头清冷溪流分布。" + ORDER_NOTE + "：静态栖息单因子（海拔带绑定），无"
        "时序无判断链。单因子链。与虹鳟杂交威胁=身份边界注记。",
        "HeadwaterNativeTrout"),
    resp_typed(
        "APA",
        [],
        "山地溪流 typed 摄食响应（S1 MSF 为栖息推断承载——正文无食性具体引文，"
        "鳟系溪流食性推断，MEDIUM）。" + ORDER_NOTE + "：无判断顺序描述。",
        "MountainStreamTrout",
        conf="MEDIUM",
        opn=["食性具体引文未引（S1 MSF=栖息推断承载）——MEDIUM；保护限制下钓法语义"
             "开放；杂交威胁边界注记"]),
    # ---------------- GOT 金鳟 ----------------
    bake_single(
        "GOT",
        ["habitat = 2100m+ 高山清冷溪湖（Kern 河上游特有）"],
        "高山溪湖分布。" + ORDER_NOTE + "：静态栖息单因子（海拔带绑定），无时序无"
        "判断链。单因子链。",
        "HighElevationGoldenTrout"),
    resp_typed(
        "GOT",
        [],
        "高山溪流 typed 摄食响应（食性面无述 S1 EO——P01 冻结主张承载，MEDIUM；"
        "稀有鳟系 3 例同构推断）。" + ORDER_NOTE + "：无判断顺序描述。",
        "HighElevationTrout",
        conf="MEDIUM",
        opn=["食性面无述（S1 EO）——稀有鳟系同构推断 MEDIUM"]),
    # ---------------- GIT 吉拉鳟 ----------------
    bake_single(
        "GIT",
        ["habitat = 2000m+ 清冷山地溪流（Gila 河系特有）",
         "conservation = EN（OPS 产品供给面边界 premise）"],
        "山地溪流分布。" + ORDER_NOTE + "：静态栖息单因子（海拔带绑定），无时序无"
        "判断链。单因子链。",
        "GilaHeadwaterTrout"),
    resp_typed(
        "GIT",
        [],
        "山地溪流 typed 摄食响应（食性面无述 S1 EO——P01 冻结主张承载，MEDIUM；"
        "稀有鳟系第 3 例同构推断）。" + ORDER_NOTE + "：无判断顺序描述。",
        "HeadwaterTroutDefault",
        conf="MEDIUM",
        opn=["食性面无述（S1 EO）——同构推断 MEDIUM"]),
    # ---------------- SVT 塞凡湖鳟 ----------------
    bake_single(
        "SVT",
        ["lake_endemic = 塞凡湖特有（湖内完成生活史——非洄游型鲑系负知识）",
         "seasonal_move = 季节近岸/深水移动（P05 季节 premise）",
         "dual_stock = 双种群不同角落/季节分离产卵（11-12 月与 1-3 月——同种空间"
         "时间分离 premise）"],
        "湖内分布+季节深浅移动。" + ORDER_NOTE + "：季节移动与双种群分离产卵为 "
        "lifecycle/季节 premise 配置级（P05），无面内判断链。单因子链。",
        "LakeEndemicDualStock"),
    resp_typed(
        "SVT",
        ["prey_specialization = 端足类专食（『feed exclusively on sand hoppers "
         "(Amphipoda)』——专食 typed context）"],
        "端足类专食 typed 摄食响应。" + ORDER_NOTE + "：无判断顺序描述（专食 typed "
        "单 evaluator）。CR 保护边界=OPS 层。",
        "AmphipodSpecialistTrout",
        opn=["双种群分离供给语义=Story Open Question；CR 限制钓法语义开放"]),
    # ---------------- PEL 高白鲑 ----------------
    bake_single(
        "PEL",
        ["life_history_tri_form = 湖-河-溯河三型（同种生活史多样 premise——驼背白鲑 "
         "R08 双型判例扩展第 4 例）"],
        "湖泊分布（三型生活史 premise）。" + ORDER_NOTE + "：三型为生活史策略 premise "
        "配置级（P05：真实生命周期差异≠必须预分供给），无面内判断链。单因子链。",
        "TriFormWhitefish"),
    resp_typed(
        "PEL",
        [],
        "三态食性 typed 摄食响应：浮游/底栖/水面昆虫（食性 breadth typed——三态为"
        "猎物层 breadth 非分级门）。" + ORDER_NOTE + "：无判断顺序描述；三态食性=typed "
        "context 非分支。",
        "TriModalWhitefish",
        opn=["三型供给语义=Story Open Question（P05 判例域）"]),
    # ---------------- CMR 常见拟鲤 ----------------
    bake_single(
        "CMR",
        ["habitat = 低地湖泊河湾绑定",
         "seasonal = 冬深水（季节 premise）",
         "spawn_shoal = 浅水植被群产（繁殖集群 premise——非互斥 FishGroup）",
         "identity_note = 库级重复身份第 2 例（与湖拟鲤同 Rutilus rutilus 双行——"
         "待 Cross-Batch 合并）"],
        "低地湖泊河湾分布+冬深水季节重排。" + ORDER_NOTE + "：冬深水为季节 premise "
        "配置级，无面内判断链。单因子链。A 行（Evidence Open 保留行）。",
        "LowlandRoachRowA"),
    resp_typed(
        "CMR",
        [],
        "杂食 typed 摄食响应：『preys predominantly on benthic invertebrates, "
        "zooplankton, plant material and detritus』。" + ORDER_NOTE + "：无判断顺序"
        "描述。粘卵无护（S6）不构 P04。",
        "RoachOmnivoreRowA",
        opn=["同种双行（与 LKR 同 Rutilus rutilus）合并处置待 Cross-Batch"]),
    # ---------------- LKR 湖拟鲤 ----------------
    bake_single(
        "LKR",
        ["identity = DUPLICATE_ROW_B（与常见拟鲤同种双行——Identity Deferred "
         "premise；B 行）",
         "winter_deep = 冬深水（季节 premise）"],
        "低地湖泊分布（同种双行 B）。" + ORDER_NOTE + "：静态栖息+季节 premise，无判断"
        "链。单因子链。",
        "LowlandRoachRowB"),
    resp_typed(
        "LKR",
        ["identity = DUPLICATE_ROW_B（同种双行 B 行——机制层同种同页引文适用）"],
        "同种杂食 typed 摄食响应（同种复用——A 行 CMR 同 URL FishBase 页引文同种"
        "适用，非跨种推算）。" + ORDER_NOTE + "：无判断顺序描述。",
        "RoachOmnivoreRowB",
        opn=["双行合并待 Cross-Batch（身份层 Deferred；机制层同种同源）"]),
    # ---------------- ASP 赤稍雅罗鱼 ----------------
    bake_single(
        "ASP",
        ["structure_ambush_site = 桥墩/堰坝/深流结构位点绑定（『bridge pillars, "
         "weirs, deep currents』——人工结构+流态伏击位点）",
         "spawn_migration = 4-6 月上游产卵迁移（P05 季节洄游 premise）"],
        "大河结构位点分布+春产卵迁移。" + ORDER_NOTE + "：产卵迁移为季节 lifecycle "
        "premise 配置级，无面内判断链。单因子链，结构位点为因子绑定值。",
        "StructureAmbushAsp"),
    resp_typed(
        "ASP",
        ["surface_presentation = 水面呈现 typed（含小型水鸟猎物——水面/落水输入）",
         "piscivory = 鲤科罕见鱼食（『One of the rare cyprinids which is "
         "piscivore』——鱼食 typed；鳡鱼 R03 鲤科掠食同构）"],
        "结构伏击鱼食 typed 摄食响应（桥墩/堰坝伏击+水面猎物含小水鸟）。" + ORDER_NOTE +
        "：无判断顺序描述（结构伏击 typed 单 evaluator）。",
        "RarePiscivoreCyprinid",
        opn=["水鸟捕食语义开放（Story Open Question——水面落物 vs 主动捕鸟）"]),
    # ---------------- BIA 针牙脂鲤 ----------------
    bake_single(
        "BIA",
        ["lifecycle = POTAMODROMOUS（河内洄游 premise）",
         "basin = Amazon/Orinoco/Paraná 大河绑定"],
        "南美大河分布。" + ORDER_NOTE + "：静态栖息单因子+洄游 premise，无判断链。"
        "单因子链。",
        "DogtoothCharacid"),
    resp_typed(
        "BIA",
        ["dentition_inference = 犬牙形态推断（犬齿 characid 獠牙——同科 "
         "Cynodontidae 巴亚拉 R06 先例；食性面推断）"],
        "獠牙鱼食 typed 摄食响应（形态推断承载——『獠牙掠食推断』S1 明言推断，"
        "MEDIUM）。" + ORDER_NOTE + "：无判断顺序描述。",
        "FishhookToothCharacid",
        conf="MEDIUM",
        opn=["食性细节开放（Story Open）；獠牙形态 EO——形态推断 MEDIUM"]),
    # ---------------- HLL 黑带兔脂鲤 ----------------
    bake_single(
        "HLL",
        ["basin = Negro 河流域绑定"],
        "Negro 河分布。" + ORDER_NOTE + "：静态栖息单因子（流域绑定），无时序无判断"
        "链。单因子链。",
        "HeadstanderCharacid"),
    resp_typed(
        "HLL",
        ["trophic_inference = trophic 2.3 植食倾向推算（食性面无述——倒立鱼 R08 同科"
         "对照推断）"],
        "植食倾向 typed 摄食响应（trophic 推算承载——S1 EO 推断，MEDIUM）。" +
        ORDER_NOTE + "：无判断顺序描述。成对草丛产卵=lifecycle premise。headstander "
        "科第 2 例对照。",
        "HerbivorousHeadstander",
        conf="MEDIUM",
        opn=["食性面 EO（trophic 2.3 推算）——同科对照推断 MEDIUM"]),
    # ---------------- BAS 巨型巴沙 ----------------
    bake_single(
        "BAS",
        ["flood_pulse = 洪泛季初产卵+成鱼入洪泛林（『spawns at the onset of flood "
         "season』——洪水周期 premise，暹罗巨鲤 R05 同构）",
         "air_breathing = 兼性气呼吸（runtime 生理条件 premise，肺鱼/雀鳝先例）"],
        "湄公/湄南大河急流+缓段+洪泛林分布。" + ORDER_NOTE + "：洪水周期为季节 premise "
        "配置级（P05 洪水系），无面内判断链。单因子链。",
        "FloodPulsePangasiid"),
    resp_typed(
        "BAS",
        [],
        "植食 typed 摄食响应（食性面简略——植食主载）。" + ORDER_NOTE + "：无判断顺序"
        "描述。蓝鲨 R03 同科对照。",
        "HerbivorousPangasiid",
        opn=["食性面开放（Story Open Question——植食细节简略）"]),
    # ---------------- JDP 宝石鲈 ----------------
    bake_single(
        "JDP",
        ["flood_opportunity = 洪水事件机会繁殖（『breed opportunistically during "
         "flood events』——洪水系第 3 例 premise：暹罗巨鲤/巴沙/本例）",
         "temp_tolerance = 40°C 耐受（runtime 生理条件 premise）",
         "habitat = 浊水大河潭（turbid water of large rivers and waterholes）"],
        "浊水河潭分布+洪水事件机会繁殖重排。" + ORDER_NOTE + "：洪水事件触发为周期 "
        "premise 配置级（P05 洪水系），无面内判断链。单因子链。",
        "FloodOpportunityPerch"),
    resp_guard(
        "JDP",
        ["guard_condition = 雄鱼护卵（洪水事件机会繁殖+雄护卵复合持续守护，P04 "
         "契约 pre-existing/persistent）",
         "guard_anchor = FLOOD_SPAWN_MALE_GUARD（洪水机会繁殖+雄护卵 anchor 提案）"],
        "鱼/甲壳/虫/贝杂食 typed 摄食 + 雄鱼护卵守护：对靠近目标摄食 Path ∥ 卵威胁"
        "评估 Path。" + ORDER_NOTE + "：洪水事件触发为 premise 配置级（P05 洪水系）"
        "非面内分支；守护按 P04 契约并行双 Path。40°C 耐受=runtime 条件。",
        "flood_spawn_male_guard（洪水机会繁殖+雄护卵）",
        "FloodGuarderPerch",
        opn=["洪水系供给语义=Story Open Question（P05×P04 复合的 anchor 语义）"]),
    # ---------------- LMP 圆鳍鱼 ----------------
    bake_single(
        "LMP",
        ["seasonal_migration = 深冬浅夏洄游（P05 季节 premise）",
         "morphology_disc = 吸盘形态（底栖附着形态事实——栖息绑定 typed context，"
         "S2 MSF）",
         "substrate = 岩底"],
        "岩底分布+季节深浅洄游。" + ORDER_NOTE + "：深冬浅夏为季节 premise 配置级，无"
        "面内判断链。单因子链，吸盘形态为栖息绑定依据。",
        "SuckerDiscLumpfish"),
    resp_guard(
        "LMP",
        ["guard_condition = 雄鱼激进护卵块（『Male guards egg-mass aggressively』——"
         "持续守护，P04 契约）",
         "guard_anchor = EGG_MASS_ROCK（卵块守护 anchor 提案——非巢结构型：附着卵块）",
         "sexual_dichromatism = 雌雄二态色（呈现变量 premise——遇鱼可见性语义不买 "
         "Mode，S7 MSF）"],
        "海蜇/梯栉水母/小甲壳/多毛/小鱼 typed 摄食 + 雄鱼卵块激进守护：对靠近目标"
        "摄食 Path ∥ 卵块威胁评估 Path。" + ORDER_NOTE + "：无面内判断顺序描述；独居"
        "（S3 SN）非群游；守护按 P04 契约并行双 Path。幼体藻隐=生态注记。",
        "egg_mass_rock（雄激进护卵块）",
        "EggMassGuarderLumpfish",
        opn=["雌雄二态呈现语义=Story Open Question（呈现变量 typed context 候选）"]),
    # ---------------- AMK 单鳍多线鱼 ----------------
    bake_single(
        "AMK",
        ["habitat = 岩礁硬底定居（六线鱼科——非洄游负知识）"],
        "岩礁硬底分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "RockCreviceHexagrammid"),
    resp_guard(
        "AMK",
        ["guard_condition = 雄岩缝产卵+胸鳍连续扇护 40-45 天（『guarded by the male "
         "who continuously fans the egg mass with his pectoral fin』——扇护持续，"
         "P04 契约 pre-existing/persistent）",
         "guard_anchor = ROCK_CREVICE_FAN（岩缝扇护 anchor 提案）",
         "spawn_rhythm = 一年两产（lifecycle 节奏 premise）"],
        "岩礁 typed 摄食（食性面无述 S1 EO——P01 冻结主张承载，MEDIUM）+ 雄岩缝扇护"
        "守护：对靠近目标摄食 Path ∥ 卵块威胁评估 Path。" + ORDER_NOTE + "：扇护（fan）"
        "为守护 Path 内供氧子动作非新增 branch——拓扑保持 P04 契约并行双 Path（岩钝鲈 "
        "ROB 同型扇护）。",
        "rock_crevice_fan（雄岩缝扇护 40-45 天）",
        "FanGuarderAtka",
        conf="MEDIUM",
        opn=["食性面无述（S1 EO）——P01 承载 MEDIUM；fan 扇护子动作语义与 ROB 同型"
             "（供氧行为 vs 新结构元素留判同阶段）"]),
    # ---------------- GSF 绿太阳鱼 ----------------
    bake_single(
        "GSF",
        ["habitat = 静水潭沼植被（quiet pools and backwaters of sluggish streams, "
         "lakes and ponds）"],
        "缓流潭沼湖池植被分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。"
        "单因子链。太阳鱼系第 5 例。",
        "GreenSunfishPool"),
    resp_typed(
        "GSF",
        ["ontogeny = 幼食未成熟虫/微型甲壳（幼体食性——阶段 premise；成鱼食性未述）",
         "nest_spawning = 巢产（太阳鱼系巢护传统——护卵行为未述 EO 不构 P04 程序）"],
        "静水 typed 摄食响应：幼食『immature insects and microcrustaceans』。"
        + ORDER_NOTE + "：无判断顺序描述；护卵面 EO 不立面。",
        "QuietWaterSunfish",
        opn=["护卵面开放（S6 EO——太阳鱼系巢护传统本种未述，若证实则 P04 同型不预立）"]),
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
    n_guard = sum(1 for p in PROGRAMS
                  if p.get("combine") == "DUAL_PATH_CONFLICT_AWARE")
    n_med = sum(1 for p in PROGRAMS if p.get("confidence") == "MEDIUM")
    print(f"frozen {len(PROGRAMS)} blind programs (Bake={n_bake} Response={n_resp} "
          f"guard_path={n_guard} MEDIUM={n_med}) -> {out}")
    for p in PROGRAMS:
        print(f"  {p['program_id']}: {p['blind_hash']}")


if __name__ == "__main__":
    main()
