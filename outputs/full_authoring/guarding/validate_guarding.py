#!/usr/bin/env python3
# REP-FULL-GUARD-001 structural validator for Guarding-system four-surface authoring files.
# Pure standard library. Checks column-structure variants (V1-V4 / R1-R2), fixed 5-col
# routing table, reference closure (conditions / rulesets / @profiles), threshold
# @-referencing (no frozen numbers), banned vague-merge phrases without operator
# annotation, Defense-only structural closure marker, share-contract validation block,
# and section/header completeness. Selftest proves every check family fires.
import io
import re
import sys
import tempfile
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BATCH_ID = "REP-FULL-GUARD-001"

CANON = {
    "V1": ["条件组", "条件", "事实/计算项", "参数1", "比较符", "比较值1", "比较值2"],
    "V2": ["条件组", "条件", "事实/计算项", "参数", "比较符", "比较值"],
    "V3": ["条件组", "条件", "事实/计算项", "比较符", "比较值"],
    "V4": ["条件", "事实/计算项", "比较符", "比较值"],
    "R1": ["规则集", "组合方式", "显示顺序", "引用类型", "引用"],
    "R2": ["规则集", "组合方式", "引用"],
    "ROUTING": ["规则集", "命中条件", "目标Group", "权重处理", "权重参数"],
    "QUALITY_BIND": ["FishGroup", "QualityTemplate", "EligibilityProfile", "GroupAffinityProfile", "说明"],
    "RESP": ["Group", "响应模板", "条件/Profile", "命中结果", "未命中"],
    "BAKE": ["字段", "值"],
    "W1": ["命中条件", "调整对象", "调整方式", "参数"],
    "W2": ["品质规则", "命中条件", "调整对象", "调整方式", "参数"],
    "W3": ["规则集", "条件", "调整对象", "调整方式", "参数"],
    "META": ["项", "值"],
}
COND_VARIANTS = {"V1", "V2", "V3", "V4"}
MERGE_PHRASES = ("固定规则合并", "固定组合规则", "固定汇总", "固定聚合", "按模板固定规则")


def norm_cell(cell: str) -> str:
    return re.sub(r"[\s　]+", "", cell)


def parse_tables(lines):
    """Yield (heading, header_cells, data_rows, start_line) for each markdown table."""
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


