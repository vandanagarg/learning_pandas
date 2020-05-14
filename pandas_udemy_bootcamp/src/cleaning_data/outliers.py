''' Detection of Outliers
There are 2 kind of outliers:
1. extreme values in our data, which are mostly incorrect and are due to
manual errors
2. which are extreme values but not incorrect, but w.r.t. other data points
these values vary a lot
So outliers always tend to negatively influence the outcomes and the results
become less reliable, hence it is very important to handle outliers. We can
mostly find outliers in our numerical data '''
from removing_duplicates import titanic, summer  # noqa: F401
import matplotlib.pyplot as plt


# using describe methods kind of gives an overview on min max values
print(titanic.describe())

# max value for age looks quite incorrect, let's see with box plot
plt.figure(figsize=(12, 6))
titanic.boxplot("Age")
plt.show()
# we see 3 outliers and box in the plot represents most frequent values

# line plot
plt.figure(figsize=(12, 6))
titanic.Age.plot()
plt.show()

# filter outliers data
print(titanic.Age.sort_values(ascending=False))
print(titanic.loc[titanic.Age > 90])

# validate Fare column
print(titanic.Fare.sort_values(ascending=False))

plt.figure(figsize=(12, 6))
titanic.Fare.plot()
plt.show()
''' here if there was just one passanger who paid too much for the
ticket then it could have been wrong, but their might be a chance that
these were premium seats/suits. Also these values are still not so
unrealistic in comparision to other fare prices. Hence we can't consider
them to be real outliers '''
