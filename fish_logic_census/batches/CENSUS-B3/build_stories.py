# -*- coding: utf-8 -*-
"""CENSUS-B3 stories.jsonl 生成器：28 Story × Sweep Log S1-S11 逐项映射
（program / 排除 / TAR 三选一）+ Surface 四面判定。盲段产物（不读 registry）。"""
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent

# sweep 映射值域：
#  program:<pid>            S 项机制由该程序体承载
#  premise-><pid>           S 项为该程序 incoming_premise（上游 fact/condition）
#  param-><pid>            S 项为该程序 typed context 参数/绑定值（骨架内注记）
#  excluded:<reason>        排除（负知识/后钩/产品面/繁殖集群非 Group 等）
#  eo_no_program            证据开放且不建体（FR 线已知 open）
#  sn                       Sweep 无发现
#  tar:<id>                 census 判定受阻缺口 → 回 FR 线
PROG = "program:"
PREM = "premise->"
PAR = "param->"
EXC = "excluded:"
EO = "eo_no_program"
SN = "sn"

SWEEPS = {
 "CHU": {"S1": PROG+"P-B3-CHU-RESP-FASTING", "S2": SN,
         "S3": EXC+"幼鲑河口群/成鱼洄游群=生活史阶段现象≠互斥 FishGroup 供给（P05/§6）",
         "S4": SN, "S5": PREM+"P-B3-CHU-BAKE", "S6": PREM+"P-B3-CHU-BAKE",
         "S7": EO, "S8": SN, "S9": PREM+"P-B3-CHU-BAKE",
         "S10": "tar:TAR-10", "S11": SN},
 "CHN": {"S1": PROG+"P-B3-CHN-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B3-CHN-BAKE",
         "S6": EXC+"巢+主副雄竞争=繁殖 lifecycle premise（Story 无 P04 guard 主张）",
         "S7": EO, "S8": SN, "S9": PREM+"P-B3-CHN-BAKE", "S10": EO, "S11": SN},
 "COH": {"S1": PROG+"P-B3-COH-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B3-COH-BAKE",
         "S6": EXC+"并排颤射产卵=lifecycle premise", "S7": EO, "S8": SN,
         "S9": PREM+"P-B3-COH-BAKE", "S10": EO, "S11": SN},
 "PIN": {"S1": PROG+"P-B3-PIN-RESP", "S2": SN, "S3": SN,
         "S4": PREM+"P-B3-PIN-BAKE", "S5": PREM+"P-B3-PIN-BAKE",
         "S6": EXC+"redd+semelparity=lifecycle premise", "S7": EO, "S8": SN,
         "S9": PREM+"P-B3-PIN-BAKE", "S10": EO, "S11": SN},
 "BRO": {"S1": PROG+"P-B3-BRO-RESP", "S2": SN, "S3": SN,
         "S4": PREM+"P-B3-BRO-BAKE", "S5": PREM+"P-B3-BRO-BAKE",
         "S6": EXC+"redd+雄驱=lifecycle premise（无 P04 guard 主张）", "S7": EO,
         "S8": SN, "S9": PREM+"P-B3-BRO-BAKE", "S10": EO, "S11": SN},
 "SHA": {"S1": PREM+"P-B3-SHA-RESP-FASTING",
         "S2": SN,
         "S3": EXC+"非生殖集群≠互斥 FishGroup（P05/§6）", "S4": SN,
         "S5": PREM+"P-B3-SHA-BAKE", "S6": EXC+"日落并游释放=lifecycle premise",
         "S7": EO, "S8": SN, "S9": PREM+"P-B3-SHA-BAKE",
         "S10": "tar:TAR-10", "S11": SN},
 "ALE": {"S1": PROG+"P-B3-ALE-RESP", "S2": SN,
         "S3": EXC+"海期群游=分布背景非互斥 FishGroup 程序", "S4": SN,
         "S5": PREM+"P-B3-ALE-BAKE", "S6": EXC+"夜产卵=lifecycle premise",
         "S7": EO, "S8": SN, "S9": PREM+"P-B3-ALE-BAKE", "S10": SN, "S11": SN},
 "AST": {"S1": PROG+"P-B3-AST-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B3-AST-BAKE", "S6": SN,
         "S7": PAR+"P-B3-AST-RESP（须探底质 typed context）",
         "S8": PAR+"P-B3-AST-BAKE（底层=因子绑定值）", "S9": PREM+"P-B3-AST-BAKE",
         "S10": EXC+"保护边界（VU/CITES II）=产品供给面非程序面",
         "S11": EXC+"snag 边界=捕获面（B02 参考，Story 明言本批不展开）"},
 "SNS": {"S1": PROG+"P-B3-SNS-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B3-SNS-BAKE", "S6": SN,
         "S7": PAR+"P-B3-SNS-RESP（短须短吻+夜行 typed context）",
         "S8": PAR+"P-B3-SNS-BAKE（软底质=因子绑定值）", "S9": SN,
         "S10": EXC+"CITES I/ESA 禁捕=OPS 捕获边界非程序面",
         "S11": EXC+"OPS 捕获边界"},
 "TAR": {"S1": PROG+"P-B3-TAR-RESP", "S2": SN,
         "S3": PAR+"P-B3-TAR-RESP（群游猎物取向 typed context）", "S4": SN,
         "S5": PREM+"P-B3-TAR-BAKE", "S6": SN,
         "S7": PAR+"P-B3-TAR-RESP（上翘口水面取向=水面呈现 typed context）",
         "S8": PAR+"P-B3-TAR-BAKE（河口/湾区绑定值）",
         "S9": PREM+"P-B3-TAR-BAKE",
         "S10": EXC+"游钓旗舰=产品面；跳跃搏鱼=后钩阶段非 FCF 前链（Story 明言）",
         "S11": SN},
 "TAI": {"S1": PROG+"P-B3-TAI-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B3-TAI-BAKE", "S6": EXC+"redd=lifecycle premise",
         "S7": PAR+"P-B3-TAI-RESP（陆生猎物水面呈现 typed context）",
         "S8": PROG+"P-B3-TAI-BAKE",
         "S9": PREM+"P-B3-TAI-RESP（幼无脊→鱼食个体发生）",
         "S10": EXC+"mouse pattern 飞钓=玩家策略（产品面）", "S11": SN},
 "ARA": {"S1": PROG+"P-B3-ARA-RESP", "S2": SN, "S3": SN,
         "S4": PREM+"P-B3-ARA-BAKE", "S5": PROG+"P-B3-ARA-BAKE",
         "S6": PROG+"P-B3-ARA-RESP（guard 双 Path：沙巢+护卵护幼）",
         "S7": "tar:TAR-11", "S8": PAR+"P-B3-ARA-BAKE（干季湖绑定值）",
         "S9": PREM+"P-B3-ARA-BAKE",
         "S10": EXC+"换气定位钓=呈现策略（引文开放同 TAR-11）", "S11": SN},
 "PB": {"S1": PROG+"P-B3-PB-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
        "S6": EO, "S7": EO, "S8": PROG+"P-B3-PB-BAKE", "S9": SN, "S10": EO,
        "S11": SN},
 "RBP": {"S1": PROG+"P-B3-RBP-RESP",
         "S2": EXC+"交替换牙连续进食=形态能力事实非程序步（open_semantics 注记）",
         "S3": EXC+"群游=防御（anti-predator）——Negative Knowledge：『no investigation "
                  "shows』无证据形态否定协作捕猎 frenzy，不得以 frenzy 购 Group Mode"
                  "（FR3 判例②）",
         "S4": SN, "S5": SN, "S6": PROG+"P-B3-RBP-RESP（guard 双 Path：树根卵团）",
         "S7": PAR+"P-B3-RBP-RESP（听觉=呈现面感官线索参数）",
         "S8": PROG+"P-B3-RBP-BAKE",
         "S9": PREM+"P-B3-RBP-RESP（体型分级时段 condition premise）",
         "S10": EO, "S11": SN},
 "BLP": {"S1": PROG+"P-B3-BLP-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": EO, "S7": EO, "S8": PROG+"P-B3-BLP-BAKE", "S9": SN,
         "S10": EXC+"深水 fish bait 捕获=钓捕事实（FishBase 原文）非程序面", "S11": SN},
 "WEL": {"S1": PROG+"P-B3-WEL-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": PROG+"P-B3-WEL-RESP（guard 双 Path：雄巢守护至幼虫孵出）",
         "S7": PAR+"P-B3-WEL-RESP（听嗅主导 typed context）",
         "S8": PROG+"P-B3-WEL-BAKE",
         "S9": PREM+"P-B3-WEL-RESP（个体发生）",
         "S10": EXC+"引入地游钓=产品面", "S11": SN},
 "FLA": {"S1": PROG+"P-B3-FLA-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": EO, "S7": PAR+"P-B3-FLA-RESP（须+底质 typed context）",
         "S8": PROG+"P-B3-FLA-BAKE", "S9": PREM+"P-B3-FLA-RESP（个体发生）",
         "S10": EO, "S11": SN},
 "BUR": {"S1": PROG+"P-B3-BUR-RESP", "S2": SN, "S3": SN,
         "S4": PROG+"P-B3-BUR-BAKE（夏深冬活动季节重排主承载）", "S5": SN,
         "S6": EXC+"冬夜产卵球=繁殖集群非摄食群，不买 Group（Story 明言）",
         "S7": PAR+"P-B3-BUR-RESP（颏须底探 typed context）",
         "S8": PAR+"P-B3-BUR-BAKE（岩缝/树根=冬季绑定值）",
         "S9": PREM+"P-B3-BUR-RESP（个体发生）", "S10": EO, "S11": SN},
 "GW": {"S1": PROG+"P-B3-GW-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
        "S6": EXC+"雨季初繁殖=lifecycle premise（无 guard 主张）",
        "S7": PAR+"P-B3-GW-RESP（落水猎物水面呈现 typed context）",
        "S8": PROG+"P-B3-GW-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "PAY": {"S1": PROG+"P-B3-PAY-RESP（形态事实推断：probably ichthyophagous）",
         "S2": SN, "S3": SN, "S4": SN, "S5": EO, "S6": EO, "S7": EO,
         "S8": EO, "S9": SN, "S10": EO, "S11": SN},
 "SGA": {"S1": PROG+"P-B3-SGA-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": EO,
         "S7": PAR+"P-B3-SGA-RESP（兼性气呼吸=runtime 条件 premise）",
         "S8": PROG+"P-B3-SGA-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "SHO": {"S1": PROG+"P-B3-SHO-RESP（同属黑鲈 P01 同构推算，属内 2/4 先例——Confidence MEDIUM）",
         "S2": SN, "S3": SN, "S4": SN, "S5": SN, "S6": EO, "S7": EO,
         "S8": EO, "S9": SN, "S10": EO, "S11": SN},
 "RFP": {"S1": PROG+"P-B3-RFP-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": SN,
         "S7": EO, "S8": PROG+"P-B3-RFP-BAKE", "S9": SN,
         "S10": EXC+"ultralight 钓法（McClane 引文）=产品面", "S11": SN},
 "DS": {"S1": PROG+"P-B3-DS-RESP（同科笋壳鱼 R05 P01 先例同构推算）", "S2": SN,
        "S3": SN, "S4": SN, "S5": SN, "S6": EO, "S7": EO,
        "S8": PROG+"P-B3-DS-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "PBF": {"S1": PROG+"P-B3-PBF-RESP", "S2": SN,
         "S3": PAR+"P-B3-PBF-RESP（群游猎物取向 typed context）",
         "S4": PREM+"P-B3-PBF-BAKE", "S5": PREM+"P-B3-PBF-BAKE", "S6": EO,
         "S7": "tar:TAR-12", "S8": PAR+"P-B3-PBF-BAKE（上层洋区绑定值）",
         "S9": PREM+"P-B3-PBF-BAKE",
         "S10": EXC+"顶级游钓=产品面", "S11": SN},
 "GT": {"S1": PROG+"P-B3-GT-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
        "S6": EXC+"浅礁/离岸滩产卵聚集=繁殖 lifecycle premise（FishBase 无互斥供给证据）",
        "S7": PAR+"P-B3-GT-RESP（夜间低光 typed context——R03 教训不买 Night Mode）",
        "S8": PAR+"P-B3-GT-BAKE（礁/沙岩/泻湖绑定值）",
        "S9": PREM+"P-B3-GT-BAKE（幼河口-成礁外阶段）", "S10": EO,
        "S11": EXC+"ciguatoxic=人类侧食物安全 Capture Boundary（FISH-R07-FIX-001 "
                  "F-E-a 回溯补标；S11 行值 SN+域标签注记）"},
 "HAL": {"S1": PROG+"P-B3-HAL-RESP", "S2": SN, "S3": SN,
         "S4": PREM+"P-B3-HAL-BAKE", "S5": PREM+"P-B3-HAL-BAKE",
         "S6": EXC+"深海 batch 产卵=lifecycle premise", "S7": EO,
         "S8": PAR+"P-B3-HAL-BAKE（50-2000m 深度绑定值）",
         "S9": EXC+"晚熟=lifecycle premise（无阶段并存供给主张）", "S10": EO,
         "S11": SN},
 "GG": {"S1": PROG+"P-B3-GG-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
        "S6": EO,
        "S7": EO, "S8": PROG+"P-B3-GG-BAKE",
        "S9": PREM+"P-B3-GG-BAKE（幼鱼礁内隐蔽 lifecycle premise）", "S10": EO,
        "S11": EXC+"ciguatoxic=Capture Boundary（同 GT，FISH-R07-FIX-001 F-E-a）"},
}

