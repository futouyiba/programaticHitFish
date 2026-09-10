### R2-A / ResponseBand
PK(binding_id,priority)；仅 R_BANDS，priority 为唯一整数递增，predicate_id FK；结果 response_strength∈[0,1]。FIRST_MATCH；无命中用显式 Default。这里的 priority 是同一响应分档规则顺序，绝非 Defense/Feeding 优先级。
<table header-row="true" fit-page-width="true">
<tr><td>binding_id</td><td>priority</td><td>predicate_id</td><td>response_strength</td></tr>
<tr><td>C03_R</td><td>10</td><td>C03_high</td><td>0.8</td></tr>
<tr><td>C03_R</td><td>20</td><td>C03_some_match</td><td>0.25</td></tr>
<tr><td>C04_R</td><td>10</td><td>C04_good_match</td><td>0.8</td></tr>
<tr><td>C04_R</td><td>20</td><td>C04_some_match</td><td>0.25</td></tr>
</table>
