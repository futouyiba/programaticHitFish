# -*- coding: utf-8 -*-
"""CENSUS-RERUN-SINGLE-001 盲重建：SINGLE 族 66 成员中 61 个有顺序还原
表达文件的成员，Bake 链形按 §2.2 顺序还原伪脚本（REP-ORDER-FIX-001..005）
机械转写为程序骨架 IR。

盲纪律：
- 输入＝顺序还原后的 B 系列表达文件（envelope 冻结输入，非 Story DB）；
- 本脚本运行时 registry v6 尚未打开（registry_seen=false 全体）；
- 事前暴露声明（manifest bias_declaration）：SINGLE v1 canonical 两步形在
  角色记忆与 B4 批档（流程范式恢复）中已知——骨架不从 canonical 反推，
  而是从各文件 §2.2 逐字链形转写（文件自身声明与 canonical 的分歧）；
- 5 个无文件成员（LAM/PIN/ASR/RVS/RDS）不在本批骨架内，记 absence_claims。

程序 ID 约定：P-RS1-<CODE>-BAKE；story ID：CENSUS-RERUN-SINGLE-001-<CODE>。

【REV-001 注记 2026-09-11】原批盲输入提取的物种名级文件扫描无面信息缺陷（guarding
目录 §2.2 护巢 vs §2.4 栖息）由独立审 CENSUS-RERUN-SINGLE-REV-001 B1 实证（4 例面
错配——MEMBERS 表 guarding 目录 4 条误取 §2.2）；修复=apply_fix_rev001.py 补录 4 条
§2.4 栖息面盲体（blind_programs.jsonl append-only，本脚本与已冻结 61 条零改动；
节级面定位约定记 HRQ-RS1-04⑥）。
"""
import hashlib
import json
from pathlib import Path

BATCH = Path(__file__).parent
FA = "outputs/full_authoring"

# ---------------------------------------------------------------------------
# 链形簇定义（从 61 份 §2.2 盲输入归纳；判同在冻结后进行）
# ---------------------------------------------------------------------------

def steps(*pairs):
    return [{"op": op, "deps": list(deps)} for op, deps in pairs]

IF3 = lambda g: {"kind": "IF3_EXIT", "guard": g}
GATE = lambda g: {"kind": "GATE", "guard": g, "else": "RETURN_0_EARLY"}

