''' Using pd.merge pandas direct method and join() method '''
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


men2004 = dfu.get_indexed_dataframe("men2004.csv", "Athlete")
men2008 = dfu.get_indexed_dataframe("men2008.csv", "Athlete")
print(men2004.head())
print(men2008.head())

# using merge() method
print(men2004.merge(men2008, how="outer", on="Athlete",
      suffixes=("_2004", "_2008"), indicator=True))
# using direct pandas merge() method
print(pd.merge(men2004, men2008, how="outer", on="Athlete",
      suffixes=("_2004", "_2008"), indicator=True))
# same results

''' using Join() method, can perform all kinds of joins, but there is a
specific case where we can find use join method more efficiently and that
is where we have 2 dataframes with same index labels/ index names as here
in our case we have Athlete as same index label '''
men_join = men2004.join(men2008, how="outer", lsuffix="_2004", rsuffix="_2008")
print(men_join.tail(50))
# no additional _merge column information option, the o/p is sorted
