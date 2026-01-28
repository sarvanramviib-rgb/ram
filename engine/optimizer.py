from .simulator import SupplyChainTwin

class AgenticOptimizer:
    def __init__(self, twin: SupplyChainTwin):
        self.twin = twin
        # These are the 'What-Ifs' the AI generates automatically
        self.scenarios = {
            "normal": 1.0,
            "market_surge": 2.5,  # Viral trend scenario
            "supply_crunch": 0.5   # Scarcity scenario
        }

    def find_best_move(self, possible_actions=[0, 50, 100, 200, 500]):
        best_action = None
        lowest_overall_risk_score = float('inf')

        for action in possible_actions:
            scenario_results = []
            
            # Augmented Thinking: Test the action against ALL scenarios
            for name, multiplier in self.scenarios.items():
                cost = self.twin.run_simulation(action, multiplier)
                scenario_results.append(cost)
            
            # The 'Rule-Free' Logic: We optimize for the 'Minimax' (Minimum Maximum Loss)
            # This makes the supply chain RESILIENT instead of just CHEAP.
            max_potential_loss = max(scenario_results)
            avg_expected_loss = sum(scenario_results) / len(scenario_results)
            
            # Combined Score (60% average performance, 40% worst-case protection)
            risk_score = (avg_expected_loss * 0.6) + (max_potential_loss * 0.4)
            
            if risk_score < lowest_overall_risk_score:
                lowest_overall_risk_score = risk_score
                best_action = action
                
        return best_action
