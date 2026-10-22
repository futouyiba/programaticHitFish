# Bass 三时段案例压力测试

Document status：**RETAINED / 解释性固定样例（fixture）报告**  
Authority：**V0 证据；非 FCF V1 契约（contract）**  
Scope：`bass_dynamic_preference` 三时段案例及其固定测试输入。  
Reproduction：`python -m bass_dynamic_preference.run_case` and the pytest command below.  
V1 promotion rule：仅可作为案例证据，不能自行升级为 V1 参数或机制。

**Verdict: PASS WITH DELTA**

本报告是 `Simplified Production V0` 的可复跑测试固定样例，不是机制权威（authority）。所有数值均为 **TEST FIXTURE / TUNING PLACEHOLDER / NOT AUTHORITY**。运行：

```text
python -m bass_dynamic_preference.run_case
pytest -q tests/test_bass_dynamic_preference.py
```

## A. 固定样例（Fixture）

固定三个长期合理区域：Grass Edge（0.90）、Shaded Wood（0.80）、Drop-off（0.70）。固定三类长期可接受食物/线索族群（food/cue family）：BAITFISH（0.90）、CRUSTACEAN（0.80）、WORM_LIKE（0.70）。第一轮固定 `Satiation=NORMAL`、`CueFamiliarity=LOW`、`EngagementMode=NORMAL`、`LifecycleCohort=ORDINARY_NORMAL`。

为隔离共模（common-mode），测试采用静态偏好加权中心化：`Σ(static × bias)` 保持不变。`LocalIntensity=100×static×bias`，`ExposedIntensity=LocalIntensity×0.80`。这只是相对重排测试，不是物理鱼数守恒或正式归一化（normalization）契约。

## B. 三时段计算（Three-Epoch Calculation）

| Zone | Morning | Midday | Evening |
|---|---:|---:|---:|
| Grass Edge | 1.300 → 117 / 93.6 | 0.700 → 63 / 50.4 | 0.900 → 81 / 64.8 |
| Shaded Wood | 0.900 → 72 / 57.6 | 1.200 → 96 / 76.8 | 0.800 → 64 / 51.2 |
| Drop-off | 0.729 → 51 / 40.8 | 1.157 → 81 / 64.8 | 1.357 → 95 / 76.0 |
| 排序 | Grass > Wood > Drop | Wood > Drop > Grass | Drop > Grass > Wood |

单元格依次为 `Bias → LocalIntensity / ExposedIntensity`。

| Food family | Morning | Midday | Evening |
|---|---|---|---|
| BAITFISH | 1.300 → 1.000 / STRONG / HIGH | 0.700 → 0.599 / MARGINAL / LOW | 0.900 → 0.769 / VALID / NORMAL |
| CRUSTACEAN | 0.900 → 0.648 / MARGINAL / LOW | 1.300 → 0.936 / STRONG / HIGH | 0.800 → 0.576 / MARGINAL / LOW |
| WORM_LIKE | 0.729 → 0.434 / MARGINAL / LOW | 1.043 → 0.620 / MARGINAL / LOW | 1.357 → 0.807 / STRONG / HIGH |

单元格依次为 `Bias → FeedingMatch / Meaning / ResponseGrade`。不计算最终参与互动（Engagement）概率（probability）；其 NONE 基线（baseline）、饱和（saturation）和分类语义（categorical semantics）仍是既有 P0 OPEN。

## C. 玩家故事（Player Story）

- **Morning：** Grass + Baitfish 是主要模式。
- **Midday：** 继续 Grass + Baitfish 明显恶化。只换区到 Wood 仍然低响应；只换线索（cue）到 Crustacean 明显恢复；Wood + Crustacean 同时恢复。
- **Evening：** Drop-off + Worm-like 成为新模式。没有一个全天稳定的“正确栖息地（Habitat）+ 正确 Bass 诱饵（lure）”。

第二轮在 Midday Wood 大量使用同一个 CRUSTACEAN CueSignature 后，只提高 `CueFamiliarity`：`FeedingPreferenceBias` 不变，FeedingMatch 不变，响应（Response）从 HIGH 降为 LOW。换 CueSignature 或换来源（Source）可恢复，不需要修改偏好（Preference）。

