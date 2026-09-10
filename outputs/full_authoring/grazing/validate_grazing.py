#!/usr/bin/env python3
# REP-FULL-GRAZE-001 structural validator for Grazing/substrate-system four-surface
# authoring files. Pure standard library. Adapted from validate_guarding.py with
# batch-specific checkpoints:
#   - NOROUTE: every file must carry the explicit "no Special Group routing program"
#     declaration in section 1 (this batch is uniform single-NormalFeeding-group).
#   - BAKEFAM: BakeTemplate value is a CLOSED enum of batch projection labels
#     {BA-SUBSTRATE-SINGLE, BA-SUBSTRATE-PATCH} (census family projections; a new
#     value is a spec action, not an authoring action).
#   - PATCHCTX: census family boundary enforced at representation layer —
#     PATCH (census PATCH_RESOURCE_FOLLOWING, PROVISIONAL) requires the PROVISIONAL
#     marker, a ContextConstraint(typed) row, and exactly one context profile
#     (zone side ZoneConstraintProfile XOR current side CurrentContextProfile);
#     SINGLE (census SINGLE_FACTOR_NORMALIZED_WEIGHT) forbids all context rows.
#   - NORMALIZE: NORMALIZE_WEIGHT is a family constant row (not author-selectable).
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

BATCH_ID = "REP-FULL-GRAZE-001"

CANON = {
    "ROUTING": ["规则集", "命中条件", "目标Group", "权重处理", "权重参数"],
    "QUALITY_BIND": ["FishGroup", "QualityTemplate", "EligibilityProfile", "GroupAffinityProfile", "说明"],
    "RESP": ["Group", "响应模板", "条件/Profile", "命中结果", "未命中"],
    "BAKE": ["字段", "值"],
    "META": ["项", "值"],
}

