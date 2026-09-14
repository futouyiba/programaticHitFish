# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-003: programs/coverage/HRQ/absence/curve 一体化产出。"""
import json
from datetime import datetime, timezone
from pathlib import Path

BATCH = Path(__file__).parent
CEN = BATCH.parents[1]
mt_lines = (BATCH / "merge_tests.jsonl").read_text(encoding="utf-8").splitlines()
mt = {}
for l in mt_lines:
    if l.strip():
        t = json.loads(l)
        mt[t["species_id"]] = t
bodies = {b["species_id"]: b for b in map(json.loads, (BATCH / "blind_programs.jsonl").read_text(encoding="utf-8").splitlines())}
stories = {s["species_id"]: s for s in map(json.loads, (BATCH / "stories.jsonl").read_text(encoding="utf-8").splitlines())}
assert len(mt) == len(bodies) == len(stories) == 118, (len(mt), len(bodies), len(stories))
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

SPECIAL_REV = {"ARO-RESP", "TIL3-RESP", "CSL-RESP", "CSN1-RESP"}

# ---- programs.jsonl ----
progs = []
for sid, t in mt.items():
    b = bodies[sid]
    verdict = t["verdict"]
    progs.append({
        "program_id": b["program_id"],
        "story_id": b["story_id"],
        "species_id": sid,
        "surface": "Bake",
        "consequence": ("MERGE_CONFIRMED" if verdict == "MERGE_CONFIDENT"
                        else ("NO_SURFACE_EFFECT_RECORDED" if verdict == "NO_SURFACE_EFFECT" else "NEW_PROGRAM_CANDIDATE")),
        "family_membership": t["target_family"],
        "membership_status": ("CONFIRMED_MEMBER" if verdict == "MERGE_CONFIDENT" else
                              ("NO_SURFACE_EFFECT" if verdict == "NO_SURFACE_EFFECT" else "CANDIDATE_FAMILY_MEMBER")),
        "related_proposal": t["related_proposal"],
        "reused_from": t["reused_from"],
        "review_ref": None if verdict in ("MERGE_CONFIDENT", "NO_SURFACE_EFFECT") else t["human_review_queued"],
        "blind_hash": b["blind_hash"],
        "original_program_body_unchanged": True,
        "registry_seen_at_creation": False,
        "post_registry_mutations": ([] if sid not in SPECIAL_REV else
                                    [{"field": "surface/return_type",
                                      "reason": "queue surface=Bake alignment + GA Bake-projection return naming (face-label contract, not registry-fit motivated)",
                                      "revision_recorded": "REV-RB3-001-%s" % sid,
                                      "bias_risk_flagged": True}]),
        "rerun_of": (b["order_derivation"]["queues"][0].replace("TRB-", "queue:TRB-")),
        "provenance": {"batch": "CENSUS-REBUILD-003", "input": "truth_rebuild_queue:%s（终局顺序还原重跑末批）" % b["order_derivation"]["queues"][0]},
    })
(BATCH / "programs.jsonl").write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in progs) + "\n", encoding="utf-8")

# ---- coverage.jsonl ----
cov = []
for sid in sorted(stories):
    t = mt[sid]
    cov.append({
        "story_id": stories[sid]["story_id"], "species_id": sid,
        "queue_ids": stories[sid]["queue_ids"],
        "layer": stories[sid]["layer"],
        "bake": t["verdict"],
        "response": "NOT_IN_SCOPE（queue 面=Bake；特例 4 条面归属注记见 open_semantics）",
        "group": "NO_SURFACE_EFFECT（queue 面=Bake）",
        "quality": "NO_SURFACE_EFFECT（queue 面=Bake）",
        "order_status": stories[sid].get("order_status", "derived"),
        "note": ("GAR1=Bake 面显式无程序（BOUNDARY-DECL 直证）" if sid == "GAR1" else
                 ("终裁提案载体" if sid.endswith(("HAB", "RESP")) else
                  ("reused_from 双 story 复用" if t["reused_from"] else ""))),
    })
(BATCH / "coverage.jsonl").write_text("\n".join(json.dumps(c, ensure_ascii=False) for c in cov) + "\n", encoding="utf-8")

