#!/usr/bin/env python3
# REP-FULL-FIELD-001 structural validator for P03 food-field (滄食/浮游场系)
# four-surface authoring files + variety L1-equivalence declaration files.
# Pure standard library. Adapted from validate_normal.py with batch-specific
# checkpoints:
#   - GROUPFORM: P03 field batch is NO-ROUTE across the archived sample
#     (census BHC/HER Group face NO_SURFACE_EFFECT; GroupPressure=Strong on
#     HER carries no routing body). Routing-atom tables and Special Group
#     routes are violations here, not options.
#   - BAKEFAM: BakeTemplate value is a CLOSED enum of one batch projection
#     label {BA-P03-FIELD-SINGLE} (census SINGLE_FACTOR_NORMALIZED_WEIGHT
#     factor_type-axis food_field instance; new value = spec action).
#   - FAMCTX: FIELD-SINGLE = exactly one FieldType(typed) row whose value
#     carries food_field, one FieldEvaluatorProfile row, NORMALIZE_WEIGHT
#     family constant; no factor-set / combine / slot rows (census SINGLE
#     forbidden_freedoms).
#   - PREMBIND: a FactorBinding row, when present, must reference a premise
#     (seasonal / run-phase switching is premise-level config, never an
#     in-body branch; census MGC/CHB precedents).
#   - CONTRACT: bake tables must reference the UsableForageAvailability input
#     contract triple (plankton / resource-patch / baitfish prey classes all
#     flow through the same contract).
#   - FIELDRESP: batch-uniform topology — R-T1 single channel with
#     Channel=FieldFeeding (the Field form of the R-T1 Feeding channel per
#     live §13.3 Forage-Coupled Feeding), Reaction slot OFF, and the
#     FOOD_FIELD_FEEDING_RESPONSE canonical body projected in a script fence
#     (EVAL_FOOD_FIELD_INTAKE -> DECIDE_FIELD_FEEDING ->
#     Response(FieldFeeding)). R-T2 is a violation in this batch.
#   - L1EQUIV: variety files (L1-EQUIV marker) must carry the four
#     surface-declaration sections, a base-species pointer row and a Profile
#     rebinding list; they are exempt from full-form tables/pseudoscripts.
#   - QUALITYCOV / SHARE / PROFILES / BAN / STRUCT as in prior batches.
# Selftest proves every check family fires on bad input, across two fixture
# topologies (field-single / l1-equiv variant).
import io
import re
import sys
import tempfile
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BATCH_ID = "REP-FULL-FIELD-001"

CANON = {
    "ROUTING": ["规则集", "命中条件", "目标Group", "权重处理", "权重参数"],
    "QUALITY_BIND": ["FishGroup", "QualityTemplate", "EligibilityProfile", "GroupAffinityProfile", "说明"],
    "RESP": ["Group", "响应模板", "条件/Profile", "命中结果", "未命中"],
    "BAKE": ["字段", "值"],
    "META": ["项", "值"],
}

BAKE_TEMPLATE_ENUM = ("BA-P03-FIELD-SINGLE",)

BAKE_FIELD_ENUM = {
    "BakeTemplate",
    "FieldType(typed)",
    "FieldEvaluatorProfile",
    "FactorBinding",
    "Normalization",
    "Bake输入契约",
    "LiveLayerProjection",
}

MERGE_PHRASES = ("固定规则合并", "固定组合规则", "固定汇总", "固定聚合", "按模板固定规则", "按模板固定位置")
NOROUTE_MARK = "无 Special Group 路由程序"
RT1OFF_MARK = "Reaction 槽 OFF"
FIELD_CH_MARK = "R-T1 单通道（FieldFeeding"
RT2_MARK = "R-T2"
CANON_RESP_STEPS = ("EVAL_FOOD_FIELD_INTAKE", "DECIDE_FIELD_FEEDING", "Response(FieldFeeding)")
BAN_PHRASES = ("组合适应度", "Runtime Stage Selector", "LifecycleCohort")
L1EQUIV_MARK = "L1-EQUIV"
VARIANT_SECTIONS = (
    "## 1. Group 面声明",
    "## 2. Bake 面声明",
    "## 3. Response 面声明",
    "## 4. Quality 面声明",
    "## 5. 自由度",
)


