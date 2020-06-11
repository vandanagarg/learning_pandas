''' Till now we added dataframes vertically and we had dataframes with
same column name and same structure now lets add 2 dataframes with
different columns names and different structure. For this we will
update the existing dataframes '''
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu
from create_dataframes import men2004, men2008


men2004.columns = ["Name", "Medals"]
men2004["Success"] = "Yes"
print(men2004)

# Pandas merges dataframes where we have identical column labels
# and for non identical columns pandas creates new column labels
# in concatenated dataframe and marks missing values as NAN
men0408 = pd.concat([men2004, men2008], ignore_index=False, keys=[
        2004, 2008], names=["Year"])
print(men0408)

# dropping Success column
men2004.drop(labels=["Success"], axis=1, inplace=True)
print(men2004)

# giving same column labels/names to both dataframes
men2008.columns = men2004.columns
print(men2008.head())

# now as expected we get a clean concatenated dataframe
men0408 = pd.concat([men2004, men2008], ignore_index=False, keys=[
        2004, 2008], names=["Year"])
print(men0408)

''' Concatenating indexed dataframes '''
men04 = dfu.get_indexed_dataframe("men2004.csv", "Athlete")
men08 = dfu.get_indexed_dataframe("men2008.csv", "Athlete")

''' here in this case we create multi-indexed structure and we also
have our former indexes but if we set ignore_index to true then we
loose our former indexes which might be essential for us '''
men48 = pd.concat([men04, men08], ignore_index=False, keys=[
        2004, 2008], names=["Year"])
print(men48)

# not recommended in case of indexed dataframes if index information is needed
men48 = pd.concat([men04, men08], ignore_index=True, keys=[
        2004, 2008], names=["Year"])
print(men48)  # creates a range index and looses all other indexes
