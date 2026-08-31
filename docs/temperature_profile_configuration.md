# FCF V1 TemperatureProfile 完整配置表

本文定义 `temperature(location, depth, causal_cut)` 的 authoring 输入。它只描述
世界温度数据及其查询方法，不包含任何 Species、Motive、Entry 或咬口解释。

## 1. 顶层配置表

| 字段 | 类型 | 必填 | 单位/枚举 | 说明 | 主要校验 |
|---|---|---:|---|---|---|
| `schema_version` | string | 是 | `fcf.temperature_profile.v1` | Profile schema 版本 | 必须精确匹配 |
| `profile_id` | stable ID | 是 | `lower_snake_case` | Profile 身份 | artifact 内唯一 |
| `waterbody_id` | reference | 是 | — | 所属水体 | 必须解析 |
| `spatial_frame_id` | revisioned reference | 是 | — | location/depth 坐标系 | 必须固定 exact revision |
| `profile_mode` | enum | 是 | `SINGLE_LAYER` / `DEPTH_LAYERS` | 空间深度能力 | SINGLE_LAYER 不得伪装深度变化 |
| `temperature_unit` | enum | 是 | `CELSIUS` | canonical 单位 | V1 只接受摄氏度 |
| `temporal_clock` | object | 是 | 见 §2 | 时间域 | clock/epoch/unit 必须明确 |
| `source_policy` | object | 是 | 见 §3 | 允许的数据源和质量门槛 | 禁止未声明 source kind |
| `interpolation_policy` | object | 是 | 见 §4 | 允许的局部插值 | 必须有算法 revision |
| `depth_layers` | array | 是 | 见 §5 | 深度层和温度样本 | 至少一层；不得重叠 |
| `thermocline_boundaries` | array | 否 | 见 §7 | 不可跨越插值的热跃层 | `DEPTH_LAYERS` 时建议显式声明 |
| `profile_revision` | immutable revision | 是 | — | 世界数据版本 | 任一语义改动生成新 revision |
| `source_manifest_hash` | string | 是 | SHA-256/内容哈希 | 原始样本清单指纹 | 必须与导入清单一致 |
| `authoring_metadata` | object | 是 | 见 §8 | 作者、说明、时间 | 不参与鱼类解释 |

没有隐式默认值。缺少必填字段时编译失败，不允许用“合理温度”补齐。

## 2. temporal_clock

| 字段 | 类型 | 必填 | 例子 | 说明 |
|---|---|---:|---|---|
| `clock_id` | stable ID | 是 | `lake_sim_clock` | 时间域身份 |
| `clock_revision` | revision | 是 | `clock:r3` | 时间转换规则版本 |
| `unit` | enum | 是 | `MILLISECONDS` | V1 canonical timestamp 单位 |
| `epoch` | string | 是 | `SIMULATION_START` / ISO-8601 | 时间零点 |

所有 `observed_at_ms`、`valid_from_ms`、`valid_to_ms` 都属于这个 clock。不同
clock 的样本不得直接插值。

## 3. source_policy

| 字段 | 类型 | 必填 | 说明 |
|---|---|---:|---|
| `accepted_source_kinds` | enum[] | 是 | `SENSOR`, `HYDRO_MODEL`, `MANUAL_CALIBRATION` |
| `maximum_uncertainty_c` | number | 是 | 超出即不可用于确定性阈值判断 |
| `freshness_by_source_s` | map | 是 | 每种 source kind 的最大新鲜时长 |
| `stale_behavior` | enum | 是 | `RETURN_STALE_FACT` 或 `RETURN_UNKNOWN` |
| `missing_behavior` | enum | 是 | V1 固定为 `RETURN_UNKNOWN` |
| `outlier_policy_id` | revisioned reference | 是 | 原始异常值分类规则 |
| `calibration_policy_id` | revisioned reference | 是 | 校准规则；校准不得覆盖原始样本 |

`RETURN_STALE_FACT` 仍必须标记 `quality=STALE`；下游不得把 STALE 当 DIRECT。

