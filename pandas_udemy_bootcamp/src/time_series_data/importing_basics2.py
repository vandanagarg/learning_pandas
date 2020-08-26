''' Time Series Basics2
Converting Strings to datetime objects with
pd.to_datetime() (used to convert string objects to datetime objects)
The earlier way was using parse_dates and index_col parameter of
read_csv() method and now we use direct pandas methods '''
import pandas as pd
from create_dataframe import temp


print(temp.head())
temp.info()
print(temp.datetime)
print(temp.datetime[0])

# using to_datetime() method to directly convert
# datetime column's string format to datetime format
print(pd.to_datetime(temp.datetime))

# to set this datetime column as index use set_index()
temp = temp.set_index(pd.to_datetime(temp.datetime)).drop("datetime", axis=1)
print(temp)
temp.info()
print(temp.index)

# handling different date/time formats by pandas
# by default format is year/month/day if we switch any gives error
print(pd.to_datetime("2015-05-20"))
print(pd.to_datetime("2015-05-20 10"))
print(pd.to_datetime("20150502"))
print(pd.to_datetime("2015/05/02"))
print(pd.to_datetime("2015 05 02"))
print(pd.to_datetime("2015-05-02"))
# print(pd.to_datetime("2015-15-02"))  # gives error
# other alternative is using MAY
print(pd.to_datetime("2015 May 20"))
print(pd.to_datetime("May2015 20"))
print(pd.to_datetime("2015 20th may"))

# passing a sequence of dates: if more than one date is
# passed we get a datetime index by default
print(pd.to_datetime(["2015 20th may", "2015 - 09 - 4"]))

# we can handle errors for a null or incorrect datetime using errors parameter
print(pd.to_datetime(["2015 20th may", "2015 - 09 - 4", ""], errors="coerce"))
print(pd.to_datetime(["2015 20th may", "2015 - 09 - 4", "Elephant"],
                     errors="coerce"))
