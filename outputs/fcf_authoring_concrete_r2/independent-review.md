# Independent Review｜FCF Authoring 具体化样本 R2

level: ARTIFACT
scope:
  - `outputs/fcf_authoring_concrete_r2/authoring-concrete-r2.md` 全文
  - 其引用的 `tables/*.csv`、`tables.json`、`cases.json`、`scripts.json`、`verification.json`、`TemplateStep` 目录及 `build.py` 复算结果
  - 本报告不覆盖历史页面、生产 Config/DSL 选型、L_confirmed、或全项目 milestone
baseline:
  - `docs/mechanism_spec_writing_and_review_guide_cn.md` §0、§6–§8、§11–§12（按独立 Artifact review 路由）
  - `docs/scoped_review_protocol.md`
  - 本 bundle 内 `baseline_gate.md`、`baseline_bass.md`、`baseline_mapping.md`、`baseline_stress.md`
  - 最新 Owner Gate：C06/C07 Defense-only、C08 固定双通道、C09–C11 复用既有 Opportunity、C12 上游分群、C13 scope resolution；Bass 五群及 coldfront overlay 为 Working candidate
proves:
  - R2 已提供可读的方案 A/B 表结构、实际列/行、中文伪脚本和示例中间计算；`python3 build.py` 复算报告 38 bindings、27 cases、12 tables、35 checks，全部 checks PASS。
  - C06/C07、C08、C09–C12、C13 的声明与最新 Gate 方向一致；未将演示模板计为 L_confirmed，也未将 C06/C07 加入 Feeding fallback。
does_not_prove:
  - 生产参数/聚合函数、空间顺序、DSL/Config 最终选型或全项目完成。
open_findings:
  - blocker: `cases.json` 出现两个相同的 `id`=`BASS-G`（一个是五群 Share，一个是 Guarding），导致案例主键/链接/回放定位不唯一；`build.py` 未检查此完整性约束。
  - minor: `ColdFront` 同时由 Slot `enabled` 和 bool Parameter 表达，但模板脚本只呈现 enabled 分支，未定义两者不一致时的校验/优先级；因此“关闭=原值”与实际参数状态可能产生歧义。
  - minor: R_REACTION/R_FEED 结果 trace 对未执行的另一通道补写 `0`（如 Feeding/Reaction），读者可误解为该通道已执行且算得 0；应记录“未执行/不适用”或仅输出实际通道。
  - minor: BASS-F_B 的中间 JSON 含 `Refuge` 字段，但 S_FORAGE 脚本只定义 `Cover`、`Deep` 和 `MAX`，该字段没有对应步骤，易造成隐藏计算或复制错误的印象。
verdict: ARTIFACT_REVISE

## Follow-up review after R2 revision

level: ARTIFACT
scope:
  - 同一 `FCF Authoring 具体化样本 R2` 完整 bundle（主文档、全部表、JSON/CSV/HTML、脚本与复算器）
  - 本次复核覆盖首轮发现对应的修订，不扩大到历史页面、生产选型或全项目 milestone
baseline:
  - 首轮本报告列出的四项 open findings
  - 同上机制指南路由章节、`scoped_review_protocol.md` 与四份 baseline Owner Gate
proves:
  - `python3 build.py` 输出 38 checks，全部 PASS；27 个案例 ID 已唯一校验。
  - Share 案例改为 `BASS-ROUTING`；Guarding 保留 `BASS-G`。
  - ColdFront 仅由 Slot `enabled` 表达，脚本明确开启/关闭，并有关闭返回 Base 的测试；多余 bool 参数已移除。
  - R_REACTION/R_FEED trace 不再伪造未执行通道的 0 值；S_FORAGE 显式定义 `Refuge=MAX(Cover,Deep)`。
  - 未发现首轮 findings 的残留 blocker；R2 仍正确声明参数、聚合、空间顺序和生产选型为 Working/Deferred。
does_not_prove:
  - 不证明生产参数冻结、最终 DSL/Config 选型、L_confirmed 或全项目 milestone 完成。
open_findings:
  - none within this artifact scope
verdict: ARTIFACT_APPROVE
