# -*- coding: utf-8 -*-
"""CENSUS-RERUN-PLAIN-001 盲重建：PLAIN 5 + HARD_GATED 2 + PATCH 2 旧成员，
按顺序还原后表达文件 §2.2/§2.4（REP-ORDER-FIX-001..004）的 NormalFeeding
（Bake）伪脚本机械转写为程序骨架 IR。

盲纪律：
- 输入＝顺序还原后的 B 系列表达文件（envelope 冻结输入，非 Story DB）；
- 本脚本运行时 registry v7 尚未打开（registry_seen=false 全体）；
- 事前暴露声明（manifest bias_declaration）：三族 v1 canonical 形在角色记忆、
  B0 批档（run_merge_tests.py CANONICALS）与 RS1 批档（流程范式恢复）中已知
  ——骨架不从 canonical 反推，而是从各文件伪脚本逐字链形转写（文件自身声明
  与 canonical 的分歧并要求 census 侧重跑裁决——work standards §5.4）；
- 9/9 成员全部有重跑输入文件（无 absence）。

程序 ID 约定：P-RP1-<CODE>-BAKE；story ID：CENSUS-RERUN-PLAIN-001-<CODE>。
"""
import hashlib
import json
from pathlib import Path

BATCH = Path(__file__).parent
FA = "outputs/full_authoring"


def steps(*pairs):
    return [{"op": op, "deps": list(deps)} for op, deps in pairs]


IF3X = lambda g: {"kind": "IF3_EXIT", "guard": g}
IF3S = lambda g: {"kind": "IF3_SLOT_VALUE", "guard": g}
GATE = lambda g: {"kind": "GATE", "guard": g, "else": "RETURN_0_EARLY"}

# ---------------------------------------------------------------------------
# 链形簇定义（从 9 份 §2.2/§2.4 盲输入归纳；判同在冻结后进行）
# ---------------------------------------------------------------------------

