''' The PeriodIndex Object '''
import pandas as pd
from create_dataframe import temp_file


temp = pd.read_csv(temp_file, parse_dates=["datetime"], index_col="datetime")
''' Although to have More Descriptive/intuitive labels we can use
periodindex but it has some drawbacks '''
temp.info()  # originally DatetimeIndex

temp_m = temp.resample("M", kind="timestamp").mean()
temp_m.info()  # we still have DatetimeIndex
print(temp_m.index)
# DatetimeIndex can be sliced using loc operator
print(temp_m.loc["2013-01"])
print(temp_m.loc["2013-05": "2013-08"])  # both ends inclusive
print(temp_m.loc["2013"])

# creating a period index
temp_m = temp.resample("M", kind="period").mean()
temp_m.info()  # now we have PeriodIndex
print(temp_m.index)
# PeriodIndex can be sliced using loc operator
print(temp_m.loc["2013-01"])  # earlier o/p as a df now pandas series
print(temp_m.loc["2013-05": "2013-08"])  # both ends inclusive

# here is the limitation we wont get all rows with 2013 year but
# we just get first row i.e. for january
print(temp_m.loc["2013"])

# to change period index to date time index
print(temp_m.to_timestamp(how="start"))
print(temp_m.to_timestamp(how="end"))  # nano sec precision
