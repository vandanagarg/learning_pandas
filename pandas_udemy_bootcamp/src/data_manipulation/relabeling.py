''' Groupby Aggregation with Relabeling (new in Version 0.25) '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")
titanic = titanic[["survived", "pclass", "sex", "age", "fare"]]
titanic.info()
print(titanic.head())

# to check the survival rate for male and females
print(titanic.groupby("sex").survived.mean())
# Name: survived, dtype: float64
''' Here the name of pandas series in the output is shown as "survived"
which is not so intuitive and what we want to describe it as is
survival_rate. So in advanced version we are able to relabel our series/
column name/labels for more intuitive names '''
print(titanic.groupby("sex").agg(survival_rate=("survived", "mean")))

# for more than 1 columns and multiple aggregation functions
print(titanic.groupby("sex").agg({"survived": ["sum", "mean"],
      "age": ["mean"]}))  # multi indexing in the columns
# relabeling individual column label as:
print(titanic.groupby("sex").agg(survival_total=("survived", "sum"),
      survival_rate=("survived", "mean"), mean_age=("age", "mean")))
