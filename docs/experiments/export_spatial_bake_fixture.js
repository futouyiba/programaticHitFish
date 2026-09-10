const fs = require('fs');
const path = require('path');
const model = require('./ogre_lake_overlay_model.js');
const out = process.argv[2] || path.join(__dirname, '..', 'spatial_bake_fixture');
fs.mkdirSync(out, {recursive:true});
const N=100,S=2, cell=(x,y)=>y*N+x;
const bandName=['0_2','2_5','5_10','10_16','16_30'];
const vegName=['OPEN','GRASS','GRASS_EDGE','PADS'];
const structName=['NONE','ROCK','WOOD','BRIDGE_DOCK'];
const substrateName=['MUD','SAND','GRAVEL_HARD'];
const shadeName=v=>v?'SHADE':'LIGHT';
const tempName=['COLD','TEMPERATE','WARM'],doName=['LOW','MEDIUM','NORMAL'];
const functionalNames=v=>{const a=[];if(v&1)a.push('SPAWN');if(v&2)a.push('NURSERY');if(v&4)a.push('AMBUSH');return a};
const values=model.model.values;
const water=[],outside=[];
for(let y=0;y<N;y++)for(let x=0;x<N;x++){
  const v=values[cell(x,y)];
  if(!v){outside.push([x,y]);continue;}
  water.push({cell_x:x,cell_y:y,wet:true,world_center_m:{x:(x+.5)*S,y:(y+.5)*S},depth_m:Number(model.depthM((x+.5)*S,(y+.5)*S).toFixed(3)),depth_band:bandName[v[1]],});
}
const grid={schema_version:'spatial-bake-fixture.v1',width_m:200,height_m:200,cell_size_m:2,grid_width:N,grid_height:N,origin_world_m:{x:0,y:0},axis_x:'east/right',axis_y:'north/up',cell_center_formula:'world_x=(cell_x+0.5)*cell_size_m; world_y=(cell_y+0.5)*cell_size_m',depth_bands_m:[[0,2],[2,5],[5,10],[10,16],[16,30]],depth_function:{name:'ogre_lake_overlay_model.depthM',source:'experiments/ogre_lake_overlay_model.js',evaluation:'deterministic fixture function',note:'depth_m is also materialized per wet cell'},water_cell_count:water.length,outside_cell_count:outside.length,outside_cells:outside,water_cells:water};
fs.writeFileSync(path.join(out,'lake_grid.json'),JSON.stringify(grid,null,2)+'\n');
const labels=[];
for(const c of water){const v=values[cell(c.cell_x,c.cell_y)];labels.push({cell_x:c.cell_x,cell_y:c.cell_y,wet:true,depth_band:bandName[v[1]],vegetation:vegName[v[2]],structure:structName[v[3]],substrate:substrateName[v[4]],shade_morning:shadeName(v[5]),shade_afternoon:shadeName(v[6]),shade_dusk:shadeName(v[7]),temperature_band:tempName[v[8]],do_band:doName[v[9]],flow:v[10]?'LOCAL_FLOW':'STILL',functional_tags:functionalNames(v[11])});}
fs.writeFileSync(path.join(out,'cell_layer_labels.json'),JSON.stringify({schema_version:'spatial-bake-fixture.v1',coordinate_reference:'same as lake_grid.json',cells:labels},null,2)+'\n');
const E=(x,y,cx,cy,rx,ry)=>((x-cx)/rx)**2+((y-cy)/ry)**2<=1;
const seg=(x,y,x1,y1,x2,y2)=>{const dx=x2-x1,dy=y2-y1,t=Math.max(0,Math.min(1,((x-x1)*dx+(y-y1)*dy)/(dx*dx+dy*dy)));return Math.hypot(x-x1-t*dx,y-y1-t*dy)};
const hasDepthBoundary=(x,y)=>{const v=values[cell(x,y)],b=v[1];return [[1,0],[-1,0],[0,1],[0,-1]].some(([dx,dy])=>{const nx=x+dx,ny=y+dy;if(nx<0||ny<0||nx>=N||ny>=N)return false;const n=values[cell(nx,ny)];return n&&n[1]!==b&&n[1]>=2})};
const sourceDefs=[
 ['GRASS_WEST_01','GRASS','WEST_GRASS_BED',c=>c.v[2]===1&&c.x<70,['0_2','2_5'],['FEEDING','AMBUSH']],
 ['GRASS_SOUTH_01','GRASS','SOUTH_GRASS_BED',c=>c.v[2]===1&&c.x>=70,['0_2','2_5'],['FEEDING']],
 ['GRASS_EDGE_WEST_01','GRASS_EDGE','WEST_GRASS_BED',c=>c.v[2]===2&&c.x<70,['0_2','2_5'],['FEEDING','AMBUSH']],
 ['GRASS_EDGE_SOUTH_01','GRASS_EDGE','SOUTH_GRASS_BED',c=>c.v[2]===2&&c.x>=70,['0_2','2_5'],['FEEDING']],
 ['WOOD_LOG_WEST_01','WOOD','WOOD_DEBRIS',c=>c.v[3]===2&&c.x<80,['2_5','5_10'],['COVER']],
 ['WOOD_LOG_EAST_01','WOOD','WOOD_DEBRIS',c=>c.v[3]===2&&c.x>=80,['2_5','5_10'],['COVER']],
 ['DROP_OFF_RIDGE_01','DROP_OFF','DROP_OFF_RIDGE',c=>hasDepthBoundary(c.x,c.y),['2_5','5_10','10_16'],['TRANSITION']],
 ['SPAWN_BED_01','SPAWN_BED','WEST_SPAWN_BED',c=>(c.v[11]&1)!==0,['0_2','2_5'],['SPAWN']],
 ['OPEN_FLAT_NORTH_01','OPEN_FLAT','OPEN_WATER',c=>c.v[2]===0&&c.v[3]===0&&c.v[1]<=2,['0_2','2_5'],['TRAVEL']],
 ['ROCK_OUTCROP_NORTH_01','ROCK','NORTH_ROCK_OUTCROP',c=>c.v[3]===1,['5_10','10_16'],['COVER','AMBUSH']],
 ['PADS_NORTH_01','PADS','NORTH_PADS',c=>c.v[2]===3,['0_2','2_5'],['FEEDING','COVER']],
 ['BRIDGE_DOCK_WEST_01','BRIDGE_DOCK','BRIDGE_DOCK_SYSTEM',c=>c.v[3]===3&&c.x<80,['0_2','2_5'],['COVER','ACCESS']],
 ['BRIDGE_DOCK_EAST_01','BRIDGE_DOCK','BRIDGE_DOCK_SYSTEM',c=>c.v[3]===3&&c.x>=80,['0_2','2_5'],['COVER','ACCESS']]
];
const sources=[];const masksById={};
for(const [source_id,source_type,parent_group_id,test,preferred_depth_bands,functional_tags] of sourceDefs){const mask=[];for(const c of water){const x=c.cell_x,y=c.cell_y,v=values[cell(x,y)];if(test({x,y,v}))mask.push([x,y]);}masksById[source_id]=mask;sources.push({source_id,source_type,parent_group_id,mask_cells:mask,preferred_depth_bands,functional_tags,authoring_layer:source_type==='DROP_OFF'?'Depth':source_type==='BRIDGE_DOCK'||source_type==='WOOD'||source_type==='ROCK'?'Structure':source_type==='SPAWN_BED'||source_type==='OPEN_FLAT'?'Functional':'Vegetation',confidence:'fixture',source_geometry_note:'Raster mask generated from deterministic Ogre Lake fixture function; not a production polygon.'});}
const overlapCounts={};let overlapCells=0;for(const c of water){const ids=sources.filter(s=>masksById[s.source_id].some(([x,y])=>x===c.cell_x&&y===c.cell_y)).map(s=>s.source_id);if(ids.length>1){overlapCells++;overlapCounts[`${ids.length}_sources`]=(overlapCounts[`${ids.length}_sources`]||0)+1;}}
fs.writeFileSync(path.join(out,'habitat_sources.json'),JSON.stringify({schema_version:'spatial-bake-fixture.v1',source_identity_rule:'one gameplay identity per authored ecological object; raster splits never create new source_id',overlap_policy:'allowed_and_explicit',sources},null,2)+'\n');
const typeCounts={};for(const s of sources)typeCounts[s.source_type]=(typeCounts[s.source_type]||0)+1;
const meta={schema_version:'spatial-bake-fixture.v1',source_count:sources.length,source_group_count:new Set(sources.map(s=>s.parent_group_id)).size,grid_cell_count:N*N,wet_cell_count:water.length,outside_cell_count:outside.length,connected_patch_count_2d:model.stages.at(-1).components,unique_state_vector_count_2d:model.stages.at(-1).combinations,habitat_volume_count_3d:model.volume.components,source_type_counts:typeCounts,source_overlap_cell_count:overlapCells,source_overlap_cardinality_counts:overlapCounts,all_values_are_fixture:true,provenance:{generated_by:'experiments/export_spatial_bake_fixture.js',model:'experiments/ogre_lake_overlay_model.js',model_grid:'100x100 at 2m',source_data:'deterministic fixture functions; no RF4 or production telemetry',dynamic_fish_state:'omitted by design'}};
fs.writeFileSync(path.join(out,'source_metadata.json'),JSON.stringify(meta,null,2)+'\n');
console.log(JSON.stringify({out,source_count:sources.length,source_group_count:meta.source_group_count,wet_cells:water.length,patches_2d:meta.connected_patch_count_2d,volumes_3d:meta.habitat_volume_count_3d,overlap_cells:overlapCells},null,2));
