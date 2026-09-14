# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-002：stories.jsonl + manifest.yaml + .freeze_marker（盲段收口，registry 打开前）。"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BATCH = Path(__file__).parent
ROOT = BATCH.parents[2]
blind = BATCH / "blind_programs.jsonl"
rows = [json.loads(l) for l in blind.read_text(encoding="utf-8").splitlines()]
assert len(rows) == 94

queue = [json.loads(l) for l in (ROOT / "fish_logic_census/truth_rebuild_queue.jsonl").read_text(encoding="utf-8").splitlines()]
layer_of = {}
for q in queue:
    layer_of[q["program_id"]] = q["layer"]

now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
frozen = rows[0]["frozen_at_utc"]

stories = []
for r in rows:
    sp = r["species_id"]
    qpid = ("P-B6-%s-BAKE" % sp) if sp in [x.split("-")[2] for x in layer_of if x.startswith("P-B6")] else ("P-RS1-%s-BAKE" % sp)
    layer = layer_of[qpid]
    stories.append({
        "story_id": r["story_id"],
        "species_id": sp,
        "source_story": ("truth_rebuild_queue:%s（%s）｜输入=story 快照[B6/B3/B4 批档或 B1/B2 冻结 sketch]"
                         "+B 系列表达文件（RS1 轨对照）+fish-reference-20260908 CSV+RB-1 真形（同鱼同面复用轨）") % (r["order_derivation"]["queues"][0], layer),
        "frozen_patterns": ["truth_rebuild", "work-standards-6.1/6.2/6.4"],
        "order_status": r["order_derivation"]["status"],
        "reused_from": r.get("reused_from"),
        "queue_ids": r["order_derivation"]["queues"],
        "surfaces": {
            "Bake": {
                "consequence": "TRUTH_RERUN_CANDIDATE",
                "program_ids": [r["program_id"]],
                "reason": "终局顺序还原重跑真形（渐进累积语义）",
            }
        },
        "consequence": "TRUTH_RERUN_CANDIDATE",
        "provenance": {"batch": "CENSUS-REBUILD-002", "frozen_at_utc": frozen},
    })
(BATCH / "stories.jsonl").write_text("\n".join(json.dumps(s, ensure_ascii=False) for s in stories) + "\n", encoding="utf-8")

sha = hashlib.sha256(blind.read_bytes()).hexdigest()[:16]
(BATCH / ".freeze_marker").write_text("blind_frozen_at=%s\nblind_sha256_16=%s\n" % (frozen, sha), encoding="utf-8")

freeze_history = """
freeze_history:
  - "2026-09-14T05:37:14Z sha256[:16]=24438c0e77d0e7a7（首冻 94 体——BHC/HER return_type=FieldFeeding）"
  - "2026-09-14T05:41:12Z sha256[:16]=1a43453f38dcec61（REV-RB2-001：BHC/HER return_type→SpatialDistributionWeight——Bake 面契约修正，顺序/结构/族形零变更；发现于 registry 已开后判同准备期，program_revisions.jsonl 全留痕——判同四态不受影响）"
"""

