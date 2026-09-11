# -*- coding: utf-8 -*-
"""CENSUS-B4 stories.jsonl 生成器：26 Story × Sweep Log S1-S11 逐项映射
（program / premise / param / excluded / eo / sn / tar）+ Surface 四面判定。
盲段产物（registry 未读）。BFS 头足类边界=Product Scope Deferred 0 程序。"""
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent

# 映射值域同 B3：
#  program:<pid> / premise-><pid> / param-><pid> / excluded:<reason> / eo_no_program / sn / tar:<id>
PROG = "program:"
PREM = "premise->"
PAR = "param->"
EXC = "excluded:"
EO = "eo_no_program"
SN = "sn"

SRC = "https://app.notion.com/p/3d7a4137d23681"
URLS = {
    "POR": SRC+"248a12ca0c07aa0147", "SDG": SRC+"3987e8e5adaffe482f",
    "TSK": SRC+"c4bba0e651f58c29fc", "ASR": SRC+"3bb4ddc091e4732e0f",
    "RVS": SRC+"768a31c8e1a247c668", "BFS": SRC+"138057c6270bcbdf5a",
    "GPF": SRC+"838c4bec5c5353659a", "RKB": SRC+"b3b45fcd8e68ade468",
    "SSL": SRC+"39a400f025268c20b6", "BSK": SRC+"b9921dcad805a00e41",
    "RRH": SRC+"58850bd6a92a93970a", "GRH": SRC+"6a9256c990073eacf8",
    "SMB": SRC+"7cacbdd7c70d8bdafa", "GDE": SRC+"a68501d8a0868160ba",
    "WIT": SRC+"b29b49da80beef6f31", "WIN": SRC+"31bed9f3f0c7f7a9db",
    "YTF": SRC+"aa883bd78444277315", "SMF": SRC+"ea964ef147f5413ce8",
    "BST": SRC+"7fb981e316c8c683d4", "FDR": SRC+"9bb8bee26d21b3e0d3",
    "BSB": SRC+"ef9f22ce9fd16a66f6", "CBM": SRC+"04ac0dc5037c9e75c4",
    "SAI": SRC+"f5b8e3e7d59f8d57ff", "HNC": SRC+"12a955dcf18edc3cf39",
    "MOO": SRC+"e49bdfda910800fd58", "RDS": SRC+"aea3d1c107ba0c3f9e",
}

EO_DIET = ("eo_no_program：食性机制细节 EO——Response 程序体由 P01 PatternFit+"
           "TargetFeeding channel 冻结主张承载（MEDIUM，形态/栖息事实推断），引文闭合归 FR 线")

