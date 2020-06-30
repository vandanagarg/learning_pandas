''' Jointplots / Regression '''
import seaborn as sns
import matplotlib.pyplot as plt
from create_dataframes import titanic


sns.set(font_scale=1.5)
# deduce the conclusions like older passengers paid more fare and than younger
# passangers and then check the relationship between their survival
# age and fare 2 continuos numerical columns

# 1st plot: jointplot: (scatter plot)
sns.jointplot(data=titanic, x="age", y="fare", height=8, kind="scatter")
plt.show()
# side graphs tells about frequency distribution of age and fare columns
# height parameter denotes height of the graph

# hexbin plot: more darker the spots higher the densities
sns.jointplot(data=titanic, x="age", y="fare", height=8, kind="hex")
plt.show()
# kernel density estimator: more darker the spots higher the densities
sns.jointplot(data=titanic, x="age", y="fare", height=8, kind="kde")
plt.show()

# to verify the relationship of age and fare, regression plot
sns.jointplot(data=titanic, x="age", y="fare", height=8, kind="reg")
plt.show()
# the line has a upward slope hence indicates a positive relationship
# shadowed area around the line shows the confidence interval of 95%
# line itself is point estimate

# 2nd plot: regression plots in seaborn using lmplot()
''' We can create subplots using parameter col, visualize data for
different groups using parameter hue, set size of plots and subplots
using aspect and height parameters '''
sns.lmplot(data=titanic, x="age", y="fare", aspect=1, height=8, hue=None)
plt.show()  # same graph as above

sns.lmplot(data=titanic, x="age", y="fare", aspect=1, height=8, hue="sex")
plt.show()  # grouping data based on sex column
# upward slope for male and female gropus

sns.lmplot(data=titanic, x="age", y="fare", aspect=1, height=8, col="sex")
plt.show()  # subplots for male and female in columns

sns.lmplot(data=titanic, x="age", y="fare", aspect=1, height=8, row="sex")
plt.show()  # subplots for male and female in rows

# 3rd plot: to analyze factors that influence survival
''' Here since survived is a categorical data column, hence we need logistic
regression and we pass logistic=True and the o/p downward slope indicates
older the passangers, less survival chance and in the start we mostly
have women and children. We can group our data or can have categorical
split using parameter col '''
sns.lmplot(data=titanic, x="age", y="survived", aspect=1, height=8,
           col=None, logistic=True)
plt.show()

# grouping data for male and female
sns.lmplot(data=titanic, x="age", y="survived", aspect=1, height=8,
           col="sex", logistic=True)
plt.show()  # downward slope for male and upward slope for females

# grouping data for pclass, downward slope for all 3, older the passanger
# lesser the chance of survival
sns.lmplot(data=titanic, x="age", y="survived", aspect=1, height=8,
           col="pclass", logistic=True)
plt.show()
