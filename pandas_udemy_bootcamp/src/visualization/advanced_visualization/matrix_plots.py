''' Matrixplots / Heatmaps
To visualize cross tabular data '''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from create_dataframes import titanic


# group data into 6 subgroups/categories
# We typically need this crosstabular data for matrix/heatmaps
print(pd.crosstab(titanic.sex, titanic.pclass))

plt.figure(figsize=(12, 8))
sns.set(font_scale=1.4)

# plot 1: heatmap()
# analyzing size of 6 groups using heatmaps
sns.heatmap(pd.crosstab(titanic.sex, titanic.pclass),
            annot=False, fmt="d", cmap=None, vmax=None)
plt.show()

# annot parameter tells exact size of each group
# cmap for another color pattern
# vmax to set a upper limit of range to help differentiate
# the color groups more nicely
sns.heatmap(pd.crosstab(titanic.sex, titanic.pclass),
            annot=True, fmt="d", cmap="Reds", vmax=150)
plt.show()

# plot 2: heatmap()
# identify/differentiate colors with survival rate of those groups
print(pd.crosstab(titanic.sex, titanic.pclass, values=titanic.survived,
                  aggfunc="mean"))

sns.heatmap(pd.crosstab(titanic.sex, titanic.pclass,
            values=titanic.survived, aggfunc="mean"),
            annot=True, cmap="Reds")
plt.show()

# plot 3: heatmap()
# correlation matrix of all numerical columns of titanic dataframe
print(titanic.corr())

sns.heatmap(titanic.corr(), annot=True, cmap="Reds")
plt.show()
