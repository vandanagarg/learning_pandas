''' Summary Statistics, Accumulations and the agg() method
To analyze summary statistics and accumulations for numerical dataframes '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic = dfu.get_dataframe("titanic.csv")

print(titanic.describe())
# for all the results in describe() method, we have separate methods as well

# gives the count of non missing values
print("\n count()")
print(titanic.count(axis=0))  # column wise/ along the row
print(titanic.count(axis="index"))  # column wise/ along the row
print(titanic.count(axis="columns"))  # row wise/ along the column
print(titanic.count(axis=1))  # row wise/ along the column

print("\n mean()")
print(titanic.mean(axis=0))  # along rows
print(titanic.mean(axis=1))  # along columns-excludes string values by itself

print("\n sum()")
print(titanic.sum(axis=0))
# o/p states that 342 passengers survived and so on, adds string values as well
print(titanic.sum(axis=1))  # sums numerical columns

print("\n Accumulations:")
print(titanic.head())
print(titanic.fare.cumsum(axis=0))  # keeps adding previous prices

# correlation between 2 numerical columns/ 2 random variables
print(titanic.corr())
print(titanic.survived.corr(titanic.pclass))

# how to create a customized set of summary statistics only with
# one line of code:
print("\n customized stats using agg() method:")
print(titanic.mean())
# pass the method as a string within agg() method
print(titanic.agg("mean"))
# pass functions collective as a list for all numerical columns,
# can even include user defined functions
print(titanic.agg(["mean", "std"]))
print(titanic.agg(["mean", "std", "min", "max", "median"]))
# as a dictionary for selective columns using selective methods
print(titanic.agg({"survived": "mean", "age": ["min", "max"]}))
