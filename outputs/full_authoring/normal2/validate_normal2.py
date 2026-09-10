#!/usr/bin/env python3
# REP-FULL-NORM2-001 structural validator for P01 Discrete-Target (普通离散
# 目标摄食系) four-surface authoring files — second-round full-closure batch.
# Pure standard library, adapted verbatim from validate_normal.py (first
# round) with batch id changed; family rules identical. Batch-specific
# checkpoints as in round one:
#   - GROUPFORM: the P01 normal layer is NO-ROUTE (census P01 Group face
#     NO_SURFACE_EFFECT across the archived sample). Routing-atom tables and
#     Special Group routes are violations here, not options.
#   - BAKEFAM: BakeTemplate value is a CLOSED enum of batch projection labels
#     {BA-P01-AMBUSH-SINGLE, BA-P01-PLAIN, BA-P01-PURSUIT-PLAIN,
#      BA-P01-OPPORTUNE-SINGLE, BA-P01-NOCTURNAL-SINGLE, BA-P01-SENSE-SINGLE,
#      BA-P01-BOUNDARY-DECL} (census SINGLE / PLAIN family projections plus a
#     boundary no-program declaration form; new value = spec action, not an
#     authoring action).
#   - FAMCTX: family boundary enforced — SINGLE labels = exactly one
#     FactorType row + NORMALIZE_WEIGHT family constant, no combine / multi
#     factor / slot rows; NOCTURNAL additionally requires a LowLight
#     SpatialSlotProfile row; PLAIN labels = Factor1 + Factor2 + CombineRule
#     with OPERATOR UNDEFINED, no Normalization / SpatialSlotProfile;
#     BOUNDARY-DECL forbids every program row (Static Habitat: the
#     declaration is the whole surface content).
#   - PREMBIND: a FactorBinding row, when present, must reference a premise
#     (season / size-class switching is premise-level config, never an
#     in-body branch; census FGA/MDF/CHB precedents). Not mandatory in this
#     batch: most archived P01 stories carry no premise switch.
#   - CONTRACT: non-boundary bake tables must reference the
#     UsableForageAvailability input contract (prey_fields / diet_classes /
#     size_window triple).
#   - REACTFORM: every file declares exactly one Response topology — R-T1
#     single channel with "Reaction 槽 OFF", or R-T2 fixed two-channel with an
#     explicit Reaction channel line, a MAX( aggregate and an operator
#     annotation. Cue-axis consumption (@ElectroFieldProfile / @ScentCueProfile)
#     must be paired with the matching fact-read line inside a script fence.
#   - QUALITYCOV: the binding table must cover every Group named in the
#     routing table (NormalFeeding included — the NO-ROUTE default row).
#   - SHARE / PROFILES / BAN / STRUCT as in prior batches.
# Selftest proves every check family fires on bad input, across five fixture
# topologies (single / plain / nocturnal / rt2 / boundary-decl).
import io
import re
import sys
import tempfile
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BATCH_ID = "REP-FULL-NORM2-001"

CANON = {
    "ROUTING": ["规则集", "命中条件", "目标Group", "权重处理", "权重参数"],
    "QUALITY_BIND": ["FishGroup", "QualityTemplate", "EligibilityProfile", "GroupAffinityProfile", "说明"],
    "RESP": ["Group", "响应模板", "条件/Profile", "命中结果", "未命中"],
    "BAKE": ["字段", "值"],
    "META": ["项", "值"],
}

BAKE_TEMPLATE_ENUM = (
    "BA-P01-AMBUSH-SINGLE",
    "BA-P01-PLAIN",
    "BA-P01-PURSUIT-PLAIN",
    "BA-P01-OPPORTUNE-SINGLE",
    "BA-P01-NOCTURNAL-SINGLE",
    "BA-P01-SENSE-SINGLE",
    "BA-P01-BOUNDARY-DECL",
)
SINGLE_LABELS = {
    "BA-P01-AMBUSH-SINGLE",
    "BA-P01-OPPORTUNE-SINGLE",
    "BA-P01-NOCTURNAL-SINGLE",
    "BA-P01-SENSE-SINGLE",
}
PLAIN_LABELS = {"BA-P01-PLAIN", "BA-P01-PURSUIT-PLAIN"}
BOUNDARY_LABEL = "BA-P01-BOUNDARY-DECL"

