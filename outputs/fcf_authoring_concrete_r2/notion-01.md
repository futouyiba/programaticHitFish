### 25.4. 表布局与字段合同
<table header-row="true" fit-page-width="true">
<tr><td>表</td><td>全列</td><td>去重实际行数</td><td>权限</td></tr>
<tr><td>Binding</td><td>binding_id / surface / subject / template_id / status</td><td>38</td><td>作者数据</td></tr>
<tr><td>Slot</td><td>binding_id / slot / enabled / ref_kind / ref_id</td><td>100</td><td>作者数据</td></tr>
<tr><td>Parameter</td><td>parameter_id / type / value / unit</td><td>32</td><td>作者数据</td></tr>
<tr><td>CurvePoint</td><td>profile_id / x / y</td><td>159</td><td>作者数据</td></tr>
<tr><td>Predicate</td><td>node_id / kind / field / operator / parameter_id</td><td>29</td><td>作者数据</td></tr>
<tr><td>PredicateMember</td><td>parent_id / display_index / child_id</td><td>17</td><td>作者数据</td></tr>
<tr><td>ResponseBand</td><td>binding_id / priority / predicate_id / response_strength</td><td>4</td><td>作者数据</td></tr>
<tr><td>GroupShare</td><td>binding_id / group / predicate_id / share_kind / share_ref / input_field</td><td>7</td><td>作者数据</td></tr>
<tr><td>QualityWeight</td><td>binding_id / bucket / base_weight</td><td>32</td><td>作者数据</td></tr>
<tr><td>QualityModifier</td><td>binding_id / rule_id / predicate_id / bucket / multiplier</td><td>64</td><td>作者数据</td></tr>
<tr><td>Boundary</td><td>case_id / scope / reason</td><td>3</td><td>作者数据</td></tr>
<tr><td>TemplateStep</td><td>template_id / step / operation / input / output / failure</td><td>46</td><td>只读目录</td></tr>
</table>
