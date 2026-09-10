from pathlib import Path
import csv, json, html, math, hashlib

ROOT=Path(__file__).resolve().parent
TABLES={
 'Binding':['binding_id','surface','subject','template_id','status'],
 'Slot':['binding_id','slot','enabled','ref_kind','ref_id'],
 'Parameter':['parameter_id','type','value','unit'],
 'CurvePoint':['profile_id','x','y'],
 'Predicate':['node_id','kind','field','operator','parameter_id'],
 'PredicateMember':['parent_id','display_index','child_id'],
 'ResponseBand':['binding_id','priority','predicate_id','response_strength'],
 'GroupShare':['binding_id','group','predicate_id','share_kind','share_ref','input_field'],
 'QualityWeight':['binding_id','bucket','base_weight'],
 'QualityModifier':['binding_id','rule_id','predicate_id','bucket','multiplier'],
 'Boundary':['case_id','scope','reason'],
 'TemplateStep':['template_id','step','operation','input','output','failure'],
}
data={k:[] for k in TABLES}
cases=[]; templates={}; traces=[]; assertions=[]
def row(table,*values):
 assert len(values)==len(TABLES[table]),(table,values)
 d=dict(zip(TABLES[table],values)); data[table].append(d); return d
def param(key,value,unit='1'):
 typ='bool' if isinstance(value,bool) else 'number' if isinstance(value,(int,float)) else 'set<string>' if isinstance(value,list) else 'string'
 row('Parameter',key,typ,value,unit); return key
def curve(key,points):
 for x,y in points: row('CurvePoint',key,x,y)
 return key
def atom(key,field,op,value,unit='1'):
 p=param(key+'_value',value,unit);row('Predicate',key,'ATOM',field,op,p);return key
def group(key,kind,*children):
 row('Predicate',key,kind,'N/A','N/A','N/A')
 for i,c in enumerate(children):row('PredicateMember',key,i+1,c)
 return key
def add_template(key,surface,steps,slots,script):
 templates[key]={'surface':surface,'slots':slots,'script':script}
 for i,(op,inp,out,fail) in enumerate(steps):row('TemplateStep',key,i+1,op,inp,out,fail)
def binding(key,surface,subject,tpl,status='DEMO_WORKING'):
 row('Binding',key,surface,subject,tpl,status)
def slot(key,name,ref,enabled=True,kind='PROFILE'):row('Slot',key,name,enabled,kind,ref)
def cp(b,name,points):
 p=curve(b+'_'+name,points);slot(b,name,p);return p
def pv(b,name,value,unit='1'):
 p=param(b+'_'+name,value,unit);slot(b,name,p,True,'PARAMETER');return p
def specs(*names):return list(names)
def step(op,inp,out,fail='输入缺失/类型错 → ValidationError；不抽签、不写状态'):return op,inp,out,fail

add_template('S_FIXED','BAKE',[
 step('查分段线性曲线','target.temperature_c × @Temperature','T'),
 step('按具名锚点读取距离，再查曲线','target.anchor_distances_m[@Anchor] × @Structure','S'),
 step('查分段线性曲线','target.depth_m × @Depth','D'),
 step('固定 Light Slot：关=1；开=查曲线','target.illuminance_lux × @Light','L'),
 step('独立因子乘积','T × S × D × L','BaseSpatialFit'),
 step('固定末端 Overlay：关=原值；开=BLEND(base,MAX(cover,deep),severity)','BaseSpatialFit / @Cover / @Deep / weather.cold_front_severity','SpatialDistributionWeight')
],specs('Temperature','Anchor','Structure','Depth','Light?','ColdFront?','Cover?','Deep?'),
'''T = 查曲线(@Temperature, target.temperature_c)
AnchorDistance = target.anchor_distances_m[@Anchor]
S = 查曲线(@Structure, AnchorDistance)
D = 查曲线(@Depth, target.depth_m)
L = 若 Light 开启 则 查曲线(@Light, target.illuminance_lux) 否则 1
Base = T × S × D × L
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(@Cover, target.cover_distance_m)
Deep = 查曲线(@Deep, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)''')
add_template('R_BANDS','RESPONSE',[
 step('只读同一 Opportunity Evaluation Scope','FeedingMatch / Presentation facts','facts'),
 step('按显式 priority 递增测试条件；FIRST_MATCH','ResponseBand + Predicate','第一条命中行'),
 step('SET；无命中使用固定 Default Slot','response_strength 或 @Default','ResponseStrength')
],specs('Default'),'''读取 本次 Scope 的只读 facts
按以下 priority 顺序，第一条满足就返回 指定响应强度
{bands}
否则 返回 响应强度(@Default)''')
add_template('R_DEFENSE','RESPONSE',[
 step('只读已准入的入侵强度','response.intrusion_strength','intrusion'),
 step('查 Defense 曲线','intrusion × @Defense','ResponseStrength；立即返回')
],specs('Defense'),'''Defense = 查曲线(@Defense, response.intrusion_strength)
返回 响应强度(Defense)
// 此模板没有普通 Feeding Slot，也没有 Defense/Feeding 优先级。''')
add_template('R_DUAL_FIXED','RESPONSE',[
 step('从同一快照评价固定 Grazing Slot','food.grazing_availability × @Grazing','G'),
 step('从同一快照评价固定 Suspended Slot','food.suspended_availability × @Suspended','S'),
 step('固定聚合 MAX（本样本的演示函数）','G,S','ResponseStrength')
],specs('Grazing','Suspended'),'''G = 查曲线(@Grazing, food.grazing_availability)
S = 查曲线(@Suspended, food.suspended_availability)
返回 响应强度(MAX(G, S))
// G、S 总是都算。没有按资源条件 SELECT Profile。''')
add_template('R_FIELD','RESPONSE',[
 step('使用已有 Session/Root/Opportunity/Scope；本模板不生成身份','同一 semantic particle 已准入 Scope','只读 facts'),
 step('查 FoodField 的量级和适宜性','food.density_index × @Density；food.suitability × @Suitability','DensityFit, SuitFit'),
 step('读取同一 Active Presentation Channel 的 FeedingMatch','response.feeding_match × @Match','PresentationFit'),
 step('乘积（演示函数）；不把帧数当次数','DensityFit × SuitFit × PresentationFit','ResponseStrength')
],specs('Density','Suitability','Match'),'''// 外层已有 Opportunity；此处不创建 FieldOpportunity 或计时器。
D = 查曲线(@Density, food.density_index)
S = 查曲线(@Suitability, food.suitability)
M = 查曲线(@Match, response.feeding_match)
返回 响应强度(D × S × M)
// M 来自同一 Session / Active Presentation Channel，不从“有食物”推导钩饵可接受。''')
add_template('R_FEED','RESPONSE',[
 step('查匹配曲线','response.feeding_match × @Match','F'),
 step('查呈现曲线','response.presentation_fit × @Presentation','P'),
 step('固定只读 Familiarity Slot：关闭=1；开启=查曲线','response.cue_familiarity × @Familiarity','U'),
 step('相乘','F × P × U','ResponseStrength')
],specs('Match','Presentation','Familiarity?'),'''F = 查曲线(@Match, response.feeding_match)
P = 查曲线(@Presentation, response.presentation_fit)
U = 若 Familiarity 开启 则 查曲线(@Familiarity, response.cue_familiarity) 否则 1
返回 响应强度(F × P × U)
// Familiarity 是只读 Overlay；此处没有压力/记忆写回。''')
add_template('R_REACTION','RESPONSE',[
 step('普通 Feeding 没有 Slot：分群已在上游完成','Migration FishGroup','只读刺激/追逐要求'),
 step('查刺激显著性与持续追逐容忍曲线','response.trigger_salience × @Salience；response.sustained_pursuit_demand × @Pursuit','R,D'),
 step('相乘；类型为 Response，不携带已证实动机','R × D','ResponseStrength')
],specs('Salience','Pursuit'),'''R = 查曲线(@Salience, response.trigger_salience)
D = 查曲线(@Pursuit, response.sustained_pursuit_demand)
返回 响应强度(R × D)
// 上游 Migration 分群；普通 Feeding 关闭。不读取 Runtime Stage Predicate。''')
add_template('R_FEED_REACTION','RESPONSE',[
 step('同一 Scope 评价 Feeding','response.feeding_match × @Match；response.presentation_fit × @Presentation','F=两 Fit 乘积'),
 step('同一 Scope 评价 Reaction','response.trigger_salience × @Salience；response.sustained_pursuit_demand × @Pursuit','R=两 Fit 乘积'),
 step('固定聚合 MAX（Working Candidate 的演示实例）','F,R','ResponseStrength')
],specs('Match','Presentation','Salience','Pursuit'),'''F = 查曲线(@Match, response.feeding_match) × 查曲线(@Presentation, response.presentation_fit)
R = 查曲线(@Salience, response.trigger_salience) × 查曲线(@Pursuit, response.sustained_pursuit_demand)
返回 响应强度(MAX(F, R))
// 两通道均评价；强短刺激与持续高速追逐是两个独立输入。''')
add_template('G_SHARES','GROUP',[
 step('读取同一物种的同一慢速世界快照','GroupShare + Predicate','各 special predicate'),
 step('并列评价：不命中=0；命中=标量或曲线','share_ref / input_field','special shares'),
 step('验证每项[0,1]且和≤1','special shares','有效 share vector','超限 → ValidationError；不归一化、不顺序扣减'),
 step('补 Normal residual','1 − SUM(special)','FishGroupShareVector')
],[],'''读取 同一份 slow_snapshot
{shares}
验证 所有 Share ∈ [0,1] 且 SUM(特殊 Share) ≤ 1，否则 ValidationError
Normal = 1 - SUM(特殊 Share)
返回 群体组成(所有特殊 Share, Normal)
// 输出在已选物种内的组成，不是咬口概率；不在此执行抽签。''')
add_template('Q_PARALLEL','QUALITY',[
 step('取已经选定的 Group 对应基准分布','QualityWeight','base[bucket]'),
 step('所有条件只读同一原始 facts','QualityModifier + Predicate','并列命中 modifier'),
 step('每桶原始权重乘所有命中乘数','base[b] × PRODUCT(multipliers[b])','raw[b]'),
 step('一次归一化','raw / SUM(raw)','QualityDistribution','负数/非有限/总和≤0 → ValidationError；本模板不抽签')
],[],'''Base = 当前 Group 的 QualityWeight
{modifiers}
对每个有限枚举桶：Raw[桶] = Base[桶] × 所有命中 Modifier 在该桶的乘数
若 SUM(Raw) ≤ 0：ValidationError
返回 品质分布(Raw / SUM(Raw))
// Modifier 不读取修改后的分布；固定桶展开不构成任意循环 DSL；后续抽签由既有 Owner 执行。''')
add_template('S_COLD','BAKE',[
 step('查相对温暖、稳定、低能耗避难所','target.relative_warmth × @Warmth；target.stability × @Stability；target.low_energy_refuge × @Refuge','W,S,R'),
 step('固定乘积','W × S × R','SpatialDistributionWeight')
],specs('Warmth','Stability','Refuge'),'''W = 查曲线(@Warmth, target.relative_warmth)
S = 查曲线(@Stability, target.stability)
R = 查曲线(@Refuge, target.low_energy_refuge)
返回 空间权重(W × S × R)''')
add_template('S_SUMMER','BAKE',[
 step('目标溶氧硬 Gate','target.oxygen_mg_l ≥ @OxygenMin','通过目标','不通过 → 空间权重0并立即返回；不执行后续适宜性'),
 step('查相对降温、氧余量、遮蔽/猎物折中','target.relative_cooling × @Cooling；target.oxygen_margin × @Oxygen；target.cover_prey_tradeoff × @Tradeoff','C,O,T'),
 step('固定乘积','C × O × T','SpatialDistributionWeight')
],specs('OxygenMin','Cooling','Oxygen','Tradeoff'),'''若 target.oxygen_mg_l < @OxygenMin：返回 空间权重(0)
C = 查曲线(@Cooling, target.relative_cooling)
O = 查曲线(@Oxygen, target.oxygen_margin)
T = 查曲线(@Tradeoff, target.cover_prey_tradeoff)
返回 空间权重(C × O × T)''')
add_template('S_FORAGE','BAKE',[
 step('猎物场准入 Gate','target.forage_school_intensity ≥ @ForageMin','通过目标','不通过 → 空间权重0并立即返回；Overlay不得复活'),
 step('猎物主锚点及垂向匹配','target.forage_school_intensity × @Forage；target.vertical_alignment × @Vertical','F,V'),
 step('温度、氧、开放水环境适宜性','target.temperature_c × @Temperature；target.oxygen_mg_l × @Oxygen；target.open_water_context × @OpenWater','T,O,W'),
 step('固定乘积','F × V × T × O × W','BaseSpatialFit'),
 step('固定末端 ColdFront Overlay；关=原值','base / Cover / Deep / severity','SpatialDistributionWeight')
],specs('ForageMin','Forage','Vertical','Temperature','Oxygen','OpenWater','ColdFront?','Cover?','Deep?'),'''若 target.forage_school_intensity < @ForageMin：返回 空间权重(0)
F = 查曲线(@Forage, target.forage_school_intensity)
V = 查曲线(@Vertical, target.vertical_alignment)
T = 查曲线(@Temperature, target.temperature_c)
O = 查曲线(@Oxygen, target.oxygen_mg_l)
W = 查曲线(@OpenWater, target.open_water_context)
Base = F × V × T × O × W
若 ColdFront 关闭：返回 空间权重(Base)
Cover = 查曲线(@Cover, target.cover_distance_m)
Deep = 查曲线(@Deep, target.adjacent_deep_access)
Refuge = MAX(Cover, Deep)
返回 空间权重((1-weather.cold_front_severity) × Base + weather.cold_front_severity × Refuge)''')

