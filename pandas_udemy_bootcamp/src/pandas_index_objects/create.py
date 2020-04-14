""" Creating Index Objects """
import pandas as pd


list_one = [1, 2, 3]
# passing a list in pd.Index method - caps I
print(pd.Index(list_one))  # integer index object

list_two = ['m', 't', 'w']
print(pd.Index(list_two))  # string/object index object

print(pd.Index(range(1, 4), name="Range_index"))  # range index object
print(type(pd.Index((range(1, 4)))))
# <class 'pandas.core.indexes.range.RangeIndex'>

index_two = pd.Index(['mon', 'tues', 'wed'], name="days")
print(index_two)
print(type(pd.Index(['mon', 'tues', 'wed'], name="days")))
# string index object - <class 'pandas.core.indexes.base.Index'>

# Using custom indexes
print("Pandas Series:")
print(pd.Series(list_one, index=index_two))
print(pd.Series(list_two, index=index_two))
print(pd.Series(list_two, index=pd.Index(range(1, 4), name="Range_index")))
