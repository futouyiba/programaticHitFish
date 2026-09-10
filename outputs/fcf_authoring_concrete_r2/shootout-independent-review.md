# Representation Shootout R3 独立审查

level: ARTIFACT
scope:
  - `representation-shootout-r3.md` 全文
  - R2 中被其引用的 C03/C06/C08/C09/C12 表行、脚本与 TemplateStep 必要闭包
  - Frozen Set 与最新 Representation Gate 的相关边界
  - 不覆盖 Reality Baseline、FR3/FISH-R01 候选、历史页面或全项目 milestone
baseline:
  - `docs/mechanism_spec_writing_and_review_guide_cn.md` §0、§6–§8、§11–§12
  - `docs/scoped_review_protocol.md`
  - R2 `tables.json`、`scripts.json`、`TemplateStep` 与四份 baseline/Owner Gate
proves:
  - 四路对照明确区分 Profile 参数资产、规范化 Table、固定有序 Step Table 与受限中文 DSL；C08 示例实际对应 R2 的双 Slot 与 MAX，且数值可复核。
  - C03 保留 FIRST_MATCH/Default，C06 为 Defense-only，C08 不引入 Selector，C09 复用既有 Opportunity，C12 使用上游 Group 分流；没有把演示写法升级为最终选型。
  - 修改成本表可操作，明确哪些改动触发 Template 变更；生产桥接、FK/类型/白名单/副作用边界和未决状态均有说明。
does_not_prove:
  - 不证明生产编译器已实现、最终 DSL/Config 选型、候选鱼覆盖或全项目完成。
open_findings:
  - minor: C03 的 PT 对照写成“threshold 0.7、default 0、response 0.8/0.25”，但真实闭包还包含第二个 `drift` 阈值 0.6；该行作为“PT 需要填”容易被读成完整参数清单。建议显式列出 `match≥0.7 AND drift≥0.6` 及 `match≥0.3` 两个阈值。
verdict: ARTIFACT_APPROVE

## Follow-up review

level: ARTIFACT
scope:
  - 同一完整 `representation-shootout-r3.md` 及其 R2 引用闭包
  - 仅复核首轮 minor finding 的修订
baseline:
  - 本报告首轮 `open_findings` 中的 C03 PT 阈值完整性问题
proves:
  - C03 PT 摘要现已明确列出 `match≥0.7` 与 `drift≥0.6`，并与 Narrow DSL 的具体条件及 R2 参数行一致。
  - 首轮 minor finding 已关闭；其余首轮结论保持有效。
does_not_prove:
  - 不扩大原 ARTIFACT scope；不证明生产实现、最终选型或全项目完成。
open_findings:
  - none within this artifact scope
verdict: ARTIFACT_APPROVE
