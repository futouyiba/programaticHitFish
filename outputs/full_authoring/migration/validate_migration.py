#!/usr/bin/env python3
# REP-FULL-MIGRA-001 structural validator for Migration/lifecycle/state-system (P05)
# four-surface authoring files. Pure standard library. Adapted from
# validate_grazing.py / validate_guarding.py with batch-specific checkpoints:
#   - GROUPFORM: every file declares exactly one Group topology — MIGRATION-ROUTED
#     (G2/C12 precedent: migration-phase share-vector routing into a
#     MigrationReaction Group) or NO-ROUTE (explicit no-routing-program
#     declaration; census P05 Group consequence = NO_SURFACE_EFFECT).
#   - REACTPATH: MIGRATION-ROUTED files must route a MigrationReaction Group with
#     an @share, and the Response section must carry the dual-path structure with
#     the structural Feeding closure line (停食判例 R06/R10 FR3 分支化).
#   - RT1OFF: NO-ROUTE files must declare the Reaction slot OFF (R-T1 shape).
#   - BAKEFAM: BakeTemplate value is a CLOSED enum of batch projection labels
#     {BA-MIGRATION-SINGLE, BA-MIGRATION-PLAIN, BA-MIGRATION-GATED}
#     (census SINGLE / PLAIN / HARD_GATED family projections; new value = spec
#     action, not an authoring action).
#   - FAMCTX: family boundary enforced — SINGLE = exactly one FactorType row +
#     NORMALIZE_WEIGHT family constant, no gate/combine rows; PLAIN = Factor1 +
#     Factor2 rows + CombineRule with OPERATOR UNDEFINED, no NORMALIZE row;
#     GATED = SurfaceGate row + CombineRule, gate is hard not relative.
#   - PREMBIND: every bake table carries a FactorBinding row referencing a
#     lifecycle/state premise (P05 batch core: phase switching is premise-level,
#     never an in-body branch).
#   - QUALITYCOV: Quality binding table must cover every Group named in the
#     routing table.
#   - SHARE / REFS / PROFILES / BAN / STRUCT as in prior batches.
# BAN vocabulary additionally guards the G2 anti-patterns (Runtime Stage
# Selector / LifecycleCohort must not be purchased).
# Selftest proves every check family fires on bad input, with independent
# probes for each Chinese guard keyword.
import io
import re
import sys
import tempfile
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BATCH_ID = "REP-FULL-MIGRA-001"

CANON = {
    "COND_ATOM": ["条件组", "条件", "事实/计算项", "参数", "比较符", "比较值"],
    "RULESET": ["规则集", "组合方式", "引用"],
    "ROUTING": ["规则集", "命中条件", "目标Group", "权重处理", "权重参数"],
    "QUALITY_BIND": ["FishGroup", "QualityTemplate", "EligibilityProfile", "GroupAffinityProfile", "说明"],
    "RESP": ["Group", "响应模板", "条件/Profile", "命中结果", "未命中"],
    "BAKE": ["字段", "值"],
    "META": ["项", "值"],
}

BAKE_TEMPLATE_ENUM = ("BA-MIGRATION-SINGLE", "BA-MIGRATION-PLAIN", "BA-MIGRATION-GATED")
BAKE_FIELD_ENUM = {
    "BakeTemplate",
    "FactorType(typed)",
    "Factor1Type(typed)",
    "Factor2Type(typed)",
    "Factor3Type(typed)",
    "Factor4Type(typed)",
    "FactorSet(typed)",
    "FactorBinding",
    "SpatialSlotProfile",
    "SurfaceGate",
    "HabitatFactorProfile",
    "PreyFactorProfile",
    "TemperatureProfile",
    "TimeProfile",
    "ExtremeTemperatureGate",
    "Normalization",
    "CombineRule",
    "Bake输入契约",
    "LiveLayerProjection",
}