def case(cid,title,ids,facts,note):
 cases.append({'id':cid,'title':title,'bindings':ids,'facts':facts,'note':note})
def spatial(b,subject,temp,structure,depth,light=None,anchor='stable_cover'):
 binding(b,'BAKE',subject,'S_FIXED');cp(b,'Temperature',temp);pv(b,'Anchor',anchor,'category');cp(b,'Structure',structure);cp(b,'Depth',depth)
 if light:cp(b,'Light',light)
 else:slot(b,'Light','N/A',False)
 slot(b,'ColdFront','N/A',False,'SWITCH');slot(b,'Cover','N/A',False);slot(b,'Deep','N/A',False)
IDENT=[(0,0),(1,1)]
spatial('C01_B','AtlanticCod.Normal',[(0,.2),(10,1),(20,.2)],[(0,1),(100,.2)],[(0,.1),(20,1),(60,.3)])
case('C01','大西洋鳕：普通觅食空间',['C01_B'],{'target.temperature_c':10,'target.anchor_distances_m':{'stable_cover':25},'target.depth_m':20},'T→S→D 是填满样本所选的演示顺序；Owner 的生产空间顺序未冻结。三个独立乘因子交换顺序不改变结果。')
spatial('C02_B','ChannelCatfish.Normal',[(5,.2),(25,1),(35,.3)],[(0,1),(100,.4)],[(0,.2),(3,1),(15,.3)])
case('C02','斑点叉尾鮰：近底空间',['C02_B'],{'target.temperature_c':25,'target.anchor_distances_m':{'stable_cover':50},'target.depth_m':3},'普通近底觅食样本；气味留在 Exposure Owner，本表不再扣一次 Feeding。生产空间顺序未冻结。')
spatial('C05_B','Walleye.Normal',[(0,.2),(15,1),(30,.1)],[(0,1),(100,.2)],[(0,.2),(8,1),(25,.4)],[(0,1),(100,.8),(1000,.2)])
case('C05','玻璃梭鲈：低光空间',['C05_B'],{'target.temperature_c':15,'target.anchor_distances_m':{'stable_cover':0},'target.depth_m':8,'target.illuminance_lux':100},'Light 是 S_FIXED 预定义 Slot；本例开启。没有新建昼夜 Runtime Mode，生产空间顺序未冻结。')
for cid,species in [('C03','RainbowTrout'),('C04','BrownTrout')]:
 b=cid+'_R';binding(b,'RESPONSE',species+'.Normal','R_BANDS');pv(b,'Default',0)
 a=atom(cid+'_good_match','response.feeding_match','GE',.7)
 if cid=='C03':
  d=atom('C03_drift','response.natural_drift_fit','GE',.6);p=group('C03_high','ALL',a,d)
 else:p=a
 low=atom(cid+'_some_match','response.feeding_match','GE',.3)
 row('ResponseBand',b,10,p,.8);row('ResponseBand',b,20,low,.25)
 case(cid,'虹鳟：自然漂流匹配' if cid=='C03' else '褐鳟：普通摄食响应',[b],{'response.feeding_match':.8,**({'response.natural_drift_fit':.7} if cid=='C03' else {})},'明确 FIRST_MATCH + 默认0；结果只到 ResponseStrength，不创建 Follow/Track/Attack 状态或后生成追击。')
for cid,subject,points in [('C06','Bluegill.Guarding',[(0,0),(.5,.6),(1,.9)]),('C07','Smallmouth.Parental',[(0,0),(.5,.7),(1,1)])]:
 b=cid+'_R';binding(b,'RESPONSE',subject,'R_DEFENSE');cp(b,'Defense',points)
 case(cid,'护巢蓝鳃太阳鱼' if cid=='C06' else '亲护小口黑鲈',[b],{'response.intrusion_strength':.5},'Previous: Defense/Feeding precedence 未决 → Updated: 上游 Guarding 分群，只评价 Defense 并返回。普通 Feeding Slot 不存在；不声称现实绝不摄食。')
binding('C08_R','RESPONSE','Tilapia.Feeding','R_DUAL_FIXED');cp('C08_R','Grazing',[(0,0),(1,.8)]);cp('C08_R','Suspended',[(0,0),(1,.9)])
case('C08','罗非鱼：固定双通道',['C08_R'],{'food.grazing_availability':.75,'food.suspended_availability':.5},'Previous: SELECT Profile candidate/结构未决 → Updated: 单 evaluator + 两固定 Slot 已闭合。MAX 只是本样本固定聚合函数，具体数值/聚合生产标定未完成；不是结构 blocker。')
for cid,subject,m in [('C09','Paddlefish.FieldFeeding',0),('C10','BigmouthBuffalo.FieldFeeding',.5),('C11','Mullet.FieldFeeding',.8)]:
 b=cid+'_R';binding(b,'RESPONSE',subject,'R_FIELD');cp(b,'Density',[(0,0),(1,.8)]);cp(b,'Suitability',IDENT);cp(b,'Match',IDENT)
 case(cid,{'C09':'匙吻鲟','C10':'大口胭脂鱼','C11':'鲻鱼'}[cid]+'：既有 Opportunity 的 FieldFeeding',[b],{'food.density_index':.75,'food.suitability':.5,'response.feeding_match':m},'Previous: 独立 FieldOpportunity 合同未决 → Updated: EXISTING_OPPORTUNITY_CONTRACT_REUSED。数值是呈现适配的演示输入；C09 使用不兼容呈现得到0，不从滤食或锚鱼记录推导钩饵接受。')
def feed(b,subject,strength=1,status='DEMO_WORKING'):
 binding(b,'RESPONSE',subject,'R_FEED',status);cp(b,'Match',[(0,0),(1,strength)]);cp(b,'Presentation',IDENT);slot(b,'Familiarity','N/A',False)
