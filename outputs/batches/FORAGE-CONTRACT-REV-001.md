# BATCH｜FORAGE-CONTRACT-REV-001

- 保存说明：agent 报告逐字归档（reviewer 无写工具；由 Coordinator 保存）。
- 归档时间：2026-09-10
- 角色：independent-narrow-reviewer
- 被审对象：outputs/usable_forage_contract_r0/（worker 首版交付包）
- verdict: ARTIFACT_REVISE（blocker F1 守卫同义词洞+中文盲区、F2 prey field 原始性无机器防线；minor F3 行级键注入、F4 输入侧义务未记账+external gate、F5 空 diet_classes 被拒、F6 README 措辞）
- 处置：见 FORAGE-CONTRACT-REP-001-R1（R1 修复，全部六项）。

---

## verdict 块（原文）

```text
level: ARTIFACT
scope:
  - outputs/usable_forage_contract_r0/README.md
  - outputs/usable_forage_contract_r0/config/usable_forage.config.json
  - outputs/usable_forage_contract_r0/config/validate_config.py
  - outputs/usable_forage_contract_r0/dsl/usable_forage.dsl.txt
  - outputs/usable_forage_contract_r0/accounting.md
baseline:
  - envelope 携带的 Design Owner 已批准契约边界
  - outputs/batches/KNIFE-READ-001.md（Knife §16/§15.2/§15.6/§16.5；归档版 03:49:56Z）
  - docs/scoped_review_protocol.md
proves:
  - 三个表达位语义逐算子一致，吸收/排除面与批准边界逐项吻合，owner 正确
  - validator 确定性；五检查族非恒真，selftest 13 例族级反例覆盖完整
  - 契约内结构守恒（duplicate 三重拒绝 + 引用一致性）
  - accounting 输出侧成本已申报；2D 不准入论证符合 §16.5 判据
does_not_prove:
  - validator/selftest 实际执行（无 Bash，静态追踪）
  - 运行层 snapshot 隔离、真实键表、上游 prey field 实际口径
  - 267 鱼规模实际表现；Config vs DSL 的 L_observed 敌意验证
  - 任何机制 promotion / Freeze
open_findings:
  - blocker F1 GUARD 词干表同义词洞 + 非 ASCII 盲区（README 主张 false fit）
  - blocker F2 prey field「原始未修正」不变量未进机器可读契约（上游修正走私无守卫）
  - minor F3 嵌套行内键注入无族拦截
  - minor F4 输入侧义务未记账；§15.7 external gate
  - minor F5 空 diet_classes 被强制非空（拒绝 baseline 合法内容）
  - minor F6 README §2 措辞字面为假
verdict: ARTIFACT_REVISE
```

## 攻击记录要点（全文见会话 transcript 与 role_memory）

- F1 逐词验证：refuge/shelter/hidden/ambush/structure/safe/risk/concealed、detectable/perceived/reachable/conspicuous/turbid、catch/catchability/grasping/encounter、cost/handling 全部漏网；中文值零 token。
- F2：`resolved_snapshot.perceived_prey_density.fish` 前缀合法、词干不命中，五族全绿——主走私通道无守卫。
- 三角验法与 selftest 静态核验细节见 verdict proves 与 role_memory 模式 3/4。
