''' How to calculate Covariance and Correlation
Correlation and Scatterplots - visual interpretation '''
import numpy as np
from create_dataframe import df
import matplotlib.pyplot as plt
import seaborn as sns


print(df)

# if the relationships change with time, its called structural change
# hence here we select latest 2016 data for analysis
df = df.loc["2016"]
print(df)

df.info()

# amounts in million US dollars
print(df.describe())
print(df.mean())
# default degree of freedom ddof=1, assumes we are working on sample & is true
print(df.var())

print("\n covariance:")
print(df.cov())  # o/p as a matrix
print(df.budget.cov(df.revenue))  # just numerical value of covariance

# positive covariance/correlation tells its a positive relationship between two

print("\n correlation coefficient:")
print(df.corr())  # o/p as a matrix
print(df.budget.corr(df.revenue))  # numerical value of correlation coefficient
# using standard formula to find correlation coefficient
print(df.budget.cov(df.revenue) / (df.budget.std() * df.revenue.std()))

# using numpy to find covariance and correlation coefficient matrix
print("\n covariance and correlation coefficient using numpy:")
print(np.cov(df.budget, df.revenue))  # covariance matrix
print(np.corrcoef(df.budget, df.revenue))  # correlation coefficient matrix

''' visual interpretation '''

df.plot(kind="scatter", x="budget", y="revenue", figsize=(15, 10), fontsize=15)
plt.xlabel("Budget (in MUSD)", fontsize=13)
plt.ylabel("Revenue (in MUSD)", fontsize=13)
plt.show()
''' MUSD - million US dollar
Graph here shows a positive relationship/correlation between budget & revenue,
but it's not a perfect relationship as every point here on graph doesn't lie on
one single line and points are dispersed widely; hence there may be some other
factors that influence the revenue of the movie
statistical test of significance (r=0), a hypothesis test is needed to prove
correlation between the 2 variables '''

# another way to plot a scatter plot is using seaborn, which is more intuitive
sns.set(font_scale=1.5)
sns.jointplot(data=df, x="budget", y="revenue", height=8)
plt.show()
# here along with the scatter plot we even have frequency distributions for
# budget and revenue, and the vast movies revenue is withing 20million
# and their budget is in between 50million