feed('C12_N','AtlanticSalmon.NormalFeeding')
binding('C12_M','RESPONSE','AtlanticSalmon.FreshwaterSpawningMigration','R_REACTION');cp('C12_M','Salience',[(0,0),(1,.5)]);cp('C12_M','Pursuit',[(0,1),(1,.1)])
case('C12','大西洋鲑：上游分群后使用两个绑定',['C12_N','C12_M'],{'response.feeding_match':.8,'response.presentation_fit':.75,'response.trigger_salience':.8,'response.sustained_pursuit_demand':.2},'两个 Binding 分别被已分配的 Group 调用，同一鱼不连续执行两个 Binding。Migration 演示选择普通 Feeding 关闭；Reaction 不声称已证明领地攻击或任一单一生物动机。')
row('Boundary','C13','SCOPE_RESOLUTION','juvenile suspended story 不作为可玩成鱼的新 Template 证据；以下仅分别填满三个生命周期情景，排除生产 cluster 计数。')
for suffix,sub,strength in [('J','JuvenileSuspended',.8),('O','OceanFeedingAdult',1),('S','FreshwaterSpawningAdult',0)]:
 feed('C13_'+suffix,'Sockeye.'+sub,strength,'SCENARIO_ONLY_NOT_PRODUCTION')
case('C13','红鲑：三个独立情景，先解决范围',['C13_J','C13_O','C13_S'],{'response.feeding_match':.8,'response.presentation_fit':.75},'J 展示浮游/小型悬浮猎物 feeding；O 的 FeedingMatch 输入可覆盖浮游与较大猎物；S 演示停食取0。三者由上游 lifecycle 情景绑定，未证明 J 是正常可钓场景，不作 breaker、不加 Runtime Selector。')
for cid,title,reason in [('C14','七鳃鳗寄生附着','宿主附着位于本次生成前 Response 表达范围外；没有合法 Binding/输出/运行步骤。'),('C15','匙吻鲟锚鱼','响应无关的外部捕获机制；不得把锚鱼成功编成 Feeding Response。')]:
 row('Boundary',cid,'OUT_OF_SCOPE',reason);case(cid,title,[],{},reason+' 表中用显式 OUT_OF_SCOPE；不使用空字符串或虚构的0响应。')

# Group routing: every predicate below reads one immutable species-level snapshot.
season=atom('guard_dates','slow.day_of_year','BETWEEN',[100,160],'day_of_year')
temp=atom('guard_temp','slow.recent5day_temp_c','GE',15,'°C')
nest=atom('guard_nest','slow.scene_structures','CONTAINS_ANY',['nest_cover'])
guard=group('guard_all','ALL',season,temp,nest)
cold=atom('cold_any','slow.cold_severity','GT',0)
summer=atom('summer_any','slow.oxythermal_compression','GT',0)
forage=group('forage_all','ALL',atom('forage_state','slow.pelagic_forage_state','EQ',True),atom('forage_available','slow.open_water_forage_availability','GT',0))
binding('BASS_G','GROUP','LargemouthBass','G_SHARES')
row('GroupShare','BASS_G','Guarding',guard,'PARAMETER',param('BassGuardShare',.2),'N/A')
row('GroupShare','BASS_G','ColdSlow',cold,'PROFILE',curve('BassColdShare',[(0,0),(1,.3)]),'slow.cold_severity')
row('GroupShare','BASS_G','SummerStress',summer,'PROFILE',curve('BassSummerShare',[(0,0),(1,.4)]),'slow.oxythermal_compression')
row('GroupShare','BASS_G','ForageChase',forage,'PROFILE',curve('BassForageShare',[(0,0),(1,.2)]),'slow.open_water_forage_availability')
case('BASS-ROUTING','鲈鱼：五群并列 Share',['BASS_G'],{'slow.day_of_year':120,'slow.recent5day_temp_c':18,'slow.scene_structures':['nest_cover'],'slow.cold_severity':.5,'slow.oxythermal_compression':.25,'slow.pelagic_forage_state':True,'slow.open_water_forage_availability':.5},'四项特殊 share 与 normal residual 共5群。为暴露 overlap 验证，此演示快照同时置入冷/夏压力；是合成测试，不声称典型水体会同时如此。')
for gid in ['G1','G2']:
 binding(gid,'GROUP',gid+'_GuardNormal','G_SHARES');row('GroupShare',gid,'Guarding',guard,'PARAMETER','BassGuardShare','N/A')
case('G1','Group 条件：日期 AND 温度 AND 巢区',['G1'],cases[-1]['facts'].copy(),'复用同一 guard_all 条件树；不复制 Owner 决策。')
case('G2','Group 同快照回退：不满足巢区',['G2'],{**cases[-1]['facts'],'slow.scene_structures':['open_water']},'Guard share=0；Normal=1。回退是剩余份额，不是 Defense vs Feeding fallback。')
spring=group('g3_spring','ALL',atom('g3_spring_date','slow.day_of_year','BETWEEN',[80,130],'day_of_year'),atom('g3_warm','slow.recent5day_temp_c','GE',12,'°C'))
fall=group('g3_fall','ALL',atom('g3_fall_date','slow.day_of_year','BETWEEN',[250,290],'day_of_year'),atom('g3_cool','slow.recent5day_temp_c','LE',18,'°C'))
g3root=group('g3_either','ANY',spring,fall);binding('G3','GROUP','SyntheticSeasonGroup','G_SHARES','SYNTHETIC_STRESS_ONLY');row('GroupShare','G3','Seasonal',g3root,'PARAMETER',param('G3Share',.25),'N/A')
case('G3','合成压力样本：(春 AND 温) OR (秋 AND 凉)',['G3'],{'slow.day_of_year':270,'slow.recent5day_temp_c':15},'用于把嵌套条件的实际存法填出来，不升级为已被鱼类证据确认的深层 Group breaker。')

# Bass five-group concrete projections, with fixed cold-front slot only in two sample bindings.
for suffix,subject in [('N','NormalFeeding'),('G','Guarding')]:
 spatial('BASS_'+suffix+'_B','LargemouthBass.'+subject,[(0,.1),(20,1),(35,.2)],[(0,1),(100,.2)] if suffix=='N' else [(0,1),(10,.2)],[(0,.2),(3,1),(15,.3)],anchor='stable_cover' if suffix=='N' else 'nest_site')
def turn_overlay(b):
 for r in data['Slot']:
  if r['binding_id']==b and r['slot']=='ColdFront':r.update(enabled=True,ref_id='N/A',ref_kind='SWITCH')
 for n,pts in [('Cover',[(0,1),(100,0)]),('Deep',IDENT)]:
  p=curve(b+'_'+n,pts)
  found=False
  for r in data['Slot']:
   if r['binding_id']==b and r['slot']==n:r.update(enabled=True,ref_id=p);found=True
  if not found:slot(b,n,p)
turn_overlay('BASS_N_B')
binding('BASS_C_B','BAKE','LargemouthBass.ColdSlow','S_COLD')
for n in ['Warmth','Stability','Refuge']:cp('BASS_C_B',n,IDENT)
binding('BASS_S_B','BAKE','LargemouthBass.SummerStress','S_SUMMER');pv('BASS_S_B','OxygenMin',3,'mg/L')
for n in ['Cooling','Oxygen','Tradeoff']:cp('BASS_S_B',n,IDENT)
binding('BASS_F_B','BAKE','LargemouthBass.ForageChase','S_FORAGE');pv('BASS_F_B','ForageMin',.2)
for n in ['Forage','Vertical','OpenWater']:cp('BASS_F_B',n,IDENT)
cp('BASS_F_B','Temperature',[(0,.1),(20,1),(35,.2)]);cp('BASS_F_B','Oxygen',[(0,0),(5,1),(10,1)]);slot('BASS_F_B','ColdFront','N/A',False,'SWITCH');turn_overlay('BASS_F_B')
feed('BASS_N_R','LargemouthBass.NormalFeeding');feed('BASS_F_R','LargemouthBass.ForageChase',.95)
for b in ['BASS_N_R','BASS_F_R']:
 p=curve(b+'_Familiarity',[(0,1),(1,.5)])
 next(r for r in data['Slot'] if r['binding_id']==b and r['slot']=='Familiarity').update(enabled=True,ref_id=p)
binding('BASS_G_R','RESPONSE','LargemouthBass.Guarding','R_DEFENSE');cp('BASS_G_R','Defense',[(0,0),(1,1)])
for s,subject,feedstrength,reactionstrength in [('C','ColdSlow',.25,.8),('S','SummerStress',.35,.7)]:
 b='BASS_'+s+'_R';binding(b,'RESPONSE','LargemouthBass.'+subject,'R_FEED_REACTION')
 cp(b,'Match',[(0,0),(1,feedstrength)]);cp(b,'Presentation',IDENT);cp(b,'Salience',[(0,0),(1,reactionstrength)]);cp(b,'Pursuit',[(0,1),(1,.1)])
gear=group('q_big_gear','ALL',atom('q_hook','gear.hook_size_index','GE',3),atom('q_bait','gear.bait_size_cm','GE',8,'cm'))
inactive=atom('q_inactive','quality_context.time_band','IN',['inactive'])
coldnight=group('q_coldnight','ALL',atom('q_cold','quality_context.water_temp_c','LE',8,'°C'),atom('q_night','quality_context.time_band','IN',['night']))
def quality(b,subject,weights,mods=True):
 binding(b,'QUALITY',subject,'Q_PARALLEL')
 for bucket,w in zip(['Small','Medium','Large','Rare'],weights):row('QualityWeight',b,bucket,w)
 if mods:
  for bucket,m in [('Large',1.5),('Rare',1.2)]:row('QualityModifier',b,'BigGear',gear,bucket,m)
  for bucket,m in [('Small',1.2),('Medium',1.2),('Large',.7),('Rare',.7)]:row('QualityModifier',b,'LowActivity',inactive,bucket,m)
  for bucket,m in [('Large',.8),('Rare',.8)]:row('QualityModifier',b,'ColdNight',coldnight,bucket,m)
