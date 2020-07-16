''' Data Cleaning and Creating additional features '''
from create_dataframe import housing_df


# so as we just have missing values for only one column
# in this case instead of replacing those values with median or
# group specific mean values , we just decide to drop them in this case
housing_df.dropna(inplace=True)
''' So here we dropped only few rows and still have lot of valid observations.
For some columns like median_house_value the values are capped & we can either
worked with caped values or try to find uncapped values, here we are more
interested in lower values & we should now check that does higher capped values
influce our results or not? In this case with random forest regression higher
capped values doesn't make much difference and hence we need not remove them
Altough we have several features that measure the size of the district for eg:
total population, total number of households, total bedrooms/rooms, here
it will make more sense if we combine those features and make them relative
features let's say rooms per household and this is an indicator for house
size and higher the size larger is the value '''

# creating a new feature - new column - rooms per household
# dividing total rooms by number of households
housing_df["rooms_per_household"] = housing_df.total_rooms.div(
                                    housing_df.households)

print(housing_df.rooms_per_household.nlargest(10))
print(housing_df.rooms_per_household.nsmallest(10))
''' here again we have a few extreme values having 141 rooms per household
or having less than 1 room per house which doesn't make much sense,
hence let's futher observe the extreme values '''

print(housing_df.loc[[1979, 5916, 8219]])
# here these observations are not so accurate and doesn't make much sense
# but we can leave them as they won't interfare much with the results

# creating additional features
housing_df["pop_per_household"] = housing_df.population.div(
                                    housing_df.households)
housing_df["bedrooms_per_room"] = housing_df.total_bedrooms.div(
                                    housing_df.total_rooms)

print(housing_df.describe())
