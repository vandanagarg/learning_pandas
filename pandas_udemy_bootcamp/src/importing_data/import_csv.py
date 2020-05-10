import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


source_file = dfu.FILE_PATH + "titanic.csv"
with open(source_file) as f:
    text = f.readlines()

print(text)
print(len(text))

# summer_df = dfu.get_dataframe("summer.csv")
titanic_df = dfu.get_dataframe("titanic.csv")
titanic_df = pd.read_csv(source_file, index_col='pclass')
print(titanic_df)

pd.read_csv(source_file, header=0)  # by default
pd.read_csv(source_file, header=None)  # no header assigned
titanic = pd.read_csv(source_file, header=1)  # 1st row as header

# new column label names
titanic = pd.read_csv(source_file, header=0, names=[
                      "alive", "class", "gender", "age", "sibsp",
                      "parch", "price", "emb", "deck"])

# read selective columns
titanic = pd.read_csv(source_file, header=0, usecols=[
                      "survived", "pclass", "sex", "age"])
print(titanic)

# changes in the dataframe post reading from file
titanic = pd.read_csv(source_file, header=0, index_col="pclass", usecols=[
                      "survived", "pclass", "sex", "age"])
print(titanic.head())
titanic.columns = ["alive", "gender", "age"]
titanic.index.name = "class"
print(titanic.head())
