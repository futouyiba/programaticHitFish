#!/usr/bin/env python3
# REP-FULL-P02-001 structural validator for Resource-Patch-system (P02) four-surface
# authoring files. Pure standard library. Adapted from validate_grazing.py with
# batch-specific checkpoints:
#   - NOROUTE: every file must carry the explicit "no Special Group routing program"
#     declaration in section 1 (this batch is uniform single-NormalFeeding-group).
#   - BAKEFAM: BakeTemplate value is a CLOSED enum of batch projection labels
#     {BA-P02-SINGLE, BA-P02-PLAIN} (census SINGLE_FACTOR_NORMALIZED_WEIGHT /
#     PLAIN_FACTOR_COMBINE projections; a new value is a spec action, not an
#     authoring action). NOTE: zero PATCH projection in this batch — census froze
#     all four P02 Bake programs as SINGLE (x3) / PLAIN (x1), so a PATCH label is
#     not expressible here (family flip on HRQ-B1-02 is a spec action).
#   - FAMCTX: census family boundary enforced at representation layer —
#     SINGLE requires FactorType(typed) + Normalization(NORMALIZE_WEIGHT), forbids
#     Factor1/2/CombineRule rows (multi-factor is PLAIN domain);
#     PLAIN requires Factor1Type + Factor2Type + CombineRule(COMBINE_WEIGHTED with
#     OPERATOR UNDEFINED annotation), forbids single FactorType row (SINGLE domain)
#     and Normalization row (no normalize step in PLAIN canonical body);
#     both forbid ContextConstraint / context profile rows (typed context step is
#     PATCH-family domain; this batch carries zero PATCH projection).
#   - CONTRACT: Bake input must reference the UsableForageAvailability contract.
#   - BAKEROWS: bake config row keys are a closed set (anti row-key injection).
#   - RT1OFF: Response section must declare the Reaction slot OFF (R-T1 shape).
# Selftest proves every check family fires on bad input.
import io
import re
import sys
import tempfile
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BATCH_ID = "REP-FULL-P02-001"

CANON = {
    "ROUTING": ["规则集", "命中条件", "目标Group", "权重处理", "权重参数"],
    "QUALITY_BIND": ["FishGroup", "QualityTemplate", "EligibilityProfile", "GroupAffinityProfile", "说明"],
    "RESP": ["Group", "响应模板", "条件/Profile", "命中结果", "未命中"],
    "BAKE": ["字段", "值"],
    "META": ["项", "值"],
}

BAKE_TEMPLATE_ENUM = ("BA-P02-SINGLE", "BA-P02-PLAIN")
CONTEXT_PROFILE_FIELDS = ("ZoneConstraintProfile", "CurrentContextProfile")
BAKE_FIELD_ENUM = {
    "BakeTemplate",
    "FactorType(typed)",
    "Factor1Type(typed)",
    "Factor2Type(typed)",
    "FactorBinding",
    "Normalization",
    "CombineRule",
    "Bake输入契约",
    "LiveLayerProjection",
    "ContextConstraint(typed)",
    "ZoneConstraintProfile",
    "CurrentContextProfile",
}

