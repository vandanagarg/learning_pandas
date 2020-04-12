""" Changing Row Index Labels """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


summer_df = dfu.get_dataframe("summer.csv")
summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
print(summer_df.index)  # row index range/ row labels - range index

print(summer.index)  # labeled index
print(summer.reset_index())  # resets/ changes the existing Athlete index
print(summer.reset_index(drop=True, inplace=False))
# if drop is True it drops the index column
# else the index column changes to a normal column instead of getting dropped

print(summer.set_index("Year", drop=True, inplace=False))  # default
print(summer.set_index("Year", drop=False))
# if drop is True earlier column is dropped- by default
# if False the year column is not dropped and set as index and is present in
# normal column list as well
print(summer.set_index("Year").index.is_unique)

print(summer.index[0])

# summer.index[0] = "changing index"  # index object is immutable
# TypeError: Index does not support mutable operations

# Broadcasting - setting a new value for all the elements of the index
# summer.index = "A new value"  # error
# TypeError: Index(...) must be called with a collection of some kind
# We either need to pass this new value as a list or sequence for all
# the elements of all indexes exclusively

print(summer.index.size)  # 31165 size of elements of index
# creating a list of index size
new_index = ["Medal_No_{}".format(i) for i in range(1, summer.index.size + 1)]
# print(new_index)
# assign the new index value list to replace existing indexes
summer.index = new_index
# validate records
print(summer.head())
print(summer.tail())
print(summer[56: 60])
print(summer.index.is_unique)

# assign index name a new value
print(summer.index.name)  # No existing value
summer.index.name = "Medal Number"
# validating new index name
print(summer.index.name)
print(summer.head())
print(summer.tail())

print(summer.reset_index())  # resets/ changes the existing new indexes
