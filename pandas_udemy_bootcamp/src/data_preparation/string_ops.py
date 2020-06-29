''' String Operations
creating new string features/columns using string operations
we can use regular expressions for more complex string operations '''
from create_dataframes import summer


# splitting the athlete name into 2 new columns
summer.Athlete = summer.Athlete.str.title()
print(summer.head())
print(summer.Athlete.str.split(", ", n=1, expand=True))

summer[["Surname", "First_Name"]] = summer.Athlete.str. \
                                        split(", ", n=1, expand=True)
print(summer.head())

summer["Surname"] = summer.Surname.str.strip()
summer["First_Name"] = summer.First_Name.str.strip()
print(summer.drop(columns="Athlete"))
