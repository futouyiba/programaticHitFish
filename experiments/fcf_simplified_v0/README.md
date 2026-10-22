# FCF Simplified V0 校准实验

文档状态：**RETAINED / GENERATED-EVIDENCE ENTRY（保留 / 生成证据入口）**  
权威级别：**仅 V0 实验；不是 FCF V1 契约**  
范围：本目录下固定种子的数值校准输出。  
复现：按"复现（Reproduce）"节的命令与记录种子执行。  
V1 晋升规则：输出保持证据身份，直至显式的 V1 归属方审查。

本目录是"校准原型实验规范 R0（Calibration Prototype Experiment Spec R0）"定义的
可执行数值实验。它不新增机制、不拟合真实鱼类参数、不改变 FCF 设计。

## 复现（Reproduce）

```text
python3 -m fcf_v1.calibration_experiment --output experiments/fcf_simplified_v0 --samples 1000000 --seed 20260831
```

本次运行使用固定种子，把所需 CSV 文件写入 `results/`、六张 PNG 图写入 `figures/`。
每个参数点至少使用 1,000,000 个解析等价的伯努利或类别样本。节律验证另外聚合合成的
60 分钟会话。

## 断言

全部所需确定性断言通过：技术/模式分裂不变性、NONE 相加不变性、概率归一化、等级
单调性、暴露单调性、仅挂钩上游隔离与仅转化参与隔离。

## 观察结果

- 本次运行中解析解与蒙特卡洛饱和/等级映射点最大相差 0.001417。
- 请求扫描中最大的固定类别替换变化为 125.00%（vary_A、Compressed、K/参考=0.25、
  被变等级=NONE）。
- 在请求的名册网格中，P(any) >= 0.9 首次出现在 N=20（pressure=0.5）。
- 在请求的 12 组比例对中，有 8 组"单次更弱、频率更高"的技术按每分钟计算更强。
- 在不限次数的转化尝试下，P(至少一次转化) >= 0.9 首次出现在 p=0.7、N=2。
- 在 Exposure=K=ReferenceExposure 时，所有映射共享 NORMAL=1，因此 NORMAL 结果相同；
  其 LOW/HIGH/VERY_HIGH 分离如 `results/summary.csv` 与
  `figures/grade_map_sensitivity.png` 所记录。

## 重开信号（REOPEN SIGNALS）

上述观察只对应五个请求的重开信号类别：替换耦合、名册饱和、节律敏感、重复转化尝试
与等级映射敏感。它们是设计线的测量，不是玩法结论。

## 输出结构说明

- `summary.csv`：K 饱和、等级映射敏感性与紧凑重开信号行。
- `invariance.csv`：精确确定性不变性检查与差值。
- `substitution.csv`：两个替换扫描方向、解析与模拟概率。
- `roster_saturation.csv`：N x pressure 曲面与各类别绝对概率。
- `cadence.csv`：机会节律曲面与归一化的成对技术比较。
- `conversion_reroll.csv`：G1/G2/G3 结果；G3 循环四个合成语义事件族标签，因此有效
  尝试上限为四。
- `gear_isolation.csv`：挂钩兼容与转化扫描的共享抽取顺序漏斗计数器。
