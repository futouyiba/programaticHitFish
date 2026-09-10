# -*- coding: utf-8 -*-
"""CENSUS-B1 盲程序骨架生成器（盲纪律产物，FIX-001 范式之外的正常盲批）。

在打开 template_registry.yaml（v2）之前，从 15 条冻结 Story（13×B01 + 2×FISH-R02，
Story DB 只读）+ P01/P02/P04/P05/P06 冻结语义 Pattern 独立重建每个有程序意义的
Story×Surface 的 Minimal Program Sketch，冻结进 blind_programs.jsonl
（内容 sha256 + registry_seen=false）。

B0 教训执行：每条 Story 的机制面（StoryDomain/PrimaryEvaluand/ResponseChannels/
Owner 推论）逐项过——program / 显式排除 / OUT_OF_SCOPE 三选一，无静默丢弃。

hash 算法：sha256(canonical_json(record minus blind_hash))[:16]
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent

U = {
    "GRB": "https://app.notion.com/p/3d6a4137d23681168a18f10342e09a94",
    "BRT": "https://app.notion.com/p/3d6a4137d236812dadf2c2e5d3260f47",
    "TIL": "https://app.notion.com/p/3d6a4137d23681389292e770ce06dd9a",
    "PAD35": "https://app.notion.com/p/3d6a4137d236813d915ae220f5ed8006",
    "DRU": "https://app.notion.com/p/3d6a4137d236815b9313c3005b469749",
    "COD": "https://app.notion.com/p/3d6a4137d23681879692c6ae73dd9798",
    "PAD34": "https://app.notion.com/p/3d6a4137d23681949995d729af6a28be",
    "PIK": "https://app.notion.com/p/3d6a4137d23681ba89cad88103708867",
    "GAR": "https://app.notion.com/p/3d6a4137d23681bf8977cc4ce1233b4a",
    "BLU": "https://app.notion.com/p/3d6a4137d23681db8441f33ca9ee08a5",
    "SMA": "https://app.notion.com/p/3d6a4137d23681deb3a9c69b5ed3d5ad",
    "RAI": "https://app.notion.com/p/3d6a4137d23681df9b7ed2edfaf0dab9",
    "LAM": "https://app.notion.com/p/3d6a4137d23681e18ed7f7d2d1a1ecb7",
    "DIS": "https://app.notion.com/p/3d6a4137d236811f9304e20d4ae4cbd3",
    "ONS": "https://app.notion.com/p/3d6a4137d23681e7a651c3b1b67ae84f",
}
S = {k: f"CENSUS-B1-{k}" for k in U}

def rec(pid, story, surface, premises, sketch, steps, branches, combine,
        return_type, instance_noise, helpers=None, open_sem=None,
        confidence=None, scope_note=None):
    r = {
        "program_id": pid, "story_id": S[story], "species_id": story,
        "surface": surface, "incoming_premises": premises,
        "human_readable_sketch": sketch, "ordered_steps": steps,
        "branches": branches, "combine": combine, "return_type": return_type,
        "instance_noise": instance_noise, "helpers": helpers or [],
        "source_evidence_ids": [U[story]], "open_semantics": open_sem or [],
    }
    if confidence:
        r["confidence"] = confidence
    if scope_note:
        r["scope_note"] = scope_note
    return r

PROGRAMS = [
    # 1 草鱼 S53：植食/预投饵 patch
    rec("P-B1-GRB-BAKE", "GRB", "Bake",
        ["prebait_patches = 玩家预投饵斑块事实（环境资源 owner 保存，世界侧 fact）"],
        "分布跟随植食资源与预投饵斑块（P02：ResourcePatch 供给背景）："
        "资源 patch 强度评估 → 归一化空间权重。单资源链，无 hard gate、无多因子组合。",
        [{"op": "EVAL_RESOURCE_PATCH", "deps": []},
         {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Grass Carp", "profile": "HerbivorePatch",
         "constants": {"resource": "aquatic_plant+bait_patch"}}),
    rec("P-B1-GRB-RESP", "GRB", "Response",
        ["resource_context = 局部食物背景（上游 fact）"],
        "离散钩饵目标 → 植食/饵取向 typed food evaluator（面包/玉米等饵可接受）"
        "→ 决定响应（P02：patch 背景下离散 TargetFeeding）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Grass Carp", "profile": None, "constants": {"bait": "bread/corn"}}),
    # 2 褐鳟 S14：中心-边缘位置分配
    rec("P-B1-BRT-BAKE", "BRT", "Bake",
        ["individual_rank = 优势等级（个体 Condition/Relation fact，上游；持久写回为 Open Question）",
         "resource_patch = 食物位置分布（上游 fact）"],
        "摄食位置竞争：食物 patch 强度评估 → 个体 rank 位置偏好因子"
        "（优势个体偏向 patch 中心，次级个体边缘化）→ 加权组合 → 空间权重。"
        "竞争性占位以个体属性因子表达，不是独立争食 Mode（owner 推论）。",
        [{"op": "EVAL_RESOURCE_PATCH", "deps": []},
         {"op": "EVAL_RANK_POSITION_PREFERENCE", "deps": []},
         {"op": "COMBINE_WEIGHTED", "deps": [0, 1]}],
        [], "WEIGHTED_FACTORS", "SpatialDistributionWeight",
        {"species": "Brown Trout", "profile": "PatchCompetitor",
         "constants": {"position": "core-vs-edge"}},
        open_sem=["rank fact 的产品持久写回未定（Story Open Question）；若产品不实现 rank 状态，退化为纯 patch 体",
                  "受控异种配对实验证据（Confidence=Medium）"],
        confidence="MEDIUM"),
    rec("P-B1-BRT-RESP", "BRT", "Response",
        ["position_context = 所占位置（上游 fact）"],
        "离散目标 → typed food evaluator（位置背景影响可及食物）→ 决定响应。"
        "竞争「明显攻击并不多」，conflict path 证据不足不建。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Brown Trout", "profile": None, "constants": {}}),
    # 3 罗非鱼 S44：口孵抑制
    rec("P-B1-TIL-RESP", "TIL", "Response",
        ["mouthbrood_state = ACTIVE（雌性口孵期，persistent condition，上游）",
         "food_response_cap = 口孵期摄食率抑制参数（随 condition）"],
        "口孵期食物响应：离散目标 → typed food evaluator → 决定响应；"
        "响应强度被口孵 condition 的 cap 参数抑制（少食/停食）。受警回口=照护行为，"
        "交实例化后照护 owner（OUT_OF_SCOPE）。body 形态同 typed-target 标准，"
        "抑制是 premise 参数不是 body 分支。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Nile Tilapia", "profile": "MouthbroodingFemale",
         "constants": {"cap": "seasonal_reduced_or_halted"}},
        confidence="MEDIUM"),
    # 4 鸭嘴鲟 S35：习惯化
    rec("P-B1-PAD35-RESP", "PAD35", "Response",
        ["cue_history = 刺激历史 fact（重复无奖励→衰减；食物强化→恢复；上游 CueMemory，状态契约 Input Contract Open）"],
        "习惯化响应：离散目标 → typed food evaluator（输入含刺激历史："
        "重复无奖励刺激→响应衰减；食物强化→恢复）→ 决定响应。"
        "历史是 evaluator 输入 fact（premise），不是 body 内控制流；"
        "状态键/写入事件/保持时间未定（Story 明言本批不新增状态或 Grammar）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Paddlefish", "profile": "HabituatedJuvenile",
         "constants": {"history_effect": "habituation+food_recovery"}},
        open_sem=["cue_history fact 的状态契约（键/写入/保持）未定；感觉疲劳/奖励历史/饱食需区分（Story 明言）"],
        confidence="MEDIUM"),
    # 5 黑鼓鱼 S46：泥云痕迹（鱼侧=底栖猎物 patch）
    rec("P-B1-DRU-BAKE", "DRU", "Bake",
        ["benthic_prey_field = 底栖猎物分布（上游 fact）",
         "feeding_traces = 翻底凹痕/泥云（本鱼种行为产物；对玩家是搜索线索，对鱼程序是痕迹可见性，环境 owner）"],
        "鱼侧空间程序：分布跟随底栖猎物资源 patch（翻底觅食）→ 归一化权重。"
        "泥云/凹痕是本行为的物理痕迹（世界侧保存与可见性，玩家搜索信息），"
        "不改变鱼自身分布程序（痕迹≠必有鱼，鱼仍对局部实际猎物响应——owner 推论）。",
        [{"op": "EVAL_RESOURCE_PATCH", "deps": []},
         {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Black Drum", "profile": "BottomForager",
         "constants": {"resource": "benthic_prey"}}),
    rec("P-B1-DRU-RESP", "DRU", "Response",
        ["benthic_context = 底质/猎物背景（上游 fact）"],
        "离散目标 → 底栖取向 typed food evaluator → 决定响应（P02）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Black Drum", "profile": None, "constants": {}}),
    # 6 鳕鱼 S52：性别相关水深
    rec("P-B1-COD-BAKE", "COD", "Bake",
        ["sex = 个体性别 fact（上游；产品是否区分性别供给未定）",
         "spawning_stage = 繁殖期状态（上游 lifecycle）"],
        "繁殖期性别相关水深：深度因子评估（绑定随 sex/stage premise 切换："
        "性别相关深度差异）→ 归一化权重。Spatial 随阶段/性别调整，"
        "先不购买互斥 FishGroup（owner 推论；GroupPressure=Possible 未证实）。",
        [{"op": "EVAL_HABITAT_FACTOR_DEPTH", "deps": []},
         {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Atlantic Cod", "profile": "SpawningSexDepth",
         "constants": {"depth_binding": "sex_and_stage"}},
        open_sem=["潜水与排卵关系是解释非逐次确认（Story）；个体异质性不确定",
                  "性别供给拆分（share-vector）是 Group 面表达选择，本批按配置级因子绑定处理"],
        confidence="MEDIUM"),
    rec("P-B1-COD-RESP", "COD", "Response",
        ["depth_context = 所在水层（上游 fact）"],
        "离散目标 → typed food evaluator → 决定响应（遥测深度不直接判定当下 FeedingMatch，无新结构）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Atlantic Cod", "profile": None, "constants": {}}),
    # 7 鸭嘴鲟 S34：幼体被动电感受
    rec("P-B1-PAD34-BAKE", "PAD34", "Bake",
        ["lifecycle_stage = JUVENILE（幼体阶段，上游）",
         "plankton_prey_field = 浮游猎物分布（上游 fact）"],
        "幼体分布跟随浮游猎物资源 patch → 归一化权重。静态栖息（Static Habitat），"
        "无空间结构差异证据；不能推广到成年滤食（Story 限定）。",
        [{"op": "EVAL_RESOURCE_PATCH", "deps": []},
         {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Paddlefish", "profile": "JuvenileElectrosense",
         "constants": {"resource": "plankton_prey"}}),
    rec("P-B1-PAD34-RESP-SENSE", "PAD34", "Response",
        ["lifecycle_stage = JUVENILE",
         "sensing_channel = PASSIVE_ELECTROSENSE（被动电感受；电呈现输入是否进产品范围未定 Product Scope Deferred）"],
        "感知段：离散目标的暴露度评估 → 被动电感受 typed evaluator（频率/强度/水电导"
        "条件调制，人工偶极实验证据）→ 决定响应。感官不同≠新 Channel（owner：先作为 "
        "typed sensory Context 影响离散目标评估）。",
        [{"op": "EVAL_TARGET_EXPOSURE_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Paddlefish", "profile": "JuvenilePassiveElectrosense",
         "constants": {"channel": "passive_electrosense"}},
        open_sem=["电呈现输入由谁提供、是否在产品范围内未定（Product Scope Deferred）"],
        confidence="MEDIUM"),
    # 8 白斑狗鱼 S20：初次接受 only
    rec("P-B1-PIK-RESP", "PIK", "Response",
        ["capture_phase = 取饵后阶段状态（交交互实例 owner，本面不读）"],
        "census 侧仅覆盖初次接受：离散目标 → typed food evaluator → 决定响应。"
        "横咬/转向吞咽/捕获阶段为 post-instantiation（Semantic Review Context §2："
        "follow/pursue/咬/contact 归 Fish AI/Gameplay/Contact owner）——OUT_OF_SCOPE。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Northern Pike", "profile": None, "constants": {}},
        scope_note="OUT_OF_SCOPE：取饵后处理/保留/Hook 阶段（交互实例 owner）"),
    # 9 鳄雀鳝 S07：初次接受 only
    rec("P-B1-GAR-RESP", "GAR", "Response",
        ["capture_phase = 取饵后阶段状态（交交互实例 owner，本面不读）"],
        "census 侧仅覆盖最初接受：离散目标 → typed food evaluator → 决定响应"
        "（TargetFeeding 只解释最初接受——owner 推论）。携行/吞咽/挂钩阶段边界为 "
        "post-instantiation owner——OUT_OF_SCOPE；hard-mouth 失败不得反写成 "
        "FeedingMatch 失败。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Alligator Gar", "profile": None, "constants": {}},
        scope_note="OUT_OF_SCOPE：携行/咀嚼吞咽/吐饵/Hook 阶段（交互实例 owner）"),
    # 10 蓝鳃 S39：季节水层 + 窄接受
    rec("P-B1-BLU-BAKE", "BLU", "Bake",
        ["season = 季节（上游 condition）"],
        "季节性水层变化：水层因子评估（绑定随季节 premise 切换）→ 归一化权重。"
        "钓法指南证据（水层随季节改变），无其他空间结构证据。",
        [{"op": "EVAL_HABITAT_FACTOR_LAYER", "deps": []},
         {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Bluegill", "profile": "SeasonalLayer",
         "constants": {"layer_binding": "season"}},
        confidence="MEDIUM"),
    rec("P-B1-BLU-RESP", "BLU", "Response",
        ["presentation_context = 呈现参数（小饵/低速——输入侧）"],
        "初次接受：离散目标 → 窄接受 typed food evaluator（小饵低阻呈现取向；"
        "参数宽度）→ 决定响应。吐饵=接触后阻力事件，归 Contact/interaction owner"
        "（OUT_OF_SCOPE），不得反证从未接受。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Bluegill", "profile": "NarrowAcceptance",
         "constants": {"acceptance": "small_slow_presentation"}},
        scope_note="OUT_OF_SCOPE：接触后阻力/吐饵（Contact/interaction owner）"),
    # 11 小口黑鲈 S32：跟随翻底
    rec("P-B1-SMA-BAKE", "SMA", "Bake",
        ["disturbance_events = 它鱼/它动物翻底扰动事件与暴露猎物区（世界侧 fact，环境 owner 产生）"],
        "跟随扰动觅食：动态机会 patch 评估（扰动暴露的猎物区）→ 归一化权重。"
        "扰动者由环境 owner 改变局部猎物可达性，鱼对实际猎物响应（owner 推论）；"
        "跟随≠RelationalConflict、不购 Field Mode（Competing）。",
        [{"op": "EVAL_RESOURCE_PATCH", "deps": []},
         {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Smallmouth Bass", "profile": "DisturbanceFollower",
         "constants": {"resource": "disturbance_revealed_prey"}}),
    rec("P-B1-SMA-RESP", "SMA", "Response",
        ["revealed_prey_context = 暴露猎物背景（上游 fact）"],
        "离散目标 → 被惊出猎物取向 typed food evaluator → 决定响应（P02）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Smallmouth Bass", "profile": None, "constants": {}}),
    # 12 虹鳟 S24：纯参数/Profile 样本
    rec("P-B1-RAI-RESP", "RAI", "Response",
        ["locale_variant = 地域策略变体（per-instance Profile 绑定，上游配置）"],
        "鼠形表面饵：离散目标 → 表面呈现 typed food evaluator（鼠形/表面 context；"
        "地域变体=Profile 重绑定参数）→ 决定响应。改变 Target 和表面 Context，"
        "无需新 Channel（owner 推论）——本批阴性样本（纯参数/Profile，无新结构预期）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Rainbow Trout", "profile": "KanektokMouseFly",
         "constants": {"presentation": "surface_mouse_fly"}}),
    # 13 海七鳃鳗 S49：非摄食化学趋向
    rec("P-B1-LAM-BAKE", "LAM", "Bake",
        ["chemical_gradient_field = 信息素/警报线索梯度场（世界侧 fact，管理投放或自然源）",
         "migratory_state = 繁殖迁移期（上游 lifecycle）"],
        "化学梯度调制迁移分布：化学梯度场评估（信息素吸引/警报排斥方向）"
        "→ 归一化权重（趋向高信息素/避开警报区的分布偏置）。"
        "非摄食空间趋向（owner：先尝试 Spatial/Condition）；诱捕/陷阱捕获为装备侧"
        "OUT_OF_SCOPE。Product Scope Deferred。",
        [{"op": "EVAL_CHEMICAL_GRADIENT_FIELD", "deps": []},
         {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Sea Lamprey", "profile": "PheromoneGuidedMigration",
         "constants": {"gradient": "pheromone_attract+alarm_avoid"}},
        open_sem=["进入诱导区域 vs 进入捕获装置是不同结果（trap 侧 OUT_OF_SCOPE）",
                  "诱捕玩法是否纳入产品未定（Product Scope Deferred）"],
        confidence="MEDIUM"),
    rec("P-B1-LAM-RESP-APPROACH", "LAM", "Response",
        ["chemical_gradient_field = 化学线索梯度（上游 fact）",
         "migratory_state = 繁殖迁移期"],
        "非摄食化学趋向响应：环境化学梯度评估（信息素/警报 typed evaluator；"
        "central evaluand=环境梯度场，非离散钩饵目标）→ 决定趋向（approach/avoid）。"
        "这是 Non-feeding cue-guided approach 候选组合（Story 待检验），"
        "不是 TargetFeeding（信息素吸引不是 Feeding），也不是 P04 冲突"
        "（求偶吸引≠入侵冲突）。census 层按感知 evaluator 记录"
        "（与表达线 REP-CUE-AXIS 独立——coordinator note）。",
        [{"op": "EVAL_AMBIENT_CUE_GRADIENT_TYPED", "deps": []},
         {"op": "DECIDE_APPROACH_OR_AVOID", "deps": [0]}],
        [], "NONE", "Response(Approach | Avoid)",
        {"species": "Sea Lamprey", "profile": "ChemotacticMigration",
         "constants": {"cue": "pheromone/alarm"}},
        open_sem=["evaluand=环境梯度（非离散目标）：与 typed-target 族的通道轴边界待判同裁决",
                  "前链负责趋向还是仅空间分布未定（Story Open Question）"],
        confidence="MEDIUM"),
    # 14 七彩神仙 S11：亲鱼护幼 dual-path
    rec("P-B1-DIS-RESP-GUARD", "DIS", "Response",
        ["guard_state = BIPARENTAL_CARE（亲鱼育幼期 persistent condition，P04）",
         "fry_anchor = 幼鱼群（贴附取食黏液的幼鱼群 relation object）"],
        "育幼期双路径：path A 食物路径（typed food evaluator）与 path B 护幼冲突路径"
        "（对 fry anchor 的入侵者距离/威胁 typed evaluator）并行评估 → 双路径合并"
        "→ 决定响应（TargetFeeding 或 RelationalConflict）。幼鱼贴附取食黏液是照护"
        "关系（允许贴附），非捕食。guard 为 persistent premise（P04：Candidate 不自动"
        "升级 FishMode）；色型不分裂（S12 白色型同构对照，不重复建体）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "EVAL_TARGET_AS_INTRUDER_TYPED", "deps": []},
         {"op": "COMBINE_DUAL_PATH", "deps": [0, 1]},
         {"op": "DECIDE_RESPONSE", "deps": [2]}],
        [], "DUAL_PATH_MERGE", "Response(TargetFeeding | RelationalConflict)",
        {"species": "Discus (orange form)", "profile": "BiparentalMucusFeeding",
         "constants": {"color_form": "not_split"}},
        confidence="HIGH"),
    # 15 准白甲鱼 S22：急流附着刮食
    rec("P-B1-ONS-BAKE", "ONS", "Bake",
        ["current_context = 流速条件（上游 fact）",
         "attached_resource_field = 石底附着藻/碎屑资源（上游 fact）"],
        "急流底质刮食：附着资源 patch 评估 → 流速 context 应用（急流石底绑定）"
        "→ 归一化权重。P06 Compression Candidate（可能压回 P02）；行为链"
        "（急流—石底—附着—刮食）Evidence Open，仅身份确认，无直接行为闭合证据。",
        [{"op": "EVAL_RESOURCE_PATCH", "deps": []},
         {"op": "APPLY_CURRENT_CONTEXT", "deps": [0]},
         {"op": "NORMALIZE_WEIGHT", "deps": [1]}],
        [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight",
        {"species": "Onychostoma simum", "profile": "RapidScraper",
         "constants": {"resource": "attached_algae_detritus", "context": "fast_flow_stone"}},
        open_sem=["行为链 Evidence Open（食性/口器行为/实钓均缺）——P06 压缩测试联动"],
        confidence="LOW"),
    rec("P-B1-ONS-RESP", "ONS", "Response",
        ["scrape_context = 口径窗/附着生物量（上游 fact）"],
        "离散目标 → 刮食取向 typed food evaluator（口径窗+附着生物量）"
        "→ 决定响应（P02/P06：连续刮食机会仍落离散钩饵 target，待检验）。",
        [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
         {"op": "DECIDE_RESPONSE", "deps": [0]}],
        [], "NONE", "Response(TargetFeeding)",
        {"species": "Onychostoma simum", "profile": None,
         "constants": {"acceptance": "mouth_gape_window"}},
        confidence="LOW"),
]


def blind_hash(record: dict) -> str:
    body = {k: v for k, v in record.items() if k != "blind_hash"}
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
