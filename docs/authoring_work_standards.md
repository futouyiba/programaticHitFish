# B 系列与 LT 系列工作标准规范

状态：**WORKING / GOVERNANCE STANDARD / 沉淀自 2026-09-10~11 全库实践**
本地规范源：本文件。Notion 镜像：Simplified V0 → Documentation Governance 分支下。
上位治理：`AGENTS.md`（scoped review verdict / 机制文档路由）+ `HARNESS_HANDOFF.md`（角色与状态机）。

## 1. B 系列（Representation 生产级表达）标准

### 1.1 条件原子（Group Routing 面）

每张条件表必须使用声明的变体（Stress Test R1 Grammar §5.1 V1-V4），**列结构固定**：

```text
V1 双值全列（7 列）：条件组 / 条件 / 事实·计算项 / 参数1 / 比较符 / 比较值1 / 比较值2
V2 单值（6 列）  ：条件组 / 条件 / 事实·计算项 / 参数 / 比较符 / 比较值
V3 无参数（5 列）：条件组 / 条件 / 事实·计算项 / 比较符 / 比较值
V4 无编号（4 列）：条件 / 事实·计算项 / 比较符 / 比较值
```

**条件必须原子化**，以下为标准形态：

```text
日期窗口     → 事实=当前日期, 比较符=BETWEEN, 值1=@SpawnWindowStart, 值2=@SpawnWindowEnd
持续条件     → 事实=连续均温, 参数=5天, 比较符=>=, 值1=@GuardTempThreshold
集合存在     → 事实=场内结构集合, 比较符=CONTAINS_ANY, 值1=@NestStructureSet
类型枚举     → 事实=洄游阶段, 比较符=IN, 值1=@MigrationStageEnum
布尔存在     → 事实=巢体已建成, 比较符=EXISTS
```

**禁止**：「满足护巢条件」「在繁殖期内」「结构合适」等非原子表述。

### 1.2 条件组合（RuleSet）

5 列结构（R1 全列 / R2 紧凑），AND/OR/NOT 显式，嵌套深度不限但须可追溯。

### 1.3 分群结果

5 列结构：规则集 / 命中条件 / 目标 Group / 权重处理 / 权重参数。
Share 契约：`SpecialShareTotal > 1` → 报 Validation Error 不静默归一化；Default Group 承接剩余。

### 1.4 伪脚本标准（Bake/Response/Quality 面）

- **完全展开**：每步具体（读取什么事实 / 查什么 Profile / 怎么合并）。
- **Early return 显式标注**：`如果 X 则返回 Y（EARLY_RETURN）`。
- **算子未定义显式**：`算子标注：OPERATOR UNDEFINED — 待机制侧（缺口说明）`。
- **数值不冻结**：全部 `@参数名` 引用（生产数值由 Profile 层定值）。
- **禁止**：「固定规则合并」「组合适应度」「满足条件后行为改变」等未展开占位。
- **无程序面显式声明**：`NO_SURFACE_EFFECT：理由`（不是跳过，是无程序的显式记录）。

### 1.5 质量管线

1. 结构校验器（每批自带 validate_*.py）→ PASS 零违规
2. 独立审（independent-narrow-reviewer）→ 7 字段 verdict
3. REVISE → 修复轮 → 复审 → 闭轮
4. 修复三步清单（reviewer 定型）：**修复 → 重加总 → 同步表格**，缺一即半修

### 1.6 跨批分工

同鱼异面可分双批（如肺鱼 P05 面[migration 批] / 护巢面[guarding 批]），须互指不重复。品系 L1-EQUIV 短形（四面声明+本体指针+Profile 重绑定）适用，不冒充本体。

## 2. LT 系列（LogicTemplate Census）标准

### 2.1 盲纪律（最高优先级）

