# -*- coding: utf-8 -*-
"""CENSUS-REBUILD-003 merge-test engine + semantic verdicts.

Opens template_registry.yaml v9 (post-freeze, read-only; zero mutation) and
compares each frozen truth body against the live Bake-family canonicals by
structural signature. Engine layer reports raw signature matches; the
semantic layer (worker adjudication below) applies family-domain reading per
work standards 2.3/6.4 + RB-1/RB-2 precedents:
  - 同签名不同轴类别序列=语义层 non-match（ORDER/OPERATOR 轴域——RB-2 判例）；
  - RB-1 提案形状（FF/SF）不在 registry——NEW 轨备注 related_proposal=HRQ-RB1-02
    （判同只对 registry v9 活族 18）；
  - C9/brooted/form_hold 特例产出=HRQ 终裁提案（HRQ-RB3-03/04/05），registry 零改动。
"""
import json, os, datetime, hashlib
import yaml

ROOT = r"A:\Projs\FCF-Harness-Handoff\programaticHitFish"
CEN = os.path.join(ROOT, "fish_logic_census")
BATCH = "CENSUS-REBUILD-003"
OUT = os.path.join(CEN, "batches", BATCH)

CANON = {
    "TIERED_SINGLE_FACTOR_CHAIN": dict(sig=["EVAL"], note="单 typed 因子三档渐进"),
    "LAYER_AXIS_DUAL_TIER_CHAIN": dict(sig=["EVAL", "EVAL"],
        note="水层软三档->premise 绑定轴段三档（第二步=premise 轴段——轴域限定）"),
    "GATED_COVER_TIER_CHAIN": dict(sig=["GATE", "EVAL"], note="结构掩体存在门->掩体/单档（factor_type typed 参数）"),
    "NOCTURNAL_LIGHTSLOT_CHAIN": dict(sig=["EVAL", "SLOT"], note="夜行底板档->低光槽（adjuster，槽位判例固定）"),
    "ZONE_SUBSTRATE_RESOURCE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL"], note="GATE_ZONE 底层硬定位->底质档->资源档"),
    "SOFT_TRIPLE_TIER_CHAIN": dict(sig=["EVAL", "EVAL", "EVAL"], note="近底带软三档->底质档->资源档（无门）"),
    "ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL"], note="GATE_ZONE->深度档->底质档->资源档"),
    "GUARD_ANCHOR_TIERED_COMBINE_CHAIN": dict(sig=["GATE", "EVAL", "EVAL", "EVAL"], note="锚存在门->锚适配->关系->局部温度（anchor 四形式轴）"),
}

TS = "TIERED_SINGLE_FACTOR_CHAIN"; GC = "GATED_COVER_TIER_CHAIN"
GA = "GUARD_ANCHOR_TIERED_COMBINE_CHAIN"; NO = "NOCTURNAL_LIGHTSLOT_CHAIN"
ZS = "ZONE_SUBSTRATE_RESOURCE_CHAIN"; ST = "SOFT_TRIPLE_TIER_CHAIN"
LA = "LAYER_AXIS_DUAL_TIER_CHAIN"
FF = "FORAGE_FIRST_DUAL_TIER_CHAIN__RB1"
SF = "SPACE_FIRST_DUAL_TIER_CHAIN__RB1"
C9_BLU = "STRUCTURE_FIRST_QUAD_TIER_CHAIN__RB3"          # 新形状证据 1（结构先行四步 EVAL）
C9_RBP = "LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN__RB3"        # 新形状证据 2（三步 EVAL 温度中置）
C9_HNC = "GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN__RB3"     # 新形状证据 3（门化四步 结构先行）
C9_ARA = "GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN__RB3"     # 新形状证据 4（门化四步 温度次置）
BROOD = "BROODED_DEGENERATE_TWO_STEP_CHAIN__RB3"         # 新形状证据 5（退化链两步——brooded 结构级）

V = {}

def add(sid, verdict, target, note, *, rel=None, ru=None, hrq=None):
    V[sid] = dict(verdict=verdict, target=target, note=note, rel=rel, ru=ru, hrq=hrq)

