''' Creating a customized DateTimeIndex with pd.date_range() '''
import pandas as pd


print(pd.to_datetime(["2015-05-20", "Feb 20 2015"]))
''' till now using to_datetime() method we have made discrete
datetime indexes, but if we need to set indexes for a particular range
let's say if for a month's duration with regular interval(1 day) then we
can use pandas direct method date_range() '''

print(pd.date_range(start="2015-07-01", end="2015-07-31"))
# by default freq="D"

# we need to define at least 2 paramters and freq by default is "D" daily
print(pd.date_range(start="2015-07-01", periods=31, freq="D"))
print(pd.date_range(end="2015-07-01", periods=31, freq="D"))

print(pd.date_range(start="2015-07-01", end="2015-07-31", freq="B"))
# "B" for business days

# hourly frequency
print(pd.date_range(start="2015-07-31", periods=10, freq="H"))

# weekly frequency # by default gives the first sunday of the week
print(pd.date_range(start="2015-07-01", periods=6, freq="W"))
# for any particular week-day
print(pd.date_range(start="2015-07-01", periods=6, freq="W-Wed"))

# monthly frequency by default we get month end dates
print(pd.date_range(start="2015-07-01", periods=6, freq="M"))
# for getting month start day "MS"
print(pd.date_range(start="2015-07-14", periods=6, freq="MS"))

# if we want to have exactly 1 month interval from the start date
print(pd.date_range(start="2015-07-14",
                    periods=6, freq=pd.DateOffset(months=1)))

# Quarterly: "Q" shows last month of the particular quater,
# QS for start month of the particular quater
print(pd.date_range(start="2015-07-14", periods=6, freq="Q"))
print(pd.date_range(start="2015-07-14", periods=6, freq="QS"))
# for defining any arbitrary quater
print(pd.date_range(start="2015-07-14", periods=6, freq="Q-May"))
print(pd.date_range(start="2015-07-14", periods=6, freq="QS-May"))

# Anuall frequency, pass "A" or "Y"
print(pd.date_range(start="2015-07-14", periods=6, freq="Y"))  # end
print(pd.date_range(start="2015-07-14", periods=6, freq="AS"))  # start
# random month but by default last day
print(pd.date_range(start="2015-07-14", periods=6, freq="A-JUN"))
print(pd.date_range(start="2015-07-14", periods=6, freq="AS-JUN"))

# yearly datetime indexes
print(pd.date_range(start="2015-07-14", periods=6,
                    freq=pd.DateOffset(years=1)))

''' Till here we have created all fixed frequencies date time indexes
and pandas provides us various fixed frequencies as D, H, W, M, Y
To create much more combined fixed width frequencies we can combine these '''
# for 2 hours frequency
print(pd.date_range(start="2015-07-14", periods=6, freq="2H"))
# for 2 days frequency
print(pd.date_range(start="2015-07-14", periods=6, freq="2D"))
# for 3 days and 8 hours frequency which is equal to 80H freq
print(pd.date_range(start="2015-07-14", periods=6, freq="3D8H"))