MERGE_PHRASES = ("固定规则合并", "固定组合规则", "固定汇总", "固定聚合", "按模板固定规则", "按模板固定位置")
NOROUTE_MARK = "无 Special Group 路由程序"
RT1OFF_MARK = "Reaction 槽 OFF"
MIGRATION_GROUP = "MigrationReaction"
FEEDING_CLOSURE = "不再评价普通 Feeding"
FEEDING_SUPPRESS = "强抑制或关闭"
BAN_PHRASES = ("组合适应度", "Runtime Stage Selector", "LifecycleCohort")


def norm_cell(cell: str) -> str:
    return re.sub(r"[\s　]+", "", cell)


def parse_tables(lines):
    """Yield dicts for each markdown table: nearest heading, header cells, data rows."""
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
    """rows: list of [field, value]; enforce BAKEFAM / FAMCTX / PREMBIND."""
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
    m = re.match(r"BA-MIGRATION-(SINGLE|PLAIN|GATED)", norm_cell(kv["BakeTemplate"]))
    if not m:
        v.append(("BAKEFAM", f"BakeTemplate not in closed enum {BAKE_TEMPLATE_ENUM}: {kv['BakeTemplate']}"))
        return
    fam = m.group(0)
    if "FactorBinding" not in kv:
        v.append(("PREMBIND", f"bake table missing FactorBinding row (P05 batch core: premise-level switching; under {heading})"))
    elif not re.search(r"premise", kv["FactorBinding"]):
        v.append(("PREMBIND", f"FactorBinding row must reference a lifecycle/state premise: {kv['FactorBinding']}"))
    if "UsableForageAvailability" not in kv.get("Bake输入契约", ""):
        v.append(("STRUCT", "bake table missing Bake 输入契约 row referencing UsableForageAvailability"))
    if fam == "BA-MIGRATION-SINGLE":
        for f in ("Factor1Type(typed)", "Factor2Type(typed)", "FactorSet(typed)", "SurfaceGate", "CombineRule", "ExtremeTemperatureGate"):
            if f in kv:
                v.append(("FAMCTX", f"SINGLE template must not carry row {f} (census SINGLE domain: single typed factor -> normalize)"))
        if "FactorType(typed)" not in kv:
            v.append(("FAMCTX", "SINGLE template missing FactorType(typed) row"))
        if "Normalization" not in kv or "NORMALIZE_WEIGHT" not in kv.get("Normalization", ""):
            v.append(("FAMCTX", "SINGLE template missing Normalization row with family constant NORMALIZE_WEIGHT"))
    elif fam == "BA-MIGRATION-PLAIN":
        for f in ("FactorType(typed)", "FactorSet(typed)", "SurfaceGate", "Normalization", "ExtremeTemperatureGate", "SpatialSlotProfile"):
            if f in kv:
                v.append(("FAMCTX", f"PLAIN template must not carry row {f} (census PLAIN domain: factor set -> combine)"))
        for f in ("Factor1Type(typed)", "Factor2Type(typed)"):
            if f not in kv:
                v.append(("FAMCTX", f"PLAIN template missing {f} row"))
        if "CombineRule" not in kv or "OPERATOR UNDEFINED" not in kv.get("CombineRule", ""):
            v.append(("FAMCTX", "PLAIN template missing CombineRule row with OPERATOR UNDEFINED (combine math must stay visibly open)"))
    else:  # GATED
        for f in ("FactorType(typed)", "Factor1Type(typed)", "Factor2Type(typed)", "Normalization", "SpatialSlotProfile"):
            if f in kv:
                v.append(("FAMCTX", f"GATED template must not carry row {f} (census HARD_GATED domain: hard gate -> factor set -> combine)"))
        if "SurfaceGate" not in kv:
            v.append(("FAMCTX", "GATED template missing SurfaceGate row (hard viability gate is the family signature)"))
        if "FactorSet(typed)" not in kv:
            v.append(("FAMCTX", "GATED template missing FactorSet(typed) row"))
        if "CombineRule" not in kv or "OPERATOR UNDEFINED" not in kv.get("CombineRule", ""):
            v.append(("FAMCTX", "GATED template missing CombineRule row with OPERATOR UNDEFINED"))


