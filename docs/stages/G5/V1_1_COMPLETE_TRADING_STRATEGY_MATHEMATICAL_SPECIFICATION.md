# Trading V1.1 — complete mathematical specification and completeness audit

Date: 2026-09-18. Status: **RESEARCHER REVIEW; EXECUTION PAUSED**.

This is a non-empirical assembly of the frozen strategy, not permission to execute it. No PnL was computed or inspected for this audit. Prior execution history is preserved, not retroactively erased. C04 correction, further trading execution and result inspection remain paused until researcher approval. Revision 2 incorporates the explicit held-security post-entry researcher decision S12. The mathematical completeness audit finds no remaining policy choice within this strategy's scope. Mathematical completeness does not certify code conformance, data qualification or historical execution; the outstanding conformance findings below remain unresolved and no repair is authorized.

## 1. Ancestry and notation

Equation ancestry labels below identify repository-relative frozen records and separately identify executable source. Source code documents implementation, not authority to resolve a policy conflict.

| Label | Source |
|---|---|
| S1 | `docs/decisions/V1_PRECOMPUTATION_TRADING_PROTOCOL_FREEZE.md`; `docs/decisions/V1_PAIR_UNIVERSE_FREEZE.md` (TRADE-A, PAIR-A) |
| S2 | `docs/stages/G4/G4_05_V1_EXECUTABLE_SPECIFICATION_REGISTRY.md`; `docs/stages/G4/G4_05A_R0_R1_STATISTICAL_COMMON_FACTOR_RELATIONSHIP_SPECIFICATION_PROPOSAL.md` |
| S3 | `docs/decisions/V1_EXECUTABLE_SEMANTICS_AMENDMENT_FREEZE.md`; `research/V1_EXECUTABLE_SEMANTICS_CONTRACT.json` |
| S4 | `docs/stages/G4/G4_04A3_CONTINUOUS_ABNORMALITY_METRIC_SPECIFICATION_PROPOSAL.md`; `docs/stages/G4/G4_04A5_RESOLUTION_OUTCOME_TARGET_VALIDATION_SPECIFICATION_PROPOSAL.md` |
| S5 | `docs/decisions/V1_MP1_A_PIT_REFERENCE_FREEZE.md`; `research/V1_MP1_I_A_CONTRACT.json` |
| S6 | `docs/decisions/V1_EV_A_V1_FD_A_ER_A_EXECUTABLE_CLOSURE.md`; `docs/decisions/V1_EV_MAP_B_FREEZE.md`; corresponding `research/V1_EXECUTABLE_CLOSURE_EV_A_V1_FD_A_ER_A.json` and `research/V1_EV_MAP_B_CONTRACT.json` |
| S7 | `research/V1_DC_A_EP_A_CONTRACT.json`; `research/V1_DECA_A_CONTRACT.json` |
| S8 | `docs/stages/G5/V1_1_FINAL_SINGLE_POLICY_CHECKPOINT.md`; approved descendant `research/TRADING_V1_1_POLICY.json` |
| S9 | `docs/decisions/V1_1_OPTION_A_ADMISSION_SIZING_DECISION.md`; `docs/decisions/V1_1_SIMULTANEOUS_ADMISSION_FINAL_FREEZE.md` |
| S10 | `docs/stages/G5/G5_TRADING_SIMULATION_V1_PROTOCOL_PROPOSAL.md` |
| S11 | `docs/stages/G4/V1_A1_H126_CANDIDATE_NEUTRAL_SCALE_AMENDMENT.md` |
| S12 | `docs/decisions/V1_1_HELD_SECURITY_POST_ENTRY_ELIGIBILITY_FREEZE.md` — researcher-selected held-security post-entry binding, 2026-09-18 |
| K1 | `tools/v1_phase1_inner_relationships.py` |
| K2 | `tools/v1_phase1_inner_r3.py` |
| K3 | `tools/v1_inner_a3_a5.py`; `tools/v1_phase1_prepare.py` |
| K4 | `tools/v1_1_trading.py` |
| K5 | `tools/v1_1_accounting.py` |

| Symbol | Definition |
|---|---|
| c, p={i,j}, k | Candidate, unordered eligible pair, security; i→j is a direction, not a second independent pair |
| t,s,q; o_t,z_t | Exchange session indices; its open and close timestamps |
| D_t, F_tau | Qualified PIT data at decision t; information actually available by timestamp tau, including availability/vintage/identifier lineage |
| P_kt,O_kt,y_kt | Raw close, raw open, qualified simple close-to-close response of security k |
| r_c(t), H_c, U_c, W_cpt | Last eligible refresh strictly prior to evaluated response construction, history length, refresh cadence, ordered qualified estimation history |
| m_s,q_kps | Frozen E03-A market response; own-industry pair-excluded response factor |
| mu_j\|i,t, a_i→j,t | Candidate expected directional response; observed minus expected departure |
| Fin(x), NZ(x), 1{E}, bottom | Finite-real predicate; finite and exactly nonzero predicate; Boolean indicator; unavailable (never numerical zero) |
| h in {P,S}, e | Peer/source channel; episode (candidate, fold, unordered pair, channel, admitted signal) |
| k_e,t_e,u_e | Episode traded security, original signal session, executed entry session |
| C,n_k,V,H_k,X_k | Book cash, security shares, NAV, surviving open-valued holdings, exiting open-valued holdings |
| kappa | One-way transaction-cost fraction: 0.0005, 0.0010 or 0.0020 |
| A,B,N,x_raw,x_e | Survivor count, simultaneous qualified proposal count, A+B, raw admission notional, executable new notional |
| ell_e(q), T_e | Held-security eligible-session predicate and qualified close-time resolution-decision set, defined in section 6 under S12 |

