# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-003 (RB-3) 终局重跑末批——盲体生成器。

批型=TRUTH_REBUILD_RERUN（HRQ-REBUILD-SCOPE-001 用户终局裁决授权；RB-1/RB-2 同工序范式）。
输入=truth_rebuild_queue 两组 118 项：
  - AMB 四层链第 4 层（B7 110）＝P-B7-*-BAKE AMB vs SINGLE v1 转真形
  - C9 立族材料 4（P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE 栖息面——面级守恒独立推导，
    不复用 RB-2 已推导的护巢面真形）
  - brooted 挂起终裁 2（P-B5-ARO-RESP / P-B0-TIL3-RESP[queue 笔误：本体=P-B7-TIL3-RESP，
    registry v9 行内 blind_hash=3e1cf6343317da2c 为 P-B7-TIL3-RESP]）
  - form_hold 挂起终裁 2（P-B5-CSL-RESP / P-B7-CSN1-RESP）
证据层：A=CENSUS-B7 input_snapshots story 快照（story_NNN.md，112 story 全档）；
B=B 系列表达文件 §0（REP-WORDING 已对齐文本）；C=fish-reference-20260908.csv；
RB1/RB2=前两批判档冻结真形（同鱼对账/复用轨）。
逐鱼顺序推导纪律=authoring_work_standards §5/§6.2（从证据推序，禁默认平铺/禁套约定序；
顺序证据不足标 order_undetermined——本批无此情形，全部鱼有可用主句锚）。
渐进累积语义=§6.1（无合并步；三档=全额/×衰减/×0.01 软出局立即返回）。
盲纪律：本脚本产出 blind_programs.jsonl（sha256+registry_seen=false），写盘完成先于
template_registry.yaml 首次打开（时序=manifest freeze_history + registry sha256 断言）。
程序 ID 约定：P-RB3-<CODE>-BAKE / P-RB3-<CODE>-HAB-BAKE / P-RB3-<CODE>-RESP；story ID：
CENSUS-REBUILD-003-<CODE>。
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCH = Path(__file__).parent
QIDS = json.load(open(BATCH / "queue_ids.json", encoding="utf-8"))

T3 = ["preferred=全额", "tolerated=×衰减(不清零)", "excluded=×0.01 软出局立即返回"]
T2 = ["成立=进入下一步", "不成立=EARLY_RETURN 返回 0"]
TSLOT = ["槽内=全额", "槽邻=×衰减(不清零)", "槽外=×0.01 软出局立即返回"]

CSV = "outputs/fish-reference-20260908/fish-reference-20260908.csv"
B7S = "fish_logic_census/batches/CENSUS-B7/input_snapshots/story_{n}.md"
B7B = "fish_logic_census/batches/CENSUS-B7/blind_programs.jsonl#P-B7-{c}-BAKE"
RB1B = "fish_logic_census/batches/CENSUS-REBUILD-001/blind_programs.jsonl#P-RB1-{c}-BAKE"
RB2B = "fish_logic_census/batches/CENSUS-REBUILD-002/blind_programs.jsonl#P-RB2-{c}-BAKE"
RS1HAB = "fish_logic_census/batches/CENSUS-RERUN-SINGLE-001/blind_programs.jsonl#{p}"
LA = ["A=frozen census story snapshot (Tier A, B7 batch)"]
LAB = ["A=frozen census story snapshot (Tier A, B7 batch)",
       "B=B-series expression file §0 chain declaration (Tier B constrained restoration - NOT copied; order re-derived per-fish)",
       "C=fish-reference-20260908.csv eco-morphology"]

def ev(op, axis):
    return {"op": op, "axis": axis, "tiers": list(T3)}

def gate(op, axis):
    return {"op": op, "axis": axis, "tiers": list(T2), "gate_semantics": "binary EARLY_RETURN"}

def slot(axis):
    return {"op": "APPLY_DYNAMIC_SPATIAL_SLOT", "axis": axis, "tiers": list(TSLOT)}

def branches_of(steps):
    out = []
    for s in steps:
        if s.get("gate_semantics"):
            out.append({"kind": "GATE", "guard": s["axis"]})
        elif s["op"] == "APPLY_DYNAMIC_SPATIAL_SLOT":
            out.append({"kind": "IF3_SLOT_VALUE", "guard": s["axis"]})
        else:
            out.append({"kind": "IF3_PROGRESSIVE", "guard": s["axis"]})
    return out

def sketch_of(steps, note):
    parts = []
    for s in steps:
        if s.get("gate_semantics"):
            parts.append("GATE[" + s["axis"] + "]")
        elif s["op"] == "APPLY_DYNAMIC_SPATIAL_SLOT":
            parts.append("SLOT[" + s["axis"] + "]")
        else:
            parts.append("EVAL[" + s["axis"] + "]")
    return ("【RB-3 终局顺序还原重跑真形】渐进累积链（无合并步）：" + " → ".join(parts)
            + "。每 EVAL 步三档=全额/×衰减/×0.01 软出局立即返回；GATE 硬门 EARLY_RETURN；"
            + "SLOT 槽位三档。每步 EVAL→三档→乘入 running weight。" + note)

F = []  # (code, snap_no, species, premises, steps, ret, family_target, related, basis, evid, open, reuse)

def add(code, snap, sp, prem, steps, ret, fam, rel, basis, evid, openq, reuse=None):
    F.append(dict(code=code, snap=snap, sp=sp, prem=prem, steps=steps, ret=ret,
                  fam=fam, rel=rel, basis=basis, evid=evid, open=openq, reuse=reuse))

