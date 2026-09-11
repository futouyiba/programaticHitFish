# -*- coding: utf-8 -*-
"""CENSUS-B6 stories.jsonl 生成器：47 Story（FISH-R10 收官批）× Sweep Log
S1-S11 逐项映射（program / premise / param / excluded / eo / sn / tar）
+ Surface 四面判定。盲段产物（registry 未读）。

R10 为压缩模板批：Sweep Surface Log 记法压缩为「Sx MSF(...)｜Sx SN｜...｜余 SN」
单行；无信封转写文件（PKS/BBH）径从「内容作者」行起（B5 CSL 同型）。
47/47 双面程序（Bake+Response）；2 例 Response 为 P04 guard 双 Path
（AWF 狼鱼/LFB 大鳍𫚪）。品系 12 行 Sweep 行宣称「全面 SN」——FCF 层有 P01
复用主张，census 程序承载为复用推算（映射记 program: 承载注记，差异在
manifest 记档）。"""
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent

PROG = "program:"
PREM = "premise->"
PAR = "param->"
EXC = "excluded:"
EO = "eo_no_program"
SN = "sn"

SRC = "https://app.notion.com/p/3d7a4137d23681"
URLS = {
    "SUK": SRC+"5bb5e3d2ec6c3b2869", "GRK": SRC+"4cb047ec23773a0918",
    "KHK": SRC+"6b9ba1da26d9c78d6e", "OGK": SRC+"1c99f6c347abaaef5c",
    "LCP": SRC+"5b80c2e23dac3be7eb", "AMC": SRC+"8892c9c5f1c0e4533e",
    "HFC": SRC+"06b433ff866961c095", "ASC": SRC+"cf900cddc64a083bba",
    "WCC": SRC+"b8b0f8e4e1fc824257", "AGC": SRC+"bf8602d799373dddd6",
    "WS2": SRC+"1b8160d0dfb297f56e", "WAG": SRC+"c39446dde48c078624",
    "HYS": SRC+"4999ecf8b16a4ed86b", "ACA": SRC+"1c82e5d1d02f4e8a22",
    "ATC": SRC+"739eaed37a4668f426", "AWF": SRC+"c096bed186d4eb6ee7",
    "PSH": SRC+"c4a80ac9828df1bb19", "LFB": SRC+"468d6df2df98d42556",
    "BMB": SRC+"a09856e09c85eaa548", "PLC": SRC+"70847be36f0c3a2da9",
    "SSM": SRC+"e892d4d8a4c4cfc9bb", "CGD": SRC+"cd95fbe74a22d1d9db",
    "GDB": SRC+"9f9475d1766007ccc8", "RBD": SRC+"fca30dedac6ddd2856",
    "RUF": SRC+"84808aee1ee2529b3c", "DBC": SRC+"25831fc171a2e93c58",
    "JSB": SRC+"71bc75ef7259f75789", "ASB": SRC+"23b84bdfcad0c1fd77",
    "DCL": SRC+"31a6bff4842e29faa8", "BHM": SRC+"c684c8dc87df817137",
    "WHC": SRC+"6388a9dab075a2efbb", "PRB": SRC+"4da518f55de491fd74",
    "RSS": SRC+"199170c957a1741514", "PCC": SRC+"a78225d1bacd38b1ca",
    "STS": SRC+"9b81d5fcdcf8285451", "PKC": SRC+"93b009c192b068fc3c",
    "BCF": SRC+"db944efd760f8ebe94", "TGS": SRC+"65b516fa5f44d871b5",
    "EUP": SRC+"de813bf105de96e004", "BTS": SRC+"018e8fec8281f1f43e",
    "GDS": SRC+"44a875d04ceaa100e4", "SLM": SRC+"98a8b6d0e5b23c89b5",
    "PKS": SRC+"2a9616e679fd88e54e", "BLT": SRC+"0495c2c7c9ae82ee73",
    "RSC": SRC+"c6b5c2ff8c9dae1d60", "BBH": SRC+"07b563fefd977c8ef5",
    "AMN": SRC+"cea7a7de48ed603f54",
}