def check_file(path: Path):
    v = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    exempt = "INSUFFICIENT_LOCAL_EVIDENCE" in text

    # HEADER
    for needle, fam in ((BATCH_ID, "HEADER"), ("NOT AUTHORITY", "HEADER"), ("SNAPSHOT_ONLY", "HEADER")):
        if needle not in text:
            v.append((fam, f"missing required marker: {needle}"))
    if not re.search(rf"^BATCH_ID: {BATCH_ID}\s*$", text, re.M):
        v.append(("HEADER", "missing trailing BATCH_ID line"))

    if exempt:
        return v

    # SECTIONS
    for sec, title in ((1, "Group Routing"), (2, "Bake"), (3, "Response"), (4, "Quality Selection"), (5, "")):
        pat = rf"^## {sec}\. {title}" if title else rf"^## {sec}\."
        if not re.search(pat, text, re.M):
            v.append(("SECTIONS", f"missing section ## {sec}. {title}".rstrip()))

    tables = parse_tables(lines)
    fences = parse_fences(lines)

    # GROUPFORM: exactly one of MIGRATION-ROUTED / NO-ROUTE
    m11 = re.search(r"^### 1\.1.*?(?=^### 1\.2|^### 1\.3|^## 2\.)", text, re.M | re.S)
    if not m11:
        v.append(("GROUPFORM", "missing section 1.1 block"))
        routed = False
    else:
        # routed topology is declared by a condition-atom section heading
        # (### 1.1 条件原子（...）; the NO-ROUTE variant heads with 路由条件原子｜无路由程序)
        routed = bool(re.match(r"^### 1\.1 条件原子（", m11.group(0)))
        noroute = NOROUTE_MARK in m11.group(0)
        if routed and noroute:
            v.append(("GROUPFORM", "file declares both routing atoms and no-routing program (exactly one topology allowed)"))
        if not routed and not noroute:
            v.append(("GROUPFORM", f'section 1.1 neither declares routing atoms nor "{NOROUTE_MARK}"'))
        if noroute:
            routed = False

    body_start = next((i for i, l in enumerate(lines) if l.startswith("## 1.")), len(lines))
    routing_groups = set()
    rulesets_declared = set()

    for t in tables:
        h = t["heading"]
        header = [norm_cell(c) for c in t["header"]]
        if t["start"] < body_start:
            expect = "META"
        elif "1.1 条件原子" in h:
            expect = "COND_ATOM"
        elif "1.2 条件组合" in h:
            expect = "RULESET"
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
        if header != CANON[expect]:
            v.append(("VARIANT_COLS", f"header mismatch for {expect} under: {h}"))
            continue
        for r in t["rows"]:
            if len(r) != len(t["header"]):
                v.append(("VARIANT_COLS", f"row width != header width under: {h}"))
                break

        if expect == "COND_ATOM" and not routed:
            v.append(("GROUPFORM", "condition-atom table present but file declares NO-ROUTE topology"))
        if expect == "RULESET":
            if not routed:
                v.append(("GROUPFORM", "ruleset table present but file declares NO-ROUTE topology"))
            else:
                for r in t["rows"]:
                    rulesets_declared.add(norm_cell(r[0]))
        if expect == "BAKE":
            check_bake_rows(t["rows"], h, v)
        if expect == "ROUTING":
            if not any(norm_cell(r[1]) == "默认" for r in t["rows"]):
                v.append(("SHARE", "routing table lacks a 默认 default route row"))
            for r in t["rows"]:
                hit = norm_cell(r[1])
                target = norm_cell(r[2])
                if target and target != "NormalFeeding":
                    routing_groups.add(target)
                if hit == "默认":
                    continue
                if not hit.startswith("@"):
                    v.append(("REFS", f"non-default route hit without @ruleset reference: {hit}"))
                elif norm_cell(hit)[1:] not in rulesets_declared:
                    v.append(("REFS", f"routing hit references ruleset not declared in 1.2 条件组合: {hit}"))
            if routed:
                if MIGRATION_GROUP not in routing_groups:
                    v.append(("GROUPFORM", "MIGRATION-ROUTED file must route a MigrationReaction Group (G2 precedent)"))
                for r in t["rows"]:
                    if norm_cell(r[2]) == MIGRATION_GROUP and not norm_cell(r[4]).startswith("@"):
                        v.append(("SHARE", "MigrationReaction route weight parameter must be an @share reference"))
            else:
                for r in t["rows"]:
                    if norm_cell(r[2]) != "NormalFeeding":
                        v.append(("GROUPFORM", f"NO-ROUTE file must not carry Special Group route: {r[2]}"))

    # SHARE: every fence that computes SpecialShareTotal must validate it
    for f in fences:
        body = "\n".join(f)
        if "SpecialShareTotal" in body:
            if "SpecialShareTotal > 1" not in body:
                v.append(("SHARE", "share script missing SpecialShareTotal > 1 validation"))
            if "不静默归一化" not in body:
                v.append(("SHARE", "share script missing 不静默归一化 validation note"))

    # REACTPATH / RT1OFF by topology
    sec3 = section_text(text, 3, 4)
    if routed:
        if MIGRATION_GROUP not in sec3:
            v.append(("REACTPATH", "Response section missing MigrationReaction Group program"))
        elif FEEDING_SUPPRESS not in sec3:
            v.append(("REACTPATH", f'MigrationReaction Response missing "{FEEDING_SUPPRESS}" suppression statement (R06/R10 停食判例)'))
        elif FEEDING_CLOSURE not in sec3:
            v.append(("REACTPATH", f'MigrationReaction Response missing structural closure line "{FEEDING_CLOSURE}" (§8.8 Typed Result 先例)'))
    else:
        if RT1OFF_MARK not in sec3:
            v.append(("RT1OFF", f'section 3 missing "{RT1OFF_MARK}" declaration (R-T1 shape marker)'))

    # QUALITYCOV: binding table covers every routed Group
    sec4 = section_text(text, 4, 5)
    bind_groups = set()
    for t in tables:
        if t["start"] >= body_start and "4.1 模板绑定" in t["heading"]:
            for r in t["rows"]:
                if r and r[0].strip():
                    bind_groups.add(norm_cell(r[0]))
    for g in sorted(routing_groups - bind_groups):
        v.append(("QUALITYCOV", f"Quality binding table does not cover routed Group: {g}"))

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

    # BAN: forbidden phrases outright; vague merge without operator annotation
    for p in BAN_PHRASES:
        if p in text:
            v.append(("BAN", f"forbidden phrase present: {p}"))
    for f in fences:
        body = "\n".join(f)
        if any(p in body for p in MERGE_PHRASES) and "算子标注" not in body:
            v.append(("BAN", "merge phrase inside a script fence without 算子标注 operator annotation"))

    return v


