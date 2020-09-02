''' Normalizing Time Series to a Base Value(100)
To actually compare the stocks if they performed equally well or not
they should start from the same base level 1 in most cases but 100 for
this case as it is most common value here, also
we will do normalization in pandas in vectorized manner '''
import matplotlib.pyplot as plt
from create_dataframe import close


# we want to have a normalized starting stock price i.e 100 for all stocks
# apple's stock start price - 1st row
print(close.iloc[0, 0])
# vectorization as we are dividing pandas series with a scalar value
print(close.AAPL.div(close.iloc[0, 0]).mul(100))

# repeating the same for other columns as well we can divide
# the entire dataframe with 1st row
print(close.iloc[0])
norm = close.div(close.iloc[0]).mul(100)
print(norm)

# a better visualization with base 100
norm.plot(figsize=(15, 8), fontsize=13)
plt.legend(fontsize=13)
plt.show()
