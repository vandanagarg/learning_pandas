''' Indexing and Slicing Time Series '''
import pandas as pd
from create_dataframe import temp_file


temp = pd.read_csv(temp_file, parse_dates=["datetime"], index_col="datetime")
# using loc operator we can perform label based indexing and slice our data
print(temp.loc["2013-01-01 01:00:00"])
print(temp.loc["2015"])  # all 2015 year data/rows
print(temp.loc["2015-05"])  # all 2015 May data/rows
print(temp.loc["2015-05-20"])  # all 2015 May 20 data/rows
print(temp.loc["2015-05-20"].shape)
print(temp.loc["2015-05-20 10"])
# print(temp.loc["2015-05-20 10:30"])  # gives error

# slicing for a particular period
print(temp.loc["2015-01-01": "2015-12-31"])
# either way is fine
print(temp.loc["2015-01-01": "2015-12-31"].equals(temp.loc["2015"]))
# arbitrary range
print(temp.loc["2014-01-01": "2015-12-1"])

# using different formats
print(temp.loc["20FEB2015"])
print(temp.loc["20FEBRUARY2015"])

# we can't slice for different timestamps
# print(temp.loc[["2015-05-20 10", "2015-05-20 12"]])  # gives error
# for this we must first convert the timestamps into date time index

two_timestamps = pd.to_datetime(["2015-05-20 10", "2015-05-20 12"])
print(two_timestamps)
# DatetimeIndex(['2015-05-20 10:00:00', '2015-05-20 12:00:00'], dtype='datetime64[ns]', freq=None)  # noqa: E501

# now can slice for timestamps as well
print(temp.loc[two_timestamps])
