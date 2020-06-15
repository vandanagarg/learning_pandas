''' Joining dataframes on different Column Labels and Indexes '''
from create_dataframes import men2004, men2008


# Non indexed dataframes
''' In case we have different indexes/column name then if we pass parameter
on then it gives keyerror if the column is not present in both dataframes.
Else we can use parameters left_on and right_on to specify the column names
and then fill missing values appropriately with other indexes/column values '''
# lets change men2004 df column labels
men2004.columns = ["Name", "Medals"]
# print(men2004.merge(men2008, how="outer", on="Athlete",
#       suffixes=("_2004", "_2008")))  # gives error KeyError: 'Athlete'
men0408 = men2004.merge(men2008, how="outer", left_on="Name",
                        right_on="Athlete", suffixes=("_2004", "_2008"),
                        indicator=True)
print(men0408)

# fill in the missing values in Name column
men0408.Name.fillna(men0408.Athlete, inplace=True)
print(men0408)

# let's drop extra Athlete and _merge columns
men0408.drop(["Athlete", "_merge"], axis=1, inplace=True)
print(men0408)


# Indexed Dataframes
# setting up Athlete as index column for 2008 dataframe
men2008.set_index("Athlete", inplace=True)
print(men2008)

# if now we again try to join both
men48 = men2004.merge(men2008, how="outer", left_on="Name",
                      right_on="Athlete", suffixes=("_2004", "_2008"),
                      indicator=True)
print(men48)  # here in this case we loose our indexes for 2008 dataframe

# hence if we are using index labels we must use different parameters
# so as not to loose our indexes
men48_i = men2004.merge(men2008, how="outer", left_on="Name",
                        right_index=True, suffixes=("_2004", "_2008"),
                        indicator=True)
print(men48_i)  # here in this case we don't loose our indexes for 2008 df
# index labels gets populated in Name column
