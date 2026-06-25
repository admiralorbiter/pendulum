# Annotated Literature Review

*When the Pendulum Doesn't Swing — Research Project*

---

## Introduction

This bibliography collects the core theoretical and empirical works underpinning the pendulum theory. Works are grouped by the mechanism they contribute; each entry includes the full citation, key claim, connection to the theory, central finding or equation, and known limitations. A recommended reading order and master search-term list follow.

The theory requires literature from six distinct traditions: (1) political science on opinion-policy responsiveness, (2) policy process theory on how agendas shift, (3) social movement and backlash theory, (4) formal models from physics and sociology of opinion dynamics, (5) system dynamics and control theory, and (6) the empirical education reform literature that anchors the primary test domain.

---

## Part I: Thermostatic Opinion & Policy Responsiveness

### 1. Wlezien, Christopher (1995). "The Public as Thermostat: Dynamics of Preferences for Spending." *American Journal of Political Science*, 39(4), 981–1000.

**Key Claim:** Public preferences respond negatively to policy outputs — when government spends more on something, public demand for more of it tends to decline; when government spends less, demand rises. Preferences function like a thermostat correcting for deviations from a desired temperature.

**Relevance to Pendulum Theory:** This is the foundational mechanism for $D_t$ in the formal model. The $\alpha(P_t - N_t)$ term directly formalizes Wlezien's thermostatic logic. It explains *why* opinion moves against policy direction — the most basic corrective mechanism in the system.

**Central Finding:** Using time-series regression of spending preference change on lagged spending change, Wlezien finds negative coefficients across multiple spending domains (defense, social programs). The "public as thermostat" metaphor holds empirically for most domestic spending categories tested.

**This Project's Value-Add Over Wlezien:** The thermostatic model explains *that* correction occurs and its average direction. It does not explain *amplitude variation* — why some swings are small and others massive. This project adds attention thresholds ($A_t$), identity threat ($B_t$ with threshold), and institutional delay ($k$) to explain when the thermostatic correction becomes an overshoot.

**Limitations:** Tested primarily on spending preferences, not regulatory or social policy. Does not model backlash as organized countermobilization — treats opinion change as atomized individual updating. Does not account for partisan polarization shifting the norm baseline.

**Search Terms:** `thermostatic public opinion`, `Wlezien public as thermostat`, `opinion policy responsiveness`, `spending preferences dynamics`

---

### 2. Soroka, Stuart N. & Wlezien, Christopher (2010). *Degrees of Democracy: Politics, Public Opinion, and Policy*. Cambridge University Press.

**Key Claim:** Policy responds to public preferences, and public preferences respond to policy — a bidirectional feedback loop whose strength varies systematically across institutional and issue contexts. More majoritarian systems show stronger thermostatic responsiveness.

**Relevance to Pendulum Theory:** Extends the thermostat to comparative context and explicitly models the bidirectional feedback between opinion and policy — the same feedback topology as the $D_t \leftrightarrow P_t$ system. Provides the error-correction modeling framework most directly applicable to the pendulum's empirical estimation.

**Central Finding:** Using error-correction models across 19 democracies, Soroka and Wlezien find that (a) policy responds to opinion in all democracies, and (b) opinion corrects for policy deviations, but the speed and strength of both linkages varies with electoral and institutional design.

**Limitations:** Focuses on aggregate opinion-policy cycles at the national level; does not model subnational variation in response speed (the delay parameter $k$ in our model). Does not model backlash as a distinct organized mechanism separate from diffuse thermostatic correction.

**Search Terms:** `Soroka Wlezien Degrees of Democracy`, `opinion policy responsiveness cross-national`, `error correction models policy`

---

## Part II: Punctuated Equilibrium & Policy Change

### 3. Baumgartner, Frank R. & Jones, Bryan D. (1993/2009). *Agendas and Instability in American Politics*. University of Chicago Press.

**Key Claim:** American public policy is characterized by long periods of incremental stability punctuated by occasional episodes of rapid, large-scale change. These punctuations occur when the dominant policy image changes and new venues become politically active.

