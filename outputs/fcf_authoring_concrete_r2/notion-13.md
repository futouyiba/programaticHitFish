### R2-A / TemplateStep
PK(template_id,step)；是方案A须明确给工程/作者看的只读模板目录，不是普通配置表。operation/input/output/failure 展开固定因果；修改执行拓扑须创建/修改模板，经现有机制治理，不能让 Switch 偷改顺序。
<table header-row="true" fit-page-width="true">
<tr><td>template_id</td><td>step</td><td>operation</td><td>input</td><td>output</td><td>failure</td></tr>
<tr><td>S_FIXED</td><td>1</td><td>查分段线性曲线</td><td>target.temperature_c × @Temperature</td><td>T</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FIXED</td><td>2</td><td>按具名锚点读取距离，再查曲线</td><td>target.anchor_distances_m[@Anchor] × @Structure</td><td>S</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FIXED</td><td>3</td><td>查分段线性曲线</td><td>target.depth_m × @Depth</td><td>D</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FIXED</td><td>4</td><td>固定 Light Slot：关=1；开=查曲线</td><td>target.illuminance_lux × @Light</td><td>L</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FIXED</td><td>5</td><td>独立因子乘积</td><td>T × S × D × L</td><td>BaseSpatialFit</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FIXED</td><td>6</td><td>固定末端 Overlay：关=原值；开=BLEND(base,MAX(cover,deep),severity)</td><td>BaseSpatialFit / @Cover / @Deep / weather.cold_front_severity</td><td>SpatialDistributionWeight</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_BANDS</td><td>1</td><td>只读同一 Opportunity Evaluation Scope</td><td>FeedingMatch / Presentation facts</td><td>facts</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_BANDS</td><td>2</td><td>按显式 priority 递增测试条件；FIRST_MATCH</td><td>ResponseBand + Predicate</td><td>第一条命中行</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_BANDS</td><td>3</td><td>SET；无命中使用固定 Default Slot</td><td>response_strength 或 @Default</td><td>ResponseStrength</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_DEFENSE</td><td>1</td><td>只读已准入的入侵强度</td><td>response.intrusion_strength</td><td>intrusion</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_DEFENSE</td><td>2</td><td>查 Defense 曲线</td><td>intrusion × @Defense</td><td>ResponseStrength；立即返回</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_DUAL_FIXED</td><td>1</td><td>从同一快照评价固定 Grazing Slot</td><td>food.grazing_availability × @Grazing</td><td>G</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_DUAL_FIXED</td><td>2</td><td>从同一快照评价固定 Suspended Slot</td><td>food.suspended_availability × @Suspended</td><td>S</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_DUAL_FIXED</td><td>3</td><td>固定聚合 MAX（本样本的演示函数）</td><td>G,S</td><td>ResponseStrength</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FIELD</td><td>1</td><td>使用已有 Session/Root/Opportunity/Scope；本模板不生成身份</td><td>同一 semantic particle 已准入 Scope</td><td>只读 facts</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FIELD</td><td>2</td><td>查 FoodField 的量级和适宜性</td><td>food.density_index × @Density；food.suitability × @Suitability</td><td>DensityFit, SuitFit</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FIELD</td><td>3</td><td>读取同一 Active Presentation Channel 的 FeedingMatch</td><td>response.feeding_match × @Match</td><td>PresentationFit</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FIELD</td><td>4</td><td>乘积（演示函数）；不把帧数当次数</td><td>DensityFit × SuitFit × PresentationFit</td><td>ResponseStrength</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FEED</td><td>1</td><td>查匹配曲线</td><td>response.feeding_match × @Match</td><td>F</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FEED</td><td>2</td><td>查呈现曲线</td><td>response.presentation_fit × @Presentation</td><td>P</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FEED</td><td>3</td><td>固定只读 Familiarity Slot：关闭=1；开启=查曲线</td><td>response.cue_familiarity × @Familiarity</td><td>U</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FEED</td><td>4</td><td>相乘</td><td>F × P × U</td><td>ResponseStrength</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_REACTION</td><td>1</td><td>普通 Feeding 没有 Slot：分群已在上游完成</td><td>Migration FishGroup</td><td>只读刺激/追逐要求</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_REACTION</td><td>2</td><td>查刺激显著性与持续追逐容忍曲线</td><td>response.trigger_salience × @Salience；response.sustained_pursuit_demand × @Pursuit</td><td>R,D</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_REACTION</td><td>3</td><td>相乘；类型为 Response，不携带已证实动机</td><td>R × D</td><td>ResponseStrength</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FEED_REACTION</td><td>1</td><td>同一 Scope 评价 Feeding</td><td>response.feeding_match × @Match；response.presentation_fit × @Presentation</td><td>F=两 Fit 乘积</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FEED_REACTION</td><td>2</td><td>同一 Scope 评价 Reaction</td><td>response.trigger_salience × @Salience；response.sustained_pursuit_demand × @Pursuit</td><td>R=两 Fit 乘积</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>R_FEED_REACTION</td><td>3</td><td>固定聚合 MAX（Working Candidate 的演示实例）</td><td>F,R</td><td>ResponseStrength</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>G_SHARES</td><td>1</td><td>读取同一物种的同一慢速世界快照</td><td>GroupShare + Predicate</td><td>各 special predicate</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>G_SHARES</td><td>2</td><td>并列评价：不命中=0；命中=标量或曲线</td><td>share_ref / input_field</td><td>special shares</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>G_SHARES</td><td>3</td><td>验证每项[0,1]且和≤1</td><td>special shares</td><td>有效 share vector</td><td>超限 → ValidationError；不归一化、不顺序扣减</td></tr>
<tr><td>G_SHARES</td><td>4</td><td>补 Normal residual</td><td>1 − SUM(special)</td><td>FishGroupShareVector</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>Q_PARALLEL</td><td>1</td><td>取已经选定的 Group 对应基准分布</td><td>QualityWeight</td><td>base[bucket]</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>Q_PARALLEL</td><td>2</td><td>所有条件只读同一原始 facts</td><td>QualityModifier + Predicate</td><td>并列命中 modifier</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>Q_PARALLEL</td><td>3</td><td>每桶原始权重乘所有命中乘数</td><td>base[b] × PRODUCT(multipliers[b])</td><td>raw[b]</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>Q_PARALLEL</td><td>4</td><td>一次归一化</td><td>raw / SUM(raw)</td><td>QualityDistribution</td><td>负数/非有限/总和≤0 → ValidationError；本模板不抽签</td></tr>
<tr><td>S_COLD</td><td>1</td><td>查相对温暖、稳定、低能耗避难所</td><td>target.relative_warmth × @Warmth；target.stability × @Stability；target.low_energy_refuge × @Refuge</td><td>W,S,R</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_COLD</td><td>2</td><td>固定乘积</td><td>W × S × R</td><td>SpatialDistributionWeight</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_SUMMER</td><td>1</td><td>目标溶氧硬 Gate</td><td>target.oxygen_mg_l ≥ @OxygenMin</td><td>通过目标</td><td>不通过 → 空间权重0并立即返回；不执行后续适宜性</td></tr>
<tr><td>S_SUMMER</td><td>2</td><td>查相对降温、氧余量、遮蔽/猎物折中</td><td>target.relative_cooling × @Cooling；target.oxygen_margin × @Oxygen；target.cover_prey_tradeoff × @Tradeoff</td><td>C,O,T</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_SUMMER</td><td>3</td><td>固定乘积</td><td>C × O × T</td><td>SpatialDistributionWeight</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FORAGE</td><td>1</td><td>猎物场准入 Gate</td><td>target.forage_school_intensity ≥ @ForageMin</td><td>通过目标</td><td>不通过 → 空间权重0并立即返回；Overlay不得复活</td></tr>
<tr><td>S_FORAGE</td><td>2</td><td>猎物主锚点及垂向匹配</td><td>target.forage_school_intensity × @Forage；target.vertical_alignment × @Vertical</td><td>F,V</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FORAGE</td><td>3</td><td>温度、氧、开放水环境适宜性</td><td>target.temperature_c × @Temperature；target.oxygen_mg_l × @Oxygen；target.open_water_context × @OpenWater</td><td>T,O,W</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FORAGE</td><td>4</td><td>固定乘积</td><td>F × V × T × O × W</td><td>BaseSpatialFit</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
<tr><td>S_FORAGE</td><td>5</td><td>固定末端 ColdFront Overlay；关=原值</td><td>base / Cover / Deep / severity</td><td>SpatialDistributionWeight</td><td>输入缺失/类型错 → ValidationError；不抽签、不写状态</td></tr>
</table>
