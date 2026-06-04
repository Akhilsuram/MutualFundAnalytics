Day 1 :
- Project structure created
- Loaded 10 datasets
- Fetched NAV data
- AMFI validation passed
- GitHub repository setup

Day 2 :
-Data Cleaning

* Cleaned NAV history dataset by parsing dates, sorting records, removing duplicates, forward-filling missing NAV values, and validating NAV > 0.
* Cleaned investor transactions dataset by standardizing transaction types, validating transaction amounts, checking KYC status values, and formatting dates.
* Cleaned scheme performance dataset by validating return metrics, checking Sharpe ratios, and verifying expense ratio ranges.

 Database Design & Loading

* Designed a SQLite star schema consisting of dimension and fact tables.
* Created tables: dim_fund, dim_date, fact_nav, fact_transactions, fact_performance, and fact_aum.
* Loaded cleaned datasets into SQLite database (bluestock_mf.db) using SQLAlchemy.
* Verified database row counts against source datasets.

 SQL Analysis & Documentation

* Created 10 analytical SQL queries for business insights.
* Prepared a comprehensive data dictionary documenting tables, columns, and definitions.
* Generated processed datasets and stored them in the data/processed directory.
* Committed and pushed all Day 2 deliverables to GitHub.


Day 3 :
- Performed Exploratory Data Analysis (EDA)
- Generated 15+ visualizations using Plotly, Matplotlib and Seaborn
- Analyzed NAV trends, AUM growth, SIP inflows and investor demographics
- Created correlation matrix and sector allocation analysis
- Exported charts as PNG files
- Documented 10 key EDA insights

Day 4 :
-Fund Performance Analytics
* Computed daily returns for all mutual fund schemes.
* Calculated CAGR across funds and compared long-term performance.
* Computed Sharpe Ratio and Sortino Ratio using risk-adjusted return methodology.
* Calculated Alpha and Beta against the NIFTY 100 benchmark using regression analysis.
* Performed Maximum Drawdown analysis to assess downside risk.
* Developed a composite Fund Scorecard for ranking schemes.
* Created benchmark comparison visualizations and documented key findings.
* Generated performance analytics datasets and notebook deliverables.
