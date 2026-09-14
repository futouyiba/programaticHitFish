# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-002（RB-2）盲重建：终局全库顺序还原重跑第 2 批。

输入=truth_rebuild_queue.jsonl 两组 94 项：
- AMB 四层链第 3 层（B6 47）：B6 R10 压缩 story 快照（Tier A）+B6 批档盲体（Tier C 对照）+CSV；
- 链族在册 order_provisional 成员（47）：RS1 批档冻结链（Tier C 对照）+原批 story 快照
  （B3/B4 有档；B1/B2 无 story 文本档→Tier C 冻结 sketch 事实）+表达文件 §0/§2.2（Tier B
  对照不照抄）+CSV。18 尾与 RB-1 同鱼同面（17 尾 B4 起源 + WS2↔WST 同种）——复用 RB-1
  真形并标注 reused_from；RBP 为同鱼异面（RB-1=摄食面/本项=护巢面 §2.2）→独立推导。

盲纪律：本脚本运行时 registry v9 尚未打开（registry_seen=false 全体）；骨架只描述观察到的
行为结构（渐进累积语义，三档=全额/×衰减/×0.01 软出局），不携带 extension/新轴/族名提案
语汇；判同提案只在 merge_tests/HRQ 段。

程序 ID 约定：P-RB2-<CODE>-BAKE；story ID：CENSUS-REBUILD-002-<CODE>。
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCH = Path(__file__).parent
RB1 = ROOT / "fish_logic_census/batches/CENSUS-REBUILD-001/blind_programs.jsonl"

QUEUE = {}
for line in (ROOT / "fish_logic_census/truth_rebuild_queue.jsonl").read_text(encoding="utf-8").splitlines():
    r = json.loads(line)
    QUEUE[r["program_id"]] = r["queue_id"]

T3 = ["preferred=全额", "tolerated=×衰减(不清零)", "excluded=×0.01 软出局立即返回"]
T2 = ["成立=进入下一步", "不成立=EARLY_RETURN 返回 0"]
TSLOT = ["槽内=全额", "槽邻=×衰减(不清零)", "槽外=×0.01 软出局立即返回"]


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
    return ("【RB-2 终局顺序还原重跑真形】渐进累积链（无合并步）：" + " → ".join(parts)
            + "。每 EVAL 步三档=全额/×衰减/×0.01 软出局立即返回；GATE 硬门 EARLY_RETURN。" + note)


CSV = "outputs/fish-reference-20260908/fish-reference-20260908.csv"
B6S = "fish_logic_census/batches/CENSUS-B6/input_snapshots/story_{c}.md"
B3S = "fish_logic_census/batches/CENSUS-B3/input_snapshots/story_{c}.md"
B12B = "fish_logic_census/batches/{b}/blind_programs.jsonl#P-{b2}-{c}-BAKE"
B12S = "fish_logic_census/batches/{b}/stories.jsonl#CENSUS-{b2}-{c}"
RS1B = "fish_logic_census/batches/CENSUS-RERUN-SINGLE-001/blind_programs.jsonl#P-RS1-{c}-BAKE"
B4S = "fish_logic_census/batches/CENSUS-B4/input_snapshots/story_{c}.md"
B6B = "fish_logic_census/batches/CENSUS-B6/blind_programs.jsonl#P-B6-{c}-BAKE"

LA = ["A=frozen census story snapshot (Tier A)"]
LA2 = ["A=frozen census story snapshot (Tier A)",
       "B=B-series expression file (Tier B constrained restoration - NOT copied)",
       "C=fish-reference-20260908.csv eco-morphology"]
LA12 = ["A=story text NOT archived (B1/B2 batches kept no input_snapshots)",
        "C'=B1/B2 census frozen blind sketch (Tier C story-derived facts)",
        "B=B-series expression file (Tier B constrained restoration - NOT copied)",
        "C=fish-reference-20260908.csv eco-morphology"]
LAB6 = ["A=frozen census story snapshot (Tier A, R10 compressed)",
        "C'=B6 census frozen bake blind (Tier C flat-form contrast only)",
        "C=fish-reference-20260908.csv eco-morphology"]

# ---------------------------------------------------------------------------
# 手写真形表：code, species, premises, steps, return_type, basis, evid, open
# ---------------------------------------------------------------------------
F = []

