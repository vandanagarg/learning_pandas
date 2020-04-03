"""Selecting particular columns/rows using specific ways/methods"""
from dataframe_utilities import DataframeUtilities as dfu

titanic_df = dfu.get_dataframe("titanic.csv")
# print(titanic_df)

# selecting one column age - output is in form of pandas series
print(titanic_df["age"])

# The datatype of output column is pandas series
print(type(titanic_df["age"]))  # <class 'pandas.core.series.Series'>

# selecting more than one column - we must pass the column names as a list
print(titanic_df[["age", "sex"]])

# The datatype of output column now is pandas dataframe
print(type(titanic_df[["age", "sex"]]))  # <class 'pandas.core.frame.DataFrame'>  # noqa: E501

# We can change the sequence and output order by just interchanging the columns
print(titanic_df[["sex", "age"]])

# In case we want to return a single column as a dataframe and not as a series
# We should then pass the column name inside a list
print(titanic_df[["age"]])
# The datatype of output column now is pandas dataframe
print(type(titanic_df[["age"]]))  # <class 'pandas.core.frame.DataFrame'>


""" Using dot notation or attribute notation to select columns """
# so the titanic_df dataframe has a attribute age and vice versa for other
# columns what we can do is fetch data for a single column by using its
# attribute along with dot notation and the o/p is pandas series.
print(titanic_df.age)

# To check if two methods are equal
print(titanic_df.age.equals(titanic_df["age"]))  # True

# But in case of unclean data as in where we have spaces in column names
# which is anyways wrong we must avoid using dot notation or we must
# first either clean the data and correct column names and then use
# dot notation
