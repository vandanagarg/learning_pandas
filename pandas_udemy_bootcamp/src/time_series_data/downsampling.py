''' Downsampling Time Series with resample()
How to convert from one frequency to another frequency with resample method '''
import pandas as pd
import matplotlib.pyplot as plt
from create_dataframe import temp_file


plt.style.use("seaborn")
temp = pd.read_csv(temp_file, parse_dates=["datetime"], index_col="datetime")
''' So here we have 3 years hourly data and it is difficult to visualize these
higher frequencies so we must convert/agg it into lower frequencies i.e:hourly
to weekly or monthly and converting data from high to low frequencies is also
called as downsampling, resampling works similar to groupy by '''

''' 1st Part of downsampling: group data use resample() & specific rule "D" '''
# resample on daily basis
print(temp.resample("D"))  # DatetimeIndexResampler object
# print(list(temp.resample("D")))
print(len(list(temp.resample("D"))))  # individual dataframe for each day

# each element is a tuple 1st element is Timestamp information and 2nd
# element is df for respective Timestamp/day's hourly data
print(list(temp.resample("D"))[0])
# selecting Timestamp in tuple
print(list(temp.resample("D"))[0][0])
# selecting dataframe in tuple
print(list(temp.resample("D"))[0][1])

''' 2nd Part aggregate data using appropriate function
how to convert 24 datapoints to one data point '''
# chaining aggregation function
# here we take first value/midnight time stamp for each group
print(temp.resample("D").first())

# different samples
print(temp.resample("2H").first())
# default month end and mean temp values
print(temp.resample("M").mean())
# custom day/range - only the labels change here
# the value remains same ie:mean()
print(temp.resample("MS", loffset="14D").mean())

# quarterly
print(temp.resample("Q").mean())
print(temp.resample("Q-Feb").mean())

# yearly
print(temp.resample("Y").mean())
print(temp.resample("YS").mean())

''' More Descriptive/intuitive labels
One thing we might notice in agg labels is that if we have monthly
data it still shows up a single date as a label so we must update the
label to indicate a months data exclusively using parameter kind to
convert an index to either datetimeindex or periodindex '''
print(temp.resample("M", kind="period").mean())
print(temp.resample("W", kind="period").mean())
print(temp.resample("Q", kind="period").mean())
print(temp.resample("A", kind="period").mean())

# We can further save the agg df
temp_m = temp.resample("M", kind="period").mean()
temp_m.info()  # we now have periodic indexes
print(temp_m.index)
print(temp_m.index[0])  # period index with monthly frequency

# graphical plots
# much cleaner line plot and a consistent plot
temp_m.plot(figsize=(15, 8), fontsize=15)
# messy and a lot of oscillations less readable
temp.plot(figsize=(15, 8), fontsize=15)
plt.show()
