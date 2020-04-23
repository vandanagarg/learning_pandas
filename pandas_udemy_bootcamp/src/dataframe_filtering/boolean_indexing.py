""" A useful technique in pandas is called boolean indexing. It is essentially
a filtering technique to find values based on a boolean condition (i.e., True
or False). The general syntax for a boolean index is as below.
dataframe[dataframe['column_name'] == 'filter_objective']
"""
import pandas as pd


# creating a dataframe with all the grades and subjects
grades = pd.DataFrame(
        {'Math': [80, 89, 93, 66, 84, 85, 74, 64],
         'Science': [94, 76, 88, 78, 88, 92, 60, 85],
         'English': [83, 76, 93, 96, 77, 85, 92, 60],
         'History': [96, 66, 76, 85, 78, 88, 69, 99]})
# print(grades)

# boolean subseting
print(grades[grades['Math'] > 80])
# subsetting but only calling a column
print(grades[grades['Math'] > 80]['Science'])
# subsetting but only calling a column using iloc
print(grades[grades['Math'] > 80].iloc[:, 3])
print(grades[grades['Math'] > 80].iloc[2:, 3])
# AND  conditions
print(grades[(grades['Math'] > 80) & (grades['Science'] < 80)])
# OR conditions but only want History score
print(grades[(grades['Math'] > 80) | (grades['Science'] < 80)][
    ['Math', 'Science', 'History']])
print(grades[(grades['Math'] > 80) | (grades['Science'] < 80)]['History'])
