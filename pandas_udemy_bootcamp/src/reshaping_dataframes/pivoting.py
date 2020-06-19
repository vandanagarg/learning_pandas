''' Pivoting Dataframes with pivot() '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Table1 Dataset
table1 = dfu.get_dataframe("table1.csv")
print(table1)
print(table1.shape)
''' This is aggregated data and if we separate out the medal's
column values for (Gold, Silver and Bronze) and make countries as row
indexes it will be more easy to visualize and understand and
this can be done with pivot method and creating pivots '''
table1.info()

''' pivot() method
index will be the column which we want to be new row index
columns will be mostly categorical data column where we have some
unique values to be splitted into columns
values will be the column which we want to be populated in our dataframe
'''
print(table1.pivot(index="Country", columns="Medal", values="Count"))

# filling up the missing values
table1_piv = table1.pivot(index="Country", columns="Medal", values="Count"
                          ).fillna(0)
print(table1_piv)
# Here the pivot method transforms the shape from long to wide format
print(table1_piv.shape)
table1_piv.info()

# COMPARING PIVOT() METHOD AND UNSTACK() METHOD
print(table1.head())
# First set indexes & then unstack inner index:(works same way as pivot method)
print(table1.set_index(["Country", "Medal"]).unstack(fill_value=0))
''' unstack() works on a multi-index dataframe
ideally pivot and unstack does the same work, the only difference is that
pivot()- applies on a column of a dataframe and use the categories of the
column to make new columns
unstack() - applies on the indexes of the multi indexed dataframe and make
new columns by pivoting the indexes '''
