''' Financial Time Series - Return and Risk '''
import matplotlib.pyplot as plt
import numpy as np
from create_dataframe import close


''' here we want to see the performance of our 6 stocks on basis of return
and risk and earlier "from normalizing_time_series import norm"
we had normalized our data for equivalent base value
so along with higher return we must consider risk as well for
a stock's performance'''
# relative performance for whole dataframe
print(close.pct_change().dropna())

ret = close.pct_change().dropna()
print(ret.head())

print(ret.describe())
# we need only mean and std for returns and risks
# and also we are transposing the matrix
print(ret.describe().T.loc[:, ["mean", "std"]])

summary = ret.describe().T.loc[:, ["mean", "std"]]
print(summary)

# annual mean and std/ returns or risks
summary["mean"] = summary["mean"]*252
summary["std"] = summary["std"] * np.sqrt(252)
print(summary)

# graphical plot - scatter plot expected 6 dots
summary.plot(kind="scatter", x="std", y="mean", figsize=(15, 12), s=50,
             fontsize=15)
# to put labels against each dot we must loop against each index
# and use method annotate to mark labels
for i in summary.index:
    plt.annotate(i, xy=(summary.loc[i, "std"]+0.002,
                 summary.loc[i, "mean"]+0.002), size=15)
plt.xlabel("ann. Risk(std)", fontsize=15)
plt.ylabel("ann. Return", fontsize=15)
plt.title("Risk/Return", fontsize=20)
plt.show()
