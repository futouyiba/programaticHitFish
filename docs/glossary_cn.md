# FCF 文档英文术语—中文 Glossary

本表汇总仓库文档、配置示例和实验说明中具有机制含义的英文术语。中文是面向
产品、策划、内容和工程的主标签；代码字段、枚举值、文件名和稳定检索标签保留
英文原文。普通连接词、通用编程词和仅用于示例的专名不单独收录。

| English term / identifier | 中文工作术语 | 定义与使用边界 | 主要语境 |
|---|---|---|---|
| Fish-Centric Conditional Funnel (FCF) | 以鱼为中心的条件漏斗 | 先按有限鱼群质量和环境条件筛选机会，再推进遭遇与结算的 V1 总机制 | 总览、工程 |
| World Fact | 世界事实 / 环境事实 | 与具体鱼无关、带来源和时间语义的观测或模型事实 | 环境、总览 |
| Species | 物种 | 声明能力（capability）的配置对象，不等同于策略 | 鱼种、DSL |
| Species Capability | 物种能力 | 鱼能感知、移动、执行任务或接受何种接触的能力约束 | 鱼种、总览 |
| Population Definition | 种群定义 | 定义有限质量单位及其供给上限的对象 | DSL、守恒 |
| Population Slice | 种群切片 | 绑定 cohort、生命周期和行为程序的可运行子集 | DSL、空间 |
| Slice | 切片 | `PopulationSlice` 的简称；不可泛指任意数据分片 | DSL、空间 |
| Cohort | 队列 / 同批群体 | 共享生命周期或策略参数的一组有限质量 | 鱼种、空间 |
| Program | 策略程序 | 选择动机和规则的政策对象；不创建鱼、不修改能力 | DSL、行为 |
| BehaviorProgram | 行为策略程序 | 按优先级确定当前策略选择和入口机会的 Program | 行为、总览 |
| Variant | 变体 | 受 allowlist 限制的策略覆盖，不是新物种或新 Owner | 鱼种、DSL |
| Capability | 能力 | 可执行动作或感知通道的约束；不表达当前是否愿意行动 | 鱼种、行为 |
| Policy | 策略 / 政策 | 可配置的选择、阈值或失败处理规则 | 全部机制文档 |
| Profile | 剖面 / 配置剖面 | 带版本、来源和适用范围的一组参数与规则 | 环境、配置 |
| Authoring | 配置编写 / Authoring | 面向策划或编辑器的声明式配置表达 | DSL、编辑器 |
| DSL (Domain-Specific Language) | 领域专用语言 | 用于表达 FCF 规则的受限声明式语言；不允许任意脚本和隐藏随机 | DSL、工程 |
| Schema | 结构模式 / Schema | 机器可校验的字段、类型、必填项和约束 | 配置、工程 |
| Compiled Artifact | 编译产物 | 由 Authoring 配置编译出的可执行、可审计版本化对象 | DSL、工程 |
| Resolver | 解析器 | 按确定性优先级把事实和规则解析为一个结果 | 动机、环境 |
| Interpretation | 语义解释 | 将能力、策略和事实解释成当前机制含义的中间层 | 总览、DSL |
| Occupancy | 栖息占位 | 有限鱼群质量长期分配到可停留节点的结果 | 空间、环境 |
| Habitat | 栖息地 | 鱼可停留的空间与环境条件集合 | 空间、环境 |
| Habitat Suitability | 栖息地适宜度 | 节点对某物种或切片的长期适宜程度 | 空间 |
| Local Presence | 局部存在度 | 当前节点或区域内可用鱼群质量的派生结果 | 空间、总览 |
| Presentation | 呈现 | 玩家当前投放或操作呈现给鱼的内容与状态 | 总览、行为 |
| Perception | 感知 | 鱼是否能接收呈现及其感知通道结果 | 总览、环境 |
| Perception Access | 感知可达性 | 呈现被鱼接收的条件结果，常记为 `A_visual` | 总览、行为 |
| Actionability | 可执行性 | 当前 task 是否在能力、几何和环境上可执行 | 总览、编辑器 |
| Hard Actionability Gate | 硬可执行性闸门 | 仅把真正不可执行的 task 标为 `BLOCKED`；不改写 A/E 分数 | 总览、行为 |
| Motive | 当前动机 | 此刻为何开始接近或行动，如 `FORAGE`、`DEFEND` | 行为、总览 |
| Entry | 进入 | 从动机到提出 encounter 机会的阶段 | 总览、工程 |
| EntryOffer | 进入机会等级 | 动机对当前呈现提出的离散机会等级 | 总览、行为 |
| Opportunity | 机会 | 一次可被候选鱼消费的物理交互机会 | 账本、工程 |
| Opportunity Ledger | 机会账本 | 记录机会消费，防止重复抽取或重复保留 | 工程、守恒 |
| Candidate | 遭遇候选 | 原子保留成功后、可继续运行 encounter 的有限质量实体 | 总览、工程 |
| Encounter | 遭遇 | 候选鱼与当前呈现进行的有限生命周期互动 | 总览、工程 |
| Encounter Conversion | 遭遇转化 | 将任务序列确定性推进到 Commit 边界的阶段 | 转化、工程 |
| Task | 任务动作 | Encounter 内要完成的动作或动作序列 | 转化、行为 |
| Task Signature | 任务签名 | 描述动作要求、难度和能力约束的稳定标识 | 转化、工程 |
| Task State Machine | 任务状态机 | 由状态、谓词、允许边和终止条件组成的任务流程 | 转化、DSL |
| State | 状态 | 可持久化或生命周期内可观察的阶段信息 | 全部机制文档 |
| Mode | 模式 | 当前行为或环境所处的离散运行模式 | 行为、环境 |
| Meaning | 呈现含义 | 鱼对当前 presentation 的语义解释，如觅食或巢穴威胁 | 总览、行为 |
| Response | 响应 | 鱼对含义和呈现的行为反应等级或动作 | 总览、行为 |
| Conversion | 转化 | 将响应/任务推进为攻击承诺或失败结果的阶段 | 总览、工程 |
| Commit | 承诺判定 | 一次明确的随机决策；结果确定后不得重复重掷 | 总览、行为 |
| ATTACK | 攻击 | Encounter 转化中达到攻击意图的阶段输出 | 转化、总览 |
| CONTINUE | 继续 | 当前任务未终止且仍可推进的阶段输出 | 转化、总览 |
| ARRIVAL | 到达 | 鱼完成接近并抵达呈现交互范围的事件/状态 | 行为、转化 |
| REJECTED | 已拒绝 | 候选或请求因规则、能力或安全边界被拒绝的终态 | 转化、工程 |
| DISENGAGED | 已脱离 | 已建立互动后主动结束但未完成承诺的终态 | 转化、工程 |
| Contact | 接触 | 鱼与呈现发生物理交互的判定 | 接触、挂钩 |
| Hook | 挂钩 | 根据口型、钩具、几何和时序判断是否挂住 | 接触、挂钩 |
| Contact / Hook | 接触 / 挂钩 | 下游物理阶段的合称；不应提前并入“咬钩概率” | 总览、接触 |
| Contact Intent | 接触意图 | 上游对接触类型、时序或几何要求的声明 | 接触、工程 |
| Contact Type | 接触类型 | 允许的物理接触类别及其兼容性要求 | 接触、鱼种 |
| Contact Attempt | 接触尝试 | 下游对一次物理接触求值的请求及其稳定身份 | 接触、工程 |
| Geometry Compatibility | 几何兼容性 | 口型、钩具、姿态和位置是否满足接触条件 | 接触、鱼种 |
| Settlement | 终结结算 | 唯一一次归还、警戒、迁移、恢复或移除的终态交易 | 工程、接触 |
| Settlement Owner | 结算 Owner | 对某一 physical consequence 负责唯一写回的机制 | 工程、治理 |
| END-CUT History | 结算末历史更新 | 在一次机会结束时统一应用饱食、警戒和恢复等 delta | 总览、历史 |
| History Delta | 历史增量 | 写入持久历史的 typed 变化量 | 历史、工程 |
| Resource History | 资源历史 | 记录饱食、暴露、恢复债务等跨机会状态 | 历史 |
| Actual Supply | 实际供给 | 尚未被保留、仍可被机会消费的有限质量 | 守恒、工程 |
| Encounter Hold | 遭遇持有量 | 已保留、暂时从 Actual Supply 移出的质量 | 守恒、工程 |
| Reservation | 原子保留 | 成功时一次性从实际供给转入 encounter hold 的操作 | 守恒、工程 |
| Atomic Reservation | 原子保留 | 不可拆分、可并发安全、成功后才创建 Candidate 的保留 | 守恒、工程 |
| Finite Mass Conservation | 有限质量守恒 | Actual Supply、Hold、Settlement 等质量总和保持不超额 | 守恒、审查 |
| Finite Mass | 有限质量 | V1 中可计数、不可凭空创建的鱼群质量单位 | 总览、审查 |
| Exchangeable Mass | 可交换质量 | 不隐式代表持久个体身份的群体质量表示 | 总览、鱼种 |
| Lifecycle | 生命周期 | 从进入、活动到退出或终止的阶段序列 | 鱼种、环境 |
| Source Group | 来源组 | 空间上共享来源、边界或权重语义的一组节点 | 空间烘焙 |
| Spatial Bake | 空间烘焙 | 将静态来源关系预计算为运行时索引或查找表 | 空间烘焙 |
| Runtime | 运行时 | 执行已编译规则和当前快照的系统阶段 | 工程、空间 |
| LUT (Lookup Table) | 查找表 | 运行时按键快速取得预计算空间或环境结果 | 空间烘焙 |
| Snapshot | 快照 | 在固定 causal cut 上读取的一致输入视图 | 工程、环境 |
| Causal Cut | 因果切点 | 固定 profile、index、算法版本和时间的求值边界 | 环境、工程 |
| Revision | 修订版本 | 可追溯、可复现的配置或算法版本标识 | 全部机制文档 |
| Deterministic | 确定性 | 相同输入、seed、scope、revision 得到相同结果 | 工程、实验 |
| Replay | 重放 | 用相同输入和身份复现一次求值或结算 | 工程、验证 |
| Idempotent | 幂等 | 同一 transaction 重试不会产生第二次物理后果 | 工程、结算 |
| Transaction Identity | 交易身份 | 标识一次唯一终态结算的稳定 ID | 工程、接触 |
| Terminal State / Outcome | 终态 / 终态结果 | 不可重新打开或重复推进的生命周期终点 | 转化、工程 |
| Typed Terminal Outcome | 类型化终态结果 | 带明确原因类型的终态返回，而非模糊失败 | 转化、接触 |
| UNKNOWN | 未知 | 数据不足或不确定性超限时的保守结果，不自动当作通过 | 环境、工程 |
| AMBIGUOUS | 有歧义 | 测量区间跨越边界，需按保守策略处理 | 温度、溶氧 |
| LETHAL_RISK | 致死风险 | 区间与致死区域相交，阻断新进入或保留 | 温度、溶氧 |
| BLOCKED | 被阻断 | Hard actionability gate 判定当前任务不可执行 | 行为、工程 |
| DROP | 放弃 / 脱离 | Encounter 在转化阶段失败并退出 | 转化、总览 |
| HOOKED | 已挂钩 | Contact/Hook 结果：几何、口型和时序均满足 | 接触 |
| SLIP | 脱钩 | 接触发生但未形成有效挂钩 | 接触 |
| NO_CONTACT | 未接触 | 未形成物理接触的终态结果 | 接触 |
| FOLLOW | 跟随 | 响应等级：开始跟随呈现但尚未承诺 | 行为 |
| TRACK | 追踪 | 响应等级：持续追踪并满足更高互动条件 | 行为 |
| COMMIT_READY | 可承诺 | 已满足转化条件、允许执行 Commit 的状态 | 工程、转化 |
| Physical Consequence | 物理后果 | 可观察且需唯一 Owner 负责的行为后果 | 治理、工程 |
| Owner | 归属方 / 责任 Owner | 对某字段、后果或写回拥有唯一权威的阶段 | 全部机制文档 |
| Causal Ownership | 因果归属 | 将一个行为后果分配给唯一结算阶段 | 治理、审查 |
| Allowlist | 允许列表 | Variant 或编辑器可覆盖的明确字段集合 | DSL、编辑器 |
| Predicate | 谓词 | 返回真/假的规则条件，用于状态迁移 | DSL、转化 |
| Transition | 状态迁移 | 从一个状态到另一个状态的合法边 | 转化、DSL |
| Priority | 优先级 | 规则冲突时的确定性排序；同优先级重叠通常编译失败 | 行为、DSL |
| Hysteresis | 滞回 | 进入和退出阈值分离，避免边界抖动 | 环境 |
| Exposure | 暴露 | 鱼对呈现或环境压力的累计接触量 | 实验、历史 |
| Recovery Debt | 恢复债务 | 暴露后尚未偿还的恢复负担 | 溶氧、历史 |
| Conservation | 守恒 | 质量、资源或结算总量不被重复创建或扣除 | 工程、审查 |
| Fixture | 固定样例 / 测试夹具 | 可重复运行的输入数据和预期结果集合 | 实验、空间 |
| Trace | 追踪样例 | 展示一次端到端状态、原因和输出的可审计记录 | 验证、实验 |
| Flagship Trace | 旗舰追踪样例 | 用于跨文档验收的代表性端到端场景 | 验证 |
| Verification | 验证 | 通过断言、守恒检查和重放证明实现行为符合约定 | 验证、工程 |
| Review Scope | 审查范围 | 明确本次 review 覆盖的 diff、artifact 或 milestone 边界 | 治理 |
| Baseline | 审查基线 | review 实际读取和比较的版本、章节与证据 | 治理 |
| Open Finding | 未闭合发现 | 尚未解决、需要决策或补证据的问题 | 审查 |
| Artifact | 交付物 / 文档工件 | 一份完整命名的文档、配置或 cohesive policy bundle | 治理 |
| Milestone | 里程碑 | 按原始 Goal 与 Definition of Done 验收的一组工作成果 | 治理 |
| Freeze / Freeze-ready | 冻结 / 可冻结 | 版本不再接受范围内语义变更，且满足里程碑验收 | 治理 |
| Temperature Profile | 温度剖面 | 按位置、深度、时间和不确定性组织的水温事实配置 | 温度 |
| Water Temperature Fact | 水温事实 | 某时空位置的观测水温及其来源、质量和有效期 | 温度 |
| Dissolved Oxygen (DO) | 溶解氧（DO） | 水体含氧量事实；安全阈值与占位/体力规则分属不同 Owner | 溶氧 |
| Oxygen Capability | 耐氧能力 | 物种对低氧、恢复和用力的能力参数 | 溶氧 |
| Flow | 流速 / 水流 | 水体流动事实及其对栖息和动作执行的影响 | 流速 |
| Flow Capability | 耐流能力 | 物种在不同流速下维持、移动和完成任务的能力 | 流速 |
| Structure | 结构 | 岸线、桥墩、沉木等提供遮蔽或边界的空间事实 | 深度、空间 |
| Vegetation | 植被 | 水草、芦苇等结构来源及其覆盖属性 | 环境、空间 |
| Substrate | 底质 | 泥、砂、砾石等水底材质事实 | 环境、空间 |
| Light | 光照 | 影响可见性、昼夜和行为模式的环境事实 | 光照、行为 |
| Turbidity | 浑浊度 | 影响视觉感知和光学风险的水体清澈程度事实 | 光照、环境 |
| Optical Fact | 光学事实 | 光照、浑浊度和可见性等感知输入的统一表示 | 光照 |
| Depth Layer | 深度层 | 用半开区间定义的有效深度范围，禁止重叠或隐式外推 | 温度、空间 |
| Thermocline | 温跃层 | 温度快速变化的深度边界；默认禁止跨层插值 | 温度 |
| Interpolation | 插值 | 在允许的空间、深度或时间间隔内估算事实值 | 环境、配置 |
| Uncertainty | 不确定性 | 测量或模型值的误差范围；超限时输出 `UNKNOWN` | 环境 |
| Freshness | 新鲜度 / 时效性 | 事实距当前时间的可接受程度 | 环境、配置 |
| Causal Revision Tuple | 因果修订元组 | profile、index、algorithm revision 与时间共同构成的固定身份 | 环境、重放 |
| Thermal Capability | 温度适应能力 | 物种对偏冷、偏热、应激和致死区间的能力参数 | 温度 |
| Safety Classification | 安全分类 | 将事实区间归为安全、风险、致死或未知的步骤 | 环境 |
| Exposure Integral | 暴露积分 | 随时间累计的环境或呈现暴露量 | 溶氧、历史 |
| Audit | 审计 | 检查因果、质量守恒、Owner 和证据链是否可追溯 | 验证、治理 |
| Journal | 日志 / 账本存储 | 持久记录事件、结算和重放所需身份的存储 | 工程 |
| Journal Adapter | 日志适配器 | 为引擎提供可替换持久化接口的组件 | 工程 |
| Durable Journal | 持久日志 | 跨进程或重启仍可恢复的事件记录 | 工程 |
| Recovery Manifest | 恢复清单 | 重启恢复时校验版本、事件和状态完整性的清单 | 工程 |
| Editor | 编辑器 | 面向作者配置、校验、预览和提交的工具界面 | 编辑器 |
| Panel | 面板 | 编辑器中展示某一类配置或诊断信息的界面区域 | 编辑器 |
| Preview | 预览 | 不写入正式状态、用于检查规则输出的求值 | 编辑器、工程 |
| Commit Boundary | 承诺边界 | 从可继续互动转为一次性随机承诺的明确边界 | 转化、工程 |
| Seed | 随机种子 | 生成可重放随机判定的输入身份 | 工程、实验 |
| Scope | 作用域 | 决定身份、缓存和随机判定适用范围的边界 | 工程、治理 |
| Merge | 合并 | 并发或多来源结果按明确规则组合的操作，不等同于相加 | 历史、工程 |
| Arbitration | 仲裁 | 规则冲突或并发写入时选择唯一结果的过程 | DSL、工程 |
| Input-Rate Invariance | 输入速率不变性 | 相同逻辑输入以不同调用频率运行仍得到相同结果 | 验证 |
| Technical Actionability | 技术可执行性 | 能力、几何、时序等硬约束形成的可执行性判定 | 行为、工程 |
| Soft Difficulty | 软难度 | 保留给下游转化使用的连续或分级难度，不提前硬阻断 | 转化 |
| Conservation Sweep | 守恒扫描 | 对多组随机/边界样例检查质量和结算守恒的验证 | 实验、验证 |
| Monte Carlo | 蒙特卡洛 | 重复随机采样以估计概率或分布的实验方法 | 实验 |
| Bernoulli | 伯努利试验 | 每次只有成功/失败两种结果的随机试验模型 | 实验、入口 |
| CSV / JSON / YAML | CSV / JSON / YAML 数据格式 | 实验输出或配置交换格式；不改变机制语义 | 实验、配置 |

## 维护规则

1. 新增机制字段时，先在本表登记中文主标签、英文实现名和 Owner。
2. 中文主标签用于正文、图例和编辑器；英文实现名用于代码、Schema、日志和检索。
3. 同一概念只能有一个中文主译名；必要的同义词写在定义中，不在正文混用。
4. 若术语含义随上下文变化，拆成独立条目并写清适用边界，不用一个泛化译名覆盖。
