# 📦 Agentic Supply Chain Orchestrator (ASCO)

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-brightgreen.svg)](#)
[![AI Architecture: Agentic](https://img.shields.io/badge/AI%20Architecture-Agentic-blue.svg)](#)

ASCO is an experimental, **rule-free** supply chain optimization engine. Unlike traditional ERP systems that follow rigid "if inventory < X" logic, ASCO uses **Scenario-Augmented Thinking** to stress-test decisions in a virtual Digital Twin before executing them.



## 🧠 The "Augmented Thinking" Model

This project implements a **Goal-Oriented** agent. Instead of following manual processes, the agent is given an **Objective Function**:
> *Minimize Total Landed Cost while protecting against Black Swan events.*

### How it works:
1. **Experience Layer**: Uses historical Poisson distributions to predict baseline demand.
2. **Augmented Reasoning**: For every potential order size, the agent "hallucinates" three futures:
   - **Baseline**: Normal operations.
   - **Market Surge**: A 2.5x demand spike (e.g., social media viral event).
   - **Supply Crunch**: A 50% slowdown (e.g., a port strike).
3. **Minimax Optimization**: It selects the action that performs best across *all* scenarios, effectively "buying insurance" through smart inventory placement.

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10+
- NumPy (for statistical simulations)

### 2. Setup
```bash
git clone [https://github.com/your-username/agentic-supply-chain.git](https://github.com/your-username/agentic-supply-chain.git)
cd agentic-supply-chain
pip install -r requirements.txt
