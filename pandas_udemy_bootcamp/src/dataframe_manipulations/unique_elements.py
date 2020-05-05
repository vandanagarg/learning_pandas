''' nunique(), nlargest() and nsmallest() with DataFrames '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic = dfu.get_dataframe("titanic.csv")

# gives error as unique() is a method for series not dataframe
# print(titanic.unique())
# AttributeError: 'DataFrame' object has no attribute 'unique'

print(titanic.age.unique())
# for series returns a numpy array with a list of unique elements

# for dataframe use nunique(), tells number of unique elements in each column
print(titanic.nunique(axis=0))  # across columns axis=0
# by default dropna parameter is True and it drops missing values

# including missing values
print(titanic.nunique(axis=0, dropna=False))

# checking unique values across the rows set axis=1, including missing value
print(titanic.nunique(axis=1, dropna=False))

# checking the largest entries for a particular column
print(titanic.nlargest(n=5, columns="fare"))
# here we need to find out first 5 passengers who paid maximum fare
# works same as: using sort_values()
print(titanic.sort_values("fare", ascending=False).head(5))

# checking the smallest entries for a particular column
print(titanic.nsmallest(n=5, columns="age"))
# checking the 5 youngest passengers on board
print(titanic.nsmallest(n=1, columns="age"))  # youngest passenger
# o/p is in form of pandas dataframe

# here we can filter a specific row with function idxmin(),
# function idxmin() returns the row label for the youngest passenger
# and loc operator returns a row/pandas series for that label
print(titanic.age.idxmin())
print(titanic.loc[titanic.age.idxmin()])
