# FCF V1 设计决策日志（Design Decision Log）

本清单是设计审议入口，不是实现待办清单（backlog）。`FROZEN` 表示 V1 不应重新讨论；
`OPEN` 表示需要明确产品/物理输入后才能继续；`V1.1` 表示有意延期，不能
伪装成当前阻塞项（blocker）。

## FROZEN

| ID | 决策 | 理由/反例 |
|---|---|---|
| D-01 | 世界事实（World Fact）与针对具体鱼的语义解释（fish-specific interpretation）分离 | 防止同一事实在不同鱼上产生隐含语义 |
| D-02 | 物种（Species）= 能力（capability）；策略程序（Program）= 当前策略（current policy）；变体（Variant）只能覆盖策略 | 防止变体越权新增物种能力 |
| D-03 | 遭遇候选（Candidate）只在原子保留（atomic reservation）后产生；Pending 不占 PSU、不运行 AI | 消除幻影候选（phantom candidate）和容量套利 |
| D-04 | A/T/E 各有语义归属方（owner），不是万能加成通道（universal bonus lanes） | 防止系数大杂烩（coefficient soup）与重复结算 |
| D-05 | 动机/遭遇转化（Motive/Encounter Conversion）默认确定性（deterministic）；随机性只在声明边界 | 保证重放/输入速率不变性（replay/input-rate invariance） |
| D-06 | 普通鱼使用可交换质量（exchangeable mass）；不隐式创建持久个体鱼（persistent individual fish） | 控制 V1 身份/存储复杂度 |
| D-07 | 一个物理后果（physical consequence）只有一个权威归属方（authoritative owner） | 防止栖息占位/进入/转化双重扣减 |
| D-08 | 所有机会（Opportunity）/原子保留（Reservation）/仲裁（Arbitration）/终结结算（Settlement）的身份（identity）可持久化且幂等 | 防止重启、并发、响应丢失造成重复结果 |
| D-09 | UNKNOWN 默认不新增质量、不生成新遭遇候选，并记录追踪样例（trace） | 不用缺失数据伪造随机奖励 |
| D-10 | 安全风险（Safety risk）阻断新进入但不追溯销毁遭遇候选 | 避免测量不确定性（uncertainty）被误结算为死亡 |

## 已拒绝的替代方案

| 方案 | 拒绝原因 | 重新启用所需证据 |
|---|---|---|
| 全局 `temperature/oxygen/current_multiplier` | 无法证明归属方与不同物理后果 | 新的因果图（causal graph）、反例（counterexample）和产品需求（product requirement） |
| Poisson + cap 入口 | 不符合有限 PSU/二项分布（Binomial）语义 | V1 core 重新开启（reopen）的守恒（conservation）证据 |
| 先随机抽鱼再判断动机（motive） | 因果顺序错误，可因输入频率套利 | 不能仅靠实现便利重新开启（reopen） |
| 每帧/每 tick 重掷机会（Opportunity） | 破坏重放/输入速率不变性 | 新的稳定语义事件契约（stable semantic event contract） |
| 变体修改 q/致死/感官/接触能力（lethal/sensory/contact capability） | 越过物种能力（Species capability） | 新的物种能力版本（Species capability version），不是变体覆盖（Variant override） |
| 挂钩/接触（Hook/Contact）直接修改 PSU/历史（History） | 绕过终结结算/历史归属方 | 新的终态归属方契约（terminal owner contract） |

## OPEN（必须先回答再进入实现）

| ID | 问题 | 所需输入 | 责任方 |
|---|---|---|---|
| O-01 | 生产运行时（runtime）的快照（snapshot）、日志（journal）、历史存储适配器（History storage adapter）是什么？ | 运行时/存储库、SLO、故障模型 | Engineering/Product |
| O-02 | 各水域温度/DO/流速/光学剖面（profile）的测量质量与空间分辨率？ | 传感器/模型数据字典 | Data/Simulation |
| O-03 | 各物种/队列（Species/cohort）的能力剖面（capability profile）与来源？ | 生物学参数、校准样本 | Design/Biology |
| O-04 | 三条旗舰追踪样例（flagship trace）的最终呈现/路径/几何真值（presentation/path/geometry truth）？ | 固定样例资产（fixture asset）与版本 | Content/Design |
| O-05 | 安全风险下已有遭遇候选的产品处置策略？ | 安全/游戏设计策略（policy） | Product/Design |

OPEN 项目不是实现细节；如果输入缺失，必须保持 `UNKNOWN` 或阻断，不能由
工程师自行补默认值。

## V1.1 / 明确延期

- 新增未声明动机（例如 ESCAPE）或新的 ContactType/能力（capability）；
- 持久个体鱼身份、复杂社交/群体 AI；
- 额外环境因子和未经归属方审计的真实性加成（realism bonus）；
- 任何将 A/T/E 合并成统一分数的便利 API。

## 设计进入实现的 gate

只有当决策项对应的输入、输出、单位、边界、归属方（owner）、修订版本（revision）、失败路径和
至少一个对抗性反例（adversarial counterexample）都已记录，并获得独立审查者（reviewer）
`APPROVE`/`APPROVE_WITH_MINOR`，才允许写入运行时契约（runtime contract）。
