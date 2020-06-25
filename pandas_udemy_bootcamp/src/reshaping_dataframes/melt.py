''' Melting Dataframes with melt()
Melting a dataframe is opposite to pivoting a dataframe
Changes wide format of a dataframe to long format'''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Table_2012 Dataset
table_2012 = dfu.get_dataframe("table_2012.csv")
print(table_2012)
table_2012.info()
print(table_2012.shape)
print(table_2012.melt(id_vars="Country", value_vars=["Gold",
                      "Silver", "Bronze"]))
''' the columns "Gold", "Silver", "Bronze" un-melt to long format
where it takes the default column name variable and value to show
the count and value of records which is customizable with following
parameters '''
print(table_2012.melt(id_vars="Country", value_vars=["Gold",
                      "Silver", "Bronze"], var_name="Medal",
                      value_name="Count"))

melt_2012 = table_2012.melt(id_vars="Country", value_vars=["Gold",
                            "Silver", "Bronze"], var_name="Medal",
                            value_name="Count")
print(melt_2012)
print(melt_2012.shape)  # 3 times the original shape long format

# pivoting the dataframe again
print(melt_2012.pivot(index="Country", columns="Medal", values="Count"
                      ).sort_values("Gold", ascending=False))