# ---------- 第 4 层 110：TS 轴段/低分辨率单步（29） ----------
for sid, note in [
    ("BRT3", "生态型绑定轴段单步（P05 lifecycle premise 配置级——PREMBIND 不变量）；与 BRT12/BRT4 同种多 story 去重联动"),
    ("BRT4", "求偶竞争场轴段单步（无 Nest guard 前提——story 明言 P04 仅竞争参照）；空间分辨率=配对场单轴段"),
    ("AEL2", "降海廊道轴段单步（P05）；『Lifecycle 与 Spatial 通达；阶段存在不必创建 Mode』"),
    ("BIB2", "洪泛繁殖通达轴段单步（P05）；群聚不单独购买 Group"),
    ("GAR3", "洪泛繁殖通达轴段单步（P05 洪水入口）；与 GAR-0 普通捕食分开（story 判语）"),
    ("YEP2", "产卵植被底质带轴段单步（P05）；卵带是环境事实不自动成为冲突对象"),
    ("MUL2", "降海廊道轴段单步（P05）；同种群游不单独购买 Group"),
    ("RAI3", "生态型绑定轴段单步（resident↔steelhead 同种不同生活史）"),
    ("SOK2", "溯河返廊道轴段单步（P05）；捕获动机未定（snagging 不当机构结论）"),
    ("SAL1", "溯河廊道轴段单步（P05）；不必新建 Return Mode（story 判语）；B 层样板链序同构独立确认"),
    ("PAD5", "溯河产卵廊道轴段单步（P05）；觅食资源与繁殖通达分开；同种三 story 去重联动（PAD1/PAD5/PAD34）"),
    ("SEA2", "阶段绑定轴段单步（三阶段 lifecycle premise）；幼体场输入与寄生分别交适当 owner"),
    ("COD2", "繁殖聚集场轴段单步（发声求偶竞争——无守巢前提）；同种三 story 去重联动（COD1/COD2/RB-2 COD）"),
    ("GRA2", "流水产卵轴段单步（P05+停食 premise F02）；与草鱼 P02 摄食面双 story 分工"),
    ("TIL3", "雄鱼领地轴段单步（Territory relation——非 brooded：领地与雌鱼口哺非同一关系对象）；brooted 终裁联动 HRQ-RB3-04"),
    ("BSH1", "盐度梯度廊道轴单步（广盐通达=唯一硬分野维；机会捕食=离散响应）；同形于 RB-2 廊道轴段族成员判法"),
    ("BRC", "单步链 MC（S1=EO 摄食对象未闭合——CSV 软定位单因子分辨率；RB-2 品系轨同型处理）"),
    ("CHS", "单步链 MC（S1=EO 猎物链未闭合——浅水溪流带单因子；不新增 Flow Mode）"),
    ("CLC", "单步链 MC（R03 story 夜行未闭合+CSV 全天——底层遮蔽带单因子，夜槽不虚构）；CLC 双 story 分层对账挂 HRQ-RB3-01"),
    ("LJB", "单步链 MC（物种级行为字段稀疏——中上水层带低强度单因子；不用近缘鲌类资料填补）"),
    ("TNS", "单步链 MC（identity-only 低置信 placeholder——shallow-flow 带单因子；不 promote 机制）"),
    ("STL", "季节绑定底穴轴段单步（冬穴-春溯 P05 premise；触须=Response 层注记）"),
    ("IDE", "个体发生轴段单步（幼沿岸↔成深水 P05 premise 配置级）；B 层样板链序同构独立确认"),
]:
    add(sid, "MERGE_CONFIDENT", TS, note)

# 品系/近亲/杂交轨（4）+鲫系（2）
for sid, note in [
    ("KOI", "单步链 MC（锦鲤品系 Identity Deferred——继承鲤基线 benthopelagic_slowwater_band 单因子）；RB-2 品系 8 尾『亲本 R03 轨补证』开放项闭合（本体同形——品系无需升档，0 冲突）"),
    ("MIR", "单步链 MC（镜鲤品系——鳞被表型=身份限定；同 KOI 同形）；RB-2 品系先例复用"),
    ("WRC", "单步链 MC（荷包红鲤地方品系——红色表型不推导机制）；同批三品系轨同形（KOI/MIR/WRC）"),
    ("RTL", "单步链 MC（Oreochromis 杂交身份不稳定——低强度温水杂食带单因子；Confidence=Low 忠实记录）；近亲种轨（TIL2/TIL3=O. niloticus）分列不互并"),
    ("GCR", "单步链 MC（黄金鲫杂交标签——鲫系底栖杂食带单因子；与 RB-1 HYC 同形对照）"),
    ("WCR2", "单步链 MC（野生鲫鱼物种级基线——鲫系单因子；『早口』不作为硬触发器）"),
]:
    add(sid, "MERGE_CONFIDENT", TS, note)