**Relevance to Pendulum Theory:** Explains why real policy oscillations are not smooth — they stick for years, then snap suddenly. This is the sawtooth component of the sine-wave vs. sawtooth tension. The piecewise policy equation formalizes this: policy is quasi-static when attention is below the institutional threshold, then snaps proportionally to accumulated demand when attention breaks through.

**Central Finding:** Policy change distributions across multiple U.S. policy domains follow leptokurtic (heavy-tailed) distributions — far more very small changes and far more very large changes than a normal distribution would predict. This "punctuated" pattern is robust across issue areas and decades.

**Limitations:** Primarily descriptive rather than formally mechanistic — does not specify conditions for when punctuation will occur or predict amplitude. Does not directly model the role of public opinion as a driver (vs. elite agenda dynamics).

**Search Terms:** `punctuated equilibrium policy process`, `Baumgartner Jones agendas instability`, `leptokurtic policy change`, `punctuated equilibrium theory`

---

### 4. Jones, Bryan D. & Baumgartner, Frank R. (2005). *The Politics of Attention: How Government Prioritizes Problems*. University of Chicago Press.

**Key Claim:** Governments are disproportionate information processors — they systematically ignore weak signals about emerging problems, then overreact when those problems break through the attention threshold. This disproportionate processing is the micro-foundation of punctuated change.

**Relevance to Pendulum Theory:** Directly operationalizes H3 (attention-threshold hypothesis) and explains the mechanism behind the $A_t > \theta_{\text{inst}}$ condition in the piecewise policy equation. The "disproportionate information processing" concept maps onto Maor's policy overreaction framework.

**Central Finding:** Government budget change distributions show systematic leptokurtosis consistent with disproportionate processing. Signal detection experiments suggest that political systems require unusually strong signals before adjusting, then adjust more than the signal warrants.

**Search Terms:** `disproportionate information processing public policy`, `Jones Baumgartner politics of attention`, `agenda setting policy punctuation`

---

## Part III: Issue-Attention Cycle

### 5. Downs, Anthony (1972). "Up and Down with Ecology: The Issue-Attention Cycle." *The Public Interest*, 28, 38–50.

**Key Claim:** Public attention to most social problems follows a characteristic five-stage cycle: pre-problem stage → alarmed discovery → realizing the cost of progress → gradual decline of intense interest → post-problem stage. This cycle occurs independent of whether the underlying problem is actually solved.

**Relevance to Pendulum Theory:** Directly informs the attention equation: $A_{t+1} = (1-\delta)A_t + \varphi|P_t - N_t| + \text{shock}_t$. The $(1-\delta)$ decay term formalizes the natural attention decline of Stages 4–5. It explains why backlash pressure eventually dissipates even when underlying grievances persist — which is what allows the system to eventually stabilize (or cycle again from a different position).

**Central Finding:** The ecology issue (environmental concerns) spiked dramatically in the late 1960s, then declined sharply by the early 1970s — despite the underlying environmental problems remaining unchanged or worsening. The mechanism: once the public encountered the cost and complexity of environmental reform, interest decayed.

**Limitations:** Primarily descriptive; does not formalize the mechanism or connect it to policy outcomes. Does not account for how media structure or political polarization changes the cycle dynamics.

**Search Terms:** `Downs issue-attention cycle`, `public attention policy cycles`, `media salience issue attention`

---

## Part IV: Policy Feedback Theory

### 6. Pierson, Paul (1993). "When Effect Becomes Cause: Policy Feedback and Political Change." *World Politics*, 45(4), 595–628.

**Key Claim:** Policies do not merely respond to politics — they reshape the politics that subsequently evaluate them. Policies alter resources, incentives, and how actors interpret the political world, thereby changing the conditions under which future policy fights occur.

**Relevance to Pendulum Theory:** Explains why each swing of the pendulum changes the conditions for the next swing. Policy feedback is why the political environment at time $t+k$ is not the same as at time $t$ — the policy itself, through its resource and interpretive effects, has reorganized who is mobilized, what elites say, and how the issue is framed. This is the mechanism behind why correction often overshoots: the policy has changed the political landscape.

