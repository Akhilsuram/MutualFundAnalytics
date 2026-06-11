import pandas as pd

df = pd.read_csv(
    "data/processed/daily_returns.csv"
)

results = []

for amfi_code, group in df.groupby("amfi_code"):

    var95 = group["daily_return"].quantile(0.05)

    cvar95 = group[
        group["daily_return"] <= var95
    ]["daily_return"].mean()

    results.append([
        amfi_code,
        round(var95,6),
        round(cvar95,6)
    ])

report = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "VaR_95",
        "CVaR_95"
    ]
)

report.to_csv(
    "data/processed/var_cvar_report.csv",
    index=False
)

print(report.head())