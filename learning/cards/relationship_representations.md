# Relationship Representations Are Different Constructs

**一句话直觉：** 同一对股票可以“相关”却不协整，也可以价格距离近却在控制共同成分后没有特殊关系；不同表示回答不同问题。

## Why it appeared

G2 不能把 distance、correlation、stochastic spread、cointegration 与 residual dependence 当作同一指标的不同参数。

## Core idea / equation

相关性可写为 `corr(r_i,r_j)`；协整检验某个价格组合 `p_i - beta p_j` 是否平稳；随机价差模型描述价差动态；残差表示保留由其他资产或因子未解释的部分。

## Measures / does not measure

这些方法分别测量共同收益变动、长期价格组合、假定动态、或条件性偏离。任何一种本身都不建立经济亲近性、结构不变性或交易有效性。

## Nearby concepts

“raw” 是未控制共同成分的关系；“residual/factor-adjusted” 是在某个控制模型之后的关系。模型选择本身会改变对象。

## Current project use/status

多个表示必须保持为 G2 的竞争候选；文献没有授权一般性优胜者。

## Paper / Claim ancestry

PF-005, PF-006; CL-PF-004, CL-PF-009. 教学说明，不构成证据。
