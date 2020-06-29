''' Creating Dummy Variables '''
import pandas as pd
from caps_floors import titanic


mapper = {1: "First", 2: "Second", 3: "Third"}
titanic.pclass = titanic.pclass.map(mapper)
titanic["no_relative"] = titanic.sibsp.add(titanic.parch)

titanic.drop(labels=["age", "sibsp", "parch", "deck", "fare_cat"
                     ], axis=1, inplace=True)
print(titanic.head())

''' Here we have some categorical and non numerical columns eg: pclass,
sex, age_cat, embarked. Most of the ML algos can only handle numerical
columns, hence we use pandas method get_dummies to form dummy variables of
those columns which gives the numerical representation of categorical columns
and it splits original column into different dummy numerical columns
with their respective values(yes 1 no 0) also called one hot encoding.
So for each column we get one 1 and rest 0 just one hot category
What it means is that we clearly know if we have 1/0 in one column we got
alternate value for other and hence we can drop other redundant column which
is very popularly known in ML as (k-1)transformation where we have k categories
& we transform into (k-1) new features/columns in ML and this can be done using
parameter drop_first in pd.get_dummies() method '''
print(pd.get_dummies(titanic, columns=["sex"]))
print(pd.get_dummies(titanic, columns=["sex", "pclass"]))

# hot encoding, drops first category
titanic_d = pd.get_dummies(titanic, columns=["sex", "pclass",
                           "embarked", "age_cat"], drop_first=True)
# we can even rename column names using prefix and prefix_sep

print(titanic_d.head())
# new columns are now integers instead of categorical columns
titanic_d.info()