# field 场浓度单步（19——factor_type=field 轴值读法，RB-2 BHC/HER 判例复活）
FIELD_NOTE = "单步场浓度 EVAL MC（factor_type=field 轴值读法——B2 判例复活/RB-2 BHC/HER 同型；evaluand=场，Bake 面=场分布权重；Response 面 FOOD_FIELD 投影注记另轨）"
for sid, extra in [
    ("BIB1", "滤食场（P03 typed FoodField——story 直证；B 文件 bubalus 底质吸食面为亚口科种级区分"),
    ("SOK1", "浮游场（P03——B 文件 sockeye 滤食登记的预留复核点兑现）"),
    ("PAD1", "滤食场（P03——CSV 行滤食面；电感受面=RB-2 PAD34 另轨）"),
    ("TIL2", "附着-悬浮颗粒场（P03——刮食+悬浮双通道=Response 层 OPERATOR UNDEFINED 标注）"),
    ("MAC1", "移动饵场-浮游场（P03——群体=发现层线索）"),
    ("JCK1", "浮游-小鱼场（P03——B 层三步受限还原不采）"),
    ("CAP1", "浮游场（P03+繁殖近岸窗 premise）"),
    ("SIL1", "浮游植物水柱场（P03——BHC canonical 同型参数差异化；鲢鳙同型不分裂）"),
    ("MDC2", "附着-碎屑场（P03——同属鲮行级不互并）"),
    ("XCD", "附着层场（P03——连续 FieldFeeding 与离散钓获边界交下游 owner）"),
    ("ROH", "植物-基质场（P06 语义→场浓度单因子；季风洄游 premise）"),
    ("MRC", "浮游-底柱场（P03——机制开放留给证据闭合）"),
    ("SPR", "有机泥-腐屑场（P06 吸泥食腐——口特化；长距洄游 premise）"),
    ("CHM", "硅藻-附着层场（P06 凿板刮食——形态特化归 Response/Profile 值域；幼成切换 premise）"),
    ("SHB", "表层悬浮-漂流物场（P03——上层属性由 Spatial 表达）"),
    ("GTB", "洪泛果实-腐屑场（P06——洪泛季果实窗+幼成栖息分异双 premise；B 文件 REV-001 撤回档不采）"),
    ("WCB", "沉水草床场（P06 选择性放牧——植物种类选择性=Profile 值域非结构）"),
    ("WBL", "细颗粒滤食场（幼体 ammocoete premise——成体面挂 owner 边界开放；与海七鳃鳗寄生阶段分型）"),
    ("BON1", "移动饵场（P03 FieldFeeding+downstream TargetFeeding）"),
]:
    add(sid, "MERGE_CONFIDENT", TS, FIELD_NOTE + "；" + extra)

# NO 夜行底板+低光槽（8）
for sid, note in [
    ("WAL2", "低光结构底板->低光槽：canonical 同构（视觉生理特化先行——tapetum 反光结构=RB 主句首句；槽邻档承载白天深水遮蔽；与 RB-2 WAG 同种双 story 去重联动）"),
    ("AEL1", "底层掩体底板->低光槽：canonical 同构（白天隐蔽/夜间摄食 story 直证）"),
    ("CCF1", "砂砾底层底板->低光槽：canonical 同构（CSV demersal/夜间活跃；气味=sensory Context 不另立面）"),
    ("WCF1", "深槽-回水底板->低光槽：canonical 同构（Soldatov 六须鲡——与 RB-2 WEL 欧洲六须鲡同科不同种不继承）"),
    ("SZE1", "浑水河道底板->低光槽：canonical 同构（CSV 夜间活跃；与 WAL2 同属不同种不继承）"),
    ("ASC2", "泥沼底板->低光槽：canonical 同构（story 判语『空气呼吸不自动创建 Night Mode』——夜槽=CSV/story 夜行；洪泛迁移=相邻 premise 不双重结算）"),
    ("BBR1", "泥底缓流底板->低光槽：canonical 同构（低光夜间底层觅食 story 直证；护卵=相邻面注记）"),
    ("MRG", "穴居底板->低光槽：canonical 同构（B 文件边界条款兑现：story 正文证实夜行低光主导→GC 换 NO 结构变更按文件预留路径——独立审复核点）"),
]:
    add(sid, "MERGE_CONFIDENT", NO, note)

