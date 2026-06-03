import pandas as pd
from sqlalchemy import create_engine
import sqlite3

engine = create_engine("sqlite:///bluestock_mf.db")

print("Database created.")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("All tables loaded successfully.")

conn = sqlite3.connect("bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:
    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        conn
    )
    print(table)
    print(count)

conn.close()