''' Barcharts and Piecharts
These plots are specifically used to visualize data that is already aggregated
or for discrete variables. To plot continuous variables histograms are used '''
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu
import matplotlib.pyplot as plt


summer_2012 = dfu.get_indexed_dataframe("summer_2012.csv", "Country")
print(summer_2012)
plt.style.use("seaborn")

# vertical plot
summer_2012.Medal.plot(kind="bar", figsize=(12, 8), fontsize=12)
plt.show()  # bars get labelled as per the index label

# horizontal plot
summer_2012.Medal.plot(kind="barh", figsize=(12, 8), fontsize=12)
plt.show()  # bars get labelled as per the index label

summer_2012.Medal.plot(kind="pie", figsize=(12, 8), fontsize=12)
plt.show()