# GC 掩体门+质量（6）
for sid, note in [
    ("PIK1", "GATE 植被掩体->掩体档：canonical 同构（S18 伏击 story——与 S20 Static Habitat 同种两 story 两读法互指=B 文件判语原样；与 RB-2 PIK19 繁殖面去重联动）"),
    ("BWF", "GATE 沼泽植被->掩体档：canonical 同构（story 明言无 universal night-only rule——无夜槽）"),
    ("BSN", "GATE 表层植被->掩体档：canonical 同构（气呼吸=栖地持续性非摄食通道；breeding guard=相邻开放 story）"),
    ("YCF", "GATE 底层洞隙->掩体档：canonical 同构（demersal 硬定位+S8 底质巢穴持久线索；守巢=相邻 Relation/Guard 候选另轨）"),
    ("CPT", "GATE 植被掩体->掩体档：canonical 同构（狗鱼科伏击形——PIK1/MUS 同科形各自推导）"),
    ("MUS", "GATE 掩体边缘->掩体档：canonical 同构（cover and edge habitat 主句；大体型目标=通道参数）"),
]:
    add(sid, "MERGE_CONFIDENT", GC, note)

# GA 锚四步（7）
for sid, note, anchor in [
    ("CRA2", "锚存在门->巢址->关系->局部温度：canonical 同构（雄鱼筑巢护卵至孵化=本种证据——构建型；建立期选址先行/照护期占位在后）；MUT 批落位表 nest 同向", "nest（构建型）"),
    ("SMA1", "锚存在门->锚址->关系->局部温度：canonical 同构（两阶段锚=Resolver 实例配置级切换不设 body 分支——B 文件 §11.2 泛化判例）；与 RB-2 SMA 摄食面不同面去重联动", "nest↔fry_school（两阶段实例切换）"),
    ("BLU2", "锚存在门->巢床->关系->局部温度：canonical 精确同构（canonical 源同种同面直验——B01-S38 story 证据 vs B 文件 §2.2 双源一致）", "colony_nest（nest 构建型——殖民巢群）"),
    ("CCF2", "锚存在门->洞巢址->关系->局部温度：canonical 同构（洞巢=利用型附着非构建）；吃卵触发条件=证据开放注记", "egg_mass（洞巢利用型）"),
    ("DIS2", "锚存在门->群栖境->贴群关系->局部温度：canonical 同构（移动锚判『稚鱼群所在栖境』——B 文件判例）；色型不分裂（S12——本批独立推导同向）", "fry_school（贴附黏液幼鱼群）"),
    ("CSN1", "锚存在门->植被掩体群栖境->环护->局部温度：canonical 同构（B 文件 §0 锚点直证；稚鱼群存在已在路由面结算 Bake 不重复）；互斥态（伏击 NONE/护幼 PARENTAL_GUARD）=路由面", "fry_school（浮巢孵化后稚鱼群）"),
    ("RSB", "锚存在门->蚌床->产卵关系->局部温度：canonical 同构（Relation Object=活淡水蚌——story 直证『不能并入普通 TargetFeeding』）", "host_brood（蚌宿主——四形式既有值；B7 EXT 轨 mussel_brood 提案落位确认）"),
]:
    add(sid, "MERGE_CONFIDENT", GA, note + "；anchor=" + anchor)

add("BDR2", "MERGE_CONFIDENT", ZS,
    "GATE_ZONE 底层->底质可翻性->底栖猎物丰度：canonical 同构（翻底物理依赖推导与 B 文件独立同序确认——DRU 同型）")
add("CAR1", "MERGE_CONFIDENT", ST,
    "近底软层->底质可拱性->底栖猎物斑块三步无门：canonical 同构（benthopelagic 软定位首步无门——与 B 文件同序独立确认；翻拱痕迹=世界侧可见性事实不改鱼程序）")
add("RED2", "MERGE_CONFIDENT", LA,
    "潮位水深层->幼成廊道轴两步：canonical 同构（垂直层+水平廊道两独立维 story 直证——RB-2 csv_anchor_standard 同型；与 RED1 同种双 story 去重联动）")