BAKE_FIELD_ENUM = {
    "BakeTemplate",
    "FactorType(typed)",
    "Factor1Type(typed)",
    "Factor2Type(typed)",
    "FactorBinding",
    "SpatialSlotProfile",
    "Normalization",
    "CombineRule",
    "Bake输入契约",
    "LiveLayerProjection",
}

MERGE_PHRASES = ("固定规则合并", "固定组合规则", "固定汇总", "固定聚合", "按模板固定规则", "按模板固定位置")
NOROUTE_MARK = "无 Special Group 路由程序"
RT1OFF_MARK = "Reaction 槽 OFF"
RT2_MARK = "R-T2 固定双通道"
BAN_PHRASES = ("组合适应度", "Runtime Stage Selector", "LifecycleCohort")
CUE_PROFILES = {
    "@ElectroFieldProfile": "电场",
    "@ScentCueProfile": "气味",
}


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
        return "NONE"
    label = norm_cell(kv["BakeTemplate"]).split("（")[0]
    if label not in BAKE_TEMPLATE_ENUM:
        v.append(("BAKEFAM", f"BakeTemplate not in closed enum: {kv['BakeTemplate']}"))
        return "NONE"
    if "FactorBinding" in kv and not re.search(r"premise", kv["FactorBinding"]):
        v.append(("PREMBIND", f"FactorBinding row must reference a premise when present: {kv['FactorBinding']}"))
    if label in SINGLE_LABELS:
        for f in ("Factor1Type(typed)", "Factor2Type(typed)", "CombineRule"):
            if f in kv:
                v.append(("FAMCTX", f"{label} must not carry row {f} (census SINGLE domain: single typed factor -> normalize)"))
        if "FactorType(typed)" not in kv:
            v.append(("FAMCTX", f"{label} missing FactorType(typed) row"))
        if "Normalization" not in kv or "NORMALIZE_WEIGHT" not in kv.get("Normalization", ""):
            v.append(("FAMCTX", f"{label} missing Normalization row with family constant NORMALIZE_WEIGHT"))
        if label == "BA-P01-NOCTURNAL-SINGLE":
            if "SpatialSlotProfile" not in kv or "LowLight" not in kv.get("SpatialSlotProfile", ""):
                v.append(("FAMCTX", "NOCTURNAL template missing SpatialSlotProfile row with a LowLight slot (live §11.5 判例)"))
        elif "SpatialSlotProfile" in kv:
            v.append(("FAMCTX", f"{label} must not carry SpatialSlotProfile row (low-light slot is NOCTURNAL-only in this batch)"))
        if "UsableForageAvailability" not in kv.get("Bake输入契约", ""):
            v.append(("CONTRACT", "bake table missing Bake 输入契约 row referencing UsableForageAvailability"))
    elif label in PLAIN_LABELS:
        for f in ("FactorType(typed)", "Normalization", "SpatialSlotProfile"):
            if f in kv:
                v.append(("FAMCTX", f"{label} must not carry row {f} (census PLAIN domain: factor set -> combine)"))
        for f in ("Factor1Type(typed)", "Factor2Type(typed)"):
            if f not in kv:
                v.append(("FAMCTX", f"{label} missing {f} row"))
        if "CombineRule" not in kv or "OPERATOR UNDEFINED" not in kv.get("CombineRule", ""):
            v.append(("FAMCTX", f"{label} missing CombineRule row with OPERATOR UNDEFINED (combine math must stay visibly open)"))
        if "UsableForageAvailability" not in kv.get("Bake输入契约", ""):
            v.append(("CONTRACT", "bake table missing Bake 输入契约 row referencing UsableForageAvailability"))
    else:  # BOUNDARY-DECL
        for f in ("FactorType(typed)", "Factor1Type(typed)", "Factor2Type(typed)", "Normalization", "CombineRule", "SpatialSlotProfile", "Bake输入契约"):
            if f in kv:
                v.append(("FAMCTX", f"{BOUNDARY_LABEL} must not carry program row {f} (Static Habitat: declaration only, no Story-derived spatial program)"))
    return label


