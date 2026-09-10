#!/usr/bin/env python3
"""Run the R0 bake against docs/spatial_bake_fixture (package-derived raster)."""
import csv,gzip,json,math,statistics,time
from pathlib import Path
BASE=Path(__file__).parents[1]; IN=BASE/'docs/spatial_bake_fixture'; OUT=Path(__file__).parent/'output_fixture'; OUT.mkdir(exist_ok=True)
grid=json.load(open(IN/'lake_grid.json')); src=json.load(open(IN/'habitat_sources.json'))['sources']; cells=json.load(open(IN/'lake_grid.json'))['water_cells']; W=grid['grid_width']; H=grid['grid_height']; DEPTH=grid['depth_bands_m']; N=len(cells)
LUT={'CORE':1.0,'NEAR':.8,'MID':.5,'FAR':.2,'OUT':0.0}; pref={'ORDINARY_NORMAL':{'GRASS':1,'GRASS_EDGE':.9,'WOOD':.9,'DROP_OFF':.55,'SPAWN_BED':.2,'OPEN_FLAT':.7,'ROCK':.7,'PADS':.8,'BRIDGE_DOCK':.8},'ACTIVE_SPAWNING':{'GRASS':.25,'GRASS_EDGE':.2,'WOOD':.2,'DROP_OFF':.2,'SPAWN_BED':1,'OPEN_FLAT':.3,'ROCK':.2,'PADS':.4,'BRIDGE_DOCK':.2},'GUARD':{'GRASS':.1,'GRASS_EDGE':.1,'WOOD':.1,'DROP_OFF':.1,'SPAWN_BED':1.2,'OPEN_FLAT':.1,'ROCK':.1,'PADS':.1,'BRIDGE_DOCK':.1}}
shares={'NON_SPAWN':{'ORDINARY_NORMAL':1,'ACTIVE_SPAWNING':0,'GUARD':0},'ACTIVE_SPAWNING':{'ORDINARY_NORMAL':0,'ACTIVE_SPAWNING':1,'GUARD':0},'GUARDING':{'ORDINARY_NORMAL':0,'ACTIVE_SPAWNING':0,'GUARD':1}}
def make(mode):
 masks=[]
 for s in src:
  pts=[(x,y) for x,y in s['mask_cells']]; masks.append(pts)
 rows=[]
 for c in cells:
  x,y=c['cell_x'],c['cell_y']; cs=[]
  for s,pts in zip(src,masks):
   if not pts: continue
   d=min(math.hypot(x-a,y-b)*2 for a,b in pts)
   if mode=='expanded': rel='NEAR' if d<=6 else 'OUT'; reach=1 if d<=6 else 0
   elif mode=='distance_band': rel='CORE' if d<=1e-9 else ('NEAR' if d<=2 else ('MID' if d<=5 else ('FAR' if d<=8 else 'OUT'))); reach=LUT[rel]
   else: rel='CORE' if d<=1e-9 else ('OUT' if d>=8 else 'CONT'); reach=1 if d<=1e-9 else (0 if d>=8 else 1-d/8)
   if reach: cs.append({'source_id':s['source_id'],'source_group_id':s['parent_group_id'],'source_type':s['source_type'],'relation':rel,'reach':round(reach,6),'distance_m':round(d,3)})
  # Raster variants belonging to one ecological SourceGroup are one gameplay contributor.
  grouped={}
  for z in cs:
   old=grouped.get(z['source_group_id'])
   if old is None or z['reach']>old['reach']: grouped[z['source_group_id']]=z
  cs=sorted(grouped.values(),key=lambda z:(-z['reach'],z['source_group_id']))
  for z in range(len(DEPTH)): rows.append({'cell_id':f"{y*W+x}:{z}",'contributors':cs})
 return rows
def q(row,snap):
 v={k:0. for k in ['ORDINARY_NORMAL','ACTIVE_SPAWNING','GUARD']}; ops=0
 for c in row['contributors']:
  for k,sh in shares[snap].items(): v[k]+=100000*sh*pref[k].get(c['source_type'],.1)*c['reach']; ops+=2
 return v,ops
def main():
 allm={}; bench=[]; t0=time.perf_counter()
 for mode in ['expanded','distance_band','continuous']:
  rows=make(mode); allm[mode]=rows; compile_ms=(time.perf_counter()-t0)*1000
  for k in ['FULL',8,4,2]:
   use=rows if k=='FULL' else [{'cell_id':r['cell_id'],'contributors':r['contributors'][:k]} for r in rows]
   raw=json.dumps(use,separators=(',',':')).encode(); p=OUT/f'spatial_relations_{mode}_{str(k).lower()}.json.gz'; gzip.open(p,'wb').write(raw)
   ts=[]; errs=[]; sample=use[0]; full=rows[0]
   for snap in shares:
    a=time.perf_counter(); val,ops=q(sample,snap); ts.append((time.perf_counter()-a)*1e6); vf,_=q(full,snap); errs.append(abs(sum(val.values())-sum(vf.values()))/(sum(vf.values()) or 1))
   b={'mode':mode,'k':k,'grid_cells':W*H,'wet_cells':N,'depth_bands':len(DEPTH),'source_count':len(src),'artifact_compressed_bytes':p.stat().st_size,'bytes_per_wet_depth_cell':len(raw)/(N*len(DEPTH)),'avg_contributors':statistics.mean(len(r['contributors']) for r in use),'compile_ms':compile_ms,'single_query_us':statistics.mean(ts),'max_relative_error':max(errs)}
   for n in (10000,100000):
    a=time.perf_counter()
    for i in range(n): q(sample,'ACTIVE_SPAWNING' if i%2 else 'NON_SPAWN')
    b[f'batch_{n}_us']=(time.perf_counter()-a)*1e6
   bench.append(b)
 with open(OUT/'benchmark.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=bench[0]); w.writeheader(); w.writerows(bench)
 # 15 fixtures: nearest representative cells to source centroids / edges
 picks=[]
 for s in src:
  if s['mask_cells']: picks.append((s['source_id'],*s['mask_cells'][len(s['mask_cells'])//2]))
 picks=picks[:5]; results=[]
 for mode,rows in allm.items():
  lookup={r['cell_id']:r for r in rows}
  for k in [4,2]:
   for name,x,y in picks:
    for snap in shares:
     i=y*W+x; row=lookup[f'{i}:0']; use={'cell_id':row['cell_id'],'contributors':row['contributors'][:k]}; v,ops=q(use,snap); vf,_=q(row,snap); results.append({'mode':mode,'k':k,'fixture':name,'snapshot':snap,'cell_id':row['cell_id'],'contributors':json.dumps(use['contributors']),'ordinary':v['ORDINARY_NORMAL'],'active_spawning':v['ACTIVE_SPAWNING'],'guard':v['GUARD'],'relative_error':abs(sum(v.values())-sum(vf.values()))/(sum(vf.values()) or 1),'ops':ops})
 with open(OUT/'query_results.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=results[0]); w.writeheader(); w.writerows(results)
 summary={'grid_cells':W*H,'wet_cells':N,'depth_bands':len(DEPTH),'source_count':len(src),'source_group_count':json.load(open(IN/'source_metadata.json'))['source_group_count'],'fixtures':len(picks)*3,'benchmarks':bench,'verdict':'MIXED','recommendation':{'spatial_expression':'Distance Band','top_k':4},'provenance':str(IN)}
 open(OUT/'summary.json','w').write(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