def check_file(path: Path):
    v = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    exempt = "INSUFFICIENT_LOCAL_EVIDENCE" in text

    # HEADER
    for needle, fam in ((BATCH_ID, "HEADER"), ("NOT AUTHORITY", "HEADER"), ("SNAPSHOT_ONLY", "HEADER")):
        if needle not in text:
            v.append((fam, f"missing required marker: {needle}"))
    if not re.search(r"^BATCH_ID: REP-FULL-GUARD-001\s*$", text, re.M):
        v.append(("HEADER", "missing trailing BATCH_ID line"))

    if exempt:
        return v

    # SECTIONS
    for sec, title in ((1, "Group Routing"), (2, "Bake"), (3, "Response"), (4, "Quality Selection"), (5, "")):
        pat = rf"^## {sec}\." if not title else rf"^## {sec}\. {title}"
        if not re.search(pat, text, re.M):
            v.append(("SECTIONS", f"missing section ## {sec}. {title}".rstrip()))

    tables = parse_tables(lines)
    fences = parse_fences(lines)
    declared_conds, ruleset_names = set(), set()

    for t in tables:
        h = t["heading"]
        header = [norm_cell(c) for c in t["header"]]
        before_body = t["start"] < next((i for i, l in enumerate(lines) if l.startswith("## 1.")), len(lines))
        if before_body:
            expect = "META"
        elif "1.1 条件原子" in h:
            m = re.search(r"V[1-4]", h)
            expect = m.group(0) if m else None
            if expect is None:
                v.append(("VARIANT", f"condition-atom table lacks declared V-variant: {h}"))
        elif "1.2 条件组合" in h:
            m = re.search(r"R[12]", h)
            expect = m.group(0) if m else None
            if expect is None:
                v.append(("VARIANT", f"ruleset table lacks declared R-variant: {h}"))
        elif "1.3 分群结果" in h:
            expect = "ROUTING"
        elif re.match(r"^### 2\.[13].*配置表", h):
            expect = "BAKE"
        elif "3.1 配置表" in h:
            expect = "RESP"
        elif "4.1 模板绑定" in h:
            expect = "QUALITY_BIND"
        elif "4.2" in h:
            m = re.search(r"W[1-3]", h)
            if t["rows"] and not m:
                v.append(("VARIANT", f"quality table lacks declared W-variant: {h}"))
            expect = m.group(0) if m else None
        else:
            v.append(("STRUCT", f"table in undeclared location: {h or '(no heading)'}"))
            continue
        if expect and header != CANON[expect]:
            v.append(("VARIANT_COLS", f"header mismatch for {expect} under: {h}"))
            continue
        for r in t["rows"]:
            if len(r) != len(t["header"]):
                v.append(("VARIANT_COLS", f"row width != header width under: {h}"))
                break

        # collect refs
        if "1.1 条件原子" in h and expect in COND_VARIANTS:
            for r in t["rows"]:
                declared_conds.add(f"{norm_cell(r[0])}.{norm_cell(r[1])}")
        if "1.2 条件组合" in h:
            for r in t["rows"]:
                ruleset_names.add(norm_cell(r[0]))
        if "1.2 条件组合" in h and expect in ("R1", "R2"):
            ref_idx = 4 if expect == "R1" else 2
            for r in t["rows"]:
                ref = norm_cell(r[ref_idx])
                if ref not in declared_conds:
                    v.append(("REFS", f"ruleset references undeclared condition: {ref}"))
        if "1.3 分群结果" in h:
            if not any(norm_cell(r[1]) == "默认" for r in t["rows"]):
                v.append(("SHARE", "routing table lacks a 默认 default route row"))
            for r in t["rows"]:
                hit = norm_cell(r[1])
                if hit.startswith("@") and hit[1:] not in ruleset_names:
                    v.append(("REFS", f"routing hit references undeclared ruleset: {hit}"))

    # THRESHOLD: no frozen numbers in condition-atom compare/param cells
    wl_line = next((l for l in lines if l.startswith("字面量白名单")), "")
    wl_body = wl_line.split("：", 1)[1] if "：" in wl_line else wl_line.split(":", 1)[-1]
    whitelist = set()
    if "无" not in wl_body[:2]:
        whitelist = {norm_cell(x) for x in re.split(r"[、,，]", wl_body) if norm_cell(x)}
    for t in tables:
        if "1.1 条件原子" in t["heading"]:
            for r in t["rows"]:
                for idx in (3, 5, 6):
                    if idx >= len(r):
                        continue
                    c = norm_cell(r[idx])
                    if c in ("—", "—") or c == "":
                        continue
                    if re.fullmatch(r"@[A-Za-z_]\w*", c):
                        continue
                    if c in whitelist:
                        continue
                    v.append(("THRESHOLD", f"non-@ threshold/param value in condition atom: {r[0]}.{r[1]} col{idx+1} = {r[idx]}"))

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
        used -= {"@" + n for n in ruleset_names}
        listed = set(tokens)
        missing = used - listed
        unused = listed - used
        for m in sorted(missing):
            v.append(("PROFILES", f"@token used but not listed: {m}"))
        for m in sorted(unused):
            v.append(("PROFILES", f"@token listed but never used: {m}"))

    # BAN: vague merge without operator annotation; forbidden phrase outright
    if "组合适应度" in text:
        v.append(("BAN", "forbidden vague phrase 组合适应度 present"))
    for f in fences:
        body = "\n".join(f)
        if any(p in body for p in MERGE_PHRASES) and "算子标注" not in body:
            v.append(("BAN", "merge phrase inside a script fence without 算子标注 operator annotation"))

    # DEFENSE: Defense-only rows require structural closure phrase in section 3
    sec3 = section_text(text, 3, 4)
    for t in tables:
        if "3.1 配置表" in t["heading"]:
            for r in t["rows"]:
                if len(r) > 1 and "Defense-only" in r[1] and "不再评价普通 Feeding" not in sec3:
                    v.append(("DEFENSE", "Defense-only template row without structural closure phrase 不再评价普通 Feeding in section 3"))

    # SHARE: every fence that computes SpecialShareTotal must validate it
    for f in fences:
        body = "\n".join(f)
        if "SpecialShareTotal" in body:
            if "SpecialShareTotal > 1" not in body:
                v.append(("SHARE", "share script missing SpecialShareTotal > 1 validation"))
            if "不静默归一化" not in body:
                v.append(("SHARE", "share script missing 不静默归一化 validation note"))

    return v


