### 25.6. 身份、失败边界与最小生产桥接

这份交付的程序只用于复算纸面样本，不接入游戏，也没有实现一个新的 FCF Runtime。生产需要的桥接是：现有 Resolver 提供只读事实 → 表格加载器/受限 DSL 前端做相同类型与引用校验 → 同一评价语义 → 现有 Typed Result。每个例子的输入和数值输出可作为两种前端的共同验收样本。

身份 Worked Example：现有 Session S_demo 的 Active Channel 是 lure_A；一个已准入 Pause 对应 Root R_demo，系统已分配 Opportunity O_demo。packet 1 和 packet 2 引用同一 R_demo，即同一个 O_demo；外部现有 resolution owner 对该 Root 只结算一次。R_FIELD 仅消费传入 Scope，读同一 lure_A 的 FeedingMatch 与 FoodField。切换一个 frame 或重发 packet 不创建新 O、不重新抽签；新的被准入语义颗粒才由原 Owner 提供新身份。Static Bottom/Float 的一个合法静止姿态颗粒同理。本文不规定新 ID 拼接法、计时器、Reservation 或 Session 写回，不证明生产的幂等实现已经通过测试。

Gate 拒绝是有效类型结果0；输入缺失/非法表引用是 ValidationError；C14/C15 是范围外，不运行、更不伪造0。质量总和0、负权重、重复优先级、Predicate 环、非法 Slot 均是配置错误。表格与 DSL 同样不得写 Actor/World/FishGroup 状态，不得生成 RNG；Response 输出由既有下游消费，不创建 Follow/Attack 行为。播放器反馈可沿当前 trace 暴露“哪项条件失败/哪条 Channel 贡献最大”，但玩家是否看到这些诊断由产品层决定，本稿不添加新玩家按钮。

### 25.7. 用同一修改任务核对成本

这些是实际样本的编辑定位，不是测得的工时。共享 Parameter 修改会影响所有引用，Clone Profile 则必须改具名引用；两种表达都应显示受影响绑定。

<table header-row="true" fit-page-width="true">
<tr><td>修改</td><td>配置 A 的实际位置</td><td>中文脚本 B 的实际位置</td><td>语义约束</td></tr>
<tr><td>C06 入侵0.5对应0.6改为0.65</td><td>CurvePoint(profile=C06_R_Defense,x=0.5).y 一格</td><td>同一共享 CurvePoint 一格；脚本不变</td><td>调 Profile，不加 Feeding</td></tr>
<tr><td>C03 漂流阈值0.6改为0.7</td><td>Parameter C03_drift_value.value 一格</td><td>同一 Parameter 一格；脚本不变</td><td>不改 FIRST_MATCH 顺序</td></tr>
<tr><td>C03 高响应再加一个 AND 条件</td><td>新 Parameter + ATOM + PredicateMember，共3行</td><td>新 Parameter 1行 + 高响应条件表达式加一项</td><td>只能读白名单输入；不能凭添加字段假定上游已提供</td></tr>
<tr><td>C08 两通道输入相同，将 MAX 换成平均</td><td>改 R_DUAL_FIXED 模板聚合步骤1行及实现/验证</td><td>改固定聚合语句及实现/验证</td><td>属候选聚合设计变更；不能假装 Profile 参数能改拓扑</td></tr>
<tr><td>Q1 大装备 Large乘数1.5改1.6</td><td>QualityModifier(Q1,BigGear,Large).multiplier 一格</td><td>Q1 对应并列修正语句1处</td><td>不改其它桶、不读取中间分布</td></tr>
<tr><td>C05 关闭低光 Slot</td><td>Slot(C05_B,Light) enabled=false 且 ref_id=N/A，同一行2格</td><td>配置 Light=关闭；固定分支仍留在模板</td><td>不交换 Runtime Order</td></tr>
<tr><td>鲈鱼夏季目标氧门提前返回</td><td>本例已有 S_SUMMER step1；不能挪到归一化/Overlay之后</td><td>已有首条“若氧&lt;阈值返回0”</td><td>真正顺序意义来自提前返回和后续步骤的执行边界</td></tr>
</table>


算法差异与排版差异：C01 的 T×S×D 因子独立，调换计算次序仍同结果，不把印刷顺序冒充 L 增长证据；S_SUMMER 的 Gate 先失败即返回，后续适宜性不应执行。Cold 和 Summer 的因果链不同，即使一份通用脚本都能写出来，也不能据此宣称它们自动是同一固定模板。

### 25.8. 样本目录与设计统计的边界

本稿的固定模板名是可运行演示目录，不是重新裁决 L_final。按四个 Surface 分开计数并排除 C13 情景与 G3 合成例，样本使用：Group=1、Bake=4、Response=7、Quality=1。这些是 `N_fixture_templates`，不能改写成 `L_confirmed`：C01/C02/C05 的生产 Spatial Runtime Order 尚未定，C08 的结构已定但具体聚合待标定，Cold/Summer 的 MAX 和 ColdFront BLEND 也仍是 Working Candidate。没有把 C08/C09–C12 的过期结构未决重新打开。

共用关系已在 Binding 行上落实：C01/C02/C05/鲈鱼Normal/Guard 共享 S_FIXED（不同 Profile 与开关）；C03/C04 共享 R_BANDS；C06/C07/鲈鱼Guard 共享 R_DEFENSE；C09–C11 共享 R_FIELD；C12 Normal/鲈鱼Normal/Forage 共享 R_FEED；鲈鱼Cold/Summer 共享 R_FEED_REACTION；各群 Quality 共享 Q_PARALLEL、只换基准与修正；所有 Group 样例共享 G_SHARES。

PT3 未因双 Profile 或上游 Lifecycle 分群成为 REQUIRED；PT4 未因 Guard 产生 Defense vs Feeding precedence 压力。FIRST_MATCH 响应分档的行 priority 是模板内部既定比较语义，不是新买 PT4。C13 仍按范围解决，不制造特殊 Template。本稿完成具体表达，不替 Owner 做最终 DSL/Config 选型、生产参数冻结或全项目 closure。