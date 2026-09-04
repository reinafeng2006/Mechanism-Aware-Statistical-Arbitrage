# Raw Price-Path Distance

**一句话直觉：** 如果两条经过同一尺度处理的历史价格路径靠得近，距离法会把它们视为候选；它只是在描述过去的共同路径。

## Why it appeared

距离是 Pair Formation 文献中常见的原始价格关系表示，必须与残差和协整分开理解。

## Core idea / equation

将形成期价格归一化后，以平方距离排序：`D(i,j)=sum_t (P_i,t - P_j,t)^2`。PF-004 的训练期与随后交易期分离是时序治理，不是经济有效性的证明。

## Measures / does not measure

测量原始、归一化历史价格路径的接近度。不能证明经济联系、因子调整后的依赖、协整、未来稳定性或利润来源。

## Nearby concepts

相关性关注共同变动；协整关注非平稳价格的长期线性组合；残差方法关注控制共同解释成分后的偏离。

## Current project use/status

保留为 G2 候选关系表示；尚未选择窗口、尺度、阈值或用途。

## Paper / Claim ancestry

PF-004; CL-PF-002. 教学说明，不构成证据。
