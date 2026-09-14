# -*- coding: utf-8 -*-
"""手册 v2 生成器（重写版）：每型=特点+骨架链+完全展开实例伪脚本+真实结构配置表+模板级参数轴
实例源：rb（RB 冻结真形体）| file（B 系列表达文件节）| synth（语义展开）| ledger（CRR）"""
import json, io, re, os

BASE = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
REPO = os.path.abspath(BASE + '/../..')
OUT = REPO + '/outputs/manual/notion'

bodies = {}
for b in ('CENSUS-REBUILD-001', 'CENSUS-REBUILD-002', 'CENSUS-REBUILD-003', 'CENSUS-RERUN-SINGLE-001'):
    for l in io.open(f'{REPO}/fish_logic_census/batches/{b}/blind_programs.jsonl', encoding='utf-8'):
        try: o = json.loads(l)
        except Exception: continue
        bodies[o['program_id']] = o

def steps_of(o):
    sl = o.get('surface_owned_logic') or {}
    if isinstance(sl, dict) and sl.get('ordered_steps'): return sl['ordered_steps']
    return o.get('ordered_steps') or []

def pretty_tiers(raw):
    if not raw:
        raw = ['preferred=全额', 'tolerated=×衰减', 'excluded=×0.01 软出局']
    out = []
    for t in raw:
        if t.startswith('preferred'): out.append('weight ×1.0（全额乘入），继续下一步')
        elif t.startswith('tolerated'): out.append('weight ×衰减系数（Profile 值域，不清零），继续下一步')
        elif t.startswith('excluded'): out.append('返回 weight×0.01（软出局 EARLY_RETURN——非零，仍可参与下游选择；本链在此转折点终止）')
        else: out.append(t)
    return out

PRE3 = ['如果 ∈ 最适应档（preferred）', '否则如果 ∈ 可接受档（tolerated）', '否则（不居留档 excluded）']

def expand_rb(pid):
    o = bodies[pid]
    sts = steps_of(o)
    sp = o.get('species_id') or '?'
    reads, lines = [], ['weight = 1.0']
    n = 0
    for st in sts:
        op = st.get('op', '?')
        axis = st.get('axis') or st.get('factor') or ''
        n += 1
        if axis: reads.append(axis.split('（')[0])
        if op.startswith('GATE') or st.get('kind') == 'GATE':
            lines += [f'第 {n} 步 GATE[{axis or op}]（二元硬门——非三档）：',
                      f'    命中门条件 → 进入第 {n+1} 步',
                      f'    不命中 → 返回 weight×0.01（EARLY_RETURN 软出局——转折点 {n}）']
        elif 'SLOT' in op or st.get('slot_kind') == 'modifier':
            lines.append(f'第 {n} 步 SLOT[{axis}]（modifier 槽位乘入）：')
            for t in (st.get('tiers') or ['槽全额=×槽系数合入', '槽削减=×衰减合入', '槽极低=×极低削减合入']):
                lines.append(f'    {t}')
        else:
            lines.append(f'第 {n} 步 EVAL[{axis or op}]（三档分级命中）：')
            for pre, t in zip(PRE3, pretty_tiers(st.get('tiers'))):
                lines.append(f'    {pre} → {t}')
            lines.append(f'    （档位成员与阈值＝@{sp}…Profile 值域，不冻结）')
    lines.append(f'返回 weight（{n} 步渐进累积完成——无终步合并步）')
    head = ['读取：' + '；'.join(dict.fromkeys(reads)), ''] if reads else []
    basis = (o.get('order_derivation') or {}).get('basis') or []
    return head + lines, basis, sp, sts

def extract_file(rel, cfg_sec, code_sec):
    s = io.open(f'{REPO}/{rel}', encoding='utf-8').read()
    m = re.search(rf'### {re.escape(cfg_sec)}.*?\n(.*?)(?=\n### |\n## |\Z)', s, re.S)
    cfg = '\n'.join(re.findall(r'^\|.*\|$', m.group(1), re.M)) if m else '（配置表提取失败）'
    m2 = re.search(rf'### {re.escape(code_sec)}.*?```[a-z ]*\n(.*?)```', s, re.S)
    code = m2.group(1).rstrip() if m2 else '（伪脚本提取失败）'
    return cfg, code

MAN = json.load(io.open(f'{REPO}/fish_logic_census/template_manual_v10.merged.json', encoding='utf-8'))
fams = {f['registry_id']: f for f in MAN['families']}

def pick(suffix, prefix='P-RB'):
    for k in bodies:
        if k.endswith(suffix) and k.startswith(prefix): return k
    for k in bodies:
        if k.endswith(suffix): return k
    raise KeyError(suffix)

