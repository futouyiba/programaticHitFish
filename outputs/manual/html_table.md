| 类型 | 面 | 成员 | 特点 | 跳转 |
|---|---|---|---|---|
| 空间先行双因子链 | Bake | 61 | 先找合适的地方，再找吃的——空间因子（水层/结构/栖境带）先行出局，猎物场第二。 | <a href="#space_first_dual_tier_chain">伪脚本</a> · <a href="#space_first_dual_tier_chain-cfg">配置表</a> |
| 觅食先行双因子链 | Bake | 34 | 镜像语序——跟着食物走优先，栖息带次之；与空间先行族因子集同、顺序相反，按顺序判据分立。 | <a href="#forage_first_dual_tier_chain">伪脚本</a> · <a href="#forage_first_dual_tier_chain-cfg">配置表</a> |
| 单因子三档链 | Bake | 94 | 全库最大族——整条空间判断只有一个 typed 因子（轴段/资源斑块/场浓度等），一步定终值。 | <a href="#tiered_single_factor_chain">伪脚本</a> · <a href="#tiered_single_factor_chain-cfg">配置表</a> |
| 结构门+质量档链 | Bake | 27 | 先过一道二元结构门（门值=gate_axis 八值之一），门内再走因子档位。 | <a href="#gated_cover_tier_chain">伪脚本</a> · <a href="#gated_cover_tier_chain-cfg">配置表</a> |
| 护巢锚门四步链 | Bake | 18 | 护巢期分布围着「守的东西」转：锚存在性硬门→锚面适配→守卫关系→温度。 | <a href="#guard_anchor_tiered_combine_chain">伪脚本</a> · <a href="#guard_anchor_tiered_combine_chain-cfg">配置表</a> |
| 夜行底板+低光槽链 | Bake | 24 | 夜行性打底，链中插一个光照档位槽。 | <a href="#nocturnal_lightslot_chain">伪脚本</a> · <a href="#nocturnal_lightslot_chain-cfg">配置表</a> |
| 水层+轴段双步链 | Bake | 7 | 第二步是生命周期轴段（深度带/洄游廊道）而非空间因子——轴域限定是与镜像双因子族的分界。 | <a href="#layer_axis_dual_tier_chain">伪脚本</a> · <a href="#layer_axis_dual_tier_chain-cfg">配置表</a> |
| 底带硬门+底质+资源链 | Bake | 7 | 非底层直接出局（硬门），然后底质档、资源档。 | <a href="#zone_substrate_resource_chain">伪脚本</a> · <a href="#zone_substrate_resource_chain-cfg">配置表</a> |
| 软三步无门链 | Bake | 3 | 无硬门，三步软档直连（跨科重复，PROV 系）。 | <a href="#soft_triple_tier_chain">伪脚本</a> · <a href="#soft_triple_tier_chain-cfg">配置表</a> |
| 底带门五步链（含深度档） | Bake | 2 | 底带门+深度档+底质+资源，五步形。 | <a href="#zone_depth_substrate_resource_chain">伪脚本</a> · <a href="#zone_depth_substrate_resource_chain-cfg">配置表</a> |
| 底质门→深冷带→资源链 | Bake | 4 | 深冷水种（白鲑/黄鲈）：底质门先行，接着深冷复合带，再资源。 | <a href="#gate_substrate_tempband_resource_chain">伪脚本</a> · <a href="#gate_substrate_tempband_resource_chain-cfg">配置表</a> |
| 护巢四步+浊度语境链 | Bake | 2 | 护巢锚门四步后加一个浊度修饰步（浑水种淡水石斑/朱氏鲈）。 | <a href="#guard_anchor_turbidity_context_chain">伪脚本</a> · <a href="#guard_anchor_turbidity_context_chain-cfg">配置表</a> |
| 结构→夜槽→猎物三步链 | Bake | 2 | 夜行结构种（石斑/寡鳞胡瓜鱼？）——结构定位→低光槽→猎物。 | <a href="#structure_lightslot_forage_triple_chain">伪脚本</a> · <a href="#structure_lightslot_forage_triple_chain-cfg">配置表</a> |
| 栖息→猎物+洪泛槽链 | Bake | 2 | 栖息→猎物双步，链尾挂洪泛连通槽（modifier 非 gate；巴沙/斯氏鳊）。 | <a href="#habitat_forage_floodslot_chain">伪脚本</a> · <a href="#habitat_forage_floodslot_chain-cfg">配置表</a> |
| 双硬门因子集链 | Bake | 2 | 生死门前置：水面可达+温度极值双硬门，过了门才轮到因子集（肺鱼/电鳗；电感知不进 Bake）。 | <a href="#hard_gated_factor_combine">伪脚本</a> · <a href="#hard_gated_factor_combine-cfg">配置表</a> |
| 极值门+无序因子集链 | Bake | 1 | 极值温度门+因子无序集（OSC 出族单成员，PROV）。 | <a href="#extreme_temp_gated_tiered_combine_chain">伪脚本</a> · <a href="#extreme_temp_gated_tiered_combine_chain-cfg">配置表</a> |
| patch 门+双槽档链 | Bake | 1 | 资源斑块门+双槽档位（BRT 出族单成员，PROV）。 | <a href="#patch_gated_dual_slot_combine_chain">伪脚本</a> · <a href="#patch_gated_dual_slot_combine_chain-cfg">配置表</a> |
| 结构先行四步链 | Bake | 1 | 蓝鳃栖息面真形：结构→…四步，结构第一（用户裁正「蓝鳃可能结构第一」的推导证实）。 | <a href="#structure_first_quad_tier_chain">伪脚本</a> · <a href="#structure_first_quad_tier_chain-cfg">配置表</a> |
| 门化结构先行四步链 | Bake | 1 | 美鱥栖息面真形：先一道门（口器/底栖形态锚），结构先行四步。 | <a href="#gated_structure_temp_time_quad_chain">伪脚本</a> · <a href="#gated_structure_temp_time_quad_chain-cfg">配置表</a> |
| 水层→温度→结构三步链 | Bake | 1 | 红腹食人鱼栖息面真形：三步，时段被证据剔除（CSV 全天活跃→不入链）。 | <a href="#layer_temp_structure_triple_chain">伪脚本</a> · <a href="#layer_temp_structure_triple_chain-cfg">配置表</a> |
| 门化温度次置四步链 | Bake | 1 | 巨骨舌鱼栖息面真形：门+四步，温度第二位（25-29℃ 窄带证据压过结构[需正文]）。 | <a href="#gated_temp_structure_time_quad_chain">伪脚本</a> · <a href="#gated_temp_structure_time_quad_chain-cfg">配置表</a> |
| 口孵退化两步链 | Bake | 1 | 卵含在嘴里=没有外部锚：常驻区适配单步即终值（无关系轴/无温度轴/无合并步；银龙/罗非雌面）。 | <a href="#brooded_degenerate_two_step_chain">伪脚本</a> · <a href="#brooded_degenerate_two_step_chain-cfg">配置表</a> |
| 受约束相对庇护所（种子） | Bake | 0 | live 侧带来的外来假说——普查 7 批 284 条 non-match 0 命中，作负证据台账留册不撤。 | <a href="#constrained_relative_refuge">伪脚本</a> · <a href="#constrained_relative_refuge-cfg">配置表</a> |
| 类型化目标摄食响应 | Response | 248 | 全库最大响应族——对离散饵目标做类型化食物评价，三档决定吃不吃。 | <a href="#typed_target_response">伪脚本</a> · <a href="#typed_target_response-cfg">配置表</a> |
| 场摄食响应 | Response | 16 | 吃的是「场」（浓度/丰度）不是离散目标——RETURN 硬判据（evaluand=场）与 TYPED 分立。 | <a href="#food_field_feeding_response">伪脚本</a> · <a href="#food_field_feeding_response-cfg">配置表</a> |
| 护巢双路径并行响应 | Response | 28 | 食物∥入侵者两条路径并行评估后合并——不是切换，是并行竞争（∥ 拓扑）。 | <a href="#guard_conflict_dual_path_response">伪脚本</a> · <a href="#guard_conflict_dual_path_response-cfg">配置表</a> |
| 状态门互斥多路径响应 | Response | 2 | 先过状态门（如停食洄游态），门内互斥选径（IF 门拓扑——与 ∥ 分立）。 | <a href="#state_gated_multi_path_response">伪脚本</a> · <a href="#state_gated_multi_path_response-cfg">配置表</a> |
| 环境梯度趋避响应 | Response | 1 | 沿环境 cue 梯度趋近或避开（单例族）。 | <a href="#cue_guided_approach_avoid">伪脚本</a> · <a href="#cue_guided_approach_avoid-cfg">配置表</a> |