# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-002: programs/coverage/HRQ/absence/curve 一体化产出。"""
import json, os
from datetime import datetime, timezone
from pathlib import Path

BATCH = Path(__file__).parent
CEN = BATCH.parents[1]
mt = {t["species_id"]: t for t in map(json.loads, (BATCH / "merge_tests.jsonl").read_text(encoding="utf-8").splitlines())}
bodies = {b["species_id"]: b for b in map(json.loads, (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines())}
stories = {s["species_id"]: s for s in map(json.loads, (BATCH / "stories.jsonl").read_text(encoding="utf-8").splitlines())}
assert len(mt) == len(bodies) == len(stories) == 94
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ---- programs.jsonl ----
progs = []
for sid, t in mt.items():
    b = bodies[sid]
    progs.append({
        "program_id": b["program_id"],
        "story_id": b["story_id"],
        "species_id": sid,
        "surface": "Bake",
        "consequence": "MERGE_CONFIRMED" if t["verdict"] == "MERGE_CONFIDENT" else "NEW_PROGRAM_CANDIDATE",
        "family_membership": t["target_family"],
        "membership_status": ("CONFIRMED_MEMBER" if t["verdict"] == "MERGE_CONFIDENT" and not t["moved_proposal"]
                              else "CANDIDATE_FAMILY_MEMBER"),
        "order_confirm": t["order_confirm"],
        "moved_proposal": t["moved_proposal"],
        "related_proposal": t["related_proposal"],
        "reused_from": t["reused_from"],
        "review_ref": None if t["verdict"] == "MERGE_CONFIDENT" else "HRQ-RB2-02",
        "blind_hash": b["blind_hash"],
        "original_program_body_unchanged": True,
        "registry_seen_at_creation": False,
        "post_registry_mutations": ([] if sid not in ("BHC", "HER") else
                                    [{"field": "return_type",
                                      "reason": "Bake face return contract correction (queue item=Bake surface; RS1 C6 frozen body same evidence) - contract field, not registry-fit motivated",
                                      "revision_recorded": "REV-RB2-001-%s" % sid,
                                      "bias_risk_flagged": True}]),
        "rerun_of": ("P-RS1-%s-BAKE" % sid) if t.get("rs1_current_family") else ("P-B6-%s-BAKE" % sid),
        "provenance": {"batch": "CENSUS-REBUILD-002", "input": "truth_rebuild_queue:%s（终局顺序还原重跑）" % b["order_derivation"]["queues"][0]},
    })
(BATCH / "programs.jsonl").write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in progs) + "\n", encoding="utf-8")

# ---- coverage.jsonl ----
cov = []
for sid in sorted(stories):
    t = mt[sid]
    cov.append({
        "story_id": stories[sid]["story_id"], "species_id": sid,
        "queue_ids": stories[sid]["queue_ids"],
        "bake": t["verdict"],
        "response": "NOT_IN_SCOPE（本批仅 Bake 面——truth_rebuild_queue surface=Bake）",
        "group": "NO_SURFACE_EFFECT（queue 面=Bake）",
        "quality": "NO_SURFACE_EFFECT（queue 面=Bake）",
        "order_status": stories[sid]["order_status"],
        "note": ("order_provisional 确认" if t["order_confirm"] else ("族移动提案" if t["moved_proposal"] else "")),
    })
(BATCH / "coverage.jsonl").write_text("\n".join(json.dumps(c, ensure_ascii=False) for c in cov) + "\n", encoding="utf-8")

