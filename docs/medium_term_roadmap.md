# Medium-Term Research Roadmap: Pinned Pendulums Extension Plan

*Document status: working roadmap — v1.0, June 2026*  
*Builds on: `empirical_design.md`, `data_sources.md`, `literature.md`, and panel review synthesis*

---

## Overview

The current state-year panel (N = 51 states × T ≈ 15 years) has returned its most important result cleanly: organized parent opt-out mobilization could **not** translate into accountability policy rollback in states bound by active ESEA waivers (β = −0.128, p = 0.014). That result, and the theoretical conditional feedback model that generates it, are publishable. But the design also ran into two hard limits that the panel reviewers identified with precision:

1. **Statistical power.** With effective N ≈ 30–38 after clustering, the MDE at 80% power is β ≈ 0.17–0.20. The H1 null (β = −0.105) falls inside the undetectable zone. We cannot distinguish "no thermostatic effect" from "a real but small effect" at this sample size. The district-level extension provides the power to resolve that ambiguity.

2. **The waiver is not the only friction.** The compliance commitment mechanism story is compelling for the ESEA waiver window (2011–2017), but it leaves open the broader theoretical question: how fast does correction operate when the lever *is* genuinely free — when no federal compliance contract blocks rollback? COVID-era school closures are the natural test case: the CDC issued guidance, not law; union contracts were the relevant friction; and rollback pressure was extreme, highly visible, and immediate.

This roadmap covers the two empirical extension tracks that flow from these limits, plus the literature expansion program needed to ground the theory in five additional scholarly conversations.

**Two empirical tracks. One literature program.**

| Track | Core question | Design | Estimated time to first results |
|---|---|---|---|
| **1: District-Level Panel** | Does within-state variation in pre-waiver evaluation intensity predict differential policy response post-ESSA? | DiD on ~13,000 district-years | 14–18 months |
| **2: COVID School Closures** | Does closure→rollback move faster when no binding federal lock-in exists? | Synthetic DiD, state-year 2019–2023 | 10–14 months |
| **3: Literature Expansion** | Five thematic buckets to deepen theoretical grounding | Systematic search + integration | Ongoing; 3–6 months for initial pass |

> [!IMPORTANT]
> **Pre-register Track 1 before opening any district data.** The CFA failure on the composite accountability index at the state level is a warning. The district panel must have its measurement and estimation strategy fully locked before data analysis begins.

---

## Track 1: District-Level Panel Extension

### 1.1 Rationale

The state-year design was the right starting point — states are the relevant institutional unit for ESEA waiver compliance — but it bottoms out at N = 51. After accounting for state fixed effects, year fixed effects, and clustered standard errors, the effective sample shrinks to roughly 30–38 independent units of variation. That is barely sufficient to detect medium-to-large effects, and insufficient to detect effects in the β ≈ 0.10–0.15 range that are substantively meaningful for education policy.

The district-level extension solves this by moving the unit of observation to the school district, exploiting within-state variation that the state-year panel was unable to use. There are approximately 13,000 districts with non-trivial data coverage, yielding a district-year panel of roughly 130,000–156,000 observations over a 10–12 year window (2010–2022, with COVID years handled separately).

**What district-level data can test that state-level cannot:**

| Question | State panel | District panel |
|---|---|---|
| Does thermostatic feedback exist at all? | MDE too large to detect small effects | MDE shrinks dramatically; β ≈ 0.03–0.05 detectable |
| Does pre-waiver evaluation intensity predict post-ESSA rollback? | N = 51 variation; limited | Within-state variation across ~600 districts per state |
| Did "always-compliant" districts behave differently from "newly constrained" districts? | Untestable — variation is between states | Core DiD contrast |
| Do union contract provisions moderate the compliance commitment effect? | Rough state-level proxies only | Contract-level variation by district |
| Do school board election dynamics mediate the mechanism? | Board outcomes unobservable at state level | Ballotpedia district-level results available |

**Statistical power comparison:**

Using the ICC ≈ 0.35 from the state panel, and assuming a similar within-group correlation structure, the district panel achieves:
- MDE ≈ 0.03–0.05 at 80% power (vs. 0.17–0.20 for the state panel)
- This is sufficient to detect not just the headline H7b effect but also the H1 null's true parameter estimate
- Non-linear interaction terms (H2, H4, H6) become confirmatory rather than exploratory

---

### 1.2 Identification Strategy

**Core design:** Difference-in-Differences (DiD) exploiting within-state, across-district variation in pre-ESEA-waiver teacher evaluation intensity.

**Treatment variation — the key insight:**  
ESEA waivers (2011–2015) required states to adopt teacher evaluation systems incorporating student growth measures (primarily VAM). But this requirement fell differently on different districts within the same state:

- **"Always-compliant" districts:** Districts that had already implemented robust teacher evaluation systems (annual evaluation, multi-level ratings, professional development linkage) before the waiver era. For these districts, the waiver-mandated VAM addition was a marginal change to an existing system. The federal compliance commitment mechanism imposed *minimal additional friction* — they were already close to compliance.

- **"Newly constrained" districts:** Districts with weak or absent teacher evaluation infrastructure before 2011. For these districts, the waiver mandate required building entire evaluation systems from scratch. The compliance commitment mechanism imposed *maximal friction* — rolling back VAM post-ESSA meant dismantling a system they had just been forced to build.

**The prediction:**  
Post-ESSA, when states recovered design authority, "newly constrained" districts should show *more* policy correction (greater rollback of VAM/test-score-linked evaluation, greater adoption of alternative metrics) than "always-compliant" districts — because they had more to undo and stronger implicit grievance about the imposition.

**Identification assumption:**  
Conditional on district fixed effects (absorbing time-invariant district characteristics) and year fixed effects (absorbing national policy shocks common to all districts), differences in pre-waiver evaluation intensity across districts *within the same state* predict differential response to the same waiver shock for reasons related to implementation burden, not to pre-existing differences in district politics, partisanship, or demographics.

**Plausibility of the assumption:**
- The identifying variation is *within-state* — state political environment, state DOE capacity, governor party, and state union contracts are all absorbed by state × year interactions (or state FE if estimating within a state-level model).
- The key threat is selection: districts that had stronger pre-waiver evaluation systems may differ systematically from those that did not on unobserved dimensions (e.g., district administrator capacity, local political appetite for reform, union strength). These concerns are partially addressed by including district-level controls (per-pupil spending, union density, poverty rate, racial composition, district size) and by testing for pre-trends.
- The strongest falsification test: estimate the DiD with *placebo* pre-periods (2008–2010 vs. 2011–2014). If "always-compliant" vs. "newly constrained" differences exist *before* the waiver shock, the identification assumption is violated.

**How this improves on the state-level identification:**  
The state-level design compared states with more vs. less intensive pre-ESSA accountability systems, but those states differ on partisanship, geography, and demographics in ways that are correlated with both accountability intensity and correction speed. The district design holds the state political environment constant — the "treatment" is relative evaluation intensity within a state, not between states. This is a much cleaner comparison.

---

### 1.3 Data Collection Plan

> [!IMPORTANT]
> Estimated total data collection effort: **6–9 months** for a two-person team. Sources 1–4 are the critical path items; Sources 5–7 are the power-boost and heterogeneity items.

#### Source 1: District Opt-Out Rates

