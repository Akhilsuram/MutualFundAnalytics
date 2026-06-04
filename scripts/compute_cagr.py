import pandas as pd
import numpy as np

nav = pd.read_csv("data/processed/02_nav_history_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])

results = []

for amfi_code, group in nav.groupby("amfi_code"):

    group = group.sort_values("date")

    nav_start = group.iloc[0]["nav"]
    nav_end = group.iloc[-1]["nav"]

    years = (
        (group.iloc[-1]["date"] - group.iloc[0]["date"]).days
        / 365.25
    )

    cagr = ((nav_end / nav_start) ** (1 / years) - 1) * 100

    results.append([
        amfi_code,
        round(cagr, 2)
    ])

cagr_df = pd.DataFrame(
    results,
    columns=["amfi_code", "cagr_pct"]
)

cagr_df.to_csv(
    "data/processed/cagr_table.csv",
    index=False
)

print(cagr_df.head())
print("\nTotal Funds:", len(cagr_df))