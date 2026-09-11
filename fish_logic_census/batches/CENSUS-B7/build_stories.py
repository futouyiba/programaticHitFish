# -*- coding: utf-8 -*-
"""CENSUS-B7 stories.jsonl 生成器：112 Story × Surface 四面判定 +
（R03/R05）Sweep Surface Log S1-S11 逐项映射。盲段产物（registry 未读）。

R01/R02/R04 story 无 Sweep Surface Log 节（FR 线该三批 story 十节不含
Sweep——B1/B2 消费同源 story 同范式：sweep_log_mapping 省略，不编造）；
R03 为逐行 11 面 Sweep；R05 为压缩单行 Sx 记号 Sweep。
零程序 story 2（PAD4 S36 锚挂边界 / SEA1 S47 附着寄生）顶层
no_surface_reason；WBL（R04 西方七鳃鳗）Response=NO_SURFACE_EFFECT
（boundary-only/Product Scope Deferred）+ Bake 程序保留。"""
import io
import json
import re
from pathlib import Path

BATCH_DIR = Path(__file__).parent
SNAP = BATCH_DIR / "input_snapshots"

PAIRS = {}
for ln in (SNAP / "fetch_pairs.tsv").read_text(encoding="utf-8").splitlines():
    fid, url, title = ln.split("\t")
    PAIRS[int(fid[6:])] = (url, title)

# code -> (fetch_num, patterns, group_reason_extra)
# patterns = story 正文 FCF Interpretation 层的比较 pattern 组合
META = {
    # ---- R01 38 ----
    "WAL2": (1, ["P01"]), "CRA1": (2, ["P01"]), "CRA2": (3, ["P04"]),
    "GAR1": (4, ["P01"]), "GAR3": (5, ["P05"]), "YEP1": (6, ["P01"]),
    "YEP2": (7, ["P05"]), "BIB1": (8, ["P03"]), "BIB2": (9, ["P05"]),
    "BRT3": (10, ["P05"]), "BRT4": (11, ["P04"]), "RED1": (12, ["P02"]),
    "RED2": (13, ["P05"]), "PIK1": (14, ["P01"]), "MUL1": (14 + 1, ["P06"]),
    "MUL2": (16, ["P05"]), "RAI2": (17, ["P01"]), "RAI3": (18, ["P05"]),
    "AEL1": (19, ["P01"]), "AEL2": (20, ["P05"]), "SOK1": (21, ["P03"]),
    "SOK2": (22, ["P05"]), "SAL1": (23, ["P05"]), "SMA1": (24, ["P04"]),
    "PAD1": (25, ["P03"]), "PAD5": (27, ["P05"]), "BLU2": (28, ["P04"]),
    "CCF1": (29, ["P01"]), "CCF2": (30, ["P04"]), "TIL2": (31, ["P03"]),
    "TIL3": (32, ["P04"]), "BDR2": (33, ["P01"]), "SEA2": (35, ["P05"]),
    "COD1": (36, ["P01"]), "COD2": (37, ["P04"]), "GRA2": (38, ["P05"]),
    # ---- R02 17 ----
    "MAC1": (39, ["P03"]), "JCK1": (40, ["P03"]), "CAP1": (41, ["P03", "P05"]),
    "LWF1": (42, ["P02", "P05"]), "SIL1": (43, ["P03"]),
    "CAR1": (44, ["P02"]), "TEN1": (45, ["P02"]), "DIS2": (46, ["P04"]),
    "BON1": (47, ["P03"]), "SBS1": (48, ["P02"]), "CSN1": (49, ["P01", "P04"]),
    "BBR1": (50, ["P01", "P04"]), "RST1": (51, ["P01", "P05"]),
    "SBH1": (52, ["P02"]), "BSH1": (53, ["P05"]), "WCF1": (54, ["P01"]),
    "SZE1": (55, ["P01"]),
    # ---- R03 24 ----
    "RTL": (56, ["P01", "P02"]), "LNK": (57, ["P01", "P02"]),
    "TPC": (58, ["P01", "P02"]), "SPS": (59, ["P01", "P02"]),
    "WRC": (60, ["P01", "P02"]), "MRF": (61, ["P01"]),
    "IRS": (62, ["P01", "P02"]), "BRC": (63, ["P01", "P02"]),
    "WCR2": (64, ["P01", "P02"]), "KOI": (65, ["P01", "P02"]),
    "MIR": (66, ["P01", "P02"]), "CLC": (67, ["P01", "P02"]),
    "HMB": (68, ["P01"]), "BKC": (69, ["P01", "P02"]),
    "ASC2": (70, ["P01", "P02"]), "CHS": (71, ["P01"]),
    "RSB": (72, ["P04"]), "LJB": (73, ["P01", "P02"]),
    "MDC2": (74, ["P03"]), "YCK": (75, ["P01"]), "STM": (76, ["P01"]),
    "XCD": (77, ["P03"]), "GCR": (78, ["P01", "P02"]),
    "YCF": (79, ["P01", "P02"]),
    # ---- R04 23 ----
    "FGA4": (80, ["P01"]), "MUS": (81, ["P01"]), "SIH": (82, ["P01", "P05"]),
    "BET": (83, ["P01", "P02"]), "BWF": (84, ["P01"]), "SB2": (85, ["P01"]),
    "WCR3": (86, ["P01"]), "CTT": (87, ["P01", "P02"]),
    "RSB2": (88, ["P02", "P01"]), "BSN": (89, ["P01", "P02"]),
    "RTB": (90, ["P01"]), "RHM2": (91, ["P02", "P01"]),
    "STB": (92, ["P01", "P02"]), "DVK": (93, ["P01", "P02"]),
    "GJC": (94, ["P02", "P01"]), "WBL": (95, []),
    "CPT": (96, ["P01"]), "BIC": (97, ["P01"]),
    "SS2": (98, ["P02", "P01"]), "TNS": (99, ["P01"]),
    "MAH": (100, ["P02", "P01"]), "YTA": (101, ["P02", "P01"]),
    "BBF": (102, ["P02", "P01"]),
    # ---- R05 10 ----
    "ROH": (103, ["P06", "P05"]), "MRC": (104, ["P03"]),
    "SPR": (105, ["P06", "P05"]), "CHM": (106, ["P06", "P05"]),
    "SHB": (107, ["P03"]), "GTB": (108, ["P06", "P05"]),
    "STL": (109, ["P01", "P05"]), "WCB": (110, ["P06"]),
    "MRG": (111, ["P01"]), "IDE": (112, ["P01", "P05"]),
}

