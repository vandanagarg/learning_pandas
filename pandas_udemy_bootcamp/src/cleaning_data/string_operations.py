''' String Operations - 2nd Step
In case of string data we will often have inconsistencies in data '''
import pandas as pd  # noqa: F401
from first_inspection import titanic, summer


def string_operation(titanic, summer):
    # Titanic Dataset, Fare column: expectation Numeric datatype
    # pd.to_numeric(titanic.Fare)  # gives error
    # ValueError: Unable to parse string "$7.25" at position 0
    titanic.Fare = titanic.Fare.str.replace("$", "")
    print(titanic.Fare.head())

    # Olympic Dataset
    # We expect names to have title case, not mixed formats
    summer.info()
    summer.Athlete_Name = summer.Athlete_Name.str.title()
    print(summer.Athlete_Name)

    # try to fetch records for name = Hajos, Alfred
    print(summer.loc[summer.Athlete_Name == "Hajos, Alfred"])  # no records
    # either use method contains for strings, spaces doesn't cause problem
    print(summer.loc[summer.Athlete_Name.str.contains("Hajos, Alfred")])
    # but we have records for Hajos, Alfred, try selecting particular element
    print(summer.iloc[0, 4])  # seems like spaces in the name

    # trim the spaces
    summer.Athlete_Name = summer.Athlete_Name.str.strip()
    print(summer.loc[summer.Athlete_Name == "Hajos, Alfred"])  # 2 rows
    print(summer.loc[summer.Athlete_Name == "Phelps, Michael"])
    return titanic, summer


# string_operation(titanic, summer)

titanic, summer = string_operation(titanic, summer)
# Titanic Dataset
# print(titanic)
# Olympic Dataset
# print(summer)
