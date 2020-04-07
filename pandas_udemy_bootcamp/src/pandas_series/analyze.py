""" Analyze single columns of a DataFrame (Pandas Series) """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu  # Type 1, 2
# from utilities.dataframe_utilities import DataframeUtilities as dfu  # Type 3

summer_df = dfu.get_dataframe("summer.csv")  # Type 1, 2, 3
print(summer_df)

summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
print(summer)
