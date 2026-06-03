# Data Dictionary

## dim_fund

amfi_code - Unique AMFI scheme code

fund_house - Mutual fund company

scheme_name - Scheme name

category - Fund category

sub_category - Fund sub-category

plan - Direct/Regular plan

launch_date - Scheme launch date

benchmark - Benchmark index

expense_ratio_pct - Expense ratio percentage

exit_load_pct - Exit load percentage

min_sip_amount - Minimum SIP amount

min_lumpsum_amount - Minimum lump sum investment

fund_manager - Fund manager name

risk_category - Risk classification

sebi_category_code - SEBI category code


## fact_nav

amfi_code - Scheme code

date - NAV date

nav - Net Asset Value


## fact_transactions

investor_id - Investor identifier

transaction_date - Transaction date

amfi_code - Scheme code

transaction_type - SIP/Lumpsum/Redemption

amount_inr - Transaction amount

state - Investor state

city - Investor city

city_tier - City tier classification

age_group - Investor age group

gender - Investor gender

annual_income_lakh - Annual income in lakhs

payment_mode - Payment mode

kyc_status - KYC verification status


## fact_performance

amfi_code - Scheme code

return_1yr_pct - 1 year return

return_3yr_pct - 3 year return

return_5yr_pct - 5 year return

benchmark_3yr_pct - Benchmark return

alpha - Alpha measure

beta - Beta measure

sharpe_ratio - Risk-adjusted return

sortino_ratio - Downside risk-adjusted return

std_dev_ann_pct - Annualized standard deviation

max_drawdown_pct - Maximum drawdown

aum_crore - Assets Under Management

expense_ratio_pct - Expense ratio

morningstar_rating - Morningstar rating

risk_grade - Risk grade


## fact_aum

date - Reporting date

fund_house - Fund house name

aum_lakh_crore - AUM in lakh crore

aum_crore - Assets Under Management

num_schemes - Number of schemes


## fact_category_inflows

month - Reporting month

category - Fund category

net_inflow_crore - Net inflow amount


## fact_folio_count

month - Reporting month

total_folios_crore - Total folios

equity_folios_crore - Equity folios

debt_folios_crore - Debt folios

hybrid_folios_crore - Hybrid folios

others_folios_crore - Other folios


## fact_portfolio_holdings

amfi_code - Scheme code

stock_symbol - Stock ticker symbol

stock_name - Company name

sector - Industry sector

weight_pct - Portfolio weight percentage

market_value_cr - Market value in crores

current_price_inr - Current stock price

portfolio_date - Portfolio reporting date


## dim_benchmark

date - Trading date

index_name - Benchmark index name

close_value - Closing index value