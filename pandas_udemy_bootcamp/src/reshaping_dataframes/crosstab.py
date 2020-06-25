''' pd.crosstab() - general pandas method
for reshaping and aggregating data '''
import pandas as pd
from create_dataframes import titanic, summer


titanic.info()
''' Here in titanic dataframe we have 2 categorical columns
sex and pclass which have 2 & 3 values respectively and in
combination they will form 6 unique groups and if we want
to find out size of each group we can do using crosstab()
method - evaluates frequency table of the factors '''
# find frequency of respective groups for column sex & pclass
print(pd.crosstab(titanic.sex, titanic.pclass))

# using group by method for the same aggregated data
print(titanic.groupby(["sex", "pclass"]).pclass.count())
# pivot inner index pclass with unstack method
print(titanic.groupby(["sex", "pclass"]).pclass.count().unstack())

# extra parameters: margins, normalize
# to populate total values for the row/columns
print(pd.crosstab(titanic.sex, titanic.pclass, margins=True))
# for relative frequencies
print(pd.crosstab(titanic.sex, titanic.pclass, margins=True,
                  normalize=True))

''' One main difference is we can pass 2 different columns
of different dataframes in crosstab method and in groupby the
2 columns have to be from same dataframe thus limited options '''

# aggregate and pivot data with crosstab function
''' we want to calculate avg/mean age for each combination of
sex and pclass groups '''
print(pd.crosstab(index=titanic.sex, columns=titanic.pclass,
                  values=titanic.age, aggfunc="mean"))

# this is same as pivot_table() method but here we can use
# columns from different dataframes as well but in pivot_table
# method we are limited to single dataframe
print(titanic.pivot_table(index="sex", columns="pclass",
                          values="age", aggfunc="mean"))

# same results using groupby()
print(titanic.groupby(["sex", "pclass"]).age.mean().unstack())

# calculating total fare paid per group
print(pd.crosstab(index=titanic.sex, columns=titanic.pclass,
                  values=titanic.fare, aggfunc="sum"))
print(pd.crosstab(index=titanic.sex, columns=titanic.pclass,
                  values=titanic.fare, aggfunc="sum",
                  margins=True, normalize=True))

# calculations with summer dataset
summer.info()

# finding the total number of medals per year for each country
# we need to pass index as a multiindex in order to group on year & country
print(pd.crosstab(index=[summer.Year, summer.Country], columns=summer.Medal,
                  values=summer.Athlete, aggfunc="count",
                  margins=True).fillna(0))

# same can be done using pivot_table, group_by method
print(summer.pivot_table(index=["Year", "Country"], columns="Medal",
                         values="Athlete", aggfunc="count", margins=True,
                         fill_value=0))

print(summer.groupby(["Year", "Country", "Medal"]).Medal.count(
        ).unstack(fill_value=0))
