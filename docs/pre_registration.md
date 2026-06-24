# Pre-Registration Template (OSF/EGAP Format)

This document serves as the pre-analysis registration template for *The Pendulum Always Swings* project, outlining hypotheses, design, variable operationalizations, and statistical models before empirical data files are formally opened for analysis.

---

## 1. Plain-English Summary

This study investigates why public policy and public perception in specific domains exhibit recurring oscillations or "pendulum swings." We hypothesize that these dynamics are emergent properties of system feedback architecture rather than simple political turnover. Specifically, when a policy is pushed far from the prevailing societal norm, it generates asymmetric cost visibility and public attention. Once this crosses a critical threshold, it triggers organized backlash that exerts pressure for a policy correction. Because institutional responses are subject to implementation and legislative lags, corrections arrive late and frequently overshoot, seeding the next cycle.

To test this general theory, we analyze K–12 education reform (NCLB $\rightarrow$ Common Core $\rightarrow$ opt-out $\rightarrow$ ESSA) across U.S. states from 2010 to 2024. We construct a state-year panel tracking policy intensity, multi-indicator backlash (media, public search, and legislative opposition), and subsequent policy changes. We contrast this against a pre-registered control domain (federal highway funding) where feedback delays and salience are low, predicting no oscillation. We commit to testing whether delayed negative feedback and threshold effects drive the amplitude and frequency of these swings.

---

## 2. Hypotheses & Falsification Thresholds

We pre-specify the following decision rules for rejecting our core hypotheses:

| Hypothesis | Theoretical Claim | Empirical Test | Numerical Rejection Criterion |
|---|---|---|---|
| **$H_1$: Thermostatic Correction** | Public demand adjusts negatively against policy overreach. | Granger causality in Panel VAR: $\text{PolicyIntensity} \rightarrow \text{Backlash}$ | Rejects if Granger $p > 0.10$ or cumulative impulse response is negative. |
| **$H_2$: Lagged Overcorrection** | Larger feedback delays ($\tau$) increase oscillation amplitude. | Correlation of state-specific CCF peak lag ($\tau_s$) with standard dev of Policy. | Rejects if Spearman rank correlation is not positive ($\rho \leq 0.00$) or $p > 0.10$. |
| **$H_3$: Attention Threshold** | Policy correction only occurs after salience crosses a threshold. | Threshold panel regression (Hansen 1999) of Correction on Backlash. | Rejects if F-test comparing threshold vs. linear model yields $p > 0.10$. |
| **$H_4$: Backlash Threshold** | Backlash grows nonlinearly as policy distance from norm exceeds $\theta$. | Panel regression comparing a piecewise spline vs. linear policy gap term. | Rejects if spline model does not significantly improve fit (F-test $p > 0.10$). |
| **$H_5$: Visibility of Costs** | Backlash is stronger when implementation costs are concentrated and visible. | Sub-indicator regression: coefficient on visible costs vs. diffuse benefits. | Rejects if coefficient on visible cost indicators is less than diffuse indicators. |
| **$H_6$: Polarization Amplification** | Narrower confidence bounds (polarization) increase swing amplitudes. | Sub-sample regression by state-year polarization index median split. | Rejects if coefficient on backlash in high-polarization states $\leq$ low-polarization. |
| **$H_7$: Institutional Dampening** | built-in damping (sunset clauses, local flexibility) decreases swings. | Interaction model: $\text{Backlash} \times \text{DampeningProxy}$ in Correction regression. | Rejects if interaction coefficient is not negative or statistically indistinguishable from zero ($p > 0.10$). |

---

## 3. Empirical Design & Variable Operationalization

*   **Study Window**: 2010–2024. 
    *   *Robustness epoch separations*: Primary analysis runs on 2010–2019 (pre-COVID); secondary analysis models 2020–2024 as a distinct epoch or includes pandemic-period interaction terms.
