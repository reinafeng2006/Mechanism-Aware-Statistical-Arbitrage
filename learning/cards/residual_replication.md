# Residual / Factor-Adjusted Dependence

**一句话直觉：** 先解释“大家一起动”的部分，再看剩下的部分，得到的是条件性偏离，不是更真实的天然关系。

## Why it appeared

G1 要区分原始共动和因子调整后关系，避免把共同市场暴露误作专属 pair link。

## Core idea / equation

可写作 `r_i = B_i f + e_i`，或用其他股票的稀疏复制组合预测对象；`e_i` 或“自身减复制组合”是残差。PF-008 用 elastic net 建立稀疏复制，PF-013 用 PCA 因子后做相关筛选。

## Measures / does not measure

测量在所选控制集合和估计规则下仍存在的依赖或偏离。它不识别经济因果联系，也不证明残差将收敛。

## Nearby concepts

与原始距离不同，残差对象依赖因子/复制模型；与协整不同，它通常针对收益或条件性解释，而非长期价格组合。

## Current project use/status

是 G2 的候选正常关系对象；因子定义、估计、点时性和稳定性必须自行验证。

## Paper / Claim ancestry

PF-008, PF-013; CL-PF-003, CL-PF-006. 教学说明，不构成证据。