FIXTURE = """# 测试鲑（Test Salmon｜Salmo testus）｜Migration/生活史系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批） |
| 基线 | SNAPSHOT_ONLY |

## 0. 上游语义与洄游形态

- 洄游形态：测试用湖海洄游。
- 证据档：Tier B（handoff 点名 + 摘要批注；Story 正文 [需正文]）。

Profile 引用清单：@TSMigrationReactionEligible @TSMigrationStages @TSMigrationWaterTypes @TSMigrationReactionShare @TSMigrationSpatialProfile @TSSubstratePreyFields @TSDietClasses @TSSizeWindow @TSNormalFeedingProfile @TSMigrationReactionProfile @TSMigrationEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 条件原子（变体 V2：条件组/条件/事实·计算项/参数/比较符/比较值）

| 条件组 | 条件 | 事实 / 计算项 | 参数 | 比较符 | 比较值 |
|---|---|---|---|---|---|
| TS1 | C1 | 当前洄游 / 繁殖阶段事实 | — | IN | @TSMigrationStages |
| TS1 | C2 | 当前水体类型 | — | IN | @TSMigrationWaterTypes |

### 1.2 条件组合（变体 R2：规则集/组合方式/引用）

| 规则集 | 组合方式 | 引用 |
|---|---|---|
| TSMigrationReactionEligible | AND | TS1.C1, TS1.C2 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| TS_Migration_Route | @TSMigrationReactionEligible | MigrationReaction | 按配置分流 | @TSMigrationReactionShare |
| TS_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前洄游 / 繁殖阶段事实
读取 当前水体类型

如果 阶段事实 IN @TSMigrationStages 并且 水体类型 IN @TSMigrationWaterTypes：
    MigrationReactionShare = @TSMigrationReactionShare
否则：
    MigrationReactionShare = 0

SpecialShareTotal = MigrationReactionShare

如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）——Share 契约（live §7）

NormalFeedingShare = 1 - SpecialShareTotal

返回 MigrationReactionShare / NormalFeedingShare
```

## 2. Bake

### 2.1 NormalFeeding Group｜配置表

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |
| FactorType(typed) | habitat_factor：洄游阶段空间重排（海洋觅食区↔产卵河段位置轴；typed 实例） |
| FactorBinding | lifecycle premise：OCEAN/MIGRATION/SPAWN 配置级切换（值域由 Profile 层定值；不建 body 分支） |
| SpatialSlotProfile | @TSMigrationSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TSSubstratePreyFields；diet_classes=@TSDietClasses；size_window=@TSSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@TSMigrationSpatialProfile（handoff 指定读法；两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的位置轴事实（洄游阶段绑定的空间轴）
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：
      prey_fields=@TSSubstratePreyFields 绑定的 prey class 生物量，
      经 diet_classes=@TSDietClasses 食性过滤
      与 size_window=@TSSizeWindow 口径过滤——在场可食生物量，未经感知/捕获修正）
读取 当前 premise（OCEAN/MIGRATION/SPAWN——上游 lifecycle trait，配置级切换因子集）

EVAL_TYPED_FIELD_OR_FACTOR：
    用位置轴事实查询 @TSMigrationSpatialProfile
    得到 MigrationSpatialFit（单 typed 因子评估）

NORMALIZE_WEIGHT：
    对 MigrationSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight（单因子链结束：无 gate、无 early return、无 combine 步
——族 forbidden_freedoms 边界；多因子组合属 PLAIN 族域，硬约束属 HARD_GATED 族域）
```

### 2.3 MigrationReaction Group｜无独立 Bake 程序（显式声明）

Reaction 不要求独立 Bake（live §17.1 先例）；洄游期空间重排由 Normal 面 premise 配置切换承载。

### 2.4 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（双 Group 双 Path；R06/R10 FR3 停食判例：P05 状态 × Response multi-path）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @TSNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |
| MigrationReaction | R-T1 单通道（Reaction；非摄食 Provocation） | @TSMigrationReactionProfile | 返回 ReactionResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本（双 Path 结构完全展开）

NormalFeeding Group：

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @TSNormalFeedingProfile
    得到 FoodEvaluation

DECIDE_RESPONSE：
    按 FoodEvaluation 决定响应档位

返回 Response(TargetFeeding)

Reaction 槽 OFF
```

MigrationReaction Group：

```plain text
读取 当前离散目标的非摄食 Provocation 事实（入侵/挑衅 Cue：突然性、贴近度、侵扰持续性）

普通 Feeding 强抑制或关闭（停食证据 [需正文]；Typed Result=档位关闭而非数值归零——
@TSMigrationReactionProfile 值域内若产品要求保留残值则 Cap 形态，数值 Profile 层定值）

EVAL_TARGET_AS_INTRUDER_TYPED：
    用 Provocation 事实评价 @TSMigrationReactionProfile
    得到 ProvocationEvaluation

DECIDE_RESPONSE：
    按 ProvocationEvaluation 决定响应档位

返回 Response(Reaction)

不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program——live §8.8 Typed Result 先例）
```

## 4. Quality Selection

### 4.1 模板绑定（live §12.2 形态；Q-T1）

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | 普通 Species Base（@SpeciesBaseQualityProfile） |
| MigrationReaction | QT-1 | @TSMigrationEligibilityByQuality | @NeutralAffinity | 洄游期成熟个体组成方向（值域 Profile 层定值） |

### 4.2 品质调整表

本鱼无已确认的物种级品质 Modifier；全局 Presentation / Context Modifier 属 live §12.3 跨鱼资产，不在本文件重复。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 当前 FishGroup（NormalFeeding 或 MigrationReaction）

对每个品质：
    读取该品质的 GroupEligibilityFactor（NormalFeeding 行查 @NeutralEligibility；MigrationReaction 行查 @TSMigrationEligibilityByQuality）
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

- 使用的自由度：G2 MigrationReaction share-vector 路由（live 样板）；SINGLE 族投影标签；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：(1) R-T2 折叠候选（Normal/Migration 两 Group 各 R-T1 vs 单程序双 Channel——live §13.3 自身未闭合，本批按 G2 分群语义表达，折叠归机制侧）；(2) 合并算子（无 combine 步；OPERATOR UNDEFINED）；(3) 数值与 Profile 值域不冻结。

BATCH_ID: REP-FULL-MIGRA-001
"""

