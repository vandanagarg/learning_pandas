''' Helpful DatetimeIndex Attributes and Methods
Using some methods we can create customized date time representation
for some manipulations '''
from create_dataframe import stocks, close


print(close.head())
close.info()

print(close.index)

# different attributes
print(close.index.day)  # tells day of the month
print(close.index.month)  # tells month of the year
print(close.index.year)  # tells year
print(close.index.day_name())  # name of the week
print(close.index.month_name())
print(close.index.weekday)
# quater 1st jan-march, 2nd apr-june
print(close.index.quarter)
print(close.index.days_in_month)

# tells the respective number of week of that year
print(close.index.week)
print(close.index.weekofyear)

# tells if a particular day is the month end day
print(close.index.is_month_end)

# creating new columns/features for close df
close["Day"] = stocks.index.day_name()
close["Quarter"] = stocks.index.quarter

print(close.head())