# ---- human_review_queue.jsonl ----
hrq = [
 {"id": "HRQ-RB2-01", "title": "十六族移动提案+FILTER_FIELD 空置提案（RS1 在册成员真形序终裁）",
  "items": [
    "TIERED_SINGLE -> LAYER_AXIS x4（CHN/COH/BRO/ALE：垂直层与水平洄游廊道独立维度——CSV benthopelagic/pelagic-neritic 锚入步；B 层样板语义还原不采）",
    "TIERED_SINGLE -> FF x3（BRT12/PB/SDG：食性主句先行两步链）+ SF x1（TSK：深冷主句先行）",
    "GATED_COVER -> ZONE_SUBSTRATE x1（SNS：'over soft substrates' 原文级底质独立步=三步链）",
    "GATED_COVER -> SF x3（FDR/BSB/SSL——RB-1 移动提案的 RS1 轨独立复核一致）+ TB x2（WIT/YTF——RB-1 提案双轨确认）",
    "FILTER_FIELD_ACCUMULATE_CHAIN -> TIERED_SINGLE x2（BHC/HER：单步场浓度评估——B 层三步展开无 story 级顺序证据）；FILTER_FIELD 移空 0 成员——空置提案（PATCH VACATED 先例）",
  ],
  "basis": "HRQ-REBUILD-SCOPE-001：链族在册成员基础序为模板约定（order_provisional）——本批 Tier A story 主句+CSV 锚逐鱼推导真形序与所在族 canonical 不符=STRUCTURAL_DIFF（裁决 2-B 顺序=族判据）",
  "ask": "批准 16 条移动+FILTER_FIELD 空置（v10 mutation 待独立审另批执行）"},
 {"id": "HRQ-RB2-02", "title": "RB-1 新族提案形状的扩充证据（FF+9/SF+6/TB+0/FS+1——本批 distinct 新族=0）",
  "items": [
    "FORAGE_FIRST（HRQ-RB1-02 提案）+16 证据：B6 层 13 尾（ASB/BHM/BTS/EUP/GDS/JSB/PKS/PLC/PRB/PSH/RSC/RUF/SSM）+RS1 轨 3 尾（BRT12/PB 推导+SDG 复用复核）",
    "SPACE_FIRST（HRQ-RB1-02）+2 新证据（CGD/RBD——栖息复合主句先行 B6 首证）+RS1 复核 4 尾（SSL/FDR/BSB/TSK）",
    "HABITAT_FORAGE_FLOODSLOT（HRQ-RB1-02 BAS 单成员 PROV）+1 第 2 实证（SLM 银斑鲫——herbivore highly dependent on floodplains 原文级）：单成员 PROV 升 2 成员",
    "GATE_SUBSTRATE_TEMPBAND（HRQ-RB1-02）+0 新增（WIT/YTF=同鱼 RS1 轨确认）",
    "本批 n_new_template（curve distinct 口径）=0：全部 NEW 落 RB-1 六提案形状内，无新形状",
  ],
  "basis": "envelope：判同只对 registry v9 活族（18）；RB-1 提案形状按 related_proposal=HRQ-RB1-02 备注累积证据",
  "ask": "与 HRQ-RB1-02 合并裁决（新族批准后成员名单扩充）"},
 {"id": "HRQ-RB2-03", "title": "BHC/HER 单步场浓度链的轴域读法+return_type 修正留痕",
  "items": [
    "单步场 evaluand（EVAL_FIELD_CONCENTRATION）按 TIERED_SINGLE factor_type=field 轴值读法（B2 判例'factor_type 轴第 2 类场实例'复活）——canonical EVAL_TYPED_FIELD_OR_FACTOR 单步+场轴",
    "B 层三步展开（滤食水层定位/鳃耙口径步）无 story 级顺序证据——census 冻结 sketch 单步场评估（'与水层'由场的水柱分布承载）",
    "REV-RB2-001：return_type FieldFeeding->SpatialDistributionWeight（Bake 面契约——RS1 C6 冻结体同证；发现于 registry 已开后判同准备期，program_revisions+manifest freeze_history 双留痕；判同四态前后不受影响）",
  ],
  "basis": "场 evaluand 因子与离散 patch 因子的族域边界（B2 HRQ-B2-01 立族判例域）",
  "ask": "裁决 factor_type=field 轴域读法是否维持（vs 立 BAKE_FIELD 单步新族）"},
 {"id": "HRQ-RB2-04", "title": "AST/SNS 的 B 层轴分歧（Tier B 受限还原 vs Tier A story 真形）",
  "items": [
    "AST：B 层第二轴=掩体档（@ATSEstuaryBottomProfile）；真形第二轴=底栖探食场（story 'feeding on crustaceans, worms, and molluscs'+口侧 4 须）——同 INC/WST gate->forage 参数读法",
    "SNS：B 层两步（GATE_ZONE->掩体档）；真形三步（+软底质插食档——'over soft substrates' 原文级）——步数差异",
  ],
  "basis": "证据分层（Tier A story vs Tier B 表达投影）——EEL 判例②同型不静默归并；表达线若补证可复议",
  "ask": "确认 Tier A 优先读法（表达线对齐另批）"},
 {"id": "HRQ-RB2-05", "title": "品系/杂交轨真形分辨率（12 品系+HYS）",
  "items": [
    "8 鲤品系（SUK/GRK/KHK/OGK/LCP/AMC/ASC/HFC）=同种 CSV 单因子（benthopelagic 静水带）MC TIERED_SINGLE——亲本（鲤/锦鲤/镜鲤/鳞鲤 R03 轨）真形不在重跑队列，补证后升档复核",
    "WAG（雀鳝科伏击）/WCC（鲿形目夜行底栖）/HYS（鲟形目底栖探食）=亲本构型+CSV 复用真形（MC）",
    "WS2=RB-1 WST 同种复用（Cross-Batch 去重联动第 2 例）；AGC=GRB 同种（批内联动）；JSB↔ASB 同 URL 同种（真形同体，双 queue 项独立记账）",
  ],
  "basis": "Identity Deferred 品系行 S1-S11 全 SN——分辨率=同种物种级（证据分辨率决定链长）",
  "ask": "确认品系轨分辨率处理（亲本批补证通道）"},
 {"id": "HRQ-RB2-06", "title": "同鱼对账执行记录（复用/异面/去重——零冲突）",
  "items": [
    "reused_from=RB-1 共 18（17 同鱼同面 B4 起源+1 同种品系 WS2）；一致性核验=RB-1 basis 事实逐条存在于 B4 快照",
    "RBP 同鱼异面：RB-1=摄食面单因子/本批=护卵面四步——两程序面独立记账（REV-001 ④ 同物种双面先例）",
    "同鱼冲突数=0（RB-1 与本批无矛盾推导——RB-1 移动提案成员的 RS1 轨复核全部一致）",
  ],
  "basis": "envelope 同鱼对账指令；面级守恒判据（RS1 REV-001 ②）",
  "ask": "备查（无需裁决——记录性条目）"},
]
(BATCH / "human_review_queue.jsonl").write_text("\n".join(json.dumps(h, ensure_ascii=False) for h in hrq) + "\n", encoding="utf-8")

