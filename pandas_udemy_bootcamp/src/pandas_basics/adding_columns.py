""" adding new columns to a dataframe """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
# print(titanic_df.head())

# Using broadcasting method to create new column and assign default value to it
# We can only use []square_bracket notation for adding columns
# titanic_df["Zeros"]
""" We need to specify a default value, this command will
give error as it just checks if there is any column name with name zeros
KeyError: 'Zeros'  """
titanic_df["Zeros"] = 0
print(titanic_df.head())

# Using .dot method notation we can only check for existing column values but
# can't create a new column
titanic_df.Ones = 1  # does nothing
print(titanic_df.head())
print("\n Value of Dataframe Attribute 'Ones':")
print(titanic_df.Ones)
print("\n")
# This is hence an attribute of the dataframe but no new column is created

""" Creating columns based on other columns """

# in pandas we can do elementwise or vectorwise operations as numpy arrays
""" Let's say we need to create a new column to save the approx DOB year of
the passengers using age column and the fact that titanic drowned in 1912 """
print("\n Column Year of Birth")
print(1912 - titanic_df.age)
titanic_df["YOB"] = 1912 - titanic_df.age
print(titanic_df.head())

print("\n Column for total relatives")
print(titanic_df.sibsp + titanic_df.parch)
titanic_df["relatives"] = titanic_df.sibsp + titanic_df.parch
print(titanic_df.head())

# clean dataframe by dropping redundant columns
titanic_df.drop(columns=["sibsp", "parch", "Zeros"], inplace=True)
print(titanic_df.head())

print("\n Column fare updated with inflation factor and shows updated fares:")
inflation_factor = 10
print(titanic_df.fare * 10)
titanic_df.fare = titanic_df.fare * 10
# overriding the same column, instead of creating a new column
print(titanic_df.head())

""" adding columns with insert() - Helps insert column at a specific index """
titanic_df = dfu.get_dataframe("titanic.csv")
print("\n Adding new columns with method insert()")
# By default new column is added at last position/index
titanic_df["test_col"] = "test"
print(titanic_df.head())
relatives = titanic_df.sibsp + titanic_df.parch
print(type(relatives))  # <class 'pandas.core.series.Series'>
print(relatives.head())

titanic_df.insert(loc=6, column="relatives", value=relatives)
# assign desired index to the loc parameter
print(titanic_df.head(10))
