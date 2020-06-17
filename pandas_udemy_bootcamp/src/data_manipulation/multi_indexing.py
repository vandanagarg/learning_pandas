''' Handling Hierarchical Indexing (Multi-index) within groupby '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
titanic = titanic[["survived", "pclass", "sex", "age", "fare"]]
titanic.info()

# handling multi indexes generated due to group by operations
summary = titanic.groupby(["sex", "pclass"]).mean()
print(summary)

# here we have 2 indexes now sex - outer index & pclass - inner index
print(summary.index)  # shows multi indexes

# now we can even do label based indexing
print(summary.loc[("female", 2), :])  # pass indexes in a tuple
print(summary.loc[("female", 2), "age"])  # a specific column

# swapping and resetting the indexes
print(summary.swaplevel())
print(summary.swaplevel().sort_index())
print(summary.reset_index())  # creating an ordinary range index
