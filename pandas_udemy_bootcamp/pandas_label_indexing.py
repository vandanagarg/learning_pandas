""" Label based indexing and Slicing with loc[] """
import pandas as pd

PATH = "/Users/peeyushsingla/projects/learning_pandas/pandas_udemy_bootcamp/Course_Materials_Part1/Video_Lecture_NBs/"  # noqa: E501
file = PATH + "summer.csv"
summer_df = pd.read_csv(file, index_col="Athlete")
# print(summer_df)

print(summer_df.loc["DRIVAS, Dimitrios"])

print(summer_df.loc["PHELPS, Michael"])  # all rows with label
print(summer_df.loc["PHELPS, Michael", "Medal"])  # all rows and column Medal
print(summer_df.loc["PHELPS, Michael", ["Medal", "Event"]])  # many rows/column
print(summer_df.loc[["PHELPS, Michael", "LEWIS, Carl"], ["Medal", "Event"]])
print(summer_df.loc[:, ["Medal", "Event"]])

# slicing
print(summer_df.loc[:"CHASAPIS, Spiridon"])  # with unique labeled index
print(summer_df.loc[:"PHELPS, Michael"])  # with non-unique labeled index
# gives error :
# KeyError: "Cannot get right slice bound for non-unique label: 'PHELPS, Michael'"  # noqa: E501