SWEEPS = {
 # S1 食性 | S2 形态机制 | S3 群游 | S4 温度/季节 | S5 洄游 | S6 繁殖 | S7 感官 | S8 栖息 | S9 体型/发育 | S10 游钓 | S11 反捕食/边界
 "POR": {"S1": PROG+"P-B4-POR-RESP", "S2": SN,
         "S3": PAR+"P-B4-POR-RESP（猎物群游取向 typed context——『pelagic schooling species』）",
         "S4": SN, "S5": PREM+"P-B4-POR-BAKE",
         "S6": EXC+"oophagy/子宫内营养竞争=繁殖内部 lifecycle 过程非 FCF 程序面",
         "S7": EO,
         "S8": PROG+"P-B4-POR-BAKE", "S9": SN,
         "S10": EXC+"游钓事实（'fako' Wikipedia 引文）=产品面；钓法引文开放",
         "S11": EXC+"VU/CITES II 保护边界=OPS 产品供给面非程序面（B3 AST 先例）"},
 "SDG": {"S1": PROG+"P-B4-SDG-RESP", "S2": SN,
         "S3": EXC+"千尾觅食群/体型性别分群=非生殖集群群结构事实≠互斥 FishGroup 供给（B3 CHU/SDG 同型判例）",
         "S4": PREM+"P-B4-SDG-BAKE（温度相关移动=水温条件 premise）",
         "S5": PREM+"P-B4-SDG-BAKE",
         "S6": EXC+"18-24 月妊娠=lifecycle premise",
         "S7": PAR+"P-B4-SDG-RESP（被动电感知 typed evaluator input——FR3 判例① K8 电轴感知端）",
         "S8": PROG+"P-B4-SDG-BAKE", "S9": SN,
         "S10": EO, "S11": EXC+"毒棘=后钩搏鱼处理非 FCF 前链"},
 "TSK": {"S1": PROG+"P-B4-TSK-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": EXC+"卵囊角=卵生 lifecycle premise",
         "S7": PAR+"P-B4-TSK-RESP（被动电感知+自发电场 typed evaluator input——FR3 判例①）",
         "S8": PROG+"P-B4-TSK-BAKE",
         "S9": PREM+"P-B4-TSK-RESP（食性随体型 ontogeny premise）",
         "S10": EO, "S11": EXC+"VU 保护边界=产品面"},
 "ASR": {"S1": PROG+"P-B4-ASR-RESP", "S2": SN,
         "S3": EXC+"成对/小群=种群结构背景非互斥 FishGroup 供给",
         "S4": SN, "S5": PREM+"P-B4-ASR-BAKE",
         "S6": EXC+"卵胎生=lifecycle premise", "S7": EO,
         "S8": PROG+"P-B4-ASR-BAKE", "S9": SN, "S10": SN,
         "S11": EXC+"毒刺类群常识 EO 且后钩非 FCF 前链（同 SDG）"},
 "RVS": {"S1": EO_DIET, "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": EXC+"胎生=lifecycle premise", "S7": EO,
         "S8": PROG+"P-B4-RVS-BAKE", "S9": SN, "S10": EO,
         "S11": EXC+"毒刺 Traumatogenic=搏鱼阶段处理（后钩）非 FCF 前链；CB 轴 Encounter lane "
                 "鱼侧防御 typed 子类（FR3 判例③）"},
 "BFS": {k: EXC+"头足类非鱼边界=Product Scope Deferred（FR3 判例②：不套 P01 不立鱼侧 "
              "pattern；光 cue 轴 provisional 挂 K8 由 FR 线承载）"
         for k in ["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11"]},
 "GPF": {"S1": EO_DIET,
         "S2": PAR+"P-B4-GPF-RESP（齿板形态 typed context——程序依据承载）",
         "S3": EXC+"高潮产卵集群=繁殖集群非摄食 FishGroup（B3 BUR 冬夜产卵球同型判例）",
         "S4": PREM+"P-B4-GPF-BAKE（潮汐窗=周期 premise）", "S5": SN,
         "S6": PREM+"P-B4-GPF-BAKE（上岸产卵事件时序=opportunity lifecycle premise；"
                  "雄咬挂对象=雌鱼腹面非 FCF 目标语义）",
         "S7": EO,
         "S8": PROG+"P-B4-GPF-BAKE", "S9": SN,
         "S10": EXC+"堤钓多饵=捕获事实（Wiki 引文）非程序面（B3 BLP 深水鱼饵同型）",
         "S11": EXC+"TTX=人类侧食物安全 Capture Boundary（ciguatoxic 同型；FR3 判例③）"},
 "RKB": {"S1": EO_DIET, "S2": EO, "S3": SN, "S4": SN, "S5": SN,
         "S6": EO,
         "S7": EO,
         "S8": PROG+"P-B4-RKB-BAKE",
         "S9": PREM+"P-B4-RKB-BAKE（幼鱼流藻=阶段 premise）",
         "S10": EO, "S11": SN},
 "SSL": {"S1": PROG+"P-B4-SSL-RESP", "S2": SN,
         "S3": EXC+"Form schools=非生殖集群背景非互斥 FishGroup 供给",
         "S4": SN, "S5": SN,
         "S6": SN,
         "S7": EO,
         "S8": PROG+"P-B4-SSL-BAKE",
         "S9": PREM+"P-B4-SSL-BAKE（幼浮游-底栖=阶段 premise）",
         "S10": SN,
         "S11": EXC+"潜沙受扰=鱼侧反捕食 runtime overlay（遇鱼可见性语义不买 Mode）；"
                 "CB 轴鱼侧反捕食 typed 子类（FR3 判例③）"},
 "BSK": {"S1": EO_DIET, "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B4-BSK-BAKE", "S6": EO,
         "S7": EO,
         "S8": PROG+"P-B4-BSK-BAKE", "S9": SN, "S10": SN, "S11": SN},
 "RRH": {"S1": PROG+"P-B4-RRH-RESP",
         "S2": EO, "S3": SN, "S4": SN,
         "S5": PREM+"P-B4-RRH-BAKE", "S6": EO, "S7": EO,
         "S8": PROG+"P-B4-RRH-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "GRH": {"S1": PROG+"P-B4-GRH-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B4-GRH-BAKE", "S6": EO, "S7": EO,
         "S8": PROG+"P-B4-GRH-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "SMB": {"S1": PROG+"P-B4-SMB-RESP",
         "S2": PAR+"P-B4-SMB-RESP（咽喉骨板磿碎=机制 typed 事实不买 Mode——草鱼 R02 先例）",
         "S3": SN, "S4": SN, "S5": SN, "S6": EO, "S7": EO,
         "S8": PROG+"P-B4-SMB-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "GDE": {"S1": PROG+"P-B4-GDE-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B4-GDE-BAKE",
         "S6": SN,
         "S7": PAR+"P-B4-GDE-RESP（夜行=低光 typed context——R03 先例不买 Night Mode）",
         "S8": PROG+"P-B4-GDE-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "WIT": {"S1": PROG+"P-B4-WIT-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": SN, "S7": EO,
         "S8": PROG+"P-B4-WIT-BAKE", "S9": SN,
         "S10": SN, "S11": EXC+"VU 保护边界=产品面"},
 "WIN": {"S1": PROG+"P-B4-WIN-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": SN, "S7": EO,
         "S8": PROG+"P-B4-WIN-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "YTF": {"S1": PROG+"P-B4-YTF-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": SN, "S7": EO,
         "S8": PROG+"P-B4-YTF-BAKE", "S9": SN,
         "S10": SN, "S11": EXC+"VU 保护边界=产品面"},
 "SMF": {"S1": EO_DIET, "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": SN, "S7": EO,
         "S8": PROG+"P-B4-SMF-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "BST": {"S1": PROG+"P-B4-BST-RESP", "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B4-BST-BAKE", "S6": EO,
         "S7": EO,
         "S8": PROG+"P-B4-BST-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "FDR": {"S1": PROG+"P-B4-FDR-RESP", "S2": SN, "S3": SN, "S4": SN, "S5": SN,
         "S6": SN,
         "S7": EXC+"产声=种内沟通/潜在声学 cue 观察（『Known to produce sound』）非本鱼摄食"
                "程序输入；钓手听觉线索=产品面 open；鸣肌机制 EO",
         "S8": PROG+"P-B4-FDR-BAKE",
         "S9": PREM+"P-B4-FDR-RESP（同类幼鱼=猎物类型 premise）",
         "S10": EO, "S11": SN},
 "BSB": {"S1": PROG+"P-B4-BSB-RESP", "S2": EO, "S3": SN, "S4": SN, "S5": SN,
         "S6": EO, "S7": EO,
         "S8": PROG+"P-B4-BSB-BAKE",
         "S9": EXC+"性转换=lifecycle premise（先雌后雄常识 EO，繁殖发育非摄食程序）",
         "S10": EO, "S11": SN},
 "CBM": {"S1": PROG+"P-B4-CBM-RESP", "S2": SN,
         "S3": EXC+"体型分级群游（『Schooling by size…initiates at 3 cm』）=群结构事实"
                "≠互斥 FishGroup 供给（SDG 同型）",
         "S4": PREM+"P-B4-CBM-BAKE（冬深水不活跃=季节 position+活动 premise）",
         "S5": SN,
         "S6": SN,
         "S7": EO,
         "S8": PROG+"P-B4-CBM-BAKE",
         "S9": EXC+"体型分级=群结构事实（与 S3 同源）非摄食程序参数",
         "S10": EO, "S11": SN},
 "SAI": {"S1": PROG+"P-B4-SAI-RESP", "S2": SN,
         "S3": EXC+"gregarious=非生殖集群背景非互斥 FishGroup 供给",
         "S4": PREM+"P-B4-SAI-BAKE（春岸冬深=季节 premise）",
         "S5": PREM+"P-B4-SAI-BAKE（南北洄游 premise）",
         "S6": SN, "S7": EO,
         "S8": PROG+"P-B4-SAI-BAKE",
         "S9": PREM+"P-B4-SAI-RESP（体型分级食性=ontogeny premise——B3 TAI 同型）",
         "S10": EO, "S11": SN},
 "HNC": {"S1": PROG+"P-B4-HNC-RESP（昼间视觉捕食=food Path typed context）", "S2": SN,
         "S3": SN, "S4": SN, "S5": SN,
         "S6": PROG+"P-B4-HNC-RESP（guard 双 Path：石巢丘 anchor+物种型 intruder 谓词）",
         "S7": PAR+"P-B4-HNC-RESP（昼间视觉 typed context）",
         "S8": PROG+"P-B4-HNC-BAKE",
         "S9": PREM+"P-B4-HNC-RESP（幼-成食性 ontogeny premise）",
         "S10": SN,
         "S11": EXC+"异种借巢+杂交=繁殖生态注记（Story 明言）；借巢者被容忍不触发冲突 Path"
                 "（guard_target_specificity 负知识半边）"},
 "MOO": {"S1": EO_DIET, "S2": SN, "S3": SN, "S4": SN,
         "S5": PREM+"P-B4-MOO-BAKE", "S6": SN, "S7": EO,
         "S8": PROG+"P-B4-MOO-BAKE", "S9": SN, "S10": EO, "S11": SN},
 "RDS": {"S1": PROG+"P-B4-RDS-RESP（贝食偏好 FishBase 原文承载）",
         "S2": EO, "S3": SN, "S4": SN, "S5": SN,
         "S6": EO, "S7": EO,
         "S8": PROG+"P-B4-RDS-BAKE", "S9": SN, "S10": EO, "S11": SN},
}