# ===========================================================================
# 第 4 层 B7 110 —— B01 系（R01 机构 story 36）
# ===========================================================================
add("WAL2", "001", "玻璃梭鲈 Walleye（Sander vitreus）",
 ["视觉 = 眼部反光结构（tapetum）低光视觉特化——低光结构缘为其空间行为第一约束",
  "diel = 晨昏浅区/白天深水遮蔽浑水（非纯夜行——story 明言不是所有种群只在夜间摄食）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "lowlight_structure_base（低光结构底板——深水结构缘/遮蔽/浑水带）"),
  slot("low_light_night_slot（晨昏低光槽——白天深水遮蔽=槽邻衰减档）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: RB 主句首句=视觉生理特化（反光结构→低光视觉）——结构缘栖息为第一约束（生理特化先行）",
  "B: normal2/walleye_feeding.md §0 夜行组样板（夜行底板栖息档位→低光槽——槽位置=§11.5 判例固定原位）",
  "C: benthopelagic 0-27m / 夜间活跃 / 1.1-29°C"],
 [B7S.format(n="001"), CSV + "#WAL2", "outputs/full_authoring/normal2/species/walleye_feeding.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["WAL2"], B7B.format(c="WAL2")],
 ["与 RB-2 WAG（B01-S02 繁殖浅滩面 GC 形）同种不同 story——双 story 去重联动，各自消费"])

add("CRA1", "002", "黑斑刺盖太阳鱼 Black Crappie（Pomoxis nigromaculatus）",
 ["stage = 幼鱼浮游→较大个体鱼类（体型阶段 Context，配置级）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "clear_structure_band（清水结构带——植被/掩体结构区）"),
  ev("EVAL_TYPED_PREY_FACTOR", "stage_graded_prey_field（阶段分级猎物场——浮游幼体→饵鱼成体）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: RB 主句『清水、植被和结构影响栖息与觅食』——结构栖息先行；食谱=体型阶段（premise）",
  "B: normal/black_crappie.md §0 机会组样板（单步机会场——story 侧两维（结构+阶段猎物）分辨率高于样板）",
  "C: benthopelagic / 晨昏活跃 / 14-30.6°C"],
 [B7S.format(n="002"), CSV + "#CRA1", "outputs/full_authoring/normal/species/black_crappie.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CRA1"], B7B.format(c="CRA1")],
 [])

add("CRA2", "003", "黑斑刺盖太阳鱼 Black Crappie（繁殖雄鱼，Pomoxis nigromaculatus）",
 ["guard_state = 雄鱼筑巢并护卵至孵化（Illinois DNR/USFWS 本种证据——构建型巢体）",
  "motivation_open = 近巢咬饵的饥饿/防御动机不可分（story Scope 限定）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "nest_anchor_present（巢锚存在性——雄鱼筑巢，构建型）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "nest_site_quality（巢址适配——沙砾浅水巢床三档）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（与巢锚距离/朝向关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（巢区局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA", None,
 ["A: story RB『雄鱼筑巢并护卵至孵化』——筑巢=构建型锚（建立期选址先行→照护期占位在后）",
  "C: 14-30.6°C 水温资料带（第 4 步温度轴方向锚）",
  "MUT 批判例②落位表：巢构建→nest（本批独立推导同向）"],
 [B7S.format(n="003"), CSV + "#CRA2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CRA2"], B7B.format(c="CRA2")],
 ["与 CRA1（S03 摄食 story）同种双 story——各自消费+去重联动"])

add("GAR1", "004", "鳄雀鳝 Alligator Gar（Atractosteus spatula）",
 [], [], "SpatialDistributionWeight", "NOS", None,
 ["A: story 主体=取饵初次接受边界（TargetFeeding 只解释最初接受——owner 推论原样）；无空间分布新证据",
  "B: normal/alligator_gar.md §0/§2.2＝BOUNDARY-DECL 显式声明（Bake 面无 Story 派生程序——顺序还原不适用）",
  "C: demersal（档案锚——无 story 空间程序证据，不冒充）"],
 [B7S.format(n="004"), "outputs/full_authoring/normal/species/alligator_gar.md#S0-S2.2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["GAR1"], B7B.format(c="GAR1")],
 ["真形=NO_SURFACE_EFFECT（显式理由：取饵接受边界/携行挂钩为 Encounter/Conversion 侧交互实例，非 Bake 空间分布证据——B 文件 BOUNDARY-DECL 直证）；Response 面档位展开照常（不在本面）"],
 None)

add("GAR3", "005", "鳄雀鳝 Alligator Gar（繁殖洪水入口 story）",
 ["lifecycle = 繁殖依赖温度与淹水浅滩/植被通达（成功繁殖并非每年必然）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "floodplain_spawn_access_axis_segment（洪泛繁殖通达轴段——淹水浅滩/植被入口）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=繁殖洪水入口（P05）；『水位与繁殖入口由 Spatial/Lifecycle 提供，与 GAR-0 普通捕食分开』",
  "B: normal/alligator_gar.md §0 双 story 分工（S05 取饵面 BOUNDARY / S06 本面）",
  "C: demersal / 17-27°C"],
 [B7S.format(n="005"), CSV + "#GAR3", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["GAR3"], B7B.format(c="GAR3")],
 [])

add("YEP1", "006", "黄鲈 Yellow Perch（Perca flavescens）",
 ["stage = 浮游→底栖无脊椎→鱼类（成长食谱切换，配置级 Context）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "vegetation_depth_band（植被掩体水层带）"),
  ev("EVAL_TYPED_PREY_FACTOR", "stage_graded_prey_field（阶段分级猎物场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: RB 主句『植被、掩体和食物所在水层影响觅食』——植被掩体水层先行；『体型和局部资源为 Context，实际饵为 Discrete Target』（体型=premise）",
  "B: normal/yellow_perch.md §0 追击组（受限还原 unordered——story 侧两维分辨率更高）",
  "C: benthopelagic 0-56m / 晨昏活跃"],
 [B7S.format(n="006"), CSV + "#YEP1", "outputs/full_authoring/normal/species/yellow_perch.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["YEP1"], B7B.format(c="YEP1")],
 [])

add("YEP2", "007", "黄鲈 Yellow Perch（产卵迁移 story）",
 ["lifecycle = 适合底质/植被处产出胶状卵带（Chesapeake 产卵栖地调查限定）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "spawning_vegetation_band_axis_segment（产卵植被底质带轴段——胶状卵带附着栖地入口）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=产卵栖地入口（P05）；『繁殖阶段改变 Spatial/Condition；卵带是环境事实』",
  "C: benthopelagic / 晨昏活跃"],
 [B7S.format(n="007"), CSV + "#YEP2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["YEP2"], B7B.format(c="YEP2")],
 ["与 YEP1（S08 摄食 story）同种双 story——各自消费+去重联动"])

add("BIB1", "008", "大口牛胭脂鱼 Bigmouth Buffalo（Ictiobus cyprinellus）",
 ["filter_evidence = 滤取浮游食物证据存在；密度/动作/连续机会因果链未闭合（story 限定）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "plankton_filter_field（浮游滤食场浓度——分布式食物场）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（typed FoodField evaluator——先问输入范围、机会寿命和去重）",
  "B: grazing/buffalo.md §0『滤食式 FieldFeeding 为大口水牛鱼 C10 故事域，种级区分』（B 文件为 I. bubalus 底质吸食面——本面按 story P03 走场形）",
  "C: benthopelagic 4m+ / 早晨活跃"],
 [B7S.format(n="008"), CSV + "#BIB1", "outputs/full_authoring/grazing/species/buffalo.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BIB1"], B7B.format(c="BIB1")],
 [])

add("BIB2", "009", "大口牛胭脂鱼 Bigmouth Buffalo（水位升高繁殖 story）",
 ["lifecycle = 温度与水位上升后成群进入浅水沼泽繁殖；卵无人照护（聚集≠守巢）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "flood_spawning_access_axis_segment（洪泛繁殖通达轴段——浅水沼泽入口）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=水位通达改变找鱼位置（P05）；『水位和阶段更新 Spatial/Condition，群聚不单独购买 Group』",
  "C: benthopelagic / 15.5-30°C"],
 [B7S.format(n="009"), CSV + "#BIB2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BIB2"], B7B.format(c="BIB2")],
 ["与 BIB1（S10 滤食 story）同种双 story——各自消费+去重联动"])

add("BRT3", "010", "褐鳟 Brown Trout（生活史共存 story，Salmo trutta）",
 ["ecotype = 终生淡水定居与入海/河口生长两生态型同河共存繁殖（lifecycle premise 配置级）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "ecotype_bound_axis_segment（生态型绑定轴段——定居河段↔河口/海区）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=生活史生态型分野（P05）；『海行、湖河定居改变找鱼水域与时间』",
  "B: normal/brown_trout.md §0（摄食面另一 story 域）",
  "C: pelagic-neritic / anadromous / 18-24°C"],
 [B7S.format(n="010"), CSV + "#BRT3", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BRT3"], B7B.format(c="BRT3")],
 ["与 RB-2 BRT12（褐鳟摄食 story FF 形）同种三 story（S13/S15 vs B1 起源 story）——去重联动，story 级各自消费"])

add("BRT4", "011", "褐鳟 Brown Trout（繁殖竞争 story）",
 ["breeding = 雌鱼选择与释放后雄鱼竞争；支配关系改变配对结果（无 Nest guard 前提——story 明言 P04 仅为竞争参照）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "breeding_arena_axis_segment（求偶竞争场轴段——配对发生区）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=繁殖竞争（无守巢前提）；『繁殖 Condition + 对手/配偶关系』——空间证据分辨率=配对场单轴段",
  "C: pelagic-neritic / 晨昏活跃"],
 [B7S.format(n="011"), CSV + "#BRT4", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BRT4"], B7B.format(c="BRT4")],
 ["与 BRT3/BRT12 同种多 story——去重联动"])

add("RED1", "012", "美国红鱼 Red Drum（Sciaenops ocellatus）",
 [],
 [ev("EVAL_TYPED_PREY_FACTOR", "benthic_crustacean_prey_patch（底栖甲壳/小鱼斑块——ResourcePatch 组织机会）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "shallow_grass_band（浅水草区带——尾露/巡游位）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: RB 主句『头朝下在底部取食而露尾，也可在水层中摄食。浅水草区和甲壳类/小鱼资源为搜索线索』——行为/资源主句先行（食性主句先行=FF 方向学），浅水草区=搜索线索次之",
  "B: normal2/red_drum.md §0 追击组（受限还原 unordered）",
  "C: demersal 10m+ / 晨昏活跃 / 15-26°C"],
 [B7S.format(n="012"), CSV + "#RED1", "outputs/full_authoring/normal2/species/red_drum.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RED1"], B7B.format(c="RED1")],
 [])

add("RED2", "013", "美国红鱼 Red Drum（潮位水深幼成栖地 story）",
 ["stage = 幼鱼多利用海湾、成鱼更多外海（生活史水平分野，配置级）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "tidal_depth_layer（潮位日内水深层——垂直维）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "juvenile_adult_corridor_axis（幼成湾区-外海廊道轴——水平维）")],
 "SpatialDistributionWeight", "LA", None,
 ["A: story 主体两维直证『潮位和温度可改变日内水深』＋『幼鱼多利用海湾、成鱼更多外海』——垂直层+水平廊道两独立维（RB-2 csv_anchor_standard：廊道+垂直层两步）",
  "C: demersal / 晨昏活跃 / 15-26°C"],
 [B7S.format(n="013"), CSV + "#RED2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RED2"], B7B.format(c="RED2")],
 ["与 RED1（S16 摄食 story）同种双 story——各自消费+去重联动"])

add("PIK1", "014", "白斑狗鱼 Northern Pike（植被伏击 story，Esox lucius）",
 [],
 [gate("GATE_COVER_EXISTENCE", "vegetation_cover_present（沉水植被/草洞掩体存在——视觉伏击位，不成立=出局）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "vegetation_ambush_quality（植被缘掩体结构质量三档）")],
 "SpatialDistributionWeight", "GC", None,
 ["A: story RB『多为视觉伏击捕食者，常从下方接近猎物』＋SS『在植被边缘和结构附近呈现仿鱼饵』——植被掩体=伏击位存在性先行",
  "B: normal/northern_pike_ambush.md §0 判断顺序=GATE_VEGETATION_COVER 门→掩体结构档（与 S20 Static Habitat 是同种两 story 两读法——census 判语互指）",
  "C: pelagic 0-30m / 晨昏活跃"],
 [B7S.format(n="014"), CSV + "#PIK1", "outputs/full_authoring/normal/species/northern_pike_ambush.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["PIK1"], B7B.format(c="PIK1")],
 ["与 RB-2 PIK19（白斑狗鱼 northern_pike_spawn.md 繁殖面 TS 轴段）同种双 story 不同面——去重联动（B 文件互指判语原样）"])

add("MUL1", "015", "鲻鱼 Flathead Grey Mullet（底质附着 story，Mugil cephalus）",
 ["action_set = 持续游动/底部颗粒捕获/表面颗粒捕获与吐出（2022 圈养动作区分——动作存在≠切换条件闭合）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "intertidal_substrate_matrix（基质连续处理带——底泥/附着物/水气界面三位基质）"),
  ev("EVAL_TYPED_PREY_FACTOR", "detritus_biofilm_field（碎屑-生物膜资源场——连续基质处理）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story RB 主句『利用底泥、附着物，也可在水气界面取食』——基质（食物载体）先行，资源场次之（Compression Candidate P06 连续基质）",
  "B: normal2/grey_mullet.md §0 机会组（CSV 杂食与刮食形态 P06 边界张力登记——story 侧证实连续基质）",
  "C: benthopelagic 0-120m / 早晨活跃 / catadromous"],
 [B7S.format(n="015"), CSV + "#MUL1", "outputs/full_authoring/normal2/species/grey_mullet.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MUL1"], B7B.format(c="MUL1")],
 [])

add("MUL2", "016", "鲻鱼 Flathead Grey Mullet（近岸生长外海产卵 story）",
 ["lifecycle = 成鱼成群外海繁殖，幼体进入近岸/河口生长（觅食底质与繁殖位置分离）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "catadromous_corridor_axis_segment（降海廊道轴段——近岸生长区↔外海繁殖区）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=生命周期空间分离（P05）；『Lifecycle/Spatial 描述位置与阶段；同种群游不单独购买 Group』",
  "C: benthopelagic / catadromous"],
 [B7S.format(n="016"), CSV + "#MUL2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MUL2"], B7B.format(c="MUL2")],
 ["与 MUL1 同种双 story——去重联动"])

add("RAI2", "017", "虹鳟 Rainbow Trout（漂流食物脉冲 story，Oncorhynchus mykiss）",
 ["seasonal_context = 鲑繁殖季卵/肉来源（Kanektok 实例限定——不泛化所有虹鳟水域）"],
 [ev("EVAL_TYPED_PREY_FACTOR", "salmon_egg_carcass_pulse_patch（鲑卵/尸体食物脉冲斑块——季节性猎物脉冲）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "drift_bottom_lane_band（漂流通道近底带——不受拖拽漂流呈现位）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: RB 主句『ADFG 的 Kanektok 实例描述鲑繁殖季卵/肉来源以及自然漂流呈现』——食物脉冲主句先行（季节脉冲型=FF 同 BRT12 形），水层配重接近底部次之",
  "C: benthopelagic / anadromous / 10-24°C"],
 [B7S.format(n="017"), CSV + "#RAI2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RAI2"], B7B.format(c="RAI2")],
 [])

add("RAI3", "018", "虹鳟 Rainbow Trout（定居/钢头共存 story）",
 ["ecotype = 定居虹鳟与海行钢头鳟同种不同生活史；个体可重复繁殖"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "ecotype_bound_axis_segment（生态型绑定轴段——定居淡水↔海行返河）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=生活史分野（P05）；『搜索水域和返回时序因生活史不同』",
  "C: benthopelagic / anadromous"],
 [B7S.format(n="018"), CSV + "#RAI3", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RAI3"], B7B.format(c="RAI3")],
 ["与 RAI2 同种双 story——去重联动"])

add("AEL1", "019", "美洲鳗鲡 American Eel（Anguilla rostrata）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "benthic_cover_base（底层掩体底板——植物/倒木隐蔽带）"),
  slot("low_light_night_slot（低光夜槽——夜间摄食窗口）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: RB 主句『白天在植物、倒木等处隐蔽，夜间摄食』——掩体底板先行+夜槽（昼夜和遮蔽为 Context/Spatial）",
  "B: normal/american_eel.md §0 夜行组样板（夜行底板栖息档位→低光槽）",
  "C: demersal 0-464m / 夜间活跃 / catadromous"],
 [B7S.format(n="019"), CSV + "#AEL1", "outputs/full_authoring/normal/species/american_eel.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["AEL1"], B7B.format(c="AEL1")],
 ["与 AEL2 同种双 story——去重联动"])

add("AEL2", "020", "美洲鳗鲡 American Eel（降海生殖迁移 story）",
 ["lifecycle = 海洋幼体→沿岸/淡水生长→返 Sargasso 繁殖；障碍物影响迁移通达"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "catadromous_corridor_axis_segment（降海廊道轴段——生长区↔繁殖海区通达）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=阶段与连通性决定出现水域（P05）；『Lifecycle 与 Spatial 通达；阶段存在不必创建 Mode』",
  "C: demersal / catadromous"],
 [B7S.format(n="020"), CSV + "#AEL2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["AEL2"], B7B.format(c="AEL2")],
 [])

add("SOK1", "021", "红鲑鱼 Sockeye Salmon（浮游滤食证据 story，Oncorhynchus nerka）",
 ["stage_ambiguity = 幼鱼食谱随大小季节变化（kokanee/海行/幼鱼不互相替换——阶段条件保留）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "zooplankton_field（浮游食物场浓度——鳃耙支持浮游摄食）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（若行为证据成立可测试 typed field evaluator——本 story 正文证实浮游摄食证据面）",
  "B: migration/sockeye_salmon.md §0 滤食性登记（按 story 证实走 P03 域——本面即其预留复核点）",
  "C: pelagic-oceanic / 滤食性 / selective plankton feeding / 晨昏活跃"],
 [B7S.format(n="021"), CSV + "#SOK1", "outputs/full_authoring/migration/species/sockeye_salmon.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SOK1"], B7B.format(c="SOK1")],
 [])

add("SOK2", "022", "红鲑鱼 Sockeye Salmon（返河繁殖 story）",
 ["lifecycle = 返河繁殖与生长期食物差异；捕获动机未定（snagging/flossing 不当机构结论）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "anadromous_return_corridor_axis_segment（溯河返廊道轴段——海洋觅食区↔产卵湖）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=Lifecycle/Spatial 解释返河（P05）；实际捕获须另核主动响应",
  "C: pelagic-oceanic / anadromous"],
 [B7S.format(n="022"), CSV + "#SOK2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SOK2"], B7B.format(c="SOK2")],
 ["与 SOK1 同种双 story——去重联动"])

add("SAL1", "023", "大西洋鲑鱼 Atlantic Salmon（Salmo salar）",
 ["lifecycle = 淡水生长期与海洋阶段食物不同；返河摄食不能写成绝对零（支流样本分歧）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "anadromous_corridor_axis_segment（溯河廊道轴段——海洋肥育区↔河口↔产卵河段）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=水域/阶段影响找鱼（P05）；『Lifecycle/Condition/Spatial 先解释差异，不必新建 Return Mode』",
  "B: migration/atlantic_salmon.md §0 判断顺序=premise 读取（OCEAN/MIGRATION/SPAWN 配置级）→阶段绑定轴段三档",
  "C: benthopelagic 0-210m / anadromous / 2-9°C"],
 [B7S.format(n="023"), CSV + "#SAL1", "outputs/full_authoring/migration/species/atlantic_salmon.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SAL1"], B7B.format(c="SAL1")],
 [])

add("SMA1", "024", "小口黑鲈 Smallmouth Bass（护巢营养竞争 story，Micropterus dolomieu）",
 ["guard_state = 雄鱼护巢/护幼（两实验营养-防御关系分歧——守护持续与当前食物反应不假设严格互斥）",
  "anchor_stages = 巢床（卵期）与稚鱼群（幼期）两阶段锚——Resolver 实例配置级切换，body 不设分支"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "nest_fry_anchor_present（巢/稚鱼锚存在性——nest_bed↔fry_school 实例切换）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "nest_site_quality（锚址适配三档）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（与锚距离/朝向关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（锚区局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA", None,
 ["A: story FCFI=P04（既存 guard Condition + nest/fry relation + 当前目标 meaning——并行候选不等于必须共同结算）",
  "B: guarding/smallmouth.md §0 锚点两阶段判例（§11.2 Fry Guard 泛化：同一模板锚差异=Resolver 实例切换不新增 BakeTemplate）；判断顺序=锚存在→锚适配→关系→局部温度",
  "C: benthopelagic 1-7m / 8.5-29.5°C"],
 [B7S.format(n="024"), CSV + "#SMA1", "outputs/full_authoring/guarding/species/smallmouth.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SMA1"], B7B.format(c="SMA1")],
 ["与 RB-2 SMA（smallmouth_follow.md 摄食面 GC 形）同种不同面——去重联动"])

add("PAD1", "025", "鸭嘴鲟 American Paddlefish（滤食输入边界 story，Polyodon spathula）",
 ["stage = 圈养亚成体 filter/particulate 行为（未观察到固定切换规律≠证明没有）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "plankton_filter_field（浮游滤食场浓度——连续机会输入）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（typed FoodField evaluator + 机会输入——先验证分布式资源是否不能由离散目标承载）",
  "B: normal/paddlefish_electro.md §0 双批分工（幼体电感受=另一 story 面——本面=CSV 行滤食面）",
  "C: demersal 2m+ / 滤食性 / filtering plankton / 全天活跃"],
 [B7S.format(n="025"), CSV + "#PAD1", "outputs/full_authoring/normal/species/paddlefish_electro.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["PAD1"], B7B.format(c="PAD1")],
 ["与 RB-2 PAD34（电感受面 TS）+PAD5（洄游面）同种三 story 三面——去重联动（电感知不进 Bake 判例维持）"])

add("PAD5", "027", "鸭嘴鲟 American Paddlefish（开放水体上游繁殖 story）",
 ["lifecycle = 利用开放水体并在繁殖季上移至适宜产卵地（觅食资源与繁殖通达分开）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "potamodromous_spawn_corridor_axis_segment（溯河产卵廊道轴段——开放水体↔上游产卵地）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=Lifecycle/Spatial 更新位置（P05）；捕获交 PAD-4，电感受和滤食另列",
  "C: demersal / potamodromous"],
 [B7S.format(n="027"), CSV + "#PAD5", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["PAD5"], B7B.format(c="PAD5")],
 ["同种三 story 去重联动（PAD1/PAD5/PAD34）"])

add("BLU2", "028", "蓝鳃太阳鱼 Bluegill Sunfish（护巢觅食食卵边界 story，Lepomis macrochirus）",
 ["guard_state = 护巢雄鱼存在替代繁殖策略；filial_cannibalism = 食卵受亲子关系/状态影响（非护巢与外部食物路径同时执行的证明）",
  "motivation_open = 近巢小饵可被摄食或防御攻击——两种原因无法单独识别（结算政策未定）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "colony_nest_anchor_present（殖民巢群锚存在性——预先建立并持续照护）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "colony_nest_site_quality（巢床结构适配三档）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（与巢群锚点距离/朝向关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（巢区局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA", None,
 ["A: story FCFI=P04（既存繁殖 Condition + Nest/Anchor relation；当前目标可有不同 meaning）",
  "B: guarding/bluegill.md §0 判断顺序=锚存在→锚适配（巢床结构三档）→关系评估→局部温度（建立期选址先行、照护期占位在后——C06 已审主张推导）",
  "C: benthopelagic / 1-36°C / 晨昏活跃"],
 [B7S.format(n="028"), CSV + "#BLU2", "outputs/full_authoring/guarding/species/bluegill.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BLU2"], B7B.format(c="BLU2")],
 ["与 RS1/RB-2 BLU（B 文件 §2.2 护巢面 canonical 源）同种同面不同证据源（story vs B 文件）——直验对照+去重联动"])

add("CCF1", "029", "斑点叉尾鮰 Channel Catfish（嗅味触觉底层 story，Ictalurus punctatus）",
 ["sensory = 味、嗅、触觉多通道寻找（气味扩散=sensory Context 非独立 FoodField）",
  "stage = 成鱼与幼鱼食谱、水层及昼夜位置可不同（配置级）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "gravel_bottom_base（砂砾底层底板）"),
  slot("low_light_night_slot（低光夜槽——夜间底层搜索窗口）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: RB 主句『利用味、嗅、触觉等寻找多样食物』+SS『机构钓法支持不同自然/气味饵及底层搜索』——底层底板先行+夜槽（气味=sensory Context 不另立面）",
  "B: normal/channel_catfish.md §0 夜行组样板（砂砾底夜行觅食）",
  "C: demersal 0-15m / 夜间活跃 / 10-31.6°C"],
 [B7S.format(n="029"), CSV + "#CCF1", "outputs/full_authoring/normal/species/channel_catfish.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CCF1"], B7B.format(c="CCF1")],
 ["与 CCF2 同种双 story——去重联动"])

add("CCF2", "030", "斑点叉尾鮰 Channel Catfish（洞巢照护 story）",
 ["guard_state = 雄鱼洞巢照护卵/幼鱼；受扰时可吃卵（机构概述，触发条件未实验验证）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "cavity_egg_anchor_present（洞巢卵锚存在性——利用型附着（洞巢非构建）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "cavity_site_quality（洞巢址适配三档）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（与洞巢锚关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（巢区局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA", None,
 ["A: story RB『两机构均记载雄鱼洞巢照护卵/幼鱼；TPWD 描述受扰时可吃卵』——洞巢=利用型附着（egg_mass 形式；MUT 批判例②落位表同向）",
  "C: demersal / 夜间活跃 / 10-31.6°C"],
 [B7S.format(n="030"), CSV + "#CCF2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CCF2"], B7B.format(c="CCF2")],
 ["吃卵与守护对象处理=story 限定（证据开放注记）"])

add("TIL2", "031", "罗非鱼 Nile Tilapia（刮食悬浮颗粒 story，Oreochromis niloticus）",
 ["action_set = 刮食+黏液截留颗粒+令颗粒再悬浮（动作存在≠完整切换条件）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "periphyton_suspended_field（附着-悬浮颗粒场——刮食基质与水柱悬浮连续场）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（typed field/substrate evaluator + 已有 Response；环境颗粒变化与鱼响应分开 owner）",
  "B: guarding/nile_tilapia.md §0 NormalFeeding 双通道（刮食+悬浮颗粒——live 例 3 表达；本面按 story P03 走场形）",
  "C: benthopelagic 0-20m / 植食性 / browsing on substrate / 全天活跃"],
 [B7S.format(n="031"), CSV + "#TIL2", "outputs/full_authoring/guarding/species/nile_tilapia.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["TIL2"], B7B.format(c="TIL2")],
 ["双通道汇总算子=Response 层 OPERATOR UNDEFINED 标注（B 文件注记原样）"])

add("TIL3", "032", "罗非鱼 Nile Tilapia（雄鱼巢区领地 story）",
 ["territory = 雄鱼建立繁殖领地；雌鱼取卵后离开并口孵（雄鱼领地与雌鱼所携幼体不是同一持久关系对象）",
  "adjacent_face = 雌鱼口哺面=B 文件 Brooding 退化链（brooted 终裁轨，另条目）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "territory_bound_axis_segment（雄鱼领地轴段——繁殖巢区防区）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story FCFI=Territory relation + reproductive Condition（P04 只作竞争参照，先区分领地与护卵）——本 story 冻结行=雄鱼领地面",
  "B: guarding/nile_tilapia.md §0（Brooding 面=雌鱼口哺退化链——分面记账，不在本面重复）",
  "C: benthopelagic / 全天活跃 / 13.5-33°C"],
 [B7S.format(n="032"), CSV + "#TIL3", "outputs/full_authoring/guarding/species/nile_tilapia.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["TIL3"], B7B.format(c="TIL3")],
 ["queue TRB-0219（本条）+TRB-0301（brooted 终裁=雌鱼口哺面）双条目；TRB-0301 program_id 前缀 P-B0 为 queue 笔误（registry v9 行内本体=P-B7-TIL3-RESP）"])

add("BDR2", "033", "黑鼓鱼 Black Drum（Pogonias cromis）",
 [],
 [gate("GATE_ZONE", "bottom_layer_zone（底层水层定位——demersal 硬定位，非底层=出局）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "substrate_workability（底质可翻性三档——触须/化学线索找底栖食物的物理依赖）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_prey_abundance（底栖猎物丰度三档——贝类等硬壳猎物斑块）")],
 "SpatialDistributionWeight", "ZS", None,
 ["A: story RB『利用触须/化学线索寻找底栖食物，用咽齿处理贝类等硬壳猎物』+FCFI=P02（底栖 ResourcePatch+typed prey traits）——翻底取食对底质可翻性有物理依赖：可翻性先于猎物丰度",
  "B: patch/black_drum.md §0 判断顺序=底层水层定位→底质可翻性档位→底栖猎物丰度档位（同序独立推导确认）",
  "C: demersal 10m+ / 晨昏活跃 / 18.5-28.5°C"],
 [B7S.format(n="033"), CSV + "#BDR2", "outputs/full_authoring/patch/species/black_drum.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BDR2"], B7B.format(c="BDR2")],
 [])

add("SEA2", "035", "海七鳃鳗 Sea Lamprey（Petromyzon marinus）",
 ["stage = 埋栖滤食幼体（ammocoete）→变态寄生→成熟繁殖期消化系统退化停食（三阶段 lifecycle premise）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "lamprey_stage_bound_axis_segment（阶段绑定轴段——幼体埋栖滤食位↔寄生附着↔繁殖通道）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=分阶段栖位分野（P05）；『Lifecycle/Condition 分阶段；幼体 field input 与实例化后寄生分别交适当 owner』",
  "C: demersal 1-4099m / anadromous / 夜间活跃"],
 [B7S.format(n="035"), CSV + "#SEA2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SEA2"], B7B.format(c="SEA2")],
 ["幼体滤食=场输入语义（owner=适当面）——本轴段只承载阶段空间分野"])

add("COD1", "036", "大西洋鳕鱼 Atlantic Cod（普通离散猎物 story，Gadus morhua）",
 [],
 [ev("EVAL_TYPED_PREY_FACTOR", "piscivore_benthic_prey_field（多鱼种-无脊椎猎物场——体型栖位影响食谱）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "shelf_demersal_band（大陆架底层带）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: RB 主句『以多种鱼类与无脊椎为食，体型和栖位影响食谱』——食性主句先行（猎物场），栖位带次之",
  "B: normal2/atlantic_cod_feeding.md §0 追击组（受限还原 unordered；CSV 行 P01 摄食面——双批分工：migration 批承载 S52 繁殖深度面）",
  "C: benthopelagic 0-600m / 全天活跃 / 0-15°C"],
 [B7S.format(n="036"), CSV + "#COD1", "outputs/full_authoring/normal2/species/atlantic_cod_feeding.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["COD1"], B7B.format(c="COD1")],
 ["与 RB-2 COD（atlantic_cod.md S52 繁殖深度面 TS）+COD2 同种三 story——去重联动"])

add("COD2", "037", "大西洋鳕鱼 Atlantic Cod（繁殖发声求偶 story）",
 ["courtship = 发声与求偶/竞争行为联系（圈养研究）；pollack 结果不外推为 cod（story 限定）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "spawning_aggregation_axis_segment（繁殖聚集场轴段——求偶/竞争发生区）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=求偶、对手关系与感官 Context 的繁殖聚集（无守巢前提）；空间证据分辨率=聚集场单轴段",
  "C: benthopelagic / 全天活跃"],
 [B7S.format(n="037"), CSV + "#COD2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["COD2"], B7B.format(c="COD2")],
 ["声学线索=研究/监测用途（story 判语）；与 COD1/RB-2 COD 同种三 story 去重联动"])

add("GRA2", "038", "草鱼 Grass Carp（流水繁殖亲鱼停食 story，Ctenopharyngodon idella）",
 ["lifecycle = 自然产卵依赖流动水及水位变化；养殖亲鱼临产前减少或停止进食（养殖语境限定）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "lotic_spawn_current_axis_segment（流水产卵轴段——河流通达决定繁殖出现位置）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story 主体=河流通达+繁殖期（P05）；『Lifecycle/Spatial 加限定 Condition；暂不增加 Spawn Mode』；停食=premise（F02）",
  "B: patch/grass_carp.md §0（P02 摄食面另一 story 域——双 story 分工）",
  "C: benthopelagic / potamodromous / 0-35°C"],
 [B7S.format(n="038"), CSV + "#GRA2", "outputs/full_authoring/patch/species/grass_carp.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["GRA2"], B7B.format(c="GRA2")],
 [])

# ===========================================================================
# 第 4 层 B7 110 —— FISH-R02 系（16）
# ===========================================================================
add("MAC1", "039", "大西洋鲭 Atlantic Mackerel（Scomber scombrus）",
 ["school = 季节性沿陆架移动的大型群体（群结构事实=发现层线索，非供给路由）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "moving_baitfish_plankton_field（移动饵场-浮游场浓度——鱼群随饵场走）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（移动 FoodField/饵鱼资源 + FieldFeeding——GroupPressure=Strong 仅表示群体是找鱼线索）",
  "SS: 先找移动饵场、鸟群和水层，再用高速或中速追猎——饵场=主体（场浓度单因子；水层=场所在维度不另立）",
  "C: pelagic-neritic 0-1000m / oceanodromous / 7.2-13.2°C"],
 [B7S.format(n="039"), CSV + "#MAC1", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MAC1"], B7B.format(c="MAC1")],
 [])

add("JCK1", "040", "日本竹荚鱼 Japanese Jack Mackerel（Trachurus japonicus）",
 ["school = 近岸群体（空间资源线索——统一响应状态无证据）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "plankton_smallfish_field（浮游-小鱼场浓度——混合构成）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（近岸 FoodField + current/temperature context + FieldFeeding——资源场先决定位置）",
  "B: field/jack_mackerel.md §0 滤食场三步（受限还原：水层→浓度→个体口径——story 级证据只支持场浓度单因子，B 层三步不采[RB-2 BHC/HER 判例同型]）",
  "C: pelagic-neritic 0-275m / 滤食性 / 10.8-16.8°C"],
 [B7S.format(n="040"), CSV + "#JCK1", "outputs/full_authoring/field/species/jack_mackerel.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["JCK1"], B7B.format(c="JCK1")],
 [])

add("CAP1", "041", "毛鳞鱼 Capelin（Mallotus villosus）",
 ["lifecycle = 繁殖季近岸或岸滩聚集（生命周期空间转换——P05 相邻 premise）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "plankton_field（浮游-小型底栖资源场浓度——短时近岸窗机会）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（Seasonal FoodField + spatial migration overlay + FieldFeeding——繁殖上岸不与全年近岸分布混谈=premise 层）",
  "B: field/capelin.md §0（BHC canonical 同型骨架——滤食场；K4 排除口径=繁殖面不冒充 P04/P01）",
  "C: pelagic-oceanic 0-725m / 滤食性 / anadromous / 1.7-3.7°C"],
 [B7S.format(n="041"), CSV + "#CAP1", "outputs/full_authoring/field/species/capelin.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CAP1"], B7B.format(c="CAP1")],
 [])

add("LWF1", "042", "湖白鲑 Lake Whitefish（Coregonus artedi）",
 ["season = 季节改变深浅分布（时变条件——垂直轴段独立维）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "lake_bottom_band（湖底-近底层带——底质资源主体）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "season_bound_depth_layer_axis（季节绑定深浅层轴）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: RB 主句『主要利用湖底和近底层资源』（底层带先行）+『季节改变深浅分布』（季节轴段次之——两独立维）；FCFI=P02/P05",
  "B: field/lake_whitefish_field.md §0 滤食场（双批分工：P03 面为另一 story 域——本 story 主体=P02 底质资源）",
  "C: pelagic-neritic 0-64m / 滤食性 / anadromous"],
 [B7S.format(n="042"), CSV + "#LWF1", "outputs/full_authoring/field/species/lake_whitefish_field.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["LWF1"], B7B.format(c="LWF1")],
 [])

add("SIL1", "043", "鲢鱼 Silver Carp（Hypophthalmichthys molitrix）",
 ["filter = 滤食处理水柱浮游生物与悬浮有机物（滤食与钩饵响应并非同一现实机制）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "phytoplankton_column_field（浮游植物水柱场浓度——上层滤食向）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03+B02（滤食是 FieldFeeding，特殊接触捕获不证明新 Grammar——走 Capture Boundary）",
  "B: field/silver_carp.md §0（BHC canonical 同型骨架参数差异化——鲢主滤浮游植物[上层]；与鳙同型不分裂）",
  "C: benthopelagic 0-20m / 植食性 / 6-30°C"],
 [B7S.format(n="043"), CSV + "#SIL1", "outputs/full_authoring/field/species/silver_carp.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SIL1"], B7B.format(c="SIL1")],
 [])

add("CAR1", "044", "鲤鱼 Common Carp（Cyprinus carpio）",
 ["disturbance = 翻拱泥云/气泡为可见痕迹（搜索线索——痕迹≠必有鱼，不改鱼程序）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "near_bottom_soft_layer（近底软水层——benthopelagic 软定位三档）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "substrate_upturnability（底质可拱性三档——口部翻拱的物理依赖）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_prey_patch（底栖猎物斑块丰度三档）")],
 "SpatialDistributionWeight", "ST", None,
 ["A: RB 主句『用口部翻拱底泥，摄食底栖无脊椎、植物碎屑和种子』——翻拱取食对底质可拱性有物理依赖：可拱性先于斑块丰度（软定位首步无门）",
  "B: patch/common_carp.md §0 判断顺序=近底带水层定位→底质可拱性→底栖猎物斑块（同序独立确认；三步无门形）",
  "C: benthopelagic 0-29m / 3-35°C"],
 [B7S.format(n="044"), CSV + "#CAR1", "outputs/full_authoring/patch/species/common_carp.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CAR1"], B7B.format(c="CAR1")],
 ["预投饵斑块=世界侧事实供给（B 文件 §0 关键判别原样——不购买新结构）"])

add("TEN1", "045", "丁鱥 Tench（Tinca tinca）",
 ["season = 暖季活动更明显（弱锚——配置级）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "vegetated_slackwater_band（静水植被边缘带——软底低扰动水域）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_omnivore_resource（底层无脊椎+植物资源场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: RB 主句『偏好静水与植被边缘，主要在底层寻找无脊椎和植物性资源』——静水植被带先行；SS『先找植被边缘、软底与低扰动水域，再以底层离散目标呈现』（位置和底质先于呈现）",
  "B: normal2/tench.md §0 追击组（受限还原 unordered——story 侧两维分辨率更高）",
  "C: demersal 1m+ / 晨昏活跃 / 4-24°C"],
 [B7S.format(n="045"), CSV + "#TEN1", "outputs/full_authoring/normal2/species/tench.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["TEN1"], B7B.format(c="TEN1")],
 [])

add("DIS2", "046", "七彩神仙鱼（白） White Discus（Symphysodon aequifasciatus 白色型）",
 ["guard_state = 亲鱼-幼鱼体表黏液摄食+守护阶段（机制语义与普通摄食不同——禁止表达成 Feeding 通道）",
  "color_morph = 色型不分裂（色型差异只在资产/外观维度——S12 判定）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "fry_anchor_present（稚鱼群锚存在性——贴附取食黏液的移动幼鱼群）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "brood_habitat_quality（群栖境适配三档——移动锚判『稚鱼群所在栖境』而非固定巢址）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（贴群关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（局部水温三档——暖水窄温向）")],
 "GuardingSpatialDistributionWeight", "GA", None,
 ["A: story FCFI=P04（与橙色型形成 Compression Candidate 而非新 Pattern——同一繁殖 Condition+Relation owner）",
  "B: guarding/discus.md §0（fry_anchor=幼鱼群；贴附=贴群关系；判断顺序=锚存在→群栖境→贴群→局部温度）",
  "C: 26-31°C（窄暖带——第 4 步温度轴方向锚）"],
 [B7S.format(n="046"), CSV + "#DIS2", "outputs/full_authoring/guarding/species/discus.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["DIS2"], B7B.format(c="DIS2")],
 ["与 B1-DIS（橙色型 fry_anchor 既有值——v9 统一 fry_school）同种色型对照（registry 行内 S12 色型不分裂注记——本批独立推导同向）"])

add("BON1", "047", "东方狐鲣 Striped Bonito（Sarda orientalis）",
 ["school = 高速追猎型（移动饵群=发现层线索）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "moving_bait_field（移动饵场浓度——小鱼头足类随水层变化）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（移动 FoodField + current/depth context + target response——FieldFeeding+downstream TargetFeeding）",
  "B: normal2/striped_bonito.md §0 追击组（受限还原 unordered）",
  "C: pelagic-neritic 1-167m / 全天活跃 / 13.5-23°C"],
 [B7S.format(n="047"), CSV + "#BON1", "outputs/full_authoring/normal2/species/striped_bonito.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BON1"], B7B.format(c="BON1")],
 [])

add("SBS1", "048", "中华倒刺鲃 Spinibarbus sinensis",
 ["evidence_open = 流速-底质-季节性摄食物种级因果链未闭合（story 明言只保留检索方向）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "gravel_run_pool_band（溪流底质带——急缓流交界/砾石砂底/深潭边缘）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_discrete_resource（底层离散资源场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『可把急缓流交界、砾石/砂底和深潭边缘作为候选搜索点，再用底层离散目标 Presentation』——空间搜索点先行，离散资源次之（Evidence Open 策略假设）",
  "B: normal/spinibarbus.md §0（同属光倒刺鲃文件——行级证据不继承，仅组样板参照）",
  "C: benthopelagic / 杂食性 / 17-27°C"],
 [B7S.format(n="048"), CSV + "#SBS1", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SBS1"], B7B.format(c="SBS1")],
 ["与 SBH1 同属不同种——行级证据不互并（B 文件注记同向）"])

add("CSN1", "049", "乌鳢 Northern Snakehead（伏击-护幼切换 story，Channa argus）",
 ["state_switch = 伏击捕食（NONE 态）与护幼关系（PARENTAL_GUARD 态）随繁殖状态互斥切换——同刻种群份额只进一个 Group（§13.1 先例）",
  "ambush_face_adjacent = 非繁殖期植被伏击面=相邻态（本 story 冻结行=护幼关系切换）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "fry_school_anchor_present（稚鱼群锚存在性——浮巢孵化后的植被区移动稚鱼群）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "brood_habitat_quality（植被掩体群栖境适配三档）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（环护关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA", None,
 ["A: story RB『繁殖期亲鱼可守护卵和幼鱼』+FCFI=P04（Persistent Guard Condition + Relation；普通捕食仍可落 P01——互斥态路由）",
  "B: guarding/snakehead.md §0（锚点=fry_school 浮巢孵化后稚鱼群——植被区移动锚；判断顺序=锚存在→植被掩体群栖境→环护→局部温度；稚鱼群存在已在路由面结算 Bake 不重复）",
  "C: benthopelagic / 4-22°C / 晨昏活跃"],
 [B7S.format(n="049"), CSV + "#CSN1", "outputs/full_authoring/guarding/species/snakehead.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CSN1"], B7B.format(c="CSN1")],
 ["queue 双条目：TRB-0156（本 Bake 面）+TRB-0303（RESP 面 form_hold 终裁——另条目）"])

add("BBR1", "050", "云斑鮰 Brown Bullhead（Ameiurus nebulosus）",
 ["sensory = 嗅味和触须线索（typed sensory Context）",
  "guard_adjacent = 繁殖时使用巢穴并照护卵/幼鱼（关系对象——相邻面，不混写）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "mud_slack_base（泥底缓流底板）"),
  slot("low_light_night_slot（低光夜槽——夜间底层觅食窗口）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: RB 主句『常在低光或夜间沿底层觅食，依赖嗅味和触须线索』——泥底底板先行+夜槽；护卵=相邻面（story Scope『夜间取食是 ordinary feeding；洞巢护卵是关系对象，不混写』）",
  "B: normal/brown_bullhead.md §0 夜行组样板（泥底缓流夜行）",
  "C: demersal 10-12m / 夜间活跃 / 0-37.4°C"],
 [B7S.format(n="050"), CSV + "#BBR1", "outputs/full_authoring/normal/species/brown_bullhead.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BBR1"], B7B.format(c="BBR1")],
 ["护巢面（P04）为相邻独立面——洞巢利用 egg_mass 形（MUT 批判例②落位表注记；不在本 Bake 面承载）"])

add("RST1", "051", "俄罗斯鲟 Russian Sturgeon（Acipenser gueldenstaedtii）",
 ["lifecycle = 河海洄游与繁殖回河阶段（迁移通达=相邻 premise——底层通道与迁移入口定位）",
  "conservation = 保护状态/捕获限制=产品 Boundary（story 判语）"],
 [ev("EVAL_TYPED_PREY_FACTOR", "benthic_fauna_field（底栖资源场——软体动物/甲壳类/小鱼）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "anadromous_bottom_corridor（河海底层廊道——底层通道+迁移入口）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: RB 主句『底栖摄食者，利用软体动物、甲壳类和小鱼等底层资源，并具有河海洄游』——食性主句先行（底栖资源场），洄游通达廊道次之（FCFI=P05 lifecycle/spatial condition + TargetFeeding）",
  "B: normal/russian_sturgeon.md §0 伏击组 GATE_ZONE（受限还原——story 主体轴=摄食先行，与样板门形不同：本 story 无『非底层即出局』硬门直证[栖息带=CSV 软证据]，按食性主句两步推）",
  "C: demersal 2-100m / anadromous / 晨昏活跃 / 10-20°C"],
 [B7S.format(n="051"), CSV + "#RST1", "outputs/full_authoring/normal/species/russian_sturgeon.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RST1"], B7B.format(c="RST1")],
 ["与 SS2（同属闪光鲟）不同种——B 文件互指判例不继承"])

add("SBH1", "052", "光倒刺鲃 Spinibarbus hollandi",
 ["evidence_open = 底层摄食-流速-底质偏好物种级链条未闭合（story 明言）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "river_run_band（河流溪流带——流速变化/深潭边缘）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_resource（底层资源场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『可把流速变化、底质和深潭边缘作为候选搜索点，再用底层离散 Presentation』——空间搜索点先行（Evidence Open 策略假设）",
  "B: normal/spinibarbus.md §0 伏击组 GATE_ROCK_CREVICE（受限还原——story 侧无石隙硬门直证，按两步推）",
  "C: benthopelagic 2-30m / 17-27°C"],
 [B7S.format(n="052"), CSV + "#SBH1", "outputs/full_authoring/normal/species/spinibarbus.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SBH1"], B7B.format(c="SBH1")],
 [])

add("BSH1", "053", "公牛鲨 Bull Shark（Carcharhinus leucas）",
 ["euryhaline = 强广盐性（海水/河口/淡水通道——盐度通达=空间条件）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "salinity_gradient_corridor_axis（盐度梯度廊道轴——河口通道可达性）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: RB 主句『具强广盐性，可利用海水、河口和淡水通道，并机会性捕食』——盐度通达=唯一硬分野维（主体轴）；机会捕食=离散响应（Presentation 仍以离散猎物响应表达——FCFI=P05 Spatial/Condition owner 优先）",
  "B: normal2/bull_shark.md §0 夜行组（受限还原——story 主体轴=盐度廊道非夜行结构）",
  "C: reef-associated 1-164m / amphidromous / 21.5-33.5°C"],
 [B7S.format(n="053"), CSV + "#BSH1", "outputs/full_authoring/normal2/species/bull_shark.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BSH1"], B7B.format(c="BSH1")],
 [])

add("WCF1", "054", "六须鲶 Soldatov's Catfish（Silurus soldatovi）",
 ["evidence_open = 夜间/气味策略按 Evidence Open 处理（本种公开资料较少）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "deep_channel_base（深槽-回水底板——大型河道缓流遮蔽）"),
  slot("low_light_night_slot（低光夜槽——大型底层掠食窗口）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: RB 主句『大型河道底层掠食鱼，主要捕食鱼类，常与深槽、缓流和遮蔽结构相关』+SS『优先找深槽、回水、浑水和低光窗口』——深槽底板先行+低光槽",
  "B: normal/soldatov_catfish.md §0 夜行组样板（深潭砾底夜行伏击）",
  "C: demersal / 夜间活跃 / 5-25°C"],
 [B7S.format(n="054"), CSV + "#WCF1", "outputs/full_authoring/normal/species/soldatov_catfish.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["WCF1"], B7B.format(c="WCF1")],
 ["与 RB-2 WEL（欧洲六须鲶 wels——hole_woody_structure_base+SLOT NO 形）同科不同种——判例不继承"])

add("SZE1", "055", "加拿大梭鲈 Sauger（Sander canadensis）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "turbid_river_base（浑水河道底板——大河/沙砾底/浑水边界）"),
  slot("low_light_night_slot（低光夜槽——晨昏/夜间窗口）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: RB 主句『常与大河、浑水、沙砾底和低光条件相关』——浑水河道底板先行+低光槽（低光/浑水改变检测与活动窗口，不改变响应对象类别——story 判语）",
  "B: normal/sauger.md §0 夜行组样板（浑水深水夜行）",
  "C: demersal 5m+ / 夜间活跃 / 19.1-31.1°C"],
 [B7S.format(n="055"), CSV + "#SZE1", "outputs/full_authoring/normal/species/sauger.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SZE1"], B7B.format(c="SZE1")],
 ["与 WAL2 同属（Sander）不同种——B 文件互指判例不继承"])

# ===========================================================================
# 第 4 层 B7 110 —— FISH-R03 系（24）
# ===========================================================================
add("ASC2", "070", "革胡子鲶 African Sharptooth Catfish（Clarias gariepinus）",
 ["air_breathing = 辅助空气呼吸（低氧耐受=现实边界，不创建独立 Mode）",
  "flood_adjacent = 洪泛季节迁移/繁殖移动=相邻 lifecycle evidence（不在本响应链重复结算）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "mud_swamp_base（泥底沼泽底板——河流/湖泊/沼泽/洪泛区）"),
  slot("low_light_night_slot（低光夜槽——夜间活动窗口）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: RB 主句『栖息于河流、湖泊、沼泽和季节性干涸洪泛区』+CSV 夜间活跃——泥沼底板先行+夜槽（『空气呼吸是现实边界，不自动创建独立 Night 或 Low-Oxygen Mode』——story 判语）",
  "B: normal/african_sharptooth_catfish.md §0 夜行组样板（泥底夜行伏击）",
  "C: benthopelagic 0-80m / 夜间活跃 / 8-35°C"],
 [B7S.format(n="070"), CSV + "#ASC2", "outputs/full_authoring/normal/species/african_sharptooth_catfish.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["ASC2"], B7B.format(c="ASC2")],
 ["体型相关食物谱=阶段 premise（story Granularity 边界原样——不双重结算）"])

add("BKC", "069", "青鱼 Black Carp（Mylopharyngodon piceus）",
 ["hard_prey = 螺类/蛤类等硬壳无脊椎为重要资源（咽齿硬壳处理特化——资源主句）"],
 [ev("EVAL_TYPED_PREY_FACTOR", "mollusk_hardshell_patch（硬壳软体斑块——螺/贝集中区）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "river_lake_bottom_band（河湖底层带——底质水流合适区）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: story SS『机制侧先寻找螺类/贝类集中、底质和水流合适的 Resource Patch，再由可辨识的离散目标进入 TargetFeeding』——硬壳资源斑块先行（食物载体先行=FF 方向学），底质水流带次之",
  "B: 无表达文件（B 系列不在册）",
  "C: demersal 5-30m / 0-40°C"],
 [B7S.format(n="069"), CSV + "#BKC", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BKC"], B7B.format(c="BKC")],
 ["养殖饲料反应不外推野生策略（story 限定）"])

add("BRC", "063", "赤眼鳟 Barbel Chub（Squaliobarbus curriculus）",
 ["evidence_open = 直接食性/阶段差异/野外钓法交叉证据不足（S1=EO 摄食对象未闭合）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（底中缓流带——CSV 软定位单因子）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story S1=EO（摄食对象未充分闭合）/S3/S4/S8=MSF（季节资源/流速底质）——顺序证据不足闭合多步链；按 CSV 软定位单因子分辨率记录（RB-2 品系轨同型处理）",
  "B: 无表达文件",
  "C: benthopelagic / 17-27°C / 早晨活跃"],
 [B7S.format(n="063"), CSV + "#BRC", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BRC"], B7B.format(c="BRC")],
 ["链序分辨率=story 证据边界（不虚构多步）；后续补证可升档"])

add("CHS", "071", "马口鱼 Chinese Hook Snout Carp（Opsariichthys bidens）",
 ["evidence_open = 物种级食谱/日周期未闭合（S1=EO 小型猎物链未充分闭合）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "shallow_stream_band（浅水溪流带——浅水/流速边界/遮蔽物）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story S1=EO/S4=MSF（浅水、流速和溪流结构）/S8=MSF（溪流河段和遮蔽物）——空间锚充分、猎物链未闭合→单因子空间带",
  "B: 无表达文件",
  "C: benthopelagic / 10-20°C / 早晨活跃"],
 [B7S.format(n="071"), CSV + "#CHS", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CHS"], B7B.format(c="CHS")],
 ["『溪流鱼』不自动变快流 Mode（story 判语——不新增 Flow Mode）"])

add("CLC", "067", "长吻𬶏 Chinese Longsnout Catfish（Tachysurus dumerili）",
 ["evidence_open = 触须/低光/夜间活动的强因果关系尚未由本批直接来源闭合（story 明言『夜间只作待验证 Context，不购买 Night Mode』）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "river_bottom_cover_band（河流底层遮蔽带——底质/遮蔽物）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story S1=EO（食物组成稀疏）/S4=MSF（底层遮蔽河流）/S8=MSF（底质和遮蔽物）——底层遮蔽单因子；夜槽证据=R03 story 未闭合（不虚构）",
  "B: 无表达文件",
  "C: demersal / 全天活跃 / 11-19°C"],
 [B7S.format(n="067"), CSV + "#CLC", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CLC"], B7B.format(c="CLC")],
 ["与 RB-1 CLC（B5/R08-09 story——NO 形含夜槽）同种双 story 不同证据分层：B5 story 闭合夜行、R03 story 未闭合+CSV 全天——story 级各自消费+去重联动（非冲突：证据分层忠实记录，HRQ 对账条目）"])

add("GCR", "078", "黄金鲫 Golden Crucian（Carassius auratus 杂交/选育标签）",
 ["strain_identity = 杂交/选育身份不稳定（不作品系特有机制——继承普通鲫鱼基线）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "crucian_benthic_omnivore_patch（鲫系底栖杂食带——浅水/底层资源）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story『普通鲫鱼资料可提供浅水/底层杂食和资源 Patch 基线……不把黄金色表型或养殖投喂反应写成独立 Mode』——品系复用先例（Identity Deferred）",
  "B: normal2/golden_crucian.md §0 机会组（CSV 方向——同种基线单因子）",
  "C: Carassius auratus hybrid / 0-41°C / 早晨活跃"],
 [B7S.format(n="078"), CSV + "#GCR", "outputs/full_authoring/normal2/species/golden_crucian.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["GCR"], B7B.format(c="GCR")],
 ["与 RB-1 HYC（crucian_benthic_omnivore_patch 单步）同系同形——跨批对照确认"])

add("HMB", "068", "青梢红鲌 Humpback（Culter recurviceps）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "inshore_midupper_band（近岸中上水层带——河湖鲌类）"),
  ev("EVAL_TYPED_PREY_FACTOR", "small_fish_prey_field（小型猎物场——中上层小型猎物）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『先按水层、近岸结构和移动猎物 Patch 找机会，再由离散目标进入 TargetFeeding』——水层结构先行，猎物场次之",
  "B: 无表达文件（近缘红鲌资料不外推——story 判语）",
  "C: benthopelagic / 17-27°C / 早晨活跃"],
 [B7S.format(n="068"), CSV + "#HMB", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["HMB"], B7B.format(c="HMB")],
 [])

add("IRS", "062", "蓝鲨 Iridescent Shark（Pangasianodon hypophthalmus）",
 ["aquaculture_boundary = 养殖场高密度行为不代表野生机制（story Granularity 边界原样）",
  "flood_adjacent = 洪泛迁移/繁殖=相邻 lifecycle evidence（不双重结算）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "river_floodplain_band（河流-洪泛带——河段/资源集中区）"),
  ev("EVAL_TYPED_PREY_FACTOR", "size_graded_omnivore_field（体型分级杂食场——浮游/昆虫/甲壳/植物/小动物）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『玩家侧先按水位、河段和资源集中找机会，再根据个体大小选择可达呈现』——水位河段带先行，体型分级资源次之",
  "B: normal2/iridescent_shark.md §0 机会组（受限还原单步——story 侧两维分辨率更高）",
  "C: benthopelagic / 22-26°C / 全天活跃"],
 [B7S.format(n="062"), CSV + "#IRS", "outputs/full_authoring/normal2/species/iridescent_shark.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["IRS"], B7B.format(c="IRS")],
 [])

add("KOI", "065", "锦鲤 Koi（Cyprinus rubrofuscus 观赏鲤品系）",
 ["strain_identity = 观赏鲤品系以 C. carpio 物种基线处理（颜色/鳞片图案不推导机制——story 明言）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（底中缓流带——鲤系底层杂食基线）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story『锦鲤的生态机制应继承普通鲤，而不能由颜色和鳞片图案单独推导』——品系轨（Identity Deferred）；FCFI=Resource Patch+Discrete Target（资源层 Resolution=物种级）",
  "B: field/koi.md（品系 L1 等效层——本体指针）",
  "C: Cyprinus rubrofuscus benthopelagic 0-29m / 3-35°C / 早晨活跃"],
 [B7S.format(n="065"), CSV + "#KOI", "outputs/full_authoring/field/species/koi.md", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["KOI"], B7B.format(c="KOI")],
 ["RB-2 品系 8 尾（SUK/GRK/KHK/OGK/LCP/AMC/ASC/HFC——benthopelagic_slowwater_band 单步）引用『亲本 R03 轨不在重跑队列』开放项——本批 KOI 本体推导同形：0 冲突，品系开放项闭合（品系真形无需升档）"])

add("LJB", "073", "鯮鱼 Long-jawed Baelama（Luciobrama macrocephalus）",
 ["evidence_open = 物种级行为字段稀疏（身份可核验；摄食对象/季节迁移/水层稳定性需直接资料）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "midwater_river_band（大河中上水层带——CSV 方向+身份入口）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story『现阶段可保留河流/湖泊水层与小型猎物资源共同决定可达机会的低强度解释』——S1/S3/S4/S8 全 EO 或稀疏→单因子低强度（不外推近缘鲌类）",
  "B: 无表达文件",
  "C: benthopelagic / 17-27°C / 早晨活跃"],
 [B7S.format(n="073"), CSV + "#LJB", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["LJB"], B7B.format(c="LJB")],
 ["不用相近物种追猎资料填补空缺（story 判语原样）"])

add("LNK", "057", "细鳞鲑 Sharp-snouted Lenok（Brachymystax lenok）",
 ["coldwater = 冷水河流鲑形鱼（水温=第一环境约束）",
  "seasonal = 季节性上溯（相邻 lifecycle——S5 MSF 候选链强度开放）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "cold_stream_structure_band（冷水溪流结构带——急流/深潭）"),
  ev("EVAL_TYPED_PREY_FACTOR", "drift_fish_invert_field（漂流昆虫-小鱼猎物场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『机制侧可先按水温、流速、深浅结构和猎物出现位置寻找 Opportunity』——水温情境（冷水结构带）先行，猎物位置次之（S1=MSF 昆虫小鱼/S4=MSF 急流深潭冷水/S8=MSF 河段深潭流速）",
  "B: normal/lenok.md §0 追击组（受限还原 unordered）",
  "C: benthopelagic / 11-19°C / 晨昏活跃 / anadromous"],
 [B7S.format(n="057"), CSV + "#LNK", "outputs/full_authoring/normal/species/lenok.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["LNK"], B7B.format(c="LNK")],
 [])

add("MDC2", "074", "鲮 Mud Carp（Cirrhinus molitorella）",
 ["mechanism_open = 连续摄食机制（拾取 vs 刮食细节）留 Profile 值域"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "periphyton_detritus_field（附着-碎屑连续场——藻类/附着生物/有机碎屑）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=Resource Patch（附着资源连续场）→FieldFeeding（P03 语义——『连续资源摄食不等于一个新 FishMode』）",
  "B: 无表达文件（同属泰鲮/印度鲮文件不外推——行级证据不继承）",
  "C: benthopelagic 5-20m / 植食性 / 22-26°C"],
 [B7S.format(n="074"), CSV + "#MDC2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MDC2"], B7B.format(c="MDC2")],
 [])

add("MIR", "066", "镜鲤 Mirror Carp（Cyprinus carpio var. specularis）",
 ["strain_identity = 鳞被表型为身份限定（品系——先按普通鲤物种基线处理）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（底中缓流带——鲤系底层杂食基线）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story『镜鲤应先按普通鲤的物种级生态基线处理，再把鳞被表型作为身份限定』——品系轨（Identity Deferred）",
  "B: 无本体表达文件（field/albino_mirror_carp.md 为白化镜鲤另一行）",
  "C: Cyprinus carpio benthopelagic 0-29m / 3-35°C / 早晨活跃"],
 [B7S.format(n="066"), CSV + "#MIR", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MIR"], B7B.format(c="MIR")],
 ["与 KOI/WRC 同批品系轨一致——RB-2 品系先例复用（0 冲突）"])

add("MRF", "061", "蒙古红鲌 Mongolian Redfin（Chanodichthys mongolicus）",
 ["school_pressure = 群聚只作发现层线索（Weak——不产生新控制流）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "midupper_current_band（中上水层流速带——河流/湖泊中上层）"),
  ev("EVAL_TYPED_PREY_FACTOR", "pursuit_prey_field（追猎猎物场——小鱼/虾移动猎物）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『机制侧可先扫描水层、流速和移动猎物 Patch，再由离散目标进入 TargetFeeding』——水层流速带先行，移动猎物场次之",
  "B: normal/mongolian_redfin.md §0 伏击组 GATE_SHADE_EDGE（受限还原——story 侧无明暗交界硬门直证，按两步推）",
  "C: benthopelagic / 10-20°C / 早晨活跃"],
 [B7S.format(n="061"), CSV + "#MRF", "outputs/full_authoring/normal/species/mongolian_redfin.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MRF"], B7B.format(c="MRF")],
 ["与 TPC/YCK/HMB（鲌类中上水层两步形）同形对照——不同种各自推导"])

add("RSB", "072", "高体鳑鲏 Rosy Bitterling（Rhodeus ocellatus）",
 ["guard_state = 雌鱼把卵产入活淡水蚌鳃腔，胚胎在蚌体内发育（对象依赖的繁殖关系——Relation Object 成立条件=活蚌+繁殖期）",
  "male_competition = 雄鱼围绕产卵机会和配偶竞争（关系性行为）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "host_brood_anchor_present（蚌宿主锚存在性——活淡水蚌为外部关系对象）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "mussel_bed_quality（蚌床栖境适配三档）"),
  ev("EVAL_GUARD_RELATION", "spawning_relation（产卵关系三档——与宿主蚌的繁殖关系对象）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA", None,
 ["A: story FCFI=P04（Relation Object / Condition——淡水蚌是繁殖所需的外部关系对象，不能并入普通 TargetFeeding）",
  "C: benthopelagic / 18-24°C / 全天活跃",
  "B7 批 EXT 轨 mussel_brood 轴值提案（v9 落位 host_brood 四形式之一）——本 Bake 面 anchor=host_brood 形确认"],
 [B7S.format(n="072"), CSV + "#RSB", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RSB"], B7B.format(c="RSB")],
 ["host_brood 既有四形式值直用（RSB 跨批复现实证判例——本批 Bake 面承载）"])

add("RTL", "056", "红罗非 Red Tilapia（Oreochromis sp. 杂交）",
 ["hybrid_identity = 杂交/选育标签非单一稳定物种（亲本/投喂史/环境驯化改变表现——低强度资源机会解释）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "warm_omnivore_band（温水杂食带——温暖淡水/底质植物资源）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story LPE=P01+P02 已能表达低强度温水杂食机会，不新增 Hybrid Mode——身份不确定性→单因子低强度（Confidence=Low）",
  "B: 无本体表达文件（guarding/nile_tilapia.md 为近亲种 O. niloticus——品系/近亲轨不冒充本体）",
  "C: Oreochromis sp. hybrid / 20-35°C / 全天活跃"],
 [B7S.format(n="056"), CSV + "#RTL", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RTL"], B7B.format(c="RTL")],
 ["近亲种轨注记：TIL2/TIL3（O. niloticus）与 RTL（hybrid）分列——身份分层不互并"])

add("SPS", "059", "花骨鱼 Spotted Steed（Hemibarbus maculatus）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "gravel_run_band（砾石河段带——河流底层/砾石砂底/河段结构）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_invert_field（底栖无脊椎场——小型无脊椎/昆虫幼体）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『机制侧先按流速、底质和小型底栖猎物集中区建立 Opportunity Context，再由离散目标进入 TargetFeeding』——底质河段带先行，底栖猎物场次之",
  "B: normal2/spotted_steed.md §0 追击组（受限还原 unordered；同属唇䱻互指不继承）",
  "C: benthopelagic / 10-24°C / 全天活跃"],
 [B7S.format(n="059"), CSV + "#SPS", "outputs/full_authoring/normal2/species/spotted_steed.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SPS"], B7B.format(c="SPS")],
 [])

add("STM", "076", "麦穗鱼 Stone Moroko（Pseudorasbora parva）",
 ["invasion = 入侵扩散只说明可用资源场（不等于个体攻击模式）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "shallow_vegetated_edge_band（浅水植被边缘带——浅水/缓流/植被缘）"),
  ev("EVAL_TYPED_PREY_FACTOR", "small_invert_egg_fry_field（小型无脊椎-鱼卵幼体场——离散小目标）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『机制侧可按浅水植被边缘和小型资源 Patch 找机会，再由鱼卵、幼体或小型无脊椎等离散目标进入 TargetFeeding』——植被边缘带先行，小目标场次之",
  "B: normal/stone_moroko.md §0 机会组（受限还原单步——story 侧两维分辨率更高）",
  "C: benthopelagic / 5-22°C / 全天活跃"],
 [B7S.format(n="076"), CSV + "#STM", "outputs/full_authoring/normal/species/stone_moroko.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["STM"], B7B.format(c="STM")],
 ["鱼卵/幼体摄食≠守巢关系（story S6 判语——不立 guard）"])

add("TPC", "058", "翘嘴红鲌 Topmouth Culter（Culter alburnus）",
 ["hydrology = 受水位、流速和繁殖季节影响的空间重排（水文=Context 维）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "midupper_current_band（中上水层流速带——河湖中上层）"),
  ev("EVAL_TYPED_PREY_FACTOR", "pursuing_prey_field（追捕猎物场——小鱼/虾移动猎物）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『设计上可先扫描中上层和流速变化，再以移动目标的速度、大小和停顿保持离散目标可见』——中上流速带先行，移动猎物场次之",
  "B: normal/topmouth_culter.md §0 伏击组 GATE_SHADE_EDGE（受限还原——story 侧无明暗交界硬门直证）",
  "C: benthopelagic / 11-19°C / 早晨活跃"],
 [B7S.format(n="058"), CSV + "#TPC", "outputs/full_authoring/normal/species/topmouth_culter.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["TPC"], B7B.format(c="TPC")],
 ["群体仅影响发现/机会，不直接产生新控制流（story FCFI 原样）"])

add("WCR2", "064", "野生鲫鱼 Wild Crucian Carp（Carassius auratus）",
 ["strain_boundary = 与观赏金鱼/养殖鲫/其它品系保持身份边界（品系/驯化差异 Evidence Open）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "crucian_benthic_omnivore_band（鲫系底栖杂食带——浅水/缓流或湖泊底层）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story『物种级基线是浅水、缓流或湖泊环境中的底层杂食机会』——鲫系单因子（『早口』或固定时段不作为硬触发器——story 判语）",
  "B: migration/prussian_carp.md（C. gibelio 银鲫近缘种文件——行级不互并，仅方向参照）",
  "C: Carassius auratus / 0-41°C / 早晨活跃"],
 [B7S.format(n="064"), CSV + "#WCR2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["WCR2"], B7B.format(c="WCR2")],
 ["与 RB-1 HYC/GCR 同系同形对照"])

add("WRC", "060", "荷包红鲤 Wuyuan Red Carp（Cyprinus carpio var. wuyuanensis）",
 ["strain_identity = 地方鲤品系（红色表型不推导机制——按 C. carpio 基线处理）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（底中缓流带——鲤系底层杂食基线）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story『先按普通鲤的底质与 Resource Patch 处理……品系外观不购买独立 Mode』——品系轨（Identity Deferred）",
  "B: 无表达文件（鲤品系轨继承）",
  "C: Cyprinus carpio var. / 0-29m / 3-35°C / 早晨活跃"],
 [B7S.format(n="060"), CSV + "#WRC", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["WRC"], B7B.format(c="WRC")],
 ["KOI/MIR/WRC 三品系轨同形——RB-2 品系先例复用（0 冲突）"])

add("XCD", "077", "黄尾鲴 Xenocypris davidi",
 ["capture_boundary = 连续 FieldFeeding 与离散钓获边界交下游 Capture owner（story S11 判语）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "periphyton_field（附着层场浓度——鲴类底质/附着资源）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=P03（连续附着资源——Resource Patch + FieldFeeding；食物组成/空间分布细节稀疏→单因子场）",
  "B: 无表达文件",
  "C: benthopelagic / 17-27°C / 早晨活跃"],
 [B7S.format(n="077"), CSV + "#XCD", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["XCD"], B7B.format(c="XCD")],
 [])

add("YCF", "079", "黄颡鱼 Yellow Catfish（Tachysurus fulvidraco）",
 ["guard_adjacent = 雄鱼黏土底质巢穴守护卵幼=相邻 Relation/Guard 候选（不在本普通摄食 Story 响应链内——story 判语）"],
 [gate("GATE_ZONE", "demersal_burrow_present（底层洞隙存在——泥底洞隙掩体，不成立=出局）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "burrow_structure_quality（洞隙掩体结构质量三档——巢穴/石缝/底质遮蔽）")],
 "SpatialDistributionWeight", "GC", None,
 ["A: RB 主句『河流与湖泊底层鱼，摄食昆虫、软体动物，偶尔鱼类』+S8=MSF（底质和巢穴区域是持久空间线索）——底层洞隙=空间第一约束（demersal 硬定位）",
  "B: normal/yellow_catfish.md §0 判断顺序=GATE_BURROW 门→掩体结构档（同序独立推导确认）",
  "C: demersal / 16-25°C / 全天活跃"],
 [B7S.format(n="079"), CSV + "#YCF", "outputs/full_authoring/normal/species/yellow_catfish.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["YCF"], B7B.format(c="YCF")],
 ["守巢面为相邻独立面（story Open Questions 原样）"])

add("YCK", "075", "鳡鱼 Yellowcheek（Elopichthys bambusa）",
 ["school_pressure = 群游/追群=发现层线索（FishModePressure=Weak——不购买 Chase/School Mode）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "midupper_current_band（中上水层流速带——大型河流中上层）"),
  ev("EVAL_TYPED_PREY_FACTOR", "pursuing_prey_field（追捕猎物场——鱼食性移动猎物）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『设计侧可按水层、流速边界和猎物移动寻找机会，再用可见的移动目标推进 TargetFeeding』——水层流速带先行，移动猎物场次之",
  "B: normal/yellowcheek.md §0 机会组（受限还原单步——story 侧两维分辨率更高）",
  "C: benthopelagic / 10-20°C / 早晨活跃 / potamodromous"],
 [B7S.format(n="075"), CSV + "#YCK", "outputs/full_authoring/normal/species/yellowcheek.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["YCK"], B7B.format(c="YCK")],
 [])

# ===========================================================================
# 第 4 层 B7 110 —— FISH-R04 系（23，压缩 story）
# ===========================================================================
add("FGA4", "080", "佛罗里达雀鳝 Florida Gar（Lepisosteus platyrhincus）",
 ["season_activity = 浅水季节水温窗口=活性 condition premise（非空间分支）"],
 [gate("GATE_COVER_EXISTENCE", "vegetation_edge_cover_present（植被缘掩体存在——浅水植被边缘伏击位）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "vegetation_edge_cover_quality（植被缘掩体结构质量三档）")],
 "SpatialDistributionWeight", "GC", None,
 ["A: story RB『freshwater predator using shallow vegetated or slow-water habitat』+SS『Search vegetation edges and quiet water』——植被缘掩体先行",
  "B: normal/florida_gar.md §0 判断顺序=GATE_VEGETATION_EDGE 门→掩体结构档（同序独立推导确认）",
  "C: demersal / 17-27°C / 晨昏活跃"],
 [B7S.format(n="080"), CSV + "#FGA4", "outputs/full_authoring/normal/species/florida_gar.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["FGA4"], B7B.format(c="FGA4")],
 ["与 RB-2 FGA（R02-S17 同种双 story——B7 判例⑦点名内容近似）同形：真形复用+reused_from 标注（双 story 复用轨）"],
 reuse=dict(from_batch="CENSUS-REBUILD-002", from_pid="P-RB2-FGA-BAKE", note="同种双 story（R04 压缩 story 与 R02-S17 机构 story）内容近似——植被缘伏击同形，复用 RB-2 真形（R02-S17 story 证据更全）；本批 story 侧 SS 同句式独立印证"))

add("MUS", "081", "北美狗鱼 Muskellunge（Esox masquinongy）",
 [],
 [gate("GATE_COVER_EXISTENCE", "cover_edge_present（掩体边缘存在——植被/结构缘伏击位）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "cover_quality（掩体结构质量三档——大体型目标通道）")],
 "SpatialDistributionWeight", "GC", None,
 ["A: story RB『often using cover and edge habitat』+SS『prioritizes large-target profiles and cover edges』——掩体边缘=空间第一约束（伏击位存在性）",
  "B: normal/muskellunge.md §0 追击组（受限还原 unordered——狗鱼系伏击型按掩体门推[PIK1/CPT 同科形]）",
  "C: demersal / 11-19°C / 晨昏活跃 / non-migratory"],
 [B7S.format(n="081"), CSV + "#MUS", "outputs/full_authoring/normal/species/muskellunge.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MUS"], B7B.format(c="MUS")],
 [])

add("SIH", "082", "双线无须鳕 Silver Hake（Merluccius bilinearis）",
 ["season = 季节性陆架/深度移动（recruitment/spawning=相邻 context）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "seasonal_shelf_depth_band（季节性陆架深度带——活动深度带）"),
  ev("EVAL_TYPED_PREY_FACTOR", "fish_squid_prey_field（鱼-头足猎物场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『locates the active depth band and presents a discrete bait in the target layer. Depth and season reorder access to the same target logic』——深度季节重排先行，同目标逻辑次之",
  "B: normal2/silver_hake.md §0 追击组（受限还原 unordered）",
  "C: demersal 55-914m / 3.9-5.9°C / oceanodromous"],
 [B7S.format(n="082"), CSV + "#SIH", "outputs/full_authoring/normal2/species/silver_hake.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SIH"], B7B.format(c="SIH")],
 [])

add("BET", "083", "大眼金枪鱼 Bigeye Tuna（Thunnus obesus）",
 ["diel = 强深度昼夜移动（DVM——垂直日循环）",
  "spawning_adjacent = 产卵迁移不在本 story 闭合范围"],
 [ev("EVAL_TYPED_PREY_FACTOR", "mesopelagic_squid_fish_field（中深层鱼-鱿鱼猎物场——鱼/鱿鱼/甲壳）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "diel_thermocline_band（昼夜温跃层深度带——温度/深度/饵标跟随）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: story SS『follows temperature, depth and prey marks, then presents a discrete target in the active layer. The control problem is finding the moving opportunity』——移动机会=猎物标先行（RB-1 海洋追击组 FF 方向学：PBF/SAF/YFT 同型），活动层带次之",
  "B: normal2/bigeye_tuna.md §0 追击组（受限还原 unordered）",
  "C: pelagic-oceanic 0-1500m / 13-29°C / oceanodromous"],
 [B7S.format(n="083"), CSV + "#BET", "outputs/full_authoring/normal2/species/bigeye_tuna.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BET"], B7B.format(c="BET")],
 [])

add("BWF", "084", "弓鳍鱼 Bowfin（Amia calva）",
 [],
 [gate("GATE_COVER_EXISTENCE", "swamp_vegetation_present（沼泽植被掩体存在——植被静水结构区）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "cover_quality（掩体结构质量三档）")],
 "SpatialDistributionWeight", "GC", None,
 ["A: story RB『predatory freshwater fish associated with vegetated, quiet or structured water』+SS『search cover edges and low-current structure』——沼泽植被掩体先行（『source record does not justify a universal night-only rule』——无夜槽）",
  "B: normal/bowfin.md §0 判断顺序=GATE_SWAMP_VEGETATION 门→掩体结构档（同序独立推导确认）",
  "C: demersal / 15-20°C / 晨昏活跃"],
 [B7S.format(n="084"), CSV + "#BWF", "outputs/full_authoring/normal/species/bowfin.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BWF"], B7B.format(c="BWF")],
 [])

add("SB2", "085", "斑点黑鲈 Spotted Bass（Micropterus punctulatus）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "current_rock_band（水流-岩礁带——current seams/rock/cover）"),
  ev("EVAL_TYPED_PREY_FACTOR", "piscivore_field（鱼食-无脊椎猎物场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story RB『commonly associated with current, rock and cover, taking fish and invertebrates』——软关联（commonly associated——非硬门）结构带先行；SS『The key variable is access to target opportunity』",
  "B: normal2/spotted_bass.md §0 机会组（受限还原单步——story 侧两维分辨率更高）",
  "C: demersal / 17-27°C / 晨昏活跃"],
 [B7S.format(n="085"), CSV + "#SB2", "outputs/full_authoring/normal2/species/spotted_bass.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SB2"], B7B.format(c="SB2")],
 ["黑鲈系互指：小口（guarding 面）/大口（0 Story 隔离）——同属泛化不成立（B 文件注记）"])

add("WCR3", "086", "白斑刺盖太阳鱼 White Crappie（Pomoxis annularis）",
 ["school = 集群=发现层 context signal（不构成新供给模式）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "structure_depth_band（结构-活动深度带——沉水结构+季节深度）"),
  ev("EVAL_TYPED_PREY_FACTOR", "small_fish_field（小鱼-无脊椎猎物场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『Locate structure and the active depth band, then present a small discrete target within the school opportunity』——结构深度带先行",
  "B: normal/white_crappie.md §0 机会组（受限还原单步）",
  "C: demersal / 20.3-32.3°C / 晨昏活跃"],
 [B7S.format(n="086"), CSV + "#WCR3", "outputs/full_authoring/normal/species/white_crappie.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["WCR3"], B7B.format(c="WCR3")],
 ["与 CRA1/CRA2（黑 crappie）同属不同种——判例不继承"])

add("CTT", "087", "白马切喉鳟 Cutthroat Trout（Oncorhynchus clarkii）",
 ["life_form = resident 与 migratory 型并存（lifecycle context——阶段改变 Context 与位置先于响应语义）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "coldwater_drift_lane_band（冷水漂流通道带——coldwater flow/drift lanes）"),
  ev("EVAL_TYPED_PREY_FACTOR", "stage_graded_prey_field（阶段分级猎物场——水生/陆生无脊椎↔鱼类）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『reads coldwater flow, drift lanes and seasonal access, then selects a small discrete target that matches the current prey field』——冷水漂流通道带先行，当前猎物场次之",
  "B: normal/cutthroat_trout.md §0 追击组（受限还原 unordered）",
  "C: demersal 0-200m / 6.1-10.1°C / anadromous"],
 [B7S.format(n="087"), CSV + "#CTT", "outputs/full_authoring/normal/species/cutthroat_trout.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CTT"], B7B.format(c="CTT")],
 [])

add("RSB2", "088", "真鲷 Red Seabream（Pagrus major）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "reef_hard_bottom_band（岩礁硬底带——礁缘/硬底）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_prey_field（底栖猎物场——鱼/甲壳/底栖饵）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『Find hard bottom or reef edges where prey patches form, then present a discrete bait close to the feeding layer』——岩礁硬底带先行（patch context guides search）",
  "B: normal2/red_seabream.md §0 机会组（受限还原单步）",
  "C: demersal 10-200m / 16.8-26.8°C / oceanodromous"],
 [B7S.format(n="088"), CSV + "#RSB2", "outputs/full_authoring/normal2/species/red_seabream.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RSB2"], B7B.format(c="RSB2")],
 [])

add("BSN", "089", "眼鳢 Bullseye Snakehead（Channa marulius）",
 ["air_breathing = 气呼吸耐受改变栖地持续性（habitat persistence——非摄食通道）",
  "guard_adjacent = breeding guard 为独立开放 story（story Scope 原样）"],
 [gate("GATE_COVER_EXISTENCE", "surface_vegetation_present（表层植被掩体存在——植被表面伏击位）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "cover_quality（掩体结构质量三档——dense cover edges）")],
 "SpatialDistributionWeight", "GC", None,
 ["A: story RB『warm freshwater predator using cover』+SS『Search dense cover edges and oxygen-stressed or shallow opportunity zones』——植被掩体先行（无独立 Low-Oxygen Mode）",
  "B: normal/giant_snakehead.md §0 判断顺序=GATE_SURFACE_VEGETATION 门→掩体结构档（同序独立推导确认）",
  "C: benthopelagic / 24-28°C / 晨昏活跃 / potamodromous"],
 [B7S.format(n="089"), CSV + "#BSN", "outputs/full_authoring/normal/species/giant_snakehead.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BSN"], B7B.format(c="BSN")],
 [])

add("RTB", "090", "红尾梭鱼 Red Tail Barracuda（Acestrorhynchus falcatus）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "current_edge_lane_band（流缘-清水猎道带——current edges/clear-water prey lanes）"),
  ev("EVAL_TYPED_PREY_FACTOR", "small_fish_field（小鱼猎物场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『uses a visible, moving discrete target near current edges and clear-water prey lanes』——流缘清水猎道带先行",
  "B: normal2/redtail_barracuda.md §0 追击组（受限还原 unordered）",
  "C: benthopelagic / 20-32°C / 晨昏活跃"],
 [B7S.format(n="090"), CSV + "#RTB", "outputs/full_authoring/normal2/species/redtail_barracuda.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RTB"], B7B.format(c="RTB")],
 [])

add("RHM2", "091", "红钩鱼 Redhook Myleus（Myloplus rubripinnis）",
 ["floodplain = 洪泛平原资源可得性（植物/果实资源丰富区）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "floodplain_plant_fruit_patch（洪泛植物果实斑块——resource-rich edges）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story SS『looks for resource-rich edges and presents a discrete item rather than assuming continuous grazing. Patch context changes encounter opportunity』——patch 单因子（discrete item 呈现=Response 层；FCFI=P02→P01）",
  "B: 无表达文件",
  "C: benthopelagic / 植食性 / 23-27°C / 全天活跃"],
 [B7S.format(n="091"), CSV + "#RHM2", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RHM2"], B7B.format(c="RHM2")],
 ["与 RB-1 RHM（B5/R08-09 story——overhanging_vegetation_leaf_patch 单步）同种双 story 内容近似：真形复用+reused_from 标注"],
 reuse=dict(from_batch="CENSUS-REBUILD-001", from_pid="P-RB1-RHM-BAKE", note="同种双 story（R04 压缩 story 与 B5 R08-09 story）patch 单因子同形——复用 RB-1 真形；本批 story 侧 P02→P01 句式独立印证"))

add("STB", "092", "美洲条纹狼鲈 Striped Bass（Morone saxatilis）",
 ["lifecycle = 洄游改变机会暴露位置（migration changes where opportunity is exposed——不新建响应通道）"],
 [ev("EVAL_TYPED_PREY_FACTOR", "baitfish_concentration_patch（饵鱼集中斑块——bait concentration）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "estuary_current_band（河口-流带——current/temperature at the active depth）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: story SS『follows current, temperature and bait concentration, then presents a discrete target at the active depth』——follows bait（移动机会=饵鱼集中先行=FF），活动流带次之",
  "B: normal/striped_bass.md §0 机会组（受限还原单步）",
  "C: demersal 30m+ / 8-25°C / anadromous"],
 [B7S.format(n="092"), CSV + "#STB", "outputs/full_authoring/normal/species/striped_bass.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["STB"], B7B.format(c="STB")],
 [])

add("DVK", "093", "花羔红点鲑 Dolly Varden Trout（Salvelinus malma）",
 ["life_form = resident 与 migratory 型并存（form changes context and location before response semantics）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "coldwater_access_band（冷水可达带——coldwater access/seasonal movement）"),
  ev("EVAL_TYPED_PREY_FACTOR", "drift_prey_field（漂流猎物场——prey drift）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『follows coldwater access, seasonal movement and prey drift, then presents a discrete target in the active lane』——冷水可达带先行",
  "B: normal2/dolly_varden.md §0 机会组（受限还原单步）",
  "C: 4-16°C / 全天活跃"],
 [B7S.format(n="093"), CSV + "#DVK", "outputs/full_authoring/normal2/species/dolly_varden.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["DVK"], B7B.format(c="DVK")],
 [])

add("GJC", "094", "蓝笛鲷 Green Jobfish（Aprion virescens）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "reef_current_break_band（礁缘流隔带——structure/current breaks）"),
  ev("EVAL_TYPED_PREY_FACTOR", "schooling_prey_field（集群猎物场——schooling prey concentration）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『searches current breaks and structure, then places a discrete target where prey is concentrated. Current and depth reorder exposure』——流隔结构带先行（搜索位置先行）",
  "B: normal2/green_jobfish.md §0 追击组（受限还原 unordered）",
  "C: reef-associated 0-180m / 21.9-33.9°C"],
 [B7S.format(n="094"), CSV + "#GJC", "outputs/full_authoring/normal2/species/green_jobfish.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["GJC"], B7B.format(c="GJC")],
 [])

add("WBL", "095", "西方七鳃鳗 Western Brook Lamprey（非寄生型）",
 ["stage = ammocoete 幼体滤食与成体/产卵 lifecycle 分离（成体不映射常规钩饵故事——story 判语）",
  "non_parasitic = 非寄生种（与海七鳃鳗寄生阶段分型）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "fine_detritus_filter_field（细颗粒滤食场——幼体埋栖过滤细有机物）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story RB『larval ammocoete stage feeds by filtering fine material and adults do not map cleanly to a conventional predatory hook-bait story』——幼体滤食场单因子（成体面=无常规摄食程序，premise 阶段绑定）",
  "C: demersal 10m+ / 0.6-18°C / 夜间活跃 / anadromous"],
 [B7S.format(n="095"), CSV + "#WBL", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["WBL"], B7B.format(c="WBL")],
 ["Do not force into TargetFeeding or FieldFeeding until product scope explicit（story FCFI 原样——成体面挂 owner 边界开放）"])

add("CPT", "096", "链纹狗鱼 Chain Pickerel（Esox niger）",
 [],
 [gate("GATE_COVER_EXISTENCE", "vegetation_cover_present（植被掩体存在——vegetated shallow water 伏击位）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "cover_quality（植被缘掩体结构质量三档）")],
 "SpatialDistributionWeight", "GC", None,
 ["A: story RB『associated with vegetated cover and small fish prey』+SS『Work the vegetation edge with a discrete prey target and controlled pauses』——植被掩体先行（狗鱼科伏击形：PIK1/MUS 同科形）",
  "B: normal/chain_pickerel.md §0 追击组（受限还原 unordered——科形按伏击门推）",
  "C: demersal 0-6m / 10-20°C / 晨昏活跃 / non-migratory"],
 [B7S.format(n="096"), CSV + "#CPT", "outputs/full_authoring/normal/species/chain_pickerel.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CPT"], B7B.format(c="CPT")],
 [])

add("BIC", "097", "长吻鲍氏脂鲤 Bicuda（Boulengerella cuvieri）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "channel_edge_lane_band（河道边缘流道带——channel edges/moving-water lanes）"),
  ev("EVAL_TYPED_PREY_FACTOR", "small_fish_field（小鱼猎物场）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『works channel edges and moving-water lanes with a discrete target that matches small prey』——河道边缘流道带先行",
  "B: normal2/bicuda.md §0 追击组（受限还原 unordered）",
  "C: pelagic / 20-32°C / 晨昏活跃"],
 [B7S.format(n="097"), CSV + "#BIC", "outputs/full_authoring/normal2/species/bicuda.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BIC"], B7B.format(c="BIC")],
 [])

add("SS2", "098", "闪光鲟 Stellate Sturgeon（Acipenser stellatus）",
 ["lifecycle = 海河系统间洄游（migratory access——通达先行）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "anadromous_bottom_corridor（溯河底层廊道——migratory access）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_invert_field（底栖无脊椎猎物场——near the substrate）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『must find migratory access and bottom resource patches, then place discrete bait near the substrate』——洄游通达廊道先行（FCFI=P02→P01 with lifecycle migration）",
  "B: normal2/stellate_sturgeon.md §0 伏击组 GATE_ZONE（受限还原——story 侧通达+底斑两步无硬门直证）",
  "C: demersal 10-100m / 10-20°C / anadromous / 晨昏活跃"],
 [B7S.format(n="098"), CSV + "#SS2", "outputs/full_authoring/normal2/species/stellate_sturgeon.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SS2"], B7B.format(c="SS2")],
 ["与 RST1（同属俄罗斯鲟 FF 形）对照：RST1 食性主句先行（RB 首句=底栖摄食者）/SS2 通达先行（SS 首句=find migratory access）——同属不同 story 语序各自推导"])

add("TNS", "099", "露仙美鱥 Tennessee Shiner（Paranotropis leuciodus）",
 ["identity_sparse = 物种级公开证据稀疏（identity-only + 低置信小目标假设）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "shallow_flow_band（浅水流带——shallow-flow 低置信 placeholder）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story『Species-level public evidence available in this sweep is sparse……a cautious working hypothesis is shallow-flow small-target presentation（research lead 非 player-facing fact）』——低置信单因子 placeholder（不 promote 机制）",
  "B: 无表达文件（neighboring shiner 行为不 transfer——story Scope）",
  "C: demersal / 11-19°C / 早晨活跃"],
 [B7S.format(n="099"), CSV + "#TNS", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["TNS"], B7B.format(c="TNS")],
 [])

add("MAH", "100", "鬼头刀 Mahi-Mahi（Coryphaena hippurus）",
 ["transient_structure = 漂浮物聚集=transient structure（机会暴露——不替代目标评估）"],
 [ev("EVAL_TYPED_PREY_FACTOR", "baitfish_school_field（饵鱼群场——concentrated baitfish）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "flotsam_surface_band（漂浮物-表层带——floating structure/oceanic surface）")],
 "SpatialDistributionWeight", "FF", "HRQ-RB1-02",
 ["A: story SS『searches floating structure or bait concentration, then keeps a fast discrete target in the active layer. Structure exposes the opportunity』——饵鱼集中先行（搜索对象=食物），漂浮表层带次之",
  "B: normal/mahimahi.md §0 追击组（受限还原 unordered）",
  "C: pelagic-neritic 0-85m / 21-30°C / oceanodromous"],
 [B7S.format(n="100"), CSV + "#MAH", "outputs/full_authoring/normal/species/mahimahi.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MAH"], B7B.format(c="MAH")],
 [])

add("YTA", "101", "黄尾鰤 Yellowtail Amberjack（Seriola lalandi）",
 ["runtime_current = 流=runtime overlay（流改变机会暴露与深度）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "current_break_reef_band（流隔-礁缘带——current breaks/reef edges）"),
  ev("EVAL_TYPED_PREY_FACTOR", "baitfish_field（饵鱼场——baitfish aggregation）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『Search current breaks and baitfish aggregation, then place a discrete target in the moving strike lane』——搜索位置（流隔礁缘）先行（GJC 同句式同形）",
  "B: normal2/yellowtail_amberjack.md §0 追击组（受限还原 unordered）",
  "C: benthopelagic 3-825m / 18-24°C"],
 [B7S.format(n="101"), CSV + "#YTA", "outputs/full_authoring/normal2/species/yellowtail_amberjack.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["YTA"], B7B.format(c="YTA")],
 [])

add("BBF", "102", "黑牛胭脂鱼 Black Buffalo（Ictiobus niger）",
 ["season = 季节性河流移动改变 patch 可达（相邻 lifecycle）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "soft_bottom_transition_band（软底-流过渡带——soft-bottom/current-transition patches）"),
  ev("EVAL_TYPED_PREY_FACTOR", "benthic_invert_field（底栖无脊椎场——benthic material/invertebrates）")],
 "SpatialDistributionWeight", "SF", "HRQ-RB1-02",
 ["A: story SS『finds soft-bottom or current-transition patches, then offers a discrete bait at the feeding layer. Resource context changes exposure』——软底过渡带先行（FCFI=P02→P01）",
  "B: grazing/buffalo.md §0（I. bubalus 底质吸食面——本行 I. niger 同亚口科不同种，story 主体=P02 离散斑块非连续吸食）",
  "C: demersal / 17-27°C / 早晨活跃"],
 [B7S.format(n="102"), CSV + "#BBF", "outputs/full_authoring/grazing/species/buffalo.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BBF"], B7B.format(c="BBF")],
 ["亚口科种级区分：BBF/BIB1/BIB2 三行分列（B 文件 bubalus 注记原样）"])

# ===========================================================================
# 第 4 层 B7 110 —— FISH-R05 系（10）
# ===========================================================================
add("ROH", "103", "泰鲮 Rohu（Labeo rohita）",
 ["monsoon = 季风期洪泛河段中游产卵（P05 语义由 premise 承载——洄游窗聚集期定位）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "plant_substrate_field（植物-基质场——成体植食连续处理底质资源）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=Resource Patch → FieldFeeding（P06 连续基质处理）；季节由 P05 语义覆盖（premise）——场浓度单因子（story 级证据=植物资源场）",
  "B: grazing/rohu.md §0 两步方向（近底带→底质资源——Tier B 受限还原：story 级无顺序证据支持多步[RB-2 BHC/HER 判例同型]，单因子场记录）",
  "C: benthopelagic 5m+ / 植食性 / 20-32°C / potamodromous"],
 [B7S.format(n="103"), CSV + "#ROH", "outputs/full_authoring/grazing/species/rohu.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["ROH"], B7B.format(c="ROH")],
 [])

add("MRC", "104", "印度鲮 Mrigal Carp（Cirrhinus mrigala）",
 ["mechanism_open = 底柱摄食机制（particulate 拾取 vs 滤）未闭合（R02 教训：不从浮游食性推导滤食）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "plankton_benthic_field（浮游-底柱场——低营养级浮游/底柱资源）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=Food Field → FieldFeeding（P03）——机制开放留给证据闭合（单因子场）",
  "B: 无表达文件",
  "C: demersal / 20-32°C / 早晨活跃"],
 [B7S.format(n="104"), CSV + "#MRC", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MRC"], B7B.format(c="MRC")],
 ["同属鲮（MDC2）行级证据不互并"])

add("SPR", "105", "巴西鲷 Streaked Prochilod（Prochilodus lineatus）",
 ["iliophagy = 口特化吸食有机泥（illiophagous——SRCHECK 已核优势腐食者）",
  "long_migration = potamodromous 长距洄游>800-1000km（P05 premise——洄游窗聚集定位）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "organic_mud_detritus_field（有机泥-腐屑场——底栖腐屑连续摄取）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=Resource Patch（有机泥层）→ FieldFeeding（P06 连续基质处理）；洄游按 P05（premise）——场浓度单因子",
  "B: grazing/streaked_prochilod.md §0 三步方向（近底带→底泥→碎屑——Tier B 受限还原：story 级单因子[RB-2 BHC/HER 判例同型]）",
  "C: benthopelagic 5m+ / 植食性 / 17-27°C / potamodromous"],
 [B7S.format(n="105"), CSV + "#SPR", "outputs/full_authoring/grazing/species/streaked_prochilod.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SPR"], B7B.format(c="SPR")],
 [])

add("CHM", "106", "美洲锐唇鲷 Chiselmouth（Gila alutacea）",
 ["ontogenetic = 幼成食谱切换（幼体水面昆虫→成体硅藻刮食——P05 语义 premise）",
  "morphology = 下颌硬板+超长肠（刮食形态特化——板使用力学开放）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "diatom_periphyton_field（硅藻-附着层场——硬基质附着生物膜/丝藻连续刮食）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=附着藻层=Resource Patch → FieldFeeding（P06）；幼成切换=P05 语义（premise）——场浓度单因子",
  "B: grazing/chiselmouth.md §0 三步方向（底层定位→硬基质→附着资源——Tier B 受限还原：story 级单因子场）",
  "C: demersal / 植食性 / 11-19°C / 早晨活跃"],
 [B7S.format(n="106"), CSV + "#CHM", "outputs/full_authoring/grazing/species/chiselmouth.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CHM"], B7B.format(c="CHM")],
 [])

add("SHB", "107", "白条鱼 Sharpbelly（Hemiculter leucisculus）",
 ["surface_layer = 上层水域（上层属性由 Spatial/Habitat 表达——story LPE 原样）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "surface_drift_field（表层悬浮-漂流物场——zooplankton/insects/crustaceans/algae/detritus）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=Food Field → FieldFeeding（上层悬浮/漂流物场），虫类拾取含 TargetFeeding 次级——场浓度单因子（上层=场的空间属性不另立步）",
  "B: 无表达文件",
  "C: benthopelagic 0-10m / 杂食性 / 18-22°C / 早晨活跃"],
 [B7S.format(n="107"), CSV + "#SHB", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["SHB"], B7B.format(c="SHB")],
 [])

add("GTB", "108", "暹罗巨鲤 Giant Barb（Catlocarpio siamensis）",
 ["flood_window = 洪泛季果实窗（seasonal Resource Patch——P05 premise）",
  "stage_habitat = 幼成栖息分异（幼体沼泽小支流↔成体大河深潭——P05 语义 premise）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "flood_fruit_detritus_field（洪泛果实-腐屑场——藻/浮游/淹没陆生植物果实+腐屑）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=洪泛季果实窗=季节性 Resource Patch（P06）；阶段栖息分异=P05——场浓度单因子（双 premise）",
  "B: grazing/giant_barb.md §0（REV-001 B1 撤回标注——Tier B 撤回档不采；field/giant_barb.md=品系 L1 等效层）",
  "C: benthopelagic / 杂食性 / 20-32°C / potamodromous"],
 [B7S.format(n="108"), CSV + "#GTB", "outputs/full_authoring/grazing/species/giant_barb.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["GTB"], B7B.format(c="GTB")],
 [])

add("STL", "109", "小体鲟 Sterlet（Acipenser ruthenus）",
 ["season = 冬季 bottom holes 聚集不活动；春季上溯砾石滩强流产卵（冬穴-春溯——P05 premise）",
  "barbel_search = 吻下四长须底栖搜寻（形态证实，用途行为学开放）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "season_bound_bottom_hole_axis_segment（季节绑定底穴轴段——冬穴聚集↔春溯砾石滩）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story FCFI=底栖触须搜寻→Discrete Target（P01，patch 背景由 P02 语义兼容）；冬穴-春溯=季节差异（P05）——空间证据分辨率=季节底穴轴段单步",
  "B: 无表达文件（鲟系 RST1/SS2 互指不继承）",
  "C: demersal 1m+ / 杂食性 / 11-19°C / potamodromous / 晨昏活跃"],
 [B7S.format(n="109"), CSV + "#STL", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["STL"], B7B.format(c="STL")],
 [])

add("WCB", "110", "团头鲂 Wuchang Bream（Megalobrama amblycephala）",
 ["selective_grazing = 选择性放牧（Hydrilla 显著抑制/Vallisneria 条件化放过——SRCHECK 细化）"],
 [ev("EVAL_FOOD_FIELD_CONCENTRATION", "hydrilla_bed_field（沉水草床场——高等水生植物/沉水草连续啃食）")],
 "SpatialDistributionWeight", "FIELD", None,
 ["A: story FCFI=沉水草床=Resource Patch → FieldFeeding（P06 连续基质处理）——场浓度单因子（植物种类选择性=Profile 值域非结构）",
  "B: grazing/wuchang_bream.md §0 三步方向（近底带→草床构成→啃食资源——Tier B 受限还原：story 级单因子场；草床构成三档有 SRCHECK 直接证据→Profile 值域承载）",
  "C: benthopelagic 5-20m / 10-20°C / 早晨活跃"],
 [B7S.format(n="110"), CSV + "#WCB", "outputs/full_authoring/grazing/species/wuchang_bream.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["WCB"], B7B.format(c="WCB")],
 ["体长数据疑错与营养级冲突=story 数据发现注记（不静默改）"])

add("MRG", "111", "笋壳鱼 Marble Goby（Oxyeleotris marmorata）",
 ["burrow = 喜深软沙、掘穴/半埋（穴/掩体=持续结构占用）",
  "facultative_air = 兼性气呼吸（现实边界）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "burrow_hole_base（穴居底板——日间藏匿底部石草间/掘穴半埋）"),
  slot("low_light_night_slot（低光夜槽——夜行伏击窗口）")],
 "SpatialDistributionWeight", "NO", None,
 ["A: story RB『夜行伏击，日间藏于底部石草间不动；喜深软沙、掘穴/半埋』——穴居底板先行+夜槽（S7=MSF 夜视伏击/S8=MSF 穴-埋直证）",
  "B: normal/marble_goby_ambush.md §0 证据边界条款：『正文证实夜行低光主导（demersal 洞隙型常见）＝换 NOCTURNAL 标签（结构变更需重审）』——本批 story 正文证实夜行主导→按文件预留路径换 NO 形（guarding 批退回档为证据不足档，不采）",
  "C: demersal 10m+ / 22-28°C / 全天活跃（CSV 弱锚——story 夜行直证优先）"],
 [B7S.format(n="111"), CSV + "#MRG", "outputs/full_authoring/normal/species/marble_goby_ambush.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["MRG"], B7B.format(c="MRG")],
 ["B 文件边界条款兑现（GC→NO 结构变更需重审——本条目即重审产物，独立审复核点）"])

add("IDE", "112", "圆腹雅罗鱼 Ide（Leuciscus idus）",
 ["ontogenetic = 食性随龄切换（幼体杂食/沿岸→成体鱼食/深水大河大湖——JUVENILE/ADULT premise 配置级）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "ontogenetic_shore_deep_axis_segment（个体发生轴段——幼体沿岸浅水带↔成体深水/大河大湖）")],
 "SpatialDistributionWeight", "TS", None,
 ["A: story FCFI=Discrete Target（P01）；阶段差异（P05）——『Larger individuals feed mainly on fishes』+幼成栖息分异=轴段单步（个体发生切换属 lifecycle premise 层——PREMBIND 不变量）",
  "B: migration/ide.md §0 判断顺序=premise 读取→阶段绑定空间轴段归属三档（同序独立推导确认）",
  "C: benthopelagic 15m+ / 杂食性 / 4-20°C / potamodromous"],
 [B7S.format(n="112"), CSV + "#IDE", "outputs/full_authoring/migration/species/ide.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["IDE"], B7B.format(c="IDE")],
 [])

# ===========================================================================
# C9 立族材料 4（栖息面——面级守恒独立推导，不复用 RB-2 护巢面真形）
# 逐鱼推导：原 RS1 修复轮四鱼『4/4 同形』经裁决 2-B 判为 BA-NORMAL-HABITAT-FIT 约定序
# 伪影；本批以 story/CSV/B 文件因子集+逐鱼特化锚独立推序（不套 §2.4 声明序）。
# ===========================================================================
add("BLU-HAB", "028", "蓝鳃太阳鱼 Bluegill（栖息面）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "structure_vegetation_band（结构-植被带——巢区/掩体/植被结构区[结构先行]）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_soft_layer（底中软水层——软定位档位归属轴）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "broad_temperature_band（宽温带——1-36°C 宽带弱分档）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "crepuscular_time_band（晨昏时段带）")],
 "SpatialDistributionWeight", "C9_BLU", None,
 ["裁决锚：HRQ-ADJUDICATION §6.2 原文举例『蓝鳃→结构先行』（人类裁决已给推导方向——蓝鳃空间行为第一约束=结构）",
  "A: B01-S38 story（护巢觅食食卵）栖息语境=巢区/浅水硬底（结构依赖）",
  "B: guarding/bluegill.md §0 Normal 面因子集=水层（软）/结构/水温/时段（序声明为约定序不采；因子集可用）",
  "C: benthopelagic（软定位）/ 1-36°C（极宽=弱分档）/ 晨昏活跃——证据强度递减排序：结构（裁决锚）→水层（软定位）→水温（宽带）→时段（弱锚）"],
 [B7S.format(n="028"), CSV + "#BLU2", "outputs/full_authoring/guarding/species/bluegill.md#S0-Normal-face", RS1HAB.format(p="P-RS1-BLU-HAB-BAKE"), "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["BLU-HAB"]],
 ["C9 终裁材料：与 RS1 冻结体（水层→结构→水温→时段）ORDER 不同——结构先行版"])

add("ARA-HAB", None, "巨骨舌鱼 Arapaima（Arapaima gigas，栖息面）",
 [],
 [gate("GATE_ZONE", "demersal_bottom_zone（底层硬定位——CSV demersal，非底层=出局）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "narrow_warm_temperature_band（窄暖温带——25-29°C ±2 强分档）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "floodplain_wood_structure（洪泛林木质结构——掩体方向级）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "crepuscular_time_band（晨昏时段带）")],
 "SpatialDistributionWeight", "C9_ARA", None,
 ["C: CSV=巨骨舌鱼 demersal / 25-29°C（窄带）/ 晨昏活跃——硬定位（出局语义）先行=第一过滤；窄暖温带（CSV 直证强分档）次之；洪泛林结构（B 文件方向级 [需正文]）第三；晨昏最后",
  "B: guarding/arapaima.md §0 Normal 面因子集=水层硬定位（demersal）/结构/水温/时段（序声明为约定序不采；因子集可用）",
  "与 B 文件声明序差异：水温与结构互换（依据=CSV 窄温带证据强度>结构 [需正文] 方向级）——逐鱼推导产物"],
 ["outputs/fish-reference-20260908/fish-reference-20260908.csv#巨骨舌鱼", "outputs/full_authoring/guarding/species/arapaima.md#S0-Normal-face", RS1HAB.format(p="P-RS1-ARA-HAB-BAKE"), "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["ARA-HAB"]],
 ["C9 终裁材料：与 RS1 冻结体 ORDER 不同——门化+温序前置版"])

add("RBP-HAB", None, "红腹食人鱼 Red-bellied Piranha（Pygocentrus nattereri，栖息面）",
 [],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "midupper_pelagic_soft_layer（中上软水层——CSV pelagic 主体空间带）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "narrow_warm_temperature_band（窄暖温带——23-27°C ±2 强分档）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "submerged_structure（沉水结构——树根/植被掩体次级锚）")],
 "SpatialDistributionWeight", "C9_RBP", None,
 ["C: CSV=红腹食人鱼 pelagic / 23-27°C（窄带）/ 全天活跃——主体空间带（软定位）先行；窄温带次之；沉水结构（B 文件护巢面树根/水草丛佐证其结构生态=Normal 面次级锚）第三；全天活跃=无时段分档（时段步不入链——证据驱动）",
  "B: guarding/red_bellied_piranha.md §0 Normal 面因子集=水层（软）/结构/水温/时段（全天）（序声明为约定序不采）",
  "Frenzy 群游无证据（negative knowledge 原样——不立群游轴）"],
 ["outputs/fish-reference-20260908/fish-reference-20260908.csv#红腹食人鱼", "outputs/full_authoring/guarding/species/red_bellied_piranha.md#S0-Normal-face", RS1HAB.format(p="P-RS1-RBP-HAB-BAKE"), "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["RBP-HAB"]],
 ["C9 终裁材料：三步形（时段不入链）——与 RS1 冻结体链长+序均不同"])

add("HNC-HAB", None, "双点美鱥 Hornyhead Chub（Nocomis biguttatus，栖息面）",
 [],
 [gate("GATE_ZONE", "demersal_gravel_zone（底层砾石硬定位——美鱥口器形态绑定底层取食/筑巢，非底层=出局）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "gravel_run_structure（砾石潭渊结构——筑巢基质/掩体）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "cool_temperature_band（冷水温带——溪流冷水向）"),
  ev("EVAL_TYPED_HABITAT_FACTOR", "morning_time_band（早晨时段带）")],
 "SpatialDistributionWeight", "C9_HNC", None,
 ["裁决锚：HRQ-ADJUDICATION §6.2 原文举例『美鱥口器形态→水层先行』（人类裁决已给推导方向——口器特化绑定底层取食→底层水层定位先行）",
  "B: guarding/hornyhead_chub.md §0 Normal 面因子集=水层硬定位（demersal）/结构/水温/时段（早晨）（序声明为约定序不采；硬定位出局语义=第一步门化[RB-1 GRH/RRH bottom_layer_zone GATE 化判例]）",
  "C: demersal / 溪流冷水 / 早晨活跃——口器特化（底层砾石取食+筑巢）→结构（砾石）→水温（冷水）→时段（早晨）"],
 ["outputs/full_authoring/guarding/species/hornyhead_chub.md#S0-Normal-face", RS1HAB.format(p="P-RS1-HNC-HAB-BAKE"), "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["HNC-HAB"]],
 ["C9 终裁材料：门化四步——与 RS1 冻结体序同但首步 GATE 化（硬定位出局语义）"])

# ===========================================================================
# brooted 挂起终裁 2（Response 面——退化链 vs 全链裁决；产出=HRQ 终裁提案）
# ===========================================================================
add("ARO-RESP", None, "银龙鱼 Silver Arowana（Osteoglossum bicirrhosum，雄鱼口哺面）",
 ["guard_condition = 雄鱼口哺携带卵/幼近 6 周（『carries eggs, larvae and early juveniles in his mouth』——携带型持续守护）",
  "feeding_state_open = 口哺期摄食状态开放（常态水面跳跃捕食与口哺并存——口哺期是否强停食无直证）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "brood_anchor_present（口哺锚存在性——与个体绑定的携带型锚）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "brooding_home_range_quality（口哺期常驻区适配——单 Factor 三档）")],
 "BroodingSpatialDistributionWeight", "BROODED", None,
 ["裁决材料（退化链方向）：①guarding/nile_tilapia.md §0 Brooding 面退化链判读（『口孵锚与个体绑定——无关系轴/无温度轴/无合并步』）为 B 层唯一口孵型判读先例；②ARO story『carries…in his mouth』=携带型同构（锚在口中=无锚址距离/朝向的空间关系语义）；③B 系列无银龙 guard 面（normal2/silver_arowana.md §0：P04 边界归 Guarding 系补批未做——无对立证据）",
  "B5 盲形全链（PARALLEL 双 Path+关系评估）=P04 契约模板套用（『携带型 vs 结构型 anchor 差异留判同阶段』——B5 冻结体自注），非银龙特有证据",
  "保留张力：口哺期水面跳跃捕食并存的生理张力（罗非口孵=强 Feeding Cap；银龙开放）——若后续证据证实口哺期全功能摄食+冲突并行，双 Path 读法可复活（HRQ 终裁项）"],
 ["fish_logic_census/batches/CENSUS-B5/input_snapshots/story_ARO.md", "fish_logic_census/batches/CENSUS-B5/blind_programs.jsonl#P-B5-ARO-RESP", "outputs/full_authoring/guarding/species/nile_tilapia.md#S0-Brooding-face", "outputs/full_authoring/normal2/species/silver_arowana.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["ARO-RESP"]],
 ["brooted 终裁提案=退化链（brooded 结构级不入 GUARD_ANCHOR 四形式——与罗非先例同构）；B5 全链盲形降级为契约套用记录"])

add("TIL3-RESP", None, "罗非鱼 Nile Tilapia（雄鱼领地面——queue 笔误 P-B0 本体 P-B7-TIL3-RESP）",
 ["territory = 雄鱼建立繁殖领地（本 story 冻结行=领地防御——与雌鱼口哺非同一关系对象）",
  "adjacent_face = 雌鱼口哺面=B 文件 Brooding 退化链（分面记账）"],
 [ev("EVAL_TYPED_HABITAT_FACTOR", "territory_bound_axis_segment（雄鱼领地轴段——繁殖巢区防区）")],
 "SpatialDistributionWeight", "BROODED_TIL3", None,
 ["裁决材料：①story S43 FCFI=Territory relation + reproductive Condition（『P04 只作为竞争参照，先区分领地与护卵』）——本 story 主体=雄鱼领地面非口哺面；②guarding/nile_tilapia.md §0 Brooding 面=雌鱼口哺退化链（锚与个体绑定——B 层直证）；③MUT 挂起登记细名=tilapia_territory（雄鱼繁殖领地——领地与幼体非同一关系对象）",
  "终裁提案分两面：雌鱼口哺面=退化链边界确认（brooded 结构级不入 GUARD_ANCHOR——B 文件退化链直证）；雄鱼领地面=非 brooded 程序（territory=关系对象非后代空间存在形式——无卵/幼锚），按 premise+轴段落 TS（与 TIL3 Bake 面同体）"],
 [B7S.format(n="032"), "outputs/full_authoring/guarding/species/nile_tilapia.md#S0-Brooding-face", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["TIL3-RESP"], "fish_logic_census/template_registry.yaml#GUARD-v9-brooded-P-B7-TIL3-RESP"],
 ["queue program_id 前缀 P-B0 为登记笔误（本体=P-B7-TIL3-RESP，registry v9 行内 blind_hash=3e1cf6343317da2c）——记档不改 queue"])

# ===========================================================================
# form_hold 挂起终裁 2（anchor 四形式证据定形；产出=HRQ 终裁提案）
# ===========================================================================
add("CSL-RESP", None, "中华沙塘鳢 Chinese Sleeper（Perccottus glenii，护卵幼面）",
 ["guard_condition = 雄鱼护卵+浮游幼体持续（『Males guard the eggs and pelagic larvae』——守护对象跨卵+浮游幼两阶段）",
  "overwinter_adjacent = 钻泥蛰伏冬眠=肺鱼式蛰伏第 2 例（P05 季节/状态语义——非本面）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "fry_larvae_anchor_present（稚幼群锚存在性——pelagic larvae 浮游幼体群）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "brood_habitat_quality（群栖境适配三档——静水植被区）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（护幼关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA_CSL", None,
 ["form_hold 终裁材料：story 引文『guard the eggs and pelagic larvae』——pelagic larvae=浮游幼体（fry_school 形式直证）；egg 阶段无巢构建/附着面判别词（B5 冻结证据无巢/构建判别词——MUT 批 REV-001 F1 原文）→不虚构 nest/egg_mass（无证据不定形）",
  "终裁提案=anchor 形式 fry_school（以 larvae 阶段直证定形；egg 阶段形式 open 留注记——与 MUT 批按初始形式落 nest 的落位注记分歧，以 story 直证为准）",
  "B 系列无 CSL 文件（B5 纯正文 7 例之一）——story 引文为唯一证据源"],
 ["fish_logic_census/batches/CENSUS-B5/input_snapshots/story_CSL.md", "fish_logic_census/batches/CENSUS-B5/blind_programs.jsonl#P-B5-CSL-RESP", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CSL-RESP"]],
 ["HRQ 终裁项：egg 阶段形式 open（后续巢/附着证据补定）"])

add("CSN1-RESP", "049", "乌鳢 Northern Snakehead（护幼面，Channa argus）",
 ["guard_condition = 繁殖期亲鱼守护卵和幼鱼（浮巢孵化后护幼——植被浮巢育幼）"],
 [gate("GATE_GUARD_ANCHOR_EXISTENCE", "fry_school_anchor_present（稚鱼群锚存在性——浮巢孵化后的植被区移动稚鱼群）"),
  ev("EVAL_ANCHOR_SITE_SUITABILITY", "brood_habitat_quality（植被掩体群栖境适配三档）"),
  ev("EVAL_GUARD_RELATION", "guard_relation（环护关系三档）"),
  ev("EVAL_GUARD_LOCAL_TEMPERATURE", "guard_local_temperature（局部水温三档）")],
 "GuardingSpatialDistributionWeight", "GA_CSN1", None,
 ["form_hold 终裁材料：guarding/snakehead.md §0 直证『锚点：fry_school（浮巢孵化后的稚鱼群，植被区移动锚）；GuardAnchor Resolver 实例=Fry/Brood Field（§11.2 泛化）』",
  "终裁提案=anchor 形式 fry_school（B 文件 §0 直证+story 护幼主体[『伏击捕食与护幼关系切换』的冻结行=护幼关系]；初始浮巢阶段为相邻阶段不在本 story 冻结行——跨阶段按 MUT 判例②的注记原则留 open 而非虚构 nest）",
  "story RB『繁殖期亲鱼可守护卵和幼鱼』——守护对象跨阶段，主体=护幼切换"],
 [B7S.format(n="049"), "outputs/full_authoring/guarding/species/snakehead.md#S0", "fish_logic_census/truth_rebuild_queue.jsonl#" + QIDS["CSN1-RESP"]],
 [])

# ===========================================================================
# 写出 blind_programs.jsonl（冻结体——registry 未开）
# ===========================================================================
def main():
    out_path = BATCH / "blind_programs.jsonl"
    rows = []
    for f in F:
        pid = "P-RB3-" + f["code"] + ("-BAKE" if not f["code"].endswith(("HAB", "RESP")) else "-BAKE" if f["code"].endswith("HAB") else "-RESP")
        # HAB -> P-RB3-<CODE>-HAB-BAKE ; RESP -> P-RB3-<CODE>-RESP
        sid = "CENSUS-REBUILD-003-" + f["code"]
        evid = list(f["evid"])
        if f["snap"]:
            evid.insert(0, B7S.format(n=f["snap"]))
        basis = list(f["basis"])
        if f["reuse"]:
            basis.insert(0, "reused_from=" + f["reuse"]["from_pid"] + "（" + f["reuse"]["from_batch"] + "）——" + f["reuse"]["note"])
        rec = {
            "program_id": pid,
            "story_id": sid,
            "species_id": f["code"],
            "surface": "Bake",
            "incoming_premises": f["prem"],
            "surface_owned_logic": {
                "chain_semantics": "PROGRESSIVE_TIERED_FUNNEL（渐进累积：每步 EVAL→三档→乘入 running weight；×0.01 软出局立即返回；无终步合并）",
                "ordered_steps": f["steps"],
            },
            "human_readable_sketch": sketch_of(f["steps"], "｜" + f["sp"] + "：栖息/分布位置权重链。" if not f["code"].endswith("RESP") else "｜" + f["sp"] + "。"),
            "branches": branches_of(f["steps"]),
            "combine": "NONE_PROGRESSIVE",
            "return_type": f["ret"],
            "instance_noise": {"species": f["sp"], "profile": None},
            "helpers": [],
            "source_evidence_ids": evid,
            "open_semantics": f["open"],
            "order_derivation": {
                "status": "reused_truth_form" if f["reuse"] else "derived",
                "basis": basis,
                "evidence_layers": LAB if any("outputs/full_authoring" in e for e in evid) else LA,
                "queues": [QIDS[f["code"]]],
                "dual_track": bool(f["reuse"]),
            },
            "registry_seen": False,
            "registry_seen_at_creation": False,
            "blind_hash": None,
            "frozen_at_utc": None,
        }
        rows.append(rec)
    # hash + freeze
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for rec in rows:
        body = json.dumps({k: v for k, v in rec.items() if k not in ("blind_hash", "frozen_at_utc")}, ensure_ascii=False, sort_keys=True)
        rec["blind_hash"] = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
        rec["frozen_at_utc"] = now
    with open(out_path, "w", encoding="utf-8") as fh:
        for rec in rows:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("froze", len(rows), "programs at", now)
if __name__ == "__main__":
    main()
