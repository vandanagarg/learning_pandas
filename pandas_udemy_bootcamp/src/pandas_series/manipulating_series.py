""" Basic manipulations within pandas series:
insert, delete, update existing index/values """
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
age = titanic_df["age"]

dic_sales = {
    "Sun": 10, "Mon": 25, "Tues": 76,
    "Thur": 6, "Sat": 36, "Fri": 0, "Wed": None}
sale = pd.Series(dic_sales)
print(dic_sales)
print(sale)

sales = (pd.Series([10, 25, 38, 46, 56, 73, None, 95], index=[
    "Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun", "Mon"]))
print(sales)

sale["Wed"] = 5  # assigning a missing value, using label based indexing
sale.iloc[3] = 30  # updating existing value, using position based indexing
print(sale)

sales["Sun"] = 5  # assigning a missing value, using label based indexing
sales.iloc[2] = 30  # updating existing value, using position based indexing
print(sales)

# element wise or vector operations with pandas series/ dataframes.
# eg converting currency column from dollars to euros
# conversion = (sales/1.1)
print((sales/1.1))

euro_sales = (sales/1.1).round(2)  # making a new series
print(euro_sales)

sales = (sales/1.1).round(2)  # updates existing series

# In case of duplicate indexes(which is not recommended)
# if we try to update the value for a particular index using
# label based indexing, it will update its all occurrences
# sales["Mon"] = 0

# In case of a series from a dataframe if we try to update an
# element in series it will update dataframe as well, thus python
# will give a warning for that but we must validate before we update an
# element of a dataframe/series if it needs to be updated/ this behavior
print(age.head())
age.iloc[1] = 30
""" : SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame """
print(age.head())
print(titanic_df.head())
