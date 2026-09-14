# -*- coding: utf-8 -*-
"""HRQ-V10-MUTATION-001 — registry v9 -> v10 终局重跑统一落册 mutation.

Kind: HRQ_ADJUDICATION_EXECUTION（非普查批——无新盲程序/无新判同；零新增裁决）。
Authorization: RB-1/2/3 三批 ARTIFACT_APPROVE（批档+审校卡在案）+ hrq_decision_log.md
全部裁决；scope = LT_ENDGAME_CHECKLIST.md 第 3 步。

纪律（HRQ-MUTATION-001 判例① 沿用）：
  - 幂等守卫：registry 已是 v10 -> exit 1 拒绝重放
  - 每处锚点替换前 count 断言（唯一性）
  - 写盘前 yaml.safe_load 全文解析 + 结构/计数断言（先验证后写盘）
  - 成员清单从三批 merge_tests.jsonl 派生（工件为准，非手打）+ 集合级对账断言
"""
import json
import os
import sys
from collections import Counter

import yaml

ROOT = r"A:\Projs\FCF-Harness-Handoff\programaticHitFish"
CEN = os.path.join(ROOT, "fish_logic_census")
REG = os.path.join(CEN, "template_registry.yaml")


def load_mt(batch):
    path = os.path.join(CEN, "batches", batch, "merge_tests.jsonl")
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


RB1 = load_mt("CENSUS-REBUILD-001")
RB2 = load_mt("CENSUS-REBUILD-002")
RB3 = load_mt("CENSUS-REBUILD-003")


def ids_for(tests, suffix, sids):
    """Derive program_ids for the given species-order list; assert the family
    membership set in merge_tests matches exactly (artifact-truth check)."""
    fam = sorted(t["species_id"] for t in tests if (t["target_family"] or "").endswith(suffix))
    assert sorted(sids) == fam, (suffix, set(sids) ^ set(fam))
    m = {t["species_id"]: t["program_id"] for t in tests}
    return [m[s] for s in sids]


def pids(tests, sids):
    """Plain sublist mapping (no family-set assertion — for partial lists whose
    full-family composition is asserted separately via assert_family)."""
    m = {t["species_id"]: t["program_id"] for t in tests}
    return [m[s] for s in sids]


def assert_family(tests, suffix, sids):
    fam = sorted(t["species_id"] for t in tests if (t["target_family"] or "").endswith(suffix))
    assert sorted(sids) == fam, (suffix, set(sids) ^ set(fam))


def arr(ids):
    return "[" + ", ".join(ids) + "]"


# ---------------------------------------------------------------------------
# Member lists (species order = batch V-map order; sets asserted vs merge_tests)
# ---------------------------------------------------------------------------
SF28 = ["RKB", "ARG", "ASP", "BLP", "BPB", "BSB", "CCR", "CMR", "CSL", "DTN", "FDR",
        "GAJ", "GG", "GSF", "HAD", "HAL", "KGO", "LKR", "LKT", "RFP", "ROB", "SPC",
        "SPK", "SSL", "TAI", "TMU", "TSK", "WIN"]
FF10 = ["POR", "SAI", "SDG", "SAF", "YFT", "STM", "ALB", "SPM", "BIA", "PBF"]
TB2 = ["WIT", "YTF"]
TU2 = ["JGC", "JDP"]
SL2 = ["GW", "GT"]
FS1 = ["BAS"]

RB1_TS16 = ["CBM", "BST", "STL", "SVT", "PRC", "HYC", "MHS", "RHM", "RBP", "HBW",
            "AKB", "APA", "GOT", "GIT", "HLL", "RVC"]
RB1_GC_STD = ["GPF", "SMF", "LMD"]
RB1_GC_FORAGE = ["INC", "WST"]
RB1_GA_NEST = ["HNC", "CRC"]
RB1_GA_EGG = ["MDC", "LMP", "AMK"]
RB1_NO4 = ["GDE", "MOO", "CLC", "RTC"]
RB1_ZS2 = ["RRH", "GRH"]
RB1_ZD1 = ["SMB"]

RB2_TS_STRAINS = ["SUK", "GRK", "KHK", "OGK", "LCP", "AMC", "ASC", "HFC"]
RB2_TS_OTHERS = ["AMN", "BLT", "BMB", "DBC", "DCL", "GDB", "LFB", "PCC", "PKC"]
RB2_TS_CONFIRMED = ["COD", "PIK19", "ARC", "VEN", "SWO", "TAR", "PAD34", "BST", "CBM"]
RB2_TS_MIGRATED = ["BHC", "HER"]
RB2_GC_NEW = ["AGC", "WAG", "HYS", "WS2", "ATC", "AWF", "RSS"]
RB2_GC_CONFIRMED = ["FGA", "SGA", "AST", "GRB", "SMA", "GPF"]
RB2_NO_NEW = ["WCC", "ACA", "BBH", "BCF", "WHC", "STS", "TGS"]
RB2_NO_CONFIRMED = ["WEL", "FLA", "BUR", "GDE", "MOO"]
RB2_LA_MIGRATED = ["CHN", "COH", "BRO", "ALE"]
RB2_LA_CONFIRMED = ["CHU", "SHA"]
RB2_ZS_CONFIRMED = ["GRH", "RRH", "DRU"]
RB2_ZS_MIGRATED = ["SNS"]
RB2_ST_CONFIRMED = ["BSK"]
RB2_ZD_CONFIRMED = ["SMB"]
RB2_GA_CONFIRMED = ["BLU", "ARA", "RBP", "HNC"]
RB2_FF_NEW = ["ASB", "BHM", "BTS", "EUP", "GDS", "JSB", "PKS", "PLC", "PRB", "PSH",
              "RSC", "RUF", "SSM"]
RB2_FF_MIGRATED = ["BRT12", "PB", "SDG"]
RB2_SF_NEW = ["CGD", "RBD"]
RB2_SF_MIGRATED = ["SSL", "FDR", "BSB", "TSK"]
RB2_TB_MIGRATED = ["WIT", "YTF"]
RB2_FS_NEW = ["SLM"]

RB3_TS_AXIS29 = ["BRT3", "BRT4", "AEL2", "BIB2", "GAR3", "YEP2", "MUL2", "RAI3", "SOK2",
                 "SAL1", "PAD5", "SEA2", "COD2", "GRA2", "TIL3", "BSH1", "BRC", "CHS",
                 "CLC", "LJB", "TNS", "STL", "IDE", "KOI", "MIR", "WRC", "RTL", "GCR", "WCR2"]
RB3_TS_FIELD19 = ["BIB1", "SOK1", "PAD1", "TIL2", "MAC1", "JCK1", "CAP1", "SIL1", "MDC2",
                  "XCD", "ROH", "MRC", "SPR", "CHM", "SHB", "GTB", "WCB", "WBL", "BON1"]
RB3_TS_OTHER2 = ["RHM2", "TIL3-RESP"]
RB3_NO8 = ["WAL2", "AEL1", "CCF1", "WCF1", "SZE1", "ASC2", "BBR1", "MRG"]
RB3_GC7 = ["PIK1", "BWF", "BSN", "YCF", "CPT", "MUS", "FGA4"]
RB3_GA7 = ["CRA2", "SMA1", "BLU2", "CCF2", "DIS2", "CSN1", "RSB"]
RB3_GA_FORMHOLD2 = ["CSL-RESP", "CSN1-RESP"]
RB3_LA1 = ["RED2"]
RB3_ZS1 = ["BDR2"]
RB3_ST1 = ["CAR1"]
RB3_FF8 = ["RED1", "RAI2", "COD1", "BET", "STB", "MAH", "BKC", "RST1"]
RB3_SF27 = ["CRA1", "YEP1", "MUL1", "TEN1", "LWF1", "SBS1", "SBH1", "HMB", "IRS", "LNK",
            "MRF", "SPS", "STM", "TPC", "YCK", "SB2", "WCR3", "CTT", "RSB2", "RTB",
            "DVK", "GJC", "SS2", "BIC", "SIH", "YTA", "BBF"]

# RS1 in-registry program ids for migrated members (registry-side moves)
RS1 = {"WIT": "P-RS1-WIT-BAKE", "YTF": "P-RS1-YTF-BAKE", "SSL": "P-RS1-SSL-BAKE",
       "FDR": "P-RS1-FDR-BAKE", "BSB": "P-RS1-BSB-BAKE", "TSK": "P-RS1-TSK-BAKE",
       "SNS": "P-RS1-SNS-BAKE", "CHN": "P-RS1-CHN-BAKE", "COH": "P-RS1-COH-BAKE",
       "BRO": "P-RS1-BRO-BAKE", "ALE": "P-RS1-ALE-BAKE", "BRT12": "P-RS1-BRT12-BAKE",
       "PB": "P-RS1-PB-BAKE", "SDG": "P-RS1-SDG-BAKE", "BHC": "P-RS1-BHC-BAKE",
       "HER": "P-RS1-HER-BAKE"}

# ---------------------------------------------------------------------------
# Load registry + idempotency guard
# ---------------------------------------------------------------------------
text = open(REG, encoding="utf-8").read()
if "\nversion: 10\n" in text or text.startswith("version: 10"):
    print("GUARD: registry already at v10 - refusing replay")
    sys.exit(1)
assert "\nversion: 9\n" in text, "expected registry v9"


def rep(old, new, n=1):
    global text
    c = text.count(old)
    assert c == n, "anchor count %d != %d for: %r" % (c, n, old[:80])
    text = text.replace(old, new)


