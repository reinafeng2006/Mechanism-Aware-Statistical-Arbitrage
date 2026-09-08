# G3B-03 — C06 Historical Industry Membership Qualification Audit

Status: **ACCEPTED / FROZEN — 2026-09-08**  
Boundary: source/PIT qualification only. No full membership files, market history, measurements, targets or outcomes were acquired or computed.

## Decision question

For security `i` and decision date `t`:

> Was security `i` legitimately inside the frozen target-industry universe using the classification information publicly available at `t`?

`current industry membership ≠ historical industry membership`.

## Finding

At least one defensible C06 path exists: **official dated full-market classification snapshots published by the CSRC / China Association for Public Companies (CAPCO), converted into publication-time as-of intervals and joined to the PIT security master.**

- The CSRC/CAPCO archive provides quarterly classification results from 2012 Q4 through 2021 Q3; the first archived result was published on 2013-01-07. The official archive then provides half-year results beginning with 2023 H1, published on 2024-02-08, and continuing thereafter.
- A 2013 CSRC announcement states that classification results would be published quarterly and used consistently within the regulatory statistical system.
- The CAPCO 2023 guideline took effect on 2023-05-01, defines the taxonomy/method, makes classification semiannual, and requires publication of results on the association website. It also specifies classification based principally on publicly disclosed audited financial information and describes initial/reclassification processes.
- Machinery-relevant major classes 34 (general-purpose equipment manufacturing) and 35 (special-purpose equipment manufacturing) exist in the inspected classification standards. This observation does **not** itself freeze the project's exact machinery-universe code set.

Qualification: **`QUALIFIED WITH DOCUMENTED LIMITATIONS — SUFFICIENT FOR A FORMAL ACQUISITION PROPOSAL`**.

## Why this is PIT-defensible

The reconstruction uses each snapshot only from its actual web publication time onward. The classification period label is descriptive; it is not treated as the availability date. Between publications, the state is `latest officially published classification as of t`, with age/staleness retained. Newly listed securities enter only when both security-master eligibility and a publicly available classification snapshot support membership.

This path avoids using today's constituents retrospectively and does not infer unpublished reclassifications.

## Remaining limitations

1. Snapshot frequency is quarterly under the 2012 regime and semiannual under the 2023 regime; true business change can precede the next official classification.
2. The visible archive has a long publication interval between 2021 Q3 and 2023 H1. Carrying the latest published state is PIT-legal but increasingly stale and must be flagged.
3. Taxonomy/method versions changed. Codes may look stable while rules or hierarchy change; version identity and crosswalk cannot be discarded.
4. Publication-page timestamps establish public availability at page/date granularity, not necessarily intraday release time. Same-day use therefore requires a conservative next-decision-clock rule unless exact release time is captured.
5. Snapshot membership does not itself supply listing/delisting or code-history truth; C01 remains a required join.
6. Exact project machinery scope—e.g. whether it is limited to official major classes 34/35 or uses another prespecified mapping—remains a researcher universe-definition decision, not a source-derived choice.

## Audit evidence

- [CSRC historical classification archive, 2012 Q4–2017 Q1 page](https://www.csrc.gov.cn/csrc/c100103/common_list_2.shtml)
- [CSRC/CAPCO archive, 2017 Q2–2021 Q3 page](https://www.csrc.gov.cn/csrc/c100103/common_list.shtml)
- [CAPCO classification-results archive](https://www.capco.org.cn/xhgg/hyfl/hyfljg/index.html)
- [CSRC 2013 publication announcement](https://www.csrc.gov.cn/csrc_en/c102034/c1371351/content.shtml)
- [CAPCO 2023 classification guideline](https://www.capco.org.cn/xhdt/tzgg/202305/20230521/j_2023052117544500016846630061707656.html)
- [JR/T 0020—2024 listed-company industry statistical classification](https://www.csrc.gov.cn/csrc/c101954/c7520291/7520291/files/%E9%99%84%E4%BB%B61%EF%BC%9A%E3%80%8A%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E8%A1%8C%E4%B8%9A%E7%BB%9F%E8%AE%A1%E5%88%86%E7%B1%BB%E4%B8%8E%E4%BB%A3%E7%A0%81%E3%80%8B.pdf)

Documentation establishes a qualified acquisition path; the actual files must later be acquired immutably under separate authorization.