def check_file(path: Path):
    v = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    exempt = "INSUFFICIENT_LOCAL_EVIDENCE" in text

    for needle, fam in ((BATCH_ID, "HEADER"), ("NOT AUTHORITY", "HEADER"), ("SNAPSHOT_ONLY", "HEADER")):
        if needle not in text:
            v.append((fam, f"missing required marker: {needle}"))
    if not re.search(rf"^BATCH_ID: {BATCH_ID}\s*$", text, re.M):
        v.append(("HEADER", "missing trailing BATCH_ID line"))

    if exempt:
        return v

    for sec, title in ((1, "Group Routing"), (2, "Bake"), (3, "Response"), (4, "Quality Selection"), (5, "")):
        pat = rf"^## {sec}\. {title}" if title else rf"^## {sec}\."
        if not re.search(pat, text, re.M):
            v.append(("SECTIONS", f"missing section ## {sec}. {title}".rstrip()))

    tables = parse_tables(lines)
    fences = parse_fences(lines)

    # GROUPFORM: P01 normal layer = NO-ROUTE only
    m11 = re.search(r"^### 1\.1.*?(?=^### 1\.2|^## 2\.)", text, re.M | re.S)
    if not m11:
        v.append(("GROUPFORM", "missing section 1.1 block"))
    else:
        if NOROUTE_MARK not in m11.group(0):
            v.append(("GROUPFORM", f'section 1.1 missing "{NOROUTE_MARK}" declaration (P01 normal layer is NO-ROUTE)'))
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
            expect = "SKIP"  # declaration block carries prose, no table
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
                    v.append(("GROUPFORM", f"P01 NO-ROUTE file must not carry Special Group route: {r[2]}"))
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

    # REACTFORM: exactly one of R-T1-OFF / R-T2; cue profile needs fact-read line
    sec3 = section_text(text, 3, 4)
    rt2 = RT2_MARK in sec3
    rt1off = RT1OFF_MARK in sec3
    if rt2 and rt1off:
        v.append(("REACTFORM", f'file declares both "{RT2_MARK}" and "{RT1OFF_MARK}" (exactly one topology allowed)'))
    if not rt2 and not rt1off:
        v.append(("REACTFORM", f'section 3 declares neither "{RT2_MARK}" nor "{RT1OFF_MARK}"'))
    if rt2:
        if "Reaction 通道" not in sec3:
            v.append(("REACTFORM", "R-T2 file missing explicit Reaction 通道 declaration"))
        if "MAX(" not in sec3:
            v.append(("REACTFORM", "R-T2 script missing MAX( aggregate line (live §17 fixed aggregate)"))
        if "算子标注" not in sec3:
            v.append(("REACTFORM", "R-T2 script missing 算子标注 operator annotation"))
    for prof, fact_word in CUE_PROFILES.items():
        if prof in sec3:
            if not any(fact_word in "\n".join(f) for f in fences):
                v.append(("REACTFORM", f"cue profile {prof} consumed but no {fact_word} fact-read line in script fences"))

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


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        sys.exit(0 if run_selftest() else 1)
    if len(sys.argv) < 2:
        print("usage: validate_normal2.py <normal2_dir> | --selftest")
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


# ---------------------------------------------------------------- fixtures

FX_SINGLE = """# 测试伏击鱼（Test Ambusher｜Ambushus testus）｜P01 普通离散目标摄食系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-NORM2-001（P01 普通层 第 6 批：第二轮全量闭合） |
| 基线 | SNAPSHOT_ONLY |

## 0. 上游语义与摄食形态

- 摄食形态：测试用植被结构伏击。
- 证据档：Tier B（CSV 方向锚；Story 行级 Pattern 标签 [需核对]）。

Profile 引用清单：@TsAmbushStructureProfile @TsPreyFields @TsDietClasses @TsSizeWindow @TsNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

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

### 2.1 Story 派生空间程序｜配置表（NormalFeeding Group；census SINGLE 族投影）

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |
| FactorType(typed) | structure_factor：植被/掩体结构轴（typed 实例） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TsPreyFields；diet_classes=@TsDietClasses；size_window=@TsSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + typed structure factor（B-T1 Independent Factor Set 单因子退化形；两层 reconciliation OPEN——README §3） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的结构轴事实（植被/掩体结构）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@TsPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@TsDietClasses 食性过滤
      与 size_window=@TsSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR：
    用结构轴事实查询 @TsAmbushStructureProfile
    得到 AmbushStructureFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 AmbushStructureFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域）
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding；census TYPED_TARGET_RESPONSE 投影）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @TsNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @TsNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
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

- 使用的自由度：SINGLE 族投影标签与 typed 因子实例语义；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：合并算子（无 combine 步；OPERATOR UNDEFINED）；数值与 Profile 值域不冻结。

BATCH_ID: REP-FULL-NORM2-001
"""

