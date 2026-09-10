#### C10｜大口胭脂鱼：既有 Opportunity 的 FieldFeeding

Previous: 独立 FieldOpportunity 合同未决 → Updated: EXISTING_OPPORTUNITY_CONTRACT_REUSED。数值是呈现适配的演示输入；C09 使用不兼容呈现得到0，不从滤食或锚鱼记录推导钩饵接受。

样本涉及 3 张作者表、10 行依赖闭包（含共享引用；不要跨案例相加当独立行数）。全局去重行见第4节。

输入：
```json
{
  "food.density_index": 0.75,
  "food.suitability": 0.5,
  "response.feeding_match": 0.5
}
```

**C10_R**
```text
表达 C10_R 用于 BigmouthBuffalo.FieldFeeding / RESPONSE
模板 R_FIELD（固定结构，仅展开便于阅读）
配置：
  Density = @C10_R_Density
  Suitability = @C10_R_Suitability
  Match = @C10_R_Match
执行：
// 外层已有 Opportunity；此处不创建 FieldOpportunity 或计时器。
D = 查曲线(@C10_R_Density, food.density_index)
S = 查曲线(@C10_R_Suitability, food.suitability)
M = 查曲线(@C10_R_Match, response.feeding_match)
返回 响应强度(D × S × M)
// M 来自同一 Session / Active Presentation Channel，不从“有食物”推导钩饵可接受。
```

本例结果：
```json
{
  "case": "C10",
  "binding": "C10_R",
  "template": "R_FIELD",
  "intermediate": {
    "Density": 0.6,
    "Suitability": 0.5,
    "Match": 0.5
  },
  "result": 0.15000000000000002
}
```