FIXTURE = """# 测试鱼（Test Fish｜Testus testus）｜Guarding 系四面生产级表达

Status：WORKING / REPRESENTATION ARTIFACT / NOT AUTHORITY / NOT PROMOTED

| 项 | 值 |
|---|---|
| 批次 | REP-FULL-GUARD-001（Guarding 系＝P04 全样本 第 1 批） |
| 基线 | SNAPSHOT_ONLY |

## 0. 上游语义

Profile 引用清单：@TestSpawnWindowStart @TestSpawnWindowEnd @TestGuardWarmupDays @TestGuardTempThreshold @TestNestStructureSet @TestGuardingShare @TestLocalGuardAnchorEligibility @TestNestSuitabilityProfile @TestGuardRelationProfile @TestGuardLocalTemperatureProfile @TestGuardThreatProfile @TestNormalLayerProfile @TestNormalStructureProfile @TestNormalTemperatureProfile @TestNormalTimeProfile @TestNormalTempFloor @TestNormalFeedingProfile @TestGuardingEligibilityByQuality @NeutralEligibility @NeutralAffinity @SpeciesBaseQualityProfile

字面量白名单（本文件条件原子比较值允许的非 @ 取值）：无（全部 @ 引用）

## 1. Group Routing

### 1.1 条件原子（变体 V1：条件组/条件/事实·计算项/参数1/比较符/比较值1/比较值2）

| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |
|---|---|---|---|---|---|---|
| TT1 | C1 | 当前日期 | — | BETWEEN | @TestSpawnWindowStart | @TestSpawnWindowEnd |
| TT1 | C2 | 连续均温 | @TestGuardWarmupDays | >= | @TestGuardTempThreshold | — |
| TT1 | C3 | 场内结构集合 | — | CONTAINS_ANY | @TestNestStructureSet | — |

### 1.2 条件组合（变体 R1：规则集/组合方式/显示顺序/引用类型/引用）

| 规则集 | 组合方式 | 显示顺序 | 引用类型 | 引用 |
|---|---|---|---|---|
| TestGuardEligible | AND | 1 | Condition | TT1.C1 |
| TestGuardEligible | AND | 2 | Condition | TT1.C2 |
| TestGuardEligible | AND | 3 | Condition | TT1.C3 |

### 1.3 分群结果（5 列固定：规则集/命中条件/目标 Group/权重处理/权重参数）

| 规则集 | 命中条件 | 目标 Group | 权重处理 | 权重参数 |
|---|---|---|---|---|
| Test_Guard_Route | @TestGuardEligible | Guarding | Species 内行为份额 | @TestGuardingShare |
| Test_Default | 默认 | NormalFeeding | 承接剩余份额 | 1 - SpecialShareTotal |

### 1.4 Group 中文伪脚本

```plain text
读取 当前日期
如果 当前日期处于 [@TestSpawnWindowStart, @TestSpawnWindowEnd]：
    GuardingShare = @TestGuardingShare
否则：
    GuardingShare = 0
SpecialShareTotal = GuardingShare
如果 SpecialShareTotal > 1：
    报配置错误并停止（不静默归一化）
NormalFeedingShare = 1 - SpecialShareTotal
```

## 2. Bake

### 2.1 Guarding Group｜配置表

| 字段 | 值 |
|---|---|
| BakeTemplate | BA-GUARD-ANCHOR-GATE |
| GuardAnchorRelationProfile | @TestGuardRelationProfile |
| GuardAnchorSuitabilityProfile | @TestNestSuitabilityProfile |
| LocalTemperatureProfile | @TestGuardLocalTemperatureProfile |

### 2.2 中文伪脚本

```plain text
读取 结构
如果当前目标不满足 @TestLocalGuardAnchorEligibility：
    返回 0
按固定规则合并 RelationFit / AnchorSuitabilityFit
算子标注：OPERATOR UNDEFINED — 待机制侧
```

### 2.3 NormalFeeding Group｜配置表

| 字段 | 值 |
|---|---|
| LayerProfile | @TestNormalLayerProfile |
| StructureProfile | @TestNormalStructureProfile |
| TemperatureProfile | @TestNormalTemperatureProfile |
| TimeProfile | @TestNormalTimeProfile |
| ExtremeTemperatureGate | @TestNormalTempFloor |

## 3. Response

### 3.1 配置表

| Group | 响应模板 | 条件 / Profile | 命中结果 | 未命中 |
|---|---|---|---|---|
| Guarding | 顺序响应规则（Defense-only） | @TestGuardThreatProfile | 返回防御 Response | 返回低 / 无响应 |
| NormalFeeding | R-T1 单通道（Feeding） | @TestNormalFeedingProfile | 返回 FeedingResponse | 返回低 / 无响应 |

### 3.2 中文伪脚本

```plain text
评价 @TestGuardThreatProfile
返回 DefenseResponse
不再评价普通 Feeding（结构性关闭）
```

## 4. Quality Selection

### 4.1 模板绑定

| FishGroup | Quality Template | Eligibility Profile | Group Affinity Profile | 说明 |
|---|---|---|---|---|
| Guarding | QT-1 | @TestGuardingEligibilityByQuality | @NeutralAffinity | 成熟雄鱼组成 |
| NormalFeeding | QT-1 | @NeutralEligibility | @NeutralAffinity | Species Base |

### 4.3 中文伪脚本

```plain text
读取 当前 Species 的基础品质权重（@SpeciesBaseQualityProfile）
读取 GroupEligibilityFactor / GroupAffinityFactor
```

## 5. 自由度

- 放弃：合并算子数学 OPERATOR UNDEFINED。

BATCH_ID: REP-FULL-GUARD-001
"""


