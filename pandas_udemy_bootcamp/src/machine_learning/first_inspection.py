''' California house value dataset, containing data for more than 20k
districts and that's the data we are going to build our machine learning
models to predicts values for districts where we don't have any
information on house values.
'''
import matplotlib.pyplot as plt
from create_dataframe import housing_df


housing_df.info()
# we mostly have no missing values other than column total_bedrooms
# and the data types are as expected float for all numerical columns
# and object for text/string column.

# to check for missing values
print(housing_df[housing_df.total_bedrooms.isna()])

# to check for duplicate values
print(housing_df[housing_df.duplicated()])  # no duplicates

# summary statistics on numerical columns
print(housing_df.describe())

# summary statistics/information on text column
print(housing_df.describe(include="O"))
# o/p means 5 districts are on island.. so on

# check unique values for numerical column
print(housing_df.ocean_proximity.value_counts())
# o/p means 18 districts have 1527 houses..so on

# for numerical columns value_counts() method is not really useful
# we will need a histogram to visualize total_rooms
print(housing_df.total_rooms.value_counts())

housing_df.hist(bins=50, figsize=(20, 15))
plt.show()
# so the graph shows there are some outliers in the numerical columns
# that might need to be cleaned up before we actually predict anything