def norm_cell(cell: str) -> str:
    return re.sub(r"[\s　]+", "", cell)


def parse_tables(lines):
    tables = []
    cur = None
    heading = ""
    for i, line in enumerate(lines):
        if line.startswith("#"):
            heading = line
        if line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cur is None:
                cur = {"heading": heading, "header": cells, "rows": [], "start": i, "sep_seen": False}
            elif all(re.fullmatch(r":?-{2,}:?", norm_cell(c)) for c in cells if norm_cell(c)):
                cur["sep_seen"] = True
            else:
                cur["rows"].append(cells)
        else:
            if cur is not None:
                tables.append(cur)
                cur = None
    if cur is not None:
        tables.append(cur)
    return tables


def parse_fences(lines):
    fences, cur, on = [], [], False
    for line in lines:
        if line.strip().startswith("```"):
            if on:
                fences.append(cur)
                cur, on = [], False
            else:
                cur, on = [], True
        elif on:
            cur.append(line)
    return fences


def section_text(text, sec_num, next_num):
    m = re.search(rf"^## {sec_num}\..*?(?=^## {next_num}\.|^BATCH_ID:|\Z)", text, re.M | re.S)
    return m.group(0) if m else ""


def check_bake_rows(rows, heading, v):
    kv = {}
    for r in rows:
        key = norm_cell(r[0])
        if key not in BAKE_FIELD_ENUM:
            v.append(("STRUCT", f"unknown bake config field: {r[0]} (under {heading})"))
            continue
        kv[key] = r[1] if len(r) > 1 else ""
    if "BakeTemplate" not in kv:
        v.append(("BAKEFAM", f"bake table missing BakeTemplate row (under {heading})"))
        return
    label = norm_cell(kv["BakeTemplate"]).split("（")[0]
    if label not in BAKE_TEMPLATE_ENUM:
        v.append(("BAKEFAM", f"BakeTemplate not in closed enum: {kv['BakeTemplate']}"))
        return
    for f in ("FactorType(typed)", "Factor1Type(typed)", "Factor2Type(typed)", "CombineRule", "SpatialSlotProfile"):
        if f in kv:
            v.append(("FAMCTX", f"{label} must not carry row {f} (census SINGLE domain: single typed field factor -> normalize; no factor-set/combine/slot)"))
    if "FieldType(typed)" not in kv:
        v.append(("FAMCTX", f"{label} missing FieldType(typed) row"))
    elif "food_field" not in kv["FieldType(typed)"]:
        v.append(("FAMCTX", f"{label} FieldType(typed) row must carry food_field typed axis: {kv['FieldType(typed)']}"))
    if "FieldEvaluatorProfile" not in kv:
        v.append(("FAMCTX", f"{label} missing FieldEvaluatorProfile row (场事实→场评估器→场适应性)")
        )
    if "Normalization" not in kv or "NORMALIZE_WEIGHT" not in kv.get("Normalization", ""):
        v.append(("FAMCTX", f"{label} missing Normalization row with family constant NORMALIZE_WEIGHT"))
    if "FactorBinding" in kv and not re.search(r"premise", kv["FactorBinding"]):
        v.append(("PREMBIND", f"FactorBinding row must reference a premise when present: {kv['FactorBinding']}"))
    if "UsableForageAvailability" not in kv.get("Bake输入契约", ""):
        v.append(("CONTRACT", "bake table missing Bake 输入契约 row referencing UsableForageAvailability"))


