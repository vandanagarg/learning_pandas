''' Discretization and Binning with pd.cut()
Here we convert the continuous value columns into discrete
values or categorical columns. We generally create the bins
& divide continuous values to fit in those bins & new series
of bins will be categorical in nature instead of continuous '''
import pandas as pd
from create_dataframes import titanic


titanic.age.fillna(titanic.age.mean(), inplace=True)
age_bins = [0, 10, 18, 30, 55, 100]
# age_bins here we define the edges or the bins for our column
# using cut() method, right=False means right boundary excluding
cats = pd.cut(titanic.age, age_bins, right=False)
print(cats)  # ordered categorical pandas series(low to high)
print(cats.value_counts())

# assigning pandas series to a new column
titanic["age_cat"] = cats
print(titanic.head())

# performing further analysis on the bins to check survival rate
print(titanic.groupby("age_cat").survived.mean())
''' So now here since we don't get a linear relationship between
age and survival of the passanger, it makes more sense to convert
it into bins in this case as mostly linear relationships are good
to visualize, else we should change them into categories or bins.
We should also consider changing the interval representation to
be more redable as strings hence we can give proper labels to bins '''

group_names = ["child", "teenager", "young_adult", "adult", "elderly"]
# pandas series with new labels, ordered categories
print(pd.cut(titanic.age, age_bins, right=False, labels=group_names))

titanic["age_cat"] = pd.cut(titanic.age, age_bins, right=False,
                            labels=group_names)

print(titanic.head(10))

''' Very important step for making bins is to decide on intervals
or edges where we would like to divide the values. initially we
manually decided the edges and passed as a list here since there
is no such unique factor to divide the fare column if we want to
divide it in 5 equal widths we can just pass an int and it will
create bins of its own '''

print(pd.cut(titanic.fare, 5, precision=3))  # default

titanic["fare_cat"] = pd.cut(titanic.fare, 5, precision=0)
print(titanic.head(10))
print(titanic.fare_cat.value_counts())
# equal width bins

''' Discretization and Binning with pd.qcut()
Quantile based distribution(20% passangers in each bin)
using pd.cut() for fare column wasn't so useful as there
is no equal distribution of passangers amongst those bins
first bin had the max values whereas 1 bin has no value at
all. so let's see how we can use pd.qcut() to optimize our
distribution '''

print(pd.qcut(titanic.fare, 5))
# equal distribution with 20% passangers in each bin

titanic["fare_cat"] = pd.qcut(titanic.fare, 5)
print(titanic.head())
print(titanic.fare_cat.value_counts())
# almost (20%) equal distribution but unequal widths

# we define here user defined quantiles for qcut() method
print(pd.qcut(titanic.fare, [0, 0.1, 0.25, 0.5, 0.9, 1], precision=0))
# 0, 0.1 first 10%; 0.1 , 0.25 is next 15%, 0.25, 0.5 is next 25% so on..
# first and last 10% super cheap/expensive..so on

fare_labels = ["very_cheap", "cheap", "moderate", "exp", "very_exp"]

titanic["fare_cat"] = pd.qcut(
                        titanic.fare, [0, 0.1, 0.25, 0.5, 0.9, 1],
                        precision=0, labels=fare_labels
                        )

print(titanic.head())
print(titanic.fare_cat.value_counts())

print(titanic.groupby(["age_cat", "fare_cat"]).survived.mean().unstack())
''' Here we can see somewhat linear relationship for survival
between the passanger age and the fare as we move towards the right '''
