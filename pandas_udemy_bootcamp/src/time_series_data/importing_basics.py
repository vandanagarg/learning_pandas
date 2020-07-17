''' Time Series Basics
Importing Time Series Data from csv-Files '''
import pandas as pd
from create_dataframe import temp, temp_file


# temperature dataset for NY and LA for years 2013 to 2016
# temp in degree celsius
print(temp.head())
temp.info()

# now to change the data type to datetime, we can do this while
# importing csv file by passing column label in this case
temp = pd.read_csv(temp_file, parse_dates=["datetime"])
print(temp.head())
temp.info()  # now the datatype is pandas internal datetime64[ns]
# [ns] indicates the accuracy

print(temp.describe())

print(temp.iloc[0, 0])  # Timestamp: Single point in time
print(type(temp.iloc[0, 0]))
# pandas specific datatype to store date time information
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# Whenever we have such date time information it always makes sense
# to store it as index, and we can do this while importing our dataframe
temp = pd.read_csv(temp_file, parse_dates=["datetime"], index_col="datetime")
# parse_dates to convert datatype to datetime and then
# index_col to set that column as index
print(temp.head())
temp.info()

print(temp.index)  # DatetimeIndex is collection of timestamps
print(temp.index[0])  # first time stamp
