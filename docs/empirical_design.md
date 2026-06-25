# Empirical Research Design

*When the Pendulum Doesn't Swing — Technical Design Document*

---

## 1. Overview of Empirical Strategy

The project runs two parallel tracks that inform each other:

| Track | Focus | Notebooks |
|---|---|---|
| **Track A — Simulation** | Toy model + agent-based model; no real data needed; explore dynamics | `01_theory_simulation`, `02_agent_based_model` |
| **Track B — Empirical** | State-year panel study; data collection → regression → results | `03_data_collection` through `08_results_visualization` |

**Integration principle:** The simulation (Track A) is not a standalone exercise — it is a **parameter identification tool** for Track B. Simulation findings should motivate specific empirical predictions; empirical patterns should calibrate simulation parameter ranges. Run simulation findings first, commit to predictions, then open the data.

---

## 2. Primary Domain: U.S. Education Reform

### Why Education Reform

U.S. K–12 education reform is the primary test domain because it offers the cleanest observable policy pendulum sequence in recent domestic U.S. policy:

| Phase | Policy | Period | Mechanism |
|---|---|---|---|
| 1 | NCLB passage | 2002 | Policy intensity shock — national test-based accountability |
| 2 | Common Core + waivers | 2010–2015 | Intensification + expansion of federal role |
| 3 | Opt-out movement | 2013–2016 | Threshold-crossing backlash — mass organized mobilization |
| 4 | ESSA passage | 2015 | Institutional correction — federal flexibility |
| 5 | ESSA implementation | 2017–2024 | State redesign — heterogeneous correction patterns |

This sequence maps cleanly onto the pendulum mechanism: policy output expands → costs become visible → attention spikes → organized backlash grows → institutions eventually correct → correction may itself generate new imbalance.

### Study Window

**Primary analysis:** 2010–2024

**Why not 2002?** The early NCLB years are harder to reconstruct comparable state-level backlash signals for. The 2010–2024 window captures Common Core rollout, testing controversy, opt-out growth, ESSA passage, and post-ESSA redesign — the full arc of the most recent cycle.

> [!WARNING]
> **COVID-era data (2020–2024) requires special handling.** Post-pandemic education politics (parent rights movements, curriculum debates, learning loss) introduced new conflict dimensions not described by the pre-COVID pendulum framework. Recommended approach:
> - **Primary analysis:** 2010–2019
> - **Robustness check 1:** Exclude 2020–2022
> - **Robustness check 2:** Add pandemic-period interaction dummy
> - **Alternative:** Treat 2020–2024 as a separate analytical epoch

### Unit of Analysis

**State-year panel:** 51 states × 15 years (2010–2024) = 765 observations at the primary level.

**District-level extension (where data permit):** ~13,000 districts provide far more statistical power for nonlinear hypotheses (H4, H6). SEDA, CRDC, and district-level NAEP estimates support this extension.

> [!IMPORTANT]
> **Statistical tightness warning (flagged by Quantitative Methodologist):** N=51 states × T=15 years is tight for the number of hypotheses, especially the nonlinear interaction terms in H2, H4, and H6. Power calculations should be run before committing these as **confirmatory** hypotheses. They may need to be treated as **exploratory** at the state-year level and confirmatory only with district-level data.

---

## 3. Variable Operationalization

### 3.1 Policy Intensity Index (Key Predictor)

**Concept:** The degree to which a state's accountability system relied on high-stakes standardized testing, sanctions, and centralized control — before ESSA.

**Components:**
1. Accountability strength (presence/absence of school ratings, AYP-equivalent)
2. Test salience (proportion of accountability weight on standardized tests)
3. Sanction severity (school turnaround requirements, grade retention, teacher dismissal linkage)
4. Rating simplicity (A-F grades vs. multi-dimensional dashboard — simple ratings are higher-stakes)
5. Teacher evaluation linkage (whether VAM/test scores determine teacher evaluation)