TITLE = {
    "SUK": "FISH-R10｜四白锦鲤｜Shiro Utsuri Koi｜Strain Default",
    "GRK": "FISH-R10｜圆点五色锦鲤｜Goromo Koi｜Strain Default",
    "KHK": "FISH-R10｜红白锦鲤｜Kohaku Koi｜Strain Default",
    "OGK": "FISH-R10｜橙黄金锦鲤｜Ogon Koi｜Strain Default",
    "LCP": "FISH-R10｜无鳞鲤｜Leather Carp｜Strain Default",
    "AMC": "FISH-R10｜镜鲤白化｜Albino Mirror Carp｜Strain Default",
    "HFC": "FISH-R10｜鳞鲤人面鲤｜Human Face Scale Carp｜Strain Default",
    "ASC": "FISH-R10｜鳞鲤白化｜Albino Scale Carp｜Strain Default",
    "WCC": "FISH-R10｜白化叉尾鮰｜White Channel Catfish｜Strain Default",
    "AGC": "FISH-R10｜白化草鱼｜Albino Grass Carp｜Strain Default",
    "WS2": "FISH-R10｜白化高首鲟｜White Sturgeon 02｜Strain Default",
    "WAG": "FISH-R10｜白金火箭｜White Alligator Gar｜Strain Default",
    "HYS": "FISH-R10｜杂交飼｜Hybrid Sturgeon｜Sterile-Hybrid Aquaculture 3rd",
    "ACA": "FISH-R10｜土鲶｜Amur Catfish｜Silurus Congeneric 2nd",
    "ATC": "FISH-R10｜大西洋小鳕｜Atlantic Tomcod｜Miniature Anadromous Cod",
    "AWF": "FISH-R10｜大西洋狼鱼｜Atlantic Wolffish｜Hard-Shell Fasting Guarder",
    "PSH": "FISH-R10｜大青鲨｜Paroon Shark｜Misnamed-Giant Pangasiid",
    "LFB": "FISH-R10｜大鳍𫚪｜Largefin Bitterling｜Mussel-Breeding 2nd",
    "BMB": "FISH-R10｜大鳞鲃｜Bulatmai Barbel｜Semi-Anadromous Barbel",
    "PLC": "FISH-R10｜宽鳍𫚭｜Pale Chub｜Riffle Omnivore",
    "SSM": "FISH-R10｜巴西马鲛｜Serra Spanish Mackerel｜Mackerel Congeneric 3rd",
    "CGD": "FISH-R10｜常见鮈鱼｜Common Gudgeon｜Sand-Bottom Baitfish",
    "GDB": "FISH-R10｜广东鲂｜Guangdong Bream｜Bream Congeneric 2nd",
    "RBD": "FISH-R10｜彩虹镖鲈｜Rainbow Darter｜Riffle Micro-Benthic First",
    "RUF": "FISH-R10｜梅花鲈｜Ruffe｜Eutrophic Invader",
    "DBC": "FISH-R10｜江黄颡｜Darkbarbel Catfish｜Bagrid Congeneric",
    "JSB": "FISH-R10｜海鲈｜Japanese Seabass｜Congeneric Reference",
    "ASB": "FISH-R10｜海鲈鱼｜Asian Seabass｜Catadromous Protandrous",
    "DCL": "FISH-R10｜湘华鮈｜Decoris Labeo｜Thin-Data Congeneric",
    "BHM": "FISH-R10｜牛头鲦｜Bullhead Minnow｜Pool Minnow",
    "WHC": "FISH-R10｜白鲶鱼｜White Catfish｜Ictalurid 3rd",
    "PRB": "FISH-R10｜短扁口鲶｜Piraiba｜Amazon Giant Apex",
    "RSS": "FISH-R10｜红斑太阳鱼｜Redspotted Sunfish｜Sunfish 6th",
    "PCC": "FISH-R10｜细纹鲶鱼｜Pencil Catfish｜Thin-Data Trichomycterid",
    "STS": "FISH-R10｜花鮨｜Swallowtail Seaperch｜Deep-Reef Nocturnal",
    "PKC": "FISH-R10｜茅尖鱼｜Pike Cichlid｜Piscivorph Cichlid",
    "BCF": "FISH-R10｜蓝鲶鱼｜Blue Catfish｜Deep-Channel Nightfeeder",
    "TGS": "FISH-R10｜虎纹鸭嘴鲇｜Tiger Sorubim｜Nocturnal Floodplain Pimelodid",
    "EUP": "FISH-R10｜赤梢鱼｜European Perch｜Diurnal Opportunist Misnamed",
    "BTS": "FISH-R10｜迷人真小鲤｜Blacktail Shiner｜Surface-Insect Shiner",
    "GDS": "FISH-R10｜金体美鱥｜Golden Shiner｜Baitfish Supply Role",
    "SLM": "FISH-R10｜银斑鲫｜Silver Mylossoma｜Floodplain Herbivore 3rd",
    "PKS": "FISH-R10｜高体太阳鱼｜Pumpkinseed｜太阳鱼系第 7 例（无信封转写——标题从 Evidence 学名 Lepomis gibbosus 推）",
    "BLT": "FISH-R10｜黑口红点鲑｜Bull Trout｜Misnamed Cold-Pool Char",
    "RSC": "FISH-R10｜黑棘鲶｜Ripsaw Catfish｜Schooling Doradid",
    "BBH": "FISH-R10｜黑鮰｜Brown Bullhead｜鲿科第 4 例（无信封转写——标题从 Evidence 学名 Ameiurus melas 推）",
    "AMN": "FISH-R10｜柳根鱼｜Amur Minnow｜Thin-Diet Minnow",
}

