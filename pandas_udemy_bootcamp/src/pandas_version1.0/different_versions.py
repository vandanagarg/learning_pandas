''' Creating the NEW extension dtypes with convert_dtypes() '''
import pandas as pd
import numpy as np
from create_dataframe import players2


print(pd.__version__)
print(pd.__git_version__)

print(players2)
players2.info()

players3 = players2.convert_dtypes()
print(players3)
players3.info()
''' convert_dtypes() converts string columns to datatype string,
likewise for boolean, Int64 etc. Also it marks NaN missing values as <NA>
Now the new datatypes are more obvious and intuitive and these are
nullable datatypes. Since these are under experiment so we have to
explicitly convert them to use these dtypes '''

# NEW pd.NA value for missing values

print(players2.loc["Cristiano Ronaldo", "Nationality"])
print(np.nan)

print(players3)
print(players3.loc["Cristiano Ronaldo", "Nationality"])
print(type(players3.loc["Cristiano Ronaldo", "Nationality"]))

print(pd.NA)
print(type(pd.NA))

# creating/assigning missing values
players3.iloc[0, 0] = pd.NA
print(players3)

''' pd.NA behaves somewhat same as np.nan except for equality
operators, below are some operations where pd.NA holds logically
correct as compared to np.nan '''
print(pd.NA + 1)
print(np.nan + 1)

print(pd.NA > 1)
print(np.nan > 1)

print(pd.NA & True)
print(pd.NA & False)
print(pd.NA | True)
print(pd.NA | False)

''' gives error: for np.nan`
TypeError: unsupported operand type(s) for &: 'float' and 'bool'
print(np.nan & True)
print(np.nan & False)
print(np.nan | True)
print(np.nan | False)
'''
print(players3.isnull())  # true for missing values
