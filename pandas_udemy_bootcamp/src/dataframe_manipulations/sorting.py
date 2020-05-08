''' Sorting Dataframes  (Version 1.0 Update)'''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic = dfu.get_dataframe("titanic.csv")

# sorting - default ascending, not inplace; creates a copy
# sorting series
print(titanic.age.sort_values())
print(titanic.head())
# sorting dataframe using by parameter
print(titanic.sort_values(by='age'))
print(titanic)

# descending, missing values in the end and inplace=True
titanic.sort_values(by='age', ascending=False, inplace=True)
print(titanic)

# sorting multiple columns, all ascending
titanic.sort_values(by=['pclass', 'sex', 'age'], ascending=True, inplace=True)
print(titanic)

# sorting multiple columns, individual order
titanic.sort_values(by=['pclass', 'sex', 'age'], ascending=[
                        True, True, False], inplace=True)
print(titanic)

# on LHS we still have unsorted original indexes in order to sort them
titanic.sort_index(ascending=True, inplace=True)
print(titanic)  # here it becomes original df after sorting

# in order to sort df and reset its indexes using reset_index()
print(titanic.sort_values(by='age').reset_index(drop=True))

# in version 1.0 there is an additional parameter ignore_index which can be
# set True and is False by default
print(titanic.sort_values(by='age', ignore_index=True))
