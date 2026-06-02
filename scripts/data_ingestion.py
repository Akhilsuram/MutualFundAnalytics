import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to raw data folder
data_path = os.path.join(BASE_DIR, "data", "raw")

print("Data Path:", data_path)

# List of CSV files
files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("\nFiles available in raw folder:")
print(os.listdir(data_path))

for file in files:
    print("\n" + "=" * 60)
    print("Processing:", file)

    file_path = os.path.join(data_path, file)

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file}")
        continue

    try:
        df = pd.read_csv(file_path)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"❌ Error reading {file}: {e}")

    print("=" * 60)