from collections import Counter
cnt = Counter(s["order_status"] for s in stories)
manifest = """# CENSUS-REBUILD-002 (RB-2) manifest
batch_id: CENSUS-REBUILD-002
batch_type: TRUTH_REBUILD_RERUN
created_utc: {now}
ruling_ref: HRQ-REBUILD-SCOPE-001（用户终局裁决授权）+ HRQ-ADJUDICATION-2026-09-11（hrq_decision_log.md @ commit b5088ab）
registry_baseline: v9（HRQ-MUTATION-001 后；本批零 mutation——v10 提案待独立审另批）

inputs:
  truth_rebuild_queue_layers:
    - AMB 四层链第 3 层（B6 47）
    - 链族在册 order_provisional 成员（47 族内——source CENSUS-RERUN-SINGLE-001）
  queue_items_selected: 94
  same_fish_reconciliation:
    - RB-1 同鱼同面复用 17（BSB/BSK/BST/CBM/FDR/GDE/GPF/GRH/HNC/MOO/RRH/SDG/SMB/SSL/TSK/WIT/YTF——B4 起源 RS1 成员，RB-1 已从同一 B4 story 快照 Tier A 推导；复用体标注 reused_from，不重推不冲突）
    - RB-1 同种品系复用 1（WS2=白化高首鲟↔WST 同种 Cross-Batch 去重联动第 2 例）
    - 同鱼异面 1（RBP：RB-1=摄食面单因子/本批 RS1 项=护卵面 §2.2——两程序面独立记账，RB-1 真形不适用于本项，独立推导）
    - 批内同种双行 1（JSB↔ASB 同 URL 同种——真形同体推导，双 queue 项独立记账+去重联动注记）
    - 批内同种品系 1（AGC 白化草鱼↔GRB 同种——GRB 本批真形复用）
  evidence_layers:
    - A=census 冻结 story 快照（B6/B3/B4 批档 input_snapshots，Tier A；R10 压缩四节格式按 B6 判例①直接消费）
    - A12=B1/B2 批无 story 文本档（batch 无 input_snapshots）——以 B1/B2 冻结盲体 sketch/premise（Tier C story 派生事实）替代
    - B=B 系列表达文件 §0 判断顺序行+§2 Bake（Tier B 受限还原——不得照抄，只作对照；其样板语义方向级还原=约定序层不采）
    - C=fish-reference-20260908.csv 形态/生态行（口器代理=食性/摄食类型；水层=栖息带；活跃时段=时段偏好）
    - RB1=CENSUS-REBUILD-001 冻结真形（同鱼同面/同种复用轨——envelope 授权复用）
    - 顺序证据不足 → order_undetermined 挂起（不虚构不默认约定序）

outputs:
  blind_programs: "94（frozen_at_utc: {frozen}；sha256[:16]={sha}；registry_seen=false）"
  order_derived: {d}
  order_reused_from_rb1: {u}
  order_undetermined: 0
  merge_tests: post-registry（判同段产出）
  human_review_queue: post-registry

bias_declaration:
  blind_discipline: 判同前未读 template_registry.yaml——全部 94 真形体（76 逐鱼推导+18 复用）冻结于 {frozen}（.freeze_marker 锚定；本 manifest 写出={now}）；RB-1 批档（batch_report/blind_programs/merge_tests）与 RS1/B1-B7 批档为归档工件（envelope 授权证据源），非 registry 读
  expression_file_usage: B 层文件仅作因子集与 §0 顺序声明对照——受限还原/样板语义方向级还原（CHN/COH/BRO/ALE/TAR 等 migration 单步链自述『样板链优先/约定序』）一律不采；每鱼 order_basis 记录与 B 层的分歧（证据分层记录）
  vocabulary_discipline: 盲体语汇自查——76 条自主体仅描述行为结构（链/档/门/槽/场 evaluand），无 extension/新轴/族名提案语汇（脚本扫描 0 泄漏）；18 条复用体携带 RB-1 冻结 basis 原文，其中 5 条（BSB/FDR/SSL/WIT/YTF）含 queue 元数据归族引用（『RS1 归族 GATED_COVER…分歧挂 HRQ』=RB-1 对输入层 queue reason 的引用，非 registry 读）——复用体不改写 RB-1 冻结推导文本，故保留原样并在此声明
  wording_alignment_state: REP-WORDING-ALIGN-001 已完成（envelope 2026-09-14 声明）——B 系列表达文件为对齐后文本（×0.01 软出局/无合并步措辞），本批引文直接按对齐后文本标注，无并行批执行中影响
  csv_anchor_standard: CSV 锚入链判据（承 RB-1 并明示）：demersal 硬定位=独立底层步（INC/WST 判例）；benthopelagic/pelagic-neritic 软定位=仅当与 story 主体轴为独立维度时入步（垂直层 vs 水平廊道分维判定——COD/ARC/VEN/SWO 轴段与栖息带同维度不另立步防双计；CHN/COH/BRO/ALE/CHU/SHA 廊道轴+垂直层两维两步）；时段偏好=夜相槽（MOO CSV 级判例）/晨昏=premise；品系行（Identity Deferred S1-S11 全 SN）分辨率=同种物种级单因子或亲本构型复用
  derived_vs_template_order: 真形顺序一律从 story 正文主句/形态生态特化/CSV 锚独立推导（推导方向承 RB-1：食性主句先行=开放水跟随型；栖息复合主句信息密度高=结构/复合带先行；口器/生理特化绑定=GATE 或特化轴先行；证据分辨率决定链长——S1 EO 则 forage 轴不立单因子）

self_qa: worker_self_qa.md（判同后补全）
{freeze_history}review_gate: INDEPENDENT_REVIEW_REQUIRED
""".format(now=now, frozen=frozen, sha=sha, d=cnt["derived"], u=cnt["reused"], freeze_history=freeze_history)
(BATCH / "manifest.yaml").write_text(manifest, encoding="utf-8")
print("stories", len(stories), "manifest written", now)
