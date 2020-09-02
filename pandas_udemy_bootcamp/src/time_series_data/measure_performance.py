''' Measuring Stock Performance with MEAN Return and STD of Returns
relative changes are always more helpful for stock performances
relative increase is also considered as return and return consists
of price increase and dividend payments '''
import matplotlib.pyplot as plt
import numpy as np
from create_dataframe import close


aapl = close.AAPL.copy().to_frame()
print(aapl.head())

# daily returns
print(aapl.pct_change().dropna())

ret = aapl.pct_change().dropna()
print(ret.head())
ret.info()

# distribution of daily returns
ret.plot(kind="hist", figsize=(12, 8), bins=100)
plt.show()

# mean is to check avg returns more is the mean its more profitable investment
# to check for the risks associated with the investment we must check std or
# variability or volatility of returns around the mean which is std/variance
# preferred high return and low volatility

daily_mean_Return = ret.mean()
print(daily_mean_Return)

var_daily_Returns = ret.var()
print(var_daily_Returns)

std_daily_Returns = np.sqrt(var_daily_Returns)
print(std_daily_Returns)

print(ret.std())

# annual returns and std, 252 trading days in a year
ann_mean_Return = ret.mean() * 252
print(ann_mean_Return)

ann_var_Returns = ret.var() * 252
print(ann_var_Returns)

ann_std_Returns = np.sqrt(ann_var_Returns)
print(ann_std_Returns)

print(ret.std() * np.sqrt(252))
''' So earlier daily returns and std wasn't much intuitive hence based
on daily returns we checked for annual returns and risk and here
we got parameters annual return (mean) and annual risk(std) and these
2 parameters can help decide the stock performance and
we can even use weekly returns or anything for this '''