## 4. interpolation_policy

| 字段 | 类型 | 必填 | 允许值/单位 | 说明 |
|---|---|---:|---|---|
| `spatial_method` | enum | 是 | `NEAREST_CELL`, `LINEAR_WITHIN_CELL_GROUP` | 只在同一允许区域内插值 |
| `maximum_spatial_gap_m` | number | 是 | m，`≥0` | 超出返回 UNKNOWN |
| `depth_method` | enum | 是 | `NEAREST_IN_LAYER`, `LINEAR_WITHIN_LAYER` | 不跨 layer/thermocline |
| `maximum_depth_gap_m` | number | 是 | m，`≥0` | 超出返回 UNKNOWN |
| `temporal_method` | enum | 是 | `HOLD_LAST`, `LINEAR_WITHIN_WINDOW` | 时间插值方式 |
| `maximum_time_gap_s` | number | 是 | s，`≥0` | 超出按 stale/missing policy |
| `thermocline_crossing` | enum | 是 | V1 固定 `BLOCK` | 禁止跨热跃层 |
| `algorithm_revision` | revision | 是 | — | 插值实现/系数 revision |

更换 method、gap 或算法实现必须生成新的 `algorithm_revision`，并进入 causal-cut
fingerprint。

## 5. depth_layers

| 字段 | 类型 | 必填 | 说明 | 主要校验 |
|---|---|---:|---|---|
| `layer_id` | stable ID | 是 | 深度层身份 | Profile 内唯一 |
| `depth_min_m` | number | 是 | 包含下界 | `≥0` |
| `depth_max_m` | number | 是 | 不包含上界 | `> depth_min_m` |
| `location_cell_group_id` | reference | 是 | 允许相互插值的 cell group | 必须属于 spatial frame |
| `samples` | array | 是 | 见 §6 | 至少一个；sample ID 唯一 |

深度层使用半开区间 `[depth_min_m, depth_max_m)`。相邻层可以共边界，但不得
重叠。`SINGLE_LAYER` 必须恰好一层，并显式覆盖 authoring 声明的有效深度范围。

## 6. samples

| 字段 | 类型 | 必填 | 单位/枚举 | 说明 |
|---|---|---:|---|---|
| `sample_id` | stable ID | 是 | — | 原始/校准样本 identity |
| `location_cell` | reference | 是 | — | spatial frame 内的 cell |
| `depth_m` | number | 是 | m | 必须位于所属 layer |
| `observed_at_ms` | integer | 是 | temporal clock ms | 观测时间 |
| `valid_from_ms` | integer | 是 | ms | 有效区间下界（包含） |
| `valid_to_ms` | integer | 是 | ms | 有效区间上界（不包含） |
| `value_c` | number | 是 | °C | canonical 温度值 |
| `uncertainty_c` | number | 是 | ±°C，`≥0` | 测量/模型不确定性 |
| `source_kind` | enum | 是 | §3 allowlist | 数据来源类型 |
| `source_revision` | revision | 是 | — | 原始数据 revision |
| `quality` | enum | 是 | `DIRECT`, `INTERPOLATED`, `STALE` | 样本质量；MISSING 不作为 sample |
| `calibration_revision` | revision/null | 是 | — | 未校准时为 `null` |
| `source_sample_ids` | raw source ID[] | 是 | — | provenance；DIRECT 至少包含一个原始数据记录 ID |

`valid_from_ms < valid_to_ms`。同 cell/depth/time 出现互相矛盾的 DIRECT 样本时，
必须由 outlier/calibration policy 明确裁决；不得依赖数组顺序。

## 7. thermocline_boundaries

| 字段 | 类型 | 必填 | 说明 |
|---|---|---:|---|
| `boundary_id` | stable ID | 是 | 边界身份 |
| `location_cell_group_id` | reference | 是 | 适用空间区域 |
| `top_depth_m` | number | 是 | 热跃层顶部 |
| `bottom_depth_m` | number | 是 | 热跃层底部；必须大于顶部 |
| `valid_from_ms` / `valid_to_ms` | integer | 是 | 半开有效时间区间 |
| `source_revision` | revision | 是 | 边界数据来源 |
| `crossing_policy` | enum | 是 | V1 固定 `BLOCK_INTERPOLATION` |

