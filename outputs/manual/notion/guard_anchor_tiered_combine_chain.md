> **类型**：护巢锚门四步链（GUARD_ANCHOR_TIERED_COMBINE_CHAIN）｜面：Bake｜状态：CANDIDATE｜名义成员：18

## 特点

护巢期分布围着「守的东西」转：锚存在性硬门→锚面适配→守卫关系→温度。

## 中文伪脚本（渐进累积语义）

```plain text
GATE[锚存在性]：处于合法锚域？否→×0.01 软出局
EVAL[锚面适配] 三档
EVAL[守卫关系（核/缘/圈外）] 三档
EVAL[局部温度] 三档
返回 running weight
```

（语义：每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零、仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN）

## 配置表（参数轴）

| 参数轴 | 取值 / 说明 |
|---|---|
| anchor | 四形式：nest 构建型/egg_mass 附着/fry_school 移动群/host_brood 蚌宿主 |
| guard_participant | male/biparental |
| guard_action_notes | fan 扇护/黏液喂养→Response；洪水→DynamicSlot；停食→premise |
| resolver_instance | 细名（colony_nest/cave_ceiling…场内定位） |

---

*数据源：template_registry.yaml v10（确定性生成——手册生成器，非手写漂移）*
