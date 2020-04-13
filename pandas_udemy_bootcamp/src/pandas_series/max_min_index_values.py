""" To find max or min column values or index values """
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
age = titanic_df["age"]

# nlargest() and nsmallest() methods

print(age.sort_values(ascending=False))
print(age.sort_values(ascending=False).head(3))  # 3 oldest passenger
print(age.nlargest())  # prints the largest values by default 5
print(age.nlargest(n=3))  # returns largest 3 values
print(age.nsmallest())  # prints the smallest values by default 5
print(age.nsmallest(n=3))  # returns smallest 3 values

# idxmin() and idxmax() methods
""" To find index labels of smallest and highest value/element """

print(age.nlargest(n=3).index)
print(age.nlargest(n=3).index[0])  # largest element index
print(age.nsmallest(n=3).index[0])  # smallest element index
# same can be done using below methods
print("Using idxmin() and idxmax() methods")
print(titanic_df.age.idxmax())
print(titanic_df.age.idxmin())

# getting full info of that passenger
print(titanic_df.loc[titanic_df.age.idxmax()])  # returns pandas series

# Checking dictionary max/min indexes
dic_sales = {
    "Sun": 10, "Mon": 25, "Tues": 76, "Thur": 6,
    "Sat": 36, "Fri": 0, "Wed": None}
print(dic_sales)

sales = pd.Series(dic_sales)
print(sales)

print(sales.sort_values(ascending=True).index[0])
print(sales.idxmin())
print(sales.sort_values(ascending=False).index[0])
print(sales.idxmax())
