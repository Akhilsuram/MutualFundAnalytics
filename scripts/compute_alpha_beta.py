import pandas as pd
from scipy.stats import linregress

funds = pd.read_csv(
    "data/processed/daily_returns.csv"
)

benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark[
    benchmark["index_name"] == "NIFTY100"
]

benchmark = benchmark.sort_values("date")

benchmark["benchmark_return"] = (
    benchmark["close_value"]
    .pct_change()
)

benchmark = benchmark.dropna()

results = []

for amfi_code, group in funds.groupby("amfi_code"):

    group["date"] = pd.to_datetime(
        group["date"]
    )

    merged = pd.merge(
        group,
        benchmark[
            ["date", "benchmark_return"]
        ],
        on="date",
        how="inner"
    )

    slope, intercept, r, p, stderr = linregress(
        merged["benchmark_return"],
        merged["daily_return"]
    )

    alpha = intercept * 252
    beta = slope

    results.append([
        amfi_code,
        round(alpha, 4),
        round(beta, 4)
    ])

alpha_beta = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

alpha_beta.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print(alpha_beta.head())