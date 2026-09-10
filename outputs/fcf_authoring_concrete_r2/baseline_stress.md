Here is the result of "fetch" for the Page with URL https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3 as of 2026-09-09T10:26:32.595Z:
<page url="https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3">
<ancestor-path>
<parent-page url="https://app.notion.com/p/3cfa4137d23681cca208eaa97dfe7767" title="中鱼机制 0.3.4｜逻辑框架升级（中间对齐骨架）"/>
<ancestor-2-page url="https://app.notion.com/p/3cda4137d23681508740ceff789abd41" title="FCF Design Branch｜Simplified Production V0｜Working Main"/>
<ancestor-3-page url="https://app.notion.com/p/3cda4137d236819dbbc0d371ee6084dd" title="Fish-Centric Conditional Funnel｜Design Branch Index"/>
<ancestor-4-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"title":"4 Logic Surface Authoring Stress Test R1｜分群 / 烘焙 / 响应 / 品质选择"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
**Status：WORKING / FAST DESIGN LANE / NOT AUTHORITY / NOT PROMOTED**
<callout icon="⚡" color="yellow_bg">
	这页不再只比较 Response。当前要验证的是一条完整的中鱼 Authoring 主链：**分群 → 烘焙 / 预计算 → Response → 品质选择**。目标是把每一块真正的配置长相与脚本长相都画出来，再判断哪些地方配置足够、哪些地方值得使用 DSL。
</callout>
<callout icon="🎣" color="blue_bg">
	**Bass 内容的上游设计源：** <mention-page url="https://app.notion.com/p/3d6a4137d23681e2af96e873eef9411a"/>。Bass 的行为组、生态理由、Group 准入与因果边界在单鱼深挖页闭合；本页只读取某个 Working Snapshot，投影成 Config / RuleSet / 中文 DSL，用于比较 Authoring 成本。不要在两页分别维护两套 Bass 机制真相。
