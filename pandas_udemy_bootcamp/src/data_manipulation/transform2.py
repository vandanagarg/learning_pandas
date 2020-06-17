''' Usecase of method transform() on groupby object:
Replacing NA values by group specific values
'''
import config_file  # noqa: F401
from utilities import DataframeUtilitiesProject as dfu


# Titanic Dataset
titanic = dfu.get_dataframe("titanic.csv")

# replacing missing values in age column
# earlier approach find mean and replace missing values with mean
mean_age = titanic.age.mean()
print(mean_age)
print(titanic.fillna(mean_age))

# to be more specific if we replace the missing values with group specific
# mean values; it will be more meaningful
print(titanic.groupby(["sex", "pclass"]).age.mean())

# a new column with group specific mean age values
titanic["group_mean_age"] = titanic.groupby(["sex", "pclass"]
                                            ).age.transform("mean")
print(titanic.head(20))

# now for more accurate results in fillna method we pass this new
# group_mean_age column as pandas series to replace missing values
titanic.age.fillna(titanic.group_mean_age, inplace=True)
print(titanic.head(10))
titanic.info()
