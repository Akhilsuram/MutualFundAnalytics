import pandas as pd
import os

df = pd.read_csv("data/raw/08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

invalid_amount = df[df["amount_inr"] <= 0]

print("Unique KYC Status Values:")
print(df["kyc_status"].unique())

print("\nUnique Transaction Types:")
print(df["transaction_type"].unique())

print("\nInvalid Amount Records:", len(invalid_amount))

df = df.drop_duplicates()

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("\nRows:", len(df))
print("Cleaned file saved successfully.")