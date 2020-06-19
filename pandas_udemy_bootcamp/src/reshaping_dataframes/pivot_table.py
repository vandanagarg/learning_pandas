''' Using pivot_table() for performing aggregation and reshaping dataframes '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Table2 Dataset
table2 = dfu.get_dataframe("table2.csv")
print(table2)
table2.info()
print(table2.shape)
# for the same dataframe we will now use pivot_table() method for reshaping and
# performing aggregations
print(table2.pivot_table(index="Country", columns="Medal", values="Count",
      aggfunc="sum", fill_value=0))

# same can be done using groupby() and unstack() method
print(table2.groupby(["Country", "Medal"]).Count.sum().unstack(fill_value=0))

# additional parameters for pivot_table() method
# parameter - margins: it adds up additional row & column showing up the total
# of all rows and columns
print(table2.pivot_table(index="Country", columns="Medal", values="Count",
      aggfunc="sum", fill_value=0, margins=True))

# this has to be done manually in groupby method (no builtin parameter)
agg = table2.groupby(["Country", "Medal"]).Count.sum().unstack(fill_value=0)
agg["All"] = agg.sum(axis=1)
agg.loc["All"] = agg.sum(axis=0)
print(agg)
