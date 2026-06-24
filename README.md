# The Pendulum Always Swings

> *When Feedback Is Delayed* — A theory and empirical study of policy-perception oscillation

[![Status](https://img.shields.io/badge/status-active%20research-blue)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## What This Project Is

This project investigates why public perception and policy oscillate — why reform often swings too far, triggers backlash, overcorrects, and swings again. It combines formal theory, mathematical simulation, and empirical panel analysis across multiple U.S. policy domains.

**The short version:**

> Policy-perception pendulums emerge from delayed corrective feedback in systems shaped by attention cycles, institutional friction, and backlash amplification. They are not random. They are not inevitable. They are what you get when feedback is delayed, costs are visible before benefits, attention spikes past thresholds, and groups perceive the change as overreach.

This is **not** an argument that both sides are equivalent, that moderation is always correct, or that the system self-corrects toward truth. See [`docs/not_saying.md`](docs/not_saying.md) for the explicit rebuttal of those misreadings.

---

## Project Structure

```
pendulum/
├── README.md                        # This file
├── requirements.txt                 # Python dependencies
│
├── docs/                            # Research documentation
│   ├── theory.md                    # Full formalized theory, model, hypotheses
│   ├── literature.md                # Annotated bibliography
│   ├── data_sources.md              # All datasets: access, variables, limitations
│   ├── empirical_design.md          # Estimating equations, identification strategy
│   ├── research_roadmap.md          # Phase-by-phase research plan
│   └── not_saying.md                # What this theory is NOT claiming
│
├── notebooks/                       # Jupyter analysis notebooks
│   ├── 00_setup.ipynb               # Environment setup & verification
│   ├── 01_theory_simulation.ipynb   # Toy model: D/P/A/B/N dynamics
│   ├── 02_agent_based_model.ipynb   # Agent-based simulation
│   ├── 03_data_collection.ipynb     # Pull all raw data sources
│   ├── 04_data_cleaning.ipynb       # Build state-year panel
│   ├── 05_eda.ipynb                 # Exploratory data analysis
│   ├── 06_backlash_index.ipynb      # Build composite backlash index
│   ├── 07_panel_regression.ipynb    # FE models, panel VAR, Granger tests
│   └── 08_results_visualization.ipynb # Final plots and tables
│
├── data/
│   ├── raw/                         # Downloaded raw files (see .gitignore)
│   └── processed/                   # Cleaned, merged panel datasets
│
├── src/                             # Reusable Python modules
│   └── (pendulum model utilities)
│
└── notes/                           # Original research notes
    ├── The Pendulum Always Swings.md
    └── deep-research-report.md
```

---

## The Theory in One Paragraph

Public demand ($D_t$) adjusts against policy ($P_t$) when policy is perceived as too far from a norm ($N_t$) — but policy responds to demand with a lag ($k$). Attention ($A_t$) amplifies both correction and backlash ($B_t$), but decays over time (Downs's issue-attention cycle). Backlash mobilizes nonlinearly: it accelerates only after policy crosses a perceived threshold. When these four forces interact with delayed feedback, the result is not random swinging but **patterned oscillation** — the amplitude and frequency determined by the delay, the correction strength, the backlash threshold, and the institutional damping built into the system.

$$D_{t+1} = D_t - \alpha(P_t - N_t) + \beta A_t - \gamma B_t + \varepsilon_t$$
$$P_{t+1} = P_t + \lambda(D_{t-k} - P_t) + \mu A_t + \eta_t$$
$$A_{t+1} = (1-\delta)A_t + \varphi|P_t - N_t| + \text{shock}_t$$
$$B_{t+1} = \rho B_t + \sigma \max(0, |P_t - N_t| - \theta)$$
$$N_{t+1} = N_t + \nu(P_t - N_t) + \eta_N$$

The norm $N_t$ drifts slowly toward prevailing policy — a ratchet effect that shifts the attractor over time.

---

## Primary Test Domain

**U.S. Education Reform, 2010–2024**

The NCLB → Common Core → opt-out → ESSA sequence is the cleanest observable policy pendulum in recent domestic U.S. policy: a clear intensity shock, visible costs (testing burden, federal overreach), threshold-crossing backlash (opt-out normalization), and a documented institutional correction (ESSA flexibility).

**State-year panel**: ~50 states × 14 years. Key question:

> Did states with stronger pre-ESSA test-based accountability experience larger subsequent backlash and adopt less test-centric accountability designs after ESSA?

### Additional Domains (planned)
| Domain | Key swing | Status |
|---|---|---|
| Policing reform | 2015–2020 reform → post-2020 reversal | Planned |
| Immigration policy | Multiple cycles | Planned |
| Climate policy | Attention cycles, international withdrawal | Planned |
| **Non-oscillating case** | e.g., federal highway funding | Required falsification case |

---

## Seven Testable Hypotheses

| Hypothesis | Short form | Direction |
|---|---|---|
| H1 | Thermostatic correction | $\beta < 0$: opinion moves against policy |
| H2 | Lagged overcorrection | Larger delay $k$ → larger swing |
| H3 | Attention threshold | Policy change only after attention crosses threshold |
| H4 | Backlash threshold | Backlash jumps nonlinearly (not linearly) with policy intensity |
| H5 | Visibility of costs | Visible-cost policies → faster, stronger backlash |
| H6 | Polarization amplification | Narrower group confidence bounds → larger within-group swings |
| H7 | Institutional dampening | Phased rollout, sunset clauses → smaller swings |

H7 is the **falsification anchor**: it predicts which systems should *not* oscillate.

---

## Two Research Tracks (Running in Parallel)

### Track A — Simulation
- `notebooks/01_theory_simulation.ipynb` — Toy model parameter sweeps; stability boundary in $(k, \lambda)$ space
- `notebooks/02_agent_based_model.ipynb` — Agent-based bounded-confidence + threshold mobilization

### Track B — Empirical Panel
- `notebooks/03–08` — Data collection → panel construction → regression → results

The simulation is not a "parallel project" — it is a **parameter identification tool** for the empirical work. Simulation findings motivate specific empirical predictions; empirical patterns calibrate simulation parameter ranges.

---

## Quick Start

```bash
# Clone and set up
git clone https://github.com/[your-repo]/pendulum.git
cd pendulum

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

Start with `notebooks/00_setup.ipynb` to verify your environment, then `notebooks/01_theory_simulation.ipynb` to explore the model dynamics.

---

## Key Documents

| Document | Purpose |
|---|---|
| [`docs/theory.md`](docs/theory.md) | Full theory: frameworks, model, hypotheses |
| [`docs/literature.md`](docs/literature.md) | Annotated bibliography |
| [`docs/data_sources.md`](docs/data_sources.md) | Every dataset with access instructions |
| [`docs/empirical_design.md`](docs/empirical_design.md) | Estimating equations, identification strategy |
| [`docs/research_roadmap.md`](docs/research_roadmap.md) | What to pull, in what order, what to look for |
| [`docs/not_saying.md`](docs/not_saying.md) | What this theory is NOT claiming |

---

## What This Theory Is NOT

Before using or citing this project, please read [`docs/not_saying.md`](docs/not_saying.md). This framework is not:
- An argument that both political sides are equivalent
- A claim that the system self-corrects toward truth
- An argument that radical change is always destabilizing
- A claim that moderation is always correct
- A suggestion that advocacy is futile because backlash is inevitable

---

## Citation

[Citation placeholder — to be added upon publication]

---

## License

MIT License. See `LICENSE` for details.
