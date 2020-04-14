""" removing rows from a dataframe """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


summer_df = dfu.get_indexed_dataframe("summer.csv", "Athlete")

# to delete a row pass row index label in drop method
print(summer_df.drop(index="HAJOS, Alfred"))  # inplace=False by default
summer_df.drop(index=["HAJOS, Alfred", "HERSCHMANN, Otto"], inplace=True)
print(summer_df.head(10))

# using labels parameter to drop rows
print(summer_df.drop(labels="DRIVAS, Dimitrios", axis=0))
# inplace=False by default
print(summer_df.drop(labels="DRIVAS, Dimitrios", axis="index"))
# 2 ways to set axis value to point to row

# mostly we should be deleting the rows if a particular boolean condition
# is satisfied, in that case should fetch the rows that are meeting the
# condition and assign them back to dataframe
summer_df = summer_df.loc[summer_df.Year == 1996]
print(summer_df.head())

# or another way is to select only those specific rows which we want to keep
summer_df = dfu.get_indexed_dataframe("summer.csv", "Athlete")
# print(summer_df.head())

# using ~ operator and boolean series to drop the rows
series1 = summer_df.Year == 1996
series2 = summer_df.Sport == "Aquatics"
summer_df = summer_df.loc[~(series1 | series2)]
print(summer_df.head())
print("\n ")
print((summer_df.Year == 1996).value_counts())
print("\n ")
# checking value of 1996 in numpy array: summer_df.Year.values
print(1996 in summer_df.Year.values)
print("\n ")
print(summer_df.Sport.isin(["Aquatics"]).any())
# or we can use this way
print((summer_df.Sport == "Aquatics").any())
