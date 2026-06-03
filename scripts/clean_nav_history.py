import pandas as pd
import os

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

df = df.drop_duplicates()

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Records:", len(invalid_nav))

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("Rows:", len(df))
print("Cleaned file saved successfully.")