### R2-A / GroupShare
PK(binding_id,group)；predicate FK。share_kind=PARAMETER 时 share_ref→[0,1]标量且 input_field=N/A；PROFILE 时 ref→CurvePoint 并指定慢速输入。全部条件同快照、同时算；总和超1拒绝；Normal 不单列可编辑 Share。
<table header-row="true" fit-page-width="true">
<tr><td>binding_id</td><td>group</td><td>predicate_id</td><td>share_kind</td><td>share_ref</td><td>input_field</td></tr>
<tr><td>BASS_G</td><td>Guarding</td><td>guard_all</td><td>PARAMETER</td><td>BassGuardShare</td><td>N/A</td></tr>
<tr><td>BASS_G</td><td>ColdSlow</td><td>cold_any</td><td>PROFILE</td><td>BassColdShare</td><td>slow.cold_severity</td></tr>
<tr><td>BASS_G</td><td>SummerStress</td><td>summer_any</td><td>PROFILE</td><td>BassSummerShare</td><td>slow.oxythermal_compression</td></tr>
<tr><td>BASS_G</td><td>ForageChase</td><td>forage_all</td><td>PROFILE</td><td>BassForageShare</td><td>slow.open_water_forage_availability</td></tr>
<tr><td>G1</td><td>Guarding</td><td>guard_all</td><td>PARAMETER</td><td>BassGuardShare</td><td>N/A</td></tr>
<tr><td>G2</td><td>Guarding</td><td>guard_all</td><td>PARAMETER</td><td>BassGuardShare</td><td>N/A</td></tr>
<tr><td>G3</td><td>Seasonal</td><td>g3_either</td><td>PARAMETER</td><td>G3Share</td><td>N/A</td></tr>
</table>
