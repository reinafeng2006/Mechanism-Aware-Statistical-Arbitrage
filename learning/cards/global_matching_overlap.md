# Global Matching and Overlap Control

**一句话直觉：** 即使每个候选关系都看起来合理，把同一只股票反复放进多个 pair 仍会造成集中风险；全局匹配管的是组合配置约束。

## Why it appeared

G1 要分开回答“这对是否有关系”与“多个候选怎样不重叠地一起使用”。

## Core idea

PF-010 在候选协整图上做最大权重匹配，使一个资产不被多个最终 pair 共享。

## Measures / does not measure

它控制重叠、集中和组合层面的一致性。它不验证 pair 的经济关系、统计真实性或稳定性。

## Nearby concepts

这是统计/组合治理，不是 company similarity，也不是 relationship validity。

## Current project use/status

若进入后续设计，只能作为一般化与组合治理候选；未选择任何图或匹配算法。

## Paper / Claim ancestry

PF-010; CL-PF-010. 教学说明，不构成证据。
