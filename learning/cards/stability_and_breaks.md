# Relationship Stability and Breaks

**一句话直觉：** 过去有关系不代表现在仍有；持续性或突变信息更适合当作“关系是否还可用”的警报。

## Why it appeared

Pair validity 需要把静态相似与关系持续性拆开，并为拒绝/不交易保留位置。

## Core idea / equation

PF-006 观察协整网络边的重复出现与存活；PF-007 使用时频特征估计结构断裂概率。两者都是关系变化的统计表征。

## Measures / does not measure

测量历史可重复性、关系改变或断裂风险。不能直接识别基本面原因、M0，或给出统一的失效阈值。

## Nearby concepts

稳定性不是经济接近性，也不是当期统计依赖；它是关系在时间上是否持续的额外问题。

## Current project use/status

可作为冻结 G2-08 架构中 R0 Relationship-Validity Warning 的候选 ancestry，但 break warning 不等于 M0。Pair Rejection、Event Rejection 与 Decision Rejection/U 必须分开；R0–R3 均未选择，检测方法、阈值和结构性解释也未冻结。

## Paper / Claim ancestry

PF-006, PF-007; CL-PF-004, CL-PF-005. 教学说明，不构成证据。