CLUSTERS = {
    # C1 单因子三档链：档位评估（三档分级命中，出局=EARLY_RETURN）→归一化
    "C1_TIERED_SINGLE": dict(
        family_hint="TIERED_SINGLE_FACTOR_CHAIN",
        ops=steps(("EVAL_TYPED_FIELD_OR_FACTOR", ()), ("NORMALIZE_WEIGHT", (0,))),
        branches=[IF3("factor_tier_full_reduced_out")],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="单一 typed 因子三档档位评估（preferred=全额/tolerated=削减不清零/excluded=出局 EARLY_RETURN）→ NORMALIZE_WEIGHT"),
    # C2 双档链：水层带软三档 → premise 绑定轴段三档 → 归一化（双档积）
    "C2_DUAL_TIER": dict(
        family_hint="LAYER_AXIS_DUAL_TIER_CHAIN",
        ops=steps(("EVAL_TYPED_FIELD_OR_FACTOR", ()), ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("NORMALIZE_WEIGHT", (0, 1))),
        branches=[IF3("layer_tier"), IF3("premise_axis_segment_tier")],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="水层带定位三档（软定位）→ premise 绑定轴段归属三档 → NORMALIZE_WEIGHT（LayerTier × AxisFit 积内归一化）"),
    # C3 门+单档链：结构掩体存在门（二元，EARLY_RETURN）→ 掩体/质量档三档 → 归一化
    "C3_GATED_TIER": dict(
        family_hint="GATED_COVER_TIER_CHAIN",
        ops=None,  # per-member（gate op 名=真实门轴）
        branches_tier=IF3("cover_quality_tier"),
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="结构存在门（GATE_<axis>：门不成立直接 EARLY_RETURN）→ 掩体/质量档位三档 → NORMALIZE_WEIGHT"),
    # C4 夜行低光链：夜行底板档三档（出局）→ 低光槽三档（调整器，无出局）→ 归一化
    "C4_NOCTURNAL": dict(
        family_hint="NOCTURNAL_LIGHTSLOT_CHAIN",
        ops=steps(("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("APPLY_DYNAMIC_SPATIAL_SLOT", (0,)),
                  ("NORMALIZE_WEIGHT", (0, 1))),
        branches=[IF3("night_habitat_tier"),
                  {"kind": "IF3_ADJUST", "guard": "lowlight_slot_tier_noexit"}],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="夜行底板栖息档三档（无夜行底板=出局 EARLY_RETURN）→ 低光/夜相槽三档（槽=调整器非 gate：亮水=极低削减不清零，出局语义不落槽内；槽位=live §11.5 判例固定）→ NORMALIZE_WEIGHT"),
    # C5a 底带门+底质档+资源档：四步链
    "C5a_ZONE_SUBSTRATE": dict(
        family_hint="ZONE_SUBSTRATE_RESOURCE_CHAIN",
        ops=steps(("GATE_ZONE", ()), ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("EVAL_TYPED_FIELD_OR_FACTOR", ()), ("NORMALIZE_WEIGHT", (1, 2))),
        branches=[GATE("bottom_zone_present"), IF3("substrate_tier"), IF3("resource_tier")],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="底层水层定位硬门（GATE_ZONE，非底层=EARLY_RETURN）→ 底质栖境档三档 → 底栖资源档三档 → NORMALIZE_WEIGHT（SubstrateTier × ResourceIntensity 积内归一化）"),
    # C5b 软三档×3（无门）：水层软档+底质档+资源档
    "C5b_TRIPLE_SOFT": dict(
        family_hint="SOFT_TRIPLE_TIER_CHAIN",
        ops=steps(("EVAL_TYPED_FIELD_OR_FACTOR", ()), ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("EVAL_TYPED_FIELD_OR_FACTOR", ()), ("NORMALIZE_WEIGHT", (0, 1, 2))),
        branches=[IF3("layer_tier"), IF3("substrate_tier"), IF3("resource_tier")],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="近底带水层软三档（无硬门）→ 底质栖境档三档 → 资源档三档 → NORMALIZE_WEIGHT（三档积内归一化）"),
    # C5c 底带门+深度档+底质档+资源档：五步链
    "C5c_ZONE_DEPTH": dict(
        family_hint="ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN",
        ops=steps(("GATE_ZONE", ()), ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("EVAL_TYPED_FIELD_OR_FACTOR", ()), ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("NORMALIZE_WEIGHT", (1, 2, 3))),
        branches=[GATE("bottom_zone_present"), IF3("depth_tier"), IF3("substrate_tier"), IF3("resource_tier")],
        combine="NONE_SINGLE_CHAIN", ret="SpatialDistributionWeight",
        chain="底层水层定位硬门 → 深度带档三档（本鱼独有步）→ 底泥栖境档三档 → 底泥资源档三档 → NORMALIZE_WEIGHT（三档积内归一化）"),
    # C6 滤食场累积链：水层档→场浓度档→口径档（同一场评估顺序判定，叠加衰减）→归一化
    "C6_FILTER_FIELD": dict(
        family_hint="FILTER_FIELD_ACCUMULATE_CHAIN",
        ops=steps(("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("EVAL_FOOD_FIELD_CONCENTRATION", (0,)),
                  ("EVAL_SIZE_GAUGE_MATCH", (1,)),
                  ("NORMALIZE_WEIGHT", (2,))),
        branches=[IF3("field_layer_tier"), IF3("field_concentration_tier"), IF3("size_gauge_tier")],
        combine="SEQUENCE_FOLD_UNDEFINED", ret="SpatialDistributionWeight",
        chain="滤食水层定位三档（携削减标记）→ 场浓度三档（FieldSuitability 叠加衰减）→ 个体大小口径三档（浓度高但口径不匹配亦出局）→ NORMALIZE_WEIGHT（步间折减合成算子 OPERATOR UNDEFINED 待机制侧）"),
    # C7 护巢锚链：锚存在门→锚适配档→关系档→温度档→合并（UNDEFINED）
    "C7_GUARD_ANCHOR": dict(
        family_hint="GUARD_ANCHOR_TIERED_COMBINE_CHAIN",
        ops=steps(("GATE_ANCHOR_EXISTENCE", ()), ("EVAL_ANCHOR_SUITABILITY", ()),
                  ("EVAL_ANCHOR_RELATION", ()), ("EVAL_LOCAL_TEMPERATURE", ()),
                  ("COMBINE_GUARD_FACTORS", (1, 2, 3))),
        branches=[GATE("guard_anchor_in_legal_domain"), IF3("anchor_suitability_tier"),
                  IF3("anchor_relation_tier"), IF3("local_temperature_tier")],
        combine="MULTI_FACTOR_UNDEFINED", ret="Guarding SpatialDistributionWeight",
        chain="锚存在性判定（GATE_ANCHOR_EXISTENCE：锚域外=EARLY_RETURN，非「算出低值」）→ 锚适配三档 → 关系评估三档 → 局部温度三档 → 合并（算子 OPERATOR UNDEFINED 待机制侧）"),
    # C8 追击双槽+组合（PLAIN 形受限还原：槽内三档，槽间 unordered，无 early return）
    "C8_PLAIN_DUALSLOT": dict(
        family_hint="PLAIN_SHAPE_DUAL_SLOT",
        ops=steps(("EVAL_TYPED_FIELD_OR_FACTOR", ()), ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                  ("COMBINE_WEIGHTED", (0, 1))),
        branches=[{"kind": "IF3_SLOT_VALUE", "guard": "forage_slot_tier"},
                  {"kind": "IF3_SLOT_VALUE", "guard": "habitat_slot_tier"}],
        combine="WEIGHTED_UNDEFINED", ret="SpatialDistributionWeight",
        chain="追击型双槽（槽间顺序按 PLAIN 族契约 unordered 不还原）：槽1 猎物场档三档（excluded=出局槽值非 EARLY_RETURN，仍进 COMBINE）→ 槽2 栖息档三档（同族域边界）→ COMBINE_WEIGHTED（算子 OPERATOR UNDEFINED 待机制侧）"),
}

# ---------------------------------------------------------------------------
# 成员表：(code, batch, 文件, FIX 批, 簇, 物种, 主 Profile, 门轴[C3 专用],
#          premises, sketch 补充注记)
# ---------------------------------------------------------------------------
P_AXIS = "上游 lifecycle/阶段 premise（配置级切换因子集，body 无阶段分支；early return 对象=格子非阶段）"
MEMBERS = [
    # --- C1 premise 轴段 10 ---
    ("COD","B1","migration/species/atlantic_cod.md","003","C1_TIERED_SINGLE","Atlantic Cod（大西洋鳕）","@CodSexStageDepthProfile","",
     ["sex/stage = 上游个体事实（繁殖期雄/雌/未繁殖深度带配置级切换）"],"轴=性别阶段绑定深度带；档位成员 [需正文]"),
    ("PIK19","B2","migration/species/northern_pike_spawn.md","003","C1_TIERED_SINGLE","Northern Pike（白斑狗鱼）","@PikeSpawnStageSpatialProfile","",
     ["spawning_stage = 上游繁殖事实（淹水草地浅滩↔深水轴段配置级切换）"],"轴=淹水草地↔深水繁殖轴段；档位成员 [需正文]"),
    ("ARC","B2","migration/species/arctic_char.md","003","C1_TIERED_SINGLE","Arctic Char（北极红点鲑）","@ArcticCharSeasonSpatialProfile","",
     ["temp/season = 上游事实（近岸↔深水冷水季节轴段配置级切换）"],"轴=近岸↔深水冷水季节轴段"),
    ("VEN","B2","migration/species/vendace.md","003","C1_TIERED_SINGLE","Vendace（欧白鲑）","@VendaceLayerSpatialProfile","",
     ["temp/season = 上游事实（底层↔水层季节段配置级切换）"],"轴=底层↔水层垂直季节轴"),
    ("SWO","B2","migration/species/swordfish_diel.md","003","C1_TIERED_SINGLE","Swordfish（剑旗鱼）","@SwordfishDielSpatialProfile","",
     ["diel 相位 = 上游昼夜事实（表层↔深层段配置级切换）"],"tolerated 档=垂直迁移过渡带（DVM 型独有语义）；2D 判据 coverage #24 未闭合沿用"),
    ("CHN","B3","migration/species/chinook_salmon.md","003","C1_TIERED_SINGLE","Chinook Salmon（帝王鲑）","@ChinookSalmonMigrationSpatialProfile","",
     ["OCEAN/MIGRATION/SPAWN = "+P_AXIS],"轴=海洋觅食区↔河口↔深河产卵段；生活史多态落 Profile 值域"),
    ("COH","B3","migration/species/coho_salmon.md","003","C1_TIERED_SINGLE","Coho Salmon（银鲑）","@CohoSalmonMigrationSpatialProfile","",
     ["OCEAN/MIGRATION/SPAWN = "+P_AXIS],"轴=海洋觅食区↔河口↔产卵支流"),
    ("BRO","B3","migration/species/brook_trout.md","003","C1_TIERED_SINGLE","Brook Trout（美洲红点鲑）","@BrookTroutMigrationSpatialProfile","",
     ["RIVER/ESTUARY/OCEAN = "+P_AXIS+"；湖封种群形态落 Profile 值域"],"轴=海洋沿岸肥育带↔河口↔河段"),
    ("ALE","B3","migration/species/alewife.md","003","C1_TIERED_SINGLE","Alewife（灰西鲱）","@AlewifeMigrationSpatialProfile","",
     ["OCEAN/MIGRATION/SPAWN = "+P_AXIS+"；陆封/溯河种群形态落 Profile 值域"],"轴=海洋觅食区↔河口↔产卵河段"),
    ("TAR","B3","migration/species/atlantic_tarpon.md","003","C1_TIERED_SINGLE","Atlantic Tarpon（大西洋大海鲢）","@TarponAmphidromousSpatialProfile","",
     ["发育阶段（LARVA/JUVENILE_RIVER/SUBADULT_SEA/ADULT_COASTAL 枚举落 Profile 值域）= "+P_AXIS],"轴=沿岸礁带↔河口↔河沼幼体带（amphidromous 发育轴）"),
    # --- C1 机会型 4 ---
    ("BRT12","B2","normal/species/brown_trout.md","004","C1_TIERED_SINGLE","Brown Trout（褐鳟）","@BrtSeasonalPulsePatchProfile","",
     ["季节脉冲窗口 = 配置级切换因子"],"机会型第一判断=食物丰度先行；轴=季节脉冲猎物 patch"),
    ("PB","B3","normal2/species/orinoco_peacock.md","004","C1_TIERED_SINGLE","Orinoco Peacock Bass（奥里诺科孔雀鲈）","@ORPPatchProfile","",
     [],"机会型；轴=静水支流鱼群机会场（好斗方向锚——同批统一 R-T1）"),
    ("BST","B4","normal/species/labeo_barbel.md","004","C1_TIERED_SINGLE","Barbel Steed·唇䱻","@LbbBenthicInvertPatchProfile","",
     [],"机会型；轴=底栖无脊椎机会场（触须底觅方向）；文件名 labeo_barbel=内容唇䱻（文件名≠标题先例）"),
    ("CBM","B4","normal2/species/chub_mackerel.md","004","C1_TIERED_SINGLE","Chub Mackerel（日本鲭）","@CBMPatchProfile","",
     [],"机会型；轴=上层浮游/小鱼机会场（撕鳍口径 [需核对]）"),
    # --- C1 感官型 3 ---
    ("PAD34","B1","normal/species/paddlefish_electro.md","004","C1_TIERED_SINGLE","Paddlefish（鸭嘴鲟）","@PadElectroZooplanktonPatchProfile","",
     ["幼体阶段 = lifecycle premise（配置级限定）"],"感官型第一判断=信号场可探测性先行；轴=浮游猎物电感受信号场（幼体口径）"),
    ("SDG","B4","normal/species/spiny_dogfish.md","004","C1_TIERED_SINGLE","Spiny Dogfish（白斑角鲨）","@DogBenthicForagePatchProfile","",
     [],"感官型；轴=底层猎物被动电感受信号场"),
    ("TSK","B4","normal/species/thorny_skate.md","004","C1_TIERED_SINGLE","Thorny Skate（棘背钝头鳐）","@SkateBenthicForagePatchProfile","",
     [],"感官型；轴=底栖猎物被动电感受信号场；本文件兼承载 ASR/RVS 身份待澄清候选（README §4）"),
    # --- C2 双档链 2 ---
    ("CHU","B3","migration/species/chum_salmon.md","003","C2_DUAL_TIER","Chum Salmon（大马哈鱼）","@ChumSalmonMigrationSpatialProfile","",
     ["OCEAN/MIGRATION/SPAWN = "+P_AXIS],"第1步近底水层软三档（CSV benthopelagic 锚）+第2步轴段三档（海洋↔河口↔产卵河段）"),
    ("SHA","B3","migration/species/american_shad.md","003","C2_DUAL_TIER","American Shad（美洲西鲱）","@AmericanShadMigrationSpatialProfile","",
     ["OCEAN/MIGRATION/SPAWN = "+P_AXIS],"第1步中上层水层软三档（CSV pelagic-neritic 锚）+第2步轴段三档"),
    # --- C3 门+单档 12 ---
    ("FGA","B2","normal/species/florida_gar.md","004","C3_GATED_TIER","Florida Gar（佛罗里达雀鳝）","@FgaVegetationStructureProfile","GATE_VEGETATION_EDGE:vegetation_edge_cover_present",
     ["浅水季节窗口 = 活性 condition premise（非空间分支）"],"门轴=植被缘掩体（伏击型第一判断=结构掩体先行）"),
    ("SGA","B3","normal/species/spotted_gar.md","004","C3_GATED_TIER","Spotted Gar（斑点雀鳝）","@SpgWeedySlackStructureProfile","GATE_WEEDY_SLACK:weedy_slack_cover_present",
     [],"门轴=缓流植被掩体"),
    ("AST","B3","normal2/species/atlantic_sturgeon.md","004","C3_GATED_TIER","Atlantic Sturgeon（尖吻鲟）","@ATSEstuaryBottomProfile","GATE_ZONE:bottom_zone_present",
     [],"门轴=河口河底底层水层带（溯河鲟底栖触须特化）"),
    ("SNS","B3","normal2/species/shortnose_sturgeon.md","004","C3_GATED_TIER","Shortnose Sturgeon（短吻鲟）","@SNSRiverDeepBedProfile","GATE_ZONE:bottom_zone_present",
     [],"门轴=河底深槽底层水层带（小型鲟贴底特化）"),
    ("GPF","B4","normal2/species/grass_puffer.md","004","C3_GATED_TIER","Grass Puffer（星点东方鲀）","@GRPTidalSandBurrowProfile","GATE_BURYABLE_SUBSTRATE:buryable_substrate_present",
     [],"门轴=可埋沙泥底质（潮间带掩埋伏击特化）"),
    ("SSL","B4","normal2/species/northern_whiting.md","004","C3_GATED_TIER","Silver Sillago·沙鮻","@NWGSandHalfBuriedProfile","GATE_BURYABLE_SUBSTRATE:buryable_substrate_present",
     [],"门轴=可埋细沙底质（半埋伏击特化）；文件名 northern_whiting=内容沙鮻（文件名≠标题先例）"),
    ("WIT","B4","normal/species/witch_flounder.md","004","C3_GATED_TIER","Witch Flounder（女巫鲽）","@WcfMudBedStructureProfile","GATE_BURYABLE_SUBSTRATE:buryable_substrate_present",
     [],"门轴=可埋软泥底质（底埋伏击特化）"),
    ("YTF","B4","normal2/species/yellowtail_flounder.md","004","C3_GATED_TIER","Yellowtail Flounder（大西洋黄盖鲽）","@YTFSoftMudBuryProfile","GATE_BURYABLE_SUBSTRATE:buryable_substrate_present",
     [],"门轴=可埋软泥底质（鲽形目贴底伏击特化）"),
    ("FDR","B4","normal/species/freshwater_drum.md","004","C3_GATED_TIER","Freshwater Drum（淡水石首鱼）","@FwdSandPoolStructureProfile","GATE_POOL_STRUCTURE:pool_structure_present",
     [],"门轴=砂砾底/深潭结构存在"),
    ("BSB","B4","normal2/species/blackhead_seabream.md","004","C3_GATED_TIER","Blackhead Seabream（黑鲷）","@BSBReefSandEdgeProfile","GATE_REEF_EDGE:reef_edge_present",
     [],"门轴=岩礁/沙泥交错过渡结构（礁缘伏击）"),
    ("GRB","B1","patch/species/grass_carp.md","001","C3_GATED_TIER","Grass Carp（草鱼）","@GrbHerbivorePatchProfile","GATE_PATCH_PRESENCE:patch_presence",
     [],"门轴=植食资源+预投饵斑块存在（双构成同源评估——来源差异在世界侧事实供给层不购买档位分叉；prebait=resolver 义务 B1 已登记）"),
    ("SMA","B1","patch/species/smallmouth_follow.md","001","C3_GATED_TIER","Smallmouth Bass（小口黑鲈·跟随翻底）","@SmaDisturbanceFollowerProfile","GATE_DISTURBANCE_WINDOW:disturbance_window_active",
     [],"门轴=扰动窗口内扰动事件存在（事件驱动机会；无扰动=本面零权重，常态分布由其它程序面承载——本程序只表达机会追随面；disturbance_events=世界侧事实）"),
    # --- C4 夜行低光 5 ---
    ("WEL","B3","normal2/species/wels_catfish_feeding.md","004","C4_NOCTURNAL","Wels Catfish（欧洲巨鲶·摄食面）","@WCFNightHabitatProfile","",
     [],"夜行底板轴=洞穴/深潭（大型伏击鲶方向）；B3 洄游批 WEL 摄食面文件（与 guarding 面 WEL-GUARD 分批互指）"),
    ("FLA","B3","normal2/species/flathead_catfish.md","004","C4_NOCTURNAL","Flathead Catfish（铲鮰）","@FHCNightHabitatProfile","",
     [],"夜行底板轴=深潭/木石结构"),
    ("BUR","B3","normal2/species/burbot.md","004","C4_NOCTURNAL","Burbot（江鳕）","@BRBNightHabitatProfile","",
     [],"夜行底板轴=石底深潭（冬夜低温方向）"),
    ("GDE","B4","normal/species/goldeye.md","004","C4_NOCTURNAL","Goldeye（金眼鱼）","@GdeOpenWaterNightHabitatProfile","",
     [],"夜行底板轴=中上层开阔水面"),
    ("MOO","B4","normal2/species/mooneye.md","004","C4_NOCTURNAL","Mooneye（月眼鱼）","@MNYNightHabitatProfile","",
     [],"夜行底板轴=开阔水面（表层昆虫/小鱼方向）"),
    # --- C5a/C5b/C5c 底质链 5 ---
    ("GRH","B4","grazing/species/golden_redhorse.md","001","C5a_ZONE_SUBSTRATE","Golden Redhorse（金红马鱼）","@GoldenRedhorseSubstratePatchProfile","",
     ["常年绑定（若正文证实切换则由上游 premise 配置切换）"],"与河红马（同属 Moxostoma）链形同构——资源构成区分走 Profile 值域非结构"),
    ("RRH","B4","grazing/species/river_redhorse.md","001","C5a_ZONE_SUBSTRATE","River Redhorse（河红马鱼）","@RiverRedhorseSubstratePatchProfile","",
     ["常年绑定（同上）"],"轴=底栖大型无脊椎（软体/底栖昆虫方向）"),
    ("DRU","B1","patch/species/black_drum.md","001","C5a_ZONE_SUBSTRATE","Black Drum（黑鼓鱼）","@DruBottomForagerProfile","",
     [],"底质档=可翻性（翻底物理依赖：可翻软泥/难翻硬底/不可翻岩盘）；翻底痕迹（feeding_traces）=环境 owner 呈现义务，不进读取集"),
    ("BSK","B4","grazing/species/blue_sucker.md","001","C5b_TRIPLE_SOFT","Blue Sucker（长背亚口鱼）","@BlueSuckerSubstratePatchProfile","",
     ["常年绑定（同上）"],"第1步=近底带软三档（无硬门——benthopelagic 软定位；硬定位与否 [需正文]）——与 GRH/RRH/DRU 硬门形不同（步数同 4 但首步 GATE vs 软档=结构差异）"),
    ("SMB","B4","grazing/species/buffalo.md","001","C5c_ZONE_DEPTH","Buffalo（水牛鱼·Smallmouth Buffalo）","@BuffaloSubstratePatchProfile","",
     ["常年绑定（同上）"],"深度带档步=本鱼独有（CSV 深≥4m 注记——四亚口中仅本鱼有深度锚，链形与同批三鱼不同：五步链）"),
    # --- C6 滤食场 2 ---
    ("BHC","B2","field/species/bighead_carp.md","005","C6_FILTER_FIELD","Bighead Carp（鳙鱼）","@BhcPlanktonFieldEvaluatorProfile","",
     [],"三步=同一场评估（FieldSuitability）顺序判定非多因子并联；鲢鱼 S07 同型对照不建体沿用（B2）"),
    ("HER","B2","field/species/atlantic_herring.md","005","C6_FILTER_FIELD","Atlantic Herring（大西洋鲱）","@HerPlanktonFieldEvaluatorProfile","",
     ["季节产卵迁移 = lifecycle premise（配置级切换因子集，不在本 body 内分支）"],"群游集聚并入分档槽值域（coverage #17 判——非独立程序步）"),
    # --- C7 护巢锚 4 ---
    ("BLU","B1","guarding/species/bluegill.md","002","C7_GUARD_ANCHOR","Bluegill Sunfish（蓝鳃太阳鱼）","@BluegillColonyNestSuitabilityProfile","",
     ["殖民地巢群繁殖资格已在路由面判定（本步不重复结算 premise）"],"锚=殖民地巢群；推导 Tier A：C06 建立期选址→照护期占位；返回类型=Guarding SpatialDistributionWeight（与分布链不同）"),
    ("ARA","B3","guarding/species/arapaima.md","002","C7_GUARD_ANCHOR","Arapaima（巨骨舌鱼）","@ArapaimaBroodHabitatSuitabilityProfile","",
     ["稚鱼群存在与洪水位相已在路由面结算（§8.5 anti-double-counting）；漫滩可及性=空间事实"],"锚=洪泛漫滩稚鱼群移动锚（锚门含漫滩可及性）；Tier B：R06 FR3「洪水护幼」一句方向级"),
    ("RBP","B3","guarding/species/red_bellied_piranha.md","002","C7_GUARD_ANCHOR","Red-bellied Piranha（红腹食人鱼）","@PiranhaNestSuitabilityProfile","",
     ["护巢资格已在路由面判定"],"锚=root_spawn 树根卵体；Tier B：R06 FR3「树根护卵」一句方向级"),
    ("HNC","B4","guarding/species/hornyhead_chub.md","002","C7_GUARD_ANCHOR","Hornyhead Chub（双点美鱥）","@HornyheadStoneNestSuitabilityProfile","",
     ["巢体存在事实已在路由面判定（C4）"],"锚=雄鱼所筑石巢（构建型：选址适配先于守位）；Tier B：R07 FR3「石巢筑造+守护」"),
    # --- C8 追击 PLAIN 形 14 ---
    ("TAI","B3","normal/species/taimen.md","004","C8_PLAIN_DUALSLOT","Siberian Taimen（哲罗鲑）","@TmnLargeForageProfile","",
     [],"槽1=鱼类猎物场（大型饵鱼）/槽2=深潭激流结构；**表达文件投影=PLAIN_FACTOR_COMBINE（双槽+COMBINE）与 census B3 归 SINGLE 分歧——本重跑按文件链形记录**"),
    ("BLP","B3","normal2/species/black_piranha.md","004","C8_PLAIN_DUALSLOT","Black Piranha（黑食人鱼）","@BKPForageProfile","",
     [],"槽1=静水小鱼猎物场/槽2=浊水植被河道；同上 PLAIN 投影分歧"),
    ("GW","B3","normal2/species/giant_wolffish.md","004","C8_PLAIN_DUALSLOT","Giant Wolffish（巨狼鱼）","@GWFForageProfile","",
     [],"槽1=小鱼无脊椎猎物场/槽2=急流岩礁河道"),
    ("RFP","B3","normal2/species/redfin_pickerel.md","004","C8_PLAIN_DUALSLOT","Redfin Pickerel（红鳍狗鱼）","@RFPForageProfile","",
     [],"槽1=小型鱼群猎物场/槽2=植被缓流结构"),
    ("DS","B3","normal2/species/chinese_sleeper.md","004","C8_PLAIN_DUALSLOT","Chinese Sleeper（葛氏鲈塘鳢）","@CHSForageProfile","",
     [],"槽1=静水小鱼无脊椎/槽2=植被泥底池塘；census B3 归 SINGLE（静态 structure 11 组）与文件追击 PLAIN 投影分歧"),
    ("PBF","B3","normal2/species/pacific_bluefin.md","004","C8_PLAIN_DUALSLOT","Pacific Bluefin Tuna（太平洋蓝鳍金枪鱼）","@PBFForageProfile","",
     [],"槽1=跨洋鱼群猎物场/槽2=温带开阔洋"),
    ("GT","B3","normal2/species/giant_trevally.md","004","C8_PLAIN_DUALSLOT","Giant Trevally（牛港鲹）","@GTVForageProfile","",
     [],"槽1=礁缘鱼群猎物场/槽2=礁盘开放水"),
    ("HAL","B3","normal/species/atlantic_halibut.md","004","C8_PLAIN_DUALSLOT","Atlantic Halibut（大西洋大比目鱼）","@AthDemersalForageProfile","",
     [],"槽1=底层鱼类猎物场/槽2=砂底深水大陆架"),
    ("GG","B3","normal2/species/giant_grouper.md","004","C8_PLAIN_DUALSLOT","Giant Grouper（鞍带石斑鱼）","@GGPForageProfile","",
     [],"槽1=礁区猎物场（鱼/龙虾）/槽2=岩礁洞穴"),
    ("POR","B4","normal/species/porbeagle.md","004","C8_PLAIN_DUALSLOT","Porbeagle（鼠鲨）","@PblSchoolingForageProfile","",
     [],"槽1=鲱形类群游猎物场/槽2=开放水温跃层"),
    ("RKB","B4","normal2/species/rock_bream.md","004","C8_PLAIN_DUALSLOT","Rock Bream（条石鲷）","@RCBForageProfile","",
     [],"槽1=底栖硬壳猎物场（贝/海胆）/槽2=岩礁结构"),
    ("WIN","B4","normal2/species/winter_flounder.md","004","C8_PLAIN_DUALSLOT","Winter Flounder（美洲拟鲽）","@WNFForageProfile","",
     [],"槽1=底栖无脊椎小鱼猎物场/槽2=砂泥底近岸"),
    ("SMF","B4","normal2/species/summer_flounder.md","004","C8_PLAIN_DUALSLOT","Summer Flounder（大西洋牙鲆）","@SMFForageProfile","",
     [],"槽1=底层小鱼猎物场/槽2=砂底大陆架"),
    ("SAI","B4","normal/species/saithe.md","004","C8_PLAIN_DUALSLOT","Saithe（绿青鳕）","@SthMidwaterForageProfile","",
     [],"槽1=中上层鱼群猎物场/槽2=开放水岩礁缘"),
]


def build():
    out = []
    for (code, batch, path, fix, ck, species, profile, gate, premises, note) in MEMBERS:
        c = CLUSTERS[ck]
        if ck == "C3_GATED_TIER":
            gname, gguard = gate.split(":")
            ops = steps((gname, ()), ("EVAL_TYPED_FIELD_OR_FACTOR", ()),
                        ("NORMALIZE_WEIGHT", (1,)))
            branches = [GATE(gguard), c["branches_tier"]]
        else:
            ops = c["ops"]
            branches = c["branches"]
        sketch = (f"【顺序还原重跑盲体｜REP-ORDER-FIX-{fix}】判断链={c['chain']}。"
                  f"实例注记：{note}。链形转写自 {path} §2.2（文件冻结输入，"
                  f"WORKING/NOT AUTHORITY；档位成员=Profile 值域不冻结 [需正文]，"
                  f"Story 正文到达后校准——顺序/档位差异本身=LogicTemplate 判据）。")
        body = {
            "program_id": f"P-RS1-{code}-BAKE",
            "story_id": f"CENSUS-RERUN-SINGLE-001-{code}",
            "species_id": code,
            "surface": "Bake",
            "incoming_premises": premises,
            "human_readable_sketch": sketch,
            "ordered_steps": ops,
            "branches": branches,
            "combine": c["combine"],
            "return_type": c["ret"],
            "instance_noise": {"species": species, "profile": profile, "constants": {}},
            "helpers": [],
            "source_evidence_ids": [f"{FA}/{path}#REP-ORDER-FIX-{fix}"],
            "open_semantics": ["档位成员与阈值=Profile 值域不冻结 [需正文]",
                               "顺序还原=CSV/批内互指方向级推导，Story 正文到达后校准"],
            "cluster_hint_blind": ck,  # 盲阶段自聚类注记（非 registry 信息）
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
    assert len(progs) == 61, len(progs)
    codes = [p["species_id"] for p in progs]
    assert len(set(codes)) == 61
    (BATCH / "blind_programs.jsonl").write_text(
        "\n".join(json.dumps(p, ensure_ascii=False) for p in progs) + "\n",
        encoding="utf-8")
    from collections import Counter
    print("frozen:", len(progs), "programs")
    print(Counter(p["cluster_hint_blind"] for p in progs))