# FF 食性先行（8——RB-1 提案形状）
for sid, note in [
    ("RED1", "真形两步[底栖甲壳斑块->浅水草区带]：食性/行为主句先行——RB-1 FF 提案形状；与 RED2 同种双 story 去重联动"),
    ("RAI2", "真形两步[鲑卵/尸体脉冲斑块->漂流近底带]：季节脉冲型食性主句先行（BRT12 同型）——RB-1 FF 提案形状"),
    ("COD1", "真形两步[多鱼种-无脊椎猎物场->陆架底层带]：食性主句先行——RB-1 FF 提案形状；同种三 story 去重联动"),
    ("BET", "真形两步[中深层鱼-鱿场->昼夜温跃层带]：移动机会先行（PBF/SAF/YFT 海洋追击型同向）——RB-1 FF 提案形状"),
    ("STB", "真形两步[饵鱼集中斑块->河口流带]：follows bait 食性先行——RB-1 FF 提案形状；洄游=lifecycle premise"),
    ("MAH", "真形两步[饵鱼群场->漂浮物表层带]：饵鱼集中先行（Structure exposes the opportunity）——RB-1 FF 提案形状"),
    ("BKC", "真形两步[硬壳软体斑块->河湖底层带]：食物载体先行（SS 先寻找螺贝集中句）——RB-1 FF 提案形状"),
    ("RST1", "真形两步[底栖资源场->河海底层廊道]：食性主句先行（RB 首句=底栖摄食者；vs SS2 同属通达先行——story 语序差异各自推导）——RB-1 FF 提案形状"),
]:
    add(sid, "NEW_TEMPLATE_CANDIDATE", FF, note, rel="HRQ-RB1-02", hrq="HRQ-RB3-02")

# SF 空间先行（27——RB-1 提案形状）
for sid, note in [
    ("CRA1", "真形两步[清水结构带->阶段分级猎物场]：结构栖息先行（体型=premise）——RB-1 SF 提案形状"),
    ("YEP1", "真形两步[植被水层带->阶段分级猎物场]：植被掩体先行——RB-1 SF 提案形状；与 YEP2 去重联动"),
    ("MUL1", "真形两步[基质连续处理带->碎屑-生物膜场]：基质（食物载体）先行（P06 Compression）——RB-1 SF 提案形状；与 MUL2 去重联动"),
    ("TEN1", "真形两步[静水植被带->底层杂食资源]：静水植被先行——RB-1 SF 提案形状"),
    ("LWF1", "真形两步[湖底带->季节深浅轴]：底层带先行+季节轴独立维——RB-1 SF 提案形状（B 文件 P03 滤食面为另一 story 域双批分工）"),
    ("SBS1", "真形两步[溪流底质带->底层离散资源]：空间搜索点先行（Evidence Open 策略假设忠实记录）——RB-1 SF 提案形状"),
    ("SBH1", "真形两步[河流带->底层资源]：同 SBS1 型（同属不同种行级不互并）——RB-1 SF 提案形状"),
    ("HMB", "真形两步[近岸中上带->小型猎物场]：水层结构先行——RB-1 SF 提案形状"),
    ("IRS", "真形两步[河流-洪泛带->体型分级杂食场]：水位河段先行——RB-1 SF 提案形状；洪泛迁移=相邻 premise"),
    ("LNK", "真形两步[冷水溪流结构带->漂流鱼虫场]：水温情境（冷水结构）先行——RB-1 SF 提案形状"),
    ("MRF", "真形两步[中上流速带->追猎猎物场]：水层流速先行——RB-1 SF 提案形状（B 文件明暗门受限还原不采）"),
    ("SPS", "真形两步[砾石河段带->底栖无脊椎场]：底质河段先行——RB-1 SF 提案形状（CGD 同型）"),
    ("STM", "真形两步[浅水植被缘带->小型无脊椎-卵幼场]：植被边缘先行——RB-1 SF 提案形状；鱼卵摄食≠守巢关系"),
    ("TPC", "真形两步[中上流速带->追捕猎物场]：中上流速先行（水文重排=Context 维）——RB-1 SF 提案形状"),
    ("YCK", "真形两步[中上流速带->追捕猎物场]：同 TPC 型（鲌类中上水层形——MRF/TPC/YCK/HMB 各自推导同形）——RB-1 SF 提案形状"),
    ("SB2", "真形两步[水流-岩礁带->鱼食场]：软关联结构带先行（commonly associated——非硬门）——RB-1 SF 提案形状"),
    ("WCR3", "真形两步[结构-深度带->小鱼场]：结构深度先行——RB-1 SF 提案形状；与 CRA 系同属不同种不继承"),
    ("CTT", "真形两步[冷水漂流通道带->阶段分级猎物场]：冷水漂流先行——RB-1 SF 提案形状；型态差异=lifecycle premise"),
    ("RSB2", "真形两步[岩礁硬底带->底栖猎物场]：岩礁硬底先行——RB-1 SF 提案形状"),
    ("RTB", "真形两步[流缘-清水猎道带->小鱼场]：流缘猎道先行——RB-1 SF 提案形状"),
    ("DVK", "真形两步[冷水可达带->漂流猎物场]：冷水可达先行（form changes context before response semantics）——RB-1 SF 提案形状"),
    ("GJC", "真形两步[礁缘流隔带->集群猎物场]：搜索位置先行——RB-1 SF 提案形状"),
    ("SS2", "真形两步[溯河底层廊道->底栖无脊椎场]：洄游通达先行（vs RST1 食性先行——同属语序差异）——RB-1 SF 提案形状"),
    ("BIC", "真形两步[河道边缘流道带->小鱼场]：河道边缘先行——RB-1 SF 提案形状"),
    ("SIH", "真形两步[季节陆架深度带->鱼-鱿场]：深度季节重排先行——RB-1 SF 提案形状"),
    ("YTA", "真形两步[流隔-礁缘带->饵鱼场]：搜索位置先行（GJC 同句式同形）——RB-1 SF 提案形状"),
    ("BBF", "真形两步[软底-流过渡带->底栖无脊椎场]：软底过渡带先行——RB-1 SF 提案形状；亚口科三行种级区分（BBF/BIB1/BIB2）"),
]:
    add(sid, "NEW_TEMPLATE_CANDIDATE", SF, note, rel="HRQ-RB1-02", hrq="HRQ-RB3-02")

