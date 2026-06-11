import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

returns = pd.read_csv(
    "data/processed/daily_returns.csv"
)

top5 = [
    119551,
    120503,
    118632,
    119092,
    120841
]

plt.figure(figsize=(12,6))

for fund in top5:

    temp = returns[
        returns["amfi_code"] == fund
    ].copy()

    temp["date"] = pd.to_datetime(
        temp["date"]
    )

    temp["rolling_sharpe"] = (
        temp["daily_return"]
        .rolling(90)
        .mean()
        /
        temp["daily_return"]
        .rolling(90)
        .std()
    ) * np.sqrt(252)

    plt.plot(
        temp["date"],
        temp["rolling_sharpe"],
        label=str(fund)
    )

plt.legend()

plt.title(
    "Rolling 90-Day Sharpe Ratio"
)

plt.savefig(
    "reports/rolling_sharpe_chart.png",
    bbox_inches="tight"
)

plt.show()
