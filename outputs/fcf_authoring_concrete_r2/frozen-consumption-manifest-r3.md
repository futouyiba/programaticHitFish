# Frozen Consumption Manifest R3｜Representation Worker

**状态：WORKING / ROUTING CHECKPOINT。** 本文件只决定哪些已审 Mechanism Story 可以被当前 Representation 样本消费；不重新建立 Reality Baseline，也不把 FISH-R01 的 Coverage Delta 候选提前转入 Representation。

## Authority 与准入

- Frozen upstream：`Reviewed Fish Mechanism Set｜Pilot-A｜Frozen at A4`，Gate=`PROCEED_TO_REPRESENTATION`。
- 当前 Representation 工件：`15 Case Authoring Visualization R0` §25 `Concrete Authoring Specimens R2`。
- FISH-R01 独立证据审核虽为 PASS，但它的 13 条 `Coverage Delta Candidate` 仍要求 FR3 Semantic Triage；在 Hub `Open Packs = NONE` 前不准入本表。

## 允许消费的 15 个 Frozen Story

| Frozen Story | 生产表达绑定 | 表面 | 当前映射 | 备注 |
| --- | --- | --- | --- | --- |
| Atlantic Cod / discrete prey | C01_B | BAKE | S_FIXED | Temperature + Anchor + Structure + Depth；生产空间顺序仍未冻结，样本顺序只作 fixture |
| Channel Catfish / discrete target + sensory context | C02_B | BAKE | S_FIXED | scent 不在 Feeding 重复扣除 |
| Rainbow Trout / discrete target + Flow Context | C03_R | RESPONSE | R_BANDS | FIRST_MATCH + typed ResponseStrength；无 Drift Mode |
| Brown Trout / ordinary baseline | C04_R | RESPONSE | R_BANDS | 不覆盖繁殖冲突 |
| Glass Zander / low-light pilot | C05_B | BAKE | S_FIXED | Light 是预定义可关 Slot，不是 LowLight Mode |
| Bluegill / Nest Guard | C06_R | RESPONSE | R_DEFENSE | 只评价 Defense；没有普通 Feeding Slot或优先级 |
| Smallmouth / Nest Guard + Fry Guard | C07_R | RESPONSE | R_DEFENSE | 同上；不声称现实绝对不摄食 |
| Nile Tilapia / mixed grazing + suspended | C08_R | RESPONSE | R_DUAL_FIXED | 一个 Feeding Evaluator + 两固定 Channel；不按 food context SELECT Profile |
| American Paddlefish / filter feeding | C09_R | RESPONSE | R_FIELD | 复用既有 Opportunity；FoodField 只是输入，hook acceptance 不由滤食证据推出 |
| Bigmouth Buffalo / filter feeding | C10_R | RESPONSE | R_FIELD | 同上 |
| Flathead Grey Mullet / continuous substrate foraging | C11_R | RESPONSE | R_FIELD | 同上；连续过程不生成新 Opportunity clock |
| Atlantic Salmon / ordinary growth | C12_N | RESPONSE | R_FEED | 只由上游 NormalFeeding Group 调用 |
| Atlantic Salmon / spawning migration | C12_M | RESPONSE | R_REACTION | 上游分群后普通 Feeding 关闭/强抑制；不声称单一攻击动机 |
| Sockeye / stage-qualified filter claim | C13_J, C13_O, C13_S | RESPONSE | R_FEED | 三个独立情景仅用于范围校验；不计作生产新 Template，不生成 Stage Selector |
| Sea lamprey / host attachment | 无 | OUT_OF_SCOPE | — | post-instantiation / product-scope boundary |
| Paddlefish / snagging | 无 | OUT_OF_SCOPE | — | Response-independent capture boundary |

表中看似 17 行，是因为 C12 的一个 Frozen Story 需要两个上游 Group binding，C13 的一个范围 Story 需要三个情景 binding；C14/C15 是明确边界而非可执行 Binding。R2 的 C01–C15 样本因此保留故事粒度，不把每个 Binding 误报成新的 LogicTemplate。

鲈鱼五群、G1–G3、Q1–Q3 是后续 Working 压力样本，不属于本 Frozen Set 的准入行。

## 暂缓消费的 R1 候选

以下来自已通过证据审核的 FISH-R01，但仍属于 `Coverage Delta Candidate / FR3 required`：鳄雀鳝阶段接触、褐鳟/鲑资源竞争、虹鳟表面鼠饵、鸭嘴鲟电感受/习惯化、黑鼓痕迹、蓝鳃低阻吐饵、尼罗罗非口孵、海七鳃鳗化学趋向、草鱼预投饵等。它们不进入当前 Binding、TemplateStep 或 L 统计；FR3 通过后，Representation Worker 再按新增 Story 的稳定 semantic claim、unresolved dimension 与 scope 逐项回归。

## R3 回归规则

1. 先检查 Hub `Coverage Delta Pack` 是否为 `CONSUMED`，并取得 FR3 的明确消费范围。
2. 只把新增 reviewed Story 连接到已有 Template / Profile / Predicate；没有证据不得把候选变成新 Group、Selector、Opportunity Contract 或 DSL 拓扑。
3. 每一新增 Binding 必须同时产生配置闭包、中文脚本、输入快照、Typed Result 与边界记录；不能只增加一行鱼名。
4. 通过同一表格/脚本复算和独立 Representation Review 后，才更新本 Manifest 的准入状态。此文件本身不改变 Hub B4，也不执行 Promotion。
