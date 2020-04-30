''' Manipulating Values in a DataFrame
Best Practice (how you should do it) '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic = dfu.get_dataframe("titanic.csv")
print(titanic.head())

#  Changing a single Value (Option 1 with loc)
titanic.loc[1, "age"] = 40
print(titanic.head())  # changes in original df

# Changing a single Value (Option 2 with iloc)
titanic.iloc[1, 3] = 41
print(titanic.head())  # changes in original df

# Changing multiple values in a column (Option 1 with loc)
titanic.loc[1:3, "age"] = 42  # 3rd including, label based
print(titanic.head())  # changes in original df

# Changing multiple values in a column (Option 2 with iloc)
titanic.iloc[1:4, 3] = [43, 44, 45]  # 4th excluding, position based
print(titanic.head())  # changes in original df

# Changing multiple values in a column (Option 3 with boolean indexing)
# getting index values of all the babies less then 1year
index_babies = titanic.loc[titanic.age < 1, "age"].index
titanic.loc[titanic.age < 1, "age"] = 1  # assign value one for the age
print(titanic.loc[index_babies])

# Changing multiple values in a row
print(titanic.head())
print(titanic.iloc[0, 0:3])
titanic.loc[0, "survived":"sex"] = [1, 1, "female"]
print(titanic.head())  # changes in original df

# Changing multiple values in multiple rows/columns
print(titanic.replace(0, "Zero"))
print(titanic.head())  # doesn't change in original df,by deafult:inplace=False
# replaced all 0 values with "Zero" string for all rows/columns

''' How you should NOT do it '''
titanic = dfu.get_dataframe("titanic.csv")
age = titanic.age
print(age.head())

# Here mostly we will be using chained indexing which is anyways
# less efficient
age[1] = 40
# this command gives a warning message as it changes original df as well
''' SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame '''
print(age.head())
print(titanic.head())

# The above command is equivalent to:
titanic.age[1] = 41  # This is Chained Indexing!!!
print(titanic.head())
''' SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame '''

# This is NOT Chained Indexing and the idiomatic/best way to do it!!!
titanic.loc[1, "age"] = 42
print(titanic.head())

# Manipulating a slice
slice1 = titanic[["sex", "age"]]
print(slice1.head())

slice1.iloc[1, 1] = 43
''' SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead '''
print(slice1)  # value changed in slice
print(titanic.head())  # doesn't change value in original df

# creating slice2 using loc operator
slice2 = titanic.loc[:, ["sex", "age"]]
print(slice2)

slice2.iloc[1, 1] = 44  # No warning message here
print(slice2.head())  # value changed in slice
print(titanic.head())  # doesn't change value in original df

index_babies = titanic[titanic.age < 1].index
titanic[titanic.age < 1]["age"] = 1
# we are here using chained indexing which is not recommended
''' SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead '''
print(titanic.loc[index_babies, :])  # doesn't change value in original df

titanic["age"][titanic.age < 1] = 1
''' SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame '''
print(titanic.loc[index_babies])  # changes the values in original df

titanic[["sex", "age"]][titanic.age == 1]["age"] = 0  # no warning
print(titanic.loc[index_babies])  # doesn't change value in original df

''' SettingWithCopyWarning: We assigned new values with Chained Indexing.
It is not clear, whether we changed the original DataFrame and whether this
was our intention at all. So, this warning doesn't make much sense.
Changing the original dataframe along with the slice changes is unpredictable
and one should check before proceeding further ; so the best practice is we
didn't use chained indexing & we get no warning and it changes original df '''


''' Rules to remember '''
# If you want to work with and manipulate the whole DataFrame...
# ... avoid chained Indexing!!! use iloc or loc operators

print("\n Rules to remember:")
titanic = dfu.get_dataframe("titanic.csv")
titanic.iloc[1, 3] = 40  # 2nd row, 4th column, no warning
print(titanic.head())  # alters original df

index_babies = titanic.loc[titanic.age < 1, "age"].index
titanic.loc[titanic.age < 1, "age"] = 1  # no warning
print(titanic.loc[index_babies])  # alters original df

# If you want to work with and manipulate a Slice of a DataFrame...
# ...avoid chained Indexing ...and make a copy with .copy()

titanic = dfu.get_dataframe("titanic.csv")
age = titanic.age.copy()
print(age.head())

age[1] = 40  # no warning
print(age.head())
print(titanic.head())  # doesn't change value in original df

baby_ages = titanic.loc[titanic.age < 1, ["age", "sex"]].copy()
print(baby_ages)  # created a new df
baby_ages["age"] = 1  # no warning
print(baby_ages)
print(titanic.loc[index_babies])  # doesn't change value in original df
