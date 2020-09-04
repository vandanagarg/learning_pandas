''' Filling NA Values in Time Series
with bfill, ffill and interpolation '''
import pandas as pd
from create_dataframe import close, temp_file


close["Day"] = close.index.day_name()
close["Quarter"] = close.index.quarter
print(close.head())

''' here in the above df we only have data for businness days but
if we want to have indexes for all days, we create a separate
date index for all days '''
all_days = pd.date_range(start="2009-12-31", end="2019-02-06", freq="D")
print(all_days)

# reset index for close df for all days
close = close.reindex(all_days)
print(close.head(20))

# replace the day and quarter column accordingly
close.Day = close.index.day_name()
close.Quarter = close.index.quarter

# in case of stocks forward fill makes more sense as the
# stock price should be same as the previous day
close.fillna(method="ffill", inplace=True)
print(close.head(15))
''' we can even perform the same step while reindexing the close df
reindex() also provides the method parameter to fill missing values '''

# filling missing values for continuous data
temp = pd.read_csv(temp_file, parse_dates=["datetime"], index_col="datetime")
print(temp.head(10))

''' we try to upsample data i.e. instead of 1hour gap we create
30min gap and it creates missing values and since it is
continuous data we can use interpolate() to fill up missing values '''
temp = temp.resample("30 Min").mean()
print(temp.head(10))

# here i expect my NA values to get filled by mean of previous and next
# value by interpolate method and still we have a lot of
# customization options available too
print(temp.interpolate())