FX_PLAIN = FX_SINGLE.replace(
    "BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化）",
    "BA-P01-PURSUIT-PLAIN（本批投影标签＝census PLAIN_FACTOR_COMBINE，registry v4；因子集→组合）",
).replace(
    "| FactorType(typed) | structure_factor：植被/掩体结构轴（typed 实例） |",
    "| Factor1Type(typed) | forage_factor：猎物场轴（typed 实例） |\n| Factor2Type(typed) | habitat_factor：开放水/结构轴（typed 实例） |",
).replace(
    "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| Bake 输入契约",
    "| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |\n| Bake 输入契约",
).replace(
    """EVAL_TYPED_FIELD_OR_FACTOR：
    用结构轴事实查询 @TsAmbushStructureProfile
    得到 AmbushStructureFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 AmbushStructureFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域）""",
    """EVAL_TYPED_FIELD_OR_FACTOR（槽1）：
    用猎物场事实查询 @TsForageFieldProfile
    得到 ForageFit

EVAL_TYPED_FIELD_OR_FACTOR（槽2）：
    用开放水/结构事实查询 @TsHabitatProfile
    得到 HabitatFit

COMBINE_WEIGHTED：
    合并 ForageFit / HabitatFit
算子标注：OPERATOR UNDEFINED — 待机制侧（多因子合并算子；live §15.3 同款占位声明）

返回 SpatialDistributionWeight（因子集链结束：无归一化步、无 gate——族边界）""",
).replace(
    "Profile 引用清单：@TsAmbushStructureProfile @TsPreyFields",
    "Profile 引用清单：@TsForageFieldProfile @TsHabitatProfile @TsPreyFields",
)

FX_NOCTURNAL = FX_SINGLE.replace(
    "BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化）",
    "BA-P01-NOCTURNAL-SINGLE（本批投影标签＝census SINGLE 族低光侧；live §11.5 判例）",
).replace(
    "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |",
    "| SpatialSlotProfile | @TsLowLightSpatialProfile（低光空间槽——live §11.5 DynamicSpatialSlot 判例） |\n| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |",
).replace(
    "Profile 引用清单：@TsAmbushStructureProfile @TsPreyFields",
    "Profile 引用清单：@TsAmbushStructureProfile @TsLowLightSpatialProfile @TsPreyFields",
)

FX_RT2 = FX_SINGLE.replace(
    "| NormalFeeding | R-T1 单通道（Feeding） | @TsNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |",
    "| NormalFeeding | R-T2 固定双通道（Feeding + Reaction；live §13.3/§17） | @TsNormalFeedingProfile + @TsReactionProfile | 返回 FinalResponse | 返回低 / 无响应 |",
).replace(
    """返回 Response(TargetFeeding)

Reaction 槽 OFF
```""",
    """Feeding Channel：
    EVAL_TARGET_AS_FOOD_TYPED：
        用目标事实评价 @TsNormalFeedingProfile
        得到 FeedingResponse

Reaction 通道（固定第二通道，不可配置为任意脚本）：
    读取 突然变向 / 加速 / 持续贴近等 Provocation 事实
    评价 @TsReactionProfile
    得到 ReactionResponse

FinalResponse = MAX(
    FeedingResponse,
    ReactionResponse
)
算子标注：OPERATOR UNDEFINED — 待机制侧（R-T2 固定双通道的 MAX 汇总算子数学未闭合；live §17 同款占位声明）

返回 FinalResponse
```""",
).replace(
    "Profile 引用清单：@TsAmbushStructureProfile @TsPreyFields",
    "Profile 引用清单：@TsAmbushStructureProfile @TsReactionProfile @TsPreyFields",
)

