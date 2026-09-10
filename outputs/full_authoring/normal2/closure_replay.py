#!/usr/bin/env python3
# REP-FULL-NORM2-001 closure replay — mechanical adjudication of all 267 CSV
# rows against the four P01 grouping rules (REP-FULL-NORM-001 §1, REV-001
# confirmed mechanically replayable) and this batch's closed exclusion
# taxonomy (README §1.4). Proves the full-closure claim: every eligible row
# lands in exactly one of R1-carried / N2(this batch, 72 files) / SIB /
# EXCLUDED(with reason); zero unhandled rows. Pure standard library.
#
# Usage: python closure_replay.py   (from anywhere; reads CSV via relative
# path from repo root or its own parent directory chain)
import csv
import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# --- carried-by-round-one (59 eligible rows incl. variant-merge White
# Platinum gar; name-diff corrections: 虎纹鳟鱼=tiger_trout, 虎纹梭鱼=
# tiger_musky, 红尾鲶鱼=redtail_catfish) ---
R1 = set(
    "鳄雀鳝 白斑狗鱼 佛罗里达雀鳝 鳜鱼 笋壳鱼 彩虹镖鲈 黄颡鱼 翘嘴红鲌 蒙古红鲌 斑鳜 "
    "俄罗斯鲟 光倒刺鲃 女巫鲽 淡水石首鱼 弓鳍鱼 眼鳢 斑点雀鳝 虎纹狗鱼 细鳞鲑 巨鲶 哲罗鲑 "
    "赤稍雅罗鱼 黑线鳕 鼠鲨 大西洋大比目鱼 虎纹鳟 绿青鳕 湖红点鲑 黄鲈 北美狗鱼 白马切喉鳟 "
    "链纹狗鱼 鬼头刀 革胡子鲶 土鲶 金眼鱼 六须鲶 加拿大梭鲈 斑点叉尾鮰 美洲鳗鲡 红尾鲶 "
    "虎纹鸭嘴鲇 云斑鮰 褐鳟 虹鳟 鸭嘴鲟 鳡鱼 麦穗鱼 海鲈 宽鳍𫚭 唇䱻 迷人真小鲤 "
    "白斑刺盖太阳鱼 黑斑刺盖太阳鱼 驼背太阳鱼 美洲条纹狼鲈 白斑角鲨 棘背钝头鳐 大青鲨 "
    "白金火箭 虎纹鳟鱼 虎纹梭鱼 红尾鲶鱼".split()
)

# --- this batch: the 72 species files (species/*.md), by CSV row name ---
N2 = set(
    "花骨鱼 大西洋鳕鱼 欧洲巨鲶 玻璃梭鲈 公牛鲨 江鳕 牛头鲦 白亚口鱼 黄金鲫 "
    "星点东方鲀 黑鲷 沙鮻 大西洋黄盖鲽 闪光鲟 北极茴鱼 银龙鱼 尖吻鲟 短吻鲟 "
    "黑口红点鲑 塞凡湖鳟 丁鱥 旗鱼 牛港鲹 黄旗金枪鱼 条纹四鳍旗鱼 葛氏鲈塘鳢 "
    "东方狐鲣 针牙脂鲤 大西洋牙鲆 鞍带石斑鱼 裸狐鲣 美洲拟鲽 巨狼鱼 巴西马鲛 "
    "双线无须鳕 大眼金枪鱼 黄尾鰤 长吻鲍氏脂鲤 太平洋蓝鳍金枪鱼 蓝笛鲷 红尾梭鱼 "
    "花鮨 高体鰤 赤梢鱼 长鳍金枪鱼 大西洋小鳕 康氏马鲛 条石鲷 黑食人鱼 巴亚拉鱼 "
    "红鳍狗鱼 美国红鱼 眼点丽鱼 月眼鱼 白鲶鱼 蓝鲶鱼 黑鮰 铲鮰 "
    "蓝鲨 斑点黑鲈 绿太阳鱼 岩钝鲈 日本鲭 常见鮈鱼 茅尖鱼 大理石倒立鱼 小须美鱥 "
    "花羔红点鲑 金目丽鱼 奥里诺科孔雀鲈 真鲷 鲻鱼".split()
)

# --- carried by sibling batches (Normal/Feeding face carried in
# guarding/grazing/migration/field files) ---
SIB = set(
    "蓝鳃太阳鱼 小口黑鲈 地图鱼 南美肺鱼 电鳗 七彩神仙橙 乌鳢 罗非鱼 红腹食人鱼 "
    "巨骨舌鱼 双点美鱥 米达斯慈鲷 淡水石斑 孔雀鲈 接吻鲷 圆鳍鱼 单鳍多线鱼 "
    "大西洋鲑 大马哈鱼 美洲西鲱 白北鲑 高首鲟 北极红点鲑 欧白鲑 剑旗鱼 帝王鲑 "
    "红鲑 银鲑 灰西鲱 美洲红点鲑 大西洋大海鲢 欧鲢 圆腹雅罗鱼 银鲫 大口牛胭脂鱼 "
    "七彩神仙鱼（橙） 七彩神仙鱼（白） 大西洋鲑鱼 黑斑须雅罗鱼 溪鲦 湄公巨鲶 "
    "印度鲮 泰鲮 巴西鲷 暹罗巨鲤 金草鱼".split()
)