MERGE_PHRASES = ("固定规则合并", "固定组合规则", "固定汇总", "固定聚合", "按模板固定规则")
NOROUTE_MARK = "无 Special Group 路由程序"
RT1OFF_MARK = "Reaction 槽 OFF"


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
    """rows: list of [field, value]; enforce BAKEFAM / FAMCTX / NORMALIZE / CONTRACT / BAKEROWS."""
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
    val = norm_cell(kv["BakeTemplate"])
    m = re.match(r"BA-P02-(SINGLE|PLAIN)", val)
    if not m:
        v.append(("BAKEFAM", f"BakeTemplate not in closed enum {BAKE_TEMPLATE_ENUM}: {kv['BakeTemplate']}"))
        return
    fam = m.group(0)
    # typed context step is PATCH-family domain; this batch has zero PATCH projection
    if "ContextConstraint(typed)" in kv:
        v.append(("FAMCTX", f"{fam} must not carry ContextConstraint row (typed context step is PATCH-family domain; zero PATCH projection in this batch)"))
    ctx_profiles = [f for f in CONTEXT_PROFILE_FIELDS if f in kv]
    if ctx_profiles:
        v.append(("FAMCTX", f"{fam} must not carry context profile rows ({', '.join(ctx_profiles)})"))
    if fam == "BA-P02-SINGLE":
        if "FactorType(typed)" not in kv:
            v.append(("FAMCTX", "SINGLE template missing FactorType(typed) row"))
        for f in ("Factor1Type(typed)", "Factor2Type(typed)", "CombineRule"):
            if f in kv:
                v.append(("FAMCTX", f"SINGLE template must not carry {f} row (multi-factor combine is PLAIN-family domain)"))
        if "Normalization" not in kv or "NORMALIZE_WEIGHT" not in kv.get("Normalization", ""):
            v.append(("NORMALIZE", "bake table missing Normalization row with family constant NORMALIZE_WEIGHT"))
    else:  # BA-P02-PLAIN
        for f in ("Factor1Type(typed)", "Factor2Type(typed)"):
            if f not in kv:
                v.append(("FAMCTX", f"PLAIN template missing {f} row"))
        if "FactorType(typed)" in kv:
            v.append(("FAMCTX", "PLAIN template must not carry single FactorType row (single-factor chain is SINGLE-family domain)"))
        if "CombineRule" not in kv:
            v.append(("FAMCTX", "PLAIN template missing CombineRule row"))
        else:
            cr = kv.get("CombineRule", "")
            if "COMBINE_WEIGHTED" not in cr or "OPERATOR UNDEFINED" not in cr:
                v.append(("FAMCTX", "PLAIN CombineRule must be template-fixed COMBINE_WEIGHTED with OPERATOR UNDEFINED annotation"))
        if "Normalization" in kv:
            v.append(("FAMCTX", "PLAIN template must not carry Normalization row (no normalize step in PLAIN canonical body)"))
    if "UsableForageAvailability" not in kv.get("Bake输入契约", ""):
        v.append(("CONTRACT", "bake table missing Bake 输入契约 row referencing UsableForageAvailability"))


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

    # NOROUTE: explicit no-routing-program declaration in the 1.1 prose block
    m11 = re.search(r"^### 1\.1.*?(?=^### 1\.2|^## 2\.)", text, re.M | re.S)
    if not m11 or NOROUTE_MARK not in m11.group(0):
        v.append(("NOROUTE", f'section 1.1 block missing explicit declaration "{NOROUTE_MARK}"'))

    body_start = next((i for i, l in enumerate(lines) if l.startswith("## 1.")), len(lines))

    for t in tables:
        h = t["heading"]
        header = [norm_cell(c) for c in t["header"]]
        if t["start"] < body_start:
            expect = "META"
        elif "1.2 分群结果" in h:
            expect = "ROUTING"
        elif "2.1" in h and "配置表" in h:
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

        if expect == "BAKE":
            check_bake_rows(t["rows"], h, v)

        if expect == "ROUTING":
            if not any(norm_cell(r[1]) == "默认" for r in t["rows"]):
                v.append(("SHARE", "routing table lacks a 默认 default route row"))
            for r in t["rows"]:
                hit = norm_cell(r[1])
                if hit == "默认":
                    continue
                if not hit.startswith("@"):
                    v.append(("REFS", f"non-default route hit without @ruleset reference: {hit}"))
                # no 1.2 ruleset tables exist in this batch: any @ruleset hit is undeclared
                else:
                    v.append(("REFS", f"routing hit references ruleset, but no 1.2 条件组合 table exists to declare it: {hit}"))

    # SHARE: every fence that computes SpecialShareTotal must validate it
    for f in fences:
        body = "\n".join(f)
        if "SpecialShareTotal" in body:
            if "SpecialShareTotal > 1" not in body:
                v.append(("SHARE", "share script missing SpecialShareTotal > 1 validation"))
            if "不静默归一化" not in body:
                v.append(("SHARE", "share script missing 不静默归一化 validation note"))

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

    # BAN: vague merge without operator annotation; forbidden phrase outright
    if "组合适应度" in text:
        v.append(("BAN", "forbidden vague phrase 组合适应度 present"))
    for f in fences:
        body = "\n".join(f)
        if any(p in body for p in MERGE_PHRASES) and "算子标注" not in body:
            v.append(("BAN", "merge phrase inside a script fence without 算子标注 operator annotation"))

    # RT1OFF: Response section declares Reaction slot OFF (R-T1 single-channel shape)
    sec3 = section_text(text, 3, 4)
    if RT1OFF_MARK not in sec3:
        v.append(("RT1OFF", f'section 3 missing "{RT1OFF_MARK}" declaration (R-T1 shape marker)'))

    return v