**Aggregation:**
> [!IMPORTANT]
> **Pre-register the aggregation method before touching data.** This is the single highest-priority credibility protection. Options:
> - **Equal weights:** Simple but atheoretical
> - **PCA:** Data-driven, but components may not be substantively interpretable
> - **IRT (Item Response Theory):** If treating accountability as a latent trait measured by binary indicators
> - **Theory-weighted:** Weight components by theoretical importance (test salience and sanctions should be highest-weighted based on backlash mechanism)
>
> Decision must be made and registered BEFORE seeing the distribution of outcomes.

**Sources:** NCES accountability tables (pre-ESSA baseline), ECS legislative archives, Education Trust state accountability analyses.

**Measurement model:** Before constructing the composite, run a confirmatory factor analysis (CFA) to test whether the five components load on a single "accountability intensity" factor. If they do not, they may be measuring distinct constructs with different causal roles.

---

### 3.2 Backlash Index (Key Outcome / Mediator)

> [!IMPORTANT]
> **"Backlash" conflates four empirically distinct phenomena.** Three of four peer reviewers flagged this independently. The index MUST be disaggregated and each component run separately before combining.

**Three distinct sub-indicators:**

**Sub-indicator 1: Mass Opinion**
- Education Next Poll (annual, national; state-level unavailable → use as national trend validator)
- PDK Poll (annual, national)
- Cooperative Election Study (CES) — large sample, allows state-level estimation via MrP
- *Operationalization:* Annual % opposing "more testing," supporting "less federal involvement," or item-specific anti-accountability responses

**Sub-indicator 2: Organized Mobilization**
- Opt-out rates by state (from EDFacts state assessment participation data; percentage of students not tested)
- ECS legislative activity — number of bills introduced restricting testing, modifying standards, or limiting federal accountability provisions per state-year
- School board election outcomes (where available)
- *Operationalization:* Opt-out rate + standardized ECS legislative count + school board reversal indicator

**Sub-indicator 3: Elite/Media Framing Shifts**
- GDELT article counts for key terms (`"Common Core"`, `"standardized testing backlash"`, `"opt out testing"`, `"No Child Left Behind"`) — count per state-year where attributable
- Media Cloud counts (better outlet control)
- Google Trends relative interest by state/DMA for same terms
- *Operationalization:* Normalized composite of article counts and search trends

> [!WARNING]
> **GDELT geographic misattribution problem (flagged by Quantitative Methodologist):** GDELT over-represents English-language national media and has systematic gaps in regional coverage. A NYT article about opt-out is NOT reliable evidence of New York State backlash specifically. Use GDELT for national trend validation; use Media Cloud with state-outlet filters and Google Trends with geographic restriction for state-level attribution.

**Validation:** Run confirmatory factor analysis on all three sub-indicators. If they load on a single "backlash" latent factor, construct a composite using factor scores. If they load on multiple factors, treat them as **separate dependent variables** with separate theoretical interpretations in the main models.

---

### 3.3 Policy Correction Score (Key Outcome)

**Concept:** The degree to which a state moved away from test-centric accountability in its post-ESSA accountability design.

Two separate measures are required:

**Cross-sectional measure (ESSA plans, 2017–18):**
- Indicator weight on standardized tests vs. non-test measures
- Whether school rating system is A-F (high test salience) vs. multi-dimensional dashboard
- Number of non-academic indicators in the accountability system
- Whether growth vs. proficiency is emphasized
- *Source:* ESSA Consolidated State Plans (U.S. Dept. of Education PDFs → manual coding)

> [!IMPORTANT]
> **ESSA plans are NOT time-varying (flagged by Quantitative Methodologist).** They were filed once (2017–18) and rarely amended. Using "Correction_{s,t+1}" as a time-varying panel outcome misrepresents the data structure. The ESSA plan content is properly a **cross-sectional outcome** that can be compared to the pre-ESSA policy intensity index.