EXEMPLARS = {
 'SPACE_FIRST_DUAL_TIER_CHAIN': ('rb', 'P-RB1-RKB-BAKE'),
 'FORAGE_FIRST_DUAL_TIER_CHAIN': ('rb', 'P-RB1-POR-BAKE'),
 'TIERED_SINGLE_FACTOR_CHAIN': ('rb', pick('-TIL2-BAKE') if any(k.endswith('-TIL2-BAKE') for k in bodies) else pick('-KGO-BAKE')),
 'GATED_COVER_TIER_CHAIN': ('file', 'outputs/full_authoring/normal2/species/arctic_grayling.md', '2.1', '2.2', '北极茴鱼（normal2 表达文件·伏击门 GATE_RIFFLE_GRAVEL·已 ×0.01 对齐）'),
 'GUARD_ANCHOR_TIERED_COMBINE_CHAIN': ('file', 'outputs/full_authoring/guarding/species/bluegill.md', '2.1', '2.2', '蓝鳃太阳鱼（guarding 表达文件·canonical 成员·已 ×0.01 对齐）'),
 'NOCTURNAL_LIGHTSLOT_CHAIN': ('file', 'outputs/full_authoring/guarding/species/wels_catfish.md', '2.3', '2.4', '欧洲巨鲶（Normal 面·夜行低光槽·已 ×0.01 对齐）'),
 'LAYER_AXIS_DUAL_TIER_CHAIN': ('rb', pick('-CHN-BAKE')),
 'ZONE_SUBSTRATE_RESOURCE_CHAIN': ('rb', pick('-GRH-BAKE')),
 'SOFT_TRIPLE_TIER_CHAIN': ('rb', pick('-CAR1-BAKE')),
 'ZONE_DEPTH_SUBSTRATE_RESOURCE_CHAIN': ('rb', pick('-SMB-BAKE')),
 'GATE_SUBSTRATE_TEMPBAND_RESOURCE_CHAIN': ('rb', 'P-RB1-WIT-BAKE'),
 'GUARD_ANCHOR_TURBIDITY_CONTEXT_CHAIN': ('file', 'outputs/full_authoring/guarding/species/jaguar_cichlid.md', '2.1', '2.2', '淡水石斑（浊水双亲·护巢四步+浊度语境步）'),
 'STRUCTURE_LIGHTSLOT_FORAGE_TRIPLE_CHAIN': ('rb', pick('-GW-BAKE') if any(k.endswith('-GW-BAKE') for k in bodies) else pick('-GT-BAKE')),
 'HABITAT_FORAGE_FLOODSLOT_CHAIN': ('rb', 'P-RB1-BAS-BAKE'),
 'HARD_GATED_FACTOR_COMBINE': ('file', 'outputs/full_authoring/guarding/species/lungfish.md', '2.3', '2.4', '南美肺鱼（Normal 面·水面可达+温度极值双硬门）'),
 'EXTREME_TEMP_GATED_TIERED_COMBINE_CHAIN': ('file', 'outputs/full_authoring/guarding/species/oscar.md', '2.3', '2.4', '地图鱼（Normal 面·极值门+无序因子集）'),
 'PATCH_GATED_DUAL_SLOT_COMBINE_CHAIN': ('rb', pick('-BRT12-BAKE')),
 'STRUCTURE_FIRST_QUAD_TIER_CHAIN': ('rb', 'P-RB3-BLU-HAB-BAKE'),
 'GATED_STRUCTURE_TEMP_TIME_QUAD_CHAIN': ('rb', 'P-RB3-HNC-HAB-BAKE'),
 'LAYER_TEMP_STRUCTURE_TRIPLE_CHAIN': ('rb', 'P-RB3-RBP-HAB-BAKE'),
 'GATED_TEMP_STRUCTURE_TIME_QUAD_CHAIN': ('rb', 'P-RB3-ARA-HAB-BAKE'),
 'BROODED_DEGENERATE_TWO_STEP_CHAIN': ('rb', 'P-RB3-ARO-RESP-RESP'),
 'CONSTRAINED_RELATIVE_REFUGE': ('ledger',),
 'TYPED_TARGET_RESPONSE': ('file', 'outputs/full_authoring/guarding/species/bluegill.md', '3.1', '3.2', '蓝鳃太阳鱼（Response 面·R-T1 单通道·DECIDE 三档已展开）'),
 'FOOD_FIELD_FEEDING_RESPONSE': ('synth', 'FOOD_FIELD_FEEDING_RESPONSE'),
 'GUARD_CONFLICT_DUAL_PATH_RESPONSE': ('synth', 'GUARD_CONFLICT_DUAL_PATH_RESPONSE'),
 'STATE_GATED_MULTI_PATH_RESPONSE': ('synth', 'STATE_GATED_MULTI_PATH_RESPONSE'),
 'CUE_GUIDED_APPROACH_AVOID': ('synth', 'CUE_GUIDED_APPROACH_AVOID'),
}

