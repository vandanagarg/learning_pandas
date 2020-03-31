"""Check implementation of various attributes and methods in pandas"""
# import pandas as pd
import python_basics as pyb

# To check a basic info (rows * columns) of a dataframe
print(pyb.titanic_df.shape)

# To check total elements in a dataframe
print(pyb.titanic_df.size)

# To validate index in a dataframe
print(pyb.titanic_df.index)

# To check columns in a dataframe
print(pyb.titanic_df.columns)

# A few methods in dataframes
print(pyb.titanic_df.head())
pyb.titanic_df.info()
print(pyb.titanic_df.min())
print(pyb.titanic_df.mean())

# Chaining methods/ Method Chaining
print(pyb.titanic_df.mean().sort_values())
print(pyb.titanic_df.mean().sort_values().head(2))
print(pyb.titanic_df.sort_values(by="age", ascending=False))  # True by default
