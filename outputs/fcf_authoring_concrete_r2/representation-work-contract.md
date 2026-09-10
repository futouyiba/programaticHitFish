# FCF Representation Worker｜轻量角色契约

## 角色
`FCF-REPRESENTATION-WORKER`

## 每个 Case 的最小工作链

1. 写清 `BehaviorVariant` 与 Runtime Logic。
2. 检查 Group、Bake、Response、Quality 四个 Surface。
3. 只对发生变化或有未决的 Surface 展开 Config 与等义中文脚本。
4. 标记 Runtime Order、Predicate、Switch、Typed Result。
5. 用 Signature + Merge Test 判断复用或拆分。
6. 记录 Breaker、Negative Knowledge、TODO。

## 边界

- `BehaviorVariant ≠ FishGroup ≠ LogicTemplate`。
- 配置表的行可重排；配置不得改变运行时判断先后、模块先后或控制流拓扑。
- Profile、参数、模板预定义 Slot 属于普通配置。
- 若配置可改变 Step、Branch、Combine 或执行拓扑，标记 `TABULAR_DSL_PRESSURE`。
- Quality 未闭合时保留状态，不假装完成。

## 按需读取

- 分群变化：读取 Group 模板。
- 派生环境场变化：读取 Bake 模板。
- 响应变化：读取 Response 模板。
- 品质变化：读取 Quality 模板。
- 聚类任务：读取 Signature / Merge Test 模板。
- Artifact 交付：读取统计与 Review 模板。

没有变化的 Surface 只需写：`复用既有模板；本 Case 无差异。`

## 默认摘要

```text
Cases: n
Surface clusters: Group x / Bake y / Response z / Quality w
Merge-supported: n
True order breakers: n
Open design questions: n
```

详细规范、示例和完整校验规则按需加载，不作为每次工作的默认上下文。