**Two channels:**
1. *Resource/incentive effects:* Policies create and destroy interests — NCLB created a testing industry with lobbying resources; opt-out created parent-activist networks
2. *Interpretive effects:* Policies change how actors understand the state — NCLB's "failing schools" label changed how parents and communities understood school quality

**Limitations:** Primarily a theoretical argument with illustrative case studies. Doesn't formally model the dynamics of feedback timing or specify when feedback will amplify vs. dampen political mobilization.

**Search Terms:** `policy feedback theory Pierson`, `policies shape politics`, `historical institutionalism policy feedback`

---

### 7. Patashnik, Eric M. (2008). *Reforms at Risk: What Happens After Major Policy Changes Are Enacted*. Princeton University Press. AND Patashnik, Eric M. (2023). *Countermobilization: Policy Feedback and Backlash in a Polarized Age*. Princeton University Press.

**Key Claim (Reforms at Risk):** Many major policy reforms are undermined after enactment by the very interests they sought to reform. Whether a reform survives depends on whether it successfully transforms the political landscape — creating new constituencies, reorganizing interests — or leaves concentrated losers intact with resources and incentives to fight back.

**Key Claim (Countermobilization):** In a polarized age, backlash risk rises when policies impose concentrated losses on organized groups, challenge deeply held arrangements, or appear to exceed public sympathy for affected groups. Countermobilization is now a predictable feature of the policy reform process, not an anomaly.

**Relevance to Pendulum Theory:** Patashnik is the political scientist closest to the project's central claim. *Reforms at Risk* provides the empirical taxonomy of which reforms survive backlash (those that restructure interests) vs. which don't (those that leave concentrated losers intact). This maps directly to H5 (visibility of costs) and H7 (institutional dampening): reforms that make benefits visible and restructure incentives are more resistant to reversal.

**Concentrated losers / diffuse beneficiaries:** This is the central mechanism for H5. When reform costs are concentrated on organized groups (teachers, testing companies, local officials) and benefits are diffuse and delayed (achievement gains for abstract future students), the politics strongly favor reversal.

**Search Terms:** `Patashnik reforms at risk`, `Patashnik countermobilization`, `policy reform survival backlash`, `concentrated losers diffuse beneficiaries`

---

## Part V: Backlash & Countermovement Theory

### 8. Meyer, David S. & Staggenborg, Suzanne (1996). "Movements, Countermovements, and the Structure of Political Opportunity." *American Journal of Sociology*, 101(6), 1628–1660.

**Key Claim:** Countermovement emergence is a predictable feature of social movement activity, not an anomaly. When movements partially succeed — especially when the state partly satisfies but does not fully resolve challenger demands — they create the organizational infrastructure and symbolic targets that mobilize countermovements.

**Relevance to Pendulum Theory:** Explains the *organized* component of $B_t$ — the mechanism by which diffuse individual dissatisfaction becomes coordinated political action. Partial reform success (NCLB passing some accountability measures but leaving teachers, parents, and local officials bearing costs) created exactly the conditions Meyer and Staggenborg describe.

**Search Terms:** `countermovement theory`, `movement countermovement interaction Meyer Staggenborg`, `social movement political opportunity structure`

---

### 9. Mansbridge, Jane & Shames, Shauna (2008). "Toward a Theory of Backlash: Dynamic Resistance and the Central Role of Power." *Politics & Gender*, 4(4), 623–634.

**Key Claim:** Backlash is best understood as resistance by actors who perceive a loss or threat to power, not merely as conservative reaction to progressive change. The key variable is perceived power threat, not the content of the policy.

**Relevance to Pendulum Theory:** Crucial for H4 (backlash threshold) and the identity-threat component of $B_t$. Backlash is not simply a function of how far policy moves from a norm — it is conditioned by whether affected groups perceive the movement as threatening their status, power, or identity. This explains why backlash can be disproportionate to the "objective" policy change.

