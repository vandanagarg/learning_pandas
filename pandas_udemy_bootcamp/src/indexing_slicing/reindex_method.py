""" Indexing and Slicing with reindex() """
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


summer_df = dfu.get_dataframe("summer.csv")
# print(summer_df)

# passing a non existing label 40000, age
print(summer_df.reindex(
    index=[0, 5, 3000, 40000], columns=["Athlete", "Medal"]))
# returns a label 40000 with NaN values

print(summer_df.reindex(
    index=[0, 5, 3000, 40000], columns=["Athlete", "Medal", "Age"]))
# returns a label, column 40000, Age with NaN values

""" Working with non unique indexes """

summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
# print(summer)

# When we don't pass an index specifically and just give the columns
print(summer.reindex(columns=["Medal", "Age"]))
# returns a column Age with NaN values

# passing a non unique row index, gives error
print(summer.reindex(index=["PHELPS, Michael"], columns=["Medal", "Age"]))
# ValueError: cannot reindex from a duplicate axis
