import pandas as pd
import datetime


url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data"  # noqa: E501
''' Assign it to a variable called data and replace the
first 3 columns by a proper datetime index '''
# parse_dates gets 0, 1, 2 columns and parses them as the index
# data = pd.read_csv(url)
data = pd.read_csv(url, sep='\s+', parse_dates=[[0, 1, 2]])  # noqa: W605
print(data)
print(data.Yr_Mo_Dy.value_counts())
