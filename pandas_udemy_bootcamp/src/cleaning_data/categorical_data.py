''' Categorical Data
Here along with cleaning data we can transform the data type of certain
columns into a special datatype category
Advantages: 1. Saves memory
2. If we have a columns with Category datatype, some operations in pandas have
better performance on them e.g group by operation is faster on categorical
datatype columns '''
from removing_outliers import titanic, summer


# Titanic Dataset
titanic.info()

# titanic.to_csv("titanic_clean.csv", index = False)
''' Here for a few columns we have repeated data for example for
Gender column we just have 2 unique values male female and by default all
these values are stored as string and as separate values; by converting
the column into category datatype it stores the values in intergers let's
say for male as 0 and female as 1 and then save the data as 891 integers
instead of saving 891 strings, so here out of all columns only gender and
emb column is of datatype object and have 2 & 3 unique values which can be
converted into category datatype '''

print(titanic.nunique())
# slicing data for 2 columns
print(titanic[["Gender", "Emb"]].describe())
# changing datatype to category
titanic.Gender = titanic.Gender.astype("category")
titanic.Emb = titanic.Emb.astype("category")

titanic.info()
print(titanic.Gender.dtype)

# Olympic Dataset
summer.info()

# summer.to_csv("summer_clean.csv", index = False)

print(summer.describe(include=["O"]))
print(summer.nunique())

summer.City = summer.City.astype("category")
summer.Sport = summer.Sport.astype("category")
summer.Discipline = summer.Discipline.astype("category")
summer.Country = summer.Country.astype("category")
summer.Gender = summer.Gender.astype("category")
summer.Medal = summer.Medal.astype("category")

summer.info()
