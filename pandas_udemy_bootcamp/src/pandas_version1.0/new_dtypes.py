import pandas as pd
from create_dataframe import players2


players3 = players2.convert_dtypes()
players3.iloc[0, 0] = pd.NA

''' The NEW "nullable" Int64Dtype '''
# creating new series with missing value
s = pd.Series([1, 2, None], dtype="Int64")
print(s)

print(players2.Goals_2019.astype("Int64"))

print(players3.select_dtypes(include="Int64"))

# difference in o/p with old and new dtype
print(players2.Goals_2019 > 20)
# with NA it gives False
print(players3.Goals_2019 > 20)
# with NA it gives NA

''' The NEW StringDtype '''
# creating a nullable string series
animals = pd.Series(['Cat', None, 'Dog'], dtype="string")
print(animals)

print(players2.Nationality.astype("string"))

# select only text columns
print(players3.select_dtypes(include="string"))

# can apply all str/ string operations
print(players3.Club)
print(players3.Club.str.upper())  # o/p is also string
print(players3.Club.str.contains("FC"))  # o/p is new boolean dtype
print(players3.Club.str.count(pat="a"))  # o/p is new Int64 dtype
print(players3.Club.str.split(pat=" "))

''' The NEW "nullable" BooleanDtype '''
# creating a nullable boolean series
s = pd.Series([True, False, None], dtype="boolean")
print(s)

print(players2.World_Champion.astype("boolean"))
print(players3.select_dtypes(include="boolean"))

# hypothetical column states one league won/or not
cl = [True, True, True, False, True]
print(cl)

print(players2.World_Champion | cl)
# old dtype gives o/p as False
print(players3.World_Champion | cl)
# new dtype gives o/p as True, which is logically correct
