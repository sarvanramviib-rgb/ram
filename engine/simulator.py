import numpy as np

class SupplyChainTwin:
    """Simulates the physics of your supply chain."""
    def __init__(self, current_inv, daily_demand_mu):
        self.initial_inv = current_inv
        self.mu = daily_demand_mu  # The 'Experience' baseline

    def run_simulation(self, order_qty, scenario_multiplier, days=14):
        """Calculates costs based on a specific future scenario."""
        inventory = self.initial_inv
        stockout_penalty = 0
        holding_costs = 0
        
        # Simulate each day in the window
        for _ in range(days):
            # Demand is predicted using a Poisson distribution (Experience-based)
            demand = np.random.poisson(self.mu * scenario_multiplier)
            inventory -= demand
            
            if inventory < 0:
                stockout_penalty += abs(inventory) * 25 # High cost for failing customer
                inventory = 0
            else:
                holding_costs += inventory * 0.75 # Cost to store items
                
        return holding_costs + stockout_penalty + (order_qty * 10) # Total Landed Cost
