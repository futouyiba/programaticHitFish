# -*- coding: utf-8 -*-
"""CENSUS-RERUN-PLAIN-001 语义裁决与产物装配（build_census_outputs）。

产物：programs.jsonl / merge_tests.jsonl / stories.jsonl /
absence_claims.jsonl（空——9/9 有输入）/ coverage.jsonl（空）/
program_revisions.jsonl（空）/ resolver_tests.jsonl（空）/
human_review_queue.jsonl / manifest.yaml +
仓库级 template_registry.yaml v7→v8 + discovery_curve.csv 追加行。

语义裁决（四态，worker 层）依据 engine_report.json + 判同经验判例：
- PLAIN 原始 5 × v1：CHB/WAL/MDF 槽值三档=slot_tiering（RS1 C8 判例）→
  TEMPLATE_EXTENSION_CANDIDATE（并入 HRQ-RS1-03 轨——本批 3 例为原始成员，
  census story 证据与表达投影同向，无来源分歧）；OSC（极值门+EXIT 档）与
  BRT（patch 门+双槽混合档+无归一化）→ NEW_TEMPLATE_CANDIDATE（gate=结构元素）
- HARD_GATED 2 × v1：LUN→canonical v2 升级提案（族定义保持，NEW 记录+挂
  HRQ-RP1-01）；EEL→AMBIGUOUS_NEEDS_EXPANSION（BUILD 投影缺口+[需核对]）
- PATCH 2 × v1：MGC/ONS→NEW（canonical 评估先行证伪），重指派
  GATED_COVER / SOFT_TRIPLE（membership 直验语义 MC）
- 边界 11 + CRR 9：non-match 证据（NEW 记录；CRR 不重复登记）
"""
import json
from pathlib import Path

BATCH = Path(__file__).parent
CENSUS = BATCH.parents[1]
REG = CENSUS / "template_registry.yaml"
CURVE = CENSUS / "discovery_curve.csv"

engine = json.loads((BATCH / "engine_report.json").read_text(encoding="utf-8"))
progs = {p["program_id"]: p for p in
         (json.loads(l) for l in (BATCH / "blind_programs.jsonl").read_text(
             encoding="utf-8").splitlines() if l.strip())}
B = "CENSUS-RERUN-PLAIN-001"

RERUN_OF = {p["species_id"]: p["rerun_of"] for p in progs.values()}


def write_jsonl(name, rows):
    (BATCH / name).write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n",
        encoding="utf-8")


