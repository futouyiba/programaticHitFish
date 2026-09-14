# -*- coding: utf-8 -*-
"""RB-3 stories.jsonl + manifest.yaml（盲段收尾产物——registry 打开前写出）。"""
import json
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[2]
QIDS = json.load(open(BATCH / "queue_ids.json", encoding="utf-8"))

# B7 story rows for the 110 layer-4 codes
b7stories = {}
for l in open(ROOT / "fish_logic_census/batches/CENSUS-B7/stories.jsonl", encoding="utf-8"):
    if l.strip():
        r = json.loads(l)
        b7stories[r["story_id"].split("-")[-1]] = r

BL = {"AMB 四层链第 4 层（B7 110）", }

def queue_row(qid):
    for l in open(ROOT / "fish_logic_census/truth_rebuild_queue.jsonl", encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            if r["queue_id"] == qid:
                return r
    raise KeyError(qid)

rows = []
for code, qid in QIDS.items():
    q = queue_row(qid)
    layer = q["layer"]
    src = None
    if code in b7stories:
        b = b7stories[code]
        src = "%s｜%s" % (b["source_story"], b.get("story_url", ""))
    elif layer.startswith("C9"):
        src = "C9 立族材料（RS1 修复轮冻结体 P-RS1-%s-HAB-BAKE 所在 story=guarding 批 §2.4 栖息面）" % code.split("-")[0]
    elif code == "ARO-RESP":
        src = "FISH-R08｜银龙鱼（Silver Arowana）雄鱼口哺｜B5 input_snapshots/story_ARO.md"
    elif code == "CSL-RESP":
        src = "FISH-R08｜中华沙塘鳢（Chinese Sleeper）雄护卵幼｜B5 input_snapshots/story_CSL.md"
    rows.append({
        "story_id": "CENSUS-REBUILD-003-" + code,
        "source_story": "truth_rebuild_queue:%s（%s）｜输入=%s" % (
            qid, layer,
            "B7 input_snapshots story 快照 + B 系列表达文件 §0 + fish-reference CSV" if layer.startswith("AMB")
            else ("guarding 批 §2.4 栖息面 B 文件 + CSV（RS1 冻结体对照）" if layer.startswith("C9")
                  else "B5/B7 冻结 story 快照 + B 系列文件 + registry v9 挂起登记")),
        "source_story_title": src,
        "queue_id": qid,
        "layer": layer,
        "frozen_patterns": (b7stories.get(code, {}).get("frozen_patterns", "") if code in b7stories else ""),
        "surfaces": {"Bake": {"consequence": "TRUTH_REBUILD_RERUN", "queue": qid}},
        "consequence": "TRUTH_REBUILD_RERUN",
        "provenance": {"batch": "CENSUS-REBUILD-003"},
    })
with open(BATCH / "stories.jsonl", "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("stories:", len(rows))

MANIFEST = """batch_id: CENSUS-REBUILD-003
stage: CENSUS
batch_type: TRUTH_REBUILD_RERUN
worker_role: FCF-CENSUS-WORKER
worker_handle: local_1e980abd-8c5f-4129-be13-6c48535c9de5
coordinator: local_53ba8fd9-a666-4aaa-ba05-80c5f9d6fb93
contract: "authoring_work_standards §2/§5/§6（顺序推导纪律+渐进累积+四形式+判同操作化）；RB-1/RB-2 固化工序范式；HRQ-REBUILD-SCOPE-001 用户终局裁决授权"
status: INDEPENDENT_REVIEW_REQUIRED

input:
  selection_rule: >-
    truth_rebuild_queue.jsonl 两组 118 项：AMB 四层链第 4 层（B7 110——P-B7-*-BAKE
    AMB vs SINGLE v1 转真形）+ 终裁特例 8（C9 立族材料 4=P-RS1-{BLU,ARA,RBP,HNC}-HAB-BAKE
    栖息面；brooted 挂起 2=P-B5-ARO-RESP/P-B0-TIL3-RESP[queue 笔误本体 P-B7-TIL3-RESP]；
    form_hold 挂起 2=P-B5-CSL-RESP/P-B7-CSN1-RESP）。特例产出=HRQ 终裁提案（registry
    零改动）。
  frozen_stories_count: 118   # queue 条目口径（B7 110 story 快照 + B5 2 + B7 CSN1 双条目 + C9 4 B 文件面）
  evidence_layers:
    - "A=CENSUS-B7 input_snapshots story 快照（112 story 全档，Tier A——R01-R05 残余）"
    - "A5=B5 input_snapshots story_ARO/story_CSL（Tier A，brooted/form_hold 特例）"
    - "B=B 系列表达文件 §0 判断顺序声明（REP-WORDING-ALIGN-001 已对齐文本——序声明按约定序伪影不采，因子集可用）"
    - "C=fish-reference-20260908.csv eco-morphology"
    - "RB1/RB2=前两批判档冻结真形（同鱼对账/复用轨）"
  per_fish_order_derivation: >-
    全部 118 项逐鱼顺序推导（无一 order_undetermined）：方向学承 RB-1（食性主句
    先行=FF／栖息复合主句=SF／生理口器特化=门或特化轴先行／证据分辨率决定链长）
    + RB-2 csv_anchor_standard（demersal 硬定位=独立底层步或门；软定位仅当独立维
    入步）+ 本批新增操作化标准（csv_band_strength_standard，见下）。
  csv_band_strength_standard: >-
    时段/水温步入链判定（本批 C9 材料与栖息面推导的操作化）：CSV 时段=全天活跃
    时该步不入链（无分档意义——证据驱动不虚构）；水温带宽度=分档强度依据（窄带
    ±2-4°C=强分档可前置；宽带>10°C=弱分档后置或并入 Response cue）；B 文件因子
    集中 [需正文] 方向级锚按证据强度排后。
  blind_vocabulary_check: "118 条 sketch/premise/open_sem 判同段语汇扫描 0 泄漏（F4 纪律——无族名/提案/立族语汇）"

freeze_history:
  frozen_at_utc_first: "2026-09-14T06:18:50Z"
  note: "首冻即终冻（本批无 registry 开后盲体修正——0 revision）"

same_fish_reconciliation:   # envelope 衔接指令（0 冲突目标）
  strain_track: "KOI/MIR/WRC（鲤品系）+RTL（Oreochromis 杂交）＝TS 单因子同 RB-2 品系轨同形——0 冲突；RB-2 品系『亲本 R03 轨补证后可升档』开放项闭合（KOI 本体同形，品系无需升档）"
  dual_story_reuse: "FGA4→RB-2 FGA（R02-S17 同种双 story 内容近似——reused_from）；RHM2→RB-1 RHM（B5 story——reused_from）"
  dual_story_independent: "BRT3/BRT4/BRT12、COD1/COD2/COD、PIK1/PIK19、PAD1/PAD5/PAD34、WAL2/WAG、SMA1/SMA、BLU2/BLU、CLC(R03)/CLC(B5)、TIL2/TIL3、RSB(Bake/EXT 轨)——story 级各自消费+去重联动注记（story 证据分层忠实记录非冲突）"
  conflicts: 0
  note: "CLC 双 story 分层（B5 story 闭合夜行→NO 形/R03 story 未闭合+CSV 全天→TS 形）挂 HRQ-RB3 对账条目（非冲突——证据分层记录）"

queue_typo_note: "TRB-0301 program_id 前缀 P-B0 为登记笔误（本体=P-B7-TIL3-RESP，registry v9 GUARD 行内 blind_hash=3e1cf6343317da2c）——记档不改 queue 文件"

outputs:
  blind_programs: 118
  derived: 116   # 118 - reused 2（FGA4/RHM2）
  reused: 2
  order_undetermined: 0
  registry_mutation: none   # registry v9 零改动（判同只读 sha256 断言）
  special_outputs: "C9/brooted/form_hold 三特例=HRQ 终裁提案（HRQ-RB3-03/04/05），registry 零改动"
"""
with open(BATCH / "manifest.yaml", "w", encoding="utf-8") as f:
    f.write(MANIFEST)
print("manifest written")
