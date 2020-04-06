""" Analyze single columns of a DataFrame (Pandas Series) """
import config_file  # noqa: F401
# from utilities.dataframe_utilities import DataframeUtilities as dfu
from utilities import DataframeUtilities as dfu

summer_df = dfu.get_dataframe("summer.csv")
print(summer_df)

summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
print(summer)
