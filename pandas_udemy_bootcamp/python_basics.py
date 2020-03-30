"""First Data Inspection"""
import pandas as pd

PATH = "/Users/peeyushsingla/projects/learning_pandas/pandas_udemy_bootcamp/Course_Materials_Part1/Video_Lecture_NBs/"  # noqa: E501
file_name = PATH + "titanic.csv"
titanic_df = pd.read_csv(file_name)
# print(titanic_df)


# To change Maximum and minimum rows setting
print(pd.options.display.max_rows)
print(pd.options.display.min_rows)
pd.options.display.max_rows = 900
# Earlier version it was 60 and used to display first and last 30 rows of a df
# if the rows are more than 60.
pd.options.display.min_rows = 20  # Allowed in latest version
print(titanic_df)

print(titanic_df.head())  # By default it prints first 5 rows
print(titanic_df.head(10))  # Can be updated as well

print(titanic_df.tail())  # By default it prints last 5 rows
print(titanic_df.tail(2))  # Can be updated as well

titanic_df.info()  # Summarize data at a glance about rows and columns

# describe returns a summary statistics on numericals columns
print(titanic_df.describe())

# to chevk summary for non numericals columns
print(titanic_df.describe(include="O"))