</callout>
## 0. 先看例子｜不要先读规则
### 例 1｜护巢鱼：先分到 Guarding Group，再只算防御 Response
这是之前版本最容易漏掉的一段。Guard 并不是一上来就执行防御 Response；前面先要有**分群逻辑**。
#### A. 如果用配置表达分群
**条件原子：**
<table fit-page-width="true" header-row="true">
<tr>
<td>条件组</td>
<td>条件</td>
<td>事实 / 计算项</td>
<td>参数1</td>
<td>比较符</td>
<td>比较值1</td>
<td>比较值2</td>
</tr>
<tr>
<td>G1</td>
<td>C1</td>
<td>当前日期</td>
<td>—</td>
<td>BETWEEN</td>
<td>繁殖窗口起点</td>
<td>繁殖窗口终点</td>
</tr>
<tr>
<td>G1</td>
<td>C2</td>
<td>连续均温</td>
<td>5天</td>
<td>&gt;=</td>
<td>护巢温度阈值</td>
<td>—</td>
</tr>
<tr>
<td>G1</td>
<td>C3</td>
<td>场内结构集合</td>
<td>—</td>
<td>CONTAINS_ANY</td>
<td>适合筑巢结构</td>
<td>—</td>
</tr>
</table>
**条件组合：**
<table fit-page-width="true" header-row="true">
<tr>
<td>规则集</td>
<td>组合方式</td>
<td>显示顺序</td>
<td>引用类型</td>
<td>引用</td>
</tr>
<tr>
<td>BestGuardian</td>
<td>AND</td>
<td>1</td>
<td>Condition</td>
<td>G1.C1</td>
</tr>
<tr>
<td>BestGuardian</td>
<td>AND</td>
<td>2</td>
<td>Condition</td>
<td>G1.C2</td>
</tr>
<tr>
<td>BestGuardian</td>
<td>AND</td>
<td>3</td>
<td>Condition</td>
<td>G1.C3</td>
</tr>
</table>
**分群结果：**
<table fit-page-width="true" header-row="true">
<tr>
<td>分群规则</td>
<td>命中条件</td>
<td>目标 Group</td>
<td>权重处理</td>
<td>权重参数</td>
</tr>
<tr>
<td>Bass_Guard_Route</td>
<td>@BestGuardian</td>
<td>Guarding</td>
<td>Species 内行为份额</td>
<td>@GuardingShare</td>
</tr>
<tr>
<td>Bass_Default</td>
<td>默认</td>
<td>NormalFeeding</td>
<td>承接剩余份额</td>
<td>1 - SpecialShareTotal</td>
</tr>
</table>
#### B. 同样逻辑如果用中文脚本表达
```plain text
读取 当前日期
读取 最近 5 天平均水温
读取 当前钓场结构集合

如果：
    当前日期处于繁殖窗口
    并且 最近 5 天平均水温 >= 护巢温度阈值
    并且 场内存在适合筑巢的结构

则：
    GuardingShare = @GuardingShare
    NormalFeedingShare = 1 - GuardingShare

否则：
    GuardingShare = 0
    NormalFeedingShare = 1

这里的 Share 是“已经抽到 Bass 后，各互斥行为程序的组成比例”；
不是最终中鱼概率，也不是空间分布权重。
```
#### C. Guarding Group 的 Response
当前 Simplified V0 的明确简化：**Guarding Group 只评价防御 Response，不再评价普通 Feeding。**
配置：
<table fit-page-width="true" header-row="true">
<tr>
<td>Group</td>
<td>响应模板</td>
<td>条件 / Profile</td>
<td>命中结果</td>
<td>未命中</td>
</tr>
<tr>
<td>Guarding</td>
<td>顺序响应规则</td>
<td>@GuardThreatRule</td>
<td>返回防御 Response</td>
<td>返回低 / 无响应</td>
</tr>
</table>
中文逻辑：
```plain text
如果 当前 FishGroup == Guarding：
    读取 当前姿态与护巢区域的关系
    评价 Defense Response
    返回 Defense Response

    不再评价普通 Feeding
```
**这里必须对工程 / 上层明确：**这是主动复杂度取舍，不是遗漏。现实上护巢鱼仍可能摄食；当前版本只保留最强、最有策略差异的防御反应，省掉 Defense / Feeding arbitration。
---
### 例 2｜普通鱼的烘焙：决定“哪里鱼多，哪里鱼少”
例如某种鱼的空间逻辑需要依次看水层、结构、温度。
#### A. 配置方式
<table fit-page-width="true" header-row="true">
<tr>
<td>配置项</td>
<td>值</td>
</tr>
<tr>
<td>烘焙逻辑模板</td>
<td>水层 → 结构 → 温度</td>
</tr>
<tr>
<td>水层 Profile</td>
<td>@LayerProfile</td>
</tr>
<tr>
<td>结构 Profile</td>
<td>@StructureProfile</td>
</tr>
<tr>
<td>温度 Profile</td>
<td>@TemperatureProfile</td>
</tr>
<tr>
<td>温度槽位开关</td>
<td>ON</td>
</tr>
</table>
#### B. 中文脚本
```plain text
读取 当前空间目标

应用 水层偏好 @LayerProfile
应用 结构偏好 @StructureProfile
应用 温度偏好 @TemperatureProfile

合并结果
返回 空间分布权重
```
如果另一种鱼真正需要：
```plain text
结构 → 温度 → 水层
```
而顺序会影响运行结果，则它是另一个烘焙 LogicTemplate；不能用 Switch 偷偷改顺序。
当前 Bake 正式输出仍只讨论 `SpatialDistributionWeight`。活性、进食准备度、追逐容忍度等只作为**鱼侧动态派生事实候选**；它们是否预计算、由谁计算、何时刷新需要另行闭合，不能在本页默认归入 Bake 输出。
---
### 例 3｜罗非鱼：同一个 Response evaluator 内保留两条摄食 Channel
当前决定：**不购买 Selector。**
#### A. 配置方式
<table fit-page-width="true" header-row="true">
<tr>
<td>响应模板</td>
<td>Channel</td>
<td>Profile</td>
<td>汇总规则</td>
</tr>
<tr>
<td>双通道摄食评价</td>
<td>刮食</td>
<td>@GrazingProfile</td>
<td>固定汇总</td>
</tr>
<tr>
<td>双通道摄食评价</td>
<td>悬浮颗粒摄食</td>
<td>@SuspendedFeedingProfile</td>
<td>固定汇总</td>
</tr>
</table>
#### B. 中文脚本
```plain text
评价 刮食 Channel：
    使用 @GrazingProfile

评价 悬浮颗粒摄食 Channel：
    使用 @SuspendedFeedingProfile

按模板固定规则合并两个 Channel
返回 最终 Response
```
这里有两个 Profile，不等于必须先 `SELECT Profile`。只有未来发现两种摄食方式连后续执行顺序 / 拓扑都整包改变，才重新考虑 Selector。
---
### 例 4｜抽中 FishGroup 以后，再决定具体品质
这一块之前的 Stress Test 基本没画，是明显缺项。
例如先有一个基础品质分布：
```plain text
普通 50%
良好 30%
大型 15%
稀有 5%
```
当前玩家用了更大的钩、更大的饵，可能提高大个体的相对占比；某些时间 / 环境也可能让成年个体活跃度下降，从而让小鱼比例上升。
#### A. 配置方式
**条件：**
<table fit-page-width="true" header-row="true">
<tr>
<td>规则</td>
<td>事实 / 计算项</td>
<td>比较符</td>
<td>比较值</td>
</tr>
<tr>
<td>Q1</td>
<td>钩尺寸</td>
<td>&gt;=</td>
<td>大型钩阈值</td>
</tr>
<tr>
<td>Q2</td>
<td>饵尺寸</td>
<td>&gt;=</td>
<td>大型饵阈值</td>
</tr>
<tr>
<td>Q3</td>
<td>当前时段</td>
<td>IN</td>
<td>成年低活性时段</td>
</tr>
</table>
**品质调整结果：**
<table fit-page-width="true" header-row="true">
<tr>
<td>命中条件</td>
<td>调整对象</td>
<td>调整方式</td>
<td>参数</td>
</tr>
<tr>
<td>Q1 AND Q2</td>
<td>大型 / 稀有品质</td>
<td>上调相对权重</td>
<td>@BigGearBoost</td>
</tr>
<tr>
<td>Q3</td>
<td>成年高品质</td>
<td>下调相对权重</td>
<td>@AdultInactivePenalty</td>
</tr>
</table>
#### B. 中文脚本
```plain text
读取 当前 FishGroup 的基础品质分布

如果 钩尺寸 >= 大型钩阈值
并且 饵尺寸 >= 大型饵阈值：
    上调 大型 / 稀有品质的相对权重

如果 当前时段属于成年低活性时段：
    下调 成年高品质的相对权重

重新归一化品质权重
抽取具体品质
```
这就是第四个独立执行面：**Quality Selection / 品质选择**。
---
## 1. 整体上其实是四块逻辑，不是一块 DSL
当前更适合用下面这个主链理解：
```plain text
① 分群逻辑
Species / 当前环境 / 特殊事件
→ 把一种鱼的权重拆到若干 FishGroup

② 烘焙 / 预计算逻辑
FishGroup / Fish / 环境 / 空间目标
→ 空间分布权重
→ 必要时预计算活性、进食准备度等稳定事实

③ Response 逻辑
当前 Opportunity
+ 玩家饵 / 姿态 / 手法
+ 当前鱼 / FishGroup
+ 已有环境事实
→ Response / 适配系数

④ 品质选择逻辑
已经抽中某 Species / FishGroup
+ 钩 / 饵 / 时段 / 环境等条件
→ 调整各品质相对权重
→ 抽取具体品质
```
**FishGroup 分群不是恢复旧 ****`LifecycleCohort`****。** 这里的 FishGroup 只是行为 / 习性路由结果：在当前条件下，把鱼种的机会权重分给不同逻辑组。它不自动购买一整套生命周期 identity、守恒账本或 population ontology。
## 2. 所以真正要比较的不是“Config vs DSL 一次性选一个”
四个执行面可以分别选择最便宜、最好维护的 Authoring 形式：
<table fit-page-width="true" header-row="true">
<tr>
<td>执行面</td>
<td>配置侧最自然的表达</td>
<td>脚本侧最自然的表达</td>
<td>当前要观察的压力</td>
</tr>
<tr>
<td>分群</td>
<td>Condition Atom + RuleSet + Group Routing Result</td>
<td>if / else + 分配 Group 权重</td>
<td>条件嵌套、Group 组合、权重操作是否变复杂</td>
</tr>
<tr>
<td>烘焙</td>
<td>LogicTemplate + Profile / 参数 / Switch</td>
<td>顺序 DSL + Gate + Return</td>
<td>不同鱼真实 Runtime Order 是否很多</td>
</tr>
<tr>
<td>Response</td>
<td>RuleSet + Channel / Profile + Typed Result</td>
<td>条件 / Channel / Return 脚本</td>
<td>是否出现需要自由控制流的案例</td>
</tr>
<tr>
<td>品质选择</td>
<td>基础品质分布 + 条件调整表</td>
<td>条件 → 调整品质权重 → 抽取</td>
<td>调整规则是否频繁组合、是否需要顺序</td>
</tr>
</table>
因此最后很可能不是：
```plain text
整个系统全部用表
或
整个系统全部用 DSL
```
而是：
```plain text
不同执行面使用不同 Authoring Surface
→ 最终编译到统一 Canonical Representation
```
## 3. Work 返回的最新 Coverage 结果怎么解释
15 Case Work 已完成 Runtime Order / LogicTemplate 聚类。当前结果：
```plain text
L_confirmed = 2
    LT-R1｜顺序响应规则
    LT-R2｜Opportunity 范围内的摄食评价器

L_lower_bound = 3
    再加 LT-S1｜空间顺序因素模板

L_unresolved_cases = 4
    C01 / C02 / C05：具体空间 Runtime Order 未冻结
    C13：Playable lifecycle scope 未裁决
```
同时：
- C06 / C07：Guarding Group = Defense-only，关闭 Defense vs Feeding arbitration；
- C08：单 evaluator + 两个 Feeding Channel，不买 Selector；
- C09–C11：复用现有 Semantic Opportunity，Food Field 只是输入；
- C12：阶段差异通过分群 / FishGroup 路由进入不同逻辑，不在 Response 内购买 Stage Selector；
- C13：转为 Scope Resolution，不强行当 Representation Breaker。
**但这里的 ****`L=2 / 3`**** 只覆盖 Spatial + Response Representation。它不是整个生产逻辑的总模板数。**
后续应拆成：
```plain text
L_group     = 分群逻辑模板数
L_bake      = 烘焙逻辑模板数
L_response  = Response 逻辑模板数
L_quality   = 品质选择逻辑模板数
```
然后再比较四块加起来的总维护复杂度。
## 4. 6 个高区分 Case 的当前角色
<table fit-page-width="true" header-row="true">
<tr>
<td>Case</td>
<td>主要验证执行面</td>
<td>当前结论</td>
</tr>
<tr>
<td>C01 / C05</td>
<td>烘焙</td>
<td>空间顺序模板存在；具体顺序仍待冻结</td>
</tr>
<tr>
<td>C03</td>
<td>Response</td>
<td>普通条件 RuleSet 可以自然表达</td>
</tr>
<tr>
<td>C06</td>
<td>分群 + Response</td>
<td>必须先分 Guarding Group；Group 内 Defense-only</td>
</tr>
<tr>
<td>C08</td>
<td>Response</td>
<td>双 Feeding Channel；不需要 Selector</td>
</tr>
<tr>
<td>C09 / C11</td>
<td>Opportunity + Response</td>
<td>复用既有 Opportunity；Food Field 不产生第二套机会</td>
</tr>
<tr>
<td>C12</td>
<td>分群 + Response</td>
<td>阶段事实先影响 Group Routing；不在 Response 内切 Stage Profile</td>
</tr>
</table>
品质选择当前需要额外加入至少一个代表 Case；不能因为原 15 Case 的重点是行为结构，就把第四执行面漏掉。
## 5. 配置表 Candidate Grammar｜中文化版本
### 5.1 条件原子
一行就是一个完整判断：
```plain text
连续均温（5天） >= 15℃
```
推荐字段：
```plain text
事实 / 计算项
参数 1
参数 2
比较符
比较值 1
比较值 2
比较值 3
```
### 5.2 条件组 / RuleSet
显式表达：
```plain text
AND(...)
OR(...)
NOT(...)
```
RuleSet 可以继续引用 RuleSet 来表达括号关系；当前不人为限制嵌套深度。真实嵌套越深，本身就是表格成本证据。
### 5.3 Switch
Switch 只能开关模板已经存在的固定槽位：
```plain text
温度槽位 ON / OFF
默认修正 ON / OFF
```
不能：
```plain text
改变执行顺序
插入任意步骤
配置 Next / Jump
改变分支拓扑
```
### 5.4 Typed Result
配置侧优先使用明确结果类型，例如：
```plain text
分流到 Guarding Group
设置 Response 档位
选择 / 绑定一个 Profile
调整品质档位权重
```
如果真实 Case 开始要求“多个 Action 可自由排序”，再记录为新的顺序 / DSL 压力，不提前购买。
## 6. 中文脚本的角色也要重新判断
中文脚本目前至少有两个可能角色：
### 角色 A｜真正的可编辑 DSL
策划直接维护：
```plain text
如果 ...：
    ...
否则：
    ...
```
适用于配置已经明显变成表格式程序、RuleSet 嵌套 / 顺序 / Gate / Return 很复杂的执行面。
### 角色 B｜由配置 / Canonical AST 自动生成的可读视图
策划主要编辑表格 / Profile / RuleSet，工具自动显示：
```plain text
如果最近 5 天均温 >= 15℃
并且场内存在适合筑巢结构：
    分流一部分鱼到 Guarding Group
```
如果脚本只是“更好读”，但没有购买不可替代的编辑能力，那么优先让它做 **可读 / Debug View**，避免形成第二套 Source of Truth。
## 7. 当前阶段结论
现在还不能给出“整个 0.3.4 应该全部 Config / 全部 DSL”的结论。
更准确的是：
```plain text
Spatial + Response：
    当前 Coverage 没有逼出通用 Sequential DSL

Group Routing：
    必须纳入下一轮 Authoring Stress Test

Quality Selection：
    必须纳入下一轮 Authoring Stress Test
```
因此目前 Verdict 应写：
```plain text
HYBRID_DIRECTION_STILL_PLAUSIBLE
BUT FOUR-SURFACE COVERAGE INCOMPLETE
```
不是提前写成 `HYBRID_SUFFICIENT`。
## 8. 下一步｜比之前更窄
下一轮只补两个真正缺失的执行面，不重跑全部 15 Case：
1. **Group Routing / 分群：**用 Guard + Atlantic Salmon 两个案例，完整画出 Config 与中文脚本，并统计条件行数、RuleSet 深度、Group 权重操作、模板数量。
2. **Quality Selection / 品质选择：**选 2–3 个高区分案例，例如大钩大饵偏大鱼、夜间成年低活性偏小鱼、特殊环境改变品质分布，完整画出 Config 与中文脚本。
然后把四块执行面放在同一张总表里，再做一次真正的 Authoring Verdict。
## 2. 分群逻辑压力测试｜3 个 Case
### G1｜护巢 / 护幼：满足条件时，从普通组分出 Guarding Group
这是最基础的 Group Routing Case，也已经是当前 Working Decision。
#### 配置表
**条件原子：**
<table fit-page-width="true" header-row="true">
<tr>
<td>条件组</td>
<td>条件</td>
<td>事实 / 计算项</td>
<td>参数1</td>
<td>比较符</td>
<td>比较值1</td>
<td>比较值2</td>
</tr>
<tr>
<td>G1</td>
<td>C1</td>
<td>当前日期</td>
<td>—</td>
<td>BETWEEN</td>
<td>繁殖窗口起点</td>
<td>繁殖窗口终点</td>
</tr>
<tr>
<td>G1</td>
<td>C2</td>
<td>连续均温</td>
<td>5天</td>
<td>&gt;=</td>
<td>护巢温度阈值</td>
<td>—</td>
</tr>
<tr>
<td>G1</td>
<td>C3</td>
<td>场内结构集合</td>
<td>—</td>
<td>CONTAINS_ANY</td>
<td>适合筑巢结构集合</td>
<td>—</td>
</tr>
</table>
**规则集：**
<table fit-page-width="true" header-row="true">
<tr>
<td>规则集</td>
<td>组合方式</td>
<td>显示顺序</td>
<td>引用类型</td>
<td>引用</td>
</tr>
<tr>
<td>GuardEligible</td>
<td>AND</td>
<td>1</td>
<td>Condition</td>
<td>G1.C1</td>
</tr>
<tr>
<td>GuardEligible</td>
<td>AND</td>
<td>2</td>
<td>Condition</td>
<td>G1.C2</td>
</tr>
<tr>
<td>GuardEligible</td>
<td>AND</td>
<td>3</td>
<td>Condition</td>
<td>G1.C3</td>
</tr>
</table>
**分群结果：**
<table fit-page-width="true" header-row="true">
<tr>
<td>路由规则</td>
<td>命中条件</td>
<td>目标 FishGroup</td>
<td>权重处理</td>
<td>参数</td>
</tr>
<tr>
<td>Route_Guard</td>
<td>@GuardEligible</td>
<td>Guarding</td>
<td>从 NormalFeeding 分流</td>
<td>@GuardingShare</td>
</tr>
<tr>
<td>Route_Default</td>
<td>默认</td>
<td>NormalFeeding</td>
<td>保留剩余权重</td>
<td>—</td>
</tr>
</table>
#### 中文逻辑
```plain text
如果 当前日期处于繁殖窗口
并且 最近 5 天平均水温 >= 护巢温度阈值
并且 当前钓场存在适合筑巢的结构：

    从 NormalFeeding Group 分出 @GuardingShare
    放入 Guarding Group

否则：
    Guarding Group 权重 = 0
    全部保留在 NormalFeeding Group
```
**读数：** 普通配置表很自然；不需要 Sequential DSL。主要复杂度来自 Predicate，而不是执行顺序。
---
### G2｜大西洋鲑：繁殖洄游条件成立时，把一部分机会路由到 Migration Reaction Group
这里不恢复 `LifecycleCohort`。FishGroup 只是当前条件下的行为路由结果。
#### 配置表
<table fit-page-width="true" header-row="true">
<tr>
<td>条件组</td>
<td>条件</td>
<td>事实 / 计算项</td>
<td>参数</td>
<td>比较符</td>
<td>比较值</td>
</tr>
<tr>
<td>G1</td>
<td>C1</td>
<td>当前洄游 / 繁殖阶段事实</td>
<td>—</td>
<td>IN</td>
<td>@FreshwaterMigrationStages</td>
</tr>
<tr>
<td>G1</td>
<td>C2</td>
<td>当前水体类型</td>
<td>—</td>
<td>IN</td>
<td>@FreshwaterMigrationWaterTypes</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>规则集</td>
<td>组合方式</td>
<td>引用</td>
</tr>
<tr>
<td>MigrationReactionEligible</td>
<td>AND</td>
<td>G1.C1, G1.C2</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>路由规则</td>
<td>命中条件</td>
<td>目标 FishGroup</td>
<td>权重处理</td>
<td>参数</td>
</tr>
<tr>
<td>Route_MigrationReaction</td>
<td>@MigrationReactionEligible</td>
<td>MigrationReaction</td>
<td>按配置分流</td>
<td>@MigrationReactionShare</td>
</tr>
<tr>
<td>Route_Normal</td>
<td>默认</td>
<td>NormalFeeding</td>
<td>保留剩余权重</td>
<td>—</td>
</tr>
</table>
#### 中文逻辑
```plain text
如果 当前鱼处于淡水繁殖洄游相关阶段
并且 当前水体属于对应洄游水体：

    从普通摄食机会中分出 @MigrationReactionShare
    放入 MigrationReaction Group

否则：
    不生成 MigrationReaction Group
```
后续 Response：
```plain text
NormalFeeding Group：
    使用普通摄食 Response

MigrationReaction Group：
    普通 Feeding 强抑制或关闭
    只评价非摄食性 Reaction / Provocation Response
```
**读数：** 分群本身仍是 Predicate + 权重路由；没有理由为了阶段差异购买 Runtime Stage Selector。
---
### G3｜复杂分群：两套不同条件都可以进入同一个 Group
这个 Case 专门测试我们前面讨论的 `G1 OR G2` 与 RuleSet 嵌套。
假设某个特殊摄食 Group 在两种完全不同的环境组合下都成立：
```plain text
路径 A：
    春季
    + 水温合适
    + 浅滩草区存在

路径 B：
    秋季
    + 水温下降
    + 深水结构存在
```
#### 配置表
<table fit-page-width="true" header-row="true">
<tr>
<td>条件组</td>
<td>条件</td>
<td>事实 / 计算项</td>
<td>参数</td>
<td>比较符</td>
<td>比较值1</td>
<td>比较值2</td>
</tr>
<tr>
<td>SpringPath</td>
<td>C1</td>
<td>当前日期</td>
<td>—</td>
<td>BETWEEN</td>
<td>春季起点</td>
<td>春季终点</td>
</tr>
<tr>
<td>SpringPath</td>
<td>C2</td>
<td>当前水温</td>
<td>—</td>
<td>BETWEEN</td>
<td>@SpringTempMin</td>
<td>@SpringTempMax</td>
</tr>
<tr>
<td>SpringPath</td>
<td>C3</td>
<td>场内结构集合</td>
<td>—</td>
<td>CONTAINS_ANY</td>
<td>浅滩 / 草区</td>
<td>—</td>
</tr>
<tr>
<td>FallPath</td>
<td>C1</td>
<td>当前日期</td>
<td>—</td>
<td>BETWEEN</td>
<td>秋季起点</td>
<td>秋季终点</td>
</tr>
<tr>
<td>FallPath</td>
<td>C2</td>
<td>近期水温趋势</td>
<td>3天</td>
<td>==</td>
<td>下降</td>
<td>—</td>
</tr>
<tr>
<td>FallPath</td>
<td>C3</td>
<td>场内结构集合</td>
<td>—</td>
<td>CONTAINS_ANY</td>
<td>深坑 / 崖壁</td>
<td>—</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>规则集</td>
<td>组合方式</td>
<td>显示顺序</td>
<td>引用类型</td>
<td>引用</td>
</tr>
<tr>
<td>R_Spring</td>
<td>AND</td>
<td>1</td>
<td>ConditionGroup</td>
<td>SpringPath</td>
</tr>
<tr>
<td>R_Fall</td>
<td>AND</td>
<td>1</td>
<td>ConditionGroup</td>
<td>FallPath</td>
</tr>
<tr>
<td>R_SpecialFeeding</td>
<td>OR</td>
<td>1</td>
<td>RuleSet</td>
<td>R_Spring</td>
</tr>
<tr>
<td>R_SpecialFeeding</td>
<td>OR</td>
<td>2</td>
<td>RuleSet</td>
<td>R_Fall</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>路由规则</td>
<td>命中条件</td>
<td>目标 FishGroup</td>
<td>权重处理</td>
<td>参数</td>
</tr>
<tr>
<td>Route_SpecialFeeding</td>
<td>@R_SpecialFeeding</td>
<td>SpecialFeeding</td>
<td>从 Default 分流</td>
<td>@SpecialFeedingShare</td>
</tr>
</table>
#### 中文逻辑
```plain text
如果：
    （当前处于春季
     并且 水温处于春季适温区间
     并且 场内存在浅滩或草区）

或者：
    （当前处于秋季
     并且 最近 3 天水温正在下降
     并且 场内存在深坑或崖壁）

则：
    从 Default Group 分出 @SpecialFeedingShare
    放入 SpecialFeeding Group
```
**读数：** 这里开始出现 RuleSet 嵌套，但仍没有出现 Step / Next / Jump。它说明“表格开始变长”，还没有说明“必须 DSL”。
## 3. 品质选择逻辑压力测试｜3 个 Case
### Q1｜大钩 + 大饵：提高大个体品质权重
#### 配置表
<table fit-page-width="true" header-row="true">
<tr>
<td>条件组</td>
<td>条件</td>
<td>事实 / 计算项</td>
<td>比较符</td>
<td>比较值</td>
</tr>
<tr>
<td>G1</td>
<td>C1</td>
<td>钩尺寸等级</td>
<td>&gt;=</td>
<td>@LargeHookThreshold</td>
</tr>
<tr>
<td>G1</td>
<td>C2</td>
<td>饵尺寸等级</td>
<td>&gt;=</td>
<td>@LargeBaitThreshold</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>规则集</td>
<td>组合方式</td>
<td>引用</td>
</tr>
<tr>
<td>BigGear</td>
<td>AND</td>
<td>G1.C1, G1.C2</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>品质规则</td>
<td>命中条件</td>
<td>调整对象</td>
<td>调整方式</td>
<td>参数</td>
</tr>
<tr>
<td>Q_BigGear</td>
<td>@BigGear</td>
<td>大型 / 稀有品质</td>
<td>上调相对权重</td>
<td>@BigGearBoost</td>
</tr>
</table>
#### 中文逻辑
```plain text
读取 当前 FishGroup 的基础品质分布

如果 钩尺寸 >= @LargeHookThreshold
并且 饵尺寸 >= @LargeBaitThreshold：
    上调 大型 / 稀有品质的相对权重 @BigGearBoost

归一化品质权重
抽取具体品质
```
**读数：** 纯条件 + 权重调整，非常适合配置表；没有 Sequence 压力。
---
### Q2｜成年个体低活性时段：让抽中的品质整体偏小
#### 配置表
<table fit-page-width="true" header-row="true">
<tr>
<td>条件</td>
<td>事实 / 计算项</td>
<td>比较符</td>
<td>比较值</td>
</tr>
<tr>
<td>C1</td>
<td>当前时段</td>
<td>IN</td>
<td>@AdultLowActivityDayparts</td>
</tr>
</table>
<table fit-page-width="true" header-row="true">
<tr>
<td>品质规则</td>
<td>命中条件</td>
<td>调整对象</td>
<td>调整方式</td>
<td>参数</td>
</tr>
<tr>
<td>Q_AdultInactive</td>
<td>C1</td>
<td>成年 / 高品质档</td>
<td>下调相对权重</td>
<td>@AdultInactivePenalty</td>
</tr>
<tr>
<td>Q_AdultInactive_Small</td>
<td>C1</td>
<td>幼小 / 低品质档</td>
<td>上调相对权重</td>
<td>@JuvenileRelativeBoost</td>
</tr>
</table>
#### 中文逻辑
```plain text
读取 当前 FishGroup 的基础品质分布

如果 当前时段属于成年个体低活性时段：
    下调 成年 / 高品质档权重
    上调 幼小 / 低品质档权重

归一化品质权重
抽取具体品质
```
**读数：** 这里第一次出现“同一个条件命中后对多个品质档做多个调整”，但这些调整之间没有可编辑先后依赖，仍可视为一个 Typed Quality Adjustment Result，而不是 Action Sequence。
---
### Q3｜复合条件：装备条件和环境条件分别作用于不同品质档
这个 Case 测试多条规则是否需要按顺序执行。
假设：
```plain text
大钩 + 大饵
→ 大型鱼更容易进入候选

夜间 + 低温
→ 成年大型个体活性下降
→ 高品质档受压
```
#### 配置表
<table fit-page-width="true" header-row="true">
<tr>
<td>规则集</td>
<td>条件</td>
<td>调整对象</td>
<td>调整方式</td>
<td>参数</td>
</tr>
<tr>
<td>R_BigGear</td>
<td>大钩 AND 大饵</td>
<td>大型 / 稀有品质</td>
<td>上调相对权重</td>
<td>@BigGearBoost</td>
</tr>
<tr>
<td>R_ColdNightAdult</td>
<td>夜间 AND 低温</td>
<td>成年高品质档</td>
<td>下调相对权重</td>
<td>@ColdNightAdultPenalty</td>
</tr>
</table>
#### 中文逻辑
```plain text
读取 当前 FishGroup 的基础品质分布

如果 大钩并且大饵：
    上调 大型 / 稀有品质权重

如果 夜间并且低温：
    下调 成年高品质权重

把所有品质调整作用到同一份基础分布
归一化
抽取具体品质
```
**关键设计点：** 当前先把多条品质规则理解为**并列 Modifier 集合**，它们共同作用到同一份基础品质分布；规则行顺序不改变语义。只有以后出现“先做 A，A 的结果再决定是否执行 B”这种明确依赖，才产生真正的 Quality Sequential LogicTemplate 压力。
## 4. 第一轮对比读数｜分群与品质选择
<table fit-page-width="true" header-row="true">
<tr>
<td>执行面</td>
<td>Case</td>
<td>配置表表现</td>
<td>中文脚本表现</td>
<td>当前新增结构压力</td>
</tr>
<tr>
<td>分群</td>
<td>G1 Guard</td>
<td>很自然</td>
<td>更易读</td>
<td>无</td>
</tr>
<tr>
<td>分群</td>
<td>G2 Migration Reaction</td>
<td>很自然</td>
<td>更易读</td>
<td>无 Stage Selector</td>
</tr>
<tr>
<td>分群</td>
<td>G3 OR-of-AND</td>
<td>开始变长，但完整</td>
<td>明显更紧凑</td>
<td>RuleSet 嵌套压力</td>
</tr>
<tr>
<td>品质</td>
<td>Q1 Big Gear</td>
<td>很自然</td>
<td>更易读</td>
<td>无</td>
</tr>
<tr>
<td>品质</td>
<td>Q2 Adult Low Activity</td>
<td>自然</td>
<td>更易读</td>
<td>Typed Multi-bin Adjustment</td>
</tr>
<tr>
<td>品质</td>
<td>Q3 Compound Modifiers</td>
<td>自然</td>
<td>更易读</td>
<td>无 Sequential pressure</td>
</tr>
</table>
### 当前工作结论
目前新增的两个执行面没有逼出 Sequential DSL：
```plain text
Group Routing
→ Condition Atom + RuleSet + Typed Weight Routing

Quality Selection
→ Condition Atom + RuleSet + Typed Quality Modifier
```
中文脚本在这两块的主要优势仍然是**阅读与 Review**，不是不可替代的编辑能力。
当前更像是：
```plain text
分群：配置 / RuleSet 作为编辑源
烘焙：更可能需要真正顺序 DSL 或固定顺序 LogicTemplate
响应：LogicTemplate + RuleSet / Profile
品质：配置 / RuleSet 作为编辑源

全部编译到同一 Canonical Program / AST
中文脚本可作为自动生成的可读视图 / Debug View
```
### 需要继续攻击的两个点
1. **Group Routing**：真实项目里是否会频繁出现比 G3 更深的 RuleSet 嵌套。如果会，表格可读性会迅速下降。
2. **Quality Selection**：是否存在真实 Case 要求“前一条品质规则执行结果成为后一条规则的输入”。如果不存在，品质选择很可能根本不需要 Sequential DSL。
<page url="https://app.notion.com/p/3d6a4137d23681799bf0e688169c049d">Authoring Projection Protocol R0｜四执行面铺量与展开粒度规范</page>
## 5. Bass FishGroup Routing Candidate｜Guard / Cold-Slow / Stress Overlay
### 5.1 `@GuardingShare` 的精确语义
`@GuardingShare` 是**配置参数引用**。Group Routing 逻辑负责判断当前 Guarding 是否成立；命中后读取该参数，决定本次 Species Supply / Opportunity Weight 有多少进入 Guarding Group。
为了避免人为制造“先改 Normal、再从 Normal 扣除”的顺序依赖，推荐语义直接写成目标分配：
```plain text
如果 GuardingEligibility 成立：
    GuardingWeight = SpeciesBaseWeight × @GuardingShare
    NormalFeedingWeight = SpeciesBaseWeight × (1 - @GuardingShare)
否则：
    GuardingWeight = 0
    NormalFeedingWeight = SpeciesBaseWeight
```
如果未来存在 3 个以上 Group，则优先让 Router 直接产生一个 Group Weight Vector / Share Vector，再做统一校验 / 归一化；不要靠可编辑的“逐条扣权重”顺序来决定结果。
### 5.2 FishGroup 的准入判据
一个环境条件**不是因为现实上很重要就自动升 FishGroup**。当前 Working 判据：
> 当某个条件会成套改变至少两个执行面的逻辑语义 / Runtime Program，例如同时改变 Bake 的空间解释和 Response 的可接受呈现方式，并且这种状态持续一个有意义的时间窗口，才优先考虑独立 FishGroup。
如果只是：
- 某个 Profile 数值变差；
- 活性 / FeedingReadiness 连续下降；
- 某些熟悉拟饵更难骗；
- 某个空间区域权重下降；
优先作为 Context / Profile / Overlay / Parameter，不升 Group。
### 5.3 大口黑鲈当前候选 Group
<table fit-page-width="true" header-row="true">
<tr>
<td>候选</td>
<td>当前判断</td>
<td>为什么</td>
</tr>
<tr>
<td>Normal Feeding</td>
<td>KEEP</td>
<td>普通觅食基线。</td>
</tr>
<tr>
<td>Spawn Guard / Parental</td>
<td>KEEP / 已形成 Working Decision</td>
<td>分群后使用 Guard-specific 空间 / Response；Defense-only simplification，不评价普通 Feeding。</td>
</tr>
<tr>
<td>Cold-Slow / Winter Quiescent</td>
<td>STRONG CANDIDATE</td>
<td>严寒时不只是“温度 Fit 变低”：空间逻辑转向相对温暖、稳定、低能耗 refuge；Functional Capacity / FeedingReadiness 显著下降；Response 对高速、长距离追逐型呈现明显不利。会同时改变 Bake 与 Response。</td>
</tr>
<tr>
<td>Heat / Hypoxia Stress</td>
<td>DEFAULT NO GROUP</td>
<td>高温、低氧可重排空间和压低能力，但大量情况仍可由 Temperature / DO / Refuge / FunctionalCapacity 连续表达。只有未来证明严重 stress 会触发一套稳定、跨多个执行面的新 Program，才升 Group。</td>
</tr>
<tr>
<td>High Angling Pressure</td>
<td>NO GROUP by default</td>
<td>更像 Cue Familiarity / learned lure avoidance / response selectivity Overlay；主要改变 Response，不应与温度等状态笛卡尔积成多个 Group。</td>
</tr>
<tr>
<td>Open-water Forage Chase / Pelagic Chase</td>
<td>DEFER / BREAKER CANDIDATE</td>
<td>季节性 prey switch 与开放水追饵存在策略故事，但目前仍可能由 Prey Field + Spatial Profile + Presentation 解释，尚未证明需要新的 Runtime Program。</td>
</tr>
<tr>
<td>Post-spawn Recovery</td>
<td>NO GROUP by default</td>
<td>优先作为 FeedingReadiness / Activity / Quality 等连续修正；除非后续证明空间与 Response 拓扑同时切换。</td>
</tr>
</table>
### 5.4 Cold-Slow Group｜当前建议逻辑
Group Routing 不应使用“当前抛点水温低”来决定整条鱼属于 Cold-Slow。它应读取**水体 / 大区级 Thermal State**，例如整个可达水体是否进入严寒状态、正常暖水 habitat 是否基本消失、仅剩相对暖 refuge 等。
```plain text
读取 水体级 Thermal State
读取 可达水域温度分布 / Warm Refuge Availability

如果 整体进入 Severe Cold：
    ColdSlow Group 权重 = 高 / 100%
    NormalFeeding Group 权重 = 低 / 0
```
进入 Cold-Slow 后，Bake 的语义发生变化：
```plain text
不是：
    只有达到普通最适温度的地点才有高权重

而是：
    在当前整体偏冷的可达环境中
    寻找相对更温暖、更稳定、能耗更低的 winter refuge
```
Response 也随 Group 改变：
```plain text
读取 当前 Presentation 的速度 / 位移 / 停留
读取 ColdSlow FunctionalCapacity / FeedingReadiness

高速、要求长距离持续追逐：
    强烈抑制

慢速、长停顿、贴近鱼位：
    相对更容易成立

近距离短爆发刺激：
    不应被“一刀切为永远无效”
    是否保留 reaction window 继续由具体 Response Rule 验证
```
### 5.5 \[SUPERSEDED\] Heat / Hypoxia 为什么暂不升 Group
> 本节已被后续“Summer Oxythermal Stress / 盛夏氧热夹压”判断替代。保留旧判断仅用于追溯，不再代表当前 Working Direction。
当前证据支持高温与低氧会影响代谢、栖地质量和空间选择，但影响并不稳定等价于“进入一种新的离散鱼脑”。例如低氧可导致避开极端缺氧区域，但也存在鱼继续留在局部低氧区域、通过深度 / 微栖地权衡解决的情况。因此当前优先：
```plain text
Temperature / DO / Refuge facts
→ Bake 空间重排
→ FunctionalCapacity / FeedingReadiness 修正
→ Response 对 pursuit / presentation 的能力约束
```
只有未来发现：
```plain text
Stress condition
→ 固定切换整套 Bake Program
→ 固定切换整套 Response Program
```
才重新评估 `HeatStress FishGroup`。
### 5.6 High Angling Pressure 为什么暂不升 Group
高钓压 / 被反复钓获更适合表达成：
```plain text
AnglingPressure / CueFamiliarity
→ 对熟悉 Cue / Presentation 的 Response 降低
→ 对新奇 / 不同 Presentation 保留相对优势
```
它与 Guard / Cold-Slow 不同：当前没有必要让它拥有独立 Spatial Bake Program。若把 `Hot + HighPressure` 直接做成一个 Group，未来很容易继续出现：
```plain text
Cold + HighPressure
Guarding + HighPressure
HeatStress + HighPressure
```
导致 Group 笛卡尔积。当前禁止这种组合型 Group 扩张，除非有明确不可压缩的 Runtime 证据。
## 6. Summer Oxythermal Stress｜盛夏氧热夹压模式
### 6.1 当前判断
将此前 `Heat / Hypoxia = default no group` 改判为：
> **STRONG FISHGROUP CANDIDATE**
前提不是“当前抛点水温高”，而是水体 / 大区级环境进入一个持续存在的夏季夹压状态：
```plain text
上层过热
+ 水体明显分层
+ 向深处虽然更凉，但深层溶氧下降
+ 光照 / 可视性、遮蔽物、prey field 等进一步限制可用位置
```
这个状态如果稳定地同时改变 Group Routing、Bake 与 Response，就符合 FishGroup 准入原则。
### 6.2 Group Routing
建议由上游 Context Resolver 提供一个水体级事实，例如：
```plain text
SummerOxythermalStress = NONE / LOW / HIGH
```
或者等价的 typed facts：
```plain text
SurfaceHeatStress
VerticalStratification
DeepOxygenConstraint
UsableRefugeBand
```
不要用“当前饵点温度高”直接切 Group。
命中后可以由配置参数决定多少 Species Supply 进入该 Group，例如：
```plain text
@SummerStressShare
```
### 6.3 Bake｜从“绝对最适”切换到“约束下相对最优”
普通模式可能问：
```plain text
这个位置的温度 / 结构 / 水层是否接近该鱼平时的最适？
```
Summer Stress Group 更应该问：
```plain text
在当前整个水体都不理想的情况下
哪个位置是“最不差、最可用”的 refuge？
```
建议的 Authoring-visible 逻辑：
```plain text
读取 当前目标水层的温度
读取 当前目标水层的溶氧
读取 当前目标水层的光照 / 可视性
读取 当前结构 / 遮蔽物
读取 当前 prey field

如果 溶氧低于严重不可用边界：
    返回 极低 / 0 空间权重

否则：
    计算 相对降温收益
    计算 溶氧安全余量
    计算 光照 / 可视性是否仍支持当前摄食方式
    计算 结构 / 遮蔽物价值
    计算 prey availability

    按 SummerStress Bake Template 的固定规则合并
    返回 当前约束下的相对 refuge score
```
当前优先把溶氧视为更接近硬下限；光照 / 可视性先作为软约束，不把“深水过暗”写成未经证明的物种硬门槛。
### 6.4 Response｜强刺激、短程 Reaction，而不是无限长追
这个 Group 不应简单理解为“高温时鱼更凶，所以所有高速饵都更好”。高温 + 低氧可能同时压低持续运动能力与普通 Feeding Readiness。
更一致的策略故事是：
```plain text
普通 Feeding Channel：
    受到抑制

长距离持续追逐：
    不占优

近距离 Reaction Channel：
    对强振动
    强闪光
    突发位移
    erratic motion
    deflection
    近距离侵入
    给予较高 salience / reaction response
```
因此“猛烈钓法”应解释为**强刺激、短程触发**，而不是“鱼在缺氧和高温下还能长期高速追逐”。
### 6.5 Evidence / Gameplay Translation 边界
生态研究可以支持高温 + 低氧会压缩可用栖息空间、改变夏季水层利用并降低低氧区域的栖息质量；专业垂钓经验也大量使用 flash / vibration / erratic presentation 来触发盛夏 reaction bite。
但目前不能把下面这句话当科学事实：
```plain text
高温低氧
→ 必然导致振动 / 闪光反应口
```
这一段应明确标成：
```plain text
Ecology-supported habitat shift
+
Angling-practice-supported gameplay translation
```
是否最终 Promotion 为正式 FishGroup，要由后续 Bass 深度 Case 验证它是否真的稳定拥有独立的 Group Routing + Bake + Response Program。
## 7. Group Routing Weight Contract｜本页先闭合最小语义
Reviewer 提出的“分群权重到底是什么”是有效问题。当前 Working Candidate：
> `GroupShare` 是 **Species 当前基础供给 / 基础机会权重的无量纲分配比例**，不是最终中鱼概率，不是 Response 质量，也不是额外生成容量。
所有 Group 分配都读取同一份 `SpeciesBaseSupplySnapshot`，不得按可编辑顺序反复从“剩余权重”继续扣。
例如：
```plain text
GuardingShare = 0.30
SummerStressShare = 0.20

GuardingWeight = SpeciesBaseSupply × 0.30
SummerStressWeight = SpeciesBaseSupply × 0.20
DefaultWeight = SpeciesBaseSupply × 0.50
```
当前约束：
```plain text
每个 share ∈ [0, 1]
所有同时成立的 special-group share 之和 <= 1
Default Group 承接剩余 share
```
若动态条件导致同时成立的 share 总和 \> 1：
```plain text
当前 Working 处理 = INVALID ROUTING RESULT
必须产生 Validation / Trace Error
不得静默归一化
```
原因：静默归一化会让策划写的 `0.4 / 0.4 / 0.4` 自动变成另一组比例，隐藏错误。
未来若确有“相对 Group 权重，最后统一归一化”的业务需求，应作为另一种明确 Routing Result Type，而不是混用当前 `Share` 语义。
## 8. Reviewer Findings Response R0
### 8.1 分群权重语义未闭合
**ACCEPT / 原 blocker 有价值。**
本页已用第 7 节补最小 Working Contract。后续正式 Contract 仍需确定字段名、Owner、Validation 生命周期。
### 8.2 品质调整数学语义不足
**ACCEPT / 仍是 blocker。**
当前 Stress Test 只能证明“配置 / RuleSet 能写出条件”，还不能证明 Quality Selection 的数值 Contract 已闭合。
等待当前 GPT Work 的 Quality Breaker Scan 回来后，由 Chat 明确：
```plain text
允许哪些 Typed Modifier
多个 Modifier 如何组合
是否只读取原始输入
何时归一化
zero-sum fallback
```
在此之前不得把 `QUALITY_PARALLEL_MODIFIERS_SUFFICIENT` 提升成生产结论。
### 8.3 Bake 预计算 Activity / FeedingReadiness 的 Owner 与生命周期
**ACCEPT，但修正方式是收窄本页，而不是现在设计完整缓存系统。**
当前 0.3.4.0 Bake 正式输出仍只有：
```plain text
SpatialDistributionWeight
```
Activity / FeedingReadiness 目前只能作为未来候选预计算事实。Owner、刷新、失效、Snapshot 边界未闭合前，不把它们写成 Current Bake 输出。
### 8.4 Canonical Representation 仍是口号
**ACCEPT AS MAJOR，但不是这篇 Fast Design Lane 的机制 blocker。**
本页可以提出：
```plain text
不同 Authoring Surface
→ 编译到 Canonical Representation
```
但当前只能算 Working Architecture Hypothesis。
在进入实现 Candidate 前，必须至少补：
```plain text
最小 Node Types
Surface Input / Output Contract
Condition / Result / Profile Ref 映射
Error / Trace Anchor
一例 Group / Bake / Response / Quality → Canonical IR
```
### 8.5 跨执行面因果归属未闭合
**STRONGLY ACCEPT / MAJOR。**
这是当前最值得立刻建立的新检查项。
同一个事实可以被多个 Surface 消费，但不能重复结算同一种因果。
例如 Summer Oxythermal Stress：
```plain text
Group Routing：
    高温 / 分层 / 深层低氧
    → 决定是否进入 SummerStress Group

Bake：
    当前目标点温度 / DO / 光照 / 结构 / prey
    → 决定 Group 内分布在哪里

Response：
    不再次重复扣一遍“高温惩罚”
    → 只消费该 Group 已定义的 FeedingReadiness / FunctionalCapacity / Reaction 语义

Quality Selection：
    只有当高温真的改变不同品质个体的相对可钓供给时才消费
    → 不因为“高温已经影响 Response”就自动再改品质
```
后续应建立 `Cause → Surface Ownership Ledger`，作为 Anti-double-counting Contract。
### 8.6 Case 覆盖口径不一致
**ACCEPT / minor-to-major for auditability。**
标题已去掉容易误导的 `6 Case`。后续应把正文样本明确标为：
```plain text
Illustrative Example
Formal Stress Case
Coverage Case
Breaker Case
```
并单独统计正式样本，不再混数。
### 8.7 重复编号
**ACCEPT / MINOR。**
下一个结构整理 Pass 统一修，不影响当前机制判断。
### 8.8 Guarding / MigrationReaction 的“关闭 Feeding”缺少 Typed Result
**PARTIAL ACCEPT。**
Guarding 不一定需要一个数值 `Feeding = 0` Result。当前更干净的结构是：
```plain text
Guarding FishGroup
→ 绑定 Defense-only Response Template
→ Feeding Evaluator 根本不进入该 Group Program
```
这是一种结构性关闭，可以通过 Program Binding 验证。
MigrationReaction 若继续使用“普通 Feeding 强抑制 / 关闭”这种表述，则必须进一步明确到底是：
```plain text
Disable Feeding Channel
CAP Feeding Response
SET Feeding Response Band
```
因此该部分 Reviewer finding 有效，仍需闭合。
### 8.9 对 Reviewer Verdict 的当前裁决
`ARTIFACT_REVISE` 是合理 Verdict。
但 Revision 目标不是把本页扩成完整 Production Spec，而是：
1. 补足会影响 Authoring 对比公平性的最小语义 Contract；
2. 删除 / 限定超出 Current 的暗示；
3. 把真正需要独立 Contract 的事项路由到对应 Owner；
4. 保留本页作为 Fast Design / Stress Test，而不是重复正式 Runtime Spec。
## 6. Bass 5-Group Representation Projection R0｜真实样板回投
> 来源：<mention-page url="https://app.notion.com/p/3d6a4137d23681e2af96e873eef9411a"/>。本节只做 **Representation Projection**，不重新决定 Bass 机制。
当前固定五个 Working Group：
```plain text
Normal Feeding
Guarding
Cold-Slow
Summer Oxythermal Stress
Open-water Forage Chase
```
冷锋、高钓压等作为 Overlay，不新增 Group。
### 6.1 Group Routing｜五个 Group 怎么分
#### A｜配置表达
**条件原子 / RuleSet 摘要：**
<table fit-page-width="true" header-row="true">
<tr>
<td>Group</td>
<td>主要输入事实</td>
<td>RuleSet 语义</td>
<td>Share 来源</td>
</tr>
<tr>
<td>Guarding</td>
<td>繁殖窗口、持续水温条件、场内合法筑巢结构</td>
<td>全部成立</td>
<td>`@GuardingShare`</td>
</tr>
<tr>
<td>Cold-Slow</td>
<td>水体级 SevereCold、正常暖 habitat 稀缺 / warm refuge 状态</td>
<td>严寒状态成立</td>
<td>`@ColdSlowShareProfile`</td>
</tr>
<tr>
<td>SummerStress</td>
<td>上层持续过热、深层低氧、可用水层被压缩</td>
<td>OxythermalCompression 达阈值</td>
<td>`@SummerStressShareProfile`</td>
</tr>
<tr>
<td>ForageChase</td>
<td>PelagicForageState、OpenWaterForageAvailability</td>
<td>开放水饵鱼群状态足够强</td>
<td>`@ForageChaseShareProfile`</td>
</tr>
<tr>
<td>NormalFeeding</td>
<td>—</td>
<td>接收剩余 Share</td>
<td>`1 - Σ SpecialShare`</td>
</tr>
</table>
**Group Routing Result：**
```plain text
GuardingShare      = 命中 Guard Rule ? resolve(@GuardingShare) : 0
ColdSlowShare      = 命中 Cold Rule ? resolve(@ColdSlowShareProfile) : 0
SummerStressShare  = 命中 Summer Rule ? resolve(@SummerStressShareProfile) : 0
ForageChaseShare   = 命中 Forage Rule ? resolve(@ForageChaseShareProfile) : 0

如果 SpecialShareTotal > 1：
    配置 / 求值错误

NormalShare = 1 - SpecialShareTotal
```
当前不使用“先从 Normal 扣 Guard、再从剩余扣 Cold”的顺序算法。
#### B｜中文逻辑
```plain text
读取 当前水体 / 钓场的慢速环境事实

如果满足护巢条件：
    GuardingShare = 读取 @GuardingShare
否则：
    GuardingShare = 0

如果整个可达水体进入严寒状态：
    ColdSlowShare = 用当前严寒程度查询 @ColdSlowShareProfile
否则：
    ColdSlowShare = 0

如果形成明显的热—氧夹压状态：
    SummerStressShare = 用当前夹压程度查询 @SummerStressShareProfile
否则：
    SummerStressShare = 0

如果开放水饵鱼群状态成立：
    ForageChaseShare = 用当前 forage state 查询 @ForageChaseShareProfile
否则：
    ForageChaseShare = 0

如果 SpecialShare 总和 > 1：
    报错，不静默归一化

NormalFeedingShare = 1 - SpecialShare 总和
返回 Group Share Vector
```
**第一轮读数：** Group Routing 当前仍像 `Condition Atom + RuleSet + Share Result`，没有出现 `Next / Jump / Early Return` 型 Sequential DSL 压力。
---
### 6.2 Bake｜五个 Group 的空间逻辑
这里是当前最有表达压力的一块。先完整承认五个 Group 的**语义程序确实不同**，再看能否在生产上聚类；不提前为了减少模板数量把它们压成一个万能 AST。
#### A｜配置 / LogicTemplate 投影
<table fit-page-width="true" header-row="true">
<tr>
<td>Group</td>
<td>Bake Program Candidate</td>
<td>关键可配置输入 / Profile</td>
<td>结构性差异</td>
</tr>
<tr>
<td>NormalFeeding</td>
<td>`BA-NORMAL-HABITAT`</td>
<td>温度、结构、水层、时段、FoodField 等 Profile</td>
<td>普通 habitat fit / ordered factors</td>
</tr>
<tr>
<td>Guarding</td>
<td>`BA-GUARD-NEST`</td>
<td>合法巢区 Rule、筑巢结构、深度、温度可行性</td>
<td>先做 Nest Eligibility；无合法巢区可提前退出</td>
</tr>
<tr>
<td>Cold-Slow</td>
<td>`BA-COLD-RELATIVE-REFUGE`</td>
<td>相对暖度、温度稳定性、低流速 / 低能耗、DO floor</td>
<td>从“绝对最适”改成“整体严寒下的相对最好 refuge”</td>
</tr>
<tr>
<td>SummerStress</td>
<td>`BA-OXYTHERMAL-TRADEOFF`</td>
<td>相对降温收益、DO 安全余量、可视性、cover、prey context</td>
<td>温度收益与低氧风险的多约束权衡；严重低氧 hard gate</td>
</tr>
<tr>
<td>ForageChase</td>
<td>`BA-FORAGE-COUPLED`</td>
<td>ForageSchoolIntensity、VerticalAlignment、温度 / DO 可行性</td>
<td>空间主锚点改为当前 Pelagic Forage Field；forage 不成立可提前退出</td>
</tr>
</table>
这里的 `BA-*` 只是**语义程序候选签名**，不是已经确认的 5 个生产 LogicTemplate。后续只有在确认执行顺序 / 拓扑无法共用时才计入 `L_bake`。
#### B｜中文逻辑投影
**Normal Feeding**
```plain text
读取 当前空间目标

用当前水温查询 @NormalTemperatureProfile
得到 TemperatureFit

用当前结构查询 @NormalStructureProfile
得到 StructureFit

用当前水层查询 @NormalLayerProfile
得到 LayerFit

用当前时段查询 @NormalTimeProfile
得到 TimeFit

读取 / 查询当前 FoodField
得到 FoodFit

按照 Normal Bake 的固定合并规则
合并这些结果
返回 SpatialDistributionWeight
```
**Guarding**
```plain text
读取 当前空间目标
读取 当前空间是否属于合法巢区 / 产床候选

如果不是合法巢区：
    返回极低 / 0 SpatialDistributionWeight

用当前结构查询 @NestStructureProfile
得到 NestStructureFit

用当前深度查询 @NestDepthProfile
得到 NestDepthFit

用当前温度查询 @NestTemperatureProfile
得到 NestTemperatureFit

按 Guarding Bake 固定规则合并
返回 SpatialDistributionWeight
```
**Cold-Slow**
```plain text
读取 当前空间目标温度
读取 当前水体整体 Thermal State
读取 当前区域温度稳定性
读取 当前流速 / 能耗 Context
读取 当前溶氧

计算：
    当前点相对于整个严寒水体的 RelativeWarmth

用 RelativeWarmth 查询 @ColdRelativeWarmthProfile
得到 WarmRefugeFit

用温度稳定性查询 @ColdThermalStabilityProfile
得到 StabilityFit

用流速 / 能耗条件查询 @ColdEnergyCostProfile
得到 EnergyRefugeFit

如果溶氧低于 Cold 可用底线：
    返回极低 / 0

按 Cold-Slow 固定 refuge 规则合并
返回 SpatialDistributionWeight
```
**Summer Oxythermal Stress**
```plain text
读取 当前空间目标温度
读取 当前空间目标溶氧
读取 当前光照 / 可视性
读取 当前 cover / structure
读取 当前 prey context
读取 水体级 Oxythermal State

如果溶氧进入不可用区：
    返回极低 / 0

计算：
    相对降温收益
    溶氧安全余量

用相对降温收益查询 @CoolingBenefitProfile
用溶氧安全余量查询 @DOSafetyProfile
用可视性查询 @StressVisibilityProfile
用 cover 查询 @StressCoverProfile

按 SummerStress 固定 trade-off 规则合并
返回 SpatialDistributionWeight
```
**Open-water Forage Chase**
```plain text
读取 当前空间目标 ForageSchoolIntensity
读取 当前空间目标与饵鱼群的水层对齐程度
读取 当前温度
读取 当前溶氧

如果 ForageSchoolIntensity 低于最低成立阈值：
    返回极低 / 0

用 ForageSchoolIntensity 查询 @ForageIntensityProfile
得到 ForageFit

用 VerticalAlignment 查询 @ForageVerticalAlignmentProfile
得到 AlignmentFit

评价温度 / 溶氧是否可行

按 Forage-Chase 固定规则合并
返回 SpatialDistributionWeight
```
**第一轮读数：** 五段中文逻辑已经明显不是“换几个参数就完全同一回事”。尤其 `Cold relative refuge`、`Summer oxythermal trade-off`、`Forage-field anchor` 各自引入不同中间语义。Bake 仍是当前最强 DSL / 顺序 Program 压力面。
---
### 6.3 Response｜当前只需要 3 类拓扑 Candidate
#### A｜配置投影
<table fit-page-width="true" header-row="true">
<tr>
<td>Group</td>
<td>Response Template Candidate</td>
<td>Profile / Rule</td>
<td>固定汇总</td>
</tr>
<tr>
<td>NormalFeeding</td>
<td>`R-FEEDING-ONLY`</td>
<td>`@NormalFeedingProfile`</td>
<td>直接返回 Feeding</td>
</tr>
<tr>
<td>ForageChase</td>
<td>`R-FEEDING-ONLY`</td>
<td>`@ForageChaseFeedingProfile`</td>
<td>直接返回 Feeding</td>
</tr>
<tr>
<td>Guarding</td>
<td>`R-DEFENSE-ONLY`</td>
<td>`@GuardThreatRule / Profile`</td>
<td>直接返回 Defense；不评价 Feeding</td>
</tr>
<tr>
<td>Cold-Slow</td>
<td>`R-FEEDING-REACTION-MAX`</td>
<td>`@ColdFeedingProfile`  • `@ColdReactionProfile`</td>
<td>`MAX` Working Candidate</td>
</tr>
<tr>
<td>SummerStress</td>
<td>`R-FEEDING-REACTION-MAX`</td>
<td>`@SummerFeedingProfile`  • `@SummerReactionProfile`</td>
<td>`MAX` Working Candidate</td>
</tr>
</table>
#### B｜中文逻辑
**Normal / ForageChase：同模板、不同 Feeding Profile**
```plain text
读取 当前 Opportunity / Presentation Cue
读取 当前 Group 的 Feeding Profile
评价 Feeding Match
返回 Feeding Response
```
ForageChase 的 Profile 更关注：
```plain text
与 forage band 的空间关系
拟饵尺寸 / silhouette
moving / search trajectory
逃逸 / erratic motion
速度匹配
```
**Guarding**
```plain text
读取 Presentation 与巢区 / 幼鱼保护区的关系
评价 Defense Threat
返回 Defense Response
不评价普通 Feeding
```
**Cold-Slow / SummerStress：共享拓扑 Candidate**
```plain text
评价 Feeding Channel：
    使用当前 Group 的 Feeding Profile

评价 Reaction Channel：
    使用当前 Group 的 Reaction Profile

按模板固定规则 MAX(Feeding, Reaction)
返回最终 Response
```
两者差异主要在 Profile：
```plain text
Cold-Slow：
    高持续追逐要求强烈不利
    慢 / 停顿 / 贴近相对有利
    短时高显著度刺激仍可触发

SummerStress：
    普通 Feeding Readiness 较低
    近距离 flash / vibration / erratic / deflection 等 Reaction 更重要
    同样不鼓励高持续追逐成本
```
**第一轮读数：** `5 Groups → 3 Response topology candidates`。这说明不同 FishGroup 可以共用 Response LogicTemplate，当前没有理由一 Group 一模板。
---
### 6.4 Quality Selection｜暂时仍是一套统一模板
#### A｜配置投影
<table fit-page-width="true" header-row="true">
<tr>
<td>Group</td>
<td>基础品质 Profile</td>
<td>后续 Modifier</td>
</tr>
<tr>
<td>NormalFeeding</td>
<td>`@BassNormalBaseQuality`</td>
<td>钩 / 饵 / 时段 / 环境 Modifier</td>
</tr>
<tr>
<td>Guarding</td>
<td>`@BassGuardBaseQuality` 或 Species 默认</td>
<td>同上；是否真需单独 Profile 待证</td>
</tr>
<tr>
<td>Cold-Slow</td>
<td>`@BassColdBaseQuality` 或 Species 默认</td>
<td>只有真实体型差异证据才覆盖</td>
</tr>
<tr>
<td>SummerStress</td>
<td>`@BassSummerStressBaseQuality` 或 Species 默认</td>
<td>只有真实体型差异证据才覆盖</td>
</tr>
<tr>
<td>ForageChase</td>
<td>`@ForageChaseBaseQualityProfile`</td>
<td>钩 / 饵等并列 Modifier</td>
</tr>
</table>
当前统一求值语义 Candidate：
```plain text
读取当前 FishGroup 的 BaseQualityProfile

评价所有 Quality Rule
每条 Rule 只读取原始输入事实
产生并列 Quality Modifier

合并 Modifier
统一归一化
抽具体 Quality
```
#### B｜中文逻辑
```plain text
读取 当前 FishGroup
选择该 Group 的基础品质分布

如果 大钩 + 大饵条件成立：
    产生 @BigGearModifier

如果 当前时段存在成年个体低活性条件：
    产生 @AdultInactiveModifier

如果还有其它品质条件：
    分别产生并列 Modifier

将所有 Modifier 一次性作用于基础品质分布
统一归一化
抽具体品质
```
ForageChase 的体型差异优先通过 `@ForageChaseBaseQualityProfile` 表达，不要求 Quality 先于 Group Routing 执行。
**第一轮读数：** 目前仍未出现“Rule B 必须读取 Rule A 修改后的中间品质结果”的真实需求，因此 Quality Sequential DSL 仍没有被证明需要。
---
### 6.5 Cold Front / High Pressure｜Overlay 压力测试
当前禁止增加：
```plain text
ColdFrontGroup
PressuredGroup
Normal_PostFront
ForageChase_PostFront
...
```
冷锋可以改变：
```plain text
Bake：CoverTightnessBias / DepthShiftBias
Response：FeedingReadiness / PursuitTolerance / Presentation acceptance
```
高钓压可以改变：
```plain text
Response：AnglingPressure / CueFamiliarity
```
但都不改变五个 Group 的基本行为身份。
### 6.6 本次 Bass Snapshot 对 Representation 的阶段性含义
```plain text
Group Routing：
    1 套 RuleSet + Share Vector 结构目前可覆盖 5 Group
    → Config 很有竞争力

Bake：
    至少出现 5 个明显不同的语义 Program
    → 当前最强 DSL / Program 化压力
    → 后续需做真实 Runtime Order clustering，不能只看名字数模板

Response：
    5 Group 暂压成 3 个拓扑 Candidate
    → LogicTemplate + Profile 很有竞争力

Quality：
    1 套 BaseProfile + Parallel Modifier 结构仍可覆盖
    → Config 很有竞争力
```
这比“整个系统表 vs DSL”更具体：
> **当前真正需要重点证明 DSL 价值的仍然是 Bake；Group Routing / Response / Quality 暂时都没有逼出同等强度的顺序编程需求。**
## 7. Cold Front Spatial Overlay｜配置 vs 中文脚本
这不是第六个 FishGroup Case，而是专门验证：**一个会改变空间分布、但不改变行为身份的天气事件，Authoring 应该怎么表达。**
### 7.1 当前语义
```plain text
当前 FishGroup 不变
→ 先得到该 Group 的 BaseSpatialFit
→ 再读取 PostFrontSeverity
→ 在 Cover Refuge / Depth Retreat 两条空间避难通路中求当前更合适的一条
→ 按冷锋强度把 BaseSpatialFit 向 PostFrontRefugeFit 偏移
```
上游先假定已经提供：
```plain text
PostFrontSeverity
Target.CoverRefugeScore / CoverProximity
Target.AdjacentDeepAccess / DepthBreakProximity
```
本页不研究这些输入如何由天气史或地图几何计算出来。
### 7.2 如果用配置表达
**固定模板槽位：**
<table fit-page-width="true" header-row="true">
<tr>
<td>配置项</td>
<td>值</td>
<td>语义</td>
</tr>
<tr>
<td>Dynamic Spatial Overlay</td>
<td>ColdFrontRefuge</td>
<td>天气事件空间修正槽</td>
</tr>
<tr>
<td>Cover Refuge Profile</td>
<td>@PostFrontCoverRefugeProfile</td>
<td>越贴有效 Cover，锋后相对越有利</td>
</tr>
<tr>
<td>Depth Retreat Profile</td>
<td>@PostFrontDepthRetreatProfile</td>
<td>越靠邻近深水 / Depth Break，锋后相对越有利</td>
</tr>
<tr>
<td>Refuge Combine</td>
<td>MAX</td>
<td>两条 refuge 当前按替代通路处理</td>
</tr>
<tr>
<td>Overlay Blend</td>
<td>BLEND_BY_SEVERITY</td>
<td>按 PostFrontSeverity 从常态向 refuge 分布过渡</td>
</tr>
</table>
**实例绑定示意：**
<table fit-page-width="true" header-row="true">
<tr>
<td>FishGroup</td>
<td>启用</td>
<td>Overlay Ref</td>
<td>备注</td>
</tr>
<tr>
<td>Normal Feeding</td>
<td>ON</td>
<td>@BassPostFrontRefuge</td>
<td>普通锋后空间收缩</td>
</tr>
<tr>
<td>Guarding</td>
<td>LOW / OFF candidate</td>
<td>@BassGuardPostFront</td>
<td>避免天气覆盖巢区忠诚</td>
</tr>
<tr>
<td>Cold-Slow</td>
<td>OFF / LOW candidate</td>
<td>—</td>
<td>避免和严寒 refuge Program 重复</td>
</tr>
<tr>
<td>SummerStress</td>
<td>OPEN</td>
<td>@BassSummerPostFront</td>
<td>需检查是否重复计算 refuge</td>
</tr>
<tr>
<td>ForageChase</td>
<td>ON candidate</td>
<td>@BassForagePostFront</td>
<td>身份仍是 ForageChase，只改变空间位置</td>
</tr>
</table>
### 7.3 同样语义的中文脚本
```plain text
先执行 当前 FishGroup 的原始烘焙逻辑
得到 BaseSpatialFit

读取 锋后强度 PostFrontSeverity

如果 锋后强度很低：
    返回 BaseSpatialFit

读取 当前空间目标的 Cover Refuge 程度
使用 @PostFrontCoverRefugeProfile
得到 CoverRefugeFit

读取 当前空间目标到邻近深水 / Depth Break 的可达程度
使用 @PostFrontDepthRetreatProfile
得到 DepthRetreatFit

在两条锋后避难通路中
选择当前更合适的一条：
    PostFrontRefugeFit = MAX(CoverRefugeFit, DepthRetreatFit)

按照锋后强度
把 BaseSpatialFit 向 PostFrontRefugeFit 偏移
得到 FinalSpatialFit

返回 FinalSpatialFit
```
### 7.4 这对 Representation 的新证据
这条 Case 很重要，因为它说明“动态空间变化”不只有两种极端：
```plain text
不是：
    只改一个 scalar 参数

也不是：
    必须新建 FishGroup / 新建完整 Bake Program

而可以是：
    固定的 Dynamic Spatial Overlay Slot
    + Profiles
    + 固定 Combine / Blend
```
当前 Config 仍然能清楚表达这一结构；中文 DSL 更容易读出因果链，但没有出现 author-editable `Next / Jump / arbitrary branch`。
因此该 Case **不新增 Sequential DSL 证据**，但会增加一个新的 Authoring 类别：
```plain text
Reusable Dynamic Spatial Overlay
```
如果后续大量天气 / 短期事件都需要不同 Overlay topology，才重新评估是否把 Overlay 本身升级成独立 Narrow DSL。
</content>
</page>
