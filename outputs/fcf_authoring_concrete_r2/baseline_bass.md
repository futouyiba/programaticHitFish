Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d6a4137d23681e2af96e873eef9411a as of 2026-09-09T10:25:50.469Z:
<page url="https://app.notion.com/p/3d6a4137d23681e2af96e873eef9411a">
<ancestor-path>
<parent-page url="https://app.notion.com/p/3cfa4137d23681cca208eaa97dfe7767" title="中鱼机制 0.3.4｜逻辑框架升级（中间对齐骨架）"/>
<ancestor-2-page url="https://app.notion.com/p/3cda4137d23681508740ceff789abd41" title="FCF Design Branch｜Simplified Production V0｜Working Main"/>
<ancestor-3-page url="https://app.notion.com/p/3cda4137d236819dbbc0d371ee6084dd" title="Fish-Centric Conditional Funnel｜Design Branch Index"/>
<ancestor-4-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"title":"大口黑鲈单鱼深挖 R0｜FishGroup × Bake × Response × Quality"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
**Status：WORKING / SINGLE-FISH DEEP DIVE / NOT AUTHORITY / NOT PROMOTED**
本页用于把大口黑鲈作为第一条完整生产样板鱼，纵向打穿：
```plain text
Group Routing
→ Bake / Spatial
→ Response
→ Quality Selection
```
本页不等待 15 Case 铺量结果；后者作为横向覆盖 / breaker 输入，回来后再攻击本页。
### 0.1 与旧 Bass Concrete Spec R1、Representation Stress Test 的关系
旧页 <mention-page url="https://app.notion.com/p/3cda4137d236819198fecae3c69570b5"/> 是同一 Simplified V0 分支上的早期 Working Discussion Spec。**它不是本页的 Current Authority，也不自动继承其旧 Mode / Task / Conversion 架构。** 本页把它作为：
```plain text
Reference
+
Negative Knowledge
+
已经验证过的 Bass Strategy Story 来源
```
只显式吸纳仍与当前四执行面兼容的知识。
当前 <mention-page url="https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3"/> 的职责不同：
```plain text
Bass 单鱼深挖
    → 决定“这条鱼实际应该有什么行为组 / 策略故事 / 因果”

Representation Stress Test
    → 读取已经形成的 Bass Working Snapshot
    → 投影成 Config / RuleSet / 中文 DSL
    → 比较 Authoring 成本
```
因此：**鱼类机制设计只在本页闭合；Representation 页只维护必要的派生投影，不复制整套生态理由和设计推演。** 当本页某个 Group 达到 Working Baseline 后，再回写一份最小可复核 Projection 到 Stress Test。
## 1. 当前 Working 候选组
<table fit-page-width="true" header-row="true">
<tr>
<td>FishGroup / 状态</td>
<td>当前判断</td>
<td>核心玩家体验</td>
<td>是否同时改变 Bake + Response</td>
</tr>
<tr>
<td>Normal Feeding</td>
<td>KEEP</td>
<td>普通结构 / 食物 / 呈现逻辑</td>
<td>基线</td>
</tr>
<tr>
<td>Spawn Guard / Parental</td>
<td>KEEP</td>
<td>找护巢区域，用侵入 / 防御触发而不是普通 Feeding</td>
<td>YES</td>
</tr>
<tr>
<td>Cold-Slow / Winter Quiescent</td>
<td>STRONG CANDIDATE</td>
<td>找相对暖、稳定、低能耗冬季 refuge；慢速 / 停顿 / 贴鱼位更有效</td>
<td>YES</td>
</tr>
<tr>
<td>Summer Oxythermal Stress</td>
<td>STRONG CANDIDATE</td>
<td>温度与深层低氧共同压缩可用水层；普通 Feeding Readiness 降低，但近距离强刺激 reaction 可保留</td>
<td>YES</td>
</tr>
<tr>
<td>High Angling Pressure</td>
<td>OVERLAY / NOT GROUP</td>
<td>熟悉 Cue / lure response 降低，新奇呈现相对占优</td>
<td>当前主要 Response</td>
</tr>
<tr>
<td>Open-water Forage Chase</td>
<td>BREAKER CANDIDATE</td>
<td>若确认跟随 prey field、开放水主动巡猎并换一套 Response，则可能升 Group</td>
<td>待证</td>
</tr>
<tr>
<td>Post-spawn Recovery</td>
<td>OVERLAY by default</td>
<td>Readiness / Activity 修正</td>
<td>当前未证</td>
</tr>
</table>
## 2. FishGroup 准入规则
不是“这个因素影响很大”就升 Group。
当前准入原则：
> 一个条件如果会在有意义的时间窗口内，稳定地让**多个执行面的逻辑一起换挡**，尤其同时改变 Bake 的空间解释和 Response 的有效呈现方式，才优先升 FishGroup。
如果只是 Profile 数值、Activity、FeedingReadiness、Cue Familiarity 连续变化，优先留在 Context / Profile / Overlay。
## 3. Group Routing 最小权重语义
Group Router 直接从同一个 Species Base Snapshot 产出各 Group 的目标权重，不使用“先从 Normal 扣一块，再扣下一块”的可编辑顺序。
```plain text
SpeciesBaseWeight = W

如果 GuardingEligibility 成立：
    GuardingWeight = W × @GuardingShare
否则：
    GuardingWeight = 0

如果 ColdSlowEligibility 成立：
    ColdSlowWeight = W × @ColdSlowShare
否则：
    ColdSlowWeight = 0

...

NormalWeight = W × RemainingShare
```
多个 Special Group 若允许同时命中，必须显式定义 share contract；默认不允许静默超配 / 静默归一化。
**吸收旧 R1 的一条防重计知识：** `Group Share` 只表达“当前 Species Supply 中多少进入这个行为逻辑”，而 Bake 再回答“这个 Group 在具体空间哪里成立”。不能同时用 Group Share 和局部 Habitat / Source Weight 重复表达同一个 Guard / refuge 事实。
旧 R1 曾采用 source-local `ModeAvailabilityFactor → LocalModeShare` 的方案，并取消全局固定 Mode 守恒。当前 0.3.4 已重新引入显式 FishGroup Routing，因此**不直接继承旧算法**；但需要保留它揭示的问题：
```plain text
Group Routing：行为组成 / eligibility
Bake：局部空间适配

二者不得因为同一条件重复扣权重。
```
`@GuardingShare` 当前仍作为 Group Routing 配置参数 Candidate；是否最终采用严格 Species-level partition，需在多 Group overlap Case 中继续验证。
## 4. Guarding Group｜当前已闭设计
### 4.1 Routing
```plain text
读取 繁殖窗口
读取 持续水温条件
读取 场内适合筑巢结构

如果 GuardingEligibility 成立：
    读取 @GuardingShare
    分配 Guarding Group 权重
```
### 4.2 Bake
Guarding Group 的空间重点围绕巢区 / 适合筑巢结构，而不是普通觅食空间。
### 4.3 Response
```plain text
如果当前 FishGroup == Guarding：
    评价玩家 Presentation 是否构成护巢 / 护幼威胁
    返回 Defense Response
    不再评价普通 Feeding
```
这是主动 gameplay simplification，不声称现实鱼完全不能摄食。
## 5. Cold-Slow Group｜Strong Candidate
### 5.1 Routing
入口应读取水体 / 大区级 Thermal State，不用当前抛点水温瞬时切组。
```plain text
如果整个可达水体进入 Severe Cold
并且普通暖水 habitat 基本消失：
    提高 ColdSlow Group Share
```
### 5.2 Bake
普通模式问：
```plain text
哪里接近正常最适条件？
```
Cold-Slow 问：
```plain text
在整体已经偏冷的前提下，哪里相对更暖、更稳定、流速 / 能耗更低、适合冬季 refuge？
```
### 5.3 Response
旧 Bass Concrete Spec R1 留下了一条应当继承的策略故事：**Cold Water Fast-Activate → Slow-Convert**。也就是说，冷水不是“速度快的刺激一律无效”，而是要把“触发注意 / 短爆发”与“持续追逐要求”拆开。
当前 Pre-generation Response 不恢复旧的 post-engagement Task / Conversion 模块，但吸收其因果区分：
```plain text
读取 当前 Presentation 的刺激显著度
    振动 / 闪光 / 突发位移 / 贴近程度

读取 当前 Presentation 对持续追逐的要求
    持续速度
    需要跟随的距离 / 时间

Cold-Slow：
    高持续追逐要求 → 强抑制
    慢速、长停顿、贴近鱼位 → 相对有利
    短时高显著度刺激 → 可以触发 reaction，不因“快”字本身被一刀切关闭
```
因此 Cold-Slow 的 Response 重点不是简单 `speed <= threshold`，而是至少要区分：
```plain text
Trigger / Salience
vs
Sustained Pursuit Demand
```
这两个语义是否需要成为正式 Response 输入，留给后续 Representation / Contract 验证。
## 6. Summer Oxythermal Stress Group｜Strong Candidate
### 6.1 Routing
不是“当前点水温高”就切组，而是读取水体级状态：
```plain text
上层持续过热
+ 深层 / 下层出现明显低氧或不可用区
+ 可用 habitat 被压缩到有限水层 / refuge
```
### 6.2 Bake
核心不是单独追求正常最适温度，而是多约束权衡：
```plain text
读取 当前目标水层温度
读取 当前目标水层溶氧
读取 光照 / 可视性
读取 cover / structure
读取 prey field

如果溶氧达到不可用区：
    强 Gate / 极低权重
否则：
    评价相对降温收益
    评价溶氧安全余量
    评价可视性 / prey / cover 价值
    合并为当前 stress 状态下的 refuge suitability
```
光照 / 可视性当前视为软约束，不先定义成绝对深度下限。
### 6.3 Response
Working gameplay hypothesis：
```plain text
普通 Feeding Readiness：下降
高持续追逐要求：不占优

如果 Presentation 同时满足：
    高 Trigger / Salience
    + 较低持续追逐成本
    + 近距离进入有效区域

则：
    Reaction Channel 可以相对增强
```
候选 Cue 包括：
```plain text
振动
闪光
突发加速 / 停顿
deflection / erratic motion
近距离侵入
```
这里吸收旧 R1 的另一条负面知识：**不要新增一个不可解释的全局 ****`ReactionBonus`****。** 反应口优势应尽量追溯到具体 Cue、局部暴露 / proximity、Cue Familiarity，以及 Presentation 要求的持续追逐成本。
需要明确区分：
- 高温 / 低氧造成 stress 与空间限制：现实证据较强；
- “闪光 / 振动 reaction bite”作为具体 Response Program：当前属于玩家经验 + 垂钓实践支持的 Design Hypothesis，需继续验证，不伪装成生物学硬事实。
## 7. High Angling Pressure｜Overlay
```plain text
AnglingPressure / CueFamiliarity
→ 熟悉 Cue / Presentation Response 下调
→ 新奇 / 不同 Presentation 相对占优
```
当前不改变独立 Bake Program，因此不升 Group，避免：
```plain text
Cold + Pressured
Guarding + Pressured
SummerStress + Pressured
...
```
的 Group 笛卡尔积。
## 8. Open-water Forage Chase｜强 Breaker Candidate
旧 R1 已经明确提醒：**植被伏击不应因为“像一种行为”就自动升级成 AMBUSH_BASS_MODE**；很多植被差异可以由局部 Exposure / geometry / Habitat 解释。这个负面知识继续保留。
但 Open-water Forage Chase 比“伏击”更值得继续攻击，因为已有现实资料显示，在某些水体与体型段，大口黑鲈会明显转向开放水、成群利用 threadfin / gizzard shad；另一些大型个体仍更多靠近结构独居伏击。也就是说，它可能同时包含：
```plain text
Prey Field / 水体类型
×
Fish Size / Quality
×
Behavior Group
```
候选故事：
```plain text
Forage-Chase Group：
    Bake：结构依赖下降，更多跟随 pelagic prey field / open-water zone
    Response：moving / search presentation 的有效性明显提高

Normal / Ambush-oriented：
    Bake：structure / cover 仍是重要锚点
    Response：更依赖局部经过、停顿、deflection / target presentation
```
**新的关键 Breaker：体型依赖。** 如果只有某些尺寸 / 品质明显进入 open-water chase，而当前主链坚持“先抽 FishGroup、后抽 Quality”，就需要验证：
```plain text
A. Forage-Chase Group 自带不同的基础 Quality Distribution / Modifier
还是
B. Group Routing 必须提前知道 Quality
```
当前优先验证 A，避免打乱“Group → Quality Selection”的主链。
结论仍未 Promote：如果最终只是 prey availability 改变，且普通 Spatial + Response Profile 足够，则不升 Group；如果 Bake + Response 稳定换挡，且这种差异在可玩体型上具有足够覆盖，则升级为 FishGroup。
## 9. Cause → Surface Ownership｜防止同一原因重复结算
以 Summer Stress 为例：
<table fit-page-width="true" header-row="true">
<tr>
<td>Cause</td>
<td>Surface</td>
<td>负责的唯一语义</td>
<td>禁止重复</td>
</tr>
<tr>
<td>高温 + 分层 + 深层低氧</td>
<td>Group Routing</td>
<td>是否进入 SummerStress / Share</td>
<td>不要在这里直接再算具体点位空间 Fit</td>
</tr>
<tr>
<td>同一环境事实</td>
<td>Bake</td>
<td>该 Group 内具体在哪个深度 / refuge 分布</td>
<td>不要重复扣一次“因为已经进 Stress Group 所以再 -30%”</td>
</tr>
<tr>
<td>Stress Group</td>
<td>Response</td>
<td>普通 Feeding / pursuit / Reaction Channel 怎么变</td>
<td>不要再次无解释乘一个高温总惩罚</td>
</tr>
<tr>
<td>高温</td>
<td>Quality</td>
<td>只有有证据证明不同品质相对可钓性变化时才进入</td>
<td>禁止因为前三面出现过就顺手再扣</td>
</tr>
</table>
## 10. 从旧 R1 吸纳 / 拒绝的知识清单
<table fit-page-width="true" header-row="true">
<tr>
<td>旧 R1 内容</td>
<td>当前处理</td>
<td>原因</td>
</tr>
<tr>
<td>Guard / nest threat 是独立行为 grammar</td>
<td>ADOPT</td>
<td>与当前 Guarding FishGroup 一致；当前进一步采用 Defense-only simplification。</td>
</tr>
<tr>
<td>Cold Water Fast-Activate → Slow-Convert</td>
<td>ADOPT AS STRATEGY STORY</td>
<td>保留“短刺激可触发、持续追逐更难”的因果；不恢复旧 Task / Conversion runtime。</td>
</tr>
<tr>
<td>高钓压与 Cue Familiarity 分离</td>
<td>ADOPT</td>
<td>支持 High Pressure 作为 Response Overlay，而非 FishGroup。</td>
</tr>
<tr>
<td>ActivityState 作为总括状态被删除</td>
<td>ADOPT AS NEGATIVE KNOWLEDGE</td>
<td>避免用一个“活性”黑箱重复解释 Spatial / Response / pursuit 差异。</td>
</tr>
<tr>
<td>植被伏击不自动升 AMBUSH Mode</td>
<td>ADOPT AS NEGATIVE KNOWLEDGE</td>
<td>优先用 Habitat / geometry / Exposure 解释。</td>
</tr>
<tr>
<td>source-local ModeAvailability / LocalModeShare 具体算法</td>
<td>REFERENCE ONLY</td>
<td>当前 0.3.4 已重新引入显式 FishGroup Routing，不能直接继承旧算法；只继承防重计原则。</td>
</tr>
<tr>
<td>Task / Conversion / Contact / Hook 完整下游拓扑</td>
<td>OUT OF CURRENT DEEP-DIVE SCOPE</td>
<td>当前四执行面聚焦生成前；不把旧下游模块偷渡回本轮 Representation。</td>
</tr>
</table>
## 11. 本轮继续深挖的问题
1. Guard / Cold-Slow / SummerStress 的 Group Share 是互斥分群、部分并存还是按条件直接独占？
2. Cold-Slow 与 SummerStress 更适合“硬切 Group + hysteresis”，还是“慢速环境事实 → 连续 Group Share”，从而避免边界频繁跳变？
3. Cold-Slow / SummerStress 是否共同需要 `TriggerSalience` 与 `SustainedPursuitDemand` 两类 Response 语义，还是可以用现有 Cue / Presentation 字段压缩表达？
4. SummerStress 的 Reaction Channel 到底需要哪些最小 Cue：flash / vibration / acceleration / deflection / proximity 中哪些是真正独立输入？
5. Open-water Forage Chase 是否真的值得新 Group；若值得，体型 / Quality 依赖如何在“Group → Quality”顺序下表达？
6. Quality Selection 在不同 Group 下是否需要 Group-specific base distribution / modifier，还是保持 Species / Quality 层独立。
## 12. Group Routing 当前候选：连续 Share，而不是持久状态机
### 12.1 先回答 hysteresis
当前更低复杂度的方案是：**FishGroup Routing 不做“这条虚拟鱼昨天进入 ColdSlow、今天退出 ColdSlow”的持久状态机。**
在生成前系统里，每次使用同一份慢速环境快照，确定性计算 Species 当前各 Group 的 Share：
```plain text
Slow Context Snapshot
    ↓
GuardingEligibility / ColdSeverity / OxythermalCompression / ForageState
    ↓
Group Share Vector
    ↓
在本 Species 内按 Share 路由 FishGroup
```
因此 Cold / SummerStress 优先使用连续 Share：
```plain text
ColdSlowShare = curve(@ColdSlowShareProfile, ColdSeverity)
SummerStressShare = curve(@SummerStressShareProfile, OxythermalCompression)
```
而不是：
```plain text
温度 < 6.0 → COLD = ON
温度 > 6.0 → COLD = OFF
```
只要 `ColdSeverity` / `OxythermalCompression` 本身来自稳定的水体级事实或平滑窗口，Share 会自然连续变化，R0 **不额外购买 Group-level hysteresis state**。
只有以后出现：
- 上游输入本身在阈值附近高频抖动；
- FishGroup 身份需要跨 Opportunity 持久保存；
- 进组 / 出组本身存在现实路径依赖；
才重新准入 hysteresis。
### 12.2 Share 的最小数学语义
当前 Candidate：`GroupShare` 是**在已经抽到该 Species 的前提下，各互斥行为程序的相对组成比例**，不是最终中鱼概率、不是空间权重、也不是 Response。
```plain text
0 <= SpecialGroupShare <= 1

SpecialShareTotal = Σ SpecialGroupShare

要求：
    SpecialShareTotal <= 1

NormalShare = 1 - SpecialShareTotal
```
若 `SpecialShareTotal > 1`：
```plain text
Validation Error
```
不静默归一化，因为这通常说明多个行为组的职责 / 条件发生了重叠。
对 Bass 当前候选，Cold-Slow 与 SummerStress 应天然由不同环境状态约束；Guarding 主要处于繁殖窗口。若未来 Forage-Chase 与 SummerStress 等真实重叠，则优先把**互斥条件写清楚**或重新定义 Group 边界，不通过可编辑优先级顺序解决。
### 12.3 `@GuardingShare` 因而是什么
它就是配置引用，可以是：
```plain text
固定 Scalar
或
一个随 GuardingAvailability / lifecycle fact 变化的 Profile
```
Router 只消费这个值。
本页暂不把它写死为具体百分比。
## 13. Cold-Slow 与 SummerStress：优先复用同一种 Response Topology
两者虽然策略故事不同，但当前看到的 Runtime 拓扑可能相同：
```plain text
Channel A｜普通 Feeding / Presentation Match
    评价食物匹配
    评价当前 Presentation
    评价持续追逐要求

Channel B｜Short Reaction
    评价高显著度 Cue
    评价 proximity
    评价短程动作成本

按模板固定规则合并
返回 Response
```
Working Candidate：
```plain text
FinalResponse = MAX(FeedingChannel, ReactionChannel)
```
`MAX` 当前只是最小候选，不自动冻结；它的优点是“哪条动机路径更能解释这次咬口，就采用哪条”，避免把 Feeding + Reaction 相加后虚构更大的总概率。
### Cold-Slow 的参数化
```plain text
Feeding Channel：
    高 Pursuit Demand 强抑制
    低速 / 停顿 / 贴近相对有利

Reaction Channel：
    短时高 Salience 可以成立
    但不能要求长距离持续追逐
```
### SummerStress 的参数化
```plain text
Feeding Channel：
    基础 readiness / normal feeding 较弱

Reaction Channel：
    flash / vibration / acceleration / deflection 等高 Salience
    + near proximity
    + low sustained pursuit cost
    → 相对更强
```
如果后续证明确实如此，则：
> Cold-Slow 与 SummerStress **不需要因为策略故事名字不同而购买两个 Response LogicTemplate**；可以共用同一“Feeding + Reaction 并行通道”模板，只绑定不同 Profile / RuleSet。
这正是本单鱼深挖后续要回投 Representation Stress Test 的一个核心样本。
## 14. Open-water Forage Chase｜新证据后的判断
现有资料已经足以把它从“随口假设”提高为**强 Breaker**，但还不足以直接 Promote 为生产 FishGroup。
有研究观察到：在特定水库中，中等体型大口黑鲈会聚集在开放水域取食 threadfin shad，而更大的个体更多作为独居鱼使用水下结构进行伏击；另有遥测研究在开放水猎物占主导的采石坑湖中观察到 Bass 大量使用离岸 / 开放水域。
Evidence Reference：
- [Food and habitat use by different sizes of largemouth bass in Alamo Lake, Arizona](https://experts.arizona.edu/en/publications/food-and-habitat-use-by-different-sizes-of-largemouth-bass-microp/)
- [Movement and Habitat Selection of Largemouth Bass in a Florida Steep-sided Quarry Lake](https://seafwa.org/journal/2005/movement-and-habitat-selection-largemouth-bass-florida-steep-sided-quarry-lake)
这说明需要认真验证一个新的四执行面故事：
```plain text
Group Routing：
    Pelagic forage availability 高
    + 当前水体支持 open-water forage
    → 分配 ForageChase Share

Bake：
    由 structure-anchor
    转为更强的 prey-field / open-water coupling

Response：
    moving / search presentation 相对占优

Quality：
    ForageChase Group 的基础品质分布或 modifier
    可能偏向特定体型段
```
这里特别有价值，因为它不是单纯“又多一个 Group”，而是会直接检验我们当前坚持的顺序：
```plain text
Group → Quality Selection
```
如果用 Group-specific Quality Distribution / Modifier 就能表达体型依赖，则不需要把 Quality 提前到 Group Routing 前面。
## 11. 冻结：Cold-Slow 与 SummerStress 的 Group / Bake / Response 关系
当前先冻结下面三条：
```plain text
Cold-Slow
与
Summer Oxythermal Stress
```
### 11.1 Group Routing 必须分开
两者进入 FishGroup 的条件完全不同：
```plain text
Cold-Slow Eligibility
    = 水体级 Severe Cold / 普通暖水 habitat 基本消失 / winter refuge 成为主要可用空间

SummerStress Eligibility
    = 上层持续过热 + 深层低氧 / 不可用 + 可用水层被压缩
```
因此它们不是一个 `StressGroup` 的两个参数档位。
### 11.2 Bake 必须分开
**Cold-Slow Bake** 的核心问题：
```plain text
在整体已经很冷的水体里：
    哪里相对更暖？
    哪里更稳定？
    哪里流速 / 能耗更低？
    哪里适合 winter refuge？
```
它是“相对温暖 + 低能耗 refuge”逻辑。
**SummerStress Bake** 的核心问题：
```plain text
上层太热
↓
向下潜可以降温
↓
但继续向下会碰到低氧 / 可视性 / prey / cover 等约束
↓
寻找多约束共同决定的可用带 / refuge
```
它是“热—氧夹压下的多约束权衡”逻辑。
因此即使两者最后 Response 共用一个模板，Bake LogicTemplate 也不应因为都叫 Stress 就合并。
### 11.3 Response 暂时共用固定双 Channel 模板
当前 Working Candidate：
```plain text
评价 Feeding Channel
评价 Reaction Channel

FinalResponse = MAX(FeedingResponse, ReactionResponse)
```
两者使用不同 Profile / 参数：
**Cold-Slow：**
```plain text
Feeding：
    高持续追逐要求 → 强抑制
    慢速 / 停顿 / 贴近 → 相对有利

Reaction：
    短时高显著度刺激仍可触发
    但不得要求长时间持续追逐
```
**SummerStress：**
```plain text
Feeding：
    普通摄食准备度下降

Reaction：
    高显著度 Cue
    + 近距离
    + 低持续追逐成本
    → 相对增强
```
这意味着：
> **不同 FishGroup 不等于不同 Response LogicTemplate。**
>
> 如果 Runtime 拓扑相同，只是 Profile / 参数不同，就应该复用模板。
`MAX` 目前仍是 Working Candidate；若后续真实 Case 证明两 Channel 需要竞争、累加或顺序依赖，再重新打开。
## 12. Open-water Forage Chase｜正式 FishGroup Candidate
### 12.1 玩家策略故事
玩家不再主要问：
```plain text
哪块草？
哪个木头？
哪条崖壁？
```
而是问：
```plain text
今天 pelagic forage / shad 在哪里？
它们处在哪个水层？
Bass 是否正在跟随这批 prey 在开放水巡猎？
我应该用什么搜索型 / moving presentation 穿过这批 prey？
```
这个故事与普通 cover-oriented Bass 有明显不同。
现实依据也支持这种差异并非纯想象：一项 Arizona reservoir 研究发现，中等体型的大口黑鲈会成群出现在开放水并取食 threadfin shad，而较大的个体更多独居在沉水结构附近伏击；另一个 Florida quarry telemetry 研究也观察到 Bass 在夏秋冬偏好 limnetic / open-water 区域，并推测这与开放水 prey 有关。
### 12.2 Group Routing｜什么时候进入 Forage-Chase
不要直接用“秋季”或“今天晴天”作为硬开关。优先读取 prey / 水体级状态：
```plain text
读取 PelagicForageState
读取 OpenWaterAvailability
读取 当前水体中活跃 forage school 的强度 / 稳定性

如果：
    存在稳定的 pelagic forage school
    并且 open-water habitat 对 Bass 可用
    并且 forage school 强度达到可形成持续巡猎的阈值

则：
    提高 ForageChase Group Share
```
季节、时段、天气可以影响 `PelagicForageState`，但不应重复成为第二套独立理由。
当前推荐：
```plain text
ForageChaseShare
    = profile(PelagicForageStrength, WaterbodyContext)
```
而不是固定：
```plain text
秋季 = 40%
```
### 12.3 Bake｜跟 prey field，而不是跟结构点
普通 cover-oriented Bass 常见空间逻辑：
```plain text
Structure / Cover
→ Layer
→ Temperature / Light / Time 等
→ Spatial Weight
```
Forage-Chase 应明显不同：
```plain text
读取 当前目标区域的 pelagic prey intensity
读取 prey school 所在水层
读取 prey school 的局部集中度 / 可持续性
读取 当前目标点的温度 / 溶氧可行性
读取 OpenWater / Structure Context

如果 prey intensity 低于最低阈值：
    当前目标空间权重 = 很低 / 0

否则：
    计算 prey-coupling fit
    计算 vertical alignment fit
    计算 thermal / oxygen feasibility

    对开放水不额外惩罚
    对“必须贴结构”不再给予普通模式的强偏好

    合并为 Forage-Chase Spatial Weight
```
关键是：
> **结构从主锚点退居环境 Context，prey field 成为主锚点。**
这也是它值得独立 FishGroup / Bake Program 的核心理由。
### 12.4 Response｜奖励“像正在逃跑 / 移动的 forage”
Forage-Chase 的主要 Response 不应该是 SummerStress 那种“非摄食 reaction”为主，而是**主动追食型 Feeding Response**。
候选输入：
```plain text
ActiveForageSignature
PresentationForageMatch
PresentationSpeed
PresentationDirection / Trajectory
VerticalAlignment
Erratic / Escape-like Motion
SearchCoverage / SustainedMovement
CueFamiliarity
```
中文逻辑候选：
```plain text
读取 当前 FishGroup 的 ActiveForageSignature
读取 当前玩家 Presentation

评价 Forage Match：
    饵尺寸 / 轮廓 / 颜色 / 振动等
    是否像当前主要 forage

评价 Movement Match：
    当前速度是否处于可追逐范围
    是否持续移动
    是否表现出逃逸 / 转向 / erratic 特征

评价 Vertical Alignment：
    Presentation 是否经过当前 prey school / Bass 常用追食水层

如果：
    Forage Match 高
    并且 Movement Match 高
    并且 Vertical Alignment 合适

则：
    Feeding Response 提高

否则：
    使用该 Group 的默认较低 Response
```
这里不需要先购买一个新的 `Reaction Channel`。当前故事本身就是 Feeding，只是 Feeding 的匹配逻辑与 cover-oriented normal feeding 不同。
### 12.5 不重复结算 prey
同一个 prey fact 在四 Surface 中的职责分开：
```plain text
Group Routing：
    是否存在足以形成 Forage-Chase 行为组的 pelagic forage state

Bake：
    这个 Group 的鱼具体跟着哪片 prey / 哪个水层分布

Response：
    玩家 Presentation 是否像“当前正在被追的 forage”

Quality：
    只有真实证据支持尺寸组成差异时才调整
```
禁止：
```plain text
因为 prey 多，Group Share +50%
Bake 又因为 prey 多 ×2
Response 又无条件因为 prey 多 ×2
```
Response 消费的应该主要是 `Presentation ↔ ActiveForageSignature` 的关系，而不是再次把 prey density 当全局加成。
### 12.6 Quality｜Group-specific 基础品质分布
开放水追逐行为与体型可能存在相关性。一项具体水库研究中，中等体型 Bass 更常成群在开放水追 threadfin shad，而大个体更常在结构附近伏击。
但这个结论具有 site-specific 特征，不能硬编码成全球规则：
```plain text
Forage-Chase = 中鱼
Large Bass = 永远不 chase
```
当前最低复杂度方案：
```plain text
抽中 Forage-Chase Group
→ 读取 @ForageChaseBaseQualityProfile
→ 再叠加钩 / 饵 / 当前环境的 Quality Modifier
→ 归一化
→ 抽具体品质
```
因此：
- 不需要把 Quality 提前到 Group Routing 前；
- 不需要让 Group Router 按质量逐档运行；
- 不需要增加 `If size == medium → ForageChase` 的逆向依赖。
这同时保住主链：
```plain text
Group Routing
→ Bake / Response
→ Quality Selection
```
## 13. Bass 当前 FishGroup Snapshot｜第一次可投影版本
<table fit-page-width="true" header-row="true">
<tr>
<td>FishGroup</td>
<td>Routing 核心</td>
<td>Bake 核心</td>
<td>Response 核心</td>
<td>Quality</td>
<td>当前状态</td>
</tr>
<tr>
<td>Normal Feeding</td>
<td>默认剩余</td>
<td>普通 structure / layer / environment</td>
<td>普通 Feeding</td>
<td>@NormalQualityProfile</td>
<td>KEEP</td>
</tr>
<tr>
<td>Guarding</td>
<td>繁殖窗口 + 巢区条件</td>
<td>nest / spawning structure</td>
<td>Defense-only</td>
<td>暂沿用 / 待必要性</td>
<td>KEEP</td>
</tr>
<tr>
<td>Cold-Slow</td>
<td>水体级 Severe Cold</td>
<td>相对暖、稳定、低能耗 refuge</td>
<td>Feeding + Reaction 双 Channel；高 sustained pursuit 成本受抑制</td>
<td>默认不单独改</td>
<td>STRONG CANDIDATE</td>
</tr>
<tr>
<td>Summer Oxythermal Stress</td>
<td>上层过热 + 深层低氧 + habitat compression</td>
<td>热—氧夹压下多约束 refuge</td>
<td>Feeding + Reaction 双 Channel；近距离高显著度 reaction 相对重要</td>
<td>默认不单独改</td>
<td>STRONG CANDIDATE</td>
</tr>
<tr>
<td>Open-water Forage Chase</td>
<td>稳定 pelagic forage school + open-water availability</td>
<td>prey-field / water-column coupled distribution</td>
<td>主动追食型 Feeding；forage / movement / layer match</td>
<td>@ForageChaseBaseQualityProfile</td>
<td>FORMAL CANDIDATE</td>
</tr>
</table>
High Angling Pressure 继续作为 Response Overlay，不升 Group；Post-spawn Recovery 继续作为连续状态 / Profile 修正，不升 Group。
## 14. 下一次回投 Representation 页时要比较什么
当本 Snapshot 暂时不再变化时，把 4 个 Special Group 回投到 Authoring Stress Test，逐个画：
```plain text
Group Routing Config
vs
Group Routing 中文脚本

Bake Config / LogicTemplate
vs
Bake 中文脚本

Response Config / LogicTemplate
vs
Response 中文脚本

Quality Config
vs
Quality 中文脚本
```
尤其观察：
1. 5 个 Group 的 Routing 条件是否仍适合 Condition Atom + RuleSet；
2. Cold-Slow / SummerStress / Forage-Chase 是否逼出 3 个不同 Bake LogicTemplate；
3. Cold-Slow / SummerStress 是否确实可共享一个 Response LogicTemplate；
4. Forage-Chase 的 Response 是否只是新的 Profile / Rule，还是需要新 Template；
5. Group-specific Quality Profile 是否能避免打破 `Group → Quality` 主顺序。
## 11. 五个 FishGroup｜Working Snapshot R0
当前先固定五个大口黑鲈行为组作为后续 Representation 的真实输入样本：
```plain text
1. Normal Feeding
2. Guarding
3. Cold-Slow
4. Summer Oxythermal Stress
5. Open-water Forage Chase
```
这五个 Group 的含义是：在当前世界 / 环境条件下，Bass 进入哪一种**稳定行为程序**。它们不是天气状态标签，也不是所有鱼侧动态参数的容器。
### 11.1 Cold-Slow 与 SummerStress 的关系
当前冻结：
```plain text
Cold-Slow
    Group Routing：独立条件
    Bake：独立逻辑
    Response：暂时允许复用共享模板 + 独立 Profile

SummerStress
    Group Routing：独立条件
    Bake：独立逻辑
    Response：暂时允许复用共享模板 + 独立 Profile
```
因此：
> 不同 FishGroup 不要求四个执行面都使用不同 LogicTemplate。
当前 Response Candidate 仍是：
```plain text
评价 Feeding Channel
评价 Reaction Channel
返回 MAX(Feeding, Reaction)
```
Cold-Slow 与 SummerStress 使用不同 Feeding / Reaction Profile。只有后续证明其中一个 Group 需要不同的执行顺序、不同 Channel 拓扑或不同固定汇总语义，才拆 Response LogicTemplate。
## 12. Open-water Forage Chase｜正式 FishGroup Candidate
### 12.1 上游边界：不在本任务里计算“饵鱼群在哪里”
当前直接假定世界 / 环境系统已经提供语义事实：
```plain text
水体级：
    PelagicForageState
    OpenWaterForageAvailability

空间目标级：
    ForageSchoolIntensity
    ForageSchoolDepth / VerticalBand
    DistanceToForageSchool / ForageProximity
```
这些字段名称仍是 Working Placeholder；本页只要求语义存在。
当前不研究：
```plain text
饵鱼如何生成
饵鱼群如何移动
饵鱼群中心点如何计算
schooling AI
prey simulation
```
原因：这些是上游世界 /生态模拟问题，不是当前 FishGroup Authoring Representation 的主线。
### 12.2 玩家策略故事
Normal Feeding 的玩家主要寻找：
```plain text
草区
木头
石头
drop-off
阴影
其它稳定结构 / habitat
```
Forage Chase 的玩家主要寻找：
```plain text
当前饵鱼群在哪里？
饵鱼群处在哪个水层？
Bass 是否跟随它们进入开放水？
如何把 moving / search bait 送进或穿过有效 forage zone？
```
### 12.3 Group Routing
Group Routing 不直接看当前某一个空间点的 forage intensity，而先读取**水体 / 大区级 forage state**，判断这种觅食程序是否在当前时段成立。
```plain text
读取 PelagicForageState
读取 OpenWaterForageAvailability

如果：
    当前存在稳定、足够强的开放水饵鱼群
    并且 Bass 可达开放水环境成立

则：
    读取 @ForageChaseShare / @ForageChaseShareProfile
    分配 ForageChase Group Share
```
季节、天气、时间可以影响 PelagicForageState，但不直接写成：
```plain text
秋季 = ForageChase
```
真正的行为原因是 forage field 已经进入足以改变 Bass 空间使用和觅食方式的状态。
### 12.4 Bake｜与 Normal Feeding 明确不同
Normal Feeding 的主要空间锚点：
```plain text
Structure / Cover / Layer / Temperature / Time / FoodField
```
Forage Chase 的主要空间锚点改成：
```plain text
Pelagic Forage Field
```
当前逻辑 Candidate：
```plain text
读取 当前空间目标的 ForageSchoolIntensity
读取 当前空间目标与饵鱼群水层的 VerticalAlignment
读取 当前空间目标温度
读取 当前空间目标溶氧
读取 必要的 OpenWater / Structure Context

如果 ForageSchoolIntensity 低于最低成立阈值：
    返回极低空间分布权重

评价 饵鱼群强度适配
评价 水层对齐
评价 温度可行性
评价 溶氧可行性

按 Forage-Chase 固定 Bake 规则合并
返回 SpatialDistributionWeight
```
这里的核心变化不是“给普通 Bake 加一个 forage bonus”，而是：
> **空间主锚点从 Structure / stable habitat 转成当前 Pelagic Forage Field。**
Structure 可以继续作为 Context / Secondary Factor，但不能继续假装它仍然是主要因果。
### 12.5 Response｜主动摄食，不等于 SummerStress Reaction
Forage Chase 当前仍是 Feeding Program，而不是 stress reaction。
```plain text
读取 当前 Presentation 与 forage school 的关系
读取 拟饵尺寸 / silhouette / movement
读取 当前速度与轨迹
读取 逃逸 / erratic motion
读取 当前水层是否与 forage band 对齐
读取 CueFamiliarity / AnglingPressure Overlay

评价 Forage-Chase Feeding Match
返回 Feeding Response
```
它可能复用通用 Feeding Evaluator，但使用单独的 `@ForageChaseFeedingProfile` / RuleSet。
暂时没有证据要求它购买独立 Reaction Channel 或新的 Response 控制流。
### 12.6 Quality｜Group-specific Base Quality Distribution
开放水追食行为与体型可能存在系统性关系。为了不破坏当前主链：
```plain text
Group Routing
→ 抽中 FishGroup
→ Quality Selection
```
当前采用：
```plain text
如果 FishGroup == ForageChase：
    基础品质分布 = @ForageChaseBaseQualityProfile
否则：
    基础品质分布 = 对应 Group / Species BaseQualityProfile

再叠加钩 / 饵 / 时间 / 环境的并列 Quality Modifier
统一归一化
抽具体品质
```
这允许表达：
```plain text
幼小个体：低 ForageChase 占比 / 低基础权重
中等及以上个体：更常进入开放水追食群
```
而不需要把 Quality Selection 整体提前到 Group Routing 前面。
## 13. 冷锋 / Front Passage｜动态参数与空间 Overlay，不升 FishGroup
### 13.1 现实 / 垂钓侧 Working 结论
冷锋前后确实可能同时改变：
```plain text
摄食积极性
追逐意愿
贴 cover 程度
局部深度 / 第一处 depth break 的利用
Presentation 速度偏好
```
尤其 post-front 条件下，Bass 经常更贴 cover、减少追逐、局部下沉或退到邻近更深位置；快速降温也会显著降低摄食。
但这些变化当前仍可以解释为：
```plain text
同一个 FishGroup
+ 不同的动态环境输入
→ Bake 局部偏置改变
→ FeedingReadiness / PursuitTolerance / Response Profile 输入改变
```
而不是：
```plain text
进入 ColdFront FishGroup
```
### 13.2 为什么不升第六个 Group
FishGroup 当前代表稳定行为程序，例如：
```plain text
守巢防御
严寒越冬迟缓
夏季热氧夹压 refuge
开放水追 forage
```
Cold Front 更像短中期环境事件，会在这些程序内部产生状态变化。
例如同样是 ForageChase：
```plain text
锋前：
    ForageChase 仍成立
    FeedingReadiness 上升
    moving bait 接受度更高

锋后：
    ForageChase 可能减弱
    局部更贴 cover / depth break
    持续追逐接受度下降
```
这不需要额外制造：
```plain text
ForageChase_PostFront
Normal_PostFront
Guarding_PostFront
...
```
### 13.3 当前动态输入 Candidate
先只保留语义，不急着冻结字段：
```plain text
FrontPhase / WeatherTransitionState
RecentTemperatureDrop
FeedingReadiness
PursuitTolerance
CoverTightnessBias
DepthShiftBias
```
这些输入可以被 Bake / Response 消费，但**不改变 FishGroup 身份本身**。
### 13.4 防重复结算
冷锋事实可以影响多个执行面，但每个面承担不同语义：
```plain text
Group Routing：
    只有当 forage / spawn / severe thermal state 本身因此改变时，间接改变 Group Share

Bake：
    当前 Group 内空间更贴 cover / 更深 / 更靠 refuge

Response：
    FeedingReadiness / pursuit tolerance / presentation acceptance 改变

Quality：
    只有有独立证据证明体型相对可钓性改变时才进入
```
禁止在每个执行面都重复乘一个 `ColdFrontPenalty`。
## 14. 下一步｜回投 Representation 的冻结输入
下一轮 Representation 不再自己发明 Bass 逻辑，只读取本页这五个 Group：
```plain text
Normal Feeding
Guarding
Cold-Slow
Summer Oxythermal Stress
Open-water Forage Chase
```
重点验证：
```plain text
A. 5 Group 的 Group Routing：配置 vs 中文逻辑
B. 5 Group 的 Bake：到底需要几个真正不同的 Bake LogicTemplate
C. Response：Guard 单独；Cold / Summer 是否共享；Forage 是否只换 Profile
D. Quality：Group-specific BaseQualityProfile + parallel Modifiers 是否足够
```
冷锋 / 高钓压等只作为 Overlay 压力测试，不增加 Group 数量。
## 14. Cold Front Spatial Overlay｜不升 Group，但需要动态空间逻辑片段
### 14.1 结论
冷锋 / 锋后状态当前**不新增 FishGroup，也不新增整套 Bake LogicTemplate**。
但它确实可能改变空间分布，因此不能只用 `FeedingReadiness` / `Activity` 之类单一动态数值解释。当前 Working 决定：
```plain text
当前 FishGroup 的原 Bake 主逻辑
+
ColdFront Spatial Overlay Slot
→ 最终 SpatialDistributionWeight
```
也就是说：
- `Normal / Guarding / Cold-Slow / SummerStress / ForageChase` 身份不因普通冷锋自动切换；
- 当前 Group 原有的 Bake 程序仍负责“这个行为组通常在哪里”；
- ColdFront Overlay 只负责“锋后在原行为框架内，空间分布往哪类 refuge 偏”。
### 14.2 现实策略故事压缩
锋后常见的两个空间变化候选：
```plain text
A. Cover Refuge
→ 更贴草、木头、码头、石头、mat 等 cover

B. Depth Retreat
→ 从原浅区 / feeding area 后退到邻近第一处明显深度变化、drop、channel edge 或较深结构
```
这两者不是要求同时成立的 AND 条件。在不同钓场中，鱼可能主要使用其中一种。因此当前不采用：
```plain text
CoverFit × DepthBreakFit
```
作为默认逻辑，因为这会错误要求“既贴 Cover 又必须靠 Depth Break”。
### 14.3 输入边界
本页不负责计算冷锋本身，也不负责从原始地图几何里求“第一处 depth break”。先假定上游 Resolver / DEF 已经提供可查询语义：
```plain text
WeatherTransitionState / PostFrontSeverity

Target.CoverProximity / CoverRefugeScore
Target.AdjacentDeepAccess / DepthBreakProximity
```
字段名只是 Working 示意，不构成正式 Schema。
当前 Bake DSL 已允许读取 `context.weather.*`、`target.depth_layer`、`target.structure_type` 等环境与空间目标事实；如果后续缺少 `CoverProximity / AdjacentDeepAccess` 这种关系型目标事实，应补 Spatial Target / Resolver 输入，而不是因此创建 ColdFront FishGroup。
### 14.4 Working 算法
推荐先把锋后空间迁移压成两个固定 Channel：
```plain text
读取 当前 Group 原始 Bake 结果
得到 BaseSpatialFit

读取 PostFrontSeverity

如果 PostFrontSeverity 很低：
    返回 BaseSpatialFit

评价 Cover Refuge：
    读取 Target.CoverProximity / CoverRefugeScore
    查询 @PostFrontCoverRefugeProfile
    得到 CoverRefugeFit

评价 Depth Retreat：
    读取 Target.AdjacentDeepAccess / DepthBreakProximity
    查询 @PostFrontDepthRetreatProfile
    得到 DepthRetreatFit

PostFrontRefugeFit = MAX(
    CoverRefugeFit,
    DepthRetreatFit
)

FinalSpatialFit = BLEND(
    BaseSpatialFit,
    PostFrontRefugeFit,
    PostFrontSeverity
)

返回 FinalSpatialFit
```
`MAX` 和 `BLEND` 当前都是 Working Candidate：
- `MAX` 表示两种 refuge 是替代通路；
- `BLEND` 表示冷锋越强，空间分布越从常态转向锋后 refuge，而不是凭空把鱼种总量再扣一次。
如果后续真实案例证明“某些 Group 只允许其中一个 Channel”或“Cover + Deep Access 需要协同而非替代”，再升级组合规则；当前不预购通用组合 DSL。
### 14.5 为什么这不是新 FishGroup
判断标准：
```plain text
冷锋前：Normal Bass 仍然在普通觅食
冷锋后：Normal Bass 仍然在普通觅食
```
变化的是：
```plain text
空间位置更收缩 / 更贴 refuge
FeedingReadiness 下降
持续追逐容忍下降
```
但没有稳定证据要求它切换成一套新的行为身份、饵类别或完整 Response topology。
因此当前归类：
```plain text
FishGroup Identity：不变
Bake：增加动态 Spatial Overlay
Response：消费动态 Readiness / PursuitTolerance 等输入
Quality：默认不受影响
```
### 14.6 与五 Group 的关系
ColdFront Overlay 是可复用的动态空间层，不是第六个 Group。
不同 Group 可以决定是否启用以及使用哪套 Profile：
```plain text
Normal Feeding：通常启用
Forage Chase：可启用，但仍保持 ForageChase identity
Guarding：若 nest fidelity 应压过天气退避，可弱化 / 关闭该 Overlay
Cold-Slow：本身已是极端严寒 Program，普通冷锋 Overlay 默认弱化或不叠加
SummerStress：是否叠加需防止与已有 refuge trade-off 重复计算
```
因此需要一个 `ColdFrontSpatialOverlayRef / Enable` 之类的固定 Slot Candidate，但**不允许该 Slot 改变 Runtime 顺序 / Group identity**。
</content>
</page>