# ---- human_review_queue.jsonl ----
hrq = [
 {"id": "HRQ-RB3-01", "title": "同鱼对账执行记录（品系/双 story/去重联动——零冲突）+CLC 证据分层",
  "items": [
    "品系轨：KOI/MIR/WRC（鲤品系）+RTL（Oreochromis 杂交）=TS 单因子同形——RB-2 品系 8 尾『亲本 R03 轨补证后可升档』开放项闭合（KOI 本体同形，品系无需升档，0 冲突）",
    "双 story 复用：FGA4<-RB-2 FGA（R02-S17 内容近似——B7 判例⑦点名）；RHM2<-RB-1 RHM（B5 story patch 单因子同形）",
    "双 story 独立消费+去重联动：BRT3/BRT4/BRT12、COD1/COD2/COD、PIK1/PIK19、PAD1/PAD5/PAD34、WAL2/WAG、SMA1/SMA、BLU2/BLU、TIL2/TIL3、RSB(Bake 面/EXT 轨)——story 证据分层忠实记录（非冲突）",
    "CLC 分层：B5 story（RB-1=NO 形含夜槽）vs R03 story（本批=TS 底层遮蔽带单因子——story 明言夜行未闭合+CSV 全天）——夜槽不虚构；两 story 真形差异=证据分层（挂本条目备查，非冲突）",
    "同鱼冲突数=0（envelope 目标达成）",
  ],
  "basis": "envelope 同鱼对账指令+面级守恒判例（RS1 REV-001 ②/RB-2 RBP 异面先例）",
  "ask": "备查（无需裁决——记录性条目；CLC 分层供独立审确认 Tier A 优先读法）"},
 {"id": "HRQ-RB3-02", "title": "RB-1 新族提案形状的扩充证据（FF+8/SF+27——本批 35 落提案形状）",
  "items": [
    "FORAGE_FIRST（HRQ-RB1-02）+8：RED1/RAI2/COD1/BET/STB/MAH/BKC/RST1（累积 RB-1 10->RB-2 26->RB-3 34）",
    "SPACE_FIRST（HRQ-RB1-02）+27：CRA1/YEP1/MUL1/TEN1/LWF1/SBS1/SBH1/HMB/IRS/LNK/MRF/SPS/STM/TPC/YCK/SB2/WCR3/CTT/RSB2/RTB/DVK/GJC/SS2/BIC/SIH/YTA/BBF（累积 RB-1 28->RB-2 34->RB-3 61）",
    "B7 110 尾中 FF+SF 共 35=该层主体形状（R01-R05 残余以机构 story 短主句+两维分辨率为主——链长 2 主导，符合证据分辨率决定链长方向学）",
  ],
  "basis": "envelope：判同只对 registry v9 活族（18）；RB-1 提案形状按 related_proposal=HRQ-RB1-02 累积",
  "ask": "与 HRQ-RB1-02 合并裁决（新族批准后成员名单扩充——FF 34/SF 61 名义）"},
 {"id": "HRQ-RB3-03", "title": "C9 立族终裁提案（四科四属栖息面）——不立原族；4 新形状证据",
  "items": [
    "原 C9 候选族（ORDERED_QUAD_TIER_COMBINE_CHAIN 水层->结构->水温->时段）证伪：逐鱼推导 4/4 无一是该形（RS1 修复轮『4/4 同形』=BA-NORMAL-HABITAT-FIT 约定序伪影——裁决 2-B 落实）",
    "BLU 真形=[E,E,E,E] 结构先行（裁决 §6.2 原文锚『蓝鳃->结构先行』；软水层->宽温->晨昏按证据强度递减）——新形状证据 1（STRUCTURE_FIRST_QUAD）",
    "RBP 真形=[E,E,E] 中上软水层->窄温带->沉水结构（时段=全天不入链——CSV 证据驱动）——新形状证据 2（LAYER_TEMP_STRUCTURE_TRIPLE）；engine 签名与 SOFT_TRIPLE 同但轴类别序列不同（语义层 non-match）",
    "HNC 真形=[G,E,E,E] 底层砾石门->砾石结构->冷水->早晨（门化=硬定位出局语义[RB-1 GRH 判例]+裁决锚『美鱥口器->水层先行』）——新形状证据 3（GATED_STRUCTURE_TEMP_TIME_QUAD）",
    "ARA 真形=[G,E,E,E] 底层门->窄暖温带->洪泛林结构->晨昏（温序前置=CSV 25-29°C 窄带证据强度>结构 [需正文]——与 B 文件声明序差异为逐鱼推导产物）——新形状证据 4（GATED_TEMP_STRUCTURE_TIME_QUAD）；vs HNC 形第 2/3 步互换=ORDER 差异",
    "面级守恒：本批栖息面与 RB-2 护巢面（BLU/ARA/RBP/HNC GA 四步）互为同种双面独立记账（无复用）",
  ],
  "basis": "queue C9 立族材料 pending_work：『真实序逐鱼推导后再裁立族』；§6.2 逐鱼推导纪律+裁决原文两锚（蓝鳃/美鱥）",
  "ask": "终裁：C9 原族撤案；4 新形状是否立族（或并入/等证据扩充）随 v10 mutation 与 RB-1 六提案并案裁决"},
 {"id": "HRQ-RB3-04", "title": "brooted 挂起终裁提案（ARO 银龙口哺/TIL3 罗非）",
  "items": [
    "ARO 终裁提案=退化链（brooded 结构级不入 GUARD_ANCHOR 四形式——与罗非先例同构）：①nile_tilapia.md §0 Brooding 退化链判读（口孵锚与个体绑定——无关系轴/无温度轴/无合并步）为 B 层唯一口孵型判读；②ARO story『carries eggs, larvae and early juveniles in his mouth』=携带型同构（锚在口中=无锚址空间关系语义）；③B 系列无银龙 guard 面（P04 边界归补批未做）",
    "B5 全链盲形（PARALLEL 双 Path+关系评估）=P04 契约模板套用（B5 冻结体自注『携带型 vs 结构型 anchor 差异留判同阶段』）——降级为契约套用记录",
    "保留张力（开放项）：口哺期水面跳跃捕食并存（罗非口孵=强 Feeding Cap；银龙开放）——若后续证据证实口哺期全功能摄食+冲突并行，双 Path 读法可复活",
    "TIL3 终裁提案=分面记账读法修正：雌鱼口哺面=退化链边界确认（B 文件直证）；雄鱼领地面=非 brooded 程序（territory=关系对象非后代空间存在形式——无卵/幼锚，按 premise+TS 轴段独立记账）；原挂起登记（anchor=brooded）混淆两关系对象——读法修正（registry 落位随 v10 mutation 另批）",
    "退化链形状证据=BROODED_DEGENERATE_TWO_STEP_CHAIN（[G,E] 两步——vs GA 四步=步数+轴结构差异=结构级，裁决 4 brooded 边界的形状依据）",
    "queue 笔误记档：TRB-0301 program_id 前缀 P-B0（本体=P-B7-TIL3-RESP，registry v9 行内 blind_hash 对应）",
  ],
  "basis": "queue brooted 挂起终裁：『以 B 系列文件 Bake 面证据裁决退化链 vs 全链（罗非退化链先例 vs B5 盲形分歧）』；裁决 4 brooded 边界",
  "ask": "终裁：ARO=退化链维持；TIL3=分面记账（雌口哺 brooded 挂起转边界成员/雄领地 TS）；退化链两步形状是否立族随 v10 并案"},
 {"id": "HRQ-RB3-05", "title": "form_hold 挂起终裁提案（CSL/CSN1 anchor 形式）+GAR1 无程序面处理",
  "items": [
    "CSL 终裁提案=anchor 形式 fry_school：story『Males guard the eggs and pelagic larvae』——pelagic larvae=浮游幼体（fry_school 直证）；egg 阶段无巢构建/附着面判别词（B5 冻结证据+MUT 批 REV-001 F1 原文）——不虚构 nest/egg_mass；与 MUT 批『按初始形式落 nest』落位注记分歧，以 story 直证为准；egg 阶段形式 open 留 HRQ",
    "CSN1 终裁提案=anchor 形式 fry_school：guarding/snakehead.md §0 直证（『锚点：fry_school（浮巢孵化后的稚鱼群，植被区移动锚）』）+story 护幼主体（『伏击捕食与护幼关系切换』冻结行=护幼）；初始浮巢阶段=相邻阶段留 open 而非虚构 nest",
    "两提案落位（fry_school 计数 3->5）随 v10 mutation 另批（registry 零改动纪律）",
    "GAR1（B01-S05）=Bake 面 NO_SURFACE_EFFECT（非四态单列）：B 文件 BOUNDARY-DECL 直证（取饵初次接受边界=Encounter/Conversion 侧交互实例非空间分布证据）；queue 条目以显式无程序消费（absence_claims 记录）",
    "field Response 投影注记：本批 19 尾场浓度单步（TS factor_type=field 轴值读法）对应 Response 面 FOOD_FIELD 投影（B7 批 16 成员族域）——面分离记账不重复",
  ],
  "basis": "queue form_hold 挂起终裁：『以 B 系列文件巢/附着证据定 anchor 形式』；MUT 批 form_hold 挂起登记（REV-001 F1/R3）",
  "ask": "终裁：CSL/CSN1=fry_school（egg 阶段 open 项保留）；GAR1 无程序面处理确认"},
]
(BATCH / "human_review_queue.jsonl").write_text("\n".join(json.dumps(h, ensure_ascii=False) for h in hrq) + "\n", encoding="utf-8")

