import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic_imp.csv")
# print(titanic)

# Olympic Dataset
summer = dfu.get_dataframe("summer_imp.csv")
# print(summer)

# Sales Dataset
sales = dfu.get_indexed_dataframe("sales.csv", 0)
# print(sales)

# Men's Dataset
men2004 = dfu.get_dataframe("men2004.csv")
# print(men2004)

men2008 = dfu.get_dataframe("men2008.csv")
# print(men2008)