**Search Terms:** `backlash theory politics Mansbridge`, `status threat backlash`, `power threat political resistance`

---

### 10. Kuran, Timur (1995). *Private Truths, Public Lies: The Social Consequences of Preference Falsification*. Harvard University Press.

**Key Claim:** People often publicly misrepresent their preferences when they perceive that expressing their true preferences would be socially costly. This preference falsification can suddenly cascade when enough people sense that others are also falsifying — producing rapid, apparently sudden shifts in public opinion that have little to do with actual changes in underlying individual preferences.

**Relevance to Pendulum Theory:** Introduces a critical complication for the theory's causal claims. If backlash can spread via cascade even when underlying individual preferences haven't changed, then "backlash" measured by polls or media attention may not reflect authentic corrective feedback — it may reflect social preference cascades. This is the "manufactured vs. authentic backlash" problem the project must address empirically: are backlash proxies correlated with actual policy costs, or only with elite-manufactured signals?

**Search Terms:** `preference falsification Kuran`, `social cascade opinion change`, `preference cascade political opinion`

---

## Part VI: Policy Overreaction & Underreaction

### 11. Maor, Moshe (2012). "Policy Overreaction." *Journal of Public Policy*, 32(3), 231–259. AND Maor, Moshe (Ed., 2017). *Organizational Reputation and the Disproportionality Bias: Over- and Underreaction in Public Administration*. Routledge.

**Key Claim:** Governments exhibit systematic patterns of disproportionate policy response — underreacting to problems for extended periods, then overreacting once issues become politically salient. Overreaction is defined in terms of disproportionate responses that generate excessive objective or perceived social costs.

**Relevance to Pendulum Theory:** This is the closest existing literature to the project's core claim. Maor's "policy overreaction" is the "swing goes too far" mechanism. The oscillation between underreaction (long flat period) and overreaction (large swing, followed by backlash) is structurally equivalent to the pendulum model's behavior in the moderate-delay, threshold-triggered regime.

**Vocabulary:** "Policy bubbles" (policies expanding beyond optimal level before collapsing), "emotional policy entrepreneurship" (amplification of signals beyond their informational content), "disproportionate information processing" (connection to Baumgartner-Jones).

**Search Terms:** `policy overreaction Maor`, `disproportionate policy response`, `policy bubbles`, `policy underreaction`

---

## Part VII: Opinion Dynamics & Formal Models

### 12. Hegselmann, Rainer & Krause, Ulrich (2002). "Opinion Dynamics and Bounded Confidence Models, Analysis, and Simulation." *Journal of Artificial Societies and Social Simulation*, 5(3).

**Key Claim:** When agents only update their opinions based on others whose opinions are within a "confidence bound" $\epsilon$ of their own, the population can produce consensus (high $\epsilon$), polarization into two camps (moderate $\epsilon$), or fragmentation into multiple clusters (low $\epsilon$).

**Relevance to Pendulum Theory:** The micro-foundation for H6 (polarization amplification). In low-$\epsilon$ environments (high affective polarization), groups stop updating from one another, producing entrenched opinion clusters that generate stronger within-group swings. This is also the connection between the ABM design and empirical polarization data.

**Formal model:**
$$x_i(t+1) = \frac{1}{|N_i(t)|} \sum_{j \in N_i(t)} x_j(t), \quad N_i(t) = \{j : |x_i(t) - x_j(t)| \leq \epsilon\}$$

**Search Terms:** `bounded confidence opinion dynamics`, `Hegselmann Krause model`, `opinion clustering polarization model`

---

### 13. Deffuant, Guillaume, Neau, David, Amblard, Frédéric & Weisbuch, Gérard (2000). "Mixing Beliefs Among Interacting Agents." *Advances in Complex Systems*, 3, 87–98.

**Key Claim:** In continuous opinion models where agents interact pairwise and update toward each other only if their opinions are within a threshold $\mu$, the long-run equilibrium is either consensus or polarized clusters depending on the threshold value and initial opinion distribution.

