# -*- coding: utf-8 -*-
"""CENSUS-B0 盲程序骨架生成器（盲纪律产物）。

本脚本在打开 template_registry.yaml 之前运行：从 FISH-R05 五条冻结 Story
（Story DB 只读快照）+ P01/P04/P05/P06 冻结语义 Pattern 独立重建每个
有程序意义的 Story×Surface 的 Minimal Program Sketch，冻结进
blind_programs.jsonl（内容 sha256 + registry_seen=false）。

盲纪律声明：此时 Worker 尚未读取本批 template_registry.yaml（初始化时对
v0 种子的暴露已记录于 role_memory，种子内容=Method R0 §6 方法合同本身）。

hash 算法：sha256(canonical_json(record minus blind_hash minus generated_at))[:16]
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent

STORY = {
    "MGC": "FISH-R05-湄公鲶-Ontogenetic-Feeding-Rebuild",
    "LUN": "FISH-R05-南美肺鱼-Aestivation-State-Switch",
    "OSC": "FISH-R05-地图鱼-Biparental-Guard-Quiet-Water-Ambush",
    "EEL": "FISH-R05-电鳗-Electrogenic-Remote-Prey-Control",
    "CHB": "FISH-R05-欧鲢-Size-Graded-Opportunism-Spawning-Run",
}
URL = {
    "MGC": "https://app.notion.com/p/3d7a4137d23681309e29fd03798c1214",
    "LUN": "https://app.notion.com/p/3d7a4137d23681f9b62bdd65f610ffb4",
    "OSC": "https://app.notion.com/p/3d7a4137d2368196abfff3130d97773c",
    "EEL": "https://app.notion.com/p/3d7a4137d23681c9a5a3dcc1c7ddd4fc",
    "CHB": "https://app.notion.com/p/3d7a4137d236817c8f4ee128d2269970",
}

def rec(program_id, story, surface, premises, sketch, steps, branches,
        combine, return_type, instance_noise, helpers=None, open_sem=None,
        confidence=None, scope_note=None):
    r = {
        "program_id": program_id,
        "story_id": STORY[story],
        "species_id": story,
        "surface": surface,
        "incoming_premises": premises,
        "human_readable_sketch": sketch,
        "ordered_steps": steps,
        "branches": branches,
        "combine": combine,
        "return_type": return_type,
        "instance_noise": instance_noise,
        "helpers": helpers or [],
        "source_evidence_ids": [URL[story]],
        "open_semantics": open_sem or [],
    }
    if confidence:
        r["confidence"] = confidence
    if scope_note:
        r["scope_note"] = scope_note
    return r

PROGRAMS = [
    # ---- 湄公鲶 ----
    rec(
        "P-MGC-BAKE-ADULT", "MGC", "Bake",
        premises=[
            "lifecycle_stage = JUVENILE | ADULT（体型/年龄 lifecycle trait，上游决定，缓慢单向发育）",
            "feeding_evaluator_binding = CARNIVORE | DETRIVORE_HERBIVORE（随 lifecycle_stage 由上游配置切换，非本面内分支）",
        ],
        sketch=(
            "成体：底部碎屑/藻资源 patch 强度场评估（typed substrate evaluator，P06 语义）"
            "→ 区域约束（底带）→ 归一化为空间权重。单资源链，无 hard gate、无相对排序。"
            "个体发生切换（幼肉食→成植食）是 premise 层配置切换：30–50cm 起齿/须退化为"
            "单调渐变、单向、同时刻单态，证据不支持并发双供给，故不在 Bake body 内设"
            "IF-juvenile 分支，也不构成 Group 路由程序。"
        ),
        steps=[
            {"op": "EVAL_RESOURCE_PATCH", "deps": []},
            {"op": "CONSTRAIN_ZONE", "deps": [0]},
            {"op": "NORMALIZE_WEIGHT", "deps": [1]},
        ],
        branches=[],
        combine="NONE_SINGLE_CHAIN",
        return_type="SpatialDistributionWeight",
        instance_noise={"species": "Mekong Giant Catfish",
                        "profile": "AdultDetritivore",
                        "constants": {"zone": "bottom", "resource": "detritus+algae"}},
        helpers=[{"name": "SubstrateResourcePatchEvaluator", "body_has_control_flow": False, "case_specific": False}],
        open_sem=[
            "幼体（肉食期）Bake 程序无空间行为证据，未建体（见 TAR-02）",
            "单资源链 vs 多因子组合的族归属由判同阶段裁决",
        ],
    ),
    rec(
        "P-MGC-RESP-FEEDING", "MGC", "Response",
        premises=["lifecycle_stage（决定 food evaluator 的类型绑定）"],
        sketch=(
            "离散目标 → 按 lifecycle stage 绑定的 typed food evaluator 评估"
            "（幼=肉食评估；成=植食/碎屑取向评估，饵与藻食偏好为参数）→ 决定响应。"
            "P01 TargetFeeding 的实例化，evaluator 类型随 premise 切换，body 单态。"
        ),
        steps=[
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "DECIDE_RESPONSE", "deps": [0]},
        ],
        branches=[],
        combine="NONE",
        return_type="Response(TargetFeeding)",
        instance_noise={"species": "Mekong Giant Catfish", "profile": None,
                        "constants": {"evaluator": "stage_bound"}},
    ),
    # ---- 南美肺鱼 ----
    rec(
        "P-LUN-BAKE-WET", "LUN", "Bake",
        premises=[
            "season_regime = WET | DRY（干湿由 world 水文状态上游决定，个体不同时双态）",
            "air_breathing = OBLIGATE（物种常量 fact：无水面通道不可存活）",
        ],
        sketch=(
            "湿态常态：构建水域可访问集 → 水面可达硬门（专性气呼吸的绝对约束，"
            "不可达即剔除，非相对排序）→ 静水偏好因子 / 塘体结构因子 / 猎物资源因子"
            "（吸吮捕食鱼虾螺蚌藻）→ 加权组合 → 空间权重。hard gate 前置 + 因子组合，"
            "无 FeasibleSet→RelativeRank 结构。"
        ),
        steps=[
            {"op": "BUILD_ACCESSIBLE_SET", "deps": []},
            {"op": "GATE_HARD_VIABILITY", "deps": [0]},
            {"op": "EVAL_HABITAT_FACTOR_STILLWATER", "deps": [1]},
            {"op": "EVAL_HABITAT_FACTOR_STRUCTURE", "deps": [1]},
            {"op": "EVAL_RESOURCE_FACTOR_PREY", "deps": [1]},
            {"op": "COMBINE_WEIGHTED", "deps": [2, 3, 4]},
        ],
        branches=[{"kind": "GATE", "guard": "surface_access_available", "else": "exclude_from_feasible"}],
        combine="WEIGHTED_FACTORS",
        return_type="SpatialDistributionWeight",
        instance_noise={"species": "South American Lungfish", "profile": "WetSeason",
                        "constants": {"hard_viability": "surface_access"}},
        open_sem=[
            "因子(2-4)间业务顺序未由冻结证据裁决；盲骨架按 SEQUENCE 记录，"
            "判同阶段提议族内按 unordered typed factor set 处理（需 review 批准）",
        ],
    ),
    rec(
        "P-LUN-BAKE-AESTIVATION", "LUN", "Bake",
        premises=[
            "season_regime = DRY（world 水文上游决定）",
            "burrow_anchor（钻泥 30–50cm 封泥留气孔，蛰伏行为产物，lifecycle-owned fact）",
            "metabolic_rate = SUPPRESSED（代谢下调参数）",
        ],
        sketch=(
            "干态蛰伏：分布退化为 burrow 单点 anchor，常态因子评估链整体空置"
            "（代谢下调抑制）。蛰伏态本身=world/lifecycle-owned state switch（premise），"
            "不是本面自有的判断程序。playable 性存疑：干季穴捕无渔业记录（S10=EO），"
            "产品是否引入 playable 蛰伏未定，本骨架仅作程序体形状记录。"
        ),
        steps=[
            {"op": "ANCHOR_TO_POINT", "deps": []},
            {"op": "SUPPRESS_FACTOR_EVALUATION", "deps": [0]},
        ],
        branches=[],
        combine="NONE_DEGENERATE",
        return_type="SpatialDistributionWeight",
        instance_noise={"species": "South American Lungfish", "profile": "Aestivation",
                        "constants": {"burrow_depth_cm": "30-50"}},
        open_sem=[
            "playable scope 未定（S10=EO）→ 结构裁决降级为 AMBIGUOUS，见 TARGETED_AUDIT_REQUEST TAR-01",
        ],
        confidence="LOW",
    ),
    rec(
        "P-LUN-RESP-FEEDING", "LUN", "Response",
        premises=["season_regime = WET（常态评估期；DRY 下响应由 premise 层 rate 参数抑制，无 body）"],
        sketch=(
            "离散目标 → 吸吮式 typed food evaluator（鱼虾螺蚌藻）→ 决定响应。"
            "P01 TargetFeeding 实例化。"
        ),
        steps=[
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "DECIDE_RESPONSE", "deps": [0]},
        ],
        branches=[],
        combine="NONE",
        return_type="Response(TargetFeeding)",
        instance_noise={"species": "South American Lungfish", "profile": None,
                        "constants": {"mouth_mode": "suck"}},
    ),
    rec(
        "P-LUN-RESP-GUARD", "LUN", "Response",
        premises=[
            "guard_state = MALE_NEST_GUARD（湿季巢穴+雄鱼守护并以血管化腹鳍供氧，persistent condition）",
            "nest_anchor（巢位置 relation object）",
        ],
        sketch=(
            "护巢期双路径：path A 食物路径（吸吮 typed food evaluator）与 path B 入侵者路径"
            "（对巢 anchor 的距离/威胁 typed evaluator）并行评估 → 双路径合并 → 决定响应"
            "（可出 TargetFeeding 或 RelationalConflict 通道）。guard 状态是 persistent "
            "condition premise（presentation 前已存在且持续，P04 语义），双路径并行评估与"
            "合并是 Response 自有程序。非护巢期该 body 不激活（单路径 P01 body 生效）。"
        ),
        steps=[
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "EVAL_TARGET_AS_INTRUDER_TYPED", "deps": []},
            {"op": "COMBINE_DUAL_PATH", "deps": [0, 1]},
            {"op": "DECIDE_RESPONSE", "deps": [2]},
        ],
        branches=[],
        combine="DUAL_PATH_MERGE",
        return_type="Response(TargetFeeding | RelationalConflict)",
        instance_noise={"species": "South American Lungfish", "profile": "MaleNestGuard",
                        "constants": {"oxygenation_organ": "vascularized_pelvic_fins"}},
        confidence="MEDIUM",
        open_sem=[
            "护巢行为实证；conflict 响应强度为 P04 语义映射（Bluegill/Smallmouth 先例），攻击性直接证据开放",
        ],
    ),
    # ---- 地图鱼 ----
    rec(
        "P-OSC-BAKE", "OSC", "Bake",
        premises=[
            "guard_state = NONE | BIPARENTAL_GUARD（清巢产卵→护卵 3–4 天→迁仔 6–7 天，persistent condition）",
            "nest_anchor | fry_anchor（guard 期 relation object：平坦石面 / 浅坑）",
        ],
        sketch=(
            "常态：静水偏好因子 / 泥沙底浅沟塘结构掩体因子 / 猎物资源因子（小鱼/螯虾/虫）"
            "→ 加权组合 → 空间权重。护巢期：anchor 邻近因子激活且权重主导（分布收缩至"
            "巢/仔区），按 P04/P05 判例作为 condition 配置级因子切换处理，body 不设分支。"
        ),
        steps=[
            {"op": "EVAL_HABITAT_FACTOR_STILLWATER", "deps": []},
            {"op": "EVAL_HABITAT_FACTOR_SUBSTRATE_STRUCTURE", "deps": []},
            {"op": "EVAL_RESOURCE_FACTOR_PREY", "deps": []},
            {"op": "EVAL_ANCHOR_PROXIMITY", "deps": []},
            {"op": "COMBINE_WEIGHTED", "deps": [0, 1, 2, 3]},
        ],
        branches=[],
        combine="WEIGHTED_FACTORS",
        return_type="SpatialDistributionWeight",
        instance_noise={"species": "Oscar", "profile": "QuietWaterAmbush",
                        "constants": {"substrate": "mud/sand", "guard_days_egg": "3-4", "guard_days_fry": "6-7"}},
        open_sem=[
            "anchor 因子激活按配置级处理（body 不分支）；若 review 判需 body 内 IF，本面结构结论需复核",
            "因子间顺序未由证据裁决（同 P-LUN-BAKE-WET 注记）",
        ],
    ),
    rec(
        "P-OSC-RESP-FEEDING", "OSC", "Response",
        premises=["guard_state = NONE（非护巢期 body）"],
        sketch=(
            "离散目标 → 伏击 typed food evaluator（静水/掩体 context 下评估小鱼/螯虾/虫/幼虫）"
            "→ 决定响应。P01 实例化（typed context = 掩体伏击）。"
        ),
        steps=[
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "DECIDE_RESPONSE", "deps": [0]},
        ],
        branches=[],
        combine="NONE",
        return_type="Response(TargetFeeding)",
        instance_noise={"species": "Oscar", "profile": None,
                        "constants": {"context": "quiet_water_cover"}},
    ),
    rec(
        "P-OSC-RESP-GUARD", "OSC", "Response",
        premises=[
            "guard_state = BIPARENTAL_GUARD（双亲护卵+迁仔，persistent condition，P04 语义）",
            "nest_anchor | fry_anchor（guard 期 relation object）",
        ],
        sketch=(
            "护巢期双路径：path A 食物路径（伏击 typed food evaluator）与 path B 入侵者路径"
            "（对卵/仔 anchor 的距离与威胁 typed evaluator）并行评估 → 双路径合并 → 决定响应"
            "（TargetFeeding 或 RelationalConflict）。双亲可同时执行（两个体同 body），"
            "不影响 body 结构。与 Bluegill/Smallmouth 护巢先例同构（P04 受理）。"
        ),
        steps=[
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "EVAL_TARGET_AS_INTRUDER_TYPED", "deps": []},
            {"op": "COMBINE_DUAL_PATH", "deps": [0, 1]},
            {"op": "DECIDE_RESPONSE", "deps": [2]},
        ],
        branches=[],
        combine="DUAL_PATH_MERGE",
        return_type="Response(TargetFeeding | RelationalConflict)",
        instance_noise={"species": "Oscar", "profile": "BiparentalGuard",
                        "constants": {}},
        confidence="HIGH",
    ),
    # ---- 电鳗（仅感知段） ----
    rec(
        "P-EEL-BAKE", "EEL", "Bake",
        premises=[
            "air_breathing = OBLIGATE（物种常量 fact）",
            "activity_phase = NOCTURNAL（condition fact）",
        ],
        sketch=(
            "泥底静水分布：构建可访问集 → 水面可达硬门（专性气呼吸）→ 静水偏好因子 / "
            "泥底结构因子 / 猎物资源因子（鱼及小型哺乳）→ 加权组合 → 空间权重。"
            "与肺鱼湿态同形：hard gate 前置 + 因子组合。"
        ),
        steps=[
            {"op": "BUILD_ACCESSIBLE_SET", "deps": []},
            {"op": "GATE_HARD_VIABILITY", "deps": [0]},
            {"op": "EVAL_HABITAT_FACTOR_STILLWATER", "deps": [1]},
            {"op": "EVAL_HABITAT_FACTOR_SUBSTRATE_STRUCTURE", "deps": [1]},
            {"op": "EVAL_RESOURCE_FACTOR_PREY", "deps": [1]},
            {"op": "COMBINE_WEIGHTED", "deps": [2, 3, 4]},
        ],
        branches=[{"kind": "GATE", "guard": "surface_access_available", "else": "exclude_from_feasible"}],
        combine="WEIGHTED_FACTORS",
        return_type="SpatialDistributionWeight",
        instance_noise={"species": "Electric Eel", "profile": "NocturnalFacultative",
                        "constants": {"substrate": "mud", "hard_viability": "surface_access"}},
        open_sem=["因子间顺序未由证据裁决（同 P-LUN-BAKE-WET 注记）"],
    ),
    rec(
        "P-EEL-RESP-SENSE", "EEL", "Response",
        premises=[
            "activity_phase = NOCTURNAL",
            "sensing_channel = ACTIVE_ELECTROLOCATION（低压 EOD ~10V 持续背景，物种常量；主动感官物理实现，非目标程序分支）",
        ],
        sketch=(
            "感知段（本批唯一授权段）：离散目标的暴露度评估 → typed 电场感知通道"
            "（电场扰动，active sensing 背景下目标的暴露/可达评估）+ 夜行弱光条件"
            "→ 决定响应。程序体上电感知是一个 typed evaluator 输入（P01 typed context"
            "通道家族的具名实例），主动发电场是持续背景行为，不构成对特定目标的程序分支。"
        ),
        steps=[
            {"op": "EVAL_TARGET_EXPOSURE_TYPED", "deps": []},
            {"op": "DECIDE_RESPONSE", "deps": [0]},
        ],
        branches=[],
        combine="NONE",
        return_type="Response(TargetFeeding)",
        instance_noise={"species": "Electric Eel", "profile": "Electrolocation",
                        "constants": {"eod_low_voltage": "~10V"}},
        scope_note=(
            "OUT_OF_SCOPE：攻击段（doublet→reveal→volley≈400pps→remote taser 冻结→攻击，"
            "FR3 冻结的 Attacker-Generated Opportunity New Pattern Candidate）与捕获边界"
            "（S11=EO）为 post-instantiation owner，按 envelope 限定不进本批 census。"
        ),
    ),
    # ---- 欧鲢（阴性对照） ----
    rec(
        "P-CHB-BAKE", "CHB", "Bake",
        premises=[
            "size_class = SMALL | LARGE（体型分级 trait，上游决定因子权重与 prey 谱）",
            "spawn_run = INACTIVE | ACTIVE（产卵洄游 lifecycle 状态，上游决定）",
        ],
        sketch=(
            "常态（barbel 带急流-深潭 mosaic）：流速因子 / 深潭结构因子 / 猎物资源因子"
            "（杂食宽谱，大个体鱼食权重升）/ 陆生猎物水面机会因子 → 加权组合 → 空间权重。"
            "产卵洄游期（spawn_run=ACTIVE）：因子集切换为快水/砾石繁殖因子（P05 判例："
            "洄游先改 Spatial/Condition 配置，配置级切换，body 不分支）。体型分级全部落"
            "在因子权重与 prey 谱参数，无结构差异。"
        ),
        steps=[
            {"op": "EVAL_HABITAT_FACTOR_FLOW", "deps": []},
            {"op": "EVAL_HABITAT_FACTOR_POOL_STRUCTURE", "deps": []},
            {"op": "EVAL_RESOURCE_FACTOR_PREY", "deps": []},
            {"op": "EVAL_RESOURCE_FACTOR_SURFACE_FILM", "deps": []},
            {"op": "COMBINE_WEIGHTED", "deps": [0, 1, 2, 3]},
        ],
        branches=[],
        combine="WEIGHTED_FACTORS",
        return_type="SpatialDistributionWeight",
        instance_noise={"species": "Common Chub", "profile": "BarbelRunOpportunist",
                        "constants": {"spawn_factors": ["fast_water", "gravel"]}},
        open_sem=[
            "spawn 因子集切换按 P05 配置级处理；若 review 判需 body 内 IF，本面结构结论需复核",
            "因子间顺序未由证据裁决（同上注记）",
        ],
    ),
    rec(
        "P-CHB-RESP-FEEDING", "CHB", "Response",
        premises=["size_class（决定 prey 偏好参数宽度：小=杂食宽谱，大=鱼食偏窄）"],
        sketch=(
            "离散目标 → 机会主义宽谱 typed food evaluator（多种饵/拟饵可钓，FishBase 原文"
            "佐证；大个体 prey 偏好参数收窄向鱼食）→ 决定响应。P01 实例化，纯参数差异。"
        ),
        steps=[
            {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "DECIDE_RESPONSE", "deps": [0]},
        ],
        branches=[],
        combine="NONE",
        return_type="Response(TargetFeeding)",
        instance_noise={"species": "Common Chub", "profile": None,
                        "constants": {"diet_breadth": "wide_opportunist"}},
    ),
]


def blind_hash(record: dict) -> str:
    body = {k: v for k, v in record.items() if k not in ("blind_hash",)}
    canonical = json.dumps(body, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]


def main():
    out = BATCH_DIR / "blind_programs.jsonl"
    lines = []
    for p in PROGRAMS:
        p["registry_seen"] = False
        p["registry_seen_at_creation"] = False
        p["blind_hash"] = blind_hash(p)
        lines.append(json.dumps(p, ensure_ascii=False))
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"frozen {len(PROGRAMS)} blind programs -> {out}")
    for p in PROGRAMS:
        print(f"  {p['program_id']}: {p['blind_hash']}")


if __name__ == "__main__":
    main()
