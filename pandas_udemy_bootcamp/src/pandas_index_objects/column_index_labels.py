""" Changing Column Index Labels """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
print(titanic_df.head())
print(titanic_df.columns)

print(titanic_df.columns[0])
# titanic_df.columns[0] = "Alive"  # index object is immutable
# TypeError: Index does not support mutable operations

# We can't change a single index, we have to pass a complete new list/
# sequence if we have to change any of the column index

titanic_df.columns = [
    'alive', 'pclass', 'sex', 'age', 'sibsp', 'parch',
    'fare', 'embarked', 'new_deck']
print(titanic_df.head())

# setting columns name
print(titanic_df.columns.name)  # No existing value o/p - None
titanic_df.columns.name = "titanic_dataframe"
print(titanic_df.columns.name)
print(titanic_df.head())
print(titanic_df.tail())

# setting a row label name
print(titanic_df.index.name)  # No existing value o/p - None
titanic_df.index.name = "Passenger No."
print(titanic_df.index.name)
print(titanic_df.head())
# Now on first column it shows both column and row bale names
