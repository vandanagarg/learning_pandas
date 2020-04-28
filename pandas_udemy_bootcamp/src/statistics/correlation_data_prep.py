''' Correlation & Regression
 Getting and Preparing the Data '''
import pandas as pd
from create_dataframe import movie_df, TARGET_PATH


# print(movie_df)
movie_df.info()

# in order to set release_date column as index we must change the datatype from
# object to datetime
print(pd.to_datetime(movie_df.release_date, errors="coerce"))
# ValueError: Given date string not likely a datetime.
# by default error is raise, if we set it to coerce it passes NaT:
# not a time to improper values

movie_df = movie_df.set_index(pd.to_datetime(
    movie_df.release_date, errors="coerce")).drop(columns=["release_date"])

movie_df.sort_index(inplace=True)
print(movie_df)

df = movie_df.loc[:, ["title", "budget", "revenue"]].copy()
print(df)

df.info()

df.budget = pd.to_numeric(df.budget, errors="coerce")
print(df.tail(50))
# ValueError: Unable to parse string "/ff9qCepilowshEtG2GYWwzt2bs4.jpg"
# by default error is raise, if we set it to coerce it passes NaN:
# to improper values
df.info()

print(df.describe())

df.iloc[:, -2:] = df.iloc[:, -2:] / 1000000
print(df)
print(df.describe())

# removing the movies which have no title
print(df.loc[df.title.isna()])
df.dropna(inplace=True)
df.info()

# It can't be possible for a movie to have budget/revenue to be zero,
# so it might be the missing values and we can filter our data to have only
# those movies which have non zero budget/revenue values
print(df.budget.value_counts())
print(df.revenue.value_counts())

df = df.loc[(df.revenue > 0) & (df.budget > 0)]
print(df)

df.info()
print(df.describe())

print(df.sort_values("budget", ascending=False))
print(df.sort_values("revenue", ascending=False))

df.to_csv(TARGET_PATH + "bud_vs_rev.csv")