# frozen_patterns（正文 FCF Interpretation/Semantic Pattern Fit 节组合为准；
# DB Semantic Pattern 字段差异在 manifest 记档）
PATTERNS = {}
for k in URLS:
    PATTERNS[k] = ["P01"]
for k in ["AGC", "SLM"]:
    PATTERNS[k] = ["P01", "P02"]
for k in ["ATC", "BMB", "SSM", "PSH", "ASB", "PRB", "WS2", "HYS"]:
    PATTERNS[k] = ["P01", "P05"]
for k in ["AWF", "LFB"]:
    PATTERNS[k] = ["P01", "P04"]


def R(code):
    return "P-B6-" + code + "-RESP"


def B(code):
    return "P-B6-" + code + "-BAKE"


# S1-S11 逐项映射（解析自各 Story Sweep Surface Log 行 + FCF 承载注记）
SWEEP = {
    # 品系 12（Sweep 行宣称全面 SN——FCF 层 P01 复用主张承载，映射记 program: 附注）
    **{c: {"S1": PROG + R(c) + "（品系复用推算承载——story Sweep 行宣称 SN，FCF "
              "Interpretation 有 P01 复用主张）",
           "S8": PROG + B(c) + "（品系复用推算承载，同上）"}
       for c in ["SUK", "GRK", "KHK", "OGK", "LCP", "AMC", "HFC", "ASC",
                 "WCC", "WAG"]},
    "AGC": {"S1": PROG + R("AGC") + "（品系复用推算承载——Sweep 行宣称 SN；P01+"
            "P02 grazing 复用）",
            "S8": PROG + B("AGC") + "（品系复用推算承载）"},
    "WS2": {"S1": PROG + R("WS2") + "（品系复用推算承载——Sweep 行宣称 SN；"
            "P01+P05 复用）",
            "S5": PREM + B("WS2") + "（亲本溯河 lifecycle——品系复用）",
            "S8": PROG + B("WS2") + "（品系复用推算承载）"},
    "HYS": {"S1": PROG + R("HYS") + "（飼系 P01 复用——MSF）",
            "S5": PREM + B("HYS") + "（飼系洄游 lifecycle 复用）",
            "S8": PROG + B("HYS") + "（飼系底栖——MSF）"},
    # 普通层 34
    "ACA": {"S1": PROG + R("ACA") + "（全鱼食 MSF）",
            "S4": SN,
            "S7": EO + "（夜行同属推断——runtime 时窗 premise 由程序 typed "
                   "context 承载，story 记 EO）",
            "S8": PROG + B("ACA") + "（河湖 MSF）"},
    "ATC": {"S1": PROG + R("ATC") + "（甲壳/虫/贝/鱿/鱼 MSF）",
            "S5": PREM + B("ATC") + "（anadromous 溯河 MSF）",
            "S8": PROG + B("ATC") + "（沿岸/咸淡水 MSF）"},
    "AWF": {"S1": PROG + R("AWF") + "（硬壳/鱼 MSF）",
            "S2": PAR + R("AWF") + "（碾压齿系 typed context MSF）",
            "S4": SN,
            "S6": PROG + R("AWF") + "（雄护卵块+护卵期停食 MSF——P04 双 Path；"
                   "停食=护卵期持续状态 premise）",
            "S8": PROG + B("AWF") + "（岩底 MSF）"},
    "PSH": {"S1": PROG + R("PSH") + "（鱼/甲壳 MSF）",
            "S4": SN,
            "S5": PREM + B("PSH") + "（potamodromous MSF）",
            "S8": PROG + B("PSH") + "（大河 MSF）",
            "S9": PREM + R("PSH") + "（幼-成同食性 MSF——ontogeny premise）",
            "S11": EO + "（CR 保护边界——OPS 产品面）"},
    "LFB": {"S1": PROG + R("LFB") + "（trophic 2.0 推算承载——story 记 EO）",
            "S5": SN,
            "S6": PROG + R("LFB") + "（贝内产卵+幼贝发育 MSF——P04 双 Path）",
            "S8": PROG + B("LFB") + "（河湖 MSF）"},
    "BMB": {"S1": PROG + R("BMB") + "（杂食 MSF）",
            "S5": PREM + B("BMB") + "（半溯河 MSF）",
            "S8": PROG + B("BMB") + "（海/河口/河 MSF）"},
    "PLC": {"S1": PROG + R("PLC") + "（杂食 MSF）",
            "S8": PROG + B("PLC") + "（急流 MSF）"},
    "SSM": {"S1": PROG + R("SSM") + "（鱼/虾/鱿 MSF）",
            "S3": SN,
            "S5": PREM + B("SSM") + "（oceanodromous MSF）",
            "S8": PROG + B("SSM") + "（礁相关 MSF）"},
    "CGD": {"S1": PROG + R("CGD") + "（虫/贝/甲壳 MSF）",
            "S3": EXC + "沙底急流群游=群结构事实非互斥 FishGroup",
            "S8": PROG + B("CGD") + "（沙底急流 MSF）"},
    "GDB": {"S1": PROG + R("GDB") + "（食性同属推算承载——story 记 EO）",
            "S8": PROG + B("GDB") + "（河川 MSF）"},
    "RBD": {"S1": PROG + R("RBD") + "（水生虫幼+鱼卵 MSF）",
            "S6": PREM + R("RBD") + "（卵埋底质 MSF——产卵行为变量非 guard，"
                   "story FR 层明言）",
            "S8": PROG + B("RBD") + "（急流砂礫濑 MSF）"},
    "RUF": {"S1": PROG + R("RUF") + "（浮游/虫/鱼 MSF）",
            "S8": PROG + B("RUF") + "（富营湖/河口 MSF）",
            "S9": PREM + R("RUF") + "（沿海鱼食 MSF——生境分化记录非分支）"},
    "DBC": {"S1": PROG + R("DBC") + "（食性同属推算承载——story 记 EO）",
            "S8": PROG + B("DBC") + "（栖息未述——同属推算承载，story 记 EO）"},
    "JSB": {"S1": PROG + R("JSB") + "（同属参照承载——story 记 EO；与 ASB 同 "
            "URL 同源去重联动注记）",
            "S8": PROG + B("JSB") + "（同属近岸岩礁 MSF）"},
    "ASB": {"S1": PROG + R("ASB") + "（浮游→鱼虾 MSF）",
            "S5": PREM + B("ASB") + "（catadromous 降海 MSF）",
            "S6": PREM + R("ASB") + "（冬深岩礁产卵 MSF——lifecycle premise）",
            "S8": PROG + B("ASB") + "（近岸岩礁 MSF）",
            "S9": PREM + R("ASB") + "（雄先熟性转换 MSF——繁殖系统变量 premise）"},
    "DCL": {"S1": PROG + R("DCL") + "（薄资料同属推算承载——story 记 EO）",
            "S8": PROG + B("DCL") + "（同属河川底栖 MSF）"},
    "BHM": {"S1": PROG + R("BHM") + "（虫幼 MSF）",
            "S8": PROG + B("BHM") + "（静潭沙泥 MSF）"},
    "WHC": {"S1": PROG + R("WHC") + "（鱼/虫/甲壳 MSF）",
            "S8": PROG + B("WHC") + "（泥底潭沼 MSF）"},
    "PRB": {"S1": PROG + R("PRB") + "（鱼食+大型猎物 MSF）",
            "S5": PREM + B("PRB") + "（potamodromous MSF）",
            "S8": PROG + B("PRB") + "（河口咸淡水 MSF）"},
    "RSS": {"S1": PROG + R("RSS") + "（底栖无脊椎 MSF）",
            "S8": PROG + B("RSS") + "（静水底 MSF）"},
    "PCC": {"S1": PROG + R("PCC") + "（食性无述同属推算承载——story 记 EO）",
            "S8": PROG + B("PCC") + "（同科底栖 MSF）"},
    "STS": {"S1": PROG + R("STS") + "（夜行甲壳/小鱼 MSF）",
            "S7": PREM + R("STS") + "（夜行 MSF——昼夜时窗 premise）",
            "S8": PROG + B("STS") + "（深礁 30-358m MSF）"},
    "PKC": {"S1": PROG + R("PKC") + "（掠食型推算承载——story 记 EO）",
            "S8": PROG + B("PKC") + "（热带河 MSF）"},
    "BCF": {"S1": PROG + R("BCF") + "（无脊椎/贝/鱼 MSF）",
            "S7": PREM + R("BCF") + "（夜间摄食 MSF——昼夜时窗 premise）",
            "S8": PROG + B("BCF") + "（深潭主河道 MSF）"},
    "TGS": {"S1": PROG + R("TGS") + "（夜鱼食+蟹 MSF）",
            "S4": PREM + B("TGS") + "（洪泛林 MSF——栖息绑定）",
            "S7": PREM + R("TGS") + "（夜行 MSF——昼夜时窗 premise）",
            "S8": PROG + B("TGS") + "（主河道 MSF）"},
    "EUP": {"S1": PROG + R("EUP") + "（昼间机会食 MSF）",
            "S4": PREM + R("EUP") + "（日升日落捕食峰 MSF——昼夜时窗 premise）",
            "S6": PREM + R("EUP") + "（卵带产 MSF——lifecycle premise）",
            "S8": PROG + B("EUP") + "（湖潭 MSF）",
            "S9": PREM + R("EUP") + "（12cm 起鱼食 MSF——ontogeny premise）"},
    "BTS": {"S1": PROG + R("BTS") + "（水面昆虫 MSF）",
            "S7": PAR + R("BTS") + "（水面呈现 typed——B5 ARG 同型）",
            "S8": PROG + B("BTS") + "（沙潭 MSF）"},
    "GDS": {"S1": PROG + R("GDS") + "（浮游/虫/贝 MSF）",
            "S8": PROG + B("GDS") + "（植被湖潭 MSF）",
            "S10": EXC + "钓饵鱼供给角色=产品面（B5 RVC 同属先例）"},
    "SLM": {"S1": PROG + R("SLM") + "（草食 MSF）",
            "S4": PREM + B("SLM") + "（洪泛依赖 MSF——P02 资源面背景）",
            "S8": PROG + B("SLM") + "（洪泛湖 MSF）"},
    "PKS": {"S1": PROG + R("PKS") + "（小鱼/无脊椎 MSF）",
            "S8": PROG + B("PKS") + "（植被静水 MSF）"},
    "BLT": {"S1": PROG + R("BLT") + "（食性未详——P01 冻结主张承载，story 记 EO）",
            "S5": PREM + B("BLT") + "（potamodromous MSF）",
            "S8": PROG + B("BLT") + "（深潭冷水 MSF）",
            "S11": EO + "（V 保护边界——OPS 产品面）"},
    "RSC": {"S1": PROG + R("RSC") + "（腐屑/虫/甲壳 MSF）",
            "S3": EXC + "泥底群游=群结构事实非互斥 FishGroup",
            "S8": PROG + B("RSC") + "（泥底 MSF）"},
    "BBH": {"S1": PROG + R("BBH") + "（虫/贝/植物/鱼 MSF）",
            "S7": PREM + R("BBH") + "（夜行 MSF——昼夜时窗 premise）",
            "S8": PROG + B("BBH") + "（软底潭沼 MSF）"},
    "AMN": {"S1": PROG + R("AMN") + "（同属推算承载——story 记 EO）",
            "S8": PROG + B("AMN") + "（河川 MSF）"},
}


