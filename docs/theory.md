# Theory: The Pendulum Always Swings — When Feedback Is Delayed

*Policy-perception oscillation: a formal theory*

---

## 1. Overview & Core Claim

Policy-perception pendulums are **emergent properties of feedback architecture** — not the result of anyone designing them, not evidence that both sides are equally wrong, and not proof that the system self-corrects toward truth. They emerge when four conditions coincide:

1. **Delayed corrective feedback** — policy responds to public demand, but with a lag
2. **Attention thresholds** — the system ignores weak signals and over-responds to salient ones
3. **Asymmetric cost visibility** — costs of a policy become visible faster than benefits
4. **Backlash mobilization** — affected groups organize nonlinearly once a perceived threshold is crossed

> *The pendulum is not magic. It is what you get when delayed feedback + attention spikes + group threat + institutional friction are all present at once.*

The project's central prediction:

> **Pendulum swings are largest when policy response is delayed, costs become visible before benefits, media attention spikes past a threshold, and affected groups perceive the change as overreach.**

---

## 2. The Core Mechanism: Delayed Negative Feedback

The mathematical backbone of the theory is **negative feedback with delay**.

In a perfectly responsive system:

$$x(t+1) = x(t) - k \cdot x(t)$$

Negative feedback stabilizes the system — it always corrects toward equilibrium.

But when response is delayed by $\tau$ periods:

$$x(t+1) = x(t) - k \cdot x(t - \tau)$$

The dynamics change qualitatively. **Delayed negative feedback can produce oscillation and overshoot.** The intuition: by the time correction arrives, the system has already moved further in the original direction. The correction then overshoots the equilibrium, requiring another correction in the opposite direction — and the cycle begins.

This is the scientific language for the pendulum:
- $k$ = correction strength
- $\tau$ = delay before response
- When $k$ and $\tau$ are both large enough, the system oscillates rather than converges

The critical mathematical insight: there exists a boundary in $(k, \tau)$ parameter space where the system transitions from stable convergence to sustained oscillation. Finding that boundary is one of the project's first computational tasks (see `notebooks/01_theory_simulation.ipynb`).

---

## 3. The Sine-Wave vs. Sawtooth Problem

> [!IMPORTANT]
> **Peer review flagged this as the most critical unresolved structural issue.** Three of four expert reviewers independently identified it. It must be resolved before the theory is submitted for publication.

The project draws on two traditions that predict **contradictory oscillation shapes**:

### The Thermostatic Model (Wlezien) → Sine Wave
Continuous, proportional, smooth correction. Public demand adjusts gradually and proportionally against policy movement. Opinion tracks policy distance in a quasi-continuous way. The implied dynamics are smooth, symmetric oscillations — a sine wave.

### Punctuated Equilibrium + Threshold Cascades (Baumgartner-Jones, Granovetter) → Sawtooth
Long periods of stability interrupted by sudden catastrophic flips. Policy sticks, sticks, sticks — then snaps. The implied dynamics are irregular, asymmetric, threshold-driven — a sawtooth.

These are **not compatible** as descriptions of the same process. A referee will immediately ask: which one does this theory claim?

### Resolution: Two Timescales, Two Mechanisms

The reconciliation is that both mechanisms operate, but at **different timescales** and on **different variables**:

| Mechanism | What it describes | Timescale | Variable |
|---|---|---|---|
| Thermostatic correction | Continuous corrective pressure *building within a cycle* | Short-run, continuous | $D_t$ adjusting against $P_t$ |
| Punctuated equilibrium | *Between-cycle transitions* — when accumulated pressure crosses an institutional threshold | Long-run, discrete | $P_t$ snapping when $A_t > \theta$ |

In plain terms: **public opinion drifts thermostati­cally every year**, but **policy only snaps when attention and political conditions align**. The smooth corrective pressure is always building; it only becomes visible as a policy swing when it breaches an institutional threshold.

### Piecewise Formulation

This suggests a piecewise policy equation:

$$P_{t+1} = \begin{cases} P_t + \lambda(D_{t-k} - P_t) & \text{if } A_t > \theta_{\text{inst}} \\ P_t + \epsilon & \text{if } A_t \leq \theta_{\text{inst}} \end{cases}$$

