''' Conditional Transformation
The use case is mostly for numerical columns on the basis
that if it satisfies a condition; assign values A, if the
condition is not met assign value B '''
import pandas as pd
import numpy as np
from feature_creation import titanic


titanic.info()
# check if a passanger has relatives assign "Yes" else "No"
print(titanic.no_relative == 0)  # boolean series

# can be done using numpy where() method
print(np.where(titanic.no_relative == 0, "Yes", "No"))  # numpy array
# pandas series
print(pd.Series(np.where(titanic.no_relative == 0, "Yes", "No")))

# assign pandas series to new column
titanic["alone"] = pd.Series(np.where(titanic.no_relative == 0, "Yes", "No"))
print(titanic.head(10))

# check if the passanger is a child or not
titanic["child"] = pd.Series(np.where(titanic.age < 18, "Yes", "No"))
print(titanic.head(10))
''' So here we typically transformed numerical columns to categorical
columns and with discrete values '''
