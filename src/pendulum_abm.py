import mesa
import networkx as nx
import numpy as np
from collections import deque

class PolicyAgent(mesa.Agent):
    """
    Agent representing an individual citizen or policy actor.
    Has continuous opinion (public demand), perceived norm, attention level, 
    and binary backlash mobilization state.
    """
    def __init__(self, model, opinion, threshold_grievance, threshold_social, norm):
        super().__init__(model)
        self.opinion = opinion                # x_i in [0, 1]
        self.theta_i = threshold_grievance    # Grievance threshold
        self.psi_i = threshold_social        # Granovetter social threshold
        self.norm = norm                      # Individual perceived norm (N_i,t)
        self.attention = 0.0                  # Individual attention (a_i,t)
        self.backlash_active = False          # Individual backlash state (b_i,t)
        
        # Buffers for synchronous updates (prevents order-dependent race conditions)
        self.next_opinion = opinion
        self.next_attention = 0.0
        self.next_backlash_active = False
        self.next_norm = norm

    def step(self):
        P = self.model.policy
        epsilon = self.model.tolerance
        
        # Get network neighbors (in Mesa 3.0+, NetworkGrid.get_neighbors returns agent objects directly)
        neighbor_agents = self.model.grid.get_neighbors(self.pos, include_center=True)
                
        # 1. Bounded Confidence (Hegselmann-Krause) social updating
        compatible_neighbors = [
            agent for agent in neighbor_agents 
            if abs(agent.opinion - self.opinion) <= epsilon
        ]
        
        if compatible_neighbors:
            x_social = np.mean([agent.opinion for agent in compatible_neighbors])
        else:
            x_social = self.opinion
            
        # 2. External Forces Calculation
        # Local policy experienced can be damped by local pressure valve kappa (H7)
        local_backlash = np.mean([1.0 if agent.backlash_active else 0.0 for agent in neighbor_agents if agent != self]) \
            if len(neighbor_agents) > 1 else (1.0 if self.backlash_active else 0.0)
        local_policy = P - self.model.kappa * local_backlash
        
        policy_gap = local_policy - self.norm
        f_policy = -self.model.alpha * policy_gap
        f_attention = self.model.beta * self.attention
        # Corrected signed backlash force
        f_backlash = -self.model.gamma * (1.0 if self.backlash_active else 0.0) * np.sign(policy_gap)
        
        if self.model.use_logit:
            # Logit transform to apply external forces without boundary clamping issues
            eps_logit = 1e-5
            x_social_clipped = np.clip(x_social, eps_logit, 1 - eps_logit)
            y_social = np.log(x_social_clipped / (1 - x_social_clipped))
            y_next = y_social + f_policy + f_attention + f_backlash
            self.next_opinion = 1.0 / (1.0 + np.exp(-y_next))
        else:
            # Standard additive update with boundary clamping (matches mean-field ODE exactly)
            self.next_opinion = np.clip(x_social + f_policy + f_attention + f_backlash, 0.0, 1.0)
        
        # 4. Attention Contagion
        local_att_mean = np.mean([agent.attention for agent in neighbor_agents if agent != self]) \
            if len(neighbor_agents) > 1 else 0.0
        self.next_attention = max(0.0, (1 - self.model.delta) * self.attention + 
                                  self.model.phi * abs(policy_gap) + 
                                  self.model.attention_diffusion * local_att_mean)
        
        # 5. Granovetter Cascade Backlash
        active_neighbors = [agent for agent in neighbor_agents if agent != self and agent.backlash_active]
        fraction_active = len(active_neighbors) / (len(neighbor_agents) - 1) \
            if len(neighbor_agents) > 1 else 0.0
        
        # Susceptibility threshold is lower than activation threshold
        theta_suscept = 0.5 * self.theta_i
        is_aggrieved = abs(policy_gap) > self.theta_i
        is_susceptible = abs(policy_gap) > theta_suscept
        social_trigger = fraction_active >= self.psi_i
        
        # Combined rule: instigators OR (susceptible AND social contagion)
        self.next_backlash_active = is_aggrieved or (is_susceptible and social_trigger)
        
        # 6. Perceived Norm Dual-Updating
        local_opinion_mean = np.mean([agent.opinion for agent in neighbor_agents])
        local_adjustment = 0.05 * (local_opinion_mean - self.norm) if self.model.use_logit else 0.0
        self.next_norm = self.norm + self.model.nu * (P - self.norm) + local_adjustment

    def advance(self):
        # Synchronous state transition
        self.opinion = self.next_opinion
        self.attention = self.next_attention
        self.backlash_active = self.next_backlash_active
        self.norm = self.next_norm


