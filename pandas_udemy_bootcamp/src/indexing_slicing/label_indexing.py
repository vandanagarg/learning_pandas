""" Label based indexing and Slicing with loc[] """
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu

summer_df = dfu.get_indexed_dataframe("summer.csv", "Athlete")
# print(summer_df)

print(summer_df.loc["DRIVAS, Dimitrios"])

print(summer_df.loc["PHELPS, Michael"])  # all rows with label
print(summer_df.loc["PHELPS, Michael", "Medal"])  # all rows and column Medal
print(summer_df.loc["PHELPS, Michael", ["Medal", "Event"]])  # many rows/column
print(summer_df.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Medal", "Event"]])
print(summer_df.loc[:, ["Medal", "Event"]])

# slicing
print(summer_df.loc[:"CHASAPIS, Spiridon"])  # with unique labeled index
print(summer_df.loc[:"PHELPS, Michael"])  # with non-unique labeled index
# gives error :
# KeyError: "Cannot get right slice bound for non-unique label: 'PHELPS, Michael'"  # noqa: E501
