''' Merging, Joining and Concatenating DataFrames
adding rows with append() and pd.concat()
Here we will either add additional rows/observations to a
dataframe or we will combine 2 dataframes vertically '''
import pandas as pd
from create_dataframes import men2004, men2008


# adding/concatenating rows of 2 different dataframes
''' append method returns a new dataframe and appends rows from
men2008 dataframe on the end of(below) the men2004 dataframe '''
# original indexes will not be ignored
print(men2004.append(men2008, ignore_index=False))
# original indexes will be ignored
print(men2004.append(men2008, ignore_index=True))


''' Here in append method we can't identify which row came from
which dataframe and hence concat method can be used in order
to overcome this drawback (concat is direct pandas method) '''
# original indexes will not be ignored, men2004 on top and men2008 below
print(pd.concat([men2004, men2008], ignore_index=False, keys=None))
# original indexes will be ignored
print(pd.concat([men2004, men2008], ignore_index=True, keys=None))

''' Advantages:
1. In order to create multi-index/hierarchical dataframes we use
parameter keys to identify data from 2004 & 2008 datasets which is
not possible with append method '''
print(pd.concat([men2004, men2008], ignore_index=False, keys=[2004, 2008]))
# naming the outer index level using parameter names
print(pd.concat([men2004, men2008], ignore_index=False, keys=[
        2004, 2008], names=["Year"]))

''' 2. In concat method it is easy to add dataframes by passing all df's
in a list at once, whereas in append method we must select 1 dataframe to
which all other dataframes will be appended and then pass that list of other
dataframes to append method
3. Using concat method we can even add dataframes horizontally(columns) using
axis parameter, but append method only adds dataframes vertically(rows).
So concat() method is more general method with a lot of parameters '''

# saving the dataframe
men0408 = pd.concat([men2004, men2008], ignore_index=False, keys=[
        2004, 2008], names=["Year"])
# changing the indexes and converting them into columns
print(men0408.reset_index())
# dropping level_1 column and using new range indexes
print(men0408.reset_index().drop(columns="level_1"))