FX_BOUNDARY = FX_SINGLE.replace(
    """| BakeTemplate | BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |
| FactorType(typed) | structure_factor：植被/掩体结构轴（typed 实例） |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TsPreyFields；diet_classes=@TsDietClasses；size_window=@TsSizeWindow） |""",
    """| BakeTemplate | BA-P01-BOUNDARY-DECL（本批无 Story 派生空间程序显式声明标签） |""",
).replace(
    """读取 当前格子的结构轴事实（植被/掩体结构）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@TsPreyFields 绑定的 prey class 生物量，
      经 diet_classes=@TsDietClasses 食性过滤
      与 size_window=@TsSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）

EVAL_TYPED_FIELD_OR_FACTOR：
    用结构轴事实查询 @TsAmbushStructureProfile
    得到 AmbushStructureFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 AmbushStructureFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域）""",
    """本 Story 无派生空间程序（显式声明）
不读取本 Story 派生的空间事实
不评价本 Story 派生的 typed 因子

鱼的空间分布由 Species 基础空间程序（BA-T1 底板，Species 层资产）承载——
本 Story（初次接受边界类）的空间语义＝Static Habitat，无新增证据行
（census 判语原样：Static Habitat 无空间新证据）""",
).replace(
    "Profile 引用清单：@TsAmbushStructureProfile @TsPreyFields @TsDietClasses @TsSizeWindow @TsNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile",
    "Profile 引用清单：@TsNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile",
)