## D. 失败边界审计（Failure Boundary Audit）

| 边界（Boundary） | 负责内容 | 玩家解法 |
|---|---|---|
| 存在度（Presence） | 当前鱼群利用与呈现（Presentation）覆盖范围（reach） | 换区域、改变搜索位置 |
| Meaning / FeedingMatch | 当前线索是否符合偏好 | 换食物/线索族群 |
| 响应（Response） | 是否开始互动 | 根据 follow/ignore/turn 调整 |
| 饱食（Satiation） | 总体觅食驱动（feeding drive） | 换时段或找更积极鱼 |
| CueFamiliarity | 来源 × CueSignature 的局部学习 | 换 Signature、换来源、等待衰减 |

机制内部可区分存在度与响应，但现有玩家反馈不足以保证玩家侧区分；这是 `Learnability / Observation Gap`。最小修复是把现有存在度结果和响应结果映射为独立、可观察的反馈，不增加新机制。

## E. 反例攻击（Counterexample Attack）

1. 所有 Bias 同时升高会偷偷提高总体供给/食欲。
2. 来源组（SourceGroup）技术切分若产生额外候选，会膨胀强度（intensity）。
3. 全图归一化会让无关新区域改变旧区域结果。
4. 空间目标（Spatial target）过粗会抹平区域差异，过细会造成高维配置编写（authoring）。
5. PresentationMatch 过强会压过偏好，重新形成万能诱饵（lure）。
6. 一个呈现同时完整映射多个食物族群（food family）会重复结算。
7. 时段（Epoch）硬切会造成热点瞬移。
8. 参与互动饱和可能把真实 Bias 翻转掩盖成玩家不可感知的差异。

## F. 复杂度审计（Complexity Audit）

两个 Bias 都必要：删除任一个都会丢失“换区”和“换线索”两种不同玩家解法。当前没有新增 State、FSM、运行时层（Runtime Layer）、FishMood、BiteChance、诱饵 SKU 归属方（owner）或潜在漂移（latent drift）；本实验的证据也从未要求新增独立模式对象（术语沿革：FishMode →（2026-09-11）FishGroup →（2026-10-22）中鱼习性模式（EngagementMode）；行为逻辑程序选择由中鱼习性模式直接持有）。空间 Bias 应作用于 `Species × Cohort × zone-local stable habitat-use group`，再编译到来源组；这是配置编写键（authoring key），不是新运行时层。觅食 Bias 应作用于低基数猎物/食物线索族群（prey/food-cue family），不作用于 SKU 或 CueSignature。

`FishConditionEpoch` 继续是描述性慢快照术语。时段切换只需插值（interpolation）/速率限制（rate limit）/滞回（hysteresis），不需要新状态机（State Machine）。未配置动态性的鱼种自然使用两个 Bias=1.0。

## G. 审核结论（Verdict）

**PASS WITH DELTA**。

当前两个 Bias 足以产生可学习、可解释的动态鱼情；没有证据要求新增长期机制结构。

现在必须闭合：

- Bias 共模防泄漏与有界相对重加权（bounded relative reweighting）；
- 来源碎片化不变性（fragmentation invariance）；
- 时段平滑切换；
- 存在度/响应玩家反馈合同。

继续 OPEN：精确归一化范围（exact normalization scope）、时段节律（cadence）、正式线索词表（cue vocabulary）、潜在漂移、参与互动 P0 概率/饱和及数值校准。

## 范围化审核结论（Scoped verdict）

```text
level: ARTIFACT
scope:
  - docs/bass_dynamic_preference_pressure_test.md
baseline:
  - Simplified Production V0 fixture inputs and fixed test commands
  - scoped_review_protocol.md default PATCH/ARTIFACT rules
proves:
  - 三时段 fixture 的重排、失败边界和反例审查记录完整
does_not_prove:
  - V0 数值是 production calibration
  - V1 contract、V1 Freeze 或跨地图机制正确
open_findings:
  - exact normalization scope、Epoch cadence、cue vocabulary、Engagement P0 与数值校准仍 OPEN
verdict: ARTIFACT_REVISE
```