weights={'N':[50,30,15,5],'G':[20,40,30,10],'C':[55,30,12,3],'S':[50,35,12,3],'F':[25,50,20,5]}
bassfacts={'target.temperature_c':20,'target.anchor_distances_m':{'stable_cover':25,'nest_site':2.5},'target.depth_m':3,'target.cover_distance_m':20,'target.adjacent_deep_access':.9,'weather.cold_front_severity':.5,'target.relative_warmth':.8,'target.stability':.9,'target.low_energy_refuge':.75,'target.oxygen_mg_l':5,'target.relative_cooling':.8,'target.oxygen_margin':.75,'target.cover_prey_tradeoff':.6,'target.forage_school_intensity':.8,'target.vertical_alignment':.75,'target.open_water_context':1,'response.feeding_match':.8,'response.presentation_fit':.75,'response.cue_familiarity':.4,'response.intrusion_strength':.8,'response.trigger_salience':.9,'response.sustained_pursuit_demand':.1,'gear.hook_size_index':3,'gear.bait_size_cm':10,'quality_context.time_band':'active','quality_context.water_temp_c':20}
for suffix,subject in [('N','NormalFeeding'),('G','Guarding'),('C','ColdSlow'),('S','SummerStress'),('F','ForageChase')]:
 quality('BASS_'+suffix+'_Q','LargemouthBass.'+subject,weights[suffix])
 case('BASS-'+suffix,'大口黑鲈 '+subject,['BASS_'+suffix+'_B','BASS_'+suffix+'_R','BASS_'+suffix+'_Q'],bassfacts.copy(),'Binding 顺序展示因果位置；品质发生于既定 Group 后，不反向决定 Group。Normal/Forage 的 ColdFront 末端 Slot 在本样本启用，其他群关闭/不提供；MAX/BLEND 与所有数字保持演示/Working Candidate。' + (' Forage 的食物场强度只在 Bake 使用，Response 不再乘同一密度。' if suffix=='F' else ''))
for q,facts,note in [
 ('Q1',{'gear.hook_size_index':3,'gear.bait_size_cm':10,'quality_context.time_band':'active','quality_context.water_temp_c':20},'大钩且大饵：Large×1.5、Rare×1.2。'),
 ('Q2',{'gear.hook_size_index':1,'gear.bait_size_cm':3,'quality_context.time_band':'inactive','quality_context.water_temp_c':20},'低活性：Small/Medium×1.2，Large/Rare×0.7。桶与成体关系只是演示映射，不声称小=幼体、大=成体的生物同一性。'),
 ('Q3',{'gear.hook_size_index':3,'gear.bait_size_cm':10,'quality_context.time_band':'night','quality_context.water_temp_c':6},'BigGear 与 ColdNight 同时命中。后者只读原始水温/时段，不读前者改完的分布。')]:
 quality(q,'IllustrativeQuality',weights['N']);case(q,'品质并列修正 '+q,[q],facts,note)

# Readable table semantics and deterministic specimen evaluator.
def getparam(p):return next(r['value'] for r in data['Parameter'] if r['parameter_id']==p)
def pred(p,facts):
 r=next(r for r in data['Predicate'] if r['node_id']==p)
 if r['kind']!='ATOM':
  children=[x['child_id'] for x in data['PredicateMember'] if x['parent_id']==p];vals=[pred(c,facts) for c in children]
  return all(vals) if r['kind']=='ALL' else any(vals) if r['kind']=='ANY' else not vals[0]
 a=facts[r['field']];b=getparam(r['parameter_id']);op=r['operator']
 if op=='GE':return a>=b
 if op=='GT':return a>b
 if op=='LE':return a<=b
 if op=='EQ':return a==b
 if op=='BETWEEN':return b[0]<=a<=b[1]
 if op=='IN':return a in b
 if op=='CONTAINS_ANY':return bool(set(a)&set(b))
 raise ValueError(op)
def expression(p):
 r=next(r for r in data['Predicate'] if r['node_id']==p)
 if r['kind']=='ATOM':return r['field']+' '+r['operator']+' @'+r['parameter_id']
 es=[expression(x['child_id']) for x in data['PredicateMember'] if x['parent_id']==p]
 return '('+ (' AND ' if r['kind']=='ALL' else ' OR ').join(es)+')' if r['kind']!='NOT' else 'NOT '+es[0]
def lookup(profile,x):
 pts=sorted([(r['x'],r['y']) for r in data['CurvePoint'] if r['profile_id']==profile])
 if x<=pts[0][0]:return pts[0][1]
 if x>=pts[-1][0]:return pts[-1][1]
 for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
  if x0<=x<=x1:return y0+(y1-y0)*(x-x0)/(x1-x0)
def evaluate(b,facts):
 bind=next(r for r in data['Binding'] if r['binding_id']==b);t=bind['template_id'];s={r['slot']:r for r in data['Slot'] if r['binding_id']==b};trace={}
 def fit(name,field):
  y=lookup(s[name]['ref_id'],facts[field]);trace[name]=round(y,8);return y
 def scalar(name):return getparam(s[name]['ref_id'])
 def overlay(base):
  trace['Base']=round(base,8)
  if not s['ColdFront']['enabled']:return base
  c=fit('Cover','target.cover_distance_m');d=fit('Deep','target.adjacent_deep_access');v=facts['weather.cold_front_severity'];trace['Refuge']=max(c,d);return (1-v)*base+v*max(c,d)
 if t=='S_FIXED':
  anchor=scalar('Anchor');distance=facts['target.anchor_distances_m'][anchor];trace['Anchor']=anchor;trace['AnchorDistance']=distance
  structure=lookup(s['Structure']['ref_id'],distance);trace['Structure']=structure
  v=fit('Temperature','target.temperature_c')*structure*fit('Depth','target.depth_m')
  v*=fit('Light','target.illuminance_lux') if s['Light']['enabled'] else 1;result=overlay(v)
 elif t=='S_COLD':result=fit('Warmth','target.relative_warmth')*fit('Stability','target.stability')*fit('Refuge','target.low_energy_refuge')
 elif t=='S_SUMMER':
  if facts['target.oxygen_mg_l']<scalar('OxygenMin'):result=0;trace['Gate']='REJECT_TARGET'
  else:result=fit('Cooling','target.relative_cooling')*fit('Oxygen','target.oxygen_margin')*fit('Tradeoff','target.cover_prey_tradeoff')
 elif t=='S_FORAGE':
  if facts['target.forage_school_intensity']<scalar('ForageMin'):result=0;trace['Gate']='REJECT_TARGET'
  else:result=overlay(fit('Forage','target.forage_school_intensity')*fit('Vertical','target.vertical_alignment')*fit('Temperature','target.temperature_c')*fit('Oxygen','target.oxygen_mg_l')*fit('OpenWater','target.open_water_context'))
 elif t=='R_BANDS':
  result=scalar('Default')
  for r in sorted([r for r in data['ResponseBand'] if r['binding_id']==b],key=lambda r:r['priority']):
   yes=pred(r['predicate_id'],facts);trace[r['predicate_id']]=yes
   if yes:result=r['response_strength'];break
 elif t=='R_DEFENSE':result=fit('Defense','response.intrusion_strength')
 elif t=='R_DUAL_FIXED':result=max(fit('Grazing','food.grazing_availability'),fit('Suspended','food.suspended_availability'))
 elif t=='R_FIELD':result=fit('Density','food.density_index')*fit('Suitability','food.suitability')*fit('Match','response.feeding_match')
 elif t in ['R_FEED','R_REACTION','R_FEED_REACTION']:
  f=fit('Match','response.feeding_match')*fit('Presentation','response.presentation_fit') if t!='R_REACTION' else 0
  r=fit('Salience','response.trigger_salience')*fit('Pursuit','response.sustained_pursuit_demand') if t!='R_FEED' else 0
  u=fit('Familiarity','response.cue_familiarity') if t=='R_FEED' and s['Familiarity']['enabled'] else 1
  result=f*u if t=='R_FEED' else r if t=='R_REACTION' else max(f,r)
  if t!='R_REACTION':trace['Feeding']=f
  if t!='R_FEED':trace['Reaction']=r
 elif t=='G_SHARES':
  result={}
  for r in data['GroupShare']:
   if r['binding_id']!=b:continue
   yes=pred(r['predicate_id'],facts);trace[r['predicate_id']]=yes
   result[r['group']]=(getparam(r['share_ref']) if r['share_kind']=='PARAMETER' else lookup(r['share_ref'],facts[r['input_field']])) if yes else 0
  total=sum(result.values())
  if total>1+1e-12 or any(v<0 or v>1 for v in result.values()):raise ValueError('ShareOverflow')
  result['Normal']=1-total
 elif t=='Q_PARALLEL':
  result={r['bucket']:r['base_weight'] for r in data['QualityWeight'] if r['binding_id']==b};hits=[]
  for r in data['QualityModifier']:
   if r['binding_id']==b and pred(r['predicate_id'],facts):result[r['bucket']]*=r['multiplier'];hits.append(r['rule_id']+'/'+r['bucket'])
  trace['hits']=hits;trace['raw']=result.copy();total=sum(result.values())
  if total<=0:raise ValueError('InvalidQualityTotal')
  result={k:v/total for k,v in result.items()}
 else:raise ValueError(t)
 return {'binding':b,'template':t,'intermediate':trace,'result':result}

def dsl(b):
 bind=next(r for r in data['Binding'] if r['binding_id']==b);tpl=templates[bind['template_id']]
 bindings=[]
 for r in data['Slot']:
  if r['binding_id']==b:bindings.append('  '+r['slot']+' = '+('开启' if r['enabled'] and r['ref_kind']=='SWITCH' else '@'+r['ref_id'] if r['enabled'] else '关闭（无引用）'))
 body=tpl['script']
 bands=[];shares=[];mods=[]
 for r in data['ResponseBand']:
  if r['binding_id']==b:bands.append('优先级 '+str(r['priority'])+'：若 '+expression(r['predicate_id'])+'：返回 响应强度('+str(r['response_strength'])+')')
 for r in data['GroupShare']:
  if r['binding_id']==b:shares.append(r['group']+' = 若 '+expression(r['predicate_id'])+' 则 '+('@'+r['share_ref'] if r['share_kind']=='PARAMETER' else '查曲线(@'+r['share_ref']+', '+r['input_field']+')')+' 否则 0')
 for r in data['QualityModifier']:
  if r['binding_id']==b:mods.append('并列修正 '+r['rule_id']+'/'+r['bucket']+'：若 '+expression(r['predicate_id'])+'，则 '+r['bucket']+' 乘 '+str(r['multiplier']))
 body=body.replace('{bands}','\n'.join(bands)).replace('{shares}','\n'.join(shares)).replace('{modifiers}','\n'.join(mods))
 # Resolve every @Slot to the concrete reference used by this specimen.
 for r in sorted([r for r in data['Slot'] if r['binding_id']==b],key=lambda r:-len(r['slot'])):
  body=body.replace('@'+r['slot'],('@'+r['ref_id']) if r['enabled'] else '关闭槽位（不可读取）')
 header='表达 '+b+' 用于 '+bind['subject']+' / '+bind['surface']+'\n模板 '+bind['template_id']+'（固定结构，仅展开便于阅读）\n'
 return header+'配置：\n'+ ('\n'.join(bindings) if bindings else '  无 Profile Slot；使用下列具名规则与共享数值表')+'\n执行：\n'+body