def run_selftest():
    cases = []

    def case(name, mutate, expect):
        cases.append((name, mutate, expect))

    case("baseline passes unchanged", lambda s: s, None)
    case("HEADER fires on missing NOT AUTHORITY", lambda s: s.replace("NOT AUTHORITY", "X"), "HEADER")
    case("HEADER fires on missing BATCH_ID line", lambda s: s.replace("BATCH_ID: REP-FULL-GUARD-001", "BATCH_ID: other"), "HEADER")
    case("SECTIONS fires on missing Bake section", lambda s: s.replace("## 2. Bake", "## X. Bake"), "SECTIONS")
    case("VARIANT fires on missing V-tag", lambda s: s.replace("（变体 V1：", "（", 1), "VARIANT")
    case("VARIANT_COLS fires on wrong V1 columns", lambda s: s.replace("| 条件组 | 条件 | 事实 / 计算项 | 参数1 | 比较符 | 比较值1 | 比较值2 |", "| 条件组 | 条件 | 事实 / 计算项 | 参数 | 比较符 | 比较值 |", 1), "VARIANT_COLS")
    case("REFS fires on undeclared condition ref", lambda s: s.replace("| TestGuardEligible | AND | 1 | Condition | TT1.C1 |", "| TestGuardEligible | AND | 1 | Condition | TT9.C1 |"), "REFS")
    case("REFS fires on undeclared ruleset in routing", lambda s: s.replace("@TestGuardEligible | Guarding", "@NopeEligible | Guarding"), "REFS")
    case("PROFILES fires on used-but-unlisted token", lambda s: s.replace("@TestNestSuitabilityProfile", "", 1), "PROFILES")
    case("PROFILES fires on listed-but-unused token", lambda s: s.replace(" @TestGuardLocalTemperatureProfile", "", 1), "PROFILES")
    case("THRESHOLD fires on bare numeric threshold", lambda s: s.replace("@TestGuardTempThreshold | —", "18 | —"), "THRESHOLD")
    case("BAN fires on forbidden phrase", lambda s: s + "\n组合适应度\n", "BAN")
    case("BAN fires on unannotated merge phrase", lambda s: s.replace("算子标注：OPERATOR UNDEFINED — 待机制侧", "注：细节略"), "BAN")
    case("DEFENSE fires on missing closure phrase", lambda s: s.replace("不再评价普通 Feeding（结构性关闭）", "返回即结束"), "DEFENSE")
    case("SHARE fires on missing default route", lambda s: s.replace("| Test_Default | 默认 |", "| Test_Default | @TestGuardEligible |"), "SHARE")
    case("SHARE fires on missing validation block", lambda s: s.replace("如果 SpecialShareTotal > 1：\n    报配置错误并停止（不静默归一化）\n", ""), "SHARE")
    case("STRUCT fires on stray table", lambda s: s.replace("## 5. 自由度\n", "## 5. 自由度\n\n| 怪表 | 值 |\n|---|---|\n| x | y |\n"), "STRUCT")

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
        f.write_text("# 退回档\n\nINSUFFICIENT_LOCAL_EVIDENCE 说明。\n\nStatus：WORKING / NOT AUTHORITY / NOT PROMOTED\n\nSNAPSHOT_ONLY。\n\nBATCH_ID: REP-FULL-GUARD-001\n", encoding="utf-8")
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
        print("usage: validate_guarding.py <guarding_dir> | --selftest")
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
