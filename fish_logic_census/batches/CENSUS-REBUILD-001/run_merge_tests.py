# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-001 merge-test engine + semantic verdicts.

Opens template_registry.yaml v9 (post-freeze) and compares each frozen truth
body against the 13 active Bake-family canonicals by structural signature
(step op-class sequence, gate presence/positions, branch kinds, slot nodes,
return type). Engine layer reports raw signature matches; the semantic layer
(worker adjudication, recorded in VERDICTS below) applies family-domain
reading per work standards 2.3/6.4:
  - same [E,E] signature across LAYER_AXIS (premise-axis 2nd step) vs
    SPACE_FIRST (spatial->resource) vs FORAGE_FIRST (resource->spatial) is
    resolved semantically (ORDER = family criterion).
Registry is read-only in this batch (zero mutation).
"""
import json, os, re, sys, datetime, hashlib
import yaml

ROOT = r"A:\Projs\FCF-Harness-Handoff\programaticHitFish"
CEN = os.path.join(ROOT, "fish_logic_census")
BATCH = "CENSUS-REBUILD-001"
OUT = os.path.join(CEN, "batches", BATCH)

# ---------------- canonical signatures from registry v9 (read-only) ----------------
CANON = {
    "CONSTRAINED_RELATIVE_REFUGE": dict(sig=["BUILD", "GATE", "RANK", "EVAL", "COMBINE"],
        note="AccessibleSet->HardViability->FeasibleSet->RelativeRank->SecondaryRefuge->FixedCombine"),
    "HARD_GATED_FACTOR_COMBINE": dict(sig=["BUILD", "GATE", "GATE", "EVAL", "EVAL", "EVAL", "EVAL"],
        note="v2: BUILD+双硬门+EXIT 档因子x4 unordered"),
    "TIERED_SINGLE_FACTOR_CHAIN": dict(sig=["EVAL"], note="单 typed 因子三档渐进"),
    "LAYER_AXIS_DUAL_TIER_CHAIN": dict(sig=["EVAL", "EVAL"],
        note="水层软三档->premise 绑定轴段三档（第二步=premise 轴段——轴域限定）"),
    "GATED_COVER_TIER_CHAIN": dict(sig=["GATE", "EVAL"], note="结构掩体存在门->掩体质量档（factor_type typed 参数）"),
    "NOCTURNAL_LIGHTSLOT_CHAIN": dict(sig=["EVAL", "SLOT"], note="夜行底板档->低光槽（adjuster，槽位判例固定）"),
    "ZONE_SUBSTRATE_RESOURCE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL"], note="GATE_ZONE 底层硬定位->底质档->资源档"),
    "SOFT_TRIPLE_TIER_CHAIN": dict(sig=["EVAL", "EVAL", "EVAL"], note="近底带软三档->底质档->资源档（无门）"),
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL"], note="GATE_ZONE->深度档->底质档->资源档"),
    "FILTER_FIELD_ACCUMULATE_CHAIN": dict(sig=["EVAL", "EVAL_FIELD", "EVAL_GAUGE"], note="滤食水层->场浓度->口径（特殊 op 语义）"),
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL"], note="锚存在门->锚适配->关系->局部温度（anchor 四形式轴）"),
    "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL", "EVAL"], note="极值水温门->EXIT 档因子x4 unordered"),
    "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN": dict(sig=["GATE", "EVAL", "SLOT"], note="patch 存在门->patch 强度档->rank position 槽"),
}

def op_class(step):
    op = step["op"]
    if op.startswith("GATE"):
        return "GATE"
    if op == "APPLY_DYNAMIC_SPATIAL_SLOT":
        return "SLOT"
    if "FOOD_FIELD" in op or "CONCENTRATION" in op:
        return "EVAL_FIELD"
    if "GAUGE" in op:
        return "EVAL_GAUGE"
    return "EVAL"

def body_signature(body):
    steps = body["surface_owned_logic"]["ordered_steps"]
    return [op_class(s) for s in steps]

# ---------------- worker semantic verdicts (adjudication layer) ----------------
# verdict map: sid -> (verdict, target_family, note)
V = {}
TS = "TIERED_SINGLE_FACTOR_CHAIN"; GC = "GATED_COVER_TIER_CHAIN"
GA = "GUARD_ANCHOR_TIERED_COMBINE_CHAIN"; NO = "NOCTURNAL_LIGHTSLOT_CHAIN"
ZS = "ZONE_SUBSTRATE_RESOURCE_CHAIN"; ST = "SOFT_TRIPLE_TIER_CHAIN"
ZD = "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN"
FF = "FORAGE_FIRST_DUAL_TIER_CHAIN__NEW"
SF = "SPACE_FIRST_DUAL_TIER_CHAIN__NEW"
TB = "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN__NEW"
TU = "GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN__NEW"
SL = "STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN__NEW"
FS = "HABITAT_FORAGE_FLOODSLOT_CHAIN__NEW"

for sid in ["CBM", "BST", "STL", "SVT", "PRC", "HYC", "MHS", "RHM", "RBP", "HBW",
            "AKB", "APA", "GOT", "GIT", "HLL", "RVC"]:
    V[sid] = ("MERGE_CONFIDENT", TS, "单步链无序判据适用问题——三档渐进语义 MC；轴值 typed 参数")
for sid in ["GPF", "SMF", "LMD"]:
    V[sid] = ("MERGE_CONFIDENT", GC, "GATE 结构/底质存在门->单档：与 canonical 同构；gate_axis 值=参数")
V["INC"] = ("MERGE_CONFIDENT", GC, "GATE_ZONE->forage 单档：结构同构（GATE->EVAL）；第二步 factor_type=typed 参数（piscivore 场）——canonical 掩体档轴域扩展注记挂 HRQ")
V["WST"] = ("MERGE_CONFIDENT", GC, "同 INC：GATE_ZONE->forage；B 层产卵深潭终段轴无 Tier A 证据不立（open_semantics）")
V["ARO"] = ("MERGE_CONFIDENT", GC, "GATE_SURFACE_ZONE->水面猎物档：结构同构；gate_axis=surface_zone=既有轴新值（参数级——B4 判例：vs 新轴才 EXT）记轴值提案挂 HRQ")
V["RRH"] = ("MERGE_CONFIDENT", ZS, "GATE_ZONE->底质->双壳贝资源：与 canonical 精确同构（canonical 源=同属 GRH）")
V["GRH"] = ("MERGE_CONFIDENT", ZS, "GATE_ZONE->底质->昆虫幼生资源：与 canonical 精确同构（canonical 源成员真形复验）")
V["SMB"] = ("MERGE_CONFIDENT", ZD, "GATE_ZONE->深度档->底质->资源：与 canonical 精确同构（canonical 源成员真形复验；CSV 深>=4m 锚）")
V["BSK"] = ("MERGE_CONFIDENT", ST, "近底带软三档->底质->资源无门：与 canonical 精确同构（canonical 源成员真形复验）")
for sid in ["GDE", "MOO", "CLC", "RTC"]:
    V[sid] = ("MERGE_CONFIDENT", NO, "夜行底板档->低光槽（adjuster 槽位原位）：与 canonical 同构；夜行轴证据分层注记（GDE=story 原文/MOO·RTC=CSV 锚/CLC=CSV+同属假说）")
for sid in ["HNC", "CRC", "MDC", "LMP", "AMK"]:
    V[sid] = ("MERGE_CONFIDENT", GA, "锚存在门->锚适配->关系->局部温度：与 canonical 精确同构；anchor 四形式值=参数（HNC/CRC=nest 构建型；MDC/LMP/AMK=egg_mass 利用型——B5 EXT 轨 anchor 值提案由真形 MC 兑现）")
for sid in ["ALB", "BIA", "PBF", "POR", "SAF", "SAI", "SDG", "SPM", "STM", "YFT"]:
    V[sid] = ("NEW_TEMPLATE_CANDIDATE", FF, "forage->habitat 两步有序链：开放水跟随型（食性主句先行）——vs LAYER_AXIS 第二步 premise 轴段=轴域差异非 MC")
for sid in ["ARG", "ASP", "BLP", "BPB", "BSB", "CCR", "CMR", "CSL", "DTN", "FDR", "GAJ", "GG",
            "GSF", "HAD", "HAL", "KGO", "LKR", "LKT", "RFP", "RKB", "ROB", "SPC", "SPK", "SSL",
            "TAI", "TMU", "TSK", "WIN"]:
    V[sid] = ("NEW_TEMPLATE_CANDIDATE", SF, "space(habitat/structure)->forage 两步有序链：结构/复合带承载先行——与 FF 序镜像（ORDER=族判据不得合并）；engine raw op 字面（EVAL_TYPED_STRUCTURE/HABITAT_FACTOR）归一读法挂 HRQ")
V["WIT"] = ("NEW_TEMPLATE_CANDIDATE", TB, "GATE 可埋底质->深冷复合带->资源三节点：vs ZONE_SUBSTRATE 因子集不同（底质门 vs 水层门+温度深度复合带步）=OPERATOR/ORDER 真差异；vs RS1 归族 GATED_COVER=族移动提案")
V["YTF"] = ("NEW_TEMPLATE_CANDIDATE", TB, "同 WIT：GATE 沙泥->中深冷复合带->多毛资源；族移动提案（RS1 GATED_COVER->本族）")
V["JGC"] = ("NEW_TEMPLATE_CANDIDATE", TU, "护巢链+浊度修饰步五节点：vs GUARD_ANCHOR 四节点多第五步（浊度语境修饰）=步数结构差异；B5 EXT 轨升级为结构差异证据")
V["JDP"] = ("NEW_TEMPLATE_CANDIDATE", TU, "同 JGC：护巢链+浊度修饰五节点（story 原文浊水承载——两尾真形一致）")
V["GW"] = ("NEW_TEMPLATE_CANDIDATE", SL, "structure->黄昏夜槽->forage 三节点：vs NOCTURNAL（底板->槽两节点）多 forage 步+首步结构语义=步数/OPERATOR 真差异")
V["GT"] = ("NEW_TEMPLATE_CANDIDATE", SL, "同 GW：礁外结构->夜槽->甲壳鱼猎物三节点")
V["BAS"] = ("NEW_TEMPLATE_CANDIDATE", FS, "habitat->forage->洪泛林槽（链尾 modifier）三节点：与 SL（槽在中位）序不同+槽语义（洪泛 vs 夜相）不同=ORDER 真差异；单成员 PROVISIONAL")
V["TGT"] = ("AMBIGUOUS_NEEDS_EXPANSION", None, "亲本系复用未消解（伏击 vs 漂流两系）+CSV 行不可信——真形挂重验（FR/表达线亲本系推导传导）")
V["PEL"] = ("AMBIGUOUS_NEEDS_EXPANSION", None, "三态食性x三型域泛化描述无链序证据——真形挂重验（FR 补证具体型/态行为描述）")

# dual-track / moved / EXT notes for HRQ
MOVED = {
    "WIT": "RS1 归族 GATED_COVER -> 本批 TB 新族（STRUCTURAL_DIFF：+深冷复合带步）",
    "YTF": "RS1 归族 GATED_COVER -> 本批 TB 新族（同 WIT）",
    "FDR": "RS1 归族 GATED_COVER -> 本批 SF（story TierA omnivore 证伪伏击门样板——无门两步链）",
    "BSB": "RS1 归族 GATED_COVER -> 本批 SF（story 无二元排除原文）",
    "SSL": "RS1 归族 GATED_COVER -> 本批 SF（story FCI：潜沙=反捕食 overlay 非伏击——证据分层）",
    "SDG": "RS1 归族 TIERED_SINGLE -> 本批 FF（裁决 4 电感知分层后 Bake 真形=双因子链）",
    "TSK": "RS1 归族 TIERED_SINGLE -> 本批 SF（深冷厂适主句先行 vs 感官组样板单步）",
}
SLOT_TIERING_CLOSE = {
    "TAI": "C8 slot_tiering 轨关闭确认->SF", "BLP": "->SF", "RFP": "->SF", "DS": "->SF(CSL 双轨合并)",
    "PBF": "->FF", "GT": "->SL 新族", "HAL": "->SF", "GG": "->SF",
    "POR": "->FF（B4 双轨合并）", "RKB": "->SF（B4 双轨合并）", "WIN": "->SF（B4 双轨合并）",
    "SMF": "->GC MC（B4 双轨合并）", "SAI": "->FF（B4 双轨合并）",
}
KGO_NOTE = "面级重指派提案：B5 EXT guard 轨（骨架占位 Tier C 零证据）vs story 无 P04——真形回归 Normal 面 SF；guard 面承载撤销挂 HRQ"

def engine_sig_matches(body_sig, canon_sig):
    return body_sig == canon_sig

def main():
    bodies = [json.loads(l) for l in open(os.path.join(OUT, "blind_programs.jsonl"), encoding="utf-8")]
    # verify registry read-only usage
    reg_path = os.path.join(CEN, "template_registry.yaml")
    reg_hash_before = hashlib.sha256(open(reg_path, "rb").read()).hexdigest()[:16]
    _ = yaml.safe_load(open(reg_path, encoding="utf-8"))  # parse check only
    assert hashlib.sha256(open(reg_path, "rb").read()).hexdigest()[:16] == reg_hash_before

    tests = []
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stats = dict(MERGE_CONFIDENT=0, TEMPLATE_EXTENSION_CANDIDATE=0, NEW_TEMPLATE_CANDIDATE=0, AMBIGUOUS_NEEDS_EXPANSION=0)
    for b in sorted(bodies, key=lambda x: x["species_id"]):
        sid = b["species_id"]
        sig = body_signature(b)
        verdict, target, note = V[sid]
        # engine raw: which canonicals share the signature
        raw = [tid for tid, c in CANON.items() if engine_sig_matches(sig, c["sig"])]
        engine_raw_diffs = []
        if target and target in CANON and sig != CANON[target]["sig"]:
            engine_raw_diffs.append("signature mismatch vs %s canonical" % target)
        tests.append(dict(
            test_id="MT-RB1-%s" % sid,
            program_id=b["program_id"], species_id=sid,
            signature=sig,
            engine_raw_same_signature_families=raw,
            engine_raw_diffs=engine_raw_diffs,
            verdict=verdict,
            target_family=target,
            same=verdict == "MERGE_CONFIDENT",
            param_only=[],
            structural_diffs=[] if verdict == "MERGE_CONFIDENT" else (
                ["ORDER（序镜像或轴域）"] if "FF" == (target or "")[-2:] or "SF" == (target or "")[-2:] else
                ["OPERATOR/步数/结构元素"]),
            semantic_note=note,
            moved_proposal=MOVED.get(sid),
            dual_track_note=SLOT_TIERING_CLOSE.get(sid),
            kgo_note=KGO_NOTE if sid == "KGO" else None,
            human_review_queued=(None if verdict == "MERGE_CONFIDENT" else (
                "HRQ-RB1-02" if (target or "").endswith("__NEW") else
                "HRQ-RB1-03" if sid in ("INC", "WST", "ARO") else "HRQ-RB1-05")),
            order_derivation_status=b["order_derivation"]["status"],
            ts=now,
        ))
        stats[verdict] += 1
    with open(os.path.join(OUT, "merge_tests.jsonl"), "w", encoding="utf-8") as f:
        for t in tests:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    report = dict(
        batch=BATCH, generated_at=now,
        registry_version="v9 (read-only; zero mutation this batch)",
        n_truth_bodies=len(bodies),
        verdicts=stats,
        new_family_proposals=dict(
            FORAGE_FIRST_DUAL_TIER_CHAIN__NEW=sorted(t["species_id"] for t in tests if t["target_family"] == FF),
            SPACE_FIRST_DUAL_TIER_CHAIN__NEW=sorted(t["species_id"] for t in tests if t["target_family"] == SF),
            GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN__NEW=sorted(t["species_id"] for t in tests if t["target_family"] == TB),
            GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN__NEW=sorted(t["species_id"] for t in tests if t["target_family"] == TU),
            STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN__NEW=sorted(t["species_id"] for t in tests if t["target_family"] == SL),
            HABITAT_FORAGE_FLOODSLOT_CHAIN__NEW=sorted(t["species_id"] for t in tests if t["target_family"] == FS),
        ),
        family_move_proposals=MOVED,
        slot_tiering_track_closure=SLOT_TIERING_CLOSE,
        confirmations=dict(
            canonical_order_confirmed_families=[
                "GATED_COVER_TIER_CHAIN(6)", "ZONE_SUBSTRATE_RESOURCE_CHAIN(2)",
                "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN(1)", "NOCTURNAL_LIGHTSLOT_CHAIN(4)",
                "GUARD_ANCHOR_TIERED_COMBINE_CHAIN(5)", "SOFT_TRIPLE_TIER_CHAIN(1)",
                "TIERED_SINGLE_FACTOR_CHAIN(16; 单步无序判据适用)",
            ],
            note="MC 成员真形序=所在族 canonical 序——为 order_provisional 证据态提供确认证据（v10 降级提案待独立审）",
        ),
        held_absence=["ASR", "RVS", "RDS"],
        ambiguity=["TGT", "PEL"],
    )
    with open(os.path.join(OUT, "engine_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))
    print("new families:", {k: len(v) for k, v in report["new_family_proposals"].items()})

if __name__ == "__main__":
    main()