CLUSTERS = {
    # P1 受限还原槽组合（PLAIN 族契约 unordered 槽间维持；槽内三档=出局槽值）
    "P1_PLAIN_SLOT_TIERED_COMBINE": dict(
        family_hint="PLAIN_FACTOR_COMBINE（slot_tiering extension 轨）",
        combine="WEIGHTED_UNDEFINED", ret="SpatialDistributionWeight",
        chain="受限顺序还原：槽间顺序按 PLAIN 族契约 unordered 不还原；每槽因子评估展开为三档分档槽（preferred=全额/tolerated=削减不清零/excluded=出局槽值非 EARLY_RETURN——槽无 gate 语义族域边界维持）；COMBINE_WEIGHTED（OPERATOR UNDEFINED 待机制侧）",
    ),
    # P2 双硬门+EXIT 档因子集（LUN：BUILD+水面可达门+极值门）
    "P2_HG_DOUBLEGATE_TIERED_FACTORS": dict(
        family_hint="HARD_GATED_FACTOR_COMBINE canonical v2 提案（LUN 源）",
        ops=steps(("BUILD_ACCESSIBLE_SET", ()),
                  ("GATE_SURFACE_ACCESS", (0,)),
                  ("GATE_EXTREME_TEMP", (0,)),
                  ("EVAL_HABITAT_FACTOR_TYPED", (1,)),
                  ("EVAL_HABITAT_FACTOR_TYPED", (1,)),
                  ("EVAL_RESOURCE_FACTOR_TYPED", (1,)),
                  ("EVAL_TIME_FACTOR_TYPED", (1,)),
                  ("COMBINE_WEIGHTED", (3, 4, 5, 6))),
        branches=[GATE("surface_access_available"), GATE("extreme_temp_band"),
                  IF3X("stillwater_factor_tier"), IF3X("structure_factor_tier"),
                  IF3X("prey_factor_tier"), IF3X("time_factor_tier")],
        combine="WEIGHTED_UNDEFINED", ret="SpatialDistributionWeight",
        chain="构建水域可访问集 → 水面可达硬门（专性气呼吸生存约束，不可达=EARLY_RETURN）→ 水温极值硬门（末位算术门还原为前置出局）→ 因子评价（静水/结构/猎物/时段，因子间顺序=族判例 unordered 原样；各三档分级命中，排除档=EARLY_RETURN）→ COMBINE_WEIGHTED（OPERATOR UNDEFINED 待机制侧）",
    ),
    # P3 双硬门+EXIT 档因子集（EEL：无 BUILD——投影层缺口，证据分层挂 HRQ）
    "P3_HG_DOUBLEGATE_NOBUILD": dict(
        family_hint="HARD_GATED_FACTOR_COMBINE v2 候选（BUILD 缺失证据分层）",
        ops=steps(("GATE_FAMILY_HARD_SURFACE_ACCESS", ()),
                  ("GATE_EXTREME_TEMP", ()),
                  ("EVAL_HABITAT_FACTOR_STRUCTURE", ()),
                  ("EVAL_HABITAT_FACTOR_STILLWATER", ()),
                  ("EVAL_RESOURCE_FACTOR_PREY", ()),
                  ("EVAL_TIME_FACTOR_TYPED", ()),
                  ("COMBINE_WEIGHTED", (2, 3, 4, 5))),
        branches=[GATE("family_surface_access"), GATE("extreme_temp_band"),
                  IF3X("structure_factor_tier"), IF3X("stillwater_factor_tier"),
                  IF3X("prey_factor_tier"), IF3X("time_factor_tier")],
        combine="WEIGHTED_UNDEFINED", ret="SpatialDistributionWeight",
        chain="族硬门（水面可达型硬约束——原平铺脚本漏写族硬门步，本批还原为第一出局条件；字段名 [需核对 HRQ-02]）→ 水温极值硬门 → 因子评价（结构/静水/猎物/时段，顺序 [需正文] 方向级——静水沼泽掩体结构优先；各三档分级命中，排除档=EARLY_RETURN）→ COMBINE_WEIGHTED（OPERATOR UNDEFINED）。投影层缺口：census P-EEL-BAKE 原体含 BUILD_ACCESSIBLE_SET，本 §2.4 未承载——证据分层 HRQ",
    ),
    # P4 极值门+EXIT 档因子集（OSC：单门无双生存门无 BUILD）
    "P4_TEMPGATE_TIERED_FACTORS": dict(
        family_hint="EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN 新候选",
        ops=steps(("GATE_EXTREME_TEMP", ()),
                  ("EVAL_HABITAT_FACTOR_STILLWATER", ()),
                  ("EVAL_HABITAT_FACTOR_STRUCTURE", ()),
                  ("EVAL_RESOURCE_FACTOR_PREY", ()),
                  ("EVAL_TIME_FACTOR_TYPED", ()),
                  ("COMBINE_WEIGHTED", (1, 2, 3, 4))),
        branches=[GATE("extreme_temp_band"),
                  IF3X("stillwater_factor_tier"), IF3X("structure_factor_tier"),
                  IF3X("prey_factor_tier"), IF3X("time_factor_tier")],
        combine="WEIGHTED_UNDEFINED", ret="SpatialDistributionWeight",
        chain="水温极值硬门（末位算术门还原为前置出局判定）→ 因子评价（静水/结构/猎物/时段，因子间顺序=census open_semantics unordered 原样；各三档分级命中，排除档=EARLY_RETURN——与 PLAIN 槽值出局语义不同）→ COMBINE_WEIGHTED（OPERATOR UNDEFINED 待机制侧）",
    ),
    # P5 patch 存在门+双槽混合档+组合（BRT：无归一化）
    "P5_PATCHGATE_DUALSLOT_COMBINE": dict(
        family_hint="PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN 新候选",
        ops=steps(("GATE_PATCH_PRESENCE", ()),
                  ("EVAL_RESOURCE_PATCH", ()),
                  ("EVAL_RANK_POSITION_PREFERENCE", ()),
                  ("COMBINE_WEIGHTED", (1, 2))),
        branches=[GATE("patch_presence"), IF3X("patch_intensity_tier"),
                  IF3S("rank_position_tier")],
        combine="WEIGHTED_UNDEFINED", ret="SpatialDistributionWeight",
        chain="patch 存在性门（无 patch 格无竞争占位对象，存在性先行；excluded 槽=EARLY_RETURN）→ patch 强度档三档（近零档=出局 EARLY_RETURN）→ rank 位置档三档（core-vs-edge：优势=中心全额/中间=削减/次级=边缘带占位更低削减不清零——出局落槽值非 EARLY_RETURN）→ COMBINE_WEIGHTED（OPERATOR UNDEFINED 待机制侧）；无归一化步——族边界（vs GATED_COVER NORMALIZE）",
    ),
    # P6 底带门+资源档+归一化（MGC：zone 侧还原为二元硬门先行）
    "P6_ZONEGATE_PATCH_CHAIN": dict(
        family_hint="GATED_COVER_TIER_CHAIN（gate_axis=bottom_zone）",
        ops=steps(("GATE_ZONE", ()),
                  ("EVAL_RESOURCE_PATCH", ()),
                  ("NORMALIZE_WEIGHT", (1,))),
        branches=[GATE("bottom_zone_present"), IF3X("resource_patch_tier")],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="底带定位硬门（census op CONSTRAIN_ZONE 的顺序还原形：zone=bottom 实例常量；非底带=EARLY_RETURN——底栖取食定位先行，无过渡档=二元门）→ 底质资源档三档（碎屑/藻；排除档=出局 EARLY_RETURN）→ NORMALIZE_WEIGHT（族常量）",
    ),
    # P7 三档×3+积归一（ONS：current 侧展开为三档并拆出石底档，无二元门）
    "P7_TRIPLE_TIER_CHAIN": dict(
        family_hint="SOFT_TRIPLE_TIER_CHAIN（typed 槽轴值 current/substrate/resource）",
        ops=steps(("GATE_CURRENT", ()),
                  ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("EVAL_RESOURCE_PATCH", ()),
                  ("NORMALIZE_WEIGHT", (0, 1, 2))),
        branches=[IF3X("current_flow_tier"), IF3X("substrate_attach_tier"),
                  IF3X("attached_resource_tier")],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="流速档三档（GATE_CURRENT 为文件原标签但分支语义=三档分级命中非二元门：急流=进入/过渡=削减不清零/缓静=出局 EARLY_RETURN——census op APPLY_CURRENT_CONTEXT 的顺序还原形）→ 石底档三档（附着面可得性；软底无附着面=出局）→ 附着资源档三档（无附着资源=出局）→ NORMALIZE_WEIGHT（CurrentTier × SubstrateTier × SubstratePatchIntensity 三档积内归一化，族常量）",
    ),
}

