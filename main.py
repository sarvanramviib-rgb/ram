from engine.simulator import SupplyChainTwin
from engine.optimizer import AgenticOptimizer

def run_orchestrator():
    print("--- 2026 Agentic Supply Chain Optimizer ---")
    
    # 1. Perception Layer (Current State)
    current_inventory = 120
    historical_avg_demand = 15
    
    # 2. Experience Layer (Initialize Digital Twin)
    twin = SupplyChainTwin(current_inventory, historical_avg_demand)
    
    # 3. Augmented Thinking Layer (Initialize Optimizer)
    ai_agent = AgenticOptimizer(twin)
    
    # 4. Decision Execution
    print("AI is running cross-scenario simulations...")
    decision = ai_agent.find_best_move()
    
    print(f"\nFinal Recommendation: Order {decision} units.")
    print("Reasoning: This quantity offers the best balance between ")
    print("normal operations and 'Black Swan' market surges.")

if __name__ == "__main__":
    run_orchestrator()
