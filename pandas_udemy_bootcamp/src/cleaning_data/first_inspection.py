''' Cleaning Data
First Inspection/Handling Inconsistent Data '''
from create_dataframes import titanic, summer


# Titanic Dataset
print(titanic)
print(titanic.head())
print(titanic.tail())

# get idea on dataframe column datatypes, if we need to convert any of them
titanic.info()
# get an idea on dataframe numerical columns, if there are anomalies
print(titanic.describe())

# get an idea on dataframe non-numerical columns, unique values etc.
print(titanic[["Survived", "Gender", "Age", "Fare", "Emb", "Deck"]
              ].describe())
print(titanic.describe(include="O"))
print(titanic.Survived.unique())  # 4 values, expected 2:(0,1)
print(titanic.Survived.value_counts())  # shows inconsistent data

# remove inconsistency for Survived column
titanic.Survived.replace(
    to_replace=["yes", "no"], value=[1, 0], inplace=True)
print(titanic.Survived.unique())  # 4 values, expected 2 int values:(0,1)
print(titanic.Survived.value_counts())  # still inconsistent datatypes
# we still have value 1, 0 present as string hence shows different values

# Olympic Dataset
print(summer)
print(summer.head())
print(summer.tail())

# get idea on dataframe column datatypes, if we need to convert any of them
summer.info()
# we have problem with 1 column name space, hence should be replaced
summer.rename(columns={"Athlete Name": "Athlete_Name"}, inplace=True)
print(summer.Athlete_Name.head())

# data inconsistency for a column
print(summer.Medal.value_counts())
# replace with correct values
summer.Medal.replace(to_replace=["Gold Medal"], value=["Gold"],
                     inplace=True)
print(summer.Medal.value_counts())

# get an idea on dataframe non numerical columns, if there are anomalies
print(summer.iloc[:, 1:].describe())  # gives an overview