# ---------------------------------------------------------------------------
# Edit 1: header — version + v10 mutation_provenance + retitle v9 block
# ---------------------------------------------------------------------------
V10_HEADER = """version: 10
mutation_provenance:
  batch: HRQ-V10-MUTATION-001
  kind: HRQ_ADJUDICATION_EXECUTION（registry mutation 批——非普查批：无新盲程序/无新判同；三批终局重跑裁决统一落册，LT 线收官 mutation）
  date: 2026-09-14
  previous_version: 9
  authorization: "RB-1/2/3 三批全部 ARTIFACT_APPROVE（批档+审校卡在案）+hrq_decision_log.md 全部裁决（七项裁决+两组语义裁定+HRQ-REBUILD-SCOPE-01 终局重跑授权）；零新增裁决——scope=LT_ENDGAME_CHECKLIST.md 第 3 步"
  authorization_chain:
    rb1: "CENSUS-REBUILD-001 产出 9e58bb6+修复轮 5bf0694；verdict 卡 d0db89b=ARTIFACT_APPROVE（2026-09-14）"
    rb2: "CENSUS-REBUILD-002 产出 e1adf08+修复轮 ecc2510/ac75b77/32e4b78+closure 96cf145；verdict 卡 2c3bc94=三轮 APPROVE 闭环"
    rb3: "CENSUS-REBUILD-003 产出 8a5bf47+清理 6a47078+卫生 0fdee44；首轮 ARTIFACT_APPROVE（checklist 8196719 在案；F1 追溯 freeze_marker 本批补建）"
  previous_state: "v9：21 条目=18 CANDIDATE+RETIRED/FALSIFIED/VACATED 各 1；9 链族 order_provisional；GUARD 28 名义（四形式 24+brooded 2+form_hold 2）；truth_rebuild_queue 303 行（经 RB-1 91/RB-2 94/RB-3 118 全消费=303/303——批档在案）"
  rebuild_completion: "终局重跑消费台账：RB-1 91 项（82 真形+6 双轨合并+3 held）/RB-2 94 项（76 derived+18 reused）/RB-3 118 项（116 derived+2 reused）；非族处置 3=AMB 2（TGT/PEL 真形挂重验——FR/表达线补证通道）+NOS 1（GAR1=B 文件 BOUNDARY-DECL 直证显式无程序）；held 3（ASR/RVS/RDS）维持 evidence_insufficient_held"
  scope_items:
    item1_new_families_11: "11 新族入册（RB-1 六族：SPACE_FIRST 61 名义=28+6+27/FORAGE_FIRST 34=10+16+8/GATE_SUBSTRATE_TEMPBAND 4=RB-1 2+RS1 迁入 2/GUARD_ANCHOR_TURBIDITY 2/STRUCTURE_LIGHTSLOT 2/HABITAT_FORAGE_FLOODSLOT 2；RB-3 五形：STRUCTURE_FIRST_QUAD/LAYER_TEMP_STRUCTURE_TRIPLE/GATED_STRUCTURE_TEMP_TIME_QUAD/GATED_TEMP_STRUCTURE_TIME_QUAD 各 1+BROODED_DEGENERATE_TWO_STEP 1）——全部渐进累积语义 canonical+推导证据引用+provenance 指向 RB 批"
    item2_family_moves_23: "族移动 23 条记录（RB-1 7+RB-2 16——其中 7 条双轨确认）落为 16 个 known_instances 成员条目迁移：TS->LA x4（CHN/COH/BRO/ALE）/TS->FF x3（BRT12/PB/SDG）/TS->SF x1（TSK）/GC->ZS x1（SNS）/GC->SF x3（SSL/FDR/BSB）/GC->TB x2（WIT/YTF）/FILTER_FIELD->TS x2（BHC/HER）——逐条 moved_from 注记"
    item3_filter_field_vacated: "FILTER_FIELD_ACCUMULATE_CHAIN->VACATED（BHC/HER 迁 TIERED_SINGLE factor_type=field 轴值——HRQ-RB2-03 裁决维持轴域读法 vs 立 BAKE_FIELD 新族；PATCH VACATED 先例同型）"
    item4_order_provisional_resolution: "order_provisional 解析：8 链族改 order_confirmed（RB-1 7 族 35 MC+RB-2 31 尾在册成员复核证据链——HRQ-RB1-06/HRQ-RB2-01）；FILTER_FIELD 随空置关闭；HARD_GATED/EXTREME_TEMP/PATCH_GATED_DUAL 三族无 RB 证据链（成员不在重跑队列——RP1 重跑体为 canonical 源）如实保留 provisional+终态注记（envelope『12 族 order_confirmed』对该三族无证据支撑——独立审确认点）"
    item5_terminal_adjudications: "TIL3 分面记账（雌口哺=brooded 退化边界成员/雄领地=TS 轴段独立——原挂起注记改双面）；ARO 退化链维持（BROODED 族 canonical 源+Response 面 GUARD 历史层注记）；CSL/CSN1 anchor->fry_school（fry_school 3->5+ARA 规则重落 net 6）；跨阶段 anchor 取值规则统一（HRQ-RB2-07 终裁：以主形式/直证为准——JDP 维持/ARA nest->fry_school/CSL 直证/SMA1 实例集记法）；KOI 品系闭合注记（RB-2 品系开放项经 RB-3 KOI 本体同形闭合——HRQ-RB3-01）"
    item6_incidental: "RB-2 批内生成器常量 7 处旧口径同步（RBP/JSB 身份措辞——防重跑再生，产物层 REV-001/R1 已修）；RB-3 追溯性 freeze_marker 补建（retrospective 标注+现盲文件 sha256）；C9 原候选形撤案注记（ORDERED_QUAD_TIER_COMBINE_CHAIN——HRQ-RS1-05/HRQ-RB3-03 终裁：4/4 分散四形状）"
  nominal_member_reconciliation: "新族 110 名义（61+34+4+2+2+2+1+1+1+1+1）=RB NEW 总数（RB-1 45+RB-2 25+RB-3 40）逐批可复算；既有族 RB 落册 181（TS 94=RS1 存留 9+迁入 2+RB-1 16+RB-2 17+RB-3 50 / GC 27 / NO 24 / LA 7 / ZS 7 / ST 3 / ZD 2 / GA 18）+MGC 1（RP1 期非 RB）=182；RB 三批 294 真形体=MC 181+NEW 110+AMB 2+NOS 1——闭合"
  active_family_calibers: "三口径：18 在册（v9 CANDIDATE 活族）/23 Bake 终态（13-1+11——envelope『过审』口径=Bake 终态数）/28 活族终态（23 Bake+Response 5）"
  envelope_discrepancies: "①STRUCTURE_LIGHTSLOT 名义：envelope/checklist 记 4，工件实数 2（RB-1 GT/GW——RB-2/3 merge_tests 零新增）——按工件入册 2；envelope 口径疑将 GT/GW 的 B3 原体（slot_tiering 前历史层 P-B3-GT/GW-BAKE）计入——独立审确认点（B7-F2 工件为准判例）。②『12 族 order_confirmed』：工件证据链仅覆盖 8 链族——按 item4 处置（3 族如实保留 provisional）"
  closed_hrqs: "RB1-01..06/RB2-01..07/RB3-01..05 全部 resolved（对账表=batches/HRQ-V10-MUTATION-001/batch_report.md §3）"
  review_gate: "本批 status=INDEPENDENT_REVIEW_REQUIRED——mutation 不自我批准；独立审通过前不推远端"
v9_mutation_history:"""

rep("version: 9\nmutation_provenance:\n  batch: REBUILD-SCOPE-001",
    V10_HEADER + "\n  batch: REBUILD-SCOPE-001")

# ---------------------------------------------------------------------------
# Edit 2: chain-family order lines -> order_confirmed (9 occurrences)
# ---------------------------------------------------------------------------
CHAIN_ORDER_OLD = ("    order_provisional: true   # 裁决 2-B：因子判断顺序=族判据；本基础序为模板约定"
                   "（B 系列表达文件序），成员真实序待终局逐鱼顺序推导（解析载体=重跑批范围声明："
                   "HRQ-MUTATION-001 batch_report §5-③；truth_rebuild_queue 已含链族在册成员——"
                   "HRQ-REBUILD-SCOPE-001 于 2026-09-14 裁定入队[REBUILD-SCOPE-001 微 mutation]）"
                   "——真实序差异=族移动")
CHAIN_ORDER_NEW = ("    order_confirmed: true   # v10（HRQ-RB1-06+HRQ-RB2-01 终裁轨）：Tier A 逐鱼推导"
                   "真形序=canonical 序——RB-1 7 族 35 MC+RB-2 31 尾在册成员复核（证据=两批 "
                   "merge_tests/engine_report order_confirm 字段）；裁决 2-B 解析闭环")
rep(CHAIN_ORDER_OLD, CHAIN_ORDER_NEW, 9)

# ---------------------------------------------------------------------------
# Edit 3: FILTER_FIELD order line -> resolution by vacation
# ---------------------------------------------------------------------------
rep("    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.FILTER_FIELD_ACCUMULATE_CHAIN\n" + CHAIN_ORDER_NEW,
    "    ir_pointer: batches/CENSUS-RERUN-SINGLE-001/run_merge_tests.py::NEW_FAMILY_SOURCE.FILTER_FIELD_ACCUMULATE_CHAIN\n"
    "    order_resolution: \"v10 随族 VACATED 关闭——成员 BHC/HER 经 HRQ-RB2-01 迁出->TIERED_SINGLE（factor_type=field 轴值读法）；三步展开经 Tier A 重跑证伪无 story 级顺序证据，本族基础序问题失载体\"")

# ---------------------------------------------------------------------------
# Edit 4-6: HARD_GATED / EXTREME_TEMP / PATCH_GATED_DUAL order final notes
# ---------------------------------------------------------------------------
rep("    order_provisional: true   # 裁决 2-B：因子判断顺序=族判据；因子集 unordered 为 v2 提案证据态（RP1 重跑证据未裁决序）——终局逐鱼推导后若序有据则分化",
    "    order_provisional: true   # 裁决 2-B：因子判断顺序=族判据；因子集 unordered 为 v2 提案证据态（RP1 重跑证据未裁决序）——终局逐鱼推导后若序有据则分化\n"
    "    order_final_note: \"v10 终态：终局重跑（RB-1/2/3，303/303 全消费）已完结——本族成员不在 truth_rebuild_queue（RP1 重跑体=canonical 源），序证据态维持 unordered 提案（无逐鱼推导覆盖）；envelope『12 族 order_confirmed』对本族无 RB 证据链支撑——如实保留 provisional（独立审确认点）\"")
rep("    order_provisional: true   # 因子集 unordered=证据态；终局逐鱼推导后若序有据则分化（裁决 2-B）",
    "    order_provisional: true   # 因子集 unordered=证据态；终局逐鱼推导后若序有据则分化（裁决 2-B）\n"
    "    order_final_note: \"v10 终态：本族成员不在 truth_rebuild_queue（RP1 重跑体=canonical 源）——序证据态维持 unordered 提案（无逐鱼推导覆盖）；envelope『12 族 order_confirmed』对本族无 RB 证据链支撑——如实保留 provisional（独立审确认点）\"")
rep("    order_provisional: true   # 双槽序=RP1 重跑证据态；终局逐鱼推导复核（裁决 2-B）",
    "    order_provisional: true   # 双槽序=RP1 重跑证据态；终局逐鱼推导复核（裁决 2-B）\n"
    "    order_final_note: \"v10 终态：本族成员不在 truth_rebuild_queue（RP1 重跑体=canonical 源）——序证据态维持 RP1 重跑证据态（无逐鱼推导覆盖）；envelope『12 族 order_confirmed』对本族无 RB 证据链支撑——如实保留 provisional（独立审确认点）\"")

# ---------------------------------------------------------------------------
# Edit 7: TIERED_SINGLE known_instances rework
# ---------------------------------------------------------------------------
TS_NEW = """    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-COD-BAKE, role: canonical_source, note: "premise 轴段亚群（10）之一：sex/stage 深度带；RB-2 真形复验 order_confirm（终局真形体 P-RB2-COD-BAKE）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-PIK19-BAKE, P-RS1-ARC-BAKE, P-RS1-VEN-BAKE, P-RS1-SWO-BAKE, P-RS1-TAR-BAKE], note: "v10 存留 5（RB-2 真形复验 order_confirm——单步链无序判据适用）；原 9 数组中 CHN/COH/BRO/ALE 四条已迁出->LAYER_AXIS（v10 族移动——HRQ-RB2-01）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-BST-BAKE, P-RS1-CBM-BAKE], note: "机会亚群存留 2（RB-2 order_confirm；B4 AMB 轨另有同种真形 P-RB1-BST/CBM-BAKE 双体并册见下）；BRT12/PB 已迁出->FORAGE_FIRST（v10）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-PAD34-BAKE, note: "感官亚群存留 1（RB-2 order_confirm）；SDG/TSK 已迁出->FORAGE_FIRST/SPACE_FIRST（v10）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-BHC-BAKE, P-RS1-HER-BAKE], moved_from: FILTER_FIELD_ACCUMULATE_CHAIN, note: "v10 族移动迁入（HRQ-RB2-01）：单步场浓度评估——factor_type=field 轴值读法（B2 判例复活：EVAL_TYPED_FIELD_OR_FACTOR 单步+场轴；B 层三步展开无 story 级顺序证据——HRQ-RB2-03 裁决维持轴域读法）；终局真形体=P-RB2-BHC/HER-BAKE（REV-RB2-001 return_type 契约修正随迁注记）；FILTER_FIELD 移空->VACATED"}
      # —— v10 终局重跑落册（RB-1/2/3 MC 真形体——判同细节权威=各批 merge_tests.jsonl）——
      - {batch: CENSUS-REBUILD-001, program_id: __RB1_TS16__, note: "16 单步真形（B4/B5 AMB 轨+slot_tiering 轨——单步链无序判据适用；RBP=摄食面单因子与护卵面 GA 成员同种双面独立记账）"}
      - {batch: CENSUS-REBUILD-002, program_id: __RB2_STRAINS__, note: "8 鲤品系（Identity Deferred S1-S11 全 SN——分辨率=同种 CSV 单因子；KOI 本体重跑同形[RB-3]->品系闭合注记见 v10_notes.strain_track_closure）"}
      - {batch: CENSUS-REBUILD-002, program_id: __RB2_TS_OTHERS__, note: "9 单步真形（B6 AMB 第 3 层；LFB P04 贝宿主=guard 面 premise 注记另轨）"}
      - {batch: CENSUS-REBUILD-003, program_id: __RB3_TS_AXIS29__, note: "29 轴段/低分辨率单步（B7 第 4 层——P05 premise 轴段配置级为主；TIL3/TIL3-RESP=雄鱼领地轴段[HRQ-RB3-04 分面记账——雌口哺面另记 BROODED 族 boundary_note]）"}
      - {batch: CENSUS-REBUILD-003, program_id: __RB3_TS_FIELD19__, note: "19 field 场浓度单步（factor_type=field 轴值读法——RB-2 BHC/HER 判例第 2 批量应用；Response 面 FOOD_FIELD 投影另轨面分离记账[HRQ-RB3-05 注记]）"}
      - {batch: CENSUS-REBUILD-003, program_id: [P-RB3-RHM2-BAKE, P-RB3-TIL3-RESP-RESP], note: "2 复用/特例（RHM2=reused_from RB-1 RHM 双 story 内容近似；TIL3-RESP=雄领地面终裁体——queue 笔误 TRB-0301 前缀 P-B0 记档）"}
    v10_notes:
      strain_track_closure: "KOI/MIR/WRC（鲤品系）+RTL（Oreochromis 杂交）=TS 同形（RB-3）——RB-2 品系『亲本 R03 轨补证后可升档』开放项闭合（KOI 本体重跑同形，品系无需升档，0 冲突——HRQ-RB3-01）"
      field_axis_reading: "factor_type 轴域含 field（场浓度 evaluand——HRQ-RB2-03 维持轴域读法）：BHC/HER+RB-3 19 尾=Bake 面场分布权重；Response 面 FOOD_FIELD 投影=面分离记账不重复"
      nominal_reconciliation: "94 名义=RS1 存留 9+FILTER_FIELD 迁入 2+RB-1 16+RB-2 17+RB-3 50"
    known_non_matches:"""

