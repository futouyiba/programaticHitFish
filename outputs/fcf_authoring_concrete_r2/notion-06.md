### R2-A / Predicate
PK node_id；kind=ATOM/ALL/ANY/NOT。ATOM 的 field 是只读白名单字段，operator∈GE/GT/LE/EQ/BETWEEN/IN/CONTAINS_ANY；parameter_id FK。组合节点三个叶字段显式 N/A。BETWEEN 为闭区间；空集、缺失字段/类型错拒绝。
<table header-row="true" fit-page-width="true">
<tr><td>node_id</td><td>kind</td><td>field</td><td>operator</td><td>parameter_id</td></tr>
<tr><td>C03_good_match</td><td>ATOM</td><td>response.feeding_match</td><td>GE</td><td>C03_good_match_value</td></tr>
<tr><td>C03_drift</td><td>ATOM</td><td>response.natural_drift_fit</td><td>GE</td><td>C03_drift_value</td></tr>
<tr><td>C03_high</td><td>ALL</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
<tr><td>C03_some_match</td><td>ATOM</td><td>response.feeding_match</td><td>GE</td><td>C03_some_match_value</td></tr>
<tr><td>C04_good_match</td><td>ATOM</td><td>response.feeding_match</td><td>GE</td><td>C04_good_match_value</td></tr>
<tr><td>C04_some_match</td><td>ATOM</td><td>response.feeding_match</td><td>GE</td><td>C04_some_match_value</td></tr>
<tr><td>guard_dates</td><td>ATOM</td><td>slow.day_of_year</td><td>BETWEEN</td><td>guard_dates_value</td></tr>
<tr><td>guard_temp</td><td>ATOM</td><td>slow.recent5day_temp_c</td><td>GE</td><td>guard_temp_value</td></tr>
<tr><td>guard_nest</td><td>ATOM</td><td>slow.scene_structures</td><td>CONTAINS_ANY</td><td>guard_nest_value</td></tr>
<tr><td>guard_all</td><td>ALL</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
<tr><td>cold_any</td><td>ATOM</td><td>slow.cold_severity</td><td>GT</td><td>cold_any_value</td></tr>
<tr><td>summer_any</td><td>ATOM</td><td>slow.oxythermal_compression</td><td>GT</td><td>summer_any_value</td></tr>
<tr><td>forage_state</td><td>ATOM</td><td>slow.pelagic_forage_state</td><td>EQ</td><td>forage_state_value</td></tr>
<tr><td>forage_available</td><td>ATOM</td><td>slow.open_water_forage_availability</td><td>GT</td><td>forage_available_value</td></tr>
<tr><td>forage_all</td><td>ALL</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
<tr><td>g3_spring_date</td><td>ATOM</td><td>slow.day_of_year</td><td>BETWEEN</td><td>g3_spring_date_value</td></tr>
<tr><td>g3_warm</td><td>ATOM</td><td>slow.recent5day_temp_c</td><td>GE</td><td>g3_warm_value</td></tr>
<tr><td>g3_spring</td><td>ALL</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
<tr><td>g3_fall_date</td><td>ATOM</td><td>slow.day_of_year</td><td>BETWEEN</td><td>g3_fall_date_value</td></tr>
<tr><td>g3_cool</td><td>ATOM</td><td>slow.recent5day_temp_c</td><td>LE</td><td>g3_cool_value</td></tr>
<tr><td>g3_fall</td><td>ALL</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
<tr><td>g3_either</td><td>ANY</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
<tr><td>q_hook</td><td>ATOM</td><td>gear.hook_size_index</td><td>GE</td><td>q_hook_value</td></tr>
<tr><td>q_bait</td><td>ATOM</td><td>gear.bait_size_cm</td><td>GE</td><td>q_bait_value</td></tr>
<tr><td>q_big_gear</td><td>ALL</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
<tr><td>q_inactive</td><td>ATOM</td><td>quality_context.time_band</td><td>IN</td><td>q_inactive_value</td></tr>
<tr><td>q_cold</td><td>ATOM</td><td>quality_context.water_temp_c</td><td>LE</td><td>q_cold_value</td></tr>
<tr><td>q_night</td><td>ATOM</td><td>quality_context.time_band</td><td>IN</td><td>q_night_value</td></tr>
<tr><td>q_coldnight</td><td>ALL</td><td>N/A</td><td>N/A</td><td>N/A</td></tr>
</table>