All other symbols are defined at first use. Candidate/fold/cost subscripts are suppressed where the equation applies separately to every book. No cross-candidate pooling, cross-fold capital transfer, short borrowing or inferred missing values is implicit.

## 2. PIT input and model equations

PAIR-A is the complete unordered universe of securities satisfying the frozen PIT C06 industry eligibility (34/35, including cross-industry pairs). There is no distance/correlation filter or Top-K selection. For qualified consecutive raw closes,

`y_kt = P_kt / P_k,t-1 − 1`. [S1–S3; K1,K3]

Its domain requires positive finite prices, stable identifier, both endpoints C05-normal, qualified C04 exclusions and no unidentified suspension/return bridge. Outside the domain y is unavailable, not zero. A bounded calendar's absence of an identified action is not proof of authoritative action-clean coverage. C06 uses the latest legitimately available snapshot, retains vintage/taxonomy lineage and does not invent a staleness cutoff.

`W_cpt = last H_c synchronized candidate-qualified observations strictly before refresh r_c(t)`. [S2,S3]

H counts observations, not days. No shortened-history fallback is permitted. Weekly/monthly refresh means the first candidate-eligible exchange session of the ISO week/calendar month; coefficients then remain fixed until the next authorized refresh. Current conditioning responses/factors are observable at the decision close. A conditional contemporaneous response is **not** a next-session return forecast. The evaluated dependent response never enters its own fit.

| Candidate identity | H / U | Directional dependent / explanatory variables | Estimator |
|---|---|---|---|
| R0-D252 / `V1-R0D-252M` | 252 / monthly | y_j / (1,y_i) | Directional OLS |
| R0-C126 / `V1-R0C-126W` | 126 / weekly | y_j / (1,y_i) | Directional OLS |
| R0-L126 / `V1-R0L-126W` | 126 / weekly | y_j / (1,y_i) | Directional OLS |
| R1-M126 / `V1-R1M-126W` | 126 / weekly | Market-residual u_j / (1,u_i) | Per-leg factor OLS, then directional residual OLS |
| R1-MI126 / `V1-R1MI-126W` | 126 / weekly | Market/industry-residual u_j / (1,u_i) | Per-leg factor OLS, then directional residual OLS |
| R3-252 / `V1-R3-252M` | 252 / monthly | y_j / (1,y_i), stratum random intercept/slope | Gaussian empirical-Bayes REML and BLUP |

### 2.1 All three R0 prediction bridges

For x_s=y_is, v_s=y_js on W, let n=H, bars denote sample means, Sxx=sum(x_s−xbar)^2 and Sxv=sum(x_s−xbar)(v_s−vbar).

`beta_ji = Sxv/Sxx; alpha_ji = vbar−beta_ji*xbar; mu_j|i,t = alpha_ji+beta_ji*y_it`. [S2,S3; K1]

The reverse direction is a separate OLS fit with x and v exchanged; it is not an algebraic inverse. Full rank, n≥3 and positive residual degrees of freedom are required. Residual variance is `R=sum(v−alpha−beta*x)^2/(n−2)`; no epsilon denominator rescue.

R0-D's representation uses chronological cumulative simple responses `C_kl=sum_{r≤l} y_k,sr`, centers `b_k=median_l C_kl`, and spreads `d_k=median_l |C_kl−b_k|`. Its distance is

`D_p = mean_l [ (C_il−b_i)/d_i − (C_jl−b_j)/d_j ]^2`. [S2; K1]

This representation's MAD does not include 1.4826. Zero/invalid d makes the representation unavailable. D is not the prediction equation, hedge ratio or selection filter. R0-C's representation is Pearson correlation `rho=Sxv/sqrt(Sxx*Svv)`; R0-L uses the explicit linear bridge. With identical qualified H126 histories, R0-C and R0-L have the same executable directional prediction equation. Their equality is specification-consistent, not proof of independent economic discoveries. [S2,S3; K1]

### 2.2 R1 factor and residual bridges

Let Z_M,s=(1,m_s) and Z_MI,kps=(1,m_s,q_kps). For each leg k independently,

