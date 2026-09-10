# FCF Scoped Review Protocol（试行）

本协议解决“局部内容审核通过，却被误读成整体完成”的问题。它不增加日常审批
层级，只限制审核结论可以证明多大范围。

## 1. 三种 review level

| Level | 审核对象 | 可以证明 | 不能证明 |
|---|---|---|---|
| `PATCH` | 指定 diff、行或章节 | 该改动没有已发现 blocker | 整篇文档完整、项目完成 |
| `ARTIFACT` | 一份完整文档/Schema/模块，或一个明确命名的 cohesive policy bundle | 该 artifact/bundle 对声明 baseline 完整且正确 | 其它 artifact 或 milestone 完成 |
| `MILESTONE` | 原始 Goal 下的一组交付物 | 覆盖完整且语义正确 | 未包含在 scope 的外部 gate |

未声明 level 的 verdict 一律按 `PATCH` 解释。

## 2. 强制 verdict 格式

```text
level: PATCH | ARTIFACT | MILESTONE
scope:
  - 精确文件、章节、模块或 milestone
baseline:
  - 本次实际对照的需求/authority
proves:
  - 本次结论可以证明什么
does_not_prove:
  - 明确排除的更大范围
open_findings:
  - blocker/minor/external gate；没有则写 none
verdict: <LEVEL>_APPROVE | <LEVEL>_REVISE
```

主代理引用 verdict 时必须保留 `level + scope`，不能只引用 `APPROVE`。

## 3. 什么时候使用

### 日常窄修改

使用 `PATCH`。Reviewer 可以只读 diff 和必要上下文，不做全库覆盖审计。

### 宣称单篇文档完整

使用 `ARTIFACT`。Reviewer 必须读取完整 artifact，并对照该文档的明确接受标准，
不能只看本轮新增段落。

### 宣称全部完成 / closed / Freeze-ready

使用 `MILESTONE`。只在这个节点执行一次：

```text
原始 Goal
→ explicit requirements
→ artifact/evidence mapping
→ missing/partial/proven
→ semantic review
```

存在任一 `MISSING` 或 `PARTIAL` 时必须 `MILESTONE_REVISE`。

## 4. 防止权限升级

以下推理无效：

```text
温度新增章节 PATCH_APPROVE
⇒ 温度机制完整             （无效）
⇒ 所有环境机制完整          （无效）
⇒ FCF 文档已完成             （无效）
```

有效的升级只能来自新的、更大 scope review：

```text
PATCH_APPROVE
→ ARTIFACT review
→ ARTIFACT_APPROVE
→ MILESTONE closure review
→ MILESTONE_APPROVE
```

这表示审核权限扩大，不要求每个 patch 都依次走完四步。

## 5. 轻量执行原则

- Patch 默认只做局部语义审查；
- Artifact review 只在准备声明该 artifact 完成时执行；
- Milestone coverage audit 只在整体完成声明前执行；
- 自动测试继续证明机器可验证的性质，不替代 scope/coverage 判断；
- Reviewer 的 `does_not_prove` 应保持简短，只写最容易被误提升的范围。

## 6. 本轮试行验收

本协议自身先接受一次 `ARTIFACT` review。之后把自然发生的最多三个真实 review
作为可选观察期，再评估是否出现：格式负担过重、scope 不清、或仍被错误扩大结论
的情况。观察期不是日常工作或 milestone review 的前置门槛，也不得为了凑数人为
制造 review。

## 7. 试行记录

### Trial 0：协议自审（不计入后续真实业务观察期）

```text
level: ARTIFACT
scope:
  AGENTS.md scoped-review rules
  + scoped_review_protocol.md
  + independent_review_checklist.md protocol reference
verdict: ARTIFACT_APPROVE
```

Reviewer 明确证明：三种权限、默认降级、`proves/does_not_prove` 和 milestone
触发条件一致且执行成本合理；同时明确 **不证明** 任何 FCF 机制、文档集或
V1 Freeze 已完成。这里的“完成”仅指本协议自身的 Trial 0 自审，不是 V1 Freeze。
剩余观察：自然发生的真实业务 review 是否仍能保持 level/scope，
且没有明显格式负担；不要求凑足次数，也不阻断其它工作或 milestone review。
