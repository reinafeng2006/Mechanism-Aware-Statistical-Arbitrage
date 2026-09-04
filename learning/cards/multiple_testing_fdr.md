# Multiple Testing and False Discovery Rate (FDR)

**一句话直觉：** 在海量候选关系里，总会出现假阳性；FDR 管的是入选结果中平均有多少可能是错的，不管经济含义。

## Why it appeared

数据驱动配对需要可复现的统计筛选治理，而不是从大量比较中挑看起来最好的结果。

## Core idea / equation

`FDR = E[V / max(R,1)]`，其中 `R` 是被拒绝的假设数、`V` 是错误拒绝数。PF-013 用因子调整相关与多重检验控制。

## Measures / does not measure

测量在特定检验假设下的统计错误发现控制。它不证明入选 pair 的经济关系、稳定性或交易价值。

## Nearby concepts

与 global matching 不同：FDR 管显著性筛选中的假阳性；matching 管组合中资产重叠与集中。

## Current project use/status

可支持 G2 的 outcome-independent 统计治理候选；假设条件与适用性须自行验证。

## Paper / Claim ancestry

PF-013; CL-PF-006. 教学说明，不构成证据。
