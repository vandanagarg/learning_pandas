''' The market model (Single Factor Model)
The most commonly known simple linear regression model in finance
Performance of overall market is the most important factor that
influences the growth of stock market, so if there is some factors that
effects the whole market then it must lower a single stock as well;
hence it should be a linear relationship between two
Here we analyze microsoft stock using S&P500 index for duration 2015-2018'''
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


df = yf.download(["MSFT", "^SP500TR"], start="2015-12-31", end="2018-12-31")
print(df)

df = df["Adj Close"]
print(df)

# calculate daily total returns using percent change method
ret = df.pct_change().dropna()
print(ret)

# visualize relationship before plotting a linear plot:
ret.plot(x="^SP500TR", y="MSFT", figsize=(12, 8), kind="scatter")
plt.grid()
plt.title("MSFT vs. SP500 (daily returns)", fontsize=15)
plt.show()

# find out correlation coefficients and performs t test
r, p_value = stats.pearsonr(ret["^SP500TR"], ret.MSFT)
print(r)  # indicates strong positive linear relationship
print(p_value)  # almost equal to 0, hence we can reject null hypothesis
# hence here these 2 variables indicates a strong linear relationship

# to interpret the linear relationship is in form:
# MSFTi = a + beta * SP500i + (intercept)i

beta, intercept, rvalue, pvalue, stderr = stats.linregress(x=ret["^SP500TR"],
                                                           y=ret.MSFT)

print(beta)  # slope: positive value indicates linear relationship
print(intercept)  # approx zero
print(rvalue)

sns.set(font_scale=1.5)
sns.lmplot(data=ret, x="^SP500TR", y="MSFT", height=8, ci=None)
plt.show()