GROUP_NO = {
 "POR": "海洋分布广域；无互斥供给主张（S3=猎物群游 param）",
 "SDG": "千尾觅食群/体型性别分群=非生殖集群≠互斥 FishGroup（P05/§6；B3 同型判例）",
 "TSK": "无集群主张（S3 SN）", "ASR": "成对/小群=种群结构背景非 Group 程序",
 "RVS": "无集群主张（S3 SN）", "BFS": "头足类边界（产品 Deferred）",
 "GPF": "高潮产卵集群=繁殖集群非摄食群不买 Group（B3 BUR 同型）",
 "RKB": "无集群主张（S3 SN）", "SSL": "Form schools=非生殖集群背景",
 "BSK": "无集群主张（S3 SN）", "RRH": "无集群主张（S3 SN）", "GRH": "无集群主张（S3 SN）",
 "SMB": "无集群主张（S3 SN）", "GDE": "无集群主张（S3 SN）", "WIT": "无集群主张（S3 SN）",
 "WIN": "无集群主张（S3 SN）", "YTF": "无集群主张（S3 SN）", "SMF": "无集群主张（S3 SN）",
 "BST": "无集群主张（S3 SN）", "FDR": "无集群主张（S3 SN）", "BSB": "无集群主张（S3 SN）",
 "CBM": "体型分级群游=群结构事实≠互斥 FishGroup（SDG 同型判例）",
 "SAI": "gregarious=非生殖集群背景≠互斥 FishGroup",
 "HNC": "无集群主张（S3 SN；石巢共生为繁殖关系非集群）",
 "MOO": "无集群主张（S3 SN）", "RDS": "无集群主张（S3 SN）",
}
QUALITY_NO = "无 Quality Selection 程序证据（同 B0-B3 基线）"

