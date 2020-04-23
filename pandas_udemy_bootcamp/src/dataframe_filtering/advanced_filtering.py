""" Advanced filtering with between(), isin(), ~, any(), all() """
import pandas as pd
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


summer_df = dfu.get_dataframe("summer.csv")
titanic_df = dfu.get_dataframe("titanic.csv")

print("\n Olympic Games 1988: ")
og_1988 = summer_df.loc[summer_df.Year == 1988]
print(og_1988.head())
print(og_1988.tail())
og_1988.info()

print("\n Olympic Games since 1992: ")
og_since1992 = summer_df.loc[summer_df.Year >= 1992]
print(og_since1992.head())
print(og_since1992.tail())
og_since1992.info()

# between()
print("\n Olympic Games 1960's: ")
print(summer_df.Year.between(1960, 1969).head())  # returns boolean series
og_60s = summer_df.loc[summer_df.Year.between(1960, 1968, inclusive=True)]
# default value inclusive=True includes both boundaries
print(og_60s.head())
print(og_60s.tail())
og_60s.info()

# isin()
print("\n Olympic Games 1972 and 1996: ")
duration = [1972, 1996]
print(summer_df.Year.isin(duration).head())  # returns boolean series
og = summer_df.loc[summer_df.Year.isin(duration)]
print(og.head())
print(og.tail())
print(og.Year.value_counts())
og.info()

# ~ (not in)
print("\n Olympic Games not in 1972 and 1996: ")
print(~summer_df.Year.isin(duration).head())  # returns boolean series
og_remaining = summer_df.loc[~summer_df.Year.isin(duration)]
print(og_remaining.head())
print(og_remaining.tail())
print(og_remaining.Year.value_counts())
print(og_remaining.Year.unique())
og_remaining.info()

""" methods any() and all() are only applicable to boolean/numeric series """
# any()- for checking aleast parameter/ supports OR operation
""" checks if any of the values along the specified axis is true,
this will return True """
print("\n any() method examples: ")
print("to check atleast one passenger is male")
print(titanic_df.sex == "male")
print((titanic_df.sex == "male").any())
print((titanic_df.sex == "child").any())  # no child value for column sex
print((titanic_df.age == 80.0).any())
print((titanic_df.age == 800.0).any())  # no passenger of age 800.0

# all() - opposite of any(); acts like AND operator
""" checks if all the values along the specified axis is true,
this will return True """
print("\n all() method examples: ")
print("to check if all passengers are male")
print((titanic_df.sex == "male").all())
# check if the value of fare column is greater than 0 for all passengers
# or all passengers should have paid for their ticket fare, if any of them
# didn't pay for ticket the o/p will be False
print(titanic_df.fare.all())

# numerical series
"""
For all positive/negative non zero numbers boolean value is True
For only zero boolean value is False
"""
# if all are true, o/p is false as there is one zero
print(pd.Series([-1, 0.5, 1, -0.1, 0]).all())
# if any of the one is true, o/p is true all other than zero are non zero
# numbers and hence true
print(pd.Series([-1, 0.5, 1, -0.1, 0]).any())
# if all are true, o/p is true as there is no zero and all are non zero numbers
print(pd.Series([-1, 0.5, 1, -0.1]).all())