**Time-varying measure (annual legislative/regulatory revisions):**
- ECS annual tracking of state legislation modifying assessment, accountability, or standards
- State administrative rule changes (Board of Education actions)
- Waiver requests and federal approval patterns
- *Operationalization:* Yearly binary or ordinal indicator of correction-direction legislative/regulatory action

---

### 3.4 Delay Parameter (τ) — CRITICAL GAP

> [!IMPORTANT]
> **H2 (lagged overcorrection) is the theory's most important hypothesis, and the delay parameter has no empirical operationalization.** This was flagged as critical by the Quantitative Methodologist. Without a cross-state measure of institutional response delay, H2 is untestable.

**Proposed operationalizations (choose one primary, use others as robustness):**

1. **Legislative session frequency:** States with annual sessions vs. biennial sessions; biennial states have structurally longer delays in legislative response
2. **Time-to-adoption:** For each major NCLB provision, how many months elapsed between federal enactment and state administrative implementation?
3. **Time-to-petition-response:** In states where opt-out petitions were introduced, how long from introduction to committee action?
4. **Institutional friction index:** Composite of legislative session frequency, gubernatorial veto power, legislative professionalism score (NCSL data)

---

### 3.5 Norm Variable (N_t)

**Concept:** The level of policy that a state's political community perceives as "normal" or "acceptable" — the baseline against which deviations are judged.

**Operationalizations:**

1. **Moving average:** $\hat{N}_{s,t} = \frac{1}{K}\sum_{j=1}^{K} P_{s,t-j}$ — the average of the past K years of policy intensity. This formalizes the slow drift equation $N_{t+1} = N_t + \nu(P_t - N_t)$.

2. **Pre-reform baseline:** Use 2000–2002 (pre-NCLB) accountability intensity as a fixed norm anchor; deviations from that baseline measure "how far from normal."

3. **Partisan-group-specific norms:** Use CES ideological estimates by state-year to construct separate R-leaning and D-leaning norm estimates. Test whether the pendulum runs asymmetrically across partisan communities.

4. **Institutional trust anchor:** ANES/GSS trust-in-education-institutions items as a proxy for perceived legitimacy of current policy.

---

### 3.6 Controls

| Variable | Source | Notes |
|---|---|---|
| Presidential vote share (R) | MIT Election Lab | State-level, presidential years; interpolate between |
| State legislative party control | MIT Election Lab / NCSL | Chamber-by-chamber, annual |
| Governor party | NCSL / Ballotpedia | Annual |
| State ideological position | CES MrP estimates | State-year |
| Teacher union strength | State union membership data | Proxy for organized backlash capacity |
| % students in poverty | ACS | Annual state |
| Racial/ethnic composition | ACS | Annual state |
| Per-pupil expenditure | NCES school finance | Annual state |
| Unemployment rate | BLS LAUS | Annual state |
| Baseline NAEP (2009) | NAEP Data Explorer | Pre-treatment achievement control |
| State education department capacity | Proxy via budget/staff | Affects implementation speed |

---

## 4. Estimating Equations

### 4.1 Backlash Equation (Distributed-Lag Fixed Effects)

$$\text{Backlash}_{s,t} = \alpha_s + \delta_t + \sum_{k=1}^3 \beta_k (\text{PolicyIntensity}_{s,t-k} - \text{Norm}_{s,t-k}) + \beta_4 \text{AchievementSignal}_{s,t-1} + \beta_5 X_{s,t} + \varepsilon_{s,t}$$

- $\alpha_s$: state fixed effects (absorb time-invariant state characteristics)
- $\delta_t$: year fixed effects (absorb national trends)
- $\text{Norm}_{s,t-k}$: 5-year rolling average representing public's adaptive norm baseline
- $\beta_1, \beta_2, \beta_3 > 0$: policy deviation from the norm predicts backlash with lag
- $X_{s,t}$: control vector (partisan government trifectas, election years, demographics, union strength)

**Predicted sign:** $\sum \hat{\beta}_k > 0$ — policy exceeding the baseline norm predicts more backlash over subsequent periods.

