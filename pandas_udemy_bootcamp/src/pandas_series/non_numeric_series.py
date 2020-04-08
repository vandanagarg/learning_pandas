""" Analyze non-numerical series with unique(), nunique() and value_count() """
import config_file  # noqa: F401
from utilities import DataframeUtilities as dfu
""" unique(), value_count() methods are only series methods """
""" nunique() method is supported by both dataframe and series """


summer_df = dfu.get_dataframe("summer.csv")
print(summer_df.head())
summer_df.info()
athlete = summer_df["Athlete"]

print(athlete.head())
print(athlete.tail())
print(type(athlete))
print(athlete.dtype)  # object
print(athlete.shape)  # (31165,)
print(athlete.describe())  # tells basic stats of this non-numeric column

print(athlete.size)  # 31165
print(athlete.count())  # 31165
# Indicates no missing values since size == count()

print(athlete.min())  # Gives the very first athlete alphabetically
print(athlete.max())  # Gives the last athlete alphabetically

print(athlete.unique())  # Gives the unique elements
print(len(athlete.unique()))  # Gives the number of unique elements
print(athlete.nunique())  # Gives unique elements(excluding NAN values)
print(athlete.nunique(dropna=True))  # default TRUE
print(athlete.nunique(dropna=False))  # same as no missing values

print(len(summer_df["Country"].unique()))  # includes missing values
print(summer_df["Country"].nunique())  # excludes missing values

print(athlete.value_counts())
print(athlete.value_counts(sort=True, ascending=True))
print(athlete.value_counts(sort=True, ascending=False, normalize=True).head())
