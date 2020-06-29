''' Scaling / Standardization
scaling and standardizing numerical columns using z scores
many a time we have some columns which are in different units and it
become difficult to scale them. Scikit learn has some sacling methods
to handle this but it can be done using simple arithmetics as below '''
import matplotlib.pyplot as plt
from create_dataframes import titanic


titanic.age.fillna(titanic.age.mean(), inplace=True)
print(titanic.describe())
''' Here altough the mean of age and fare column is quite close but
it has a varying std and thus not on the same scale. It differs a lot.
But these 2 columns can be brought on same scale using z scores '''
# line plots for age and fare columns; different scales
titanic.fare.plot(figsize=(12, 8))
titanic.age.plot(figsize=(12, 8))
plt.show()

# calculating z scores
mean_age = titanic.age.mean()
mean_fare = titanic.fare.mean()

std_age = titanic.age.std()
std_fare = titanic.fare.std()

# z score is no of std that the respective observation is away from the mean
titanic["age_z"] = round((titanic.age-mean_age) / std_age, 2)
titanic["fare_z"] = round((titanic.fare-mean_fare) / std_fare, 2)

print(titanic.head(10))
''' z score 0 means it is 0 distance away from the mean. Using z score
normalize the data such that it get 0 mean and 1 std for all the variables '''
print(round(titanic.describe(), 2))

# line plots for z scores, almost same scale 0 mean and 1 std
titanic.fare_z.plot(figsize=(12, 8))
titanic.age_z.plot(figsize=(12, 8))
plt.show()