def check_variant(path, text, lines, v):
    # L1EQUIV: short-form variety declaration file
    for sec in VARIANT_SECTIONS:
        if not re.search(re.escape(sec), text, re.M):
            v.append(("L1EQUIV", f"variety file missing declaration section: {sec}"))
    if not re.search(r"^\| 本体 \|", text, re.M):
        v.append(("L1EQUIV", "variety file missing 本体 (base species) pointer row in header table"))
    if not re.search(r"^Profile 重绑定清单：", text, re.M):
        v.append(("L1EQUIV", "variety file missing Profile 重绑定清单 line"))
    # PROFILES closure over the rebinding list
    list_line_idx, tokens = None, []
    for i, l in enumerate(lines):
        if l.startswith("Profile 重绑定清单："):
            list_line_idx = i
            tokens = re.findall(r"@[A-Za-z_]\w*", l)
            break
    if list_line_idx is None:
        v.append(("PROFILES", "missing Profile rebinding list line"))
    else:
        used = set()
        for i, l in enumerate(lines):
            if i == list_line_idx:
                continue
            used |= set(re.findall(r"@[A-Za-z_]\w*", l))
        listed = set(tokens)
        for m_ in sorted(used - listed):
            v.append(("PROFILES", f"@token used but not listed: {m_}"))
        for m_ in sorted(listed - used):
            v.append(("PROFILES", f"@token listed but never used: {m_}"))
    if not re.search(r"\b同物种\b", text):
        v.append(("L1EQUIV", "variety file must state the same-species L1 equivalence ground"))
    return v


def check_file(path: Path):
    v = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    for needle, fam in ((BATCH_ID, "HEADER"), ("NOT AUTHORITY", "HEADER"), ("SNAPSHOT_ONLY", "HEADER")):
        if needle not in text:
            v.append((fam, f"missing required marker: {needle}"))
    if not re.search(rf"^BATCH_ID: {BATCH_ID}\s*$", text, re.M):
        v.append(("HEADER", "missing trailing BATCH_ID line"))

    if L1EQUIV_MARK in text:
        check_variant(path, text, lines, v)
        for p in BAN_PHRASES:
            if p in text:
                v.append(("BAN", f"forbidden phrase present: {p}"))
        return v

    for sec, title in ((1, "Group Routing"), (2, "Bake"), (3, "Response"), (4, "Quality Selection"), (5, "")):
        pat = rf"^## {sec}\. {title}" if title else rf"^## {sec}\."
        if not re.search(pat, text, re.M):
            v.append(("SECTIONS", f"missing section ## {sec}. {title}".rstrip()))

    tables = parse_tables(lines)
    fences = parse_fences(lines)

    # GROUPFORM: field batch = NO-ROUTE only
    m11 = re.search(r"^### 1\.1.*?(?=^### 1\.2|^## 2\.)", text, re.M | re.S)
    if not m11:
        v.append(("GROUPFORM", "missing section 1.1 block"))
    else:
        if NOROUTE_MARK not in m11.group(0):
            v.append(("GROUPFORM", f'section 1.1 missing "{NOROUTE_MARK}" declaration (field batch is NO-ROUTE)'))
        if re.search(r"^### 1\.1 条件原子", m11.group(0)):
            v.append(("GROUPFORM", "routing-atom section present in a NO-ROUTE batch file"))

    body_start = next((i for i, l in enumerate(lines) if l.startswith("## 1.")), len(lines))
    routing_groups = set()
    bind_groups = set()

    for t in tables:
        h = t["heading"]
        header = [norm_cell(c) for c in t["header"]]
        if t["start"] < body_start:
            expect = "META"
        elif "1.1" in h and "无路由" in h:
            expect = "SKIP"
        elif "分群结果" in h:
            expect = "ROUTING"
        elif "2." in h and "配置表" in h:
            expect = "BAKE"
        elif "3.1 配置表" in h:
            expect = "RESP"
        elif "4.1 模板绑定" in h:
            expect = "QUALITY_BIND"
        else:
            v.append(("STRUCT", f"table in undeclared location: {h or '(no heading)'}"))
            continue
        if expect == "SKIP":
            if t["rows"]:
                v.append(("STRUCT", f"table under no-route declaration block: {h}"))
            continue
        if header != CANON[expect]:
            v.append(("VARIANT_COLS", f"header mismatch for {expect} under: {h}"))
            continue
        for r in t["rows"]:
            if len(r) != len(t["header"]):
                v.append(("VARIANT_COLS", f"row width != header width under: {h}"))
                break

        if expect == "ROUTING":
            if not any(norm_cell(r[1]) == "默认" for r in t["rows"]):
                v.append(("SHARE", "routing table lacks a 默认 default route row"))
            for r in t["rows"]:
                target = norm_cell(r[2])
                if target:
                    routing_groups.add(target)
                if target != "NormalFeeding":
                    v.append(("GROUPFORM", f"field-batch NO-ROUTE file must not carry Special Group route: {r[2]}"))
                if norm_cell(r[1]) != "默认":
                    v.append(("GROUPFORM", f"non-default route row in NO-ROUTE file: {r[1]}"))
        if expect == "BAKE":
            check_bake_rows(t["rows"], h, v)
        if expect == "QUALITY_BIND":
            for r in t["rows"]:
                if r and r[0].strip():
                    bind_groups.add(norm_cell(r[0]))

    # SHARE: every fence that computes SpecialShareTotal must validate it
    for f in fences:
        body = "\n".join(f)
        if "SpecialShareTotal" in body:
            if "SpecialShareTotal > 1" not in body:
                v.append(("SHARE", "share script missing SpecialShareTotal > 1 validation"))
            if "不静默归一化" not in body:
                v.append(("SHARE", "share script missing 不静默归一化 validation note"))

    # FIELDRESP: batch-uniform R-T1 FieldFeeding topology
    sec3 = section_text(text, 3, 4)
    if FIELD_CH_MARK not in sec3:
        v.append(("FIELDRESP", f'section 3 missing "{FIELD_CH_MARK}" topology declaration'))
    if RT1OFF_MARK not in sec3:
        v.append(("FIELDRESP", f'section 3 missing "{RT1OFF_MARK}"'))
    if RT2_MARK in sec3:
        v.append(("FIELDRESP", f"R-T2 topology declared in a field batch file (batch is uniformly R-T1 FieldFeeding)"))
    fences_all = "\n".join("\n".join(f) for f in fences)
    for step in CANON_RESP_STEPS:
        if step not in fences_all:
            v.append(("FIELDRESP", f"script fence missing canonical step {step} (FOOD_FIELD_FEEDING_RESPONSE projection)"))
    for step in ("EVAL_FOOD_FIELD_CONCENTRATION",):
        if step not in fences_all:
            v.append(("FAMCTX", f"script fence missing canonical bake step {step} (SINGLE food_field projection)"))

    # QUALITYCOV: binding table covers every Group named in routing table
    for g in sorted(routing_groups - bind_groups):
        v.append(("QUALITYCOV", f"Quality binding table does not cover Group: {g}"))

    # PROFILES: list line must close over every @token used (and vice versa)
    list_line_idx, tokens = None, []
    for i, l in enumerate(lines):
        if l.startswith("Profile 引用清单"):
            list_line_idx = i
            tokens = re.findall(r"@[A-Za-z_]\w*", l)
            break
    if list_line_idx is None:
        v.append(("PROFILES", "missing Profile reference list line"))
    else:
        used = set()
        for i, l in enumerate(lines):
            if i == list_line_idx:
                continue
            used |= set(re.findall(r"@[A-Za-z_]\w*", l))
        listed = set(tokens)
        for m_ in sorted(used - listed):
            v.append(("PROFILES", f"@token used but not listed: {m_}"))
        for m_ in sorted(listed - used):
            v.append(("PROFILES", f"@token listed but never used: {m_}"))

    for p in BAN_PHRASES:
        if p in text:
            v.append(("BAN", f"forbidden phrase present: {p}"))
    for f in fences:
        body = "\n".join(f)
        if any(p in body for p in MERGE_PHRASES) and "算子标注" not in body:
            v.append(("BAN", "merge phrase inside a script fence without 算子标注 operator annotation"))

    return v


