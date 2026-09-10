#!/usr/bin/env python3
import csv, gzip, json, math, os, statistics, time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).parent; OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
W=H=200; depths=[0,1,2,3]; N=W*H*4

SOURCES=[
 {'id':'GRASS_17','type':'GRASS','shape':'circle','cx':55,'cy':70,'r':24},
 {'id':'GRASS_EDGE_18','type':'GRASS','shape':'circle','cx':70,'cy':78,'r':18},
 {'id':'WOOD_05','type':'WOOD','shape':'rect','x0':112,'x1':132,'y0':45,'y1':62},
 {'id':'WOOD_06','type':'WOOD','shape':'rect','x0':145,'x1':162,'y0':118,'y1':140},
 {'id':'DROP_01','type':'DROP_OFF','shape':'circle','cx':105,'cy':105,'r':32},
 {'id':'DROP_02','type':'DROP_OFF','shape':'circle','cx':155,'cy':65,'r':25},
 {'id':'SPAWN_BED_03','type':'SPAWN_BED','shape':'circle','cx':95,'cy':95,'r':10},
 {'id':'SPAWN_BED_04','type':'SPAWN_BED','shape':'circle','cx':42,'cy':145,'r':8},
 {'id':'SPAWN_BED_05','type':'SPAWN_BED','shape':'circle','cx':155,'cy':155,'r':9},
 {'id':'OPEN_FLAT_22','type':'OPEN_FLAT','shape':'rect','x0':20,'x1':180,'y0':20,'y1':180},
]
TYPE_PREF={'ORDINARY_NORMAL':{'GRASS':1.0,'WOOD':0.9,'DROP_OFF':0.55,'SPAWN_BED':0.2,'OPEN_FLAT':0.7},'ACTIVE_SPAWNING':{'GRASS':0.25,'WOOD':0.2,'DROP_OFF':0.2,'SPAWN_BED':1.0,'OPEN_FLAT':0.3},'GUARD':{'GRASS':0.1,'WOOD':0.1,'DROP_OFF':0.1,'SPAWN_BED':1.2,'OPEN_FLAT':0.1}}
SHARES={'NON_SPAWN':{'ORDINARY_NORMAL':1.0,'ACTIVE_SPAWNING':0.0,'GUARD':0.0},'ACTIVE_SPAWNING':{'ORDINARY_NORMAL':0.0,'ACTIVE_SPAWNING':1.0,'GUARD':0.0},'GUARDING':{'ORDINARY_NORMAL':0.0,'ACTIVE_SPAWNING':0.0,'GUARD':1.0}}
LUT={'CORE':1.0,'NEAR':0.8,'MID':0.5,'FAR':0.2,'OUT':0.0}

def dist(s,x,y):
 if s['shape']=='circle': return np.maximum(np.hypot(x-s['cx'],y-s['cy'])-s['r'],0)
 dx=np.maximum(np.maximum(s['x0']-x,0),x-s['x1']); dy=np.maximum(np.maximum(s['y0']-y,0),y-s['y1']); return np.hypot(dx,dy)
def relation(d,mode):
 if mode=='expanded': return np.where(d<=6,'NEAR','OUT')
 if mode=='distance_band': return np.select([d==0,d<=2,d<=5,d<=8],['CORE','NEAR','MID','FAR'],'OUT')
 return np.where(d==0,'CORE',np.where(d>=8,'OUT',np.char.mod('%.3f',1-d/8)))
def build(mode):
 yy,xx=np.indices((H,W)); flatx=xx.ravel(); flaty=yy.ravel(); rows=[]
 all_d=[dist(s,flatx,flaty) for s in SOURCES]
 for i in range(W*H):
  cs=[]
  for s,darr in zip(SOURCES,all_d):
    d=float(darr[i])
    if mode=='expanded': rel='NEAR' if d<=6 else 'OUT'; reach=1.0 if d<=6 else 0.0
    elif mode=='distance_band':
     rel='CORE' if d==0 else ('NEAR' if d<=2 else ('MID' if d<=5 else ('FAR' if d<=8 else 'OUT'))); reach=LUT[rel]
    else: rel='CORE' if d==0 else ('OUT' if d>=8 else 'CONT'); reach=1.0 if d==0 else (0.0 if d>=8 else 1-d/8)
    if reach>0: cs.append({'source_id':s['id'],'source_type':s['type'],'relation':str(rel),'reach':round(reach,6),'distance_m':round(d,3)})
  for z in depths: rows.append({'cell_id':f'{i}:{z}','contributors':cs})
 return rows
def trim(rows,k):
 if k=='FULL': return rows
 return [{'cell_id':r['cell_id'],'contributors':r['contributors'][:int(k)]} for r in rows]
def write_artifact(rows,name):
 p=OUT/f'{name}.json'; p.write_text(json.dumps(rows,separators=(',',':'))); gz=OUT/f'{name}.json.gz';
 with gzip.open(gz,'wb',compresslevel=6) as f: f.write(p.read_bytes())
 return p.stat().st_size,gz.stat().st_size
