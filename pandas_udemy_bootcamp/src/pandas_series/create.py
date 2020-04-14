""" We can either create a pandas series by reading a single row/column of
a pandas dataframe or using below ways """
import pandas as pd
import numpy as np
import config_file  # noqa: F401
from utilities.file_utilities import FileUtilities


PATH = FileUtilities.get_abs_path("../../Course_Materials_Part1/Video_Lecture_NBs/")  # noqa: E501
file_name = PATH + "summer.csv"
summer_df = pd.read_csv(file_name, usecols=["Athlete"], squeeze=True)
# squeeze by default is False, if we make it true then it reads the column
# as series instead of dataframe
print(summer_df)


# Using function pd.Series() (capital S)
print(pd.Series([10, 25, 38, 46, 56, 73, 0]))
print(pd.Series([10, 25, 38, 46, 56, 73, 0], index=[
    "Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]))
print(pd.Series([10, 25, 38, 46, 56, 73, 0], index=[
    "Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"
    ], name="Sales", dtype=str))

# Using numpy array
sales = np.array([10, 25, 38, 46, 56, 73, 0])
print(sales)
print(pd.Series(sales))

# Using List, Tuple and Dictionary
numbers_list = [10, 25, 38, 46, 56, 73, 0]
numbers_tuple = (10, 25, 38, 46, 56, 73, 0)
print(pd.Series(numbers_list))
print(pd.Series(numbers_tuple))

dic = {"Mon": 10, "Tues": 20, "Wed": 30, "Thurs": 40, "Fri": 50}
print(dic)
print(pd.Series(dic))

# explicitly passing indexes for a dictionary - these indexes are
# given preference over dictionary keys

# On passing mixed indexes the order is diplayed as per the index keys and
# not dictionary keys, in case keys doesn't exist in dictionary then NaN value
# is populated and if dict key is not present in index key then that value
# is not displayed e.g: Thurs goes missing here
print(pd.Series(dic, index=["Fri", "Sat", "Sun", "Tues", "Wed", "Mon"]))
# On passing completely different index keys returns NaN values for all indexes
print(pd.Series(dic, index=[1, 2, 3, 4, 5, 6]))
