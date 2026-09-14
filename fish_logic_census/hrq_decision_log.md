# HRQ 人类裁决日志（互动式裁决 · 2026-09-11）

裁决人：用户（互动式）｜记录：Coordinator｜执行：全部裁完后统一 mutation 批（registry v9）→ 独立审 → 文档 v13

## 裁决 1：HRQ-RS1-01｜SINGLE 族处置 ✅

- **裁定：A——确认拆分 + 234 条 AMB 转入「真形重验队列」**
- 效果链：
  1. SINGLE v1 canonical 正式退役（61/61 结构不符 + B4 饱和伪影根因在案）
  2. RS1 拆出的 9 个链族（TIERED_SINGLE 17 / GATED_COVER 13 / NOCTURNAL 5 / ZONE_SUBSTRATE 3 / SOFT_TRIPLE 2 / ZONE_DEPTH 1 / LAYER_AXIS 2 / FILTER_FIELD 2 / GUARD_ANCHOR 4）由 CANDIDATE-pending-RS1-01 转正
  3. AMB 四层链 234（B4 25 + B5 52 + B6 47 + B7 110）改标 `pending_truth_rebuild`，成为终局「全库顺序还原重跑」的输入清单
  4. 5 条无 B 系列表达文件成员（LAM/PIN/ASR/RVS/RDS）保持证据不足挂起（归 FR/表达线补证，不并入任何族）
- 联动消除：HRQ-B4-02 / B5-01 / B6-01 / B7-01（AMB 挂账主链）随之关闭；HRQ-RS1-01④（4 原栖息面程序归宿）→ 并入重验队列

## 语义裁定（用户口述，随裁决 2/3 生效）✅

1. **无合并步——渐进累积语义**：不存在终点"合并"步骤；乘法逐步进行（weight = weight × step_fit）。三档＝最喜爱不折损 / 可接受 ×衰减 / 不居留 **×0.01 软出局返回**（非零、仍可参与下游——对齐 0.3.4.0 Bake DSL `return 0.01 * weight` 语义）。这裁决了 B 系列全部「合并算子 OPERATOR UNDEFINED」占位。
2. **B 系列措辞对齐待办**：B 系列表达文件中「排除档返回 0 出局」措辞与 ×0.01 软出局不一致——mutation 批统一对齐（含 work standards §5.1 表述更新）。
3. **C9「4/4 同形」证据作废**：四鱼栖息面同序源于 BA-NORMAL-HABITAT-FIT 模板约定序（当时均标 [需正文]），非逐鱼推导——第二层平铺伪影（第一层丢顺序，这一层丢「谁先谁后」）。逐鱼顺序推导（如美鱥口器→水层先行、蓝鳃结构先行）＝重跑批必做工序。

## 裁决 2：顺序在族层面的地位 ✅

- **裁定：B——严格判据：因子判断顺序＝族判据**
- 效果：任何顺序不同＝不同族；重跑判同基准＝完整有序链（含门/槽位位置与因子排列）。族数预计显著膨胀——接受（真数字优于假数字）。
- 联动：9 个 RS1 链族转正时 canonical 标注 order-provisional（骨架判据成立——门/槽/链长的差异是结构级的；但基础序为模板约定，成员真实序待重跑逐鱼推导后可能移动）。

## 裁决 3：C9 处置 ✅

- **裁定：A——缓立，并入重跑**
- 效果：以修正概念 PROGRESSIVE_TIERED_FUNNEL（渐进三档漏斗 + 顺序轴）作为重跑判同基准之一；4 成员真实顺序逐鱼推导后再定成员资格；157 对 PENDING_CANDIDATE 比较材料保持悬置至重跑。
- HRQ-RS1-05 随之关闭（立族与否由重跑证据决定；ΔL +1 归属位问题消解——若重跑后立族，计入当批）。

## 裁决 4：GUARD anchor 轴管理规则 ✅

- **裁定：A——四形式方案**
- **轴设计**：anchor 轴取值＝后代空间存在形式，仅四值＋一边界：
  - `nest`（构建型，C4 巢体存在原子：stone_nest/gravel_ridge 合一、pebble_mound、泡沫巢、殖民巢、清巢…）
  - `egg_mass`（利用型附着：岩缝/洞顶/岩面/树根——底质差异归 suitability）
  - `fry_school`（移动稚鱼群：discus 黏液喂养→Response 注记；arapaima 洪水→DynamicSpatialSlot）
  - `host_brood`（蚌宿主：大鳍𫚪/鳑鲏跨批复现）
  - `brooded`（口孵/体内携带）＝**结构级退化链，不入本族**——银龙盲形与罗非退化链先例的冲突登记待真形重跑终裁
- **配套拆解规则**：底质→@NestStructureSet（路由 C3）+ suitability Profile（轴不重复记账）；谁守→guard_participant 轴（male/biparental）；怎么守→Response 动作注记（fan/黏液）；位相→DynamicSpatialSlot；停食→premise。GuardAnchorResolverInstance 字段保留细名（实例管场内定位，轴值管语义分类）。
- **9 值落位**：石巢脊→nest；洪水护卵群→fry_school+slot；洞顶→egg_mass+suitability；卵块→egg_mass；岩缝扇护→egg_mass+Response(fan)；双亲巢→nest+participant(biparental)；狼鱼停食→egg_mass+premise(fasting)；贝内产卵→host_brood；口孵→待重跑（退化链候选）。
- **联动消解**：HRQ-B5-02 / B6-02 / B7-02 关闭（18-20 候选值收敛为 4 值+拆解）；pebble_mound 18-vs-19 口径关闭（→nest）；discus_mucus vs fry_anchor 覆盖关系关闭（→fry_school+注记）；guard_participant 立独立轴确认；「轴膨胀速度」关注项关闭（膨胀根因＝四维度塞一轴）。

