import pandas as pd
import os

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

fund_path = os.path.join(BASE_DIR, "data", "raw", "01_fund_master.csv")
nav_path = os.path.join(BASE_DIR, "data", "raw", "02_nav_history.csv")

fund = pd.read_csv(fund_path)
nav = pd.read_csv(nav_path)

fund_codes = set(fund["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = fund_codes - nav_codes

print("Missing Codes")
print(missing)

print("Count:", len(missing))