def closure_rows(ids):
 rows={k:[] for k in TABLES};preds=set();params=set();profiles=set();tids=set()
 for k in ['Binding','Slot','ResponseBand','GroupShare','QualityWeight','QualityModifier']:
  rows[k]=[r for r in data[k] if r['binding_id'] in ids]
 for r in rows['Binding']:tids.add(r['template_id'])
 for r in rows['Slot']:
  if r['enabled'] and r['ref_kind']!='SWITCH':(params if r['ref_kind']=='PARAMETER' else profiles).add(r['ref_id'])
 for k in ['ResponseBand','GroupShare','QualityModifier']:
  for r in rows[k]:preds.add(r['predicate_id'])
 for r in rows['GroupShare']:(params if r['share_kind']=='PARAMETER' else profiles).add(r['share_ref'])
 changed=True
 while changed:
  old=len(preds)
  for r in data['PredicateMember']:
   if r['parent_id'] in preds:preds.add(r['child_id'])
  changed=len(preds)!=old
 rows['Predicate']=[r for r in data['Predicate'] if r['node_id'] in preds]
 rows['PredicateMember']=[r for r in data['PredicateMember'] if r['parent_id'] in preds]
 params.update(r['parameter_id'] for r in rows['Predicate'] if r['kind']=='ATOM')
 rows['Parameter']=[r for r in data['Parameter'] if r['parameter_id'] in params]
 rows['CurvePoint']=[r for r in data['CurvePoint'] if r['profile_id'] in profiles]
 rows['TemplateStep']=[r for r in data['TemplateStep'] if r['template_id'] in tids]
 return rows

def validate():
 # Minimal specimen static checks. No claim to be a production compiler.
 assert len(cases)==len({c['id'] for c in cases}),'duplicate case_id'
 def unique(k,fields):
  vals=[tuple(str(r[f]) for f in fields) for r in data[k]];assert len(vals)==len(set(vals)),k
 for k,fields in {'Binding':['binding_id'],'Slot':['binding_id','slot'],'Parameter':['parameter_id'],'CurvePoint':['profile_id','x'],'Predicate':['node_id'],'PredicateMember':['parent_id','display_index'],'ResponseBand':['binding_id','priority'],'GroupShare':['binding_id','group'],'QualityWeight':['binding_id','bucket'],'QualityModifier':['binding_id','rule_id','bucket'],'Boundary':['case_id'],'TemplateStep':['template_id','step']}.items():unique(k,fields)
 for r in data['Binding']:
  spec=templates[r['template_id']]['slots'];actual=[x for x in data['Slot'] if x['binding_id']==r['binding_id']]
  assert all(x['slot'] in [n.rstrip('?') for n in spec] for x in actual)
  assert all(n in [x['slot'] for x in actual] for n in spec if not n.endswith('?'))
 for r in data['Slot']:
  assert r['binding_id'] in [b['binding_id'] for b in data['Binding']]
  if r['ref_kind']=='SWITCH':assert r['ref_id']=='N/A' and r['slot']=='ColdFront'
  elif r['enabled']:
   assert r['ref_id'] in [x['parameter_id'] for x in data['Parameter']] if r['ref_kind']=='PARAMETER' else r['ref_id'] in [x['profile_id'] for x in data['CurvePoint']]
  else:assert r['ref_id']=='N/A'
 for r in data['CurvePoint']:assert math.isfinite(r['x']) and 0<=r['y']<=1
 for r in data['ResponseBand']:assert 0<=r['response_strength']<=1
 for r in data['QualityWeight']:assert r['base_weight']>=0
 for r in data['QualityModifier']:assert r['multiplier']>=0
 for r in data['Predicate']:
  if r['kind']=='ATOM':assert r['parameter_id'] in [p['parameter_id'] for p in data['Parameter']]
  else:
   cs=[m for m in data['PredicateMember'] if m['parent_id']==r['node_id']];assert len(cs)==1 if r['kind']=='NOT' else len(cs)>0
 def walk(p,stack):
  assert p not in stack,'cycle'
  for m in data['PredicateMember']:
   if m['parent_id']==p:walk(m['child_id'],stack+[p])
 for p in data['Predicate']:walk(p['node_id'],[])
 for c in cases:
  for b in c['bindings']:traces.append({'case':c['id'],**evaluate(b,c['facts'])})
 def check(label,actual,expected):
  if isinstance(expected,dict):assert set(actual)==set(expected) and all(abs(actual[k]-v)<1e-9 for k,v in expected.items()),(label,actual,expected)
  else:assert abs(actual-expected)<1e-9,(label,actual,expected)
  assertions.append({'check':label,'actual':actual,'expected':expected,'status':'PASS'})
 get=lambda b:next(t['result'] for t in traces if t['binding']==b)
 for b,v in {'C01_B':.8,'C02_B':.7,'C03_R':.8,'C04_R':.8,'C05_B':.8,'C06_R':.6,'C07_R':.7,'C08_R':.6,'C09_R':0,'C10_R':.15,'C11_R':.24,'C12_N':.6,'C12_M':.328,'C13_J':.48,'C13_O':.6,'C13_S':0,'BASS_N_B':.85,'BASS_G_B':.8,'BASS_C_B':.54,'BASS_S_B':.36,'BASS_F_B':.75,'BASS_C_R':.6552,'BASS_S_R':.5733}.items():check(b,get(b),v)
 check('五群同快照剩余份额',get('BASS_G'),{'Guarding':.2,'ColdSlow':.15,'SummerStress':.1,'ForageChase':.1,'Normal':.45})
 check('Q1',get('Q1'),{k:v/108.5 for k,v in zip(['Small','Medium','Large','Rare'],[50,30,22.5,6])})
 check('Q2',get('Q2'),{k:v/110 for k,v in zip(['Small','Medium','Large','Rare'],[60,36,10.5,3.5])})
 check('Q3',get('Q3'),{k:v/102.8 for k,v in zip(['Small','Medium','Large','Rare'],[50,30,18,4.8])})
 check('Q3 交换 Modifier 行仍等义',evaluate('Q3',next(c['facts'] for c in cases if c['id']=='Q3'))['result'],get('Q3'))
 # Actually reverse the rows for the order-invariance check.
 data['QualityModifier'].reverse();check('Q3 反转 Modifier 后',evaluate('Q3',next(c['facts'] for c in cases if c['id']=='Q3'))['result'],get('Q3'));data['QualityModifier'].reverse()
 check('夏季硬 Gate 零',evaluate('BASS_S_B',{**bassfacts,'target.oxygen_mg_l':2})['result'],0)
 check('Forage Gate 不被 Overlay 复活',evaluate('BASS_F_B',{**bassfacts,'target.forage_school_intensity':.1})['result'],0)
 check('低 salience 仍计算另一 Channel',evaluate('C08_R',{'food.grazing_availability':0,'food.suspended_availability':1})['result'],.9)
 check('双阈值无命中使用 default',evaluate('C03_R',{'response.feeding_match':.1,'response.natural_drift_fit':1})['result'],0)
 # Missing required input must be an error, never silently converted to zero.
 try:evaluate('C06_R',{})
 except KeyError:assertions.append({'check':'缺失必需输入拒绝','status':'PASS','actual':'KeyError (specimen ValidationError boundary)','expected':'error'})
 else:raise AssertionError('missing input accepted')
 old=getparam('BassGuardShare');next(r for r in data['Parameter'] if r['parameter_id']=='BassGuardShare')['value']=.9
 try:evaluate('BASS_G',next(c['facts'] for c in cases if c['id']=='BASS-ROUTING'))
 except ValueError:assertions.append({'check':'Group Share 超1拒绝','status':'PASS','actual':'ShareOverflow','expected':'error'})
 else:raise AssertionError('overflow accepted')
 next(r for r in data['Parameter'] if r['parameter_id']=='BassGuardShare')['value']=old
 assertions.append({'check':'27个案例ID唯一','status':'PASS','actual':len({c['id'] for c in cases}),'expected':len(cases)})
 switch=next(r for r in data['Slot'] if r['binding_id']=='BASS_N_B' and r['slot']=='ColdFront')
 switch['enabled']=False;check('ColdFront纯开关关闭返回Base',evaluate('BASS_N_B',bassfacts)['result'],.8);switch['enabled']=True
 assert 'Feeding' not in evaluate('C12_M',next(c['facts'] for c in cases if c['id']=='C12'))['intermediate']
 assert 'Reaction' not in evaluate('C12_N',next(c['facts'] for c in cases if c['id']=='C12'))['intermediate']
 assertions.append({'check':'未执行通道不伪造0值Trace','status':'PASS','actual':'absent','expected':'absent'})
validate()

def fmt(v):
 if isinstance(v,(dict,list)):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
 if isinstance(v,float):return format(v,'.8g')
 return str(v)
def md_table(cols,rows):
 return '| '+' | '.join(cols)+' |\n| '+' | '.join('---' for c in cols)+' |\n'+'\n'.join('| '+' | '.join(fmt(r[c]).replace('|','\\|').replace('\n','<br>') for c in cols)+' |' for r in rows)+'\n'