# ---------------------------------------------------------------- fixtures

FX_FIELD = """# 测试滤食鱼（Test Filterer｜Filterus testus）｜滤食浮游场系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（P03 滄食/浮游场系＝第 5 批） |
| 基线 | SNAPSHOT_ONLY |

## 0. 上游语义与食物场形态

- 食物场形态：滤食浮游场（场 evaluand——浓度场）。
- 证据档：Tier B（CSV 方向锚；Story 行级 Pattern 标签 [需核对]）。

Profile 引用清单：@TsPlanktonFieldEvaluatorProfile @TsPlanktonPreyFields @TsDietClasses @TsSizeWindow @TsFieldIntakeProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Ts_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.3 Group 中文伪脚本

```plain text
本鱼无 Special Group 路由程序（显式声明）
不读取路由事实
不评价任何 Special Group 资格条件

SpecialShareTotal = 0（无 Special Group 成立）

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 全部供给 → NormalFeeding（默认路由）
```

## 2. Bake

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族 food_field 场投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例，registry v4；2 步场评估→归一化） |
| FieldType(typed) | food_field：plankton 场（场 evaluand——浮游浓度场） |
| FieldEvaluatorProfile | @TsPlanktonFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TsPlanktonPreyFields；diet_classes=@TsDietClasses；size_window=@TsSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed food-field factor（B-T1 单因子退化形）；场耦合 live 参照读法=§10 BA-T5——两层 reconciliation OPEN，README §3 |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的食物场事实（浮游浓度场）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@TsPlanktonPreyFields 绑定的 plankton prey class 生物量，
      经 diet_classes=@TsDietClasses 食性过滤
      与 size_window=@TsSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_FOOD_FIELD_CONCENTRATION：
    用食物场浓度事实查询 @TsPlanktonFieldEvaluatorProfile
    得到 FieldSuitability（场适应性）

NORMALIZE_WEIGHT：
    对 FieldSuitability 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单场因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，typed context 属 PATCH 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=FieldFeeding；census FOOD_FIELD_FEEDING_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） | @TsFieldIntakeProfile | 返回 FieldFeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前食物场事实（浮游浓度场——上游 premise/Bake 供给的事实，非离散钩饵目标）

EVAL_FOOD_FIELD_INTAKE：
    用食物场浓度评价 @TsFieldIntakeProfile
    得到 FieldIntakeEvaluation

DECIDE_FIELD_FEEDING：
    按 FieldIntakeEvaluation 决定场摄食响应档位

返回 Response(FieldFeeding)

Reaction 槽 OFF
（evaluand=食物场非离散目标——与 TYPED 族通道轴不可互吞（B1-LAM 判例同型））
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（恒为 NormalFeeding——无 Special Group）

对每个品质：
    读取该品质的 GroupEligibilityFactor（查 @NeutralEligibility）
    读取该品质的 GroupAffinityFactor（查 @NeutralAffinity）
    读取当前 lure / bait / hook / context 等原始事实
    评价所有适用的 Presentation Modifier / Context Modifier（只读原始事实）

    原始品质权重 =
        基础品质权重
        × GroupEligibilityFactor
        × GroupAffinityFactor
        × 所有适用 Modifier

汇总所有品质的原始权重

如果总权重 > 0：
    统一归一化
    输出 QualityWeightVector
否则：
    当前 FishQuality × FishGroup 不产生可实现候选
```

## 5. 自由度、边界与放弃项

- 使用的自由度：SINGLE 族 food_field 轴投影标签；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：离散钩饵捕获通道表达（TAR-09 Open）；合并算子（OPERATOR UNDEFINED）；数值不冻结。

BATCH_ID: REP-FULL-FIELD-001
"""