| Field | Detail |
|---|---|
| **Source** | EDFacts District Assessment Participation Data (U.S. Department of Education) |
| **URL** | https://www.ed.gov/data/edfacts |
| **What it provides** | District-level participation rates in state summative assessments (grades 3–8), by subgroup; annual, 2010–present |
| **Access** | Public; downloadable as CSV from the EDFacts Data Files portal. Requires registration but no FOIA. |
| **Key variables** | Participation rate (%) by district-year-grade-subgroup; non-participation rate = opt-out proxy |
| **Estimated effort** | **Low-medium.** Files are structured but require year-by-year merging (file format changed in 2015 and 2018). Allow 3–4 weeks for download, format harmonization, and merge with NCES Common Core of Data district IDs. |
| **Notes** | This is the district-level analogue to the state opt-out rate already in the current panel. It serves as both an outcome variable (Did districts with higher pre-waiver friction show higher opt-out rates?) and a backlash proxy (Did high opt-out districts push more post-ESSA correction?). |

#### Source 2: Pre-Waiver Teacher Evaluation Scores by District

| Field | Detail |
|---|---|
| **Source** | State Department of Education microdata (varies by state) |
| **URL** | Varies; contact state DOE research offices directly |
| **What it provides** | Distribution of teacher evaluation ratings (Highly Effective / Effective / Developing / Ineffective) by district-year; in some states, VAM scores at the teacher or classroom level |
| **Access** | **Mixed.** Approximately 15–20 states post evaluation summary data publicly (FL, TN, MA, NJ among the most complete). The remaining states require FOIA requests or data use agreements. Some states (e.g., NY) have released restricted-use data to researchers under IRB agreements. |
| **Estimated effort** | **High.** This is the most labor-intensive source. Plan for: (a) 3–4 weeks to catalog all 51 state data availability statuses; (b) 6–8 weeks for FOIA requests in non-public states; (c) 4–6 weeks for harmonization (rating scales differ across states). Prioritize the 15–20 states with public data for a first-pass analysis; expand via FOIA in Year 2. |
| **Notes** | This is the **key independent variable** — pre-waiver evaluation intensity by district. A summary measure of the proportion of teachers rated Highly Effective or Effective in 2010–2013 (pre-waiver mandate) serves as the "always-compliant" proxy. Districts with high pre-waiver HE/E rates had more prior infrastructure; districts with compressed distributions had less. |

#### Source 3: School Board Election Outcomes

| Field | Detail |
|---|---|
| **Source** | Ballotpedia School Board Elections; state election offices |
| **URL** | https://ballotpedia.org/School_board_elections |
| **What it provides** | Candidate names, incumbency status, win/loss, ideological self-description, contested vs. uncontested races; 2010–present |
| **Access** | **Partially public.** Ballotpedia covers major districts comprehensively; small rural districts are sparsely covered. State election offices have official results but rarely in machine-readable form. Expect significant web scraping + manual coding for small/mid districts. |
| **Estimated effort** | **Medium-high.** For a national panel, scraping Ballotpedia and standardizing to district IDs will take 4–6 weeks of scripted collection plus 2–3 weeks of manual validation. For a state-specific subsample (e.g., Florida, Texas, New York, Pennsylvania — states with comprehensive coverage), this can be done in 2–3 weeks. |
| **Key variables** | Incumbent defeat rate by district-year; presence of explicitly reform-skeptic candidates; change in board ideological composition index. |
| **Notes** | School board election outcomes serve as a secondary *outcome* variable and as a *mediator* test: Did opt-out mobilization translate into board turnover, and did board turnover predict post-ESSA policy correction at the district level? This is the institutional mechanism the state-level panel could not test directly. |

#### Source 4: District-Level ESSA Plan Weights

| Field | Detail |
|---|---|
| **Source** | State DOE ESSA Consolidated Plan documents; CCSSO ESSA implementation tracker |
| **URL** | https://www.ed.gov/essa/implementing/plans/index.html; https://ccsso.org/ |
| **What it provides** | State-level accountability indicator weights (test scores, growth, chronic absenteeism, graduation rate, etc.) as filed with USDE; district-level variation where states delegated indicator weight flexibility to LEAs |
| **Access** | **Partially public.** ESSA state plans are public PDFs. District-level variation exists in ~15–20 states that gave LEAs some design flexibility (e.g., Connecticut, California, Colorado). These states are the most informative for within-state DiD. |
| **Estimated effort** | **Medium.** For the 15–20 states with district flexibility, plan coding takes approximately 2–3 weeks per state for a trained coder using a pre-registered coding instrument. Total: 10–15 weeks for the full 20-state subsample. Remaining states contribute only state-level ESSA plan data (already partly coded in the current project). |
| **Key variables** | Test-score weight (%) in state accountability formula at district level; binary: A-F school rating system retained vs. dashboard adopted; number of non-test indicators in district accountability plan. |

#### Source 5: Union Contract Provisions by District

| Field | Detail |
|---|---|
| **Source** | NEA state affiliate data; District union contracts (public records); National Council on Teacher Quality (NCTQ) |
| **URL** | https://www.nea.org/; https://www.nctq.org/contract-database |
| **What it provides** | Teacher evaluation procedure language in collective bargaining agreements: who controls evaluation criteria, how VAM scores factor into evaluation, grievance procedures for evaluation disputes |
| **Access** | **Mixed.** Teacher CBAs are public records in most states. No national database; contracts must be requested district-by-district. NCTQ has collected CBAs for the largest ~200 districts. |
| **Estimated effort** | **Medium for large districts; high for full panel.** NCTQ covers the largest 200+ districts comprehensively — sufficient for a first-pass analysis of major urban districts. For a full 13,000-district panel, CBA collection is intractable; focus on a stratified subsample of ~500 districts covering full variation in size, geography, and union density. Allow 4–6 weeks to compile and code the NCTQ database plus 2–3 weeks for stratified subsample FOIA requests. |
| **Key variables** | Binary: Does the CBA explicitly restrict use of VAM in evaluations? Ordinal: 0–3 scale of union veto power over evaluation criteria. Continuous: number of grievance provisions addressing evaluation. |

#### Source 6: SEDA District-Level Achievement Data

| Field | Detail |
|---|---|
| **Source** | Stanford Education Data Archive (SEDA), Harvard Center for Education Policy Research (CEPR) |
| **URL** | https://edopportunity.org/ (SEDA); https://dataverse.harvard.edu/ (bulk download) |
| **What it provides** | District-level standardized test score trends (math and reading, grades 3–8), 2008/09–2019; standardized to NAEP scale for cross-state comparability; demographic covariates |
| **Access** | **Free public download** from Harvard Dataverse. No registration required. |
| **Estimated effort** | **Low.** Download takes 1–2 hours; merging with district identifiers (NCES LEAID) takes 1–2 days. The key challenge is the 2019 endpoint — coverage does not extend through the full ESSA implementation period. Plan to supplement SEDA with state assessment data from EDFacts for 2019–2022. |
| **Key variables** | Mean test score (standardized), test score trend slope, achievement gap by subgroup — all at district-year level. Used as outcome validator and as a control for pre-existing achievement trajectories. |

#### Source 7: CRDC District-Level Civil Rights Data