TS_OLD = """    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-COD-BAKE, role: canonical_source, note: "premise 轴段亚群（10）之一：sex/stage 深度带"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-PIK19-BAKE, P-RS1-ARC-BAKE, P-RS1-VEN-BAKE, P-RS1-SWO-BAKE, P-RS1-CHN-BAKE, P-RS1-COH-BAKE, P-RS1-BRO-BAKE, P-RS1-ALE-BAKE, P-RS1-TAR-BAKE], note: "premise 轴段亚群其余 9（繁殖轴段/季节轴/季节水层/DVM 相位/洄游轴段×4/发育轴段）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-BRT12-BAKE, P-RS1-PB-BAKE, P-RS1-BST-BAKE, P-RS1-CBM-BAKE], note: "机会亚群（4）：食物丰度先行"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-PAD34-BAKE, P-RS1-SDG-BAKE, P-RS1-TSK-BAKE], note: "感官亚群（3）：信号场可探测性先行"}
    known_non_matches:"""

TS_NEW = (TS_NEW
          .replace("__RB1_TS16__", arr(ids_for(RB1, "TIERED_SINGLE_FACTOR_CHAIN", RB1_TS16)))
          .replace("__RB2_STRAINS__", arr(pids(RB2, RB2_TS_STRAINS)))
          .replace("__RB2_TS_OTHERS__", arr(pids(RB2, RB2_TS_OTHERS)))
          .replace("__RB3_TS_AXIS29__", arr(pids(RB3, RB3_TS_AXIS29)))
          .replace("__RB3_TS_FIELD19__", arr(pids(RB3, RB3_TS_FIELD19))))
# cross-check: full-family composition per batch
assert_family(RB2, "TIERED_SINGLE_FACTOR_CHAIN", RB2_TS_STRAINS + RB2_TS_OTHERS + RB2_TS_CONFIRMED + RB2_TS_MIGRATED)
assert_family(RB3, "TIERED_SINGLE_FACTOR_CHAIN", RB3_TS_AXIS29 + RB3_TS_FIELD19 + RB3_TS_OTHER2)
rep(TS_OLD, TS_NEW)

# ---------------------------------------------------------------------------
# Edit 8: LAYER_AXIS known_instances rework
# ---------------------------------------------------------------------------
LA_OLD = """    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-CHU-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-SHA-BAKE}"""
LA_NEW = """    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-CHU-BAKE, role: canonical_source, note: "RB-2 真形复验 order_confirm（终局真形体 P-RB2-CHU-BAKE；CSV benthopelagic 锚=RS1 入步依据被独立推导确认）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-SHA-BAKE, note: "RB-2 order_confirm（终局真形体 P-RB2-SHA-BAKE；pelagic-neritic+鳃耙构型）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-CHN-BAKE, P-RS1-COH-BAKE, P-RS1-BRO-BAKE, P-RS1-ALE-BAKE], moved_from: TIERED_SINGLE_FACTOR_CHAIN, note: "v10 族移动迁入（HRQ-RB2-01）：垂直层与水平洄游廊道独立维度（CSV benthopelagic/pelagic-neritic 锚入步；B 层样板语义还原不采）——真形两步[软定位->廊道轴段]；终局真形体=P-RB2-*-BAKE"}
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-RED2-BAKE, note: "潮位水深层->幼成廊道轴两步（story 直证两独立维——RB-2 csv_anchor_standard 同型；与 RED1 同种双 story 去重联动）"}"""
assert_family(RB2, "LAYER_AXIS_DUAL_TIER_CHAIN", RB2_LA_MIGRATED + RB2_LA_CONFIRMED)
assert_family(RB3, "LAYER_AXIS_DUAL_TIER_CHAIN", RB3_LA1)
rep(LA_OLD, LA_NEW)

# ---------------------------------------------------------------------------
# Edit 9: GATED_COVER known_instances rework + RB adds
# ---------------------------------------------------------------------------
GC_OLD = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-FGA-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-SGA-BAKE, P-RS1-AST-BAKE, P-RS1-SNS-BAKE, P-RS1-GPF-BAKE, P-RS1-SSL-BAKE, P-RS1-WIT-BAKE, P-RS1-YTF-BAKE, P-RS1-FDR-BAKE, P-RS1-BSB-BAKE], note: "伏击门 9 例（engine raw=gate_axis 字面，语义 MC——GUARD anchor 判例同型）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-GRB-BAKE, P-RS1-SMA-BAKE], note: "patch/扰动门 2 例（vs PATCH 族 ORDER 真差异——门先行 vs 评估先行；merge_tests 边界证据）"}"""
GC_NEW = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-FGA-BAKE, role: canonical_source, note: "RB-2 真形复验 order_confirm（终局真形体 P-RB2-FGA-BAKE；RB-3 FGA4 双 story 复用第 3 证）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-SGA-BAKE, P-RS1-AST-BAKE, P-RS1-GPF-BAKE], note: "伏击门存留 3（RB-2 order_confirm；AST=gate->forage 参数读法——HRQ-RB2-04 Tier A 优先确认）；原 9 数组中 SNS/SSL/WIT/YTF/FDR/BSB 六条已迁出->ZONE_SUBSTRATE x1/SPACE_FIRST x3/GATE_SUBSTRATE_TEMPBAND x2（v10 族移动——HRQ-RB1-01+HRQ-RB2-01 双轨一致）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-GRB-BAKE, P-RS1-SMA-BAKE], note: "patch/扰动门 2 例（RB-2 order_confirm）；vs PATCH 族 ORDER 真差异——门先行 vs 评估先行"}"""
assert_family(RB2, "GATED_COVER_TIER_CHAIN", RB2_GC_NEW + RB2_GC_CONFIRMED)
assert_family(RB1, "GATED_COVER_TIER_CHAIN", RB1_GC_STD + RB1_GC_FORAGE + ["ARO"])
assert_family(RB3, "GATED_COVER_TIER_CHAIN", RB3_GC7)
rep(GC_OLD, GC_NEW)

MGC_ANCHOR = "原体 P-MGC-BAKE-ADULT 见 PATCH 族历史层\"}"
GC_ADD = MGC_ANCHOR + """
      # —— v10 终局重跑落册（RB-1/2/3 MC 真形体）——
      - {batch: CENSUS-REBUILD-001, program_id: __GC_STD__, note: "标准掩体档 3（GPF=RS1 轨双体并册——B4 AMB 轨 P-RB1-GPF 与 RS1 在册 P-RS1-GPF 两 queue 项独立记账）"}
      - {batch: CENSUS-REBUILD-001, program_id: __GC_FORAGE__, note: "gate->forage 单档 2（HRQ-RB1-03 MC 确认：canonical 第二步 factor_type typed 参数读法涵盖 forage 场——轴域扩展注记）"}
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-ARO-BAKE, note: "gate_axis=surface_zone 既有轴新值登记（HRQ-RB1-03：水面猎物档——参数级=B4 判例非新轴）；同种 Response 面口哺退化链另记 BROODED 族（双面独立记账——HRQ-RB3-04）"}
      - {batch: CENSUS-REBUILD-002, program_id: __RB2_GC__, note: "7（B6 AMB 第 3 层：品系 AGC/WAG 伏击/HYS+ATC+RSS 底层探食 gate->forage 同型读法/WS2 同种品系/awf 岩底硬壳——雄护卵停食=guard premise 注记另轨）"}
      - {batch: CENSUS-REBUILD-003, program_id: __RB3_GC__, note: "7（B7 第 4 层伏击门；FGA4=reused_from RB-2 FGA 双 story；PIK1 与 PIK19 同种双 story 两读法互指=B 文件判语原样）"}"""
GC_ADD = (GC_ADD
          .replace("__GC_STD__", arr(pids(RB1, RB1_GC_STD)))
          .replace("__GC_FORAGE__", arr(pids(RB1, RB1_GC_FORAGE)))
          .replace("__RB2_GC__", arr(pids(RB2, RB2_GC_NEW)))
          .replace("__RB3_GC__", arr(pids(RB3, RB3_GC7))))
rep(MGC_ANCHOR, GC_ADD)

# ---------------------------------------------------------------------------
# Edit 10: NOCTURNAL known_instances rework + adds
# ---------------------------------------------------------------------------
NO_OLD = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-WEL-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-FLA-BAKE, P-RS1-BUR-BAKE, P-RS1-GDE-BAKE, P-RS1-MOO-BAKE], note: "engine 零差异（含 PREMISE raw）"}"""
ids_for(RB2, "NOCTURNAL_LIGHTSLOT_CHAIN", RB2_NO_NEW + RB2_NO_CONFIRMED)
ids_for(RB1, "NOCTURNAL_LIGHTSLOT_CHAIN", RB1_NO4)
ids_for(RB3, "NOCTURNAL_LIGHTSLOT_CHAIN", RB3_NO8)
NO_NEW = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-WEL-BAKE, role: canonical_source, note: "RB-2 真形复验 order_confirm（终局真形体 P-RB2-WEL-BAKE；story 原文级夜行）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-FLA-BAKE, P-RS1-BUR-BAKE, P-RS1-GDE-BAKE, P-RS1-MOO-BAKE], note: "engine 零差异（含 PREMISE raw）；RB-2 order_confirm（终局真形体 P-RB2-*-BAKE）"}
      # —— v10 终局重跑落册（RB-1/2/3 MC 真形体）——
      - {batch: CENSUS-REBUILD-001, program_id: __RB1_NO__, note: "4（GDE/MOO=RS1 轨双体并册——B4 AMB 轨与 RS1 在册两 queue 项；夜行轴证据分层：GDE=story 原文/余=CSV 锚）"}
      - {batch: CENSUS-REBUILD-002, program_id: __RB2_NO__, note: "7（B6 鲿形目夜行底栖为主——BBH/BCF story 原文级/WHC CSV 锚分层注记）"}
      - {batch: CENSUS-REBUILD-003, program_id: __RB3_NO__, note: "8（B7 第 4 层；MRG=B 文件边界条款兑现——夜行主导正文证实换 NO 形[独立审复核点]；CLC B5/R03 双 story 分层见 HRQ-RB3-01——B5 轨在 NO/R03 轨在 TS，证据分层非冲突）"}"""
assert_family(RB2, "NOCTURNAL_LIGHTSLOT_CHAIN", RB2_NO_NEW + RB2_NO_CONFIRMED)
assert_family(RB1, "NOCTURNAL_LIGHTSLOT_CHAIN", RB1_NO4)
assert_family(RB3, "NOCTURNAL_LIGHTSLOT_CHAIN", RB3_NO8)
NO_NEW = (NO_NEW
          .replace("__RB1_NO__", arr(pids(RB1, RB1_NO4)))
          .replace("__RB2_NO__", arr(pids(RB2, RB2_NO_NEW)))
          .replace("__RB3_NO__", arr(pids(RB3, RB3_NO8))))
rep(NO_OLD, NO_NEW)

# ---------------------------------------------------------------------------
# Edit 11: ZONE_SUBSTRATE known_instances rework + adds
# ---------------------------------------------------------------------------
ZS_OLD = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-GRH-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-RRH-BAKE, P-RS1-DRU-BAKE], note: "engine 零差异（同属同构+翻底可翻性轴值）"}"""
ids_for(RB2, "ZONE_SUBSTRATE_RESOURCE_CHAIN", RB2_ZS_CONFIRMED + RB2_ZS_MIGRATED)
ids_for(RB1, "ZONE_SUBSTRATE_RESOURCE_CHAIN", RB1_ZS2)
ids_for(RB3, "ZONE_SUBSTRATE_RESOURCE_CHAIN", RB3_ZS1)
ZS_NEW = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-GRH-BAKE, role: canonical_source, note: "RB-1/RB-2 真形复验 order_confirm（canonical 源真形复验——B4 AMB 轨 P-RB1-GRH 同形双体并册见下）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-RRH-BAKE, P-RS1-DRU-BAKE], note: "engine 零差异（同属同构+翻底可翻性轴值）；RB-2 order_confirm（终局真形体 P-RB2-*-BAKE）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-SNS-BAKE, moved_from: GATED_COVER_TIER_CHAIN, note: "v10 族移动迁入（HRQ-RB2-01）：『over soft substrates』原文级底质独立步=三步链（vs GC 两步=步数差异——B 层两步分歧记档 HRQ-RB2-04）；夜行=condition premise；终局真形体=P-RB2-SNS-BAKE"}
      # —— v10 终局重跑落册 ——
      - {batch: CENSUS-REBUILD-001, program_id: __RB1_ZS__, note: "2（B4 AMB 轨真形——canonical 源 GRH 真形复验+RRH 同属）"}
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-BDR2-BAKE, note: "1（翻底物理依赖推导与 B 文件独立同序确认——DRU 同型）"}"""
assert_family(RB2, "ZONE_SUBSTRATE_RESOURCE_CHAIN", RB2_ZS_CONFIRMED + RB2_ZS_MIGRATED)
assert_family(RB1, "ZONE_SUBSTRATE_RESOURCE_CHAIN", RB1_ZS2)
assert_family(RB3, "ZONE_SUBSTRATE_RESOURCE_CHAIN", RB3_ZS1)
ZS_NEW = ZS_NEW.replace("__RB1_ZS__", arr(pids(RB1, RB1_ZS2)))
rep(ZS_OLD, ZS_NEW)

# ---------------------------------------------------------------------------
# Edit 12: SOFT_TRIPLE adds CAR1
# ---------------------------------------------------------------------------
rep("""      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BSK-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-ONS-BAKE,""",
    """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BSK-BAKE, role: canonical_source, note: "RB-2 真形复验 order_confirm（终局真形体 P-RB2-BSK-BAKE）"}
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-CAR1-BAKE, note: "v10 落册第 3 成员：近底软层->底质可拱性->底栖猎物斑块三步无门（benthopelagic 软定位首步无门——与 B 文件同序独立确认；翻拱痕迹=世界侧可见性事实不改鱼程序）"}
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-ONS-BAKE,""")
ids_for(RB3, "SOFT_TRIPLE_TIER_CHAIN", RB3_ST1)

# ---------------------------------------------------------------------------
# Edit 13: ZONE_DEPTH adds RB-1 SMB body
# ---------------------------------------------------------------------------
rep("""    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-SMB-BAKE, role: canonical_source}""",
    """    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-SMB-BAKE, role: canonical_source, note: "RB-2 真形复验 order_confirm（终局真形体 P-RB2-SMB-BAKE）"}
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-SMB-BAKE, note: "v10 落册（B4 AMB 轨真形——canonical 源同种双体并册：CSV 深>=4m 锚复验）"}""")
ids_for(RB1, "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN", RB1_ZD1)
ids_for(RB2, "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN", RB2_ZD_CONFIRMED)

# ---------------------------------------------------------------------------
# Edit 14: GUARD_ANCHOR (Bake) known_instances rework + adds + axis note
# ---------------------------------------------------------------------------
GA_OLD = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BLU-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-ARA-BAKE, P-RS1-RBP-BAKE, P-RS1-HNC-BAKE], note: "engine 零差异（4 锚型）；v9 四形式对齐：colony_nest[BLU]->nest / floodplain_fry_school[ARA]->fry_school / root_spawn_eggs[RBP]->egg_mass / pebble_mound[HNC]->nest（pebble_mound 口径经裁决 4 关闭；HNC 与 HRQ-B4-01 Response 面提案同源）"}"""
ids_for(RB2, "GUARD_ANCHOR_TIERED_COMBINE_CHAIN", RB2_GA_CONFIRMED)
ids_for(RB1, "GUARD_ANCHOR_TIERED_COMBINE_CHAIN", RB1_GA_NEST + RB1_GA_EGG)
ids_for(RB3, "GUARD_ANCHOR_TIERED_COMBINE_CHAIN", RB3_GA7 + RB3_GA_FORMHOLD2)
GA_NEW = """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BLU-BAKE, role: canonical_source, note: "RB-2 真形复验 order_confirm（Tier A C06 建立期选址->照护期占位=步序证据；终局真形体 P-RB2-BLU-BAKE）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-ARA-BAKE, P-RS1-RBP-BAKE, P-RS1-HNC-BAKE], note: "engine 零差异（4 锚型）；RB-2 order_confirm（终局真形体 P-RB2-*-BAKE）；四形式：colony_nest[BLU]->nest / floodplain_fry_school[ARA]->fry_school（v10 跨阶段规则重落维持——HRQ-RB2-07 主形式/直证）/ root_spawn_eggs[RBP]->egg_mass / pebble_mound[HNC]->nest（口径经裁决 4 关闭）"}
      # —— v10 终局重跑落册（B5 EXT 轨 anchor 值兑现+第 4 层+form_hold 终裁）——
      - {batch: CENSUS-REBUILD-001, program_id: __GA_NEST__, note: "anchor=nest x2（HNC=RS1 轨双体并册——B4 AMB 轨与 RS1 在册两 queue 项；CRC=雄砾巢脊连续建造[挖坑->覆石->紧邻下游再挖成脊]）——B5 EXT 轨 anchor 值提案由真形 MC 兑现（HRQ-RB1-04）"}
      - {batch: CENSUS-REBUILD-001, program_id: __GA_EGG__, note: "anchor=egg_mass x3（MDC 洞顶/LMP 岩面卵块/AMK 岩缝扇护——利用型附着；fan=guard_action_notes）——B5 EXT 轨值兑现同上"}
      - {batch: CENSUS-REBUILD-003, program_id: __RB3_GA7__, note: "7（B7 第 4 层）：anchor=CRA2 nest（本种筑巢证据实证）/SMA1 nest<->fry_school 两阶段实例切换（B 文件 §11.2——HRQ-RB2-07 规则实例集记法）/BLU2 nest（canonical 源同种同面直验——B01-S38 与 B 文件 §2.2 双源一致）/CCF2 egg_mass（洞巢利用型）/DIS2 fry_school（色型不分裂——S12 本批独立推导同向）/CSN1 fry_school（HRQ-RB3-05 终裁）/RSB host_brood（B7 EXT 轨 mussel_brood 提案落位确认——四形式既有值）"}
      - {batch: CENSUS-REBUILD-003, program_id: __RB3_FH2__, note: "form_hold 终裁 2（HRQ-RB3-05）：anchor=fry_school（CSL=『Males guard the eggs and pelagic larvae』larvae 直证/CSN1=snakehead.md §0 直证）；egg/浮巢初始阶段 open 保留（不虚构 nest/egg_mass）"}"""