FX_VARIANT = """# 测试品系鱼（Test Variant Carp｜Cyprinus carpio Var. Test）｜品系 L1 等效层四面声明

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED
**L1-EQUIV——品系同物种色型第一层逻辑等效声明（R10 品系行/变体行归并判例；本文件不独立展开四面伪脚本）**

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-FIELD-001（品系 L1 等效层） |
| 身份锚 | fish-reference-20260908：测试品系鱼行（同物种 → 普通鲤鱼） |
| 本体 | 普通鲤鱼（Cyprinus carpio）——本体四面文件未建（K3 补批登记，见 §0） |
| 基线 | SNAPSHOT_ONLY |

## 0. 本体与等效声明

- L1 等效判语：本品行与本体**同物种**（CSV 行级同物种标注）——四面结构与本体完全等效。
- 视觉层差异（@TvcVisualProfile）是 L2 视觉资产占位，不在 FCF 四面程序内。

Profile 重绑定清单：@TvcVisualProfile @TvcQualityProfile @SpeciesBaseQualityProfile

## 1. Group 面声明

同本体（无路由退化形）；品系不引入新 Special Group。

## 2. Bake 面声明

复用本体 BakeTemplate 与全部 typed 因子（本体未建时＝绑定声明）；品系不新增空间程序。

## 3. Response 面声明

复用本体 Response 拓扑；品系接受窗参数差异并入 @TvcQualityProfile 同层重绑定位（数值不冻结）。

## 4. Quality 面声明

复用本体 QT-1 模板绑定；品系差异＝Species Base 的品系重绑定位（@TvcQualityProfile——与 @SpeciesBaseQualityProfile 同层）。

## 5. 自由度、边界与放弃项

- 使用的自由度：L1 等效声明形态；Profile 重绑定占位命名。
- 放弃的自由度：独立四面展开；视觉层程序化；数值不冻结。

BATCH_ID: REP-FULL-FIELD-001
"""