# 复用轨 2（双 story 内容近似——reused_from）
add("FGA4", "MERGE_CONFIDENT", GC,
    "GATE 植被缘掩体->掩体档：canonical 同构；reused_from=RB-2 FGA（R02-S17 同种双 story 内容近似——B7 判例⑦点名；本批 R04 story SS 同句式独立印证）",
    ru="reused_from=CENSUS-REBUILD-002:P-RB2-FGA-BAKE（同种双 story 复用）")
add("RHM2", "MERGE_CONFIDENT", TS,
    "单步链 MC（floodplain_plant_fruit_patch 场斑块）；reused_from=RB-1 RHM（B5 R08-09 同种双 story 内容近似——patch 单因子同形；本批 P02→P01 句式独立印证）",
    ru="reused_from=CENSUS-REBUILD-001:P-RB1-RHM-BAKE（同种双 story 复用）")

# NO_SURFACE（1——非四态，显式记录）
add("GAR1", "NO_SURFACE_EFFECT", None,
    "Bake 面 NO_SURFACE_EFFECT（显式理由：取饵初次接受边界/携行挂钩=Encounter/Conversion 侧交互实例，非空间分布证据——B 文件 BOUNDARY-DECL 直证+story owner 推论原样）；Response 面档位展开照常（不在本面）；queue 条目以显式无程序消费")

# ---------- C9 立族材料 4（栖息面——终裁提案） ----------
add("BLU-HAB", "NEW_TEMPLATE_CANDIDATE", C9_BLU,
    "真形四步 EVAL[结构->软水层->宽温->晨昏]（结构先行——裁决 §6.2 原文锚『蓝鳃→结构先行』）；vs 全部活族：四步纯 EVAL 链无 canonical（ZD 带 GATE/LA 两步/ST 三步）——新形状证据 1；vs RS1 冻结体（水层->结构->水温->时段）ORDER 不同=原 C9 形证伪；C9 终裁提案=不立原族（4/4 分散）",
    hrq="HRQ-RB3-03")
add("RBP-HAB", "NEW_TEMPLATE_CANDIDATE", C9_RBP,
    "真形三步 EVAL[中上软水层->窄温带->沉水结构]（时段=全天不入链——证据驱动）；engine 签名与 ST 同 [E,E,E] 但轴类别序列不同（层-环境调制-空间 vs 层-底质-资源——语义层 non-match，RB-2 判例）；新形状证据 2；vs RS1 冻结体链长+序均不同",
    hrq="HRQ-RB3-03")
add("HNC-HAB", "NEW_TEMPLATE_CANDIDATE", C9_HNC,
    "真形 GATE+三步[底层砾石门->砾石结构->冷水->早晨]（门化=硬定位出局语义[RB-1 GRH 判例]+裁决锚『美鱥口器->水层先行』）；engine 签名与 ZD/GA 同 [G,E,E,E] 但轴类别序列不同（zone-空间-环境调制-环境调制 vs 资源链/guard 链）——语义 non-match；新形状证据 3",
    hrq="HRQ-RB3-03")
add("ARA-HAB", "NEW_TEMPLATE_CANDIDATE", C9_ARA,
    "真形 GATE+三步[底层门->窄暖温带->洪泛林结构->晨昏]（温序前置=CSV 25-29°C 窄带证据强度>结构 [需正文]——与 B 文件声明序差异为逐鱼推导产物）；vs HNC 形第 2/3 步互换=ORDER 差异（§6.2 严格判据）；新形状证据 4",
    hrq="HRQ-RB3-03")