# --- exclusion taxonomy (README §1.4 classes 1-19; class 0 = SIB above) ---
EXCL = {
    1: "FIELD 批补批（handoff 指定）",
    2: "census P02/P03/K3 冻结",
    3: "K4 繁殖锚聚类",
    4: "品系/变体行不分裂（L1-EQUIV 层）",
    5: "Carassius 属种群对账线",
    6: "同种异行（虹鳟种复合体）",
    7: "植食/滤食→P06/P03 对账线",
    8: "亚口科 P06 张力（grazing 批登记 1）",
    9: "whitefish 系 P05 对账",
    10: "鲑科洄游行 P05 对账",
    11: "七鳃鳗系（cue 轴线/身份待核）",
    12: "Story DB 0 Story（Identity 隔离）",
    13: "P04 补批对账",
    14: "头足类 Product Scope Deferred",
    15: "鳐身份三候选待澄清",
    16: "R09 拟鲤双行对账",
    17: "花鲈种复合体双行对账",
    18: "P03 场化承载互指+机会组从紧",
    19: "名实错位待核",
}
EXCL_ROWS = {
    1: ["鲢鱼"],
    2: ["黑鼓鱼", "草鱼", "鳙鱼", "大西洋鲱鱼", "青鱼", "鲤鱼", "鲮"],
    3: ["毛鳞鱼"],
    4: ["锦鲤", "荷包红鲤", "镜鲤", "红罗非", "工程鲫", "鳞鲤(白化)", "鳞鲤(人面鲤)",
        "四白锦鲤", "镜鲤(白化)", "红白锦鲤", "白化草鱼", "无鳞鲤", "圆点五色锦鲤",
        "橙黄金锦鲤", "白化高首鲟", "白化叉尾鮰"],
    5: ["野生鲫鱼", "金鲫"],
    6: ["金鳟", "硬头鳟"],
    7: ["淡水白鲳", "美洲锐唇鲷", "红钩鱼", "日本竹荚鱼", "湖白鲑"],
    8: ["水牛鱼", "金红马鱼", "河红马鱼", "黑牛胭脂鱼"],
    9: ["驼背白鲑", "高白鲑"],
    10: ["粉鲑"],
    11: ["海七鳃鳗", "西方七鳃鳗"],
    12: ["大口黑鲈"],
    13: ["大西洋狼鱼"],
    14: ["莱氏拟乌贼"],
    15: ["大西洋黄貂鱼", "眼斑河魟"],
    16: ["常见拟鲤", "湖拟鲤"],
    17: ["海鲈鱼"],
    18: ["短扁口鲶"],
    19: ["枯叶鱼"],
}
ROW_TO_CLASS = {n: c for c, names in EXCL_ROWS.items() for n in names}

# --- species files on disk (cross-check N2 set vs species/*.md) ---
HERE = Path(__file__).resolve().parent
SPECIES_ZH = {
    "spotted_steed": "花骨鱼", "atlantic_cod_feeding": "大西洋鳕鱼",
    "wels_catfish_feeding": "欧洲巨鲶", "walleye_feeding": "玻璃梭鲈",
    "bull_shark": "公牛鲨", "burbot": "江鳕", "bullhead_minnow": "牛头鲦",
    "white_sucker": "白亚口鱼", "golden_crucian": "黄金鲫",
    "grass_puffer": "星点东方鲀", "blackhead_seabream": "黑鲷",
    "northern_whiting": "沙鮻", "yellowtail_flounder": "大西洋黄盖鲽",
    "stellate_sturgeon": "闪光鲟", "arctic_grayling": "北极茴鱼",
    "silver_arowana": "银龙鱼", "atlantic_sturgeon": "尖吻鲟",
    "shortnose_sturgeon": "短吻鲟", "blackmouth_char": "黑口红点鲑",
    "sevan_trout": "塞凡湖鳟", "tench": "丁鱥", "sailfish": "旗鱼",
    "giant_trevally": "牛港鲹", "yellowfin_tuna": "黄旗金枪鱼",
    "striped_marlin": "条纹四鳍旗鱼", "chinese_sleeper": "葛氏鲈塘鳢",
    "striped_bonito": "东方狐鲣", "biara": "针牙脂鲤",
    "summer_flounder": "大西洋牙鲆", "giant_grouper": "鞍带石斑鱼",
    "dogtooth_tuna": "裸狐鲣", "winter_flounder": "美洲拟鲽",
    "giant_wolffish": "巨狼鱼", "serra_mackerel": "巴西马鲛",
    "silver_hake": "双线无须鳕", "bigeye_tuna": "大眼金枪鱼",
    "yellowtail_amberjack": "黄尾鰤", "bicuda": "长吻鲍氏脂鲤",
    "pacific_bluefin": "太平洋蓝鳍金枪鱼", "green_jobfish": "蓝笛鲷",
    "redtail_barracuda": "红尾梭鱼", "anthias": "花鮨",
    "greater_amberjack": "高体鰤", "european_perch": "赤梢鱼",
    "albacore": "长鳍金枪鱼", "atlantic_tomcod": "大西洋小鳕",
    "narrowbarred_mackerel": "康氏马鲛", "rock_bream": "条石鲷",
    "black_piranha": "黑食人鱼", "payara": "巴亚拉鱼",
    "redfin_pickerel": "红鳍狗鱼", "red_drum": "美国红鱼",
    "butterfly_peacock": "眼点丽鱼", "mooneye": "月眼鱼",
    "white_catfish": "白鲶鱼", "blue_catfish": "蓝鲶鱼",
    "black_bullhead": "黑鮰", "flathead_catfish": "铲鮰",
    "iridescent_shark": "蓝鲨", "spotted_bass": "斑点黑鲈",
    "green_sunfish": "绿太阳鱼", "rock_bass": "岩钝鲈",
    "chub_mackerel": "日本鲭", "common_gudgeon": "常见鮈鱼",
    "pike_cichlid": "茅尖鱼", "headstander": "大理石倒立鱼",
    "river_chub": "小须美鱥", "dolly_varden": "花羔红点鲑",
    "speckled_peacock": "金目丽鱼", "orinoco_peacock": "奥里诺科孔雀鲈",
    "red_seabream": "真鲷", "grey_mullet": "鲻鱼",
}