SYNTH = {
 'FOOD_FIELD_FEEDING_RESPONSE': dict(
   inst='鲢/鳙类场摄食（FOOD_FIELD 族·16 成员）',
   code=['读取 当前格子的滤食场浓度事实（prey_fields 绑定的浮游生物量——UsableForageAvailability 契约输出）', '',
         'EVAL_FIELD_CONCENTRATION（三档分级命中）：',
         '    如果 ∈ 富集档 → weight×1.0（全额乘入），继续',
         '    否则如果 ∈ 中等档 → weight×衰减系数（不清零），继续',
         '    否则（贫瘠档）→ 返回 weight×0.01（软出局——场没了，格子出局）', '',
         'DECIDE_RESPONSE（三档）：',
         '    FieldEvaluation ∈ 摄食活跃档 → 返回 Response(FieldFeeding)（全额响应）',
         '    ∈ 边际档 → 低强度滤食响应（削减不清零）',
         '    否则 → 无响应（出局）', '',
         '返回 FieldFeedingResponse'],
   cfg=[['BakeTemplate','BA-FIELD-CONCENTRATION（渐进累积）'],['evaluand','field（场浓度——RETURN 硬判据：与离散目标 TYPED 分立）'],['prey_fields','@…FilterFieldPreyFields（浮游 prey class 绑定）'],['@ConcentrationProfile','三档档位成员=Profile 值域不冻结'],['DECIDE 档','接受=全额 / 边际=削减 / 无响应=出局']]),
 'GUARD_CONFLICT_DUAL_PATH_RESPONSE': dict(
   inst='护巢期双路径并行（live 例 1C 形态·§17.5 RR-T2）',
   code=['读取 当前格子的食物机会事实', '读取 侵入者威胁事实（侵入距离/持续时间/威胁 Cue）', '',
         '并行（∥ 拓扑——两条路径同时评估，不是切换）：',
         '    路径 A：EVAL_FOOD_OPPORTUNITY → FoodEvaluation',
         '    路径 B：EVAL_INTRUDER_THREAT → ThreatEvaluation', '',
         'COMBINE_DUAL_PATH：',
         '    合算两路径评价（合并算子数学＝机制侧定义——OPERATOR 占位）', '',
         'DECIDE_RESPONSE（三档）：',
         '    威胁主导 → 返回 Response(Defense)',
         '    食物主导且无威胁 → 返回 Response(TargetFeeding)',
         '    双边际 → 低强度混合响应', '',
         '返回 Response'],
   cfg=[['ResponseTemplate','RR-DEFENSE-01 / RR-T2（∥ 双路径并行——≠IF 门互斥）'],['PathA.Evaluator','@FoodOpportunityProfile'],['PathB.Evaluator','@IntruderThreatProfile'],['CombineOp','COMBINE_DUAL_PATH（数学待机制侧）'],['仲裁注记','live V0：Guarding Group 只评 Defense（例 1C）——本族真值属 census↔live 对账']]),
 'STATE_GATED_MULTI_PATH_RESPONSE': dict(
   inst='停食洄游双例（大马哈鱼/美洲西鲱——§9.2 判例）',
   code=['读取 生命周期状态事实（洄游期 premise）', '',
         'IF[状态门]（互斥选径——与 ∥ 并行分立）：',
         '    命中洄游态 → 走径 A：',
         '        径 A：迁移行为主导（抵目标河段权重高）',
         '        摄食路径＝关闭（停食 premise——「停食≠不咬钩」中的停食侧）',
         '    未命中 → 走径 B：',
         '        径 B：常规 EVAL_TARGET_AS_FOOD + DECIDE 三档', '',
         '返回 Response'],
   cfg=[['StateGate','lifecycle=migrating（premise 状态门——IF 拓扑）'],['PathA','洄游径（停食 premise 携带）'],['PathB','常规摄食径（typed 评价）'],['判例','§9.2：∥ 并行竞争与 IF 门互斥不得互并']]),
 'CUE_GUIDED_APPROACH_AVOID': dict(
   inst='环境梯度趋避（单例族）',
   code=['读取 环境 cue 梯度事实（如溶氧梯度/温度梯度方向）', '',
         'EVAL_GRADIENT：',
         '    梯度方向与强度查询 @GradientProfile（三档=Profile 值域）',
         '    顺梯度（趋向有利） → 返回 Response(Approach)（趋近响应）',
         '    逆梯度（避开不利） → 返回 Response(Avoid)（避离响应）',
         '    中性 → 低响应继续', '',
         '返回 Approach/Avoid'],
   cfg=[['evaluand','环境 cue 梯度（非饵非场）'],['@GradientProfile','趋/避/中性三档=Profile 值域']]),
}