FIXTURE_NOROUTE = """# 测试湖鱼（Test Lakefish｜Lacus testus）｜Migration/生活史系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-MIGRA-001（Migration/生活史系＝P05 全样本 第 3 批） |
| 基线 | SNAPSHOT_ONLY |

## 0. 上游语义与洄游形态

- 洄游形态：测试用季节位移。

Profile 引用清单：@TLSeasonSpatialProfile @TLSubstratePreyFields @TLDietClasses @TLSizeWindow @TLNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达（G-T1 DECLARATIVE ROUTING VECTOR 的退化形：空 Special 集 + 默认路由）。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| TL_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生空间程序｜配置表

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |
| FactorType(typed) | habitat_factor：季节位置轴（近岸↔深水；typed 实例） |
| FactorBinding | lifecycle premise：season 配置级切换（值域由 Profile 层定值；不建 body 分支） |
| SpatialSlotProfile | @TLSeasonSpatialProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TLSubstratePreyFields；diet_classes=@TLDietClasses；size_window=@TLSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot=@TLSeasonSpatialProfile（两层 reconciliation OPEN——README §3 登记） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的位置轴事实
读取 当前格子的可食资源原始事实
    （UsableForageAvailability 契约输出：prey_fields=@TLSubstratePreyFields，
      diet_classes=@TLDietClasses，size_window=@TLSizeWindow 过滤后在场生物量）
读取 当前 premise（season——上游 trait，配置级切换因子集）

EVAL_TYPED_FIELD_OR_FACTOR：
    用位置轴事实查询 @TLSeasonSpatialProfile
    得到 SeasonSpatialFit

NORMALIZE_WEIGHT：
    对 SeasonSpatialFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight
```

### 2.3 live 层投影声明

census SINGLE 族与 live 句型层 reconciliation OPEN（README §3 登记 1）。

## 3. Response

### 3.1 配置表（R-T1 单通道，Channel=Feeding）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @TLNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标（钩饵 Presentation 事实：尺寸、速度/轨迹、水层与相对位置）

EVAL_TARGET_AS_FOOD_TYPED：
    用目标事实评价 @TLNormalFeedingProfile
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

- 使用的自由度：SINGLE 族投影标签；Profile 命名；伪脚本步序（canonical 两步固定）。
- 放弃的自由度：合并算子（无 combine 步；OPERATOR UNDEFINED）；数值与 Profile 值域不冻结。

BATCH_ID: REP-FULL-MIGRA-001
"""