BAKE_TEMPLATE_ENUM = ("BA-SUBSTRATE-SINGLE", "BA-SUBSTRATE-PATCH")
CONTEXT_PROFILE_FIELDS = ("ZoneConstraintProfile", "CurrentContextProfile")
BAKE_FIELD_ENUM = {
    "BakeTemplate",
    "PatchResourceType(typed)",
    "FactorType(typed)",
    "ContextConstraint(typed)",
    "ZoneConstraintProfile",
    "CurrentContextProfile",
    "SubstratePatchProfile",
    "FactorBinding",
    "Normalization",
    "Bake输入契约",
    "LiveLayerProjection",
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
    """rows: list of [field, value]; enforce BAKEFAM / PATCHCTX / NORMALIZE / CONTRACT / BAKEROWS."""
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
    m = re.match(r"BA-SUBSTRATE-(SINGLE|PATCH)", val)
    if not m:
        v.append(("BAKEFAM", f"BakeTemplate not in closed enum {BAKE_TEMPLATE_ENUM}: {kv['BakeTemplate']}"))
        return
    fam = m.group(0)
    has_ctx_row = "ContextConstraint(typed)" in kv
    ctx_profiles = [f for f in CONTEXT_PROFILE_FIELDS if f in kv]
    if fam == "BA-SUBSTRATE-PATCH":
        if "PROVISIONAL" not in kv["BakeTemplate"]:
            v.append(("PATCHCTX", "PATCH template cell missing PROVISIONAL marker (census family status must stay visible)"))
        if not has_ctx_row:
            v.append(("PATCHCTX", "PATCH template without ContextConstraint(typed) row"))
        if len(ctx_profiles) != 1:
            v.append(("PATCHCTX", f"PATCH requires exactly one context profile (zone XOR current side), found {len(ctx_profiles)}"))
    else:  # SINGLE
        if has_ctx_row:
            v.append(("PATCHCTX", "SINGLE template must not carry ContextConstraint row (typed context step is PATCH domain)"))
        if ctx_profiles:
            v.append(("PATCHCTX", f"SINGLE template must not carry context profile rows ({', '.join(ctx_profiles)})"))
    if "Normalization" not in kv or "NORMALIZE_WEIGHT" not in kv.get("Normalization", ""):
        v.append(("NORMALIZE", "bake table missing Normalization row with family constant NORMALIZE_WEIGHT"))
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


FIXTURE = """# 测试鲴（Test Grazer｜Testus grazus）｜Grazing 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GRAZE-001（Grazing/底质系＝P06 全样本 第 2 批） |
| 基线 | SNAPSHOT_ONLY |

## 0. 上游语义与底质处理形态

- 底质处理形态：测试用附着资源刮食。

Profile 引用清单：@TGSubstratePatchProfile @TGSubstrateSpatialProfile @TGSubstratePreyFields @TGDietClasses @TGSizeWindow @TGNormalFeedingProfile @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

## 1. Group Routing

### 1.1 路由条件原子｜无路由程序（显式声明）

本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。这不是省略 Group 面——单一 NormalFeeding Group、无条件路由是本鱼的完整 Group 表达。

### 1.2 分群结果（5 列固定：规则集/命中条件/目标Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| TestGrazer_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

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

### 2.1 Story 派生底质程序｜配置表

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-SUBSTRATE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |
| FactorType(typed) | resource_patch：附着藻/碎屑（typed 实例） |
| FactorBinding | 常年绑定 |
| SubstratePatchProfile | @TGSubstratePatchProfile |
| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |
| Bake 输入契约 | UsableForageAvailability（prey_fields=@TGSubstratePreyFields；diet_classes=@TGDietClasses；size_window=@TGSizeWindow） |
| LiveLayerProjection | BA-NORMAL-HABITAT-FIT + DynamicSpatialSlot=@TGSubstrateSpatialProfile（coverage delta K3 吸收读法；两层 reconciliation OPEN） |

### 2.2 中文伪脚本（完全展开）

```plain text
读取 当前格子的底质类型
读取 当前格子的基质资源原始事实（UsableForageAvailability 契约输出：prey_fields=@TGSubstratePreyFields，diet_classes=@TGDietClasses，size_window=@TGSizeWindow 过滤后在场生物量）

用基质资源事实查询 @TGSubstratePatchProfile
得到 SubstratePatchFit

对 SubstratePatchFit 执行 NORMALIZE_WEIGHT（族固定归一化）

返回 SpatialDistributionWeight
（无 gate、无 early return、无 combine 步——族 forbidden_freedoms 边界）
```

### 2.3 live 层投影声明

BA-T1 底板与 DynamicSpatialSlot 的组合算子待机制侧。

## 3. Response

### 3.1 配置表（R-T1 单通道）

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| NormalFeeding | R-T1 单通道（Feeding） | @TGNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
读取 当前离散目标事实

评价 @TGNormalFeedingProfile
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

BATCH_ID: REP-FULL-GRAZE-001
"""


def run_selftest():
    cases = []

    def case(name, mutate, expect):
        cases.append((name, mutate, expect))

    case("baseline passes unchanged", lambda s: s, None)
    case("HEADER fires on missing NOT AUTHORITY", lambda s: s.replace("NOT AUTHORITY", "X"), "HEADER")
    case("HEADER fires on missing BATCH_ID line", lambda s: s.replace("BATCH_ID: REP-FULL-GRAZE-001", "BATCH_ID: other"), "HEADER")
    case("SECTIONS fires on missing Bake section", lambda s: s.replace("## 2. Bake", "## X. Bake"), "SECTIONS")
    case("NOROUTE fires when 1.1 block loses declaration (marker only in script fence)", lambda s: s.replace("### 1.1 路由条件原子｜无路由程序（显式声明）\n\n本鱼无 Special Group 路由程序：不读取路由事实、不评价任何 Special Group 资格条件。", "### 1.1 路由条件原子｜无路由程序（显式声明）\n\n本鱼没有路由（声明被削弱测试）。"), "NOROUTE")
    case("SHARE fires on missing default route", lambda s: s.replace("| TestGrazer_Default | 默认 |", "| TestGrazer_Default | @TGEligible |"), "SHARE")
    case("SHARE fires on missing validation block", lambda s: s.replace("如果 SpecialShareTotal > 1：\n    报配置错误并停止（不静默归一化）——结构性不可达，保留 Share 契约校验位（live §7）\n", ""), "SHARE")
    case("REFS fires on @ruleset hit with no ruleset table", lambda s: s.replace("| TestGrazer_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |", "| TestGrazer_Default | @NopeEligible | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |"), "REFS")
    case("BAKEFAM fires on value outside closed enum", lambda s: s.replace("BA-SUBSTRATE-SINGLE（本批投影标签", "BA-SUBSTRATE-MAGIC（本批投影标签"), "BAKEFAM")
    case("BAKEFAM fires on missing BakeTemplate row", lambda s: s.replace("| BakeTemplate | BA-SUBSTRATE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化） |\n", ""), "BAKEFAM")
    case("PATCHCTX fires on PATCH without PROVISIONAL marker", lambda s: s.replace("BA-SUBSTRATE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化）", "BA-SUBSTRATE-PATCH（本批投影标签＝census PATCH_RESOURCE_FOLLOWING，registry v4；3 步带 typed context）"), "PATCHCTX")
    case("PATCHCTX fires on PATCH missing ContextConstraint row", lambda s: s.replace("BA-SUBSTRATE-SINGLE（本批投影标签＝census SINGLE_FACTOR_NORMALIZED_WEIGHT，registry v4；2 步单 typed 因子→归一化）", "BA-SUBSTRATE-PATCH（本批投影标签 PROVISIONAL；3 步带 typed context）"), "PATCHCTX")
    case("PATCHCTX fires on SINGLE carrying ContextConstraint row", lambda s: s.replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| ContextConstraint(typed) | zone=bottom |"), "PATCHCTX")
    case("PATCHCTX fires on SINGLE carrying context profile row", lambda s: s.replace("| FactorBinding | 常年绑定 |", "| FactorBinding | 常年绑定 |\n| ZoneConstraintProfile | @TGZone |"), "PATCHCTX")
    case("NORMALIZE fires on missing Normalization row", lambda s: s.replace("| Normalization | NORMALIZE_WEIGHT（族常量；非作者可选算子） |\n", ""), "NORMALIZE")
    case("CONTRACT fires on missing forage contract reference", lambda s: s.replace("UsableForageAvailability（prey_fields=@TGSubstratePreyFields", "契约占位（prey_fields=@TGSubstratePreyFields"), "CONTRACT")
    case("PROFILES fires on used-but-unlisted token", lambda s: s.replace(" @TGSizeWindow", "", 1), "PROFILES")
    case("PROFILES fires on listed-but-unused token", lambda s: s.replace("Profile 引用清单：@TGSubstratePatchProfile", "Profile 引用清单：@TGUnusedToken @TGSubstratePatchProfile"), "PROFILES")
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
        f.write_text("# 退回档\n\nINSUFFICIENT_LOCAL_EVIDENCE 说明。\n\nStatus：WORKING / NOT AUTHORITY / NOT PROMOTED\n\nSNAPSHOT_ONLY。\n\nBATCH_ID: REP-FULL-GRAZE-001\n", encoding="utf-8")
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
        print("usage: validate_grazing.py <grazing_dir> | --selftest")
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
