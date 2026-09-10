### R2-A / Parameter
PK parameter_id；type=number/bool/string/set<string>；value 按 type 解析（BETWEEN 的数值二元范围见特例）；unit 必须一致。所有本批数字是 DEMO 校验值，不是生态/平衡标定。
<table header-row="true" fit-page-width="true">
<tr><td>parameter_id</td><td>type</td><td>value</td><td>unit</td></tr>
<tr><td>C01_B_Anchor</td><td>string</td><td>stable_cover</td><td>category</td></tr>
<tr><td>C02_B_Anchor</td><td>string</td><td>stable_cover</td><td>category</td></tr>
<tr><td>C05_B_Anchor</td><td>string</td><td>stable_cover</td><td>category</td></tr>
<tr><td>C03_R_Default</td><td>number</td><td>0</td><td>1</td></tr>
<tr><td>C03_good_match_value</td><td>number</td><td>0.7</td><td>1</td></tr>
<tr><td>C03_drift_value</td><td>number</td><td>0.6</td><td>1</td></tr>
<tr><td>C03_some_match_value</td><td>number</td><td>0.3</td><td>1</td></tr>
<tr><td>C04_R_Default</td><td>number</td><td>0</td><td>1</td></tr>
<tr><td>C04_good_match_value</td><td>number</td><td>0.7</td><td>1</td></tr>
<tr><td>C04_some_match_value</td><td>number</td><td>0.3</td><td>1</td></tr>
<tr><td>guard_dates_value</td><td>range&lt;number&gt;</td><td>[100,160]</td><td>day_of_year</td></tr>
<tr><td>guard_temp_value</td><td>number</td><td>15</td><td>°C</td></tr>
<tr><td>guard_nest_value</td><td>set&lt;string&gt;</td><td>[&quot;nest_cover&quot;]</td><td>1</td></tr>
<tr><td>cold_any_value</td><td>number</td><td>0</td><td>1</td></tr>
<tr><td>summer_any_value</td><td>number</td><td>0</td><td>1</td></tr>
<tr><td>forage_state_value</td><td>bool</td><td>True</td><td>1</td></tr>
<tr><td>forage_available_value</td><td>number</td><td>0</td><td>1</td></tr>
<tr><td>BassGuardShare</td><td>number</td><td>0.2</td><td>1</td></tr>
<tr><td>g3_spring_date_value</td><td>range&lt;number&gt;</td><td>[80,130]</td><td>day_of_year</td></tr>
<tr><td>g3_warm_value</td><td>number</td><td>12</td><td>°C</td></tr>
<tr><td>g3_fall_date_value</td><td>range&lt;number&gt;</td><td>[250,290]</td><td>day_of_year</td></tr>
<tr><td>g3_cool_value</td><td>number</td><td>18</td><td>°C</td></tr>
<tr><td>G3Share</td><td>number</td><td>0.25</td><td>1</td></tr>
<tr><td>BASS_N_B_Anchor</td><td>string</td><td>stable_cover</td><td>category</td></tr>
<tr><td>BASS_G_B_Anchor</td><td>string</td><td>nest_site</td><td>category</td></tr>
<tr><td>BASS_S_B_OxygenMin</td><td>number</td><td>3</td><td>mg/L</td></tr>
<tr><td>BASS_F_B_ForageMin</td><td>number</td><td>0.2</td><td>1</td></tr>
<tr><td>q_hook_value</td><td>number</td><td>3</td><td>1</td></tr>
<tr><td>q_bait_value</td><td>number</td><td>8</td><td>cm</td></tr>
<tr><td>q_inactive_value</td><td>set&lt;string&gt;</td><td>[&quot;inactive&quot;]</td><td>1</td></tr>
<tr><td>q_cold_value</td><td>number</td><td>8</td><td>°C</td></tr>
<tr><td>q_night_value</td><td>set&lt;string&gt;</td><td>[&quot;night&quot;]</td><td>1</td></tr>
</table>