def ht_table(cols,rows):
 return '<div class="scroll"><table><thead><tr>'+''.join('<th>'+html.escape(c)+'</th>' for c in cols)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+html.escape(fmt(r[c]))+'</td>' for c in cols)+'</tr>' for r in rows)+'</tbody></table></div>'
def nt_table(cols,rows):
 return '<table header-row="true" fit-page-width="true">\n<tr>'+''.join('<td>'+html.escape(c)+'</td>' for c in cols)+'</tr>\n'+''.join('<tr>'+''.join('<td>'+html.escape(fmt(r[c]))+'</td>' for c in cols)+'</tr>\n' for r in rows)+'</table>\n'

SCHEMA_NOTES={
 'Binding':'PK binding_id；surface=GROUP/BAKE/RESPONSE/QUALITY；template_id FK→只读模板目录。subject 是上游已选择的群/情景；不以字符串匹配在 Runtime 路由。status 区分演示 Working、情景及合成压力。',
 'Slot':'PK(binding_id,slot)，binding FK；slot 必须属于该模板白名单。enabled 为 bool；ref_kind=PROFILE/PARAMETER/SWITCH。PROFILE/PARAMETER 开启时 ref_id 必须存在且类型匹配，关闭时 N/A。纯 SWITCH 的 ref_id 始终 N/A，唯一真值源就是 enabled，没有第二个 bool Parameter。可关 Slot 没有 Side effect，也不能调整步骤位置。',
 'Parameter':'PK parameter_id；type=number/bool/string/set<string>；value 按 type 解析（BETWEEN 的数值二元范围见特例）；unit 必须一致。所有本批数字是 DEMO 校验值，不是生态/平衡标定。',
 'CurvePoint':'PK(profile_id,x)；x 严格递增、有限，y∈[0,1]。至少两点；线性插值、两端夹持。不同 Profile 不混单位；输入量纲由固定 Slot 定义。没有未写出的 spline 或随机噪声。',
 'Predicate':'PK node_id；kind=ATOM/ALL/ANY/NOT。ATOM 的 field 是只读白名单字段，operator∈GE/GT/LE/EQ/BETWEEN/IN/CONTAINS_ANY；parameter_id FK。组合节点三个叶字段显式 N/A。BETWEEN 为闭区间；空集、缺失字段/类型错拒绝。',
 'PredicateMember':'PK(parent_id,display_index)；parent/child FK→Predicate；ALL/ANY 至少一个子节点，NOT 恰一个；禁止环。display_index 只用于作者阅读，没有 Runtime 顺序意义；全部条件是纯读。',
 'ResponseBand':'PK(binding_id,priority)；仅 R_BANDS，priority 为唯一整数递增，predicate_id FK；结果 response_strength∈[0,1]。FIRST_MATCH；无命中用显式 Default。这里的 priority 是同一响应分档规则顺序，绝非 Defense/Feeding 优先级。',
 'GroupShare':'PK(binding_id,group)；predicate FK。share_kind=PARAMETER 时 share_ref→[0,1]标量且 input_field=N/A；PROFILE 时 ref→CurvePoint 并指定慢速输入。全部条件同快照、同时算；总和超1拒绝；Normal 不单列可编辑 Share。',
 'QualityWeight':'PK(binding_id,bucket)；bucket 固定 Small/Medium/Large/Rare 的演示枚举；base_weight 非负、至少一项正值。不声称这四桶已成为生产枚举，也不等同生命周期。',
 'QualityModifier':'PK(binding_id,rule_id,bucket)；predicate FK；multiplier 非负有限。命中行按桶连乘，未列桶×1；所有条件读原始快照；只归一化一次，抽样在外部。',
 'Boundary':'PK case_id；scope=SCOPE_RESOLUTION/OUT_OF_SCOPE；reason 是作者范围说明，不是可执行 predicate。C14/C15 无 Binding 而非伪造 Response=0。',
 'TemplateStep':'PK(template_id,step)；是方案A须明确给工程/作者看的只读模板目录，不是普通配置表。operation/input/output/failure 展开固定因果；修改执行拓扑须创建/修改模板，经现有机制治理，不能让 Switch 偷改顺序。',
}
# Correct range parameter type, after primitive construction, for export.
for r in data['Parameter']:
 if isinstance(r['value'],list) and r['value'] and isinstance(r['value'][0],(int,float)):r['type']='range<number>'

INTRO='''# FCF Authoring 具体化样本 R2｜配置表、中文伪脚本与逐步结果

**状态：WORKING / PRE-GATE / 演示数据；未 Promote，未选择最终 Config Table 或 DSL。**

这份附录把表达写到可填写、可复算的程度：同一输入在表格方案中对应哪些行，在中文伪脚本中执行哪些步骤，得到哪些中间值与类型化输出。完整覆盖 C01–C15 的范围处理，并补入 G1–G3、Q1–Q3 和最新鲈鱼五群样本。文中所有阈值、曲线、乘数、分档、MAX/BLEND 的具体演示使用均是可替换的样本选择，不是新增机制 Authority。

## 1. 本轮来源与边界

Source Map：Router → Project Current → Branch Index → Simplified V0 Working Main 做最小 Rebase；最新 Representation Design Gate R1 和鲈鱼深挖尾部 Working snapshot 处理过期未决；原 C01–C15 Mapping 保留鱼类故事边界。Existing Base Check：旧15例页面已有矩阵/伪代码，但尚不足以还原完整配置；本附录保留旧投影，以新行表补齐。Gap Classification：表列/行/中间计算属于 DOCUMENTATION GAP；曲线数值与候选聚合的最终标定属于 DEFERRED / NON-BLOCKING；生产空间顺序、C13 可玩范围仍未替 Owner 决定。

核心输入：[Representation Design Gate R1](https://app.notion.com/p/3d6a4137d23681eab6cfd3a535a8938a)、[原15例页面](https://app.notion.com/p/3d6a4137d236814ea872ed6305942594)、[案例映射](https://app.notion.com/p/3d6a4137d2368151b762e50bc5ce6dfd)、[Authoring Stress Working](https://app.notion.com/p/3d6a4137d2368118aeb7c6a569c4c3c3)、[鲈鱼五群最新 Working](https://app.notion.com/p/3d6a4137d23681e2af96e873eef9411a)。这些 Working 输入没有自动提升为 Current。

本稿骨架已经落实为：共用语义 → 具体表 Schema → 每例样例行及中文脚本 → 输入/中间值/输出 → 相同修改操作 → 验证与边界。旧文的 C08/C09–C12 结构“等待 Owner”标记以最新 Gate 为准；旧独立审核不覆盖本附录。

## 2. 一屏模型：作者到底填什么

慢速世界快照 → GroupShare（同物种组成） → 已分配 FishGroup → Bake（空间权重）。既有 PresentationSession → 合法 semantic particle → Root Semantic Occurrence → OpportunityId → Evaluation Scope → 群专属 Response。Quality 使用已经选定的 Group 基准分布，读原始 facts 并列修正，归一化后交既有抽样 Owner。以上箭头表示合同依赖，不是本附录新造的完整抽签顺序。

表格作者选择固定模板、填 Profile/参数、连接 Predicate 树、填写结果行；模板内部代码是共享工程成本。中文脚本作者仍引用同一份数值表，把条件与因果关系连续写出来；本稿把每个模板实际展开，不能只用“执行某 Profile”隐藏逻辑。

ResponseStrength 是本演示的类型化归一强度标量，不等于最终中鱼概率；SpatialDistributionWeight 是空间适宜性输出，不改 Species 总量；FishGroupShareVector 仅描述物种内组成；QualityDistribution 仅是归一化分布。到生产 Typed Result 的字段映射须跟随现有合同，本文这些短字段名不是宣告新增正式 API。

## 3. 两种方案的完整物理布局

方案 A 有 **11 张作者数据表 + 1 张只读 TemplateStep 目录**。方案 B 有 **5 张共用数据表（Binding、Parameter、CurvePoint、QualityWeight、Boundary）+ 1 份 Script 文本集合**。B 把 Slot/Predicate/Member/ResponseBand/GroupShare/QualityModifier 的内容写入正文；没有消灭其逻辑与校验成本。其 Script 记录为 `binding_id, dialect_version, source`，一绑定一记录；这里 `dialect_version=CN_PSEUDO_R2`，不是已经实现的生产 DSL 编译器。两边都需模板/运行时实现，表数不是复杂度结论。

配置只接受下文列出的模板槽、算子、字段和输出；无任意循环、跳转、写世界状态或 RNG。DSL 中 `返回` 会终止该绑定；固定双通道均评价再聚合；配置 Predicate 子项换行/换序不构成新模板。修改 TemplateStep 的有语义 Gate/依赖关系是模板改动，不是调一个 Profile 或 Switch。

所有样例输入是本次快照的只读别名：slow.* 来自水体/时令 Resolver；target.* 来自空间目标 Resolver；weather.* 来自天气 Resolver；food.* 来自本 Opportunity 可用的 FoodField facts；response.* 来自既有 Scope 的鱼种/呈现匹配与刺激事实；gear.* 来自同一 Active Presentation Channel；quality_context.* 来自品质评价快照。连续 index 为[0,1]，距离m、深度m、温度°C、溶氧mg/L、光照lux，日期为1–366日，hook_size_index 是演示有序尺码。`target.cover_prey_tradeoff` 等复合量是演示输入适配别名，不能由本稿反推 Resolver 算法已经实现。输入不存在/非有限/单位错时返回 ValidationError；它不等于机制的“条件不满足”。没有隐式0、空字符串默认或二次随机。

公共曲线查询：节点 (x0,y0),(x1,y1) 间 `y=y0+(y1-y0)*(x-x0)/(x1-x0)`；范围外取端点。示例 Structure(0,1),(100,0.2)，距离25m得到0.8。表格与脚本使用同一曲线，不在脚本里偷偷增加自由算式。
'''