GUARD_CODES = {"CRA2", "SMA1", "BLU2", "CCF2", "TIL3", "DIS2", "CSN1",
               "BBR1", "RSB"}
FIELD_CODES = {"MAC1", "JCK1", "CAP1", "SIL1", "BON1", "MDC2", "XCD",
               "ROH", "MRC", "SPR", "CHM", "SHB", "GTB", "WCB"}
ZERO_CODES = {"PAD4": 26, "SEA1": 34}  # fetch 行号
BAKE_ONLY = {"WBL"}

# R01 表里 MUL1 的 fetch 行号修正（S21 是第 15 位）
META["MUL1"] = (15, ["P06"])


def sweep_map_r03(t, code):
    """R03 逐行 Sweep -> S1-S11 映射。"""
    m = re.search(r"## Sweep Surface Log\n(.*?)(?=\n</content>|\Z)", t, re.S)
    if not m:
        return None
    lines = [l for l in m.group(1).strip().splitlines() if l.strip()]
    out = {}
    for i, ln in enumerate(lines[:11], 1):
        key = f"S{i}"
        body = re.sub(r"^\d+\.\s*", "", ln).strip()
        if "MATERIAL STORY FOUND" in body:
            note = body.split("MATERIAL STORY FOUND：", 1)[-1][:40]
            if i in (1, 6):
                out[key] = ("program:P-B7-" + code + "-RESP（" + note + "）"
                            if i == 1 else
                            ("program:P-B7-" + code + "-RESP（繁殖关系面承载）"
                             if code in GUARD_CODES else
                             "premise->P-B7-" + code + "-RESP（繁殖关系 premise）"))
            elif i == 8:
                out[key] = "program:P-B7-" + code + "-BAKE（" + note + "）"
            elif i in (4, 5):
                out[key] = "premise->P-B7-" + code + "-BAKE（" + note + "）"
            elif i == 3:
                out[key] = "param->P-B7-" + code + "-RESP（" + note + "）"
            elif i == 7:
                out[key] = "param->P-B7-" + code + "-RESP（" + note + "）"
            else:
                out[key] = "sn"
        elif "SEARCHED-NO" in body:
            out[key] = "sn"
        elif "EVIDENCE OPEN" in body:
            note = body.split("EVIDENCE OPEN：", 1)[-1][:30]
            out[key] = ("eo_no_program（" + note + "）" if i not in (4, 5, 9)
                        else "eo_no_program（" + note + "）")
        elif "OUT OF PRODUCT SCOPE" in body:
            out[key] = "excluded:" + body.split("OUT OF PRODUCT SCOPE：", 1)[-1][:20]
        else:
            out[key] = "sn"
    full = {f"S{i}": "sn" for i in range(1, 12)}
    full.update(out)
    return full


def sweep_map_r05(t, code):
    """R05 压缩单行 Sweep -> 映射。"""
    m = re.search(r"## Sweep Surface Log\n(.*?)\n(?:</content>|$)", t, re.S)
    if not m:
        return None
    line = m.group(1).strip()
    full = {f"S{i}": "sn" for i in range(1, 12)}
    for part in re.split(r"[｜|]", line):
        part = part.strip()
        mm = re.match(r"S(\d+)\s+(MSF|SN|EO|OPS)(?:\(([^)]*)\))?", part)
        if not mm:
            continue
        i, tag, note = int(mm.group(1)), mm.group(2), mm.group(3) or ""
        key = f"S{i}"
        if tag == "MSF":
            if i in (1, 2, 6):
                full[key] = ("program:P-B7-" + code + "-RESP（" +
                             (note or "MSF") + "）")
            elif i in (3, 4, 5, 8):
                full[key] = ("premise->P-B7-" + code +
                             ("-BAKE（" if i in (4, 5, 8) else "-RESP（") +
                             (note or "MSF") + "）")
            elif i == 7:
                full[key] = "param->P-B7-" + code + "-RESP（" + note + "）"
            else:
                full[key] = "program:P-B7-" + code + "-BAKE（" + note + "）"
        elif tag == "EO":
            full[key] = "eo_no_program" + (("（" + note + "）") if note else "")
        elif tag == "OPS":
            full[key] = "excluded:" + (note or "产品范围外")
    return full


