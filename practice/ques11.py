import pandas as pd
from file_utilities import FILE_PATH


file = "dataset_US_Crime_Rates_1960_2014.csv"

crime = pd.read_csv(FILE_PATH + file, header=0)
# print(crime)

print(crime.columns.dtype)
print(crime.columns)
print(crime.describe())
crime.info()

crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()
print(crime.head())

crime = crime.set_index('Year', drop=True)

del crime["Total"]
print(crime.head())

# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population
print(crimes.head())

# apparently the 90s was a pretty dangerous time in the US
print(crime.idxmax(0))
