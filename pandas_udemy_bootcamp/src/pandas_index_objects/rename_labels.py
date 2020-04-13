""" Renaming Index & Column Labels """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


summer_df = dfu.get_dataframe("summer.csv")
summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
print(summer_df.index)  # row index range/ row labels - range index
print(summer.index)  # labeled index
print(summer.index[0])

# to change a single row/column index using method rename()
print(summer.rename(
    mapper={"HAJOS, Alfred": "updated row index"}, axis="index"))
summer.rename(index={"HAJOS, Alfred": "updated row index"}, inplace=True)
print(summer.head())


print(summer.rename(
    mapper={"Gender": "Sex", "City": "updated column index"},
    axis="columns", inplace=True))
print(summer.head(2))
summer.rename(
    columns={"Gender": "Sex", "City": "updated column index"}, inplace=True)
print(summer.head())

# Here it gives no error in case of missing/ wrong/ duplicate keys.