GA_NEW = (GA_NEW
          .replace("__GA_NEST__", arr(pids(RB1, RB1_GA_NEST)))
          .replace("__GA_EGG__", arr(pids(RB1, RB1_GA_EGG)))
          .replace("__RB3_GA7__", arr(pids(RB3, RB3_GA7)))
          .replace("__RB3_FH2__", arr(pids(RB3, RB3_GA_FORMHOLD2))))
rep(GA_OLD, GA_NEW)

rep("与 Response 面 GUARD anchor 轴同源对齐[18-vs-19 口径经裁决 4 关闭])",
    "与 Response 面 GUARD anchor 轴同源对齐[18-vs-19 口径经裁决 4 关闭]；跨阶段取值规则=主形式/直证为准[HRQ-RB2-07 终裁——与 Response 面同规])")

# ---------------------------------------------------------------------------
# Edit 15: FILTER_FIELD -> VACATED
# ---------------------------------------------------------------------------
rep("""  - template_id: FILTER_FIELD_ACCUMULATE_CHAIN
    surface: Bake
    status: CANDIDATE""",
    """  - template_id: FILTER_FIELD_ACCUMULATE_CHAIN
    surface: Bake
    status: VACATED""")
rep("""      origin: SINGLE 族拆分（滤食场链形）；canonical=P-RS1-BHC-BAKE；与 Response 面 FOOD_FIELD_FEEDING_RESPONSE 不同 surface（Bake 分布 vs Response 摄入）""",
    """      origin: SINGLE 族拆分（滤食场链形）；canonical=P-RS1-BHC-BAKE；与 Response 面 FOOD_FIELD_FEEDING_RESPONSE 不同 surface（Bake 分布 vs Response 摄入）
    vacated_provenance:
      ruling: "HRQ-RB2-01（RB-2 批档；v10 envelope 授权执行）：FILTER_FIELD_ACCUMULATE_CHAIN 空置撤销——BHC/HER 终局真形=单步场浓度评估（B 层三步[水层/浓度/口径]展开无 story 级顺序证据），按 TIERED_SINGLE factor_type=field 轴值读法迁出（B2 判例复活——HRQ-RB2-03 裁决维持轴域读法 vs 立 BAKE_FIELD 新族）；移空 0 成员——PATCH VACATED 先例同型"
      disposition: "known_instances 2 条原体记录=历史层保留（不删）；成员资格由 P-RB2-BHC/HER-BAKE 于 TIERED_SINGLE 承载（moved_from 注记在彼侧）"
      status_note: VACATED（活族计数移出——v9 活族 18->v10 终态 28 的 -1 项；gauge/场浓度多步形若后续证据复活需新证据新裁决）""")
rep("""    known_instances:
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BHC-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-HER-BAKE, note: "engine 零差异；群游集聚并入槽值域（coverage #17）"}""",
    """    known_instances:
      # —— v10 历史层（族 VACATED——两成员经 HRQ-RB2-01 迁出->TIERED_SINGLE，成员资格由终局真形体承载）——
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BHC-BAKE, role: canonical_source, note: "v10 已迁出 TIERED_SINGLE_FACTOR_CHAIN（factor_type=field 轴值读法）——终局真形体 P-RB2-BHC-BAKE 承载成员资格；REV-RB2-001 return_type 契约修正（FieldFeeding->SpatialDistributionWeight）随迁注记"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-HER-BAKE, note: "v10 已迁出 TIERED_SINGLE（同 BHC 判据）；原注记：engine 零差异；群游集聚并入槽值域（coverage #17）"}""")

# ---------------------------------------------------------------------------
# Edit 16: GUARD (Response) — four_form_disposition + cross-stage rule + 7 member notes
# ---------------------------------------------------------------------------
rep("""      counts: "28 名义=既有 8（含 HNC 挂账转正）+挂账 20（B5 9+B6 2+B7 9）；四形式正式 24[nest 12/egg_mass 7/fry_school 3/host_brood 2]+brooded 挂起 2[ARO/TIL3——结构级退化链边界成员不计四形式轴值，待真形重跑终裁]+form-hold 挂起 2[CSL/CSN1——冻结证据无巢/构建判别词（HRQ-MUTATION-REV-001 F1），待真形重跑终裁]\"""",
    """      counts_v10: "26 名义（v10 终态）=四形式正式 26[nest 11/egg_mass 7/fry_school 6/host_brood 2]；v9 28->v10 26 变动：form_hold 2[CSL/CSN1]经 HRQ-RB3-05 终裁->fry_school（3->5）+ARA 经跨阶段规则重落 nest->fry_school（net nest 12->11/fry_school 3->6）；brooded 2[ARO/TIL3]经 HRQ-RB3-04 终裁退族->BROODED_DEGENERATE_TWO_STEP_CHAIN 边界轨道（ARO=canonical 源成员；TIL3=分面记账——雌口哺面边界注记无独立程序体/雄领地面=TS 轴段承载）——GUARD known_instances 2 条 brooded 记录转历史层注记不计名义"
      cross_stage_anchor_rule: "HRQ-RB2-07 终裁（v10 envelope 授权）：跨阶段成员 anchor 取值以主形式/直证为准（非初始形式）——JDP[直证=裁决 4 落位表洪水护卵群->fry_school 维持]/ARA[主形式=洪水季稚鱼群伴游+B 文件 GuardAnchorResolverInstance=fry_school 直证——初始沙底巢=相邻阶段 open]/CSL[直证=pelagic larvae]/SMA1[B 文件 §11.2 直证=两阶段实例集{nest_bed,fry_school}无单值主形式——按实例集记法计 nest 初始实例+fry_school 后阶段注记]；MUT 批『按初始形式落位』注记（ARA/SMA1）经本规则取代\"""")