1. **先冻结后开 registry**：全部程序骨架写入 `blind_programs.jsonl`（sha256 + `registry_seen=false`）后才允许读 `template_registry.yaml`。
2. **时序可证**：冻结节点 commit 锚定（coordinator 在冻结后 registry 打开前插入 commit）；或双时间戳 + hash 自证（偏差须事前声明）。
3. **零 post-registry 改动**：看了 registry 后回头改骨架 = `BLIND_SKETCH_POST_REGISTRY_MUTATION`，只能建 revision 留痕；若动机来自 fit existing template 须标 `BIAS_RISK` 入 Human Review。

### 2.2 程序骨架纪律

- 保留：`ordered_steps`（顺序不可排序）/ branches / gates / intermediate values + dependencies / combine / early return / return topology。
- `incoming_premises` 与 `surface_owned_logic` 分开记录（F02：activation 差异留 premise，不算 body 差异）。
- IR 节点类型仅：SEQUENCE / OPERATOR / IF / PARALLEL_SET / RETURN。SEQUENCE 顺序不可变；PARALLEL_SET 仅契约明确无序时可用。
- De-instantiation 只生成 comparison view（擦物种/Profile 名/常量），原 body 永不改写。

### 2.3 判同四态

```text
MERGE_CONFIDENT            = 控制流拓扑 + 业务顺序 + 算子 + Gate/Branch + 中间依赖 + 合并/返回 全同
TEMPLATE_EXTENSION_CANDIDATE = 拓扑不变 + 新有限 typed 参数轴（须出 extension vs new 复杂度对比）
NEW_TEMPLATE_CANDIDATE     = ORDER / OPERATOR / BRANCH / GATE / DEPENDENCY / COMBINE / RETURN 任一真差异
AMBIGUOUS_NEEDS_EXPANSION  = 证据或程序细节不足
```

- 顺序有业务意义即 `STRUCTURAL_DIFF = ORDER`，**不得 MERGE**。
- 族完整性：≥3 成员族须 canonical body 版本，**禁链式合并**（A≈B 且 B≈C ⇏ A≈C）；每新成员直验 canonical。
- §9.2 dual-topology：∥ 并行竞争（GUARD 型）与 IF 门互斥（STATE_GATED 型）为不同拓扑，**不得互并**。

### 2.4 覆盖与计数纪律

- 每个 Story 的 Sweep Log 逐 S 项过：MSF 项必须有 program / 显式排除 / TAR 三选一（B0 教训）。
- 计数四方对账：merge_tests verdict 计数 == discovery_curve.csv == 批报告散文 == registry 条目数（B1/B2 教训）。
- canonical 源自测条计入 `n_merge_confident`（B1 教训）。
- `AMBIGUOUS` verdict 不得被散文升格为 `non-match`（B0-F-3 / B2-F-2 教训）。

### 2.5 质量管线

同 B 系列 1.5，另有：
- **金样本门**：真实批前 F01-F17 全 PASS（census_engine + validate_batch）。
- **每批停止**：Self-QA + validate PASS → `INDEPENDENT_REVIEW_REQUIRED` → 停。

## 3. 通用纪律

- **统计句先跑 query 再写**（R05/R06 两批教训）：任何统计宣称先 live 实算后才写入。
- **引号内禁合成**（R07 教训）：多个引文短句不得拼成一个引号句。
- **同属先例核库**（R06 教训）：「属 N/N 全 Px」要先 query 该属全部库内行。
- **DB 字段与正文主张一致**（R07 教训）：写入后逐字段核对 properties 与正文结论。
- **选鱼名单从台账导出，禁凭记忆重建**（R10 事故教训）。
- **三步修复清单**：修复 → 重加总 → 同步表格。
- **修复完权威句必查 Machine Status**（R10 同型第三发）。

## 4. 状态与权限

- 所有产出标 `WORKING / NOT AUTHORITY / NOT PROMOTED`。
- 测试/校验通过不替代语义审核，不构成 promotion / Freeze。
- Notion 写回：Single-Writer 范围内自写自核（fetch live → 写 → readback）。
