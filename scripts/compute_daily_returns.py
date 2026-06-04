import pandas as pd
import os

nav = pd.read_csv("data/processed/02_nav_history_clean.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

daily_returns = nav.dropna(subset=["daily_return"])

os.makedirs("data/processed", exist_ok=True)

daily_returns.to_csv(
    "data/processed/daily_returns.csv",
    index=False
)

print("Rows:", len(daily_returns))

print("\nDaily Return Summary:")
print(daily_returns["daily_return"].describe())