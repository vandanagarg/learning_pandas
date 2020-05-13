''' Changing Datatypes - 3rd Step
using astype()/pd.to_numeric '''
import pandas as pd  # noqa: F401
from string_operations import titanic, summer


print("\n part3:")

# conversion from float/object to numeric datatypes
print(pd.to_numeric(titanic.Fare))
titanic.Fare = titanic.Fare.astype("float")
titanic["Survived"] = titanic.Survived.astype("int")
# titanic["Age"] = titanic.Age.astype("float")
# This gives error while conversion since it has missing data,
# and before conversion we must first handle missing data
titanic.info()
print(titanic.head())

# This datafame looks good as required, thus no need to alter any datatype
print(summer.head())
summer.info()
