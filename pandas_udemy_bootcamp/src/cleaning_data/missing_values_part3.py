''' Replacing missing values with fillna() '''
from missing_values_part2 import titanic, summer  # noqa: F401


''' from previous cleaning of data we have a lot of missing values in age
column and now we can replace NA with other values, the big question is
what what to choose for replacing, generally for a numerical
column its best to replace with mean/ median values but it can always vary as
per the situation, we can even use grouped mean/average values and so on.. '''

print(titanic.Age.mean())

mean = round(titanic.Age.mean(), 1)
print(mean)

titanic.Age.fillna(mean, inplace=True)
print(titanic.head(7))
titanic.info()