def run_selftest():
    cases = []

    def case(name, mutate, expect, fixture=FX_FIELD):
        cases.append((name, mutate, expect, fixture))

    case("baseline (field-single) passes unchanged", lambda s: s, None)
    case("baseline (l1-equiv variant) passes unchanged", lambda s: s, None, FX_VARIANT)
    case("HEADER fires on missing NOT AUTHORITY", lambda s: s.replace("NOT AUTHORITY", "X"), "HEADER")
    case("HEADER fires on missing BATCH_ID line", lambda s: s.replace("BATCH_ID: REP-FULL-FIELD-001", "BATCH_ID: other"), "HEADER")
    case("SECTIONS fires on missing Bake section", lambda s: s.replace("## 2. Bake", "## X. Bake"), "SECTIONS")
    case("GROUPFORM fires when 1.1 loses no-route declaration", lambda s: s.replace("本鱼无 Special Group 路由程序：", "本鱼没有路由：", 1), "GROUPFORM")
    case("GROUPFORM fires on Special Group route row", lambda s: s.replace("| Ts_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |", "| Ts_X | @TsAny | Schooling | 按配置分流 | @TsShare |\n| Ts_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |"), "GROUPFORM")
    case("SHARE fires on missing default route row", lambda s: s.replace("| Ts_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |\n", ""), "SHARE")
    case("SHARE fires on missing validation block", lambda s: s.replace("如果 SpecialShareTotal > 1：\n    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）\n", ""), "SHARE")
    case("BAKEFAM fires on value outside closed enum", lambda s: s.replace("BA-P03-FIELD-SINGLE（本批投影标签", "BA-P03-MAGIC（本批投影标签"), "BAKEFAM")
    case("BAKEFAM fires on missing BakeTemplate row", lambda s: s.replace("| BakeTemplate | BA-P03-FIELD-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT factor_type 轴 food_field 场实例，registry v4；2 步场评估→归一化） |\n", ""), "BAKEFAM")
    case("FAMCTX fires when FieldType loses food_field axis", lambda s: s.replace("food_field：plankton 场（场 evaluand——浮游浓度场）", "structure_factor：植被结构轴"), "FAMCTX")
    case("FAMCTX fires on missing FieldEvaluatorProfile row", lambda s: s.replace("| FieldEvaluatorProfile | @TsPlanktonFieldEvaluatorProfile（场评估器：场事实→场评估器→场适应性） |\n", ""), "FAMCTX")
    case("STRUCT fires on FIELD carrying CombineRule row (whitelist is first layer)", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| CombineRule | Template-fixed |"), "STRUCT")
    case("FAMCTX fires when bake fence loses canonical step", lambda s: s.replace("EVAL_FOOD_FIELD_CONCENTRATION：", "EVAL_SOMETHING_ELSE："), "FAMCTX")
    case("PREMBIND fires on binding without premise", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| FactorBinding | 常年绑定 |"), "PREMBIND")
    case("CONTRACT fires on missing forage contract row", lambda s: s.replace("| Bake 输入契约 | UsableForageAvailability（prey_fields=@TsPlanktonPreyFields；diet_classes=@TsDietClasses；size_window=@TsSizeWindow） |\n", ""), "CONTRACT")
    case("FIELDRESP fires when topology loses FieldFeeding channel", lambda s: s.replace("| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） |", "| NormalFeeding | R-T1 单通道（Feeding） |"), "FIELDRESP")
    case("FIELDRESP fires when Reaction slot ON marker missing", lambda s: s.replace("Reaction 槽 OFF", "反应槽关"), "FIELDRESP")
    case("FIELDRESP fires on R-T2 topology declared", lambda s: s.replace("| NormalFeeding | R-T1 单通道（FieldFeeding；intake_semantics=持续滤食） |", "| NormalFeeding | R-T2 固定双通道（错标） |"), "FIELDRESP")
    case("FIELDRESP fires when canonical intake step missing", lambda s: s.replace("EVAL_FOOD_FIELD_INTAKE：", "EVAL_AS_TARGET："), "FIELDRESP")
    case("FIELDRESP fires when canonical RETURN missing", lambda s: s.replace("返回 Response(FieldFeeding)", "返回 Response(TargetFeeding)"), "FIELDRESP")
    case("QUALITYCOV fires when binding table emptied", lambda s: s.replace("| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |\n", ""), "QUALITYCOV")
    case("PROFILES fires on used-but-unlisted token", lambda s: s.replace(" @TsSizeWindow", "", 1), "PROFILES")
    case("PROFILES fires on listed-but-unused token", lambda s: s.replace("Profile 引用清单：@TsPlanktonFieldEvaluatorProfile", "Profile 引用清单：@TsUnusedToken @TsPlanktonFieldEvaluatorProfile"), "PROFILES")
    case("BAN fires on forbidden phrase LifecycleCohort", lambda s: s + "\nLifecycleCohort 提及\n", "BAN")
    case("BAN fires on unannotated merge phrase in fence", lambda s: s + "\n```plain text\n按固定规则合并\n```\n", "BAN")
    case("STRUCT fires on stray table", lambda s: s.replace("## 5. 自由度、边界与放弃项\n", "## 5. 自由度、边界与放弃项\n\n| 怪表 | 值 |\n|---|---|\n| x | y |\n"), "STRUCT")
    case("STRUCT fires on unknown bake config field", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| 随便字段 | x |"), "STRUCT")
    case("L1EQUIV fires when variant loses a declaration section", lambda s: s.replace("## 2. Bake 面声明", "## 2. 别的面"), "L1EQUIV", FX_VARIANT)
    case("L1EQUIV fires when variant loses base-species pointer row", lambda s: s.replace("| 本体 |", "| 基体 |"), "L1EQUIV", FX_VARIANT)
    case("L1EQUIV fires when variant loses rebinding list", lambda s: s.replace("Profile 重绑定清单：", "Profile 清单："), "L1EQUIV", FX_VARIANT)
    case("PROFILES fires on variant listed-but-unused token", lambda s: s.replace("Profile 重绑定清单：@TvcVisualProfile", "Profile 重绑定清单：@TvcExtra @TvcVisualProfile"), "PROFILES", FX_VARIANT)

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        ok = True
        for name, mutate, expect, fixture in cases:
            f = tmp / "fixture.md"
            f.write_text(mutate(fixture), encoding="utf-8")
            v = check_file(f)
            fams = {x[0] for x in v}
            passed = (not v) if expect is None else (expect in fams)
            if not passed:
                ok = False
            print(f"[{'OK  ' if passed else 'FAIL'}] {name}" + ("" if passed else f" -> violations={v}"))
        print(f"== selftest ==\n{'SELFTEST PASS' if ok else 'SELFTEST FAIL'}")
        return ok


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        sys.exit(0 if run_selftest() else 1)
    if len(sys.argv) < 2:
        print("usage: validate_field.py <field_dir> | --selftest")
        sys.exit(2)
    root = Path(sys.argv[1])
    species_dir = root / "species"
    files = sorted(species_dir.glob("*.md"))
    readme = root / "README.md"
    total_v = 0
    for f in files:
        v = check_file(f)
        for fam, msg in v:
            print(f"[VIOL] {f.name}: {fam}: {msg}")
        total_v += len(v)
        print(f"{'[PASS]' if not v else '[FAIL]'} {f.name}")
    if readme.exists():
        rtext = readme.read_text(encoding="utf-8")
        for f in files:
            if f.stem not in rtext:
                print(f"[VIOL] README: species {f.name} missing from summary table")
                total_v += 1
    else:
        print("[VIOL] README: README.md missing")
        total_v += 1
    print(f"== result ==\n{'PASS' if total_v == 0 else 'FAIL'} ({len(files)} species files, {total_v} violations)")
    sys.exit(0 if total_v == 0 else 1)


if __name__ == "__main__":
    main()
