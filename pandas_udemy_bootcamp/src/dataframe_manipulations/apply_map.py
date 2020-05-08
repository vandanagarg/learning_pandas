''' Applying User-defined functions to dataframes using
apply(), map() and applymap() '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


summer = dfu.get_dataframe("summer.csv")
sales = dfu.get_indexed_dataframe("sales.csv", 0)
print(sales)
sales.info()

# MIN ACROSS ROWS
print(sales.min(axis=0))

# MIN ACROSS COLUMNS
print(sales.min(axis=1))

''' if we need to perform a specific operation on a dataframe but we don't have
a predefined function e.g: we want to check range of min and max sales either
on a day or for an individual, we must create a function and use it with
apply() method '''

# to check range for each weekday/ individual


def range(series):
    return series.max() - series.min()


# using apply() method on rows/columns of a dataframe
print("\n To check range on each weekday:")
print(sales.apply(range, axis=0))
print("\n To check range for each individual:")
print(sales.apply(range, axis=1))

# or replacing user defined range() function with lambda function
print("\n To check range using lambda function:")
print(sales.apply(lambda series: series.max() - series.min(), axis=1))
print(sales.apply(lambda x: x.max() - x.min(), axis=0))  # any name is fine

# using apply method on all elements of a particular column of a dataframe
print(summer.head())
print(summer.Athlete.apply(lambda x: x[0]))

# using map() function
print(summer.Athlete.map(lambda x: x[0]))
# o/p same as apply method

# using applymap() function directly on elements of a dataframe
print(summer.iloc[:, 1:3])
print(summer.iloc[:, 1:3].applymap(lambda x: x[0]))

# calculating 40% of daily sales and substracting 5 to get daily sales
# using user defined function
print(sales.applymap(lambda x: 0.4*x-5))
# using simple arithmetics on the dataframe
print(sales*0.4-5)
