# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-001 output builder: programs.jsonl, coverage.jsonl,
human_review_queue.jsonl, manifest verdict section append."""
import json, os, datetime

ROOT = r"A:\Projs\FCF-Harness-Handoff\programaticHitFish"
BATCH = "CENSUS-REBUILD-001"
OUT = os.path.join(ROOT, "fish_logic_census", "batches", BATCH)

def main():
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    bodies = {json.loads(l)["species_id"]: json.loads(l) for l in open(os.path.join(OUT, "blind_programs.jsonl"), encoding="utf-8")}
    tests = [json.loads(l) for l in open(os.path.join(OUT, "merge_tests.jsonl"), encoding="utf-8")]
    stories = [json.loads(l) for l in open(os.path.join(OUT, "stories.jsonl"), encoding="utf-8")]

    FAMNAME = {
        "TIERED_SINGLE_FACTOR_CHAIN": "TIERED_SINGLE_FACTOR_CHAIN",
        "GATED_COVER_TIER_CHAIN": "GATED_COVER_TIER_CHAIN",
        "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": "GUARD_ANCHOR_TIERED_COMBINE_CHAIN",
        "NOCTURNAL_LIGHTSLOT_CHAIN": "NOCTURNAL_LIGHTSLOT_CHAIN",
        "ZONE_SUBSTRATE_RESOURCE_CHAIN": "ZONE_SUBSTRATE_RESOURCE_CHAIN",
        "SOFT_TRIPLE_TIER_CHAIN": "SOFT_TRIPLE_TIER_CHAIN",
        "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN",
        "FORAGE_FIRST_DUAL_TIER_CHAIN__NEW": "FORAGE_FIRST_DUAL_TIER_CHAIN（新族提案——registry 零改动，v10 待批）",
        "SPACE_FIRST_DUAL_TIER_CHAIN__NEW": "SPACE_FIRST_DUAL_TIER_CHAIN（新族提案——registry 零改动，v10 待批）",
        "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN__NEW": "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN（新族提案）",
        "GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN__NEW": "GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN（新族提案）",
        "STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN__NEW": "STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN（新族提案）",
        "HABITAT_FORAGE_FLOODSLOT_CHAIN__NEW": "HABITAT_FORAGE_FLOODSLOT_CHAIN（新族提案）",
    }
    # programs.jsonl
    with open(os.path.join(OUT, "programs.jsonl"), "w", encoding="utf-8") as f:
        for t in sorted(tests, key=lambda x: x["species_id"]):
            b = bodies[t["species_id"]]
            f.write(json.dumps(dict(
                program_id=t["program_id"], story_id=b["story_id"], species_id=t["species_id"],
                surface="Bake",
                consequence=t["verdict"],
                family_membership=FAMNAME.get(t["target_family"], "UNDETERMINED_HELD"),
                review_ref=None if t["verdict"] == "MERGE_CONFIDENT" else (
                    "HRQ-RB1-02" if (t["target_family"] or "").endswith("__NEW") else
                    "HRQ-RB1-03" if t["species_id"] in ("INC", "WST", "ARO") else
                    "HRQ-RB1-05" if t["species_id"] in ("TGT", "PEL") else "HRQ-RB1-01"),
                blind_hash=b["blind_hash"],
                original_program_body_unchanged=True,
                registry_seen_at_creation=False,
                post_registry_mutations=[],
                provenance=dict(batch=BATCH),
            ), ensure_ascii=False) + "\n")
    # coverage.jsonl
    with open(os.path.join(OUT, "coverage.jsonl"), "w", encoding="utf-8") as f:
        for s in stories:
            sid = s["species_id"]
            t = next(x for x in tests if x["species_id"] == sid)
            f.write(json.dumps(dict(
                story_id=s["story_id"], species_id=sid,
                queue_ids=s["queue_ids"],
                bake=t["verdict"], response="NOT_IN_SCOPE（本批仅 Bake 面——truth_rebuild_queue surface=Bake）",
                group="NO_SURFACE_EFFECT（queue 面=Bake）", quality="NO_SURFACE_EFFECT（queue 面=Bake）",
                note="dual_track" if s["dual_track"] else "",
            ), ensure_ascii=False) + "\n")
        # held absence coverage
        for a in [json.loads(l) for l in open(os.path.join(OUT, "absence_claims.jsonl"), encoding="utf-8")]:
            f.write(json.dumps(dict(
                story_id="%s-%s-HELD" % (BATCH, a["species_id"]), species_id=a["species_id"],
                queue_ids=a["queue_ids"], bake="EVIDENCE_INSUFFICIENT_HELD",
                response="NOT_IN_SCOPE", group="NOT_IN_SCOPE", quality="NOT_IN_SCOPE",
                note=a["reason"],
            ), ensure_ascii=False) + "\n")
    # HRQ
    hrq = [
        dict(id="HRQ-RB1-01", title="七条族移动提案：RS1 归族 vs 本批 Tier A 真形分歧",
             items=["WIT/YTF: RS1 GATED_COVER -> GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN（+深冷/中深冷复合带步——story 原文一句群）",
                    "FDR/BSB/SSL: RS1 GATED_COVER -> SPACE_FIRST（story：FDR=Bottom Omnivater 无伏击/BSB 无二元排除原文/SSL 潜沙=反捕食 overlay）",
                    "SDG/TSK: RS1 TIERED_SINGLE -> FF/SF（裁决 4 电感知分层后 SDG=双因子链；TSK 深冷主句先行）"],
             basis="证据分层：RS1 归族依表达文件样板（Tier B 受限还原），本批真形从 Tier A story 主句推导——EEL 判例②同型不静默归并",
             ask="批准 7 条移动+新族接收（WIT/YTF 为 TB 新族源成员）"),
        dict(id="HRQ-RB1-02", title="六个新族提案+同签名三族语义区分",
             items=["FORAGE_FIRST_DUAL_TIER_CHAIN（10：POR SAI SDG SAF YFT STM ALB SPM BIA PBF）——forage->habitat 序",
                    "SPACE_FIRST_DUAL_TIER_CHAIN（28：结构/复合带->forage 序——与 FF 序镜像）",
                    "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN（2：WIT YTF）",
                    "GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN（2：JGC JDP——护巢链+浊度修饰第五步）",
                    "STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN（2：GW GT——结构->夜槽->猎物）",
                    "HABITAT_FORAGE_FLOODSLOT_CHAIN（1：BAS——链尾洪泛槽 modifier，单成员 PROVISIONAL）"],
             basis="[E,E] 签名三族语义区分：LAYER_AXIS 第二步=premise 轴段（轴域限定）vs FF/SF 两空间因子序镜像——ORDER=族判据；SPACE_FIRST 族内 op 字面（EVAL_TYPED_STRUCTURE_FACTOR vs EVAL_TYPED_HABITAT_FACTOR）归一为『空间适配先行』判断位读法需确认",
             ask="六族立案（v10）+op 字面归一读法确认+canonical 源成员指定（FF=PORS、SF=建议 RKB 或 BSB、TB=WIT、TU=JGC、SL=GW、FS=BAS——canonical=本批冻结真形体）"),
        dict(id="HRQ-RB1-03", title="GATED_COVER 轴域扩展三点",
             items=["INC/WST：GATE_ZONE->forage 单档 MC——canonical 第二步『掩体/质量档』语义扩展到 forage 场（factor_type typed 参数读法）",
                    "ARO：gate_axis=surface_zone 新轴值（既有轴新值=参数级——B4 判例）",
                    "对照：GPF/SMF/LMD 标准掩体档 MC 无争议"],
             basis="GATED_COVER 族域=门+单档（forbidden: 无门单档=TIERED_SINGLE 域）——factor_type 是否涵盖 forage 场语义",
             ask="INC/WST MC 确认+ARO 轴值登记"),
        dict(id="HRQ-RB1-04", title="B5 EXT guard 轨四例处置",
             items=["MDC/LMP/AMK/CRC：anchor 四形式值提案由真形 MC 兑现（EXT->MC 成员资格确认）",
                    "JGC：EXT 轨升级为结构差异（+浊度修饰步=TU 新族）",
                    "KGO：面级重指派——story 无 P04（S6 SN），真形回归 Normal 面 SF；B5 guard 面承载（骨架占位 Tier C 零证据）撤销提案"],
             basis="story Sweep 逐项证据 vs B5 EXT 轨（表达文件 Tier B/C 投影）",
             ask="三类处置批准"),
        dict(id="HRQ-RB1-05", title="真形挂起与 held 复核",
             items=["TGT：亲本系复用未消解（褐鳟机会型 vs 溪鳟伏击）+CSV 行不可信（reef-associated 海水行 vs 淡水杂交种）",
                    "PEL：三态食性×三型泛化无链序证据",
                    "3 held（ASR/RVS/RDS）：维持 evidence_insufficient_held（无表达文件）"],
             basis="§6.4-4 顺序证据不足不虚构",
             ask="挂起重验队列立案（FR/表达线补证通道）"),
        dict(id="HRQ-RB1-06", title="order_provisional 确认证据+并行批影响确认",
             items=["7 族获真形序确认：GATED_COVER(6)/ZONE_SUBSTRATE(2)/ZONE_DEPTH(1)/NOCTURNAL(4)/GUARD_ANCHOR(5)/SOFT_TRIPLE(1)/TIERED_SINGLE(16 单步)——MC 成员真形序=canonical 序",
                    "v10 提案：上述 7 族 order_provisional 证据态降级（本批 Tier A 逐鱼推导为据）",
                    "REP-WORDING-ALIGN-001 并行影响=零（其不动 §0 顺序行/链形/步序；本批引文按对齐前文本标注——manifest bias_declaration 已声明）"],
             basis="本批 35 MC 真形复验+registry 零改动纪律",
             ask="降级提案批准（随 v10 mutation 批）"),
    ]
    with open(os.path.join(OUT, "human_review_queue.jsonl"), "w", encoding="utf-8") as f:
        for h in hrq:
            f.write(json.dumps(h, ensure_ascii=False) + "\n")
    # manifest append verdict section
    mc = sum(1 for t in tests if t["verdict"] == "MERGE_CONFIDENT")
    nw = sum(1 for t in tests if t["verdict"] == "NEW_TEMPLATE_CANDIDATE")
    am = sum(1 for t in tests if t["verdict"] == "AMBIGUOUS_NEEDS_EXPANSION")
    # REV-001 F6: idempotent guard + format fix (template had unformatted {mc} literal and garbage string)
    _post = """
