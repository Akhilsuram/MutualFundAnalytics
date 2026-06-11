import pandas as pd

portfolio = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

results = []

for fund, group in portfolio.groupby(
    "amfi_code"
):

    hhi = (
        (group["weight_pct"] / 100) ** 2
    ).sum()

    results.append([
        fund,
        round(hhi,4)
    ])

hhi_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "HHI"
    ]
)

hhi_df = hhi_df.sort_values(
    "HHI",
    ascending=False
)

hhi_df.to_csv(
    "data/processed/hhi_report.csv",
    index=False
)

print(hhi_df.head())