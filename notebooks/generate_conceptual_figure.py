import matplotlib.pyplot as plt
import numpy as np

# Set style for professional look
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, axes = plt.subplots(1, 2, figsize=(12, 5), dpi=300)

# -- PANEL A: Conceptual Flowchart --------------------------------------
ax_flow = axes[0]
ax_flow.set_title("A. Conceptual Framework: The Institutional Filter", fontsize=12, fontweight='bold', pad=15)
ax_flow.axis('off')

# Draw boxes
bbox_props = dict(boxstyle="round,pad=0.5", fc="#f8f9fa", ec="#ced4da", lw=1.5)
bbox_open = dict(boxstyle="round,pad=0.5", fc="#e7f5ff", ec="#228be6", lw=2)
bbox_damp = dict(boxstyle="round,pad=0.5", fc="#f1f3f5", ec="#868e96", lw=2)
bbox_block = dict(boxstyle="round,pad=0.5", fc="#fff5f5", ec="#fa5252", lw=2)

# Text positions
ax_flow.text(0.1, 0.75, "Backlash Signal\n(Mass Opt-Out)", ha="center", va="center", size=10, fontweight="bold", bbox=bbox_props)
ax_flow.text(0.5, 0.75, "Institutional Pathway\n(Waivers, Calendars)", ha="center", va="center", size=10, fontweight="bold", bbox=bbox_props)
ax_flow.text(0.9, 0.75, "Policy Correction\n(Rollback)", ha="center", va="center", size=10, fontweight="bold", bbox=bbox_props)

# Draw main arrows
ax_flow.annotate("", xy=(0.33, 0.75), xytext=(0.23, 0.75), arrowprops=dict(arrowstyle="->", lw=2, color="#495057"))
ax_flow.annotate("", xy=(0.77, 0.75), xytext=(0.67, 0.75), arrowprops=dict(arrowstyle="->", lw=2, color="#495057"))

# Draw 3 regimes below
ax_flow.text(0.5, 0.5, "1. Pathway Open\n(φ_F = 0)", ha="center", va="center", size=9, bbox=bbox_open)
ax_flow.text(0.5, 0.3, "2. Pathway Damped\n(φ_F moderate)", ha="center", va="center", size=9, bbox=bbox_damp)
ax_flow.text(0.5, 0.1, "3. Pathway Blocked\n(φ_F → ∞)", ha="center", va="center", size=9, bbox=bbox_block)

# Draw connections from pathway to outcomes
ax_flow.annotate("Pendulum Swings", xy=(0.85, 0.55), xytext=(0.65, 0.5), ha="center",
                 arrowprops=dict(arrowstyle="->", lw=1.5, color="#228be6", connectionstyle="arc3,rad=-0.1"))
ax_flow.annotate("Low-Amplitude Drift", xy=(0.85, 0.4), xytext=(0.65, 0.3), ha="center",
                 arrowprops=dict(arrowstyle="->", lw=1.5, color="#868e96"))
ax_flow.annotate("Pinned Pendulum", xy=(0.85, 0.25), xytext=(0.65, 0.1), ha="center",
                 arrowprops=dict(arrowstyle="->", lw=1.5, color="#fa5252", connectionstyle="arc3,rad=0.1"))


# -- PANEL B: Simulated Trajectories ------------------------------------
ax_sim = axes[1]
ax_sim.set_title("B. Simulated Policy Trajectories", fontsize=12, fontweight='bold', pad=15)

t = np.linspace(0, 15, 300)

# 1. Free Pendulum (oscillating and correcting)
# Simulate overshoot and correction after initial backlash at t=3
y_free = np.zeros_like(t)
y_free[t < 3] = 1.0
y_free[t >= 3] = 1.0 - 1.5 * np.sin(0.4 * (t[t >= 3] - 3)) * np.exp(-0.15 * (t[t >= 3] - 3))

# 2. Frictionally Damped (slow, low-amplitude correction)
y_damp = np.zeros_like(t)
y_damp[t < 3] = 1.0
y_damp[t >= 3] = 1.0 - 0.4 * (1 - np.exp(-0.2 * (t[t >= 3] - 3)))

# 3. Pinned Pendulum (locked in, no correction)
y_locked = np.ones_like(t)

ax_sim.plot(t, y_free, label="Pathway Open: Free Pendulum (Texas)", color="#228be6", lw=2.5)
ax_sim.plot(t, y_damp, label="Pathway Damped: Frictionally Damped (Biennial)", color="#868e96", lw=2.5, linestyle="--")
ax_sim.plot(t, y_locked, label="Pathway Blocked: Pinned Pendulum (Waivers)", color="#fa5252", lw=2.5, linestyle="-.")

# Aesthetics
ax_sim.set_xlabel("Time (Years)", fontsize=10)
ax_sim.set_ylabel("Policy Intensity", fontsize=10)
ax_sim.axvline(3, color="#495057", linestyle=":", alpha=0.7)
ax_sim.text(3.2, 0.1, "Backlash Begins", fontsize=9, color="#495057")

ax_sim.set_ylim(-0.8, 1.3)
ax_sim.legend(loc="lower left", frameon=True, facecolor="white", edgecolor="#ced4da", fontsize=9)

plt.tight_layout()
plt.savefig("reports/conceptual_framework.png", bbox_inches='tight', dpi=300)
print("Saved reports/conceptual_framework.png successfully!")
