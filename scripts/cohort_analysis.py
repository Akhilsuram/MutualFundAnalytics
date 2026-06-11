import pandas as pd

df = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

first_txn = (
    df.groupby("investor_id")
    ["transaction_date"]
    .min()
)

cohort = first_txn.dt.year

df["cohort_year"] = (
    df["investor_id"]
    .map(cohort)
)

summary = (
    df.groupby("cohort_year")
    .agg(
        avg_amount=("amount_inr","mean"),
        total_invested=("amount_inr","sum")
    )
)

print(summary)
