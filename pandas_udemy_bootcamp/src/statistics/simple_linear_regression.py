''' Create a simple Linear Regression Model with the independent variable
Movie Budget and one dependent variable Movie Revenue
Visualize and interpret the regression coefficients '''
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from create_dataframe import df


np.set_printoptions(precision=2, suppress=True)

df = df.loc["2016"]
print(df)

# first using seaborn lmplot() to visualize data
sns.set(font_scale=1.5)
sns.lmplot(data=df, x="budget", y="revenue", height=8, ci=None)
plt.show()

# Linear Regression with numpy
x = df.iloc[:, -2].values  # create numpy array for budget column
print(x)

y = df.iloc[:, -1].values  # create numpy array for revenue column
print(y)

# Linear regression model with np.polyfit()
print("\n regression coefficients: slope coefficient, intercept")
reg = np.polyfit(x=x, y=y, deg=1)  # pass deg=1 for linear, 2 for quadratic etc
print(reg)
# either pass column names
print(np.polyfit(x=df.budget, y=df.revenue, deg=1))

# creating x and y values for regression line: to create a line we minimum
# need to data points; hence here we are taking min and max 2 points:
X = np.array([min(x), max(x)])
print(X)

# other way is use np.polyval() function and use regression coefficients and X
# to calculate corresponding Y values to plot a line
Y = np.polyval(reg, X)
print(Y)

plt.figure(figsize=(12, 8))
plt.plot(X, Y)  # plots linear regression line
plt.scatter(x=x, y=y)  # plots 235 data points/observations
plt.xlabel("Budget (in MUSD)")
plt.ylabel("Revenue (in MUSD)")
plt.show()

# Linear regression with scipy
print(df)

print(stats.linregress(x=df.budget, y=df.revenue))
# gives the values of slope, intercept etc variables

# How to interpret regression coefficients(intercept, slope)
plt.figure(figsize=(12, 8))
plt.plot(X, Y)
plt.grid()
plt.scatter(x=x, y=y)
plt.xlabel("Budget (in MUSD)", fontsize=15)
plt.ylabel("Revenue (in MUSD)", fontsize=15)
plt.title("Linear Regression Model Revenue vs. Budget", fontsize=15)
plt.show()

# represents the slope coefficient:
# covariance of xy/variance of independent variable x
print(df.budget.cov(df.revenue) / df.budget.var())
