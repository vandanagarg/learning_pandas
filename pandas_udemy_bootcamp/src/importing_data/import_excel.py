''' Importing from excel files using pd.read_excel() '''
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


source_file = dfu.FILE_PATH + "sales.xls"

sales = pd.read_excel(source_file)
sales = pd.read_excel(source_file, index_col=0)
sales = pd.read_excel(source_file, index_col=0, header=0)
# zero based indexing is applicable here
# header=0 by default
# if we pass None to any of the parameter it creates a range index as labels
print(sales)
sales.info()

# assigning new column and indexes name
sales = pd.read_excel(source_file, index_col=0, header=0, names=[
    "Name", "Loc_city", "Loc_Country", "Revenue", "Add_Comp"])
print(sales)

# reading selective columns
sales = pd.read_excel(source_file, index_col=0, header=0, usecols="A:C")
# pass column names as a string, recommended way to use column labels
sales = pd.read_excel(source_file, index_col=0, header=0, usecols="C:E")
sales = pd.read_excel(source_file, index_col=0, header=0, usecols="A,C:E")
sales = pd.read_excel(source_file, index_col=0, header=0, usecols=":C")
# sales = pd.read_excel(source_file, index_col=0, header=0, usecols="C:")
# gives error - IndexError: list index out of range
sales = pd.read_excel(source_file, index_col=0, header=0, usecols=[0, 3, 4])
# sales = pd.read_excel(source_file, index_col=0, header=0, usecols=2)  # error
#  ValueError: Passing an integer for `usecols` is no longer supported.
# Please pass in a list of int from 0 to `usecols` inclusive instead.
sales = pd.read_excel(source_file, index_col=0, header=0, usecols=[
                    "City", "Sales"])  # not recommended
print(sales)