def story_rec(code):
    n, patterns = META[code]
    url, title = PAIRS[n]
    rec = {
        "story_id": "CENSUS-B7-" + code,
        "source_story": title,
        "story_url": url,
        "frozen_patterns": patterns,
        "surfaces": {
            "Group": {"consequence": "NO_SURFACE_EFFECT",
                      "reason": "无互斥供给主张（群游/聚集=群结构事实或发现层"
                                "线索，story 层明言不购买 FishGroup）"},
            "Bake": {"consequence": "NEW_PROGRAM_CANDIDATE",
                     "program_ids": [f"P-B7-{code}-BAKE"],
                     "reason": "栖息/洄游/空间因子程序证据（story 空间描述承载）"},
            "Response": {"consequence": "NEW_PROGRAM_CANDIDATE",
                         "program_ids": [f"P-B7-{code}-RESP"],
                         "reason": ("P04 guard 双 Path（food ∥ conflict → "
                                    "COMBINE）" if code in GUARD_CODES else
                                    "P03/P06 场评估响应（FieldFeeding——"
                                    "story 行为描述）" if code in FIELD_CODES else
                                    "P01 typed 离散目标响应")},
            "Quality": {"consequence": "NO_SURFACE_EFFECT",
                        "reason": "无 Quality Selection 程序证据（B0-B6 基线）"},
        },
        "consequence": "NEW_PROGRAM_CANDIDATE",
        "provenance": {"batch": "CENSUS-B7"},
    }
    # R03/R05 sweep 映射
    t = io.open(SNAP / f"story_{n:03d}.md", encoding="utf-8").read()
    sm = sweep_map_r03(t, code) if 56 <= n <= 79 else (
        sweep_map_r05(t, code) if 103 <= n <= 112 else None)
    if sm:
        rec["sweep_log_mapping"] = sm
    return rec


def zero_rec(code, num, reason):
    url, title = PAIRS[num]
    return {
        "story_id": "CENSUS-B7-" + code,
        "source_story": title,
        "story_url": url,
        "frozen_patterns": ["B02"] if code == "PAD4" else ["B01"],
        "surfaces": {
            "Group": {"consequence": "NO_SURFACE_EFFECT",
                      "reason": "非供给语义 story"},
            "Bake": {"consequence": "NO_SURFACE_EFFECT",
                     "reason": "无空间因子主张（同鱼其它 story 承载栖息面）"},
            "Response": {"consequence": "NO_SURFACE_EFFECT",
                         "reason": reason.split("；")[0]},
            "Quality": {"consequence": "NO_SURFACE_EFFECT",
                        "reason": "无程序证据"},
        },
        "consequence": "NO_SURFACE_EFFECT",
        "no_surface_reason": reason,
        "provenance": {"batch": "CENSUS-B7"},
    }


def main():
    recs = []
    for code in sorted(META, key=lambda c: META[c][0]):
        rec = story_rec(code)
        if code in BAKE_ONLY:
            rec["surfaces"]["Response"] = {
                "consequence": "NO_SURFACE_EFFECT",
                "reason": "boundary-only/Product Scope Deferred（story FR 层 "
                          "Semantic Open：不强并入 Target/FieldFeeding 直至 "
                          "product scope 与 owner boundary 显式）"}
        recs.append(rec)
    recs.append(zero_rec(
        "PAD4", 26,
        "B01-S36 鸭嘴鲟锚挂：Response=B02 捕获边界（story：Contact/capture "
        "owner 处理不依赖主动响应路径，FCF feeding 不添加新 Channel）；Bake 无"
        "空间主张（捕获方式 story，栖息面由同鱼 S33/S37 承载）——0 程序 story。"))
    recs.append(zero_rec(
        "SEA1", 34,
        "B01-S47 海七鳃鳗附着寄生：Response=实例化后关系 owner（story：持续 "
        "attachment 交实例化后关系 owner，前链最多负责宿主相关机会——"
        "post-instantiation 边界）；Bake 无空间主张（寄生行为 story）——"
        "0 程序 story。"))
    out = BATCH_DIR / "stories.jsonl"
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False)
                             for r in recs) + "\n", encoding="utf-8")
    n_sweep = sum(1 for r in recs if "sweep_log_mapping" in r)
    print(f"stories: {len(recs)} with-sweep-map: {n_sweep} "
          f"zero-program: {sum(1 for r in recs if r['consequence']=='NO_SURFACE_EFFECT')}")


if __name__ == "__main__":
    main()