class PendulumABM(mesa.Model):
    """
    Agent-Based Model matching the 5-equation policy-perception system.
    Integrates network structures, logit updates, weighted demand feedback, 
    and H7 policy stabilizers.
    """
    def __init__(self, N=100, network_type='small_world', tolerance=0.2, tau=3, lambda_=0.3,
                 alpha=0.15, beta=0.05, gamma=0.1, delta=0.3, phi=0.25, nu=0.02, 
                 attention_diffusion=0.1, theta_inst=0.2, omega=2.0, kappa=0.0,
                 theta_mean=1.0, theta_std=0.2, psi_min=0.1, psi_max=0.4, initial_policy=0.0,
                 use_logit=True):
        super().__init__()
        self.num_agents = N
        self.tolerance = tolerance
        self.tau = tau
        self.lambda_ = lambda_
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.phi = phi
        self.nu = nu
        self.attention_diffusion = attention_diffusion
        self.theta_inst = theta_inst
        self.omega = omega
        self.kappa = kappa
        self.use_logit = use_logit
        
        self.policy = initial_policy
        self.demand_history = deque(maxlen=max(1, tau + 1))
        
        # Topology initialization
        if network_type == 'complete':
            self.G = nx.complete_graph(N)
        elif network_type == 'scale_free':
            self.G = nx.barabasi_albert_graph(N, m=2)
        else: # Default: small_world (Watts-Strogatz)
            self.G = nx.watts_strogatz_graph(N, k=4, p=0.1)
            
        self.grid = mesa.space.NetworkGrid(self.G)
        
        # Initialize agents with heterogeneous thresholds
        for i, node in enumerate(self.G.nodes()):
            theta_i = max(0.1, np.random.normal(theta_mean, theta_std)) # Grievance threshold
            psi_i = np.random.uniform(psi_min, psi_max)               # Social threshold
            opinion_i = np.random.uniform(0.0, 1.0)
            
            agent = PolicyAgent(self, opinion_i, theta_i, psi_i, opinion_i)
            # Set unique_id manually for consistency with Node IDs
            agent.unique_id = i
            self.grid.place_agent(agent, node)
            self.agents.add(agent)
            
        # Initial history buffer with initial weighted demand
        D_0 = self.calculate_weighted_demand()
        for _ in range(tau + 1):
            self.demand_history.append(D_0)
            
        # Setup DataCollector
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Policy": lambda m: m.policy,
                "Norm": lambda m: np.mean([a.norm for a in m.agents]),
                "Demand": lambda m: np.mean([a.opinion for a in m.agents]),
                "WeightedDemand": lambda m: m.calculate_weighted_demand(),
                "Attention": lambda m: np.mean([a.attention for a in m.agents]),
                "Backlash": lambda m: np.mean([1.0 if a.backlash_active else 0.0 for a in m.agents])
            },
            agent_reporters={
                "Opinion": "opinion",
                "Attention": "attention",
                "Backlash": "backlash_active",
                "Norm": "norm"
            }
        )

    def calculate_weighted_demand(self):
        """
        Computes the politically weighted demand index (D^W_t).
        Mobilized agents receive a weight multiplier (1 + omega).
        """
        total_weight = 0.0
        weighted_sum = 0.0
        for agent in self.agents:
            w = 1.0 + self.omega if agent.backlash_active else 1.0
            weighted_sum += w * agent.opinion
            total_weight += w
        return weighted_sum / total_weight if total_weight > 0 else 0.5

    def step(self):
        # Stage 1: Agents evaluate state
        for agent in self.agents:
            agent.step()
            
        # Stage 2: Agents update state synchronously
        for agent in self.agents:
            agent.advance()
            
        # Collect data
        self.datacollector.collect(self)
        
        # Retrieve delayed demand D^W_{t-tau} (prior to appending current step's demand)
        lagged_demand = self.demand_history[0]
        
        A_t = np.mean([agent.attention for agent in self.agents])
        
        # Update policy using lagged demand and current attention
        if A_t >= self.theta_inst:
            # Salience scales policy correction speed, removing unsigned positive drift
            self.policy += (self.lambda_ + 0.2 * A_t) * (lagged_demand - self.policy)
            
        # Append current demand to history for future steps
        D_w = self.calculate_weighted_demand()
        self.demand_history.append(D_w)