# ---------- brooted 终裁 2 ----------
add("ARO-RESP", "NEW_TEMPLATE_CANDIDATE", BROOD,
    "退化链两步[口哺锚门->常驻区适配]（无关系轴/无温度轴——与 nile_tilapia §0 Brooding 退化链判读同构；携带型锚与个体绑定=无锚址空间关系语义）；vs GA canonical 四步=步数+轴结构差异（结构级——裁决 4 brooded 边界的形状依据）；B5 全链盲形（PARALLEL 双 Path）=P04 契约模板套用降级；brooted 终裁提案=退化链维持（口哺期摄食状态张力留 HRQ 开放项）",
    hrq="HRQ-RB3-04")
add("TIL3-RESP", "MERGE_CONFIDENT", TS,
    "雄鱼领地轴段单步（TS MC）；brooted 终裁提案=分面记账：雌鱼口哺面=退化链边界确认（B 文件直证）/雄鱼领地面=非 brooded 程序（territory=关系对象非后代空间存在形式）；原挂起登记（anchor=brooded）混淆两关系对象——读法修正提案（registry 落位随 v10 mutation 另批）",
    hrq="HRQ-RB3-04")

# ---------- form_hold 终裁 2 ----------
add("CSL-RESP", "MERGE_CONFIDENT", GA,
    "锚存在门->群栖境->护幼关系->局部温度：canonical 同构；form_hold 终裁提案=anchor 形式 fry_school（『Males guard the eggs and pelagic larvae』——larvae 阶段直证；egg 阶段无巢/附着判别词不定形[不虚构 nest/egg_mass]——与 MUT 批按初始形式落 nest 注记分歧，以 story 直证为准）；egg 阶段形式 open 留 HRQ",
    hrq="HRQ-RB3-05")
add("CSN1-RESP", "MERGE_CONFIDENT", GA,
    "锚存在门->植被掩体群栖境->环护->局部温度：canonical 同构；form_hold 终裁提案=anchor 形式 fry_school（B 文件 §0 直证『锚点：fry_school（浮巢孵化后的稚鱼群，植被区移动锚）』+story 护幼主体；初始浮巢阶段=相邻阶段不在冻结行——跨阶段留 open 而非虚构 nest）",
    hrq="HRQ-RB3-05")

assert len(V) == 118, len(V)


def op_class(step):
    op = step["op"]
    if op.startswith("GATE"):
        return "GATE"
    if op == "APPLY_DYNAMIC_SPATIAL_SLOT":
        return "SLOT"
    if "FOOD_FIELD" in op or "CONCENTRATION" in op:
        return "EVAL_FIELD"
    if "GAUGE" in op:
        return "EVAL_GAUGE"
    return "EVAL"


def body_signature(body):
    return [op_class(s) for s in body["surface_owned_logic"]["ordered_steps"]]


