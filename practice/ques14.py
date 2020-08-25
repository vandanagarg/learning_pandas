import pandas as pd
import numpy as np


'''
Step 2. Create 3 differents Series, each of length 100, as follows:
The first a random number from 1 to 4
The second a random number from 1 to 3
The third a random number from 10,000 to 30,000 '''

ser1 = pd.Series(np.random.randint(1, high=5, size=100, dtype="l"))
ser2 = pd.Series(np.random.randint(1, high=4, size=100, dtype="l"))
ser3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype="l"))
# print(ser1)
# print(ser2)
# print(ser3)

df = pd.concat([ser1, ser2, ser3], axis=1)

# df.rename(columns={0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'},
#           inplace=True)
df.columns = ["bedrs", "bathrs", "price_sqr_meter"]
print(df)

# Create a one column DataFrame with the values of the 3 Series
# and assign it to 'bigcolumn'
# join concat the values along rows
bigcolumn = pd.concat([ser1, ser2, ser3], axis=0)

# it is still a Series, so we need to transform it to a DataFrame
bigcolumn = bigcolumn.to_frame()
print(type(bigcolumn))
print(bigcolumn)

# Oops, it seems it is going only until index 99. Is it true?
# no the index are kept but the length of the DataFrame is 300
print(len(bigcolumn))

bigcolumn.reset_index(drop=True, inplace=True)
print(bigcolumn)