post_registry:
  registry_opened_for_merge_tests: true（run_merge_tests.py 只读——template_registry.yaml 零改动验证：sha256 前后一致）
  verdicts:
    counts: MERGE_CONFIDENT={mc} NEW_TEMPLATE_CANDIDATE={nw} AMBIGUOUS_NEEDS_EXPANSION={am} HELD=3
    new_family_proposals_distinct: 6（FF 10/SF 28/TB 2/TU 2/SL 2/FS 1——curve n_new_template=6）
    family_move_proposals: 7（HRQ-RB1-01）
    canonical_order_confirmations: 7 族（HRQ-RB1-06）
  status: INDEPENDENT_REVIEW_REQUIRED
""".format(mc=mc, nw=nw, am=am)
    _mf = os.path.join(OUT, "manifest.yaml")
    if "post_registry:" in open(_mf, encoding="utf-8").read():
        print("manifest post_registry already present (idempotent skip)")
    else:
        with open(_mf, "a", encoding="utf-8") as f:
            f.write(_post)
    with open(os.path.join(OUT, "manifest.yaml"), "a", encoding="utf-8") as f:
        f.write("  generated_at: %s\n" % now)
    print("programs:", len(tests), "| hrq:", len(hrq))

if __name__ == "__main__":
    main()