rep("""      - {batch: CENSUS-B3, program_id: P-B3-ARA-RESP, blind_hash: 5f3f40e142fffa81, anchor: nest, participant: male, note: "第 5 成员（巨骨舌鱼洪水护巢）：细名 sand_nest（沙巢）->nest（构建型底质巢）；换气暴露 runtime premise（TAR-11）保留；engine raw 仅槽名/合并步标名字面差异"}""",
    """      - {batch: CENSUS-B3, program_id: P-B3-ARA-RESP, blind_hash: 5f3f40e142fffa81, anchor: fry_school, participant: male, note: "第 5 成员（巨骨舌鱼洪水护巢）：v10 跨阶段规则重落（HRQ-RB2-07 终裁——主形式/直证为准）：主形式=洪水季稚鱼群伴游+B 文件 GuardAnchorResolverInstance=fry_school 直证（洪泛漫滩移动锚）——原 v9『按初始形式落 nest（沙巢）』读法经规则取代；初始沙底巢=相邻阶段 open 注记；换气暴露 runtime premise（TAR-11）保留；engine raw 仅槽名/合并步标名字面差异"}""")

rep("""洪水位相=DynamicSpatialSlot 注记（guard_action_notes）"}""",
    """洪水位相=DynamicSpatialSlot 注记（guard_action_notes）；v10 跨阶段规则重落确认（HRQ-RB2-07：直证=裁决 4 落位表——维持 fry_school）"}""")

rep("""      - {batch: CENSUS-B5, program_id: P-B5-CSL-RESP, blind_hash: 0b9376d0e1ae6a8e, anchor: form_hold, membership: pending_truth_rebuild, note: "细名 nest_pelagic_larvae（雄护卵+浮游幼体跨两发育阶段）——冻结 premise/story 无巢/构建判别词，四形式证据不足不虚构（HRQ-MUTATION-REV-001 F1）：anchor 形式挂起，待真形重跑以 B 系列证据终裁；浮游幼体期 fry_school 语义注记保留"}""",
    """      - {batch: CENSUS-B5, program_id: P-B5-CSL-RESP, blind_hash: 0b9376d0e1ae6a8e, anchor: fry_school, note: "细名 nest_pelagic_larvae（雄护卵+浮游幼体跨两发育阶段）——v10 终裁（HRQ-RB3-05）：anchor=fry_school（story『Males guard the eggs and pelagic larvae』——pelagic larvae=浮游幼体直证）；egg 阶段无巢/附着判别词不定形（不虚构 nest/egg_mass）——egg 阶段形式 open 留 HRQ；与 MUT 批『按初始形式落 nest』注记分歧以 story 直证为准；跨阶段规则一致（HRQ-RB2-07 主形式/直证）；Bake 面终局真形 P-RB3-CSL-RESP-RESP 同值"}""")

rep("""      - {batch: CENSUS-B7, program_id: P-B7-CSN1-RESP, blind_hash: 37b8128562ea4a77, anchor: form_hold, membership: pending_truth_rebuild, note: "细名 snakehead_brood_guard（繁殖期亲鱼守护卵幼+植被伏击捕食双语境）——冻结 premise/story 无浮巢/筑巢判别词，『浮巢构建型』系册外知识注入（HRQ-MUTATION-REV-001 F1）：anchor 形式挂起，待真形重跑以 B 系列证据终裁；护幼期 fry_school 语义注记保留；P01 伏击+P04 组合注记保留"}""",
    """      - {batch: CENSUS-B7, program_id: P-B7-CSN1-RESP, blind_hash: 37b8128562ea4a77, anchor: fry_school, note: "细名 snakehead_brood_guard（繁殖期亲鱼守护卵幼+植被伏击捕食双语境）——v10 终裁（HRQ-RB3-05）：anchor=fry_school（guarding/snakehead.md §0 直证『锚点：fry_school（浮巢孵化后的稚鱼群，植被区移动锚）』+story 护幼主体）；初始浮巢阶段=相邻阶段 open（不虚构 nest——原『浮巢构建型』系册外知识注入的判定维持）；P01 伏击+P04 组合注记保留；Bake 面终局真形 P-RB3-CSN1-RESP-RESP 同值"}""")

rep("""      - {batch: CENSUS-B7, program_id: P-B7-SMA1-RESP, blind_hash: 11115f7e48c569a8, anchor: nest, note: "细名 smallmouth_nest_fry_guard（巢与幼鱼守护+营养竞争语境）——按初始存在形式落 nest+跨阶段注记[稚鱼期 fry_school 语义；主形式待终局重跑——未点名成员，独立审复核点]；2009 饱食/2016 补食实验注记保留"}""",
    """      - {batch: CENSUS-B7, program_id: P-B7-SMA1-RESP, blind_hash: 11115f7e48c569a8, anchor: nest, note: "细名 smallmouth_nest_fry_guard（巢与幼鱼守护+营养竞争语境）——v10 跨阶段规则落地（HRQ-RB2-07）：B 文件 §0/§11.2 直证=两阶段实例集{nest_bed,fry_school}（Resolver 实例配置级切换不设 body 分支）无单值主形式——按实例集记法计 nest 初始实例+稚鱼期 fry_school 后阶段注记（原『主形式待终局重跑』经规则闭合）；2009 饱食/2016 补食实验注记保留"}""")

rep("""      - {batch: CENSUS-B5, program_id: P-B5-ARO-RESP, blind_hash: 42a78bf0eb4760ce, anchor: brooded, membership: pending_truth_rebuild, note: "银龙雄口哺携带卵/幼近 6 周——落位表『口孵->待重跑（退化链候选）』+裁决 4 brooded 边界（结构级退化链不入本族）：anchor 轴值挂起不计四形式，待真形重跑终裁；水面跳捕 P01 面另行"}""",
    """      - {batch: CENSUS-B5, program_id: P-B5-ARO-RESP, blind_hash: 42a78bf0eb4760ce, anchor: brooded, membership: exited_v10_brooded_degenerate, note: "银龙雄口哺携带卵/幼近 6 周——v10 终裁（HRQ-RB3-04）：退化链维持（brooded 结构级不入本族）——退族至 BROODED_DEGENERATE_TWO_STEP_CHAIN（Bake 面终局真形体 P-RB3-ARO-RESP-RESP=该族 canonical 源；本 Response 条目=历史层不计 GUARD 名义）；B5 全链盲形（PARALLEL 双 Path）=P04 契约模板套用降级；口哺期水面跳捕张力开放项随退化链族保留；水面跳捕 P01 面另行"}""")

rep("""      - {batch: CENSUS-B7, program_id: P-B7-TIL3-RESP, blind_hash: 3e1cf6343317da2c, anchor: brooded, membership: pending_truth_rebuild, note: "细名 tilapia_territory（雄鱼繁殖领地——雌鱼取卵离巢口孵，领地与幼体非同一关系对象）——裁决 4 brooded 边界点名『罗非退化链先例』：结构级退化链待真形重跑终裁，anchor 轴值挂起不计四形式；Semantic Open（领地 vs 护巢轴内一致性）随重跑重审"}""",
    """      - {batch: CENSUS-B7, program_id: P-B7-TIL3-RESP, blind_hash: 3e1cf6343317da2c, anchor: brooded, membership: exited_v10_split_face_bookkeeping, note: "细名 tilapia_territory——v10 终裁（HRQ-RB3-04）：分面记账读法修正（原挂起登记混淆两关系对象）：雌鱼口哺面=brooded 退化链边界成员（B 文件 nile_tilapia.md §0 Brooding 退化链直证——BROODED_DEGENERATE_TWO_STEP_CHAIN 族 boundary_note 记账，无独立程序体重跑体）；雄鱼领地面=非 brooded 程序（territory=关系对象非后代空间存在形式）——TS 轴段独立记账（终局真形体 P-RB3-TIL3-BAKE/P-RB3-TIL3-RESP-RESP）；本 Response 条目=历史层不计 GUARD 名义；Semantic Open（领地 vs 护巢轴内一致性）随分面读法闭合"}""")

# ---------------------------------------------------------------------------
# Edit 17: insert RB-1 six families before EXTREME_TEMP
# ---------------------------------------------------------------------------
SF27_IDS = pids(RB1, [s for s in SF28 if s != "RKB"])
FF9_IDS = pids(RB1, [s for s in FF10 if s != "POR"])
TB_IDS = ids_for(RB1, "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN__NEW", TB2)
TU_IDS = ids_for(RB1, "GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN__NEW", TU2)
SL_IDS = ids_for(RB1, "STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN__NEW", SL2)
FS_IDS = ids_for(RB1, "HABITAT_FORAGE_FLOODSLOT_CHAIN__NEW", FS1)
RB2_SF_NEW_IDS = ids_for(RB2, "SPACE_FIRST_DUAL_TIER_CHAIN__RB1", RB2_SF_NEW + RB2_SF_MIGRATED)
RB2_FF_NEW_IDS = ids_for(RB2, "FORAGE_FIRST_DUAL_TIER_CHAIN__RB1", RB2_FF_NEW + RB2_FF_MIGRATED)
RB2_TB_IDS = ids_for(RB2, "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN__RB1", RB2_TB_MIGRATED)
RB2_FS_IDS = ids_for(RB2, "HABITAT_FORAGE_FLOODSLOT_CHAIN__RB1", RB2_FS_NEW)
RB3_SF27_IDS = ids_for(RB3, "SPACE_FIRST_DUAL_TIER_CHAIN__RB1", RB3_SF27)
RB3_FF8_IDS = ids_for(RB3, "FORAGE_FIRST_DUAL_TIER_CHAIN__RB1", RB3_FF8)