**Relevance to Pendulum Theory:** Alternative bounded-confidence model to Hegselmann-Krause; has been more thoroughly analyzed for convergence properties. Useful as the ABM's baseline comparison for opinion dynamics results.

**Search Terms:** `Deffuant Weisbuch opinion dynamics`, `continuous opinion dynamics bounded confidence`

---

### 14. Granovetter, Mark (1978). "Threshold Models of Collective Behavior." *American Journal of Sociology*, 83(6), 1420–1443.

**Key Claim:** Many social behaviors — riots, strikes, voting, fads — follow threshold dynamics: individuals join a behavior once enough others have done so. The distribution of thresholds across a population determines whether small initial shocks produce small responses or large cascades.

**Relevance to Pendulum Theory:** The `max(0, |P_t - N_t| - θ)` term in the $B_t$ equation is a population-level formalization of Granovetter's threshold idea. The threshold $\theta$ is the point above which backlash mobilization begins. More formally, the distribution of individual thresholds across the population determines the shape of the backlash response function — a uniform distribution produces a linear response above threshold; a clustered distribution produces a sharper nonlinear jump.

**Critical for H4:** The backlash threshold hypothesis predicts that the aggregate backlash response is nonlinear (threshold-triggered), which requires that individual thresholds are distributed in a way that produces aggregate nonlinearity.

**Search Terms:** `Granovetter threshold model collective behavior`, `social cascade threshold`, `riot model collective action`

---

### 15. Schelling, Thomas C. (1971). "Dynamic Models of Segregation." *Journal of Mathematical Sociology*, 1(2), 143–186. AND Schelling, Thomas C. (1978). *Micromotives and Macrobehavior*. Norton.

**Key Claim:** Mild individual preferences for neighbors of similar type can produce extreme collective segregation. The key insight: macro outcomes need not reflect extreme individual preferences — they can emerge from modest local rules through tipping dynamics.

**Relevance to Pendulum Theory:** Provides the micro-to-macro bridging insight. Pendulum swings may not require most people to become extreme; they can emerge from modest local updating rules when social networks are structured appropriately. This is important for the ABM design: the macro oscillation can emerge from agents with moderate individual thresholds if the network structure channels interactions.

**Search Terms:** `Schelling dynamic models segregation`, `micromotives macrobehavior`, `tipping model social dynamics`, `emergent polarization agent-based`

---

### 16. Castellano, Claudio, Fortunato, Santo & Loreto, Vittorio (2009). "Statistical Physics of Social Dynamics." *Reviews of Modern Physics*, 81(2), 591–646.

**Key Claim:** Tools from statistical physics — Ising models, voter models, surface-tension dynamics — can be applied to model opinion dynamics, cultural dynamics, language dynamics, crowd behavior, and social spreading. The review synthesizes bounded-confidence models, voter models, and related traditions.

**Relevance to Pendulum Theory:** The broadest scientific overview of the opinion dynamics literature. Useful for locating the Hegselmann-Krause and Deffuant models within the larger landscape of formal social dynamics. Also reviews methods (agent-based simulation, Monte Carlo, density-based equations) applicable to the project's simulation design.

**Search Terms:** `statistical physics social dynamics`, `voter model opinion dynamics`, `Ising model opinion dynamics`, `Castellano Fortunato Loreto`

---

## Part VIII: System Dynamics & Control Theory

### 17. Sterman, John D. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World*. McGraw-Hill. AND Sterman, John D. (1994). "Learning in and About Complex Systems." *System Dynamics Review*, 10(2–3), 291–330. AND Sterman, John D. (1989). "Misperceptions of Feedback in Dynamic Decision Making." *Organizational Behavior and Human Decision Processes*, 43(3), 301–335.

**Key Claim (Business Dynamics):** Complex social and business systems can be understood through stocks, flows, feedback loops, nonlinearities, and time delays. Oscillation, boom-bust cycles, and policy resistance are emergent properties of feedback architecture, not evidence of irrationality.

