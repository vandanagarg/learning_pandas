import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
# print(titanic)

# Olympic Dataset
summer = dfu.get_dataframe("summer.csv")
# print(summer)

# Sales Dataset
sales = dfu.get_indexed_dataframe("sales.csv", 0)
# print(sales)
