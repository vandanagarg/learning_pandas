''' Changing Datatypes - 3rd Step
using astype()/pd.to_numeric '''
import pandas as pd  # noqa: F401
from string_operations import titanic, summer


if __name__ == "__main__":
    # print(pd.to_numeric(titanic.Fare))
    # print(titanic, summer)
    # print(summer.loc[summer.Athlete_Name == "Phelps, Michael"])
    titanic.Fare = pd.to_numeric(titanic.Fare)
    print(titanic)

titanic = titanic
# print(titanic.Fare)
