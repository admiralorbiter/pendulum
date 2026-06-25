# Research Roadmap

*When the Pendulum Doesn't Swing — Phase-by-Phase Research Plan*

This is the living operational document. It answers: **what to pull, in what order, what to look for, and what success looks like at each phase.**

---

## Overview: Two Parallel Tracks

```
Track A (Simulation) ─────────────────────────────────────────────────────►
  Phase A1: Stability analysis       Phase A2: ABM design
  notebooks/01_theory_simulation     notebooks/02_agent_based_model

Track B (Empirical) ──────────────────────────────────────────────────────►
  Phase B1: Pre-registration  →  Phase B2: Data collection  →  Phase B3: Analysis
  (OSF/EGAP)                     notebooks/03–04               notebooks/05–08
```

Both tracks inform each other. Simulation findings motivate empirical predictions. Empirical patterns calibrate simulation parameters.

---

## PHASE A1: Theory Simulation
**Notebook:** `notebooks/01_theory_simulation.ipynb`  
**No real data needed — start immediately**

### What to Build
The 5-equation system (D, P, A, B, N) implemented in Python/NumPy.

### What to Compute

**Step 1: Stability analysis in (k, λ) space**
- For the policy equation $P_{t+1} = P_t + \lambda(D_{t-k} - P_t)$, find the critical curve where the dominant eigenvalue crosses the unit circle
- Map three regions: stable convergence / oscillation / instability
- This is the model's core mathematical deliverable

**Step 2: Parameter sweeps**
Vary one parameter at a time while holding others constant:
- Delay $k$: 0, 1, 2, 4, 8 periods → measure oscillation amplitude
- Correction strength $\lambda$: 0.1 to 1.0
- Backlash threshold $\theta$: low, medium, high
- Norm drift rate $\nu$: 0 (fixed norm) to 0.5 (fast adaptation)
- Attention decay $\delta$: fast vs. slow

**Step 3: Phase portraits and time series**
For each interesting parameter combination:
- Time series of all 5 variables
- Phase portrait (D vs. P)
- Oscillation amplitude as function of k

**Step 4: Qualitative regime identification**
Label the distinct behavioral regimes:
- Regime 1: Stable convergence (policy and opinion settle)
- Regime 2: Damped oscillation (swings shrink over time)
- Regime 3: Sustained oscillation / limit cycle (pendulum)
- Regime 4: Divergence (explosive instability)

Map which real-world conditions correspond to each regime.

### What to Look For
- **Confirmation**: Oscillation emerges when $k$ is large and $\lambda$ is moderate — this is the key theoretical claim
- **Surprise**: Do any parameter combinations produce asymmetric oscillations (swings larger in one direction)? This would be theoretically important
- **For H7 (dampening)**: Adding institutional damping (reducing $\lambda$ after threshold) should reduce amplitude — verify this

### Success Criterion
A stable, reproducible notebook that clearly shows the stability boundary and produces oscillation under delay conditions that plausibly map to real policy systems.

---

## PHASE A2: Agent-Based Model
**Notebook:** `notebooks/02_agent_based_model.ipynb`

### What to Build
A Mesa-based ABM with:
- Agents with: opinion, tolerance (confidence bound), attention level, threshold for backlash, network neighbors
- Interaction rules: agents update toward neighbors within tolerance; ignore opinions outside tolerance
- Policy rule: policy responds to mean (or weighted mean) opinion with lag $k$
- Attention rule: rises when policy moves far from norm; decays over time
- Backlash rule: activates after threshold; spreads via network

> [!IMPORTANT]
> **Separate this from the mean-field ODE.** The ABM should answer: what distributional properties (variance, bimodality) does the mean-field model miss? A bimodal opinion distribution with the same mean as a unimodal one will produce different backlash dynamics.

### Key Experiments
1. **Homogeneous vs. heterogeneous thresholds**: What happens when agents have varying backlash thresholds (Granovetter distribution)?
2. **Network structure**: Random vs. clustered vs. scale-free networks — does backlash cascade differently?
3. **Elite injection**: Add a small number of "elite" agents who can spike attention regardless of policy distance — test the manufactured backlash mechanism
4. **Dampening mechanisms**: Add a "sunset clause" agent type that reduces policy velocity after each swing — does it stabilize?

### Pre-Registration Required
**Commit to specific ABM predictions BEFORE running the empirical panel analysis.** What patterns does the ABM predict for:
- Low tolerance (high polarization) vs. high tolerance (consensus)?
- Long policy delay vs. short delay?
- Network clustering vs. diffuse networks?

Write these predictions to `docs/pre_registration.md` before opening any empirical data files.

---