GROUP_NO = {
 "CHU": "洄游期集群=阶段现象；幼鲑群散下入海；成鱼洄游停食群≠互斥 FishGroup（P05/§6）",
 "CHN": "ocean/stream/jack 型=生活史差异不并发拆分 Group（P05；B01 大西洋鲑负例同构）",
 "COH": "无集群主张（S3 SN）", "PIN": "奇偶年隔离=周期语义非同 scope 并存（P05 层 open）",
 "BRO": "salter/定居双型=P05 阶段语义（GroupPressure=Possible 记语义层，census 无 routing 证据）",
 "SHA": "非生殖集群≠互斥 FishGroup（P05/§6）", "ALE": "海期群游=分布背景非 Group 程序",
 "AST": "无集群主张（S3 SN）", "SNS": "无集群主张（S3 SN）",
 "TAR": "猎物群游是猎物侧事实；本种无互斥供给主张",
 "TAI": "领域独居型（深潭 anchor）；无集群主张（S3 SN）",
 "ARA": "无集群主张（S3 SN；换气暴露非集群）",
 "PB": "无集群主张（S3 SN）",
 "RBP": "群游=防御性集聚（anti-predator）；『no investigation shows』无证据形态否定协作捕猎 "
        "frenzy——Negative Knowledge，不买 Group Mode/FishGroup（FR3 判例②）",
 "BLP": "无集群主张（S3 SN；胆怯独居）", "WEL": "无集群主张（S3 SN；独居伏击）",
 "FLA": "无集群主张（S3 SN）", "BUR": "冬夜产卵球=繁殖集群非摄食群（不买 Group——Story 明言）",
 "GW": "无集群主张（S3 SN）", "PAY": "无集群主张（S3 SN）", "SGA": "无集群主张（S3 SN）",
 "SHO": "无集群主张（S3 SN）", "RFP": "无集群主张（S3 SN）", "DS": "无集群主张（S3 SN）",
 "PBF": "顶级洄游分布；无互斥供给主张（S3=猎物群游，param）",
 "GT": "无集群主张（S3 SN；产卵聚集=lifecycle premise）", "HAL": "无集群主张（S3 SN）",
 "GG": "无集群主张（S3 SN）",
}
QUALITY_NO = "无 Quality Selection 程序证据（同 B0-B2 基线）"

