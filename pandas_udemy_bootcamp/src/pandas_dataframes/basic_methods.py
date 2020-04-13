import pandas as pd
# creating a dataframe with all the grades and subjects

grades = pd.DataFrame(
        {'Math': [80, 89, 93, 66, 84, 85, 74, 64],
         'Science': [94, 76, 88, 78, 88, 92, 60, 85],
         'English': [83, 76, 93, 96, 77, 85, 92, 60],
         'History': [96, 66, 76, 85, 78, 88, 69, 99]})
# print(grades)

""" Quantiles - Using the .describe() function we automatically got quantiles
for 25, 50, and 75. We can also state our own quantiles. Below I have selected
10%, 40%, 70% etc. Note — we can pass in as many quantiles in the formula below
"""
# quantitles
print(grades.quantile([0.1, 0.4, 0.7, 0.8, 0.9]))

"""
Concat
Using concat, we can merge two data frames together based on an axis.
For example, we can add new values to our dataframe in two scenarios.
Add more rows — axis = 0
Add more columns — axis = 1
"""
grades2 = pd.DataFrame(
            {'Math': [77, 55, 93, 76],
             'Science': [88, 60, 90, 74],
             'English': [84, 76, 66, 90],
             'History': [77, 69, 92, 81],
             'Geography': [75, 60, 29, 18]})
# attach dataframes together, reset index and drop the index col
print(pd.concat([grades, grades2], axis=0).reset_index(drop=True))
print(pd.concat([grades, grades2], axis=1).reset_index(drop=True))

"""
Adding Columns - Adding more columns to a dataframe is as simple as
creating a new column name and setting the values equal to it.
"""
# new columns
grades['Student'] = [
    'Tom', 'Jane', 'Mike', 'Jason', 'Kim', 'Stephanie', 'Mary', 'Jack']
grades['Gender'] = ['M', 'F', 'M', 'M', 'F', 'F', 'F', 'M']
grades['Class'] = ['A', 'A', 'C', 'B', 'C', 'A', 'B', 'C']
print(grades)

# reorder columns - pass a list as a list and index
# order we want
cols = ['Student', 'Class', 'Gender', 'Math',
        'Science', 'English', 'History']
# overwrite the old dataframe with the same dataframe but new column order
grades = grades[cols]
print(grades)

"""
Pivot Table - A table of statistics that summarizes the data of a more
extensive table (such as from a database, spreadsheet, or business intelligence
program). This summary might include sums, averages, or other statistics, which
the pivot table groups together in a meaningful way.
"""
print(grades.pivot_table(index=['Class', 'Gender']))

"""
Group By
A groupby operation involves some combination of splitting the object, applying
a function, and combining the results. This can be used to group large amounts
of data and compute operations on these groups. The great thing about groupby
function in pandas is chaining on several aggregate functions using agg method
"""
print(grades.groupby(by='Gender').mean())
# groupby and adding several funcitons with agg
print(grades.groupby(by='Class').agg(['sum', 'mean']).round(2))
