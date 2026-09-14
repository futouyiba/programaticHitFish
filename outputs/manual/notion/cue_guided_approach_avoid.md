> **环境梯度趋避响应**（`CUE_GUIDED_APPROACH_AVOID`）｜面：Response｜状态：CANDIDATE｜名义成员：1

## 特点

沿环境 cue 梯度趋近或避开（单例族）。

## 骨架（一行链序）

```plain text
读取 cue 梯度 → EVAL[梯度方向] → 趋近/避开 → 返回 Approach/Avoid
```

## 完全展开实例伪脚本（环境梯度趋避（单例族））

```plain text
读取 环境 cue 梯度事实（如溶氧梯度/温度梯度方向）

EVAL_GRADIENT：
    梯度方向与强度查询 @GradientProfile（三档=Profile 值域）
    顺梯度（趋向有利） → 返回 Response(Approach)（趋近响应）
    逆梯度（避开不利） → 返回 Response(Avoid)（避离响应）
    中性 → 低响应继续

返回 Approach/Avoid
```

## 配置表（真实结构·字段-值）

| 字段 | 值 |
|---|---|
| evaluand | 环境 cue 梯度（非饵非场） |
| @GradientProfile | 趋/避/中性三档=Profile 值域 |

## 模板级参数轴（抽象层）

| 参数轴 | 取值 / 说明 |
|---|---|
| cue | 环境梯度 |

*数据源：registry v10 + RB 冻结真形体/B 系列表达文件（确定性生成·v2 手册升级：完全展开+真实配置表）*