ENGINEERING='''## 6. 身份、失败边界与最小生产桥接

这份交付的程序只用于复算纸面样本，不接入游戏，也没有实现一个新的 FCF Runtime。生产需要的桥接是：现有 Resolver 提供只读事实 → 表格加载器/受限 DSL 前端做相同类型与引用校验 → 同一评价语义 → 现有 Typed Result。每个例子的输入和数值输出可作为两种前端的共同验收样本。

身份 Worked Example：现有 Session S_demo 的 Active Channel 是 lure_A；一个已准入 Pause 对应 Root R_demo，系统已分配 Opportunity O_demo。packet 1 和 packet 2 引用同一 R_demo，即同一个 O_demo；外部现有 resolution owner 对该 Root 只结算一次。R_FIELD 仅消费传入 Scope，读同一 lure_A 的 FeedingMatch 与 FoodField。切换一个 frame 或重发 packet 不创建新 O、不重新抽签；新的被准入语义颗粒才由原 Owner 提供新身份。Static Bottom/Float 的一个合法静止姿态颗粒同理。本文不规定新 ID 拼接法、计时器、Reservation 或 Session 写回，不证明生产的幂等实现已经通过测试。

Gate 拒绝是有效类型结果0；输入缺失/非法表引用是 ValidationError；C14/C15 是范围外，不运行、更不伪造0。质量总和0、负权重、重复优先级、Predicate 环、非法 Slot 均是配置错误。表格与 DSL 同样不得写 Actor/World/FishGroup 状态，不得生成 RNG；Response 输出由既有下游消费，不创建 Follow/Attack 行为。播放器反馈可沿当前 trace 暴露“哪项条件失败/哪条 Channel 贡献最大”，但玩家是否看到这些诊断由产品层决定，本稿不添加新玩家按钮。

## 7. 用同一修改任务核对成本

这些是实际样本的编辑定位，不是测得的工时。共享 Parameter 修改会影响所有引用，Clone Profile 则必须改具名引用；两种表达都应显示受影响绑定。

| 修改 | 配置 A 的实际位置 | 中文脚本 B 的实际位置 | 语义约束 |
| --- | --- | --- | --- |
| C06 入侵0.5对应0.6改为0.65 | CurvePoint(profile=C06_R_Defense,x=0.5).y 一格 | 同一共享 CurvePoint 一格；脚本不变 | 调 Profile，不加 Feeding |
| C03 漂流阈值0.6改为0.7 | Parameter C03_drift_value.value 一格 | 同一 Parameter 一格；脚本不变 | 不改 FIRST_MATCH 顺序 |
| C03 高响应再加一个 AND 条件 | 新 Parameter + ATOM + PredicateMember，共3行 | 新 Parameter 1行 + 高响应条件表达式加一项 | 只能读白名单输入；不能凭添加字段假定上游已提供 |
| C08 两通道输入相同，将 MAX 换成平均 | 改 R_DUAL_FIXED 模板聚合步骤1行及实现/验证 | 改固定聚合语句及实现/验证 | 属候选聚合设计变更；不能假装 Profile 参数能改拓扑 |
| Q1 大装备 Large乘数1.5改1.6 | QualityModifier(Q1,BigGear,Large).multiplier 一格 | Q1 对应并列修正语句1处 | 不改其它桶、不读取中间分布 |
| C05 关闭低光 Slot | Slot(C05_B,Light) enabled=false 且 ref_id=N/A，同一行2格 | 配置 Light=关闭；固定分支仍留在模板 | 不交换 Runtime Order |
| 鲈鱼夏季目标氧门提前返回 | 本例已有 S_SUMMER step1；不能挪到归一化/Overlay之后 | 已有首条“若氧<阈值返回0” | 真正顺序意义来自提前返回和后续步骤的执行边界 |

算法差异与排版差异：C01 的 T×S×D 因子独立，调换计算次序仍同结果，不把印刷顺序冒充 L 增长证据；S_SUMMER 的 Gate 先失败即返回，后续适宜性不应执行。Cold 和 Summer 的因果链不同，即使一份通用脚本都能写出来，也不能据此宣称它们自动是同一固定模板。

## 8. 样本目录与设计统计的边界

本稿的固定模板名是可运行演示目录，不是重新裁决 L_final。按四个 Surface 分开计数并排除 C13 情景与 G3 合成例，样本使用：Group=1、Bake=4、Response=7、Quality=1。这些是 `N_fixture_templates`，不能改写成 `L_confirmed`：C01/C02/C05 的生产 Spatial Runtime Order 尚未定，C08 的结构已定但具体聚合待标定，Cold/Summer 的 MAX 和 ColdFront BLEND 也仍是 Working Candidate。没有把 C08/C09–C12 的过期结构未决重新打开。

共用关系已在 Binding 行上落实：C01/C02/C05/鲈鱼Normal/Guard 共享 S_FIXED（不同 Profile 与开关）；C03/C04 共享 R_BANDS；C06/C07/鲈鱼Guard 共享 R_DEFENSE；C09–C11 共享 R_FIELD；C12 Normal/鲈鱼Normal/Forage 共享 R_FEED；鲈鱼Cold/Summer 共享 R_FEED_REACTION；各群 Quality 共享 Q_PARALLEL、只换基准与修正；所有 Group 样例共享 G_SHARES。

PT3 未因双 Profile 或上游 Lifecycle 分群成为 REQUIRED；PT4 未因 Guard 产生 Defense vs Feeding precedence 压力。FIRST_MATCH 响应分档的行 priority 是模板内部既定比较语义，不是新买 PT4。C13 仍按范围解决，不制造特殊 Template。本稿完成具体表达，不替 Owner 做最终 DSL/Config 选型、生产参数冻结或全项目 closure。
'''

