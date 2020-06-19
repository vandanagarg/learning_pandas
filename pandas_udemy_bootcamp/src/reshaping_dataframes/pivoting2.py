''' Limits of pivot() method
How to overcome these limitations using goupby() and unstack() method '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Table2 Dataset
table2 = dfu.get_dataframe("table2.csv")
print(table2)
table2.info()
print(table2.shape)
# print(table2.pivot(index="Country", columns="Medal", values="Count"))
''' Problem Statement:
again we want to pivot table2 data but we have some not real duplicates
in our dataset and that cause a problem while pivoting and gives error;
ValueError: Index contains duplicate entries, cannot reshape
So what it means is to pivot dataframe year column is causing problem as
it should have unique combination of medal and country column but is not true
in this case as we have some duplicate entries for medal and country column
for different years which gives us value error
Solution: What we can do here is aggregate the values of the duplicates, which
can be done using groupby(), since pivot() can't do aggregations and it can be
done using pivot_table() too. but here we are not focusing on aggregations but
on reshaping our dataframes. For aggregations we need to form a multi index
dataframe but we can't even make a multiindex dataframe using pivot() method
as it doesn't accept a dataframe as input and hence we use groupby() method
'''

# first make groups on combination of Country, Medal and Year column and then
# take count value for each combination
print(table2.groupby(["Country", "Year", "Medal"]).Count.sum())
# using unstack() we will now pivot on the inner index level
print(table2.groupby(["Country", "Year", "Medal"]).Count.sum().unstack())
# fill missing values
print(table2.groupby(["Country", "Year", "Medal"]
                     ).Count.sum().unstack().fillna(0))
# new shape
print(table2.groupby(["Country", "Year", "Medal"]
                     ).Count.sum().unstack().fillna(0).shape)
table2.groupby(["Country", "Year", "Medal"]
               ).Count.sum().unstack().fillna(0).info()