def main():
    bodies = [json.loads(l) for l in open(os.path.join(OUT, "blind_programs.jsonl"), encoding="utf-8")]
    reg_path = os.path.join(CEN, "template_registry.yaml")
    reg_hash_before = hashlib.sha256(open(reg_path, "rb").read()).hexdigest()[:16]
    _ = yaml.safe_load(open(reg_path, encoding="utf-8"))
    assert hashlib.sha256(open(reg_path, "rb").read()).hexdigest()[:16] == reg_hash_before

    tests = []
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stats = dict(MERGE_CONFIDENT=0, TEMPLATE_EXTENSION_CANDIDATE=0, NEW_TEMPLATE_CANDIDATE=0,
                 AMBIGUOUS_NEEDS_EXPANSION=0, NO_SURFACE_EFFECT=0)
    for b in sorted(bodies, key=lambda x: x["species_id"]):
        sid = b["species_id"]
        sig = body_signature(b)
        v = V[sid]
        raw = [tid for tid, c in CANON.items() if sig == c["sig"]]
        engine_raw_diffs = []
        if v["verdict"] == "MERGE_CONFIDENT" and v["target"] in CANON and sig != CANON[v["target"]]["sig"]:
            engine_raw_diffs.append("signature mismatch vs %s canonical" % v["target"])
        if v["verdict"] == "NEW_TEMPLATE_CANDIDATE":
            engine_raw_diffs.append("no live registry family matches derived truth signature (semantic axis-class sequence)" if raw
                                    else "no live registry family matches derived truth signature")
        if sid in ("RBP-HAB", "HNC-HAB", "ARA-HAB"):
            engine_raw_diffs.append("engine same-signature with %s — semantic axis-class sequence non-match (ORDER/OPERATOR domain)" % raw[0])
        moved = None
        tests.append(dict(
            test_id="MT-RB3-%s" % sid,
            program_id=b["program_id"], species_id=sid,
            signature=sig,
            engine_raw_same_signature_families=raw,
            engine_raw_diffs=engine_raw_diffs,
            verdict=v["verdict"],
            target_family=v["target"],
            same=v["verdict"] == "MERGE_CONFIDENT",
            param_only=[],
            structural_diffs=[] if v["verdict"] == "MERGE_CONFIDENT" else ["ORDER/步数/轴类别序列（vs 全部活族 canonical）"],
            semantic_note=v["note"],
            related_proposal=v["rel"],
            reused_from=v["ru"],
            human_review_queued=v["hrq"],
            order_derivation_status=b["order_derivation"]["status"],
            queues=b["order_derivation"]["queues"],
            ts=now,
        ))
        stats[v["verdict"]] += 1
    with open(os.path.join(OUT, "merge_tests.jsonl"), "w", encoding="utf-8") as f:
        for t in tests:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    ff = sorted(t["species_id"] for t in tests if t["target_family"] == FF)
    sf = sorted(t["species_id"] for t in tests if t["target_family"] == SF)
    c9 = sorted(t["species_id"] for t in tests if (t["target_family"] or "").endswith("__RB3"))
    mc_by_fam = {}
    for t in tests:
        if t["verdict"] == "MERGE_CONFIDENT":
            mc_by_fam[t["target_family"]] = mc_by_fam.get(t["target_family"], 0) + 1
    report = dict(
        batch=BATCH, generated_at=now,
        registry_version="v9 (read-only; zero mutation this batch)",
        n_truth_bodies=len(bodies),
        verdicts=stats,
        mc_by_family=mc_by_fam,
        related_rb1_proposals=dict(
            FORAGE_FIRST=dict(n=len(ff), members=ff,
                              cumulative="RB-1 10 -> RB-2 26 -> RB-3 34（+8）"),
            SPACE_FIRST=dict(n=len(sf), members=sf,
                             cumulative="RB-1 28 -> RB-2 34 -> RB-3 61（+27）"),
            note="RB-1 提案形状累积证据（不在 registry v9 活族——NEW 轨+related_proposal=HRQ-RB1-02）"),
        new_shapes_this_batch=dict(
            n_distinct=5, members=c9 + ["ARO-RESP（BROODED_DEGENERATE_TWO_STEP_CHAIN）"],
            note="本批 distinct 新形状=5（C9 材料 4 形状+brooded 退化链 1 形状）——RB-1 六提案外新证据，HRQ-RB3-03/04 终裁提案载体；n_new_template=5（distinct 口径）"),
        same_fish_reconciliation=dict(
            strain_track="KOI/MIR/WRC（鲤品系）+RTL（杂交）=TS 同形——RB-2 品系开放项闭合（亲本 KOI 本体补证同形，0 冲突）",
            dual_story_reuse=["FGA4<-RB-2 FGA", "RHM2<-RB-1 RHM"],
            dual_story_independent=["BRT3/BRT4/BRT12", "COD1/COD2/COD", "PIK1/PIK19", "PAD1/PAD5/PAD34",
                                    "WAL2/WAG", "SMA1/SMA", "BLU2/BLU", "TIL2/TIL3", "RSB(Bake/EXT)", "CLC(B5/R03)——挂 HRQ-RB3-01"],
            conflicts=0,
        ),
        special_adjudications=dict(
            C9="HRQ-RB3-03（不立原 C9 族——4/4 分散 4 新形状）",
            brooted="HRQ-RB3-04（ARO 退化链维持；TIL3 分面记账读法修正）",
            form_hold="HRQ-RB3-05（CSL/CSN1 anchor=fry_school——story/B 文件直证）",
            no_surface="GAR1=Bake 面显式无程序（BOUNDARY-DECL 直证，非四态单列）",
        ),
        revision="REV-RB3-001（4 特例 surface/return_type 契约标注——program_revisions.jsonl）",
    )
    with open(os.path.join(OUT, "engine_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))
    print("MC by fam:", mc_by_fam)
    print("FF", len(ff), "SF", len(sf), "RB3-new", len(c9))


if __name__ == "__main__":
    main()
