# FCF V1 Design Decision Log

本清单是设计审议入口，不是实现 backlog。`FROZEN` 表示 V1 不应重新讨论；
`OPEN` 表示需要明确产品/物理输入后才能继续；`V1.1` 表示有意延期，不能
伪装成当前 blocker。

## FROZEN

| ID | 决策 | 理由/反例 |
|---|---|---|
| D-01 | World Fact 与 fish-specific interpretation 分离 | 防止同一事实在不同鱼上产生隐含语义 |
| D-02 | Species = capability；Program = current policy；Variant 只能覆盖 policy | 防止 Variant 越权新增物种能力 |
| D-03 | Candidate 只在 atomic reservation 后产生；Pending 不占 PSU、不运行 AI | 消除 phantom candidate 和容量套利 |
| D-04 | A/T/E 各有语义 owner，不是 universal bonus lanes | 防止 coefficient soup 与重复结算 |
| D-05 | Motive/Encounter Conversion 默认 deterministic；随机性只在声明边界 | 保证 replay/input-rate invariance |
| D-06 | 普通鱼使用 exchangeable mass；不隐式创建 persistent individual fish | 控制 V1 identity/storage 复杂度 |
| D-07 | 一个 physical consequence 只有一个 authoritative owner | 防止 occupancy/entry/conversion 双重扣减 |
| D-08 | 所有 Opportunity/Reservation/Arbitration/Settlement identity 可持久化且幂等 | 防止重启、并发、响应丢失造成重复结果 |
| D-09 | UNKNOWN 默认不新增质量、不生成新 Candidate，并记录 trace | 不用缺失数据伪造随机奖励 |
| D-10 | Safety risk 阻断新进入但不追溯销毁 Candidate | 避免测量 uncertainty 被误结算为死亡 |

## 已拒绝的替代方案

| 方案 | 拒绝原因 | 重新启用所需证据 |
|---|---|---|
| 全局 `temperature/oxygen/current_multiplier` | 无法证明 owner 与不同物理后果 | 新的 causal graph、counterexample 和 product requirement |
| Poisson + cap 入口 | 不符合有限 PSU/Binomial 语义 | V1 core 重新 reopen 的 conservation 证据 |
| 先随机抽鱼再判断 motive | 因果顺序错误，可因输入频率套利 | 不能仅靠实现便利 reopen |
| 每帧/每 tick 重掷 Opportunity | 破坏 replay/input-rate invariance | 新的 stable semantic event contract |
| Variant 修改 q/lethal/sensory/contact capability | 越过 Species capability | 新 Species capability version，不是 Variant override |
| Hook/Contact 直接修改 PSU/History | 绕过 Settlement/History owner | 新 terminal owner contract |

## OPEN（必须先回答再进入实现）

| ID | 问题 | 所需输入 | 责任方 |
|---|---|---|---|
| O-01 | 生产 runtime 的 snapshot、journal、History storage adapter 是什么？ | runtime/repository、SLO、故障模型 | Engineering/Product |
| O-02 | 各水域温度/DO/流速/光学 profile 的测量质量与空间分辨率？ | 传感器/模型数据字典 | Data/Simulation |
| O-03 | 各 Species/cohort 的 capability profile 与来源？ | 生物学参数、校准样本 | Design/Biology |
| O-04 | 三条 flagship trace 的最终 presentation/path/geometry truth？ | fixture asset 与版本 | Content/Design |
| O-05 | Safety risk 下已有 Candidate 的产品处置策略？ | 安全/游戏设计 policy | Product/Design |

OPEN 项目不是实现细节；如果输入缺失，必须保持 `UNKNOWN` 或阻断，不能由
工程师自行补默认值。

## V1.1 / 明确延期

- 新增未声明 motive（例如 ESCAPE）或新的 ContactType/capability；
- persistent individual fish identity、复杂社交/群体 AI；
- 额外环境因子和未经 owner 审计的 realism bonus；
- 任何将 A/T/E 合并成统一 score 的便利 API。

## 设计进入实现的 gate

只有当决策项对应的输入、输出、单位、边界、owner、revision、失败路径和
至少一个 adversarial counterexample 都已记录，并获得独立 reviewer
`APPROVE`/`APPROVE_WITH_MINOR`，才允许写入 runtime contract。
