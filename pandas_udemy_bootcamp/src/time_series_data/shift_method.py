''' The shift() method
It allows us to calculate the absolute/relative change in
stock prices from yesterday till today or last week till etc '''
from create_dataframe import close


# we are only working with apple stock
# converting pandas series into a dataframe
aapl = close.AAPL.copy().to_frame()
print(aapl.head())

''' To compare the prices we first shift the values (to one day) here
create a new column of these values and then using sub function we
can see the difference in prices of stocks or daily increase or
decrease in stock price and can also store the results '''
print(aapl.shift(periods=1))

aapl["lag1"] = aapl.shift(periods=1)
print(aapl.head())

print(aapl.AAPL.sub(aapl.lag1))

# absolute difference
aapl["Diff"] = aapl.AAPL.sub(aapl.lag1)
print(aapl.head())

# in finance it is more meaningful to have relative difference
# it is also called as return or percentage change
print(aapl.AAPL.div(aapl.lag1).sub(1).mul(100))

aapl["pct_change"] = aapl.AAPL.div(aapl.lag1).sub(1).mul(100)
print(aapl.head())
