import pandas as pd

df = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

df = df[
    df["transaction_type"] == "Sip"
]

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

results = []

for investor, group in df.groupby(
    "investor_id"
):

    if len(group) < 6:
        continue

    group = group.sort_values(
        "transaction_date"
    )

    gap = (
        group["transaction_date"]
        .diff()
        .dt.days
        .mean()
    )

    status = (
        "At Risk"
        if gap > 35
        else "Healthy"
    )

    results.append([
        investor,
        round(gap,2),
        status
    ])

sip_report = pd.DataFrame(
    results,
    columns=[
        "investor_id",
        "avg_gap_days",
        "status"
    ]
)

print(
    sip_report["status"]
    .value_counts()
)