`theta_k = (Z_k'Z_k)^−1 Z_k'y_k; f_ks=Z_ks*theta_k; u_ks=y_ks−f_ks`. [S2,S3; K1]

The first element is an intercept; the others are market and, for MI, industry loadings. The market is the single fixed E03-A benchmark bound by input lineage, not an implementation-time choice of index. The industry factor is

`q_kps = (1/|J_kps|) sum_{l in J_kps} y_ls`,

where J is the qualified own-industry constituent set excluding **both** pair members; empty J makes the factor unavailable. S3's later amendment binds the leg's own industry g(k,t) legitimately available at the decision origin: q_kps=q_{g(k,t),s}, with contemporaneous eligible constituents at s. This supersedes earlier historical-leg-index wording; code conformance is a separate issue below. [S2,S3]

Using residuals from those per-leg fits, fit `u_js=alpha^u_ji+beta^u_ji*u_is+epsilon_s` by the OLS equations above. Then

`mu_j|i,t = f_jt + alpha^u_ji + beta^u_ji*(y_it−f_it)`. [S3; K1]

Reverse residual regression is fitted separately. M uses no industry regressor; MI uses each leg's own factor, not a shared average of the two industries. MI's required factor availability may reduce native history/support relative to M. Prediction-domain eligibility and cross-candidate matched support are distinct.

For a scalar directional bridge, K1 records predictive variance `R*[1+1/n+(x_t−xbar)^2/Sxx]`, with raw x for R0 and residual x for R1. This is a diagnostic, not the A3 scale, and does not silently include first-stage factor-estimation uncertainty. [S2–S4; K1]

### 2.3 R3 hierarchical bridge

Fit separately by PIT taxonomy-versioned unordered industry stratum (34×34, 35×35, 34×35) and stored direction. For each eligible pair p, X_p has rows (1,y_is), Y_p has entries y_js:

`Y_p = X_p beta_G + X_p b_p + epsilon_p; b_p ~ N(0,D); epsilon_p ~ N(0,R I)`.

`D=L L'; L=[[l00,0],[l10,l11]], l00,l11≥0; V_p=X_p D X_p'+R I`. [S2,S3; K2]

Stack Y and X and use block-diagonal V. With `P_V=V^−1−V^−1 X(X'V^−1 X)^−1 X'V^−1`, estimate covariance parameters by minimizing

`0.5*[log|V|+log|X'V^−1 X|+Y'P_V Y+(n−2)log(2*pi)]`,

where n is total stacked observations. Then

`beta_G=(X'V^−1 X)^−1 X'V^−1 Y`,

`C_p=L[I+L'X_p'X_p L/R]^−1 L'`,

`bhat_p=C_p X_p'(Y_p−X_p beta_G)/R`,

`mu_j|i,t=(1,y_it)*(beta_G+bhat_p)`. [S2,S3; K2]

H252/U1M, separate directions and PIT stratum membership remain mandatory. N0 fixes D=0 and is the pooled stratum reference, not a seventh trading book. A positive-semidefinite boundary D is not automatically a failure. Unsupported rank, insufficient independent pairs, nonfinite likelihood or failed convergence are not repaired by substituting another model.

