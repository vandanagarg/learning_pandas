''' Reshaping Dataframes '''
from create_dataframes import titanic
from create_dataframes import titanic as titanic1


print(titanic.head())
titanic.info()
''' Transposing dataframes
first way to reshape a dataframe is transposing it '''
print(titanic.T)  # using attribute T
# index labels are now replaced with initial column labels
# and column labels have changed to range index and vice versa
print(titanic.transpose())  # using method transpose()
titanic = titanic.transpose()
titanic.info()

''' * The pandas is mostly generalized in a way that we have
observations as rows and characteristics of observations as columns.
* Like we have observations as titanic passangers and their
characteristics are their age, pclass etc and each characteristic
should have a particular datatype as it gives the same information.
* But if we transpose the dataframe: the datatype for all columns
changes to object as it then contains values with mix datatypes.
* So it might not be a great choice here as it also leads to a very
wide dataframe which is hard to interpret as well.
* Now if we try to again transpose the dataframe the pandas has lost
its actual information and datatypes and just assigns them as object
datatype which cause issues for any further evaluations '''

titanic = titanic.T
titanic.info()

print(titanic.survived.mean())  # no errors

# print(titanic.groupby(["sex", "pclass"]).survived.mean())  # gives data error
# pandas.core.base.DataError: No numeric types to aggregate

# using original dataframe
print(titanic1.groupby(["sex", "pclass"]).survived.mean())
print(titanic1.groupby(["sex", "pclass"]).survived.mean().unstack().T)
titanic1.groupby(["sex", "pclass"]).survived.mean().unstack().T.info()
''' In this case it might be a good idea to transpose the datframe as we have
only numerical (average) data and it will hence won't update the datatypes
and for representation purpose it will have more intuitive column labels to
represent the data and numerical indexes will now be changed to row indexes '''
