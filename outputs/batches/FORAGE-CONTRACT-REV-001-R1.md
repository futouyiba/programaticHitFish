# BATCH｜FORAGE-CONTRACT-REV-001-R1

- 保存说明：agent 报告要点归档（verdict 块原文如下；全文见会话 transcript 与 role_memory）。
- 角色：independent-narrow-reviewer
- 被审对象：outputs/usable_forage_contract_r0/ R1 版（F1–F6 处置）
- verdict: PATCH_APPROVE；新 minor M1（英文转义面不对称）/M2（段级白名单）/M3（$ vs \Z）/M4（中文直译漏词）——均属已声明残余风险或覆盖边界外延，不推翻处置
- B3 意见：REV findings 全部处置且证据自洽，本复审覆盖面内不构成 B3 阻碍；最终裁决权在 Design Owner。

```text
level: PATCH
scope:
  - validate_config.py 的 R1 diff（词干 25 条/中文 18 条/三面解码/事实族 allowlist/行级 allowlist/空 diet_classes/selftest 66 用例）
  - usable_forage.config.json 的 contract.prey_field_semantics
  - README.md §2/§5/§6/§7、accounting.md §2b/§3.1/§6、dsl L10/L45
baseline:
  - outputs/batches/FORAGE-CONTRACT-REV-001.md（F1–F6 权威基线）
  - docs/scoped_review_protocol.md；五工件 R1 全文
proves:
  - F1 成立：点名英文同义词 100% 命中 25 词干；中文三面防线封死 JSON 转义走私；README 如实降级为词法代理
  - F2 成立：prey_field_semantics 机器可读；SNAP allowlist 双防线 fail 修正键、不误伤 8 合法形态
  - F3 成立：三个数据行键集固定，中性词注入被纯键集防线拦截
  - F4/F5/F6 落实；66 用例静态一致；worker 自查两缺陷确认已修
does_not_prove:
  - validator/selftest 实际执行（静态追踪）；真实键表到达后的收窄履行
  - dsl 工件机器守卫（validator 只吃 config）
  - §15.7 页 live 内容；任何 B3/milestone/promotion 状态
open_findings:
  - minor M1 英文词干只扫 raw_text（转义面不对称）
  - minor M2 instance/contract/fixed_combine 段内键无白名单
  - minor M3 allowlist 用 $ 而非 \Z（尾换行走私，fail-loud 方向）
  - minor M4 中文族内直译漏词（隐蔽/能见度/捕食/能耗），属已声明残余风险
verdict: PATCH_APPROVE
```