| Field | Detail |
|---|---|
| **Source** | Civil Rights Data Collection (CRDC), U.S. Department of Education Office for Civil Rights |
| **URL** | https://www2.ed.gov/about/offices/list/ocr/data.html |
| **What it provides** | District-level data on: school discipline rates (suspension, expulsion by race), referrals to law enforcement, restraint and seclusion, enrollment by race/disability/ELL status |
| **Access** | **Free public download.** Biennial collection (2011–12, 2013–14, 2015–16, 2017–18, 2020–21). |
| **Estimated effort** | **Low.** Files are large (1M+ rows) but well-structured; merge with NCES LEAID is straightforward. Allow 2–3 weeks for download, merge, and documentation of data quality flags. The biennial cadence requires interpolation for odd years if the panel requires annual observations. |
| **Key variables** | Suspension rate by race/grade/district-year (discipline policy intensity proxy); chronic absenteeism rate; ELL enrollment share (diversity proxy for accountability design pressure). |

---

### 1.4 Outcome Variables

**Primary outcome: District policy change (ΔPolicyIntensity post-ESSA)**

Measured as the change in district-level accountability intensity between the pre-ESSA period (2010–2016) and the post-ESSA period (2017–2022). The core operationalization mirrors the state-level policy intensity index but adapted for district-level implementation:

1. **District test-score weight in accountability formula** (from ESSA plan data for LEA-flexibility states; state-mandated weight otherwise)
2. **Teacher evaluation VAM linkage** (from CBA and state administrative records): Does the district still use student growth data in summative teacher evaluations post-ESSA?
3. **Opt-out rate trend** (from EDFacts): Is the district's opt-out rate rising (continued mobilization) or falling (correction underway)?

The ΔPolicyIntensity outcome is the difference between the district's post-ESSA policy score and its pre-ESSA policy score, normalized by state year-effects (within-state demeaned). A negative value means the district moved away from test-centric accountability; a positive value means entrenchment or continued intensification.

**Secondary outcomes:**

| Outcome | Operationalization | Source |
|---|---|---|
| School board election turnover | Incumbent defeat rate (district-year) | Ballotpedia, state election offices |
| Opt-out rate trend | Δ participation rate, year-over-year (district-year) | EDFacts |
| Board ideological shift | % of newly elected members with explicit reform-skeptic platform | Ballotpedia coded text |
| Achievement trajectory | SEDA score trend slope, pre vs. post-ESSA | SEDA / EDFacts |

**Measuring 'policy implementation intensity' at district vs. state level:**

At the state level, the policy intensity index captured statewide statutory and regulatory choices (A-F grading, third-grade retention laws, teacher evaluation statutes). At the district level, the relevant measure shifts to *implementation* intensity — the degree to which the district's actual practices (evaluation instruments used, proportion of teachers rated on VAM, etc.) track state mandates. This distinction matters theoretically: a "newly constrained" district that was forced to build a VAM system may have implemented it superficially (low actual intensity) even under high nominal state mandate. Implementation fidelity data (from state audits and program reviews, where available) is a potential enrichment.

---

### 1.5 Estimation Strategy

**Primary specification:**

$$\Delta \text{PolicyIntensity}_{d,s,t} = \alpha_d + \delta_{s,t} + \beta_1 \text{PreWaiverIntensity}_{d,s} + \beta_2 \text{PostESSA}_t + \beta_3 (\text{PreWaiverIntensity}_{d,s} \times \text{PostESSA}_t) + \gamma X_{d,s,t} + \varepsilon_{d,s,t}$$

where:
- $d$ = district, $s$ = state, $t$ = year
- $\alpha_d$ = district fixed effects (absorb time-invariant district characteristics: size, demographics, political context)
- $\delta_{s,t}$ = state × year fixed effects (absorb *all* state-level time-varying confounders, including state political shocks, governor changes, and state DOE policy shifts)
- $\text{PreWaiverIntensity}_{d,s}$ = district's pre-waiver teacher evaluation infrastructure score (2008–2011 average), standardized within state
- $\text{PostESSA}_t$ = indicator for 2017–2022
- $\beta_3$ = **the key coefficient**: Did districts with weaker pre-waiver infrastructure show more policy correction after ESSA gave them the freedom to roll back? Predicted sign: **negative** (districts with lower pre-waiver intensity = "newly constrained" = more rollback post-ESSA)
- $X_{d,s,t}$ = district-level controls: per-pupil expenditure, poverty rate, racial composition, district size, union density proxy, superintendent stability

> [!IMPORTANT]
> The state × year fixed effects ($\delta_{s,t}$) absorb all state-level confounders. This means the identifying variation is **entirely within-state, across-district variation** in pre-waiver evaluation intensity. This is the design's key strength: it implicitly controls for state partisanship, governor ideology, and state policy trajectory.

**Fixed effects structure:**

| FE | Rationale |
|---|---|
| District FE ($\alpha_d$) | Absorb all time-invariant district characteristics |
| State × Year FE ($\delta_{s,t}$) | Absorb all state-level time-varying shocks — the strongest possible within-state control |
| Alternative: State FE + Year FE | Use if state × year interactions cause over-absorption in states with few districts |

**Clustering strategy:**

Standard errors clustered at the **district level** as the primary specification. Robustness checks:
1. Two-way clustering: district + state-year
2. Spatial clustering by state (Moulton-style), given within-state correlation in unobservables
3. Wild bootstrap with state-level clustering (for robustness given ~50 clusters at state level)

**Key robustness checks:**