K2 uses one L-BFGS-B fit (maxiter 1000, ftol 1e-8); initialization is pooled-OLS residual variance and the sample covariance (ddof=1) of pair-OLS coefficients, symmetrized with negative initialization eigenvalues clipped to zero and triangular square-root construction. These are recorded implementation mechanics, not permission to retune. K2's conditional prediction variance is `R+(1,y_it) C_p (1,y_it)'`; fixed-effect/hyperparameter uncertainty is not added by this audit. [K2; S2,S3 estimator ancestry]

## 3. A3 and morphology

For each direction,

`a_i→j,t = y_jt−mu_j|i,t; g_i→j,t=−a_i→j,t; e_i→j,t=a_j→i,t`.

`UR0_i→j,t=|mu_j|i,t|−sign(mu_j|i,t)*y_jt=sign(mu_j|i,t)*g_i→j,t`.

`PS0(W)=1.4826*median_{s in W}|y_s−median_W y|`,

`PS1(W)=sqrt(sum_{s in W}(y_s−mean_W y)^2/(|W|−1))`,

`MP0_i→j,t=e_i→j,t/PS0_i`. [S4; K1–K4]

PS0/PS1 fail only when unavailable, nonfinite, exactly zero or mathematically unsupported; PS1 requires at least two observations. No near-zero threshold is introduced. UR1, when a legitimately calibrated positive predictive SD exists, is UR0 divided by that SD; otherwise uncertainty is explicitly unavailable. UR1 is not a new V1.1 gate.

**Scale lineage:** A1 common-support loss uses the separately versioned candidate-neutral strictly-prior H126 PS0/PS1 layer. S11 explicitly preserves existing A3/A5 payloads, and S8 inherits those objects. Trading therefore consumes their stored scales, not a newly substituted A1 layer. K3's A3 uses candidate-native scales (H126 or H252); the earlier S4 candidate-neutral description must not be used to mislabel these fields. Historical candidate-native scales are NOT CANONICAL FOR CROSS-CANDIDATE A1 LOSS COMPARISON. This lineage limitation is disclosed, not repaired here. [S4,S8,S11]

K3 stores the four A3 columns as float32: `(a_i→j, a_i→j/PS0_j, a_j→i, a_j→i/PS0_i)`. K4 consumes those immutable fields, promoting to float64 for arithmetic; its g/e anchors use the stored departures. K3's A5 generation uses its internal departure precision. The algebraic identity above is not a claim of bitwise identity across differently rounded operands. Preserve payload/field/precision lineage; do not refit or regenerate them. [K3,K4; S11]

Let v_kt be positive finite volume, b_kt positive finite amount, and Q_kt=b_kt/v_kt. At each weekly MP1 refresh, use the last 126 qualified Q observations strictly before refresh and let M_kt be their exact median, carried until the next refresh:

`MP1_kt=log(Q_kt/M_kt)`. [S5,S8; K4]

Both numerator and reference require C04/C05/identifier/PIT qualification and finite positive ratio. No current observation enters its reference, no calendar-day fallback and no shortened window. Source-channel MP1 uses source security i. Missing MP1 remains unavailable.

## 4. Explicit eligibility and direction

For evidence dimension d, retain bits `(p_d,u_d)`: (0,0)=qualified absence, (1,0)=present, (0,1)=unavailable, (1,1)=invalid. Let `ValidBits=product_d 1{p_d+u_d≤1}`. A missing record is not automatically (0,0). [S6]

Define the required-data predicate

`V_cijt = Authorized_c,t * PairEligible_p,t * PIT_cijt * ID_cijt * ResponseOK_it * ResponseOK_jt * RegressorsOK_cpt * HistoryOK_cpt * FitOK_cpt * A3OK_cijt * ValidBits_cijt`,

where every factor is Boolean: authorization fixes candidate/fold; PairEligible implements PAIR-A; PIT requires all input availabilities by signal and fit/reference observations strictly prior; ID requires unambiguous frozen identifier lineage; ResponseOK implements section 2's complete qualification; RegressorsOK requires every regressor; HistoryOK requires full H/U; FitOK requires supported rank/covariance and convergence; A3OK requires both finite directional predictions/departures and supported positive finite required scales. [S1–S8]

Let R,B,D,Cf,F denote positive M0 rejection, break, mechanical/data invalidity, observable unresolved directional/mechanism conflict, and future leakage evidence. Then

`K=(1−p_R)(1−p_B)(1−p_D)(1−p_Cf)`,

`J_P(c,i,j,t)=V*K*NZ(mu_j|i,t)*NZ(g_i→j,t)*Fin(UR0_i→j,t)*1{UR0_i→j,t>0}`,

`J_S(c,i,j,t)=V*K*(1−p_F)*NZ(e_i→j,t)*NZ(MP0_i→j,t)*MP1Available_it*Fin(MP1_it)*1{MP1_it>0}`. [S4–S8]

Unavailable *mechanism* evidence is annotated unavailable, not forced negative and not an automatic universal no-trade rule under the morphology-only descendant. Unavailable required data, identifiers, PIT qualification or MP1 does fail V/the specified gate. U5 dimensions remain separate, not a score. Unavailable uncertainty is not made into positive evidence.

`S_peer(c,i,j,t)=sign(g_i→j,t); traded security=j; other-leg shares=0`,

`S_source(c,i,j,t)=−sign(e_i→j,t); traded security=i; other-leg shares=0`. [S4,S8]

Let Active_cph,t indicate an already admitted episode for that candidate/pair/channel (including an exit pending execution). The final signal indicators are

`I_peer=J_P(c,i,j,t)*(1−Active_cpP,t)*(1−J_P(c,j,i,t))*1{S_peer=+1}`,

`I_source=J_S(c,i,j,t)*(1−Active_cpS,t)*(1−J_S(c,j,i,t))*1{S_source=+1}`. [S7,S8]

DECA-A rejects both raw eligible opposite directions **before** applying short executability. A disallowed short does not rescue its conflicted opposite signal. EP-A suppresses a new signal while its episode is active; a next-open exit does not retrospectively create a prior-close signal. Peer and source channels can coexist. These are pair-conditioned **single-security** positions, not two-leg spreads: there is no simultaneous short of the conditioning security, market hedge or beta hedge. Negative theoretical directions are EXECUTION UNAVAILABLE, not reversed into long trades.

## 5. Entry and exact simultaneous allocation

Let sigma_t be the signal timestamp, no earlier than close z_t and the availability of every required signal input. The only entry opportunity is the immediately next scheduled exchange-session open o_{t+1}, with `sigma_t<o_{t+1}`. Let PairAdmissionOK_e(o) mean all frozen pair/directional admission requirements still hold using information available by o, including both members' required eligibility and the frozen signal's validity. It neither uses the future close nor refits the origin. Define Qentry_e(o) as PairAdmissionOK_e(o) AND finite positive observed raw open AND valid identifier AND qualified C04 signal/execution interval AND known executable/non-suspended state. Then

`tau_entry,e = o_{t+1}` if `I_h=1 AND Qentry_e(o_{t+1})=1`; otherwise no entry. [S1,S6,S8,S12]

There is no search for a later entry, carry-forward or close-price fallback. Thus 'next qualified open' does not authorize skipping an unqualified first entry opportunity. Exits have a different delay rule.

At open o, process qualified exits first. Let Eminus be previously active episodes, X the episodes with pending exit executable now, and Es=Eminus\X the survivors. Failed/pending exits remain in Es. Form the complete proposal set Bset from prior signals passing Qentry. Define

`A=|Es|; B=|Bset|; N=A+B; x_raw=V_pre/N` for B>0. [S9]

Every proposal gets the same raw target. B is counted before funding allocation, so proposals later assigned zero remain in B. No A+1 sequential rule or proposal priority is permitted.

With n_e the previously executed episode shares and O_ko the qualified current open, define

`H_k=sum_{e in Es:k_e=k} n_e O_ko; X_k=sum_{e in X:k_e=k} n_e O_ko`,

`V_pre=C_minus+sum_k(H_k+X_k); C_0=C_minus+sum_k X_k`. [S8,S9; K5]

V_pre is before the simultaneous net execution's fee. Exit proceeds are available at this event; costs are charged once on net security execution, not once on gross exits and again on netting. V_pre must be finite and positive.

Let b_k count proposals trading k; d_k=b_k*x_raw is their combined raw request. For each security,

`cap_k=max(0,0.10*V_pre−H_k); z_k=min(d_k,cap_k); Z=sum_k z_k`,

`G_remaining=max(0,V_pre−sum_k H_k); lambda_G=min(1,G_remaining/Z)` when Z>0. [S8,S9]

Security-specific reduction is proportional among identical raw contributors to that security. No released capacity is redistributed. For lambda in [0,lambda_G],

`F(lambda)=C_0−lambda*Z−kappa*sum_k |lambda*z_k−X_k|`,

`lambda_star=max{lambda in [0,lambda_G]: F(lambda)≥0}`,

`x_e=lambda_star*z_{k_e}/b_{k_e}`. [S8,S9; derived K5]

Zero Z means zero admissions; costs on exits still apply. An empty feasible set is an unqualified accounting state, not authorization to resize survivors. For Z>0 and kappa<1, F is continuous strictly decreasing: solve its piecewise-linear root at breakpoints X_k/z_k inside the feasible interval, or use lambda_G if feasible. This is a deterministic feasibility equation, not a parameter search. K5 rounds a floating root toward feasibility if representation alone makes cash negative. No numerical materiality threshold is introduced.

If x_e=0, record FUNDING UNAVAILABLE with no position, turnover, exposure, fabricated fill or delayed admission. Otherwise episode shares are `n_e=x_e/O_k_e,o`. Existing episodes keep their previous shares. Aggregate security shares and actual net orders are

`n_k,plus=sum_{e in Es:k_e=k} n_e + sum_{e in Bset:k_e=k} x_e/O_ko`,

`Delta n_k=n_k,plus−n_k,minus; TC_o=kappa*sum_k O_ko*|Delta n_k|`,

`C_plus=C_minus−sum_k O_ko*Delta n_k−TC_o=F(lambda_star)`. [S8,S9]

Use fractional research shares; no invented lot, financing, settlement or borrow model. Sorting for reproducibility cannot affect allocations. Each of six candidates has three independent cost paths (5/10/20 bps; 10 primary); costs affect feasible admissions, so the sensitivity books are not obtained by subtracting different fees from one shared holdings path.

The complete same-open order is: qualified exits → survivors → complete proposal batch → A,B,N → identical raw targets → security aggregation/caps → remaining gross capacity → actual net cost/cash feasibility → simultaneous net security execution → subsequent qualified close valuation and exit-trigger evaluation. [S9]

## 6. Holding evolution and stopping times

For an active episode between entry and executed exit, `n_e(q+)=n_e(q−)` unless a separately qualified mandatory corporate-action/accounting adjustment applies. Exit sets n_e to zero; a new entry initializes n_e as above. No count, NAV, price movement or unrelated entry/exit generates a survivor target. This is **equal admission sizing**, not equal active-portfolio weighting. [S8,S9]

A qualified action may apply an explicitly established share factor f and cash entitlement d per eligible share: `n_plus=f*n_minus; C_plus=C_minus+d*n_entitled`. This states the accounting form, not authority to invent f,d, entitlement timing or reinvestment. Without qualified treatment, the affected interval is unavailable under C04/T09. [S1,S8]

Keep the original signal anchor a_e=g_i→j,t_e for peer, or a_e=e_i→j,t_e for source. Let

`Delta_e(q)=sum_{s=t_e+1}^{q} y_k_e,s`,

`R_e(q)=a_e−Delta_e(q)` for peer; `R_e(q)=a_e+Delta_e(q)` for source. [S4,S8]

These are sums of qualified simple responses, not compounded returns or newly fitted anchors. An unknown required interval makes Delta unavailable; it cannot be skipped, filled by zero or bridged. Entry does not reset the signal anchor.

After admission let k_e be the held security (j for peer, i for source). Define Boolean predicates at session q, using only then-available information:

- ID_e(q): held-security identity/lineage is qualified and continuous.
- CA_e(q): the held episode's relevant interval satisfies frozen C04/T09 exclusion or separately qualified entitlement accounting; unresolved does not mean clean.
- HOLD_e(q): held-security session status satisfies the frozen holding-session qualification, including known C05 state; it is not inferred from counterparty status.
- VAL_e(q): the required held-security valuation price is observed, finite, positive and qualified; no synthetic mark.
- RESP_e(q): the held-security response required by the clock/resolution obeys section 2's frozen qualification (including qualified endpoints); an unknown/suspended bridge is not filled or counted.

Then the closed held-security clock and resolution-decision set are

`ell_e(q)=1{q≥u_e}*ID_e(q)*CA_e(q)*HOLD_e(q)*VAL_e(q)*RESP_e(q)`,

`T_e={q≥u_e: ell_e(q)=1 AND OriginValid_e AND Fin(Delta_e(q))}`. [S1,S8,S12]

OriginValid_e means the episode was validly admitted with a finite nonzero original anchor and preserved origin lineage. It is fixed at admission, not a renewed model-fit or counterparty test. Required-data unknowns remain explicitly unavailable even though their eligibility indicator is zero. In particular, a zero clock increment does not turn a missing held-security response into a zero response or restore a broken cumulative/accounting chain.

There is **no post-entry counterparty eligibility factor** in ell, T, held-security valuation or Qexit. Full pair eligibility remains mandatory for any new signal/admission. Changing only the untraded counterparty state while holding all required held-security inputs fixed leaves ell, T, R, the anchor, identity, direction and holding clock unchanged. No model/state refresh is performed for the existing episode. With u_e the actual entry session,

`L_e(q)=sum_{s=u_e}^{q} ell_e(s)`,

`theta_zero,e=inf{z_q: q≥u_e, q in T_e, Fin(R_e(q)), a_e*R_e(q)≤0}`,

`theta_10,e=inf{z_q: q≥u_e, q in T_e, L_e(q)≥10}`,

`theta_e=min(theta_zero,e,theta_10,e)`. [S1,S8,S12]

Infimum of the empty set is infinity. Entry session counts as session one when eligible. The boundary includes exact zero; there is no tolerance, new convergence percentage or near-zero rule. Triggers are observed at close, never traded at that same close.

Let Qexit_e(o) require the held security's qualified observed finite positive executable open, known tradable status, qualified corporate-action accounting and identifier state. It does not require renewed pair eligibility or current counterparty data. Then

`tau_exit,e=inf{o_s: o_s>theta_e, Qexit_e(o_s)=1, s within the same fold}`. [S1,S8,S12]

Known suspension/untradeability leaves an exit pending until the first qualified open, with no newly imposed maximum delay. Unknown intervals are economically unevaluable, not assumed tradable or flat-return. Pending exit episodes remain active for EP-A. At fold end, no fabricated liquidation and no cross-fold episode: use a qualified terminal mark and disclose open episodes; unavailable terminal valuation makes the corresponding metric unavailable. Each independent fold starts NAV 1 and cash 1. [S8]

## 7. Portfolio accounting, qualification and metrics

At a qualified close q,

`V_q=C_q+sum_k n_kq P_kq; w_kq=n_kq P_kq/V_q`,

`Gross_q=sum_k |w_kq|; Net_q=sum_k w_kq; CashWeight_q=C_q/V_q`. [S8,S10]

These books are long-only, so gross and net coincide when defined; no neutrality optimization or leverage above the admission gross cap is implied. Cash earns zero. Passive drift diagnostics are `1{max_k |w_kq|>0.10}` and `1{Gross_q>1}`. Drift alone does not trigger a sale or create entry capacity. Report actual overlap `Overlap_kq=sum_active_e 1{k_e=k}` and peer/source coexistence `1{active peer count>0 AND active source count>0}`. [S8,S9]

Define Qecon_q as the conjunction of qualified needed prices, identity continuity, executable fills, complete cash/share entitlements and C04 accounting coverage over the affected portfolio interval. Define chain qualification `Qchain_q=product_{s≤q} Qecon_s`. [S1,S8]

If either is false, the affected portfolio interval/chain is unavailable. Do not drop affected holdings, renormalize survivors, substitute adjusted prices, reset NAV or treat no identified action as exhaustively action-clean. A positive action without qualified entitlement treatment is excluded/unavailable; an unresolved effective date or coverage gap remains unresolved. Thus input availability is not a new trading-policy choice.

For a complete qualified independent fold with n sessions and V_0=1, define r_q=V_q/V_{q−1}−1, rbar=mean_q r_q, and s_r=sqrt(sum_q(r_q−rbar)^2/(n−1)). Then

| Metric | Exact formula and ancestry |
|---|---|
| Session return | `r_q=V_q/V_{q−1}−1`, after actual costs [S8] |
| Cumulative net return / net PnL | `prod_q(1+r_q)−1=V_n/V_0−1`; `PnL_net=V_n−V_0` [S8,S10] |
| Annualized return | `(V_n/V_0)^(252/n)−1`, n>0 and supported positive NAV [S8] |
| Annualized volatility | `sqrt(252)*s_r`, n≥2 [S8] |
| Sharpe | `sqrt(252)*rbar/s_r`, n≥2 and s_r>0; zero risk-free/cash convention [S8,S10] |
| Maximum drawdown | `max_{0≤q≤n}(1−V_q/max_{0≤s≤q}V_s)` [S8,S10] |
| Event/fold turnover | `T_o=sum_k O_ko*|Delta n_ko|/V_pre,o`; fold `sum_o T_o` [S10; K4] |
| Net security trade count | `sum_o sum_k 1{Delta n_ko≠0}` [S8; explicit counting object] |
| Episode counts | Entries `sum_e 1{x_e>0}`; executed exits `sum_o |X_o|`; terminal open episodes `|E_terminal|` [S8] |
| Exposure diagnostics | Gross, Net, CashWeight, security weights, cap-drift flags, overlap and channel coexistence as above [S8,S9] |
| Raw executed-path PnL | `PnL_raw=PnL_net+sum_o TC_o`; this is the same holdings path before charged fees, not a separate zero-cost counterfactual strategy [K4; S8 raw/net reporting] |

Undefined quantities are unavailable, not zero or infinity. There is no new cross-fold compounding rule, channel fee-allocation rule, significance threshold, winning-book selection or cost sensitivity optimization. Report peer/source/coexistence and execution-/funding-unavailable opportunity counts separately. Do not conflate security trades, episodes and signals. [S8]

## 8. Compact implementer pipeline

`D_t → mu → a,g,e,UR0,MP0,MP1 → I_peer,I_source → S → proposal batch → x_e → n_k → theta,tau_exit → V → PnL`.

1. For each frozen candidate, fold and kappa, initialize cash/NAV 1, no holdings. Build only qualified PIT response histories (section 2). Refresh the specified OLS/two-stage/REML equations at U with H prior observations; evaluate the directional response using current-close conditioning inputs.
2. Consume immutable A3 departures/scales with their precision lineage; compute gap/excess, UR0 and prior-H126 weekly log-ratio MP1 (section 3). Do not substitute the A1 loss layer.
3. Evaluate every Boolean factor in section 4. Apply raw-direction DECA conflict, active-episode EP-A, then long-only executability. Keep diagnostic reasons for unavailable/rejected/short opportunities. Save original anchors and signal timestamp.
4. At the sole immediate next-open entry opportunity, qualify execution. Execute eligible pending exits, preserve survivors, construct the entire qualified batch, count N=A+B, and allocate by the security-cap then maximal common cash/gross-feasible factor in section 5. Convert positive notional to shares; zero allocation is funding unavailable. Net at security level and charge kappa once.
5. Carry survivor shares and origin state unchanged. At each close, increment the clock by ell_e(q) from section 6; only held-security qualification enters this predicate. Evaluate original-anchor residuals on T_e and the two stopping times. Counterparty-only loss changes neither the existing episode nor its clock, but still blocks new admissions requiring that counterparty. Execute pending exits at the first subsequent held-security qualified open; preserve unresolved intervals as unavailable.
6. Apply only qualified accounting adjustments, value holdings plus cash, and compute section 7 metrics only on complete qualified chains. At fold end mark without invented liquidation and disclose remaining episodes. Never use output performance to alter a preceding step.

Steps 1–6 plus the symbol definitions are the complete mathematical algorithm; S12 closes the former G1 choice. They do not authorize an empirical run, data correction or code repair. Code conformity and input qualification remain separate gates.

## 9. MATHEMATICAL COMPLETENESS AUDIT

| Required component | Classification | Audit conclusion |
|---|---|---|
| Candidate identities, H/U, directional OLS and representation/bridge distinction | FULLY SPECIFIED | Six books; no R4 or implicit spread |
| R1 residualization and R3 REML/BLUP | FULLY SPECIFIED | Later S3 industry-origin amendment controls; code conformance must be checked, not chosen by PnL |
| PIT membership, response/identifier/C04/C05 qualification | DATA-DEPENDENT BUT NOT POLICY-DEPENDENT | Missing evidence cannot be fabricated |
| A3/g/e/UR0/MP0; preserved native-scale lineage | FULLY SPECIFIED | S8/S11 preserve objects; do not call them the amended A1 scale |
| MP1 ratio/log/reference | FULLY SPECIFIED | Later S8 ratio-log binding controls over older amount-only descriptions |
| Evidence bits, positive blocking gates, missing mechanism evidence | FULLY SPECIFIED | Required data unknown differs from mechanism evidence unavailable |
| Boolean eligibility, EP-A, DECA-A, long-only directions | FULLY SPECIFIED | Order and channel identities explicit |
| Immediate next-open entry and raw execution price | FULLY SPECIFIED | No delayed entry or close fallback |
| Simultaneous N=A+B and Option-A survivor priority | FULLY SPECIFIED | No sequential admission or survivor resizing |
| Security-cap proportional allocation and common cash/gross root | DERIVABLE FROM FROZEN RULES | Exact order-invariant equations; no redistribution |
| Shares, passive drift, net execution costs, cash | DERIVABLE FROM FROZEN RULES | No additional rebalancing, leverage or funding policy |
| Original anchors, zero crossing, entry-inclusive ten count | FULLY SPECIFIED | Boundary is exactly zero, count is exactly ten |
| Eligibility predicate for holding count/exit decision after counterparty-only eligibility loss | FULLY SPECIFIED | S12: held-security predicates only after valid pair admission; no reset or refreshed anchor |
| Known suspended exit delay, unknown interval, terminal mark | FULLY SPECIFIED | Pending exit; unavailable unknowns; no fabricated liquidation |
| Corporate-action entitlements and qualified prices | DATA-DEPENDENT BUT NOT POLICY-DEPENDENT | No new entitlement/acquisition/repair authorized |
| NAV, returns, 252 annualization, sample SD, Sharpe, drawdown, turnover | FULLY SPECIFIED | Mathematical domains and unavailability explicit |
| Trade/episode/exposure/coverage counters | DERIVABLE FROM FROZEN RULES | Distinct counting objects; not one ambiguous count |
| 5/10/20 bps separate paths and independent folds | FULLY SPECIFIED | No ex-post cost/path or winner selection |

### G1 — resolved by explicit researcher decision S12

The researcher selected held-security post-entry eligibility. Section 6 now binds ell_e(q) and T_e without an untraded-counterparty term. Full pair/directional eligibility at signal and admission is retained in sections 4–5. A5 outcome eligibility is not substituted for the trading clock. Unknown held-security accounting/response intervals remain unavailable; no anchor, identity, direction or clock reset is introduced.

Rerun audit result: **zero remaining MISSING / RESEARCHER DECISION REQUIRED mathematical policy components** in the defined strategy. Fully specified rules, their deterministic derivations, and data-dependent qualification requirements are distinguished in the table. This conclusion does not declare existing code conformant or data sufficient. No alternative is left open at G1 and no ordinary sizing/accounting decision is reopened.

### Implementation conformance findings — not new policy questions

Source-only inspection identifies matters requiring a later separately authorized conformance pass, not silent repair in this task:

- K1 indexes historical MI leg industry at s, while later S3 binds g(k,t) at the decision origin. Equality cannot be presumed across industry changes. No input values were inspected to measure its incidence.
- K1 global-period fit/cache refresh may not instantiate 'first candidate-eligible session' for a pair first eligible later in the week/month. K2's stratum cache also needs explicit taxonomy-version binding against S3. Do not assume numerical equivalence without proof.
- K1's three-regressor solver has a determinant cutoff `1e-30`; the frozen rank contract is not permission to introduce an arbitrary new near-singularity scientific rule. This audit records the distinction without changing it.
- K4's signal function does not explicitly receive all observable rejection/PIT/conflict dimensions in section 4. Upstream validity requires demonstrated field-level lineage; morphology-only numeric validity is not itself proof that every gate was applied.
- K4's handling of non-normal held open states does not itself demonstrate the complete known-suspension pending-exit contract. T09 unavailability must not be conflated with an authorized synthetic exit.
- A3 stored float32 anchors versus A5 internal precision, and legacy A3 native scales versus the separate H126 A1 scale, must remain explicitly distinguished. No payload rewriting or A1 substitution is authorized.

None of these findings was resolved using market values, PnL or candidate performance. They do not authorize refitting, recomputation or correction of frozen payloads. Existing empirical history and frozen tags remain untouched.

**TRADING V1.1 MATHEMATICALLY COMPLETE / RESEARCHER APPROVAL REQUIRED**

C04 correction, trading execution, PnL access and V2 remain paused. Approval of the assembled specification is still required. Implementation/data corrections and any execution would require explicit bounded authorization; the completeness finding does not grant it.