BAKE_SINGLE_BLOCK = """| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P02-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |
| FactorType(typed) | resource_patch：测试底栖猎物 patch 轴（typed 实例） |
| FactorBinding | 常年绑定 |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TPPreyFields；diet_classes=@TPDietClasses；size_window=@TPSizeWindow） |
| LiveLayerProjection | BA-T1 底板 + DynamicSpatialSlot（两层 reconciliation OPEN） |"""

BAKE_PLAIN_BLOCK = """| 字段 | 值 |
|---|---|
| BakeTemplate | BA-P02-PLAIN（本批投影标签＝census PLAIN_FACTOR_COMBINE，registry v4；typed 因子集→组合） |
| Factor1Type(typed) | resource_patch：测试食物位置轴 |
| Factor2Type(typed) | habitat_factor：测试结构轴 |
| FactorBinding | 常年绑定 |
| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TPPreyFields；diet_classes=@TPDietClasses；size_window=@TPSizeWindow） |
| LiveLayerProjection | B-T1 Independent Factor Set（两层 reconciliation OPEN） |"""


def _plain(s):
    return s.replace(BAKE_SINGLE_BLOCK, BAKE_PLAIN_BLOCK)


FIXTURE = f"""# 测试斑鲤（Test Patchfish｜Testus patchus）｜Resource Patch 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-P02-001（Resource Patch→Discrete Target→TargetFeeding 系＝P02 补批 第 7 批） |
| 基线 | SNAPSHOT_ONLY |

## 0. 上游语义与资源斑块形态

- 资源斑块形态：测试用底栖猎物 patch 追随。

Profile 引用清单：@TPBenthicPatchProfile @TPPreyFields @TPDietClasses @TPSizeWindow @TPNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| TestPatchfish_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

{BAKE_SINGLE_BLOCK}

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的底栖猎物 patch 轴事实
读取 当前格子的可食资源原始事实（UsableForageAvailability 契约输出：prey_fields=@TPPreyFields，diet_classes=@TPDietClasses，size_window=@TPSizeWindow 过滤后在场生物量）

EVAL_TYPED_FIELD_OR_FACTOR：
    用 patch 轴事实查询 @TPBenthicPatchProfile
    得到 BenthicPatchFit

NORMALIZE_WEIGHT：
    对 BenthicPatchFit 执行模板固定归一化（族常量，非作者可选）

返回 SpatialDistributionWeight
（无 gate、无 early return、无 combine 步——族 forbidden_freedoms 边界）
```

### 2.3 live 层投影声明

BA-T1 底板与 DynamicSpatialSlot 的组合算子待机制侧。

## 3. Response

### 3.1 配置表（R-T1 单通道）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @TPNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标事实

EVAL_TARGET_AS_FOOD_TYPED：
    评价 @TPNormalFeedingProfile
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

本鱼无物种级品质 Modifier。

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
```

## 5. 自由度、边界与放弃项

- 放弃：合并算子数学 OPERATOR UNDEFINED。

BATCH_ID: REP-FULL-P02-001
"""


