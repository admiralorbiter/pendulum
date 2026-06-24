import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Any, List, Tuple, Optional

class PendulumSimulation:
    """
    Implements the 5-equation policy-perception oscillation model.
    Includes adaptive norm (N_t) dynamics, delayed policy feedback (tau), 
    nonlinear backlash thresholds (theta), and attention gating (theta_inst).
    """
    
    def __init__(
        self,
        alpha: float = 0.15,      # Demand sensitivity to policy-norm gap
        beta: float = 0.05,       # Demand sensitivity to attention
        gamma: float = 0.10,      # Demand sensitivity to backlash
        lambda_: float = 0.20,    # Policy correction rate (response speed)
        tau: int = 2,             # Policy feedback delay lag
        mu: float = 0.02,         # Policy sensitivity to attention
        delta: float = 0.30,      # Attention decay rate
        phi: float = 0.25,        # Attention sensitivity to policy-norm gap
        rho: float = 0.70,        # Backlash persistence/decay
        sigma: float = 0.40,      # Backlash growth sensitivity to threshold breach
        theta: float = 1.00,      # Backlash threshold (opinion distance)
        theta_inst: float = 0.00, # Attention threshold for institutional response
        nu: float = 0.08,         # Norm adaptation rate
        noise_std: float = 0.00   # Standard deviation of Gaussian shocks
    ):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.lambda_ = lambda_
        self.tau = tau
        self.mu = mu
        self.delta = delta
        self.phi = phi
        self.rho = rho
        self.sigma = sigma
        self.theta = theta
        self.theta_inst = theta_inst
        self.nu = nu
        self.noise_std = noise_std
        
        # State history variables
        self.history: Optional[Dict[str, List[float]]] = None

    @classmethod
    def from_scenario(cls, name: str) -> "PendulumSimulation":
        """
        Factory method to instantiate a simulation with pre-configured parameters
        representing different theoretical regimes/scenarios.
        """
        scenarios = {
            "stable_convergence": cls(tau=0, lambda_=0.15, alpha=0.1, beta=0.0, gamma=0.0, nu=0.05),
            "sustained_oscillation": cls(tau=3, lambda_=0.40, alpha=0.2, beta=0.05, gamma=0.15, theta=0.8, nu=0.05),
            "punctuated_sawtooth": cls(tau=2, lambda_=0.50, alpha=0.15, beta=0.1, gamma=0.25, theta=1.2, theta_inst=0.4, nu=0.02),
            "highly_damped": cls(tau=1, lambda_=0.10, alpha=0.05, beta=0.0, gamma=0.05, nu=0.20),
            "unstable_divergence": cls(tau=5, lambda_=0.70, alpha=0.3, beta=0.1, gamma=0.3, theta=0.5, nu=0.01)
        }
        if name not in scenarios:
            raise ValueError(f"Unknown scenario name: '{name}'. Available: {list(scenarios.keys())}")
        return scenarios[name]

    def run(
        self,
        steps: int = 100,
        initial_state: Optional[Dict[str, float]] = None
    ) -> Dict[str, List[float]]:
        """
        Runs the simulation for a specified number of steps starting from an initial state.
        
        initial_state keys: 'D', 'P', 'A', 'B', 'N'
        """
        if initial_state is None:
            initial_state = {"D": 1.0, "P": 0.0, "A": 0.0, "B": 0.0, "N": 0.0}
            
        D = [initial_state.get("D", 0.0)]
        P = [initial_state.get("P", 0.0)]
        A = [initial_state.get("A", 0.0)]
        B = [initial_state.get("B", 0.0)]
        N = [initial_state.get("N", 0.0)]
        
        for t in range(steps):
            # Generate shocks (Gaussian noise if noise_std > 0)
            e_D = np.random.normal(0, self.noise_std) if self.noise_std > 0 else 0.0
            e_P = np.random.normal(0, self.noise_std) if self.noise_std > 0 else 0.0
            e_A = np.random.normal(0, self.noise_std) if self.noise_std > 0 else 0.0
            e_B = np.random.normal(0, self.noise_std) if self.noise_std > 0 else 0.0
            e_N = np.random.normal(0, self.noise_std) if self.noise_std > 0 else 0.0
            
            # 1. Demand transition (D_t+1)
            D_next = D[-1] - self.alpha * (P[-1] - N[-1]) + self.beta * A[-1] - self.gamma * B[-1] + e_D
            
            # 2. Policy transition (P_t+1) with delay lag tau
            # Retrieve delayed demand: if t - tau < 0, use initial D[0]
            lagged_idx = max(0, t - self.tau)
            D_lagged = D[lagged_idx]
            
            if A[-1] >= self.theta_inst:
                P_next = P[-1] + self.lambda_ * (D_lagged - P[-1]) + self.mu * A[-1] + e_P
            else:
                P_next = P[-1] + e_P
                
            # 3. Attention transition (A_t+1) - bound by 0
            A_next = max(0.0, (1 - self.delta) * A[-1] + self.phi * abs(P[-1] - N[-1]) + e_A)
            
            # 4. Backlash transition (B_t+1) - bound by 0
            B_next = max(0.0, self.rho * B[-1] + self.sigma * (abs(P[-1] - N[-1]) - self.theta) + e_B)
            
            # 5. Norm transition (N_t+1)
            N_next = N[-1] + self.nu * (P[-1] - N[-1]) + e_N
            
            D.append(D_next)
            P.append(P_next)
            A.append(A_next)
            B.append(B_next)
            N.append(N_next)
            
        self.history = {
            "step": list(range(steps + 1)),
            "D": D,
            "P": P,
            "A": A,
            "B": B,
            "N": N
        }
        return self.history

    def to_dataframe(self) -> pd.DataFrame:
        """
        Converts the run history to a pandas DataFrame.
        """
        if self.history is None:
            raise ValueError("No simulation history found. Run the simulation first.")
        return pd.DataFrame(self.history)

    def describe_regime(self) -> str:
        """
        Returns a plain-English diagnosis of the current parameter configuration.
        """
        if self.tau == 0:
            return "Stable Convergence: No feedback delay ensures policy matches public demand smoothly."
        elif self.tau >= 3 and self.lambda_ >= 0.35:
            return "Sustained Oscillation: High delay combined with strong correction speeds produces recurring overshoot cycles."
        elif self.theta_inst > 0.1:
            return "Punctuated Sawtooth: Attention gating suppresses small adjustments, causing rapid, sharp corrections once salience is high."
        elif self.nu >= 0.15:
            return "Highly Damped: Rapid norm adaptation causes public baselines to adjust to policy quickly, dampening feedback loops."
        else:
            return "Damped Oscillation: The system experiences transient swings that slowly decay to equilibrium."

    def parameter_sweep(
        self,
        tau_range: List[int],
        lambda_range: List[float],
        steps: int = 150
    ) -> pd.DataFrame:
        """
        Performs a sweep over tau and lambda combinations to measure system properties
        such as convergence, standard deviation (amplitude), and existence of cycle peaks.
        """
        results = []
        for tau in tau_range:
            for lmb in lambda_range:
                sim = PendulumSimulation(
                    alpha=self.alpha, beta=self.beta, gamma=self.gamma,
                    lambda_=lmb, tau=tau, mu=self.mu, delta=self.delta,
                    phi=self.phi, rho=self.rho, sigma=self.sigma,
                    theta=self.theta, theta_inst=self.theta_inst, nu=self.nu,
                    noise_std=self.noise_std
                )
                hist = sim.run(steps=steps)
                p_series = hist["P"][int(steps * 0.4):] # Analyze post-initial transient phase
                
                # Metrics
                std_p = np.std(p_series)
                final_val = p_series[-1]
                
                # Check for cycle presence (number of directional changes)
                diffs = np.diff(p_series)
                sign_changes = np.sum(diffs[:-1] * diffs[1:] < 0)
                
                regime = "convergent"
                if std_p > 0.05:
                    if sign_changes >= 3:
                        regime = "oscillating"
                    else:
                        regime = "diverging/runaway"
                        
                results.append({
                    "tau": tau,
                    "lambda": lmb,
                    "amplitude_std": std_p,
                    "sign_changes": sign_changes,
                    "final_value": final_val,
                    "regime": regime
                })
        return pd.DataFrame(results)

    def calibrate(self, observed: pd.DataFrame, loss: str = "mse") -> dict:
        """
        Fit model parameters to observed (policy, backlash) time series.
        Fits parameters via loss minimization placeholder.
        
        Args:
            observed: DataFrame containing columns 'P_observed' and 'B_observed' index-matched by time.
            loss: Loss metric name, default 'mse'.
            
        Returns:
            Dict containing best-fit parameters and final loss value.
        """
        # Placeholder fitting stub implementing calibration interface
        # In a real run, this would optimize over alpha, lambda_, tau, sigma, theta
        t_steps = len(observed)
        best_loss = 999.0
        best_params = {
            "alpha": self.alpha,
            "lambda_": self.lambda_,
            "tau": self.tau,
            "sigma": self.sigma,
            "theta": self.theta
        }
        
        # Simple grid-search placeholder output demonstrating functionality
        return {
            "parameters": best_params,
            "loss_metric": loss,
            "loss_value": best_loss,
            "status": "placeholder calibration completed successfully"
        }

    def plot_time_series(self, title: str = "Policy-Perception Oscillation Trajectory") -> plt.Figure:
        """
        Generates a standard time-series line plot of all 5 variables.
        """
        if self.history is None:
            raise ValueError("No simulation history found. Run the simulation first.")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        steps = self.history["step"]
        
        ax.plot(steps, self.history["D"], label="Demand (D_t)", color="royalblue", alpha=0.9)
        ax.plot(steps, self.history["P"], label="Policy (P_t)", color="crimson", linewidth=2.0)
        ax.plot(steps, self.history["A"], label="Attention (A_t)", color="orange", linestyle="--")
        ax.plot(steps, self.history["B"], label="Backlash (B_t)", color="darkviolet", linestyle=":")
        ax.plot(steps, self.history["N"], label="Norm (N_t)", color="forestgreen", alpha=0.7)
        
        ax.set_xlabel("Time step")
        ax.set_ylabel("Intensity / Value")
        ax.set_title(f"{title}\nRegime: {self.describe_regime()}")
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.legend(loc="upper right")
        
        plt.tight_layout()
        return fig

    def plot_phase_space(self) -> plt.Figure:
        """
        Generates a phase-space scatter/line plot of Policy vs Demand.
        """
        if self.history is None:
            raise ValueError("No simulation history found. Run the simulation first.")
            
        fig, ax = plt.subplots(figsize=(8, 6))
        P = self.history["P"]
        D = self.history["D"]
        
        # Draw path
        ax.plot(P, D, color="purple", alpha=0.7, label="Trajectory")
        ax.scatter(P[0], D[0], color="green", s=100, label="Start", zorder=5)
        ax.scatter(P[-1], D[-1], color="red", s=100, label="End", zorder=5)
        
        ax.set_xlabel("Policy Position (P_t)")
        ax.set_ylabel("Public Demand (D_t)")
        ax.set_title("Phase Space: Policy vs. Public Demand")
        ax.grid(True, linestyle=":", alpha=0.6)
        ax.legend()
        
        plt.tight_layout()
        return fig
