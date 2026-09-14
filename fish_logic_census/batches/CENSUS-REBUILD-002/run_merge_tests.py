# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-002 merge-test engine + semantic verdicts.

Opens template_registry.yaml v9 (post-freeze, read-only; zero mutation) and
compares each frozen truth body against the 13 active Bake-family canonicals
by structural signature. Engine layer reports raw signature matches; the
semantic layer (worker adjudication below) applies family-domain reading per
work standards 2.3/6.4 + RB-1 precedents:
  - [E,E] same-signature families disambiguated semantically (ORDER=族判据)；
  - RS1 在册成员双轨：order_confirm（真形序=所在族 canonical 序——清 order_provisional 提案）
    vs moved_proposal（真形序≠所在族——族移动提案 STRUCTURAL_DIFF=ORDER/步数）；
  - RB-1 新族提案形状（FF/SF/TB/FS）不在 registry——NEW 轨备注 related_proposal=HRQ-RB1-02
    （本批判同只对 registry v9 活族）。
"""
import json, os, datetime, hashlib
import yaml

ROOT = r"A:\Projs\FCF-Harness-Handoff\programaticHitFish"
CEN = os.path.join(ROOT, "fish_logic_census")
BATCH = "CENSUS-REBUILD-002"
OUT = os.path.join(CEN, "batches", BATCH)

CANON = {
    "CONSTRAINED_RELATIVE_REFUGE": dict(sig=["BUILD", "GATE", "RANK", "EVAL", "COMBINE"],
        note="AccessibleSet->HardViability->FeasibleSet->RelativeRank->SecondaryRefuge->FixedCombine"),
    "HARD_GATED_FACTOR_COMBINE": dict(sig=["BUILD", "GATE", "GATE", "EVAL", "EVAL", "EVAL", "EVAL"],
        note="v2: BUILD+双硬门+EXIT 档因子x4 unordered"),
    "TIERED_SINGLE_FACTOR_CHAIN": dict(sig=["EVAL"], note="单 typed 因子三档渐进"),
    "LAYER_AXIS_DUAL_TIER_CHAIN": dict(sig=["EVAL", "EVAL"],
        note="水层软三档->premise 绑定轴段三档（第二步=premise 轴段——轴域限定）"),
    "GATED_COVER_TIER_CHAIN": dict(sig=["GATE", "EVAL"], note="结构掩体存在门->掩体/单档（factor_type typed 参数）"),
    "NOCTURNAL_LIGHTSLOT_CHAIN": dict(sig=["EVAL", "SLOT"], note="夜行底板档->低光槽（adjuster，槽位判例固定）"),
    "ZONE_SUBSTRATE_RESOURCE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL"], note="GATE_ZONE 底层硬定位->底质档->资源档"),
    "SOFT_TRIPLE_TIER_CHAIN": dict(sig=["EVAL", "EVAL", "EVAL"], note="近底带软三档->底质档->资源档（无门）"),
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL"], note="GATE_ZONE->深度档->底质档->资源档"),
    "FILTER_FIELD_ACCUMULATE_CHAIN": dict(sig=["EVAL", "EVAL_FIELD", "EVAL_GAUGE"], note="滤食水层->场浓度->口径（特殊 op 语义）"),
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL"], note="锚存在门->锚适配->关系->局部温度（anchor 四形式轴）"),
    "EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL", "EVAL"], note="极值水温门->EXIT 档因子x4 unordered"),
    "PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN": dict(sig=["GATE", "EVAL", "SLOT"], note="patch 存在门->patch 强度档->rank position 槽"),
}

# RS1 在册成员的 registry 归族（v9 known_instances 递归提取）
RS1_FAMILY = {
 "TIERED_SINGLE_FACTOR_CHAIN": ["COD", "PIK19", "ARC", "VEN", "SWO", "CHN", "COH", "BRO", "ALE", "TAR",
                                 "BRT12", "PB", "BST", "CBM", "PAD34", "SDG", "TSK"],
 "LAYER_AXIS_DUAL_TIER_CHAIN": ["CHU", "SHA"],
 "GATED_COVER_TIER_CHAIN": ["FGA", "SGA", "AST", "SNS", "GPF", "SSL", "WIT", "YTF", "FDR", "BSB", "GRB", "SMA"],
 "NOCTURNAL_LIGHTSLOT_CHAIN": ["WEL", "FLA", "BUR", "GDE", "MOO"],
 "ZONE_SUBSTRATE_RESOURCE_CHAIN": ["GRH", "RRH", "DRU"],
 "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": ["SMB"],
 "SOFT_TRIPLE_TIER_CHAIN": ["BSK"],
 "FILTER_FIELD_ACCUMULATE_CHAIN": ["BHC", "HER"],
 "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": ["BLU", "ARA", "RBP", "HNC"],
}
RS1_MEMBERSHIP = {sp: fam for fam, sps in RS1_FAMILY.items() for sp in sps}
assert len(RS1_MEMBERSHIP) == 47

TS = "TIERED_SINGLE_FACTOR_CHAIN"; GC = "GATED_COVER_TIER_CHAIN"
GA = "GUARD_ANCHOR_TIERED_COMBINE_CHAIN"; NO = "NOCTURNAL_LIGHTSLOT_CHAIN"
ZS = "ZONE_SUBSTRATE_RESOURCE_CHAIN"; ST = "SOFT_TRIPLE_TIER_CHAIN"
ZD = "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN"; LA = "LAYER_AXIS_DUAL_TIER_CHAIN"
FF = "FORAGE_FIRST_DUAL_TIER_CHAIN__RB1"
SF = "SPACE_FIRST_DUAL_TIER_CHAIN__RB1"
TB = "GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN__RB1"
FS = "HABITAT_FORAGE_FLOODSLOT_CHAIN__RB1"

# verdict map: sid -> dict(verdict, target, note, order_confirm, moved_from, related, reused)
V = {}


def add(sid, verdict, target, note, *, oc=False, mf=None, rel=None, ru=None):
    V[sid] = dict(verdict=verdict, target=target, note=note, order_confirm=oc,
                  moved_from=mf, related=rel, reused=ru)


R1 = "reused_from=CENSUS-REBUILD-001（同鱼同面复用——零冲突序）"

# ---- RS1 47：链族在册成员（order_provisional 终裁轨） ----
for sid in ["COD", "PIK19", "ARC", "VEN", "SWO", "TAR", "PAD34"]:
    add(sid, "MERGE_CONFIDENT", TS,
        "单步链无序判据适用——三档渐进语义 MC；轴值 typed 参数（premise 轴段/感官信号场）",
        oc=True)
add("CHN", "MERGE_CONFIDENT", LA,
    "真形两步[近底软定位->洄游廊道轴段]：垂直层与水平廊道独立维度（CSV benthopelagic 锚入步）；vs 所在族 TS 单步=步数差异——族移动提案 TS->LA；B 层样板语义还原（约定序）不采",
    mf=TS)
add("COH", "MERGE_CONFIDENT", LA,
    "真形两步[中上层软定位->廊道轴段]（CSV pelagic-neritic 锚）：族移动提案 TS->LA（同 CHN 推导）",
    mf=TS)
add("BRO", "MERGE_CONFIDENT", LA,
    "真形两步[近底软定位->salter 廊道轴段]（CSV benthopelagic）：族移动提案 TS->LA",
    mf=TS)
add("ALE", "MERGE_CONFIDENT", LA,
    "真形两步[中上层软定位->廊道轴段]（CSV pelagic-neritic；陆封/溯河双型落值域）：族移动提案 TS->LA",
    mf=TS)
add("BRT12", "NEW_TEMPLATE_CANDIDATE", FF,
    "真形两步[季节脉冲猎物 patch->中上层软带]：食性主句先行（机会型）——落在 RB-1 FF 提案形状（不在 registry v9 活族）——族移动提案 TS->FF；B 层单步未含 CSV 定位步",
    mf=TS, rel="HRQ-RB1-02")
add("PB", "NEW_TEMPLATE_CANDIDATE", FF,
    "真形两步[characiform 追猎场->浅渊湾/缓流带]：食性主句先行——RB-1 FF 提案形状；族移动提案 TS->FF（B 层机会场单步未入 S8 栖息句）",
    mf=TS, rel="HRQ-RB1-02")
add("BST", "MERGE_CONFIDENT", TS, "单步链 MC（底栖无脊机会场）", oc=True, ru=R1)
add("CBM", "MERGE_CONFIDENT", TS, "单步链 MC（浮游/小鱼机会场）", oc=True, ru=R1)
add("SDG", "NEW_TEMPLATE_CANDIDATE", FF,
    "真形两步[底层杂食猎物场->陆架带]：RB-1 FF 形状（裁决 4 电感知分层后双因子）——族移动提案 TS->FF",
    mf=TS, rel="HRQ-RB1-02", ru=R1)
add("TSK", "NEW_TEMPLATE_CANDIDATE", SF,
    "真形两步[深冷底带->底层广食场]：RB-1 SF 形状（深冷主句先行）——族移动提案 TS->SF",
    mf=TS, rel="HRQ-RB1-02", ru=R1)
add("CHU", "MERGE_CONFIDENT", LA,
    "真形两步[近底软定位->廊道轴段]：与 canonical 精确同构（canonical 源成员真形复验；CSV benthopelagic 锚=RS1 入步依据被本批独立推导确认）",
    oc=True)
add("SHA", "MERGE_CONFIDENT", LA,
    "真形两步[中上层软定位->廊道轴段]：与 canonical 精确同构（canonical 源成员真形复验；pelagic-neritic+鳃耙构型）",
    oc=True)
for sid, note in [
    ("FGA", "GATE 植被缘掩体->掩体档：与 canonical 同构（canonical 源成员真形复验）；gate_axis 值=参数"),
    ("SGA", "GATE 缓流植被掩体->掩体档：canonical 源成员真形复验"),
    ("AST", "GATE_ZONE 河口底层->底栖探食场单档：结构同构（GATE->EVAL）；第二步 factor_type=探食场（INC/WST gate->forage 参数读法同型——canonical 掩体档轴域扩展注记挂 HRQ）；B 层第二轴=掩体档（Tier B 与 Tier A 轴分歧记档 HRQ-RB2-04）"),
    ("GRB", "GATE 斑块存在->斑块质量档：canonical 同构（canonical 源成员真形复验）；gate_axis=patch_presence 既有值"),
    ("SMA", "GATE 扰动窗口->暴露猎物机会档：canonical 同构（canonical 源成员真形复验）；事件驱动机会面"),
]:
    add(sid, "MERGE_CONFIDENT", GC, note, oc=True)
add("SNS", "MERGE_CONFIDENT", ZS,
    "真形三步[GATE_ZONE 底层->软底质插食档->底栖猎物场]：'over soft substrates' 原文级底质独立步——vs 所在族 GC 两步=步数差异；族移动提案 GC->ZS（GRH/RRH/DRU 同形）；B 层两步（Tier B 与 Tier A 步数分歧记档 HRQ-RB2-04）；夜行=condition premise（SWO diel 同型）",
    mf=GC)
add("GPF", "MERGE_CONFIDENT", GC, "GATE 可埋沙泥->潮间带掩体档：canonical 同构（canonical 源成员真形复验）", oc=True, ru=R1)
for sid in ["SSL", "FDR", "BSB"]:
    add(sid, "NEW_TEMPLATE_CANDIDATE", SF,
        "真形两步 space->forage：RB-1 SF 形状（story Tier A 证伪伏击门样板——SSL 潜沙=反捕食 overlay/FDR=Bottom Omnivore/BSB 无二元原文）——族移动提案 GC->SF",
        mf=GC, rel="HRQ-RB1-02", ru=R1)
for sid in ["WIT", "YTF"]:
    add(sid, "NEW_TEMPLATE_CANDIDATE", TB,
        "真形三步 GATE 可埋底质->深冷复合带->资源：RB-1 TB 提案形状（+深冷复合带步=OPERATOR/步数真差异）——族移动提案 GC->TB；双轨确认（RB-1 已提案，本批 RS1 轨独立复核一致）",
        mf=GC, rel="HRQ-RB1-02", ru=R1)
for sid, note in [
    ("WEL", "夜行结构底板档->低光槽：canonical 同构（canonical 源成员真形复验；story 原文级夜行）"),
    ("FLA", "倒木深潭底板->低光槽：canonical 同构；夜槽=CSV 锚（MOO 同型证据分层注记）"),
    ("BUR", "石底深潭底板->低光槽：canonical 同构（story 原文级黄昏夜行）"),
]:
    add(sid, "MERGE_CONFIDENT", NO, note, oc=True)
for sid in ["GDE", "MOO"]:
    add(sid, "MERGE_CONFIDENT", NO, "夜行底板->低光槽：canonical 同构（GDE=story 原文/MOO=CSV 锚——RB-1 证据分层注记沿用）",
        oc=True, ru=R1)
for sid in ["GRH", "RRH"]:
    add(sid, "MERGE_CONFIDENT", ZS, "GATE_ZONE->底质->资源三步：canonical 同构（canonical 源成员真形复验）", oc=True, ru=R1)
add("DRU", "MERGE_CONFIDENT", ZS, "GATE_ZONE->可翻性->底栖猎物场三步：canonical 同构（翻底物理依赖推导与 canonical 同理由）", oc=True)
add("SMB", "MERGE_CONFIDENT", ZD, "GATE_ZONE->深度->底质->资源四步：canonical 同构（canonical 源成员真形复验；CSV 深>=4m 锚）", oc=True, ru=R1)
add("BSK", "MERGE_CONFIDENT", ST, "近底软三档->底质->资源无门：canonical 同构（canonical 源成员真形复验）", oc=True, ru=R1)
for sid, note, anchor in [
    ("BLU", "锚存在门->选址->占位关系->局部温度：canonical 精确同构（canonical 源成员真形复验；Tier A C06 建立期选址->照护期占位=步序证据）", "colony_nest（nest 构建型——殖民地巢群）"),
    ("ARA", "锚存在门->漫滩栖境->环护关系->局部温度：canonical 精确同构（A 正文全句证据升级 B 层一句方向级）；anchor 跨阶段（沙底巢->稚鱼群）按初始形式落 nest+后阶段注记（MUT ② CSL 先例）", "nest（沙底巢+稚鱼群 brood 后阶段注记）"),
    ("RBP", "锚存在门->树根附着面->护卵关系->局部温度：canonical 精确同构（A 正文原句 'Eggs are laid on tree roots...guarded'）；同鱼异面注记：RB-1 RBP=摄食面单因子（另轨）——本项=护卵面独立记账", "egg_mass（树根附着利用型）"),
]:
    add(sid, "MERGE_CONFIDENT", GA, note + "；anchor=" + anchor, oc=True)
add("HNC", "MERGE_CONFIDENT", GA, "锚存在门->石巢选址->关系->局部温度：canonical 同构（RB-1 MC 复用；anchor=nest 构建型）", oc=True, ru=R1)
for sid in ["BHC", "HER"]:
    add(sid, "MERGE_CONFIDENT", TS,
        "真形单步场浓度评估（场 evaluand 因子）：vs 所在族 FILTER_FIELD 三步 canonical（水层/口径步）=步数差异——族移动提案 FILTER_FIELD->TS（factor_type=field 轴值读法——B2 判例复活：EVAL_TYPED_FIELD_OR_FACTOR 单步+场轴）；B 层三步展开=handoff 判序指令落置（无 story 级顺序证据，census 冻结 sketch 单步场评估）；FILTER_FIELD 移空后 0 成员——空置提案挂 HRQ（PATCH VACATED 先例）；return_type 修正=REV-RB2-001 留痕",
        mf="FILTER_FIELD_ACCUMULATE_CHAIN")

# ---- B6 47：AMB 第 3 层真形判同（vs registry v9 活族） ----
for sid, sp in [("SUK", "四白锦鲤"), ("GRK", "Goromo 锦鲤"), ("KHK", "Kohaku 锦鲤"), ("OGK", "Ogon 锦鲤"),
                ("LCP", "无鳞鲤"), ("AMC", "镜鲤白化"), ("ASC", "鳞鲤白化"), ("HFC", "人面鲤")]:
    add(sid, "MERGE_CONFIDENT", TS,
        "单步链 MC（同种鲤品系——Identity Deferred S1-S11 全 SN，分辨率=同种 CSV benthopelagic 单因子；无序判据适用）；亲本真形待 R03 轨（open_semantics）")
add("AGC", "MERGE_CONFIDENT", GC,
    "GATE 斑块存在->斑块质量档：canonical 同构（同种 GRB 本批真形复用——品系先例；AGC↔GRB 同种 Cross-Batch 去重联动）")
add("WAG", "MERGE_CONFIDENT", GC,
    "GATE 植被缘掩体->掩体档：canonical 同构（复用 B01 伏击 story 明言+FGA/SGA 同科构型判例）")
add("WCC", "MERGE_CONFIDENT", NO,
    "底潭底板->低光槽：canonical 同构（复用 B01+CSV demersal/夜间活跃——夜槽 CSV 锚 MOO 同型；BBH/BCF/WHC 同批同科同构）")
add("HYS", "MERGE_CONFIDENT", GC,
    "GATE_ZONE 底层->底栖探食场单档：canonical 同构（亲本飼系 P01+P05 复用 story 明言+鲟形目构型 WS2/AST 同形——gate->forage 参数读法 INC/WST 同型）；杂交行 CSV 栖息带空=亲本构型补位（open_semantics）")
add("ACA", "MERGE_CONFIDENT", NO,
    "鲶系结构底板->低光槽：canonical 同构（WEL 同属第 2 例+CSV demersal/夜间活跃；夜行=同属推算+CSV 锚分层注记）")
add("AMN", "MERGE_CONFIDENT", TS, "单步链 MC（S1 EO forage 轴不立——河川带单因子）")
add("ASB", "NEW_TEMPLATE_CANDIDATE", FF,
    "真形两步 forage->habitat：食性主句先行（幼浮游->成鱼虾发育切换信息密度）——RB-1 FF 提案形状（不在 registry 活族）；catadromous/protandry/冬礁产卵=premise",
    rel="HRQ-RB1-02")
add("ATC", "MERGE_CONFIDENT", GC,
    "GATE_ZONE 底层->底栖小动物场：canonical 同构（demersal CSV+鳕科微型底栖；INC/WST gate->forage 参数读法同型）")
add("AWF", "MERGE_CONFIDENT", GC,
    "GATE_ZONE 岩底->硬壳猎物场：canonical 同构（gate_axis=rock_bottom zone 值；gate->forage 参数读法同型）；雄护卵块+护卵停食=guard premise 注记（B6 判例④族）；碾压齿=Response 层注记（裁决 4 分层）")
for sid in ["BBH", "BCF", "WHC"]:
    add(sid, "MERGE_CONFIDENT", NO,
        "底板->低光槽：canonical 同构（鲿形目夜行底栖——BBH/BCF story S7 原文级夜行/WHC CSV 锚分层注记）")
add("BHM", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：食性主句先行（虫幼单类）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("BLT", "MERGE_CONFIDENT", TS, "单步链 MC（S1 EO——深潭冷水带单因子）")
add("BMB", "MERGE_CONFIDENT", TS, "单步链 MC（廊道域=premise——广食场单因子）")
add("BTS", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：水面昆虫食性主句先行（表层取向）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("CGD", "NEW_TEMPLATE_CANDIDATE", SF,
    "真形两步 habitat->forage：'沙底急流'复合栖息句（流速+底质两要素）+鮈类底栖特化绑定——复合带先行；RB-1 SF 提案形状", rel="HRQ-RB1-02")
add("DBC", "MERGE_CONFIDENT", TS, "单步链 MC（S1/S8 EO 同属推算——demersal 单因子；黄颡鱼 R03 轨补证后复核）")
add("DCL", "MERGE_CONFIDENT", TS, "单步链 MC（薄资料同属推算——同属河川底栖带单因子；无 CSV 行）")
add("EUP", "NEW_TEMPLATE_CANDIDATE", FF,
    "真形两步 forage->habitat：'opportunistic diurnal feeder' 食性主句先行（晨昏峰=condition premise）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("GDB", "MERGE_CONFIDENT", TS, "单步链 MC（S1 EO 同属推算——河川带单因子）")
add("GDS", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：杂食主句先行（植被湖潭次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("JSB", "NEW_TEMPLATE_CANDIDATE", FF,
    "真形两步 forage->habitat：同种 ASB 真形同体推导（JSB↔ASB 同 URL 同种——批内去重联动，双 queue 项独立记账）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("LFB", "MERGE_CONFIDENT", TS, "单步链 MC（S1 EO trophic 推算——河湖带单因子；P04 贝宿主=guard 面 premise 注记另轨）")
add("PCC", "MERGE_CONFIDENT", TS, "单步链 MC（S1 EO——同科底栖带单因子）")
add("PKC", "MERGE_CONFIDENT", TS, "单步链 MC（S1 EO 掠食推算——热带河带单因子）")
add("PKS", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：小鱼/无脊椎主句先行（植被静水次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("PLC", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：五类广谱漂食主句先行（急流带次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("PRB", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：'Feeds on fish'主句先行（河口带次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("PSH", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：鱼/甲壳主句先行（大河带次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("RBD", "NEW_TEMPLATE_CANDIDATE", SF,
    "真形两步 habitat->forage：'fast gravel and rubble riffles'复合句+镖鲈微底栖特化绑定——复合带先行；RB-1 SF 提案形状", rel="HRQ-RB1-02")
add("RSS", "MERGE_CONFIDENT", GC,
    "GATE_ZONE 底层->底栖无脊椎场：canonical 同构（demersal CSV+'Consumes benthic prey' 底栖绑定；INC/WST gate->forage 参数读法同型）")
add("RSC", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：腐屑/摇蚊主句先行（泥底带次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("RUF", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：浮游/虫主句先行（富营湖/河口带次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("SLM", "NEW_TEMPLATE_CANDIDATE", FS,
    "真形三步 habitat->forage->洪泛槽尾：BAS 形状第 2 实证（RB-1 单成员 PROV 提案升 2 成员——related_proposal=HRQ-RB1-02；herbivore highly dependent on floodplains 原文级绑定）",
    rel="HRQ-RB1-02")
add("SSM", "NEW_TEMPLATE_CANDIDATE", FF, "真形两步 forage->habitat：鱼/虾/鱿主句先行（礁相关洄游带次之）——RB-1 FF 提案形状", rel="HRQ-RB1-02")
add("STS", "MERGE_CONFIDENT", NO, "深礁底板->低光槽：canonical 同构（S7 夜行 story 原文+深礁 30-358m）")
add("TGS", "MERGE_CONFIDENT", NO, "洪泛主河道底板->低光槽：canonical 同构（S7 夜行 story 原文+demersal/夜间活跃 CSV）")
add("WS2", "MERGE_CONFIDENT", GC,
    "GATE_ZONE 底层->分级鱼食场：canonical 同构（RB-1 WST 真形同种复用——品系先例；WS2↔WST Cross-Batch 去重联动第 2 例）",
    ru="reused_from=CENSUS-REBUILD-001:P-RB1-WST-BAKE（同种品系复用）")

assert len(V) == 94, len(V)


def op_class(step):
    op = step["op"]
    if op.startswith("GATE"):
        return "GATE"
    if op == "APPLY_DYNAMIC_SPATIAL_SLOT":
        return "SLOT"
    if "FOOD_FIELD" in op or "CONCENTRATION" in op:
        return "EVAL_FIELD"
    if "GAUGE" in op:
        return "EVAL_GAUGE"
    return "EVAL"


def body_signature(body):
    return [op_class(s) for s in body["surface_owned_logic"]["ordered_steps"]]


def main():
    bodies = [json.loads(l) for l in open(os.path.join(OUT, "blind_programs.jsonl"), encoding="utf-8")]
    reg_path = os.path.join(CEN, "template_registry.yaml")
    reg_hash_before = hashlib.sha256(open(reg_path, "rb").read()).hexdigest()[:16]
    _ = yaml.safe_load(open(reg_path, encoding="utf-8"))
    assert hashlib.sha256(open(reg_path, "rb").read()).hexdigest()[:16] == reg_hash_before

    tests = []
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stats = dict(MERGE_CONFIDENT=0, TEMPLATE_EXTENSION_CANDIDATE=0, NEW_TEMPLATE_CANDIDATE=0, AMBIGUOUS_NEEDS_EXPANSION=0)
    for b in sorted(bodies, key=lambda x: x["species_id"]):
        sid = b["species_id"]
        sig = body_signature(b)
        v = V[sid]
        raw = [tid for tid, c in CANON.items() if sig == c["sig"]]
        engine_raw_diffs = []
        if v["target"] in CANON and sig != CANON[v["target"]]["sig"]:
            engine_raw_diffs.append("signature mismatch vs %s canonical" % v["target"])
        if v["verdict"] != "MERGE_CONFIDENT":
            engine_raw_diffs.append("no live registry family matches derived truth signature")
        moved = None
        if v["moved_from"]:
            moved = "%s -> %s（STRUCTURAL_DIFF=步数/ORDER——真形序与所在族 canonical 不符）" % (v["moved_from"], v["target"])
        tests.append(dict(
            test_id="MT-RB2-%s" % sid,
            program_id=b["program_id"], species_id=sid,
            rs1_current_family=RS1_MEMBERSHIP.get(sid),
            signature=sig,
            engine_raw_same_signature_families=raw,
            engine_raw_diffs=engine_raw_diffs,
            verdict=v["verdict"],
            target_family=v["target"],
            same=v["verdict"] == "MERGE_CONFIDENT",
            param_only=[],
            structural_diffs=[] if v["verdict"] == "MERGE_CONFIDENT" else ["ORDER/步数（vs 全部活族 canonical）"],
            semantic_note=v["note"],
            order_confirm=v["order_confirm"] or None,
            moved_proposal=moved,
            related_proposal=v["related"],
            reused_from=v["reused"],
            human_review_queued=(None if v["verdict"] == "MERGE_CONFIDENT" else "HRQ-RB2-02"),
            order_derivation_status=b["order_derivation"]["status"],
            ts=now,
        ))
        stats[v["verdict"]] += 1
    with open(os.path.join(OUT, "merge_tests.jsonl"), "w", encoding="utf-8") as f:
        for t in tests:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    conf = [t for t in tests if t["order_confirm"]]
    mv = [t for t in tests if t["moved_proposal"]]
    ff = sorted(t["species_id"] for t in tests if t["target_family"] == FF)
    sf = sorted(t["species_id"] for t in tests if t["target_family"] == SF)
    tb = sorted(t["species_id"] for t in tests if t["target_family"] == TB)
    fs = sorted(t["species_id"] for t in tests if t["target_family"] == FS)
    report = dict(
        batch=BATCH, generated_at=now,
        registry_version="v9 (read-only; zero mutation this batch)",
        n_truth_bodies=len(bodies),
        verdicts=stats,
        order_provisional_confirmations=dict(
            n=len(conf),
            families=sorted({(t["rs1_current_family"]) for t in conf}),
            members=sorted(t["species_id"] for t in conf),
            note="MC 成员真形序=所在族 canonical 序——order_provisional 清零提案证据（v10 降级待独立审，registry 零改动纪律）",
        ),
        family_move_proposals=dict(
            n=len(mv),
            moves={t["species_id"]: t["moved_proposal"] for t in mv},
            filter_field_vacate="FILTER_FIELD_ACCUMULATE_CHAIN 移空（BHC/HER 出族后 0 成员）——空置提案（PATCH VACATED 先例）挂 HRQ-RB2-01",
        ),
        related_rb1_proposals=dict(
            FORAGE_FIRST=ff, SPACE_FIRST=sf, GATE_SUBSTRATE_TEMPBAND=tb, HABITAT_FORAGE_FLOODSLOT=fs,
            note="RB-1 新族提案形状扩充证据（不在 registry v9 活族——NEW 轨+related_proposal=HRQ-RB1-02）；本批 distinct 新族=0（无 RB-1 六提案外新形状）",
        ),
        same_fish_reconciliation=dict(
            reused_same_face=17, reused_same_species_strain=1, same_fish_diff_face=dict(RBP="RB-1=摄食面/本批=护卵面——独立记账"),
            in_batch_dedup=["JSB<->ASB（同 URL 同种——真形同体）", "AGC<->GRB（同种品系）"],
            conflicts=0,
        ),
        revision="REV-RB2-001（BHC/HER return_type 契约修正——program_revisions.jsonl）",
    )
    with open(os.path.join(OUT, "engine_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))
    print("order_confirm:", len(conf), "moves:", len(mv))
    print("FF", len(ff), "SF", len(sf), "TB", len(tb), "FS", len(fs))


if __name__ == "__main__":
    main()