SIX_FAMILIES = """
  - template_id: SPACE_FIRST_DUAL_TIER_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-001
      seeded: 2026-09-14
      review_queue: HRQ-RB1-02（+HRQ-RB2-02/HRQ-RB3-02 累积证据并案——v10 入册授权=三批 verdict 卡全 APPROVE）
      origin: 终局顺序还原重跑 RB-1 新族提案（28 尾）；canonical=源成员 P-RB1-RKB-BAKE 冻结真形体（HRQ-RB1-02 ask 指定建议首选）
      sha_chain: "RB-1 9e58bb6+5bf0694（verdict d0db89b）/RB-2 e1adf08..2c3bc94（+6）/RB-3 8a5bf47..8196719（+27）"
    canonical_program_body: |
      EVAL_TYPED_SPACE_FACTOR(空间适配先行——结构/复合栖息带三档分级命中，渐进累积语义[语义裁定 1]：
        preferred=全额乘入 running weight / tolerated=×衰减乘入 / excluded=×0.01 软出局乘入[非零、仍可参与下游]；
        族内 op 字面[EVAL_TYPED_STRUCTURE_FACTOR/EVAL_TYPED_HABITAT_FACTOR]归一为本判断位读法——HRQ-RB1-02 ask 确认项)
      -> EVAL_TYPED_FORAGE_FACTOR(猎物/资源场三档——同上乘入)
      -> [渐进累积：weight = weight × SpaceTierFit × ForageFit——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-001/blind_programs.jsonl::P-RB1-RKB-BAKE（canonical 源冻结体；判同记录=同批 merge_tests.jsonl）
    order_note: "canonical 序=Tier A 逐鱼推导真形序（栖息主句信息密度高=结构/复合带先行——RB-1 推导方向学）；61 尾跨三批复核同序——非模板约定序，无 order_provisional 需求"
    allowed_parameter_axes:
      - space_factor_axis(typed: 岩礁结构 | 植被带 | 复合栖息带 | 流速-底质复合带 | …；op 字面归一)
      - forage_factor_axis(typed: 猎物场 | 资源场 | 底栖资源 | …)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, forage 先行（FORAGE_FIRST 域——ORDER=族判据）, premise 轴段第二步（LAYER_AXIS 域——轴类别序列差异）, 硬门首步（GATED_* 域）, 第三步槽/修饰（SL/FS 域——步数）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-RKB-BAKE, role: canonical_source, note: "结构先行源成员（岩礁结构->硬壳猎物场——『Inhabits coastal rocky reefs』栖息主句先行；与 B 样板展示序相反=顺序判据分歧记录）"}
      - {batch: CENSUS-REBUILD-001, program_id: __SF27__, note: "RB-1 提案 28 尾其余 27（含 slot_tiering 轨关闭归属 TAI/BLP/RFP/DS[=CSL 双轨合并体]/HAL/GG/WIN；KGO=B5 guard 面承载撤销后面级重指派——HRQ-RB1-04；CSL/RHM/RBP=摄食面与护巢面同种双面独立记账）"}
      - {batch: CENSUS-REBUILD-002, program_id: __SF_RB2_NEW__, note: "B6 首证栖息复合先行 2（CGD 沙底急流复合句/RBD 砾石急滩复合句——跨批复证）"}
      - {batch: CENSUS-REBUILD-002, program_id: __SF_RB2_MIG__, moved_from: "GATED_COVER_TIER_CHAIN(SSL/FDR/BSB)+TIERED_SINGLE_FACTOR_CHAIN(TSK)", note: "v10 族移动迁入（HRQ-RB1-01 首提+HRQ-RB2-01 RS1 轨独立复核——双轨一致）：Tier A story 证伪伏击门/单步样板（SSL 潜沙=反捕食 overlay/FDR=Bottom Omnivore 无伏击/BSB 无二元排除原文/TSK 深冷主句先行）；终局真形体=P-RB2-*-BAKE"}
      - {batch: CENSUS-REBUILD-003, program_id: __SF_RB3__, note: "B7 第 4 层 27 尾（story 短主句+两维分辨率——链长 2 主导；累积 28->34->61）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-001, template_id: FORAGE_FIRST_DUAL_TIER_CHAIN, reason: "ORDER（序镜像——space->forage vs forage->space；裁决 2-B 严格判据不得合并）"}
      - {batch: CENSUS-REBUILD-001, template_id: LAYER_AXIS_DUAL_TIER_CHAIN, reason: "同签名 [E,E] 轴类别序列差异（第二步 premise 轴段[轴域限定] vs forage 因子）——语义层 non-match（RB-1 判例）"}
    nominal_count_note: "61 名义=RB-1 28+RB-2 6（新 2+迁入 4）+RB-3 27"
  - template_id: FORAGE_FIRST_DUAL_TIER_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-001
      seeded: 2026-09-14
      review_queue: HRQ-RB1-02（+HRQ-RB2-02/HRQ-RB3-02 累积并案）
      origin: RB-1 新族提案（10 尾——开放水跟随型）；canonical=源成员 P-RB1-POR-BAKE 冻结真形体（HRQ-RB1-02 ask 指定）
      sha_chain: "RB-1 9e58bb6+5bf0694/RB-2 e1adf08..2c3bc94（+16）/RB-3 8a5bf47..8196719（+8）"
    canonical_program_body: |
      EVAL_TYPED_FORAGE_FACTOR(猎物/资源场三档分级命中——渐进累积语义[语义裁定 1]：
        preferred=全额乘入 running weight / tolerated=×衰减乘入 / excluded=×0.01 软出局乘入[非零、仍可参与下游])
      -> EVAL_TYPED_SPACE_FACTOR(空间适配次之——开放水/栖息带三档——同上乘入)
      -> [渐进累积：weight = weight × ForageFit × SpaceTierFit——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-001/blind_programs.jsonl::P-RB1-POR-BAKE（canonical 源冻结体；判同记录=同批 merge_tests.jsonl）
    order_note: "canonical 序=Tier A 逐鱼推导真形序（食性主句先行=开放水跟随型——RB-1 推导方向学）；34 尾跨三批复核同序——非模板约定序，无 order_provisional 需求"
    allowed_parameter_axes:
      - forage_factor_axis(typed: 群游猎物场 | 季节脉冲 patch | 硬壳软体斑块 | 腐屑场 | …)
      - space_factor_axis(typed: 开放水温跃层-深水连续 | 陆架底层带 | 植被静水 | 急流带 | …)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, space 先行（SPACE_FIRST 域——ORDER=族判据）, 单因子（TIERED_SINGLE 域——步数）, 硬门首步（GATED_* 域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-POR-BAKE, role: canonical_source, note: "食性先行源成员（中上/底层群游鱼+鱿猎物场->开放水温跃层-深水连续——食性横跨水层；温血=热生理容忍扩展注记非独立步——裁决 4 电感知分层同域思路）"}
      - {batch: CENSUS-REBUILD-001, program_id: __FF9__, note: "RB-1 提案 10 尾其余 9（POR/SAI=B4 双轨合并体）"}
      - {batch: CENSUS-REBUILD-002, program_id: __FF_RB2_NEW__, note: "B6 13 尾（食性主句先行——ASB 幼成发育切换/JSB↔ASB 同属参照双 queue 项[REV-001 F2 勘误口径]等）"}
      - {batch: CENSUS-REBUILD-002, program_id: __FF_RB2_MIG__, moved_from: TIERED_SINGLE_FACTOR_CHAIN, note: "v10 族移动迁入（HRQ-RB1-01 SDG+HRQ-RB2-01 BRT12/PB——双轨确认）：真形两步[猎物/机会场->栖息带]；SDG=裁决 4 电感知分层后双因子；终局真形体=P-RB2-*-BAKE（SDG=RB-1 复用体承载）"}
      - {batch: CENSUS-REBUILD-003, program_id: __FF_RB3__, note: "B7 第 4 层 8 尾（累积 10->26->34）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-001, template_id: SPACE_FIRST_DUAL_TIER_CHAIN, reason: "ORDER（序镜像——forage->space vs space->forage）"}
      - {batch: CENSUS-REBUILD-001, template_id: TIERED_SINGLE_FACTOR_CHAIN, reason: "步数（两因子 vs 单因子）——SDG/BRT12/PB 单步归族经重跑证伪为族移动"}
    nominal_count_note: "34 名义=RB-1 10+RB-2 16（新 13+迁入 3）+RB-3 8"
  - template_id: GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-001
      seeded: 2026-09-14
      review_queue: HRQ-RB1-02（+HRQ-RB2-01 TB 移动双轨确认并案）
      origin: RB-1 新族提案（WIT/YTF——RS1 GATED_COVER 族移动目标族）；canonical=源成员 P-RB1-WIT-BAKE 冻结真形体
      sha_chain: "RB-1 9e58bb6+5bf0694/RB-2 e1adf08..2c3bc94（双轨确认 +0 新增）"
    canonical_program_body: |
      GATE_BURYABLE_SUBSTRATE(可埋底质硬定位门：不成立=EARLY_RETURN——门语义保留[二元门前出局非三档出局])
      -> EVAL_TYPED_HABITAT_FACTOR(深冷复合带三档——温度+深度复合描述不拆解；渐进累积语义乘入 running weight)
      -> EVAL_TYPED_FORAGE_FACTOR(底栖资源场三档——同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-001/blind_programs.jsonl::P-RB1-WIT-BAKE（canonical 源冻结体；判同记录=同批 merge_tests.jsonl）
    order_note: "canonical 序=Tier A 逐鱼推导真形序（鲽形目贴底埋伏体构=可埋底质先行+story 原文一句群复合带不虚构拆解）；RB-2 同鱼 RS1 轨独立复核同序"
    allowed_parameter_axes:
      - gate_axis(typed: 可埋软泥 | 沙泥——与 GATED_COVER gate_axis 同源值域的底质门值)
      - tempband_axis(typed: 深冷复合带 2-6°C/45-366m | 中深冷复合带——带边界=Profile 值域不冻结)
      - forage_factor_axis(typed: 底栖无脊椎场 | 多毛资源场 | …)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 无门复合带链（SF 域）, 水层门+底质/资源步（ZONE_SUBSTRATE 域——因子集 OPERATOR/ORDER 真差异）, 门+单档（GATED_COVER 域——步数）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-WIT-BAKE, role: canonical_source, note: "源成员（软泥可埋门->深冷泥底复合带 2-6°C/45-366m->甲壳/多毛/蛇尾底栖场——『soft mud bottoms in fairly deep water』原文复合描述）"}
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-YTF-BAKE, note: "同形（GATE 沙泥->中深冷复合带->多毛资源）"}
      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-WIT-BAKE, P-RS1-YTF-BAKE], moved_from: GATED_COVER_TIER_CHAIN, note: "v10 族移动迁入（HRQ-RB1-01 首提+HRQ-RB2-01 RS1 轨独立复核——双轨一致）：RS1 伏击门样板经 Tier A 重跑证伪——+深冷复合带步（OPERATOR/步数真差异）；终局真形体=P-RB2-WIT/YTF-BAKE"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-001, template_id: ZONE_SUBSTRATE_RESOURCE_CHAIN, reason: "因子集（底质门+深冷复合带步 vs 水层门+底质/资源步）——OPERATOR/ORDER 真差异"}
      - {batch: CENSUS-REBUILD-001, template_id: GATED_COVER_TIER_CHAIN, reason: "步数（三节点 vs 门+单档）——WIT/YTF 族移动判据"}
    nominal_count_note: "4 名义=RB-1 2+RS1 迁入 2（RB-2 双轨确认）"
  - template_id: GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-001
      seeded: 2026-09-14
      review_queue: HRQ-RB1-02（JGC 升级结构差异证据=HRQ-RB1-04 EXT 轨处置并案）
      origin: RB-1 新族提案（护巢链+浊度修饰第五步）；canonical=源成员 P-RB1-JGC-BAKE 冻结真形体
      sha_chain: "RB-1 9e58bb6+5bf0694（verdict d0db89b）"
    canonical_program_body: |
      GATE_ANCHOR_EXISTENCE(锚存在门：锚域外=EARLY_RETURN——门语义保留)
      -> EVAL_TYPED_ANCHOR_SUITABILITY(锚适配三档——渐进累积语义乘入 running weight)
      -> EVAL_TYPED_RELATION_FACTOR(守卫关系三档——同上乘入)
      -> EVAL_TYPED_LOCAL_TEMPERATURE(局部温度三档——同上乘入)
      -> EVAL_TYPED_TURBIDITY_CONTEXT(浊度语境修饰步三档——unary 轴修饰非路由；同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子]
      -> SpatialDistributionWeight（护巢面 Bake 分布权重——与 GUARD_ANCHOR 族同域返回）
    ir_pointer: batches/CENSUS-REBUILD-001/blind_programs.jsonl::P-RB1-JGC-BAKE（canonical 源冻结体；判同记录=同批 merge_tests.jsonl）
    order_note: "canonical 序=Tier A 逐鱼推导真形序（B §0 unary 轴声明与 story 原文一致——浊度步 story 原文承载）"
    allowed_parameter_axes:
      - anchor_type(typed: nest | fry_school——四形式[裁决 4-A]；JGC=nest[双亲巢]/JDP=fry_school[洪水护卵群+DynamicSlot]）
      - turbidity_context_axis(typed: 浊水语境 unary 修饰——与结构掩体轴不同域)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 四步无浊度修饰（GUARD_ANCHOR 域——步数结构差异）, 关系轴缺失（BROODED 退化域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-JGC-BAKE, role: canonical_source, anchor: nest, participant: biparental, note: "源成员（B5 EXT 轨 JGC 升级为结构差异——+第五步浊度语境；『turbid waters and mud bottoms of the highly eutrophic lakes』story 原文承载）；Response 面 GUARD 族 P-B5-JGC-RESP 同种双面独立记账"}
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-JDP-BAKE, anchor: fry_school, participant: male, note: "同形（护巢四步+浊水修饰——两尾真形一致）；洪水位相=DynamicSpatialSlot 注记（guard_action_notes 同 Response 面）；Response 面 P-B5-JDP-RESP 双面独立记账"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-001, template_id: GUARD_ANCHOR_TIERED_COMBINE_CHAIN, reason: "第五步浊度修饰（步数结构差异——B5 EXT 轨升级判据 HRQ-RB1-04）"}
    nominal_count_note: "2 名义=RB-1 2（JGC/JDP）"
  - template_id: STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-001
      seeded: 2026-09-14
      review_queue: HRQ-RB1-02（slot_tiering 轨 GT/GW 关闭归属并案——裁决 6-③ 终态）
      origin: RB-1 新族提案（结构->夜槽->猎物三节点）；canonical=源成员 P-RB1-GW-BAKE 冻结真形体
      sha_chain: "RB-1 9e58bb6+5bf0694（verdict d0db89b）"
    canonical_program_body: |
      EVAL_TYPED_STRUCTURE_FACTOR(结构三档——渐进累积语义乘入 running weight)
      -> APPLY_DYNAMIC_SPATIAL_SLOT(低光/夜相槽 modifier——槽位=链中位：槽值乘入；槽内无出局语义[族域边界同 NOCTURNAL 判例])
      -> EVAL_TYPED_FORAGE_FACTOR(猎物场三档——同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-001/blind_programs.jsonl::P-RB1-GW-BAKE（canonical 源冻结体；判同记录=同批 merge_tests.jsonl）
    order_note: "canonical 序=Tier A 逐鱼推导真形序（『counter current zones...at dusk and at night』story 标题级复合主句=空间结构+时间窗复合）"
    allowed_parameter_axes:
      - structure_axis(typed: 逆流区位 | 礁外结构 | …)
      - lowlight_slot(低光/夜相槽——槽位中位非作者可选；与 NOCTURNAL 槽同语义不同位)
      - forage_factor_axis(typed: 鱼+落水无脊椎场 | 甲壳鱼猎物场 | …)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 两节点夜行链（NOCTURNAL 域——步数+首步语义）, 槽位链尾（HABITAT_FORAGE_FLOODSLOT 域——ORDER）, 无槽两步（FF/SF 域——步数）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-GW-BAKE, role: canonical_source, note: "源成员（逆流区位结构->黄昏夜相槽->鱼+落水陆生无脊椎猎物场）"}
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-GT-BAKE, note: "同形（礁外结构->夜槽->甲壳鱼猎物）；GT/GW=slot_tiering 轨关闭归属（C8 轨 14/14 关闭——HRQ 裁决 6-③+RB-1 §5）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-001, template_id: NOCTURNAL_LIGHTSLOT_CHAIN, reason: "步数+首步语义（三节点[结构->槽->forage] vs 两节点[夜行底板->槽]）——OPERATOR 真差异"}
      - {batch: CENSUS-REBUILD-001, template_id: HABITAT_FORAGE_FLOODSLOT_CHAIN, reason: "ORDER（槽位中位 vs 链尾）+槽语义（夜相 vs 洪泛连通）"}
    nominal_count_note: "2 名义=RB-1 2（GT/GW）——envelope/checklist 记 4 与工件不符（RB-2/3 merge_tests 零新增）：按工件入册 2；envelope 口径疑将 GT/GW 的 B3 原体（slot_tiering 前历史层 P-B3-GT/GW-BAKE）计入——独立审确认点（工件为准——B7-F2 判例）"
  - template_id: HABITAT_FORAGE_FLOODSLOT_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-001
      seeded: 2026-09-14
      review_queue: HRQ-RB1-02（+HRQ-RB2-02 SLM 第 2 实证升格并案）
      origin: RB-1 新族提案（BAS 单成员 PROVISIONAL）；canonical=源成员 P-RB1-BAS-BAKE 冻结真形体
      sha_chain: "RB-1 9e58bb6+5bf0694/RB-2 e1adf08..2c3bc94（+1 升格）"
    canonical_program_body: |
      EVAL_TYPED_HABITAT_FACTOR(栖息带三档——大河急流+缓段复合带；渐进累积语义乘入 running weight)
      -> EVAL_TYPED_FORAGE_FACTOR(植食/资源场三档——同上乘入)
      -> APPLY_DYNAMIC_SPATIAL_SLOT(洪泛槽 modifier 链尾——裁决 4 拆解规则[洪水->DynamicSpatialSlot]：槽值乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-001/blind_programs.jsonl::P-RB1-BAS-BAKE（canonical 源冻结体；判同记录=同批 merge_tests.jsonl）
    order_note: "canonical 序=Tier A 逐鱼推导真形序（栖息主句先行+洪泛事件槽链尾——裁决 4 拆解规则）"
    allowed_parameter_axes:
      - habitat_axis(typed: 大河急流+缓段复合带 | …)
      - forage_factor_axis(typed: 植食资源 | …)
      - floodplain_slot(洪泛连通槽——链尾位非作者可选）
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 槽位中位（STRUCTURE_LIGHTSLOT 域——ORDER）, 洪泛槽做路由条件（裁决 4 拆解规则——Group 面读位相 Bake 不重复结算）, 无槽两步（FF/SF 域——步数）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-001, program_id: P-RB1-BAS-BAKE, role: canonical_source, note: "源成员（RB-1 单成员 PROVISIONAL 提案——栖息主句先行+植食资源+洪泛林槽链尾）"}
      - {batch: CENSUS-REBUILD-002, program_id: P-RB2-SLM-BAKE, note: "第 2 实证（银斑鲫——『herbivore highly dependent on floodplains』原文级绑定；单成员 PROV 升双成员）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-001, template_id: STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN, reason: "ORDER（槽位链尾 vs 中位）+槽语义（洪泛 vs 夜相）"}
    nominal_count_note: "2 名义=RB-1 1+RB-2 1"
"""

