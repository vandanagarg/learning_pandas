import pandas as pd


url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv"  # noqa: E501
baby_names = pd.read_csv(url)
# print(baby_names.shape)

# Delete the column 'Unnamed: 0' and 'Id'
del baby_names['Unnamed: 0']
del baby_names['Id']
print(baby_names.head(10))

print(baby_names.Gender.value_counts())

# Group the dataset by name and assign to names
# you don't want to sum the Year column, so you delete it
del baby_names["Year"]

# group the data
names = baby_names.groupby("Name").sum()

# print the first 5 observations
print(names.head())

# print the size of the dataset
print(names.shape)

# sort it from the biggest value to the smallest one
print(names.sort_values("Count", ascending=0).head())

# How many different names exist in the dataset?
# as we have already grouped by the name, all the names are unique already
# get the length of names
print(len(names))

# What is the name with most occurrences?
print(names.Count.idxmax())
# OR
print(names[names.Count == names.Count.max()])

# How many different names have the least occurrences?
print(names[names.Count == names.Count.min()])
print(len(names[names.Count == names.Count.min()]))

# What is the median name occurrence?¶
print(names[names.Count == names.Count.median()])

# What is the standard deviation of names?
print(names.Count.std())

# Get a summary with the mean, min, max, std and quartiles.
print(names.describe())
