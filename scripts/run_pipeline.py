"""
Mutual Fund Analytics
Master Pipeline Runner
"""

import os

print("Starting Pipeline...\n")

os.system("python scripts/compute_daily_returns.py")
os.system("python scripts/compute_cagr.py")
os.system("python scripts/compute_sharpe.py")
os.system("python scripts/compute_sortino.py")
os.system("python scripts/compute_alpha_beta.py")
os.system("python scripts/compute_drawdown.py")
os.system("python scripts/compute_scorecard.py")
os.system("python scripts/compute_var_cvar.py")

print("\nPipeline Completed Successfully")