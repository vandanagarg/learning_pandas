""" Advanced Indexing and Slicing using range() """
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


summer_df = dfu.get_dataframe("summer.csv")
# print(summer_df)
summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
# print(summer)

# Case1: Getting the first 5 rows and rows 354 and 765
rows = list(range(5)) + [354, 765]
print(rows)
print(summer_df.iloc[rows])

# Case 2: Getting the first three columns and the columns "Gender" and "Event"
col = summer_df.columns[:3].to_list() + ["Gender", "Event"]
print(col)
print(summer_df.loc[:, col])

# Case 3: Combining Position- and label-based Indexing: Rows at Positions 200
# and 300 and columns "Athlete" and "Medal"
print(summer_df.loc[[200, 300], ["Athlete", "Medal"]])

# Case 4: Combining Position- and label-based Indexing: Rows "PHELPS Michael"
# and positional columns 4 and 6
col = summer.columns[[4, 6]]
print(col)
print(summer.loc["PHELPS, Michael", col])
# print(summer.ix["PHELPS, Michael", [4, 6]])
