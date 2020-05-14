''' Detection of Duplicates '''
import pandas as pd
from missing_values_part3 import titanic, summer


''' Here in our dataframes, duplicates can refer to entries of a particular
passanger twice or more, which might not be needed to be entered again.
Even sometimes we can have such data where we might need duplicate entries
so it will be always case dependent '''

alphabet = pd.DataFrame(["a", "b", "c", "c", "d", "e", "f", "g", "g", "g"],
                        columns=["Alphabet"])
print(alphabet)

# checks for all rows for duplicate values/entries
# keep=False marks all occurrences as True, can be changed as well
print(alphabet.duplicated(keep=False))  # boolean series
print(alphabet[alphabet.duplicated(keep=False)])  # duplicate entries

# Titanic Dataset
# check for duplicate entries for a passanger, keep=first, 1st entry will
# not be considered duplicate and rest all entries will be marked duplicate
print(titanic.duplicated(keep="first"))
print(titanic.duplicated(keep="first").sum())
print(titanic[titanic.duplicated(keep=False)])  # to check values

''' here it turns out to be 114 potential duplicates, but it is not true, since
our dataframe is missing key identifier, there is nothing unique to identify or
differentiate 2 passengers (no name, no unique id etc), also we have replaced
a lot of age column data with mean age value. Here by default we are using all
columns to check for duplicates. It here checks if 2 rows are completely
identical same values in all fields, thus right now in our case we can't
confirm if it is really duplicate data since we don't have a key identifier
to confirm on that thus parameter subset is not of much use here '''

print(titanic.duplicated(keep="first", subset=["Survived", "Class"]).sum())
# gives only 6 unique combinations for columns Survived and Class

# Olympic Dataset
summer.info()
print(summer.duplicated(keep="first").sum())  # 7 potential duplicates
# here in this case all values for duplicate rows/each column are exactly same,
# hence in this case these 7 rows are surely duplicate
print(summer[summer.duplicated(keep=False)])

''' Here in this sample dataset if we consider medals as per each player than
the medals are not duplicate, but if we consider w.r.t. the Country these
medals are duplicate '''
print(summer.loc[(summer.Sport == "Basketball") & (summer.Year == 2012)])
print(summer.loc[(summer.Sport == "Basketball") & (summer.Year == 2012)
                 ].duplicated(keep="first").sum())  # 0 - no duplication
print(summer.loc[(summer.Sport == "Basketball") & (summer.Year == 2012)
                 ].duplicated(keep="first", subset=["Country"]).sum())
# 67 duplicates
print(summer.loc[(summer.Sport == "Basketball") & (summer.Year == 2012)
                 ]["Country"].value_counts())
