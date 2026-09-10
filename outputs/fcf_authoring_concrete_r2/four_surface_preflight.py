from pathlib import Path
import re, json
p=Path(__file__).with_name('four-surface-completion-r1.md'); s=p.read_text()
cases=[f'C{i:02d}' for i in range(1,16)]
surfaces=['Group','Bake','Response','Quality']
rows=[]
for c in cases:
 for surf in surfaces:
  marker=f'| {c} · {surf} |'
  rows.append((c,surf,marker in s))
missing=[f'{c}×{u}' for c,u,ok in rows if not ok]
# 每个逐案记录至少应有 7 个表格单元（Case、输入、绑定、执行、结果、边界等）
malformed=[]
for c,u,ok in rows:
    if ok:
        line=next((ln for ln in s.splitlines() if ln.startswith(f'| {c} · {u} |')), '')
        if len(line.split('|')) < 7: malformed.append(f'{c}×{u}')
checks={
 'case_count':len(cases),
 'surface_count':len(surfaces),
 'cell_count':len(rows),
 'present_cells':sum(ok for _,_,ok in rows),
 'missing_cells':missing,
 'malformed_cells':malformed,
 'has_minimum_binding_rule':'case_surface' in s and 'typed_result' in s and 'boundary_status' in s,
 'has_script_section':'关键新增中文伪脚本' in s,
}
checks['pass']=not missing and not malformed and checks['has_minimum_binding_rule'] and checks['has_script_section']
Path(__file__).with_name('four_surface_preflight.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False))
raise SystemExit(0 if checks['pass'] else 1)
