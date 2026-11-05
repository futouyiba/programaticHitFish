# Proposal C 策略翻转独立实验

本目录检验一个窄问题：**同一套 Proposal C 响应算法，在不同鱼况下，最佳策略是否会发生
合理、稳定、玩家能学到的翻转？**

它不复述设计，也不修改任何契约。所有输入都是 `fixtures.json` 里显式标注的示意夹具，
不是鱼种数据或生产参数。

## 权威与版本

- 模型来源：`futouyiba/HitFish-Up`，`main` @ `dcba9ee9`（2026-11-05）。
  - `docs/proposals/lure-response-proposal-c-evaluation-items.md`
  - `docs/proposals/lure-response-proposal-c-semantic-contract.md`
  - `docs/proposals/lure-response-proposal-c-response-algorithm-v1.md`
  - `docs/proposals/lure-response-proposal-c-fish-condition-mechanism-contracts.md`
  - `docs/proposals/lure-response-proposal-c-opportunity-l-production.md`
  - `prototypes/lure-response/proposal_c_end_to_end_probe.py`
  - `prototypes/lure-response/proposal_c_opportunity_support_probe.py`
- 上述文档的状态是 **Candidate / Working**，不是 Current Contract；本实验的结果同样没有
  规范地位。
- 本仓基座：`futouyiba/programaticHitFish`，`main` @ `80af4d2`。
  本仓现有的 Response 方案一（`docs/response_scheme_1.md`）属于 FCF Simplified V0，
  不是 Proposal C；本实验没有使用它作为权威，也没有改动它。

## 运行

```bash
cd experiments/proposal_c_strategy_flips
python3 run.py
```

只依赖 Python 标准库。输出：

- `results/results.json`：全部场景、扫描与断言数据；
- `results/scenarios.csv`：场景表；
- `figures/*.svg`：纯 SVG 图，不需要 matplotlib。

脚本内含断言，覆盖负结果（快搜被慢速支配、无 cue 时 Wariness 不改变 C、隐蔽翻转的覆盖边界等）。
断言失败即退出非零。

## 文件

| 文件 | 作用 |
|---|---|
| `model.py` | 按契约转写的响应公式与玩具机会模型；标注了每个常量的来源 |
| `fixtures.json` | 四条策略轴的策略、鱼况与示意参数 |
| `stealth_samples.json` | 从 `tackle.xlsx` 的 Lines / Leaders 抽取的样例，含新增的 `clarity` 测试参数 |
| `stealth.py` | 由直径、颜色、透明度与材料清晰度计算可见度的测试算法 |
| `run.py` | 场景、单变量扫描、边界搜索、饱和统计、SVG 输出 |
| `report.md` | 完整报告：结果、边界、反例、归因与建议 |
| `policy_brief.md` | 一页面向策划会的结论 |
| `results/`、`figures/` | 固定输出 |

## 边界

- **Response 层**是按当前公式的忠实转写；`C` 的数值可以复核。
- **Opportunity 层**只是 `r × τ × coverage` 的玩具近似，用来做敏感性分析，
  不能称为游戏真实效率。报告里凡是综合收益都标为 “toy yield”。
- 鱼种、Engagement Mode、体型档没有仓内生产数据。实验用归一化速度 `q`、尺寸调整
  `size_adjustment` 和鱼况数值来覆盖这些维度；按名称的鱼种结论一律标为 `Blocked`。
- 隐蔽轴的输入来自 `tackle.xlsx` 的公开配置字段（直径、颜色、透明度）；`clarity` 与可见度权重
  是新增的测试假设，不是配置表已有字段，也不代表生产参数。
