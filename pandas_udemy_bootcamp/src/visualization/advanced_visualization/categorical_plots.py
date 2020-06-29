''' Categorical Plots
They all have one thing in common that they are grouped and
we then further analyse them on basis of other columns '''
import seaborn as sns
import matplotlib.pyplot as plt
from create_dataframes import titanic


# finding conclusions like the 1st class male passangers are older
# to female 3rd class passangers
plt.figure(figsize=(12, 8))  # fig size for all
sns.set(font_scale=1.5)  # increased font size

# 1st plot: categorical scatter plot: stripplot()
# sns.stripplot(data=titanic, x="sex", y="age", jitter=False,
#               hue=None, dodge=False)
sns.stripplot(data=titanic, x="sex", y="age", jitter=True,
              hue="pclass", dodge=True)
plt.show()

sns.stripplot(data=titanic, x="sex", y="age", jitter=True,
              hue="survived", dodge=True)
plt.show()
''' x: categorical variable
jitter: true to distribute data instead of overlapping
hue: "pclass": to further group daa on some values
dodge: True : in order to separate different groups on hue bases
now we can clearly see the decreasing trend in age and increasing trend
of survival amongst female passangers '''

# 2nd plot: categorical scatter plot: swarmplot()
sns.swarmplot(data=titanic, x="sex", y="age", hue="pclass", dodge=True)
plt.show()
# helps plot categorical scatter plot with non overlapping points.
# similar to parameter jitter=True
# shows distribution/frequency of the dots by plotting them side to side

# 3rd plot: categorical scatter plot: violinplot()
sns.violinplot(data=titanic, x="sex", y="age", hue="pclass", dodge=True)
plt.show()
# enhanced visualization using line plot to see frequency distributions

# combination of violinplot() and swarmplot()
sns.violinplot(data=titanic, x="sex", y="age", hue="pclass", dodge=True)
sns.swarmplot(data=titanic, x="sex", y="age", hue="pclass", dodge=True,
              color="black")
plt.show()

# reversing the columns in violinplot() and then combining for collective
# analysis or side by side analysis(LHS male, RHS female)
sns.violinplot(data=titanic, x="pclass", y="age", hue="sex", dodge=True,
               split=False)  # splitted plots, 6 violins
plt.show()

sns.violinplot(data=titanic, x="pclass", y="age", hue="sex", dodge=True,
               split=True)  # combined plots, 3 violins
plt.show()

# 4th plot: categorical scatter plot: barplot()
sns.barplot(data=titanic, x="pclass", y="age", hue="sex", dodge=True)
plt.show()
# by default calculates the mean age of all 6 groups(height of bar)
# Shows point estimates and confidence interval for the groups

# 5th plot: categorical scatter plot: pointplot()
sns.pointplot(data=titanic, x="pclass", y="age", hue="sex", dodge=True)
plt.show()
# instead of bars we have lines and rectangular bars denote confidence
# interval and dots denote the mean age
''' for 1st and 3rd class passangers since the confidence interval for
male and female doesn't overlap hence it is sure that for 1st and 3rd
class the males were older then female '''
