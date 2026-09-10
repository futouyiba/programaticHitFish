/* Deterministic 2 m raster proxy for the Ogre Lake authoring experiment.
 * Counts are connected components of identical cumulative state vectors.
 */
const N = 100, CELL_M = 2;
const idx = (x, y) => y * N + x;
const insideEllipse = (x,y,cx,cy,rx,ry) => ((x-cx)/rx)**2+((y-cy)/ry)**2 <= 1;
const distSeg = (x,y,x1,y1,x2,y2) => {
  const dx=x2-x1,dy=y2-y1,t=Math.max(0,Math.min(1,((x-x1)*dx+(y-y1)*dy)/(dx*dx+dy*dy)));
  return Math.hypot(x-(x1+t*dx),y-(y1+t*dy));
};
function wet(x,y){
  const outer=insideEllipse(x,y,103,96,94,82)||insideEllipse(x,y,132,157,58,38);
  const island=insideEllipse(x,y,98,91,27,20);
  return outer&&!island;
}
function depthM(x,y){
  const r=Math.sqrt(((x-105)/98)**2+((y-100)/87)**2);
  let d=1+19*Math.max(0,1-r);
  d+=8*Math.exp(-(((x-139)/30)**2+((y-126)/25)**2));
  d-=5*Math.exp(-(((x-47)/30)**2+((y-55)/22)**2));
  return Math.max(.5,Math.min(27,d));
}
function depthBand(x,y){const d=depthM(x,y);return d<2?0:d<5?1:d<10?2:d<16?3:4}
function vegetation(x,y){
  const west=insideEllipse(x,y,43,74,34,42), south=insideEllipse(x,y,89,158,48,24), pads=insideEllipse(x,y,157,55,34,23);
  if(pads)return 3;
  const inGrass=west||south;
  const core=insideEllipse(x,y,43,74,27,34)||insideEllipse(x,y,89,158,39,17);
  if(core)return 1;
  if(inGrass)return 2;
  return 0;
}
function structure(x,y){
  if(insideEllipse(x,y,124,48,22,13))return 1;
  if(distSeg(x,y,151,130,184,158)<5||distSeg(x,y,163,128,151,166)<4)return 2;
  if((Math.abs(x-181)<5&&y>73&&y<119)||(Math.abs(y-150)<4&&x>45&&x<77))return 3;
  return 0;
}
function substrate(x,y){
  if(y>122+.28*(x-80))return 0;
  if(y<62+.18*x)return 2;
  return 1;
}
function shadeMorning(x,y){return ((x+0.55*y<112)||(x<78&&y>105))?1:0}
function shadeAfternoon(x,y){return ((x-0.45*y>82)||(x>112&&y<70))?1:0}
function shadeDusk(x,y){return y>142-0.18*x?1:0}
function temperature(x,y){const t=18+3*(x/200)-.18*depthM(x,y)+(y>135?1:0);return t<16?0:t<19?1:2}
function dissolvedOxygen(x,y){const v=8-.22*depthM(x,y)-(insideEllipse(x,y,139,126,38,31)?1.2:0);return v<4?0:v<6?1:2}
function flow(x,y){return x>166&&y>82&&y<128?1:0}
function functional(x,y){let v=0;if(insideEllipse(x,y,65,61,33,22))v|=1;if(insideEllipse(x,y,57,136,38,25))v|=2;if(insideEllipse(x,y,149,119,31,24))v|=4;return v}
const layers=[
  ['Geometry',()=>0],['Depth',depthBand],['Vegetation',vegetation],['Structure',structure],['Substrate',substrate],
  ['Shade · Morning',shadeMorning],['Shade · Afternoon',shadeAfternoon],['Shade · Dusk',shadeDusk],
  ['Temperature · afternoon snapshot',temperature],['DO · dawn snapshot',dissolvedOxygen],['Flow',flow],['Functional tags',functional]
];
function componentAnalysis(values, activeLayer){
  const seen=new Uint8Array(N*N);let components=0;const combos=new Set();const componentId=new Int32Array(N*N);componentId.fill(-1);
  for(let y=0;y<N;y++)for(let x=0;x<N;x++){
    const i=idx(x,y);if(!values[i]||seen[i])continue;components++;const key=values[i].slice(0,activeLayer+1).join('|');combos.add(key);
    const q=[i];seen[i]=1;componentId[i]=components-1;
    for(let h=0;h<q.length;h++){const a=q[h],ax=a%N,ay=(a/N)|0;for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const nx=ax+dx,ny=ay+dy;if(nx<0||ny<0||nx>=N||ny>=N)continue;const ni=idx(nx,ny);if(!values[ni]||seen[ni])continue;if(values[ni].slice(0,activeLayer+1).join('|')!==key)continue;seen[ni]=1;componentId[ni]=components-1;q.push(ni)}}
  }
  return {components,combinations:combos.size,componentId};
}
function build(){
  const values=new Array(N*N).fill(null), wetCells=[];
  for(let gy=0;gy<N;gy++)for(let gx=0;gx<N;gx++){const x=(gx+.5)*CELL_M,y=(gy+.5)*CELL_M;if(!wet(x,y))continue;const a=layers.map(l=>l[1](x,y));values[idx(gx,gy)]=a;wetCells.push(idx(gx,gy));}
  const stages=layers.map((l,i)=>({name:l[0],...componentAnalysis(values,i)}));
  stages.forEach((s,i)=>{s.delta=i?s.components-stages[i-1].components:s.components;s.split_old_patches=0;s.nonzero_cells=0;if(i===0)return;const prev=stages[i-1].componentId,byOld=new Map();for(const c of wetCells){const a=values[c][i];if(a!==0)s.nonzero_cells++;if(!byOld.has(prev[c]))byOld.set(prev[c],new Set());byOld.get(prev[c]).add(a)}s.split_old_patches=[...byOld.values()].filter(v=>v.size>1).length});
  return {values,wetCells,stages};
}
function volumeCount(model){
  const Z=14,total=N*N*Z,exists=new Uint8Array(total),keys=new Array(total),at=(x,y,z)=>(z*N+y)*N+x;
  for(const c of model.wetCells){const x=c%N,y=(c/N)|0,wx=(x+.5)*2,wy=(y+.5)*2,d=depthM(wx,wy),nz=Math.max(1,Math.ceil(d/2));for(let z=0;z<nz;z++){
    const dep=(z+.5)*2,rel=dep/d,zone=dep<=2?0:(d-dep<=2?2:1);
    const shadeVec=[shadeMorning(wx,wy),shadeAfternoon(wx,wy),shadeDusk(wx,wy)];
    const light=shadeVec.reduce((a,b)=>a+b,0)+(dep>6?2:dep>3?1:0);
    const temp=18+3*(wx/200)-.22*dep+(wy>135?1:0),tb=temp<16?0:temp<19?1:2;
    const ov=8-.25*dep-(insideEllipse(wx,wy,139,126,38,31)?1.2:0),ob=ov<4?0:ov<6?1:2;
    const hv=model.values[c];const key=[hv[1],hv[2],hv[3],hv[4],zone,light,tb,ob,hv[10],hv[11]].join('|');
    const vi=at(x,y,z);exists[vi]=1;keys[vi]=key;
  }}
  const seen=new Uint8Array(total);let components=0,voxels=0;for(let z=0;z<Z;z++)for(let y=0;y<N;y++)for(let x=0;x<N;x++){const i=at(x,y,z);if(!exists[i])continue;voxels++;if(seen[i])continue;components++;const key=keys[i],q=[i];seen[i]=1;for(let h=0;h<q.length;h++){const a=q[h],az=(a/(N*N))|0,rem=a%(N*N),ay=(rem/N)|0,ax=rem%N;for(const [dx,dy,dz] of [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]){const nx=ax+dx,ny=ay+dy,nz=az+dz;if(nx<0||ny<0||nz<0||nx>=N||ny>=N||nz>=Z)continue;const ni=at(nx,ny,nz);if(exists[ni]&&!seen[ni]&&keys[ni]===key){seen[ni]=1;q.push(ni)}}}}
  return {components,voxels,voxel_size_m:[2,2,2]};
}
const model=build();
const output={grid:`${N}×${N}`,cell_m:CELL_M,wet_cells:model.wetCells.length,stages:model.stages.map(({componentId,...s})=>s),volume:volumeCount(model)};
if(typeof module!=='undefined')module.exports={...output,model,layers,depthM,wet,vegetation,structure,substrate,shadeMorning,shadeAfternoon,shadeDusk,temperature,dissolvedOxygen,flow,functional,insideEllipse,distSeg};
if(require.main===module)console.log(JSON.stringify(output,null,2));