# ---------------------------------------------------------------------------
# 成员表：(code, 原批, 原程序, 文件, FIX 批, 簇, 物种, premises,
#          P1 槽定义[P1 专用], sketch 补充注记)
# ---------------------------------------------------------------------------
P_AXIS = "上游 lifecycle/阶段 premise（配置级切换因子集，body 无阶段分支）"

MEMBERS = [
    # --- PLAIN 5 ---
    ("OSC", "B0", "P-OSC-BAKE", "guarding/species/oscar.md", "002",
     "P4_TEMPGATE_TIERED_FACTORS", "Oscar（地图鱼）",
     ["护巢期 anchor 因子激活且权重主导 = condition premise（P04/P05 判例配置级因子切换，body 不设分支——分布收缩至巢/仔区在配置层完成）"],
     None,
     "原 PLAIN 第 1 批成员（B0 阴性对照 4 槽）；guarding 目录 NormalFeeding 面 §2.4 顺序还原：极值水温门从末位算术门还原为前置出局判定；因子槽 4（静水/结构/猎物/时段——时段槽为还原新增），排除档=EARLY_RETURN 非 PLAIN 槽值出局——两处族域边界位移"),
    ("CHB", "B0", "P-CHB-BAKE", "migration/species/common_chub.md", "003",
     "P1_PLAIN_SLOT_TIERED_COMBINE", "Common Chub（欧鲢）",
     ["spawn_run = " + P_AXIS + "（INACTIVE=常态 4 槽因子集 / ACTIVE=快水+砾石繁殖因子集 {fast_water, gravel} 冻结常量）",
      "size_class = 体型 premise（大个体鱼食权重升——落槽 3 猎物谱参数非结构）"],
     [("EVAL_HABITAT_FACTOR_FLOW", "flow_tier"),
      ("EVAL_HABITAT_FACTOR_POOL_STRUCTURE", "pool_structure_tier"),
      ("EVAL_RESOURCE_FACTOR_PREY", "prey_tier"),
      ("EVAL_RESOURCE_FACTOR_SURFACE_FILM", "surface_film_tier")],
     "族早期成员 4 槽（B0 与 P-OSC-BAKE factor_set 轴内直验同构阴性对照）；§2.2 受限还原：槽间 unordered 契约维持、槽内三档=出局槽值"),
    ("BRT", "B1", "P-B1-BRT-BAKE", "patch/species/brown_trout_position.md", "001",
     "P5_PATCHGATE_DUALSLOT_COMBINE", "Brown Trout（褐鳟·位置竞争）",
     ["rank premise = individual_rank 优势等级（上游个体 Condition/Relation fact——首个个体属性调制因子，具名 typed 因子准入待批 HRQ-B1-04；rank fact 产品持久写回未定 TAR-05）"],
     None,
     "原 PLAIN 第 3 成员（B1 patch+rank 2 因子）；§2.2 完全还原为门先行链：patch 存在性门（无 patch 格无竞争占位语义，存在性先行）→patch 强度档（出局=EARLY_RETURN）→rank 位置档（core-vs-edge，出局=槽值）→COMBINE；退化条款：TAR-05 未定则槽 2 退化常量→纯 patch 形族归属翻案（open_semantics 原样）"),
    ("WAL", "B2", "P-B2-WAL-BAKE", "migration/species/walleye_spawn.md", "003",
     "P1_PLAIN_SLOT_TIERED_COMBINE", "Walleye（玻璃梭鲈）",
     ["spawning_stage = 上游繁殖事实（配置级切换因子值域：繁殖浅滩期↔散后深水结构期——值域由 Profile 层定值，不建 body 分支）"],
     [("EVAL_HABITAT_FACTOR_TYPED", "temperature_tier"),
      ("EVAL_RESOURCE_FACTOR_TYPED", "prey_tier")],
     "原 PLAIN 第 4 成员（温度+食物 2 因子，B2 唯一 Tier A PLAIN 投影）；§2.2 受限还原同 CHB"),
    ("MDF", "B2", "P-B2-MDF-BAKE", "normal/species/mandarin_fish.md", "004",
     "P1_PLAIN_SLOT_TIERED_COMBINE", "Mandarin Fish（鳜鱼）",
     ["低温期（season）= 深度因子绑定的 premise（配置级偏好偏移，不建 body 分支）"],
     [("EVAL_TYPED_FIELD_OR_FACTOR", "structure_factor_tier"),
      ("EVAL_TYPED_FIELD_OR_FACTOR", "depth_cold_habitat_tier")],
     "原 PLAIN 第 5 成员（结构+深度 2 因子）；§2.2 受限还原同 CHB——追击型判断主体=猎物场+栖息双槽组间顺序判据注记"),
    # --- HARD_GATED 2 ---
    ("LUN", "B0", "P-LUN-BAKE-WET", "guarding/species/lungfish.md", "002",
     "P2_HG_DOUBLEGATE_TIERED_FACTORS", "South American Lungfish（南美肺鱼·WET 态）",
     ["水文季节 = lifecycle premise（本 Bake 仅 WET 态激活；AESTIVATION 态程序 B0 悬置 TAR-01——P05 判例配置级切换）"],
     None,
     "HARD_GATED canonical 源成员重跑；§2.4 顺序还原：硬门前置判断序形态明示+第二道极值水温门（末位算术门还原为前置出局）+因子槽 4（时段槽还原新增）+因子档位化（排除档=EARLY_RETURN）；因子间顺序 unordered 原样保留"),
    ("EEL", "B0", "P-EEL-BAKE", "guarding/species/electric_eel.md", "002",
     "P3_HG_DOUBLEGATE_NOBUILD", "Electric Eel（电鳗）",
     [],
     None,
     "HARD_GATED 第 2 成员重跑；§2.4 还原：族硬门（水面可达型）为原平铺脚本漏写、本批从配置表还原为第一出局条件（字段名 [需核对 HRQ-02]）+极值门+因子档位化；**投影层缺口：census 原体 BUILD_ACCESSIBLE_SET 在 §2.4 未承载——B0 story 证据（Tier A）与表达投影（Tier B）分歧，证据分层挂 HRQ**；因子序 [需正文] 方向级（静水沼泽掩体优先）"),
    # --- PATCH 2 ---
    ("MGC", "B0", "P-MGC-BAKE-ADULT", "grazing/species/mekong_giant_catfish.md", "001",
     "P6_ZONEGATE_PATCH_CHAIN", "Mekong Giant Catfish（湄公巨鲶·ADULT）",
     ["lifecycle premise：ADULT 绑定（幼体肉食期 Bake 无空间行为证据不建体 TAR-02；potamodromous 因子集随 premise 配置切换——CHB 先例，细节少知不展开）"],
     None,
     "PATCH canonical 源成员重跑；§2.2 顺序还原：zone=bottom 从 census canonical 计算序的约束乘法步（EVAL→CONSTRAIN→NORM）还原为**首道二元定位判定**（无过渡档）——门先行 vs 评估先行=ORDER 真差异；资源档三档（排除=出局）"),
    ("ONS", "B1", "P-B1-ONS-BAKE", "grazing/species/onychostoma.md", "001",
     "P7_TRIPLE_TIER_CHAIN", "Onychostoma simum（白甲鱼·急流刮食）",
     [],
     None,
     "PATCH 第 2 成员重跑；§2.2 顺序还原：行为链四环原序（急流—石底—附着—刮食）；census context 常量 fast_flow_stone 拆为流速档+石底档两步且**均展开为三档分级命中**（流速档含过渡削减带=非二元门）——三步带 typed context 链还原为三档×3 四步链；confidence LOW（行为链 Evidence Open）——P06 Compression Candidate 联动原样（HRQ-04/HRQ-B1-02 PENDING）"),
]


