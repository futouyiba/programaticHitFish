以下是针对 URL 为 https://app.notion.com/p/3d7a4137d23681e8b9f2c532513b81a4 的页面 "fetch" 的结果，截至 2026-09-10T13:36:59.889Z：
<page url="https://app.notion.com/p/3d7a4137d23681e8b9f2c532513b81a4">
<ancestor-path>
<parent-page url="https://app.notion.com/p/3d6a4137d23681338596c10634e31c6b" title="鱼种参考库｜全库现实/策略研究与 FCF 机制发现 R2"/>
<ancestor-2-page url="https://app.notion.com/p/3d5a4137d23681a28bc7e3c75172feb8" title="公共资料｜鱼种参考资料库｜V3鱼总表精选"/>
<ancestor-3-page url="https://app.notion.com/p/3cca4137d2368152bcd4dadaa0ab9e47" title="Fish-Centric Conditional Funnel｜Start Here / Agent Router"/>
</ancestor-path>
<properties>
{"title":"FISH-R07｜Research Package｜FR3 CLOSED"}
</properties>
<iconMetadata>null</iconMetadata>
<content>
## Machine Status
```plain text
CURRENT_STATUS: FR1 / FISH-R07 RESEARCH_PACKAGE_READY
BATCH_ID: FISH-R07
SPECIES_COUNT: 26 (25 identity-confirmed + 1 product-scope-deferred cephalopod；0 quarantine)
STORY_COUNT: 26
COVERAGE_COMPLETE: 26/26 story-linked；累计 DB 168 Coverage 行 = 166 distinct 鱼种 + 2 已知双行（雀鳝 R02/R04、大口黑鲈 B01/R04，待 Cross-Batch 处置）；本批 26 行无重复
SELF_QA: COMPLETE（持久角色会话自写自核）
COLD_REVIEW: COMPLETE (worker-level; independent evidence review pending)
NEXT_STATE: FR2 INDEPENDENT_EVIDENCE_REVIEW
REPRESENTATION_STATUS: NOT ENTERED
WRITE_STATUS: SELF-WRITTEN (persistent role session, readback verified)
```
## Scope and Stop Point
FISH-R07 继续 R2 Campaign。切片：§4 优先级 5（海水与特殊底栖/软体/鳐鲨等边界案例）主体 + 优先级 6（普通补齐）。鲨/鳐/魟电感知系、鲽鲆形态对照系、亚口科磿螺系、头足类非鱼边界、河鲀高潮产卵边界。本包止于 FR1；不进入 Representation、PT1–PT4、Table-vs-DSL 或 Design Authority。
## Coverage Result
26 条 Coverage 行（BatchID=FISH-R07、Complete、Self-QA Passed、鱼种 relation 全挂）。选鱼：V3 库 267 减已覆盖（前六批 DB 142 行 = 140 distinct + 2 双行）后按 §4 优先级 5/6 选 26。**选鱼剔除 2 条存疑条目**：臼齿鱼（Mylopharodon conocephalus——FishBase 页面分布描述与 V3/学名矛盾且资料极薄，身份/资料双存疑留人工确认）；圆吻鲴（Distoechodon tumirostris——FishBase/Wikipedia 均被内容过滤拦截，源不可达）→ 换小冠太阳鱼。黄盖鲽 V3 学名 Myzopsetta ferruginea 经 FishBase 接受名验证一致（原疑虑消除）。
## Mechanism Story Result
26 条 Story；域分布（create-pages 响应回显实算，multi_select 按出现次数）：Ordinary Feeding 26、Spatial/Habitat 25、Sensory/Presentation 8、Lifecycle/Migration 10、Reproduction/Guard 6、**Capture Boundary 4（首次成轴出现：河魟毒刺/拟乌贼 jig/河鲀 TTX/沙鮻潜沙；FIX-001 F-E-b 补注：非同质聚类——人类侧食物安全×2（河鲀 TTX+R06 补标 ciguatoxic 系）/捕获路径×1（无饵 jig）/鱼侧反捕食×1（潜沙），轴定义域待显式声明）**（合计 79 标签）；ResearchDepth：L3×4（鼠鲨/莱氏拟乌贼/星点东方鲀/双点美鱥，各双源）、L2×22。Confidence：High 20 / Medium 6（FISH-R07-FIX-001 F-B 复算修正）。
<table header-row="true">
<tr>
<td>#</td>
<td>鱼</td>
<td>Story 短语</td>
<td>Pattern</td>
<td>Depth</td>
</tr>
<tr>
<td>1</td>
<td>鼠鲨 Porbeagle</td>
<td>Endothermic Migrating Shark</td>
<td>P01+P05</td>
<td>L3</td>
</tr>
<tr>
<td>2</td>
<td>白斑角鲨 Spiny Dogfish</td>
<td>Passive-Electrosense Foraging School</td>
<td>P01+P05</td>
<td>L2</td>
</tr>
<tr>
<td>3</td>
<td>棘背钝头鳐 Thorny Skate</td>
<td>Cold-Deep Electrosense Bottom Forager</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>4</td>
<td>大西洋黄貂鱼 Atlantic Stingray</td>
<td>Euryhaline Bottom Forager</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>5</td>
<td>眼斑河魟 River Stingray</td>
<td>Freshwater Ray Venom Boundary</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>6</td>
<td>莱氏拟乌贼 Bigfin Reef Squid</td>
<td>Cephalopod Boundary + Phototaxis Jig</td>
<td>Boundary/Deferred</td>
<td>L3</td>
</tr>
<tr>
<td>7</td>
<td>星点东方鲀 Grass Puffer</td>
<td>High-Tide Beach Spawning + TTX Boundary</td>
<td>P01</td>
<td>L3</td>
</tr>
<tr>
<td>8</td>
<td>条石鲷 Rock Bream</td>
<td>Reef Beak-Crusher Boundary</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>9</td>
<td>沙鮻 Silver Sillago</td>
<td>Sand-Burial Bottom Feeder</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>10</td>
<td>长背亚口鱼 Blue Sucker</td>
<td>Swift-Chute Benthic Sucker</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>11</td>
<td>河红马鱼 River Redhorse</td>
<td>Rock-Pool Mollusk Feeder</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>12</td>
<td>金红马鱼 Golden Redhorse</td>
<td>Insect-Larvae Bottom Feeder</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>13</td>
<td>水牛鱼 Smallmouth Buffalo</td>
<td>Throat-Plate Mollusk Grinder</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>14</td>
<td>金眼鱼 Goldeye</td>
<td>Nocturnal Turbid-River Omnivore</td>
<td>P01+P05</td>
<td>L2</td>
</tr>
<tr>
<td>15</td>
<td>女巫鲽 Witch Flounder</td>
<td>Cold-Deep Mud Flatfish</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>16</td>
<td>美洲拟鲽 Winter Flounder</td>
<td>Diurnal Nearshore Bottom Feeder</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>17</td>
<td>大西洋黄盖鲽 Yellowtail Flounder</td>
<td>Polychaete Mud-Flat Forager</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>18</td>
<td>大西洋牙鲆 Summer Flounder</td>
<td>Left-Eye Burrow Ambusher</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>19</td>
<td>唇䱻 Barbel Steed</td>
<td>Barbel-Bottom Insectivore</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>20</td>
<td>淡水石首鱼 Freshwater Drum</td>
<td>Sound-Producing Bottom Omnivore</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>21</td>
<td>黑鲷 Blackhead Seabream</td>
<td>Bay-Reef Shellfish Biter</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>22</td>
<td>日本鲭 Chub Mackerel</td>
<td>Size-Graded Night Schooling</td>
<td>P01+P05</td>
<td>L2</td>
</tr>
<tr>
<td>23</td>
<td>绿青鳕 Saithe</td>
<td>Gregarious Seasonal Migrator</td>
<td>P01+P05</td>
<td>L2</td>
</tr>
<tr>
<td>24</td>
<td>双点美鱥 Hornyhead Chub</td>
<td>Pebble-Mound Guard + Nest Associates</td>
<td>P01+P04</td>
<td>L3</td>
</tr>
<tr>
<td>25</td>
<td>月眼鱼 Mooneye</td>
<td>Deep-Pool River Pelagic</td>
<td>P01</td>
<td>L2</td>
</tr>
<tr>
<td>26</td>
<td>小冠太阳鱼 Redear Sunfish</td>
<td>Mollusk-Preferring Sunfish</td>
<td>P01</td>
<td>L2</td>
</tr>
</table>
## Semantic Pattern Result
Existing Pattern 25 + Boundary 1（拟乌贼 Product Scope Deferred——头足类无鱼响应骨架，不套 P01）；New Pattern Candidate 0；Compression 0；Semantic Open 0。P04×1（双点美鱥石巢）。同属对照：Moxostoma 2/2、Hiodon 2/2、鲽科 4 例（女巫/拟鲽/黄盖/大比目鱼 R06 右鲽系+牙鲆左鲆）形态对照、Ictiobus 3/3、Scomber 2/2。不升 Design Authority。
## Coverage Delta Candidates（3）
1. **被动电感知双例**（白斑角鲨+棘背钝头鳐，FishBase 原文 "Detects weak electric fields"）：电轴感知端样本——CD-R05-01（电鳗发电端）的对偶面；按感知面 owner 记录不建新轴，K8 电轴前提的感知侧输入。
2. **光 cue 轴**（莱氏拟乌贼：夜钓集鱼灯 "usually done at night and utilise bright lights" + 趋光 "strong positive phototactic behaviour"，两句分引）：集鱼灯人工光场改变遇鱼分布+无饵 jig 捕获——scent/电轴之后的新 cue 模态候选；附产品边界（头足类）。
3. （以上两条为主；其余样本如石巢借巢记 Open Question 不立 Candidate）
## Evidence Chain and Open Findings
- 特殊观察点（Coordinator 提示电鳗三段模板的展开）：①被动电感知（角鲨/鳐感知端 vs 电鳗发电端——同一电场 cue 轴的双向语义）②光诱捕获（拟乌贼——光轴+无饵 jig 非常规捕获路径，B02 关联）③高潮海滩产卵（河鲀——潮汐窗机会生命周期+TTX 食物安全边界）④磿螺咽喉机制系（水牛鱼原文/河红马/小冠太阳鱼偏好）⑤潜沙反捕食（沙鮻）⑥石巢共生（双点美鱥——护巢仅对同种+异种借巢+杂交，P04 内部结构变量 guard target specificity）。
- 资料缺口：拟乌贼 FishBase 公开版无页（Wiki 主源，需补资料）；唇䱌/黑鲷/小冠太阳鱼磿碎与性转换面 EO。
- 选鱼剔除：臼齿鱼（身份/资料矛盾）、圆吻鲴（源被过滤层拦截）——待人工确认后补批。
- 保护边界：鼠鲨 VU/CITES II；短吻鲟系 OPS 先例延续（本批无新增禁捕种）。
## Worker Cold Review
四类自查：①Missed Story/False Default——薄资料种（月眼鱼/长背亚口/眼斑河魟）保留 EO；拟乌贼主动不套 P01（非鱼响应骨架）避免 False Fit；②Over-fragmentation——鲽科四例形态对照不拆独立故事（左右眼形态差异不买 Mode）；③Trigger Open catch-all——0 条 Open（拟乌贼用 Field Opportunity Candidate）；④Coverage Delta inflation——仅 2 主题 3 条（电感知双例合并为一主题）。
## Handoff Contract
```plain text
FROM_ROLE: FCF-FISH-RESEARCHER
TO_ROLE: FCF-EVIDENCE-REVIEWER
BATCH_ID: FISH-R07
CURRENT_STATE: FR1 RESEARCH_PACKAGE_READY
REQUESTED_ACTION: FR2 INDEPENDENT_EVIDENCE_REVIEW
EXPECTED_OUTPUT: scoped verdict with level, scope, baseline, proves, does_not_prove, open_findings, verdict
BLOCKING_FINDINGS: NONE
```
## Representative Coverage / Story Links（全量 26+26）
- <mention-page url="https://app.notion.com/p/3d7a4137d23681eca709f83a8b08f980"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681248a12ca0c07aa0147"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236817f9678d8251d464e80"/> → <mention-page url="https://app.notion.com/p/3d7a4137d236813987e8e5adaffe482f"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681eb86f6c6162e2ab125"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681c4bba0e651f58c29fc"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236813b940af55675a49a02"/> → <mention-page url="https://app.notion.com/p/3d7a4137d236813bb4ddc091e4732e0f"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236813ca413c34cc1ff3d43"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681768a31c8e1a247c668"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681169aa3c0249e3b2143"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681138057c6270bcbdf5a"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681fe907bfc200da6820f"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681838c4bec5c5353659a"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236817798a5f7aae4cf8299"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681b3b45fcd8e68ade468"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681069e66de0a0c16d41d"/> → <mention-page url="https://app.notion.com/p/3d7a4137d2368139a400f025268c20b6"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681509eeaf251f1447818"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681b9921dcad805a00e41"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236819cb2bec0a6fecf17a3"/> → <mention-page url="https://app.notion.com/p/3d7a4137d2368158850bd6a92a93970a"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236813bb367dae276c06857"/> → <mention-page url="https://app.notion.com/p/3d7a4137d236816a9256c990073eacf8"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d2368133bacad0228f32a42b"/> → <mention-page url="https://app.notion.com/p/3d7a4137d236817cacbdd7c70d8bdafa"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681de8c58deee61116575"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681a68501d8a0868160ba"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681f88d67fd4577fb14b4"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681b29b49da80beef6f31"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681eeb0e4cab68b7be182"/> → <mention-page url="https://app.notion.com/p/3d7a4137d2368131bed9f3f0c7f7a9db"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d2368177a936e161894af916"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681aa883bd78444277315"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236819bb379e24be9d7e754"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681ea964ef147f5413ce8"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236811ea1efd1b919e2b461"/> → <mention-page url="https://app.notion.com/p/3d7a4137d236817fb981e316c8c683d4"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681778e8cc3b789f98f2b"/> → <mention-page url="https://app.notion.com/p/3d7a4137d236819bb8bee26d21b3e0d3"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d2368191ac6cfb97ca6d74dd"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681ef9f22ce9fd16a66f6"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681e789dce8299f2041e3"/> → <mention-page url="https://app.notion.com/p/3d7a4137d2368104ac0dc5037c9e75c4"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681e4a61cc667ded9c67e"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681f5b8e3e7d59f8d57ff"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d236812eb0e0e9766db6bc56"/> → <mention-page url="https://app.notion.com/p/3d7a4137d236812a955dcf18edc3cf39"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d23681d9a7eafd0efeb358c9"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681e49bdfda910800fd58"/>
- <mention-page url="https://app.notion.com/p/3d7a4137d2368106820acc82fee7c950"/> → <mention-page url="https://app.notion.com/p/3d7a4137d23681aea3d1c107ba0c3f9e"/>
</content>
</page>
