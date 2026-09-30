# S3 Phase A data feasibility and immutable manifest report

2026-09-30 · Frozen protocol commit: 0ef007f22deebcfc76520a5c4d6d72787a73606f.

**Overall state B: S3 DEVELOPMENT NON-ESTIMABLE UNDER FROZEN PROTOCOL.**

This is a bounded evidence-availability finding **for the evidence accessible and qualified in this Phase A**, not proof that no provider or account owner anywhere could hold the missing records. No mandatory family is presently certified for Phase B. In particular, binding historical account-specific borrow, funding/capital, order/settlement and timing evidence cannot be inferred from the existing daily market archive or supplied contracts: those contracts are absent. Proceeding now would require unsupported substitution. The strategy remains frozen; no fallback or redesign is proposed.

Authority: [Phase A record](../../decisions/S3_PHASE_A_EVIDENCE_AUTHORIZATION_AND_DISPOSITION.md).
Machine-readable deliverable: [immutable V1 manifest](../../../research/manifests/S3_PHASE_A_EVIDENCE_MANIFEST_V1.json), with [SHA-256 receipt](../../../research/manifests/S3_PHASE_A_EVIDENCE_MANIFEST_V1.sha256).
The manifest is an evidence inventory and qualification record, **not a qualified S3 dataset or a certificate that external payload bytes exist locally**. Corrections require a new manifest version with ancestry; do not overwrite V1.

## Scope and verification method

The authorized scientific/economic date interval is 2015-01-01 through 2019-12-31. Only source documentation, schema/source-code definitions, coverage declarations, manifests, receipt hashes and filesystem existence metadata were inspected. Parent metadata sometimes describes a broader archive; its envelope is recorded as provenance, not permission to read its scientific rows. No 2020–2025 scientific/economic outcome data were accessed. No raw market endpoint was called, account queried, or economic array opened; provider documentation examples were not used as project evidence.

Verified canonical main equals the specified frozen commit at the start. Reviewed the frozen protocol/plan, core metadata, inner-input metadata, C06 availability amendment, C04 inner-calendar metadata, sidecar schema, preparation source and external migration inventory. The latter is explicitly metadata-only; its paths/hashes are historical receipts, not fresh payload validation. Searched its raw/QA locators for the required new evidence types; no qualifying fund/borrow/order/intraday archive was identified. Library filenames matching substrings are not datasets.

The local repository has neither data/raw nor data/qa_work. No documented external research volume is mounted in this client. No alternative account/archive location was supplied during this audit. This establishes local inaccessibility, not destruction of the original Windows archive. A source catalogue is evidence of a possible product, not proof of a purchased, historically applicable, PIT-qualified dataset.

No numerical exposures, A/h/w, T1, z0, attempts, capture, costs or payoffs were computed. No counterfactual fills, forward development, PnL, C04 repair or V1 mutation occurred. No dataset completeness percentage is invented where the underlying permitted partition is inaccessible.

## Source/provider and field findings

The existing source architecture is Tushare daily stock/master/benchmark records plus official classification and action companions. Its historical approval explicitly retained provider-vintage, revision and missingness limitations; S3 cannot promote that into full execution qualification. C06's separate amendment establishes historical publication dates at date precision, but not an intraday receipt archive.