PATTERNS = {
 "POR": ["P01","P05"], "SDG": ["P01","P05"], "TSK": ["P01"], "ASR": ["P01"],
 "RVS": ["P01"], "BFS": ["Boundary/Deferred"], "GPF": ["P01"], "RKB": ["P01"],
 "SSL": ["P01"], "BSK": ["P01"], "RRH": ["P01"], "GRH": ["P01"], "SMB": ["P01"],
 "GDE": ["P01","P05"], "WIT": ["P01"], "WIN": ["P01"], "YTF": ["P01"],
 "SMF": ["P01"], "BST": ["P01"], "FDR": ["P01"], "BSB": ["P01"],
 "CBM": ["P01","P05"], "SAI": ["P01","P05"], "HNC": ["P01","P04"], "MOO": ["P01"],
 "RDS": ["P01"],
}
TITLE = {
 "POR": "R07-S01｜鼠鲨｜Porbeagle｜Endothermic Migrating Shark",
 "SDG": "R07-S02｜白斑角鲨｜Spiny Dogfish｜Passive-Electrosense Foraging School",
 "TSK": "R07-S03｜棘背钝头鳐｜Thorny Skate｜Cold-Deep Electrosense Bottom Forager",
 "ASR": "R07-S04｜大西洋黄貂鱼｜Atlantic Stingray｜Euryhaline Bottom Forager",
 "RVS": "R07-S05｜眼斑河魟｜Ocellate River Stingray｜Freshwater Ray Venom Boundary",
 "BFS": "R07-S06｜莱氏拟乌贼｜Bigfin Reef Squid｜Cephalopod Boundary + Phototaxis Jig",
 "GPF": "R07-S07｜星点东方鲀｜Grass Puffer｜High-Tide Beach Spawning + TTX Boundary",
 "RKB": "R07-S08｜条石鲷｜Rock Bream｜Reef Beak-Crusher Boundary",
 "SSL": "R07-S09｜沙鮻｜Silver Sillago｜Sand-Burial Bottom Feeder",
 "BSK": "R07-S10｜长背亚口鱼｜Blue Sucker｜Swift-Chute Benthic Sucker",
 "RRH": "R07-S11｜河红马鱼｜River Redhorse｜Rock-Pool Mollusk Feeder",
 "GRH": "R07-S12｜金红马鱼｜Golden Redhorse｜Insect-Larvae Bottom Feeder",
 "SMB": "R07-S13｜水牛鱼｜Smallmouth Buffalo｜Throat-Plate Mollusk Grinder",
 "GDE": "R07-S14｜金眼鱼｜Goldeye｜Nocturnal Turbid-River Omnivore",
 "WIT": "R07-S15｜女巫鲽｜Witch Flounder｜Cold-Deep Mud Flatfish",
 "WIN": "R07-S16｜美洲拟鲽｜Winter Flounder｜Diurnal Nearshore Bottom Feeder",
 "YTF": "R07-S17｜大西洋黄盖鲽｜Yellowtail Flounder｜Polychaete Mud-Flat Forager",
 "SMF": "R07-S18｜大西洋牙鲆｜Summer Flounder｜Left-Eye Burrow Ambusher",
 "BST": "R07-S19｜唇䱻｜Barbel Steed｜Barbel-Bottom Insectivore",
 "FDR": "R07-S20｜淡水石首鱼｜Freshwater Drum｜Sound-Producing Bottom Omnivore",
 "BSB": "R07-S21｜黑鲷｜Blackhead Seabream｜Bay-Reef Shellfish Biter",
 "CBM": "R07-S22｜日本鲭｜Chub Mackerel｜Size-Graded Night Schooling",
 "SAI": "R07-S23｜绿青鳕｜Saithe｜Gregarious Seasonal Migrator",
 "HNC": "R07-S24｜双点美鱥｜Hornyhead Chub｜Pebble-Mound Guard + Nest Associates",
 "MOO": "R07-S25｜月眼鱼｜Mooneye｜Deep-Pool River Pelagic",
 "RDS": "R07-S26｜小冠太阳鱼｜Redear Sunfish｜Mollusk-Preferring Sunfish",
}


