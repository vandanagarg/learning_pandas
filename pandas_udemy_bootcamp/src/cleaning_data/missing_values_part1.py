''' missing values(N/A), Not a number(NaN) '''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # for statistical plotting
from create_dataframes import sales
from change_datatype import titanic, summer


print("\n part4:")

print(sales)
sales.info()
print(sales.loc["Steven", "Thu"])

# Manually assigning missing values
sales.iloc[1, 1] = None
print(sales)

# preferred way of assigning missing value (using np.nan)
sales.iloc[2, 2] = np.nan
print(sales)
sales.info()

''' sometimes in real world data instead of None or no values, string
values like ' ' whitespaces or "no data" or etc. are passed, which are
not seen as missing values or null values, in this case we must check such
values using methods like nunique(), value_counts() etc '''

# manual assignment
sales.iloc[2, 1] = " "
sales.iloc[2, 2] = "no data"
print(sales)
sales.info()

''' Detecting missing values -
First way to look for missing values is info() method,
it will give an idea on None/ NaN/ N/A values by checking total count '''

titanic.info()

''' Second way is using isna() or notna() method '''

print(titanic.isna())
# o/p is a dataframe with boolean values in place of missing values
# numerical conversion to get count of missing values/ rows
print(titanic.isna().sum(axis=0))
print(titanic.isna().any(axis=0))  # checks if any value in a row/column is NaN
print(titanic.isna().any(axis=1))  # gives boolean series
print(titanic[titanic.isna().any(axis=1)])  # get rows with missing values

# opposite method notna()
print(titanic.notna())  # returns opposite boolean series
# can be chained as well
print(titanic.notna().sum(axis=0))
print(titanic.notna().all(axis=0))  # returns True if no value is NaN

''' Using Graphical plots - 3rd way
The breaks in graphs indicate missing values at those points '''

plt.figure(figsize=(12, 8))
sns.heatmap(titanic.notna())
plt.show()
# here value 0 means missing value (black color), 1 is true
# it also helps to get an idea on positions of missing values

''' Fourth way is using value_counts() method
It gives the frequency of each unique value within the dataframe,
Thus next we need to replace incorrect data strings/values with NaN values
'''
print(titanic.Age.value_counts(dropna=False))
# replacing Missing Data with NaN
titanic.Age.replace(to_replace="Missing Data", value=np.nan, inplace=True)
titanic.info()  # decreased count for age column
print(titanic.Age.value_counts(dropna=False))

# more lines on plot
plt.figure(figsize=(12, 8))
sns.heatmap(titanic.notna())
plt.show()

# now since there is no more ambiguous data we can change datatype of age
titanic.Age = titanic.Age.astype("float")
print(titanic.Age)

# Olympic Dataset
summer.info()
print(summer[summer.isna().any(axis=1)])  # rows with missing values