**Run separately on each backlash sub-indicator before combining.**

### 4.2 Correction Equation

$$\text{Correction}_{s,t+1} = \alpha_s + \delta_t + \gamma_1 \text{Backlash}_{s,t} + \gamma_2 (\text{PolicyIntensity}_{s,t-1} - \text{Norm}_{s,t-1}) + \gamma_3 X_{s,t} + u_{s,t}$$

**Predicted sign:** $\hat{\gamma}_1 > 0$ — more backlash predicts more policy correction.

> [!WARNING]
> **This two-equation design is a mediation chain, not a structural model.** The Quantitative Methodologist reviewer flagged that both equations are endogenous to each other (legislators anticipate backlash; backlash responds to correction signals). Lagged terms help but do not fully solve the problem. Run alongside the panel VAR (below) as the primary estimator.

### 4.3 Panel VAR (Primary Time-Series Estimator)

**3-variable system:** [PolicyIntensity$_{s,t}$, Backlash$_{s,t}$, Correction$_{s,t}$]

$$\mathbf{Y}_{s,t} = \sum_{p=1}^{P} \mathbf{A}_p \mathbf{Y}_{s,t-p} + \mathbf{u}_{s,t}$$

Where $\mathbf{Y}_{s,t} = [\text{PolicyIntensity}, \text{Backlash}, \text{Correction}]^\top$.

**VAR Identification Scheme (Cholesky Ordering):**
For Impulse-Response Functions (IRFs), we impose the recursive Cholesky ordering:
\[
\text{PolicyIntensity}_{s,t} \rightarrow \text{Backlash}_{s,t} \rightarrow \text{Correction}_{s,t}
\]
*Justification:*
1. Policy intensity is highly predetermined (sticky institutional rules).
2. Backlash responds contemporaneously to policy changes, but policy only responds to backlash with a lag.
3. Policy correction is the most endogenous, responding contemporaneously to both policy and backlash shocks.

**Why VAR is preferable to sequential regression:**
- Does not impose a causal ordering (both equations are endogenous)
- Allows bidirectional effects
- Granger-causality tests directly test the theory's temporal ordering claims
- Impulse-response functions give a vivid picture of how a shock to policy intensity propagates through backlash to correction over time — and whether it oscillates or converges

**Key tests:**
- Does PolicyIntensity Granger-cause Backlash? ($p < 0.05$ → supports H1/H3)
- Does Backlash Granger-cause Correction? ($p < 0.05$ → supports core mechanism)
- Does Correction Granger-cause lower subsequent PolicyIntensity? ($p < 0.05$ → confirms full cycle)
- Impulse-response function: does the system oscillate in response to a policy intensity shock, or converge monotonically?

**Lag order selection:** AIC/BIC; baseline is VAR(1) to avoid parameter bloat in a T=15 panel.

**Implementation:** statsmodels VARResultsWrapper in Python (estimating on pooled demeaned panel) or a panel VAR R-bridge (for the Abrigo-Love estimator).

---

## 5. Causal Identification Strategy

> [!IMPORTANT]
> **This is the project's most critical methodological weakness.** Three of four peer reviewers flagged that distributed-lag FE regression is insufficient for causal identification. States with high pre-ESSA accountability intensity are systematically different on partisanship, union strength, and demographic composition — all of which independently predict backlash.

### 5.1 Primary Strategy: Dosage-Based Event Study

**Design:** Use pre-ESSA policy intensity (measured 2010–2014, before ESSA passage) as a continuous "dosage" variable. Compare post-ESSA trajectories of backlash and correction across states with different pre-ESSA intensities.

**Identification assumption:** Conditional on pre-ESSA trends in backlash indicators (parallel trends), differences in post-ESSA correction and backlash trajectories are attributable to differences in pre-ESSA policy intensity rather than to confounders.