边界表示“不能跨越它插值”，不是自动的鱼类栖息阻断。

## 8. authoring_metadata

| 字段 | 类型 | 必填 | 说明 |
|---|---|---:|---|
| `author` | string | 是 | 创建者 |
| `created_at` | ISO-8601 | 是 | artifact 创建时间 |
| `change_reason` | string | 是 | 变更原因 |
| `evidence_refs` | string[] | 是 | 数据/校准依据；可以为空数组 |

## 9. 完整 YAML 示例

```yaml
schema_version: fcf.temperature_profile.v1
profile_id: north_lake_summer
waterbody_id: north_lake
spatial_frame_id: north_lake_grid:r4
profile_mode: DEPTH_LAYERS
temperature_unit: CELSIUS

temporal_clock:
  clock_id: north_lake_sim_clock
  clock_revision: clock:r3
  unit: MILLISECONDS
  epoch: SIMULATION_START

source_policy:
  accepted_source_kinds: [SENSOR, HYDRO_MODEL, MANUAL_CALIBRATION]
  maximum_uncertainty_c: 1.0
  freshness_by_source_s:
    SENSOR: 900
    HYDRO_MODEL: 3600
    MANUAL_CALIBRATION: 86400
  stale_behavior: RETURN_STALE_FACT
  missing_behavior: RETURN_UNKNOWN
  outlier_policy_id: thermal_outlier:r2
  calibration_policy_id: thermal_calibration:r5

interpolation_policy:
  spatial_method: LINEAR_WITHIN_CELL_GROUP
  maximum_spatial_gap_m: 50
  depth_method: LINEAR_WITHIN_LAYER
  maximum_depth_gap_m: 2
  temporal_method: LINEAR_WITHIN_WINDOW
  maximum_time_gap_s: 600
  thermocline_crossing: BLOCK
  algorithm_revision: thermal_interp:r7

depth_layers:
  - layer_id: surface_0_4m
    depth_min_m: 0
    depth_max_m: 4
    location_cell_group_id: north_basin_cells
    samples:
      - sample_id: sensor_a_000184
        location_cell: cell_n17
        depth_m: 2
        observed_at_ms: 3600000
        valid_from_ms: 3600000
        valid_to_ms: 4200000
        value_c: 20.4
        uncertainty_c: 0.2
        source_kind: SENSOR
        source_revision: sensor_a:r18
        quality: DIRECT
        calibration_revision: thermal_calibration:r5
        source_sample_ids: [sensor_a_raw_000184]

  - layer_id: deep_7_12m
    depth_min_m: 7
    depth_max_m: 12
    location_cell_group_id: north_basin_cells
    samples:
      - sample_id: hydro_n17_3600
        location_cell: cell_n17
        depth_m: 8
        observed_at_ms: 3600000
        valid_from_ms: 3600000
        valid_to_ms: 7200000
        value_c: 16.2
        uncertainty_c: 0.4
        source_kind: HYDRO_MODEL
        source_revision: hydro_model:r11
        quality: DIRECT
        calibration_revision: null
        source_sample_ids: [hydro_raw_n17_3600]

thermocline_boundaries:
  - boundary_id: north_basin_thermocline
    location_cell_group_id: north_basin_cells
    top_depth_m: 4
    bottom_depth_m: 7
    valid_from_ms: 0
    valid_to_ms: 86400000
    source_revision: hydro_model:r11
    crossing_policy: BLOCK_INTERPOLATION

profile_revision: temperature_profile:r12
source_manifest_hash: sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
authoring_metadata:
  author: environment_team
  created_at: "2026-08-31T10:00:00+08:00"
  change_reason: summer stratification calibration
  evidence_refs: [sensor_campaign_2026_08, hydro_run_441]
```