## 裁决 5：HARD_GATED v2 canonical ✅

- **裁定：A——确认 v2（双硬门→EXIT 档因子集，渐进累积语义）＋肺鱼/电鳗双成员**
- 电感知分层按 REP-CUE-AXIS-001 裁定（主动放电/远程麻痹归 Encounter/Conversion、被动电感知归 Response cue，不进 Bake）——电鳗 AMBIGUOUS 了结。canonical 重写随 mutation 批（渐进累积＋顺序判据口径）。

## 裁决 6：目录卫生三件套 ✅

- **裁定：A——打包确认**
- ①PATCH_RESOURCE_FOLLOWING 空置撤销（MGC→GATED_COVER gate_axis bottom_zone 第 3 实例；ONS→SOFT_TRIPLE 第 2 成员；provenance 留档不删历史）
- ②PLAIN_FACTOR_COMBINE v1 废止（0/5 自有成员证伪，证据随册）——「因子集无序」读法正式关闭（与裁决 2 一致）
- ③14 条 slot_tiering 追击型并入真形重验队列（与裁决 1 的 234 条同队同流程；HRQ-RS1-03 轨道关闭）
- 活族数 21 → 19（两个 Bake 空壳移除；后续重跑增减另计）

## 裁决 7：CRR 处置 + 簿记打包 ✅

- **CRR：A——负证据台账保留**（live 侧资产不撤；284 条 non-match 反对票继续记，作 census↔live 对账弹药；HRQ-B2-02 关闭）。
- **簿记：A——打包确认**（名义扩容入册 TYPED 248 / FOOD_FIELD 16 / GUARD 四形式重排+participant 轴 / 程序数 166；饱和候选 LOCAL_SATURATION_CANDIDATE 正式撤销；MGC 旧口径追溯、5 无文件成员挂起归 FR 线、面定位约定与 README 固化等小项随批）。

---

# 互动式裁决收官总结（2026-09-11）

**七项裁决 + 两组语义裁定，全部落定：**

| # | 裁决 | 结果 |
|---|---|---|
| 1 | SINGLE 族 | 拆；234 条转真形重验队列 |
| 语义 | 合并步 / 三档 | 无合并步——渐进累积；×0.01 软出局 |
| 2 | 顺序地位 | 严格判据：顺序＝族判据 |
| 3 | C9 | 缓立并入重跑（概念修正为渐进三档漏斗+顺序轴） |
| 4 | anchor 轴 | 四形式方案（nest/egg_mass/fry_school/host_brood + brooted 退化边界）+ 拆解规则 |
| 5 | HARD_GATED | v2 确认＋肺鱼/电鳗双成员；电感知留 Response 层 |
| 6 | 目录卫生 | PATCH 撤架、PLAIN 撤稿、14 条并队（21→19） |
| 7 | CRR + 簿记 | 负证据台账保留；名义入册打包 |

**关闭的 HRQ**：RS1-01/04⑥/05、B4-01（饱和撤销）、B4-02、B5-01/02、B6-01/02、B7-01/02、RS1-03、B2-02。
**移交重跑批**：234+14 条真形重验队列（逐鱼顺序推导为必做工序）；C9 与 brooded 由重跑证据终裁。
**mutation 批执行清单（registry v9）**：SINGLE v1 退役（61 moved 转正归属+5 无文件挂起）→ 9 链族转正（canonical 重写：渐进累积语义、order-provisional 标注）→ anchor 四形式轴+participant 轴建立（GUARD 族改写）→ HARD_GATED v2 → PATCH/PLAIN 撤除（provenance）→ CRR 台账保留注记 → 名义数字入册（TYPED 248/FOOD_FIELD 16/166 程序）→ 饱和候选撤销 → mutation_provenance 全记录。

## 追加裁决：HRQ-REBUILD-SCOPE-01（2026-09-14，用户口述）✅

- **裁定：①链族 47 个在册成员纳入重跑队列；②重跑为终局级别（全库顺序还原重跑，输出 registry v10 终态）**
- 执行：REBUILD-SCOPE-001 范围 mutation——truth_rebuild_queue.jsonl 248→**303 行**（+47 链族 order_provisional 成员 +8 终裁特例[C9×4 栖息面/brooded×2/form_hold×2]）；9 链族 order_provisional 注记解析载体更新为已入队；handed_to_rerun 同步；registry 版本维持 9（范围 mutation 不动族结构）。
- 分批方案（终局重跑 RB 系列）：
  - **RB-1**：B4 25 + B5 52 + slot_tiering 14 = 91 项（同鱼互引最密，先清最纠缠层）
  - **RB-2**：B6 47 + 链族 47 = 94 项（order_provisional 解析主力）
  - **RB-3**：B7 110 + 终裁特例 8 = 118 项（含 C9 立族材料终裁）
  - 每批：证据源 = B 系列表达文件（顺序还原后）+ census 冻结快照 + fish-reference CSV 形态/生态 → 逐鱼推导判断顺序 → 盲冻结 → 对 registry v9 判同（严格顺序判据+渐进累积）→ HRQ 提案 → 独立审 → 之后统一 mutation（registry v10）