*   **Unit of Analysis**: State-year panel ($N=51$ states, $T=14$ years).
*   **Policy Intensity ($P_{s,t}$)**: Standardized composite index of state accountability strength, standard test requirements, and teacher evaluation linkages.
*   **Perceived Norm ($N_{s,t}$)**: Operationalized as a 5-year rolling moving average of past policy intensity, reflecting how public expectations adapt:
    \[
    N_{s,t} = \frac{1}{5}\sum_{i=1}^5 P_{s,t-i}
    \]
*   **Backlash ($B_{s,t}$)**: Validated via confirmatory factor analysis (CFA) using the following pre-specified factor structure:
    *   *Factor 1 (Media Mobilization)*: GDELT policy-sentiment count, Media Cloud coverage volume.
    *   *Factor 2 (Elite Signaling)*: ANES state education trust, ECS legislative activity count.
    *   *Factor 3 (Mass Mobilization)*: Standardized opt-out/participation rates, PDK/EdNext public opinion opposition items.
    *   *CFA Decision Rule*: If CFA fit is acceptable ($\text{CFI} > 0.95$, $\text{RMSEA} < 0.06$) for a single latent dimension $\rightarrow$ use factor scores as $B_{s,t}$. Otherwise, retain the three factors as separate sub-indices and run downstream regressions on each.

---

## 4. Statistical Models & Identification

### A. Core Regression Specifications
We estimate the following two equations using panel OLS with state and year fixed effects:

$$\text{Backlash}_{s,t} = \alpha_s + \delta_t + \sum_{k=1}^3 \beta_k (P_{s,t-k} - N_{s,t-k}) + \gamma \text{PartisanControl}_{s,t} + \mathbf{X}_{s,t}\mathbf{\Gamma} + \epsilon_{s,t}$$

$$\text{Correction}_{s,t} = \alpha_s + \delta_t + \theta \text{Backlash}_{s,t-1} + \gamma \text{PartisanControl}_{s,t} + \mathbf{X}_{s,t}\mathbf{\Gamma} + u_{s,t}$$

*   **Partisan Control Confound**: We explicitly control for state government partisan control (trifecta status from MIT Election Lab) and a dummy for gubernatorial election years to rule out simple electoral cycling.
*   **Robustness Subsample**: We run a within-party-control subsample check (restricting to periods of constant party control in a state) to verify that the backlash-correction link holds independently of partisan transitions.

### B. Panel VAR Identification
We estimate a 3-variable Panel VAR (using `statsmodels` on pooled demeaned series or a panel VAR R-bridge if required for the Abrigo-Love estimator) to capture dynamic feedbacks. We pre-specify the **Cholesky recursive ordering**:

$$\mathbf{Y}_{s,t} = [P_{s,t}, B_{s,t}, C_{s,t}]'$$

where:
1.  **Policy Intensity ($P$)** is treated as the most predetermined variable, reflecting institutional sticky states.
2.  **Backlash ($B$)** responds to contemporaneous policy shocks but policy only responds to backlash with a lag.
3.  **Policy Correction ($C$)** is the most endogenous variable, reacting contemporaneously to both policy and backlash shocks.

---

## 5. Falsification Control Case

*   **Control Domain**: Federal Highway Funding.
*   **Theoretical Basis**: Low visibility of implementation costs, low public salience, immediate tangible benefits, and lack of ideological mobilization mean the attention threshold is rarely breached.
*   **Falsification Test**: We collect highway funding obligation data (FHWA) and Google Trends "highway funding" salience to construct the same panel and run equations.
*   **Null Prediction**: The estimated Granger causality $\text{Funding} \rightarrow \text{Backlash}$ will be statistically zero ($p > 0.10$) and the standard deviation of funding levels will be at least $1.5\times$ smaller than education policy changes, showing no cyclical oscillation.

---

## 6. Simulation Pre-Commitment

We pre-commit to the following parameter regimes for our deterministic simulations:
*   $\tau \ge 3, \lambda \ge 0.35$: Predicts sustained limit-cycle oscillations.
*   $\tau = 0$: Predicts monotonic convergent decay to equilibrium.
*   $\theta_{\text{inst}} \ge 0.4$: Predicts a punctuated sawtooth step-function correction pattern.