SIX_FAMILIES = (SIX_FAMILIES
                .replace("__SF27__", arr(SF27_IDS))
                .replace("__SF_RB2_NEW__", arr(RB2_SF_NEW_IDS[:2]))
                .replace("__SF_RB2_MIG__", arr([RS1[s] for s in RB2_SF_MIGRATED]))
                .replace("__SF_RB3__", arr(RB3_SF27_IDS))
                .replace("__FF9__", arr(FF9_IDS))
                .replace("__FF_RB2_NEW__", arr(RB2_FF_NEW_IDS[:13]))
                .replace("__FF_RB2_MIG__", arr([RS1[s] for s in RB2_FF_MIGRATED]))
                .replace("__FF_RB3__", arr(RB3_FF8_IDS)))

INSERT_ANCHOR = """      - {batch: CENSUS-RERUN-SINGLE-001, template_id: PLAIN_FACTOR_COMBINE, reason: "RETURN（Guarding vs 分布）+COMBINE（UNDEFINED 多评估合并 vs WEIGHTED 终合并）+前置锚门——真差异"}

  - template_id: EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN"""
rep(INSERT_ANCHOR,
    """      - {batch: CENSUS-RERUN-SINGLE-001, template_id: PLAIN_FACTOR_COMBINE, reason: "RETURN（Guarding vs 分布）+COMBINE（UNDEFINED 多评估合并 vs WEIGHTED 终合并）+前置锚门——真差异"}
""" + SIX_FAMILIES + """
  - template_id: EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN""")

