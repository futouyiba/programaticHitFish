# Fish-Centric Conditional Funnel（FCF，以鱼为中心的条件漏斗）V1

本仓库是 RC4 机制的可执行设计基线。权威契约记录在
[`docs/fcf_v1_engineering_spec.md`](docs/fcf_v1_engineering_spec.md)，
并由 [`tests/test_fcf_v1.py`](tests/test_fcf_v1.py) 中的测试驱动验证。

中文入口总览见 [`docs/fcf_v1_overview_cn.md`](docs/fcf_v1_overview_cn.md)，其中包含
概念、整体机制、配置示例、中文术语和主链路图示。

全仓库机制英文术语的中文对照见 [`docs/glossary_cn.md`](docs/glossary_cn.md)。

Simplified V0 文档治理见 [`docs/fcf_v0_document_governance.md`](docs/fcf_v0_document_governance.md)，
其中规定 V0 实验、V1 契约和发布镜像的边界。

其它审查面：

- [`docs/editor_contract.md`](docs/editor_contract.md) — 事务性编辑器与属性配置工作流；
- [`docs/flagship_traces.md`](docs/flagship_traces.md) — 产卵护巢鲈鱼（Spawn Bass）、鳟鱼漂流（Trout Drift）、鲤鱼静态饵（Carp Static Bait）三条旗舰追踪样例；
- [`docs/independent_review_checklist.md`](docs/independent_review_checklist.md) — 窄域收口审查矩阵；
- [`docs/verification_report.md`](docs/verification_report.md) — 已执行的证据与剩余闸门。

原型有意只建模 V1 语义边界，而非完整游戏运行时：有限来源本地种群单位、机会账本
进入、即时候选、确定性遭遇转化、承诺判定、接触仲裁、挂钩兼容与幂等终结结算。

运行验证套件：

```text
python3 -m pytest -q
```

## Simplified V0 校准实验

隔离的纯数值校准实验可复现：

```text
python3 -m fcf_v1.calibration_experiment --output experiments/fcf_simplified_v0
```

它生成解析解与固定种子蒙特卡洛 CSV 结果及六张所需图表，不改变 FCF V1 运行时模型。

## 生产交接冒烟检查

生产运行时应暴露一个满足 `JournalAdapter` 支撑的引擎契约的工厂。在运行完整固定样例
套件之前，先运行确定性交接检查：

```python
from fcf_v1 import FCFEngine, SQLiteJournal, run_core_conformance

def production_factory():
    return FCFEngine(
        production_sources(),
        journal=SQLiteJournal("/var/lib/fcf/events.sqlite"),
        detailed_capacity=production_capacity(),
    )

report = run_core_conformance(production_factory)
if not report.passed:
    raise SystemExit(report.to_json())
```

该冒烟检查刻意收窄（有限进入、无重掷重放、幂等终结结算与守恒）。CI 还必须运行完整的
RC4 固定样例/并发/性质套件，并将 JSON 报告持久化为审查证据。

## Contract Authority 与仓库关系

本仓是 **Reference Implementation / Evidence**，不是产品 Contract Authority。现行产品契约、语义裁定、范围和编辑器规范以 [`futouyiba/HitFish-Up`](https://github.com/futouyiba/HitFish-Up) 的 `main` 分支 Git Markdown 为准，当前编辑器入口为 [`docs/fish-habit-editor-v1/`](https://github.com/futouyiba/HitFish-Up/tree/main/docs/fish-habit-editor-v1)。

本仓承载：

- FCF / Species Funnel 参考运行时；
- Response / Condition 原型与实验；
- harness、测试和验证证据；
- 与实现相关的 tracker。

实现或实验不得把自身代码、测试或 working 文档反向升级为产品 Contract。每个可审计验证批次应记录：

```yaml
contract_repository: futouyiba/HitFish-Up
contract_ref: <pinned HitFish-Up commit>
implementation_repository: futouyiba/programaticHitFish
implementation_ref: <pinned implementation commit>
authority_rule: HitFish-Up Contract is authoritative; this repository is reference implementation and evidence.
```

两个仓库通过 commit pin、release/tag 和 GitHub issue/PR 互引关联，不使用 submodule。