Current [Tushare daily schema](https://tushare.pro/document/2?doc_id=27) documents raw daily fields and identifies pre_close/pct_chg with ex-rights reference semantics. Thus those columns are not a substitute for an entitlement ledger or original receipt clock. Only field semantics were used here; no product sample values support this report.

[SSE Info's historical-product catalogue](https://www.sseinfo.com/services/assortment/historical/) documents snapshot, trade and bar product categories. It does not establish this project's licensed 2015–2019 both-venue stock/fund coverage, original receipt timestamps or broker acknowledgements. No current product cadence was converted into a historical IOC timing rule. Previously documented SZSE/issuer/index source classes remain candidate requirements, not newly qualified contracts. No provider was selected, purchased or contacted.

For each family below, “verified schema” means a field name/definition is present in the cited metadata or source; it does not mean every value, vintage, receipt, license or account term has passed. “Required/unverified” names exact missing contract fields, not fabricated dataset columns. Full details, source paths, hashes and reason codes are also in the manifest.

### Frozen baseline / relationship inputs

- **Source/provider; dataset:** Tushare C01/C03/E02/E03-A; official CSRC/CAPCO C06; internal frozen lineage. CORE-DATASET-FREEZE-V1; V1-PHASE1-INNER-INPUT-1.0; C06-AVAILABILITY-AMENDMENT-V1.
- **Verified schema fields:** `stable_security_id`, `observation_date`, `historical_ticker_code`, `identifier_lineage_state`, `c04_structural_state`, `c04_basis`, `c05_structural_state`, `c05_basis`, `eligibility_rule_version`, `upstream_artifact_references`, `schema_version`, `generation_version`, `ts_code`, `trade_date`, `open`, `close`, `vol`, `amount`, `snapshot_title`, `logical_snapshot_identifier`, `taxonomy_version`, `corrected_publication_time`
- **Required/unverified fields:** `source_event_time`, `original_receipt_time`, `source_revision_id`, `qualified_2015_2019_partition_hash`.
- **Coverage:** Declared parent core 2013-01-07–2025-12-31; declared inner input ends 2019-12-31. Authorized intersection 2015-01-01–2019-12-31 only; actual partition completeness not verified.
- **PIT/vintage:** Daily trade date is not original receipt time. C06 amendment uses first decision clock strictly after qualified publication date; date precision only. Raw-provider vintage/receipt proof remains limited. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Market/model fields generally account-independent; executable use needs separately qualified account evidence.
- **Missingness:** Payloads absent locally; no permitted restored partition; historical unknown missingness retained; no 2015–2019 missing-row percentage computed.
- **Legal/license/access:** Historical Tushare authorization does not prove present entitlement/license or rights for every S3 use; original licensing not supplied.
- **S3 support/disposition:** not qualified as a complete family; **REQUIRES DESCENDANT REQUALIFICATION**. Reasons: PAYLOAD_NOT_ACCESSIBLE, PIT_RECEIPT_UNVERIFIED, SCOPED_PARTITION_REQUIRED.
- **Evidence:** [CORE_DATASET_FREEZE_V1.json](../../../data/manifests/CORE_DATASET_FREEZE_V1.json); [V1_PHASE1_INNER_INPUT.json](../../../data/manifests/V1_PHASE1_INNER_INPUT.json); [SECURITY_DATE_ELIGIBILITY_SIDECAR_CONTRACT.md](../../../docs/stages/G3B/SECURITY_DATE_ELIGIBILITY_SIDECAR_CONTRACT.md); [V1_C06_AVAILABILITY_AMENDMENT_FREEZE.md](../../../docs/decisions/V1_C06_AVAILABILITY_AMENDMENT_FREEZE.md); [v1_phase1_prepare.py](../../../tools/v1_phase1_prepare.py).

### PIT fund-share universe and registry lineage

- **Source/provider; dataset:** No qualified project source identified; official issuer/exchange/index records are required source classes. UNAVAILABLE.
- **Verified schema fields:** None supplied for a qualifying dataset.
- **Required/unverified fields:** `instrument_id`, `exchange`, `share_class`, `first_tradable_date`, `delist_date`, `merger_predecessor_id`, `mandate`, `benchmark_id`, `taxonomy_version`, `holdings_publication_time`, `holdings_receipt_time`, `revision_id`, `currency`, `tick`, `lot`, `settlement_rule`, `calendar_version`.
- **Coverage:** No verified 2015–2019 candidate-universe dataset, including dead/merged funds.
- **PIT/vintage:** No vintage/receipt chain or historical mandate/taxonomy qualification supplied; present survivors cannot establish it. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Broker/share-class access and short eligibility unverified.
- **Missingness:** Entire required qualified registry lineage unavailable; no inferred missingness rate.
- **Legal/license/access:** No acquired fund-data license/account entitlement evidenced; no procurement performed.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: FUND_UNIVERSE_NOT_REGISTERED, SURVIVORSHIP_LINEAGE_UNVERIFIED, LICENSE_UNVERIFIED.
- **Evidence:** [EXTERNAL_ARTIFACT_INVENTORY.json](../../../research/migration/EXTERNAL_ARTIFACT_INVENTORY.json); [S3_FROZEN_STRATEGY_AND_PRE_DEVELOPMENT_PROTOCOL.md](../../../docs/stages/G5/S3_FROZEN_STRATEGY_AND_PRE_DEVELOPMENT_PROTOCOL.md).

### Stock/fund raw price and corporate-action histories

- **Source/provider; dataset:** Stock daily: Tushare; partial stock actions: SSE historical action tables/SZSE monthly tables; qualified fund source absent. CORE-DATASET-FREEZE-V1 stock C03; C04-A-OFFICIAL-CALENDAR-V1; fund component UNAVAILABLE.
- **Verified schema fields:** `ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`, `historical_ticker`, `record_date`, `effective_ex_date`, `action_publication_date`, `action_types`, `source`
- **Required/unverified fields:** `original_receipt_time`, `revision_chain`, `original_share_multiplier`, `cash_entitlement`, `long_tax_treatment`, `short_manufactured_distribution`, `receivable_settlement`, `fund_action_lineage`.
- **Coverage:** Stock parent envelope includes permitted years; inner C04 archive ends 2019-12. No full stock+fund 2015–2019 coverage qualification. No action/price rows read.
- **PIT/vintage:** C04 retrieval in 2026 is not historical availability; code allows absent publication dates. Action-date exclusion is not entitlement-complete accounting; future-adjusted price alone prohibited. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Gross issuer events alone do not establish account withholding, manufactured payments or settlement rights.
- **Missingness:** Fund histories and complete long/short cash-flow terms missing; original stock payloads inaccessible. No absence-as-clean inference.
- **Legal/license/access:** Official source provenance documented; archival/access/reuse rights and account applicability still require qualified terms.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: ENTITLEMENT_ACCOUNTING_UNQUALIFIED, FUND_HISTORY_UNAVAILABLE, PAYLOAD_NOT_ACCESSIBLE, RECEIPT_NOT_EVENT_TIME.
- **Evidence:** [C04_A_OFFICIAL_CALENDAR_V1.json](../../../data/manifests/C04_A_OFFICIAL_CALENDAR_V1.json); [v1_c04_official_action_calendar.py](../../../tools/v1_c04_official_action_calendar.py); [v1_phase1_prepare.py](../../../tools/v1_phase1_prepare.py); [SECURITY_DATE_ELIGIBILITY_SIDECAR_CONTRACT.md](../../../docs/stages/G3B/SECURITY_DATE_ELIGIBILITY_SIDECAR_CONTRACT.md).

### Factor reconstruction lineage

- **Source/provider; dataset:** Existing internal factor/model definitions, Tushare E03-A benchmark and official C06 membership; complete holding-accumulation source not qualified. V1-PHASE1-INNER-INPUT-1.0; G4-05-MODEL-CONTRACT-1.0; S3 C_f reconstruction UNAVAILABLE.
- **Verified schema fields:** `benchmark_response`, `industry`, `snapshot_index`, `snapshot_ids`, `taxonomy_versions`, `response`, `response_ok`, `pair_member`
- **Required/unverified fields:** `factor_id`, `factor_definition_version`, `constituent_id`, `weight_effective_time`, `weight_available_time`, `cash_flow_reconstruction_lineage`, `holding_accumulation_mapping`, `receipt_time`, `revision_id`.
- **Coverage:** Existing inner-input metadata covers permitted intersection; no separately qualified 2015–2019 cash-flow-consistent factor holding archive.
- **PIT/vintage:** Publication-qualified membership does not establish every constituent/weight/cash-flow vintage or factor-to-static-holding map. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Research factor itself is not a tradable instrument; account qualification not applicable to its equation, but basket remains account-dependent.
- **Missingness:** Frozen source schema exists; payload restoration and required static accumulation proof absent. No factors or tracking computed.
- **Legal/license/access:** Underlying licenses inherit raw sources; no additional licensed constituent/weight archive supplied.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: FACTOR_ACCUMULATION_UNQUALIFIED, PAYLOAD_NOT_ACCESSIBLE.
- **Evidence:** [G4_05_MODEL_SPECIFICATION_CONTRACT.json](../../../research/G4_05_MODEL_SPECIFICATION_CONTRACT.json); [v1_phase1_prepare.py](../../../tools/v1_phase1_prepare.py); [S3_FROZEN_STRATEGY_AND_PRE_DEVELOPMENT_PROTOCOL.md](../../../docs/stages/G5/S3_FROZEN_STRATEGY_AND_PRE_DEVELOPMENT_PROTOCOL.md).

### Intraday quotes/trades/calendar states

- **Source/provider; dataset:** SSE Info historical product capability documented; no qualified licensed project feed; SZSE source-contract qualification absent. Product catalogue only; acquired dataset identifier UNAVAILABLE.
- **Verified schema fields:** None supplied for a qualifying dataset.
- **Required/unverified fields:** `instrument_id`, `event_timestamp`, `receipt_timestamp`, `sequence`, `bid_price`, `ask_price`, `bid_quantity`, `ask_quantity`, `depth`, `trade_correction`, `halt_state`, `price_limit_state`, `continuous_open`, `continuous_close`, `calendar_revision`.
- **Coverage:** No verified both-venue stock+fund 2015–2019 partition coverage.
- **PIT/vintage:** Public snapshots/ticks product capability does not prove historical original receipt clocks, synchronized coverage or correction chain. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Market-feed license/access and route eligibility not evidenced for an execution account.
- **Missingness:** No acquired qualified intraday dataset found in bounded metadata inventory; daily OHLC cannot fill this gap.
- **Legal/license/access:** Commercial application/license needed where applicable; no signed entitlement, purchase or download.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: INTRADAY_ARCHIVE_NOT_QUALIFIED, RECEIPT_CLOCK_UNVERIFIED, LICENSE_UNVERIFIED.
- **Evidence:** [G3B_02_PROVIDER_FIELD_SCHEMA_PIT_QUALIFICATION_AUDIT.md](../../../docs/stages/G3B/G3B_02_PROVIDER_FIELD_SCHEMA_PIT_QUALIFICATION_AUDIT.md); [EXTERNAL_ARTIFACT_INVENTORY.json](../../../research/migration/EXTERNAL_ARTIFACT_INVENTORY.json).

### Account-specific historical borrow

- **Source/provider; dataset:** No historical broker/lender/account source supplied or registered. UNAVAILABLE.
- **Verified schema fields:** None supplied for a qualifying dataset.
- **Required/unverified fields:** `account_id`, `broker_id`, `lender_id`, `instrument_id`, `locate_id`, `locate_receipt_time`, `valid_from`, `valid_to`, `binding_commitment`, `reserved_quantity`, `remaining_quantity`, `borrow_rate`, `reset_formula`, `day_count`, `minimum_fee`, `collateral_terms`, `recall_notice_time`, `recall_deadline`, `buyin_terms`, `manufactured_distribution_terms`, `short_restrictions`.
- **Coverage:** No verified records for any required 2015–2019 account/instrument/time.
- **PIT/vintage:** No historical locate/commitment receipt or revisions; present-day lists and exchange short-interest aggregates are not substitutes. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Not qualified: no named applicable account, historical agreement or reservation evidence.
- **Missingness:** Entire binding commitment/quantity/terms chain unavailable; missing is not not-borrowable or zero fee.
- **Legal/license/access:** Private broker/lender records require owner authority and applicable confidentiality/access rights; no credentials requested/accessed.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: HISTORICAL_BINDING_LOCATE_ABSENT, ACCOUNT_NOT_IDENTIFIED.
- **Evidence:** [EXTERNAL_ARTIFACT_INVENTORY.json](../../../research/migration/EXTERNAL_ARTIFACT_INVENTORY.json); [S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md](../../../docs/stages/G5/S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md).

### Funding/collateral/fees/capital terms

- **Source/provider; dataset:** No historical account-specific broker/custodian/funder contracts supplied. UNAVAILABLE.
- **Verified schema fields:** None supplied for a qualifying dataset.
- **Required/unverified fields:** `account_id`, `effective_from`, `effective_to`, `available_time`, `contract_version`, `funded_NAV_basis`, `book_allocation`, `cash_balance`, `encumbrances`, `eligible_collateral`, `haircuts`, `initial_margin`, `maintenance_margin`, `restricted_proceeds`, `credit_limit`, `funding_rate`, `day_count`, `commission_schedule`, `tax_applicability`, `fee_minimum`, `rebates`.
- **Coverage:** No verified 2015–2019 historical applicability or capital basis.
- **PIT/vintage:** Current public rules cannot establish historic signed account terms, receipt times or revisions. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Not qualified: no account, capital allocation, historical facility or applicable fee contract.
- **Missingness:** Required terms unknown; no invented capital/fees/rates, no balance/PnL inspection.
- **Legal/license/access:** Private account contracts and licensed records not available; no procurement/account contact performed.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: HISTORICAL_ACCOUNT_TERMS_ABSENT, CAPITAL_BASIS_UNDECLARED.
- **Evidence:** [EXTERNAL_ARTIFACT_INVENTORY.json](../../../research/migration/EXTERNAL_ARTIFACT_INVENTORY.json); [S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md](../../../docs/stages/G5/S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md).

### Orders/fills/cancels/settlement evidence

- **Source/provider; dataset:** No historical broker/venue order-event or settlement archive identified; old research simulations not qualifying source. UNAVAILABLE.
- **Verified schema fields:** None supplied for a qualifying dataset.
- **Required/unverified fields:** `account_id`, `parent_order_id`, `child_order_id`, `instrument_id`, `side`, `requested_quantity`, `filled_quantity`, `limit_price`, `benchmark_timestamp`, `submit_time`, `ack_time`, `reject_time`, `cancel_time`, `fill_time`, `receipt_time`, `sequence`, `late_fill_link`, `fee_event`, `borrow_return`, `cash_settlement`, `remaining_claim`.
- **Coverage:** No verified 2015–2019 complete event lifecycle for the frozen execution contract.
- **PIT/vintage:** No sequence/receipt/late-fill/cancel completeness certificate; market prints or bars do not identify account fills. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Not qualified: absent account and route/settlement linkage.
- **Missingness:** Observed or independently qualified reconstructible path evidence missing; counterfactual reconstruction not performed.
- **Legal/license/access:** Account/venue confidentiality and use rights unverified. Historical trading-result artifacts excluded from inspection.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: ORDER_EVENT_EVIDENCE_ABSENT, COUNTERFACTUAL_IDENTIFICATION_UNPROVEN.
- **Evidence:** [EXTERNAL_ARTIFACT_INVENTORY.json](../../../research/migration/EXTERNAL_ARTIFACT_INVENTORY.json); [S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md](../../../docs/stages/G5/S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md).

### Timing-contract evidence

- **Source/provider; dataset:** No qualified historical feed/venue/broker service-contract bundle supplied. UNAVAILABLE.
- **Verified schema fields:** None supplied for a qualifying dataset.
- **Required/unverified fields:** `feed_id`, `venue_id`, `account_route_id`, `clock_basis`, `timestamp_resolution`, `clock_error_bound`, `receipt_latency_bound`, `quote_validity`, `cross_leg_skew_bound`, `dispatch_bound`, `ack_deadline`, `cancel_semantics`, `IOC_completion_deadline`, `retry_rule`, `effective_dates`, `available_time`, `version`.
- **Coverage:** No verified contracts effective across required 2015–2019 sessions.
- **PIT/vintage:** Current product frequency is not a historical end-to-end receipt/dispatch/ack guarantee. Pinned repository evidence at 0ef007f22deebcfc76520a5c4d6d72787a73606f; historical provider/receipt version unverified unless explicitly documented.
- **Account:** Not qualified: no account/route-specific historical semantics.
- **Missingness:** All contractual timing bounds required for qualified joint entry/exit remain unidentified.
- **Legal/license/access:** Historical feed/broker contracts needed; no current brochure is backdated.
- **S3 support/disposition:** not qualified as a complete family; **MISSING / NON-ESTIMABLE**. Reasons: HISTORICAL_TIMING_CONTRACT_ABSENT, ACCOUNT_ROUTE_UNQUALIFIED.
- **Evidence:** [EXTERNAL_ARTIFACT_INVENTORY.json](../../../research/migration/EXTERNAL_ARTIFACT_INVENTORY.json); [S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md](../../../docs/stages/G5/S3_DATA_ACQUISITION_AND_DEVELOPMENT_EXECUTION_PLAN.md).

## C04 lineage and bounded descendant requirement

The frozen core sidecar explicitly leaves C04 unresolved. The later inner C04-A descendant records identified action dates/exclusions and states that no identified action does not mean authoritatively action-clean. Its metadata says no adjusted price was constructed and core state was not mutated. The inspected preparation source derives response eligibility by excluding dates found in the action calendar; it does not build the complete cash/stock/right/short-entitlement accounting S3 requires.

The documented later-period mismatch arose when a calendar ending in 2019 was reused for extended inputs. That 2020–2025 issue is **OUT OF SCOPE** here: its documented mechanism was read, but no later action rows, masks, outcomes or extension payloads were opened. This audit does **not** assert a newly measured 2015–2019 mask discrepancy. Within the permitted region the independently established gap is exclusion-calendar versus full S3 entitlement/availability qualification.

A conditional immutable descendant path is specified, not executed:
- **Sources:** unchanged frozen stock raw files and sidecar; C04-A-OFFICIAL-CALENDAR-V1 and its official SSE historical tables/SZSE monthly records; C06 availability amendment; for missing terms, original issuer/exchange notices and account-specific long/short tax/manufactured-distribution/settlement contracts. Missing fund histories require independently qualified issuer/exchange fund evidence.
- **Affected fields:** c04_structural_state/c04_basis, effective_ex_date, record_date, action_publication_date, revision/receipt lineage, original-share multipliers, signed cash/rights/receivables, tax/short-entitlement applicability, and lineage of downstream response_ok/pair_member masks. No response/payoff values are recalculated in Phase A.
- **Affected periods:** potential coverage is 2015-01-01–2019-12-31 only. Exact security/date rows are not verified and must not be invented. Earlier formation and later completion are excluded.
- **Transformation:** verify original hashes; create a safely isolated authorized-date partition; join stable IDs and dated action/availability metadata; preserve unknowns; attach original-share entitlement/account terms with explicit proof. Never infer clean intervals from absent notices, substitute future-adjusted prices, splice economic identities, or overwrite core/C04 parents.
- **Expected version:** proposed logical descendant S3-INPUT-QUALIFICATION-2015-2019-V1, with a C04/entitlement companion S3-C04-ENTITLEMENT-2015-2019-V1. These names reserve a prospective output identity only; no dataset/version has been created or qualified.
- **Required authorization:** a separate bounded restoration/partitioning and descendant-requalification action naming source versions, fields, paths and permitted verification. Metadata-only joins/checks may be non-scientific if they expose no economic values. Entitlement reconstruction, response regeneration and price/cash-flow transforms are not authorized by this Phase A and require their own explicit bounded scope. A custodian-produced permitted-date export must retain parent/partition hashes; merely running the old multi-year loader would cross the current boundary.
- **Feasibility:** conditional engineering lineage exists for existing metadata; availability of missing original/account evidence is unproven. This is not a fully qualified, non-scientific repair path for all mandatory families and therefore cannot justify overall state A.

## Integrity and limitations

The manifest registers Git blob identities and freshly computed SHA-256 hashes of the metadata/schema documents actually read. Its detached checksum certifies the manifest bytes. Frozen-core/inner-input/C04 payload hashes are explicitly labeled **previously recorded expected hashes; payload not rehashed**. No core-data validator was run because its mixed-period external inputs are unavailable and outside the present payload scope. PowerShell validators are unavailable in this client. JSON/schema, exact nine-family disposition, citation/link, historical-preservation, whitespace and allowed-path checks are the present validation scope.

No source row count spanning the parent archive is reported as 2015–2019 coverage. “Missing” means the required evidence was not supplied/located/qualified within this bounded inventory, not zero events or a measured negative economic result. Current contracts, borrow lists, daily OHLC, adjusted prices and survivor-only fund lists cannot cure the missing historical proof. Any later supplied original evidence must receive a new immutable qualification record; the frozen strategy is not amended.

Phase A is complete as an evidence feasibility/manifest action. Phase B is **not eligible or authorized** on this record. No further computation or automatic acquisition follows; NEXT_ACTION returns to NONE.

**S3 DEVELOPMENT NON-ESTIMABLE UNDER FROZEN PROTOCOL**

| Evidence family | Qualified source exists? | Coverage | PIT-qualified? | Account-qualified? | Mandatory for S3? | Disposition |
|---|---|---|---|---|---|---|
| Frozen baseline / relationship inputs | No complete qualified family (ancestors registered) | Parent interval declared; permitted partition not verified | No (C06 date-level lineage only) | Not established where required | Yes | REQUIRES DESCENDANT REQUALIFICATION |
| PIT fund-share universe and registry lineage | No complete qualified family | 2015–2019 not verified | No | Not established where required | Yes | MISSING / NON-ESTIMABLE |
| Stock/fund raw price and corporate-action histories | No complete qualified family | Stock/C04 parent metadata; funds missing | No | Not established where required | Yes | MISSING / NON-ESTIMABLE |
| Factor reconstruction lineage | No complete qualified family | Inner research inputs declared; holding reconstruction missing | No | Not established where required | Yes | MISSING / NON-ESTIMABLE |
| Intraday quotes/trades/calendar states | No complete qualified family | 2015–2019 not verified | No | Not established where required | Yes | MISSING / NON-ESTIMABLE |
| Account-specific historical borrow | No complete qualified family | 2015–2019 not verified | No | No | Yes | MISSING / NON-ESTIMABLE |
| Funding/collateral/fees/capital terms | No complete qualified family | 2015–2019 not verified | No | No | Yes | MISSING / NON-ESTIMABLE |
| Orders/fills/cancels/settlement evidence | No complete qualified family | 2015–2019 not verified | No | No | Yes | MISSING / NON-ESTIMABLE |
| Timing-contract evidence | No complete qualified family | 2015–2019 not verified | No | No | Yes | MISSING / NON-ESTIMABLE |