def build():
 csvdir=ROOT/'tables';csvdir.mkdir(exist_ok=True)
 for k,rows in data.items():
  with (csvdir/(k+'.csv')).open('w',encoding='utf-8-sig',newline='') as f:
   w=csv.DictWriter(f,fieldnames=TABLES[k]);w.writeheader();w.writerows({c:fmt(r[c]) for c in TABLES[k]} for r in rows)
 scripts=[{'binding_id':r['binding_id'],'dialect_version':'CN_PSEUDO_R2','source':dsl(r['binding_id'])} for r in data['Binding']]
 for filename,obj in [('tables.json',data),('scripts.json',scripts),('cases.json',cases),('traces.json',traces),('verification.json',assertions)]:
  (ROOT/filename).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
 totals=[{'表':k,'全列':' / '.join(TABLES[k]),'去重实际行数':len(data[k]),'权限':'只读目录' if k=='TemplateStep' else '作者数据'} for k in TABLES]
 counts=md_table(['表','全列','去重实际行数','权限'],totals)
 schema='\n## 4. 字段合同与完整全局行表\n\n'+counts
 schema+='\n所有 PK/FK 和空值约定如下。Parameter 中数值二元列表使用 range<number>，BETWEEN 包含端点；列类型不是根据显示文本猜测。\n'
 for k in TABLES:schema+='\n### '+k+'\n\n'+SCHEMA_NOTES[k]+'\n\n'+md_table(TABLES[k],data[k])
 m=INTRO+schema+'\n## 5. 每个案例：样例行 → 中文脚本 → 中间值\n'
 sections=[];notion_cases=[]
 for c in sorted(cases,key=lambda c:(0 if c['id'].startswith('C') and c['id'][1:].isdigit() else 1,c['id'])):
  rel=closure_rows(c['bindings']);related=sum(len(v) for k,v in rel.items() if k!='TemplateStep');n_tables=sum(bool(v) for k,v in rel.items() if k!='TemplateStep')
  # Global table rows appear once in Markdown; HTML expands the complete per-case dependency closure.
  cm='\n### '+c['id']+'｜'+c['title']+'\n\n'+c['note']+'\n\n'
  if not c['bindings']:cm+='Boundary 表中已列出，执行表与脚本均不适用。\n';m+=cm;notion_cases.append(cm);sections.append('<section class="case" data-search="'+html.escape(c['id']+' '+c['title'])+'"><h2>'+html.escape(c['id']+' '+c['title'])+'</h2><p>'+html.escape(c['note'])+'</p></section>');continue
  cm+='样本涉及 '+str(n_tables)+' 张作者表、'+str(related)+' 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。\n\n'
  cm+='输入：\n```json\n'+json.dumps(c['facts'],ensure_ascii=False,indent=2)+'\n```\n'
  lhs='';rhs=''
  for k,rows in rel.items():
   if rows:lhs+='<details><summary>'+html.escape(k)+' · '+str(len(rows))+' 行</summary>'+ht_table(TABLES[k],rows)+'</details>'
  for b in c['bindings']:
   src=dsl(b);cm+='\n**'+b+'**\n```text\n'+src+'\n```\n';rhs+='<h4>'+b+'</h4><pre>'+html.escape(src)+'</pre>'
   tr=next(t for t in traces if t['binding']==b);cm+='\n本例结果：\n```json\n'+json.dumps(tr,ensure_ascii=False,indent=2)+'\n```\n';rhs+='<details open><summary>中间值与结果</summary><pre>'+html.escape(json.dumps(tr,ensure_ascii=False,indent=2))+'</pre></details>'
  m+=cm;notion_cases.append(cm)
  sections.append('<section class="case" data-search="'+html.escape(c['id']+' '+c['title'])+'"><h2>'+html.escape(c['id']+' '+c['title'])+'</h2><p>'+html.escape(c['note'])+'</p><p class="small">'+str(n_tables)+' 张作者表 · '+str(related)+' 行引用闭包（全局去重另计）</p><details><summary>完整输入快照</summary><pre>'+html.escape(json.dumps(c['facts'],ensure_ascii=False,indent=2))+'</pre></details><div class="pair"><div><h3>A · 实际配置行</h3>'+lhs+'</div><div><h3>B · 等义中文伪脚本</h3>'+rhs+'</div></div></section>')
 m+='\n'+ENGINEERING+'\n## 9. 本次复算\n\n静态引用/槽位/Predicate 无环/数值范围校验，加上独立手算预期值对照。中文文本是同一模板的展开显示，尚无独立 DSL 解析器，所以这些复算证明的是样本表及展示计算的一致性，不能声称两套生产编译器已经语义等价。\n\n'+md_table(['check','actual','expected','status'],[{**{'actual':'—','expected':'—'},**r} for r in assertions])
 (ROOT/'authoring-concrete-r2.md').write_text(m,encoding='utf-8')
 # Publish global rows and scripts, without repeating shared rows for every case.
 ns=INTRO.replace('# FCF Authoring 具体化样本 R2｜配置表、中文伪脚本与逐步结果','## 25. Concrete Authoring Specimens R2｜全表列、样例行与等义中文脚本',1)
 import re
 def convert_md_tables(txt):
  lines=txt.splitlines();out=[];i=0
  while i<len(lines):
   if lines[i].startswith('| ') and i+1<len(lines) and lines[i+1].startswith('| ---'):
    cols=[x.strip() for x in lines[i].strip('|').split('|')];rows=[];i+=2
    while i<len(lines) and lines[i].startswith('| '):
     vals=[x.strip() for x in lines[i].strip('|').split('|')];rows.append(dict(zip(cols,vals)));i+=1
    out.append(nt_table(cols,rows))
   else:out.append(lines[i]);i+=1
  return '\n'.join(out)
 def notion_links(txt):return re.sub(r'\[([^\]]+)\]\((https://app\.notion\.com/p/[a-f0-9]+)\)',r'<mention-page url="\2"/>',txt)
 # Page appendix uses own subheadings; native table grammar only.
 ns=re.sub(r'^## ([123])\. ',lambda m:'### 25.'+m.group(1)+'. ',ns,flags=re.M)
 chunks=[notion_links(ns),'### 25.4. 表布局与字段合同\n'+nt_table(['表','全列','去重实际行数','权限'],totals)]
 for k in TABLES:chunks.append('### R2-A / '+k+'\n'+SCHEMA_NOTES[k]+'\n'+nt_table(TABLES[k],data[k]))
 chunks.append('### 25.5. 每个案例的完整中文脚本、输入与结果')
 chunks+=[c.replace('\n### ','\n#### ',1).lstrip() for c in notion_cases]
 chunks.append(notion_links(convert_md_tables(re.sub(r'^## ([678])\. ',lambda m:'### 25.'+m.group(1)+'. ',ENGINEERING,flags=re.M))))
 chunks.append('### R2-C｜Self-QA 与 Worker Cold Review\n样本静态校验与 '+str(len(assertions))+' 项手算/边界复算通过。Worker Cold Review 检查：没有把演示值提升为 Authority；没有恢复 C06/C07 Feeding fallback；C08 仍为固定双通道；C09–C11 没有新建身份合同；C12 无单一动机断言；C13 情景未计作生产新模板；中文文本没有省略 Profile 实际曲线或表格端的固定聚合。独立审核结论另行写入，不以 Self-QA 代替独立 Reviewer。')
 for i,ch in enumerate(chunks):
  (ROOT/f'notion-{i:02}.md').write_text(ch,encoding='utf-8')
 # A standalone, self-contained reader; no CDN, no tracking, no framework.
 page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FCF 具体配置与中文脚本 · R2</title><style>
 :root{color-scheme:light;--ink:#15352e;--soft:#ecf3ef;--line:#d4e0d9;--accent:#17624d}*{box-sizing:border-box}body{margin:0;background:#f6f7f2;color:var(--ink);font:16px/1.7 system-ui,-apple-system,'PingFang SC',sans-serif}header,main,footer{max-width:1480px;margin:auto;padding:32px}header{padding-top:64px}h1{font-size:clamp(30px,4vw,54px);line-height:1.2;max-width:1000px}h2{font-size:26px;line-height:1.4}h3{margin-top:20px}a{color:var(--accent)}.eyebrow,.small{font-size:13px;color:#526b61}.badge{border:1px solid var(--line);border-radius:20px;padding:6px 12px;display:inline-block;margin-right:8px;background:white}.flow{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:24px 0}.flow b{padding:14px 20px;background:#deebe1;border-radius:8px}.toolbar{position:sticky;top:0;z-index:3;background:#f6f7f2ee;backdrop-filter:blur(10px);border-block:1px solid var(--line);padding:12px;display:flex;gap:8px;flex-wrap:wrap}input,select,button{font:inherit;padding:10px 14px;border:1px solid #afc4b6;border-radius:6px;background:white;color:var(--ink)}input{flex:1;min-width:170px}.case{background:white;padding:26px;border:1px solid var(--line);border-radius:12px;margin:24px 0;scroll-margin-top:95px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:22px;min-width:0}.pair>div{min-width:0}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:12px;line-height:1.5}th,td{padding:8px 10px;text-align:left;border:1px solid var(--line);vertical-align:top}th{background:#e8f0e9;white-space:nowrap}details{border:1px solid var(--line);border-radius:6px;margin:8px 0;padding:10px}summary{cursor:pointer;font-weight:600}pre{font:13px/1.65 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap;overflow-wrap:anywhere;padding:16px;border-radius:6px;background:#f0f5f1;margin:8px 0;max-height:900px;overflow:auto}.notice{padding:18px 22px;background:#fff4d9;border-left:4px solid #ab7b29}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:24px 0}.stats>div{padding:18px;background:#e7eee5;border-radius:8px}.stats strong{display:block;font-size:32px}.hide{display:none}.single .pair{grid-template-columns:1fr}.single .pair>div:first-child{display:none}@media(max-width:850px){header,main,footer{padding:20px}.pair{grid-template-columns:1fr}.stats{grid-template-columns:1fr 1fr}.case{padding:16px}}@media print{.toolbar{display:none}details>*{display:block}.case{break-inside:avoid}pre{max-height:none}.pair{grid-template-columns:1fr}}
 </style><header><span class="eyebrow">FCF / AUTHORING REPRESENTATION / R2</span><h1>配置到底填什么，<br>中文脚本到底怎么写。</h1><p>左边是完整样例行，右边是展开后的中文执行逻辑。相同输入、相同曲线、相同结果。</p><span class="badge">WORKING · 未选型</span><span class="badge">全数值为演示</span><span class="badge">保留历史投影</span><div class="flow"><b>只读快照</b>→<b>具名条件 / Profile</b>→<b>固定因果步骤</b>→<b>类型化结果</b></div><div class="notice">“两张 Profile”不等于 Selector；“8条 PARTIAL”不等于都要继续查鱼。当前演示沿用最新 Design Gate，具体数值仍与生产决策分开。</div><div class="stats"><div><strong>11 + 1</strong>表格：作者表 + 模板目录</div><div><strong>5 + 1</strong>脚本：共用表 + 文本集合</div><div><strong>15</strong>原案例含范围外边界</div><div><strong>5</strong>鲈鱼群体完整投影</div></div><p><a href="authoring-concrete-r2.md">完整中文文档</a> · <a href="tables.json">完整表数据</a> · <a href="scripts.json">全部中文脚本</a> · <a href="verification.json">复算记录</a></p></header><main><div class="toolbar"><input id="search" aria-label="搜索案例" placeholder="搜索 C08、鲈鱼、Q3…"><select id="group" aria-label="选择案例组"><option value="all">所有案例</option><option value="C">C01–C15</option><option value="BASS">鲈鱼五群</option><option value="G">Group 条件</option><option value="Q">Quality 修正</option></select><button id="mode">只看脚本</button><button id="expand">展开当前案例的全部表</button></div>'''
 page+='<section class="case"><h2>全局表头与实际行数</h2><p>行数按本文件去重，不把每例重复引用的共享行重复相加。TemplateStep 是工程提供的固定目录。</p>'+ht_table(['表','全列','去重实际行数','权限'],totals)+'<details><summary>字段类型、主键与规则</summary>'+''.join('<h3>'+k+'</h3><p>'+html.escape(v)+'</p>' for k,v in SCHEMA_NOTES.items())+'</details></section>'
 page+=''.join(sections)
 page+='<section class="case"><h2>同一修改，改哪里？</h2><p>C06 入侵强度0.5的响应从0.6改0.65：两边都只改共享 CurvePoint 的一格。C08 的 MAX 改平均：两边都要修改聚合逻辑与验证；表格版不能把它伪装成普通 Profile 调参。</p><p>C03 再加一个 AND 子条件：表格增加 Parameter、Predicate 和 PredicateMember 三行；脚本增加 Parameter 并展开条件表达式。两边都要验证输入是否已被准入。</p><p>全量修改定位、身份边界和表统计口径见完整中文文档第6–9节。</p></section></main><footer>本页是同一具名样本包的阅读视图。演示模板目录不等于 L_final；未实现生产 DSL 编译器，未 Promote。独立审查结果见随附 review 文件。</footer><script>const search=document.querySelector("#search"),group=document.querySelector("#group");function filter(){let q=search.value.toLowerCase(),g=group.value;document.querySelectorAll(".case[data-search]").forEach(e=>{let t=e.dataset.search;e.classList.toggle("hide",!t.toLowerCase().includes(q)||(g!=="all"&&!t.startsWith(g)))});}search.oninput=filter;group.onchange=filter;document.querySelector("#mode").onclick=function(){document.body.classList.toggle("single");this.textContent=document.body.classList.contains("single")?"左右对照":"只看脚本"};document.querySelector("#expand").onclick=()=>document.querySelectorAll(".case:not(.hide) details").forEach(e=>e.open=true);</script></html>'
 page=page.replace('</style>','body{overflow-wrap:anywhere}.scroll{max-width:100%}details{min-width:0}</style>').replace('.case:not(.hide) details','.case[data-search]:not(.hide) details')
 page=page.replace('<a href="verification.json">复算记录</a>','<a href="verification.json">复算记录</a> · <a href="independent-review.md">独立审核记录</a> · <a href="https://app.notion.com/p/3d6a4137d236814ea872ed6305942594">Notion 正文 §25</a>')
 (ROOT/'index.html').write_text(page,encoding='utf-8')
 print(json.dumps({'bindings':len(data['Binding']),'cases':len(cases),'checks':len(assertions),'tables':{k:len(v) for k,v in data.items()},'notion_chunks':len(chunks),'doc_characters':len(m)},ensure_ascii=False))
build()