def run_selftest():
    cases = []

    def case(name, mutate, expect):
        cases.append((name, mutate, expect))

    case("baseline passes unchanged", lambda s: s, None)
    case("HEADER fires on missing NOT AUTHORITY", lambda s: s.replace("NOT AUTHORITY", "X"), "HEADER")
    case("HEADER fires on missing BATCH_ID line", lambda s: s.replace("BATCH_ID: REP-FULL-P02-001", "BATCH_ID: other"), "HEADER")
    case("SECTIONS fires on missing Bake section", lambda s: s.replace("## 2. Bake", "## X. Bake"), "SECTIONS")
    case("NOROUTE fires when 1.1 block loses declaration", lambda s: s.replace("### 1.1 路由条件原子｜无路由程序（显式声明）\n\n本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。", "### 1.1 路由条件原子｜无路由程序（显式声明）\n\n本鱼没有路由（声明被削弱测试）。"), "NOROUTE")
    case("SHARE fires on missing default route", lambda s: s.replace("| TestPatchfish_Default | 默认 |", "| TestPatchfish_Default | @TPEligible |"), "SHARE")
    case("SHARE fires on missing validation block", lambda s: s.replace("如果 SpecialShareTotal > 1：\n    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）\n", ""), "SHARE")
    case("REFS fires on @ruleset hit with no ruleset table", lambda s: s.replace("| TestPatchfish_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |", "| TestPatchfish_Default | @NopeEligible | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |"), "REFS")
    case("BAKEFAM fires on value outside closed enum", lambda s: s.replace("BA-P02-SINGLE（本批投影标签", "BA-P02-MAGIC（本批投影标签"), "BAKEFAM")
    case("BAKEFAM fires on PATCH label (zero PATCH projection this batch)", lambda s: s.replace("BA-P02-SINGLE（本批投影标签", "BA-P02-PATCH（本批投影标签"), "BAKEFAM")
    case("BAKEFAM fires on missing BakeTemplate row", lambda s: s.replace("| BakeTemplate | BA-P02-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |\n", ""), "BAKEFAM")
    case("FAMCTX fires on SINGLE missing FactorType row", lambda s: s.replace("| FactorType(typed) | resource_patch：测试底栖猎物 patch 轴（typed 实例） |\n", ""), "FAMCTX")
    case("FAMCTX fires on SINGLE carrying Factor1Type row (PLAIN domain)", lambda s: s.replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| Factor1Type(typed) | resource_patch：走私槽 |"), "FAMCTX")
    case("FAMCTX fires on SINGLE carrying CombineRule row", lambda s: s.replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |"), "FAMCTX")
    case("FAMCTX fires on SINGLE carrying ContextConstraint row (PATCH domain)", lambda s: s.replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| ContextConstraint(typed) | zone=bottom |"), "FAMCTX")
    case("FAMCTX fires on SINGLE carrying context profile row", lambda s: s.replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| ZoneConstraintProfile | @TPZone |"), "FAMCTX")
    case("FAMCTX fires on PLAIN missing Factor2Type row", lambda s: _plain(s).replace("| Factor2Type(typed) | habitat_factor：测试结构轴 |\n", ""), "FAMCTX")
    case("FAMCTX fires on PLAIN missing CombineRule row", lambda s: _plain(s).replace("| CombineRule | Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧） |\n", ""), "FAMCTX")
    case("FAMCTX fires on PLAIN CombineRule without OPERATOR UNDEFINED", lambda s: _plain(s).replace("Template-fixed COMBINE_WEIGHTED（数学 OPERATOR UNDEFINED 待机制侧）", "Template-fixed COMBINE_WEIGHTED（数学已定义随便算）"), "FAMCTX")
    case("FAMCTX fires on PLAIN carrying single FactorType row (SINGLE domain)", lambda s: _plain(s).replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| FactorType(typed) | resource_patch：走私单因子 |"), "FAMCTX")
    case("FAMCTX fires on PLAIN carrying Normalization row (no normalize step in PLAIN body)", lambda s: _plain(s).replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| Normalization | NORMALIZE_WEIGHT（族常量） |"), "FAMCTX")
    case("PLAIN variant of fixture passes (positive control)", _plain, None)
    case("NORMALIZE fires on missing Normalization row", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n", ""), "NORMALIZE")
    case("CONTRACT fires on missing forage contract reference", lambda s: s.replace("UsableForageAvailability（prey_fields=@TPPreyFields", "契约占位（prey_fields=@TPPreyFields"), "CONTRACT")
    case("PROFILES fires on used-but-unlisted token", lambda s: s.replace(" @TPSizeWindow", "", 1), "PROFILES")
    case("PROFILES fires on listed-but-unused token", lambda s: s.replace("Profile 引用清单：@TPBenthicPatchProfile", "Profile 引用清单：@TPUnusedToken @TPBenthicPatchProfile"), "PROFILES")
    case("BAN fires on forbidden phrase", lambda s: s + "\n组合适应度\n", "BAN")
    case("BAN fires on unannotated merge phrase in fence", lambda s: s + "\n```plain text\n按固定规则合并\n```\n", "BAN")
    case("RT1OFF fires on missing Reaction-slot-OFF marker", lambda s: s.replace("Reaction 槽 OFF", "反应槽关闭"), "RT1OFF")
    case("STRUCT fires on stray table", lambda s: s.replace("## 5. 自由度、边界与放弃项\n", "## 5. 自由度、边界与放弃项\n\n| 怪表 | 值 |\n|---|---|\n| x | y |\n"), "STRUCT")
    case("STRUCT fires on unknown bake config field", lambda s: s.replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| 随便字段 | x |"), "STRUCT")

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        ok = True
        for name, mutate, expect in cases:
            f = tmp / "fixture.md"
            f.write_text(mutate(FIXTURE), encoding="utf-8")
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
        f.write_text("# 退回档\n\nINSUFFICIENT_LOCAL_EVIDENCE 说明。\n\nStatus：WORKING / NOT AUTHORITY / NOT PROMOTED\n\nSNAPSHOT_ONLY。\n\nBATCH_ID: REP-FULL-P02-001\n", encoding="utf-8")
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
        print("usage: validate_patch.py <patch_dir> | --selftest")
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
