""" Analyze single columns of a DataFrame (Pandas Series) """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu  # Type 1, 2
# from utilities.dataframe_utilities import DataframeUtilities as dfu  # Type 3

titanic_df = dfu.get_dataframe("titanic.csv")  # Type 1, 2, 3
age = titanic_df["age"]
# print(titanic_df)

# summer = dfu.get_indexed_dataframe("summer.csv", "Athlete")
# print(summer)

# Same methods as in dataframe datatype
print(age.head(2))
print(age.tail(2))
print(age.dtype)  # To check datatype
print(age.shape)  # To check rows * columns
print(len(age))
print(age.index)
# age.info()  # This method doesn't exist for series
print(age.to_frame())  # To convert a series into dataframe
# After converting into dataframe, now we can run info method on the same
age.to_frame().info()