# ---- absence_claims.jsonl（GAR1 显式无程序记录；其余 117 项全消费） ----
claims = [{
    "story_id": "CENSUS-REBUILD-003-GAR1", "species_id": "GAR1",
    "queue_id": stories["GAR1"]["queue_ids"][0],
    "claim": "NO_SURFACE_EFFECT_EXPLICIT",
    "reason": "B01-S05 取饵初次接受边界——TargetFeeding 只解释最初接受（story owner 推论原样）；携行/咀嚼吞咽/挂钩=Encounter/Conversion/Contact 侧交互实例；B 文件 alligator_gar.md §2.2=BOUNDARY-DECL 显式声明（Bake 面无 Story 派生程序）；hard-mouth 失败不反写 FeedingMatch",
    "evidence": ["B7 story_004.md", "outputs/full_authoring/normal/species/alligator_gar.md#S0-S2.2"],
}]
(BATCH / "absence_claims.jsonl").write_text("\n".join(json.dumps(c, ensure_ascii=False) for c in claims) + "\n", encoding="utf-8")

# ---- discovery curve append（幂等守卫） ----
from collections import Counter
cnt = Counter(t["verdict"] for t in mt.values())
assert cnt["MERGE_CONFIDENT"] + cnt["NEW_TEMPLATE_CANDIDATE"] + cnt["NO_SURFACE_EFFECT"] == 118
curve = CEN / "discovery_curve.csv"
lines = curve.read_text(encoding="utf-8").strip().splitlines()
assert lines[0].startswith("batch_id,n_stories_consumed")
# n_new_template_candidate 列=distinct 新族口径（RB-1 REV-001 #2 判例）：
# 本批 distinct=5（C9 材料 4 形状+brooded 退化链 1 形状）——FF/SF 35 条为 RB-1 提案形状累积
# （related_proposal=HRQ-RB1-02，不占 distinct——RB-2 口径沿用，随行声明）。
DISTINCT_NEW_FAMILIES_RB3 = 5
row = "CENSUS-REBUILD-003,118,118,%d,0,%d,0,0,0,0,0,0,0,0" % (cnt["MERGE_CONFIDENT"], DISTINCT_NEW_FAMILIES_RB3)
if any(l.startswith("CENSUS-REBUILD-003,") for l in lines):
    print("curve: row already present (idempotent skip)")
else:
    lines.append(row)
    curve.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("curve: appended", row)

print("programs", len(progs), "coverage", len(cov), "hrq", len(hrq), "absence", len(claims))