sems = '每步三档＝最适应·全额乘入 / 可接受·×衰减乘入 / 不居留·×0.01 软出局立即返回（非零仍可参与下游）；无终步合并步；GATE 硬门＝二元 EARLY_RETURN'

results = {}
for fid, f in fams.items():
    ex = EXEMPLARS.get(fid)
    if ex is None:
        for k, v in EXEMPLARS.items():
            if fid.startswith(k[:20]) or k.startswith(fid[:20]): ex = v; break
    axes_tbl = '\n'.join('| {} | {} |'.format(a, b) for a, b in f['axes'])
    parts = []
    parts.append('> **{}**（`{}`）｜面：{}｜状态：{}｜名义成员：{}\n'.format(f['cn'], fid, f['face'], f['status'], f['members']))
    parts.append('## 特点\n\n{}\n'.format(f['sig']))
    parts.append('## 骨架（一行链序）\n\n```plain text\n{}\n```\n'.format(' → '.join(f['pseudo'])))
    kind = ex[0]
    if kind == 'ledger':
        parts.append('## 完全展开实例\n\n（无成员——负证据台账载体，无程序实例）\n')
        parts.append('## 配置表（真实结构）\n\n（不适用——live 侧外来假说，7 批 284 条 non-match）\n')
    elif kind == 'rb':
        pid = ex[1]
        body_lines, basis, sp, sts = expand_rb(pid)
        basis_md = '\n'.join('- {}'.format(b) for b in basis[:6]) or '- （RS1 期真形体——basis 见批档）'
        parts.append('## 完全展开实例伪脚本（canonical 真形体：{}）\n\n（渐进累积完全展开——每个 early return 转折点显形；{}）\n\n```plain text\n{}\n```\n\n**顺序推导证据**（逐鱼推导依据，节选）：\n{}\n'.format(pid, sems, '\n'.join(body_lines), basis_md))
        n_eval = sum(1 for st in sts if not (st.get('op', '').startswith('GATE') or 'SLOT' in st.get('op', '')))
        n_gate = sum(1 for st in sts if st.get('op', '').startswith('GATE'))
        cfg_rows = [['BakeTemplate', '{}（渐进累积语义）'.format(fid)],
                    ['Step 数', '{} 步'.format(len(sts))],
                    ['Early Return 转折点数', '{}（每 EVAL 步 1 个不居留档出口{}）'.format(n_eval + n_gate, '＋每 GATE 步 1 个不过门出口' if n_gate else '')],
                    ['Combine', '无终步合并（weight 逐步累积）']]
        for i, st in enumerate(sts, 1):
            op = st.get('op', '?')
            axis = (st.get('axis') or '')[:80]
            cfg_rows.append(['Step{}.Op'.format(i), op])
            if axis: cfg_rows.append(['Step{}.Factor/Axis'.format(i), axis + '（@Profile 值域不冻结）'])
            tiers = st.get('tiers') or ['preferred', 'tolerated', 'excluded ×0.01']
            cfg_rows.append(['Step{}.TierSet'.format(i), ' / '.join(tiers)])
        cfg_rows.append(['数值状态', '全部阈值与档位成员＝@参数引用（Profile 层定值，不冻结）'])
        cfg_tbl = '| 字段 | 值（实例={}） |\n|---|---|\n'.format(pid) + '\n'.join('| {} | {} |'.format(a, b) for a, b in cfg_rows)
        parts.append('## 配置表（真实结构·字段-值）\n\n{}\n'.format(cfg_tbl))
    elif kind == 'file':
        _, rel, cfg_sec, code_sec, inst_name = ex
        cfg, code = extract_file(rel, cfg_sec, code_sec)
        parts.append('## 完全展开实例伪脚本（{}）\n\n```plain text\n{}\n```\n'.format(inst_name, code))
        parts.append('## 配置表（真实结构·字段-值——实例文件原表）\n\n{}\n'.format(cfg))
    else:
        sy = SYNTH[ex[1]]
        parts.append('## 完全展开实例伪脚本（{}）\n\n```plain text\n{}\n```\n'.format(sy['inst'], '\n'.join(sy['code'])))
        cfg_tbl = '| 字段 | 值 |\n|---|---|\n' + '\n'.join('| {} | {} |'.format(a, b) for a, b in sy['cfg'])
        parts.append('## 配置表（真实结构·字段-值）\n\n{}\n'.format(cfg_tbl))
    parts.append('## 模板级参数轴（抽象层）\n\n| 参数轴 | 取值 / 说明 |\n|---|---|\n{}\n'.format(axes_tbl))
    parts.append('*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*')
    md = '\n'.join(parts)
    io.open('{}/{}.md'.format(OUT, fid.lower()), 'w', encoding='utf-8', newline='\n').write(md)
    results[fid] = len(md.splitlines())
print(json.dumps(results, ensure_ascii=False))