# ---- absence_claims.jsonl（本批无 held——94 项全消费） ----
(BATCH / "absence_claims.jsonl").write_text("", encoding="utf-8")

# ---- discovery curve append（幂等守卫） ----
from collections import Counter
cnt = Counter(t["verdict"] for t in mt.values())
curve = CEN / "discovery_curve.csv"
lines = curve.read_text(encoding="utf-8").strip().splitlines()
assert lines[0].startswith("batch_id,n_stories_consumed")
# REV-001 F1：n_new_template_candidate 列=distinct 新族口径（判例 CENSUS-REBUILD-001-REV-001 #2）——
# 本批 distinct=0（NEW 25 全落 RB-1 提案形状，无本批新族）。distinct_new_families 显式常量承口径。
DISTINCT_NEW_FAMILIES_RB2 = 0
row = "CENSUS-REBUILD-002,94,94,%d,0,%d,0,0,0,0,0,0,0,0" % (cnt["MERGE_CONFIDENT"], DISTINCT_NEW_FAMILIES_RB2)
if any(l.startswith("CENSUS-REBUILD-002,") for l in lines):
    print("curve: row already present (idempotent skip)")
else:
    lines.append(row)
    curve.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("curve: appended", row)

print("programs", len(progs), "coverage", len(cov), "hrq", len(hrq), "absence 0")
