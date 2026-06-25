# Centralized project parameters and config

CONFIG = {
    # Theoretical Model Parameters (ABM & ODE)
    "alpha": 0.15,       # Demand sensitivity to policy-norm gap
    "beta": 0.05,        # Demand sensitivity to attention
    "gamma": 0.10,       # Demand sensitivity to backlash
    "rho": 0.70,         # Backlash persistence/decay
    "sigma": 0.40,       # Backlash growth sensitivity to threshold breach
    "theta": 1.00,       # Backlash threshold (opinion distance)
    "kappa": 0.30,       # Backlash effect on policy
    "omega": 2.00,       # Attention responsiveness modifier (ABM)
    "theta_inst": 0.00,  # Attention gate threshold (ODE)
    "theta_inst_abm": 0.20, # Attention gate threshold (ABM)
    "mu": 0.02,          # Attention-responsiveness modifier
    "nu": 0.08,          # Norm adaptation rate
    "nu_abm": 0.02,      # Norm adaptation rate (ABM)

    # Empirical Parameters
    "nu_empirical": 0.08,# EWMA decay parameter for norm construction
    "iv_lags": 2,        # Lags for GMM instruments
}
