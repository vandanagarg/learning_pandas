''' Caps and Floors
How to handle outliers by using caps and floors so that
it doesn't negatively influence the resuts in case of
actual extreme values we can do so by creating bins '''
from discretization_binning import titanic
import matplotlib.pyplot as plt


titanic.fare.plot(figsize=(12, 8))
plt.show()
# here although 512 is an extreme value but
# still be considered likewise in last group
print(titanic.fare.describe())
print(titanic.fare.sort_values(ascending=False))

''' Now we know the passangers who paid 512 are extremely rich
ones but the value 512 doesn't mean much to us for visualization,
like wise for the lower fares who paid nothing doesn't mean much.
So what we can do is put a fare cap and floor cap in order to
represent much visual data and to avoid extreme scenarios, we put
a cap for all prices above 250 to be changed as 250 and all prices
below 5 to be changed as 5 '''
fare_cap = 250
titanic.loc[titanic.fare > fare_cap, "fare"] = fare_cap

fare_floor = 5
titanic.loc[titanic.fare < fare_floor, "fare"] = fare_floor

print(titanic.head())
titanic.fare.plot(figsize=(12, 8))
plt.show()  # much symmetrical visualization
print(titanic.fare.describe())  # less std, no outliers
