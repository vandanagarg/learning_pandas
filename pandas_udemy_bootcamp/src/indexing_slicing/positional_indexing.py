""" Position based indexing and Slicing with iloc[] """
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu

summer_df = dfu.get_dataframe("summer.csv")
# print(summer_df)

# Changing default indexes
summer_df.info()  # RangeIndex: 31165 entries, 0 to 31164
# earlier it prints default indexes as numbers
# if we want to make a specific column to act as a index use index_col
# give column name while reading file and it decreases our data columns

summer_df = dfu.get_indexed_dataframe("summer.csv", "Athlete")
summer_df.info()  # Index: 31165 entries, HAJOS, Alfred to LIDBERG, Jimmy

# reading rows
print(summer_df.iloc[0])  # o/p is pandas series for one row
# Here the name of the pandas series will be the name of the label
print(type(summer_df.iloc[0]))  # <class 'pandas.core.series.Series'>

print(summer_df.iloc[-1])  # o/p is pandas series for one row

# More than one row pass a list of indexes or directly slice indexes
print(summer_df.iloc[[1, 2, 3]])  # o/p is pandas dataframe for more than 1 row
print(summer_df.iloc[11:13])  # o/p is pandas dataframe for more than 1 row
print(type(summer_df.iloc[[1, 2, 3]]))  # <class 'pandas.core.frame.DataFrame'>

# last 5 rows
print(summer_df.iloc[-5:])  # here the o/p is all 5 rows
print(summer_df.iloc[-5:-1])  # here the o/p is only 4 rows as -1 is exclusive

# all rows
print(summer_df.iloc[:])

# random rows
print(summer_df.iloc[[111, 9032, 863]])

# Slicing using iloc[]

# Getting a single/multiple elements (slice/ subset)
print(summer_df.iloc[0, 4])
print(summer_df.iloc[0, :3])  # o/p is pandas series
print(summer_df.iloc[0, [0, 2, 5, 7]])  # o/p is pandas series
print(summer_df.iloc[34:37, [0, 2, 5, 7]])  # o/p is pandas dataframe

# selecting columns
print(summer_df.iloc[:, 4])
print(type(summer_df.iloc[:, 4]))  # o/p is pandas series
# <class 'pandas.core.series.Series'>
