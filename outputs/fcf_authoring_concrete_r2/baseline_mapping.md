Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d6a4137d2368151b762e50bc5ce6dfd as of 2026-09-09T06:52:18.484Z:
<page url="https://app.notion.com/p/3d6a4137d2368151b762e50bc5ce6dfd">
<ancestor-path>
<parent-page url="https://app.notion.com/p/3d6a4137d23681d99a2ac51f8f564d5f" title="Work Harness R0｜267 Fish → Logic Template Coverage / Escape Scan"/>
<ancestor-2-page url="https://app.notion.com/p/3d6a4137d23681309f9ff91cb3d7614b" title="0.3.4｜自定义执行顺序下的表达结构后果 R0"/>
<ancestor-3-page url="https://app.notion.com/p/3cfa4137d23681cca208eaa97dfe7767" title="中鱼机制 0.3.4｜逻辑框架升级（中间对齐骨架）"/>
<ancestor-4-page url="https://app.notion.com/p/3cda4137d23681508740ceff789abd41" title="FCF Design Branch｜Simplified Production V0｜Working Main"/>
<ancestor-5-page url="https://app.notion.com/p/3cda4137d236819dbbc0d371ee6084dd" title="Fish-Centric Conditional Funnel｜Design Branch Index"/>
<ancestor-6-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"title":"表达验证案例映射｜Pilot-A｜REP-R1｜C01–C15（Representation Case Mapping）"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
**中文化说明：** 本文保留 REP-R1 当时的冻结输入、统计、判定与审核记录，仅调整语言表达。当前流程状态以统筹中心为准，本次不重新裁定案例或启动后续阶段。
**标识对照：** FIT = 适配；UNCERTAIN = 未确定；OUT_OF_SCOPE = 范围外；PASS = 通过；POSSIBLE_SCHEMA_ESCAPE = 可能超出现有表达结构；POSSIBLE_NEW_COMPOSITION = 可能需要新组合。技术标识及机器判定值保留英文，便于与原协议对照。
**工作稿 / 表达验证证据 / 尚未提升为正式规格。** 2026-09-09。表达验证执行者的最终案例映射；不是独立审核报告。唯一输入范围为 <mention-page url="https://app.notion.com/p/3d6a4137d236816286c4ec21e387d973"/>。
## 阅读口径
共 15 个冻结机制故事，来自 14 个独立鱼种证据链；C09 与 C15 为同一 Paddlefish 的不同故事。5 个核心负例、2 个护巢压力、3 个食物场需求、1 个连续底食、2 个生命周期负压力、2 个仅作边界检查，逐项对应冻结集第 2–7 节。没有补入 8 条仅自检（Self-QA）的普通记录，也没有纳入 3 条身份隔离。
每条只有一个主处置结论（Outcome）。**最佳候选模板（Best PT）是候选定位，不是通过票；UNCERTAIN 行不会进入确认 FIT / L_observed。** 空间（Spatial）与响应（Response）是独立执行面，不能把同一因素跨面匿名重复结算。控制流骨架是静态表示推导，不是生物因果顺序实测或可执行运行时（Runtime）验证。
动作表达需求（Action Pressure）中 RETURN 若属于 PT1，是模板的固定出口，不是实例可任意插入的 RETURN；SET/SELECT 只在相应责任方白名单内成立。未绑定动作（Action）的行明确记不适用。中间结果依赖（Intermediate-result Dependency）的 POSSIBLE 在 C08/C12 仅指候选 SELECT 的结果被固定处理链（Pipeline）消费，已有 PT3 可吸收；没有证据要求 S4 或自由程序连接。
证据置信度（Evidence Confidence）评价本行**完整表示判断**的可信度；UNCERTAIN 不撤销上游已审生物事实。所有记录均保留源证据链的范围、阶段、来源访问限制。冻结集允许测试部分暂缓（Deferred）故事，不等于允许执行者关闭暂缓（Deferred）。
## 固定自检规则
每行均按六项执行：Q1 冻结范围及独立审核通过（Independent PASS）证据；Q2 输入/参数配置（Profile）与模板分轴；Q3 PT 自由度未扩大；Q4 执行面（Surface）/下游边界；Q5 控制流骨架精简且未假造事实；Q6 处置结论（Outcome）与已知/未知一致。逐行结果见自检（Self-QA），检查完成不等于事实/机制未决项已关闭。
## C01｜大西洋鳕鱼（Atlantic Cod）｜普通离散目标摄食
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681d8a687de638c693432"/>
**角色：** 核心适配案例
**执行面（Surface）：** 空间（Spatial）
**评价对象 / 输入范围（Evaluand / input scope）：** DiscreteTarget；本映射主面是当前位置的空间适配，TargetFeeding 保持既有响应（Response）边界。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 底层离散猎物摄食；已审钓饵/拟饵故事只支持靠近真实猎物水层。季节位置变化按种群限定，不推导特殊动作顺序。
**控制流骨架（Control-flow Skeleton）：**
```plain text
读取当前空间事实与已解析参数配置（Profile）引用（Ref）
→ 按声明顺序 APPLY_PROFILE（已有水层/栖地因素）
→ 固定合并计算输出空间（Spatial）限定类型的结果
```
**最佳候选模板（Best PT）：** PT1
**处置结论（Outcome）：** 通过参数适配（`FIT_WITH_PARAMETER`）
**实例使用的自由度（Instance Freedom Used）：** 已有空间因素槽位（Factor Slot）的引用（Ref）、参数和有限排序；本故事不要求新增硬关卡（Gate）。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** 既有水层/栖地参数配置（Profile）的物种参数绑定；不申请新能力。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 明确（CLEAR）
**未决维度（Unresolved dimension）：** 地域/季节参数未校准；不影响已声明的空间控制拓扑。
**自检（Self-QA）：** Q1–Q6 已检查；未把季节迁移写成新模式（Mode）；未把空间低适配重复写成响应（Response）惩罚。
## C02｜斑点叉尾鮰（Channel Catfish）｜离散目标与感官情境
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d2368195a862e6286e5cf034"/>
**角色：** 核心适配案例
**执行面（Surface）：** 空间（Spatial）
**评价对象 / 输入范围（Evaluand / input scope）：** DiscreteTarget + 空间/感官情境（Context）；空间（Spatial）主面，感官可达性保留暴露（Exposure）责任方。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 近底饵钓与夜间浅水位置利用得到已审支持；嗅味觉参与搜寻。冻结故事不覆盖洞巢防御动机。
**控制流骨架（Control-flow Skeleton）：**
```plain text
读取当前水层/栖地事实与参数配置（Profile）引用（Ref）
→ 有序 APPLY_PROFILE
→ 固定合并计算输出空间（Spatial）限定类型的结果
```
**最佳候选模板（Best PT）：** PT1
**处置结论（Outcome）：** 通过参数适配（`FIT_WITH_PARAMETER`）
**实例使用的自由度（Instance Freedom Used）：** 有限空间槽位（Slot）、日内配置与引用（Ref）绑定；感官不作为新步骤类型（StepType）。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** 既有底部/浅水/掩体参数；气味为呈现（Presentation）/暴露（Exposure）既有词表，不申请 ScentMode。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 明确（CLEAR）
**未决维度（Unresolved dimension）：** 具体感官阈值留校准；当前可达性事实不再重复改变食欲。
**自检（Self-QA）：** Q1–Q6 已检查；只用冻结普通摄食；排除本条工作稿中未被纳入的洞巢故事。
## C03｜虹鳟（Rainbow Trout）｜水流情境
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681528003cfc978d2c39b"/>
**角色：** 核心适配案例
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** DiscreteTarget；响应（Response）读取既有 FeedingMatch / 呈现关系的派生语义，再按 PT2 条件规则输出响应；空间存在与感知可达已在上游处理。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** Alaska 已审策略为卵/鱼肉模仿物随自然水流漂流。漂流的是离散食物，不能从名称新增 Drift 模式（Mode）。
**控制流骨架（Control-flow Skeleton）：**
```plain text
读取当前已准入的 FeedingMatch / 呈现关系事实
→ 有序谓词（Predicate）（已有 compare / AND）→ SET 限定类型的响应（Response）
→ 使用规则面固定默认值
```
**最佳候选模板（Best PT）：** PT2
**处置结论（Outcome）：** 通过既有谓词适配（`FIT_WITH_EXISTING_PREDICATE`）
**实例使用的自由度（Instance Freedom Used）：** 已有谓词（Predicate）操作数 / 阈值引用（Ref）与响应（Response） SET 绑定；FIRST_MATCH；不开放通道（Channel）调用或新增因素槽位（Factor Slot）。
**谓词表达需求（Predicate Pressure）：** ALL
**动作表达需求（Action Pressure）：** SET
**输入 / 参数配置扩展（Input / Profile Expansion）：** 已审地域的食物/呈现匹配参数绑定；沿用已有 Compare / AND，不新增 Match-the-Hatch 故事。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 较可能（LIKELY）
**未决维度（Unresolved dimension）：** 参数配置（Profile）内容和权重未校准；这是结构表达判断，未实测钓获率。
**自检（Self-QA）：** Q1–Q6 已检查；没有套用旧 Trout Flow 示例中的强 flow 关卡（Gate）或中途群组（Group）选择器（Selector）；没有计 steelhead 为第二样本。 冷审（Cold Review）：撤回未经逐项证明的响应（Response）因素槽位（Factor Slot）假设，改用验证框架明确支持的谓词（Predicate）→SET 响应（Response） PT2；未增加任何运行时（Runtime）能力。
## C04｜褐鳟（Brown Trout）｜仅普通摄食基线
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d236818fa4d2ddd5fa8b3c46"/>
**角色：** 核心适配案例
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** DiscreteTarget 普通摄食；不包含任何繁殖冲突或回归期非摄食响应（Response）。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 已审范围是获取离散动物性食物及留居/海鳟栖地差异。上游明确特殊策略故事为 NONE FOUND / NOT REQUIRED，按猎物与栖地选饵只是解释性推导。
**控制流骨架（Control-flow Skeleton）：**
```plain text
读取当前已准入的 FeedingMatch
→ 有序谓词（Predicate）（已有 compare）→ SET 限定类型的响应（Response）
→ 使用规则面固定默认值
```
**最佳候选模板（Best PT）：** PT2
**处置结论（Outcome）：** 通过既有谓词适配（`FIT_WITH_EXISTING_PREDICATE`）
**实例使用的自由度（Instance Freedom Used）：** 已有谓词（Predicate）操作数 / 阈值引用（Ref）与响应（Response） SET 绑定；FIRST_MATCH；不开放通道（Channel）调用或新增因素槽位（Factor Slot）。
**谓词表达需求（Predicate Pressure）：** 字段比较
**动作表达需求（Action Pressure）：** SET
**输入 / 参数配置扩展（Input / Profile Expansion）：** 既有离散食物匹配参数绑定；不创造生命周期子群或新谓词能力。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 较可能（LIKELY）
**未决维度（Unresolved dimension）：** 缺独立特殊钓法故事；本 FIT 仅为普通摄食机制表达，不作为玩家打法实验证据。
**自检（Self-QA）：** Q1–Q6 已检查；未将 Species Default 扩展为该物种所有策略均 Default；未搬入 Brown Trout conflict 案例库。 冷审（Cold Review）：撤回未经逐项证明的响应（Response）因素槽位（Factor Slot）假设，改用验证框架明确支持的谓词（Predicate）→SET 响应（Response） PT2；未增加任何运行时（Runtime）能力。
## C05｜玻璃梭鲈｜冻结的低光案例（证据: Walleye / Sander vitreus）
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681539ee4e534897defa2"/>
**角色：** 核心适配案例
**执行面（Surface）：** 空间（Spatial）
**评价对象 / 输入范围（Evaluand / input scope）：** DiscreteTarget；本面只表达光照 / 遮蔽对空间利用的影响。冻结的 Glass Zander 是本案例显示标签，不外推到另一物种。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 冻结 低光 故事对应证据链中 Walleye / Sander vitreus：晨昏可到浅滩，亮时利用阴影/深水。已审策略为随光照/季节调整位置，不新增 LowLight 模式（Mode）。
**控制流骨架（Control-flow Skeleton）：**
```plain text
读取当前光照/水层/掩体事实
→ 有序 APPLY_PROFILE（已有空间槽位（Slot））
→ 固定合并计算输出空间（Spatial）限定类型的结果
```
**最佳候选模板（Best PT）：** PT1
**处置结论（Outcome）：** 通过参数适配（`FIT_WITH_PARAMETER`）
**实例使用的自由度（Instance Freedom Used）：** 已有光照 / 遮蔽 / 深度槽位（Slot）的物种参数配置（Profile）参数、引用（Ref）和排序。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** 既有低光/遮蔽/深浅参数配置（Profile）参数；无新感知通道（Channel）。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 明确（CLEAR）
**未决维度（Unresolved dimension）：** 若以后要求显式 行为模式→参数配置 选择器，可测试 PT3；本冻结故事未要求该额外控制流。
**自检（Self-QA）：** Q1–Q6 已检查；核对 公共 事实复核层 与证据学名一致；低光可达性与栖地后果分开，未追加匿名响应（Response）加成。
## C06｜蓝鳃太阳鱼（Bluegill Sunfish）｜护巢
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681ff8ea6d954a69f7385"/>
**角色：** 挑战案例 / 模式需求
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** DiscreteTarget + 当前巢关系/照护条件（Condition）；TargetFeeding 与 RelationalConflict。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 部分雄鱼预先建立并持续照护巢区；入侵者与小拟饵可引发防御响应。普通进食仍存在，证据未指定两个动机同时成立时的精确优先级。
**控制流骨架（Control-flow Skeleton）：**
```plain text
候选：有序 predicates（照护条件（Condition） AND 当前巢关系/威胁；普通食物匹配）
→ 既有限定类型的响应（Response）动作
→ 同时命中时的策略未定；不得把 SELECT channel 当作 EVAL channel
```
**最佳候选模板（Best PT）：** PT2
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 候选使用已有 ALL/Compare 与 SET/RETURN；FIRST_MATCH/APPLY_ALL 的故事级选择未获证。
**谓词表达需求（Predicate Pressure）：** ALL
**动作表达需求（Action Pressure）：** SET / RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** 当前照护条件（Condition） / 临时巢关系的只读输入绑定；具体白名单与责任方接口仍 OPEN，不新增持久 锚点。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** K1：条件（Condition） + 关系 + PT2 候选，竞争持久程序（Program）程序包（Bundle） / PT4；仅局部谓词可表达，整故事未闭合。
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R01：多动机同时成立时的输出/优先策略；R02：跨执行面（Surface）程序包身份的必要性未证。
**自检（Self-QA）：** Q1–Q6 已检查；不把护巢存在性当成防御（Defense）-first 决定性 返回 的事实；不把 PT2 扩为 EVAL_CHILD_PROGRAM。
## C07｜小口黑鲈（Smallmouth Bass）｜护巢 / 护幼
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681759b0fff070b2f0e4c"/>
**角色：** 挑战案例 / 模式需求
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** DiscreteTarget + 当前照护/幼体关系；冻结的是护巢/护幼压力，不纳入另一个扰底跟随故事。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 雄鱼照护巢与幼鱼；照护状态支持区别于普通猎物获取的关系性响应。第二轮审核明确不证明 Suski 2003 的具体钓放/窝内损失效应，本轮不使用该效应构造时间反馈算法。
**控制流骨架（Control-flow Skeleton）：**
```plain text
候选：有序 predicates（照护条件（Condition） AND 当前关系；普通食物匹配）
→ 既有限定类型的响应（Response）动作
→ 重叠 / 默认值策略未定
```
**最佳候选模板（Best PT）：** PT2
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 已有 ALL/Compare、SET/RETURN 的候选绑定；不加自由调用、状态变更或循环。
**谓词表达需求（Predicate Pressure）：** ALL
**动作表达需求（Action Pressure）：** SET / RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** 照护阶段/幼体关系输入绑定；不把未审损失效应写为新动态字段。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** K1：与 C06 共用低自由度条件结构候选；不同关系参数不自动产生第二个模板。
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R01 / R02 同 C06；迁徙幅度缺口与本响应（Response）故事分开。
**自检（Self-QA）：** Q1–Q6 已检查；未套用旧 Spawn Guard Bass 的固定防御（Defense）→摄食（Feeding）作为本鱼事实；未把下一机会照护变化误作本次中间结果依赖。
## C08｜尼罗罗非鱼（Nile Tilapia）｜刮食与悬浮颗粒摄食混合
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d236819e93c1f2cf006532b8"/>
**角色：** 挑战案例 / 食物场机会
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** ResourcePatch / FoodField / DiscreteTarget 的食物情境差异；保留限定类型的评价器竞争解释。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 已审证据支持刮取附着物及截留悬浮颗粒，摄食方式随食物环境变化。没有已闭合的玩家造场/钩饵策略故事，不纳入口孵特殊钓法。
**控制流骨架（Control-flow Skeleton）：**
```plain text
候选：PT2-style 选择器读取已给定食物情境
→ SELECT 有限限定类型的参数配置/Variant 引用（Ref）
→ 固定 PT1-style 处理链；食物场机会责任方/输入尚未闭合
```
**最佳候选模板（Best PT）：** PT3
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 候选仅 SELECT 限定类型的参数配置/Variant 后固定处理链（Pipeline）；若必须调用不同程序则本候选失效。
**谓词表达需求（Predicate Pressure）：** ALL
**动作表达需求（Action Pressure）：** SELECT / RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** V1 FoodField 快照 + V2 限定类型的食物评价器/参数配置 绑定（见扩展登记）；非新模板。
**组合需求（Composition Pressure）：** PT3_FIXED
**中间结果依赖（Intermediate-result Dependency）：** 可能（POSSIBLE）
**压缩候选（Compression Candidate）：** K2：食物情境选择 + 限定类型的评价器，竞争独立食物场（Field） Grammar；不改上游暂缓（Deferred）。
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R03：食物场（Field）身份/生命周期/去重、同一供给防重复；R04：玩家呈现与自然摄食的连接；相斥/同时可用 情境 的选择策略未定。
**自检（Self-QA）：** Q1–Q6 已检查；只做候选拓扑；不把 SELECT ChannelRef 假称已经执行；不把混合摄食变成可自由拼接的程序（Program）。
## C09｜鸭嘴鲟（American Paddlefish）｜滤食
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681a48773c46adf6abba6"/>
**角色：** 挑战案例 / 食物场机会
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** FoodField + FieldFeeding；只测试一次合法机会下的有限评价，不假定机会已定义。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 冻结成鱼游泳滤食证据；颗粒摄取证据有早期阶段及两尾圈养鱼限制。常见锚钩捕获（snagging）不支持主动接受钩饵，本故事与 C15 分开。
**控制流骨架（Control-flow Skeleton）：**
```plain text
候选：读取合法食物场机会快照
→ 有序 APPLY_PROFILE（暴露/食物适配按责任方分面）
→ 固定限定类型的结果；机会创建/去重在模板之外仍 OPEN
```
**最佳候选模板（Best PT）：** PT1
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 有限已有因素槽位（Factor Slot） + 限定类型的颗粒 / 食物参数配置（Profile）引用（Ref）；不把连续时间放入实例循环。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** V1 / V2：FoodField 与食物适配参数配置（Profile）；具体输入 协议 OPEN。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** K2：连续摄食不必购买新 Grammar；候选 PT1 不证明跨机会生命周期已经适配。
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R03 / R04；若无合法离散机会，有限求值只是条件式，不算 FIT。
**自检（Self-QA）：** Q1–Q6 已检查；未借锚钩捕获（snagging）填响应（Response）；未将圈养颗粒摄取泛化为野外全龄。
## C10｜大口牛胭脂鱼（Bigmouth Buffalo）｜滤食
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d2368139bf62f16e80bdf503"/>
**角色：** 挑战案例 / 食物场机会
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** FoodField + FieldFeeding；与 C09 同候选评价器，不因第二个物种增加模板。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** Wabash River 已审材料支持滤食，构成另一物种的同类压力。官方资料少见钩线捕获，不足以建立稳定钩饵吸引链。
**控制流骨架（Control-flow Skeleton）：**
```plain text
候选：读取合法食物场机会快照
→ 有序 APPLY_PROFILE
→ 固定限定类型的结果；身份 / 去重 / 交接未定
```
**最佳候选模板（Best PT）：** PT1
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 同质因素槽位（Factor Slot）和食物/颗粒参数配置（Profile）参数；无分支 / 跳转。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** 复用 V1 / V2；只增加物种参数，不再计一个词表类。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** K2：复用 C09 限定类型的评价器候选，保留两物种独立事实但不重复计结构。
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R03 / R04；自然滤食不是完整玩家机会合同。
**自检（Self-QA）：** Q1–Q6 已检查；未把 P1 n=3 写成三个已验证玩家造场策略；未把未定义输入当结构越界（Escape）。
## C11｜鲻鱼（Flathead Grey Mullet）｜持续底部 / 底质觅食
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681f2af3ed529d8a54f18"/>
**角色：** 挑战案例 / 连续资源
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** ResourcePatch；响应（Response）通道（Channel）仍未判定，不能用空数组推为 TargetFeeding。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 已审自然摄食包括吸取底泥表层、刮取附着物。自然连续底食与特定钩饵呈现的对应机制未闭合。
**控制流骨架（Control-flow Skeleton）：**
```plain text
候选：读取 ResourcePatch 与当前暴露快照
→ 有限限定类型的参数配置评价
→ 输出当前 执行面 结果；是否存在合法玩家钩饵交接未定
```
**最佳候选模板（Best PT）：** PT1
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 只提出有限 因素/参数配置（Profile）绑定；不新增 刮食 动作或 持续 循环。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** V3 底质资源评价器/参数配置 候选；不是已存在通道（Channel）。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** K3：ResourcePatch 情境 / 限定类型的评价器，竞争独立连续底食程序；没有证据允许压成单次咬食。
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R04：玩家钩饵 目标、输入粒度与通道（Channel）责任方；连续过程是否全属下游亦未定。
**自检（Self-QA）：** Q1–Q6 已检查；未把自然摄食离散化后宣布成功；未把资源区与离散猎物同义化。
## C12｜大西洋鲑鱼（Atlantic Salmon）｜普通成长与繁殖洄游
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681d1b26ed8d7102ec625"/>
**角色：** 生命周期 / 对群组划分必要性的负向检验
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** 生长/繁殖阶段情境（Context）；不允许用回归期做新通道（Channel） Fit。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 生长期摄取离散动物性食物，繁殖洄游有停食描述。回归期拟饵响应原因没有闭合，生命周期差异只支持 GroupPressure Possible。
**控制流骨架（Control-flow Skeleton）：**
```plain text
候选：阶段情境（Context） → SELECT 已定义阶段参数配置（Profile）
→ 固定处理链（Pipeline）表达已知摄食约束
→ 回归期非摄食响应（Response）未知，整故事停止定案
```
**最佳候选模板（Best PT）：** PT3
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 候选限定类型的 阶段/参数配置 选择；不生成互斥供给身份或 ReactionMode。
**谓词表达需求（Predicate Pressure）：** ALL
**动作表达需求（Action Pressure）：** SELECT / RETURN
**输入 / 参数配置扩展（Input / Profile Expansion）：** 既有阶段情境（Context）/参数配置（Profile）的参数候选；不新增正式词表。
**组合需求（Composition Pressure）：** PT3_FIXED
**中间结果依赖（Intermediate-result Dependency）：** 可能（POSSIBLE）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R05：回归期响应动机；不以一个摄食（Feeding） CAP 推为所有响应（Response）均低。
**自检（Self-QA）：** Q1–Q6 已检查；普通生长期可局部复用 PT1，但未拆成新 FIT 行稀释未决比例。
## C13｜红鲑鱼（Sockeye Salmon）｜有滤食证据但阶段范围未明
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d2368183a2a6c257bafd6426"/>
**角色：** 生命周期 / 对群组划分必要性的负向检验
**执行面（Surface）：** 响应（Response）
**评价对象 / 输入范围（Evaluand / input scope）：** FoodField / DiscreteTarget 竞争解释尚未选定；不计已闭合 FieldOpportunity 正例。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 冻结的是已有正向鳃耙滤食描述，同时年龄、海迁/陆封型与实际摄食动作未映射闭合。不得将该不确定性解释成没有滤食证据。
**控制流骨架（Control-flow Skeleton）：**
```plain text
确认阶段/动作范围
→ 目前不能选择食物场（Field）或 discrete 评价器
→ 不生成可计入 FIT 的运行骨架
```
**最佳候选模板（Best PT）：** 无（None）
**处置结论（Outcome）：** 未确定（`UNCERTAIN`）
**实例使用的自由度（Instance Freedom Used）：** 未绑定实例控制流。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** 无：未绑定动作（Action）（不计入动作（Action）类型计数）
**输入 / 参数配置扩展（Input / Profile Expansion）：** 无新增；已有证据所需的阶段精度缺失。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 未确定（UNCERTAIN）
**未决维度（Unresolved dimension）：** R05：连续滤水 vs 逐粒摄取后保留的阶段化证据；不重新研究关闭它。
**自检（Self-QA）：** Q1–Q6 已检查；正向证据与不确定性同时保留；不计入 K2 的三条食物场挑战案例。
## C14｜海七鳃鳗（Sea lamprey）｜HostAttachmentFeeding
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681b6a907f475138affea"/>
**角色：** 仅作边界检查
**执行面（Surface）：** 其他（Other）
**评价对象 / 输入范围（Evaluand / input scope）：** HostAttachmentFeeding 的持续附着；不纳入幼体滤食或完整生活史 PT Fit。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 寄生阶段口盘附着宿主并持续摄食；常规拟饵与附着机制的玩法联系未获证。A4 明确作为实例化后/产品范围边界。
**控制流骨架（Control-flow Skeleton）：**
```plain text
实例化后建立/维持宿主关系
→ 持续附着行为归下游
→ 不进入本轮生成前 PT Fit
```
**最佳候选模板（Best PT）：** 无（None）
**处置结论（Outcome）：** 范围外（`OUT_OF_SCOPE`）
**实例使用的自由度（Instance Freedom Used）：** 未使用。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** 无：未绑定动作（Action）（不计入动作（Action）类型计数）
**输入 / 参数配置扩展（Input / Profile Expansion）：** 无；本轮不创建寄生输入/动作。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 明确（CLEAR）
**未决维度（Unresolved dimension）：** PRODUCT_SCOPE_DEFERRED；持续寄生玩法是否纳入由产品/下游责任方（Owner）决定。
**自检（Self-QA）：** Q1–Q6 已检查；未拿附着循环当生成前结构越界（Escape）；未映射上游未冻结的幼体故事。
## C15｜鸭嘴鲟（Paddlefish）｜锚钩捕获（snagging）
**鱼种 / 案例 / 证据链（Fish / Case / Evidence Chain）：** <mention-page url="https://app.notion.com/p/3d6a4137d23681a48773c46adf6abba6"/>
**角色：** 仅作边界检查
**执行面（Surface）：** 其他（Other）
**评价对象 / 输入范围（Evaluand / input scope）：** 响应（Response）-independent capture；独立故事计数，但与 C09 共用同一物种和证据链。
**已审机制故事 / 稳定语义主张（Audited Story / stable semantic claim）：** 已审捕获方式包含锚钩捕获（snagging），不能作为自愿接受钩饵证据。A4 将其列为响应无关捕获边界。
**控制流骨架（Control-flow Skeleton）：**
```plain text
捕获/接触（Contact）路径
→ 不以摄食（Feeding）响应（Response）为前提
→ 本轮不要求 PT1–PT4 覆盖
```
**最佳候选模板（Best PT）：** 无（None）
**处置结论（Outcome）：** 范围外（`OUT_OF_SCOPE`）
**实例使用的自由度（Instance Freedom Used）：** 未使用。
**谓词表达需求（Predicate Pressure）：** 无（NONE）
**动作表达需求（Action Pressure）：** 无：未绑定动作（Action）（不计入动作（Action）类型计数）
**输入 / 参数配置扩展（Input / Profile Expansion）：** 无；不增加摄食（Feeding）动作（Action）。
**组合需求（Composition Pressure）：** 无（NONE）
**中间结果依赖（Intermediate-result Dependency）：** 否（NO）
**压缩候选（Compression Candidate）：** 无（NONE）
**现有结构无法表达的原因（Escape Reason）：** 不适用；本行未标 POSSIBLE_SCHEMA_ESCAPE。
**证据置信度（Evidence Confidence）：** 明确（CLEAR）
**未决维度（Unresolved dimension）：** PRODUCT_SCOPE_DEFERRED；是否纳入捕获玩法与接触（Contact）接口由下游处理。
**自检（Self-QA）：** Q1–Q6 已检查；未把捕获结果倒推出响应（Response）；未将两条 Paddlefish 故事作为两独立物种。
## 状态与消费边界
确认 FIT：C01–C05；候选但未定案：C06–C13；明确范围外：C14–C15。任何后续完整 FIT 必须说明如何消除本行未决项，不能只把本行处置结论（Outcome）换名。冷审（Cold Review）的逐项攻击、统计分母、生产模板计数与下一步建议统一在正式审核包中提供：<mention-page url="https://app.notion.com/p/3d6a4137d2368165b064dab4b0db8f60"/>。本页未新增 PT5/PT6、食物场机会协议、模式（Mode）身份或状态写回规则。
</content>
</page>
