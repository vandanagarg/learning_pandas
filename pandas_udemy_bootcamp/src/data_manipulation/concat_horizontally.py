''' Horizontal concatenation '''
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


topfive_2004 = dfu.get_indexed_dataframe("topfive_2004.csv", "Athlete")
topfive_2008 = dfu.get_indexed_dataframe("topfive_2008.csv", "Athlete")
topfive_20008 = dfu.get_dataframe("topfive_2008.csv")
# print(topfive_2004, topfive_2008)

# with indexes
print(pd.concat([topfive_2004, topfive_2008], axis=1, ignore_index=False,
                keys=[2004, 2008], names=["Year"]))
# without indexes
print(pd.concat([topfive_2004, topfive_20008], axis=1, ignore_index=False,
                keys=[2004, 2008], names=["Year"]))

men04 = dfu.get_indexed_dataframe("men2004.csv", "Athlete")
men08 = dfu.get_indexed_dataframe("men2008.csv", "Athlete")
men008 = dfu.get_dataframe("men2008.csv")
# print(men04, men08)

# with indexes
men48 = pd.concat([men04, men08], axis=1, ignore_index=False, keys=[
        2004, 2008], names=["Year"])
print(men48)

# without indexes
men408 = pd.concat([men04, men008], axis=1, ignore_index=False, keys=[
        2004, 2008], names=["Year"])
print(men408)
