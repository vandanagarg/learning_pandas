""" Pandas Series indexing and Slicing works same as dataframes using
[]square bracket notation, iloc[] and loc[] operaters. The only problem is
since it is 1D array we can't slice for rows and columns at once for series """

import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
age = titanic_df["age"]

# Here labels are range so can't say if its a label/position based indexing
print(age[0])
print(age[2])

# Pandas here can't know that we are try to perform position based indexing
# print(age[-1])  # gives error
print(age.iloc[-1])  # iloc helps specify position based indexing

print(age[[3, 4]])

# slicing
print(age[:3])  # Here it behaves as position based indexing, excludes 3
print(age.iloc[:3])  # excludes 3
# Here iloc confirms it as position based indexing and is preferred to use
print(age.loc[:3])  # Here it behaves as label based indexing, includes 3

""" Thus prefer using iloc[] or loc[] operators to be sure of
which indexing are we applying """

# In case of labelled indexes and not ranges indexes position based indexing
# using square brackets is clear to pandas and gives no error

summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
# print(summer)

event = summer.Event
# print(event)

print(event[1])
print(event[-1])  # gives no error
print(event[:3])

# we can even use label name and do label based indexing
print(event["DRIVAS, Dimitrios"])
print(event["PHELPS, Michael"])

# Check equality
print(event.loc["PHELPS, Michael"].equals(event["PHELPS, Michael"]))

# In case of many occurencens the search fails and gives error
# If we try to pass a non exsisting label, it gives KeyError
# print(event[["DRIVAS, Dimitrios", "Donald"]])
