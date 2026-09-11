# -*- coding: utf-8 -*-
"""CENSUS-B6 盲程序骨架生成器（盲纪律：template_registry.yaml 未开——程序体冻结前不读 registry 本体）。

47 条冻结 Story（FISH-R10 全库收官批，FR3 CLOSED；packet + 逐鱼 story 快照见
input_snapshots/；R10 为压缩模板批：正文节=Reality Baseline/FCF Interpretation
（部分省略）/Evidence/Verdict/Sweep Surface Log，十节契约压缩已由 FR 线
FISH-R10-FIX-001 F-B 声明处置）。骨架从 Story 正文独立推写；语义输入=P01/P04/P05
pattern 页（B3 input_snapshots 同 URL 冻结快照复用——P04 契约『守巢/护幼状态在
Presentation 前存在且持续；当前目标可同时触发摄食与关系冲突路径』；P05 洞见
『停食→P05 状态抑制 Feeding Path，不落 P04』；R10 停食判例族分支化=FR3 关系
证实→P04 语境（狼鱼护卵首例）/未证实→P05）；P02=ResourcePatch 背景语义
（AGC/SLM story FR 冻结解释承载，无独立快照，B5 RHM/RBP 同型）。
hash: sha256(canonical_json(record minus blind_hash))[:16]

【B6-F-0 类偏差注记（bias_declaration 同文）】本会话盲段加载流程管线时读过 B5 的
build_blind_programs.py / build_stories.py（B5 104 条盲体的 SINGLE 链与 TYPED/guard
形态 op 名层面）与 B5 batch_report/worker_self_qa（族名与计数散文）；角色记忆 v5
亦含各族散文描述与 B0-B4/RS1/RP1/B5 判例。template_registry.yaml 本体（v8）在盲
冻结前未读。缓解：本批 94 条 sketch 严格从 47 份 Story 压缩正文 + P01/P04/P05
冻结 pattern 页独立推写，每条含顺序推导注记（正文有判断顺序的反映顺序）；P04
2 例按契约拓扑（PARALLEL_SET 依据=契约文本）非按 registry 形状；未按 registry
形状定制。

【盲体语汇纪律（B5 F4 判例，本批强制执行）】盲 sketch/premise/open_semantics
只描述观察到的行为结构——不携带 extension/新轴/anchor 轴值提案等判同段框架
语汇（判同提案只出现在判同产物 merge_tests/HRQ）。守护对象以行为事实描述
（『雄鱼守护卵块直至孵化』/『卵产于双壳贝体内并在贝内发育』），不预写轴名。

【顺序推导纪律（authoring_work_standards §5.1）】47 Story 逐条顺序扫描结论：
- 无一 Story 正文描述面内 early-return 判断链（分级命中 if/elif/else 型）；
  压缩模板正文均为静态食性/栖息陈述+引文，无先判什么后判什么的次序描述。
- 出现的先后序均为 lifecycle/洄游/昼夜/ontogeny/guard 期——ATC 溯河/BMB 半溯河/
  SSM 礒相关洄游/PSH+PRB potamodromous/ASB 降海+雄先熟性转换/BLT potamodromous/
  WS2+HYS 飼系溯河复用/EUP 12cm 起鱼食+日出日落捕食峰/BCF+TGS+BBH+STS 夜行或
  夜摄/ASB 幼浮游→成鱼虾/RUF 沿海鱼食分化/AWF 护卵期雄鱼几乎不食——按 B3 判例④
  记 premise 配置级 position 绑定，不是面内 ordered branch。
- AWF 护卵停食按 FR3 R10 关系证实分支=P04 语境（护卵期能量分配代价）记 guard
  premise 注记（P05 停食判例族联动 open 留判同段），不立面内分支。
"""
import hashlib
import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent
P = "https://app.notion.com/p/3d7a4137d23681"
U = {
    "SUK": P + "5bb5e3d2ec6c3b2869", "GRK": P + "4cb047ec23773a0918",
    "KHK": P + "6b9ba1da26d9c78d6e", "OGK": P + "1c99f6c347abaaef5c",
    "LCP": P + "5b80c2e23dac3be7eb", "AMC": P + "8892c9c5f1c0e4533e",
    "HFC": P + "06b433ff866961c095", "ASC": P + "cf900cddc64a083bba",
    "WCC": P + "b8b0f8e4e1fc824257", "AGC": P + "bf8602d799373dddd6",
    "WS2": P + "1b8160d0dfb297f56e", "WAG": P + "c39446dde48c078624",
    "HYS": P + "4999ecf8b16a4ed86b", "ACA": P + "1c82e5d1d02f4e8a22",
    "ATC": P + "739eaed37a4668f426", "AWF": P + "c096bed186d4eb6ee7",
    "PSH": P + "c4a80ac9828df1bb19", "LFB": P + "468d6df2df98d42556",
    "BMB": P + "a09856e09c85eaa548", "PLC": P + "70847be36f0c3a2da9",
    "SSM": P + "e892d4d8a4c4cfc9bb", "CGD": P + "cd95fbe74a22d1d9db",
    "GDB": P + "9f9475d1766007ccc8", "RBD": P + "fca30dedac6ddd2856",
    "RUF": P + "84808aee1ee2529b3c", "DBC": P + "25831fc171a2e93c58",
    "JSB": P + "71bc75ef7259f75789", "ASB": P + "23b84bdfcad0c1fd77",
    "DCL": P + "31a6bff4842e29faa8", "BHM": P + "c684c8dc87df817137",
    "WHC": P + "6388a9dab075a2efbb", "PRB": P + "4da518f55de491fd74",
    "RSS": P + "199170c957a1741514", "PCC": P + "a78225d1bacd38b1ca",
    "STS": P + "9b81d5fcdcf8285451", "PKC": P + "93b009c192b068fc3c",
    "BCF": P + "db944efd760f8ebe94", "TGS": P + "65b516fa5f44d871b5",
    "EUP": P + "de813bf105de96e004", "BTS": P + "018e8fec8281f1f43e",
    "GDS": P + "44a875d04ceaa100e4", "SLM": P + "98a8b6d0e5b23c89b5",
    "PKS": P + "2a9616e679fd88e54e", "BLT": P + "0495c2c7c9ae82ee73",
    "RSC": P + "c6b5c2ff8c9dae1d60", "BBH": P + "07b563fefd977c8ef5",
    "AMN": P + "cea7a7de48ed603f54",
}
SP = {
    "SUK": "Shiro Utsuri Koi", "GRK": "Goromo Koi", "KHK": "Kohaku Koi",
    "OGK": "Ogon Koi", "LCP": "Leather Carp", "AMC": "Albino Mirror Carp",
    "HFC": "Human Face Scale Carp", "ASC": "Albino Scale Carp",
    "WCC": "White Channel Catfish", "AGC": "Albino Grass Carp",
    "WS2": "White Sturgeon 02", "WAG": "White Alligator Gar",
    "HYS": "Hybrid Sturgeon", "ACA": "Amur Catfish",
    "ATC": "Atlantic Tomcod", "AWF": "Atlantic Wolffish",
    "PSH": "Paroon Shark", "LFB": "Largefin Bitterling",
    "BMB": "Bulatmai Barbel", "PLC": "Pale Chub",
    "SSM": "Serra Spanish Mackerel", "CGD": "Common Gudgeon",
    "GDB": "Guangdong Bream", "RBD": "Rainbow Darter",
    "RUF": "Ruffe", "DBC": "Darkbarbel Catfish",
    "JSB": "Japanese Seabass", "ASB": "Asian Seabass",
    "DCL": "Decoris Labeo", "BHM": "Bullhead Minnow",
    "WHC": "White Catfish", "PRB": "Piraiba",
    "RSS": "Redspotted Sunfish", "PCC": "Pencil Catfish",
    "STS": "Swallowtail Seaperch", "PKC": "Pike Cichlid",
    "BCF": "Blue Catfish", "TGS": "Tiger Sorubim",
    "EUP": "European Perch", "BTS": "Blacktail Shiner",
    "GDS": "Golden Shiner", "SLM": "Silver Mylossoma",
    "PKS": "Pumpkinseed", "BLT": "Bull Trout",
    "RSC": "Ripsaw Catfish", "BBH": "Brown Bullhead",
    "AMN": "Amur Minnow",
}
S = {k: f"CENSUS-B6-{k}" for k in U}

