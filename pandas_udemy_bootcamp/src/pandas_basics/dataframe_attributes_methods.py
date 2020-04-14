"""Check implementation of various attributes and methods in pandas"""
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")

# To check a basic info (rows * columns) of a dataframe
print(titanic_df.shape)

# To check total elements in a dataframe
print(titanic_df.size)

# To validate index in a dataframe
print(titanic_df.index)

# To check columns in a dataframe
print(titanic_df.columns)

# A few methods in dataframes
print(titanic_df.head())
titanic_df.info()
print(titanic_df.min())
print(titanic_df.mean())

# Chaining methods/ Method Chaining
print(titanic_df.mean().sort_values())
print(titanic_df.mean().sort_values().head(2))
print(titanic_df.sort_values(by="age", ascending=False))  # True by default
