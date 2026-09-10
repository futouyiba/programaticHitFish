### R2-A / PredicateMember
PK(parent_id,display_index)；parent/child FK→Predicate；ALL/ANY 至少一个子节点，NOT 恰一个；禁止环。display_index 只用于作者阅读，没有 Runtime 顺序意义；全部条件是纯读。
<table header-row="true" fit-page-width="true">
<tr><td>parent_id</td><td>display_index</td><td>child_id</td></tr>
<tr><td>C03_high</td><td>1</td><td>C03_good_match</td></tr>
<tr><td>C03_high</td><td>2</td><td>C03_drift</td></tr>
<tr><td>guard_all</td><td>1</td><td>guard_dates</td></tr>
<tr><td>guard_all</td><td>2</td><td>guard_temp</td></tr>
<tr><td>guard_all</td><td>3</td><td>guard_nest</td></tr>
<tr><td>forage_all</td><td>1</td><td>forage_state</td></tr>
<tr><td>forage_all</td><td>2</td><td>forage_available</td></tr>
<tr><td>g3_spring</td><td>1</td><td>g3_spring_date</td></tr>
<tr><td>g3_spring</td><td>2</td><td>g3_warm</td></tr>
<tr><td>g3_fall</td><td>1</td><td>g3_fall_date</td></tr>
<tr><td>g3_fall</td><td>2</td><td>g3_cool</td></tr>
<tr><td>g3_either</td><td>1</td><td>g3_spring</td></tr>
<tr><td>g3_either</td><td>2</td><td>g3_fall</td></tr>
<tr><td>q_big_gear</td><td>1</td><td>q_hook</td></tr>
<tr><td>q_big_gear</td><td>2</td><td>q_bait</td></tr>
<tr><td>q_coldnight</td><td>1</td><td>q_cold</td></tr>
<tr><td>q_coldnight</td><td>2</td><td>q_night</td></tr>
</table>