**Implementation:**
1. Compute pre-ESSA intensity index for each state (2010–2014 average)
2. Verify parallel pre-trends: plot backlash indicators by intensity quartile, 2010–2015 — they should be parallel before ESSA passage
3. Estimate event-study coefficients for each year post-ESSA, interacted with pre-ESSA intensity
4. Report event-study plot: states by intensity quartile, -5 to +7 years around ESSA

**Key assumption test:** Is there a pre-trend? If high-intensity states were already showing higher backlash before ESSA, the identification fails. This is the most important diagnostic.

### 5.2 Alternative: DiD with Pre-2010 Intensity

Use 2000–2009 pre-treatment accountability intensity × post-ESSA period as the DiD setup. Pre-2010 intensity is less likely to be endogenous to 2013–2016 backlash dynamics.

### 5.3 Instrumental Variables

**Candidate instruments (must be relevant and exogenous):**
- *Race to the Top eligibility/award:* States that received RttT funding implemented stronger accountability provisions partly due to grant incentives, not purely because of pre-existing political demand
- *State education department capacity (pre-2002):* States with more institutionalized ed departments adopted NCLB provisions faster — a plausible determinant of accountability intensity that predates the backlash period
- *NCLB waivers timing:* Whether and when states received NCLB waivers (2011–2015) was partly determined by federal review processes, introducing quasi-random variation in how long they were subject to NCLB-era sanctions

### 5.4 Synthetic Control (Robustness)

For 3–5 high-profile cases (e.g., Texas, Massachusetts, New York, California, Tennessee), construct synthetic control states and compare their post-ESSA correction trajectories to the synthetic counterfactual.

---

## 6. Competitor Hypothesis: Partisan Cycling

> [!IMPORTANT]
> **The most parsimonious alternative explanation must be directly tested, not just controlled for.**

**Partisan cycling hypothesis:** Republicans took control of more state governments and Congress and rolled back Obama-era education policy on partisan grounds, unrelated to any thermostatic feedback mechanism.

**Test:** Does backlash predict correction **within** party-control periods — i.e., do Republican-controlled states that had higher policy intensity show more correction even when partisan control doesn't change?

- Add interaction: PolicyIntensity × PartisanTurnover
- If the policy intensity effect disappears when controlling for partisan cycling (partisan turnover predicts all correction), the pendulum may be an artifact of electoral politics rather than a distinct feedback mechanism
- If the effect persists within party-control periods, it supports the thermostatic mechanism over simple partisan cycling

---

## 7. Validity Threats & Mitigations

| Threat | Description | Mitigation |
|---|---|---|
| **Reverse causality** | Backlash may precede policy intensity (anticipatory politics) | Lagged policy terms; event-study pre-trend tests; Granger causality |
| **Partisan confounding** | Conservative states had both stronger accountability AND stronger anti-accountability politics | Explicit partisan controls (CES ideology, presidential vote, legislative control); within-party-period analysis |
| **National/state opinion mismatch** | Education Next/PDK are national; can't directly map to state-year | Use as national trend validators only; use CES for state-level opinion estimation via MrP |
| **Backlash measurement error** | Any single backlash proxy is noisy | Multi-indicator composite with CFA validation; run models on each indicator separately |
| **COVID disruption** | Post-2020 education politics are structurally different | Primary analysis 2010–2019; COVID robustness checks |
| **Federalism heterogeneity** | States differ structurally in ways that affect both intensity and correction | State fixed effects; explicit institutional capacity controls |
| **GDELT geographic misattribution** | GDELT over-represents national media; state-level attribution is unreliable | Use Media Cloud (with state outlet filters) and Google Trends for state-level backlash attribution |
| **ESSA plan tautology** | States with weak pre-ESSA systems had more room to diversify (floor effects) — correction may reflect capacity, not backlash | Separate correction models by pre-ESSA intensity quartile; include pre-ESSA intensity as control in correction equation |
| **Oscillation vs. trend** | A slowly shifting partisan trend + single reversion could look like a pendulum | Spectral analysis; distinguish oscillation from monotone drift with reversal |

