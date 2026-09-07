# Event-Time Provenance versus Outcome Validation

**一句话直觉：** “信息何时首次公开、peer 当时有没有反应”属于当时可用的解释证据；“peer 后来是否追上”只能检验预测有没有发生。

## Core distinction

Decision-time candidates include link vintage/effective date, source identity, first-public timestamp, source and peer price/return through the decision time, own-news and pre-event leakage checks. Later peer return, portfolio return and real performance are outcome-only validation variables.

## What it does not establish

public timestamp 不是 private information 未先传播的证明；daily close 也可能太粗，不能识别经济上有效的信息到达时间。

## Current project status

**DEFINED timing principle; G2-11 SEMANTIC CONTRACT APPROVED / FROZEN.** G2-11 freezes six separate timestamps: `observation_time`, `public_time`, `available_time`, `compute_time`, `decision_time`, and `outcome_time`. Event-time inputs require `available_time ≤ decision_time`; derived inputs must also finish computation by decision time. G3 才决定 provider、实际 frequency、数据库与 acquisition。

## Frequency versus latency

Source/update frequency、observation granularity、publication/availability latency、computation latency 与 decision-path latency 是不同属性。低频 filing 在新发布时仍可成为 fast timestamped update；重复计算未变化数据不构成新证据。

## Lineage chain

`raw source → source vintage → availability time → transformation/version → derived measurement → downstream use`

这条链解释一项信息为什么可合法进入某个 decision origin；它不选择数据库 schema 或 provider。

## Paper / Claim ancestry

M1-001, M1-008; CL-M1-001, CL-M1-003. 教学说明，不构成证据。