When attention is below the institutional threshold, policy is nearly static (punctuated equilibrium's long flat periods). When attention crosses the threshold, policy responds proportionally to accumulated demand — the snap.

This formulation makes the sine-wave vs. sawtooth tension a feature rather than a contradiction: real oscillations will look like **sawtooth with smooth interpolation** — long flat periods punctuated by rapid corrections, where the corrections themselves are smooth once attention unlocks the system.

---

## 4. The Seven Academic Frameworks

### 4.1 Thermostatic Public Opinion
**Contribution:** The basic corrective mechanism. Explains *why* opinion moves against policy direction.

**Key works:** Christopher Wlezien (1995), "The Public as Thermostat: Dynamics of Preferences for Spending." *American Journal of Political Science*. Stuart Soroka & Christopher Wlezien (2010), *Degrees of Democracy*, Cambridge.

**Formal model:**
$$\text{Demand}_{t+1} = \text{Demand}_t - \alpha(\text{Policy}_t - \text{PreferredPolicy}_t) + \varepsilon_t$$

When government does more of something, public demand for more tends to fall. When government does less, demand rises. Wlezien tested this using time-series regression on spending preferences.

**This project's value-add over Wlezien:** The thermostatic model explains *that* correction occurs; this project explains *why amplitude and timing vary* — through attention thresholds, identity threat, and backlash dynamics that the simple thermostat ignores.

**Search terms:** `thermostatic public opinion`, `Wlezien public as thermostat`, `Soroka Wlezien public opinion policy responsiveness`, `error correction models policy responsiveness`

### 4.2 Punctuated Equilibrium Theory
**Contribution:** Explains why real policy oscillations are not smooth — they stick, then snap.

**Key works:** Frank Baumgartner & Bryan Jones (1993/2009), *Agendas and Instability in American Politics*. Bryan Jones & Frank Baumgartner, "The Politics of Attention" — disproportionate information processing.

**Key claim:** Policy systems are bounded in their information processing. They ignore weak signals for too long, then over-attend once pressure breaks through. The result is a leptokurtic distribution of policy change: mostly small changes, with occasional very large ones.

**Formal prediction:**
$$\text{PolicyChange} \approx \text{small (most of the time)}; \quad \text{PolicyChange} \approx \text{very large (when attention} > \theta)$$

**Implication for oscillation shape:** Instead of a sine wave, expect: `flat → flat → flat → jump → backlash → flat → jump`

**Search terms:** `punctuated equilibrium policy process`, `Baumgartner Jones policy change`, `leptokurtic policy change distributions`, `disproportionate information processing public policy`

### 4.3 Issue-Attention Cycle
**Contribution:** Explains why public attention rises and falls — and why the corrective mechanism eventually decays even when the underlying problem persists.

**Key works:** Anthony Downs (1972), "Up and Down with Ecology: The Issue-Attention Cycle." *The Public Interest*.

**Five-stage cycle:** (1) Pre-problem stage, (2) Alarmed discovery and euphoric enthusiasm, (3) Realizing the cost of significant progress, (4) Gradual decline of intense public interest, (5) Post-problem stage (lower attention, some institutionalization).

**Model connection:** The $(1 - \delta)A_t$ decay term in the attention equation captures Stage 4-5 — attention decays automatically even without policy response. This is what prevents the system from sustaining indefinite backlash: attention fatigue sets in.

**Search terms:** `Downs issue-attention cycle`, `public attention policy cycles`, `media attention policy salience`

### 4.4 Policy Feedback Theory
**Contribution:** Explains why each policy creates the political conditions for the *next* policy fight. Policies are not just outputs of politics — they become inputs to subsequent politics.

**Key works:** Paul Pierson (1993), "When Effect Becomes Cause: Policy Feedback and Political Change." *World Politics*. Eric Patashnik (2008), *Reforms at Risk*; (2023), *Countermobilization*.

**Two feedback channels (Pierson):**
1. **Resource/incentive effects:** Policies change who has money, organization, and incentives to engage
2. **Interpretive effects:** Policies change how actors understand the political world and frame their interests

**Patashnik's addition:** Backlash risk is highest when policies impose **concentrated losses** on organized groups while distributing benefits diffusely. This maps directly onto H5 (visibility of costs): the losers see their losses immediately; the winners' gains are diffuse and slow-arriving.

**Search terms:** `policy feedback theory`, `Pierson policy feedback`, `policies shape politics`, `Patashnik reforms at risk`, `Patashnik countermobilization`

### 4.5 Backlash & Countermovement Theory
**Contribution:** Explains organized resistance — why backlash is not just individual opinion change but coordinated collective action.

**Key works:** Meyer & Staggenborg (1996), "Movements, Countermovements, and the Structure of Political Opportunity." *American Journal of Sociology*. Mansbridge & Shames — backlash as resistance by actors who perceive a loss or threat to power. Timur Kuran (1995), *Private Truths, Public Lies* — preference falsification.

**Key mechanism (Meyer & Staggenborg):** Movement-countermovement interaction is a recurring feature of contemporary politics, especially when the state partly enables but does not fully satisfy challengers. This creates a structural dynamic: each reform that partially succeeds generates the organizational infrastructure for its own opposition.

**Kuran's relevance:** Backlash can be *manufactured* — preference falsification means that public opinion can cascade rapidly via social pressure even when underlying individual preferences haven't changed. This is the "authentic vs. synthetic backlash" problem the project must address empirically.

**Search terms:** `backlash theory politics`, `countermovement theory`, `movement countermovement interaction`, `status threat backlash`, `preference falsification Kuran`

### 4.6 Policy Overreaction & Underreaction
**Contribution:** Explains amplitude — not just that the pendulum moves, but why it moves *too far*.

**Key works:** Moshe Maor (2012), "Policy Overreaction." Collected volume on disproportionate policy response.

**Key claim:** Governments underreact to problems until pressure builds (long flat period, H3), then overreact once the issue becomes politically salient (large swing). The oscillation between under- and overreaction is a property of disproportionate information processing systems.

**Vocabulary for amplitude:** "Policy bubbles" — policies that expand well beyond optimal level before triggering collapse. "Emotional policy entrepreneurship" — advocates who amplify signals beyond their informational content, contributing to overreaction.

**Search terms:** `policy overreaction Maor`, `policy underreaction`, `disproportionate policy response`, `policy bubbles public policy`

### 4.7 Opinion Dynamics & Polarization Models
**Contribution:** Explains the micro-foundations — how individual opinion updating can produce macro-level polarization, cascades, and tipping points.

**Key works:**
- Hegselmann & Krause (2002), bounded confidence model
- Deffuant-Weisbuch model (continuous opinion updating)
- Mark Granovetter (1978), "Threshold Models of Collective Behavior." *American Journal of Sociology*
- Thomas Schelling (1971), "Dynamic Models of Segregation." *Journal of Mathematical Sociology*
- Castellano, Fortunato & Loreto (2009), "Statistical Physics of Social Dynamics." *Reviews of Modern Physics*

**Bounded confidence model (Hegselmann-Krause):**
$$\text{Agent}_i \text{ updates toward Agent}_j \text{ only if } |\text{opinion}_i - \text{opinion}_j| < \epsilon$$

When $\epsilon$ is wide, populations converge. When $\epsilon$ is narrow, populations fragment into clusters. This connects directly to H6: narrow confidence bounds → stronger within-group swings.

**Threshold model (Granovetter):**
$$\text{Person joins backlash if } \text{ObservedSupport} > \text{PersonalThreshold}$$

This gives the micro-mechanism for cascade dynamics: once enough people join, more people join. Small changes in visible support can produce large cascades if thresholds cluster.

**Schelling's insight:** Mild individual preferences can generate extreme collective outcomes. Pendulum swings may not require everyone to become extreme — extreme collective movement can emerge from modest local rules.

**Search terms:** `bounded confidence opinion dynamics`, `Hegselmann Krause model`, `Deffuant Weisbuch opinion dynamics`, `Granovetter threshold model collective behavior`, `Schelling dynamic models segregation`, `agent based polarization model`

---

## 5. The Formal Model

### 5.1 Variables

| Variable | Symbol | Interpretation |
|---|---|---|
| Public demand | $D_t$ | The direction and intensity of what the public wants policy to do |
| Policy position | $P_t$ | Actual policy intensity/position at time $t$ |
| Attention/salience | $A_t$ | How much public and media attention the issue is receiving |
| Backlash pressure | $B_t$ | Organized countermobilization pressure against the policy |
| Perceived norm | $N_t$ | The baseline level of policy that the public perceives as "normal" or acceptable |

### 5.2 The Equations

**Public Demand:**
$$D_{t+1} = D_t - \alpha(P_t - N_t) + \beta A_t - \gamma B_t \cdot \text{sign}(P_t - N_t) + \varepsilon_t$$

*Plain language:* Public demand shifts against policy when policy is perceived as too far from the norm ($\alpha$ term). Attention amplifies demand movement ($\beta$ term). Backlash pressure pulls demand *away* from policy (opposing the policy direction, hence signed by the policy-norm gap; $\gamma$ term). $\varepsilon_t$ is noise.

*Equilibrium:* $D^* = N^*$ when $P = N$ and $A = B = 0$.

---

**Policy Position:**
$$P_{t+1} = P_t + (\lambda + \mu A_t)(D_{t-k} - P_t) + \eta_t$$

*Plain language:* Policy adjusts toward public demand, but with a lag of $k$ periods. Attention scales the responsiveness speed ($\mu$ term — when an issue is salient, legislators respond faster), removing artificial positive policy drift. $\eta_t$ is noise.

*The delay $k$ is the engine of oscillation.* When $k = 0$, the system can converge. When $k$ is large, the correction arrives after demand has already shifted further, producing overshoot.

---

**Attention/Salience:**
$$A_{t+1} = (1 - \delta)A_t + \varphi|P_t - N_t| + \text{shock}_t$$

*Plain language:* Attention decays at rate $\delta$ (Downs's issue-attention cycle — audiences eventually move on). Attention rises when policy is perceived as far from the norm. $\text{shock}_t$ captures exogenous events (a school shooting, a viral video) that spike attention regardless of policy distance.

> [!NOTE]
> **Endogeneity of attention (flagged by Complex Systems reviewer):** Attention is also strategically manufactured by elites, media organizations, and movement entrepreneurs. The $\text{shock}_t$ term currently treats this as noise rather than as a structured process. Elite-driven attention cascades are mechanistically different from organic salience. Future versions should model this explicitly.

---

**Backlash Pressure:**
$$B_{t+1} = \rho B_t + \sigma \max(0, |P_t - N_t| - \theta)$$

*Plain language:* Backlash has persistence ($\rho$ term — movements don't instantly dissolve). It grows nonlinearly: **only after policy crosses a perceived threshold $\theta$**. Below the threshold, backlash pressure is zero or trivial. Above it, backlash grows proportionally to the excess. This is the `max(0, ...)` functional form — the right mathematical representation of Granovetter-style threshold mobilization.

*The nonlinearity in $B_t$ is the key structural feature connecting this model to punctuated equilibrium.* Below $\theta$: flat politics. Above $\theta$: rapid backlash growth.

---

**Perceived Norm (NEW — added from peer review):**
$$N_{t+1} = N_t + \nu(P_t - N_t) + \eta_N$$

*Plain language:* The perceived norm drifts slowly toward prevailing policy. If policy stays at a new level long enough, that level becomes the new "normal." This creates **ratchet effects**: a reform that survives long enough shifts the norm, making the pre-reform state harder to restore. $\nu$ controls how fast norms adapt (small $\nu$ = slow adaptation, large $\nu$ = fast norm updating).

> [!IMPORTANT]
> **Why N_t needed its own equation:** The norm variable appeared in three of the four original equations but had no dynamics, no measurement strategy, and no account of partisan divergence. Without this equation, the model can only produce oscillations around a fixed point — it cannot model polarization-driven norm divergence (where different groups perceive entirely different "norms"). This was flagged as a critical gap by all 4 peer reviewers.

*Partisan extension:* In a polarized polity, $N_t$ should be indexed by group: $N_{t,R}$ and $N_{t,D}$ (Republican-perceived and Democrat-perceived norms). When these diverge, the pendulum may run in opposite directions simultaneously in different partisan communities.

### 5.3 Parameter Table

| Parameter | Symbol | Range (typical) | Interpretation | Effect on oscillation |
|---|---|---|---|---|
| Thermostatic correction | $\alpha$ | 0.1–0.8 | How strongly demand corrects against policy | Higher → stronger corrective pressure |
| Attention amplification of demand | $\beta$ | 0–0.5 | How much attention boosts demand movement | Higher → larger swings when salient |
| Backlash dampening of demand | $\gamma$ | 0–0.5 | How much backlash pulls demand further from policy | Higher → more extreme demand during backlash |
| Policy correction rate | $\lambda$ | 0.1–0.9 | How fast policy moves toward demand | Higher $\lambda$ with high $k$ → instability |
| Attention effect on policy | $\mu$ | 0–0.3 | How much salience accelerates policy response | Higher → faster but potentially premature corrections |
| Attention decay | $\delta$ | 0.1–0.5 | How fast attention fades (Downs cycle) | Higher → shorter cycles |
| Attention sensitivity to policy distance | $\varphi$ | 0–0.5 | How much policy-norm gap raises attention | Higher → self-amplifying attention spirals |
| Backlash persistence | $\rho$ | 0.5–0.95 | How long backlash pressure lasts | Higher → longer-lived countermovements |
| Backlash growth rate | $\sigma$ | 0–1.0 | How fast backlash grows past threshold | Higher → faster mobilization |
| Norm drift rate | $\nu$ | 0.01–0.2 | How fast norms adapt to prevailing policy | Low → stable norm; High → ratchet effects |
| Policy delay | $k$ | 1–8 periods | Institutional response lag | **Primary driver of oscillation** |
| Backlash threshold | $\theta$ | 0.5–3.0 | Policy distance required to trigger mobilization | Lower → more frequent backlash |

### 5.4 Stability Analysis

> [!IMPORTANT]
> **This needs to be derived computationally in `notebooks/01_theory_simulation.ipynb`.** The stability boundary in $(k, \lambda)$ space — where the dominant eigenvalue of the linearized system crosses the unit circle — is the model's core mathematical deliverable.

Qualitatively, the three dynamical regimes are:

| Region | Conditions | Behavior |
|---|---|---|
| **Stable convergence** | Small $k$, small $\lambda$ | System settles to equilibrium; no persistent oscillation |
| **Sustained oscillation** | Moderate $k$, moderate $\lambda$ | Persistent pendulum swings — the target regime |
| **Divergence / instability** | Large $k$, large $\lambda$ | Explosive, unrealistic dynamics |

The Hopf bifurcation framing from the notes: as $k$ increases past a critical value (for fixed $\lambda$), the fixed point loses stability and gives way to a limit cycle. **Citing this without showing the stability analysis will attract referee criticism** — the eigenvalue conditions on the Jacobian of the linearized 5-equation system need to be shown.

---

## 6. The Seven Testable Hypotheses

### H1: Thermostatic Correction Hypothesis

**Statement:** When policy moves strongly in one direction, later public demand should move in the opposite direction.

**Formal prediction:**
$$\text{OpinionChange}_{t+1} = \alpha - \beta \cdot \text{PolicyChange}_t + \varepsilon; \quad \beta < 0$$

**Confirms:** $\hat{\beta}$ is negative and statistically significant across multiple policy domains.

**Falsifies:** Policy consistently moves one way and opinion keeps moving the same way without reversal or saturation. Or $\hat{\beta}$ is positive (opinion amplifies policy rather than correcting it).

**Empirical test:** Time-series regression of opinion change on lagged policy change, for each domain separately. Cross-domain meta-analysis of $\hat{\beta}$ estimates.

---

### H2: Lagged Overcorrection Hypothesis

**Statement:** The longer the delay between public concern and policy response, the larger the eventual swing.

**Formal prediction:** Larger $k$ → larger overshoot amplitude.

**Confirms:** States or domains with slower institutional response (higher $\hat{\tau}$) show larger subsequent opinion and policy reversals.

**Falsifies:** No relationship between response delay and swing amplitude across comparable policy episodes.

> [!IMPORTANT]
> **The delay parameter $\tau$ is not yet empirically operationalized** — this is a critical gap flagged by the Quantitative Methodologist. Proposed proxies: (a) legislative session frequency, (b) time between NCLB passage and state adoption, (c) time from opt-out petition to committee action. This MUST be operationalized to test H2.

---

### H3: Attention-Threshold Hypothesis

**Statement:** Policy will not swing merely because conditions change. It swings when attention crosses a threshold.

**Formal prediction:**
$$\text{PolicyChange}_t \approx 0 \text{ unless } A_t > \theta_{\text{attention}}$$

**Confirms:** Long flat periods in policy time series punctuated by sudden jumps; jumps are predicted by attention spikes more than by objective condition changes alone.

**Falsifies:** Policy changes continuously and proportionally to objective conditions, with no threshold effect; attention adds no predictive power beyond condition severity.

**Empirical test:** Compare GDELT/Google Trends attention spikes against timing of ESSA-era policy changes. Does high attention predict correction even when achievement signals are weak?

---

### H4: Backlash Threshold Hypothesis

**Statement:** Backlash increases nonlinearly once policy crosses a perceived "too far" point.

**Formal prediction:** $\partial B / \partial |P - N| \approx 0$ below threshold; $\partial B / \partial |P - N| > 0$ above.

**Confirms:** Nonlinear dose-response curve in survey experiment; spline regression shows breakpoint in the policy intensity → backlash relationship.

**Falsifies:** Linear relationship between policy intensity and backlash at all levels; no detectable threshold.

> [!IMPORTANT]
> **Design note from peer review:** The original notes proposed a 3-point vignette design (moderate/strong/extreme). This is insufficient to detect nonlinearity — it can only detect linear trends. Use a **5–7 point dosage design** (or continuous-dose with splines). At minimum, two intermediate conditions are needed around the hypothesized inflection point.

---

### H5: Visibility-of-Costs Hypothesis

**Statement:** A reform is more likely to trigger a pendulum swing when its costs become visible faster than its benefits.

**Formal prediction:** Policies with immediate, personal, observable costs and delayed/diffuse benefits generate stronger backlash and faster reversal pressure, controlling for policy intensity.

**Confirms:** Cross-domain comparison shows larger swings in domains with higher cost-visibility asymmetry (education testing: costs = test anxiety, teacher evaluation pressure, visible; benefits = achievement gains, slow/noisy).

**Falsifies:** Cost-visibility asymmetry shows no predictive power for swing amplitude after controlling for policy intensity.

---

### H6: Polarization Amplification Hypothesis

**Statement:** Pendulum swings should be stronger when groups stop updating from one another.

**Formal prediction:** Lower confidence bound $\epsilon$ → more polarized opinion clusters → stronger within-group swings.

**Confirms:** In simulation, reducing $\epsilon$ produces larger within-cluster swings. In empirical data, higher affective polarization (CES/ANES measures) moderates the policy-backlash relationship upward.

**Falsifies:** Polarization shows no interaction effect with policy intensity in predicting backlash.

---

### H7: Institutional Dampening Hypothesis *(the falsification anchor)*

**Statement:** Some systems should have smaller pendulum swings because they have built-in damping mechanisms.

**Damping mechanisms:** Sunset clauses, pilot programs, phased implementation, local variation, feedback review periods, bipartisan commissions, independent evaluation.

**Formal prediction:** Presence of dampening mechanisms moderates the policy intensity → backlash relationship negatively.

**Confirms:** Policies implemented with gradual feedback mechanisms show weaker backlash and less reversal than equivalent policies implemented suddenly and symbolically.

**Falsifies:** Dampening mechanisms show no effect on swing amplitude.

> [!IMPORTANT]
> **H7 is the most important hypothesis for the public-facing project.** The actionable message for practitioners is not "does the pendulum swing?" but "what stops it?" H7 should lead the policy recommendations section. It is also the project's primary falsification condition: it predicts domains or policy designs where oscillation should **not** occur. If the project only presents cases where the pendulum swings, it is cherry-picking — H7 cases are the essential counterexamples.

---

## 7. Concept-to-Model Mapping

| Pendulum concept | Academic framework | Formal mechanism |
|---|---|---|
| Pendulum swing | Delayed negative feedback | $P_{t+1} = P_t + \lambda(D_{t-k} - P_t)$ |
| Overcorrection | Control theory overshoot; Maor overreaction | Large $k$ + large $\lambda$ → overshoot |
| Public correction | Thermostatic opinion (Wlezien) | $\alpha(P_t - N_t)$ term in $D_{t+1}$ |
| Sudden flip | Threshold/cascade models (Granovetter) | $\max(0, |P_t - N_t| - \theta)$ in $B_{t+1}$ |
| Long stability then rupture | Punctuated equilibrium (Baumgartner-Jones) | Piecewise $P_{t+1}$: flat until $A_t > \theta_{\text{inst}}$ |
| Polarization/fracture | Bounded confidence (Hegselmann-Krause) | Narrow $\epsilon$ → cluster fragmentation |
| Policy creating its own backlash | Policy feedback (Pierson, Patashnik) | $B_{t+1}$ grows with $|P_t - N_t|$ |
| Mild preferences → extreme outcomes | Schelling emergent behavior | Aggregate threshold distributions |
| Norm adaptation/ratchet | New $N_t$ dynamics equation | $N_{t+1} = N_t + \nu(P_t - N_t)$ |

---

## 8. What This Theory Is NOT Claiming

See [`docs/not_saying.md`](not_saying.md) for the full treatment. Brief summary of the five most dangerous misreadings:

1. **"Both sides are equally extreme"** — The mechanism is symmetric; the content of policy swings is not evaluated by the model
2. **"The system self-corrects toward truth"** — The correction mechanism is thermostatic, not truth-seeking; it corrects toward perceived norms, which are themselves politically constructed
3. **"Radical change is always destabilizing"** — H7 shows that implementation design matters; well-designed radical change can avoid destructive backlash
4. **"Moderation is always correct"** — The model has no content position; it describes dynamics, not optimal policy levels
5. **"Advocacy is futile because backlash is inevitable"** — H7 shows it isn't inevitable; dampening conditions substantially reduce swing amplitude

---

## 9. Open Questions & Known Limitations

> [!IMPORTANT]
> **Q1: Is the pendulum a true cycle, a pulse, or a punctuated pattern?**
> These three qualitative behaviors require different modeling frameworks and make different empirical predictions. The current framework blurs all three. The project must commit to a primary claim about which dynamics dominate — or explicitly model conditions under which each applies.

> [!IMPORTANT]
> **Q2: Is backlash ever a misfiring rather than authentic corrective feedback?**
> Kuran's preference falsification suggests public opinion can cascade via social pressure even when individual preferences haven't changed. The project must empirically distinguish authentic corrective feedback from manufactured backlash. Are backlash proxies correlated with actual achievement/outcome signals, or only with media frame shifts?

> [!IMPORTANT]
> **Q3: Can the project distinguish the pendulum from simple electoral cycling?**
> The most parsimonious competitor hypothesis is partisan turnover: Republicans rolled back Obama-era education policy on partisan grounds, unrelated to any feedback mechanism. The design needs a direct falsification test: does backlash predict correction *within* party-control periods (controlling for electoral change)?

> [!IMPORTANT]
> **Q4: How does the model handle partisan polarization as a structural change?**
> If perceived norms ($N_t$) are partisan and diverging, the pendulum may be multiple simultaneous oscillations in different directions. The state-year panel with partisan controls needs to test whether backlash is bidirectional across partisan communities, not just unidirectional nationally.

> [!IMPORTANT]
> **Q5: What does non-oscillation look like, and which case is the strongest falsification test?**
> H7 predicts dampened swings, not no swings. The project needs at least one domain where the theory predicts **zero oscillation** — and that domain needs to be pre-specified, not chosen after seeing the data. Federal highway funding, actuarial insurance regulation, or other low-salience, high-institutional-friction domains are candidates.

> [!IMPORTANT]
> **Q6: What determines oscillation amplitude?**
> The theory predicts oscillation emerges but does not fully specify what determines whether the swing is small (thermostat-like) or large (major overcorrection). Amplitude is a function of $k$, $\lambda$, $\theta$, and $\sigma$ — but the relative contributions need to be mapped numerically and empirically. This is the theory's most important practical payoff.

> [!IMPORTANT]
> **Q7: How does norm divergence under polarization affect the model's predictions?**
> In a high-polarization polity, Republican and Democratic communities may perceive entirely different $N_t$ values — meaning the "pendulum" may run in opposite directions in different communities simultaneously, producing apparent national stability that masks intense within-group oscillation. The empirical design should test this directly rather than treating partisanship as merely a control variable.
