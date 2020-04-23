""" Filtering Dataframes with one Condition """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu


titanic_df = dfu.get_dataframe("titanic.csv")
print(titanic_df.sex.head(10))
print(titanic_df.sex == "male")
# o/p is a pandas series with boolean values

# Now create a new dataframe by passing the above boolean series in a dataframe
print(titanic_df[titanic_df.sex == "male"])
# or we can use dot notation as well; also we can filter both rows/columns
print(titanic_df[titanic_df.sex == "male"]["fare"])  # chained indexing
print(titanic_df.loc[titanic_df.sex == "male", "fare"])  # preferred way to do
# using .loc[] method is much preferred since we can filter rows/columns in
# single []bracket, else it uses chained indexing which is not preferred way

# creating a series and passing the variable for readability
male_series = (titanic_df.sex == "male")
# print(male_series)
titanic_male = titanic_df.loc[male_series]  # creating a new dataframe
print(titanic_male.head())

# Filtering Columns
print(titanic_df.dtypes)
print(titanic_df.dtypes == object)  # o/p boolean series
print("\n Readable form")
datatype_series = titanic_df.dtypes == object
print(datatype_series)  # o/p boolean series

# getting all rows and not object columns
print(titanic_df.loc[:, ~datatype_series])

print(titanic_df.loc[male_series, ~datatype_series])  # filter both row/column
# o/p is all male rows with only numerical columns