def run_selftest():
    cases = []

    def case(name, mutate, expect, fixture=FIXTURE):
        cases.append((name, mutate, expect, fixture))

    case("baseline (routed) passes unchanged", lambda s: s, None)
    case("baseline (no-route) passes unchanged", lambda s: s, None, FIXTURE_NOROUTE)
    case("HEADER fires on missing NOT AUTHORITY", lambda s: s.replace("NOT AUTHORITY", "X"), "HEADER")
    case("HEADER fires on missing BATCH_ID line", lambda s: s.replace("BATCH_ID: REP-FULL-MIGRA-001", "BATCH_ID: other"), "HEADER")
    case("SECTIONS fires on missing Bake section", lambda s: s.replace("## 2. Bake", "## X. Bake"), "SECTIONS")
    case("GROUPFORM fires when 1.1 loses both topologies", lambda s: s.replace("### 1.1 条件原子（变体 V2：条件组/条件/事实·计算项/参数/比较符/比较值）", "### 1.1 路由条件原子（形态不明）"), "GROUPFORM")
    case("GROUPFORM fires when NO-ROUTE file gains a Special Group route", lambda s: s.replace("| TL_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |", "| TL_Mig | @TLAny | MigrationReaction | 按配置分流 | @TLShare |\n| TL_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |", ), "GROUPFORM", FIXTURE_NOROUTE)
    case("GROUPFORM fires when routed file loses MigrationReaction Group", lambda s: s.replace("| TS_Migration_Route | @TSMigrationReactionEligible | MigrationReaction | 按配置分流 | @TSMigrationReactionShare |", "| TS_Migration_Route | @TSMigrationReactionEligible | MigrationFeeding | 按配置分流 | @TSMigrationReactionShare |"), "GROUPFORM")
    case("SHARE fires on missing default route", lambda s: s.replace("| TS_Default | 默认 |", "| TS_Default | @TSMigrationReactionEligible |"), "SHARE")
    case("SHARE fires on missing validation block", lambda s: s.replace("如果 SpecialShareTotal > 1：\n    报配置错误并停止（不静默归一化）——Share 契约（live §7）\n", ""), "SHARE")
    case("SHARE fires on non-@ MigrationReaction share parameter", lambda s: s.replace("按配置分流 | @TSMigrationReactionShare", "按配置分流 | 0.3"), "SHARE")
    case("REFS fires on undeclared ruleset reference", lambda s: s.replace("@TSMigrationReactionEligible | MigrationReaction", "@TSNopeEligible | MigrationReaction"), "REFS")
    case("BAKEFAM fires on value outside closed enum", lambda s: s.replace("BA-MIGRATION-SINGLE（本批投影标签", "BA-MIGRATION-MAGIC（本批投影标签"), "BAKEFAM")
    case("BAKEFAM fires on missing BakeTemplate row", lambda s: s.replace("| BakeTemplate | BA-MIGRATION-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |\n", ""), "BAKEFAM")
    case("FAMCTX fires on SINGLE carrying CombineRule row", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n| CombineRule | Template-fixed |"), "FAMCTX")
    case("FAMCTX fires on PLAIN missing Factor2 row", lambda s: s.replace("BA-MIGRATION-SINGLE（本批投影标签", "BA-MIGRATION-PLAIN（本批投影标签").replace("| FactorType(typed) | habitat_factor：洄游阶段空间重排（海洋觅食区↔产卵河段位置轴；typed 实例） |", "| Factor1Type(typed) | habitat_factor：温度 |").replace("| SpatialSlotProfile | @TSMigrationSpatialProfile |\n", "").replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |"), "FAMCTX")
    case("FAMCTX fires on GATED missing SurfaceGate row", lambda s: s.replace("BA-MIGRATION-SINGLE（本批投影标签", "BA-MIGRATION-GATED（本批投影标签").replace("| FactorType(typed) | habitat_factor：洄游阶段空间重排（海洋觅食区↔产卵河段位置轴；typed 实例） |", "| FactorSet(typed) | 静水/结构/猎物 |").replace("| SpatialSlotProfile | @TSMigrationSpatialProfile |\n", "").replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |", "| CombineRule | Template-fixed（数学 OPERATOR UNDEFINED 待机制侧） |"), "FAMCTX")
    case("PREMBIND fires on missing FactorBinding row", lambda s: s.replace("| FactorBinding | lifecycle premise：OCEAN/MIGRATION/SPAWN 配置级切换（值域由 Profile 层定值；不建 body 分支） |\n", ""), "PREMBIND")
    case("PREMBIND fires on binding without premise", lambda s: s.replace("| FactorBinding | lifecycle premise：OCEAN/MIGRATION/SPAWN 配置级切换（值域由 Profile 层定值；不建 body 分支） |", "| FactorBinding | 常年绑定 |"), "PREMBIND")
    case("REACTPATH fires on missing suppression statement", lambda s: s.replace("普通 Feeding 强抑制或关闭（停食证据 [需正文]", "普通 Feeding 处理（停食证据 [需正文]"), "REACTPATH")
    case("REACTPATH fires on missing structural Feeding closure", lambda s: s.replace("不再评价普通 Feeding（结构性关闭：Feeding evaluator 不进入该 Group Program——live §8.8 Typed Result 先例）", "不评价 Feeding 了"), "REACTPATH")
    case("RT1OFF fires on missing Reaction-slot-OFF marker", lambda s: s.replace("Reaction 槽 OFF", "反应槽关"), "RT1OFF", FIXTURE_NOROUTE)
    case("QUALITYCOV fires when binding table misses a routed Group", lambda s: s.replace("| MigrationReaction | QT-1 | @TSMigrationEligibilityByQuality | @NeutralAffinity | 洄游期成熟个体组成方向（值域 Profile 层定值） |\n", ""), "QUALITYCOV")
    case("PROFILES fires on used-but-unlisted token", lambda s: s.replace(" @TSSizeWindow", "", 1), "PROFILES")
    case("PROFILES fires on listed-but-unused token", lambda s: s.replace("Profile 引用清单：@TSMigrationReactionEligible", "Profile 引用清单：@TSUnusedToken @TSMigrationReactionEligible"), "PROFILES")
    case("BAN fires on forbidden phrase LifecycleCohort", lambda s: s + "\nLifecycleCohort 提及\n", "BAN")
    case("BAN fires on forbidden phrase Runtime Stage Selector", lambda s: s + "\nRuntime Stage Selector 提及\n", "BAN")
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
            if expect is None:
                passed = not v
            else:
                passed = expect in fams
            if not passed:
                ok = False
            print(f"[{'OK  ' if passed else 'FAIL'}] {name}" + ("" if passed else f" -> violations={v}"))
        # exempt-file behavior
        f = tmp / "exempt.md"
        f.write_text("# 退回档\n\nINSUFFICIENT_LOCAL_EVIDENCE 说明。\n\nStatus：WORKING / NOT AUTHORITY / NOT PROMOTED\n\nSNAPSHOT_ONLY。\n\nBATCH_ID: REP-FULL-MIGRA-001\n", encoding="utf-8")
        v = check_file(f)
        passed = not v
        ok = ok and passed
        print(f"[{'OK  ' if passed else 'FAIL'}] exempt INSUFFICIENT_LOCAL_EVIDENCE file only needs header markers" + ("" if passed else f" -> {v}"))
        print(f"== selftest ==\n{'SELFTEST PASS' if ok else 'SELFTEST FAIL'}")
        return ok


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        sys.exit(0 if run_selftest() else 1)
    if len(sys.argv) < 2:
        print("usage: validate_migration.py <migration_dir> | --selftest")
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
    # README cross-check
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
