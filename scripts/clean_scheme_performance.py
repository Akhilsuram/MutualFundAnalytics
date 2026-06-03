import pandas as pd
import os

df = pd.read_csv("data/raw/07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("Null values in return columns:")
print(df[return_cols].isnull().sum())

negative_sharpe = df[df["sharpe_ratio"] < 0]

print("\nNegative Sharpe Ratio Records:")
print(len(negative_sharpe))

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))

df = df.drop_duplicates()

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("\nRows:", len(df))
print("Cleaned file saved successfully.")