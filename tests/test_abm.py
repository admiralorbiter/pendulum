import pytest
import numpy as np
import pandas as pd
from src.pendulum_abm import PendulumABM, PolicyAgent
from src.pendulum_model import PendulumSimulation

def test_abm_initialization():
    # Verify PendulumABM initializes correct number of agents and network
    model = PendulumABM(N=50, network_type='complete', tolerance=0.2, tau=2)
    assert len(model.agents) == 50
    assert model.grid.G.number_of_nodes() == 50
    assert model.policy == 0.0
    assert len(model.demand_history) == 3  # tau + 1

def test_abm_step():
    # Verify advancing a step updates agent variables and datacollector
    model = PendulumABM(N=20, network_type='small_world', tolerance=0.3, tau=1)
    model.step()
    df = model.datacollector.get_model_vars_dataframe()
    assert len(df) == 1
    assert "Policy" in df.columns
    assert "Demand" in df.columns
    assert "Backlash" in df.columns

def test_logit_bounds():
    # Verify opinions stay strictly bounded in (0, 1) and do not clamp or overflow
    model = PendulumABM(N=10, network_type='complete', tolerance=0.5, tau=1,
                        alpha=5.0, beta=5.0, gamma=5.0)  # extremely high forces
    for _ in range(5):
        model.step()
    
    for agent in model.agents:
        assert 0.0 < agent.opinion < 1.0
        assert 0.0 < agent.norm < 1.0

def test_abm_mean_field_ode_equivalence():
    # Under complete graph, omega=0, no threshold heterogeneity (std=0),
    # attention diffusion=0, and local norm adaptation matching global norm,
    # the ABM aggregate mean-field trajectory should closely mirror the ODE model.
    steps = 15
    tau = 2
    lmb = 0.25
    alpha = 0.15
    beta = 0.0
    gamma = 0.0  # disable backlash for simplified comparison
    nu = 0.05
    
    np.random.seed(42)
    # Instantiate ABM
    abm = PendulumABM(N=300, network_type='complete', tolerance=0.6, tau=tau, lambda_=lmb,
                      alpha=alpha, beta=beta, gamma=gamma, nu=nu, omega=0.0,
                      theta_mean=1.5, theta_std=0.0, initial_policy=0.0, use_logit=False,
                      theta_inst=0.0)
                      
    # Override initial opinions to be centered around 0.6 (avoids clamping limits)
    for agent in abm.agents:
        agent.opinion = 0.6
        agent.norm = 0.6
        agent.next_opinion = 0.6
        agent.next_norm = 0.6
    # Reset demand history buffer
    abm.demand_history.clear()
    for _ in range(tau + 1):
        abm.demand_history.append(0.6)

    # Run ABM
    for _ in range(steps):
        abm.step()
        
    df_abm = abm.datacollector.get_model_vars_dataframe()
    
    # Run equivalent ODE model
    ode = PendulumSimulation(alpha=alpha, beta=beta, gamma=gamma, lambda_=lmb, tau=tau,
                             nu=nu, theta=1.5, noise_std=0.0)
    # Initial state matching ABM mean initial values
    ode.run(steps=steps, initial_state={"D": 0.6, "P": 0.0, "A": 0.0, "B": 0.0, "N": 0.6})
    df_ode = ode.to_dataframe()
    
    # Compare aggregate D and P at the end of the runs
    # Mean-field limits should be close
    abm_final_p = df_abm["Policy"].values[-1]
    ode_final_p = df_ode["P"].values[-1]
    
    abm_final_d = df_abm["Demand"].values[-1]
    ode_final_d = df_ode["D"].values[-1]
    
    # Tolerances are set to be reasonable given N=300 size
    assert abs(abm_final_p - ode_final_p) < 0.05
    assert abs(abm_final_d - ode_final_d) < 0.05
