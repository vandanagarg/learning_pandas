''' Group By operations
(source df) -> [split] (group_by object/df) -> [apply] -> [combine] (target df)
'''
from create_dataframes import titanic


titanic.info()
titanic_slice = titanic.iloc[:10, [2, 3]]
print(titanic_slice)

gbo = titanic_slice.groupby("Gender")
print(gbo)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7ff02da7c8b0>

print(type(gbo))
# <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

# groupby objects have specific attributes
print(gbo.groups)

# transforming groupby object into a list
l_gbo = list(gbo)
print(l_gbo)

print(len(l_gbo))  # 2 elements in list

# list of tuples
print(l_gbo[0])  # 1st element
print(type(l_gbo[0]))  # <class 'tuple'>
print("\n elements of tuple:")
# 1st element of tuple
print(l_gbo[0][0])  # string object
print(type(l_gbo[0][0]))  # <class 'str'>
# 2nd element of tuple
print(l_gbo[0][1])  # dataframe
print(type(l_gbo[0][1]))  # <class 'pandas.core.frame.DataFrame'>

# similarly
print(l_gbo[1])  # 2nd element
print(type(l_gbo[1]))  # <class 'tuple'>

''' Groupby method splits our original dataframe into 2 dataframes
or objects and 1st df contains all rows with female passengers and
2nd df contains all rows with male passenger's
'''

# we can even create slices out of titanic_slice dataframe
titanic_slice_f = titanic_slice.loc[titanic_slice.Gender == "female"]
titanic_slice_m = titanic_slice.loc[titanic_slice.Gender == "male"]
print(titanic_slice_f, titanic_slice_m)

# to check if o/p of slicing dataframe is equal to group by o/p
print(titanic_slice_f.equals(l_gbo[0][1]))
print(titanic_slice_m.equals(l_gbo[1][1]))

# we can even iterate over our groupby object using for loop, and
# for each element in our group by object we want to print dataframe
for element in gbo:
    print(element[1])
