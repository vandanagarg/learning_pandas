import pandas as pd


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'

users = pd.read_csv(url, sep='|', index_col="user_id", header=0)
print(users.head(25))
print(users.tail(10))

print(users.shape[0])

print(users.shape[1])

print(users.columns)

print(users.index)

users.info()
print(users.dtypes)

print(users.occupation)

print(users.occupation.unique())
print(users.occupation.nunique())

print(users.occupation.value_counts().nlargest(1))
print(users.occupation.value_counts().index[0])

print(users.describe())
print(users.describe(include="O"))
print(users.describe(include="all"))

print(users.occupation.describe())

print(users.age.mean())

print(users.age.value_counts().sort_values().nsmallest(1))
print(users.age.value_counts())
print(users.age.value_counts().tail())