# ---------------------------------------------------------------------------
# Edit 18: append RB-3 five shapes at EOF
# ---------------------------------------------------------------------------
RB3_FAMILIES = """
  - template_id: STRUCTURE_FIRST_QUAD_TIER_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-003
      seeded: 2026-09-14
      review_queue: HRQ-RB3-03（C9 立族终裁——4 新形状之一；v10 入册授权=RB-3 首轮 ARTIFACT_APPROVE）
      origin: C9 候选族撤案后四形状之一（BLU 结构先行四步）；canonical=源成员 P-RB3-BLU-HAB-BAKE 冻结真形体（裁决 §6.2 锚『蓝鳃->结构先行』）
      c9_withdrawal_note: "原 C9 候选形 ORDERED_QUAD_TIER_COMBINE_CHAIN（水层->结构->水温->时段约定序）经 HRQ-RB3-03 终裁撤案——逐鱼推导 4/4 无一是该形（RS1 修复轮『4/4 同形』=BA-NORMAL-HABITAT-FIT 约定序伪影——语义裁定 3 落实；HRQ-RS1-05 关闭链）"
      sha_chain: "RB-3 8a5bf47+6a47078+0fdee44（checklist 8196719）"
    canonical_program_body: |
      EVAL_TYPED_HABITAT_FACTOR(结构-植被带三档[结构先行——裁决锚『蓝鳃->结构先行』]——渐进累积语义[语义裁定 1]乘入 running weight)
      -> EVAL_TYPED_HABITAT_FACTOR(软水层定位三档（benthopelagic 软定位档位归属轴）——同上乘入)
      -> EVAL_TYPED_HABITAT_FACTOR(宽温带三档（宽带弱分档后置——csv_band_strength_standard）——同上乘入)
      -> EVAL_TYPED_HABITAT_FACTOR(晨昏时段带三档——同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-003/blind_programs.jsonl::P-RB3-BLU-HAB-BAKE（canonical 源冻结体；判同记录=同批 merge_tests.jsonl）
    order_note: "canonical 序=Tier A 推导真形序（证据强度递减：结构[裁决锚]->水层[软定位]->水温[宽带]->时段[弱锚]）"
    allowed_parameter_axes:
      - band_axis_sequence(typed 四元组: 结构带 | 软水层 | 宽温带 | 时段带——同轴四步环境调制尾链)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 门化首步（GATED_STRUCTURE_TEMP_TIME 域——OPERATOR）, 温度中置三步（LAYER_TEMP_STRUCTURE_TRIPLE 域——链长+序）, 两步链（FF/SF/LA 域——步数）, guard 轴域（GA/TU 域——轴类别序列）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-BLU-HAB-BAKE, role: canonical_source, note: "蓝鳃栖息面（与护巢面 GA 成员 P-RS1-BLU/P-RB3-BLU2 同种双面独立记账——面级守恒）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-003, template_id: ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN, reason: "四步纯 EVAL 链无门 vs GATE 首步（OPERATOR）+轴类别序列（资源链 vs 环境调制链）"}
      - {batch: CENSUS-REBUILD-003, template_id: GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN, reason: "门化有无（GATE 首步——OPERATOR 真差异）"}
    provisional_note: 单成员 CANDIDATE（B7 栖息面一属一形——扩充证据待后续输入）
  - template_id: LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-003
      seeded: 2026-09-14
      review_queue: HRQ-RB3-03（C9 立族终裁——4 新形状之二）
      origin: C9 撤案后四形状之一（RBP 三步温度中置）；canonical=源成员 P-RB3-RBP-HAB-BAKE 冻结真形体
      sha_chain: "RB-3 8a5bf47+6a47078+0fdee44"
    canonical_program_body: |
      EVAL_TYPED_HABITAT_FACTOR(中上软水层三档（CSV pelagic 主体空间带）——渐进累积语义乘入 running weight)
      -> EVAL_TYPED_HABITAT_FACTOR(窄暖温带三档（23-27°C ±2 强分档中置——csv_band_strength_standard）——同上乘入)
      -> EVAL_TYPED_HABITAT_FACTOR(沉水结构三档（树根/植被掩体次级锚）——同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子；时段=CSV 全天活跃不入链（证据驱动不虚构）]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-003/blind_programs.jsonl::P-RB3-RBP-HAB-BAKE（canonical 源冻结体）
    order_note: "canonical 序=Tier A 推导真形序（CSV 证据分档强度排位——窄带中置/时段不入链）"
    allowed_parameter_axes:
      - band_axis_sequence(typed 三元组: 软水层 | 窄温带 | 沉水结构)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 底质/资源轴类别序列（SOFT_TRIPLE 域——语义 non-match）, 四步（STRUCTURE_FIRST_QUAD 域——链长）, 门化（GATED_* 域——OPERATOR）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-RBP-HAB-BAKE, role: canonical_source, note: "红腹食人鱼栖息面（与护巢面 GA 成员 P-RS1-RBP 同种双面独立记账；Frenzy 群游无证据不立群游轴——negative knowledge 原样）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-003, template_id: SOFT_TRIPLE_TIER_CHAIN, reason: "engine 同签名 [E,E,E]——轴类别序列不同（层-环境调制-空间 vs 层-底质-资源）=语义层 non-match（RB-2 判例第三批复证）"}
      - {batch: CENSUS-REBUILD-003, template_id: STRUCTURE_FIRST_QUAD_TIER_CHAIN, reason: "链长（三步 vs 四步）+序（温度中置 vs 结构先行）"}
    provisional_note: 单成员 CANDIDATE（B7 栖息面一属一形——扩充证据待后续输入）
  - template_id: GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-003
      seeded: 2026-09-14
      review_queue: HRQ-RB3-03（C9 立族终裁——4 新形状之三）
      origin: C9 撤案后四形状之一（HNC 门化四步结构先行）；canonical=源成员 P-RB3-HNC-HAB-BAKE 冻结真形体（裁决锚『美鱥口器->水层先行』+demersal GATE 化）
      sha_chain: "RB-3 8a5bf47+6a47078+0fdee44"
    canonical_program_body: |
      GATE_ZONE(底层砾石硬定位门——美鱥口器形态绑定底层取食/筑巢：非底层=EARLY_RETURN——门化=硬定位出局语义[RB-1 GRH/RRH 判例])
      -> EVAL_TYPED_HABITAT_FACTOR(砾石潭渊结构三档（筑巢基质/掩体）——渐进累积语义乘入 running weight)
      -> EVAL_TYPED_HABITAT_FACTOR(冷水温带三档——同上乘入)
      -> EVAL_TYPED_HABITAT_FACTOR(早晨时段带三档——同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-003/blind_programs.jsonl::P-RB3-HNC-HAB-BAKE（canonical 源冻结体）
    order_note: "canonical 序=Tier A 推导真形序（裁决锚『美鱥口器->水层先行』——口器特化绑定底层取食->结构->水温->时段）"
    allowed_parameter_axes:
      - gate_axis(typed: 底层砾石硬定位——demersal GATE 化值)
      - band_axis_sequence(typed 三元组: 砾石结构 | 冷水温带 | 早晨时段带)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 无门四步（STRUCTURE_FIRST_QUAD 域——OPERATOR）, 温度次置（GATED_TEMP_STRUCTURE_TIME 域——ORDER：第 2/3 步互换）, guard 轴域（GA/TU 域——轴类别序列）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-HNC-HAB-BAKE, role: canonical_source, note: "双点美鱥栖息面（与护巢面 GA 成员 P-RS1-HNC/P-RB1-HNC 同种多面独立记账——面级守恒）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-003, template_id: ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN, reason: "engine 同签名 [G,E,E,E]——轴类别序列不同（环境调制链 vs 资源链）=语义层 non-match（RB-2 判例）"}
      - {batch: CENSUS-REBUILD-003, template_id: GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN, reason: "ORDER（第 2/3 步互换——结构/水温序；§6.2 严格判据）"}
      - {batch: CENSUS-REBUILD-003, template_id: GUARD_ANCHOR_TIERED_COMBINE_CHAIN, reason: "engine 同签名 [G,E,E,E]——轴类别序列不同（guard 链 vs 环境调制链）=语义层 non-match"}
    provisional_note: 单成员 CANDIDATE（B7 栖息面一属一形——扩充证据待后续输入）
  - template_id: GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-003
      seeded: 2026-09-14
      review_queue: HRQ-RB3-03（C9 立族终裁——4 新形状之四）
      origin: C9 撤案后四形状之一（ARA 门化四步温度次置）；canonical=源成员 P-RB3-ARA-HAB-BAKE 冻结真形体
      sha_chain: "RB-3 8a5bf47+6a47078+0fdee44"
    canonical_program_body: |
      GATE_ZONE(底层硬定位门——CSV demersal：非底层=EARLY_RETURN——门语义保留)
      -> EVAL_TYPED_HABITAT_FACTOR(窄暖温带三档（25-29°C ±2 强分档前置——CSV 直证证据强度）——渐进累积语义乘入 running weight)
      -> EVAL_TYPED_HABITAT_FACTOR(洪泛林木质结构三档（方向级 [需正文] 锚按证据强度排后）——同上乘入)
      -> EVAL_TYPED_HABITAT_FACTOR(晨昏时段带三档——同上乘入)
      -> [渐进累积：weight 逐步乘入——无终步合并算子]
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-003/blind_programs.jsonl::P-RB3-ARA-HAB-BAKE（canonical 源冻结体）
    order_note: "canonical 序=Tier A 推导真形序（温序前置=CSV 窄带证据强度>结构 [需正文]——与 B 文件声明序差异为逐鱼推导产物；vs HNC 形第 2/3 步互换=ORDER 差异）"
    allowed_parameter_axes:
      - gate_axis(typed: 底层硬定位——demersal GATE 化值)
      - band_axis_sequence(typed 三元组: 窄暖温带 | 洪泛林结构 | 晨昏时段带)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 结构次置（GATED_STRUCTURE_TEMP_TIME 域——ORDER）, 无门（STRUCTURE_FIRST_QUAD 域——OPERATOR）, guard 轴域（GA/TU 域——轴类别序列）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-ARA-HAB-BAKE, role: canonical_source, note: "巨骨舌鱼栖息面（与护巢面 GA 成员 P-RS1-ARA 同种双面独立记账——面级守恒）"}
    known_non_matches:
      - {batch: CENSUS-REBUILD-003, template_id: GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN, reason: "ORDER（第 2/3 步互换——水温/结构序；§6.2 严格判据）"}
      - {batch: CENSUS-REBUILD-003, template_id: STRUCTURE_FIRST_QUAD_TIER_CHAIN, reason: "门化有无+序（GATE 首步 vs 纯 EVAL 结构先行）"}
    provisional_note: 单成员 CANDIDATE（B7 栖息面一属一形——扩充证据待后续输入）
  - template_id: BROODED_DEGENERATE_TWO_STEP_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-REBUILD-003
      seeded: 2026-09-14
      review_queue: HRQ-RB3-04（brooded 挂起终裁——退化链维持）
      origin: 裁决 4 brooded 结构级边界的形状承载族；canonical=源成员 P-RB3-ARO-RESP-RESP 冻结真形体（[G,E] 两步——无关系轴/无温度轴）
      sha_chain: "RB-3 8a5bf47+6a47078+0fdee44"
    canonical_program_body: |
      GATE_GUARD_ANCHOR_EXISTENCE(口哺锚存在门——携带型锚与个体绑定（锚在口中无锚址空间关系语义）：无锚=EARLY_RETURN——门语义保留)
      -> EVAL_ANCHOR_SITE_SUITABILITY(口哺期常驻区适配三档——渐进累积语义乘入 running weight)
      -> [退化链：无关系轴/无温度轴/无终步合并——裁决 4 brooded 边界的形状依据（vs GUARD_ANCHOR 四步=步数+轴结构差异=结构级）]
      -> BroodingSpatialDistributionWeight
    ir_pointer: batches/CENSUS-REBUILD-003/blind_programs.jsonl::P-RB3-ARO-RESP-RESP（canonical 源冻结体）
    order_note: "canonical 序=Tier A 推导真形序（B 层唯一口孵型判读先例 nile_tilapia §0 Brooding 退化链同构）"
    allowed_parameter_axes:
      - brood_anchor_binding(typed: 口哺携带型锚——与个体绑定非空间锚址)
      - home_range_quality_axis(typed: 口哺期常驻区适配)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 关系轴/温度轴（GUARD_ANCHOR 域——步数+轴结构=结构级）, PARALLEL 双 Path 全链读法（B5 契约模板套用——证据翻转条件见 provisional_note）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-REBUILD-003, program_id: P-RB3-ARO-RESP-RESP, role: canonical_source, note: "银龙雄口哺（『carries eggs, larvae and early juveniles in his mouth』=携带型同构；B5 全链盲形 PARALLEL 双 Path=P04 契约模板套用降级——Response 面 GUARD 历史层注记见该族）；口哺期水面跳跃捕食张力=开放项（证据翻转条件：口哺期全功能摄食+冲突并行证实则双 Path 读法复活——HRQ-RB3-04 保留）"}
    boundary_note: "TIL3 罗非雌鱼口哺面=退化链边界成员（B 文件 nile_tilapia.md §0 Brooding 退化链直证）——无独立程序体重跑体（其 queue 项 TRB-0301 终裁为雄鱼领地面 TS——分面记账 HRQ-RB3-04）；边界记账不入 nominal"
    known_non_matches:
      - {batch: CENSUS-REBUILD-003, template_id: GUARD_ANCHOR_TIERED_COMBINE_CHAIN, reason: "步数+轴结构（两步[门+常驻区适配] vs 四步[门+适配+关系+温度]）=结构级——裁决 4 brooded 边界的形状依据"}
    provisional_note: 单成员 CANDIDATE（退化链形状族——罗非退化链先例+银龙同构两证；开放项=口哺期摄食张力）
"""

EOF_ANCHOR = "    provisional_note: 单成员 PROVISIONAL + 退化条款（TAR-05 rank fact 未定则槽 2 退化常量→纯 patch 形族归属翻案——open_semantics 原样携带）\n"
assert text.endswith(EOF_ANCHOR), "unexpected EOF anchor"
text = text + RB3_FAMILIES

# ---------------------------------------------------------------------------
# Validate BEFORE writing (MUT-001 discipline: parse + assertions first)
# ---------------------------------------------------------------------------
doc = yaml.safe_load(text)
assert doc["version"] == 10, doc["version"]
tpl_list = doc["templates"]
assert len(tpl_list) == 32, len(tpl_list)
tpl = {t["template_id"]: t for t in tpl_list}
assert len(tpl) == 32, "duplicate template_id"


def nominal(tid):
    n = 0
    for inst in tpl[tid].get("known_instances") or []:
        p = inst.get("program_id")
        n += len(p) if isinstance(p, list) else 1
    return n


expect = {
    "SPACE_FIRST_DUAL_TIER_CHAIN": 61, "FORAGE_FIRST_DUAL_TIER_CHAIN": 34,
    "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN": 4, "GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN": 2,
    "STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN": 2, "HABITAT_FORAGE_FLOODSLOT_CHAIN": 2,
    "STRUCTURE_FIRST_QUAD_TIER_CHAIN": 1, "LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN": 1,
    "GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN": 1, "GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN": 1,
    "BROODED_DEGENERATE_TWO_STEP_CHAIN": 1,
    "TIERED_SINGLE_FACTOR_CHAIN": 94, "GATED_COVER_TIER_CHAIN": 27,
    "NOCTURNAL_LIGHTSLOT_CHAIN": 24, "LAYER_AXIS_DUAL_TIER_CHAIN": 7,
    "ZONE_SUBSTRATE_RESOURCE_CHAIN": 7, "SOFT_TRIPLE_TIER_CHAIN": 3,
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": 2, "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": 18,
}
actual = {}
for k, v in expect.items():
    a = nominal(k)
    actual[k] = a
    assert a == v, (k, a, v)

g = tpl["GUARD_CONFLICT_DUAL_PATH_RESPONSE"]
active = [i for i in g["known_instances"] if not str(i.get("membership", "")).startswith("exited_v10")]
exited = [i for i in g["known_instances"] if str(i.get("membership", "")).startswith("exited_v10")]
assert len(exited) == 2 and all(i.get("anchor") == "brooded" for i in exited), exited
anchors = Counter(i["anchor"] for i in active if i.get("anchor"))
assert anchors == Counter({"nest": 11, "egg_mass": 7, "fry_school": 6, "host_brood": 2}), anchors
assert len(active) == 26, len(active)

statuses = Counter(t["status"] for t in tpl_list)
assert statuses == Counter({"CANDIDATE": 28, "RETIRED": 1, "FALSIFIED": 1, "VACATED": 2}), statuses
assert tpl["FILTER_FIELD_ACCUMULATE_CHAIN"]["status"] == "VACATED"

n_oc = sum(1 for t in tpl_list if t.get("order_confirmed"))
n_op = sum(1 for t in tpl_list if t.get("order_provisional"))
assert n_oc == 8, n_oc
assert n_op == 3, n_op

bake_cand = [t for t in tpl_list if t["status"] == "CANDIDATE" and t["surface"] == "Bake"]
resp_cand = [t for t in tpl_list if t["status"] == "CANDIDATE" and t["surface"] == "Response"]
assert len(bake_cand) == 23, len(bake_cand)
assert len(resp_cand) == 5, len(resp_cand)

# moved_from accounting: 16 migrated member entries across families
moved = []
for t in tpl_list:
    for inst in t.get("known_instances") or []:
        if inst.get("moved_from"):
            p = inst.get("program_id")
            moved.extend(p if isinstance(p, list) else [p])
assert len(moved) == 16, moved

# ---------------------------------------------------------------------------
# Write (only after all validation passed)
# ---------------------------------------------------------------------------
with open(REG, "w", encoding="utf-8", newline="\n") as f:
    f.write(text)

print("v10 mutation applied: HRQ-V10-MUTATION-001")
print("  templates: 32 entries (28 CANDIDATE + RETIRED/FALSIFIED/VACATED x2)")
print("  active families: 28 = 23 Bake + 5 Response (v9 in-register 18)")
print("  new families nominal:", {k: actual[k] for k in list(expect)[:11]})
print("  existing families nominal:", {k: actual[k] for k in list(expect)[11:]})
print("  GUARD anchors:", dict(anchors), "= 26 nominal")
print("  order_confirmed families: 8; order_provisional kept: 3")
print("  migrated member entries:", len(moved))
