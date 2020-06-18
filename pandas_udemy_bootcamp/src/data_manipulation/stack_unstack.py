''' stack() and unstack() methods to reorganize dataframes '''
import matplotlib.pyplot as plt
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Summer Dataset
summer = dfu.get_dataframe("summer.csv")

medals_by_country = summer.groupby(["Country", "Medal"]).Medal.count()
print(medals_by_country)  # o/p as pandas series
# Here we have multi-indexes with outer index as Country & inner index as medal

# slicing pandas series
print(medals_by_country.loc["USA"])  # outer index
print(medals_by_country.loc[("USA", "Gold")])  # outer & inner index
print(medals_by_country.shape)  # 350 rows and 1 column

# Applying unstack method on pandas series
print(medals_by_country.unstack())
''' So here we organize/split inner index as columns and we get a new dataframe
where we have index country and 3 columns bronze, gold, silver where Medal is
column label, altough we get too many missing values which can be handled '''

# by default unstacks the inner index or index at -1 level or right most
print(medals_by_country.unstack(level=-1))
print(medals_by_country.unstack(level=-2))
''' Now we have a different dataframe by splitting outer indexes into columns,
now we have Medal index as row index and country index as columns, still there
are a lot of missing values '''

# replacing missing values
medals_by_country = medals_by_country.unstack(level=-1, fill_value=0)
print(medals_by_country)
print(medals_by_country.shape)
''' hence the shape changes from long format(more rows) to wide format
(more columns). The wide format is good w.r.t. to presentation and the
ease of readability; rather than using long format which appears to be
less readable '''

# rearranging columns
medals_by_country = medals_by_country[["Gold", "Silver", "Bronze"]]
print(medals_by_country)
medals_by_country.sort_values(by=["Gold", "Silver", "Bronze"],
                              ascending=[False, False, False],
                              inplace=True)
print(medals_by_country)

# plotting a bar graph for top 10 countries
plt.style.use("seaborn")

medals_by_country.head(10).plot(kind="bar", figsize=(12, 8), fontsize=13)
plt.xlabel("Country", fontsize=13)
plt.ylabel("Medals", fontsize=13)
plt.title("Medals per Country", fontsize=16)
plt.legend(fontsize=15)
plt.show()

''' STACK() method is reverse of unstack method '''
print(medals_by_country.stack())  # pandas series, long format
# it just recreates our inner index Medal or multi indexes(Country, Medal)

# method chaining
print(medals_by_country.stack().unstack())  # wide format