def diet(r):
    try:
        return json.loads(r["食性（源表候选）"]) if r["食性（源表候选）"] else []
    except (ValueError, TypeError):
        return []


def main():
    root = HERE.parent.parent.parent  # outputs/full_authoring/normal2 -> repo
    csv_path = None
    for cand in (
        root / "outputs/fish-reference-20260908/fish-reference-20260908.csv",
        Path("outputs/fish-reference-20260908/fish-reference-20260908.csv"),
    ):
        if cand.exists():
            csv_path = cand
            break
    if csv_path is None:
        print("FAIL: fish-reference-20260908.csv not found")
        sys.exit(1)

    rows = list(csv.DictReader(open(csv_path, encoding="utf-8-sig")))
    stats, unhandled, out_of_scope = {}, [], {}
    for i, r in enumerate(rows, 1):
        c, d, t = r["性格"], diet(r), r["时段偏好"]
        carn, omni, noct = ("肉食性" in d), ("杂食性" in d), ("夜间" in t)
        if c in ("孤僻", "躲藏") and carn and not noct:
            tag = "ambush"
        elif c == "追猎" and carn and not noct:
            tag = "pursuit"
        elif noct and (carn or omni):
            tag = "nocturnal"
        elif c in ("活泼", "温和", "撕鳍", "好斗", "警惕"):
            tag = "opportune"
        else:
            out_of_scope.setdefault(r["中文名"], i)
            continue
        n = r["中文名"]
        if n in R1:
            cls = "R1"
        elif n in N2:
            cls = "N2"
        elif n in SIB:
            cls = "SIB"
        elif n in ROW_TO_CLASS:
            cls = f"EXCL:{ROW_TO_CLASS[n]}"
        else:
            cls = "???"
            unhandled.append(f"row {i} {n}")
        key = cls.split(":")[0]
        stats.setdefault(tag, {})
        stats[tag][key] = stats[tag].get(key, 0) + 1

    # cross-check: every species file on disk maps to an N2 row, and vice versa
    files = sorted(p.stem for p in (HERE / "species").glob("*.md"))
    file_zh = {f: SPECIES_ZH.get(f, "?") for f in files}
    missing_on_disk = sorted(n for n in N2 if n not in file_zh.values())
    missing_in_set = sorted(f for f in files if file_zh[f] == "?")

    grand = 0
    for g in ("ambush", "pursuit", "nocturnal", "opportune"):
        s = stats[g]
        tot = sum(s.values())
        grand += tot
        print(f"{g}: total={tot} R1={s.get('R1',0)} N2={s.get('N2',0)} "
              f"SIB={s.get('SIB',0)} EXCL={s.get('EXCL',0)}")
    print(f"grand total eligible rows: {grand} (expected 220)")
    print(f"rows out of grouping scope (not adjudicated by CSV rules): {len(out_of_scope)}")
    print(f"unhandled eligible rows: {unhandled if unhandled else 'NONE — FULL CLOSURE'}")
    print(f"species files on disk: {len(files)} (expected 72)")
    print(f"N2 set vs disk mismatch: missing_on_disk={missing_on_disk or 'NONE'} "
          f"unmapped_files={missing_in_set or 'NONE'}")
    ok = (grand == 220 and not unhandled and len(files) == 72
          and not missing_on_disk and not missing_in_set)
    print(f"== closure replay ==\n{'PASS' if ok else 'FAIL'}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
