# BATCH｜CENSUS-B2-REV-002（修复复检 PATCH_APPROVE → B2 闭轮）

- 四点全过：三方互记 6 边闭环（新增 2 条留痕+reason 双向镜像）；24+1 独立重加总（5+9+10=24，AMBIGUOUS 1 恰好不计）；engine_raw_diffs 32/32 逐行 mirror（5 行 [] 精确）；self_qa 逐项对账+守恒链 20→20→20→20 闭合。
- Git 锚点链完整（6928aed→7940f54→7a95815→c3749d2）。
- 1 minor 挂账：修复轮统一在 registry mutation_provenance 留 fix_round 节点（B2-FIX 未设，B0 有先例）。
- **B2 闭轮。Registry v4 = 9 族/58 程序/94 判同。census worker 第一会话（B0/B1/B2+三修复轮）收官。**