---

## 8. Power Analysis

> [!IMPORTANT]
> **Run simulation-based power analysis before treating nonlinear hypotheses as confirmatory.**

The Quantitative Methodologist flagged that N≈50 × T≈14 is tight for:
- **H2:** Delay × intensity interaction ($\tau \times \text{PolicyIntensity}$)
- **H4:** Nonlinear backlash threshold (requires detecting a breakpoint in the dose-response curve)
- **H6:** Polarization × swing amplitude interaction

**Tool:** R's `DeclareDesign` package (or Python equivalent) for simulation-based power analysis with realistic DGP assumptions.

**Recommended approach:**
1. Simulate 1,000 datasets from the toy model with plausible parameter values
2. Run the main regression on each simulated dataset
3. Report the proportion of simulations where the hypothesis is correctly detected at $p < 0.05$
4. If power is below 0.80 for a hypothesis, treat it as **exploratory** and note the limitation explicitly

---

## 9. Pre-Registration Plan

> [!IMPORTANT]
> **Pre-register on OSF (https://osf.io/) or EGAP (https://egap.org/registry/) BEFORE beginning data collection or analysis.**

### What to Pre-Register

1. **Policy intensity index:** Which components, which aggregation method, decision rules for missing state-years and ambiguous state plans
2. **Backlash sub-indicators:** Exact GDELT/Media Cloud keywords, date ranges, normalization; exact ECS categories; exact CES items
3. **Backlash composite construction:** CFA protocol; what factor loading threshold constitutes evidence of convergent validity; what to do if CFA fails
4. **Estimating equations:** Exact specification, lag structure, control variables
5. **Identification strategy:** Which strategy is primary (event-study); which are robustness checks (IV, synthetic control)
6. **ABM predictions:** Parameter ranges and qualitative patterns predicted for different (k, σ) combinations — commit to these BEFORE opening the empirical data
7. **Falsification criteria:** Specific patterns that would lead to theory rejection (not just parameter re-estimation)
8. **COVID treatment:** Primary analysis window; robustness check specifications

---

## 10. Multi-Domain Extension Design

For each domain beyond education, specify four structural parameters to derive ordered predictions:

| Parameter | Education | Policing | Immigration | Climate | Highway funding |
|---|---|---|---|---|---|
| Feedback delay (τ) | Medium (2–4 yrs) | Short–medium | Long | Very long (decades) | Very long |
| Cost visibility | High (test scores, teacher eval) | High (crime stats) | High (deportations) | Low (diffuse/distant) | Very low |
| Federalism level | Mixed (fed+state) | Local | Federal dominant | Federal+international | Federal dominant |
| Interest group concentration | Medium | Medium-high | High | High | Low |
| **Predicted oscillation** | **Strong** | **Medium-strong** | **Medium** | **Weak** | **None (falsification)** |

**Non-oscillating comparison case:** Federal highway funding (or actuarial insurance regulation). Prediction: minimal pendulum dynamics because cost visibility is low, interest groups are non-mobilized on ideological grounds, attention threshold is rarely crossed, and benefits are immediate and visible (roads get built). **This case must be pre-specified before analysis begins.**

---

## 11. Notebook Mapping

| Notebook | Purpose | Key outputs |
|---|---|---|
| `03_data_collection.ipynb` | Download/scrape all raw data sources | Raw files in `data/raw/` |
| `04_data_cleaning.ipynb` | Build state-year panel, operationalize all variables | `state_year_panel.csv` |
| `05_eda.ipynb` | Time-series plots, spectral analysis, cross-state variation | Diagnostic charts; pre-trend plots |
| `06_backlash_index.ipynb` | CFA on sub-indicators, composite construction | Backlash index; factor loadings |
| `07_panel_regression.ipynb` | FE models, panel VAR, event study, robustness | Regression tables; IRF plots |
| `08_results_visualization.ipynb` | Final publication-quality figures | All figures for paper and public project |