**Key Claim (Misperceptions):** People systematically misread feedback in complex dynamic systems — they misattribute internally generated dynamics to outside shocks, underestimate time delays, and respond in ways that amplify rather than dampen instability.

**Relevance to Pendulum Theory:** System dynamics is the most mature computational tradition for modeling the kind of feedback-delay-oscillation dynamics the theory describes. The "misperceptions of feedback" finding is directly relevant to why politicians and the public respond to policy dynamics in ways that amplify swings: they don't understand they're looking at delayed feedback from their own prior actions.

The system dynamics vocabulary (stocks = $P_t$, $D_t$, $B_t$; flows = rates of change; feedback loops; time delays) provides a visual and computational language for the model.

**Search Terms:** `system dynamics policy feedback delay oscillation`, `Sterman misperceptions feedback`, `Forrester social systems feedback`, `business dynamics systems thinking`

---

### 18. Forrester, Jay W. (1971). *World Dynamics*. Wright-Allen Press. AND Forrester, Jay W. (1969). *Urban Dynamics*. MIT Press.

**Key Claim:** Complex social systems (urban systems, world population-resource systems) have counterintuitive behaviors because of their feedback structure. Policies that seem locally sensible often produce system-level oscillation or collapse because they fail to account for delayed feedback effects.

**Relevance to Pendulum Theory:** Foundational to the system dynamics tradition. Forrester's insight that "well-intentioned policies backfire due to delayed feedback" is structurally equivalent to the core claim of the pendulum theory. The urban dynamics work specifically models how policy interventions (urban renewal, housing programs) generate unexpected backlash dynamics.

**Search Terms:** `Forrester system dynamics`, `urban dynamics feedback loops`, `world dynamics counterintuitive behavior`

---

## Part IX: Education Reform Empirical Literature

### 19. McGuinn, Patrick J. — Obama-Era Federal Reform and Political Backlash

**Key Claim:** Aggressive federal education reform efforts during the Obama administration (Race to the Top, NCLB waivers, Common Core promotion) produced political backlash against both the specific reforms and federal involvement in education more broadly, contributing to the ESSA settlement that rolled back the federal role.

**Relevance to Pendulum Theory:** Provides the political mechanism for the NCLB→ESSA correction. Shows that federal overreach (in the view of both left and right) mobilized a cross-ideological coalition that ultimately produced ESSA decentralization — a textbook Pierson-style policy feedback story.

**Search Terms:** `McGuinn education reform backlash federal`, `Race to Top political backlash`, `Common Core federal involvement`

---

### 20. Kornhaber, Mindy, et al. — Common Core: Elite Support to Grassroots Conflict

**Key Claim:** Common Core began with unusually strong elite consensus (business groups, governors, civil rights organizations) but came under attack from a wide ideological range of politicians and interest groups. Ground-level reactions from parents, educators, and communities disrupted state-level support.

**Relevance to Pendulum Theory:** Documents the threshold-crossing backlash dynamic empirically. Common Core's collapse of elite support was not gradual — it was rapid and involved strange-bedfellow coalitions (Tea Party conservatives + progressive educators). This is the Granovetter cascade in real political time.

**Search Terms:** `Common Core backlash political opposition`, `Kornhaber Common Core`, `standards movement political opposition`

---

### 21. Portz, John & Beauchamp, Zach — ESSA State Redesign Variation

**Key Claim:** ESSA opened substantial space for state redesign and states responded in measurably different ways — on indicator selection, rating systems, and treatment of traditional test-based metrics. This variation reflects heterogeneous state backlash intensities and political contexts.

**Relevance to Pendulum Theory:** Documents the policy correction phase (post-ESSA) and its cross-state variation — exactly the dependent variable the empirical panel study needs to explain.

---

### 22. NBER Working Paper — NCLB-to-ESSA as Decentralization Shock

**Key Claim:** The NCLB-to-ESSA transition constitutes a measurable decentralization shock. States with stronger pre-ESSA test-based accountability retreated from output-based teacher policy after ESSA, and this retreat is associated with lower subsequent achievement growth in the authors' estimates.