def story_rec(sid):
    if sid == "BFS":
        surfaces = {
            "Group": {"consequence": "NO_SURFACE_EFFECT", "reason": GROUP_NO[sid]},
            "Bake": {"consequence": "NO_SURFACE_EFFECT",
                     "reason": "头足类非鱼——无 FCF 空间程序骨架（Product Scope Deferred，FR3 判例②）"},
            "Response": {"consequence": "NO_SURFACE_EFFECT",
                         "reason": "头足类无咽部咬合响应骨架（Story 明言）；趋光/jig=光 cue 轴 K8 "
                                   "provisional +捕获路径 CB 轴，均 FR 线承载非 census 程序"},
            "Quality": {"consequence": "NO_SURFACE_EFFECT", "reason": QUALITY_NO},
        }
        consequence = "NO_SURFACE_EFFECT"
        no_surface_reason = ("头足类非鱼边界样本（FCF 鱼语义边界外）——Product Scope Deferred"
                             "（FR3 FISH-R07 判例②：不套 P01 不立鱼侧 pattern）；光 cue 轴 "
                             "provisional 挂 K8 与无饵 jig 捕获路径 CB 轴均由 FR 线承载；"
                             "26 Story 中唯一 0 程序样本，四面 NO_SURFACE_EFFECT 显式记录")
    else:
        resp_reason = ("P04 guard 双 Path（food ∥ species-typed conflict → COMBINE）"
                       if sid == "HNC" else "P01 typed 离散目标响应")
        surfaces = {
            "Group": {"consequence": "NO_SURFACE_EFFECT", "reason": GROUP_NO[sid]},
            "Bake": {"consequence": "NEW_PROGRAM_CANDIDATE",
                     "program_ids": [f"P-B4-{sid}-BAKE"],
                     "reason": "栖息/周期空间因子程序证据（S8 MSF 全 25 例）"},
            "Response": {"consequence": "NEW_PROGRAM_CANDIDATE",
                         "program_ids": [f"P-B4-{sid}-RESP"],
                         "reason": resp_reason},
            "Quality": {"consequence": "NO_SURFACE_EFFECT", "reason": QUALITY_NO},
        }
        consequence = "NEW_PROGRAM_CANDIDATE"
        no_surface_reason = None
    rec = {
        "story_id": f"CENSUS-B4-{sid}", "source_story": TITLE[sid],
        "story_url": URLS[sid],
        "frozen_patterns": PATTERNS[sid],
        "sweep_log_mapping": SWEEPS[sid],
        "surfaces": surfaces,
        "consequence": consequence,
        "provenance": {"batch": "CENSUS-B4"},
    }
    if no_surface_reason:
        rec["no_surface_reason"] = no_surface_reason
    return rec


def main():
    out = BATCH_DIR / "stories.jsonl"
    recs = [story_rec(sid) for sid in SWEEPS]
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in recs) + "\n",
                   encoding="utf-8")
    n_prog = sum(1 for r in recs for s in r["surfaces"].values()
                 if s["consequence"] == "NEW_PROGRAM_CANDIDATE")
    print(f"wrote {len(recs)} stories; program-bearing surfaces={n_prog}")


if __name__ == "__main__":
    main()