## PHASE B1: Pre-Registration
**Platform:** OSF (https://osf.io/) or EGAP (https://egap.org/registry/)  
**Complete before any empirical data analysis**

### What to Pre-Register

1. **Policy intensity index construction protocol**
   - Which components (accountability strength, test salience, sanctions, rating simplicity, teacher-eval linkage)
   - Aggregation method (equal weights vs. PCA — specify WHICH before seeing the data)
   - Decision rules for missing state-years
   - Decision rules for ambiguous state plans
   
2. **Backlash index construction protocol**
   - Which GDELT/Media Cloud keywords, date ranges, normalization method
   - Which Google Trends keywords
   - Which ECS legislative categories count as "backlash"
   - CFA validation: what loading threshold constitutes evidence of convergent validity?
   
3. **Estimating equations** — specify exact lag structure, fixed effects structure, controls
   
4. **Falsification predictions**
   - Which states should show NO significant backlash (name them)
   - Which domain should show NO pendulum (the non-oscillating comparison case)
   - What coefficient signs would lead to theory rejection (not just theory refinement)

5. **ABM predictions** (from Phase A2)

---

## PHASE B2: Data Collection
**Notebook:** `notebooks/03_data_collection.ipynb`

### Collection Order (priority order)

**Week 1–2: Policy variables**
- [ ] Download all ESSA state plans (PDF → structured coding)
- [ ] Pull ECS assessment/accountability/standards archives (annual, state-level)
- [ ] Pull NCLB federal policy timeline
- [ ] Pull NCES accountability tables (pre-ESSA baseline)

**Week 3–4: Opinion data**
- [ ] Download Education Next Poll data file (2007–present)
- [ ] Download PDK Poll archives
- [ ] Download CES cumulative file (2006–present) from Harvard Dataverse
- [ ] Download ANES 2000–2022 cumulative file

**Week 5–6: Media & attention data**
- [ ] Set up GDELT BigQuery queries for key terms (2010–2024)
- [ ] Set up Media Cloud API pulls for same terms
- [ ] Pull Google Trends data via pytrends (state-level where available)

**Week 7–8: Outcomes and controls**
- [ ] Download NAEP state data (grades 4 and 8, math and reading, 2009–2023)
- [ ] Pull ACS 5-year estimates (2010–2023, state-level)
- [ ] Download MIT Election Lab returns (president 2008–2020, governor, state legislature)
- [ ] Pull BLS LAUS unemployment (annual state-level, 2010–2024)
- [ ] Download NCES school finance data

**Week 9–10: Discipline comparison case**
- [ ] Download CRDC biennial files (2011–12 through most recent)
- [ ] Pull ECS discipline policy archives

### What to Look For During Collection
- **Are the variables actually available at the state-year level?** Some things that look annual are actually biennial or cross-sectional (ESSA plans, CRDC). Document this in `data/raw/README.md`.
- **Are GDELT state-level signals plausible?** Spot-check: do Google Trends and GDELT agree on when "opt out" peaked nationally? (~2015–2016)
- **Does the policy intensity index have meaningful cross-state variation?** States should differ substantially on pre-ESSA accountability intensity. If variation is too low, the main comparison collapses.

---

## PHASE B3: Data Cleaning & Panel Construction
**Notebook:** `notebooks/04_data_cleaning.ipynb`

### What to Build
A clean `state_year_panel.csv` with:
- State × Year as the primary key (51 states + DC × 2010–2024 = ~714 rows)
- All policy, backlash, outcome, and control variables
- Clear documentation of each variable's source and construction

### Key Construction Steps
1. Build policy intensity index (per pre-registered protocol)
2. Build three separate backlash sub-indicators
3. Run CFA on backlash sub-indicators — document results
4. Build policy correction score from ESSA plans (cross-sectional) and annual revisions (time-varying)
5. Operationalize delay parameter ($\tau$) — at minimum one proxy measure
6. Operationalize norm variable ($N_t$) — moving average of historical policy intensity
7. Merge all controls

### Data Quality Checks
- Missing data map: which state-years are missing which variables?
- Distribution checks: are any variables suspiciously uniform (no variation)?
- Pre-trend check: plot policy intensity, backlash indicators, and outcomes over time for 5–6 diverse states

---

## PHASE B4: Exploratory Data Analysis
**Notebook:** `notebooks/05_eda.ipynb`

### What to Examine

**Time-series patterns (national)**
- Plot NAEP scores, Education Next/PDK opinion trends, GDELT/Google Trends attention, ECS legislative activity from 2010–2024
- Do you see the NCLB → opt-out → ESSA correction pattern visually?

**Cross-state variation**
- Which states had the highest pre-ESSA policy intensity?
- Which states show the largest shifts in ESSA plan design?
- Does backlash correlate visually with policy intensity (lagged)?

**Spectral analysis**
- Is there evidence of periodicity in the national opinion/policy series?
- Distinguish: true cycle vs. monotone trend + reversion
- Use scipy.signal.periodogram on key time series

**Cross-correlation analysis**
- Does opinion change lag policy change by a predictable number of periods? (H1, H2)
- Does attention spike before or after policy change? (H3)

### What to Look For
- **The clearest visual confirmation**: A chart showing that states with high pre-ESSA accountability index values showed larger opt-out rates and more diverse ESSA plans
- **Potential trouble**: If all states look similar on the policy intensity index, the identification strategy collapses
- **COVID break**: Clearly visible in NAEP 2022 — mark this in all time-series plots

---

## PHASE B5: Backlash Index
**Notebook:** `notebooks/06_backlash_index.ipynb`

### Steps
1. Compute each sub-indicator separately: mass opinion, organized mobilization, elite/media framing
2. Run CFA — are the three indicators one construct or multiple?
3. If multiple factors, treat separately. If one, compute composite using factor scores or standardized average.
4. Validate: does the composite peak at expected times (2013–2016 for education)?

---

## PHASE B6: Panel Regression & Causal Analysis
**Notebook:** `notebooks/07_panel_regression.ipynb`

### Estimation Sequence

**Step 1: Pre-trend checks**
Before running anything, verify parallel pre-trends for the ESSA event study. Plot backlash indicators by pre-ESSA intensity quartile from 2010 to 2015 — they should be parallel before the "treatment" (ESSA).

**Step 2: Distributed-lag FE models**
$$\text{Backlash}_{s,t} = \alpha_s + \delta_t + \beta_1 \text{PolicyIntensity}_{s,t-1} + \beta_2 \text{PolicyIntensity}_{s,t-2} + \beta_3 \text{AchievementSignal}_{s,t-1} + \beta_4 X_{s,t} + \varepsilon_{s,t}$$

$$\text{Correction}_{s,t+1} = \alpha_s + \delta_t + \gamma_1 \text{Backlash}_{s,t} + \gamma_2 \text{PolicyIntensity}_{s,t-1} + \gamma_3 X_{s,t} + u_{s,t}$$

Run separately on each backlash sub-indicator before combining.

**Step 3: Panel VAR (primary time-series estimator)**
3-variable VAR: [PolicyIntensity, Backlash, Correction]
- Granger causality tests: does policy intensity Granger-cause backlash? Does backlash Granger-cause correction?
- Impulse-response functions: how does a shock to policy intensity propagate through backlash to correction over time?

**Step 4: ESSA event-study (identification strategy)**
- Pre-ESSA intensity as continuous dosage variable
- Compare ESSA plan correction scores across intensity quartiles
- Parallel pre-trend validation (from Step 1)

**Step 5: Nonlinear tests (H4)**
- Use splines or piecewise linear specification for the policy intensity → backlash relationship
- Test for breakpoint (threshold) using Chow test or smooth transition regression

**Step 6: Robustness checks**
- Exclude 2020–2022
- Exclude partisan high-polarization states
- Alternative backlash measures (each sub-indicator alone)
- Alternative policy intensity weighting schemes

**Step 7: Partisan cycling falsification**
- Add interaction: PolicyIntensity × PartisanTurnover
- Does backlash predict correction WITHIN party-control periods (controlling for electoral change)?
- If effect disappears when controlling for partisan cycling, that is serious evidence against the pendulum mechanism

### What to Look For
- **Core result**: $\beta_1 < 0$ (more policy intensity → less support for more) in the backlash equation; $\gamma_1 > 0$ (more backlash → more policy correction) in the correction equation
- **H2 test**: $\beta$ should be larger (more negative) for states with higher delay proxy $\tau$
- **Critical threat**: If the effect disappears when adding partisan controls, the pendulum may be an artifact of electoral cycling

---

## PHASE B7: Visualization & Results
**Notebook:** `notebooks/08_results_visualization.ipynb`

### Required Outputs
1. National time-series plots with key events annotated (NCLB, Race to the Top, ESSA)
2. State-level scatter: pre-ESSA intensity vs. ESSA correction score
3. Impulse-response function from panel VAR
4. Event-study plot: states by intensity quartile, pre and post-ESSA
5. Nonlinear backlash threshold plot (H4)
6. Comparison table: education domain vs. discipline domain
7. Falsification case: the non-oscillating domain

---

## Pre-Analysis Checklist

Before touching any empirical data, confirm:
- [ ] Pre-registration filed on OSF/EGAP
- [ ] ABM predictions committed in `docs/pre_registration.md`
- [ ] Stability boundary computed in Phase A1
- [ ] Policy intensity index construction protocol documented
- [ ] Backlash sub-indicator definitions documented
- [ ] At least one "non-pendulum" domain specified

---

## Timeline Estimate

| Phase | Estimated Duration |
|---|---|
| A1: Theory simulation | 1–2 weeks |
| A2: Agent-based model | 2–3 weeks |
| B1: Pre-registration | 1 week |
| B2: Data collection | 6–10 weeks |
| B3: Data cleaning | 2–3 weeks |
| B4: EDA | 1–2 weeks |
| B5: Backlash index | 1 week |
| B6: Regression | 2–4 weeks |
| B7: Visualization | 1–2 weeks |
| **Total** | **~5–7 months** |

Simulation work (Track A) can begin immediately and run in parallel with the early phases of Track B.
