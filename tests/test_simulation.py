import pytest
import pandas as pd
import numpy as np
from src.pendulum_model import PendulumSimulation

def test_initialization():
    sim = PendulumSimulation(tau=3, lambda_=0.4)
    assert sim.tau == 3
    assert sim.lambda_ == 0.4
    assert sim.noise_std == 0.0

def test_scenarios():
    sim = PendulumSimulation.from_scenario("stable_convergence")
    assert sim.tau == 0
    
    with pytest.raises(ValueError):
        PendulumSimulation.from_scenario("non_existent_scenario")

def test_run():
    sim = PendulumSimulation(tau=2, lambda_=0.2)
    history = sim.run(steps=50)
    
    assert "step" in history
    assert "D" in history
    assert "P" in history
    assert "A" in history
    assert "B" in history
    assert "N" in history
    
    # 50 steps yields 51 states including initial t=0 state
    assert len(history["step"]) == 51
    assert len(history["P"]) == 51
    assert history["step"][0] == 0
    assert history["step"][-1] == 50

def test_to_dataframe():
    sim = PendulumSimulation()
    with pytest.raises(ValueError):
        sim.to_dataframe()  # Should fail before run
        
    sim.run(steps=10)
    df = sim.to_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 11
    assert list(df.columns) == ["step", "D", "P", "A", "B", "N"]

def test_convergence_vs_oscillation():
    # Stable convergence scenario should result in low policy variance at the end
    sim_conv = PendulumSimulation(tau=0, lambda_=0.1)
    hist_conv = sim_conv.run(steps=100, initial_state={"D": 1.0, "P": 0.0, "A": 0.0, "B": 0.0, "N": 0.0})
    # Variance of the last 40% steps should be very small
    p_last_conv = hist_conv["P"][60:]
    assert np.var(p_last_conv) < 0.01
    
    # Sustained oscillation scenario should have high policy variance
    sim_osc = PendulumSimulation(tau=4, lambda_=0.5, alpha=0.3, nu=0.0)
    hist_osc = sim_osc.run(steps=150, initial_state={"D": 1.0, "P": 0.0, "A": 0.0, "B": 0.0, "N": 0.0})
    p_last_osc = hist_osc["P"][90:]
    # Should maintain fluctuation and not settle to a single point
    assert np.var(p_last_osc) > 0.1

def test_describe_regime():
    sim = PendulumSimulation(tau=0)
    assert "Stable Convergence" in sim.describe_regime()
    
    sim2 = PendulumSimulation(tau=3, lambda_=0.4)
    assert "Sustained Oscillation" in sim2.describe_regime()

def test_parameter_sweep():
    sim = PendulumSimulation()
    df_sweep = sim.parameter_sweep(tau_range=[0, 2], lambda_range=[0.1, 0.4], steps=50)
    assert isinstance(df_sweep, pd.DataFrame)
    assert len(df_sweep) == 4
    assert "amplitude_std" in df_sweep.columns
    assert "regime" in df_sweep.columns
