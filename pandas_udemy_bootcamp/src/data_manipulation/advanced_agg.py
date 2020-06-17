''' Advanced aggregation with agg() '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
titanic = titanic[["survived", "pclass", "sex", "age", "fare"]]
titanic.info()
print(titanic.head())

# using single aggregation functions on groupby objects
print(titanic.groupby("sex").mean())
print(titanic.groupby("sex").sum())

# using more than 1 aggregation function on groupby objects(pass as a list)
print(titanic.groupby("sex").agg(["sum", "mean"]))
print(titanic.groupby("sex").agg(["mean", "sum", "min", "max"]))

''' customizing the aggregation methods for different columns as
for some columns some aggregations don't make much sense as min/max
for survived column, sum for pclass etc. Pass keys as column labels
and values as list of aggregation functions(FOR MORE THAN 1) '''

print(titanic.groupby("sex").agg({"survived": ["sum", "mean"],
      "pclass": "mean", "age": ["mean", "median"], "fare": "max"}))
