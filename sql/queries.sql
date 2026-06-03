-- 1
SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2
SELECT strftime('%Y-%m', date) AS month,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3
SELECT state,
       COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 4
SELECT scheme_name,
       expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- 5
SELECT transaction_type,
       COUNT(*) AS count
FROM fact_transactions
GROUP BY transaction_type;

-- 6
SELECT risk_grade,
       COUNT(*) AS funds
FROM fact_performance
GROUP BY risk_grade;

-- 7
SELECT fund_house,
       AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_return DESC;

-- 8
SELECT city_tier,
       AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY city_tier;

-- 9
SELECT gender,
       COUNT(*) AS investors
FROM fact_transactions
GROUP BY gender;

-- 10
SELECT category,
       COUNT(*) AS schemes
FROM dim_fund
GROUP BY category;