def build():
    out = []
    for (code, batch, orig, path, fix, ck, species, premises, p1_slots, note) in MEMBERS:
        c = CLUSTERS[ck]
        if ck == "P1_PLAIN_SLOT_TIERED_COMBINE":
            n = len(p1_slots)
            ops = steps(*[(op, ()) for op, _ in p1_slots] + [("COMBINE_WEIGHTED", tuple(range(n)))])
            branches = [IF3S(g) for _, g in p1_slots]
        else:
            ops = c["ops"]
            branches = c["branches"]
        sketch = (f"【顺序还原重跑盲体｜REP-ORDER-FIX-{fix}｜{orig} 重跑】"
                  f"判断链={c['chain']}。实例注记：{note}。链形转写自 {path} "
                  f"§2.2/§2.4 NormalFeeding（Bake）面（文件冻结输入，WORKING/"
                  f"NOT AUTHORITY；档位成员=Profile 值域不冻结 [需正文]，Story 正文"
                  f"到达后校准——顺序/档位差异本身=LogicTemplate 判据）。")
        body = {
            "program_id": f"P-RP1-{code}-BAKE",
            "story_id": f"CENSUS-RERUN-PLAIN-001-{code}",
            "species_id": code,
            "surface": "Bake",
            "incoming_premises": premises,
            "human_readable_sketch": sketch,
            "ordered_steps": ops,
            "branches": branches,
            "combine": c["combine"],
            "return_type": c["ret"],
            "instance_noise": {"species": species, "profile": None, "constants": {}},
            "helpers": [],
            "source_evidence_ids": [f"{FA}/{path}#REP-ORDER-FIX-{fix}"],
            "open_semantics": ["档位成员与阈值=Profile 值域不冻结 [需正文]",
                               "顺序还原=表达文件 §5.1 受限/完全还原推导（Tier B），Story 正文到达后校准"],
            "cluster_hint_blind": ck,  # 盲阶段自聚类注记（非 registry 信息）
            "rerun_of": orig,
            "registry_seen": False,
            "registry_seen_at_creation": False,
        }
        body["blind_hash"] = hashlib.sha256(
            json.dumps({k: body[k] for k in ("ordered_steps", "branches", "combine",
                                             "return_type", "incoming_premises")},
                       ensure_ascii=False, sort_keys=True).encode("utf-8")
        ).hexdigest()[:16]
        out.append(body)
    return out


if __name__ == "__main__":
    progs = build()
    assert len(progs) == 9, len(progs)
    codes = [p["species_id"] for p in progs]
    assert len(set(codes)) == 9
    (BATCH / "blind_programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in progs) + "\n",
        encoding="utf-8")
    from collections import Counter
    print("frozen:", len(progs), "programs")
    print(Counter(p["cluster_hint_blind"] for p in progs))