| Check | Purpose |
|---|---|
| Pre-trend test (placebo period 2008–2011) | Verify no pre-existing differential trend between "always-compliant" and "newly constrained" districts |
| COVID exclusion (drop 2020–2022) | Verify results are not artifacts of pandemic-era disruption |
| Subsample by state union environment | Does the effect concentrate in low-union districts? (Tests the friction mechanism) |
| LOCO test (exclude VAM component from pre-waiver intensity measure) | Addresses circularity: pre-waiver VAM intensity → post-ESSA VAM rollback is partly mechanical |
| Heterogeneity by district size quartile | Small districts may face different implementation pressures than large urban districts |
| Staggered DiD (Callaway-Sant'Anna) | Account for heterogeneous treatment timing across states (ESSA phase-in varied) |
| Synthetic DiD (Arkhangelsky et al. 2021) | Compare to weighted DiD as alternative estimator |

---

### 1.6 Pre-Registration Plan

> [!CAUTION]
> The composite accountability index failed its confirmatory factor analysis at the state level — the five components did not load on a single factor as predicted. This is a methodological warning sign about researcher degrees of freedom in index construction. The district extension must be pre-registered before any data analysis begins. There is no exception to this rule.

**Why pre-registration is essential:**

The state-level CFA failure means we are in a domain where our measurement theory was wrong in at least one dimension. The district-level extension may face the same problem (components may not cohere) or a different one (implementation-level data may have high missingness). Either way, decisions made after seeing the data — about which components to include, how to handle missing districts, whether to use the VAM component — create researcher degrees of freedom that reviewers will scrutinize.

**What to lock down before opening district data:**

1. **PreWaiverIntensity operationalization:** Exact components (teacher evaluation rating distribution, VAM usage binary, observation frequency), weights, and aggregation method. Decision: equal weights vs. PCA. Must be specified in advance.
2. **Outcome definition:** Exact formula for ΔPolicyIntensity at the district level. What counts as a "correction"? What counts as "intensification"? Decision rules for districts with missing ESSA plan data.
3. **DiD estimator choice:** Callaway-Sant'Anna (staggered adoption) vs. standard two-period DiD. Specify which is primary before seeing the data.
4. **Sample inclusion criteria:** Minimum district size threshold (e.g., exclude districts with < 500 students). Missing data treatment rules.
5. **Hypothesis ordering:** Pre-specify which results will be treated as confirmatory (β₃) and which as exploratory (heterogeneity tests by union density, district size).
6. **Falsification criteria:** What result would constitute evidence *against* the compliance commitment mechanism? (If β₃ is positive — "newly constrained" districts show *more* entrenchment post-ESSA — the mechanism is reversed or absent.)

**Recommended registry:**

- **Primary:** OSF (https://osf.io/) — most widely accepted in political science; supports document uploads, timestamps, and embargo for journal review
- **Alternative:** EGAP (https://egap.org/registry/) — strong reputation in causal identification work; better for designs with explicit quasi-experimental claims
- **Optional supplement:** AsPredicted (https://aspredicted.org/) — shorter format, faster registration, useful for individual hypothesis tests

**Registration timing:** Complete pre-registration *before obtaining any district-level outcomes data*. Pre-treatment data (2008–2015) can be examined for covariate balance and pre-trend testing before registration, but outcome data (2017–2022) must remain unopened until the design is locked.

---

### 1.7 Timeline and Milestones

| Phase | Activities | Duration | Key deliverable |
|---|---|---|---|
| **Phase 0: Pre-registration** | Draft measurement instrument, estimation specification, falsification criteria; register on OSF | 4–6 weeks | Pre-registration document (timestamped) |
| **Phase 1: Data collection** | EDFacts opt-out (4 wks); state DOE teacher eval microdata — public states (6–8 wks); NCTQ CBA database (4–5 wks); SEDA + CRDC merge (2 wks); Ballotpedia scrape (4–5 wks) | **5–7 months** | Raw district-year panel (2008–2022) |
| **Phase 2: Cleaning and validation** | Harmonize district IDs across sources; impute/flag missing data; construct PreWaiverIntensity index; run CFA on index components; pre-trend plots by intensity quartile | **2–3 months** | Analysis-ready district-year panel; CFA report |
| **Phase 3: Primary analysis** | DiD estimation; pre-trend test; key robustness checks (Callaway-Sant'Anna, Synthetic DiD, LOCO, COVID exclusion); heterogeneity tests | **2–3 months** | Regression tables; event-study plots |
| **Phase 4: Drafting** | Write extension paper; integrate with state-level findings; submit | **3–4 months** | Working paper draft |
| **Total** | | **~14–18 months** | Submitted working paper |

**Critical path:** Phase 1 (data collection) drives the timeline. The FOIA requests to state DOEs for teacher evaluation microdata are the bottleneck — begin these in Month 1, in parallel with registration preparation.

> [!TIP]
> **Fastest path to first results:** Run the proof-of-concept analysis on the 15–20 states that already post teacher evaluation summary data publicly. This can be completed in 6–8 months and will refine the measurement strategy before the full FOIA campaign. Strongly recommended as a first-pass validation step.

---

## Track 2: COVID School Closures Comparison Case

### 2.1 Rationale

The pinned pendulum theory is not just about education accountability. Its core claim is that backlash produces correction *when the institutional lever is free* — and fails to produce correction when a compliance commitment mechanism pins the lever in place. To test this conditional claim properly, we need variation in the *lever condition*, not just in backlash intensity.

The ESEA waiver is one instance of a federal compliance commitment mechanism. COVID-era school closures offer the theoretical contrast: extreme, highly visible backlash pressure (school board recalls, parental mobilization, media saturation) operating against a *different* lever condition. The CDC issued guidance on school operations; it did not issue legally binding mandates with financial penalties for noncompliance. The relevant friction was not federal lock-in but rather union collective bargaining agreements specifying remote-work provisions.

**The key theoretical prediction:**  
When the lever is free (CDC guidance ≠ compliance commitment), correction should be faster. States where union contracts did *not* protect remote work — where the lever was genuinely free — should have reopened schools faster than states where union contracts created equivalent institutional friction to the ESEA waiver.

This is not simply "red states reopened faster because Republicans." That is the partisan confounding story. The leverage comes from *within-party variation*: Republican-governed states with strong union remote-work provisions should have reopened slower than Republican-governed states without them. Democratic-governed states with weak union provisions should have reopened faster than those with strong ones. The institutional friction story is *orthogonal to partisan preference* once you condition on party.

**Why COVID is the right comparison:**

| Criterion | COVID closures | ACA rollback | Immigration enforcement |
|---|---|---|---|
| Backlash speed and visibility | Extreme and immediate | Slow, elite-mediated | Slow, elite-mediated |
| Federal lock-in type | Guidance only (free lever) | Statutory + judicial (partial lock-in) | Executive authority varies |
| Within-party variation in constraint | Union contracts vary within party | Uniform partisan alignment | Mostly federal, less state variation |
| Comparable backlash measure | Board elections, recall petitions, Google Trends | Limited organized backlash | Complex backlash topology |
| Theoretical contrast clean? | Yes | Partially | No |

---

### 2.2 Theoretical Parallel

The following table maps the NCLB/ESEA accountability sequence onto the COVID school closure sequence across key dimensions of the pendulum model:

| Dimension | NCLB/ESEA Accountability (Track 1 case) | COVID School Closures (Track 2 case) |
|---|---|---|
| **Policy intensity shock** | NCLB (2002): national test-based accountability mandated; waiver (2011–2015): VAM/evaluation intensification | March 2020: rapid shift to full remote instruction; intensity = days fully closed, remote vs. hybrid |
| **Federal lock-in type** | **Strong:** ESEA waiver = conditional grant with penalty regime. WA and OK had waivers revoked. | **Weak:** CDC guidance only; no legal penalties for reopening. States retained full authority. |
| **Institutional friction source** | ESEA waiver compliance commitment mechanism | Union CBA remote-work provisions (varied by district/state) |
| **Backlash mobilization type** | Organized opt-out (parents), legislative activity, media coverage | School board election turnover (2021), recall petitions (CA, CO), Google Trends spikes |
| **Backlash visibility** | High but delayed (test score → parent → mobilization lag: 2–4 years) | **Extreme and immediate** (economic disruption, visible childcare crisis, within months) |
| **Correction speed prediction** | **Slow** (compliance commitment mechanism pins lever; correction only after ESSA 2015) | **Fast** (no federal lock-in; correction speed determined by union friction only) |
| **Oscillation/overshoot risk** | Low (lever pinned; no oscillation observable in waiver states) | **Higher** (fast rollback may overshoot; some districts went to full in-person before variants allowed) |
| **Partisan confounding severity** | Moderate (R states had both stronger accountability AND more rollback) | **Severe** (R governors explicitly drove reopening; must isolate from institutional friction) |
| **Visibility ceiling risk** | No ceiling (attention-gating variation observable across states) | **Ceiling concern** (COVID was essentially universal; may eliminate attention-gating variation) |

**Theoretical contribution of the comparison:**  
If the conditional feedback model is correct, we expect β(closure intensity → rollback speed) to be strongly negative *in states without union remote-work provisions* and near-zero *in states with strong union remote-work provisions* — regardless of governor party. This is the cleanest test of the compliance commitment mechanism: it produces the same friction whether the commitment comes from a federal grant contract (ESEA) or a private bargaining contract (union CBA).

---

### 2.3 Design

**Unit of analysis:** State-year panel (primary); district-year panel for within-state tests (secondary, exploiting district-level variation in union contract provisions).

**Time window:** 2019–2023 (2019 as pre-treatment baseline; 2020 as treatment year; 2021–2023 as outcome window).

**Treatment variable: 2020 closure intensity** (multi-component index):
1. **Days fully closed** (March–June 2020): Count of school days with 100% remote instruction
2. **Reopening mode in fall 2020:** Fully remote (3), hybrid (2), in-person (1) — ordinal
3. **Closure duration persistence:** Did the state/district extend closure into spring 2021?

Source: Brown Center on Education Policy state reopening tracker; COVID-19 StatePolicy database (University of Washington).

**Backlash measures (multiple):**

| Backlash measure | Operationalization | Source |
|---|---|---|
| School board election turnover | Incumbent defeat rate in 2021 elections; presence of "reopening" candidate platforms | Ballotpedia 2021 school board election results |
| Google Trends | Weekly state-level search intensity for "school reopening," "school board elections," "open schools" | pytrends API, geo-restricted to state DMA |
| Recall petition signatures | Signed recall petitions against school board members (2020–2022) | Manual collection: RECALL watch lists, news archives |
| Parent organization formation | New PTA/parent advocacy group registrations, 2020–2021 | State nonprofit registrations (SOS databases) |

**Outcome variables:**

| Outcome | Operationalization | Source |
|---|---|---|
| Reopening date | First date of ≥50% in-person instruction statewide | Brown Center; COVID StatePolicy db |
| Mask mandate lifting date | Date state rescinded indoor mask mandate | COVID StatePolicy database |
| ESSER fund allocation patterns | % ESSER I/II/III allocated to learning recovery vs. facilities vs. staffing | State ESSER plans (ED.gov) |
| School board ideological shift | Change in board composition toward reopening-favorable members | Ballotpedia coded |

**Key heterogeneity test: Within-party variation by union remote-work provisions**

The primary test is a three-way interaction:

$$\text{ReopeningSpeed}_{s} = \alpha + \beta_1 \text{ClosureIntensity}_s + \beta_2 \text{UnionRemoteWork}_s + \beta_3 (\text{ClosureIntensity}_s \times \text{UnionRemoteWork}_s) + \beta_4 \text{GovParty}_s + \beta_5 (\text{ClosureIntensity}_s \times \text{GovParty}_s) + X_s + \varepsilon_s$$

**Predicted sign:** $\hat{\beta}_3 < 0$ — higher union remote-work protection weakens the closure→rollback relationship (friction blocks correction, just as ESEA waivers blocked accountability rollback). The $\beta_5$ interaction tests whether the union effect is *orthogonal to* or *mediated by* partisan preference.

---

### 2.4 Identification Challenges

**Challenge 1: Partisan confounding**  
Republican governors used school reopening as an explicit political signal of anti-lockdown identity, meaning governor party is correlated with both (a) initial closure intensity and (b) rollback speed, independently of any institutional friction mechanism.

*Mitigation:* Estimate the model **within party** (R-governed states only; D-governed states only). If the union remote-work provision effect holds within Republican governors, the institutional friction story survives the partisan confounding threat.

**Challenge 2: Policy process asymmetry**  
Education accountability policy moves through regular legislative channels (biennial sessions, Board of Education rulemaking). COVID closure/reopening moved through emergency executive orders — a qualitatively different policy process with much shorter timescales.

*Mitigation:* Design the COVID module as a **fully separate paper** (as the panel reviewers unanimously recommended). The theoretical link is the compliance commitment mechanism; the estimation strategy, outcome variables, and data sources are entirely separate. Do not attempt to pool the two panels or directly compare regression coefficients.

**Challenge 3: Measurement incommensurability**  
The accountability backlash index (opt-out rates, ECS legislative counts, media coverage) and COVID backlash measures (board elections, Google Trends, recall petitions) are not on the same scale and were not designed to be.

*Mitigation:* Build a new measurement architecture for the COVID module from scratch. Do not import the accountability backlash index into the COVID panel. Develop COVID-specific backlash measures and validate them against each other using CFA before constructing any composite.

**Challenge 4: Visibility ceiling**  
The ODE model requires attention-gating variation ($A_t$ above vs. below institutional threshold) to generate the conditional correction prediction. COVID school closures were essentially universal in their visibility — attention may hit a ceiling for all observations, eliminating the attention-gating variation.

*Mitigation:* Frame the COVID module as a test of the *institutional friction* component specifically, not attention-gating. The prediction is: conditional on attention being uniformly high (all states above threshold), correction speed should vary with institutional friction (union remote-work provisions), not with attention. This is actually a *cleaner* test of the friction mechanism than the accountability panel, where attention variation was part of the identification strategy.

---

### 2.5 Recommended Specification

**Primary design: Synthetic Difference-in-Differences (Arkhangelsky et al. 2021)**

Synthetic DiD is preferred over standard DiD because: (1) treatment (closure intensity) is continuous rather than binary; (2) states differ substantially in pre-pandemic trajectories; (3) synthetic DiD constructs state-specific weights to match pre-treatment trends, essential with only a 1–2 year pre-period.

**Pre-period (2018–2019):** Establish parallel trends on school calendar (days in session), board election turnover rates, and political context variables.

**Treatment assignment:** Quartile assignment based on 2020 closure intensity score. Top quartile = "high closure" (treatment); bottom quartile = "low closure" (comparison). Sensitivity test: continuous treatment variable.

**Control variables:**
- Governor party (binary: R = 1)
- State partisan lean (2020 presidential vote margin)
- **COVID case rate (log weekly cases per 100,000, March–August 2020)** — critical control: states with worse outbreaks had stronger epidemiological justification for closure. Conditioning on case rate isolates variation in closure intensity attributable to political/institutional factors vs. epidemiological necessity.
- State union density (BLS state union membership rate)
- Union remote-work provision indicator (coded from CBAs: does the statewide or dominant urban district CBA protect remote work as a contractual option?)
- Pre-pandemic school finance (per-pupil expenditure, 2019)
- State poverty rate (ACS 2019)

**Key test:**

$$\hat{\beta}_3 = \left.\frac{\partial \text{ReopeningSpeed}}{\partial \text{ClosureIntensity}}\right|_{\text{UnionRemoteWork}=1} - \left.\frac{\partial \text{ReopeningSpeed}}{\partial \text{ClosureIntensity}}\right|_{\text{UnionRemoteWork}=0}$$

If $\hat{\beta}_3 < 0$: union remote-work provisions slow the closure→rollback path (institutional friction confirmed). If $\hat{\beta}_3 \approx 0$: the closure→rollback path is unaffected by union contract provisions (friction story does not hold for COVID; result returns to partisan preference story).

---

### 2.6 Data Sources

| Source | What it provides | Access | URL |
|---|---|---|---|
| **NWEA MAP COVID Learning Loss Data** | District-level test score changes 2019–2021 (learning loss from closure) | Free download (NWEA research) | https://www.nwea.org/research/ |
| **Brown Center State Closure/Reopening Data** | State and district-level reopening mode by week (remote, hybrid, in-person) | Free download | https://www.brookings.edu/topic/education/ |
| **COVID-19 StatePolicy Database** | State-level executive orders: school closure dates, mask mandate dates, emergency education rules | Free download (University of Washington) | https://statepolicies.com/ |
| **Ballotpedia 2021 School Board Elections** | Candidate outcomes, incumbency, platform descriptions for school board races nationwide | Public scrape (API available) | https://ballotpedia.org/School_board_elections,_2021 |
| **Google Trends** | Weekly state-level search interest for "school reopening," "school board elections" | pytrends Python API | https://trends.google.com/ |
| **NEA/AFT Union Contract Provisions** | CBA language on remote work, emergency operations, school closure protocols | FOIA / public records; NCTQ for large districts | https://www.nctq.org/contract-database |
| **BLS Union Membership Data** | State-level union membership and coverage rates, annual | Free download | https://www.bls.gov/news.release/union2.htm |
| **CDC COVID Data Tracker** | State-level weekly COVID case and death rates (justification control) | Free public access | https://covid.cdc.gov/covid-data-tracker |

---

### 2.7 Risks and Mitigations

**Risk 1: Partisan confounding is too severe to isolate the institutional friction effect**

*Probability: High.* Republican governance is correlated with lower initial closure intensity AND faster rollback AND lower union density AND weaker remote-work provisions — a near-perfect confounding constellation.

*Mitigation:* Within-party analysis is primary. If the union provision effect disappears within R-governed states, the confounding is fatal and the result should be described honestly as: "we cannot separate partisan preference from institutional friction in the COVID case." Do not oversell the COVID result; it is a comparison case, not the main identification.

**Risk 2: Different policy process timescale makes the comparison misleading**

*Probability: Medium.* Emergency executive orders operate on a weekly timescale; accountability legislation operates on an annual-to-biennial timescale. "Rollback speed" is not directly comparable.

*Mitigation:* Frame explicitly as a qualitative theoretical comparison, not a quantitative equivalence claim. The timescale difference is itself theoretically informative: it shows that the pendulum can swing fast when the lever is free, providing a theoretical upper bound on correction speed.

**Risk 3: Measurement incommensurability between accountability and COVID backlash indices**

*Probability: High if incorrectly designed; Low if designed correctly.*

*Mitigation:* Do not attempt to put the two backlash measures on the same scale. Build a COVID-specific measurement architecture and validate it internally.

---

### 2.8 Timeline and Milestones

| Phase | Activities | Duration | Key deliverable |
|---|---|---|---|
| **Phase 0: Design finalization** | Confirm COVID module as separate paper; finalize theoretical parallel table; pre-register design | 3–4 weeks | Pre-registration; theoretical parallel table |
| **Phase 1: Data assembly** | COVID StatePolicy db (2 wks); Brown Center data (1–2 wks); Ballotpedia 2021 scrape (3–4 wks); Google Trends collection (1–2 wks); Union CBA coding (4–6 wks); BLS union density (1 wk) | **3–4 months** | COVID state-year panel (2018–2023) |
| **Phase 2: Cleaning and measurement validation** | Construct closure intensity index; CFA on backlash measures; covariate balance check; pre-trend plots | **1–2 months** | Analysis-ready panel; measurement validation report |
| **Phase 3: Analysis** | Synthetic DiD; within-party subgroup analyses; union provision heterogeneity tests; placebo tests | **1.5–2 months** | Regression tables; synthetic control plots |
| **Phase 4: Drafting** | COVID comparison module as standalone paper | **2–3 months** | Working paper draft |
| **Total** | | **~10–14 months** | Submitted working paper |

**Sequencing note:** Track 2 can begin in parallel with Track 1 Phase 1. The data collection tasks are largely non-overlapping and the COVID module involves a shorter panel with fewer sources. A two-person team could run Track 2 data collection (Months 1–4) simultaneously with Track 1 pre-registration and early data collection.

---

## Track 3: Literature Expansion (Five Buckets)

> [!NOTE]
> The existing `literature.md` covers thermostatic opinion, policy feedback, punctuated equilibrium, and opinion dynamics thoroughly. The five buckets below fill gaps identified by the panel reviewers — especially the formal compliance mechanism, veto points, and empirical education accountability literatures.

---

### Bucket 1: Conditional Democratic Responsiveness / Thermostatic Feedback

**Relevance to the paper:**  
The core theoretical claim is that thermostatic feedback is *conditional* — it operates when the institutional lever is free and fails when the lever is pinned. The existing Wlezien (1995) and Soroka & Wlezien (2010) citations establish the unconditional thermostat; this bucket adds the conditionality literature that the paper's contribution extends.

**Key papers to read:**

| Paper | Key claim | Integration point |
|---|---|---|
| Wlezien, C. & Soroka, S. (2012). "Political Institutions and the Opinion-Policy Link." *West European Politics*, 35(6), 1407–1432. | Majoritarian institutions strengthen thermostatic responsiveness; consensus institutions dampen it. | Federal lock-in operates as a "consensus veto" that dampens the state-level thermostat — directly analogous to the compliance commitment mechanism. |
| Hobolt, S. & Klemmensen, R. (2008). "Government Responsiveness and Political Competition in Comparative Perspective." *Political Studies*, 56(4), 709–732. | Electoral competition strengthens opinion-policy responsiveness; one-party dominance weakens it. | Districts with contested school board elections should show faster thermostatic correction — testable in Track 1. |
| Erikson, R., MacKuen, M., & Stimson, J. (2002). *The Macro Polity*. Cambridge University Press. | Public mood drives policy change across institutions; politicians anticipate opinion shifts. | The anticipatory correction story: are states that *expected* backlash pre-registering policy changes? Potential threat to identification. |
| Lax, J. & Phillips, J. (2012). "The Democratic Deficit in the States." *American Journal of Political Science*, 56(1), 148–166. | State governments are systematically less responsive to public opinion than the federal government; the gap varies by policy domain. | Benchmarks the state-level thermostatic assumption; shows responsiveness is genuinely weak in some domains — may explain the H1 null independent of the waiver. |
| Caughey, D. & Warshaw, C. (2018). "Policy Preferences and Policy Change: Dynamic Responsiveness in the American States." *American Political Science Review*, 112(2), 249–266. | State policies respond to public preferences with a 1–3 year lag; the lag varies by ideological distance between public and government. | Directly operationalizes the delay parameter ($\tau_R$) in the state context; estimated lags are in the range predicted by the theory. |

**Search terms:** `conditional democratic responsiveness`, `thermostatic feedback institutional context`, `Caughey Warshaw dynamic responsiveness states`, `Lax Phillips democratic deficit states`, `opinion-policy link veto players`

**Integration:** Use Caughey & Warshaw (2018) to anchor the delay parameter estimates empirically. Use Lax & Phillips (2012) to motivate the conditional claim: state-level responsiveness is already weak even absent federal lock-in. The waiver effect (H7b) is the *additional* suppression on top of a baseline that is already imperfect.

---

### Bucket 2: Federal Compliance Commitment Mechanisms / Conditional Grants

**Relevance to the paper:**  
The panel reviewers identified "lock-in" as imprecise terminology. The correct framing is "federal compliance commitment mechanism" — a conditional grant structure that creates a penalty regime for policy reversal. This bucket grounds that reframing in the intergovernmental relations (IGR) and public finance literatures.

**Key papers to read:**

| Paper | Key claim | Integration point |
|---|---|---|
| Posner, P. (1998). *The Politics of Unfunded Mandates: Whither Federalism?* Georgetown University Press. | Federal mandates create compliance obligations with varying enforcement mechanisms; the key distinction is whether states bear costs for noncompliance. | Distinguishes ESEA waivers (conditional grants with compliance penalty) from unfunded mandates (where noncompliance costs are absorbed differently). |
| Manna, P. (2006). *School's In: Federalism and the National Education Agenda*. Georgetown University Press. | Federal education policy succeeds when states have "borrowing strength" — capacity and incentive structures that align federal goals with state interests. | The waiver era as a "high borrowing strength" moment: states *wanted* AYP relief, which gave the federal government leverage to require VAM adoption. |
| Peterson, P., Rabe, B., & Wong, K. (1986). *When Federalism Works*. Brookings Institution. | Redistributive federal programs generate more state-level resistance and require stronger enforcement mechanisms than developmental programs. | Categorizes NCLB/waiver accountability as redistributive (benefits to disadvantaged students, costs to tested teachers/schools) — which predicts the strong compliance resistance and enforcement requirement. |
| Volden, C. (2005). "Intergovernmental Political Competition in American Federalism." *American Journal of Political Science*, 49(2), 327–342. | States respond strategically to federal grant conditions; when conditions are costly, states adopt minimum compliance strategies. | "Minimum compliance" strategy explains why some states adopted VAM systems that were technically compliant but not genuinely integrated — creating measurement noise in the pre-waiver intensity variable. |
| Ryan, J. (2004). "The Perverse Incentives of the No Child Left Behind Act." *NYU Law Review*, 79(3), 932–989. | NCLB's AYP system created perverse incentives for states to game accountability measures. | Context for why the waiver program was designed: waivers were the Obama administration's attempt to fix NCLB perversions without congressional action — which is why the compliance conditions were so specific (VAM, teacher evaluation). |

**Search terms:** `conditional grants federal compliance mechanism`, `intergovernmental compliance commitment`, `Manna borrowing strength federalism`, `NCLB waiver compliance conditions`, `conditional path dependency federalism`

**Integration:** Add a 2–3 paragraph subsection in the theory section (after the formal model, before the hypotheses) on "compliance commitment mechanisms as institutional friction." Cite Posner for the general category; Manna for the education-specific mechanism; Volden for the strategic compliance prediction. The panel reviewer's recommended terminology ("conditional contract with penalty regime") maps directly onto Posner's compliance cost framework.

---

### Bucket 3: Institutional Veto Points and Policy Lock-In

**Relevance to the paper:**  
The formal theorist reviewer recommended anchoring the frictional attenuation parameter ($\phi_F$) in a political institutions literature. Veto points theory provides the most established framework for formalizing why some institutional configurations produce slower policy correction than others.

**Key papers to read:**

| Paper | Key claim | Integration point |
|---|---|---|
| Tsebelis, G. (2002). *Veto Players: How Political Institutions Matter*. Princeton University Press. | Policy stability increases with the number of veto players and their ideological distance. The status quo is "stickier" in systems with more veto players. | The compliance commitment mechanism is a veto player in the correction path: waiver revocation threat = an additional veto point on the rollback action. $\phi_F$ maps onto Tsebelis's "absorption coefficient." |
| Immergut, E. (1992). *Health Politics: Interests and Institutions in Western Europe*. Cambridge University Press. | Health reform outcomes across democracies are determined by institutional "veto points" in the policy process, not by interest group strength alone. | Federal compliance mechanisms add a veto point external to the state, which is why they have stronger lock-in than state-internal veto players. |
| Pierson, P. (2000). "Increasing Returns, Path Dependence, and the Study of Politics." *American Political Science Review*, 94(2), 251–267. | Positive feedback processes in politics create increasing returns to policy maintenance, making reversal progressively more costly over time — even absent external enforcement. | Adds the endogenous lock-in mechanism: the longer VAM systems were in place, the more infrastructure (data systems, training programs, contract language) accumulated, raising the cost of reversal independent of the waiver. |
| Mahoney, J. & Thelen, K. (Eds., 2010). *Explaining Institutional Change: Ambiguity, Agency, and Power*. Cambridge University Press. | Institutions change through four mechanisms (displacement, layering, drift, conversion), not only through dramatic punctuations. | Correction may occur through drift (letting VAM requirements atrophy without formally removing them) or conversion (repurposing evaluation systems). |
| Hacker, J. (2005). "Policy Drift: The Hidden Politics of US Welfare State Retrenchment." In Streeck & Thelen (Eds.), *Beyond Continuity*. Oxford University Press. | When enacting formal policy change is costly, political actors may achieve retrenchment by allowing existing policies to decay through inaction. | "Policy drift" as a correction mechanism in pinned-lever states: states unable to formally repeal VAM requirements may allow them to be implemented with decreasing fidelity. |

**Search terms:** `Tsebelis veto players policy stability`, `institutional veto points policy change`, `path dependence increasing returns Pierson`, `policy drift Hacker`, `Mahoney Thelen institutional change mechanisms`

**Integration:** Use Tsebelis's veto players framework to anchor $\phi_F$: $\phi_F$ is a function of the number of veto players on the rollback path, including the federal compliance commitment as one additional veto player. Add a footnote on the Hacker drift mechanism: some of the "correction" observable post-ESSA may be drift rather than active legislative rollback — a distinction the district-level panel can test by comparing states with explicit legislative rollback vs. those with administrative non-enforcement.

---

### Bucket 4: Policy Feedback and Countermobilization

**Relevance to the paper:**  
The panel VAR finding that backlash Granger-predicts *increases* in policy intensity (β = +0.055, p = 0.033) — the "defensive entrenchment" result — needs theoretical grounding. Moe's politics of structural choice and Patashnik's countermobilization framework provide this. This bucket also addresses the asymmetry between backlash mobilization and counter-backlash mobilization.

**Key papers to read:**

| Paper | Key claim | Integration point |
|---|---|---|
| Moe, T. (1990). "Political Institutions: The Neglected Side of the Story." *Journal of Law, Economics, & Organization*, 6, 213–253. | Political actors deliberately design institutions to be resistant to future political attack — structuring bureaucracies, funding formulas, and rules to be hard to undo. | The "politics of structural choice" explains why reform proponents embedded VAM requirements so deeply: they anticipated future political attack and designed for durability. The compliance commitment mechanism was partly *intentional*. |
| Patashnik, E. & Zelizer, J. (2013). "The Struggle to Remake Politics: Liberal Reform and the Limits of Policy Feedback." *Perspectives on Politics*, 11(4), 1071–1087. | Liberal reforms of the 1960s–1990s often failed to generate the positive feedback loops needed to protect themselves, leaving them vulnerable to reversal when political coalitions shifted. | Accountability reform generated negative feedback (backlash) rather than positive feedback (self-reinforcing constituencies), partly because concentrated losers (teachers, local officials) were better organized than diffuse beneficiaries (students). |
| Campbell, A. (2003). *How Policies Make Citizens: Senior Political Activism and the American Welfare State*. Princeton University Press. | Policies can create their own constituencies through resource and interpretive effects, making some policy expansions politically self-reinforcing. | Contrast case: accountability reforms *did* create constituencies (testing companies, edu-management consultants, reform foundations) but these were *not* mass constituencies capable of generating counter-mobilization against the backlash. |
| Goss, K. (2006). *Disarmed: The Missing Movement for Gun Control in America*. Princeton University Press. | Even where public support for policy change is high, reform may fail when the organizational infrastructure for mobilization is absent or under-resourced. | Even where parent backlash sentiment was high, rollback required organized infrastructure (opt-out networks, school board campaigns, legislative lobbying) absent in some states. |
| Weaver, R.K. (1986). "The Politics of Blame Avoidance." *Journal of Public Policy*, 6(4), 371–398. | Politicians systematically prefer policies that allow blame diffusion; they resist explicit policy reversals that would make them responsible for the reversal's consequences. | Rather than explicitly repealing VAM, many states allowed requirements to atrophy because explicit repeal would make them "responsible" for whatever test-score changes followed — explaining the drift mechanism. |

**Search terms:** `Moe politics of structural choice`, `policy feedback countermobilization Patashnik`, `positive policy feedback self-reinforcing`, `blame avoidance Weaver`, `organized interests policy durability`

**Integration:** The Granger positive sign (backlash → more policy) needs a dedicated paragraph, not just a footnote. Use Moe's "politics of structural choice" to explain why reform advocates responded to opt-out mobilization by *intensifying* accountability infrastructure: they anticipated future political attack and used backlash as political cover to lock in their preferred policies while they could. This is not measurement artifact — it is a theoretically predicted feature of the conflict over high-stakes testing.

---

### Bucket 5: Education Accountability Politics (Empirical)

**Relevance to the paper:**  
The existing `literature.md` has McGuinn, Kornhaber, and a generic NBER working paper. This bucket adds the specific empirical studies that most directly test the mechanisms the paper claims — with real estimates the paper can benchmark against or distinguish itself from.

**Key papers to read:**

| Paper | Key claim | Integration point |
|---|---|---|
| Dee, T. & Jacob, B. (2011). "The Impact of No Child Left Behind on Student Achievement." *Journal of Policy Analysis and Management*, 30(3), 418–446. | NCLB had positive effects on 4th grade math, especially for disadvantaged students. | Benchmarks the achievement signal variable: states where NCLB *worked* (by Dee-Jacob's estimates) should show *less* backlash — testing this prediction distinguishes genuine backlash from partisan cycling. |
| Polikoff, M. et al. (2016). "The Watered-Down, Federalized, Pilloried, and Sacked Common Core." *Educational Researcher*, 45(9), 556–564. | Common Core state adoptions were rapidly followed by modifications, renaming, and effective abandonment in many states. | Direct documentation of the correction phase; provides state-level timing of Common Core rollback that can be merged with the backlash index as an outcome variable. |
| Aldeman, C. & Carey, K. (2017). "A Measured Approach: How the Obama Education Department Used Its Waiver Authority to Pursue Education Reform." Education Policy Initiative. | ESEA waivers were designed as a policy tool to implement Common Core and teacher evaluation in exchange for AYP relief; the compliance conditions were explicit and enforced. | Provides the policy mechanism description for the compliance commitment story — cites specific waiver conditions, enforcement cases (WA, OK), and the strategic design of the exchange. |
| Ladd, H. & Zelli, A. (2002). "School-Based Accountability in North Carolina: The Responses of Schools and Teachers." *Educational Administration Quarterly*, 38(4), 494–529. | Schools and teachers respond strategically to accountability pressures — gaming metrics, narrowing curriculum — rather than improving underlying performance. | Mechanism evidence for why backlash was rational: the costs that the accountability system imposed on teachers and schools were real and generated genuine grievances, not manufactured backlash. |
| Wong, K. & Guthrie, J. (Eds., 2019). *The Political Economy of Education Accountability*. Routledge. | Edited volume collecting the strongest empirical work on the political economy of education accountability, including chapters on backlash, waiver politics, and ESSA implementation. | Use as a domain literature anchor; several chapters provide direct benchmarks for the correction and backlash variables. |

**Search terms:** `NCLB effects student achievement Dee Jacob`, `Common Core rollback political opposition Polikoff`, `ESEA waiver conditions enforcement Aldeman`, `education accountability backlash organized mobilization`, `opt-out movement education empirical`, `ESSA implementation state variation`

**Integration:** Add a dedicated "Empirical Context" subsection in the paper's empirical design section citing Dee & Jacob (2011) for the achievement signal; Polikoff et al. (2016) for the timing and mechanisms of Common Core rollback; and Aldeman & Carey (2017) for the institutional mechanism behind waiver compliance conditions. These citations ground the paper's empirical claims in the domain literature and preempt reviewer challenges that the paper ignores what happened in the classroom.

---

## Summary Table: Priority and Timeline

| Track | Priority | Est. time to first results | Key data challenge | Theoretical contribution |
|---|---|---|---|---|
| **Track 1: District-Level Panel DiD** | 🔴 **High** — resolves the N=51 power problem and provides the confirmatory test of H7b | **14–18 months** | State DOE teacher eval microdata (FOIA-dependent); ESSA plan district-level coding | Tests whether compliance commitment mechanism operates at within-state district level; resolves H1 null by providing MDE ≈ 0.03–0.05; directly extends the paper's headline result |
| **Track 2: COVID School Closures** | 🟡 **Medium** — theoretically important comparison case but severe partisan confounding | **10–14 months** | Union CBA remote-work coding; partisan confounding cannot be fully controlled | Tests whether the conditional feedback model generalizes to non-education policy; provides an "unlocked lever" case to contrast with ESEA; if within-party variation isolates institutional friction, strongest external validity test |
| **Track 3: Literature Expansion** | 🟡 **Medium** — needed for current paper submission, not just future roadmap work | **3–6 months for initial pass** | None — search and synthesis task | Grounds the conditional feedback model in IGR theory (Bucket 2), veto points literature (Bucket 3), and empirical accountability literature (Bucket 5); provides benchmark estimates and theoretical vocabulary for the compliance commitment mechanism reframing |

**Recommended sequencing:**

```
Month 1–2:   Track 3 literature search (Buckets 2, 3, 5 first — most urgent for submission)
             + Track 1 pre-registration preparation
             + Track 2 design finalization and pre-registration

Month 2–4:   Track 1 pre-registration completed (OSF)
             + Track 1 Phase 1 data collection begins (EDFacts, SEDA, CRDC — low-FOIA sources first)
             + Track 2 Phase 1 data collection begins (COVID StatePolicy db, Ballotpedia 2021)

Month 4–8:   Track 1 FOIA requests in flight; public state DOE data being cleaned
             + Track 2 analysis-ready panel complete; preliminary Synthetic DiD results
             + Track 3 integration: revise theory section, add compliance mechanism subsection

Month 8–12:  Track 1 analysis-ready panel; pre-trend tests; primary DiD results
             + Track 2 working paper draft

Month 12–18: Track 1 working paper draft; integrate with state-level paper
             + Full submission package for both papers
```

> [!TIP]
> **The fastest path to Track 1 results** runs through the 15–20 states that already post teacher evaluation summary data publicly. A "proof of concept" analysis on this subsample can be completed in 6–8 months and used to refine the measurement strategy before the full FOIA campaign. This is strongly recommended as a first-pass validation step before committing to the full national data collection effort.

---

*End of roadmap. Version 1.0 — June 2026.*  
*Next scheduled review: October 2026 (after Phase 1 data collection status assessment).*
