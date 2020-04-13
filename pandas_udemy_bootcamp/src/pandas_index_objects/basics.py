""" Pandas Index Objects """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


summer_df = dfu.get_dataframe("summer.csv")
summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
print(summer_df.index)  # row index range/ row labels - range index
print(type(summer_df.index))  # class 'pandas.core.indexes.range.RangeIndex'
print(summer_df.columns)
# column index objects - column labels are index labels
print(type(summer_df.columns))  # class 'pandas.core.indexes.base.Index'

# Indexes are diffrent than list or arrays and hence have some special methods

print(summer_df.axes)  # to see (row indexes, column indexes)
print(summer_df.columns[:3])  # First 3 column indexes
print(summer_df.index[0])  # First row index
print(summer_df.index[-1])  # Last row index
print(summer_df.index[100: 102])  # slicing row range indexes
print(summer_df.columns[3: 5])  # slicing column indexes

print(summer.index)  # row index range/ row labels - index with string objects
print(type(summer.index))  # <class 'pandas.core.indexes.base.Index'>
print(summer.axes)  # to see (row indexes, column indexes)
print(summer.index[0])  # First row index
print(summer.index[100: 102])  # slicing row indexes
print(summer.columns[3: 5])  # slicing column indexes

# To convert the indexes into a list
print(summer.columns.to_list())

# To check if existing indexes are unique or not
print(summer.index.is_unique)
print(summer_df.index.is_unique)
print(summer.columns.is_unique)

# To get the location/position of an index label
print(summer.index.get_loc("DRIVAS, Dimitrios"))
