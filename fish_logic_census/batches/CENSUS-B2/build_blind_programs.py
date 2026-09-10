# -*- coding: utf-8 -*-
"""CENSUS-B2 盲程序骨架生成器（盲纪律：registry v3 未开）。
10 条冻结 Story（B01×3 + R02×6 + R03×1[状态存疑标注]）。
hash: sha256(canonical_json(record minus blind_hash))[:16]
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent
U = {
    "PIK19": "https://app.notion.com/p/3d6a4137d23681c0bc32c9542d458b54",
    "WAL": "https://app.notion.com/p/3d6a4137d23681c5ac98fd6e4982c846",
    "BRT12": "https://app.notion.com/p/3d6a4137d23681e59906c90017cd6aea",
    "ARC": "https://app.notion.com/p/3d6a4137d23681a1bfe0f18abd8436c4",
    "VEN": "https://app.notion.com/p/3d6a4137d23681b282d3e08c885d8a71",
    "FGA": "https://app.notion.com/p/3d6a4137d236817891fed67a8f77c477",
    "SWO": "https://app.notion.com/p/3d6a4137d23681c787cffee3652033e2",
    "BHC": "https://app.notion.com/p/3d6a4137d236815cbb26ff16d2b2e05a",
    "HER": "https://app.notion.com/p/3d6a4137d2368155b1cefba3ab182dd9",
    "MDF": "https://app.notion.com/p/3d6a4137d2368170b944ebc5e7ad2c11",
}
S = {k: f"CENSUS-B2-{k}" for k in U}

def rec(pid, story, surface, premises, sketch, steps, branches, combine,
        return_type, instance_noise, open_sem=None, confidence=None, status=None):
    r = {"program_id": pid, "story_id": S[story], "species_id": story,
         "surface": surface, "incoming_premises": premises,
         "human_readable_sketch": sketch, "ordered_steps": steps,
         "branches": branches, "combine": combine, "return_type": return_type,
         "instance_noise": instance_noise, "helpers": [],
         "source_evidence_ids": [U[story]], "open_semantics": open_sem or []}
    if confidence: r["confidence"] = confidence
    if status: r["input_status"] = status
    return r

def single(factor, binding, note=None):
    return [{"op": f"EVAL_{factor}", "deps": []},
            {"op": "NORMALIZE_WEIGHT", "deps": [0]}]

def typed(note=None):
    return [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
            {"op": "DECIDE_RESPONSE", "deps": [0]}]

PROGRAMS = [
    # PIK19 白斑狗鱼：产卵浅水↔产后深水
    rec("P-B2-PIK19-BAKE", "PIK19", "Bake",
        ["spawning_stage = PRE | POST（上游 lifecycle）"],
        "产卵期进入浅水支流/淹水草地散卵，产后返较深水：位置/深度因子随繁殖阶段 "
        "premise 配置切换（P05 配置级；Spawning aggregation≠Guard≠互斥 Group——Story 明言）。",
        single("HABITAT_FACTOR_POSITION", "spawning_stage", "位置因子（浅水草地↔深水）"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Northern Pike", "profile": "FloodedGrassSpawner", "constants": {}}),
    rec("P-B2-PIK19-RESP", "PIK19", "Response", [],
        "离散目标 → typed food evaluator → 决定响应（钓点随产前后位置变化是玩家策略，鱼响应标准）。",
        typed("TYPED 标准形态"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Northern Pike", "profile": None, "constants": {}}),
    # WAL 玻璃梭鲈：季节位置重排（温度+食物）
    rec("P-B2-WAL-BAKE", "WAL", "Bake",
        ["season = 季节（上游 condition）"],
        "季节位置重排：温度因子与食物分布因子（证据明言位置改变与繁殖、温度和食物分布有关）"
        "→ 加权组合 → 空间权重；季节改变浅滩/坡缘/深水结构的使用（P05：不建季节 Mode）。",
        [{"op": "EVAL_HABITAT_FACTOR_TEMPERATURE", "deps": []},
         {"op": "EVAL_RESOURCE_FACTOR_PREY", "deps": []},
         {"op": "COMBINE_WEIGHTED", "deps": [0, 1]}],
        [], "WEIGHTED_FACTORS", "SpatialDistributionWeight",
        {"species": "Walleye", "profile": "SeasonalReorder", "constants": {}},
        open_sem=["因子间顺序与 combine 权重未由证据裁决（B0 HRQ-07 同提案适用）"]),
    rec("P-B2-WAL-RESP", "WAL", "Response", [],
        "离散目标 → typed food evaluator → 决定响应（产卵聚集不证明更强取食——Story）。",
        typed("TYPED 标准形态"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Walleye", "profile": None, "constants": {}}),
    # BRT12 褐鳟：季节猎物脉冲
    rec("P-B2-BRT12-BAKE", "BRT12", "Bake",
        ["prey_pulse = 季节猎物脉冲事件（如蜉蝣羽化；世界侧 fact）"],
        "季节猎物脉冲：猎物资源 patch 强度随季节脉冲波动（ResourcePatch 描述——Story "
        "Competing 明言食物脉冲可由 ResourcePatch 描述，Hatch 无独立持续身份）。",
        single("RESOURCE_PATCH", "prey_pulse", "季节脉冲猎物 patch"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Brown Trout", "profile": "SeasonalPulse", "constants": {"pulse": "mayfly_emergence"}}),
    rec("P-B2-BRT12-RESP", "BRT12", "Response", ["seasonal_prey_context = 季节可见食物（上游 fact）"],
        "离散目标 → typed food evaluator（猎物类型与季节作 typed Context——owner 推论；"
        "饵型随可见食物变化=参数）→ 决定响应。",
        typed("TYPED 标准形态（季节 context 参数）"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Brown Trout", "profile": None, "constants": {}}),
    # ARC 北极红点鲑：冷水季节位移
    rec("P-B2-ARC-BAKE", "ARC", "Bake",
        ["season_temperature = 季节/温度（上游 condition）"],
        "冷水季节位移：近岸/深水位置利用随季节与温度切换（temperature/depth context——"
        "Story Lowest-Power；洄游/湖居种群差异不合并 FishMode）。",
        single("HABITAT_FACTOR_POSITION", "season_temperature", "近岸↔深水位置因子"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Arctic Char", "profile": "ColdWaterShift", "constants": {}},
        confidence="MEDIUM"),
    rec("P-B2-ARC-RESP", "ARC", "Response", [],
        "离散目标 → typed food evaluator → 决定响应（入口条件较强=参数；Presentation 仍是离散猎物响应——Story）。",
        typed("TYPED 标准形态"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Arctic Char", "profile": None, "constants": {}}, confidence="MEDIUM"),
    # VEN 欧白鲑：水层随水温季节
    rec("P-B2-VEN-BAKE", "VEN", "Bake",
        ["water_temperature_season = 水温/季节（上游 condition）"],
        "水层利用随水温与季节改变：水层因子随温度/季节绑定切换（typed cold-water/depth "
        "context——Story Lowest-Power；不购买新 Mode）。",
        single("HABITAT_FACTOR_LAYER", "water_temperature_season", "底层↔水层切换因子"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Vendace", "profile": "LayerShift", "constants": {}},
        confidence="MEDIUM"),
    rec("P-B2-VEN-RESP", "VEN", "Response", [],
        "离散目标 → typed food evaluator → 决定响应（浮游/小型猎物取向参数）。",
        typed("TYPED 标准形态"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Vendace", "profile": None, "constants": {}}, confidence="MEDIUM"),
    # FGA 佛罗里达雀鳝：植被伏击+季节窗口
    rec("P-B2-FGA-BAKE", "FGA", "Bake",
        ["activity_window = 季节/水温活动窗口（condition，影响活性非空间）"],
        "浅水植被缓流结构伏击：植被/结构栖息因子（静态）→ 归一化权重；季节水温改变"
        "浅水活动窗口（活性 condition premise，非空间程序分支）。",
        single("HABITAT_FACTOR_STRUCTURE", "static_vegetation", "植被结构栖息因子"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Florida Gar", "profile": "VegetatedAmbush", "constants": {}}),
    rec("P-B2-FGA-RESP", "FGA", "Response", [],
        "离散目标 → typed food evaluator（猎物轮廓/停顿/贴近结构 typed context）→ 决定响应（P01）。",
        typed("TYPED 标准形态"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Florida Gar", "profile": None, "constants": {}}),
    # SWO 剑旗鱼：昼夜垂直迁移
    rec("P-B2-SWO-BAKE", "SWO", "Bake",
        ["diel_phase = DAY | NIGHT（昼夜相位，上游 condition）"],
        "昼夜垂直迁移：水层因子随昼夜相位绑定切换（白天较深水层、夜间近表层——条件切换，"
        "不把全日行为压成静态栖息层——Story Scope）。深度/光照/温度层是策略变量。",
        single("HABITAT_FACTOR_LAYER", "diel_phase(day→deep/night→surface)", "昼夜垂直迁移水层因子"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Swordfish", "profile": "DielVerticalMigrate", "constants": {}},
        open_sem=["coverage report #24 定向 2D 样本：Layer×Diel 是否『最优带系统性迁移』不可分离交互，"
                  "取决于迁移驱动（自身节律 vs 饵群跟随）——Story 正文无『迁移驱动』节，未闭合；"
                  "本骨架按 premise 绑定切换处理，2D 判据留 representation 线裁决"]),
    rec("P-B2-SWO-RESP", "SWO", "Response", ["layer_context = 温跃层/猎物水层（上游 fact）"],
        "离散目标 → typed food evaluator（鱼/鱿取向；水层匹配是呈现侧参数）→ 决定响应。",
        typed("TYPED 标准形态"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Swordfish", "profile": None, "constants": {}}),
    # BHC 鳙鱼：滤食浮游场（P03）
    rec("P-B2-BHC-BAKE", "BHC", "Bake",
        ["food_field = 浮游动物/植物/悬浮颗粒浓度场（世界侧 fact，水柱分布）"],
        "滤食机会由 FoodField 浓度与水层决定：食物场浓度评估（场 evaluand——分布式浓度场，"
        "非离散 patch）→ 归一化权重（P03：FieldFeeding + FoodField；高生产力水层定位）。",
        single("FOOD_FIELD_CONCENTRATION", "plankton_field", "食物场浓度因子（场 evaluand）"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Bighead Carp", "profile": "FilterFeeder", "constants": {}}),
    rec("P-B2-BHC-RESP-FIELD", "BHC", "Response",
        ["food_field = 浓度场（上游 fact）"],
        "滤食响应：食物场摄入评估（场浓度驱动的持续滤食摄食——无离散钩饵目标 evaluator；"
        "滤食与离散钩饵响应并非同一现实机制——Story 明言）→ 场摄食决策。产品捕获方式"
        "由 Product Scope 决定（Story Open Question→TAR）：非主动滤食捕获走 Boundary/Scope。",
        [{"op": "EVAL_FOOD_FIELD_INTAKE", "deps": []},
         {"op": "DECIDE_FIELD_FEEDING", "deps": [0]}],
        [], "NONE", "Response(FieldFeeding)",
        {"species": "Bighead Carp", "profile": "FilterFeeding", "constants": {}},
        open_sem=["evaluand=食物场（非离散目标）：与 typed-target 族通道轴不可互吞（B1-LAM 判例同型），族归属判同裁决",
                  "产品捕获方式未定（Product Scope）——鲢鱼 R02-S07 同型对照不建体"]),
    # HER 大西洋鲱：群游+浮游食场（P03；GroupStrong）
    rec("P-B2-HER-BAKE", "HER", "Bake",
        ["food_field = 浮游食场（世界侧 fact）",
         "school_overlay = 群游集聚（空间 Factor 值域承载，coverage #17 判；非独立程序）"],
        "浮游食场跟随：食物场浓度评估 → 归一化权重；群游集聚由空间 Factor 值域承载"
        "（不单独购买结构）；季节产卵迁移为 lifecycle premise。",
        single("FOOD_FIELD_CONCENTRATION", "plankton_field+school", "浮游食场因子（群体 overlay）"),
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Atlantic Herring", "profile": "SchoolingFilter", "constants": {}}),
    rec("P-B2-HER-RESP-FIELD", "HER", "Response",
        ["food_field = 浮游食场（上游 fact）"],
        "场摄食响应：食物场摄入评估（浮游食场；找鱼=定位饵鱼层/群体边缘——玩家策略）"
        "→ 场摄食决策。产卵群体≠摄食群体（不可统一全年群体触发器——Story）。",
        [{"op": "EVAL_FOOD_FIELD_INTAKE", "deps": []},
         {"op": "DECIDE_FIELD_FEEDING", "deps": [0]}],
        [], "NONE", "Response(FieldFeeding)",
        {"species": "Atlantic Herring", "profile": "SchoolingFilter", "constants": {}}),
    # MDF 鳜鱼：结构+冬季深水+移动目标（状态存疑）
    rec("P-B2-MDF-BAKE", "MDF", "Bake",
        ["temperature = 水温（上游 condition：冬季低温→深水；>15°C 活性）",
         "turbidity_pref = 清水偏好（物种常量 fact）"],
        "结构遮蔽+季节深度：结构因子（石/树根/水草遮蔽，常态停留）与深度因子"
        "（冬季低温进深水，温度绑定）加权组合 → 空间权重。",
        [{"op": "EVAL_HABITAT_FACTOR_STRUCTURE", "deps": []},
         {"op": "EVAL_HABITAT_FACTOR_DEPTH", "deps": []},
         {"op": "COMBINE_WEIGHTED", "deps": [0, 1]}],
        [], "WEIGHTED_FACTORS", "SpatialDistributionWeight",
        {"species": "Mandarin Fish", "profile": "StructureWinterDeep", "constants": {"active_above_c": 15}},
        open_sem=["因子组合语义证据弱（FAO 描述并列两维）；夜间摄食=活性窗口 condition 非空间程序"],
        confidence="MEDIUM",
        status="frozen_status_disputed: 属性 ReviewStatus=Independent PASS 与正文 ReviewStatus=REVISE 矛盾；R03 批 Package=ARTIFACT_REVISE（Completion Claims Withdrawn）——待 coordinator 裁决"),
    rec("P-B2-MDF-RESP", "MDF", "Response",
        ["prey_motion_state = 目标移动状态（上游呈现侧 fact：静止不触发，移动触发追捕）"],
        "移动目标触发追捕：离散目标 → typed food evaluator（移动性为核心输入：静止目标"
        "通常不触发追捕，目标开始移动后迅速追捕——FAO 实证）→ 决定响应。P01 typed "
        "context 的强实例（motion 输入）。",
        typed("TYPED（motion-triggered evaluator 强实例）"),
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Mandarin Fish", "profile": "MotionTriggered", "constants": {}},
        confidence="MEDIUM",
        status="frozen_status_disputed（同 P-B2-MDF-BAKE）"),
]


def blind_hash(record):
    body = {k: v for k, v in record.items() if k != "blind_hash"}
    return hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True)
                          .encode("utf-8")).hexdigest()[:16]


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
