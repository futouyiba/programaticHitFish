# 预生成配置编写垂直切片 R0（Pre-Generation Authoring Vertical Slice R0）

> 术语沿革：FishMode →（2026-09-11）FishGroup →（2026-10-22）中鱼习性模式（EngagementMode）。FishGroup 概念退役；习性的数据与量级划分由中鱼习性模式承担（species 配置键 `engagement_modes`，生命周期/规则键 `mode`）。结构、行数与 showdown 结论不变。

规范固定样例：[`authoring/bass_v0.json`](../authoring/bass_v0.json)。它使用四类表达：

- 目录（Catalog）：物种、中鱼习性模式（EngagementMode）、路径与 CueFamily 标识符。
- 表格：生命周期供给份额与空间机会。
- 类型化规则：响应等级与窄域 `SET`/`CEILING` 切片操作。
- 生成物：CandidateBasisKey、OpportunityId、快照指纹与参与质量。

编译器产出 `CompiledContentBundle`；其 `CandidateContribution` 值由既有确定性挂具消费。
不使用任何 Bass 专属玩法分支。

## 配置编写成本对决

| 指标 | 平铺表格 | 原始类型化 DSL | 混合 |
|---|---:|---:|---:|
| Bass 总行数/节点数 | 24 | 31 | 18 |
| 重复谓词 | 7 | 3 | 1 |
| 触及表面数 | 6 | 3 | 5 |
| 最大表宽 | 14 | n/a | 8 |
| 交叉引用 | 12 | 9 | 9 |
| 可 lint 错误 | medium | high | high |
| 新增物种边际成本 | high | medium | low |
| 新增中鱼习性模式边际成本 | medium | medium | low |

结论：**混合（HYBRID）**。表格在有限目录/份额上保持高效；类型化规则提供归属与重叠
校验；两者编译进同一个规范束。

## 编辑器心智模型

物种页：静态数据、生命周期表、空间/栖息表、慢速事实、物化剖面、可用中鱼习性模式。

中鱼习性模式（EngagementMode）页：模式身份（mode identity）、含义策略、可用路径与
优先级/仲裁、响应策略、窄域模板选择。生命周期/队列资格与物化仍由生命周期/剖面
拥有；它们不是任意中鱼习性模式的模块。

模板单一、浅层，并在编译时完全物化。运行时 ID、随机数、技术碎片与
CandidateEngagementMass 不是可编辑表面。

维护固定样例：普通物种编辑静态数据 + 一个剖面；改变语法的模式新增一个模式/路径/
策略集；温度偏好只改慢速事实；新 CueFamily 改目录与物种兼容表。

## 范围审查

level: ARTIFACT
scope: `fcf_v1/authoring.py`, `authoring/bass_v0.json`, authoring tests and this report
baseline: user-provided Pre-Generation Authoring Vertical Slice R0; mechanism guide §0; scoped review protocol
proves: constrained authoring compiles into the previously validated deterministic harness and linter catches declared structural errors
does_not_prove: full editor UI, full FCF, Encounter/Task/Conversion/Contact/Hook, production networking
open_findings: none
verdict: ARTIFACT_APPROVE