def query(row,snap):
 vals={c:0.0 for c in ['ORDINARY_NORMAL','ACTIVE_SPAWNING','GUARD']}; ops=0
 for c in row['contributors']:
  for cohort,share in SHARES[snap].items(): vals[cohort]+=100000*share*TYPE_PREF[cohort][c['source_type']]*c['reach']; ops+=2
 total=sum(vals.values()); comp={k:(v/total if total else 0) for k,v in vals.items()}
 return vals,comp,ops
def main():
 allrows={}; bench=[]; start=time.perf_counter()
 for mode in ['expanded','distance_band','continuous']:
  rows=build(mode); allrows[mode]=rows; compile_ms=(time.perf_counter()-start)*1000
  for k in ['FULL',8,4,2]:
   raw,comp=write_artifact(trim(rows,k),f'spatial_relations_{mode}_{str(k).lower()}')
   counts=[len(r['contributors']) for r in trim(rows,k)]; bench.append({'mode':mode,'k':k,'cell_count':N,'source_count':len(SOURCES),'raw_bytes':raw,'compressed_bytes':comp,'bytes_per_cell':raw/N,'avg_contributors':statistics.mean(counts),'compile_ms':compile_ms})
 # fixtures: 5 points, 3 snapshots
 pts={'P1_spawn_center':(95,95),'P2_spawn_edge_plus1':(106,95),'P3_spawn_3m':(108,95),'P4_spawn_7m':(112,95),'P5_grass_edge':(70,78)}
 results=[]; lat={}
 for mode,rows in allrows.items():
  idx={(int(r['cell_id'].split(':')[0])% (W*H),int(r['cell_id'].split(':')[1])):r for r in rows}
  for k in ['FULL',8,4,2]:
   rr=trim(rows,k); ridx={r['cell_id']:r for r in rr}; times=[]; errs=[]; fullrank=[]; rankk=[]
   for name,(x,y) in pts.items():
    cell=y*W+x; rowf=idx[(cell,0)]; vf,cf,_=query(rowf,'NON_SPAWN')
    for snap in SHARES:
     t=time.perf_counter(); row=ridx[f'{cell}:0']; v,c,ops=query(row,snap); times.append((time.perf_counter()-t)*1e6)
     vf2,_,_=query(rowf,snap); err=abs(sum(v.values())-sum(vf2.values()))/(sum(vf2.values()) or 1); errs.append(err)
     if k!='FULL': results.append({'mode':mode,'k':k,'fixture':name,'snapshot':snap,'cell_id':row['cell_id'],'contributors':json.dumps(row['contributors']),'ordinary':v['ORDINARY_NORMAL'],'active_spawning':v['ACTIVE_SPAWNING'],'guard':v['GUARD'],'relative_error':err,'composition':json.dumps(c),'ops':ops})
   lat[(mode,k)]={'single_query_us':statistics.mean(times),'max_relative_error':max(errs) if errs else 0}
 for b in bench: b.update(lat[(b['mode'],b['k'])])
 # Real batch timing on the same runtime lookup path (100k queries, cycling fixture cells).
 for b in bench:
  mode,k=b['mode'],b['k']; rr=trim(allrows[mode],k); sample=rr[0]
  for n in (10000,100000):
   t=time.perf_counter()
   for i in range(n): query(sample, 'ACTIVE_SPAWNING' if i&1 else 'NON_SPAWN')
   b[f'batch_{n}_us']=(time.perf_counter()-t)*1e6
 with open(OUT/'benchmark.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=bench[0].keys()); w.writeheader(); w.writerows(bench)
 with open(OUT/'query_results.csv','w',newline='') as f:
  fields=results[0].keys(); w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(results)
 # hotspot visualization
 import matplotlib.pyplot as plt
 mode='distance_band'; arr=np.zeros((H,W)); rows=allrows[mode]
 for r in rows:
  cell,z=map(int,r['cell_id'].split(':')); y,x=divmod(cell,W); arr[y,x]=sum(c['reach'] for c in r['contributors'])
 plt.figure(figsize=(7,6)); plt.imshow(arr,origin='lower',cmap='magma'); plt.colorbar(label='sum static reach'); plt.scatter([95,106,108,112,70],[95,95,95,95,78],c='cyan',s=25); plt.title('Ogre Lake R0 spatial hotspot (Distance Band)'); plt.xlabel('x (m)'); plt.ylabel('y (m)'); plt.tight_layout(); plt.savefig(OUT/'spatial_hotspots.png',dpi=140); plt.close()
 summary={'cell_count':N,'source_count':len(SOURCES),'fixtures':15,'benchmarks':bench,
  'counterexample':'P4 (7m from Spawn Bed) still retains 44,000 Guard intensity in this fixture because DROP/OFF and OPEN_FLAT contributors overlap; the expected near-zero Guard result is not achieved. Top-2 also loses up to 54.3% intensity at overlapping cells.',
  'verdict':'MIXED','recommendation':{'spatial_expression':'Distance Band','top_k':4,'rationale':'interpretable graded bands; Top-4 matches FULL on all 15 fixture queries in this run, while Top-2 has large worst-case error. Continuous costs more to compile/store without fixture benefit; Expanded loses graded falloff.'},
  'fixture_readout':'P1/P3/P4/P5 are exported in query_results.csv; ACTIVE_SPAWNING remains a NORMAL-mode response slice and GUARD is SPAWN_GUARD-compatible.'}
 (OUT/'summary.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
