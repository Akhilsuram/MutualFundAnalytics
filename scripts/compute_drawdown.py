import pandas as pd

nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

results = []

for amfi_code, group in nav.groupby(
    "amfi_code"
):

    group = group.sort_values("date")

    running_max = group["nav"].cummax()

    drawdown = (
        group["nav"] / running_max
        - 1
    )

    max_dd = drawdown.min()

    results.append([
        amfi_code,
        round(max_dd * 100, 2)
    ])

drawdown_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown_pct"
    ]
)

drawdown_df.to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)

print(drawdown_df.head())