SOURCE = {
 "CHU": "R06-S01｜大马哈鱼｜Chum Salmon｜Anadromous Fasting Run",
 "CHN": "R06-S02｜帝王鲑｜Chinook Salmon｜Long-Distance Run + Life-History Polymorphism",
 "COH": "R06-S03｜银鲑｜Coho Salmon｜Prey Escalation Run",
 "PIN": "R06-S04｜粉鲑｜Pink Salmon｜Fixed Two-Year Cycle Run",
 "BRO": "R06-S05｜美洲红点鲑｜Brook Trout｜Salter-Resident Polymorphism",
 "SHA": "R06-S06｜美洲西鲱｜American Shad｜Anadromous Fasting Run",
 "ALE": "R06-S07｜灰西鲱｜Alewife｜Dual Life-History Form",
 "AST": "R06-S08｜尖吻鲟｜Atlantic Sturgeon｜Barbel-Bottom Anadromous Run",
 "SNS": "R06-S09｜短吻鲟｜Shortnose Sturgeon｜Nocturnal Soft-Bottom Probing",
 "TAR": "R06-S10｜大西洋大海鲢｜Atlantic Tarpon｜Air-Breathing Surface Predator + Silver King",
 "TAI": "R06-S11｜哲罗鲑｜Siberian Taimen｜Deep-Pool Territorial Apex + Terrestrial Prey",
 "ARA": "R06-S12｜巨骨舌鱼｜Arapaima｜Obligate Air-Gulp Exposure + Flood-Pulse Guarder",
 "PB": "R06-S13｜奥里诺科孔雀鲈｜Orinoco Peacock Bass｜Shallow-Lagoon Pursuit",
 "RBP": "R06-S14｜红腹食人鱼｜Red-bellied Piranha｜Frenzy-Myth Correction + Root-Guard",
 "BLP": "R06-S15｜黑食人鱼｜Black Piranha｜Timid Opportunist in Rapids",
 "WEL": "R06-S16｜欧洲巨鲶｜Wels Catfish｜Hole-Ambush Nocturnal + Introduced Sport Giant",
 "FLA": "R06-S17｜铲鮰｜Flathead Catfish｜Log-Pool Benthic Predator",
 "BUR": "R06-S18｜江鳕｜Burbot｜Winter-Spawn Ball + Crepuscular Benthic",
 "GW": "R06-S19｜巨狼鱼｜Giant Wolf Fish｜Counter-Current Dusk Ambush",
 "PAY": "R06-S20｜巴亚拉鱼｜Payara｜Fang-Tooth Ichthyophage",
 "SGA": "R06-S21｜斑点雀鳝｜Spotted Gar｜Backwater Ambush + Facultative Air",
 "SHO": "R06-S22｜浅滩鲈鱼｜Shoal Bass｜Congeneric Micropterus Default",
 "RFP": "R06-S23｜红鳍狗鱼｜Redfin Pickerel｜Vegetated-Pool Small Ambush",
 "DS": "R06-S24｜沙塘鳢｜Dark Sleeper｜Benthic Small Ambush",
 "PBF": "R06-S25｜太平洋蓝鳍金枪鱼｜Pacific Bluefin Tuna｜Endothermic Oceanic Migrator",
 "GT": "R06-S26｜牛港鲹｜Giant Trevally｜Nocturnal Reef-Edge Predator",
 "HAL": "R06-S27｜大西洋大比目鱼｜Atlantic Halibut｜Deep-Winter Demersal Predator",
 "GG": "R06-S28｜鞍带石斑鱼｜Giant Grouper｜Cave-Wreck Ambush Apex",
}
PATTERNS = {
 "CHU": ["P01", "P05"], "CHN": ["P01", "P05"], "COH": ["P01", "P05"],
 "PIN": ["P01", "P05"], "BRO": ["P01", "P05"], "SHA": ["P01", "P05"],
 "ALE": ["P01", "P05"], "AST": ["P01", "P05"], "SNS": ["P01", "P05"],
 "TAR": ["P01", "P05"], "TAI": ["P01", "P05"], "ARA": ["P01", "P04", "P05"],
 "PB": ["P01"], "RBP": ["P01", "P04"], "BLP": ["P01"], "WEL": ["P01", "P04"],
 "FLA": ["P01"], "BUR": ["P01", "P05"], "GW": ["P01"], "PAY": ["P01"],
 "SGA": ["P01"], "SHO": ["P01"], "RFP": ["P01"], "DS": ["P01"],
 "PBF": ["P01", "P05"], "GT": ["P01", "P05"], "HAL": ["P01", "P05"], "GG": ["P01"],
}


