''' Initial Analysis/ Visual Inspection of Time Series '''
import pandas as pd
import matplotlib.pyplot as plt
from create_dataframe import temp_file


temp = pd.read_csv(temp_file, parse_dates=["datetime"], index_col="datetime")
temp.info()
print(temp.describe())
print(temp.LA.value_counts())

# graphical analysis using plot method for time series
temp.plot(figsize=(15, 7))  # single plot

temp.plot(figsize=(15, 7), subplots=True)  # different plots

temp.plot(figsize=(15, 7), subplots=True, layout=(1, 2))  # different layouts

# now since we need to compare two series side by side we must have the same
# scale and thus the y axis should be shared amongst them
temp.plot(figsize=(15, 7), subplots=True, layout=(1, 2), sharey=True)
plt.show()  # by default line plot
# x axis for index as in datetime
# y axis for temperature

''' now since we have a lot of data points and the data is on hourly basis so
the graph is not so obvious and it makes more sense to aggregate data on
weekly or monthly basis so that we get discrete data points '''
