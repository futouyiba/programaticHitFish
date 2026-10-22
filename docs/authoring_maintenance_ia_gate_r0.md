# 配置维护与编辑器信息架构闸门 R0（Authoring Maintenance & Editor IA Gate R0）

## 维护成本矩阵

| 操作 | 触及文件 | 新增/变更配置节点 | 复用共享定义 | 跨归属方编辑 |
|---|---:|---|---|---:|
| 新增普通物种 | 1 | 1 个物种块 | NORMAL 路径、响应规则、剖面 | 0 |
| 新增改变语法的 FishMode | 1 | 3（模式、路径、规则） | 响应等级与类型化操作 | 0 |
| 修改进食准备度（FeedingReadiness） | 1 | 1 个标量 | 全部生命周期/空间/模式/物化 | 0 |
| 新增 CueFamily | 1 | 1 个兼容条目 | 进食规则与响应策略 | 0 |

这些是针对 `authoring/bass_v0.json` 实测的固定样例 diff，不是估算。普通物种的边际成本
足够低；FishMode 仍是稀缺的改变语法结构；局部调参保持局部；CueFamily 是共享目录概念。

## 编辑器信息架构 R0

```text
Species
├─ Overview
├─ Species Static Data
├─ Lifecycle (table)
├─ Spatial / Habitat (semantic supports only)
├─ Slow Facts
├─ Cue Families (shared catalog links + local disposition)
├─ Materialization Profiles
└─ Available FishModes

FishMode
├─ Mode Definition
├─ Meaning Policy
├─ Interaction Pathways
├─ Pathway Arbitration (priority, fallback)
└─ Response Policy / narrow slices

Shared Catalogs
├─ CueFamily
├─ InteractionPathway
├─ Meaning Vocabulary
├─ ResponseGrade
├─ ResponseSlice Operation (SET / CEILING)
└─ Templates
```

生命周期归属、繁殖资格、行为锚点与空间支持不因界面对称而塞进 FishMode。

### 类型化规则编辑器

每条规则呈现 `priority`、类型化条件、类型化输入、类型化输出、显式回退标记与校验状态。
任意代码不是主要配置面。

### 可解释性流

```text
Source View → Resolved / Compiled Preview → Lint → Affected Species / Modes
```

预览必须展示展开后的继承，例如：

```text
ACTIVE_SPAWNING
→ inherited NORMAL_FEEDING
→ ResponseSlice CEILING LOW
→ final effective response policy
```

## 模板边界

只支持`单一显式模板 + 浅层覆盖`。编译器输出完全物化的规范产物；无运行时继承、深层
继承、多重继承或魔法合并。

## 闸门结果

**READY_FOR_EDITOR_PROTOTYPE**

该闸门证明四个维护固定样例与规则歧义检查。它不证明生产 UI、协作模型或范围外的
FCF 阶段。

level: ARTIFACT
scope: maintenance fixtures, authoring compiler/linter extensions, IA contract and tests
baseline: user-provided Authoring Maintenance & Editor IA Gate R0; mechanism guide §0; scoped review protocol
proves: local maintenance boundaries and constrained compiler semantics are executable and tested
does_not_prove: production editor implementation or full gameplay architecture
open_findings: none
verdict: ARTIFACT_APPROVE