## 10. 烘焙输出（只读）

```text
BakedTemperatureIndex {
  profile_id
  profile_revision
  index_revision
  interpolation_algorithm_revision
  spatial_frame_revision
  source_manifest_hash
  layer_index
  time_segments
  blocked_crossings
  bake_diagnostics[]
}
```

`index_revision` 由烘焙产物生成，不是作者手填。任何输入或算法 revision 改变都
产生新 index；旧 index 不覆盖，用于 replay。

## 11. 查询输出

```text
WaterTemperatureFact {
  value_celsius
  uncertainty_celsius
  location_id
  depth_m
  measured_at
  valid_from / valid_to
  source_kind
  quality
  source_revision = (
    profile_revision,
    index_revision,
    interpolation_algorithm_revision
  )
  provenance_sample_ids[]
}
```

若 location/depth/time 无可接受数据、超过 gap、跨热跃层、revision 不可解析、
`uncertainty_c > maximum_uncertainty_c`，或 freshness 超出并由 policy 指定
`RETURN_UNKNOWN`，返回 typed `UNKNOWN(reason, revision_tuple)`，不返回一个虚构标量。
若 stale policy 为 `RETURN_STALE_FACT`，则返回 `quality=STALE` 的 Fact，后续安全/
阈值 resolver 仍按保守策略处理。

## 12. Semantic compiler（跨字段校验）

JSON Schema 只负责结构；以下不变量由 `compile_temperature_profile` fail-closed
校验，不能推迟到查询时猜测：

| Diagnostic | 条件 |
|---|---|
| `DEPTH_LAYER_RANGE` | `depth_max_m <= depth_min_m` 或负深度 |
| `DEPTH_LAYER_OVERLAP` | 两个 depth layer 相交 |
| `DUPLICATE_LAYER_ID` | layer ID 重复 |
| `DUPLICATE_SAMPLE_ID` | 任意 layer 间 sample ID 重复 |
| `SAMPLE_OUTSIDE_LAYER` | sample depth 不在所属半开区间 |
| `SAMPLE_VALIDITY_RANGE` | `valid_from_ms >= valid_to_ms` |
| `SAMPLE_OBSERVED_OUTSIDE_VALIDITY` | observed time 不在有效区间 |
| `THERMOCLINE_RANGE` | bottom 不大于 top |
| `THERMOCLINE_VALIDITY_RANGE` | boundary 有效区间倒置 |
| `SINGLE_LAYER_COUNT` | SINGLE_LAYER 不是恰好一层 |
| `SAMPLE_SOURCE_NOT_ALLOWED` | sample source 不在 allowlist |
| `SOURCE_FRESHNESS_MISSING` | accepted source 没有 freshness policy |
| `SOURCE_MANIFEST_HASH` | 不是 `sha256:` + 64 位十六进制 |
| `CLOCK_EPOCH` | 不是 `SIMULATION_START` 或 ISO-8601 |
| `NONFINITE_PHYSICAL_VALUE` | 温度、uncertainty、深度、freshness 或 gap 为 NaN/Infinity |

空间 frame/cell/group 与外部 registry 的存在性由 reference-resolution pass 校验；
无法解析也必须阻止 compile/bake。

## 13. 公开编译与 manifest 验证顺序

生产 authoring pipeline 必须固定为：

```text
parse YAML/JSON（拒绝非标准数字）
→ temperature_profile.schema.json structural validation
→ compile_temperature_profile semantic validation
→ reference resolution（frame/cell/group/policy revision）
→ 根据排序后的 canonical raw source manifest 重算 SHA-256
→ constant-time compare source_manifest_hash
→ bake immutable index
```

任何阶段失败都不生成 index。`source_manifest_hash` 不能只验证字符串格式；bake
必须从实际导入的 raw sample manifest 重算并比对，防止作者声明与输入样本不一致。
序列化使用标准 JSON 并设置 `allow_nan=false`；NaN/Infinity 一律阻止编译。
