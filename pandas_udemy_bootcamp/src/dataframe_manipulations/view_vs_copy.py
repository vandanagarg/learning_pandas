''' View vs. Copy
Slicing a DataFrame / creating a view on the original DataFrame
creating views of dataframe; altering a view alters dataframe as well '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic = dfu.get_dataframe("titanic.csv")
print(titanic.head())

# selecting a column is making a view
age = titanic.age
print(age.head())

# check if age is a view: True
print(age._is_view)

# check if age is not a copy of something: True
print(age._is_copy is None)

age[1] = 40  # gives warning
''' SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame '''
print(age.head())
print(titanic.head())  # changes the values in original df

''' Slicing a DataFrame / creating a copy of the original DataFrame
creating a copy creates a new independent object and any manipulations
in copy object doesn't alter original dataframe '''
df_baby = titanic[titanic.age < 1]

print(df_baby._is_view)  # False
print(df_baby._is_copy is None)  # False: means is a copy
print(df_baby._is_copy)
# <weakref at 0x1008f6090; to 'DataFrame' at 0x1008a91f0>
print(df_baby._is_copy())  # gives the df from which it is copied

df_baby.age = 1  # gives warning
print(df_baby)  # changes the values only in copy object df_baby

index_babies = titanic.loc[titanic.age < 1, "age"].index
print(titanic.loc[index_babies])  # doesn't change value in original df
