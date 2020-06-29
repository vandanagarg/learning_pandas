''' Advanced visualization/ statistical plotting with Seaborn '''
import seaborn as sns
import matplotlib.pyplot as plt
from create_dataframes import titanic


print(titanic.head())

''' plotting a countplot, similar functionality to groupby()
plots a graph by grouping the data as per given i/p column '''
# style 1
plt.figure(figsize=(12, 8))
# groups data for male and female values
sns.countplot(data=titanic, x="sex")  # vertical plot on x axis
# sns.countplot(data=titanic, y="sex")  # horizontal plot on y axis
plt.show()


# style 2
''' further grouping the data using hue parameter.
"hue - we can pass a column with categorical data"
grouping or binning data for male/famale based on pclass '''
plt.figure(figsize=(12, 8))
# different categories for male/female based on pclass
sns.countplot(data=titanic, x="sex", hue="pclass")
plt.show()


# style 3
''' changing different styles using sns.set() method '''
plt.figure(figsize=(12, 8))
sns.set(font_scale=2, palette="viridis")
sns.countplot(data=titanic, x="sex", hue="pclass")
plt.show()
