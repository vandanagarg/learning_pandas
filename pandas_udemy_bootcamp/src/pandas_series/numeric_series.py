""" Analyze numerical series with unique(), nunique() and value_count() """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
age = titanic_df["age"]

print(age.describe())
print(age.count())  # Gives the count of existing values
print(age.size)  # Gives the total count including missing values

# pandas method will handle missing values and gives the total of existing fields  # noqa: E501
print(age.sum())
# if we explicitly set skipna to false then it behaves like python sum method
print(age.sum(skipna=False))  # True by default
# here the inbuilt python function can't handle missing values and returns nan
print(sum(age))

print(age.mean())
print(age.median())
print(age.std())
print(age.min())
print(age.max())

# returns unique values in our series in order of appearance
print(age.unique())
# number of unique elements
print(len(age.unique()))
# gives the number of unique elements but excludes missing/NAN values
print(age.nunique())

# Gives the list of unique elements with the occurrence most to less frequent
print(age.value_counts())

# sorting: True by default High to low frequency (desc)
print(age.value_counts(sort=True))
# Here values are sorted on based of their appearance
print(age.value_counts(sort=False))

# missing values: True by default and NAN values are ignored
print(age.value_counts(dropna=True))
# else if set to false includes missing values too
print(age.value_counts(dropna=False))

# ascending: False by default and shows High to low frequency(desc)
print(age.value_counts(ascending=False))
# Changed to Low to High frequency
print(age.value_counts(ascending=True))

# normalize: False by default and calculates absolute frequency
print(age.value_counts(normalize=False))
# To calculate relative frequency set it to True
print(age.value_counts(normalize=True))
# 24.00    0.042017 - means 4.2% passengers are of 24yrs
# 22.00    0.037815 - - means 3.7% passengers are of 22yrs

# how is relative frequency calculated
# relative frequency = (absolute frequency) / (age.count())
# age.count() is the total number of non missing values
print(30/age.count())  # 30/714

# If we want to include missing values as well to calculate relative frequency
print(age.value_counts(dropna=False, normalize=True))
# here age.size is the total number of values including missing values
print(30/age.size)  # 30/891

# To make a frequency distribution kind of separation using bins
print(age.value_counts(bins=5))
print(age.value_counts(normalize=True, bins=10))  # could be any number depends

#  o/p of value_counts methods is a pandas series as well hence we can perform
# method chaining easily
# returns approx 1 as its a relative frequency
print(age.value_counts(dropna=False, normalize=True).sum())