def story_rec(sid):
    bake_ids = []
    if sid not in ("PAY", "SHO"):
        bake_ids = [f"P-B3-{sid}-BAKE"]
    resp_id = (f"P-B3-{sid}-RESP-FASTING" if sid in ("CHU", "SHA")
               else f"P-B3-{sid}-RESP")
    bake_surface = ({"consequence": "NEW_PROGRAM_CANDIDATE",
                     "program_ids": bake_ids, "reason": "栖息/阶段空间因子程序证据"}
                    if bake_ids else
                    {"consequence": "NO_SURFACE_EFFECT",
                     "reason": "栖息/洄游面 FishBase EO（Story 明言资料缺失），无空间程序证据——不建体不冒用"})
    return {
        "story_id": f"CENSUS-B3-{sid}", "source_story": SOURCE[sid],
        "frozen_patterns": PATTERNS[sid],
        "sweep_log_mapping": SWEEPS[sid],
        "surfaces": {
            "Group": {"consequence": "NO_SURFACE_EFFECT", "reason": GROUP_NO[sid]},
            "Bake": bake_surface,
            "Response": {"consequence": "NEW_PROGRAM_CANDIDATE",
                         "program_ids": [resp_id],
                         "reason": ("停食洄游双 Path（FR3 判例① multi-path）" if sid in ("CHU", "SHA")
                                    else "P04 guard 双 Path（food ∥ conflict → COMBINE）" if sid in ("ARA", "RBP", "WEL")
                                    else "P01 typed 离散目标响应")},
            "Quality": {"consequence": "NO_SURFACE_EFFECT", "reason": QUALITY_NO},
        },
        "consequence": "NEW_PROGRAM_CANDIDATE",
        "provenance": {"batch": "CENSUS-B3"},
    }


def main():
    out = BATCH_DIR / "stories.jsonl"
    recs = [story_rec(sid) for sid in SWEEPS]
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in recs) + "\n",
                   encoding="utf-8")
    n_prog = sum(1 for r in recs
                 for s in r["surfaces"].values()
                 if s["consequence"] == "NEW_PROGRAM_CANDIDATE")
    print(f"wrote {len(recs)} stories; program-bearing surfaces={n_prog}")


if __name__ == "__main__":
    main()
