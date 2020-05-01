''' Ranking Dataframes with rank() '''
import pandas as pd
import config_file  # noqa: F401
from utilities.dataframe_utilities import DataframeUtilities as dfu


titanic = dfu.get_dataframe("titanic.csv")

sales = pd.Series([15, 32, 45, 21, 55, 15, 0], index=[
    "Mo", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
print(sales)

print(sales.sort_values(ascending=False))
print(sales.rank())
print(sales.rank().sort_values(ascending=False))

# But we want to give friday highest sale rank 1
print(sales.rank(ascending=False).sort_values())

# by default for equal values rank method takes average of positions & assign
# that rank to all values eg: avg of 5 & 6 5.5 assigned to both mon and sat
# by default
print(sales.rank(ascending=False, method="average").sort_values())
# here it assigns min rank to the values
print(sales.rank(ascending=False, method="min").sort_values())

# pct parameter gives percentage of ranks eg: fri rank = 1/7 = 0.14
print(sales.rank(ascending=False, method="min", pct=True).sort_values())

# ranking fare column, highest fare has lowest rank here & vice versa
print(titanic.fare.rank(ascending=False))

titanic["fare_rank"] = titanic.fare.rank(ascending=False, method="min")
print(titanic.head())
print(titanic.sort_values("fare", ascending=False))
# in order to drop the column fare_rank
# titanic.drop(columns="fare_rank", inplace=True)
