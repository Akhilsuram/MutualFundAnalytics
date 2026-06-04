import pandas as pd
import numpy as np

rf = 0.065

df = pd.read_csv(
    "data/processed/daily_returns.csv"
)

results = []

for amfi_code, group in df.groupby("amfi_code"):

    mean_return = group["daily_return"].mean()

    std_return = group["daily_return"].std()

    sharpe = (
        ((mean_return * 252) - rf)
        / (std_return * np.sqrt(252))
    )

    results.append([
        amfi_code,
        round(sharpe, 4)
    ])

sharpe_df = pd.DataFrame(
    results,
    columns=["amfi_code", "sharpe_ratio"]
)

sharpe_df = sharpe_df.sort_values(
    "sharpe_ratio",
    ascending=False
)

sharpe_df.to_csv(
    "data/processed/sharpe_ratios.csv",
    index=False
)

print(sharpe_df.head())