def main():
    # ---------------- programs.jsonl ----------------
    FAM = {
        "OSC": ("EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN", "CANDIDATE_NEW_FAMILY", "HRQ-RP1-02"),
        "CHB": ("PLAIN_FACTOR_COMBINE", "PROPOSED_PENDING_REVIEW", "HRQ-RS1-03+HRQ-RP1-03"),
        "BRT": ("PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN", "CANDIDATE_NEW_FAMILY", "HRQ-RP1-02"),
        "WAL": ("PLAIN_FACTOR_COMBINE", "PROPOSED_PENDING_REVIEW", "HRQ-RS1-03+HRQ-RP1-03"),
        "MDF": ("PLAIN_FACTOR_COMBINE", "PROPOSED_PENDING_REVIEW", "HRQ-RS1-03+HRQ-RP1-03"),
        "LUN": ("HARD_GATED_FACTOR_COMBINE", "CANONICAL_V2_SOURCE_PROPOSED", "HRQ-RP1-01"),
        "EEL": ("HARD_GATED_FACTOR_COMBINE", "AMBIGUOUS_PENDING_EVIDENCE_LAYERING", "HRQ-RP1-01+HRQ-RP1-04"),
        "MGC": ("GATED_COVER_TIER_CHAIN", "PROPOSED_PENDING_REVIEW", "HRQ-RP1-02"),
        "ONS": ("SOFT_TRIPLE_TIER_CHAIN", "PROPOSED_PENDING_REVIEW", "HRQ-RP1-02"),
    }
    programs = []
    for pid, p in progs.items():
        code = p["species_id"]
        fam, status, ref = FAM[code]
        programs.append({
            "program_id": pid, "story_id": p["story_id"],
            "species_id": code, "surface": "Bake",
            "consequence": "NEW_PROGRAM_CANDIDATE",
            "family_membership": fam,
            "membership_status": status,
            "review_ref": ref,
            "blind_hash": p["blind_hash"],
            "original_program_body_unchanged": True,
            "registry_seen_at_creation": False,
            "post_registry_mutations": [],
            "rerun_of": RERUN_OF[code],
            "provenance": {"batch": B,
                           "input": "顺序还原后 B 系列表达文件 §2.2/§2.4 NormalFeeding 面（REP-ORDER-FIX-001..004）"},
        })
    write_jsonl("programs.jsonl", programs)

    # ---------------- merge_tests.jsonl（语义四态） ----------------
    tests = []
    raw = {}
    for sec in ("vs_plain_v1", "vs_hard_gated_v1", "vs_patch_v1"):
        for r in engine[sec]:
            raw[(sec, r["program_id"])] = r["engine_structural_diff"]
    for r in engine["membership"]:
        raw[("membership", r["program_id"], r["family"])] = r["engine_structural_diff"]
    for r in engine["boundary"]:
        raw[("boundary", r["program_id"], r["template"])] = r["engine_structural_diff"]
    for r in engine["vs_crr"]:
        raw[("crr", r["program_id"])] = r["engine_structural_diff"]
    body_diff = lambda d: sorted(x for x in d if x != "PREMISE")
    P = lambda v: {"provenance": {"batch": B}}

    # A) PLAIN 5 × v1
    for pid in ("P-RP1-CHB-BAKE", "P-RP1-WAL-BAKE", "P-RP1-MDF-BAKE"):
        code = pid.split("-")[2]
        tests.append({
            "program_id": pid, "template_id": "PLAIN_FACTOR_COMBINE",
            "verdict": "TEMPLATE_EXTENSION_CANDIDATE", "same": False, "param_only": True,
            "structural_diffs": ["BRANCH"],
            "engine_raw_diffs": raw[("vs_plain_v1", pid)],
            "extension_complexity_cost": (
                "+1 有界 typed 参数轴 slot_tiering(FLAT | IF3_SLOT_VALUE)（§5.1 对 PLAIN 槽的"
                "受限档位化：excluded=出局槽值非 EARLY_RETURN——槽无 gate 语义族域边界维持）；"
                "canonical body 拓扑零改动（槽间 unordered/终合并不变）；槽 arity 在 factor_set 轴"
                "声明域（2–6 槽，HRQ-B1-04 先例）；槽名/槽值 guard=factor_type 字面（B0 OSC/CHB "
                "判例：OPERATOR 仅为具体因子名字面在轴内）"),
            "new_template_complexity_cost": (
                "为槽内档位化复制整条 PLAIN 槽-组合拓扑为独立族——与本族原始成员仅差槽内 branch，"
                "且顺序还原已对全库 PLAIN 投影文件统一施加同款受限还原（RS1 14 例+本批 3 例=17 例"
                "同形），违反 F10/F14 节俭"),
            "recommended_shape": (
                "扩展 PLAIN：slot_tiering 轴提案并入 HRQ-RS1-03（本批 3 例=原始成员身份，census "
                "story 证据=多因子 PLAIN 与表达投影同向——与 RS1 14 例的『story 证据单因子 vs 投影"
                "双槽』来源分歧不同，本批无证据分层问题，仅 slot_tiering 一项真差异；PLAIN v1 平铺"
                "canonical 经原始成员全体重跑证伪，canonical v2 为唯一存活读法）。批前 3 例维持挂账"),
            "proposed_parameter_axis": "slot_tiering(FLAT | IF3_SLOT_VALUE)（RS1 已提案轴，HRQ-RS1-03）",
            "human_review_queued": "HRQ-RS1-03+HRQ-RP1-03", **P(0)})
    for pid, reason in (
            ("P-RP1-OSC-BAKE",
             "前置极值水温硬门（GATE_EXTREME_TEMP——末位算术门还原为前置出局判定）+因子槽 EXIT 档"
             "（排除档=EARLY_RETURN 非 PLAIN 槽值出局）——gate 为结构元素（B0 LUN vs PLAIN 判例"
             "同型：前置 hard gate=真结构差异不得 MERGE，HRQ-03 谱系）+档位化双位移。处置提案="
             "新候选族 EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN（单成员 PROVISIONAL）"),
            ("P-RP1-BRT-BAKE",
             "patch 存在性门先行（无 patch 格无竞争占位对象——存在性先行）+槽1 EXIT 档+槽2 槽值档"
             "（core-vs-edge）+COMBINE 无归一化步——GATE/BRANCH/归一化缺失=三重结构差异非轴内"
             "（槽 arity 2 在 factor_set 轴内不计）。处置提案=新候选族 "
             "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN（单成员 PROVISIONAL；TAR-05 退化条款携带）")):
        tests.append({
            "program_id": pid, "template_id": "PLAIN_FACTOR_COMBINE",
            "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
            "structural_diffs": body_diff(raw[("vs_plain_v1", pid)]),
            "engine_raw_diffs": raw[("vs_plain_v1", pid)],
            "reasoning": "顺序还原重跑：与 PLAIN v1 平铺 canonical body 结构差异——" + reason,
            "human_review_queued": "HRQ-RP1-02", **P(0)})

    # B) HARD_GATED 2 × v1
    tests.append({
        "program_id": "P-RP1-LUN-BAKE", "template_id": "HARD_GATED_FACTOR_COMBINE",
        "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
        "structural_diffs": body_diff(raw[("vs_hard_gated_v1", "P-RP1-LUN-BAKE")]),
        "engine_raw_diffs": raw[("vs_hard_gated_v1", "P-RP1-LUN-BAKE")],
        "reasoning": (
            "顺序还原重跑 vs v1 canonical（BUILD→GATE→平铺因子→COMBINE）body 结构差异：①第二道"
            "极值水温硬门（末位算术门还原为前置出局）②因子档位化（BRANCH：排除档=EARLY_RETURN）"
            "③时段槽新增（因子 3→4，factor_set 轴内）。族定义（硬门前置+因子组合，forbidden "
            "freedoms『gate 后相对寻优』边界未动）保持——2/2 成员同向。处置提案=canonical v2 "
            "升级（非拆族非新族）：v2=本成员冻结体（BUILD→GATE_SURFACE_ACCESS→GATE_EXTREME_TEMP"
            "→EXIT 档因子×4 unordered→COMBINE_WEIGHTED）。与 RS1 SINGLE v2-or-SPLIT 问题同构"
            "（HRQ-RS1-01），worker 倾向升级：差异全在族定义内的门数/档位轴，无族域违例"),
        "human_review_queued": "HRQ-RP1-01", **P(0)})
    tests.append({
        "program_id": "P-RP1-EEL-BAKE", "template_id": "HARD_GATED_FACTOR_COMBINE",
        "verdict": "AMBIGUOUS_NEEDS_EXPANSION", "same": False, "param_only": False,
        "structural_diffs": body_diff(raw[("vs_hard_gated_v1", "P-RP1-EEL-BAKE")]),
        "engine_raw_diffs": raw[("vs_hard_gated_v1", "P-RP1-EEL-BAKE")],
        "reasoning": (
            "悬置待证据扩充：§2.4 投影自声明缺陷——①族硬门为本批从配置表还原（原平铺脚本漏写），"
            "字段名 [需核对：P-EEL-BAKE 硬门字段名]（HRQ-02 队列在案）；②census B0 原体"
            "BUILD_ACCESSIBLE_SET 在 §2.4 未承载（文件无『构建可访问集』行）。Tier A story 证据"
            "（B0：构建可访问集→水面可达硬门→…）支持 BUILD 存在——若按 story 层补回 BUILD+具名"
            "硬门，EEL 与 LUN v2 形同构（直验并入）；若投影层缺口为真（无 BUILD），EEL 为双门"
            "无 BUILD 变体（vs LUN 真差异）。来源分歧（投影 Tier B vs story Tier A）裁决前不裁"
            "NEW/MERGE——RS1 HRQ-RS1-03 证据分层判例同型"),
        "human_review_queued": "HRQ-RP1-01+HRQ-RP1-04", **P(0)})

    # C) PATCH 2 × v1
    tests.append({
        "program_id": "P-RP1-MGC-BAKE", "template_id": "PATCH_RESOURCE_FOLLOWING",
        "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
        "structural_diffs": body_diff(raw[("vs_patch_v1", "P-RP1-MGC-BAKE")]),
        "engine_raw_diffs": raw[("vs_patch_v1", "P-RP1-MGC-BAKE")],
        "reasoning": (
            "族域边界证据：zone=bottom 从 canonical 计算序的约束乘法步还原为**首道二元定位判定**"
            "（GATE_ZONE→EVAL_RESOURCE_PATCH→NORMALIZE：门先行 vs 评估先行=ORDER 真差异，顺序有"
            "业务意义——底栖取食定位先行；RS1 GRB/SMA vs PATCH 判例同型）且无过渡档（二元门非"
            "三档）。canonical 评估先行形在本成员证伪。处置提案=重指派 GATED_COVER_TIER_CHAIN"
            "（membership 直验语义 MC，见 membership 段）"),
        "human_review_queued": "HRQ-RP1-02", **P(0)})
    tests.append({
        "program_id": "P-RP1-ONS-BAKE", "template_id": "PATCH_RESOURCE_FOLLOWING",
        "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
        "structural_diffs": body_diff(raw[("vs_patch_v1", "P-RP1-ONS-BAKE")]),
        "engine_raw_diffs": raw[("vs_patch_v1", "P-RP1-ONS-BAKE")],
        "reasoning": (
            "族域边界证据：typed context 中间步（context_type=current 单绑定常量）还原后**展开并"
            "升档**——拆为流速档+石底档两步且均三档分级命中（流速档含过渡削减带=非二元门）+附着"
            "资源档=三档×3 四步链（vs canonical 三步带 typed context：OPERATOR/DEPENDENCY/"
            "BRANCH 真差异）。canonical 三步形在本成员证伪。处置提案=重指派 SOFT_TRIPLE_TIER_"
            "CHAIN（membership 直验语义 MC）。envelope 问项回答：PATCH 的 current 侧中间步=是，"
            "展开为三档分级命中；zone 侧（MGC）=否，还原为二元硬门——两成员不同形"),
        "human_review_queued": "HRQ-RP1-02", **P(0)})

    # D) membership 直验（F15）
    for r in engine["membership"]:
        pid, fam, role = r["program_id"], r["family"], r["role"]
        d = r["engine_structural_diff"]
        if not d:
            tests.append({
                "program_id": pid, "template_id": fam,
                "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
                "structural_diffs": [], "engine_raw_diffs": [], "role": role,
                "reasoning": "canonical 源自测（engine 零差异；STATE_GATED 物化先例——canonical "
                             "即源成员冻结体）", **P(0)})
            continue
        note, axis, reason = None, None, None
        if pid == "P-RP1-EEL-BAKE":
            reason = ("悬置（vs LUN v2 冻结体）：BUILD_ACCESSIBLE_SET 缺失（投影层缺口）+族硬门"
                      "guard 字面（family_surface_access vs surface_access_available——[需核对]"
                      "标记）+因子序方向级 [需正文]。Tier A story 证据支持 BUILD 存在则并入 v2；"
                      "证据分层裁决 HRQ-RP1-01/04")
            tests.append({
                "program_id": pid, "template_id": fam,
                "verdict": "AMBIGUOUS_NEEDS_EXPANSION", "same": False, "param_only": False,
                "structural_diffs": body_diff(d), "engine_raw_diffs": d, "role": role,
                "reasoning": reason, "human_review_queued": "HRQ-RP1-01+HRQ-RP1-04", **P(0)})
            continue
        if fam == "PLAIN_SHAPE_DUAL_SLOT__PLAIN_PROPOSAL":
            axis = ("factor_set(typed 2–6 槽：CHB 4 槽/WAL·MDF 2 槽——HRQ-B1-04 先例)+"
                    "factor_type(typed 槽名/槽值字面)+slot_tiering(IF3_SLOT_VALUE)")
            reason = ("F15 直验 vs RS1 C8 提案载体（TAI 冻结体）：骨架同构（槽值三档×N+COMBINE，"
                      "槽间 unordered 契约维持，无门无 early return）。engine raw=槽 arity"
                      "（DEPENDENCY，axis 内）/槽名与 guard 字面（OPERATOR/BRANCH——factor_type "
                      "字面，B0 判例）/PREMISE（F02 不计 body）。与 RS1 14 例同簇——槽内三档=slot_"
                      "tiering extension 轨（HRQ-RS1-03），语义层簇内 MC")
        elif fam == "GATED_COVER_TIER_CHAIN":
            axis = ("gate_axis(typed: bottom_zone——AST/SNS 同值第 3 实例)+"
                    "factor_type(typed: resource_patch 评估器字面)")
            reason = ("F15 直验 vs GATED_COVER canonical（FGA 冻结体）：骨架同构（二元存在门→"
                      "单档三档分级命中→NORMALIZE；deps 位形全同——engine 无 DEPENDENCY diff）。"
                      "engine raw=门轴与档位 op/guard 字面（BRANCH/OPERATOR=gate_axis+factor_type "
                      "值差异，GUARD anchor 判例同型；伏击门 9 例先例）+PREMISE（F02 不计）。"
                      "MGC 重指派提案：门先行形与 AST/SNS 同构")
        elif fam == "SOFT_TRIPLE_TIER_CHAIN":
            axis = ("tier1_axis(typed: current_flow——vs BSK layer_tier 轴值)+"
                    "substrate_tier_axis(typed)+factor_type(typed)")
            reason = ("F15 直验 vs SOFT_TRIPLE canonical（BSK 冻结体）：骨架同构（三档×3+三值积"
                      "归一化；deps 位形全同——engine 无 DEPENDENCY diff；首步均无二元门）。"
                      "engine raw=op/guard 字面（BRANCH/OPERATOR——GATE_CURRENT 为文件原标签但"
                      "分支语义=三档分级命中含过渡削减带，APPLY_CURRENT_CONTEXT 顺序还原形；"
                      "typed context 槽命名差异=B1 判例）+PREMISE（F02 不计）。ONS 重指派提案："
                      "族 1→2 成员（跨科独立重复：BSK 吸口形 vs ONS 急流刮食形）——单成员 "
                      "PROVISIONAL 升格候选")
        tests.append({
            "program_id": pid, "template_id": fam,
            "verdict": "MERGE_CONFIDENT", "same": True, "param_only": False,
            "structural_diffs": [], "engine_raw_diffs": d, "role": role,
            "proposed_parameter_axis": axis,
            "reasoning": reason, **P(0)})

    # E) 边界证据（11）
    BOUND = {
        ("P-RP1-OSC-BAKE", "vs_HARD_GATED_V2"):
            "OSC（单门+EXIT 档因子集+COMBINE）vs LUN v2（BUILD+双门+EXIT 档因子集）：门数（1 vs 2）"
            "与 BUILD 前置=结构元素差异非 typed 轴（B0 HRQ-03 判例：前置 hard gate 不得 MERGE）——"
            "extend-vs-split 复杂度对比入 HRQ-RP1-02，worker 裁 NEW 单成员候选（极值门≠水面可达"
            "生存门，门语义轴不同且门数不可参数化）",
        ("P-RP1-OSC-BAKE", "vs_GATED_COVER"):
            "EXIT 档因子集+COMBINE（多槽合并）vs 单档+NORMALIZE——COMBINE/槽数真差异（RS1 GATED_"
            "COVER vs HARD_GATED 边界判例同型）",
        ("P-RP1-OSC-BAKE", "vs_C8_CARRIER"):
            "前置门+槽 EXIT 语义（排除档=EARLY_RETURN）vs 无门+槽值出局（excluded=槽值仍进 "
            "COMBINE）——GATE+branch kind 真差异（slot_tiering 轨域边界维持：槽值出局=PLAIN 族域"
            "判据，RS1 C8 判例原文）",
        ("P-RP1-BRT-BAKE", "vs_GATED_COVER"):
            "门+双槽+COMBINE 无归一化 vs 门+单档+NORMALIZE——第二槽/COMBINE vs NORMALIZE/RETURN "
            "拓扑真差异",
        ("P-RP1-BRT-BAKE", "vs_C8_CARRIER"):
            "patch 存在门+槽1 EXIT 档 vs 无门+槽值档——GATE 真差异+槽出局语义混合（EXIT+槽值）",
        ("P-RP1-BRT-BAKE", "vs_OSC_SOURCE"):
            "两新候选互记：BRT（门+混合档双槽链式 COMBINE 无归一化）vs OSC（极值门+全 EXIT 档"
            "unordered 因子集+COMBINE）——门轴/槽语义组合/归一化缺失/槽序契约四重差异，各自独立"
            "立族",
        ("P-RP1-LUN-BAKE", "vs_GATED_COVER"):
            "HARD_GATED v2 方向边界：BUILD_ACCESSIBLE_SET+双硬门+多槽 COMBINE vs 结构存在门+单档+"
            "NORMALIZE——无 accessible-set 构建/多槽合并（RS1 12 例边界判例在 v2 形下续存）",
        ("P-RP1-MGC-BAKE", "vs_HARD_GATED_V1"):
            "反向边界：单资源链+NORMALIZE vs BUILD+硬门+多槽 COMBINE——单链无合并（B0 MGC vs "
            "HARD_GATED 判例在重跑形下续存）",
        ("P-RP1-MGC-BAKE", "vs_ZONE_SUBSTRATE"):
            "档位步数（1 vs 2）真差异：门+单档三步 vs 门+双档四步——链长=ORDER/OPERATOR 判据"
            "（C5c vs C5a 同型）；MGC 归 GATED_COVER（三步）非 ZONE_SUBSTRATE（四步）",
        ("P-RP1-ONS-BAKE", "vs_ZONE_SUBSTRATE"):
            "envelope 问项边界证据：首步三档分级命中（含过渡削减带）vs 首步二元 GATE 硬门——"
            "gate-kind（IF3_EXIT vs GATE）真差异，ONS 归 SOFT_TRIPLE（无二元门）非 ZONE_SUBSTRATE",
        ("P-RP1-ONS-BAKE", "vs_ZONE_DEPTH"):
            "链长（4 vs 5 步）真差异：无深度档步——C5c 独有步判据续存",
    }
    for r in engine["boundary"]:
        key = (r["program_id"], r["template"])
        tests.append({
            "program_id": r["program_id"],
            "template_id": r["template"].replace("vs_", "").replace("V1", "_V1").replace("V2", "_V2"),
            "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
            "structural_diffs": body_diff(r["engine_structural_diff"]),
            "engine_raw_diffs": r["engine_structural_diff"],
            "role": "boundary_evidence",
            "reasoning": "族域边界证据：" + BOUND[key],
            "human_review_queued": "HRQ-RP1-02", **P(0)})

    # F) 9 × CRR
    for r in engine["vs_crr"]:
        tests.append({
            "program_id": r["program_id"], "template_id": "CONSTRAINED_RELATIVE_REFUGE",
            "verdict": "NEW_TEMPLATE_CANDIDATE", "same": False, "param_only": False,
            "structural_diffs": body_diff(r["engine_structural_diff"]),
            "engine_raw_diffs": r["engine_structural_diff"],
            "reasoning": ("CRR non-match 续存（重跑链形仍无 RelativeRank(reference_set=FeasibleSet) "
                          "判别结构）。registry 决定：同物种原程序 B0-B2 已登记 CRR known_non_matches"
                          "（MGC/LUN/OSC/EEL/CHB=B0，BRT/ONS=B1，WAL/MDF=B2），重跑程序不重复追加"
                          "名单（HRQ-RS1-04 判例延续；HRQ-RP1-04 记档）"),
            "human_review_queued": "HRQ-RP1-04", **P(0)})
    write_jsonl("merge_tests.jsonl", tests)

    # ---------------- stories.jsonl ----------------
    stories = []
    for pid, p in progs.items():
        code = p["species_id"]
        fam = FAM[code][0]
        stories.append({
            "story_id": p["story_id"],
            "source_story": ("CENSUS-RERUN 单元｜" + RERUN_OF[code] +
                             " 重跑｜输入=" + p["source_evidence_ids"][0]),
            "frozen_patterns": ["work-standards-§5.1", "work-standards-§5.4"],
            "surfaces": {"Bake": {
                "consequence": "NEW_PROGRAM_CANDIDATE", "program_ids": [pid],
                "reason": "顺序还原链形重跑（" + fam + "）"}},
            "consequence": "NEW_PROGRAM_CANDIDATE",
            "provenance": {"batch": B}})
    write_jsonl("stories.jsonl", stories)
    for name in ("absence_claims.jsonl", "coverage.jsonl", "program_revisions.jsonl",
                 "resolver_tests.jsonl"):
        (BATCH / name).write_text("", encoding="utf-8")

    # ---------------- human_review_queue.jsonl ----------------
    write_jsonl("human_review_queue.jsonl", [
        {"id": "HRQ-RP1-01",
         "topic": "HARD_GATED_FACTOR_COMBINE canonical v2 升级提案 + EEL 证据分层",
         "facts": ("2/2 成员顺序还原重跑 vs v1 canonical（BUILD→GATE→平铺因子→COMBINE）body 结构"
                   "差异：LUN=BUILD+双硬门（水面可达+极值水温）+EXIT 档因子×4（时段槽新增）+"
                   "COMBINE；EEL=双门+EXIT 档因子×4 但 BUILD_ACCESSIBLE_SET 在 §2.4 投影未承载"
                   "（文件自声明 [需核对：硬门字段名]，Tier A story 证据 B0 原体含 BUILD）"),
         "decision_needed": ("①canonical v2 升级 vs 新族：worker 倾向升级（族定义『硬门前置+因子"
                             "组合』保持，差异=门数/档位/槽 arity 轴内或族定义内新增，无族域违例——"
                             "与 SINGLE v2-or-SPLIT（HRQ-RS1-01）同构但方向相反）；②EEL 证据分层"
                             "裁决：story 层（BUILD 存在）补回则直验并入 v2，投影层缺口为真则 EEL "
                             "为双门无 BUILD 变体（vs LUN 真差异）——裁决路由到表达文件侧修复"
                             "（[需核对] 字段回写）；③v2 批准后 hard_constraint_gate 轴声明更新"
                             "（surface_access|extreme_temp_band 门序列）"),
         "provenance": {"batch": B}},
        {"id": "HRQ-RP1-02",
         "topic": "2 新候选族立族 + MGC/ONS 重指派 + PATCH 族空置提案",
         "facts": ("①EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN（OSC——原 PLAIN 第 1 批成员出族："
                   "极值门+EXIT 档 unordered 因子集+COMBINE；vs HARD_GATED=门数/BUILD 差异，vs "
                   "GATED_COVER=COMBINE/NORMALIZE 差异，vs C8=门+EXIT 语义差异——边界证据 11 条"
                   "在案）；②PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN（BRT——原 PLAIN 第 3 成员出族："
                   "patch 门+槽1 EXIT 档+槽2 槽值档+COMBINE 无归一化；TAR-05 rank fact 退化条款"
                   "携带）；③MGC→GATED_COVER_TIER_CHAIN（gate_axis=bottom_zone 第 3 实例，语义 "
                   "MC deps 全同）；④ONS→SOFT_TRIPLE_TIER_CHAIN（三档×3+积归一 deps 全同，族 "
                   "1→2 成员跨科独立重复——单成员 PROVISIONAL 升格候选）；⑤PATCH 族 2/2 成员对 "
                   "canonical 证伪（MGC 门先行 ORDER / ONS context 展开升档）——重指派批准后"
                   "族空置"),
         "decision_needed": ("①两新族立族批准（各含 vs 邻族的 extend-vs-split 复杂度对比——worker "
                             "裁 NEW：门数/BUILD/归一化缺失=结构元素非 typed 轴）；②MGC/ONS 重指派"
                             "与 SOFT_TRIPLE 升格批准；③PATCH 族空置处置：撤销 or 保留为 P06 压缩"
                             "候选载体（HRQ-04/HRQ-B1-02 PENDING 联动——P06 压回 P02 问题时本族"
                             "canonical 已证伪，需先落定重指派）；④单成员 PROVISIONAL 双族（OSC/"
                             "BRT）——B4 判例延续"),
         "provenance": {"batch": B}},
        {"id": "HRQ-RP1-03",
         "topic": "PLAIN 原始 5 成员重跑：slot_tiering 轨并入 + canonical v1 证伪 + OSC/BRT 出族",
         "facts": ("CHB（4 槽）/WAL（2 槽）/MDF（2 槽）受限还原=槽值三档+COMBINE（与 RS1 C8 14 例"
                   "同形，slot_tiering 唯一真差异）；本批 3 例为 PLAIN 原始成员——census story "
                   "证据=多因子 PLAIN 与表达投影同向（无 RS1 14 例的来源分歧）；OSC/BRT 出族"
                   "（HRQ-RP1-02）。PLAIN v1 平铺 canonical 经原始 5 成员全体重跑证伪（0 匹配）——"
                   "族形状问题与 SINGLE v1 同型（HRQ-RS1-01 判例）"),
         "decision_needed": ("①slot_tiering 轨并入 HRQ-RS1-03 联合裁决：PLAIN canonical v2"
                             "（slot_tiering=IF3_SLOT_VALUE）批准后 3 例以原始成员身份回归（RS1 "
                             "14 例的证据分层问题独立裁决）；②OSC/BRT 出族批准（联动 HRQ-RP1-02）；"
                             "③名义计数：PLAIN 5→3+挂账 14（RS1）+本批 3=过渡双列不删，批准后"
                             "纯重指派"),
         "provenance": {"batch": B}},
        {"id": "HRQ-RP1-04",
         "topic": "重跑输入层缺陷与治理追加（RS1 HRQ-RS1-04 谱系）",
         "facts": ("①EEL §2.4 投影缺口：族硬门字段名 [需核对]（HRQ-02 谱系）+BUILD_ACCESSIBLE_"
                   "SET 未承载（census B0 原体有）——投影层自声明缺陷，影响 HRQ-RP1-01 裁决；"
                   "②guarding 目录 3 文件的 Bake 面在 §2.3/§2.4（非 §2.2——§2.2 为 Guarding 面），"
                   "输入定位约定记档；③ONS confidence LOW（行为链 Evidence Open）+P06 压缩候选"
                   "联动原样（HRQ-04/HRQ-B1-02 PENDING）；④CRR non-match 不重复登记判例延续"
                   "（9 例 engine 证据留档本批 merge_tests，registry 名单不追加）"),
         "decision_needed": ("输入层缺陷修复路由：EEL [需核对] 字段回写机制（Story 正文到达后校准，"
                             "同 RS1 档位校准回写机制议题）；guarding 目录 §2.3/§2.4 输入定位约定"
                             "纳入重跑范式文档"),
         "provenance": {"batch": B}}])

    # ---------------- manifest.yaml ----------------
    manifest = """batch_id: CENSUS-RERUN-PLAIN-001
role: FCF-CENSUS-WORKER
status: INDEPENDENT_REVIEW_REQUIRED
trigger: envelope CENSUS-RERUN-PLAIN-001（RS1 同构：SINGLE 重跑后 PLAIN/HARD_GATED/PATCH
  自有成员的顺序还原复检——B 系列 FIX 已触及全库文件）
scope:
  families: PLAIN_FACTOR_COMBINE（原始 5）+ HARD_GATED_FACTOR_COMBINE（2）+ PATCH_RESOURCE_FOLLOWING（2）
  rerun_with_input: 9/9（B0:5 B1:2 B2:2）
  rerun_input_unavailable: 0（absence_claims 空）
  input_layer: 顺序还原后 B 系列表达文件 §2.2（migration/normal/grazing/patch）与
    §2.3/§2.4 NormalFeeding 面（guarding——目录约定记 HRQ-RP1-04）
  input_dirs: 6（grazing/migration/normal/patch/guarding[Bake 在 §2.3/2.4]/——
    envelope ARTIFACT_URL 指全量顺序还原表达文件，成员清单从批档台账导出 RS1 判例④）
execution_mode: B3-F-0（fresh spawn 单轮；program_revisions 空）
blind_discipline:
  blind_programs_frozen_at: "2026-09-11T05:25:21Z"   # 终冻（本地 13:25:21+0800；文件系统精确时刻）
  freeze_history: "两次冻结：05:24:07Z 首冻 → 05:25:21Z 终冻。间隔内仅做 IR deps 忠实度修正
    （档位步/因子步读原始事实 deps=()——RS1 C3 惯例 vs HARD_GATED 因子集约定区分），依据=文件
    正文读取行重读，registry 全程未开（05:25:21Z 前零 registry 读取），无判同信息流入"
  n_programs: 9
  registry_opened_at: ">=2026-09-11T05:26:00Z（冻结后读取 v7；opened_at 为声明性下界，
    权威锚=blind 文件 mtime 05:25:21Z 先于 registry Read）"
  post_registry_mutations: 0
  bias_declaration: |
    事前暴露：三族 v1 canonical 形在角色记忆、B0 批档（run_merge_tests.py CANONICALS——
    流程范式恢复时读取，与 RS1 同源）与 RS1 批档/报告中已知；RS1 9 新族（GATED_COVER/
    SOFT_TRIPLE 等）的存在与 canonical 源成员亦经 RS1 report（流程范式）已知——本批骨架
    不从任何 canonical 反推，全部 9 条为各文件伪脚本的机械 IR 转写（文件自身声明与
    canonical 的分歧并要求 census 侧重跑裁决——work standards §5.4）。盲重建顺序：读 9 份
    输入 → 转写冻结 → 开 registry v7 → 判同。重跑语义：输入为表达文件（非 Story DB
    快照），与 B0-B4 批的 Story 输入层不同——envelope 明示授权（ARTIFACT_URL=顺序还原
    后表达文件）。
order_discipline: 判断顺序从文件伪脚本正文推导（§5.1）：PLAIN 4 例=受限还原（槽间 unordered
  族契约维持不发明链序）；HARD_GATED/OSC=门先行 EARLY_RETURN 链；BRT=门+槽序链；MGC=门
  先行二元；ONS=行为链四环原序；分级命中全部展开为 if/elif/else 分支（IF3_EXIT/IF3_SLOT_
  VALUE 区分出局语义）非单一布尔——2026-09-11 用户新标准
verdict_counts:
  merge_confident: 8          # 语义层（3 canonical 源自测+P1 三成员 vs TAI 载体+MGC/ONS 直验）
  extension_candidate: 3      # CHB/WAL/MDF × PLAIN v1（slot_tiering 轨并入 HRQ-RS1-03）
  new_template_candidate_families: 2   # distinct 新候选族（OSC/BRT 形）
  ambiguous: 2                # EEL × {HARD_GATED v1, v2}——证据分层（BUILD 投影缺口）
deltas:
  dL_group: 0
  dL_bake: 2                  # EXTREME_TEMP_GATED_TIERED_COMBINE + PATCH_GATED_DUAL_SLOT_COMBINE（candidate 级）
  dL_response: 0
  dL_quality: 0
registry: v7 -> v8（PLAIN/HARD_GATED/PATCH 三族重跑注记 + HARD_GATED v2 提案 + 2 新候选族 +
  GATED_COVER/SOFT_TRIPLE 重指派挂账；名义 162 不变——重指派非新增）
"""
    (BATCH / "manifest.yaml").write_text(manifest, encoding="utf-8")

    # ---------------- discovery curve ----------------
    row = "CENSUS-RERUN-PLAIN-001,9,9,8,3,2,2,0,2,0,0,0,0,0\n"
    txt = CURVE.read_text(encoding="utf-8")
    if not txt.endswith("\n"):
        txt += "\n"
    if "CENSUS-RERUN-PLAIN-001" not in txt:  # 幂等重入
        CURVE.write_text(txt + row, encoding="utf-8")

    # ---------------- registry v7 -> v8 ----------------
    reg = REG.read_text(encoding="utf-8")
    assert reg.count("version: 7\n") == 1
    reg = reg.replace("version: 7\n", "version: 8\n", 1)
    reg = reg.replace(
        "mutation_provenance:\n",
        """mutation_provenance:
  batch: CENSUS-RERUN-PLAIN-001
  date: 2026-09-11
  previous_version: 7
  rerun_summary: "PLAIN/HARD_GATED/PATCH 三族自有成员顺序还原重跑（RS1 同构；9/9 有输入）：PLAIN 原始 5 → 3 例 slot_tiering 受限还原（并入 HRQ-RS1-03 轨；v1 平铺 canonical 经原始成员全体证伪）+OSC/BRT 出族候选；HARD_GATED 2 → canonical v2 提案（双硬门+EXIT 档因子集；LUN 源）+EEL AMBIGUOUS（BUILD 投影缺口证据分层）；PATCH 2 → canonical 评估先行证伪：MGC 门先行→GATED_COVER 重指派（gate_axis bottom_zone 第 3 实例）/ONS 三档×3→SOFT_TRIPLE 重指派（族 1→2，PROVISIONAL 升格候选）——族空置提案 pending；+2 新 Bake 候选族（EXTREME_TEMP_GATED_TIERED_COMBINE[OSC 单成员 PROV]/PATCH_GATED_DUAL_SLOT_COMBINE[BRT 单成员 PROV]）；名义 162 不变（重指派挂账 moved_pending_review）；dL_bake=+2；HRQ-RP1-01..04"
""", 1)
    # PLAIN：open_precedents 追加 + 原始成员重跑注记
    reg = reg.replace(
        "    open_precedents: [HRQ-07（因子槽间顺序 unordered 提案）, HRQ-03（gate 轴 extend-vs-split）, HRQ-B1-04（槽位数伸缩+rank 因子类型）, HRQ-RS1-03（slot_tiering 轴+14 重归族挂账）]\n",
        """    open_precedents: [HRQ-07（因子槽间顺序 unordered 提案）, HRQ-03（gate 轴 extend-vs-split）, HRQ-B1-04（槽位数伸缩+rank 因子类型）, HRQ-RS1-03（slot_tiering 轴+14 重归族挂账）, HRQ-RP1-03（原始 5 成员重跑：slot_tiering 轨并入+OSC/BRT 出族）]
    rerun_2026_09_11_original_members: "CENSUS-RERUN-PLAIN-001：原始 5 成员（OSC/CHB/BRT/WAL/MDF——P-RP1-*-BAKE）顺序还原重跑：3 例（CHB 4 槽/WAL 2 槽/MDF 2 槽）受限还原=槽值三档+COMBINE（与 RS1 C8 形同构，slot_tiering 唯一真差异；census story 证据=多因子 PLAIN 与表达投影同向——无 RS1 14 例来源分歧）→并入 HRQ-RS1-03 extension 轨（批前挂账）；OSC（极值门+EXIT 档因子集）与 BRT（patch 门+双槽混合档+COMBINE 无归一化）出族候选（HRQ-RP1-02）。PLAIN v1 平铺 canonical 经原始成员全体重跑证伪（0 匹配）——canonical v2（slot_tiering）为唯一存活读法 pending"
""", 1)
    # HARD_GATED：open_precedents 追加 + v2 提案注记
    reg = reg.replace(
        "    open_precedents: [HRQ-03（与 PLAIN 的 extend-vs-split）, HRQ-B4-01（guard_target_specificity 新轴+anchor pebble_mound 提案）]\n",
        """    open_precedents: [HRQ-03（与 PLAIN 的 extend-vs-split）, HRQ-B4-01（guard_target_specificity 新轴+anchor pebble_mound 提案）, HRQ-RP1-01（canonical v2 升级提案+EEL BUILD 证据分层）]
    rerun_2026_09_11_canonical_v2_proposal:
      batch: CENSUS-RERUN-PLAIN-001
      outcome: "2/2 成员顺序还原重跑 vs v1 canonical（BUILD→GATE→平铺因子→COMBINE）body 结构差异（第二道极值水温门+因子 EXIT 档位化+时段槽）——族定义（硬门前置+因子组合）保持；canonical v2 提案=源成员 P-RP1-LUN-BAKE 冻结体（BUILD→GATE_SURFACE_ACCESS→GATE_EXTREME_TEMP→EXIT 档因子×4 unordered→COMBINE_WEIGHTED）；EEL=AMBIGUOUS_NEEDS_EXPANSION（§2.4 投影未承载 census 原体 BUILD_ACCESSIBLE_SET+族硬门字段名 [需核对 HRQ-02]——Tier A story 证据支持 BUILD 存在则直验并入 v2）"
      review: HRQ-RP1-01
""", 1)
    # PATCH：重跑证伪注记（插在 provisional_note 前）
    reg = reg.replace(
        "    provisional_note: 双成员（湄公鲶成体 zone + 准白甲鱼 current）均 P06 域；PROVISIONAL 维持待 P06 压缩测试；context_type 轴（zone|current）待批；与 SINGLE 族的 optional_context 边界交 HRQ-B1-02；helper SubstrateResourcePatchEvaluator 同 PROVISIONAL\n",
        """    rerun_2026_09_11:
      batch: CENSUS-RERUN-PLAIN-001
      outcome: "2/2 成员 vs canonical 评估先行三步 body 证伪：MGC zone=bottom 还原为首道二元定位门（GATE_ZONE→EVAL_RESOURCE_PATCH→NORMALIZE=门先行）→GATED_COVER_TIER_CHAIN 重指派提案（gate_axis bottom_zone 第 3 实例，AST/SNS 同值；deps 位形全同语义 MC）；ONS current 侧展开为流速三档+石底档两步（三档×3 链无二元门——首档含过渡削减带）→SOFT_TRIPLE_TIER_CHAIN 重指派提案（族 1→2，单成员 PROVISIONAL 升格候选；deps 位形全同语义 MC）——重指派批准后本族空置（P06 压缩候选联动 HRQ-04/HRQ-B1-02 PENDING 不受影响，归并裁决一并处置）"
      review: HRQ-RP1-02
    provisional_note: 双成员（湄公鲶成体 zone + 准白甲鱼 current）均 P06 域；PROVISIONAL 维持待 P06 压缩测试；context_type 轴（zone|current）待批；与 SINGLE 族的 optional_context 边界交 HRQ-B1-02；helper SubstrateResourcePatchEvaluator 同 PROVISIONAL；RP1 重跑后两成员均重指派提案 pending（本注记为历史态，见 rerun_2026_09_11）
""", 1)
    # GATED_COVER：MGC 挂账成员
    reg = reg.replace(
        """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-GRB-BAKE, P-RS1-SMA-BAKE], note: "patch/扰动门 2 例（vs PATCH 族 ORDER 真差异——门先行 vs 评估先行；merge_tests 边界证据）"}
""",
        """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: [P-RS1-GRB-BAKE, P-RS1-SMA-BAKE], note: "patch/扰动门 2 例（vs PATCH 族 ORDER 真差异——门先行 vs 评估先行；merge_tests 边界证据）"}
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-MGC-BAKE, note: "重指派提案 pending HRQ-RP1-02：PATCH 族 canonical 源成员 MGC 顺序还原门先行形（GATE_ZONE→EVAL_RESOURCE_PATCH→NORMALIZE）；gate_axis=bottom_zone 第 3 实例（AST/SNS 同值）；engine raw=门/tier 字面（B/O/P），语义 MC——伏击门 9 例同型；批准前不计正式成员"}
""", 1)
    # SOFT_TRIPLE：ONS 挂账成员 + provisional_note 更新
    reg = reg.replace(
        """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BSK-BAKE, role: canonical_source}
""",
        """      - {batch: CENSUS-RERUN-SINGLE-001, program_id: P-RS1-BSK-BAKE, role: canonical_source}
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-ONS-BAKE, note: "重指派提案 pending HRQ-RP1-02：PATCH 族 ONS 顺序还原三档×3 链（流速档[含过渡削减带]/石底档/附着资源档+三值积归一化；deps 位形全同语义 MC——GATE_CURRENT 为文件原标签、分支语义=IF3 非二元门）；族 1→2 跨科独立重复（BSK 吸口形 vs ONS 急流刮食形）——单成员 PROVISIONAL 升格候选；批准前不计正式成员"}
""", 1)
    reg = reg.replace(
        "    provisional_note: 单成员 PROVISIONAL（Tier B CSV benthopelagic 软定位推导，硬定位与否 [需正文]——正文证实硬定位则并入 ZONE_SUBSTRATE 族）\n",
        "    provisional_note: 单成员 PROVISIONAL（Tier B CSV benthopelagic 软定位推导，硬定位与否 [需正文]——正文证实硬定位则并入 ZONE_SUBSTRATE 族）；RP1 后 2 成员候选（+ONS pending HRQ-RP1-02）——批准后升格\n", 1)
    # 2 个新族条目（文件末追加）
    new_templates = """
  - template_id: EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-PLAIN-001
      seeded: 2026-09-11
      review_queue: HRQ-RP1-02
      origin: PLAIN 原始成员 OSC 顺序还原出族（极值水温门从末位算术门还原为前置出局判定）；canonical=P-RP1-OSC-BAKE 冻结体
    canonical_program_body: |
      GATE_EXTREME_TEMP(极值水温硬门：末位算术门还原为前置出局——极值带=EARLY_RETURN)
      -> EVAL 因子×4 unordered（静水/结构/猎物/时段——因子间顺序=证据未裁决 unordered 原样；
         各三档分级命中，排除档=EARLY_RETURN——EXIT 语义非 PLAIN 槽值出局）
      -> COMBINE_WEIGHTED(算子 OPERATOR UNDEFINED 待机制侧)
      -> SpatialDistributionWeight
    ir_pointer: batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE.EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN
    allowed_parameter_axes:
      - factor_set(typed, bounded 2–6 槽；时段槽=还原新增)
      - factor_tiering(EXIT 档语义族内固定——与 PLAIN slot_tiering 槽值语义为族域边界)
      - temp_gate_band(极值带边界=Profile 值域不冻结 [需正文])
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 双硬门链/生存门（HARD_GATED 域——门数与门语义=结构非轴内）, BUILD_ACCESSIBLE_SET（HARD_GATED 域）, 槽值出局语义（PLAIN slot_tiering 域）, 单档链+NORMALIZE（GATED_COVER 域）, 无门因子组合（PLAIN 域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-OSC-BAKE, role: canonical_source}
    known_non_matches:
      - {batch: CENSUS-RERUN-PLAIN-001, template_id: PLAIN_FACTOR_COMBINE, reason: "前置门+槽 EXIT 语义 vs 无门平铺/槽值——GATE+BRANCH 真差异（B0 HRQ-03 谱系）"}
      - {batch: CENSUS-RERUN-PLAIN-001, template_id: HARD_GATED_FACTOR_COMBINE, reason: "门数（1 vs 2）+无 BUILD——结构元素差异（v2 提案形下续存）"}
      - {batch: CENSUS-RERUN-PLAIN-001, template_id: GATED_COVER_TIER_CHAIN, reason: "EXIT 档因子集+COMBINE vs 单档+NORMALIZE"}
    provisional_note: 单成员 PROVISIONAL（guarding 目录 1 文件承载）；vs HARD_GATED extend-vs-split：门数/BUILD=结构元素非 typed 轴——worker 裁 NEW，复杂度对比入 merge_tests（HRQ-RP1-02）
  - template_id: PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN
    surface: Bake
    status: CANDIDATE
    provenance:
      batch: CENSUS-RERUN-PLAIN-001
      seeded: 2026-09-11
      review_queue: HRQ-RP1-02
      origin: PLAIN 第 3 成员 BRT 顺序还原出族（patch 存在性先行——无 patch 格无竞争占位对象）；canonical=P-RP1-BRT-BAKE 冻结体
    canonical_program_body: |
      GATE_PATCH_PRESENCE(patch 存在性门：无 patch=EARLY_RETURN——竞争占位对象存在性先行)
      -> EVAL_RESOURCE_PATCH(patch 强度档三档：近零档=出局 EARLY_RETURN)
      -> EVAL_RANK_POSITION_PREFERENCE(core-vs-edge 三档：优势=中心全额/中间=削减/次级=边缘带占位
         更低削减不清零——出局落槽值非 EARLY_RETURN)
      -> COMBINE_WEIGHTED(算子 OPERATOR UNDEFINED 待机制侧)
      -> SpatialDistributionWeight（无归一化步——族边界）
    ir_pointer: batches/CENSUS-RERUN-PLAIN-001/run_merge_tests.py::NEW_FAMILY_SOURCE.PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN
    allowed_parameter_axes:
      - gate_axis(patch_presence——与 GATED_COVER 门轴同源值)
      - slot2_type(typed: rank_position 个体属性调制因子|…；准入待批 HRQ-B1-04 联动)
      - factor_set(typed, bounded)
    forbidden_freedoms: [arbitrary policy, arbitrary steps, arbitrary expression, arbitrary next, 归一化步（GATED_COVER 域——COMBINE 终结=族边界）, 无门双槽（PLAIN 域）, 全 EXIT 档 unordered 因子集（EXTREME_TEMP_GATED 域）, 单档链（GATED_COVER 域）]
    helper_dependencies: []
    resolver_dependencies: []
    known_instances:
      - {batch: CENSUS-RERUN-PLAIN-001, program_id: P-RP1-BRT-BAKE, role: canonical_source}
    known_non_matches:
      - {batch: CENSUS-RERUN-PLAIN-001, template_id: PLAIN_FACTOR_COMBINE, reason: "门先行+槽 EXIT 档+无归一化 vs 无门槽值组合——GATE/BRANCH/RETURN 拓扑真差异"}
      - {batch: CENSUS-RERUN-PLAIN-001, template_id: GATED_COVER_TIER_CHAIN, reason: "第二槽+COMBINE vs 单档+NORMALIZE"}
      - {batch: CENSUS-RERUN-PLAIN-001, template_id: EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN, reason: "互记：门轴（patch 存在性 vs 极值带）+混合槽语义（EXIT+槽值）链式 vs 全 EXIT unordered 因子集+无归一化"}
    provisional_note: 单成员 PROVISIONAL + 退化条款（TAR-05 rank fact 未定则槽 2 退化常量→纯 patch 形族归属翻案——open_semantics 原样携带）
"""
    reg = reg.rstrip("\n") + "\n" + new_templates
    REG.write_text(reg, encoding="utf-8")

    print("outputs written:")
    print(f"  programs={len(programs)} stories={len(stories)} merge_tests={len(tests)}")
    from collections import Counter
    print("  verdicts:", dict(Counter(t["verdict"] for t in tests)))
    print("  registry: v8 written; curve row appended")


if __name__ == "__main__":
    main()
