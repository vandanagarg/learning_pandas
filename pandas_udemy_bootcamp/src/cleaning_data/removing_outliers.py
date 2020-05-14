''' Handling / Removing Outliers
To handle incorrect/outliers/NA values we must either
1. delete that data - in this case we even loose other important
information in other columns
2. We either replace that existing values with mean/median/average values
3. leave them as it is- this can work with missing values as pandas can
drop/handle missing values but leaving outliers will temper the results
which can lead to errors in future '''
from outliers import titanic, summer  # noqa: F401
import matplotlib.pyplot as plt


# let's evaluate outliers data in Age column in titanic dataset

print(titanic.loc[titanic.Age > 90])

index_outl = titanic.loc[titanic.Age > 90].index
print(index_outl)

''' let's assume now we realized this was a manual error and we need to shift
decimal point to correct the age and also for 217 index person the correct
age is 42yrs so we need to now correct the values and after updating the plot
seems to have reasonable range below 80yrs of age '''
titanic.loc[titanic.Age > 90, "Age"] = titanic.loc[titanic.Age > 90, "Age"]/10
print(titanic.loc[index_outl])

titanic.loc[217, "Age"] = 42.0
print(titanic.loc[index_outl])

plt.figure(figsize=(12, 6))
titanic.Age.plot()
plt.show()

titanic.info()
