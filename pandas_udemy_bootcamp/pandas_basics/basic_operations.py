"""First Data Inspection"""
import pandas as pd
from utilities.dataframe_utilities import DataframeUtilities as dfu

# titanic_df = dfu.get_dataframe("titanic.csv")
# # print(titanic_df)


# # To change Maximum and minimum rows setting
# print(pd.options.display.max_rows)
# print(pd.options.display.min_rows)
# # pd.options.display.max_rows = 900  # uncomment to change the max row limit
# # Earlier version it was 60 and used to display first and last 30 rows of a df
# # if the rows are more than 60.
# pd.options.display.min_rows = 20  # Allowed in latest version
# print(titanic_df)

# print(titanic_df.head())  # By default it prints first 5 rows
# print(titanic_df.head(10))  # Can be updated as well

# print(titanic_df.tail())  # By default it prints last 5 rows
# print(titanic_df.tail(2))  # Can be updated as well

# titanic_df.info()  # Summarize data at a glance about rows and columns

# # describe returns a summary statistics on numerical columns
# print(titanic_df.describe())

# # to check summary for non numerical columns
# print(titanic_df.describe(include="O"))

# """ Main 3 datatypes in pandas """
# # Dataframe
# print(type(titanic_df))  # <class 'pandas.core.frame.DataFrame'>
# # object titanic_df is an instance of class pandas dataframe

# # Series
# print(type(titanic_df["age"]))  # <class 'pandas.core.series.Series'>

# # Index Object
# print(titanic_df.columns)  # using attribute columns
# print(titanic_df.index)  # using attribute index
# print(type(titanic_df.columns))  # <class 'pandas.core.indexes.base.Index'>
# print(type(titanic_df.index))  # <class 'pandas.core.indexes.range.RangeIndex'>
