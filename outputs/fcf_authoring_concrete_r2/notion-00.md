## 25. Concrete Authoring Specimens R2｜全表列、样例行与等义中文脚本

**状态：WORKING / PRE-GATE / 演示数据；未 Promote，未选择最终 Config Table 或 DSL。**

这份附录把表达写到可填写、可复算的程度：同一输入在表格方案中对应哪些行，在中文伪脚本中执行哪些步骤，得到哪些中间值与类型化输出。完整覆盖 C01–C15 的范围处理，并补入 G1–G3、Q1–Q3 和最新鲈鱼五群样本。文中所有阈值、曲线、乘数、分档、MAX/BLEND 的具体演示使用均是可替换的样本选择，不是新增机制 Authority。

### 25.1. 本轮来源与边界

Source Map：Router → Project Current → Branch Index → Simplified V0 Working Main 做最小 Rebase；最新 Representation Design Gate R1 和鲈鱼深挖尾部 Working snapshot 处理过期未决；原 C01–C15 Mapping 保留鱼类故事边界。Existing Base Check：旧15例页面已有矩阵/伪代码，但尚不足以还原完整配置；本附录保留旧投影，以新行表补齐。Gap Classification：表列/行/中间计算属于 DOCUMENTATION GAP；曲线数值与候选聚合的最终标定属于 DEFERRED / NON-BLOCKING；生产空间顺序、C13 可玩范围仍未替 Owner 决定。

核心输入：<mention-page url="https://app.notion.com/p/3d6a4137d23681eab6cfd3a535a8938a"/>、<mention-page url="https://app.notion.com/p/3d6a4137d236814ea872ed6305942594"/>、<mention-page url="https://app.notion.com/p/3d6a4137d2368151b762e50bc5ce6dfd"/>、<mention-page url="https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3"/>、<mention-page url="https://app.notion.com/p/3d6a4137d23681e2af96e873eef9411a"/>。这些 Working 输入没有自动提升为 Current。

本稿骨架已经落实为：共用语义 → 具体表 Schema → 每例样例行及中文脚本 → 输入/中间值/输出 → 相同修改操作 → 验证与边界。旧文的 C08/C09–C12 结构“等待 Owner”标记以最新 Gate 为准；旧独立审核不覆盖本附录。

### 25.2. 一屏模型：作者到底填什么

慢速世界快照 → GroupShare（同物种组成） → 已分配 FishGroup → Bake（空间权重）。既有 PresentationSession → 合法 semantic particle → Root Semantic Occurrence → OpportunityId → Evaluation Scope → 群专属 Response。Quality 使用已经选定的 Group 基准分布，读原始 facts 并列修正，归一化后交既有抽样 Owner。以上箭头表示合同依赖，不是本附录新造的完整抽签顺序。

表格作者选择固定模板、填 Profile/参数、连接 Predicate 树、填写结果行；模板内部代码是共享工程成本。中文脚本作者仍引用同一份数值表，把条件与因果关系连续写出来；本稿把每个模板实际展开，不能只用“执行某 Profile”隐藏逻辑。

ResponseStrength 是本演示的类型化归一强度标量，不等于最终中鱼概率；SpatialDistributionWeight 是空间适宜性输出，不改 Species 总量；FishGroupShareVector 仅描述物种内组成；QualityDistribution 仅是归一化分布。到生产 Typed Result 的字段映射须跟随现有合同，本文这些短字段名不是宣告新增正式 API。

### 25.3. 两种方案的完整物理布局

方案 A 有 **11 张作者数据表 + 1 张只读 TemplateStep 目录**。方案 B 有 **5 张共用数据表（Binding、Parameter、CurvePoint、QualityWeight、Boundary）+ 1 份 Script 文本集合**。B 把 Slot/Predicate/Member/ResponseBand/GroupShare/QualityModifier 的内容写入正文；没有消灭其逻辑与校验成本。其 Script 记录为 `binding_id, dialect_version, source`，一绑定一记录；这里 `dialect_version=CN_PSEUDO_R2`，不是已经实现的生产 DSL 编译器。两边都需模板/运行时实现，表数不是复杂度结论。

配置只接受下文列出的模板槽、算子、字段和输出；无任意循环、跳转、写世界状态或 RNG。DSL 中 `返回` 会终止该绑定；固定双通道均评价再聚合；配置 Predicate 子项换行/换序不构成新模板。修改 TemplateStep 的有语义 Gate/依赖关系是模板改动，不是调一个 Profile 或 Switch。

所有样例输入是本次快照的只读别名：slow.* 来自水体/时令 Resolver；target.* 来自空间目标 Resolver；weather.* 来自天气 Resolver；food.* 来自本 Opportunity 可用的 FoodField facts；response.* 来自既有 Scope 的鱼种/呈现匹配与刺激事实；gear.* 来自同一 Active Presentation Channel；quality_context.* 来自品质评价快照。连续 index 为[0,1]，距离m、深度m、温度°C、溶氧mg/L、光照lux，日期为1–366日，hook_size_index 是演示有序尺码。`target.cover_prey_tradeoff` 等复合量是演示输入适配别名，不能由本稿反推 Resolver 算法已经实现。输入不存在/非有限/单位错时返回 ValidationError；它不等于机制的“条件不满足”。没有隐式0、空字符串默认或二次随机。

公共曲线查询：节点 (x0,y0),(x1,y1) 间 `y=y0+(y1-y0)*(x-x0)/(x1-x0)`；范围外取端点。示例 Structure(0,1),(100,0.2)，距离25m得到0.8。表格与脚本使用同一曲线，不在脚本里偷偷增加自由算式。
