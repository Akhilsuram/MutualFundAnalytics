import pandas as pd

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

sharpe = pd.read_csv(
    "data/processed/sharpe_ratios.csv"
)

df = fund.merge(
    sharpe,
    on="amfi_code"
)

risk_input = input(
    "Enter Risk Appetite (Low / Moderate / High): "
)

mapping = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High", "Very High"]
}

filtered = df[
    df["risk_category"]
    .isin(mapping[risk_input])
]

recommendations = (
    filtered
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nRecommended Funds:\n")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_category",
            "sharpe_ratio"
        ]
    ]
)