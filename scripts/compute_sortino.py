import pandas as pd
import numpy as np

rf = 0.065

df = pd.read_csv(
    "data/processed/daily_returns.csv"
)

results = []

for amfi_code, group in df.groupby("amfi_code"):

    mean_return = group["daily_return"].mean()

    downside = group[
        group["daily_return"] < 0
    ]["daily_return"]

    downside_std = downside.std()

    sortino = (
        ((mean_return * 252) - rf)
        / (downside_std * np.sqrt(252))
    )

    results.append([
        amfi_code,
        round(sortino, 4)
    ])

sortino_df = pd.DataFrame(
    results,
    columns=["amfi_code", "sortino_ratio"]
)

sortino_df = sortino_df.sort_values(
    "sortino_ratio",
    ascending=False
)

sortino_df.to_csv(
    "data/processed/sortino_ratios.csv",
    index=False
)

print(sortino_df.head())