ORDER_NOTE = "顺序推导注记"


def rec(pid, story, surface, premises, sketch, steps, branches, combine,
        return_type, profile, confidence=None, open_sem=None):
    r = {"program_id": pid, "story_id": S[story], "species_id": story,
         "surface": surface, "incoming_premises": premises,
         "human_readable_sketch": sketch, "ordered_steps": steps,
         "branches": branches, "combine": combine, "return_type": return_type,
         "instance_noise": {"species": SP[story], "profile": profile,
                            "constants": {}},
         "helpers": [], "source_evidence_ids": [U[story]],
         "open_semantics": open_sem or []}
    if confidence:
        r["confidence"] = confidence
    return r


def bake_single(story, prem, sketch, profile, opn=None):
    return rec(f"P-B6-{story}-BAKE", story, "Bake", prem, sketch,
               [{"op": "EVAL_HABITAT_FACTOR_POSITION", "deps": []},
                {"op": "NORMALIZE_WEIGHT", "deps": [0]}],
               [], "NONE_SINGLE_CHAIN", "SpatialDistributionWeight", profile,
               open_sem=opn)


def resp_typed(story, prem, sketch, profile, conf=None, opn=None):
    return rec(f"P-B6-{story}-RESP", story, "Response", prem, sketch,
               [{"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
                {"op": "DECIDE_RESPONSE", "deps": [0]}],
               [], "NONE", "Response(TargetFeeding)", profile,
               confidence=conf, open_sem=opn)


def resp_guard(story, prem, sketch, guard_note, profile, conf=None, opn=None):
    """P04 guard 双 Path：守护状态 pre-existing/persistent（契约）；
    目标同时可触发摄食 Path 与关系冲突 Path（PARALLEL_SET——契约明确同时，无序）；
    COMBINE 后统一决策。守护对象/参与者/期间行为以观察到的行为事实记
    premise + open_semantics（顺序推导注记：守护期间行为与参与者差异非新增
    branch/gate——拓扑保持 P04 契约并行双 Path，差异留判同阶段裁决）；
    不预写任何判同段框架语汇（盲体语汇纪律）。"""
    steps = [
        {"op": "EVAL_TARGET_AS_FOOD_TYPED", "deps": []},
        {"op": "EVAL_NEST_INTRUDER_RELATION", "deps": []},
        {"op": "COMBINE_CONFLICT_AWARE", "deps": [0, 1]},
        {"op": "DECIDE_RESPONSE", "deps": [2]},
    ]
    sketch_full = (sketch + "｜守护面=" + guard_note +
                   "｜Path 结构：摄食 Path ∥ 关系冲突 Path（PARALLEL_SET，P04 契约"
                   "『当前目标可同时触发摄食与关系冲突路径』）→ 冲突感知合并 → 统一响应决策"
                   "（§9.2 one-program-multi-path：不拆两 Mode supply）")
    return rec(f"P-B6-{story}-RESP", story, "Response", prem, sketch_full,
               steps, [], "DUAL_PATH_CONFLICT_AWARE",
               "Response(TargetFeeding | RelationalConflict)", profile,
               confidence=conf, open_sem=opn)


PROGRAMS = [
    # ================= 品系/杂交身份层 13（ROW01-13） =================
    # ---------------- SUK 四白锦鲤 ----------------
    bake_single(
        "SUK",
        ["strain_reuse = 锦鲤 R03 品系复用（Identity Deferred——品系外观/养殖条件"
         "不构成机制差异）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（锦鲤先例复用承载）。" + ORDER_NOTE + "：品系行正文无时序"
        "无判断链（S1-S11 全面 SN）。单因子链。",
        "KoiStrainDefault"),
    resp_typed(
        "SUK",
        ["strain_reuse = 锦鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 锦鲤先例机制复用承载）。" + ORDER_NOTE +
        "：无判断顺序描述（品系复用）。",
        "KoiStrainTyped",
        conf="Low"),
    # ---------------- GRK 圆点五色锦鲤 ----------------
    bake_single(
        "GRK",
        ["strain_reuse = 锦鲤 R03 品系复用（Identity Deferred）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（锦鲤先例复用承载）。" + ORDER_NOTE + "：同 SUK——无时序"
        "无判断链。单因子链。",
        "KoiStrainDefault"),
    resp_typed(
        "GRK",
        ["strain_reuse = 锦鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序描述。",
        "KoiStrainTyped",
        conf="Low"),
    # ---------------- KHK 红白锦鲤 ----------------
    bake_single(
        "KHK",
        ["strain_reuse = 锦鲤 R03 品系复用（Identity Deferred）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（锦鲤先例复用承载）。" + ORDER_NOTE + "：同 SUK——无时序"
        "无判断链。单因子链。",
        "KoiStrainDefault"),
    resp_typed(
        "KHK",
        ["strain_reuse = 锦鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序描述。",
        "KoiStrainTyped",
        conf="Low"),
    # ---------------- OGK 橙黄金锦鲤 ----------------
    bake_single(
        "OGK",
        ["strain_reuse = 锦鲤 R03 品系复用（Identity Deferred）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（锦鲤先例复用承载）。" + ORDER_NOTE + "：同 SUK——无时序"
        "无判断链。单因子链。",
        "KoiStrainDefault"),
    resp_typed(
        "OGK",
        ["strain_reuse = 锦鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序描述。",
        "KoiStrainTyped",
        conf="Low"),
    # ---------------- LCP 无鳞鲤 ----------------
    bake_single(
        "LCP",
        ["strain_reuse = 镜鲤 R03 品系复用（Identity Deferred）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（镜鲤先例复用承载）。" + ORDER_NOTE + "：无时序无判断链。"
        "单因子链。",
        "MirrorStrainDefault"),
    resp_typed(
        "LCP",
        ["strain_reuse = 镜鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序描述。",
        "MirrorStrainTyped",
        conf="Low"),
    # ---------------- AMC 镜鲤白化 ----------------
    bake_single(
        "AMC",
        ["strain_reuse = 镜鲤 R03 品系复用（Identity Deferred）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（镜鲤先例复用承载）。" + ORDER_NOTE + "：无时序无判断链。"
        "单因子链。",
        "MirrorStrainDefault"),
    resp_typed(
        "AMC",
        ["strain_reuse = 镜鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序描述。",
        "MirrorStrainTyped",
        conf="Low"),
    # ---------------- HFC 鳞鲤人面鲤 ----------------
    bake_single(
        "HFC",
        ["strain_reuse = 鳞鲤 R03 品系复用（Identity Deferred）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（鳞鲤先例复用承载）。" + ORDER_NOTE + "：无时序无判断链。"
        "单因子链。",
        "ScaleStrainDefault"),
    resp_typed(
        "HFC",
        ["strain_reuse = 鳞鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序描述。",
        "ScaleStrainTyped",
        conf="Low"),
    # ---------------- ASC 鳞鲤白化 ----------------
    bake_single(
        "ASC",
        ["strain_reuse = 鳞鲤 R03 品系复用（Identity Deferred）",
         "habitat = 静水养殖鲤系（品系先例）"],
        "鲤品系静态栖息（鳞鲤先例复用承载）。" + ORDER_NOTE + "：无时序无判断链。"
        "单因子链。",
        "ScaleStrainDefault"),
    resp_typed(
        "ASC",
        ["strain_reuse = 鳞鲤 R03 复用（Identity Deferred）"],
        "鲤系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序描述。",
        "ScaleStrainTyped",
        conf="Low"),
    # ---------------- WCC 白化叉尾鮰 ----------------
    bake_single(
        "WCC",
        ["strain_reuse = 叉尾鮰 B01 品系复用（Identity Deferred）",
         "habitat = 泥底潭沼（亲本先例）"],
        "叉尾鮰白化品系栖息复用（B01 先例承载）。" + ORDER_NOTE + "：无时序无判断"
        "链。单因子链。",
        "ChannelStrainDefault"),
    resp_typed(
        "WCC",
        ["strain_reuse = 叉尾鮰 B01 复用（Identity Deferred）"],
        "叉尾鮰系杂食 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序"
        "描述。",
        "ChannelStrainTyped",
        conf="Low"),
    # ---------------- AGC 白化草鱼 ----------------
    bake_single(
        "AGC",
        ["strain_reuse = 草鱼 B01 品系复用（Identity Deferred）",
         "habitat = 大江河湖+洪泛植被区（亲本 grazing 联系——P02 背景语义由"
         "story FR 解释承载）"],
        "草鱼白化品系栖息复用（B01 先例承载）。" + ORDER_NOTE + "：无时序无判断"
        "链。单因子链。",
        "GrassStrainDefault"),
    resp_typed(
        "AGC",
        ["strain_reuse = 草鱼 B01 复用（Identity Deferred）",
         "grazing_context = 草食 grazing 型摄食（P02 资源面背景——B5 RHM/RBP"
         " 同型承载）"],
        "草食 grazing typed 摄食响应（P01+P02 复用）。" + ORDER_NOTE + "：无判断"
        "顺序描述。",
        "GrassStrainTyped",
        conf="Low"),
    # ---------------- WS2 白化高首鲟 ----------------
    bake_single(
        "WS2",
        ["strain_reuse = 高首鲟 R09 品系复用（Identity Deferred——与 B5 WST"
         " 同种 Acipenser transmontanus，同 URL 同源）",
         "lifecycle = 巨型溯河（亲本先例，P05）"],
        "高首鲟白化品系栖息复用（R09 WST 先例承载）。" + ORDER_NOTE + "：溯河为"
        " lifecycle premise 配置级，无面内判断链。单因子链。",
        "SturgeonStrainDefault"),
    resp_typed(
        "WS2",
        ["strain_reuse = 高首鲟 R09 复用（Identity Deferred）",
         "lifecycle = 溯海-河（P05 premise）"],
        "鲟系体型分级鱼食 typed 摄食响应（P01+P05 复用）。" + ORDER_NOTE + "：无"
        "判断顺序描述。",
        "SturgeonStrainTyped",
        conf="Low"),
    # ---------------- WAG 白金火箭（鳄雀鳝白化） ----------------
    bake_single(
        "WAG",
        ["strain_reuse = 鳄雀鳝 B01 品系复用（Identity Deferred）",
         "habitat = 缓流植被（亲本先例）"],
        "鳄雀鳝白化品系栖息复用（B01 先例承载）。" + ORDER_NOTE + "：无时序无判断"
        "链。单因子链。",
        "GarStrainDefault"),
    resp_typed(
        "WAG",
        ["strain_reuse = 鳄雀鳝 B01 复用（Identity Deferred）"],
        "雀鳝系伏击 typed 摄食响应（P01 复用）。" + ORDER_NOTE + "：无判断顺序"
        "描述。",
        "GarStrainTyped",
        conf="Low"),
    # ---------------- HYS 杂交鲟 ----------------
    bake_single(
        "HYS",
        ["hybrid_reuse = 杂交飼（A. schrenckii × H. daurus，库锚即杂交式学名）"
         "复用飼系 P01+P05（Identity Deferred，判例第 3 例）",
         "lifecycle = 飼系底栖+洄游（亲本先例）"],
        "杂交鲟栖息复用（飼系先例承载）。" + ORDER_NOTE + "：无时序无判断链"
        "（S8 MSF=飼系底栖）。单因子链。",
        "HybridSturgeonDefault",
        opn=["杂交身份裁决归 FR 线（Identity Deferred）；库锚即杂交式学名无独立"
             "物种页"]),
    resp_typed(
        "HYS",
        ["hybrid_reuse = 飼系 P01+P05 复用（Identity Deferred）"],
        "飼系 typed 摄食响应（P01+P05 复用）。" + ORDER_NOTE + "：无判断顺序"
        "描述。",
        "HybridSturgeonTyped"),
    # ================= 普通层 34（ROW14-47） =================
    # ---------------- ACA 土鲶 ----------------
    bake_single(
        "ACA",
        ["habitat = 河湖（『河湖』S8 MSF）",
         "nocturnal = 夜行（S7 EO 同属推断——巨鲶 R06 同属夜行鲶系）"],
        "河湖分布+夜行。 " + ORDER_NOTE + "：夜行为昼夜时窗 premise 配置级，无"
        "面内判断链。单因子链。",
        "AmurCatfishRiver"),
    resp_typed(
        "ACA",
        ["congener_ref = Silurus asotus 与欧洲巨鲶 R06 同属第 2 例（『Adults "
         "feed on all types of fish』全鱼食引文）",
         "nocturnal = 夜行伏击 typed context（同属 S7 EO 推断）"],
        "鱼食夜行伏击 typed 摄食响应（P01——巨鲶 R06 同构）。" + ORDER_NOTE +
        "：伏击无判断顺序描述（夜行=时窗 premise）。",
        "SilurusNightAmbush",
        opn=["夜行 S7 EO 同属推断（引文闭合前 High 主张由同属结构承载）"]),
    # ---------------- ATC 大西洋小鳕 ----------------
    bake_single(
        "ATC",
        ["lifecycle = anadromous 溯河（P05 premise）",
         "habitat = 沿岸/咸淡水（S8 MSF）"],
        "沿岸/咸淡水分布+溯河洄游。" + ORDER_NOTE + "：溯河为 lifecycle premise"
        " 配置级，无面内判断链。单因子链。",
        "TomcodCoastAnadromous"),
    resp_typed(
        "ATC",
        ["diet = 小型底栖食（『feed mostly on small crustaceans, especially "
         "shrimps and amphipods; also worms, small mollusks, squids and "
         "fishes』）"],
        "小型底栖食 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述"
        "（鳕科微型）。",
        "TomcodBenthivore"),
    # ---------------- AWF 大西洋狼鱼 ----------------
    bake_single(
        "AWF",
        ["habitat = 岩底 18-110m（『rocky bottoms』S8 MSF）"],
        "岩底分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "WolffishRockBottom"),
    resp_guard(
        "AWF",
        ["guard_condition = 雄鱼持续守护卵块直至孵化（『Males guard a clutch "
         "of eggs right up to the time of hatching』——守护持续至孵化时刻，"
         "P04 契约 pre-existing/persistent）",
         "guard_object = 卵块（雄鱼单亲守护）",
         "fasting_during_guard = 护卵期雄鱼几乎不进食（『the male hardly "
         "feeds』——护卵期持续状态；FR3 R10 关系证实分支=P04 语境（护卵期"
         "能量分配代价），停食判例族语境从洄游扩展到护卵）",
         "shell_tool = 硬壳碾压齿系（『hard-shelled mollusks, crabs, lobsters, "
         "sea urchins』——碾压摄食 typed context，狼鱼科特殊齿系）"],
        "岩底硬壳碾压 typed 摄食（软体/蟹/龙虾/海胆等+鱼）+ 雄鱼护卵块守护：对"
        "硬壳目标摄食 Path ∥ 对卵块的威胁评估 Path。" + ORDER_NOTE + "：碾压摄食"
        "无判断顺序描述（硬壳 typed 单 evaluator）；守护按 P04 契约并行双 Path；"
        "护卵期停食为 guard 期持续状态注记（P05 停食判例族语境扩展——洄游型停食"
        "4 例 vs 护卵型本例的关系证实分支由 FR3 裁定，census 不预裁结构差异）。",
        "雄鱼守护卵块直至孵化+护卵期几乎不进食（硬壳碾压 typed 摄食并行）",
        "WolffishHardShellGuarder",
        opn=["护卵停食语境（P04 guard 期）与洄游停食语境（P05 状态抑制 4 例）的"
             "判例族关系=Story Open Question（FR3 relation 证实→P04 分支已裁，"
             "语义域扩展留 review）；狼鱼科碾压齿系 R04 条纹狼鱼同型孤例注记"]),
    # ---------------- PSH 大青鲨（名实分离） ----------------
    bake_single(
        "PSH",
        ["lifecycle = potamodromous 河湖洄游（P05 premise）",
         "habitat = 大河（S8 MSF）"],
        "大河分布+河湖洄游。" + ORDER_NOTE + "：洄游为 lifecycle premise 配置级，"
        "无面内判断链。单因子链。",
        "ParoonRiverGiant"),
    resp_typed(
        "PSH",
        ["diet = 鱼食巨型鲶（『Both young and adults feed on fishes and "
         "crustaceans』+大型个体食病殍）",
         "naming = 名实分离（中文名『大青鲨』错位——Paroon Shark 鲶科非鲨；库锚"
         "学名 Pangasius sanitwongsei 从，学名明确有效非 Identity Deferred）"],
        "巨型鱼食 typed 摄食响应（P01——幼成同食性）。" + ORDER_NOTE + "：无判断"
        "顺序描述（幼-成 S9 MSF 同食性）。",
        "ParoonApexPiscivore",
        opn=["CR 保护边界=OPS 产品面排除；病殍食腐注记（大型个体）为食性 breadth"
             " 记录非程序分支"]),
    # ---------------- LFB 大鳍𫚪 ----------------
    bake_single(
        "LFB",
        ["habitat = 河湖（S8 MSF）"],
        "河湖分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "BitterlingRiverLake"),
    resp_guard(
        "LFB",
        ["guard_condition = 繁殖依赖贝宿主：雌鱼产卵管将卵产于双壳贝体内，幼鱼"
         "留在贝内直至能游泳（『Female has an ovipositor which is used to "
         "deposit eggs inside bivalves』+『Young remain in the bivalve until "
         "they can swim』——贝内卵幼持续期，鳑鲏 R03 先例第 2 例）",
         "guard_object = 贝体内卵/幼（贝=繁殖对象依赖关系）",
         "diet = 低营养杂食（trophic 2.0 推算——食性细节 EO）"],
        "低营养杂食 typed 摄食（trophic 2.0 推算承载）+ 贝宿主繁殖关系：对食物"
        "目标摄食 Path ∥ 对贝宿主/卵幼的威胁评估 Path。" + ORDER_NOTE + "：杂食"
        "无判断顺序描述；贝宿主关系按鳑鲏 R03 先例（P04 契约并行双 Path）；贝为"
        "繁殖对象依赖（Relation Object 语义，story FR 层明言）非独立捕食/资源"
        "程序。",
        "卵产于双壳贝体内+幼贝内发育（产卵管；鳑鲏 R03 先例第 2 例）",
        "MusselBroodBitterling",
        conf="MEDIUM",
        opn=["食性细节 EO（trophic 2.0 推算）——引文闭合前 MEDIUM；贝宿主可用性"
             "是否构成通域遇鱼条件=Story Open Question（FR 层已裁『不扩』，Representation"
             " 层留判断）"]),
    # ---------------- BMB 大鳞鲃 ----------------
    bake_single(
        "BMB",
        ["lifecycle = 半溯河 semi-anadromous（海+河口+河流，P05 premise）",
         "habitat = 海/河口/河（S8 MSF）"],
        "海-河口-河分布+半溯河。" + ORDER_NOTE + "：洄游为 lifecycle premise 配置"
        "级，无面内判断链。单因子链。",
        "BarbelSemiAnadromous"),
    resp_typed(
        "BMB",
        ["diet = 杂食（无脊椎/藻/腐屑/小鱼）",
         "spawn = 沙砂强流产卵（lifecycle premise）"],
        "杂食 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述。",
        "BarbelOmnivore",
        opn=["V 保护边界=OPS 产品面排除"]),
    # ---------------- PLC 宽鳍𫚭 ----------------
    bake_single(
        "PLC",
        ["habitat = 急流（S8 MSF——马口鱼系同构）"],
        "急流分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "PaleChubRiffle"),
    resp_typed(
        "PLC",
        ["diet = 杂食（『Feed on zooplankton, small crustaceans, macroscopic "
         "algae, small fish and detritus』）"],
        "急流杂食 typed 摄食响应（P01——马口鱼系同构）。" + ORDER_NOTE + "：无判断"
        "顺序描述。",
        "RiffleOmnivore"),
    # ---------------- SSM 巴西马鲛 ----------------
    bake_single(
        "SSM",
        ["lifecycle = oceanodromous 礁相关洄游（P05 premise）",
         "habitat = 礁相关（S8 MSF）"],
        "礁相关海域分布+洄游。" + ORDER_NOTE + "：洄游为 lifecycle premise 配置级，"
        "无面内判断链。单因子链。",
        "MackerelReefOceanodromous"),
    resp_typed(
        "SSM",
        ["congener_ref = 马鲛系第 3 例（Scomberomorus 属——康氏马鲛 B5 SPM 同属）",
         "diet = 鱼食为主（『Feeds largely on fishes, with smaller quantities "
         "of penaeid shrimps and loliginid cephalopods』）"],
        "马鲛系鱼食 typed 摄食响应（P01+P05 同构）。" + ORDER_NOTE + "：无判断顺序"
        "描述。",
        "MackerelPiscivore"),
    # ---------------- CGD 常见鮈鱼 ----------------
    bake_single(
        "CGD",
        ["habitat = 沙底急流（S8 MSF）"],
        "沙底急流分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子"
        "链。",
        "GudgeonSandRiffle"),
    resp_typed(
        "CGD",
        ["diet = 小型底栖（『Feeds on insect larvae, mollusks, and "
         "crustaceans』）",
         "schooling = 沙底急流群游（S3 MSF——群结构事实非互斥供给主张）"],
        "沙底小型底栖 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述；"
        "群游为群结构事实（S3 记录，非程序面）。",
        "SandBenthivore"),
    # ---------------- GDB 广东鲂 ----------------
    bake_single(
        "GDB",
        ["habitat = 河川（S8 MSF）"],
        "河川分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "BreamRiver"),
    resp_typed(
        "GDB",
        ["congener_ref = 鲂系同属推算（Megalobrama——团头鲂 R05 先例第 2 例；"
         "食性未述 trophic 3.3 同属推算）"],
        "鲂系食性同属推算 typed 摄食响应（P01——团头鲂先例）。" + ORDER_NOTE +
        "：无判断顺序描述（S1 EO 同属推算）。",
        "BreamCongeneric",
        conf="MEDIUM",
        opn=["食性 S1 EO 同属推算——引文闭合前 MEDIUM"]),
    # ---------------- RBD 彩虹镖鲈 ----------------
    bake_single(
        "RBD",
        ["habitat = 急流砂礫濑（『fast gravel and rubble riffles』S8 MSF——"
         "镖鲈科首例 darter 型微底栖）"],
        "急流砂礫濑分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单"
        "因子链。",
        "DarterRiffleMicro"),
    resp_typed(
        "RBD",
        ["diet = 水生虫幼+鱼卵（『Feed on midge larvae, hydropsychid and "
         "hydroptilid caddisfly larvae, mayfly nymphs, and fish eggs』）",
         "spawn = 产卵埋入底质（S6 MSF——产卵行为变量非守护，story FR 层明言）"],
        "急流微底栖 typed 摄食响应（P01——镖鲈科首例）。" + ORDER_NOTE + "：无判断"
        "顺序描述；卵埋底质为产卵行为（lifecycle premise），非持续守护状态"
        "（story FR 层明言产卵行为变量非 guard）。",
        "DarterMicroBenthivore",
        opn=["镖鲈科体型/流速转化或有独立 Grain 需求=Story Open Question"
             "（无证据，Representation 层留判断）"]),
    # ---------------- RUF 梅花鲈 ----------------
    bake_single(
        "RUF",
        ["habitat = 富营湖/河口（S8 MSF）"],
        "富营湖-河口分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。"
        "单因子链。",
        "RuffeEutrophicLake"),
    resp_typed(
        "RUF",
        ["diet = 浮游/虫/鱼（『feeds on zooplankton, chironomids, "
         "oligochaetes and amphipods』+沿海鱼食）",
         "coastal_shift = 沿海个体鱼食（S9 MSF——生境分化记录）",
         "invasive = 入侵种（供给注记——OPS 层，非程序面）"],
        "富营湖底栖 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述；"
        "沿海鱼食为生境分化记录（S9）非程序分支。",
        "RuffeBenthivore",
        opn=["入侵种供给语义=OPS 层（同 B5 CSL 入侵判例）"]),
    # ---------------- DBC 江黄颡 ----------------
    bake_single(
        "DBC",
        ["habitat = 栖息未述（同属推算河川底栖——S8 EO）"],
        "同属推算栖息（黄颡鱼系）。" + ORDER_NOTE + "：静态栖息推算，无时序无判断"
        "链。单因子链。",
        "BagridCongeneric"),
    resp_typed(
        "DBC",
        ["congener_ref = 黄颡鱼 R03 同属推算（Tachysurus/Pelteobagrus 系；"
         "食性/栖息未详 trophic 3.7 同属推算）"],
        "黄颡鱼系食性同属推算 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断"
        "顺序描述（S1/S8 双 EO 同属推算）。",
        "BagridCongenericTyped",
        conf="MEDIUM",
        opn=["食性+栖息双 EO 同属推算——引文闭合前 MEDIUM；DD 数据缺注记"]),
    # ---------------- JSB 海鲈（同属参照） ----------------
    bake_single(
        "JSB",
        ["habitat = 近岸岩礁（同属参照——S8 MSF 同属推算）"],
        "近岸岩礁分布（同属参照承载）。" + ORDER_NOTE + "：静态栖息，无时序无判断"
        "链。单因子链。",
        "SeabassCongeneric"),
    resp_typed(
        "JSB",
        ["congener_ref = 花鲈属同属参照（maculatus 专项数据薄——历史同物异名，"
         "japonicus 数据承载：杂食性掠食）",
         "dedup = 与 ASB（Asian Seabass=Lateolabrax japonicus）同 URL 同源"
         "引文（Evidence 同指 japonicus 页）——批内同源参照注记"],
        "花鲈属同属参照 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述"
        "（同属参照 S1 EO）。",
        "SeabassCongenericTyped",
        conf="MEDIUM",
        opn=["maculatus 专项数据薄+历史同物异名注记——身份裁决归 FR 线；与 ASB "
             "同 URL 同源（japonicus 页）——去重联动注记（Cross-Batch/批内）"]),
    # ---------------- ASB 海鲈鱼 ----------------
    bake_single(
        "ASB",
        ["lifecycle = catadromous 降海（幼河成海降海产卵——P05 premise；与溯河"
         "系方向对照）",
         "habitat = 近岸岩礁（S8 MSF）+冬季深岩礁产卵位"],
        "近岸岩礁分布+降海洄游。" + ORDER_NOTE + "：降海为 lifecycle premise 配置"
        "级，无面内判断链。单因子链。",
        "SeabassCatadromous"),
    resp_typed(
        "ASB",
        ["diet = 幼浮游→成小鱼虾（ontogeny premise——『Small fish and "
         "shrimps』成鱼）",
         "sex_change = 雄先熟性转换（protandrous——繁殖系统变量 premise 非"
         " Mode；story FR 层明言）",
         "lifecycle = 降海洄游（P05 premise）"],
        "掠食 typed 摄食响应（P01+P05 降海生活史）。" + ORDER_NOTE + "：幼→成"
        "食性转为 ontogeny premise 配置级，无面内判断链；性转换=繁殖系统变量"
        "非程序分支。",
        "CatadromousProtandrousSeabass",
        opn=["降海型与溯河系洄游方向对照=FR 层对照注记（同 P05 premise 值差异）"]),
    # ---------------- DCL 湘华鮈 ----------------
    bake_single(
        "DCL",
        ["habitat = 同属河川底栖（S8 MSF 同属推算——湘华鮈 FishBase 公开版无页，"
         "同属 Hemibarbus labeo 参照）"],
        "同属推算河川底栖。" + ORDER_NOTE + "：静态栖息推算，无时序无判断链。单"
        "因子链。",
        "LabeoCongenericRiffle"),
    resp_typed(
        "DCL",
        ["congener_ref = 同唇䱌系同属推算（Hemibarbus labeo 底栖刮食型——薄"
         "资料同属替代）"],
        "同属推算底栖刮食 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序"
        "描述（S1 EO 薄资料同属推算）。",
        "LabeoCongenericTyped",
        conf="MEDIUM",
        opn=["湘华鮈 FishBase 公开版无页（薄资料）——同属替代承载，引文闭合前 "
             "MEDIUM"]),
    # ---------------- BHM 牛头鲦 ----------------
    bake_single(
        "BHM",
        ["habitat = 静潭沙泥（S8 MSF）"],
        "静潭沙泥分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子"
        "链。",
        "BullheadMinnowPool"),
    resp_typed(
        "BHM",
        ["diet = 虫幼（『They feed on insect immatures』）"],
        "虫幼 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述。",
        "PoolInsectivore",
        conf="MEDIUM"),
    # ---------------- WHC 白鲶鱼 ----------------
    bake_single(
        "WHC",
        ["habitat = 泥底潭沼（S8 MSF）"],
        "泥底潭沼分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子"
        "链。",
        "WhiteCatfishMudPool"),
    resp_typed(
        "WHC",
        ["diet = 杂食（『wide variety of fishes, insects and crustaceans』）",
         "series = 鮰科第 3 例（Ameiurus catus——story 称鲿科第 3 例，科名宽泛"
         "用法注记）"],
        "杂食 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述。",
        "WhiteCatfishOmnivore",
        opn=["story『鲿科』称法与 Ameiurus（Ictaluridae 鮰科）系统分类的科名"
             "宽泛用法注记——非程序面差异"]),
    # ---------------- PRB 短扁口鲶（Piraiba） ----------------
    bake_single(
        "PRB",
        ["lifecycle = potamodromous（P05 premise）",
         "habitat = 河口咸淡水（S8 MSF）"],
        "河口咸淡水分布+河湖洄游。" + ORDER_NOTE + "：洄游为 lifecycle premise"
        " 配置级，无面内判断链。单因子链。",
        "PiraibaEstuaryGiant"),
    resp_typed(
        "PRB",
        ["diet = 鱼食巨型顶级掠食（『Feeds on fish』+猴/人胃含物记录——"
         "大型猎物 breadth 记录）",
         "size = 360cm/200kg 巨型（体型注记非程序分支）"],
        "巨型鱼食 typed 摄食响应（P01——顶级掠食）。" + ORDER_NOTE + "：无判断"
        "顺序描述；猴/人胃含物=猎物谱记录非程序分支。",
        "PiraibaApexPiscivore",
        conf="MEDIUM",
        opn=["P05 洄游 premise（potamodromous）+S1 大型猎物记录——Confidence "
             "Medium 按故事字段携带"]),
    # ---------------- RSS 红斑太阳鱼 ----------------
    bake_single(
        "RSS",
        ["habitat = 静水底（S8 MSF）"],
        "静水底分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子"
        "链。",
        "RedspottedSunfishPool"),
    resp_typed(
        "RSS",
        ["diet = 底栖无脊椎（『Invertebrate feeder. Consumes benthic prey』）",
         "series = 太阳鱼系第 6 例"],
        "底栖无脊椎 typed 摄食响应（P01——太阳鱼系）。" + ORDER_NOTE + "：无判断"
        "顺序描述。",
        "SunfishBenthivore"),
    # ---------------- PCC 细纹鲶鱼 ----------------
    bake_single(
        "PCC",
        ["habitat = 同科底栖（S8 MSF——毛鼻鲶科 Trichomycterid）"],
        "同科底栖推算。" + ORDER_NOTE + "：静态栖息推算，无时序无判断链。单因子"
        "链。",
        "PencilCatfishBenthic"),
    resp_typed(
        "PCC",
        ["congener_ref = 毛鼻鲶科小型——食性未述同属推算（Trichomycterus "
         "striatus，V3 资料薄）"],
        "毛鼻鲶科食性同属推算 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断"
        "顺序描述（S1 EO 食性无述）。",
        "PencilCatfishTyped",
        conf="MEDIUM",
        opn=["食性无述同属推算——引文闭合前 MEDIUM（薄资料）"]),
    # ---------------- STS 花鮨 ----------------
    bake_single(
        "STS",
        ["habitat = 深礁 30-358m（S8 MSF）",
         "nocturnal = 夜行（S7 MSF——昼夜时窗 premise）"],
        "深礁分布+夜行。" + ORDER_NOTE + "：夜行为昼夜时窗 premise 配置级，无面内"
        "判断链。单因子链。",
        "SeaperchDeepReef"),
    resp_typed(
        "STS",
        ["diet = 夜行甲壳/小鱼（typed）",
         "naming = V3 英文名 Grouper 泛指错位注记（Anthias anthias 花鮨科——"
         "库锚学名从）"],
        "深礁夜行 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述（夜行"
        "=时窗 premise）。",
        "DeepReefNocturnalFeeder",
        opn=["V3 英文名泛指错位（Grouper）注记——非 Identity Deferred（学名"
             "明确有效）"]),
    # ---------------- PKC 茅尖鱼 ----------------
    bake_single(
        "PKC",
        ["habitat = 热带河（S8 MSF）"],
        "热带河分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子"
        "链。",
        "PikeCichlidTropicalRiver"),
    resp_typed(
        "PKC",
        ["diet = 慈鲷掠食型推算（trophic 3.6——食性细节 EO）",
         "naming = 臼齿鱼错链清空后的茅尖鱼 Coverage 页承载（Crenicichla "
         "lepidota——pike cichlid 掠食型）"],
        "慈鲷掠食型推算 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述"
        "（S1 EO 掠食型推算）。",
        "PikeCichlidPiscivore",
        conf="MEDIUM",
        opn=["食性细节 EO（trophic 3.6 推算）——引文闭合前 MEDIUM"]),
    # ---------------- BCF 蓝鲶鱼 ----------------
    bake_single(
        "BCF",
        ["habitat = 深潭主河道（S8 MSF）"],
        "深潭主河道分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单"
        "因子链。",
        "BlueCatfishDeepChannel"),
    resp_typed(
        "BCF",
        ["diet = 无脊椎/贝/鱼（『Food consists of small aquatic "
         "invertebrates, clams and fishes』）",
         "nocturnal = 夜间摄食（S7 MSF——昼夜时窗 premise）"],
        "深潭 typed 摄食响应+夜间摄食时窗。" + ORDER_NOTE + "：夜摄为昼夜时窗"
        " premise 配置级，无面内判断链。",
        "DeepChannelNightfeeder"),
    # ---------------- TGS 虎纹鸭嘴鲇 ----------------
    bake_single(
        "TGS",
        ["habitat = 洪泛林+主河道（S8 MSF）"],
        "洪泛林-主河道分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。"
        "单因子链。",
        "SorubimFloodplain"),
    resp_typed(
        "TGS",
        ["diet = 夜行鱼食+蟹（『They feed at night on fish (loricariids, "
         "cichlids and characoids) as well as crabs』）",
         "nocturnal = 夜行（S7 MSF——昼夜时窗 premise）"],
        "夜行鱼食 typed 摄食响应（P01——夜间捕食时窗 premise）。" + ORDER_NOTE +
        "：夜食为昼夜时窗 premise 配置级，无面内判断链。",
        "NocturnalFloodplainPiscivore"),
    # ---------------- EUP 赤梢鱼（名实分离欧洲鲈） ----------------
    bake_single(
        "EUP",
        ["habitat = 湖潭（S8 MSF）"],
        "湖潭分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "PerchLakeBasin"),
    resp_typed(
        "EUP",
        ["diet = 昼间机会食（『opportunistic diurnal feeder which preys "
         "mainly during sunrise and sunset』）",
         "crepuscular_peak = 日升日落捕食峰（S4 MSF——昼夜时窗 premise）",
         "ontogeny = 成体 12cm 起鱼食（S9 MSF——体型阈值 ontogeny premise）",
         "naming = 名实分离（V3 中文名赤梢鱼与学名 Perca fluviatilis 欧洲"
         "鲈错位——库锚学名从）"],
        "昼间机会食 typed 摄食响应（P01——鲈科模式种）。" + ORDER_NOTE + "：日升"
        "日落捕食峰与 12cm 阈值均为时窗/ontogeny premise 配置级，无面内判断链"
        "（非分级命中链——正文无先判后判次序描述）。",
        "DiurnalOpportunistPerch"),
    # ---------------- BTS 迷人真小鲤 ----------------
    bake_single(
        "BTS",
        ["habitat = 沙潭（S8 MSF）"],
        "沙潭分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "ShinerSandPool"),
    resp_typed(
        "BTS",
        ["diet = 水面昆虫（『Adults feed on surface insects』——水面呈现"
         " typed，B5 ARG 北极茴鱼同型）"],
        "水面昆虫 typed 摄食响应（P01+S7 水面呈现）。" + ORDER_NOTE + "：无判断"
        "顺序描述。",
        "SurfaceInsectShiner",
        conf="MEDIUM"),
    # ---------------- GDS 金体美鱥 ----------------
    bake_single(
        "GDS",
        ["habitat = 植被湖潭（S8 MSF）",
         "physiology = 低氧耐热（runtime 生理条件 premise）"],
        "植被湖潭分布+低氧耐热。" + ORDER_NOTE + "：生理耐受为 runtime premise，"
        "无面内判断链。单因子链。",
        "GoldenShinerVegetatedPool"),
    resp_typed(
        "GDS",
        ["diet = 浮游/虫/贝杂食（typed）",
         "bait_role = 钓饵鱼供给角色（S10 SN——产品面排除；B5 RVC 小须美鱥"
         "同属）"],
        "杂食 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述；饵鱼"
         "角色=产品面排除。",
        "BaitfishOmnivore"),
    # ---------------- SLM 银斑鲫 ----------------
    bake_single(
        "SLM",
        ["habitat = 洪泛湖（S8 MSF）",
         "flood_dependence = 洪泛依赖（S4 MSF——『highly dependent on "
         "floodplains』P02 资源面背景，B5 RHM/RBP 同型承载）"],
        "洪泛湖分布+洪泛资源依赖。" + ORDER_NOTE + "：洪泛周期为季节/事件 premise"
        " 配置级，无面内判断链。单因子链。",
        "MylossomaFloodplain"),
    resp_typed(
        "SLM",
        ["diet = 草食（herbivore——Serrasalmid 植食第 3 例，食人鱼科植食反差"
         "系第 3 例）",
         "flood_resource = 洪泛区资源背景（P02 语义由 story FR 解释承载）"],
        "草食 typed 摄食响应（P01——离散植物目标；B5 RHM 植物叶判例同型）。" +
        ORDER_NOTE + "：无判断顺序描述。",
        "FloodplainHerbivore",
        conf="MEDIUM",
        opn=["Serrasalmid 植食第 3 例（RHM/RBP 后）——反差例系列注记"]),
    # ---------------- PKS 高体太阳鱼 ----------------
    bake_single(
        "PKS",
        ["habitat = 植被静水（S8 MSF）"],
        "植被静水分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子"
        "链。",
        "PumpkinseedVegetatedPool"),
    resp_typed(
        "PKS",
        ["diet = 小鱼/无脊椎（『Feeds on small fishes and other "
         "vertebrates』+无脊椎）",
         "series = 太阳鱼系第 7 例（Lepomis gibbosus）"],
        "太阳鱼系 typed 摄食响应（P01——小鱼/无脊椎）。" + ORDER_NOTE + "：无判断"
        "顺序描述。",
        "SunfishPiscivore",
        opn=["快照纯正文转写（无信封）——正文承载为准；引入 pest=OPS 层注记"]),
    # ---------------- BLT 黑口红点鲑（Bull Trout 名实分离） ----------------
    bake_single(
        "BLT",
        ["lifecycle = potamodromous（P05 premise）",
         "habitat = 深潭冷水/高山雪河（S8 MSF）"],
        "深潭冷水-高山雪河分布+河湖洄游。" + ORDER_NOTE + "：洄游为 lifecycle "
        "premise 配置级，无面内判断链。单因子链。",
        "BullTroutColdPool"),
    resp_typed(
        "BLT",
        ["diet = 食性未详（S1 EO——P01 冻结主张承载）",
         "naming = 名实分离（中文名黑口红点鲑与库锚 Salvelinus confluentus="
         "公鱼鳟/Bull Trout 错位——库锚学名从）"],
        "冷水溪流食性栖息推断承载（S1 MSF 无食性引文——P01 承载）。" + ORDER_NOTE +
        "：无判断顺序描述。",
        "BullTroutTyped",
        conf="MEDIUM",
        opn=["食性 S1 EO（P01 冻结主张承载）——引文闭合前 MEDIUM；V 保护边界="
             "OPS 产品面排除"]),
    # ---------------- RSC 黑棘鲶 ----------------
    bake_single(
        "RSC",
        ["habitat = 泥底（S8 MSF）"],
        "泥底分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "RipsawMudBottom"),
    resp_typed(
        "RSC",
        ["diet = 腐屑/摇蚊/蜉蝣幼/甲壳（typed）",
         "schooling = 泥底群游（S3 MSF——甲鲶科群游群结构事实非程序面）"],
        "腐屑-无脊椎 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述；"
        "群游=群结构事实（S3 记录）。",
        "DoradidDetritivore",
        conf="MEDIUM"),
    # ---------------- BBH 黑鮰 ----------------
    bake_single(
        "BBH",
        ["habitat = 软底潭沼（S8 MSF）"],
        "软底潭沼分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子"
        "链。",
        "BullheadSoftPool"),
    resp_typed(
        "BBH",
        ["diet = 虫/贝/植物/鱼杂食（typed）",
         "nocturnal = 夜行（S7 MSF——昼夜时窗 premise）",
         "series = 鮰系第 4 例（Ameiurus melas——story 称鲿科第 4 例，科名"
         "宽泛用法注记）"],
        "夜行杂食 typed 摄食响应（P01——夜行时窗 premise）。" + ORDER_NOTE + "："
        "夜行为昼夜时窗 premise 配置级，无面内判断链。",
        "BullheadNocturnalOmnivore",
        opn=["快照纯正文转写（无信封）——正文承载为准；story『鲿科』称法科名"
             "宽泛用法注记（同 WHC）"]),
    # ---------------- AMN 柳根鱼 ----------------
    bake_single(
        "AMN",
        ["habitat = 河川（S8 MSF）"],
        "河川分布。" + ORDER_NOTE + "：静态栖息单因子，无时序无判断链。单因子链。",
        "AmurMinnowRiver"),
    resp_typed(
        "AMN",
        ["congener_ref = 食性未述同属推算（Rhynchocypris lagowskii——trophic "
         "3.5 同属推算）"],
        "食性同属推算 typed 摄食响应（P01）。" + ORDER_NOTE + "：无判断顺序描述"
        "（S1 EO 同属推算）。",
        "MinnowCongenericTyped",
        conf="MEDIUM",
        opn=["食性无述同属推算——引文闭合前 MEDIUM"]),
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
    n_bake = sum(1 for p in PROGRAMS if p["surface"] == "Bake")
    n_resp = sum(1 for p in PROGRAMS if p["surface"] == "Response")
    n_guard = sum(1 for p in PROGRAMS
                  if p.get("combine") == "DUAL_PATH_CONFLICT_AWARE")
    n_med = sum(1 for p in PROGRAMS if p.get("confidence") == "MEDIUM")
    n_low = sum(1 for p in PROGRAMS if p.get("confidence") == "Low")
    print(f"frozen {len(PROGRAMS)} blind programs (Bake={n_bake} Response={n_resp} "
          f"guard_path={n_guard} MEDIUM={n_med} Low={n_low}) -> {out}")
    for p in PROGRAMS:
        print(f"  {p['program_id']}: {p['blind_hash']}")


if __name__ == "__main__":
    main()