# ===== B6 47（第 3 层 AMB）=====
F += [
 dict(code="SUK", sp="四白锦鲤 Shiro Utsuri Koi（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 锦鲤 R03 品系复用先例（Identity Deferred——品系外观/养殖条件不构成机制差异，story 明言）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用锦鲤 R03 先例，S1-S11 全 SN——无独立机制证据，真形分辨率=同种物种级",
          "C: Cyprinus carpio benthopelagic 0-29m / 3-35°C / 早晨活跃 / 杂食（源表食性条目口径差异不采）",
          "B: 无表达文件（R10 品系行不在 B 系列表达集）"],
  evid=[B6S.format(c="SUK"), CSV + "#SUK", B6B.format(c="SUK"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0078"],
  open=["亲本（鲤/锦鲤 R03 轨）真形不在重跑队列——本真形以同种 CSV 单因子分辨率记录，亲本批补证后可升档"]),
 dict(code="GRK", sp="圆点五色锦鲤 Goromo Koi（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 锦鲤 R03 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用锦鲤 R03 先例，S1-S11 全 SN——同种物种级分辨率",
          "C: Cyprinus carpio benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="GRK"), CSV + "#GRK", B6B.format(c="GRK"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0079"],
  open=["亲本真形待 R03 轨（同 SUK 注记）"]),
 dict(code="KHK", sp="红白锦鲤 Kohaku Koi（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 锦鲤 R03 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用锦鲤 R03 先例，S1-S11 全 SN", "C: Cyprinus carpio benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="KHK"), CSV + "#KHK", B6B.format(c="KHK"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0080"],
  open=["亲本真形待 R03 轨（同 SUK 注记）"]),
 dict(code="OGK", sp="橙黄金锦鲤 Ogon Koi（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 锦鲤 R03 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用锦鲤 R03 先例，S1-S11 全 SN", "C: Cyprinus carpio benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="OGK"), CSV + "#OGK", B6B.format(c="OGK"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0081"],
  open=["亲本真形待 R03 轨（同 SUK 注记）"]),
 dict(code="LCP", sp="无鳞鲤 Leather Carp（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 镜鲤 R03 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用镜鲤 R03 先例，S1-S11 全 SN——同种物种级分辨率", "C: Cyprinus carpio benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="LCP"), CSV + "#LCP", B6B.format(c="LCP"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0082"],
  open=["亲本真形待 R03 轨（同 SUK 注记）"]),
 dict(code="AMC", sp="镜鲤白化 Albino Mirror Carp（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 镜鲤 R03 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用镜鲤 R03 先例，S1-S11 全 SN", "C: Cyprinus carpio benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="AMC"), CSV + "#AMC", B6B.format(c="AMC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0083"],
  open=["亲本真形待 R03 轨（同 SUK 注记）"]),
 dict(code="ASC", sp="鳞鲤白化 Albino Scale Carp（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 鳞鲤 R03 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用鳞鲤先例，S1-S11 全 SN", "C: Cyprinus carpio benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="ASC"), CSV + "#ASC", B6B.format(c="ASC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0084"],
  open=["亲本真形待 R03 轨（同 SUK 注记）"]),
 dict(code="HFC", sp="鳞鲤人面鲤 Human Face Scale Carp（Cyprinus carpio 品系）", prem=[
   "strain_reuse = 鳞鲤 R03 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "benthopelagic_slowwater_band（同种鲤 CSV benthopelagic 软定位——静水湖沼带）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 品系复用鳞鲤先例，S1-S11 全 SN", "C: Cyprinus carpio benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="HFC"), CSV + "#HFC", B6B.format(c="HFC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0085"],
  open=["亲本真形待 R03 轨（同 SUK 注记）"]),
 dict(code="AGC", sp="白化草鱼 Albino Grass Carp（Ctenopharyngodon idella 白化品系）", prem=[
   "strain_reuse = 草鱼 B01 品系复用先例（Identity Deferred——P01+P02 复用 grazing）"],
  steps=[gate("GATE_PATCH_PRESENCE", "herbivore_patch_presence（植食资源+预投饵斑块存在——同种 GRB 本批真形复用：斑块追随先验=存在性先行）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "herbivore_patch_quality（斑块质量档——水生植物/预投饵双构成同源评估）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '复用草鱼 B01 grazing'（P01+P02）——同种 GRB 本批真形（存在门→质量档两步）复用；品系无独立机制证据",
          "C: Ctenopharyngodon idella benthopelagic 0-30m / 植食性 browsing / 2 / 温和（与 GRB 同行）",
          "去重联动：AGC↔GRB 同种 Cross-Batch 品系（本批内互指）", "B: 无表达文件（R10 品系行）"],
  evid=[B6S.format(c="AGC"), CSV + "#AGC", B6B.format(c="AGC"), RS1B.format(c="GRB"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0x"],
  open=["同种 GRB 轨真形互指——品系行零独立证据，GRB 补证后联动复核"]),
 dict(code="WAG", sp="白金火箭 White Alligator Gar（Atractosteus spatula 白化品系）", prem=[
   "strain_reuse = 鳄雀鳝 B01 品系复用先例（Identity Deferred）"],
  steps=[gate("GATE_VEGETATION_EDGE", "vegetation_edge_cover_present（植被缘掩体存在——雀鳝科伏击构型，复用 B01 伏击 story 明言）"),
          ev("EVAL_TYPED_STRUCTURE_FACTOR", "vegetation_slack_cover_quality（植被/缓流掩体结构档）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '复用 B01 伏击'——伏击构型=结构掩体绑定（门先行：无掩体格不产生伏击分布）",
          "C: Atractosteus spatula demersal / 晨昏活跃 / 孤僻——底栖伏击锚",
          "同科对照：本批 FGA/SGA 雀鳝科真形同构（植被/缓流掩体门→掩体档）", "B: 无表达文件（R10 品系行）"],
  evid=[B6S.format(c="WAG"), CSV + "#WAG", B6B.format(c="WAG"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0086"],
  open=[]),
 dict(code="WCC", sp="白化叉尾鮰 White Channel Catfish（Ictalurus punctatus 白化品系）", prem=[
   "strain_reuse = 叉尾鮰 B01 品系复用先例（Identity Deferred）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "bottom_pool_structure_base（底层潭沼结构底板——Ictalurus 鲿形目夜行底栖构型）"),
          slot("low_light_night_slot（低光/夜相槽——同种 CSV 夜间活跃锚）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '复用 B01'——叉尾鮰机制复用", "C: Ictalurus punctatus demersal 0-15m / 夜间活跃 / 杂食 variable——底栖夜行双锚",
          "同批同构：BBH/BCF/WHC 鲿形目夜行底栖真形（底板档→夜槽）", "B: 无表达文件"],
  evid=[B6S.format(c="WCC"), CSV + "#WCC", B6B.format(c="WCC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0087"],
  open=[]),
 dict(code="HYS", sp="杂交鲟 Hybrid Sturgeon（Acipenser schrenckii × Huso dauricus）", prem=[
   "hybrid_sterile = 杂交不育（生活史 premise）",
   "parent_reuse = 复用飼系 P01+P05（story 明言——亲本机制复用非未消解推断）",
   "anadromous_parent = 亲本溯河域切换（P05 premise）"],
  steps=[gate("GATE_ZONE", "bottom_layer_zone（底层水层带——鲟形目底栖触须特化硬定位）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_probing_field（底栖探食场——甲壳/软体/虫，亲本飼系 P01 复用）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '复用飼系 P01+P05'+库锚即杂交式学名——亲本线复用为 story 自身机制陈述",
          "C: 杂交鲟行 晨昏活跃 10-20°C（栖息带字段空——亲本施氏鲟鲟形目底栖构型补位）",
          "同形对照：WS2/WST/AST 鲟形目真形（底层硬门→底栖探食场）", "B: 无表达文件"],
  evid=[B6S.format(c="HYS"), CSV + "#HYS", B6B.format(c="HYS"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0088"],
  open=["杂交行 CSV 栖息带字段空——底栖定位依亲本鲟形目构型，亲本行补证后复核"]),
 dict(code="ACA", sp="土鲶 Amur Catfish（Silurus asotus）", prem=[
   "nocturnal_congener = 夜行同属推算（S7 EO——'与欧洲巨鲶 R06 同属'夜行鲶系同构，story 明言）",
   "piscivore_adult = 成体全鱼食（S1——食性主句，Response 层取向）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "silurid_hole_structure_base（鲶系河湖底结构底板——Silurus 同属巨鲶同构）"),
          slot("low_light_night_slot（低光/夜相槽——CSV 夜间活跃锚+同属夜行推算）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'Adults feed on all types of fish'+夜行鲶系同构（同属第 2 例）+S8 MSF(河湖)——底板主句先行",
          "C: Silurus asotus demersal / 夜间活跃 / 4.43 / 孤僻",
          "同属对照：本批 WEL 摄食面真形同构（结构底板→夜槽）", "B: 无表达文件"],
  evid=[B6S.format(c="ACA"), CSV + "#ACA", B6B.format(c="ACA"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0089"],
  open=[]),
 dict(code="AMN", sp="柳根鱼 Amur Minnow（Rhynchocypris lagowskii）", prem=[
   "diet_eo = 食性未述（同属推算 3.5——S1 EO，forage 轴不立）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "river_current_band（河川带——S8 MSF 单因子）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(同属推算)+S8 MSF(河川)——证据分辨率=单因子（forage 轴不立）",
          "C: Rhynchocypris lagowskii benthopelagic / 早晨活跃 / 躲藏", "B: 无表达文件"],
  evid=[B6S.format(c="AMN"), CSV + "#AMN", B6B.format(c="AMN"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0090"],
  open=["食性补证后可能升两步链"]),
 dict(code="ASB", sp="海鲈鱼 Asian Seabass（Lateolabrax japonicus 系）", prem=[
   "catadromous = 幼河成海降海产卵（域切换 P05 premise——S5）",
   "protandry = 雄先熟性转换（繁殖系统变量 S9 premise，非 Mode）",
   "winter_deep_reef_spawn = 冬季深岩礁产卵（S6 premise）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "fish_shrimp_piscivore_field（成鱼鱼虾猎物场——幼浮游→成 small fish and shrimps 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "inshore_reef_band（近岸岩礁带——S8 单要素栖息句次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '幼浮游→成 small fish and shrimps' 食性主句（含发育切换信息）先行；S8 近岸岩礁单要素次之——开放水跟随型读法",
          "C: Lateolabrax japonicus reef-associated / catadromous / 晨昏活跃 / 3.1", "B: 无表达文件"],
  evid=[B6S.format(c="ASB"), CSV + "#ASB", B6B.format(c="ASB"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0091"],
  open=[]),
 dict(code="ATC", sp="大西洋小鳕 Atlantic Tomcod（Microgadus tomcod）", prem=[
   "anadromous = 溯河洄游（域切换 P05 premise——S5）"],
  steps=[gate("GATE_ZONE", "bottom_layer_zone（底层水层带——demersal CSV 硬定位+鳕科微型底栖特化）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_small_fauna_field（小型底栖食场——shrimps/amphipods 甲壳+worms/贝/鱿/鱼）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'feed mostly on small crustaceans...also worms, small mollusks, squids and fishes'+S8 沿岸/咸淡水——底层硬定位先行，底栖小动物场次之",
          "C: Microgadus tomcod demersal 0-69m / 4.4-8.4°C / anadromous / 追猎",
          "同形对照：INC/WST/ATC 鳕形-鲟形 demersal 硬门→底栖食场", "B: 无表达文件"],
  evid=[B6S.format(c="ATC"), CSV + "#ATC", B6B.format(c="ATC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0092"],
  open=[]),
 dict(code="AWF", sp="大西洋狼鱼 Atlantic Wolffish（Anarhichas lupus）", prem=[
   "egg_guard_male = 雄护卵块至孵化（P04 语境——guard 面 premise 注记，不进 Bake 分布链）",
   "fasting_while_guarding = 护卵期 the male hardly feeds（停食 premise——护卵型停食判例族）",
   "crusher_dentition = 狼鱼科特殊碾压齿（口器特化——Response/呈现层注记不进 Bake 判断步）"],
  steps=[gate("GATE_ZONE", "rock_bottom_zone（岩底带——'岩底 18-110m' S8+demersal CSV 硬定位）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "hard_shell_fauna_field（硬壳猎物场——mollusks/crabs/lobsters/urchins 棘皮+鱼）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'hard-shelled mollusks, crabs, lobsters, sea urchins'+鱼 / 岩底 18-110m（S8）——岩底硬定位先行，硬壳猎物场次之",
          "C: Anarhichas lupus demersal 1-600m / 5.8-9.8°C / oceanodromous", "B: 无表达文件"],
  evid=[B6S.format(c="AWF"), CSV + "#AWF", B6B.format(c="AWF"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0093"],
  open=["碾压齿独立碾碎机制 R04 条纹狼鱼同型未做——孤例注记（Response 线）"]),
 dict(code="BBH", sp="黑鮰 Black Bullhead（Ameiurus melas）", prem=[
   "mixed_diet = 虫/贝/植物/鱼广食（S1——取向注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "soft_pool_swamp_base（软底潭沼底板——S8+鲿科第 4 例底栖构型）"),
          slot("low_light_night_slot（低光/夜相槽——S7 MSF 夜行 story 原文）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 夜行（S7 MSF）+软底潭沼（S8 MSF）——夜行底板先行，夜相槽次之（GDE 判例同型）",
          "C: Ameiurus melas demersal / 夜间活跃 / 3.81", "B: 无表达文件"],
  evid=[B6S.format(c="BBH"), CSV + "#BBH", B6B.format(c="BBH"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0094"],
  open=[]),
 dict(code="BCF", sp="蓝鲶鱼 Blue Catfish（Ictalurus furcatus）", prem=[
   "mixed_diet = 无脊椎/贝/鱼（S1——取向注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "deep_channel_pool_base（深潭主河道底板——S8 MSF）"),
          slot("low_light_night_slot（低光/夜相槽——S7 MSF 夜间摄食 story 原文+CSV 夜间活跃）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 深潭主河道（S8）+夜间摄食（S7）——底板先行夜槽次之",
          "C: Ictalurus furcatus demersal 0-50m / 夜间活跃 / 3.41", "B: 无表达文件"],
  evid=[B6S.format(c="BCF"), CSV + "#BCF", B6B.format(c="BCF"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0095"],
  open=[]),
 dict(code="BHM", sp="牛头鲦 Bullhead Minnow（Pimephales vigilax）", prem=[],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "insect_larvae_field（虫幼猎物场——'They feed on insect immatures' 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "quiet_pool_sand_mud_band（静潭沙泥带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 食性主句先行（虫幼单类）+S8 静潭沙泥——开放水跟随型读法（小型鲤科非结构特化绑定）",
          "C: Pimephales vigilax demersal / 早晨活跃 / 躲藏", "B: 无表达文件"],
  evid=[B6S.format(c="BHM"), CSV + "#BHM", B6B.format(c="BHM"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0096"],
  open=[]),
 dict(code="BLT", sp="黑口红点鲑 Bull Trout（Salvelinus confluentus）", prem=[
   "potamodromous = 河湖洄游（S5 premise）",
   "vu = V 保护（供给边界注记）",
   "name_misalign = 中文名错位注记（库锚学名 Salvelinus confluentus 从）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "cold_deep_pool_band（深潭冷水带——'深潭冷水/高山区雪河' S8 栖息主句单因子）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(食性未详)——forage 轴不立；S8 深潭冷水栖息主句——证据分辨率=单因子",
          "C: Salvelinus confluentus benthopelagic / 晨昏活跃 / 3.72", "B: 无表达文件"],
  evid=[B6S.format(c="BLT"), CSV + "#BLT", B6B.format(c="BLT"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0097"],
  open=["食性补证后可能升两步链"]),
 dict(code="BMB", sp="大鳞鲃 Bulatmai Barbel（Luciobarbus capito）", prem=[
   "semi_anadromous = 海+河口+河流半溯河域切换（P05 premise——S5/S8 廊道域为 premise 域）",
   "sand_gravel_spawning = 沙砂强流产卵（S6 premise）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "omnivore_benthic_field（广食场——无脊椎/藻/腐屑/小鱼 S1 食性主句）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '无脊椎/藻/腐屑/小鱼'食性主句；S8 海/河口/河=廊道域切换（premise 域不立链步）——单因子",
          "C: Luciobarbus capito benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="BMB"), CSV + "#BMB", B6B.format(c="BMB"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0098"],
  open=["非洄游态栖息复合句补证后可能升两步链"]),
 dict(code="BTS", sp="迷人真小鲤 Blacktail Shiner（Cyprinella venusta）", prem=[
   "surface_presentation = 水面呈现（S7——呈现面注记）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "surface_insect_field（水面昆虫猎物场——'Adults feed on surface insects' 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "sand_pool_band（沙潭带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 水面昆虫食性主句（表层取向）先行+S8 沙潭次之——跟随型读法",
          "C: Cyprinella venusta benthopelagic / 早晨活跃", "B: 无表达文件"],
  evid=[B6S.format(c="BTS"), CSV + "#BTS", B6B.format(c="BTS"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0099"],
  open=[]),
 dict(code="CGD", sp="常见鮈鱼 Common Gudgeon（Gobio gobio）", prem=[
   "schooling = 沙底急流群游（S3——群结构事实并入分档槽值域，非独立程序步）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "sand_riffle_band（沙底急流复合带——S8 流速+底质复合栖息句先行）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_invert_field（虫/贝/甲壳底栖猎物场次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '沙底急流'复合栖息句（流速+底质两要素）+鮈类底栖特化绑定——复合带先行；S1 虫/贝/甲壳次之",
          "C: Gobio gobio benthopelagic / potamodromous / 3.13", "B: 无表达文件"],
  evid=[B6S.format(c="CGD"), CSV + "#CGD", B6B.format(c="CGD"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0100"],
  open=[]),
 dict(code="DBC", sp="江黄颡 Darkbarbel Catfish（Tachysurus vachellii）", prem=[
   "congeneric_inference = 黄颡鱼 R03 同属推算（S1/S8 均 EO——食性栖息未详，同属替代证据）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "bottom_band（底层带——同属鲿形目底栖构型+CSV demersal 推算锚）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(同属推算)+S8 EO(栖息未述)——分辨率=同属构型单因子（forage 轴不立）",
          "C: Tachysurus vachellii demersal / 全天活跃 / 孤僻", "B: 无表达文件"],
  evid=[B6S.format(c="DBC"), CSV + "#DBC", B6B.format(c="DBC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0101"],
  open=["黄颡鱼 R03 同属轨补证后升档（食性/栖息细节）"]),
 dict(code="DCL", sp="湘华鮈 Decoris Labeo（Hemibarbus sp.）", prem=[
   "congeneric_inference = 同唇䱌系同属推算（底栖刮食型——FishBase 公开版无页，同属替代）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "river_benthic_band（同属河川底栖带——S8 同属推算锚单因子）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(薄资料同属推算)——forage 轴不立；S8 MSF(同属河川底栖)——单因子",
          "C: 无 CSV 行（薄资料）——同属参照 Hemibarbus labeo", "B: 无表达文件"],
  evid=[B6S.format(c="DCL"), B6B.format(c="DCL"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0102"],
  open=["同属（唇䱌系）轨补证后升档——刮食取向若证实可立 forage 步"]),
 dict(code="EUP", sp="赤梢鱼 European Perch（Perca fluviatilis）", prem=[
   "crepuscular_peaks = 日升日落捕食峰（S4 时段窗 condition premise——非空间分支）",
   "egg_ribbon_spawn = 卵带产 1m 白带（S6 premise）",
   "size_threshold_piscivory = 成体 12cm 起鱼食（S9 发育阈值 premise）",
   "name_misalign = 中文名赤梢鱼与学名错位注记（库锚 Perca fluviatilis 从）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "opportunistic_fish_fauna_field（昼间机会食场——'opportunistic diurnal feeder' 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "lake_pool_band（湖潭带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'opportunistic diurnal feeder which preys mainly during sunrise and sunset' 食性主句先行；S8 湖潭单要素次之——机会跟随型读法（晨昏峰=premise）",
          "C: Perca fluviatilis demersal 1-30m / 晨昏活跃 / 4.35", "B: 无表达文件"],
  evid=[B6S.format(c="EUP"), CSV + "#EUP", B6B.format(c="EUP"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0103"],
  open=[]),
 dict(code="GDB", sp="广东鲂 Guangdong Bream（Megalobrama terminalis）", prem=[
   "congeneric_inference = 团头鲂 R05 同属第 2 例推算（S1 EO 食性同属推算 3.3）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "river_band（河川带——S8 MSF 单因子）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(同属推算)+S8 MSF(河川)——单因子分辨率",
          "C: Megalobrama terminalis benthopelagic / 早晨活跃 / 躲藏", "B: 无表达文件"],
  evid=[B6S.format(c="GDB"), CSV + "#GDB", B6B.format(c="GDB"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0104"],
  open=["食性补证后可能升两步链"]),
 dict(code="GDS", sp="金体美鱥 Golden Shiner（Notemigonus crysoleucas）", prem=[
   "hypoxia_tolerance = 低氧耐热（生理容忍注记——能力变量非空间分支）",
   "baitfish = 钓饵鱼供给角色（S10 注记非 gamefish）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "plankton_invert_omnivore_field（浮游/虫/贝杂食场——S1 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "vegetated_lake_pool_band（植被湖潭带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: '浮游/虫/贝杂食'食性主句先行+S8 植被湖潭次之——杂食跟随型读法（非结构特化绑定）",
          "C: Notemigonus crysoleucas demersal / 早晨活跃 / 杂食 variable / 2.65", "B: 无表达文件"],
  evid=[B6S.format(c="GDS"), CSV + "#GDS", B6B.format(c="GDS"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0105"],
  open=[]),
 dict(code="JSB", sp="海鲈 Japanese Seabass（Lateolabrax maculatus，同属 japonicus 参照）", prem=[
   "congeneric_reference = maculatus 专项数据薄——同属 japonicus 参照（历史同物异名现均有效）",
   "catadromous_ref = 同属降海洄游参照（ASB 同种对——批内去重联动）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "fish_shrimp_piscivore_field（鱼虾猎物场——同属参照'杂食性掠食'食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "inshore_reef_band（同属近岸岩礁带——S8 同属参照次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 同属 japonicus 参照（数据薄）——食性主句先行+S8 同属近岸岩礁次之（与 ASB 同种同 URL 去重联动——真形同体，本行独立记账）",
          "C: Lateolabrax maculatus 晨昏活跃（字段薄——同种 ASB 行补位）", "B: 无表达文件"],
  evid=[B6S.format(c="JSB"), CSV + "#JSB", B6B.format(c="JSB"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0106"],
  open=["maculatus 专项数据补证后独立复核（当前=同种同体推导）"]),
 dict(code="LFB", sp="大鳍𫚪 Largefin Bitterling（Acheilognathus macropterus）", prem=[
   "mussel_brood = 贝内产卵+幼贝内发育（P04 贝宿主关系——guard 面 premise 注记，Bake 分布面不重复结算）",
   "ovipositor = 产卵管形态（注记）",
   "diet_inferred = trophic 2.0 低营养杂食（S1 EO 推算——forage 轴不立）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "river_lake_soft_band（河湖带——S8 MSF 单因子）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(食性 2.0 推算)——forage 轴不立；S8 MSF(河湖)——单因子分辨率",
          "C: Acheilognathus macropterus benthopelagic / 全天活跃 / 躲藏", "B: 无表达文件"],
  evid=[B6S.format(c="LFB"), CSV + "#LFB", B6B.format(c="LFB"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0107"],
  open=["贝宿主关系（guard 面）不在本 Bake 真形范围——guard 轨另载"]),
 dict(code="PCC", sp="细纹鲶鱼 Pencil Catfish（Trichomycterus striatus）", prem=[
   "thin_data = V3 资料薄（注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "trichomycterid_benthic_band（同科底栖带——S8 同科推算锚单因子）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(食性无述)+S8 MSF(同科底栖)——单因子分辨率",
          "C: Trichomycterus striatus 晨昏活跃（字段薄）/ 孤僻", "B: 无表达文件"],
  evid=[B6S.format(c="PCC"), CSV + "#PCC", B6B.format(c="PCC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0108"],
  open=["食性补证后可能升两步链"]),
 dict(code="PKC", sp="茅尖鱼 Pike Cichlid（Crenicichla lepidota）", prem=[
   "piscivorph_inferred = 慈鲷掠食型 trophic 3.6（S1 EO 推算——forage 轴不立）",
   "ornamental = 观赏非 gamefish（注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "tropical_river_band（热带河带——S8 MSF 单因子）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: S1 EO(掠食型推算)——forage 轴不立；S8 MSF(热带河)——单因子分辨率",
          "C: Crenicichla lepidota 20-28°C / 全天活跃 / 活泼（字段薄）", "B: 无表达文件"],
  evid=[B6S.format(c="PKC"), CSV + "#PKC", B6B.format(c="PKC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0109"],
  open=["掠食取向补证后可立 forage 步"]),
 dict(code="PKS", sp="驼背太阳鱼 Pumpkinseed（Lepomis gibbosus）", prem=[
   "sunfish_7th = 太阳鱼系第 7 例（同构注记）",
   "introduced_pest = 引入 pest（供给注记）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "small_fish_invert_field（小鱼/无脊椎猎物场——S1 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "vegetated_slackwater_band（植被静水带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'Feeds on small fishes and other vertebrates'+无脊椎 食性主句先行+S8 植被静水次之——跟随型读法",
          "C: Lepomis gibbosus benthopelagic 0-41m / 晨昏活跃 / 3.25 / 好斗", "B: 无表达文件"],
  evid=[B6S.format(c="PKS"), CSV + "#PKS", B6B.format(c="PKS"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0110"],
  open=[]),
 dict(code="PLC", sp="宽鳍𫚭 Pale Chub（Zacco platypus）", prem=[
   "zacco_congener = 马口鱼系同构（注记）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "drift_omnivore_field（漂食杂食场——浮游/甲壳/藻/小鱼/腐屑 S1 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "riffle_run_band（急流带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'zooplankton, small crustaceans, macroscopic algae, small fish and detritus' 食性主句（五类广谱）先行+S8 急流次之",
          "C: Zacco platypus benthopelagic / 早晨活跃 / 杂食 variable / 3.05", "B: 无表达文件"],
  evid=[B6S.format(c="PLC"), CSV + "#PLC", B6B.format(c="PLC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0111"],
  open=[]),
 dict(code="PRB", sp="短扁口鲶 Piraiba（Brachyplatystoma filamentosum）", prem=[
   "potamodromous = 河湖洄游（S5 premise）",
   "apex_giant = 巨型顶级掠食 360cm/200kg（体型注记）",
   "extreme_prey_note = 猴/人胃含物记录（极端猎物注记——取向不立步）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "piscivore_large_prey_field（鱼食猎物场——'Feeds on fish' 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "estuary_channel_band（河口咸淡水带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'Feeds on fish'+猴/人记录 食性主句先行+S8 河口咸淡水次之——巨型鲶跟随型读法",
          "C: Brachyplatystoma filamentosum 22-28°C / 早晨活跃 / 活泼（字段薄）", "B: 无表达文件"],
  evid=[B6S.format(c="PRB"), CSV + "#PRB", B6B.format(c="PRB"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0112"],
  open=[]),
 dict(code="PSH", sp="大青鲨误名 Paroon Shark（Pangasius sanitwongsei）", prem=[
   "potamodromous = 洄游（S5 premise）",
   "cr = CR 保护边界（S11 注记）",
   "size_graded = 幼-成体型分级（S9 premise）",
   "name_misalign = 中文名大青鲨错位（Paroon Shark 非鲨——名实分离注记非 Identity Deferred）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "fish_crustacean_field（鱼/甲壳猎物场——'Both young and adults feed on fishes and crustaceans' 食性主句先行；大型个体食殍=取向注记）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "large_river_channel_band（大河带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 鱼/甲壳食性主句先行+S8 大河次之——巨型鲑鲶跟随型读法",
          "C: Pangasius sanitwongsei benthopelagic / 20-32°C / 追猎 / 3.99", "B: 无表达文件"],
  evid=[B6S.format(c="PSH"), CSV + "#PSH", B6B.format(c="PSH"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0113"],
  open=[]),
 dict(code="RBD", sp="彩虹镖鲈 Rainbow Darter（Etheostoma caeruleum）", prem=[
   "egg_burying = 产卵埋入底质（S6 premise）",
   "darter_microbenthic = 镖鲈科微底栖首例（体构绑定注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "fast_riffle_gravel_rubble_band（急流砾石石块复合带——'fast gravel and rubble riffles' 流速+底质复合栖息句先行）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_insect_larvae_field（水生虫幼+鱼卵猎物场次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'fast gravel and rubble riffles' 复合栖息句（流速+底质两要素）+镖鲈微底栖特化绑定——复合带先行；S1 虫幼+鱼卵次之",
          "C: Etheostoma caeruleum benthopelagic / 晨昏活跃 / 3.3 / 孤僻", "B: 无表达文件"],
  evid=[B6S.format(c="RBD"), CSV + "#RBD", B6B.format(c="RBD"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0114"],
  open=[]),
 dict(code="RSC", sp="黑棘鲶 Ripsaw Catfish（Oxydoras niger）", prem=[
   "schooling = 泥底群游（S3——群结构事实并入分档槽值域）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "detritus_chironomid_field（腐屑/摇蚊/蜉蝣幼/甲壳场——S1 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "mud_bottom_band（泥底带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 腐屑/摇蚊/蜉蝣幼/甲壳食性主句先行+S8 泥底次之——群游底栖跟随型读法",
          "C: Oxydoras niger 18-30°C / 晨昏活跃 / 孤僻（字段薄）", "B: 无表达文件"],
  evid=[B6S.format(c="RSC"), CSV + "#RSC", B6B.format(c="RSC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0115"],
  open=[]),
 dict(code="RSS", sp="红斑太阳鱼 Redspotted Sunfish（Lepomis miniatus）", prem=[
   "sunfish_6th = 太阳鱼系第 6 例（同构注记）"],
  steps=[gate("GATE_ZONE", "bottom_layer_zone（底层水层带——demersal CSV 硬定位+'Consumes benthic prey' 底栖绑定）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_invert_field（底栖无脊椎猎物场——'Invertebrate feeder. Consumes benthic prey'）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'Invertebrate feeder. Consumes benthic prey'——底栖猎物绑定；底层硬定位先行（demersal 锚），底栖猎物场次之",
          "C: Lepomis miniatus demersal / 晨昏活跃 / 躲藏",
          "同形对照：demersal+底栖食场两步形（INC/WST 同型）", "B: 无表达文件"],
  evid=[B6S.format(c="RSS"), CSV + "#RSS", B6B.format(c="RSS"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0116"],
  open=[]),
 dict(code="RUF", sp="梅花鲈 Ruffe（Gymnocephalus cernua）", prem=[
   "invasive = 入侵种（供给注记）",
   "coastal_fish_diet = 沿海鱼食（S9——发育取向注记）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "zooplankton_chironomid_field（浮游/摇蚊/寡毛/钩虾场——S1 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "eutrophic_lake_estuary_band（富营湖/河口带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'feeds on zooplankton, chironomids, oligochaetes and amphipods' 食性主句先行+S8 富营湖/河口次之——富营底栖跟随型读法",
          "C: Gymnocephalus cernua benthopelagic 2-85m / 晨昏活跃 / 杂食 variable / 3.26", "B: 无表达文件"],
  evid=[B6S.format(c="RUF"), CSV + "#RUF", B6B.format(c="RUF"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0117"],
  open=[]),
 dict(code="SLM", sp="银斑鲫 Silver Mylossoma（Mylossoma duriventre）", prem=[
   "commercial = 商业+游钓（供给注记）",
   "serrasalmid_herbivore_3rd = Serrasalmid 植食第 3 例（同构注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "floodplain_lake_band（洪泛湖带——S8 栖息句先行）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "floodplain_herbivore_field（洪泛草食场——herbivore highly dependent on floodplains 食性主句与洪泛绑定）"),
          slot("flood_pulse_slot（洪泛脉冲槽——S4 洪泛依赖位相槽）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'herbivore highly dependent on floodplains'+S4 MSF(洪泛依赖)+S8 MSF(洪泛湖)——洪泛湖栖息先行、洪泛草食场次之、洪泛位相槽殿后（草食-洪泛双绑定程序）",
          "C: Mylossoma duriventre 22-28°C / 早晨活跃 / 躲藏（字段薄）", "B: 无表达文件"],
  evid=[B6S.format(c="SLM"), CSV + "#SLM", B6B.format(c="SLM"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0118"],
  open=["同批 BAS 形（栖息→草食→洪泛槽尾）对照——判同段处理"]),
 dict(code="SSM", sp="巴西马鲛 Serra Spanish Mackerel（Scomberomorus brasiliensis）", prem=[
   "oceanodromous = 礁相关洄游（S5 premise）",
   "mackerel_3rd = 马鲛系第 3 例（同构注记）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "fish_shrimp_squid_field（鱼/虾/鱿猎物场——'Feeds largely on fishes...' 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "reef_migratory_band（礁相关洄游带——S8 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'Feeds largely on fishes, with smaller quantities of penaeid shrimps and loliginid cephalopods' 食性主句先行+S8 礁相关洄游带次之",
          "C: Scomberomorus brasiliensis reef-associated / oceanodromous / 追猎 / 3.31", "B: 无表达文件"],
  evid=[B6S.format(c="SSM"), CSV + "#SSM", B6B.format(c="SSM"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0119"],
  open=[]),
 dict(code="STS", sp="花鮨 Swallowtail Seaperch（Anthias anthias）", prem=[
   "grouper_name_note = V3 英文名 Grouper 泛指错位注记（花鮨科）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "deep_reef_base（深礁底板带 30-358m——S8 深礁栖息主句先行）"),
          slot("low_light_night_slot（低光/夜相槽——S7 MSF 夜行 story 原文）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 夜行（S7 MSF）+深礁 30-358m（S8 MSF）——深礁底板先行夜槽次之",
          "C: Anthias anthias reef-associated 30-358m / 3.75 / 追猎", "B: 无表达文件"],
  evid=[B6S.format(c="STS"), CSV + "#STS", B6B.format(c="STS"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0120"],
  open=[]),
 dict(code="TGS", sp="虎纹鸭嘴鲇 Tiger Sorubim（Pseudoplatystoma fasciatum）", prem=[
   "night_feeding = 夜间摄食鱼+蟹（S1——时段与食性主句）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "floodplain_channel_base（洪泛林主河道底板——S8 主河道+S4 洪泛林栖息句先行）"),
          slot("low_light_night_slot（低光/夜相槽——S7 MSF 夜行 story 原文+CSV 夜间活跃）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 夜鱼食+蟹（S1）+洪泛林（S4）+主河道（S8）+夜行（S7）——洪泛主河道底板先行夜槽次之（夜摄食=夜槽承载）",
          "C: Pseudoplatystoma fasciatum demersal / 夜间活跃 / 4.38 / 追猎", "B: 无表达文件"],
  evid=[B6S.format(c="TGS"), CSV + "#TGS", B6B.format(c="TGS"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0121"],
  open=[]),
 dict(code="WHC", sp="白鲶鱼 White Catfish（Ameiurus catus）", prem=[
   "mixed_diet = 鱼/虫/甲壳广食（S1——取向注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "mud_pool_base（泥底潭沼底板——S8 MSF）"),
          slot("low_light_night_slot（低光/夜相槽——CSV 夜间活跃锚；story 无 S7 原文——夜行证据分层注记）")],
  ret="SpatialDistributionWeight",
  basis=["A-R10: 'wide variety of fishes, insects and crustaceans'+S8 泥底潭沼——底板先行；夜槽依 CSV 夜间活跃锚（MOO 同型 CSV 级证据）",
          "C: Ameiurus catus demersal / 夜间活跃 / potamodromous / 3.18",
          "同科对照：BBH/BCF 鲿科夜行底栖真形同构", "B: 无表达文件"],
  evid=[B6S.format(c="WHC"), CSV + "#WHC", B6B.format(c="WHC"), "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0122"],
  open=[]),
]

# ===== RS1 47（链族在册 order_provisional 成员）=====
EXP = {
 "COD": "migration/species/atlantic_cod.md", "PIK19": "migration/species/northern_pike_spawn.md",
 "ARC": "migration/species/arctic_char.md", "VEN": "migration/species/vendace.md",
 "SWO": "migration/species/swordfish_diel.md", "CHN": "migration/species/chinook_salmon.md",
 "COH": "migration/species/coho_salmon.md", "BRO": "migration/species/brook_trout.md",
 "ALE": "migration/species/alewife.md", "TAR": "migration/species/atlantic_tarpon.md",
 "BRT12": "normal/species/brown_trout.md", "PB": "normal2/species/orinoco_peacock.md",
 "PAD34": "normal/species/paddlefish_electro.md", "CHU": "migration/species/chum_salmon.md",
 "SHA": "migration/species/american_shad.md", "FGA": "normal/species/florida_gar.md",
 "SGA": "normal/species/spotted_gar.md", "AST": "normal2/species/atlantic_sturgeon.md",
 "SNS": "normal2/species/shortnose_sturgeon.md", "GRB": "patch/species/grass_carp.md",
 "SMA": "patch/species/smallmouth_follow.md", "WEL": "normal2/species/wels_catfish_feeding.md",
 "FLA": "normal2/species/flathead_catfish.md", "BUR": "normal2/species/burbot.md",
 "DRU": "patch/species/black_drum.md", "BHC": "field/species/bighead_carp.md",
 "HER": "field/species/atlantic_herring.md", "BLU": "guarding/species/bluegill.md",
 "ARA": "guarding/species/arapaima.md", "RBP": "guarding/species/red_bellied_piranha.md",
}

F += [
 dict(code="COD", sp="大西洋鳕 Atlantic Cod（Gadus morhua）", src="B1", prem=[
   "sex = 个体性别 fact（上游；产品是否区分性别供给未定）",
   "spawning_stage = 繁殖期状态（上游 lifecycle）",
   "unverified_spawning_dive = 未确认产卵潜水（Story 原文证据分级标注——不建体）"],
  steps=[ev("EVAL_TYPED_DEPTH_FACTOR", "sex_stage_bound_depth_band（性别阶段绑定深度带——繁殖期雄/雌/未繁殖深度段随 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B1: '繁殖期性别相关水深：深度因子评估（绑定随 sex/stage premise 切换）'——深度带单因子（Tier C 冻结 sketch 语义）",
          "C: benthopelagic 0-600m / 0-15°C / oceanodromous——栖息带与深度带同维度（垂直），不另立独立水层步（双计防护）",
          "B §0: 单步链（premise 读取→深度带三档→归一化）——与本推导一致"],
  evid=[B12B.format(b="CENSUS-B1", b2="B1", c="COD"), B12S.format(b="CENSUS-B1", b2="B1", c="COD"),
        "outputs/full_authoring/" + EXP["COD"], CSV + "#COD", RS1B.format(c="COD"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0249"],
  open=["档位成员与阈值全 Profile 值域不冻结 [需正文]"]),
 dict(code="PIK19", sp="白斑狗鱼 Northern Pike（Esox lucius）", src="B2", prem=[
   "spawning_stage = PRE | POST（上游 lifecycle premise）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "spawning_stage_bound_axis_segment（淹水草地浅滩↔深水结构带轴段——产卵期进浅水支流/淹水草地散卵，产后返较深水）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '位置/深度因子随繁殖阶段 premise 配置切换'——轴段单因子；轴本身横跨浅↔深（垂直跨度内建于轴）",
          "C: pelagic 0-30m / potamodromous——栖息带锚与轴段同域不另立步", "B §0: 单步链一致"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="PIK19"), B12S.format(b="CENSUS-B2", b2="B2", c="PIK19"),
        "outputs/full_authoring/" + EXP["PIK19"], CSV + "#PIK19", RS1B.format(c="PIK19"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0250"],
  open=[]),
 dict(code="ARC", sp="北极红点鲑 Arctic Char（Salvelinus alpinus）", src="B2", prem=[
   "season_temperature = 季节/温度（上游 condition premise）",
   "polymorphic_stock = 洄游/湖居种群差异（值域承载不并 Mode）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "season_bound_shore_deep_axis（暖季近岸带↔冷水季深水带轴段——temp/season premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '近岸/深水位置利用随季节与温度切换'——单轴段因子（位置轴内建深浅跨度）",
          "C: benthopelagic 0-70m / anadromous / 4-16°C——轴段同域", "B §0: 单步链一致（'CSV benthopelagic 锚未入链——冻结单因子形优先'）"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="ARC"), B12S.format(b="CENSUS-B2", b2="B2", c="ARC"),
        "outputs/full_authoring/" + EXP["ARC"], CSV + "#ARC", RS1B.format(c="ARC"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0251"],
  open=[]),
 dict(code="VEN", sp="欧白鲑 Vendace（Coregonus albula）", src="B2", prem=[
   "water_temperature_season = 水温/季节（上游 condition premise）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "season_bound_vertical_layer_axis（冷水期底层↔暖季水层垂直轴段——temp/season premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '水层利用随水温与季节改变：水层因子随温度/季节绑定切换'——垂直水层轴单因子（轴=垂直维本身）",
          "C: benthopelagic 30m+ / 1.6-3.6°C / 滤食性——垂直维与轴同域不另立步", "B §0: 单步链一致"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="VEN"), B12S.format(b="CENSUS-B2", b2="B2", c="VEN"),
        "outputs/full_authoring/" + EXP["VEN"], CSV + "#VEN", RS1B.format(c="VEN"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0252"],
  open=[]),
 dict(code="SWO", sp="剑旗鱼 Swordfish（Xiphias gladius）", src="B2", prem=[
   "diel_phase = DAY | NIGHT（昼夜相位，上游 condition premise）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "diel_bound_dvm_layer_axis（夜间表层↔昼间深层 DVM 轴段——diel premise 取段；tolerated 档=垂直迁移过渡带独有语义）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '昼夜垂直迁移：水层因子随昼夜相位绑定切换（白天较深水层、夜间近表层）'——DVM 垂直轴单因子",
          "C: pelagic-oceanic 0-2878m / oceanodromous——垂直维内建于轴", "B §0: 单步链一致（tolerated 过渡带语义保留）"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="SWO"), B12S.format(b="CENSUS-B2", b2="B2", c="SWO"),
        "outputs/full_authoring/" + EXP["SWO"], CSV + "#SWO", RS1B.format(c="SWO"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0253"],
  open=["2D 定向判据（coverage #24）留 representation 线"]),
 dict(code="CHN", sp="帝王鲑 Chinook Salmon（Oncorhynchus tshawytscha）", src="B3", prem=[
   "life_stage = OCEAN | MIGRATION | SPAWN（域切换配置级 premise）",
   "life_history_polymorphism = ocean-type/stream-type/jack 型（阶段差异落 Profile 值域）",
   "semelparous = 产后死亡（生活史 premise）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "near_bottom_soft_layer（近底水层软定位——CSV benthopelagic 锚，与水平洄游廊道为独立维度）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "stage_bound_corridor_axis（海洋觅食区↔河口↔深河产卵段轴段——4827km 溯河 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 海期'primarily other fish when older'+4827km 溯河——水平廊道轴段为主体；垂直近底定位为独立第二维（CSV benthopelagic 锚）先于廊道（水柱内定位先于沿廊道分档）",
          "C: benthopelagic 0-375m / anadromous / 晨昏活跃",
          "B §0: 单步链='G2/C12 样板语义方向级还原（Tier B 无行级证据）'——样板约定序不采；真形按 A+C 两维推导",
          "同构对照：CHU 同批真形（近底软定位→廊道轴段两步）——同证据层同推导"],
  evid=[B3S.format(c="CHN"), "outputs/full_authoring/" + EXP["CHN"], CSV + "#CHN", RS1B.format(c="CHN"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0254"],
  open=["档位成员 [需正文]"]),
 dict(code="COH", sp="银鲑 Coho Salmon（Oncorhynchus kisutch）", src="B3", prem=[
   "life_stage = OCEAN | MIGRATION | SPAWN（域切换配置级 premise）",
   "prey_escalation = 浮游→水母/鱿/鱼猎物升级（S1 发育取向——forage 值域承载）",
   "semelparous = 产后死亡（生活史 premise）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "midupper_pelagic_layer（中上层软定位——CSV pelagic-neritic 锚）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "stage_bound_corridor_axis（海洋↔河口↔产卵支流轴段——夜行降海/溯河 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 淡水昆虫→入海浮游甲壳→后期水母/鱿/鱼猎物升级+S5 洄游——廊道轴段为主体；中上层垂直定位独立维（CSV pelagic-neritic）先行",
          "C: pelagic-neritic 0-250m / anadromous / 晨昏活跃",
          "B §0: 单步链=样板语义方向级还原——约定序不采；SHA 同批真形同构（中上层→廊道）"],
  evid=[B3S.format(c="COH"), "outputs/full_authoring/" + EXP["COH"], CSV + "#COH", RS1B.format(c="COH"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0255"],
  open=[]),
 dict(code="BRO", sp="美洲红点鲑 Brook Trout（Salvelinus fontinalis）", src="B3", prem=[
   "life_stage = RIVER | ESTUARY | OCEAN（salter 型季节降海↔回河配置级 premise；湖封种群落值域）",
   "redd_guard_note = 雌鱼挖巢+雄鱼驱敌（S6——guard 面另载注记）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "near_bottom_soft_layer（近底水层软定位——CSV benthopelagic 锚）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "stage_bound_corridor_axis（海洋沿岸肥育带↔河口↔河段轴段——salter 春温升入海 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 'Anadromous in some populations'——salter 型 run to the sea in the spring as stream temperature rises——廊道轴段主体；近底垂直定位独立维（CSV benthopelagic）先行",
          "C: benthopelagic 15-27m / anadromous / 晨昏活跃",
          "B §0: 单步链=样板语义方向级还原（同属先例读法）——约定序不采"],
  evid=[B3S.format(c="BRO"), "outputs/full_authoring/" + EXP["BRO"], CSV + "#BRO", RS1B.format(c="BRO"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0256"],
  open=[]),
 dict(code="ALE", sp="灰西鲱 Alewife（Alosa pseudoharengus）", src="B3", prem=[
   "life_stage = OCEAN | MIGRATION | SPAWN（域切换配置级 premise——陆封/溯河双型落值域）",
   "night_spawning = 夜产卵+≥27.8°C 停止（S4/S6 繁殖 premise）",
   "gill_raker_ontogeny = 鳃耙随龄增长（S9 注记）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "midupper_pelagic_layer（中上层软定位——CSV pelagic-neritic 锚）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "stage_bound_corridor_axis（海洋觅食区↔河口↔产卵河段轴段——anadromous/landlocked 双型 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 'Individuals with access to ocean are anadromous'与 landlocked 双型+'Adults feed on shrimps and small fishes'——廊道轴段主体；中上层垂直定位独立维先行（CSV pelagic-neritic）",
          "C: pelagic-neritic 5-145m / anadromous",
          "B §0: 单步链=样板语义方向级还原——约定序不采；同属停食判例不默认继承（story 无停食原文）"],
  evid=[B3S.format(c="ALE"), "outputs/full_authoring/" + EXP["ALE"], CSV + "#ALE", RS1B.format(c="ALE"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0257"],
  open=[]),
 dict(code="TAR", sp="大西洋大海鲢 Atlantic Tarpon（Megalops atlanticus）", src="B3", prem=[
   "developmental_stage = LARVA | JUVENILE_RIVER | SUBADULT_SEA | ADULT_COASTAL（amphidromous 发育枚举配置级 premise）",
   "obligate_air_breathing = 专性气呼吸（runtime persistent 条件——肺鱼先例不买 Mode）",
   "leaping_post_hook = 跳跃搏鱼（后钩阶段非 FCF 前链注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "developmental_stage_bound_axis（沿岸礁带↔河口↔河沼幼体带发育轴段——leptocephalus 幼体入河口 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: amphidromous 发育轴（leptocephalus 幼体入河口）+沿岸礁带/河口/湾区——发育轴段单因子；CSV reef-associated 锚由轴段'沿岸礁带'承载不另立独立步（栖息带=轴段的海侧取值）",
          "C: reef-associated 0-40m / amphidromous", "B §0: 单步链一致（'CSV reef-associated 锚未入链——样板链优先'，本推导给出不另立步的证据理由=轴段承载）"],
  evid=[B3S.format(c="TAR"), "outputs/full_authoring/" + EXP["TAR"], CSV + "#TAR", RS1B.format(c="TAR"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0258"],
  open=[]),
 dict(code="BRT12", sp="褐鳟 Brown Trout（Salmo trutta）", src="B2", prem=[
   "prey_pulse = 季节猎物脉冲事件（如蜉蝣羽化——世界侧 fact premise）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "seasonal_pulse_prey_patch（季节脉冲猎物 patch——机会场食物丰度档，'普通摄食与季节猎物脉冲'食性主句先行）"),
          ev("EVAL_TYPED_LAYER_FACTOR", "midupper_soft_layer（中上层软定位——CSV pelagic-neritic 锚次之；结构安全/水流次级因子无 Story 证据不立）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '季节猎物脉冲：猎物资源 patch 强度随季节脉冲波动（ResourcePatch 描述——Story Competing 明言）'——机会型食物丰度先行",
          "C: pelagic-neritic 0-28m / anadromous / 晨昏活跃",
          "B §0: 单步链（机会场食物丰度档位）——B 层未含 CSV 层定位步；真形按 A+C 双证据立两步（猎物场先行、水层次之）"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="BRT12"), B12S.format(b="CENSUS-B2", b2="B2", c="BRT12"),
        "outputs/full_authoring/" + EXP["BRT12"], CSV + "#BRT12", RS1B.format(c="BRT12"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0259"],
  open=[]),
 dict(code="PB", sp="奥里诺科孔雀鲈 Orinoco Peacock Bass（Cichla orinocensis）", src="B3", prem=[
   "gamefish = 游钓（供给注记）",
   "breeding_eo = 繁殖面 FishBase 无描述（EO——Cichla 属双亲护巢常识未核验不写）"],
  steps=[ev("EVAL_TYPED_FORAGE_FACTOR", "characiform_pursuit_field（小型 characiform 鱼追猎场——'Feeds mainly on small characiform fish' 食性主句先行）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "shallow_lagoon_slow_reach_band（浅水近岸渊湾/缓流带——'shallow near-shore areas of lagoons and slow moving reaches' 次之）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 'Feeds mainly on small characiform fish' 食性主句先行+S8 浅渊湾/缓流栖息句次之——追猎跟随型读法",
          "C: benthopelagic / 27-29°C / 好斗 / 4.48", "B §0: 单步链（机会场）——B 层未入栖息句；真形按 A 双句立两步"],
  evid=[B3S.format(c="PB"), "outputs/full_authoring/" + EXP["PB"], CSV + "#PB", RS1B.format(c="PB"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0260"],
  open=[]),
 dict(code="PAD34", sp="鸭嘴鲟 Paddlefish（Polyodon spathula 幼体）", src="B1", prem=[
   "lifecycle_stage = JUVENILE（幼体阶段，上游 premise——Story 限定不能推广到成年）",
   "plankton_prey_field = 浮游猎物分布（上游 fact）"],
  steps=[ev("EVAL_TYPED_SENSOR_FIELD_FACTOR", "electroceptive_zooplankton_signal_field（浮游猎物电感受信号场——可探测=全额/弱信号=×衰减/无信号=软出局）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B1: '幼体分布跟随浮游猎物资源 patch'+电感受定位——感官信号场单因子（感官型第一判断=信号场可探测性先行）",
          "C: demersal 2m+ / 滤食性 filtering plankton——成体栖息带锚不适用于幼体限定轨", "B §0: 单步链一致"],
  evid=[B12B.format(b="CENSUS-B1", b2="B1", c="PAD34"), B12S.format(b="CENSUS-B1", b2="B1", c="PAD34"),
        "outputs/full_authoring/" + EXP["PAD34"], CSV + "#PAD34", RS1B.format(c="PAD34"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0261"],
  open=["成年滤食轨不在本 Story 限定内"]),
 dict(code="CHU", sp="大马哈鱼 Chum Salmon（Oncorhynchus keta）", src="B3", prem=[
   "life_stage = OCEAN | MIGRATION | SPAWN（域切换配置级 premise）",
   "fasting_freshwater_entry = 入淡水停食（'Adults cease feeding in freshwater'——停食触点=入淡水 premise）",
   "semelparous = 产后约一周死亡（生活史 premise）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "near_bottom_soft_layer（近底水层软定位——CSV benthopelagic 软锚，无硬门）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "stage_bound_corridor_axis（海洋觅食区↔河口↔产卵河段轴段——精准归巢 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 海洋期'feed mainly on copepods, tunicates and euphausiids'+溯河停食+归巢——廊道轴段主体；近底垂直定位独立维先行（CSV benthopelagic）",
          "C: benthopelagic 0-250m / anadromous / 晨昏活跃",
          "B §0: 两步链（premise→近底定位→轴段）——与本推导一致（B 层此处非样板约定=CSV 锚入链）"],
  evid=[B3S.format(c="CHU"), "outputs/full_authoring/" + EXP["CHU"], CSV + "#CHU", RS1B.format(c="CHU"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0262"],
  open=[]),
 dict(code="SHA", sp="美洲西鲱 American Shad（Alosa sapidissima）", src="B3", prem=[
   "life_stage = OCEAN | MIGRATION | SPAWN（域切换配置级 premise）",
   "fasting_whole_run = 溯河洄游全程停食（'Feeding ceases during upstream spawning migration'——停食触点=洄游全程 premise）"],
  steps=[ev("EVAL_TYPED_LAYER_FACTOR", "midupper_pelagic_layer（中上层软定位——CSV pelagic-neritic+细长鳃耙浮食构型）"),
          ev("EVAL_TYPED_HABITAT_FACTOR", "stage_bound_corridor_axis（海洋↔河口↔产卵河段轴段——630km 溯河 premise 取段）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 海期浮游食性+细长鳃耙（浮食构型）+630km 溯河停食——廊道轴段主体；中上层垂直定位独立维先行（CSV pelagic-neritic+鳃耙形态）",
          "C: pelagic-neritic 0-250m / anadromous / 3.48",
          "B §0: 两步链（premise→中上层定位→轴段）——与本推导一致"],
  evid=[B3S.format(c="SHA"), "outputs/full_authoring/" + EXP["SHA"], CSV + "#SHA", RS1B.format(c="SHA"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0263"],
  open=[]),
 dict(code="FGA", sp="佛罗里达雀鳝 Florida Gar（Lepisosteus platyrhincus）", src="B2", prem=[
   "shallow_season_window = 浅水季节水温活动窗口（活性 condition premise——非空间分支）"],
  steps=[gate("GATE_VEGETATION_EDGE", "vegetation_edge_cover_present（植被缘掩体存在——伏击型第一判断=结构掩体存在性）"),
          ev("EVAL_TYPED_STRUCTURE_FACTOR", "vegetation_edge_cover_quality（植被缘掩体结构档）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '浅水植被缓流结构伏击：植被/结构栖息因子（静态）'——伏击构型=掩体绑定（门先行：无掩体格不产生伏击分布）",
          "C: demersal / 17-27°C / 孤僻——底栖伏击锚", "B §0: 门→掩体档两步一致"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="FGA"), B12S.format(b="CENSUS-B2", b2="B2", c="FGA"),
        "outputs/full_authoring/" + EXP["FGA"], CSV + "#FGA", RS1B.format(c="FGA"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0264"],
  open=[]),
 dict(code="SGA", sp="斑点雀鳝 Spotted Gar（Lepisosteus oculatus）", src="B3", prem=[
   "facultative_air_breathing = 兼性气呼吸（runtime 条件 premise——鳄雀鳝 B01 同构不买 Mode）"],
  steps=[gate("GATE_WEEDY_SLACK", "weedy_slack_cover_present（缓流植被掩体存在——静水洄湾伏击构型）"),
          ev("EVAL_TYPED_STRUCTURE_FACTOR", "weedy_slack_cover_quality（缓流植被掩体结构档）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 'quiet, clear pools and backwaters of lowland creeks...swamps and sloughs'+'voracious predator'——静水洄湾伏击=掩体绑定门先行",
          "C: demersal 0m+ / 12-20°C / 孤僻", "B §0: 门→掩体档两步一致"],
  evid=[B3S.format(c="SGA"), "outputs/full_authoring/" + EXP["SGA"], CSV + "#SGA", RS1B.format(c="SGA"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0265"],
  open=[]),
 dict(code="AST", sp="尖吻鲟 Atlantic Sturgeon（Acipenser oxyrinchus）", src="B3", prem=[
   "anadromous = 溯河洄游（域切换 P05 premise——春季上溯产卵）",
   "female_spawn_interval = 雌鱼 3-5 年产卵一次（生活史 premise）",
   "vu_cites = VU/CITES II（保护边界注记）"],
  steps=[gate("GATE_ZONE", "estuary_bottom_zone（河口河底底层水层带——溯河鲟底栖触须特化硬定位）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_probing_field（底栖探食场——'feeding on crustaceans, worms, and molluscs' 口侧 4 须触探）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 底栖无脊椎食性+口侧 4 须+S5 溯河——底层硬定位先行（触须底探特化），底栖探食场次之",
          "C: demersal 1-46m / anadromous / 晨昏活跃",
          "同形对照：WST 鲟形目真形（底层硬门→分级食场）", "B §0: GATE_ZONE→掩体档——B 层第二轴=掩体结构；真形第二轴按 A 正文推为底栖食场（探食场）——轴语义差异记档"],
  evid=[B3S.format(c="AST"), "outputs/full_authoring/" + EXP["AST"], CSV + "#AST", RS1B.format(c="AST"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0266"],
  open=[]),
 dict(code="SNS", sp="短吻鲟 Shortnose Sturgeon（Acipenser brevirostrum）", src="B3", prem=[
   "nocturnal_feeding = 'Feeds mostly at night'（夜行摄食窗口=condition premise——SWO diel premise 同型）",
   "estuary_semianadromy = 河口/海湾/偶尔入海域切换（P05 premise）",
   "vu_cites1 = VU+CITES I+ESA 保护禁捕（捕获边界注记）"],
  steps=[gate("GATE_ZONE", "bottom_layer_zone（底层水层带——小型鲟贴底特化+CSV demersal 硬定位）"),
          ev("EVAL_TYPED_SUBSTRATE_FACTOR", "soft_bottom_probing（软底质插食档——'over soft substrates' 物理依赖：软泥/泥沙/硬底）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_invert_mollusk_field（底栖猎物场——幼鱼底栖甲壳/虫+成鱼加软体）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 'Feeds mostly at night over soft substrates'+幼成食性——底层硬定位先行（demersal+贴底特化）、软底质插食次之（插食物理依赖先于猎物评估）、底栖猎物场第三",
          "C: demersal 6-53m / anadromous / 晨昏活跃",
          "B §0: GATE_ZONE→掩体档两步——真形按 A 正文软底质句立三步（底质独立步）——B 层轴差异记档",
          "同形对照：GRH/RRH/DRU 真形（底层门→底质→资源三步）"],
  evid=[B3S.format(c="SNS"), "outputs/full_authoring/" + EXP["SNS"], CSV + "#SNS", RS1B.format(c="SNS"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0267"],
  open=[]),
 dict(code="GRB", sp="草鱼 Grass Carp（Ctenopharyngodon idella）", src="B1", prem=[
   "prebait_patches = 玩家预投饵斑块事实（环境资源 owner 保存，世界侧 fact——resolver 义务）",
   "morning_activity = 早晨活跃（CSV 锚——无 Story 空间程序证据不入链）"],
  steps=[gate("GATE_PATCH_PRESENCE", "herbivore_patch_presence（植食资源+预投饵斑块存在——斑块追随程序的先验：无斑块格不产生追随分布）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "herbivore_patch_quality（斑块质量档——水生植物/预投饵双构成同源评估）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B1: '分布跟随植食资源与预投饵斑块'——斑块追随=存在性先行（无斑块即无本程序分布），质量评估次之",
          "C: benthopelagic 0-30m / 植食性 browsing on substrate / 2 / 温和",
          "B §0: 斑块存在性→斑块质量档两步一致（同推导理由）"],
  evid=[B12B.format(b="CENSUS-B1", b2="B1", c="GRB"), B12S.format(b="CENSUS-B1", b2="B1", c="GRB"),
        "outputs/full_authoring/" + EXP["GRB"], CSV + "#GRB", RS1B.format(c="GRB"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0268"],
  open=[]),
 dict(code="SMA", sp="小口黑鲈·跟随翻底 Smallmouth Bass（Micropterus dolomieu）", src="B1", prem=[
   "disturbance_events = 它鱼/它动物翻底扰动事件与暴露猎物区（世界侧 fact，环境 owner 产生）",
   "dawn_dusk_activity = 晨昏活跃（CSV 锚不入链）"],
  steps=[gate("GATE_DISTURBANCE_WINDOW", "disturbance_window_active（扰动窗口内扰动事件存在——事件驱动机会：无扰动事件即无机会斑块）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "exposed_prey_opportunity（暴露猎物机会档——大量暴露=全额/有限暴露=×衰减/残余=软出局）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B1: '跟随扰动觅食：动态机会 patch 评估（扰动暴露的猎物区）'——动态机会=事件驱动，存在性是第一道门；常态分布由该鱼其它程序面承载（本程序只表达机会追随面）",
          "C: benthopelagic 1-7m / 8.5-29.5°C / 好斗", "B §0: 扰动机会存在性→暴露猎物档两步一致"],
  evid=[B12B.format(b="CENSUS-B1", b2="B1", c="SMA"), B12S.format(b="CENSUS-B1", b2="B1", c="SMA"),
        "outputs/full_authoring/" + EXP["SMA"], CSV + "#SMA", RS1B.format(c="SMA"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0269"],
  open=[]),
 dict(code="WEL", sp="欧洲巨鲶·摄食面 Wels Catfish（Silurus glanis）", src="B3", prem=[
   "hearing_smell_dominant = 听嗅主导猎捕（S7——感官 Response 层注记不进 Bake 判断步）",
   "male_nest_guard = 雄鱼筑巢护巢（S6——P04 guard 面另批承载，WEL-GUARD 互指）",
   "beaching_pigeons = 水边捕鸽 28%（水面呈现面注记）",
   "ontogeny_diet = 幼底栖无脊→成鱼/水生脊椎（S9 premise）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "hole_woody_structure_base（洞穴/沉木结构底板——'holes in the riverbed, sunken trees' 日藏结构主句先行）"),
          slot("low_light_night_slot（低光/夜相槽——'A nocturnal predator' story 原文）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 'nocturnal predator, foraging near bottom and in water column'+'prefers...holes in the riverbed, sunken trees'——结构底板先行、夜相槽次之（夜行底板=结构+夜槽双承载）",
          "C: benthopelagic 0-30m / 夜间活跃 / 4.36 / 孤僻", "B §0: 夜行底板档→低光槽两步一致"],
  evid=[B3S.format(c="WEL"), "outputs/full_authoring/" + EXP["WEL"], CSV + "#WEL", RS1B.format(c="WEL"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0270"],
  open=[]),
 dict(code="FLA", sp="铲鮰 Flathead Catfish（Pylodictis olivaris）", src="B3", prem=[
   "ontogeny_diet = 幼鱼 riffle 虫幼→成鱼螯虾/贝/鱼（S9 premise）",
   "nocturnal_eo = 夜行/伏击行为面 FishBase 未述（story EO）——夜槽依 CSV 夜间活跃锚（证据分层注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "log_pool_structure_base（倒木/碎屑深潭底板——成鱼'pools with logs and other debris' 栖息主句先行）"),
          slot("low_light_night_slot（低光/夜相槽——CSV 夜间活跃锚 Tier C 级）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 成鱼'pools with logs and other debris'——结构底板先行；夜行=story EO+CSV 锚（MOO 同型 CSV 级证据分层）",
          "C: demersal / 21.5-33.5°C / 夜间活跃 / 3.78", "B §0: 夜行底板档→低光槽两步一致"],
  evid=[B3S.format(c="FLA"), "outputs/full_authoring/" + EXP["FLA"], CSV + "#FLA", RS1B.format(c="FLA"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0271"],
  open=[]),
 dict(code="BUR", sp="江鳕 Burbot（Lota lota）", src="B3", prem=[
   "seasonal_depth_shift = 夏深冬活动季节重排（S4——P05 阶段语义 premise）",
   "winter_spawn_ball = 冬夜产卵球 20 尾缠绕（S6——繁殖集群非摄食群 premise）",
   "chin_barbel = 颏须 1 根（S7 形态注记）"],
  steps=[ev("EVAL_TYPED_HABITAT_FACTOR", "rock_pool_deep_base（石底深潭底板——岩缝/树根 S8+'deep waters in summer' 栖息主句先行）"),
          slot("low_light_night_slot（低光/夜相槽——'Crepuscular and nocturnal' story 原文）")],
  ret="SpatialDistributionWeight",
  basis=["A-B3: 'Crepuscular and nocturnal'+岩缝/树根（S8）+夏深（S4→premise）——石底深潭底板先行、夜相槽次之",
          "C: demersal 1-700m / 夜间活跃 / 3.84", "B §0: 夜行底板档→低光槽两步一致"],
  evid=[B3S.format(c="BUR"), "outputs/full_authoring/" + EXP["BUR"], CSV + "#BUR", RS1B.format(c="BUR"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0272"],
  open=[]),
 dict(code="DRU", sp="黑鼓鱼 Black Drum（Pogonias cromis）", src="B1", prem=[
   "benthic_prey_field = 底栖猎物分布（上游 fact）",
   "feeding_traces = 翻底凹痕/泥云（本鱼行为产物——世界侧痕迹可见性，不改变鱼自身分布程序）",
   "dusk_dawn_activity = 晨昏活跃（CSV 锚不入链）"],
  steps=[gate("GATE_ZONE", "bottom_layer_zone（底层水层带——demersal CSV 硬定位+翻底取食特化）"),
          ev("EVAL_TYPED_SUBSTRATE_FACTOR", "substrate_turnover_ability（底质可翻性档——可翻软泥/难翻硬底/不可翻岩盘：翻底物理依赖先于猎物评估）"),
          ev("EVAL_TYPED_FORAGE_FACTOR", "benthic_fauna_field（底栖猎物场—— crab/虾/贝/虫）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B1: '分布跟随底栖猎物资源 patch（翻底觅食）'——翻底取食对底质可翻性有物理依赖：底层定位先行、可翻性次之、猎物场第三",
          "C: demersal 10m+ / 18.5-28.5°C / oceanodromous / 3.38",
          "B §0: 底层定位→可翻性→猎物三步一致（同推导理由）"],
  evid=[B12B.format(b="CENSUS-B1", b2="B1", c="DRU"), B12S.format(b="CENSUS-B1", b2="B1", c="DRU"),
        "outputs/full_authoring/" + EXP["DRU"], CSV + "#DRU", RS1B.format(c="DRU"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0273"],
  open=[]),
 dict(code="BHC", sp="鳙鱼 Bighead Carp（Hypophthalmichthys nobilis）", src="B2", prem=[
   "food_field = 浮游动物/植物/悬浮颗粒浓度场（世界侧 fact，水柱分布）"],
  steps=[ev("EVAL_FIELD_CONCENTRATION", "plankton_concentration_field（浮游浓度场评估——场 evaluand 分布式浓度场；水柱层分布并入场事实非独立判断步）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '滤食机会由 FoodField 浓度与水层决定：食物场浓度评估（场 evaluand——分布式浓度场，非离散 patch）→ 归一化'——单步场评估（'与水层'由场的水柱分布承载）",
          "C: benthopelagic / 0.5-38°C / 杂食 variable / 2.83",
          "B §0: 三步链（水层定位→浓度→鳃耙口径）＝'handoff 判序指令落于场评估语义'的展开——census 侧读法分歧已登记 README §7；真形按 Tier C 冻结 sketch 单步场评估（B 层展开无 story 级顺序证据）"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="BHC"), B12S.format(b="CENSUS-B2", b2="B2", c="BHC"),
        "outputs/full_authoring/" + EXP["BHC"], CSV + "#BHC", RS1B.format(c="BHC"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0274"],
  open=["B 层三步展开（水层/口径步）无 story 级顺序证据——表达线若补证可复议"]),
 dict(code="HER", sp="大西洋鲱 Atlantic Herring（Clupea harengus）", src="B2", prem=[
   "food_field = 浮游食场（世界侧 fact）",
   "school_overlay = 群游集聚（空间 Factor 值域承载——coverage #17 判，非独立程序步）",
   "seasonal_spawning_migration = 季节产卵迁移（lifecycle premise——配置级切换因子集）"],
  steps=[ev("EVAL_FIELD_CONCENTRATION", "plankton_concentration_field（浮游食场浓度评估——场 evaluand；群游集聚并入分档槽值域）")],
  ret="SpatialDistributionWeight",
  basis=["C'-B2: '浮游食场跟随：食物场浓度评估 → 归一化'——单步场评估",
          "C: benthopelagic 0-364m / 滤食性 selective plankton feeding / 1-18°C",
          "B §0: 三步链=handoff 判序指令展开（同 BHC）——与 census canonical 两步判语的拓扑分歧已登记 README §7；真形按 Tier C 冻结 sketch 单步场评估"],
  evid=[B12B.format(b="CENSUS-B2", b2="B2", c="HER"), B12S.format(b="CENSUS-B2", b2="B2", c="HER"),
        "outputs/full_authoring/" + EXP["HER"], CSV + "#HER", RS1B.format(c="HER"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0275"],
  open=["同 BHC 注记"]),
 dict(code="BLU", sp="蓝鳃太阳鱼 Bluegill Sunfish（Lepomis macrochirus）·护巢面", src="B1", prem=[
   "colony_breeding_eligible = 殖民地巢群繁殖资格已在路由面判定（本步不重复结算 premise）",
   "season_layer_note = 季节性水层变化（Normal 面另载——B1 sketch，本真形=Guard 面 §2.2）"],
  steps=[gate("GATE_ANCHOR_EXISTENCE", "colony_nest_anchor（殖民地巢群锚存在——巢体不存在格×0.01 软出局返回非零）"),
          ev("EVAL_TYPED_ANCHOR_SUITABILITY", "colony_nest_site_quality（巢床结构选址档——C06 已审'预先建立并持续照护'：建立期选址先行）"),
          ev("EVAL_TYPED_RELATION_FACTOR", "guard_relation（照护期占位关系档——与巢群锚点距离/朝向三档）"),
          ev("EVAL_TYPED_LOCAL_TEMPERATURE", "guard_local_temperature（护巢局部温度档）")],
  ret="GuardingSpatialDistributionWeight",
  basis=["C'-B1+A: 蓝鳃 colony 巢群护巢——'C06 建立期选址→照护期占位'（Tier A 已审主张）：锚存在先行、选址适配次之、占位关系第三、局部温度第四",
          "C: benthopelagic / 1-36°C / 晨昏活跃",
          "B §0 guard 面: 锚存在→锚适配→关系→局部温度四步一致（推导来源 Tier A 同引）"],
  evid=[B12B.format(b="CENSUS-B1", b2="B1", c="BLU"), B12S.format(b="CENSUS-B1", b2="B1", c="BLU"),
        "outputs/full_authoring/" + EXP["BLU"], CSV + "#BLU", RS1B.format(c="BLU"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0276"],
  open=["档位成员 [需正文]"]),
 dict(code="ARA", sp="巨骨舌鱼 Arapaima（Arapaima gigas）·护幼面", src="B3", prem=[
   "flood_pulse = 洪水周期生命周期（低水期产卵/洪泛季幼鱼成长/干季孤立湖——P05 阶段语义 premise）",
   "obligate_air_breathing = 专性气呼吸（runtime persistent 条件——可预测水面机会 typed 注记不买 Mode）",
   "brood_eligible = 稚鱼群存在与洪水位相已在路由面结算（anti-double-counting premise）"],
  steps=[gate("GATE_ANCHOR_EXISTENCE", "nest_brood_anchor（沙底巢+稚鱼群锚存在——含洪泛漫滩可及性；洪水位相只在锚门消费一次）"),
          ev("EVAL_TYPED_ANCHOR_SUITABILITY", "floodplain_brood_habitat_quality（漫滩掩体群栖境档——巢址 sandy bottoms 15cm 深 50cm 宽+稚鱼群栖境）"),
          ev("EVAL_TYPED_RELATION_FACTOR", "guard_relation（环护关系档——guards the eggs and the young）"),
          ev("EVAL_TYPED_LOCAL_TEMPERATURE", "guard_local_temperature（护幼局部温度档）")],
  ret="GuardingSpatialDistributionWeight",
  basis=["A-B3: 'Builds a nest...in sandy bottoms...guards the eggs and the young'+洪水周期（幼鱼用洪泛季成长）——锚存在先行（巢+稚鱼群双目标）、栖境适配次之、环护关系第三、局部温度第四",
          "C: demersal / 25-29°C / 4.5 / 追猎", "B §0 guard 面: 四步一致（Tier B 一句'洪水护幼'方向级+本 A 正文全句证据升级）"],
  evid=[B3S.format(c="ARA"), "outputs/full_authoring/" + EXP["ARA"], CSV + "#ARA", RS1B.format(c="ARA"),
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0277"],
  open=[]),
 dict(code="RBP", sp="红腹食人鱼 Red-bellied Piranha（Pygocentrus nattereri）·护卵面", src="B3", prem=[
   "dusk_dawn_feeding = 黄昏/夜虫/鱼/腐食摄食（S1——摄食面 premise；RB-1 RBP 摄食面真形另载）",
   "defensive_schooling = 群游为防御非合作捕猎（S3——群结构事实背景）",
   "auditory_capacity = 高度发达听觉（S7——呈现面感官线索注记）",
   "guard_eligible = 护卵资格已在路由面判定（premise）"],
  steps=[gate("GATE_ANCHOR_EXISTENCE", "tree_root_egg_mass_anchor（沉水树根卵块锚存在——'Eggs are laid on tree roots trailing in the water and are guarded'）"),
          ev("EVAL_TYPED_ANCHOR_SUITABILITY", "root_spawning_surface_quality（树根/水草附着面档——利用型附着基质）"),
          ev("EVAL_TYPED_RELATION_FACTOR", "guard_relation（护卵关系档）"),
          ev("EVAL_TYPED_LOCAL_TEMPERATURE", "guard_local_temperature（护卵局部温度档）")],
  ret="GuardingSpatialDistributionWeight",
  basis=["A-B3: 'Eggs are laid on tree roots trailing in the water and are guarded'——附着卵块锚存在先行、附着面适配次之、护卵关系第三、局部温度第四",
          "C: pelagic / 23-27°C / 3.72", "B §0 guard 面: 四步一致（Tier B 一句'树根护卵'+本 A 正文原句证据升级）",
          "同鱼异面注记：RB-1 P-RB1-RBP-BAKE=摄食面单因子（虫/腐植 patch）——本真形=护卵面（§2.2），两程序面独立记账不互推"],
  evid=[B3S.format(c="RBP"), "outputs/full_authoring/" + EXP["RBP"], CSV + "#RBP", RS1B.format(c="RBP"),
        "fish_logic_census/batches/CENSUS-REBUILD-001/blind_programs.jsonl#P-RB1-RBP-BAKE",
        "fish_logic_census/truth_rebuild_queue.jsonl#TRB-0278"],
  open=[]),
]

# ===== RB-1 复用 17（B4 起源同鱼同面）+ WS2（同种 WST）=====
REUSE = {
 "BSB": ("TRB-0279",), "BSK": ("TRB-0280",), "BST": ("TRB-0281",), "CBM": ("TRB-0282",),
 "FDR": ("TRB-0283",), "GDE": ("TRB-0284",), "GPF": ("TRB-0285",), "GRH": ("TRB-0286",),
 "HNC": ("TRB-0287",), "MOO": ("TRB-0288",), "RRH": ("TRB-0289",), "SDG": ("TRB-0290",),
 "SMB": ("TRB-0291",), "SSL": ("TRB-0292",), "TSK": ("TRB-0293",), "WIT": ("TRB-0294",),
 "YTF": ("TRB-0295",),
}


def build():
    rb1 = {}
    for line in RB1.read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        rb1[r["species_id"]] = r

    out = []
    for d in F:
        code = d["code"]
        qid = QUEUE.get("P-B6-%s-BAKE" % code) or QUEUE.get("P-RS1-%s-BAKE" % code)
        assert qid, code
        steps = d["steps"]
        evid = [e for e in d["evid"] if not e.startswith("fish_logic_census/truth_rebuild_queue.jsonl#")]
        evid.append("fish_logic_census/truth_rebuild_queue.jsonl#%s" % qid)
        body = {
            "program_id": "P-RB2-%s-BAKE" % code,
            "story_id": "CENSUS-REBUILD-002-%s" % code,
            "species_id": code,
            "surface": "Bake",
            "incoming_premises": d["prem"],
            "surface_owned_logic": {
                "chain_semantics": "PROGRESSIVE_TIERED_FUNNEL（渐进累积：每步 EVAL→三档→乘入 running weight；×0.01 软出局立即返回；无终步合并）",
                "ordered_steps": steps,
            },
            "human_readable_sketch": sketch_of(steps, ""),
            "branches": branches_of(steps),
            "combine": "NONE_PROGRESSIVE",
            "return_type": d["ret"],
            "instance_noise": {"species": d["sp"], "profile": None, "constants": {}},
            "helpers": [],
            "source_evidence_ids": evid,
            "open_semantics": d["open"],
            "order_derivation": {
                "status": "derived",
                "basis": d["basis"],
                "evidence_layers": LAB6 if d["evid"][0].startswith("fish_logic_census/batches/CENSUS-B6") else (LA2 if d["evid"][0].startswith("fish_logic_census/batches/CENSUS-B3") else LA12),
                "queues": [qid],
                "dual_track": False,
            },
            "registry_seen": False,
            "registry_seen_at_creation": False,
        }
        out.append(body)

    # RB-1 复用体：copy 语义体，重打 program/story/evidence/reuse 标注
    for code, (qid,) in REUSE.items():
        src = rb1[code]
        steps = src["surface_owned_logic"]["ordered_steps"]
        od = dict(src["order_derivation"])
        od["status"] = "reused"
        od["reused_from"] = "CENSUS-REBUILD-001:P-RB1-%s-BAKE" % code
        od["queues"] = [QUEUE["P-RS1-%s-BAKE" % code]]
        od["consistency_check"] = ("同鱼同面复用：RB-1 证据层（B4 story 快照+表达文件+CSV）与本批 RS1 证据层指向同一 B4 冻结 story——"
                                   "无新顺序证据（Tier B 表达链=约定序层不构成冲突证据）；一致性核验=RB-1 basis 事实逐条存在于 B4 快照（本批复核通过）")
        od["evidence_layers"] = src["order_derivation"]["evidence_layers"] + ["RB1=CENSUS-REBUILD-001 frozen truth body (same-species same-face reuse)"]
        body = {
            "program_id": "P-RB2-%s-BAKE" % code,
            "story_id": "CENSUS-REBUILD-002-%s" % code,
            "species_id": code,
            "surface": "Bake",
            "incoming_premises": src["incoming_premises"],
            "surface_owned_logic": src["surface_owned_logic"],
            "human_readable_sketch": src["human_readable_sketch"].replace("【RB-1", "【RB-2（复用 RB-1 推导）", 1),
            "branches": src["branches"],
            "combine": src["combine"],
            "return_type": src["return_type"],
            "instance_noise": src["instance_noise"],
            "helpers": [],
            "source_evidence_ids": [
                B4S.format(c=code),
                "fish_logic_census/batches/CENSUS-REBUILD-001/blind_programs.jsonl#P-RB1-%s-BAKE" % code,
                RS1B.format(c=code),
                "fish_logic_census/truth_rebuild_queue.jsonl#%s" % QUEUE["P-RS1-%s-BAKE" % code],
            ],
            "open_semantics": src["open_semantics"],
            "order_derivation": od,
            "registry_seen": False,
            "registry_seen_at_creation": False,
            "reused_from": "CENSUS-REBUILD-001:P-RB1-%s-BAKE" % code,
        }
        out.append(body)

    # WS2：白化高首鲟品系=同种 WST 复用（Cross-Batch 去重联动第 2 例）
    src = rb1["WST"]
    steps = src["surface_owned_logic"]["ordered_steps"]
    od = dict(src["order_derivation"])
    od["status"] = "reused"
    od["reused_from"] = "CENSUS-REBUILD-001:P-RB1-WST-BAKE"
    od["queues"] = [QUEUE["P-B6-WS2-BAKE"]]
    od["consistency_check"] = ("同种复用：WS2=高首鲟白化品系（story 明言'复用 R09'+Identity Deferred）；WST RB-1 真形（B5 story Tier A+CSV）=同种机制——"
                               "品系行 S1-S11 全 SN 无独立机制证据；去重联动 WS2↔WST Cross-Batch 第 2 例")
    od["evidence_layers"] = src["order_derivation"]["evidence_layers"] + ["RB1=CENSUS-REBUILD-001 frozen truth body (same-species strain reuse)"]
    body = {
        "program_id": "P-RB2-WS2-BAKE",
        "story_id": "CENSUS-REBUILD-002-WS2",
        "species_id": "WS2",
        "surface": "Bake",
        "incoming_premises": ["strain_reuse = 高首鲟 R09 品系复用先例（Identity Deferred——品系外观不构成机制差异）"] + src["incoming_premises"],
        "surface_owned_logic": src["surface_owned_logic"],
        "human_readable_sketch": src["human_readable_sketch"].replace("【RB-1", "【RB-2（复用 RB-1 推导·同种 WST）", 1),
        "branches": src["branches"],
        "combine": src["combine"],
        "return_type": src["return_type"],
        "instance_noise": {"species": "白化高首鲟 White Sturgeon 02（Acipenser transmontanus 品系）", "profile": None, "constants": {}},
        "helpers": [],
        "source_evidence_ids": [
            B6S.format(c="WS2"), CSV + "#WS2",
            "fish_logic_census/batches/CENSUS-REBUILD-001/blind_programs.jsonl#P-RB1-WST-BAKE",
            B6B.format(c="WS2"),
            "fish_logic_census/truth_rebuild_queue.jsonl#%s" % QUEUE["P-B6-WS2-BAKE"],
        ],
        "open_semantics": src["open_semantics"],
        "order_derivation": od,
        "registry_seen": False,
        "registry_seen_at_creation": False,
        "reused_from": "CENSUS-REBUILD-001:P-RB1-WST-BAKE",
    }
    out.append(body)

    # hash + freeze
    from datetime import datetime, timezone
    frozen = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = []
    for b in out:
        b["blind_hash"] = hashlib.sha256(json.dumps(b, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()[:16]
        b["frozen_at_utc"] = frozen
        lines.append(json.dumps(b, ensure_ascii=False))
    return out, lines


if __name__ == "__main__":
    out, lines = build()
    assert len(out) == 94, len(out)
    ids = [b["program_id"] for b in out]
    assert len(set(ids)) == 94
    BATCH.mkdir(parents=True, exist_ok=True)
    (BATCH / "blind_programs.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("frozen", len(out), "bodies")
