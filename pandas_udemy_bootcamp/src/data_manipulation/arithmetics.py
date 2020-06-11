''' Arithmetic between Pandas Objects/Data Alignment
Arithmetics between dataframes is done on the basis of indexes by comparing
all possible options of index pairs. It can be carried out using arithmetic
operators or arithmetic functions, but functions provide much more
functionality and ease to manipulate data using different parameters '''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


topfive_2004 = dfu.get_indexed_dataframe("topfive_2004.csv", "Athlete")
topfive_2008 = dfu.get_indexed_dataframe("topfive_2008.csv", "Athlete")
print(topfive_2004, topfive_2008)

''' Here we have some common values in both dataframes and some are unique
Also the column bronze label isn't identical in both dataframes '''
# addition using arithmetic operator
print(topfive_2004 + topfive_2008)
# here in case of addition with a missing value it returns a missing value,
# hence it has populated only 6 values and rest all are NAN values

''' To handle addition with missing values we must update missing value to
behave as 0 in our case using parameter fill_value in method add()'''
print(topfive_2004.add(topfive_2008, fill_value=0))
# this treats addition with NAN value as addition with 0

# to remove other missing values because of bronze column label
topfive_2008.rename(columns={"bronze": "Bronze"}, inplace=True)
print(topfive_2004.add(topfive_2008, fill_value=0))  # no NAN values now

# to substract two dataframes
print(topfive_2004.sub(topfive_2008, fill_value=0))
# it can be interpreted as eg PHELPS, Michael won 2 medals more in
# 2008 event than 2004 event
