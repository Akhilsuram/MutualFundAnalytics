import pandas as pd

cagr = pd.read_csv("data/processed/cagr_table.csv")
sharpe = pd.read_csv("data/processed/sharpe_ratios.csv")
alpha = pd.read_csv("data/processed/alpha_beta.csv")
drawdown = pd.read_csv("data/processed/max_drawdown.csv")

fund = pd.read_csv("data/raw/01_fund_master.csv")

df = cagr.merge(sharpe,on="amfi_code")
df = df.merge(alpha,on="amfi_code")
df = df.merge(drawdown,on="amfi_code")

df = df.merge(
    fund[["amfi_code","expense_ratio_pct"]],
    on="amfi_code"
)

# Ranks
df["cagr_rank"] = df["cagr_pct"].rank(pct=True)

df["sharpe_rank"] = df["sharpe_ratio"].rank(pct=True)

df["alpha_rank"] = df["alpha"].rank(pct=True)

df["expense_rank"] = (
    df["expense_ratio_pct"]
    .rank(ascending=False,pct=True)
)

df["drawdown_rank"] = (
    df["max_drawdown_pct"]
    .rank(ascending=False,pct=True)
)

df["fund_score"] = (
      30 * df["cagr_rank"]
    + 25 * df["sharpe_rank"]
    + 20 * df["alpha_rank"]
    + 15 * df["expense_rank"]
    + 10 * df["drawdown_rank"]
)

df = df.sort_values(
    "fund_score",
    ascending=False
)

df.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print(df[
    ["amfi_code","fund_score"]
].head())