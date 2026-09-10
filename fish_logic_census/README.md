# FCF Fish Logic Census

数什么：现实机制真正需要多少种 LogicTemplate（程序函数体族）——不是 Mode 数、不是 Story 数、不是 Program 实例数、更不是 Representation Schema 数。

- 方法合同：https://app.notion.com/p/3d7a4137d23681aa9640f14a997a9f23（Method R0）
- 执行合同：https://app.notion.com/p/3d7a4137d23681938302d08dcb0ba060（Orchestrator Prompt R2，Stage 隔离）
- 输入：FR campaign 冻结故事（FR3-passed，Story DB 只读）
- 关键纪律：盲重建（骨架先冻结再开 registry）、四态判同、族完整性、负知识保存
- 权威文件：template_registry.yaml / resolver_registry.yaml / discovery_curve.csv / batches/*/
- 停止：每批止于 INDEPENDENT_REVIEW_REQUIRED；饱和只能报 SATURATION_SIGNAL，由 Review/Gate 裁决

角色：FCF-CENSUS-WORKER（持久 tab，Registry Segment B）。
