from pathlib import Path
import json, re

ROOT=Path(__file__).resolve().parent
tables=json.loads((ROOT/'tables.json').read_text())
scripts={x['binding_id']:x['source'] for x in json.loads((ROOT/'scripts.json').read_text())}
bindings={x['binding_id']:x for x in tables['Binding']}
allowed_refs={r['parameter_id'] for r in tables['Parameter']} | {r['profile_id'] for r in tables['CurvePoint']}
checks=[]
def ok(name,actual,expected=True):
 checks.append({'check':name,'actual':actual,'expected':expected,'status':'PASS' if actual==expected else 'FAIL'})
for bid,b in bindings.items():
 src=scripts.get(bid,'')
 executable='\n'.join(line.split('//',1)[0] for line in src.splitlines())
 ok(bid+' script exists',bool(src))
 ok(bid+' binding/template named',bid in src and b['template_id'] in src)
 refs=set(re.findall(r'@([A-Za-z0-9_]+)', executable))
 ok(bid+' has no unknown @references',refs <= allowed_refs,True)
 slots=[x for x in tables['Slot'] if x['binding_id']==bid]
 for s in slots:
  token=(('@'+s['ref_id']) if s['enabled'] else ('关闭槽位' if s['slot']!='ColdFront' else '关闭'))
  # A SWITCH uses the visible 开启/关闭 words; enabled Profile/Parameter uses @ref.
  if s['ref_kind']=='SWITCH' and s['enabled']: token='开启'
  ok(f'{bid} Slot {s["slot"]} represented',token in src)
 # Rule/Group/Quality records must leave an explicit predicate/rule trace in the script.
 for key in ('ResponseBand','GroupShare','QualityModifier'):
  for r in tables[key]:
   if r.get('binding_id')==bid:
    if key=='ResponseBand':token='优先级 '+str(r['priority'])
    elif key=='GroupShare':token=r['group']+' ='
    else:token='并列修正 '+r['rule_id']+'/'+r['bucket']
    ok(f'{bid} {key} row represented',token in src)
for bid in ['C03_R','C06_R','C08_R','C09_R','C12_N','C12_M']:
 ok(bid+' has a typed return', '返回 ' in scripts[bid])
ok('all bindings have scripts',len(scripts),len(bindings))
ok('all checks pass',all(x['status']=='PASS' for x in checks))
out={'artifact':'Representation Equivalence R3','binding_count':len(bindings),'check_count':len(checks),'checks':checks}
(ROOT/'representation-equivalence-r3.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps({'binding_count':len(bindings),'check_count':len(checks),'failed':[x for x in checks if x['status']=='FAIL']},ensure_ascii=False))
assert out['checks'][-1]['status']=='PASS' and all(x['status']=='PASS' for x in checks)
