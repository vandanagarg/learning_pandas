''' Hierarchical Indexing (MultiIndex)
using multi index we can create multi dimensional structure, in normal
we have 2D-rows and columns, with 2 columns as index we create a 3D
structure, where 1st dimension is first index column, 2nd dimension is
second index column and 3rd dimension is rest of the column. Also often
group by operations leads to multi index dataframes '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic = dfu.get_dataframe("titanic.csv")
titanic = titanic.iloc[:50, :]  # taking a slice of dataframe

# setting multiple columns as index, pass column names in a list
titanic.set_index(["pclass", "sex"], inplace=True)
print(titanic)

# sorting indexes individually in ascending order
titanic.sort_index(ascending=[True, True], inplace=True)
print(titanic)

# it helps swap the inner and outer indexes if needed
print("\n swapping indexes:")
print(titanic.swaplevel())  # there is no inplace parameter here
# we need to reassign it to titanic variable to save the changes

# here if we want to drop all indexes and switch back to range indexes
# earlier indexed columns are again made columns of dataframe
titanic.reset_index(inplace=True)
print(titanic)

# multi indexing is also called as Hierarchical indexing and here pclass
# is first hierarchy and sex is second hierarchy
print("\n further concepts:")
titanic = dfu.get_dataframe("titanic.csv")
titanic = titanic.iloc[: 50, ]
# print(titanic)

titanic = titanic.set_index(["pclass", "sex"]).sort_index(ascending=True)
# print(titanic)

# label based indexing
# "1" be the label for column pclass, that selects all 1st class passengers
print(titanic.loc[1])  # returns slice of dataframe for pclass 1

# multiple labels
print(titanic.loc[[1, 2]])  # returns slice of dataframe for pclass 1 & 2
print(titanic.loc[:2])  # returns all rows/columns of dataframe for pclass 1&2

print("\n filtering/slicing on both outer and inner indexes:")
# returns slice of dataframe for pclass 1 & sex = female
print(titanic.loc[1, "female"])
print(titanic.loc[(1, "female")])
# pass indexes in brackets so as to query columns as well

# returns slice of dataframe of age column for pclass 1 & sex = female
print(titanic.loc[(1, "female"), "age"])
# print(titanic.loc[1, "female", "age"])
# gives error: too many indexes, since "age" column is not an index

# returns slice of dataframe of age, fare column for pclass 1,2 & sex = female
print(titanic.loc[([1, 2], "female"), ["age", "fare"]])

# returns slice of dataframe of age, fare column for pclass 1,2 & sex = female
print(titanic.loc[([1, 2], "female"), :])
# print(titanic.loc[([1, 2], "female")])  # gives error - KeyError: 'female'
# for multiple values in indexes to select all columns we must pass colon

print(titanic)

print("\n using slice keyword:")
# if we want to query all outer index for female inner index and all columns
# below gives a syntax error and it can be done with slice keyword
# print(titanic.loc[([:, "female"), :])
print(titanic.loc[(slice(None), slice("female")), :])
# here it doesn't slice outer index and slices only female rows
# for inner index and includes all columns
print(titanic.loc[(slice(1), slice("female")), :])
# slices for pclass=1 and sex=female and all columns
print(titanic.loc[(slice(1), slice("female")), "age"])
# slices for pclass=1 and sex=female and age columns
''' Or what we can do is if we don't want to slice outer index we can
swap the indexes and just slice outer index and the we need not to use
any slice keyword '''

titanic = titanic.swaplevel()
print(titanic.head())
print(titanic.loc["female"])
# slices for only female indexes/labels for all classes and columns
