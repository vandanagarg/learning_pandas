''' perform split, apply, combine operations on a dataframe
using groupby method '''
import matplotlib.pyplot as plt
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
print(titanic.head())
titanic.info()

''' Till now splitting was to make different groups of a df based on some keys
and now next is applying a function on the splitted groups/dataframes and
then combining the o/p's into a single dataframe '''
titanic_slice = titanic.iloc[:10, [2, 3]]
print(titanic_slice)
titanic_slice.info()

# splitting the sliced dataframe
# creating a groupby object
print(titanic_slice.groupby("sex"))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7ff94aa867c0>
# group 1
print(list(titanic_slice.groupby("sex"))[0][1])
# group 2
print(list(titanic_slice.groupby("sex"))[1][1])

# apply - applying function mean on the groupby objects, it will be
# applied to both dataframes by itself and gives o/p as a combined dataframe
print(titanic_slice.groupby("sex").mean())
# o/p is a new combined final dataframe

# applying aggregate functions on the groupby objects
print(titanic_slice.groupby("sex").sum())
print(titanic.groupby("sex").sum())

# using method chaining to check for only survived column
print(titanic.groupby("sex").survived.sum())

# selecting more than one column (pass a list)
print(titanic.groupby("sex")[["fare", "age"]].sum())
print(titanic.groupby("sex")[["fare", "age"]].max())
print(titanic.groupby("sex")[["fare", "age"]].min())

new_df = titanic.groupby("sex").mean()
print(new_df)  # a new grouped dataframe with mean values is created

# creating a plot to visualize the new dataframe
plt.style.use("seaborn")

# creating a bar plot to visualize each column for male and female
new_df.plot(kind="bar", subplots=True, figsize=(8, 15), fontsize=13)
plt.show()
