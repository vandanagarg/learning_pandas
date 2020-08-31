''' Advanced Indexing with reindex() '''
import pandas as pd
from create_dataframe import temp_file


# creating datetime indexes
temp = pd.read_csv(temp_file, parse_dates=["datetime"], index_col="datetime")
# downsampling - daily data
temp_d = temp.resample("D").mean()
# slicing rows for a particular interval for every year
chris = pd.date_range(end="2016-12-24", periods=3, freq=pd.DateOffset(years=1))
print(chris)
# filter dataframe for particular indexes to check temp for those days
print(temp_d.loc[chris])

# in this case we had the same periods as present in the df
# if we take a range for which some timestamps are not present in df
# then it shows error with loc and to over write them we can use reindex()
chris_ten = pd.date_range(end="2018-12-24", periods=10,
                          freq=pd.DateOffset(years=1))
print(chris_ten)
# print(temp_d.loc[chris_ten])  # gives error
print(temp_d.reindex(chris_ten))  # prints missing values

# fills all backwards missing values with first value
print(temp_d.reindex(chris_ten, method="bfill"))
# fills all forward missing values with last value
print(temp_d.reindex(chris_ten, method="ffill"))
# combination of bfill and ffill
print(temp_d.reindex(chris_ten, method="nearest"))

# but in this case it makes no sense to fill these missing values
# as in a years gap the temp never remains the same
