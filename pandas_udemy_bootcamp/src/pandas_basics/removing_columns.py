""" removing columns from a dataframe """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


summer_df = dfu.get_dataframe("summer.csv")

# to delete a column pass column label in drop method
print(summer_df.drop(columns="Sport"))  # inplace=False by default
summer_df.drop(columns=["Sport", "Discipline"], inplace=True)
print(summer_df.head())

# using labels parameter to drop row/column
print(summer_df.drop(labels="Event", axis=1))  # inplace=False by default
print(summer_df.drop(labels="Event", axis="columns"))
# 2 ways to set axis value to point to columns

# using keyword del
del summer_df["Event"]  # is not recommended
print(summer_df.head())

# or another way is to select only those specific columns which we want to keep
summer_df = dfu.get_dataframe("summer.csv")
summer_df = summer_df.loc[:, [
    "Year", "City", "Athlete", "Country", "Gender", "Medal"]]
print(summer_df.head())