**Relevance to Pendulum Theory:** Provides the cleanest empirical estimate of the ESSA flexibility shock and its consequences. The finding that post-ESSA correction is associated with achievement costs is directly relevant to whether the pendulum "overcorrects" — if states retreat too far from accountability, outcomes suffer.

---

## Recommended Reading Order

### Stage 1: Core Theory (Week 1–2)
1. Wlezien (1995) — thermostatic model
2. Pierson (1993) — policy feedback
3. Downs (1972) — issue-attention cycle
4. Granovetter (1978) — threshold models

### Stage 2: Formal Models (Week 3–4)
5. Hegselmann & Krause (2002) — bounded confidence
6. Sterman (2000) chapters on feedback and delay (Part II)
7. Baumgartner & Jones (1993) chapters 1–4

### Stage 3: Backlash & Correction (Week 5–6)
8. Patashnik (2008) — *Reforms at Risk*
9. Meyer & Staggenborg (1996)
10. Maor (2012) — policy overreaction
11. Patashnik (2023) — *Countermobilization*

### Stage 4: Education Domain (Week 7)
12. McGuinn on Obama-era backlash
13. Kornhaber et al. on Common Core
14. NBER working paper on ESSA decentralization
15. Soroka & Wlezien (2010) chapters 1–3

### Stage 5: Broader Formal Literature (as needed)
16. Schelling (1978)
17. Castellano, Fortunato & Loreto (2009) — survey of physics approaches
18. Kuran (1995)

---

## Master Search Terms List

### Thermostatic Opinion
- `thermostatic public opinion`
- `Wlezien public as thermostat`
- `Soroka Wlezien Degrees of Democracy`
- `opinion policy responsiveness error correction`
- `spending preferences dynamics time series`

### Punctuated Equilibrium
- `punctuated equilibrium policy process`
- `Baumgartner Jones agendas instability`
- `leptokurtic policy change distributions`
- `disproportionate information processing public policy`
- `agenda setting policy punctuation`

### Issue-Attention Cycle
- `Downs issue-attention cycle`
- `public attention policy cycles`
- `media salience issue attention`
- `attention decay public opinion`

### Policy Feedback
- `policy feedback theory Pierson`
- `policies shape politics historical institutionalism`
- `Patashnik reforms at risk`
- `Patashnik countermobilization`
- `concentrated losers diffuse beneficiaries backlash`

### Backlash & Countermovement
- `backlash theory politics`
- `countermovement theory Meyer Staggenborg`
- `movement countermovement political opportunity`
- `status threat backlash Mansbridge`
- `preference falsification Kuran`
- `social cascade opinion change`

### Policy Overreaction
- `policy overreaction Maor`
- `policy underreaction disproportionate response`
- `policy bubbles public policy`
- `emotional policy entrepreneurship`

### Opinion Dynamics
- `bounded confidence opinion dynamics`
- `Hegselmann Krause model`
- `Deffuant Weisbuch opinion dynamics`
- `voter model opinion dynamics`
- `Ising model social dynamics`
- `Castellano Fortunato Loreto statistical physics social dynamics`
- `Granovetter threshold model collective behavior`
- `social cascade threshold tipping`
- `Schelling dynamic models segregation`
- `micromotives macrobehavior emergent outcomes`

### System Dynamics & Control Theory
- `system dynamics policy feedback delay oscillation`
- `Sterman misperceptions feedback dynamic decision making`
- `Forrester social systems feedback loops`
- `delayed negative feedback oscillation`
- `delay differential equations Hopf bifurcation`
- `control theory overshoot settling time`
- `feedback control systems damping`

### Education Reform Empirical
- `No Child Left Behind accountability backlash`
- `Common Core political opposition`
- `Every Student Succeeds Act state flexibility`
- `opt-out testing movement social movement`
- `education accountability pendulum`
- `NCLB ESSA transition decentralization`
- `Race to the Top political consequences`