def story_rec(sid):
    full = {f"S{i}": SN for i in range(1, 12)}
    full.update(SWEEP[sid])
    group_exc = ("NO_SURFACE_EFFECT"
                 if sid in ("CGD", "RSC")
                 else "NO_SURFACE_EFFECT")
    group_reason = {
        "CGD": "沙底急流群游=群结构事实（S3 excluded）",
        "RSC": "甲鲶科泥底群游=群结构事实（S3 excluded）",
    }.get(sid, "无互斥供给主张（S3 SN 或群结构事实排除）")
    guard = sid in ("AWF", "LFB")
    resp_reason = ("P04 guard 双 Path（food ∥ conflict → COMBINE）" if guard
                   else "P01 typed 离散目标响应（品系复用推算承载）" if sid in (
                       "SUK", "GRK", "KHK", "OGK", "LCP", "AMC", "HFC", "ASC",
                       "WCC", "AGC", "WS2", "WAG", "HYS")
                   else "P01 typed 离散目标响应")
    return {
        "story_id": "CENSUS-B6-" + sid,
        "source_story": TITLE[sid],
        "story_url": URLS[sid],
        "frozen_patterns": PATTERNS[sid],
        "sweep_log_mapping": full,
        "surfaces": {
            "Group": {"consequence": group_exc, "reason": group_reason},
            "Bake": {"consequence": "NEW_PROGRAM_CANDIDATE",
                     "program_ids": [B(sid)],
                     "reason": "栖息/洄游空间因子程序证据（S8 MSF 或复用承载）"},
            "Response": {"consequence": "NEW_PROGRAM_CANDIDATE",
                         "program_ids": [R(sid)],
                         "reason": resp_reason},
            "Quality": {"consequence": "NO_SURFACE_EFFECT",
                        "reason": "无 Quality Selection 程序证据（B0-B5 基线）"},
        },
        "consequence": "NEW_PROGRAM_CANDIDATE",
        "provenance": {"batch": "CENSUS-B6"},
    }


def main():
    out = BATCH_DIR / "stories.jsonl"
    recs = [story_rec(sid) for sid in URLS]
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False)
                             for r in recs) + "\n", encoding="utf-8")
    n_map = sum(len(r["sweep_log_mapping"]) for r in recs)
    print(f"stories: {len(recs)} sweep entries: {n_map} (expect 47*11={47*11})")


if __name__ == "__main__":
    main()