def run_selftest():
    cases = []

    def case(name, mutate, expect, fixture=FX_SINGLE):
        cases.append((name, mutate, expect, fixture))

    case("baseline (single) passes unchanged", lambda s: s, None)
    case("baseline (plain/pursuit) passes unchanged", lambda s: s, None, FX_PLAIN)
    case("baseline (nocturnal) passes unchanged", lambda s: s, None, FX_NOCTURNAL)
    case("baseline (rt2) passes unchanged", lambda s: s, None, FX_RT2)
    case("baseline (boundary-decl) passes unchanged", lambda s: s, None, FX_BOUNDARY)
    case("HEADER fires on missing NOT AUTHORITY", lambda s: s.replace("NOT AUTHORITY", "X"), "HEADER")
    case("HEADER fires on missing BATCH_ID line", lambda s: s.replace("BATCH_ID: REP-FULL-NORM2-001", "BATCH_ID: other"), "HEADER")
    case("SECTIONS fires on missing Bake section", lambda s: s.replace("## 2. Bake", "## X. Bake"), "SECTIONS")
    case("GROUPFORM fires when 1.1 loses no-route declaration", lambda s: s.replace("本鱼无 Special Group 路由程序：", "本鱼没有路由：", 1), "GROUPFORM")
    case("GROUPFORM fires on Special Group route row", lambda s: s.replace("| Ts_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |", "| Ts_X | @TsAny | Aggression | 按配置分流 | @TsShare |\n| Ts_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |"), "GROUPFORM")
    case("SHARE fires on missing default route row", lambda s: s.replace("| Ts_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |\n", ""), "SHARE")
    case("SHARE fires on missing validation block", lambda s: s.replace("如果 SpecialShareTotal > 1：\n    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）\n", ""), "SHARE")
    case("BAKEFAM fires on value outside closed enum", lambda s: s.replace("BA-P01-AMBUSH-SINGLE（本批投影标签", "BA-P01-MAGIC（本批投影标签"), "BAKEFAM")
    case("BAKEFAM fires on missing BakeTemplate row", lambda s: s.replace("| BakeTemplate | BA-P01-AMBUSH-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |\n", ""), "BAKEFAM")
    case("FAMCTX fires on SINGLE carrying CombineRule row", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| CombineRule | Template-fixed |"), "FAMCTX")
    case("FAMCTX fires on PLAIN missing Factor2 row", lambda s: s.replace("| Factor1Type(typed) | forage_factor：猎物场轴（typed 实例） |\n| Factor2Type(typed) | habitat_factor：开放水/结构轴（typed 实例） |", "| Factor1Type(typed) | forage_factor：猎物场轴（typed 实例） |"), "FAMCTX", FX_PLAIN)
    case("FAMCTX fires on PLAIN carrying Normalization row", lambda s: s.replace("| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |", "| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |\n| Normalization | NORMALIZE_WEIGHT |"), "FAMCTX", FX_PLAIN)
    case("FAMCTX fires on NOCTURNAL missing LowLight slot", lambda s: s.replace("@TsLowLightSpatialProfile（低光空间槽——live §11.5 DynamicSpatialSlot 判例）", "@TsSomeSlot（普通槽）"), "FAMCTX", FX_NOCTURNAL)
    case("FAMCTX fires on non-nocturnal carrying slot row", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| SpatialSlotProfile | @TsLowLightSpatialProfile |\n| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |"), "FAMCTX")
    case("FAMCTX fires on BOUNDARY carrying program row", lambda s: s.replace("| BakeTemplate | BA-P01-BOUNDARY-DECL（本批无 Story 派生空间程序显式声明标签） |", "| BakeTemplate | BA-P01-BOUNDARY-DECL（本批无 Story 派生空间程序显式声明标签） |\n| FactorType(typed) | structure_factor |"), "FAMCTX", FX_BOUNDARY)
    case("PREMBIND fires on binding without premise", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| FactorBinding | 常年绑定 |"), "PREMBIND")
    case("CONTRACT fires on missing forage contract row", lambda s: s.replace("| Bake 输入契约 | UsableForageAvailability（prey_fields=@TsPreyFields；diet_classes=@TsDietClasses；size_window=@TsSizeWindow） |\n", ""), "CONTRACT")
    case("REACTFORM fires when both topologies declared", lambda s: s.replace("Reaction 槽 OFF", "Reaction 槽 OFF（R-T2 固定双通道错标）"), "REACTFORM")
    case("REACTFORM fires when neither topology declared", lambda s: s.replace("Reaction 槽 OFF", "反应槽关"), "REACTFORM")
    case("REACTFORM fires on R-T2 missing MAX aggregate", lambda s: s.replace("FinalResponse = MAX(\n    FeedingResponse,\n    ReactionResponse\n)", "FinalResponse = 汇总(FeedingResponse, ReactionResponse)"), "REACTFORM", FX_RT2)
    case("REACTFORM fires on R-T2 missing operator annotation", lambda s: s.replace("算子标注：OPERATOR UNDEFINED — 待机制侧（R-T2 固定双通道的 MAX 汇总算子数学未闭合；live §17 同款占位声明）\n\n", ""), "REACTFORM", FX_RT2)
    case("REACTFORM fires on cue profile without fact read", lambda s: s.replace("| NormalFeeding | R-T1 单通道（Feeding） | @TsNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |", "| NormalFeeding | R-T1 单通道（Feeding；电感知 cue 轴并入） | @TsNormalFeedingProfile + @ElectroFieldProfile | 返回 FeedingResponse | 返回低 / 无响应 |"), "REACTFORM")
    case("QUALITYCOV fires when binding table emptied", lambda s: s.replace("| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |\n", ""), "QUALITYCOV")
    case("PROFILES fires on used-but-unlisted token", lambda s: s.replace(" @TsSizeWindow", "", 1), "PROFILES")
    case("PROFILES fires on listed-but-unused token", lambda s: s.replace("Profile 引用清单：@TsAmbushStructureProfile", "Profile 引用清单：@TsUnusedToken @TsAmbushStructureProfile"), "PROFILES")
    case("BAN fires on forbidden phrase LifecycleCohort", lambda s: s + "\nLifecycleCohort 提及\n", "BAN")
    case("BAN fires on unannotated merge phrase in fence", lambda s: s + "\n```plain text\n按固定规则合并\n```\n", "BAN")
    case("STRUCT fires on stray table", lambda s: s.replace("## 5. 自由度、边界与放弃项\n", "## 5. 自由度、边界与放弃项\n\n| 怪表 | 值 |\n|---|---|\n| x | y |\n"), "STRUCT")
    case("STRUCT fires on unknown bake config field", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| 随便字段 | x |"), "STRUCT")

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
        f = tmp / "exempt.md"
        f.write_text("# 退回档\n\nINSUFFICIENT_LOCAL_EVIDENCE 说明。\n\nStatus：WORKING / NOT AUTHORITY / NOT PROMOTED\n\nSNAPSHOT_ONLY。\n\nBATCH_ID: REP-FULL-NORM2-001\n", encoding="utf-8")
        v = check_file(f)
        passed = not v
        ok = ok and passed
        print(f"[{'OK  ' if passed else 'FAIL'}] exempt INSUFFICIENT_LOCAL_EVIDENCE file only needs header markers" + ("" if passed else f" -> {v}"))
        print(f"== selftest ==\n{'SELFTEST PASS' if ok else 'SELFTEST FAIL'}")
        return ok


if __name__ == "__main__":
    main()
